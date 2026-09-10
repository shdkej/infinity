#!/usr/bin/env python3
"""Regression tests for the rich research report contract."""

import tempfile
import unittest
from pathlib import Path

import validate_research_report as validator


FINDING = "이 발견은 사용자의 다음 판단에 직접 연결되는 구체적 근거와 한계를 함께 설명합니다. " * 8


def report(body: str) -> str:
    return f'''<!doctype html><html lang="ko" data-infinity-report="rich-v1"><head>
    <meta name="viewport" content="width=device-width,initial-scale=1"><style>
    .sheet{{max-width:720px}} @media (max-width:640px){{.sheet{{padding:12px}}}}
    </style></head><body>{body}<h2>핵심 내용</h2><h2>핵심 발견</h2>
    <ol><li>{FINDING}</li><li>{FINDING}</li><li>{FINDING}</li></ol>
    <h2>근거 · 소스</h2><a href="https://a.example">A</a><a href="https://b.example">B</a><a href="https://c.example">C</a>
    <h2>다음 판단</h2><p>{FINDING}</p></body></html>'''


def errors(html: str) -> list[str]:
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp) / "report.html"
        path.write_text(html, encoding="utf-8")
        original = __import__("sys").argv
        try:
            __import__("sys").argv = ["validator", str(path)]
            return_code = validator.main()
        finally:
            __import__("sys").argv = original
    return ["validator returned failure"] if return_code else []


class RichReportContractTest(unittest.TestCase):
    def test_rich_template_structure_passes(self):
        body = '''<main class="sheet"><div class="axis ax1">맥락</div><div class="axis ax2">결론</div>
        <div class="callout">추천</div><details open><summary>핵심</summary>본문</details>
        <details><summary>한계</summary>상세</details></main>'''
        self.assertEqual(errors(report(body)), [])

    def test_bare_html_fails(self):
        self.assertNotEqual(errors("<html><body>bare</body></html>"), [])

    def test_detached_layout_markers_fail(self):
        body = '''<div class="sheet"></div><div class="axis ax1"></div><div class="axis ax2"></div>
        <div class="callout"></div><details><summary>one</summary></details><details><summary>two</summary></details>'''
        self.assertNotEqual(errors(report(body)), [])


if __name__ == "__main__":
    unittest.main()
