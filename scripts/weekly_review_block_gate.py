#!/usr/bin/env python3
"""Gate helper for idempotent weekly_review.md block replacement."""

from __future__ import annotations

import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^### (?P<week>\d{4}-W\d{2})(?: \((?P<range>[^)]*)\))?\s*$", re.MULTILINE)
CANONICAL_RE = re.compile(r"^### (?P<week>\d{4}-W\d{2}) \(\d{4}-\d{2}-\d{2} ~ \d{4}-\d{2}-\d{2}\)\s*$")


def replace_canonical_week_block(text: str, week: str, block: str) -> str:
    """Replace exactly one canonical block for week; preserve manual-note blocks."""
    matches = list(HEADING_RE.finditer(text))
    canonical = []
    for idx, match in enumerate(matches):
        if match.group("week") != week:
            continue
        line = text[match.start() : text.find("\n", match.start())]
        if CANONICAL_RE.match(line):
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
            canonical.append((match.start(), end))

    normalized = block.strip() + "\n"
    if not canonical:
        return text.rstrip() + "\n\n" + normalized

    start, end = canonical[0]
    updated = text[:start] + normalized
    cursor = end
    for dup_start, dup_end in canonical[1:]:
        updated += text[cursor:dup_start]
        cursor = dup_end
    updated += text[cursor:]
    return updated


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: weekly_review_block_gate.py weekly_review.md YYYY-Www block.md", file=sys.stderr)
        return 2
    path = Path(argv[1])
    week = argv[2]
    block = Path(argv[3]).read_text()
    before = path.read_text()
    after = replace_canonical_week_block(before, week, block)
    count = sum(
        1
        for line in after.splitlines()
        if line.startswith(f"### {week} (") and CANONICAL_RE.match(line)
    )
    if count != 1:
        print(f"FAIL canonical block count for {week}: {count}", file=sys.stderr)
        return 1
    print(f"PASS canonical block count for {week}: 1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
