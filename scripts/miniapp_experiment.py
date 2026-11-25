#!/usr/bin/env python3
"""Read-only decisions and whole-window reports for the 2026-11-25 experiment.

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
import subprocess
import sys

import yaml

INTENT_ID = "miniapp-image-tools-20261118-qa-01"
RUN_ID = "miniapp-20261125-2h"
REMOTE_ENDPOINT = "repos/shdkej/infinity/contents/INTENTS.yaml?ref=main"
START = "2026-11-25T17:00:00+09:00"
END = "2026-11-25T23:00:00+09:00"
TERMINAL = {"completed", "completed_no_change", "completed_with_blockers", "failed",
            "blocked", "partial_blocked", "expired", "timed_out", "cancelled", "done"}
GUARD_TERMINAL = {"completed", "failed", "expired", "timed_out", "cancelled", "terminated"}
UNSENT = {None, "pending", "prepared", "not_sent"}
PENDING = {"pending", "prepared", "queued", "ready"}
BLOCKED = {"failed", "blocked", "partial_blocked", "completed_with_blockers", "expired", "timed_out"}


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


def extract_run(registry):
    lanes = registry.get("lanes", {})
    if not isinstance(lanes, dict):
        raise ValueError("registry lanes must be a mapping")
    matches = [item for lane in lanes.values() if isinstance(lane, list)
               for item in lane if isinstance(item, dict) and item.get("id") == INTENT_ID]
    if len(matches) != 1:
        raise ValueError("expected exactly one experiment Intent")
    run = matches[0].get("experiment_run")
    if not isinstance(run, dict) or run.get("run_id") != RUN_ID:
        raise ValueError("current experiment run does not match expected run")
    return run


def window_id(window):
    return window.get("id") or window.get("window_id")


def validate_run(run):
    if run.get("run_id") != RUN_ID:
        raise ValueError("unexpected experiment run")
    windows = run.get("windows")
    tasks = run.get("tasks")
    if not isinstance(windows, list) or len(windows) != 3 or not isinstance(tasks, list):
        raise ValueError("run requires three windows and a tasks list")
    expected = parse_time(START)
    ids = []
    for window in windows:
        wid = window_id(window)
        start, end = parse_time(window.get("start_at")), parse_time(window.get("end_at"))
        if start != expected or (end - start).total_seconds() != 7200:
            raise ValueError("windows must be contiguous two-hour intervals on the approved day")
        if window.get("observation_due_at") and parse_time(window["observation_due_at"]) != end - timedelta(minutes=15):
            raise ValueError("window observation must be fifteen minutes before its end")
        ids.append(wid)
        expected = end
    if ids != ["r1", "r2", "r3"] or expected != parse_time(END):
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


def guard_released(task, now):
    guard = task.get("guard") or {}
    if guard.get("state") not in GUARD_TERMINAL:
        return False
    if not guard.get("finished_at") or not guard.get("lock_free_verified_at"):
        return False
    finished = parse_time(guard["finished_at"])
    released = parse_time(guard["lock_free_verified_at"])
    return finished <= released <= now


def terminal_safe(task, now):
    return task.get("status") in TERMINAL and guard_released(task, now)


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
    }


def snapshot(run, now):
    validate_run(run)
    now = parse_time(now)
    windows, tasks = run["windows"], run["tasks"]
    current = next((window for window in windows
                    if parse_time(window["start_at"]) <= now < parse_time(window["end_at"])), None)
    ordered = sorted(enumerate(tasks), key=lambda pair:
                     (parse_time(pair[1].get("start_at") or START), pair[0]))
    current_task = ordered[-1][1] if ordered else None
    result = {
        "run_id": RUN_ID, "now": now.isoformat(), "fire": False, "reasons": [],
        "window_id": window_id(current) if current else None,
        "current_task": copy.deepcopy(current_task), "reports_due": [],
        "dispatch_allowed": False, "reuse_task_id": None, "status_check_task_id": None,
        "metrics": copy.deepcopy(run.get("metrics")),
        "window_summaries": [summarize_window(run, window) for window in windows],
    }
    if not current or not (parse_time(START) <= now < parse_time(END)):
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
    observation_due = parse_time(current.get("observation_due_at") or current["end_at"])
    metrics = current.get("metrics") or {}
    observation_recorded = any(value and observation_due <= parse_time(value) <= now for value in
                               (metrics.get("observed_at"), metrics.get("obs_attempted_at"), current.get("obs_attempted_at")))
    needs_observation = now >= observation_due and not observation_recorded
    if not unsafe:
        candidates = [task for _, task in ordered if task["window_id"] == window_id(current) and unsent(task)
                      and (not current.get("exhausted") or task.get("required") is True or needs_observation)]
        if candidates:
            pending = candidates[0]
            if not pending.get("end_at") or now < parse_time(pending["end_at"]):
                result["reuse_task_id"] = pending["id"]
                result["dispatch_allowed"] = True
                result["reasons"].append("prepared_task_ready")
        elif not current.get("exhausted") or needs_observation:
            result["dispatch_allowed"] = True
            if not needs_observation:
                result["reasons"].append("task_terminal_guard_released" if tasks else "first_task")
        if needs_observation:
            result["reasons"].append("metrics_observation_due")
    if unsafe:
        # A confirmed running/accepted worker needs no repeated model wakeups.
        for task in unsafe:
            guard = task.get("guard") or {}
            if task.get("status_check_at"):
                continue
            if now >= parse_time(task["end_at"]):
                result["status_check_task_id"] = task["id"]
                result["reasons"].append("task_deadline_status_check")
                break
            if task.get("status") in {"running", "accepted"} or guard.get("state") == "running":
                continue
            since = task.get("handoff_at") or task.get("sent_at") or task.get("handoff_attempt_at") or task.get("start_at")
            if since and (now - parse_time(since)).total_seconds() >= 600:
                result["status_check_task_id"] = task["id"]
                result["reasons"].append("unconfirmed_handoff_status_check")
                break
    result["fire"] = bool(result["reasons"])
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("snapshot", "report"):
        command = commands.add_parser(name)
        source = command.add_mutually_exclusive_group()
        source.add_argument("--remote", action="store_true")
        source.add_argument("--registry", type=Path)
        command.add_argument("--now", help="ISO timestamp with timezone (default: now)")
        if name == "report":
            command.add_argument("--window", choices=("r1", "r2", "r3"), required=True)
    args = parser.parse_args(argv)
    try:
        run = extract_run(load_registry(args.remote, args.registry))
        result = snapshot(run, parse_time(args.now) if args.now else datetime.now(timezone.utc))
        if args.command == "report":
            result = {"run_id": RUN_ID, "metrics": copy.deepcopy(run.get("metrics")),
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
