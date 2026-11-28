#!/usr/bin/env python3
"""Read-only decisions and whole-window reports for the current daily experiment.

Examples (JSON on stdout; errors exit nonzero without exposing API output):
  python3 scripts/miniapp_experiment.py snapshot --remote
  python3 scripts/miniapp_experiment.py report --window r1 --registry INTENTS.yaml
No scheduling, dispatch, publication, registry writes, or metric summation occurs here.
"""
import argparse
import base64
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import subprocess
import sys

import yaml

INTENT_ID = "miniapp-image-tools-20261118-qa-01"
REMOTE_ENDPOINT = "repos/shdkej/infinity/contents/INTENTS.yaml?ref=main"
TERMINAL = {"completed", "completed_no_change", "completed_with_blockers", "failed",
            "blocked", "partial_blocked", "expired", "timed_out", "cancelled", "done"}
GUARD_TERMINAL = {"completed", "failed", "expired", "timed_out", "cancelled", "terminated"}
UNSENT = {None, "pending", "prepared", "not_sent"}
PENDING = {"pending", "prepared", "queued", "ready"}
BLOCKED = {"failed", "blocked", "partial_blocked", "completed_with_blockers", "expired", "timed_out"}
GENERAL_MINUTES = 20
OBSERVATION_MINUTES = 15


def parse_time(value):
    """Require an explicit timezone: local process timezone must not affect gates."""
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, str):
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    else:
        raise ValueError("timestamp must be an ISO string with a timezone")
    if parsed.tzinfo is None:
        raise ValueError("timestamp requires a timezone")
    return parsed


def load_registry(remote=False, registry=None):
    if remote:
        try:
            response = subprocess.run(["gh", "api", REMOTE_ENDPOINT], capture_output=True,
                                      text=True, timeout=15, check=False)
        except subprocess.TimeoutExpired as exc:
            raise ValueError("remote registry read timed out") from exc
        except OSError as exc:
            raise ValueError("remote registry reader unavailable") from exc
        if response.returncode:
            raise ValueError("remote registry read failed")
        try:
            envelope = json.loads(response.stdout)
            if envelope.get("encoding") != "base64":
                raise ValueError("unexpected registry encoding")
            content = base64.b64decode("".join(envelope["content"].split()), validate=True).decode("utf-8")
        except (KeyError, TypeError, UnicodeError, ValueError) as exc:
            raise ValueError("invalid remote registry response") from exc
    else:
        content = Path(registry or Path(__file__).resolve().parents[1] / "INTENTS.yaml").read_text(encoding="utf-8")
    try:
        value = yaml.safe_load(content)
    except yaml.YAMLError as exc:
        raise ValueError("invalid registry YAML") from exc
    if not isinstance(value, dict):
        raise ValueError("registry must be a mapping")
    return value


def extract_run(registry, intent_id=INTENT_ID):
    lanes = registry.get("lanes", {})
    if not isinstance(lanes, dict):
        raise ValueError("registry lanes must be a mapping")
    matches = [item for lane in lanes.values() if isinstance(lane, list)
               for item in lane if isinstance(item, dict) and item.get("id") == intent_id]
    if len(matches) != 1:
        raise ValueError("expected exactly one experiment Intent")
    run = matches[0].get("experiment_run")
    if not isinstance(run, dict):
        raise ValueError("current experiment run must be a mapping")
    validate_run(run)
    return run


def window_id(window):
    return window.get("id") or window.get("window_id")


def validate_run(run):
    match = re.fullmatch(r"(?:miniapp|threads)-(\d{8})-2h", str(run.get("run_id", "")))
    day = str(run.get("date", ""))
    if not match or match[1] != day.replace("-", "") or run.get("timezone") != "Asia/Seoul":
        raise ValueError("unexpected experiment run")
    run_start, run_end = parse_time(run.get("start_at")), parse_time(run.get("end_at"))
    seoul = timezone(timedelta(hours=9))
    if (run_start.astimezone(seoul).date().isoformat() != day
            or run_end.astimezone(seoul).date().isoformat() != day
            or (run_end - run_start).total_seconds() != 21600):
        raise ValueError("run must cover six hours on its declared day")
    windows = run.get("windows")
    tasks = run.get("tasks")
    if not isinstance(windows, list) or len(windows) != 3 or not isinstance(tasks, list):
        raise ValueError("run requires three windows and a tasks list")
    expected = run_start
    ids = []
    for window in windows:
        wid = window_id(window)
        start, end = parse_time(window.get("start_at")), parse_time(window.get("end_at"))
        if start != expected or (end - start).total_seconds() != 7200:
            raise ValueError("windows must be contiguous two-hour intervals on the approved day")
        if window.get("observation_due_at") and not (
                start <= parse_time(window["observation_due_at"]) <= end - timedelta(minutes=OBSERVATION_MINUTES)):
            raise ValueError("window observation must leave at least fifteen minutes before its end")
        ids.append(wid)
        expected = end
    if ids != ["r1", "r2", "r3"] or expected != run_end:
        raise ValueError("unexpected experiment windows")
    task_ids = set()
    for task in tasks:
        if not isinstance(task, dict) or not task.get("id") or task.get("window_id") not in ids:
            raise ValueError("invalid task identity or window")
        if task["id"] in task_ids:
            raise ValueError("duplicate task identity")
        task_ids.add(task["id"])
        window = next(item for item in windows if window_id(item) == task["window_id"])
        start, end = parse_time(task.get("start_at")), parse_time(task.get("end_at"))
        if not (parse_time(window["start_at"]) <= start < end == parse_time(window["end_at"])):
            raise ValueError("task timestamps must stay within its window and end at the window deadline")
        if "wrap_up_by" in task and not start < parse_time(task["wrap_up_by"]) <= end:
            raise ValueError("task wrap-up must follow its start and stay within its deadline")


def guard_released(task, now):
    guard = task.get("guard") or {}
    if guard.get("state") not in GUARD_TERMINAL:
        return False
    if guard.get("task_id", task["id"]) != task["id"] or type(guard.get("exit_code")) is not int:
        return False
    if guard["state"] == "completed" and guard["exit_code"] != 0:
        return False
    if not guard.get("finished_at") or not guard.get("lock_free_verified_at"):
        return False
    finished = parse_time(guard["finished_at"])
    released = parse_time(guard["lock_free_verified_at"])
    return parse_time(task["start_at"]) <= finished <= released <= now


def router_rejected_before_start(task, now):
    """An explicit expired-router receipt proves this task never owned the lock.

    This is not a release receipt: every other sent task still passes its own gate.
    """
    guard = task.get("guard") or {}
    checked = task.get("receipt_checked_at")
    return (task.get("status") == "expired" and type(task.get("router_exit_code")) is int
            and task["router_exit_code"] == 5
            and guard.get("state") == "not_started"
            and all(guard.get(key) is None for key in ("exit_code", "finished_at", "lock_free_verified_at"))
            and bool(task.get("receipt_evidence_url")) and bool(checked)
            and parse_time(task["end_at"]) <= parse_time(checked) <= now)


def expired_without_handoff(task, now):
    """Close an unsent deadline miss only when no delivery or process was attempted."""
    guard = task.get("guard") or {}
    expired = task.get("expired_at")
    return (task.get("status") == "expired" and task.get("handoff_status") in {"not_sent", "prepared"}
            and all(not task.get(key) for key in (
                "handoff_message_id", "handoff_queue_id", "handoff_attempt_at", "handoff_at",
                "sent_at", "handoff_receipt", "actual_started_at"))
            and guard.get("state") == "not_started"
            and all(guard.get(key) is None for key in (
                "started_at", "exit_code", "finished_at", "lock_free_verified_at"))
            and bool(task.get("expiry_reason")) and bool(expired)
            and parse_time(task["end_at"]) <= parse_time(expired) <= now)


def terminal_safe(task, now):
    return (bool(task.get("result_summary")) and task.get("status") in TERMINAL
            and (guard_released(task, now) or router_rejected_before_start(task, now)
                 or expired_without_handoff(task, now)))


def unsent(task):
    guard = task.get("guard") or {}
    return (task.get("status") in PENDING and task.get("handoff_status") in UNSENT
            and not task.get("handoff_message_id")
            and guard.get("state") in {None, "pending", "not_started"})


def unique(values):
    seen, result = set(), []
    for value in values:
        key = json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)
        if key not in seen:
            seen.add(key)
            result.append(copy.deepcopy(value))
    return result


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def summarize_window(run, window):
    wid = window_id(window)
    tasks = [task for task in run["tasks"] if task.get("window_id") == wid]
    changes = unique([value for task in tasks for key in ("product_changes", "changes")
                      for value in as_list(task.get(key))])
    releases = unique([value for task in tasks for value in as_list(task.get("release_runs"))])
    blockers = unique([value for task in tasks for value in
                       (as_list(task.get("blockers")) or
                        ([task["result_summary"]] if task.get("status") in BLOCKED and task.get("result_summary") else []))])
    return {
        "window_id": wid, "start_at": window["start_at"], "end_at": window["end_at"],
        "task_count": len(tasks), "task_ids": [task["id"] for task in tasks],
        "status_counts": {status: sum(str(task.get("status")) == status for task in tasks)
                          for status in sorted({str(task.get("status")) for task in tasks})},
        "product_changes": changes, "release_runs": releases, "blockers": blockers,
        "unknown_task_ids": [task["id"] for task in tasks if not task.get("result_summary")],
        "result_summaries": unique([task["result_summary"] for task in tasks if task.get("result_summary")]),
        "metrics": copy.deepcopy(window.get("metrics")),
        "observation_due_at": window.get("observation_due_at"),
        "report_status": window.get("report_status"), "exhausted": window.get("exhausted") is True,
        "pdca": copy.deepcopy(window.get("pdca")),
    }



def pdca_closed(run, window, now):
    """A decision must cite this window's finished observation, including failure."""
    p = window.get("pdca") or {}
    ids = p.get("check_task_ids")
    evidence = [t for t in run["tasks"] if t["window_id"] == window_id(window)
                and isinstance(ids, list) and t["id"] in ids]
    if (not ids or not isinstance(ids, list) or len(evidence) != len(set(ids))
            or not any(t.get("kind") == "observation" for t in evidence)
            or not all(terminal_safe(t, now) for t in evidence)
            or p.get("decision") not in {"keep", "refine", "pivot", "inconclusive"}
            or not p.get("learning") or not p.get("next_change")):
        return False
    try:
        check, act = parse_time(p.get("check_at")), parse_time(p.get("act_at"))
        if not parse_time(window.get("observation_due_at") or window["start_at"]) <= check <= act <= now:
            return False
        if p.get("observation_status") == "unavailable":
            return p["decision"] == "inconclusive"
        observed = (window.get("metrics") or {}).get("observed_at")
        return (p.get("observation_status") == "observed" and bool(observed)
                and parse_time(window["observation_due_at"]) <= parse_time(observed) <= check)
    except (ValueError, TypeError, KeyError):
        return False


def pdca_plan_ready(window, previous, now):
    p = window.get("pdca") or {}
    if not all(isinstance(p.get(k), str) and p[k].strip()
               for k in ("hypothesis", "changed_variable", "success_rule")):
        return False
    try:
        planned = parse_time(p.get("plan_at"))
        if planned > now:
            return False
        if previous is None:
            return True
        old = previous.get("pdca") or {}
        return (p.get("based_on_window_id") == window_id(previous)
                and p.get("changed_variable") == old.get("next_change")
                and isinstance(p.get("source_task_ids"), list)
                and set(p["source_task_ids"]) == set(old.get("check_task_ids") or [])
                and planned >= parse_time(old.get("act_at")))
    except (ValueError, TypeError):
        return False


def snapshot(run, now):
    validate_run(run)
    now = parse_time(now)
    windows, tasks = run["windows"], run["tasks"]
    current = next((window for window in windows
                    if parse_time(window["start_at"]) <= now < parse_time(window["end_at"])), None)
    ordered = sorted(enumerate(tasks), key=lambda pair:
                     (parse_time(pair[1]["start_at"]), pair[0]))
    due_tasks = [task for _, task in ordered if parse_time(task["start_at"]) <= now]
    current_task = due_tasks[-1] if due_tasks else None
    result = {
        "run_id": run["run_id"], "now": now.isoformat(), "fire": False, "reasons": [],
        "window_id": window_id(current) if current else None,
        "current_task": copy.deepcopy(current_task), "reports_due": [],
        "dispatch_allowed": False, "reuse_task_id": None, "status_check_task_id": None,
        "reconcile_task_id": None,
        "normalization_proposals": [], "dispatch_blocked_reason": None,
        "pdca_close_required_windows": [], "pdca_plan_required_window": None,
        "proposed_task": None,
        "metrics": copy.deepcopy(run.get("metrics")),
        "window_summaries": [summarize_window(run, window) for window in windows],
    }
    if not current or not (parse_time(run["start_at"]) <= now < parse_time(run["end_at"])):
        return result
    if run.get("enabled") is False or run.get("status") in {"finished", "completed", "cancelled", "stopped"}:
        return result
    result["reports_due"] = [window_id(window) for window in windows
                             if parse_time(window["end_at"]) <= now
                             and window.get("report_status") not in {"sent", "delivered"}]
    if result["reports_due"]:
        result["reasons"].append("window_report_due")
    # A previous-window process still owns the same lock. Result reports do not bypass it.
    unsafe = [task for _, task in ordered if not unsent(task) and not terminal_safe(task, now)]
    # A result label is not a machine state. Ask the supervisor to persist the
    # verified state, then re-read; this read-only helper does not open the gate.
    for task in unsafe:
        if (task.get("status") not in TERMINAL and task.get("result_summary")
                and guard_released(task, now)):
            state = task["guard"]["state"]
            result["normalization_proposals"].append({
                "task_id": task["id"], "status": "failed" if state == "terminated" else state,
                "reason": "same_task_result_and_guard_receipt_verified"})
    if result["normalization_proposals"]:
        result["reasons"].append("task_status_normalization_required")
    observation_due = parse_time(current.get("observation_due_at") or current["end_at"])
    metrics = current.get("metrics") or {}
    observation_recorded = any(value and observation_due <= parse_time(value) <= now for value in
                               (metrics.get("observed_at"), metrics.get("obs_attempted_at"), current.get("obs_attempted_at")))
    needs_observation = now >= observation_due and not observation_recorded
    if not unsafe:
        candidates = [task for _, task in ordered if task["window_id"] == window_id(current) and unsent(task)
                      and parse_time(task["start_at"]) <= now
                      and (not current.get("exhausted") or task.get("required") is True or needs_observation)]
        if needs_observation:
            candidates = [task for task in candidates if task.get("kind") == "observation"]
        remaining_minutes = (parse_time(current["end_at"]) - now).total_seconds() / 60
        if candidates:
            pending = candidates[0]
            deadline = min(parse_time(current["end_at"]), parse_time(pending.get("wrap_up_by") or pending["end_at"]))
            remaining_minutes = (deadline - now).total_seconds() / 60
            minimum = OBSERVATION_MINUTES if pending.get("kind") == "observation" else GENERAL_MINUTES
            if remaining_minutes >= minimum:
                result["reuse_task_id"] = pending["id"]
                result["dispatch_allowed"] = True
                result["reasons"].append("prepared_task_ready")
            else:
                result["dispatch_blocked_reason"] = ("insufficient_time_before_task_wrap_up" if pending.get("wrap_up_by")
                                                     else "insufficient_time_before_window_end")
        elif current.get("planned_tasks_only"):
            result["dispatch_blocked_reason"] = "no_due_planned_task"
        elif not current.get("exhausted") or needs_observation:
            minimum = OBSERVATION_MINUTES if needs_observation else GENERAL_MINUTES
            if remaining_minutes >= minimum:
                result["dispatch_allowed"] = True
                if not needs_observation:
                    result["reasons"].append("task_terminal_guard_released" if tasks else "first_task")
            else:
                result["dispatch_blocked_reason"] = "insufficient_time_before_window_end"
        if needs_observation and result["dispatch_allowed"]:
            result["reasons"].append("metrics_observation_due")
    if unsafe:
        # A status request is not a terminal receipt. Reconcile the original thread
        # after ten minutes, then at most every fifteen minutes while unresolved.
        # This only wakes the supervisor; it never relaxes the dispatch/lock gate.
        for task in unsafe:
            guard = task.get("guard") or {}
            running = task.get("status") in {"running", "accepted"} or guard.get("state") == "running"
            if guard_released(task, now) and not task.get("result_summary"):
                result["reconcile_task_id"] = task["id"]
                result["reasons"].append("terminal_result_missing")
                break
            if any(item["task_id"] == task["id"] for item in result["normalization_proposals"]):
                continue
            if task.get("status_check_at"):
                checked = task.get("receipt_checked_at")
                since = parse_time(checked or task["status_check_at"])
                interval = 900 if checked or running else 600
                if (now - since).total_seconds() >= interval:
                    result["reconcile_task_id"] = task["id"]
                    result["reasons"].append("receipt_reconciliation_due")
                    break
                continue
            if now >= parse_time(task["end_at"]):
                result["status_check_task_id"] = task["id"]
                result["reasons"].append("task_deadline_status_check")
                break
            since = (guard.get("started_at") or task.get("actual_started_at") or task.get("handoff_at")
                     or task.get("sent_at") or task.get("handoff_attempt_at") or task.get("start_at"))
            if running:
                target = task.get("execution_target_minutes", 45)
                if type(target) is not int or target <= 0:
                    raise ValueError("execution target must be a positive integer of minutes")
                if (now - parse_time(since)).total_seconds() >= target * 60:
                    result["status_check_task_id"] = task["id"]
                    result["reasons"].append("execution_target_status_check")
                    break
                if needs_observation and task.get("kind") != "observation":
                    result["status_check_task_id"] = task["id"]
                    result["reasons"].append("observation_blocked_status_check")
                    break
                continue
            if since and (now - parse_time(since)).total_seconds() >= 600:
                result["status_check_task_id"] = task["id"]
                result["reasons"].append("unconfirmed_handoff_status_check")
                break
    if run.get("pdca_required") and not unsafe:
        for window in windows:
            observations = [t for t in tasks if t["window_id"] == window_id(window)
                            and t.get("kind") == "observation"]
            if (parse_time(window["start_at"]) <= now and observations
                    and all(terminal_safe(t, now) for t in observations)
                    and not pdca_closed(run, window, now)):
                result["pdca_close_required_windows"].append(window_id(window))
        pending = next((t for t in tasks if t["id"] == result["reuse_task_id"]), None)
        if result["dispatch_allowed"] and (not pending or pending.get("kind") != "observation"):
            index = windows.index(current)
            previous = windows[index - 1] if index else None
            if previous and not pdca_closed(run, previous, now):
                if window_id(previous) not in result["pdca_close_required_windows"]:
                    result["pdca_close_required_windows"].append(window_id(previous))
                result["dispatch_blocked_reason"] = "previous_pdca_not_closed"
            elif not pdca_plan_ready(current, previous, now):
                result["pdca_plan_required_window"] = window_id(current)
                result["dispatch_blocked_reason"] = "pdca_plan_not_ready"
            if result["dispatch_blocked_reason"]:
                result["dispatch_allowed"] = False
                result["reuse_task_id"] = None
                result["reasons"] = [x for x in result["reasons"] if x != "prepared_task_ready"]
        if result["pdca_close_required_windows"]:
            result["reasons"].append("pdca_check_act_required")
        if result["pdca_plan_required_window"]:
            result["reasons"].append("pdca_plan_required")
    result["fire"] = bool(result["reasons"])
    if result["dispatch_allowed"] and not result["reuse_task_id"]:
        prefix = f"{run['run_id'].removesuffix('-2h')}-{window_id(current)}-t"
        serial, used = 1, {task["id"] for task in tasks}
        while f"{prefix}{serial:02d}" in used:
            serial += 1
        result["proposed_task"] = {
            "id": f"{prefix}{serial:02d}", "window_id": window_id(current),
            "kind": "observation" if needs_observation else "engagement",
            "goal": None, "start_at": now.astimezone(timezone.utc).isoformat(),
            "end_at": current["end_at"], "status": "prepared",
            "handoff_status": "prepared", "handoff_message_id": None,
            "result_summary": None, "changes": [], "release_runs": [],
            "guard": {"state": "not_started", "exit_code": None,
                      "finished_at": None, "lock_free_verified_at": None},
            "status_check_at": None,
        }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("snapshot", "report"):
        command = commands.add_parser(name)
        source = command.add_mutually_exclusive_group()
        source.add_argument("--remote", action="store_true")
        source.add_argument("--registry", type=Path)
        command.add_argument("--intent-id", default=INTENT_ID)
        command.add_argument("--now", help="ISO timestamp with timezone (default: now)")
        if name == "report":
            command.add_argument("--window", choices=("r1", "r2", "r3"), required=True)
    args = parser.parse_args(argv)
    try:
        run = extract_run(load_registry(args.remote, args.registry), args.intent_id)
        result = snapshot(run, parse_time(args.now) if args.now else datetime.now(timezone.utc))
        if args.command == "report":
            result = {"run_id": run["run_id"], "metrics": copy.deepcopy(run.get("metrics")),
                      "window": next(item for item in result["window_summaries"] if item["window_id"] == args.window)}
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":"), default=str))
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        # Do not print remote stdout/stderr, YAML fragments, or credentials.
        print(f"miniapp_experiment: {type(exc).__name__}: " +
              (str(exc) if isinstance(exc, ValueError) else "registry unavailable or invalid"), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
