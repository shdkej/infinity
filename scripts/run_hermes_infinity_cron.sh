#!/usr/bin/env bash
# Hermes cron entrypoint: deliberately fail closed until the Ubuntu cutover is verified.
# --check is local/read-only and never touches Git, S3, the action queue, or messaging.
set -euo pipefail

ROLE="${1:-}"
MODE="${2:-run}"
case "$ROLE" in dispatcher|consumer|notifier) ;; *) printf 'unknown Infinity role\n' >&2; exit 64 ;; esac
case "$MODE" in run|--check) ;; *) printf 'unknown mode\n' >&2; exit 64 ;; esac
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STATE_DIR="${INFINITY_HERMES_STATE_DIR:-${HERMES_HOME:-$HOME/.hermes}/state/infinity}"
RECEIPT="$STATE_DIR/dispatcher-terminal-notifications.json"
BOOTSTRAP="$STATE_DIR/receipt-bootstrap.sha256"
BASELINE="$STATE_DIR/notification-ledger-intake-baseline.json"
CUTOVER="$STATE_DIR/ubuntu-consumer-stopped.confirmed"
EXPECTED_RECEIPT_SHA="a33b0be96db917069d3b66761ab7dc8aa92aacb3a06e6e1a64d761028c724666"
READY=false
REASON=ubuntu_consumer_stop_unconfirmed
if [[ -f "$CUTOVER" ]] && [[ "$(cat "$CUTOVER")" == 'confirmed-ubuntu-consumer-stopped' ]]; then
  REASON=receipt_not_handed_over
  # The frozen intake copy retains the original SHA. The mutable runtime
  # ledger may grow, but every intake delivery must remain represented so a
  # replaced/empty ledger cannot replay already-sent or uncertain messages.
  if [[ -f "$RECEIPT" && -f "$BOOTSTRAP" && -f "$BASELINE" ]] &&
     [[ "$(cat "$BOOTSTRAP")" == "$EXPECTED_RECEIPT_SHA" ]] &&
     python3 "$ROOT/scripts/verify_hermes_receipt.py" "$BASELINE" "$RECEIPT" "$EXPECTED_RECEIPT_SHA" >/dev/null 2>&1; then
    REASON=hermes_runtime_not_implemented
    if [[ "$ROLE" == consumer || "$ROLE" == dispatcher ]]; then
      REASON=ok
      READY=true
    fi
  fi
fi
if [[ "$MODE" == --check ]]; then
  printf '{"role":"%s","ready":%s,"reason":"%s"}\n' "$ROLE" "$READY" "$REASON"
  exit 0
fi
if [[ "$READY" != true ]]; then
  printf 'Infinity %s blocked: %s\n' "$ROLE" "$REASON" >&2
  exit 75
fi
# A second role must not mutate the same canonical checkout while this role
# fetches, records a trace, commits, or proves the remote revision.
exec 8>"$STATE_DIR/canonical-git.lock"
flock -n 8 || exit 0
[[ "$(git -C "$ROOT" symbolic-ref --quiet --short HEAD)" == main ]] || exit 75
export PYTHONPATH="${INFINITY_PYDEPS:-$HOME/.local/share/infinity-pydeps}${PYTHONPATH:+:$PYTHONPATH}"
export PATH="/usr/bin:$PATH"
if [[ "$ROLE" == dispatcher ]]; then
  export INFINITY_EXECUTOR=hermes
  export INFINITY_DISPATCHER_STATE_DIR="$STATE_DIR"
  export INFINITY_DISPATCHER_LOCK_FILE="$STATE_DIR/dispatcher.lock"
  exec timeout --signal=TERM --kill-after=5s 600s bash "$ROOT/scripts/run_registered_dispatcher_cycle.sh"
fi
[[ "$ROLE" == consumer ]] || exit 75
export INFINITY_DASHBOARD_ACTION_STATE_DIR="$STATE_DIR"
exec timeout --signal=TERM --kill-after=5s 180s bash "$ROOT/scripts/run_dashboard_actions_cron.sh"
