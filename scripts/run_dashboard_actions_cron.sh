#!/usr/bin/env bash
# Cron entrypoint: consume dashboard button/action requests only.
set -u -o pipefail
umask 077

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STATE_DIR="${INFINITY_DASHBOARD_ACTION_STATE_DIR:-/home/ubuntu/.openclaw/state/infinity-dispatcher-runs}"
LOCK_FILE="${INFINITY_DASHBOARD_ACTION_LOCK_FILE:-$STATE_DIR/dashboard-actions.lock}"
RUN_FILE="$STATE_DIR/dashboard-actions-$(date -u +%Y%m%dT%H%M%SZ)-$$.json"
fail() {
  printf 'dashboard action cron: %s\n' "$1" >&2
  exit 1
}

mkdir -p "$STATE_DIR" || fail "cannot create state directory: $STATE_DIR"
exec 9>"$LOCK_FILE"
flock -n 9 || exit 0

git -C "$ROOT" fetch --prune origin main >/dev/null 2>&1 || fail "git fetch origin main failed"
ORIGIN_SHA="$(git -C "$ROOT" rev-parse refs/remotes/origin/main 2>/dev/null)" || fail "cannot resolve origin/main"
git -C "$ROOT" pull --ff-only origin main >/dev/null 2>&1 || fail "git pull --ff-only origin main failed"
CURRENT_SHA="$(git -C "$ROOT" rev-parse HEAD 2>/dev/null)" || fail "cannot resolve checkout HEAD"
[[ "$CURRENT_SHA" == "$ORIGIN_SHA" ]] || fail "checkout HEAD does not match fetched origin/main"

RESULT="$(python3 "$ROOT/scripts/process_action_requests.py" --apply --limit 10 --json 2>&1)"
EXIT_CODE=$?

if [[ "$EXIT_CODE" -eq 0 ]] && ! git -C "$ROOT" diff --quiet -- INTENTS.yaml artifacts/dashboard-actions intents/archive; then
  git -C "$ROOT" add INTENTS.yaml artifacts/dashboard-actions intents/archive
  git -C "$ROOT" commit --only -m "chore(infinity): persist dashboard action transition" -- INTENTS.yaml artifacts/dashboard-actions intents/archive >/dev/null 2>&1 || fail "could not commit dashboard action transition"
  git -C "$ROOT" push origin HEAD:main >/dev/null 2>&1 || fail "could not push dashboard action transition"
  PUSHED_SHA="$(git -C "$ROOT" rev-parse HEAD 2>/dev/null)" || fail "cannot resolve pushed HEAD"
  REMOTE_SHA="$(git -C "$ROOT" ls-remote origin refs/heads/main | awk '{print $1}')" || fail "cannot verify remote main"
  [[ -n "$REMOTE_SHA" && "$PUSHED_SHA" == "$REMOTE_SHA" ]] || fail "pushed commit does not match remote main"
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
if [[ "$EXIT_CODE" -ne 0 ]]; then
  printf '%s\n' "$RESULT" >&2
fi
exit "$EXIT_CODE"
