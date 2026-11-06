import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "update_dataset_stats", Path(__file__).parent.parent / "update_dataset_stats.py"
)
uds = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(uds)

FMRI = {"sub-01": {"total_runs": 2, "total_duration_h": 10.0},
        "sub-02": {"total_runs": 2, "total_duration_h": 20.0}}
SESS = {"sub-01": 1, "sub-02": 1}


def run(tmp_path, text, has_fmri=True):
    p = tmp_path / "dataset_info.yaml"
    p.write_text(text)
    changes = uds.update_or_create(p, "x", FMRI if has_fmri else {}, SESS, has_fmri)
    return p, changes


BASE = "stats:\n  subjects_n: 2\n  neuroimaging:\n    fmri: {total_h: 30.0, per_subject_h: 15.0}\n  tasks:\n"
SUBJ = "subjects:\n- {id: sub-01, status: available}\n- {id: sub-02, status: available}\n" \
       "- {id: sub-03, status: not_collected}\n- {id: sub-04, status: not_collected}\n" \
       "- {id: sub-05, status: not_collected}\n- {id: sub-06, status: not_collected}\n"


def load(p):
    from ruamel.yaml import YAML
    return YAML().load(p.read_text())["stats"]["tasks"]


def test_whole_block_stimulus(tmp_path):
    t = BASE + ("    video:\n      source: $FMRI\n      total_unique: 1\n      per_subject_unique: 1\n"
                "      total_with_repetition: 1\n      per_subject_with_repetition: 1\n") + SUBJ
    p, _ = run(tmp_path, t)
    v = load(p)["video"]
    assert v["source"] == "$FMRI"
    assert (v["total_unique"], v["per_subject_unique"]) == (30.0, 15.0)
    assert (v["total_with_repetition"], v["per_subject_with_repetition"]) == (30.0, 15.0)


def test_whole_block_game(tmp_path):
    p, _ = run(tmp_path, BASE + "    game:\n      source: $FMRI\n      total_h: 1\n      per_subject_h: 1\n" + SUBJ)
    g = load(p)["game"]
    assert (g["total_h"], g["per_subject_h"]) == (30.0, 15.0)


def test_source_fields_subset(tmp_path):
    t = BASE + ("    audio:\n      source: $FMRI\n      source_fields: [total_with_repetition, per_subject_with_repetition]\n"
                "      total_unique: 1\n      per_subject_unique: 2\n"
                "      total_with_repetition: 1\n      per_subject_with_repetition: 1\n") + SUBJ
    p, _ = run(tmp_path, t)
    a = load(p)["audio"]
    assert (a["total_unique"], a["per_subject_unique"]) == (1, 2)
    assert (a["total_with_repetition"], a["per_subject_with_repetition"]) == (30.0, 15.0)


def test_no_fmri_warns_and_leaves_block(tmp_path, capsys):
    t = "stats:\n  subjects_n: 0\n  tasks:\n    game:\n      source: $FMRI\n      total_h: 1\n      per_subject_h: 1\n" + SUBJ
    p, _ = run(tmp_path, t, has_fmri=False)
    assert "WARNING" in capsys.readouterr().err
    assert load(p)["game"]["total_h"] == 1


def test_unknown_source_raises(tmp_path):
    t = BASE + "    game:\n      source: $OTHER\n      total_h: 1\n      per_subject_h: 1\n" + SUBJ
    with pytest.raises(ValueError):
        run(tmp_path, t)


def test_bad_source_field_raises(tmp_path):
    t = BASE + "    game:\n      source: $FMRI\n      source_fields: [bogus]\n      total_h: 1\n      per_subject_h: 1\n" + SUBJ
    with pytest.raises(ValueError):
        run(tmp_path, t)


def test_no_marker_unchanged(tmp_path):
    t = BASE.replace("30.0", "30.0") + "    game:\n      total_h: 1\n      per_subject_h: 1\n" + SUBJ
    p, _ = run(tmp_path, t)
    first = p.read_text()
    run(tmp_path, first)
    assert p.read_text() == first
    assert load(p)["game"]["total_h"] == 1
