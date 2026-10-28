#!/usr/bin/env bash
# Cron entrypoint: consume dashboard button/action requests only.
set -u -o pipefail
umask 077

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STATE_DIR="${INFINITY_DASHBOARD_ACTION_STATE_DIR:-/home/ubuntu/.openclaw/state/infinity-dispatcher-runs}"
LOCK_FILE="${INFINITY_DASHBOARD_ACTION_LOCK_FILE:-$STATE_DIR/dashboard-actions.lock}"
RUN_FILE="$STATE_DIR/dashboard-actions-$(date -u +%Y%m%dT%H%M%SZ)-$$.json"
mkdir -p "$STATE_DIR" || exit 0
exec 9>"$LOCK_FILE"
flock -n 9 || exit 0

git -C "$ROOT" fetch --prune origin main >/dev/null 2>&1 || exit 0
ORIGIN_SHA="$(git -C "$ROOT" rev-parse refs/remotes/origin/main 2>/dev/null)" || exit 0
git -C "$ROOT" pull --ff-only origin main >/dev/null 2>&1 || exit 0
CURRENT_SHA="$(git -C "$ROOT" rev-parse HEAD 2>/dev/null)" || exit 0
[[ "$CURRENT_SHA" == "$ORIGIN_SHA" ]] || exit 0

RESULT="$(python3 "$ROOT/scripts/process_action_requests.py" --apply --limit 10 --json 2>&1)"
EXIT_CODE=$?

if [[ "$EXIT_CODE" -eq 0 ]] && ! git -C "$ROOT" diff --quiet -- INTENTS.yaml artifacts/dashboard-actions intents/archive; then
  git -C "$ROOT" add INTENTS.yaml artifacts/dashboard-actions intents/archive
  git -C "$ROOT" commit -m "chore(infinity): persist dashboard action transition" >/dev/null 2>&1 || exit 0
  git -C "$ROOT" push origin HEAD:main >/dev/null 2>&1 || exit 0
  PUSHED_SHA="$(git -C "$ROOT" rev-parse HEAD 2>/dev/null)" || exit 0
  REMOTE_SHA="$(git -C "$ROOT" ls-remote origin refs/heads/main | awk '{print $1}')" || exit 0
  [[ -n "$REMOTE_SHA" && "$PUSHED_SHA" == "$REMOTE_SHA" ]] || exit 0
else
  PUSHED_SHA=""
  REMOTE_SHA="$ORIGIN_SHA"
fi

python3 - "$RUN_FILE" "$ORIGIN_SHA" "$PUSHED_SHA" "$REMOTE_SHA" "$EXIT_CODE" "$RESULT" <<'PY'
import json, sys
from pathlib import Path
Path(sys.argv[1]).write_text(json.dumps({
    "component": "dashboard_actions",
    "origin_sha": sys.argv[2],
    "pushed_sha": sys.argv[3],
    "remote_sha": sys.argv[4],
    "exit_code": int(sys.argv[5]),
    "result": sys.argv[6],
}, ensure_ascii=False, indent=2) + "\n")
PY
exit 0
