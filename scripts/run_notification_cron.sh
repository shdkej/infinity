#!/usr/bin/env bash
# Cron entrypoint: reconcile and deliver Infinity notifications only.
set -u -o pipefail
umask 077

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STATE_FILE="${INFINITY_TERMINAL_STATE_FILE:-$ROOT/data/dispatcher-terminal-notifications.json}"
STATE_DIR="${INFINITY_NOTIFICATION_STATE_DIR:-/home/ubuntu/.openclaw/state/infinity-dispatcher-runs}"
LOCK_FILE="${INFINITY_NOTIFICATION_LOCK_FILE:-$STATE_DIR/notifications.lock}"
CARD_DIR="${INFINITY_NOTIFICATION_CARD_DIR:-$STATE_DIR/cards}"
OPENCLAW_BIN="${OPENCLAW_BIN:-/home/ubuntu/.npm-global/bin/openclaw}"
mkdir -p "$STATE_DIR" "$CARD_DIR" || exit 0
exec 9>"$LOCK_FILE"
flock -n 9 || exit 0

CHANNEL="${INFINITY_CHANGE_NOTIFICATION_CHANNEL:-telegram}"
TARGET="${INFINITY_CHANGE_NOTIFICATION_TARGET:-telegram:433493318}"
TERMINAL_CHANNEL="${INFINITY_TERMINAL_NOTIFICATION_CHANNEL:-$CHANNEL}"
TERMINAL_TARGET="${INFINITY_TERMINAL_NOTIFICATION_TARGET:-$TARGET}"

python3 "$ROOT/scripts/dispatch_terminal_notifications.py" \
  --repo "$ROOT" --state "$STATE_FILE" --deliver --openclaw-bin "$OPENCLAW_BIN" \
  --change-channel "$CHANNEL" --change-target "$TARGET" \
  --terminal-channel "$TERMINAL_CHANNEL" --terminal-target "$TERMINAL_TARGET" \
  --card-dir "$CARD_DIR"
exit $?
