#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RUN_ROOT="$ROOT/.watcher-runs"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
WORKTREE="$RUN_ROOT/$STAMP"
mkdir -p "$RUN_ROOT"
cleanup() {
  git -C "$ROOT" worktree remove --force "$WORKTREE" >/dev/null 2>&1 || true
}
trap cleanup EXIT

git -C "$ROOT" fetch origin main --quiet
git -C "$ROOT" worktree add --detach "$WORKTREE" origin/main >/dev/null
cd "$WORKTREE"
python3 scripts/backlog_watcher.py --apply
if git diff --quiet -- INTENTS.yaml; then
  exit 0
fi
git add INTENTS.yaml
git commit -m "chore: add monitored candidates to backlog"
git push origin HEAD:main
