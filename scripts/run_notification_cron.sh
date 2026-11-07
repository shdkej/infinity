#!/usr/bin/env bash
# Cron entrypoint: reconcile and deliver Infinity notifications only.
set -u -o pipefail
umask 077

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STATE_FILE="${INFINITY_TERMINAL_STATE_FILE:-$ROOT/data/dispatcher-terminal-notifications.json}"
STATE_DIR="${INFINITY_NOTIFICATION_STATE_DIR:-/home/ubuntu/.openclaw/state/infinity-dispatcher-runs}"
LOCK_FILE="${INFINITY_NOTIFICATION_LOCK_FILE:-$STATE_DIR/notifications.lock}"
CARD_DIR="${INFINITY_NOTIFICATION_CARD_DIR:-$STATE_DIR/cards}"
NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
if [[ ! -s "$NVM_DIR/nvm.sh" ]]; then
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"setup","failure_class":"nvm_unavailable","outcome":"error"}' >&2
  exit 1
fi
if ! . "$NVM_DIR/nvm.sh" 2>/dev/null; then
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"setup","failure_class":"nvm_init_failed","outcome":"error"}' >&2
  exit 1
fi
if ! nvm use --silent default >/dev/null 2>&1; then
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"setup","failure_class":"nvm_use_failed","outcome":"error"}' >&2
  exit 1
fi
OPENCLAW_BIN="${OPENCLAW_BIN:-${NVM_BIN:-}/openclaw}"
if [[ ! -x "$OPENCLAW_BIN" ]]; then
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"setup","failure_class":"openclaw_cli_unavailable","outcome":"error"}' >&2
  exit 1
fi
if ! command -v timeout >/dev/null 2>&1; then
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"setup","failure_class":"timeout_utility_unavailable","outcome":"error"}' >&2
  exit 1
fi
if ! mkdir -p "$STATE_DIR" "$CARD_DIR" 2>/dev/null; then
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"setup","failure_class":"state_directory_unavailable","outcome":"error"}' >&2
  exit 1
fi
exec 9>"$LOCK_FILE" 2>/dev/null || {
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"lock","failure_class":"lock_file_unavailable","outcome":"error"}' >&2
  exit 1
}
if flock -n 9; then
  :
else
  flock_status=$?
  if [[ $flock_status -eq 1 ]]; then
    printf '%s\n' '{"event":"infinity_notification_skip","phase":"lock","reason":"already_running"}' >&2
    exit 0
  fi
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"lock","failure_class":"lock_failed","outcome":"error"}' >&2
  exit "$flock_status"
fi

timeout --signal=TERM --kill-after=5s 120s python3 "$ROOT/scripts/dispatch_terminal_notifications.py" \
  --repo "$ROOT" --state "$STATE_FILE" --deliver --openclaw-bin "$OPENCLAW_BIN" \
  --send-timeout-seconds 20 --git-timeout-seconds 10 --run-timeout-seconds 110 \
  --card-dir "$CARD_DIR"
run_status=$?
if [[ $run_status -eq 124 || $run_status -eq 137 ]]; then
  printf '{"event":"infinity_notification_failure","phase":"run","failure_class":"outer_timeout","outcome":"ambiguous","exit_status":%d}\n' "$run_status" >&2
elif [[ $run_status -eq 125 ]]; then
  printf '%s\n' '{"event":"infinity_notification_failure","phase":"run","failure_class":"timeout_utility_failed","outcome":"error","exit_status":125}' >&2
fi
exit "$run_status"
