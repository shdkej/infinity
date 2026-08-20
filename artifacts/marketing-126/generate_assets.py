from __future__ import annotations

import html
import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
W, H = 1080, 1350
CX, CY, R = 540, 675, 258
STROKE = 34
CHROMIUM = "/snap/bin/chromium"

STEPS = [
    ("가설", -90, "무엇을 바꾸면\n생활이 나아질까"),
    ("실행", 30, "작게 만들고\n바로 써본다"),
    ("증거", 150, "쓴 것과\n막힌 점"),
]

CARDS = [
    {
        "slug": "card-01-why",
        "kicker": "01 / WHY",
        "title": ["여행은", "실험실이 됩니다"],
        "body": ["불편을 발견하면", "작게 만들고 직접 써봅니다."],
        "focus": "가설",
    },
    {
        "slug": "card-02-loop",
        "kicker": "02 / LOOP",
        "title": ["가설 → 실행 → 증거", "이 순서로 돕니다"],
        "body": ["좋아 보이는 말보다", "실제로 쓴 장면을 남깁니다."],
        "focus": "실행",
    },
    {
        "slug": "card-03-next",
        "kicker": "03 / NEXT",
        "title": ["기록에서 골라", "다음 선택을 고칩니다"],
        "body": ["한 번의 결론보다", "다음 반복에서 달라진 것을 봅니다."],
        "focus": "증거",
    },
]


def polar(deg: float, radius: float = R) -> tuple[float, float]:
    t = math.radians(deg)
    return CX + radius * math.cos(t), CY + radius * math.sin(t)


def arc_path(start: float, span: float = 104) -> str:
    x1, y1 = polar(start)
    x2, y2 = polar(start + span)
    return f"M {x1:.3f} {y1:.3f} A {R} {R} 0 0 1 {x2:.3f} {y2:.3f}"


def arrow_points(end_deg: float) -> str:
    t = math.radians(end_deg)
    tangent = (-math.sin(t), math.cos(t))
    normal = (math.cos(t), math.sin(t))
    tip = polar(end_deg)
    base = (tip[0] - tangent[0] * 42, tip[1] - tangent[1] * 42)
    pts = [
        tip,
        (base[0] + normal[0] * 26, base[1] + normal[1] * 26),
        (base[0] - normal[0] * 26, base[1] - normal[1] * 26),
    ]
    return " ".join(f"{x:.3f},{y:.3f}" for x, y in pts)


def label(step: str, deg: float, caption: str, focus: str) -> str:
    x, y = polar(deg + 52, 356)
    anchor = "middle"
    weight = "800" if step == focus else "650"
    opacity = "1" if step == focus else "0.72"
    cap = "".join(
        f'<tspan x="{x:.1f}" dy="{24 if i else 34}">{html.escape(line)}</tspan>'
        for i, line in enumerate(caption.split("\n"))
    )
    return f'''
    <text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" opacity="{opacity}">
      <tspan x="{x:.1f}" font-size="26px" font-weight="{weight}">{html.escape(step)}</tspan>
      <tspan x="{x:.1f}" dy="28" font-size="17px" font-weight="400">{cap}</tspan>
    </text>'''


def multiline(lines: list[str], x: int, y: int, size: int, weight: int, leading: int) -> str:
    body = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else leading}">{html.escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )
    return f'<text x="{x}" y="{y}" font-size="{size}px" font-weight="{weight}">{body}</text>'


def svg(card: dict[str, object]) -> str:
    focus = str(card["focus"])
    arcs = []
    arrows = []
    for step, start, _caption in STEPS:
        arcs.append(
            f'<path d="{arc_path(start)}" opacity="{"1" if step == focus else "0.88"}" />'
        )
        arrows.append(f'<polygon points="{arrow_points(start + 104)}" />')
    labels = "".join(label(step, start, caption, focus) for step, start, caption in STEPS)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <title>{html.escape(str(card["kicker"]))} — closed loop intro</title>
  <desc>White card with one black circular loop split into three equal steps: hypothesis, action, evidence.</desc>
  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <g fill="#111111" font-family="Pretendard, Noto Sans CJK KR, Apple SD Gothic Neo, sans-serif">
    <text x="94" y="125" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="18px" font-weight="700" letter-spacing="3px">{html.escape(str(card["kicker"]))}</text>
    {multiline(card["title"], 94, 212, 55, 800, 70)}
  </g>
  <g fill="none" stroke="#111111" stroke-width="{STROKE}" stroke-linecap="butt" stroke-linejoin="round">
    {''.join(arcs)}
  </g>
  <g fill="#111111">{''.join(arrows)}</g>
  <g fill="#111111" font-family="Pretendard, Noto Sans CJK KR, Apple SD Gothic Neo, sans-serif">
    {labels}
  </g>
  <g fill="#111111" font-family="Pretendard, Noto Sans CJK KR, Apple SD Gothic Neo, sans-serif">
    {multiline(card["body"], 94, 1100, 30, 450, 44)}
  </g>
  <text x="986" y="1244" text-anchor="end" fill="#111111" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="15px" font-weight="700" letter-spacing="2px">CLOSED LOOP</text>
</svg>'''


def main() -> None:
    for card in CARDS:
        (ROOT / f'{card["slug"]}.svg').write_text(svg(card), encoding="utf-8")
    for path in sorted(ROOT.glob("card-*.svg")):
        subprocess.run(
            [
                CHROMIUM,
                "--headless",
                "--no-sandbox",
                "--disable-gpu",
                "--hide-scrollbars",
                "--window-size=1080,1350",
                f"--screenshot={path.with_suffix('.png')}",
                f"file://{path}",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    manifest = {
        "canvas": [W, H],
        "geometry": {
            "center": [CX, CY],
            "radius": R,
            "segments": [{"start": s, "span": 104, "gap": 16} for _n, s, _c in STEPS],
            "equal_step_interval_degrees": 120,
            "stroke_width": STROKE,
            "arrow_tip_rule": "arc endpoint; tangent-derived",
        },
        "public_posted": False,
        "profile_changed": False,
        "external_uploaded": False,
        "assets": [f'{card["slug"]}.png' for card in CARDS],
    }
    (ROOT / "render-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("rendered marketing-126 assets")


if __name__ == "__main__":
    main()
