#!/usr/bin/env bash
set -euo pipefail

# --no-figures: skip run-notebooks (no figures, no fmri_stats.json extras beyond
# the TSVs) — just the three TSV-producing tasks. Used by CI's per-PR job, which
# only needs dataset_info.yaml numbers refreshed and must stay fast; also usable
# locally to check for drift without paying for the notebook run.
NO_FIGURES=0
for arg in "$@"; do
  case "$arg" in
    --no-figures) NO_FIGURES=1 ;;
    *) echo "Unknown argument: $arg" >&2; exit 1 ;;
  esac
done

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATS_DIR="$REPO_ROOT/analysis/cneuromod.all.statistics"

cd "$STATS_DIR"

# Point source_data/cneuromod.all at this checkout instead of cloning a second
# copy — this is what keeps cneuromod.all from being a submodule of itself.
# fetch-cneuromod only creates the symlink; we deliberately do NOT run
# `invoke fetch` / `fetch-bids`, which would `datalad update --merge` every
# */bids subdataset in this very working tree and could advance its pointers.
uv run invoke fetch-cneuromod --source "$REPO_ROOT"

if [ "$NO_FIGURES" -eq 1 ]; then
  uv run invoke clean-statistics clean-fmri-stats clean-fmri-per-subject-stats
  uv run invoke run-statistics run-fmri-stats run-fmri-per-subject-stats
else
  uv run invoke run --force
fi
