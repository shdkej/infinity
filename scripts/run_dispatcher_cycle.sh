#!/usr/bin/env bash
# The only Infinity dispatcher schedule is the host's existing 10-minute cron.
set -u -o pipefail
umask 077

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OPENCLAW_BIN="/home/ubuntu/.npm-global/bin/openclaw"
STATE_DIR="${INFINITY_DISPATCHER_STATE_DIR:-/home/ubuntu/.openclaw/state/infinity-dispatcher-runs}"
TERMINAL_STATE_FILE="${INFINITY_TERMINAL_STATE_FILE:-$ROOT/data/dispatcher-terminal-notifications.json}"
LOCK_FILE="${INFINITY_DISPATCHER_LOCK_FILE:-/tmp/infinity-dispatcher.lock}"
AGENT_TIMEOUT_SECONDS="${INFINITY_DISPATCHER_AGENT_TIMEOUT_SECONDS:-480}"
mkdir -p "$STATE_DIR" 2>/dev/null || { printf '%s\n' 'Infinity 점검을 시작하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다.'; exit 0; }
exec 9>"$LOCK_FILE"
flock -n 9 || exit 0

RUN_FILE="$STATE_DIR/$(date -u +%Y%m%dT%H%M%SZ)-$$.json"
PLAN_FILE="$(mktemp)"
POST_PLAN_FILE="$(mktemp)"
PROMPT_FILE="$(mktemp)"
trap 'rm -f "$PLAN_FILE" "$POST_PLAN_FILE" "$PROMPT_FILE"' EXIT

bootstrap_failure() {
  python3 - "$RUN_FILE" <<'PY'
import json, sys
from pathlib import Path
Path(sys.argv[1]).write_text(json.dumps({"outcome":"canonical_fetch_failed","user_failure":{"stage":"canonical_fetch_failed","message":"Infinity 점검을 시작하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다."}}, ensure_ascii=False, indent=2)+"\n")
PY
  printf '%s\n' 'Infinity 점검을 시작하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다.'
  exit 0
}

# Planning and terminal checks must not depend on a dirty primary checkout.
VERIFY_ROOT="$(mktemp -d /tmp/infinity-dispatcher-verify-XXXXXX)"
git -C "$ROOT" fetch origin main >/dev/null 2>&1 || bootstrap_failure
git -C "$ROOT" worktree add --detach "$VERIFY_ROOT" origin/main >/dev/null 2>&1 || bootstrap_failure
trap 'git -C "$ROOT" worktree remove --force "$VERIFY_ROOT" >/dev/null 2>&1 || true; rm -f "$PLAN_FILE" "$POST_PLAN_FILE" "$PROMPT_FILE"' EXIT
test -z "$(git -C "$VERIFY_ROOT" status --porcelain)" || bootstrap_failure
python3 "$VERIFY_ROOT/scripts/prepare_dispatch_cycle.py" --repo "$VERIFY_ROOT" --json >"$PLAN_FILE" || bootstrap_failure

TERMINAL_EXIT=0
POST_TERMINAL_EXIT=0
DASHBOARD_EXIT=0
TERMINAL_RESULT="$(python3 "$VERIFY_ROOT/scripts/dispatch_terminal_notifications.py" --repo "$VERIFY_ROOT" --state "$TERMINAL_STATE_FILE" --deliver --openclaw-bin "$OPENCLAW_BIN" 2>&1)" || TERMINAL_EXIT=$?
DASHBOARD_RESULT="$(python3 "$ROOT/scripts/process_action_requests.py" --apply --limit 10 --json 2>&1)" || DASHBOARD_EXIT=$?
[[ "$TERMINAL_EXIT" -ne 0 ]] && TERMINAL_RESULT="terminal_error(exit=${TERMINAL_EXIT}):${TERMINAL_RESULT}"
[[ "$DASHBOARD_EXIT" -ne 0 ]] && DASHBOARD_RESULT="dashboard_error(exit=${DASHBOARD_EXIT}):${DASHBOARD_RESULT}"
HANDOFF_EXIT=0
HANDOFF_STATE="not_needed"
HANDOFF_VERIFY_EXIT=0

if python3 - "$PLAN_FILE" <<'PY'
import json, sys
plan = json.load(open(sys.argv[1]))
raise SystemExit(0 if plan["dispatch_required"] else 1)
PY
then
  # Custody must be durable before Genie is invoked.  This is intentionally a
  # dispatcher-owned write, not an instruction that a delegated session may
  # forget to perform.
  while IFS= read -r INTENT_ID; do
    [[ -z "$INTENT_ID" ]] && continue
    python3 "$ROOT/scripts/record_intent_trace.py" dispatcher-handoff \
      --intent-id "$INTENT_ID" \
      --run-id "$(python3 - "$PLAN_FILE" <<'PY'
import json, sys
print(json.load(open(sys.argv[1]))["run_id"])
PY
)" \
      --canonical-sha "$(python3 - "$PLAN_FILE" <<'PY'
import json, sys
print(json.load(open(sys.argv[1]))["canonical_sha"])
PY
)"
  done < <(python3 - "$PLAN_FILE" <<'PY'
import json, sys
for item in json.load(open(sys.argv[1]))["handoff_candidates"]:
    print(item["intent_id"])
PY
)
  python3 - "$PLAN_FILE" "$PROMPT_FILE" <<'PY'
import json, sys
plan = json.load(open(sys.argv[1]))
message = f'''You are the direct Genie executor for the single existing Infinity dispatcher.
Canonical revision: {plan["canonical_sha"]}
Dispatcher run: {plan["run_id"]}
Plan: {json.dumps(plan, ensure_ascii=False)}

Do not create schedules. Do not use dashboard_actions as work status. Fetch Infinity origin/main first; if its revision changed, make no mutation and return that reason. Repair each invalid_state item only by moving it to its contract-correct lane or recording its exact blocker. For every promotion candidate, move only that canonical Inbox block to Active, never exceeding three Active intents. For every waiting_retry_candidate, move the canonical Waiting block to Active and attempt the stated autonomous alternative; do not ask the user again unless a real approval boundary remains. For each handoff/resume candidate, execute or resume it yourself; do not return it to the main agent. A plan_activation_candidate has no active task: first mark exactly its named pending task Active in both task-plan.json and task-plan.md, preserve its dependencies, set started_at, and commit/push that transition, then execute it. A terminalization_candidate has no remaining plan task: verify its Archive contract (required report, Red result, remote proof, and any domain gates). `INTENTS.md` is the canonical source block: an individual `intents/{lane}/{id}.md` file is optional. If that file is absent but the registry block and required evidence exist, create `intents/archive/{id}.md` from the registry fields, move the registry block to Archive, and finish agent-owned closeout. Normalize a legacy trace with `scripts/record_intent_trace.py` before treating its old shape as a blocker. Otherwise move it to Waiting only for a user, external, approval, or genuinely missing artifact condition; never use Waiting for a missing optional intent file. Never activate a task until every depends_on task is done. Never call a broad 'quality iteration' a task: it must be an explicitly Active leaf task with a concrete evidence target. A timebox_reassessment_candidate has hit max_minutes: do not continue blindly. Record a dashed plan change and choose exactly one: split into smaller leaf tasks, switch to a verified alternative, or record a real external blocker. Recalculate the remaining deadline budget before activating follow-on work. If the active leaf task cannot produce new evidence, record its precise blocker and move it to the correct lane instead of accepting another empty handoff. Inspect follow_up_candidates explicitly: create only safe, non-duplicate Inbox follow-ups with the original notification metadata; leave approval-boundary follow-ups Waiting with their exact blocker.

Before substantive work, append a dispatcher_handoff event to traces/<intent-id>.json with run_id, canonical_sha, agent=genie, session_key=agent:genie:infinity-dispatcher, timestamp, and status=accepted. Commit and push only explicit Infinity files, fetch, and prove HEAD == origin/main. Preserve approval boundaries. If starting is unsafe, record a precise Waiting or stale_guard_released reason; never claim completion.

Return JSON containing intent IDs, session evidence, state changes, commit, and remote proof.'''
if plan.get("waiting_closeout_candidates"):
    message += """\n\nFor every waiting_closeout_candidate: this is explicitly `waiting_on: internal`, with completed work and no user/external approval boundary. Complete its archive receipt, move it to Archive, and notify its original thread. Do not ask the user to approve an internal record."""
if plan.get("expansion_candidates"):
    message += """\n\nFor every expansion_candidate: before terminalization, append at most its stated batch_size of concrete, evidence-bearing leaf tasks from expansion_brief to both task-plan.json and task-plan.md. Preserve completed tasks and dependencies, append a dashed plan-change record with the count and reason, and never exceed target_total_tasks (always 50–60). Do not expand without that explicit policy, and never use it to bypass an approval, safety, or quality gate."""
open(sys.argv[2], "w", encoding="utf-8").write(message)
PY
  timeout --foreground "${AGENT_TIMEOUT_SECONDS}s" "$OPENCLAW_BIN" agent --agent genie --session-key agent:genie:infinity-dispatcher --message-file "$PROMPT_FILE" --thinking low --timeout "$AGENT_TIMEOUT_SECONDS" --json >"$STATE_DIR/$(basename "$RUN_FILE" .json)-genie.json" 2>&1
  HANDOFF_EXIT=$?
  HANDOFF_STATE="returned"
  [[ "$HANDOFF_EXIT" -eq 124 ]] && HANDOFF_STATE="timeout"
  if [[ "$HANDOFF_EXIT" -eq 0 ]]; then
    if ! python3 "$ROOT/scripts/prepare_dispatch_cycle.py" --repo "$ROOT" --json >"$POST_PLAN_FILE"; then
      HANDOFF_VERIFY_EXIT=1
      HANDOFF_STATE="post_handoff_fetch_failed"
    elif ! python3 - "$PLAN_FILE" "$POST_PLAN_FILE" "$ROOT" <<'PY'
import json, re, subprocess, sys
before, after = (json.load(open(path)) for path in sys.argv[1:3])
requested = {item["intent_id"] for item in before["handoff_candidates"]}
if before["dispatch_required"] and after["canonical_sha"] == before["canonical_sha"]:
    raise SystemExit("canonical revision unchanged after required dispatcher work")
if requested:
    still_stale = requested & {item["intent_id"] for item in after["resume_candidates"]}
    if still_stale:
        raise SystemExit("still missing execution evidence: " + ",".join(sorted(still_stale)))
for item in before.get("expansion_candidates", []):
    expansion = item["expansion"]
    raw = subprocess.check_output(["git", "show", f"origin/main:{expansion['task_plan']}"], cwd=sys.argv[3], text=True)
    tasks = json.loads(raw).get("tasks", [])
    leaves = [task for task in tasks if re.fullmatch(r"T\d+\.\d+", str(task.get("id", "")))]
    ready = [task for task in leaves if str(task.get("status", "")).lower() in {"pending", "active"}]
    before_ids = set(expansion["current_leaf_ids"])
    after_ids = {str(task.get("id")) for task in leaves}
    removed = before_ids - after_ids
    added = after_ids - before_ids
    if removed:
        raise SystemExit(f"expansion rewrote completed leaf history for {item['intent_id']}: removed={sorted(removed)}")
    if not (1 <= len(added) <= expansion["batch_size"]):
        raise SystemExit(f"expansion was not persisted for {item['intent_id']}: added={len(added)}")
    if not ready:
        raise SystemExit(f"expansion did not leave executable leaf work for {item['intent_id']}")
PY
    then
      HANDOFF_VERIFY_EXIT=1
      HANDOFF_STATE="post_handoff_unverified"
    else
      HANDOFF_STATE="verified"
    fi
  fi
else
  HANDOFF_STATE="not_needed"
fi

# Genie may move an intent to Waiting or Archive during this cycle.  Reconciling
# only before the handoff silently delays that state transition until a later
# cron run; send its origin-thread notification now and persist the receipt.
POST_TERMINAL_RESULT="$(python3 "$VERIFY_ROOT/scripts/dispatch_terminal_notifications.py" --repo "$VERIFY_ROOT" --state "$TERMINAL_STATE_FILE" --deliver --openclaw-bin "$OPENCLAW_BIN" 2>&1)" || POST_TERMINAL_EXIT=$?
[[ "$POST_TERMINAL_EXIT" -ne 0 ]] && POST_TERMINAL_RESULT="terminal_post_handoff_error(exit=${POST_TERMINAL_EXIT}):${POST_TERMINAL_RESULT}"

python3 - "$RUN_FILE" "$PLAN_FILE" "$POST_PLAN_FILE" "$TERMINAL_RESULT" "$POST_TERMINAL_RESULT" "$DASHBOARD_RESULT" "$HANDOFF_EXIT" "$HANDOFF_STATE" "$TERMINAL_EXIT" "$POST_TERMINAL_EXIT" "$DASHBOARD_EXIT" "$HANDOFF_VERIFY_EXIT" <<'PY'
import json, sys
from pathlib import Path
post_plan = json.loads(Path(sys.argv[3]).read_text()) if Path(sys.argv[3]).stat().st_size else None
Path(sys.argv[1]).write_text(json.dumps({
  "outcome": "attention" if int(sys.argv[10]) or int(sys.argv[11]) or int(sys.argv[7]) or int(sys.argv[12]) else "handoff_verified" if sys.argv[8] == "verified" else "no_dispatch_needed",
  "plan": json.loads(Path(sys.argv[2]).read_text()),
  "post_handoff_plan": post_plan,
  "terminal": sys.argv[4],
  "post_handoff_terminal": sys.argv[5],
  "dashboard_actions": sys.argv[6],
  "genie_exit": int(sys.argv[7]),
  "genie_handoff_state": sys.argv[8],
  "terminal_exit": int(sys.argv[9]),
  "post_handoff_terminal_exit": int(sys.argv[10]),
  "dashboard_exit": int(sys.argv[11]),
  "handoff_verify_exit": int(sys.argv[12]),
}, ensure_ascii=False, indent=2) + "\n")
PY
SNAPSHOT_PUBLISH_EXIT=0
python3 "$ROOT/scripts/publish_dispatcher_snapshot.py" "$RUN_FILE" >/dev/null 2>&1 || SNAPSHOT_PUBLISH_EXIT=$?
if [[ "$SNAPSHOT_PUBLISH_EXIT" -ne 0 ]]; then
  # The protected run record remains the source of truth; the next cycle retries
  # the small metrics mirror without exposing raw diagnostics to cron output.
  python3 - "$RUN_FILE" <<'PY'
import json, sys
from pathlib import Path
path = Path(sys.argv[1]); data = json.loads(path.read_text())
data["snapshot_publish_exit"] = 1
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
PY
fi
FINAL_EXIT="$HANDOFF_EXIT"
if [[ "$TERMINAL_EXIT" -ne 0 || "$POST_TERMINAL_EXIT" -ne 0 || "$DASHBOARD_EXIT" -ne 0 || "$HANDOFF_VERIFY_EXIT" -ne 0 ]]; then
  python3 - "$RUN_FILE" <<'PY'
import json, sys
from pathlib import Path
path = Path(sys.argv[1]); data = json.loads(path.read_text())
data["user_failure"] = {"stage":"dispatcher","message":"Infinity 작업 일부를 확인하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다."}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
PY
  FINAL_EXIT=0
fi
exit "$FINAL_EXIT"
