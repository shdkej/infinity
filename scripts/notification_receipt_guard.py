#!/usr/bin/env python3
"""Durable monotonic receipt checkpoint beside the mutable notification ledger.

Initialize explicitly from a SHA-verified intake baseline. A missing checkpoint
is never recreated during a notification cycle. Record the attempt *before*
any external transport and fail closed when the ledger loses a recorded key.
"""
from __future__ import annotations

import hashlib
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3
import sys

from verify_hermes_receipt import STABLE_FIELDS, verify as verify_intake


def _deliveries(ledger: dict) -> dict:
    rows = ledger["deliveries"]
    if not isinstance(rows, dict) or not isinstance(ledger.get("observed_intents"), dict):
        raise ValueError("invalid receipt ledger")
    return rows


def _compatible(old: dict, new: dict) -> bool:
    if not isinstance(old, dict) or not isinstance(new, dict):
        return False
    if any(new.get(key) != old.get(key) for key in STABLE_FIELDS):
        return False
    allowed = {
        "sent": {"sent"}, "delivery_unknown": {"delivery_unknown", "superseded"},
        "superseded": {"superseded"},
        "claimed": {"claimed", "sent", "delivery_unknown", "failed_before_acceptance", "superseded"},
        "failed_before_acceptance": {"failed_before_acceptance", "claimed", "sent", "delivery_unknown", "superseded"},
    }
    state = old.get("state")
    if not isinstance(state, str) or new.get("state") not in allowed.get(state, {state}):
        return False
    attempted = old.get("attempt_started_at")
    if attempted and attempted != new.get("attempt_started_at"):
        # The notifier permits an explicitly classified pre-acceptance failure
        # to retry with a new attempt marker; all other resets are ambiguous.
        if state != "failed_before_acceptance" or old.get("failure_class") not in {
            "command_start_failed", "run_timeout"}:
            return False
    return True


def _connect(path: Path) -> sqlite3.Connection:
    if not path.is_file():
        raise ValueError("receipt checkpoint missing; do not auto-initialize")
    db = sqlite3.connect(path, timeout=5)
    db.execute("PRAGMA synchronous=FULL")
    if db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='receipts'").fetchone() is None:
        db.close()
        raise ValueError("receipt checkpoint corrupt")
    return db


def _verify(db: sqlite3.Connection, ledger: dict) -> None:
    rows = _deliveries(ledger)
    if db.execute("SELECT value FROM metadata WHERE key='intake_sha'").fetchone() is None:
        raise ValueError("missing intake proof")
    for key, raw in db.execute("SELECT receipt_key, receipt_json FROM receipts"):
        if key not in rows or not _compatible(json.loads(raw), rows[key]):
            raise ValueError("receipt continuity unverified")


def initialize(path: Path, baseline: Path, current: Path, expected_sha: str) -> None:
    if path.exists():
        raise ValueError("checkpoint exists; refusing overwrite")
    if not verify_intake(baseline, current, expected_sha):
        raise ValueError("intake receipt continuity unverified")
    ledger = json.loads(current.read_bytes())
    rows = _deliveries(ledger)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)
    os.close(fd)
    try:
        with closing(sqlite3.connect(path, timeout=5)) as db, db:
            db.execute("PRAGMA synchronous=FULL")
            db.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY,value TEXT NOT NULL)")
            db.execute("CREATE TABLE receipts (receipt_key TEXT PRIMARY KEY,receipt_json TEXT NOT NULL)")
            db.execute("INSERT INTO metadata VALUES ('intake_sha',?)", (expected_sha,))
            db.executemany("INSERT INTO receipts VALUES (?,?)",
                           ((key, json.dumps(value, sort_keys=True)) for key, value in rows.items()))
        dir_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        path.unlink(missing_ok=True)
        raise


def verify(path: Path, ledger: dict) -> None:
    with closing(_connect(path)) as db, db:
        _verify(db, ledger)


def record(path: Path, ledger: dict) -> None:
    with closing(_connect(path)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        _verify(db, ledger)
        db.executemany("INSERT OR REPLACE INTO receipts VALUES (?,?)",
                       ((key, json.dumps(value, sort_keys=True))
                        for key, value in _deliveries(ledger).items()))


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 5 and argv[0] == "init":
            initialize(Path(argv[1]), Path(argv[2]), Path(argv[3]), argv[4])
        elif len(argv) == 3 and argv[0] in {"verify", "record"}:
            ledger = json.loads(Path(argv[2]).read_bytes())
            (verify if argv[0] == "verify" else record)(Path(argv[1]), ledger)
        else:
            return 2
        return 0
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error):
        print("receipt checkpoint continuity unverified", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
