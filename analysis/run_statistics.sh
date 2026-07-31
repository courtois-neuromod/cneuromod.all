#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATS_DIR="$(dirname "${BASH_SOURCE[0]}")/cneuromod.all.statistics"

export INVOKE_CNEUROMOD_ALL_DIR="$REPO_ROOT"

cd "$STATS_DIR"
uv run invoke -e clean
uv run invoke -e run
