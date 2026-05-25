#!/usr/bin/env python3
"""HTML 리포트(reports/{id}/{ts}.html)를 텔레그램용 평문으로 변환한다.

heartbeat 리포트가 .md → .html 로 바뀌면서 알림에 태그/CSS가 그대로 노출되던 문제를
해결하기 위한 도구. 템플릿별로 결론 2축 마커(.axis/.lead 등)가 달라 특정 클래스에
의존하지 않고, head/style/script 를 제거한 뒤 태그를 벗겨 읽히는 텍스트만 남긴다.

Usage: python3 html_report_to_text.py <report.html> [max_lines]
출력: 제목 한 줄 + 빈 줄 + 본문 상위 N줄(기본 14)
"""
import sys
import re
import html


def extract(path: str, max_lines: int = 14) -> str:
    src = open(path, encoding="utf-8").read()

    m = re.search(r"<title>(.*?)</title>", src, re.S | re.I)
    title = html.unescape(re.sub(r"\s+", " ", m.group(1)).strip()) if m else ""

    body = re.sub(r"<head.*?</head>", "", src, flags=re.S | re.I)
    body = re.sub(r"<(style|script)[^>]*>.*?</\1>", "", body, flags=re.S | re.I)
    body = re.sub(r"<br\s*/?>", "\n", body, flags=re.I)
    body = re.sub(r"</(div|p|li|h1|h2|h3|tr|section|article)>", "\n", body, flags=re.I)
    text = html.unescape(re.sub(r"<[^>]+>", "", body))

    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln]

    out = [title] if title else []
    if lines:
        if out:
            out.append("")
        out.extend(lines[:max_lines])
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: html_report_to_text.py <report.html> [max_lines]")
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 14
    print(extract(sys.argv[1], n))
