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
CUTOVER="$STATE_DIR/ubuntu-consumer-stopped.confirmed"
EXPECTED_RECEIPT_SHA="a33b0be96db917069d3b66761ab7dc8aa92aacb3a06e6e1a64d761028c724666"
READY=false
REASON=ubuntu_consumer_stop_unconfirmed
if [[ -f "$CUTOVER" ]] && [[ "$(cat "$CUTOVER")" == 'confirmed-ubuntu-consumer-stopped' ]]; then
  REASON=receipt_not_handed_over
  if [[ -f "$RECEIPT" ]] && [[ "$(sha256sum "$RECEIPT" | cut -d' ' -f1)" == "$EXPECTED_RECEIPT_SHA" ]]; then
    REASON=hermes_runtime_not_implemented
    if [[ "$ROLE" == consumer ]]; then
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
# Only the dashboard consumer has an implemented WSL runtime path. Other roles
# are held until their OpenClaw handoff/delivery is replaced and tested.
[[ "$ROLE" == consumer ]] || exit 75
[[ "$(git -C "$ROOT" symbolic-ref --quiet --short HEAD)" == main ]] || exit 75
export INFINITY_DASHBOARD_ACTION_STATE_DIR="$STATE_DIR"
export PYTHONPATH="${INFINITY_PYDEPS:-$HOME/.local/share/infinity-pydeps}${PYTHONPATH:+:$PYTHONPATH}"
export PATH="/usr/bin:$PATH"
exec timeout --signal=TERM --kill-after=5s 180s bash "$ROOT/scripts/run_dashboard_actions_cron.sh"
