#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATS_DIR="$REPO_ROOT/analysis/cneuromod.all.statistics"

cd "$STATS_DIR"

# Point source_data/cneuromod.all at this checkout instead of cloning a second
# copy — this is what keeps cneuromod.all from being a submodule of itself.
# fetch-cneuromod only creates the symlink; we deliberately do NOT run
# `invoke fetch` / `fetch-bids`, which would `datalad update --merge` every
# */bids subdataset in this very working tree and could advance its pointers.
uv run invoke fetch-cneuromod --source "$REPO_ROOT"

uv run invoke run --force
