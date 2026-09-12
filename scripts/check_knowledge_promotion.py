#!/usr/bin/env python3
"""Validate that an archived Infinity intent has a closed Knowledge Lab decision."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_LAB = ROOT.parent
ARCHIVE = KNOWLEDGE_LAB / "source" / "infinity" / "archive"
INFINITY_ARCHIVE = ROOT / "intents" / "archive"
INGEST_INDEX = KNOWLEDGE_LAB / "ingest" / "INDEX.md"
WIKI_LOG = KNOWLEDGE_LAB / "agent-wiki" / "content" / "docs" / "log.mdx"


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


def context_log_errors(intent_id: str, text: str) -> list[str]:
    """v2 packs require an append-only query receipt, even without promotion."""
    context_path = field(text, "context_pack") or field(text, "source_context_pack")
    if not context_path or not (ROOT / context_path).is_file():
        return []  # legacy archive detail; normal trace validation still applies.
    try:
        pack = json.loads((ROOT / context_path).read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ["context_pack is invalid JSON"]
    if not pack.get("selected_context_required"):
        return []
    receipt = field(text, "knowledge_log")
    expected = f"agent-wiki/content/docs/log.mdx#{intent_id}"
    if receipt != expected:
        return [f"Context Pack v2 requires knowledge_log: {expected}"]
    if not WIKI_LOG.is_file():
        return [f"Knowledge Lab query log is missing: {WIKI_LOG}"]
    heading = re.search(rf"(?m)^## [^\n]*\[{re.escape(intent_id)}\][^\n]*$", WIKI_LOG.read_text(encoding="utf-8"))
    if not heading:
        return [f"Knowledge Lab query log has no heading tagged [{intent_id}]"]
    end = re.search(r"(?m)^## ", WIKI_LOG.read_text(encoding="utf-8")[heading.end():])
    entry = WIKI_LOG.read_text(encoding="utf-8")[heading.start(): heading.end() + (end.start() if end else len(WIKI_LOG.read_text(encoding="utf-8")[heading.end():]))]
    pages = [item.get("path") for item in pack.get("selected_context", []) if isinstance(item, dict)]
    missing = [page for page in pages if isinstance(page, str) and page not in entry]
    return [f"Knowledge Lab query log entry omits selected_context path(s): {', '.join(missing)}"] if missing else []


def check(intent_id: str) -> list[str]:
    # Retained execution records deliberately live only in the Infinity repo;
    # promoted/superseded records additionally have the Knowledge Lab source.
    infinity_path = INFINITY_ARCHIVE / f"{intent_id}.md"
    path = infinity_path if infinity_path.exists() else ARCHIVE / f"{intent_id}.md"
    if not path.exists():
        return [f"archive not found: {path}"]
    text = path.read_text(encoding="utf-8")
    status = field(text, "knowledge_status")
    decision = field(text, "knowledge_decision")
    reflection = field(text, "knowledge_reflection")
    commit = field(text, "knowledge_commit")
    ingest_status, ingest_source, ingest_targets = ingest_entry(intent_id)
    errors: list[str] = []
    errors.extend(context_log_errors(intent_id, text))
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
    if status in {"promoted", "superseded"}:
        expected_source = f"source/infinity/archive/{intent_id}.md"
        if ingest_status is None:
            errors.append(f"{intent_id} is missing from root ingest index: {INGEST_INDEX}")
        elif ingest_status != "integrated":
            errors.append(f"{intent_id} ingest status must be integrated, got: {ingest_status}")
        if ingest_source != expected_source:
            errors.append(f"{intent_id} ingest source must be {expected_source}, got: {ingest_source}")
        # agent-wiki is an independent consumer. Its files and commits are
        # intentionally outside this gate; ingest only owns registration and
        # the decision to retain/promote the Infinity result.
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
    print(f"PASS {args.intent_id}: knowledge decision closed and ingest entry verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
