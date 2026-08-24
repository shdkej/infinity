#!/usr/bin/env python3
"""Check INTENTS.md lane consistency for dashboard/recap consumers."""

from __future__ import annotations

import re
import sys
from pathlib import Path


CLOSED_RE = re.compile(
    r"\b(completed|resolved|done|archived|closed|canceled|cancelled|rejected|approved|failed)\b",
    re.I,
)
COMMENT_RE = re.compile(r"<!--\s*([\s\S]+?)\s*-->")
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
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("INTENTS.md")
    text = path.read_text()
    sections = split_sections(text)
    errors: list[str] = []

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

    archive_items: list[tuple[tuple[int, int, int, int, int, int], str]] = []
    for comment in COMMENT_RE.finditer(sections.get("Archive", "")):
        body = comment.group(1).strip()
        id_match = ID_RE.match(body)
        if not id_match:
            continue
        date_match = DATE_RE.search(body)
        archive_items.append((date_key(date_match.group(1) if date_match else ""), id_match.group(1)))

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
