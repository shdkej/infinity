#!/usr/bin/env bash
set -euo pipefail
umask 077

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RUN_ROOT="$ROOT/.watcher-runs"
STATE_DIR="/home/ubuntu/.openclaw/state"
LOCK_FILE="$STATE_DIR/role-watchers.lock"
LOG_DIR="/home/ubuntu/.openclaw/logs"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
WORKTREE="$RUN_ROOT/$STAMP"
mkdir -p "$RUN_ROOT" "$STATE_DIR" "$LOG_DIR"
exec 9>"$LOCK_FILE"
flock -n 9 || exit 0

cleanup() { git -C "$ROOT" worktree remove --force "$WORKTREE" >/dev/null 2>&1 || true; }
trap cleanup EXIT

git -C "$ROOT" fetch origin main --quiet
git -C "$ROOT" worktree add --detach "$WORKTREE" origin/main >/dev/null
cd "$WORKTREE"
python3 scripts/role_watchers.py --apply >"$LOG_DIR/role-watchers-$STAMP.json"
python3 scripts/dedupe_role_backlog.py --apply >"$LOG_DIR/role-backlog-dedupe-$STAMP.yaml"

if ! git diff --quiet -- INTENTS.yaml data/role-watcher-state.json; then
  git add INTENTS.yaml data/role-watcher-state.json
  git commit -m "chore(infinity): collect role watcher candidates" >/dev/null
  git push origin HEAD:main >/dev/null
  local_sha="$(git rev-parse HEAD)"
  remote_sha="$(git ls-remote origin refs/heads/main | awk '{print $1}')"
  [[ "$local_sha" == "$remote_sha" ]]
fi

# Genie performs semantic grouping/rejection after deterministic collection.
OPENCLAW_BIN="/home/ubuntu/.npm-global/bin/openclaw"
if [[ -x "$OPENCLAW_BIN" ]]; then
  "$OPENCLAW_BIN" agent --agent genie --session-key agent:genie:role-watcher-backlog-manager \
    --message-file "$WORKTREE/docs/ROLE_WATCHER_BACKLOG_MANAGER.md" --thinking low --timeout 480 --json \
    >>"$LOG_DIR/role-backlog-manager-$STAMP.json" 2>&1 || true
fi
