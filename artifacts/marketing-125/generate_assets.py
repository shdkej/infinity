from __future__ import annotations

import html
import math
from pathlib import Path

OUT = Path(__file__).parent
W, H = 1080, 1350
CX, CY, R, STROKE = 540, 650, 260, 32
CARDS = [
    {"slug": "card-01-experiment", "index": "01 / EXPERIMENT", "headline": ["적게 들고 오래 떠나는 선택을", "실제 여행에서 시험합니다."], "body": "짐과 도구를 줄였을 때\n생활이 정말 편해지는지 봅니다."},
    {"slug": "card-02-evidence", "index": "02 / EVIDENCE", "headline": ["써본 것, 안 쓴 것,", "다시 챙길 것을 기록합니다."], "body": "사용한 장면과 불편했던 순간을\n다음 선택의 근거로 남깁니다."},
    {"slug": "card-03-next", "index": "03 / NEXT FIX", "headline": ["기록에서 불편을 골라", "다음 여행과 작은 도구를 고칩니다."], "body": "한 번의 결론보다\n다음 반복에서 달라지는 것을 봅니다."},
]

def polar(deg: float, radius: float = R):
    t = math.radians(deg)
    return CX + radius * math.cos(t), CY + radius * math.sin(t)

def arc_path(start: float) -> str:
    x1, y1 = polar(start); x2, y2 = polar(start + 120)
    return f"M {x1:.6f} {y1:.6f} A {R} {R} 0 0 1 {x2:.6f} {y2:.6f}"

def arrow_points(end_deg: float) -> str:
    t = math.radians(end_deg)
    tx, ty = -math.sin(t), math.cos(t)
    nx, ny = math.cos(t), math.sin(t)
    tipx, tipy = polar(end_deg)
    basecx, basecy = tipx - tx * 34, tipy - ty * 34
    return " ".join(f"{x:.6f},{y:.6f}" for x, y in [(tipx, tipy), (basecx + nx * 22, basecy + ny * 22), (basecx - nx * 22, basecy - ny * 22)])

def text(lines, x, y, size, weight, leading):
    spans = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else leading}">{html.escape(line)}</tspan>' for i, line in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}px" font-weight="{weight}">{spans}</text>'

def svg(card):
    paths = "".join(f'<path d="{arc_path(start)}" />' for start in (0, 120, 240))
    arrows = "".join(f'<polygon points="{arrow_points(start + 120)}" />' for start in (0, 120, 240))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <title>{html.escape(card["index"])} — closed-loop experiment</title>
  <desc>Exact circle center ({CX},{CY}), radius {R}; three equal 120 degree clockwise arcs and tangent-derived arrowheads.</desc>
  <rect width="1080" height="1350" fill="#ffffff"/>
  <g fill="#111111" font-family="Noto Sans CJK KR, Pretendard, sans-serif">
    <text x="96" y="126" font-family="ui-monospace, monospace" font-size="18px" font-weight="600" letter-spacing="3px">{html.escape(card["index"])}</text>
    {text(card["headline"], 96, 210, 47, 700, 66)}
    <line x1="96" y1="310" x2="984" y2="310" stroke="#111111" stroke-width="2"/>
  </g>
  <g fill="none" stroke="#111111" stroke-width="{STROKE}" stroke-linecap="butt" stroke-linejoin="round">{paths}</g>
  <g fill="#111111">{arrows}</g>
  <g fill="#111111" font-family="Noto Sans CJK KR, Pretendard, sans-serif">
    <text x="96" y="1010" font-size="18px" font-weight="600" letter-spacing="2px">CLOSED LOOP / {html.escape(card["index"].split(" / ")[1])}</text>
    {text(card["body"].split("\n"), 96, 1092, 25, 400, 38)}
  </g>
  <line x1="96" y1="1212" x2="984" y2="1212" stroke="#111111" stroke-width="2"/>
  <text x="984" y="1250" text-anchor="end" fill="#111111" font-family="ui-monospace, monospace" font-size="16px">SAM SAMUEL</text>
</svg>'''

if __name__ == "__main__":
    for card in CARDS:
        (OUT / f'{card["slug"]}.svg').write_text(svg(card), encoding="utf-8")
