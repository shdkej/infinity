#!/usr/bin/env bash
# The OpenClaw automation owns the only 10-minute Infinity dispatcher schedule.
set -u -o pipefail
umask 077

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
if [[ ! -s "$NVM_DIR/nvm.sh" ]]; then
  printf '%s\n' 'NVM initialization script is unavailable; dispatcher cannot start.' >&2
  exit 1
fi
. "$NVM_DIR/nvm.sh"
nvm use --silent default >/dev/null
OPENCLAW_BIN="${OPENCLAW_BIN:-${NVM_BIN:-}/openclaw}"
if [[ ! -x "$OPENCLAW_BIN" ]]; then
  printf 'OpenClaw CLI is unavailable at %s.\n' "$OPENCLAW_BIN" >&2
  exit 1
fi
STATE_DIR="${INFINITY_DISPATCHER_STATE_DIR:-/home/ubuntu/.openclaw/state/infinity-dispatcher-runs}"
LOCK_FILE="${INFINITY_DISPATCHER_LOCK_FILE:-/tmp/infinity-dispatcher.lock}"
AGENT_TIMEOUT_SECONDS="${INFINITY_DISPATCHER_AGENT_TIMEOUT_SECONDS:-480}"
DISPATCHER_SESSION_KEY="${INFINITY_DISPATCHER_SESSION_KEY:-agent:genie:infinity-dispatcher-command-v1}"
mkdir -p "$STATE_DIR" 2>/dev/null || { printf '%s\n' 'Infinity 점검을 시작하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다.'; exit 1; }
exec 9>"$LOCK_FILE"
flock -n 9 || exit 0

RUN_FILE="$STATE_DIR/$(date -u +%Y%m%dT%H%M%SZ)-$$.json"
PLAN_FILE="$(mktemp)"
POST_PLAN_FILE="$(mktemp)"
PROMPT_FILE="$(mktemp)"
PROMPT_STAGE_FILE="${PROMPT_FILE}.stage"
trap 'rm -f "$PLAN_FILE" "$POST_PLAN_FILE" "$PROMPT_FILE" "$PROMPT_STAGE_FILE"' EXIT

bootstrap_failure() {
  python3 - "$RUN_FILE" <<'PY'
import json, sys
from pathlib import Path
Path(sys.argv[1]).write_text(json.dumps({"outcome":"canonical_fetch_failed","user_failure":{"stage":"canonical_fetch_failed","message":"Infinity 점검을 시작하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다."}}, ensure_ascii=False, indent=2)+"\n")
PY
  printf '%s\n' 'Infinity 점검을 시작하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다.'
  exit 1
}

# Keep the canonical checkout on main. Never let a scheduled run update or
# write through a feature branch; switch only when Git can preserve local work.
CHECKED_OUT_BRANCH="$(git -C "$ROOT" symbolic-ref --quiet --short HEAD 2>/dev/null || true)"
if [[ "$CHECKED_OUT_BRANCH" != "main" ]]; then
  git -C "$ROOT" switch main >/dev/null 2>&1 || bootstrap_failure
fi

# The dispatcher owns the repository sync boundary: pull before planning, and
# never treat a local commit as complete until the remote ref proves it.
git -C "$ROOT" pull --ff-only origin main >/dev/null 2>&1 || bootstrap_failure

# Planning and terminal checks must not depend on a dirty primary checkout.
VERIFY_ROOT="$(mktemp -d /tmp/infinity-dispatcher-verify-XXXXXX)"
git -C "$ROOT" fetch --prune origin main >/dev/null 2>&1 || bootstrap_failure
FETCHED_MAIN_SHA="$(git -C "$ROOT" rev-parse FETCH_HEAD 2>/dev/null)" || bootstrap_failure
ORIGIN_MAIN_SHA="$(git -C "$ROOT" rev-parse refs/remotes/origin/main 2>/dev/null)" || bootstrap_failure
[[ "$FETCHED_MAIN_SHA" == "$ORIGIN_MAIN_SHA" ]] || bootstrap_failure
PRIMARY_HEAD_SHA="$(git -C "$ROOT" rev-parse HEAD 2>/dev/null)" || bootstrap_failure
[[ "$PRIMARY_HEAD_SHA" == "$ORIGIN_MAIN_SHA" ]] || bootstrap_failure
git -C "$ROOT" worktree add --detach "$VERIFY_ROOT" origin/main >/dev/null 2>&1 || bootstrap_failure
trap 'git -C "$ROOT" worktree remove --force "$VERIFY_ROOT" >/dev/null 2>&1 || true; rm -f "$PLAN_FILE" "$POST_PLAN_FILE" "$PROMPT_FILE" "$PROMPT_STAGE_FILE"' EXIT
test -z "$(git -C "$VERIFY_ROOT" status --porcelain)" || bootstrap_failure
python3 "$VERIFY_ROOT/scripts/prepare_dispatch_cycle.py" --repo "$VERIFY_ROOT" --json >"$PLAN_FILE" || bootstrap_failure

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
  # Write the handoff atomically and never call the CLI with an empty message.
  if ! python3 - "$PLAN_FILE" "$PROMPT_STAGE_FILE" <<'PY'
import json, sys
plan = json.load(open(sys.argv[1]))
class _LiteralIntentPath:
    """Preserve the one literal `{intent-id}` path token in the f-string."""
    def __sub__(self, _other):
        return "{intent-id}"
intent = _LiteralIntentPath()
id = None
message = f'''You are the direct Genie executor for the single existing Infinity dispatcher.
Canonical revision: {plan["canonical_sha"]}
Dispatcher run: {plan["run_id"]}
Plan: {json.dumps(plan, ensure_ascii=False)}

Do not create schedules. Do not use dashboard_actions as work status. Your sole execution repository is `/home/ubuntu/workspace/infinity`: begin by `cd /home/ubuntu/workspace/infinity && git fetch origin main`, then compare that repository's `origin/main` with the canonical revision. Do not treat a revision from any other checkout as an Infinity stale guard. If this Infinity revision changed, make no mutation and return that reason. Repair each invalid_state item only by moving it to its contract-correct lane or recording its exact blocker. For every promotion candidate, move only that canonical Inbox block to Active, never exceeding three Active intents. For every waiting_retry_candidate, move the canonical Waiting block to Active and attempt the stated autonomous alternative; do not ask the user again unless a real approval boundary remains. If the only autonomous blocker is a missing task-plan, create the required `artifacts/{intent-id}/work/task-plan.json` and `task-plan.md` from `ARTIFACT_RULES.md#대형-작업-태스크-계획`, add `task_plan`, `task_plan_doc`, and `task_plan_template` to the canonical card, then activate its first evidence-bearing leaf and execute it. Do not send that planning prerequisite to Waiting. This repair is permitted only with a valid explicit future canonical `deadline`; otherwise do not create a repair plan/leaf and use existing-material closeout. This missing-plan first-leaf repair applies only when the Intent has a valid explicit future canonical `deadline`; for every other missing-plan case, do not create a plan or leaf and use existing-material closeout. For each handoff/resume candidate, execute or resume it yourself; do not return it to the main agent. A plan_activation_candidate has no active task: first mark exactly its named pending task Active in both task-plan.json and task-plan.md, preserve its dependencies, set started_at, and commit/push that transition, then execute it. A terminalization_candidate can mean a completed plan, an explicit deadline reached with unfinished tasks, or a no-deadline missing-plan closeout: verify its Archive contract (required report, Red result, remote proof, and domain gates), preserve unfinished task IDs as incomplete, and never claim unperformed work is done. `INTENTS.yaml` is the canonical lifecycle source; an individual `intents/{lane}/{id}.md` file is optional. If that file is absent but the registry block and required evidence exist, create `intents/archive/{id}.md` from the registry fields, move the registry block to Archive, and finish agent-owned closeout. Normalize a legacy trace with `scripts/record_intent_trace.py` before treating its old shape as a blocker. Otherwise move it to Waiting only for a user, external, approval, or genuinely missing artifact condition; never use Waiting for a missing optional intent file. Never activate a task until every depends_on task is done. Never call a broad 'quality iteration' a task: it must be an explicitly Active leaf task with a concrete evidence target. A timebox_reassessment_candidate has hit max_minutes: do not continue blindly. Record a dashed plan change. Split it into smaller leaves only when `timebox_reassessment.allow_split` is true (a valid explicit future Intent `deadline`); otherwise switch to a verified alternative within the existing leaf or record its precise blocker and close out with the task incomplete—never add a child leaf. Recalculate remaining deadline budget before any allowed split. If the active leaf cannot produce new evidence, record its precise blocker and move it to the correct lane instead of accepting another empty handoff. Inspect follow_up_candidates explicitly: create only safe, non-duplicate Inbox follow-ups with the original notification metadata; leave approval-boundary follow-ups Waiting with their exact blocker.

For every missing_plan_repair_candidate (emitted only for an Active Intent with a valid explicit future `deadline`), create the required contract-compliant task-plan, add its card references, activate the first evidence-bearing leaf, and execute it in this cycle. Never create a repair plan or first leaf for a no-deadline Active Intent; route it to terminal closeout from existing evidence. Whenever an Active Intent creates or replaces a human-readable Markdown work artifact, update both its canonical INTENTS.yaml card and its detail intent (when present) with the current `artifact:` paths in the same commit, so the dashboard can display them even when GitHub directory listing is rate-limited. Automatic evidence-leaf expansion is permitted only when the canonical Intent field `deadline` contains a valid timezone-aware timestamp explicitly supplied by the user and the dispatch plan timestamp is before it. Never infer or invent a deadline from `delivery_not_before`, task timeboxes, `decision_deadline`, or an assumed duration. With no valid explicit deadline, finish only already-planned leaves; once they are complete, trigger normal terminal closeout from existing evidence or honor an explicit user stop, without replenishing leaves. For an explicit deadline, stop task execution/expansion at or after that timestamp and run one atomic terminal bundle: final Markdown, any user- or Intent-required HTML report, Archive card/detail transition, remote archive verification, dashboard Archive-card check, then original-thread notice. Before committing any Archive transition, run `python3 scripts/check_intents_consistency.py INTENTS.yaml`; for research intents also run `python3 scripts/verify_archive_remote.py <intent-id>` after the report and monthly ledger are present. If either check fails, do not push or notify terminal completion. A partial prose summary is not terminal work and never substitutes for the bundle. Internal report/commit/verification closeout is agent-owned and is not a Waiting condition; use Waiting only for a real user/external/approval blocker with an exact exit condition.

Before substantive work, append a dispatcher_handoff event to data/traces/<intent-id>.json with run_id, canonical_sha, agent=genie, session_key=agent:genie:infinity-dispatcher-v2, timestamp, and status=accepted. Commit and push only explicit Infinity files, fetch, and prove HEAD == origin/main. Preserve approval boundaries. If starting is unsafe, record a precise Waiting or stale_guard_released reason; never claim completion.

Return JSON containing intent IDs, session evidence, state changes, commit, and remote proof.'''
if plan.get("waiting_closeout_candidates"):
    message += """\n\nFor every waiting_closeout_candidate: this is explicitly `waiting_on: internal`, with completed work and no user/external approval boundary. Complete its archive receipt, move it to Archive, and notify its original thread. Do not ask the user to approve an internal record."""
if any(item.get("project_executor") for item in plan.get("handoff_candidates", [])):
    message += """\n\nProject execution contract: use `project_executor` only to resolve the exact project repository, TASKS.md, and required documents. Genie remains the direct executor and must read the listed documents, update the project's TASKS.md and artifact, and return the report path, commit SHA, origin/main SHA, and verification. Do not delegate project work to a retired project-specific agent or infer a different repository from the title."""
if plan.get("expansion_candidates"):
    message += """\n\nFor every expansion_candidate, first verify the canonical Intent's `deadline` is a valid timezone-aware timestamp, `Plan.at < deadline`, and that the deadline has not passed before you persist the additions. If any check fails, do not expand and allow the existing-plan/terminalization path to proceed. When eligible, append at most its stated batch_size of concrete, evidence-bearing leaf tasks from expansion_brief to both task-plan.json and task-plan.md. Preserve completed tasks and dependencies, append a dashed plan-change record with the count and reason, and never exceed target_total_tasks (always 50–60). Never use expansion to bypass an approval, safety, or quality gate."""
open(sys.argv[2], "w", encoding="utf-8").write(message)
PY
  then
    HANDOFF_EXIT=0
    HANDOFF_STATE="prompt_generation_failed"
    HANDOFF_VERIFY_EXIT=1
  elif [[ ! -s "$PROMPT_STAGE_FILE" ]]; then
    HANDOFF_EXIT=0
    HANDOFF_STATE="prompt_generation_empty"
    HANDOFF_VERIFY_EXIT=1
  else
    mv "$PROMPT_STAGE_FILE" "$PROMPT_FILE"
    timeout --foreground "${AGENT_TIMEOUT_SECONDS}s" "$OPENCLAW_BIN" agent --agent genie --session-key "$DISPATCHER_SESSION_KEY" --message-file "$PROMPT_FILE" --thinking low --timeout "$AGENT_TIMEOUT_SECONDS" --json >"$STATE_DIR/$(basename "$RUN_FILE" .json)-genie.json" 2>&1
    HANDOFF_EXIT=$?
    HANDOFF_STATE="returned"
    [[ "$HANDOFF_EXIT" -eq 124 ]] && HANDOFF_STATE="timeout"
  fi
  rm -f "$PROMPT_STAGE_FILE"
  if [[ "$HANDOFF_STATE" != prompt_generation_* && "$HANDOFF_EXIT" -eq 0 ]]; then
    if ! python3 "$ROOT/scripts/prepare_dispatch_cycle.py" --repo "$ROOT" --json >"$POST_PLAN_FILE"; then
      HANDOFF_VERIFY_EXIT=1
      HANDOFF_STATE="post_handoff_fetch_failed"
    elif ! python3 "$ROOT/scripts/check_intents_consistency.py" "$ROOT/INTENTS.yaml"; then
      HANDOFF_VERIFY_EXIT=1
      HANDOFF_STATE="archive_registry_contract_failed"
    elif ! python3 - "$PLAN_FILE" "$POST_PLAN_FILE" "$ROOT" <<'PY'
import json, re, subprocess, sys
import datetime as dt
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
    try:
        planned_at = dt.datetime.fromisoformat(before["at"].replace("Z", "+00:00"))
        verified_at = dt.datetime.fromisoformat(after["at"].replace("Z", "+00:00"))
        deadline = dt.datetime.fromisoformat(expansion["deadline"].replace("Z", "+00:00"))
    except (KeyError, TypeError, ValueError) as exc:
        raise SystemExit(f"expansion lacks a valid explicit deadline for {item['intent_id']}: {exc}")
    if (deadline.tzinfo is None or deadline.utcoffset() is None
            or planned_at.tzinfo is None or verified_at.tzinfo is None
            or planned_at >= deadline or verified_at >= deadline):
        raise SystemExit(f"expansion is not before a valid explicit deadline for {item['intent_id']}")
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
    doc = subprocess.check_output(["git", "show", f"origin/main:{expansion['task_plan_doc']}"], cwd=sys.argv[3], text=True)
    for leaf_id in added:
        match = re.search(rf"(?ms)^[●◐○].*?\b{re.escape(leaf_id)}\b.*?(?=^[●◐○].*?\bT\d+\.\d+\b|\Z)", doc)
        if not match or not all(token in match.group(0) for token in ("예상/최대", "의존", "증거:")):
            raise SystemExit(f"expansion leaf is missing a complete task-plan.md entry for {item['intent_id']}:{leaf_id}")
    if "— 계획 변경" not in doc or not all(leaf_id in doc for leaf_id in added):
        raise SystemExit(f"expansion is missing an append-only task-plan.md change record for {item['intent_id']}")
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

python3 - "$RUN_FILE" "$PLAN_FILE" "$POST_PLAN_FILE" "$HANDOFF_EXIT" "$HANDOFF_STATE" "$HANDOFF_VERIFY_EXIT" <<'PY'
import json, sys
from pathlib import Path
post_plan = json.loads(Path(sys.argv[3]).read_text()) if Path(sys.argv[3]).stat().st_size else None
Path(sys.argv[1]).write_text(json.dumps({
  "outcome": "attention" if int(sys.argv[6]) or int(sys.argv[4]) else "handoff_verified" if sys.argv[5] == "verified" else "no_dispatch_needed",
  "plan": json.loads(Path(sys.argv[2]).read_text()),
  "post_handoff_plan": post_plan,
  "genie_exit": int(sys.argv[4]),
  "genie_handoff_state": sys.argv[5],
  "handoff_verify_exit": int(sys.argv[6]),
}, ensure_ascii=False, indent=2) + "\n")
PY
FINAL_EXIT="$HANDOFF_EXIT"
if [[ "$HANDOFF_VERIFY_EXIT" -ne 0 || "$HANDOFF_EXIT" -ne 0 ]]; then
  python3 - "$RUN_FILE" <<'PY'
import json, sys
from pathlib import Path
path = Path(sys.argv[1]); data = json.loads(path.read_text())
data["user_failure"] = {"stage":"dispatcher","message":"Infinity 작업 일부를 확인하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다."}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
PY
  FINAL_EXIT=1
fi
exit "$FINAL_EXIT"
