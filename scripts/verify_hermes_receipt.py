#!/usr/bin/env python3
"""Check immutable intake SHA and original receipt continuity, without writing.

The baseline is a private frozen copy of the received operational ledger. The
runtime ledger may gain new receipts or supersede an uncertain one, but may not
lose or reset a historical delivery. This is a guard, not cutover permission.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


STABLE_FIELDS = ("destination", "fingerprint", "intent_id", "terminal_state")


def verify(baseline: Path, current: Path, expected_sha: str) -> bool:
    try:
        raw = baseline.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected_sha:
            return False
        old, new = json.loads(raw), json.loads(current.read_bytes())
        old_deliveries, new_deliveries = old["deliveries"], new["deliveries"]
        if not isinstance(old_deliveries, dict) or not isinstance(new_deliveries, dict):
            return False
        if not isinstance(new.get("observed_intents"), dict):
            return False
        for key, old_receipt in old_deliveries.items():
            new_receipt = new_deliveries.get(key)
            if not isinstance(old_receipt, dict) or not isinstance(new_receipt, dict):
                return False
            old_state, new_state = old_receipt.get("state"), new_receipt.get("state")
            if not isinstance(old_state, str) or not isinstance(new_state, str):
                return False
            allowed = {"sent": {"sent"}, "superseded": {"superseded"},
                       "delivery_unknown": {"delivery_unknown", "superseded"}}
            if new_state not in allowed.get(old_state, {old_state}):
                return False
            if any(new_receipt.get(field) != old_receipt.get(field) for field in STABLE_FIELDS):
                return False
        return True
    except (OSError, ValueError, TypeError, KeyError):
        return False


def main(argv: list[str]) -> int:
    if len(argv) != 3 or not verify(Path(argv[0]), Path(argv[1]), argv[2]):
        print("receipt continuity unverified", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
