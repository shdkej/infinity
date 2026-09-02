#!/usr/bin/env bash
# The only Infinity dispatcher schedule is the host's existing 10-minute cron.
set -u -o pipefail

ROOT="/home/ubuntu/workspace/knowledge-lab/infinity"
OPENCLAW_BIN="/home/ubuntu/.npm-global/bin/openclaw"
STATE_DIR="${INFINITY_DISPATCHER_STATE_DIR:-/home/ubuntu/.openclaw/state/infinity-dispatcher-runs}"
LOCK_FILE="${INFINITY_DISPATCHER_LOCK_FILE:-/tmp/infinity-dispatcher.lock}"
AGENT_TIMEOUT_SECONDS="${INFINITY_DISPATCHER_AGENT_TIMEOUT_SECONDS:-480}"
mkdir -p "$STATE_DIR"
exec 9>"$LOCK_FILE"
flock -n 9 || exit 0

RUN_FILE="$STATE_DIR/$(date -u +%Y%m%dT%H%M%SZ)-$$.json"
PLAN_FILE="$(mktemp)"
PROMPT_FILE="$(mktemp)"
trap 'rm -f "$PLAN_FILE" "$PROMPT_FILE"' EXIT

if ! python3 "$ROOT/scripts/prepare_dispatch_cycle.py" --repo "$ROOT" --json >"$PLAN_FILE"; then
  python3 - "$RUN_FILE" "$PLAN_FILE" <<'PY'
import json, sys
from pathlib import Path
Path(sys.argv[1]).write_text(json.dumps({"outcome": "canonical_fetch_failed", "detail": json.loads(Path(sys.argv[2]).read_text())}, ensure_ascii=False, indent=2) + "\n")
PY
  exit 1
fi

TERMINAL_EXIT=0
DASHBOARD_EXIT=0
TERMINAL_RESULT="$(python3 "$ROOT/scripts/dispatch_terminal_notifications.py" --repo "$ROOT" --state "$ROOT/data/dispatcher-terminal-notifications.json" --deliver --openclaw-bin "$OPENCLAW_BIN" 2>&1)" || TERMINAL_EXIT=$?
DASHBOARD_RESULT="$(python3 "$ROOT/scripts/process_action_requests.py" --apply --limit 10 --json 2>&1)" || DASHBOARD_EXIT=$?
[[ "$TERMINAL_EXIT" -ne 0 ]] && TERMINAL_RESULT="terminal_error(exit=${TERMINAL_EXIT}):${TERMINAL_RESULT}"
[[ "$DASHBOARD_EXIT" -ne 0 ]] && DASHBOARD_RESULT="dashboard_error(exit=${DASHBOARD_EXIT}):${DASHBOARD_RESULT}"
HANDOFF_EXIT=0
HANDOFF_STATE="not_needed"

if python3 - "$PLAN_FILE" <<'PY'
import json, sys
plan = json.load(open(sys.argv[1]))
raise SystemExit(0 if plan["dispatch_required"] else 1)
PY
then
  python3 - "$PLAN_FILE" "$PROMPT_FILE" <<'PY'
import json, sys
plan = json.load(open(sys.argv[1]))
message = f'''You are the direct Genie executor for the single existing Infinity dispatcher.
Canonical revision: {plan["canonical_sha"]}
Dispatcher run: {plan["run_id"]}
Plan: {json.dumps(plan, ensure_ascii=False)}

Do not create schedules. Do not use dashboard_actions as work status. Fetch Infinity origin/main first; if its revision changed, make no mutation and return that reason. For every promotion candidate, move only that canonical Inbox block to Active, never exceeding three Active intents. For each handoff/resume candidate, execute or resume it yourself; do not return it to the main agent. Inspect follow_up_candidates explicitly: create only safe, non-duplicate Inbox follow-ups with the original notification metadata; leave approval-boundary follow-ups Waiting with their exact blocker.

Before substantive work, append a dispatcher_handoff event to traces/<intent-id>.json with run_id, canonical_sha, agent=genie, session_key=agent:genie:infinity-dispatcher, timestamp, and status=accepted. Commit and push only explicit Infinity files, fetch, and prove HEAD == origin/main. Preserve approval boundaries. If starting is unsafe, record a precise Waiting or stale_guard_released reason; never claim completion.

Return JSON containing intent IDs, session evidence, state changes, commit, and remote proof.'''
open(sys.argv[2], "w", encoding="utf-8").write(message)
PY
  timeout --foreground "${AGENT_TIMEOUT_SECONDS}s" "$OPENCLAW_BIN" agent --agent genie --session-key agent:genie:infinity-dispatcher --message-file "$PROMPT_FILE" --thinking low --timeout "$AGENT_TIMEOUT_SECONDS" --json >"$STATE_DIR/$(basename "$RUN_FILE" .json)-genie.json" 2>&1
  HANDOFF_EXIT=$?
  HANDOFF_STATE="returned"
  [[ "$HANDOFF_EXIT" -eq 124 ]] && HANDOFF_STATE="timeout"
else
  HANDOFF_STATE="not_needed"
fi

python3 - "$RUN_FILE" "$PLAN_FILE" "$TERMINAL_RESULT" "$DASHBOARD_RESULT" "$HANDOFF_EXIT" "$HANDOFF_STATE" "$TERMINAL_EXIT" "$DASHBOARD_EXIT" <<'PY'
import json, sys
from pathlib import Path
Path(sys.argv[1]).write_text(json.dumps({
  "outcome": "attention" if int(sys.argv[7]) or int(sys.argv[8]) or int(sys.argv[5]) else "handoff_returned" if sys.argv[6] == "returned" else "no_dispatch_needed",
  "plan": json.loads(Path(sys.argv[2]).read_text()),
  "terminal": sys.argv[3],
  "dashboard_actions": sys.argv[4],
  "genie_exit": int(sys.argv[5]),
  "genie_handoff_state": sys.argv[6],
  "terminal_exit": int(sys.argv[7]),
  "dashboard_exit": int(sys.argv[8]),
}, ensure_ascii=False, indent=2) + "\n")
PY
exit "$HANDOFF_EXIT"
