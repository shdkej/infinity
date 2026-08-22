#!/usr/bin/env python3
"""Validate that an archived Infinity intent has a closed Knowledge Lab decision."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_LAB = ROOT.parent
ARCHIVE = ROOT / "intents" / "archive"
INGEST_INDEX = KNOWLEDGE_LAB / "ingest" / "INDEX.md"


def field(text: str, name: str) -> str | None:
    match = re.search(rf"(?m)^-\s*{re.escape(name)}:\s*(.*?)\s*$", text)
    return match.group(1).strip() if match else None


def targets(value: str | None) -> list[str]:
    if not value or value in {"[]", "-", "none", "null"}:
        return []
    value = value.strip("[]")
    return [part.strip().strip("'\"") for part in value.split(",") if part.strip()]


def ingest_entry(intent_id: str) -> tuple[str | None, str | None, list[str]]:
    """Read the root Knowledge Lab ingest entry for one Infinity archive."""
    if not INGEST_INDEX.exists():
        return None, None, []
    text = INGEST_INDEX.read_text(encoding="utf-8")
    match = re.search(
        rf"(?ms)^### [^\n]*(?:{re.escape(intent_id)}|intents/archive/{re.escape(intent_id)}\.md)[^\n]*\n"
        rf"(?:(?!^### ).)*",
        text,
    )
    if not match:
        return None, None, []
    block = match.group(0)
    status = field(block, "status")
    source = field(block, "source")
    target = field(block, "target")
    return status, source, [] if not target or target == "none" else targets(target)


def check(intent_id: str) -> list[str]:
    path = ARCHIVE / f"{intent_id}.md"
    if not path.exists():
        return [f"archive not found: {path}"]
    text = path.read_text(encoding="utf-8")
    status = field(text, "knowledge_status")
    decision = field(text, "knowledge_decision")
    reflection = field(text, "knowledge_reflection")
    commit = field(text, "knowledge_commit")
    target_paths = targets(field(text, "knowledge_targets"))
    ingest_status, ingest_source, ingest_targets = ingest_entry(intent_id)
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
    if status in {"promoted", "superseded"} and not target_paths:
        errors.append(f"{status} archive must list at least one knowledge_targets path")
    if status in {"promoted", "superseded"} and not commit:
        errors.append(f"{status} archive must list the Knowledge Lab commit in knowledge_commit")
    if status in {"promoted", "superseded"}:
        expected_source = f"infinity/intents/archive/{intent_id}.md"
        if ingest_status is None:
            errors.append(f"{intent_id} is missing from root ingest index: {INGEST_INDEX}")
        elif ingest_status != "integrated":
            errors.append(f"{intent_id} ingest status must be integrated, got: {ingest_status}")
        if ingest_source != expected_source:
            errors.append(f"{intent_id} ingest source must be {expected_source}, got: {ingest_source}")
        for target in target_paths:
            if target not in ingest_targets:
                errors.append(f"{intent_id} ingest entry must list knowledge target: {target}")
    for target in target_paths:
        target_path = (KNOWLEDGE_LAB / target).resolve()
        if KNOWLEDGE_LAB not in target_path.parents and target_path != KNOWLEDGE_LAB:
            errors.append(f"knowledge target escapes Knowledge Lab: {target}")
        elif not target.startswith("agent-wiki/content/docs/"):
            errors.append(f"knowledge target must be an agent-wiki content page: {target}")
        elif not target_path.exists():
            errors.append(f"knowledge target does not exist: {target}")
    if commit:
        wiki_repo = KNOWLEDGE_LAB / "agent-wiki"
        result = subprocess.run(
            ["git", "-C", str(wiki_repo), "cat-file", "-e", f"{commit}^{{commit}}"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            errors.append(f"knowledge_commit is not present in agent-wiki: {commit}")
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
