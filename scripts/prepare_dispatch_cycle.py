#!/usr/bin/env python3
"""Build a read-only, origin/main-based Infinity dispatcher plan."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import uuid
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LANES = ("Inbox", "Active", "Waiting", "Archive")
MAX_ACTIVE = 3
FRESH_MINUTES = 25

def split_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## (Inbox|Active|Waiting|Archive)\s*$", text, re.M))
    return {match.group(1): text[match.end(): matches[i + 1].start() if i + 1 < len(matches) else len(text)] for i, match in enumerate(matches)}

def parse_entries(text: str, lane: str) -> list[dict[str, Any]]:
    starts = list(re.finditer(r"^### \[([^\]]+)\]\s*(.+?)\s*$", text, re.M))
    entries: list[dict[str, Any]] = []
    for i, match in enumerate(starts):
        body = text[match.end(): starts[i + 1].start() if i + 1 < len(starts) else len(text)]
        fields = {f.group(1): f.group(2) for f in re.finditer(r"^- ([a-zA-Z0-9_]+):\s*(.*?)\s*$", body, re.M)}
        entries.append({"id": match.group(1), "title": match.group(2), "lane": lane, "fields": fields})
    return entries

def expected_status(lane: str) -> set[str]:
    return {"Inbox": {"", "inbox"}, "Active": {"active"}, "Waiting": {"waiting", "blocked"}, "Archive": {"archived", "completed", "complete", "done"}}[lane]

def fresh_trace(intent_id: str, repo: Path, reference: dt.datetime, sha: str) -> dict[str, str] | None:
    path = repo / "traces" / f"{intent_id}.json"
    try:
        raw = path.read_text(encoding="utf-8") if sha == "fixture" else subprocess.check_output(["git", "show", f"origin/main:traces/{intent_id}.json"], cwd=repo, text=True)
        events = json.loads(raw).get("events", [])
    except (json.JSONDecodeError, subprocess.CalledProcessError, FileNotFoundError):
        return None
    for event in reversed(events):
        if event.get("type") not in {"dispatcher_handoff", "execution"}:
            continue
        try:
            at = dt.datetime.fromisoformat(str(event.get("at") or event.get("timestamp") or "").replace("Z", "+00:00"))
        except ValueError:
            continue
        status = str(event.get("status", "")).lower()
        if status in {"", "accepted", "running", "dispatched", "resumed"} and reference - at <= dt.timedelta(minutes=FRESH_MINUTES):
            return {"at": at.isoformat(), "status": status or "execution", "path": str(path.relative_to(repo))}
    return None

def canonical(repo: Path, intents: Path | None) -> tuple[str, str]:
    if intents:
        return intents.read_text(encoding="utf-8"), "fixture"
    subprocess.run(["git", "fetch", "origin", "main"], cwd=repo, check=True, capture_output=True, text=True)
    sha = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=repo, text=True).strip()
    return subprocess.check_output(["git", "show", "origin/main:INTENTS.md"], cwd=repo, text=True), sha

def priority(entry: dict[str, Any]) -> tuple[int, str, str]:
    rank = {"critical": 0, "high": 1, "normal": 2, "low": 3}.get(entry["fields"].get("priority", "normal").lower(), 2)
    return rank, entry["fields"].get("requested", ""), entry["id"]

def build_plan(text: str, sha: str, repo: Path) -> dict[str, Any]:
    sections = split_sections(text)
    missing = [lane for lane in LANES if lane not in sections]
    if missing:
        raise ValueError("missing_lanes:" + ",".join(missing))
    entries = [entry for lane in LANES for entry in parse_entries(sections[lane], lane)]
    invalid = [{"intent_id": e["id"], "lane": e["lane"], "status": e["fields"].get("status", "")} for e in entries if e["fields"].get("status", "").lower() not in expected_status(e["lane"])]
    inbox = [e for e in entries if e["lane"] == "Inbox"]
    active = [e for e in entries if e["lane"] == "Active"]
    reference = dt.datetime.now(dt.timezone.utc)
    live, resume = [], []
    for entry in active:
        item = {"intent_id": entry["id"], "title": entry["title"], "evidence": fresh_trace(entry["id"], repo, reference, sha)}
        (live if item["evidence"] else resume).append(item)
    slots = max(0, MAX_ACTIVE - len(active))
    promote = [{"intent_id": e["id"], "title": e["title"], "target_agent": "genie", "reason": "available_active_slot"} for e in sorted(inbox, key=priority)[:slots] if e["fields"].get("target_agent", "genie") == "genie"]
    invalid_ids = {e["intent_id"] for e in invalid}
    handoff = [e for e in promote + resume if e["intent_id"] not in invalid_ids]
    followups = []
    for entry in entries:
        if entry["lane"] != "Archive":
            continue
        report = entry["fields"].get("report", "")
        if not report:
            continue
        try:
            report_text = (repo / report).read_text(encoding="utf-8") if sha == "fixture" else subprocess.check_output(["git", "show", f"origin/main:{report}"], cwd=repo, text=True)
        except (OSError, subprocess.CalledProcessError):
            continue
        ids = re.search(r"(?mi)^\s*(?:- )?follow_up_intent_ids:\s*(.+?)\s*$", report_text)
        reasons = re.search(r"(?mi)^\s*(?:- )?follow_up_not_created_reasons:\s*(.+?)\s*$", report_text)
        if ids or reasons:
            followups.append({"intent_id": entry["id"], "report": report, "follow_up_intent_ids": ids.group(1) if ids else "", "follow_up_not_created_reasons": reasons.group(1) if reasons else ""})
    return {"schema_version": 1, "run_id": "dispatch-" + uuid.uuid4().hex, "at": reference.replace(microsecond=0).isoformat().replace("+00:00", "Z"), "canonical_sha": sha, "counts": {"inbox": len(inbox), "active": len(active), "waiting": sum(e["lane"] == "Waiting" for e in entries), "archive": sum(e["lane"] == "Archive" for e in entries)}, "invalid_state": invalid, "live_active": live, "resume_candidates": resume, "promote_candidates": promote, "handoff_candidates": handoff, "follow_up_candidates": followups, "no_work": not handoff and not invalid and not followups}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--intents", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        text, sha = canonical(args.repo, args.intents)
        plan = build_plan(text, sha, args.repo)
    except Exception as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(plan, ensure_ascii=False, indent=2 if args.json else None))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
