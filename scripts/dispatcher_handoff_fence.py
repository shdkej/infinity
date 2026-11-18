#!/usr/bin/env python3
"""Private per-Intent durable fence for recurring dispatcher handoffs.

The guard's per-run task ID is not a logical-work dedupe key. Reserve all
candidate Intent IDs before invoking a child. No wall-clock expiry applies.
"""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys


def _db(state_dir: str | Path) -> sqlite3.Connection:
    root = Path(state_dir)
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = root / "dispatcher-handoff-fence.sqlite3"
    existed = path.exists()
    db = sqlite3.connect(path, timeout=5)
    os.chmod(path, 0o600)
    db.execute("PRAGMA synchronous=FULL")
    db.execute("""CREATE TABLE IF NOT EXISTS handoffs (
        intent_id TEXT PRIMARY KEY, run_id TEXT NOT NULL, task_id TEXT NOT NULL,
        canonical_sha TEXT NOT NULL, status TEXT NOT NULL,
        updated_at TEXT NOT NULL)""")
    db.commit()
    if not existed:
        fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
    return db


def reserve(state_dir: str | Path, run_id: str, task_id: str,
            canonical_sha: str, intent_ids: list[str]) -> bool:
    if not intent_ids or len(set(intent_ids)) != len(intent_ids) or not all(intent_ids):
        raise ValueError("nonempty unique Intent IDs required")
    with closing(_db(state_dir)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        blocked = db.execute(
            f"SELECT 1 FROM handoffs WHERE intent_id IN ({','.join('?' for _ in intent_ids)}) AND status='pending' LIMIT 1",
            intent_ids,
        ).fetchone()
        if blocked:
            return False
        stamp = datetime.now(timezone.utc).isoformat()
        for intent_id in intent_ids:
            db.execute("""INSERT INTO handoffs(intent_id,run_id,task_id,canonical_sha,status,updated_at)
                          VALUES(?,?,?,?,'pending',?) ON CONFLICT(intent_id) DO UPDATE SET
                          run_id=excluded.run_id, task_id=excluded.task_id,
                          canonical_sha=excluded.canonical_sha, status='pending',
                          updated_at=excluded.updated_at""",
                       (intent_id, run_id, task_id, canonical_sha, stamp))
    return True


def _followups_proved(repo: Path | None, old_sha: str, new_sha: str,
                     candidates: list[dict]) -> bool:
    if not repo or not candidates or not all(re.fullmatch(r"[0-9a-f]{40,64}", s) for s in (old_sha, new_sha)):
        return False
    def registry_ids(sha: str) -> set[str]:
        text = subprocess.check_output(["git", "show", f"{sha}:INTENTS.yaml"],
                                       cwd=repo, text=True, stderr=subprocess.DEVNULL)
        return set(re.findall(r"(?m)^\s*- id:\s*([^\s#]+)", text))
    old, new = registry_ids(old_sha), registry_ids(new_sha)
    for candidate in candidates:
        raw = str(candidate.get("follow_up_intent_ids") or "").strip()
        ids = [value for value in re.split(r"[\s,\[\]]+", raw) if value]
        if not ids or any(not re.fullmatch(r"[A-Za-z0-9._-]+", value) for value in ids):
            return False
        if not all(value in new and value not in old for value in ids):
            return False
    return True


def resolve(state_dir: str | Path, run_id: str, outcome: str,
            receipt: Path | None = None, exit_code: int | None = None,
            post_plan: Path | None = None, remote_sha: str | None = None,
            prelaunch: bool = False, repo: Path | None = None) -> bool:
    with closing(_db(state_dir)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        rows = db.execute("SELECT intent_id, task_id, canonical_sha FROM handoffs WHERE run_id=? AND status='pending'",
                          (run_id,)).fetchall()
        if not rows:
            return False
        task_ids = {row[1] for row in rows}
        if len(task_ids) != 1:
            return False
        if outcome == "nonstarted" and prelaunch and receipt is None:
            pass  # caller has not entered the route invocation; false negatives remain pending
        else:
            try:
                evidence = json.loads(receipt.read_text()) if receipt else {}
            except (OSError, ValueError):
                return False
            if evidence.get("task_id") not in task_ids:
                return False
            if outcome == "nonstarted":
                if exit_code != 4 or evidence.get("state") != "busy":
                    return False
            elif outcome == "verified":
                if exit_code != 0 or evidence.get("state") != "completed" or not post_plan:
                    return False
                try:
                    plan = json.loads(post_plan.read_text())
                except (OSError, ValueError):
                    return False
                sha = plan.get("canonical_sha")
                if not sha or sha != remote_sha or any(sha == row[2] for row in rows):
                    return False
                ids = {row[0] for row in rows}
                if ids & {str(c.get("intent_id")) for name in (
                    "resume_candidates", "handoff_candidates", "invalid_state")
                          for c in plan.get(name, [])}:
                    return False
                followups = [c for c in plan.get("follow_up_candidates", [])
                             if str(c.get("intent_id")) in ids]
                if followups and not _followups_proved(repo, rows[0][2], sha, followups):
                    return False
            else:
                return False
        db.execute("UPDATE handoffs SET status=?,updated_at=? WHERE run_id=? AND status='pending'",
                   (outcome, datetime.now(timezone.utc).isoformat(), run_id))
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", required=True)
    sub = parser.add_subparsers(dest="action", required=True)
    res = sub.add_parser("reserve")
    res.add_argument("--run-id", required=True)
    res.add_argument("--task-id", required=True)
    res.add_argument("--canonical-sha", required=True)
    res.add_argument("intent_ids", nargs="+")
    done = sub.add_parser("resolve")
    done.add_argument("--run-id", required=True)
    done.add_argument("--outcome", choices=("verified", "nonstarted"), required=True)
    done.add_argument("--receipt", type=Path)
    done.add_argument("--exit-code", type=int)
    done.add_argument("--post-plan", type=Path)
    done.add_argument("--remote-sha")
    done.add_argument("--repo", type=Path)
    done.add_argument("--prelaunch", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.action == "reserve":
            ok = reserve(args.state_dir, args.run_id, args.task_id, args.canonical_sha, args.intent_ids)
            return 0 if ok else 3
        ok = resolve(args.state_dir, args.run_id, args.outcome, args.receipt,
                     args.exit_code, args.post_plan, args.remote_sha, args.prelaunch, args.repo)
        return 0 if ok else 3
    except (OSError, sqlite3.Error, ValueError, subprocess.CalledProcessError):
        print("handoff fence could not establish proof", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
