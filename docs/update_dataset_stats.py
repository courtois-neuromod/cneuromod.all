#!/usr/bin/env python3
"""Update or create dataset_info.yaml files from cneuromod.all.statistics output.

Drives entirely from the statistics pipeline output — every dataset present
in fmri_stats_per_subject.tsv or session_counts.tsv (with any sessions) is
processed. For each:
  - If dataset_info.yaml exists: update subjects_n, subjects[*].status, and
    neuroimaging.fmri hours (when fMRI stats are available).
  - If dataset_info.yaml is absent: create a minimal skeleton.

Statuses partial / pending / collected_not_released are never overwritten.
Fields not derived from the pipeline (tasks, physiology, modalities, etc.)
are left untouched.

Run from the repo root:
  python docs/update_dataset_stats.py
"""

import argparse
import csv
import sys
from pathlib import Path

from ruamel.yaml import YAML

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_STATS_DIR = (
    REPO_ROOT / "analysis" / "cneuromod.all.statistics" / "output_data"
)

# Stats dataset name → folder name (only non-trivial overrides needed)
STATS_TO_FOLDER = {
    "mario3": "mario",
}

PRESERVE_STATUSES = {"partial", "pending", "collected_not_released"}

ALL_SUBJECTS = ["sub-01", "sub-02", "sub-03", "sub-04", "sub-05", "sub-06"]


def load_tsv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def build_fmri_index(rows):
    """Return {stat_name: {subject: {total_runs, total_duration_h}}}."""
    index = {}
    for row in rows:
        ds = row["dataset"]
        if ds == "all":
            continue
        subj = row["subject"]
        runs = int(row["total_runs"]) if row["total_runs"] else 0
        duration = float(row["total_duration_h"]) if row["total_duration_h"] else 0.0
        index.setdefault(ds, {})[subj] = {"total_runs": runs, "total_duration_h": duration}
    return index


def build_session_index(rows):
    """Return {stat_name: {subject: n_sessions}}."""
    index = {}
    for row in rows:
        index.setdefault(row["dataset"], {})[row["subject"]] = int(row["n_sessions"])
    return index


def skeleton_yaml(stat_name, subjects_n, subj_sessions, has_fmri):
    """Return a minimal dataset_info.yaml dict for a new file."""
    data = {
        "stats": {
            "subjects_n": subjects_n,
        },
        "subjects": [
            {"id": s, "status": "available" if subj_sessions.get(s, 0) > 0 else "not_collected"}
            for s in ALL_SUBJECTS
        ],
    }
    if has_fmri:
        data["stats"]["neuroimaging"] = {"fmri": {"total_h": None, "per_subject_h": None}}
    return data


def update_or_create(yaml_path, stat_name, subj_fmri, subj_sessions, has_fmri):
    yaml = YAML()
    yaml.preserve_quotes = True

    active_ids = (
        {s for s, v in subj_fmri.items() if v["total_runs"] > 0}
        if has_fmri
        else {s for s, n in subj_sessions.items() if n > 0}
    )
    subjects_n = len(active_ids)

    if has_fmri and subjects_n:
        total_h = round(sum(subj_fmri[s]["total_duration_h"] for s in active_ids), 1)
        per_subject_h = round(total_h / subjects_n, 1)
    else:
        total_h = per_subject_h = None

    # --- Create skeleton if file absent ---
    if not yaml_path.exists():
        data = skeleton_yaml(stat_name, subjects_n, subj_sessions, has_fmri)
        if has_fmri and total_h is not None:
            data["stats"]["neuroimaging"]["fmri"]["total_h"] = total_h
            data["stats"]["neuroimaging"]["fmri"]["per_subject_h"] = per_subject_h
        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        with open(yaml_path, "w") as f:
            yaml.dump(data, f)
        return ["  (created skeleton)"]

    # --- Update existing file ---
    with open(yaml_path) as f:
        data = yaml.load(f)

    changes = []

    old_n = data.get("stats", {}).get("subjects_n")
    if old_n != subjects_n:
        changes.append(f"  subjects_n: {old_n} → {subjects_n}")
    data["stats"]["subjects_n"] = subjects_n

    if has_fmri and total_h is not None:
        fmri = data.get("stats", {}).get("neuroimaging", {}).get("fmri", {})
        if fmri.get("total_h") != total_h:
            changes.append(f"  neuroimaging.fmri.total_h: {fmri.get('total_h')} → {total_h}")
        if fmri.get("per_subject_h") != per_subject_h:
            changes.append(f"  neuroimaging.fmri.per_subject_h: {fmri.get('per_subject_h')} → {per_subject_h}")
        data["stats"]["neuroimaging"]["fmri"]["total_h"] = total_h
        data["stats"]["neuroimaging"]["fmri"]["per_subject_h"] = per_subject_h

    for entry in data.get("subjects", []):
        subj_id = entry["id"]
        if entry.get("status") in PRESERVE_STATUSES:
            continue
        new_status = "available" if subj_id in active_ids else "not_collected"
        if entry.get("status") != new_status:
            changes.append(f"  subjects[{subj_id}].status: {entry.get('status')} → {new_status}")
            entry["status"] = new_status

    with open(yaml_path, "w") as f:
        yaml.dump(data, f)

    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stats-dir",
        type=Path,
        default=DEFAULT_STATS_DIR,
        help="Path to cneuromod.all.statistics output_data directory",
    )
    args = parser.parse_args()

    stats_dir = args.stats_dir
    per_subject_path = stats_dir / "fmri_stats_per_subject.tsv"
    sessions_path = stats_dir / "session_counts.tsv"

    for p in (per_subject_path, sessions_path):
        if not p.exists():
            print(f"ERROR: missing file: {p}", file=sys.stderr)
            sys.exit(1)

    fmri_index = build_fmri_index(load_tsv(per_subject_path))
    session_index = build_session_index(load_tsv(sessions_path))

    # All datasets with any data in either source
    all_stat_names = set(fmri_index) | {
        ds for ds, counts in session_index.items() if any(n > 0 for n in counts.values())
    }

    any_changes = False
    for stat_name in sorted(all_stat_names):
        folder = STATS_TO_FOLDER.get(stat_name, stat_name)
        folder_path = REPO_ROOT / folder
        yaml_path = folder_path / "dataset_info.yaml"

        has_fmri = stat_name in fmri_index
        subj_fmri = fmri_index.get(stat_name, {})
        subj_sessions = session_index.get(stat_name, {})

        suffix = "" if has_fmri else " (session counts only — fMRI hours not updated)"
        changes = update_or_create(yaml_path, stat_name, subj_fmri, subj_sessions, has_fmri)

        if changes:
            created = changes == ["  (created skeleton)"]
            verb = "Created" if created else "Updated"
            print(f"{verb} {folder}/dataset_info.yaml{'' if created else suffix}:")
            for c in changes:
                print(c)
            any_changes = True
        else:
            print(f"No changes: {folder}/dataset_info.yaml")

    if not any_changes:
        print("All files already up to date.")


if __name__ == "__main__":
    main()
