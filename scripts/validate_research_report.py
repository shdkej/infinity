#!/usr/bin/env python3
"""Reject thin final HTML reports for research intents."""

from __future__ import annotations

import argparse
import re
import sys
from html import unescape
from pathlib import Path


def visible_text(html: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", html))).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    html = args.report.read_text(encoding="utf-8")
    text = visible_text(html)
    errors: list[str] = []

    required = ("핵심 내용", "핵심 발견", "근거 · 소스", "다음 판단")
    for marker in required:
        if marker not in text:
            errors.append(f"missing required research section: {marker}")
    findings = re.findall(r"<li\b[^>]*>(.*?)</li>", html, flags=re.I | re.S)
    substantial = [visible_text(item) for item in findings if len(visible_text(item)) >= 70]
    if len(substantial) < 3:
        errors.append("research report needs at least 3 substantial, decision-useful findings")
    if len(re.findall(r"<a\b[^>]*href=", html, flags=re.I)) < 3:
        errors.append("research report needs at least 3 linked sources")
    if len(text) < 1400:
        errors.append("research report body is too thin; synthesize the findings, comparison, limits, and next decision")

    if errors:
        print("FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS research report quality: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
