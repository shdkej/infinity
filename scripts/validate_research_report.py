#!/usr/bin/env python3
"""Reject thin or visually incomplete final HTML reports for research intents."""

from __future__ import annotations

import argparse
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


def visible_text(html: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", html))).strip()


class LayoutParser(HTMLParser):
    """Capture rendered-structure signals without trusting literal strings."""

    def __init__(self) -> None:
        super().__init__()
        self.rich_v1 = False
        self.viewport = False
        self.stack: list[tuple[str, set[str]]] = []
        self.axis_roles: set[str] = set()
        self.callout_in_sheet = False
        self.details_in_sheet = 0
        self.summaries_in_details = 0
        self._in_style = False
        self.styles: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html" and values.get("data-infinity-report") == "rich-v1":
            self.rich_v1 = True
        if tag == "meta" and values.get("name", "").lower() == "viewport":
            self.viewport = True
        classes = set((values.get("class") or "").split())
        inside_sheet = any("sheet" in ancestor_classes for _, ancestor_classes in self.stack)
        inside_details = any(ancestor_tag == "details" for ancestor_tag, _ in self.stack)
        if tag == "style":
            self._in_style = True
        if inside_sheet and {"axis", "ax1"}.issubset(classes):
            self.axis_roles.add("ax1")
        if inside_sheet and {"axis", "ax2"}.issubset(classes):
            self.axis_roles.add("ax2")
        if inside_sheet and "callout" in classes:
            self.callout_in_sheet = True
        if tag == "details" and inside_sheet:
            self.details_in_sheet += 1
        if tag == "summary" and inside_sheet and inside_details:
            self.summaries_in_details += 1
        self.stack.append((tag, classes))

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self._in_style = False
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data: str) -> None:
        if self._in_style:
            self.styles.append(data)


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

    # Research reports are read in the Infinity dashboard, not merely parsed as
    # HTML. Require the shared rich template's responsive, hierarchy-bearing
    # structure so a bare collection of headings cannot pass as a final report.
    layout = LayoutParser()
    layout.feed(html)
    if not layout.rich_v1:
        errors.append("missing rich report marker: html[data-infinity-report=rich-v1]")
    if not layout.viewport:
        errors.append("missing responsive viewport metadata")
    if layout.axis_roles != {"ax1", "ax2"}:
        errors.append("rich report needs both conclusion axes inside the sheet")
    if not layout.callout_in_sheet:
        errors.append("rich report needs a callout inside the sheet")
    styles = "".join(layout.styles)
    if "@media (max-width:640px)" not in styles:
        errors.append("missing 390px-oriented responsive layout rule")
    if layout.details_in_sheet < 2 or layout.summaries_in_details < 2:
        errors.append("rich research report needs an open reading surface and a separate detail surface")
    if re.search(r"{{[A-Z0-9_]+}}", html):
        errors.append("rich report contains unresolved template placeholders")

    if errors:
        print("FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS research report quality: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
