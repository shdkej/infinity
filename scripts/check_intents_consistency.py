#!/usr/bin/env python3
"""Check INTENTS.md lane consistency for dashboard/recap consumers."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from intent_registry import ARCHIVE_DIR, load_registry, archive_entries


CLOSED_RE = re.compile(
    r"\b(completed|resolved|done|archived|closed|canceled|cancelled|rejected|approved|failed)\b",
    re.I,
)
COMMENT_RE = re.compile(r"<!--\s*([\s\S]+?)\s*-->")
CARD_RE = re.compile(r"^###\s+\[([^\]]+)\][^\n]*(.*?)(?=^###\s+\[|\Z)", re.M | re.S)
FIELD_RE = re.compile(r"^\s*-\s+([^:\n]+):\s*(.*?)\s*$", re.M)
ID_RE = re.compile(r"([a-z][a-z0-9]*(?:-[a-z0-9]+)*-\d+)\b")
DATE_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2}(?:[T\s](?:\d{2}:\d{2}(?::\d{2})?|\d{4}(?:\d{2})?)Z?)?)"
)


def split_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {"__preamble__": []}
    current = "__preamble__"
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        else:
            sections.setdefault(current, []).append(line)
    return {k: "\n".join(v) for k, v in sections.items()}


def date_key(value: str) -> tuple[int, int, int, int, int, int]:
    match = re.match(
        r"(\d{4})-(\d{2})-(\d{2})(?:[T\s](?:(\d{2}):(\d{2})(?::(\d{2}))?|(\d{2})(\d{2})(\d{2})?))?",
        value or "",
    )
    if not match:
        return (0, 0, 0, 0, 0, 0)
    year, month, day, hour, minute, second, compact_hour, compact_minute, compact_second = match.groups()
    return (
        int(year),
        int(month),
        int(day),
        int(hour or compact_hour or 0),
        int(minute or compact_minute or 0),
        int(second or compact_second or 0),
    )


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("INTENTS.yaml")
    data = load_registry(path)
    errors: list[str] = []

    seen: set[str] = set()
    for lane in ("inbox", "active", "waiting"):
        for item in data.get("lanes", {}).get(lane, []):
            intent_id = str(item.get("id") or "")
            title = str(item.get("title") or "")
            if not intent_id or intent_id in seen: errors.append(f"{lane}: duplicate or missing id: {intent_id}")
            seen.add(intent_id)
            if not title or title != str(item.get("task_name") or ""):
                errors.append(f"{lane}: {intent_id} requires matching title/task_name")
            if title.startswith("#") or title.startswith("[") or re.match(r"^-\s*\w+\s*:", title):
                errors.append(f"{lane}: {intent_id} has malformed title")
            missing = [key for key in ("notification_channel", "notification_target") if not item.get(key)]
            if missing: errors.append(f"{lane}: {intent_id} missing terminal notification field(s): {', '.join(missing)}")
            intent_fields = ("user_intent", "desired_outcome", "out_of_scope", "success_evidence")
            missing_intent = [key for key in intent_fields if not str(item.get(key) or "").strip()]
            if missing_intent:
                errors.append(f"{lane}: {intent_id} missing user-intent contract field(s): {', '.join(missing_intent)}")
    for item in archive_entries():
        intent_id = str(item.get("id") or "")
        if intent_id in seen: errors.append(f"Archive: duplicate id {intent_id}")
        seen.add(intent_id)
        if not (item.get("completed_at") or item.get("archived_at") or item.get("date")):
            errors.append(f"Archive: {intent_id} missing archive date field")
        if str(item.get("title") or "") != str(item.get("task_name") or ""):
            errors.append(f"Archive: {intent_id} requires matching title/task_name")

    if errors:
        for err in errors: print(err, file=sys.stderr)
        return 1
    print("INTENTS.yaml consistency OK")
    return 0

    # Legacy parser retained below for historical fixtures only.

    headers = re.findall(r"^##\s+(.+?)\s*$", text, re.M)
    seen_headers: set[str] = set()
    for header in headers:
        if header in seen_headers:
            errors.append(f"Duplicate lane section: ## {header}")
        seen_headers.add(header)

    for lane in ("Inbox", "Active", "Waiting"):
        for comment in COMMENT_RE.finditer(sections.get(lane, "")):
            body = comment.group(1).strip()
            id_match = ID_RE.match(body)
            if id_match and CLOSED_RE.search(body):
                errors.append(f"{lane}: closed comment must move to Archive: {id_match.group(1)}")

        # The dispatcher has no access to the original chat context.  An open
        # card without this pair could reach a terminal state silently, so make
        # the omission a pre-push error.  Legacy Archive records stay readable.
        for card in CARD_RE.finditer(sections.get(lane, "")):
            intent_id = card.group(1)
            fields = {key.strip(): value.strip() for key, value in FIELD_RE.findall(card.group(2))}
            missing = [key for key in ("notification_channel", "notification_target") if not fields.get(key)]
            if missing:
                errors.append(f"{lane}: {intent_id} missing terminal notification field(s): {', '.join(missing)}")

    archive_items: list[tuple[tuple[int, int, int, int, int, int], str]] = []
    for comment in COMMENT_RE.finditer(sections.get("Archive", "")):
        body = comment.group(1).strip()
        id_match = ID_RE.match(body)
        if not id_match:
            continue
        date_match = DATE_RE.search(body)
        completed = date_key(date_match.group(1) if date_match else "")
        intent_id = id_match.group(1)
        archive_items.append((completed, intent_id))

    for card in CARD_RE.finditer(sections.get("Archive", "")):
        intent_id = card.group(1)
        fields = {key.strip(): value.strip() for key, value in FIELD_RE.findall(card.group(2))}
        if not (fields.get("completed_at") or fields.get("archived_at")):
            errors.append(f"Archive: {intent_id} missing completed_at/archived_at for dashboard ordering")

    for prev, cur in zip(archive_items, archive_items[1:]):
        if (prev[0], prev[1]) < (cur[0], cur[1]):
            errors.append(f"Archive order broken: {prev[1]} appears before newer {cur[1]}")

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    print("INTENTS.md consistency OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
