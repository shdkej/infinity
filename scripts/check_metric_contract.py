#!/usr/bin/env python3
"""Validate the metric contract for non-simple open Infinity intents."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ENTRY_RE = re.compile(r"^### \[([^\]]+)\]", re.M)


def fields(entry: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in entry.splitlines():
        match = re.match(r"^-\s+([a-z][a-z0-9_]*)\s*:\s*(.*?)\s*$", line)
        if match:
            result[match.group(1)] = match.group(2)
    return result


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("INTENTS.md")
    text = path.read_text()
    errors: list[str] = []
    sections = re.split(r"^## ", text, flags=re.M)
    for section in sections:
        if not section.startswith(("Inbox\n", "Active\n", "Waiting\n")):
            continue
        lane = section.splitlines()[0]
        matches = list(ENTRY_RE.finditer(section))
        for index, match in enumerate(matches):
            entry = section[match.start():matches[index + 1].start() if index + 1 < len(matches) else len(section)]
            data = fields(entry)
            if not data.get("goal") or not data.get("success_criteria"):
                continue
            intent_id = match.group(1)
            for required in ("metric_question", "metric_signal", "metric_decision_rule"):
                if not data.get(required):
                    errors.append(f"{lane}: {intent_id} missing {required}")
            rule = data.get("metric_decision_rule", "")
            if rule and not {"continue", "change", "hold"}.intersection(re.findall(r"\b(?:continue|change|hold)\b", rule)):
                errors.append(f"{lane}: {intent_id} metric_decision_rule must include continue/change/hold")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Metric contract OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
