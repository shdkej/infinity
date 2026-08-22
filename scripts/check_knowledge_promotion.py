#!/usr/bin/env python3
"""Validate that an archived Infinity intent has a closed Knowledge Lab decision."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_LAB = ROOT.parent
ARCHIVE = ROOT / "intents" / "archive"


def field(text: str, name: str) -> str | None:
    match = re.search(rf"(?m)^-\s*{re.escape(name)}:\s*(.*?)\s*$", text)
    return match.group(1).strip() if match else None


def targets(value: str | None) -> list[str]:
    if not value or value in {"[]", "-", "none", "null"}:
        return []
    value = value.strip("[]")
    return [part.strip().strip("'\"") for part in value.split(",") if part.strip()]


def check(intent_id: str) -> list[str]:
    path = ARCHIVE / f"{intent_id}.md"
    if not path.exists():
        return [f"archive not found: {path}"]
    text = path.read_text(encoding="utf-8")
    status = field(text, "knowledge_status")
    decision = field(text, "knowledge_decision")
    reflection = field(text, "knowledge_reflection")
    target_paths = targets(field(text, "knowledge_targets"))
    errors: list[str] = []
    if status not in {"raw", "promoted", "superseded"}:
        errors.append("knowledge_status must be raw, promoted, or superseded (candidate cannot be archived)")
    if decision not in {"promote", "retain_in_infinity", "supersede"}:
        errors.append("knowledge_decision must be promote, retain_in_infinity, or supersede")
    if not reflection or reflection in {"null", "TODO", "-"}:
        errors.append("knowledge_reflection must explain the decision")
    if decision == "promote" and status != "promoted":
        errors.append("promote requires knowledge_status: promoted")
    if decision == "retain_in_infinity" and status != "raw":
        errors.append("retain_in_infinity requires knowledge_status: raw")
    if decision == "supersede" and status != "superseded":
        errors.append("supersede requires knowledge_status: superseded")
    if status == "promoted" and not target_paths:
        errors.append("promoted archive must list at least one knowledge_targets path")
    for target in target_paths:
        target_path = (KNOWLEDGE_LAB / target).resolve()
        if KNOWLEDGE_LAB not in target_path.parents and target_path != KNOWLEDGE_LAB:
            errors.append(f"knowledge target escapes Knowledge Lab: {target}")
        elif not target_path.exists():
            errors.append(f"knowledge target does not exist: {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("intent_id")
    args = parser.parse_args()
    errors = check(args.intent_id)
    if errors:
        print(f"FAIL {args.intent_id}")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS {args.intent_id}: knowledge decision closed and targets verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
