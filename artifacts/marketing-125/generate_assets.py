from __future__ import annotations

import html
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent
W, H = 1080, 1350
SCALE = 3
CX, CY, R = 540, 660, 286
STROKE = 44
SEGMENT_DEG = 102
GAP_DEG = 18
STARTS = [-90 + GAP_DEG / 2, 30 + GAP_DEG / 2, 150 + GAP_DEG / 2]
FONT_REGULAR = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"

CARDS = [
    {
        "slug": "card-01-experiment",
        "title": ["여행·AI·제품을", "작게 실험합니다"],
        "body": ["아이디어를 크게 믿기 전에", "생활 속에서 먼저 써봅니다."],
    },
    {
        "slug": "card-02-evidence",
        "title": ["써본 것과", "안 쓴 것을 남깁니다"],
        "body": ["좋았다는 말보다", "다시 고를 근거를 모읍니다."],
    },
    {
        "slug": "card-03-next",
        "title": ["기록에서 골라", "다음 선택을 고칩니다"],
        "body": ["한 번의 결론보다", "다음 반복에서 달라진 것을 봅니다."],
    },
]


def polar(deg: float, radius: float = R) -> tuple[float, float]:
    rad = math.radians(deg)
    return CX + radius * math.cos(rad), CY + radius * math.sin(rad)


def tangent(deg: float) -> tuple[float, float]:
    rad = math.radians(deg)
    return -math.sin(rad), math.cos(rad)


def arc_points(start: float, end: float, steps: int = 90) -> list[tuple[float, float]]:
    return [polar(start + (end - start) * i / steps) for i in range(steps + 1)]


def arrow_polygon(end: float) -> list[tuple[float, float]]:
    tip = polar(end)
    tx, ty = tangent(end)
    nx, ny = math.cos(math.radians(end)), math.sin(math.radians(end))
    length = 70
    half_width = 38
    base = (tip[0] - tx * length, tip[1] - ty * length)
    return [
        tip,
        (base[0] + nx * half_width, base[1] + ny * half_width),
        (base[0] - nx * half_width, base[1] - ny * half_width),
    ]


def svg_path(start: float, end: float) -> str:
    x1, y1 = polar(start)
    x2, y2 = polar(end)
    return f"M {x1:.6f} {y1:.6f} A {R} {R} 0 0 1 {x2:.6f} {y2:.6f}"


def svg_text_lines(lines: list[str], x: int, y: int, size: int, weight: int, leading: int) -> str:
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else leading
        tspans.append(f'<tspan x="{x}" dy="{dy}">{html.escape(line)}</tspan>')
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}">' + "".join(tspans) + "</text>"


def write_svg(card: dict) -> None:
    paths = []
    arrows = []
    for start in STARTS:
        end = start + SEGMENT_DEG
        paths.append(f'<path d="{svg_path(start, end)}"/>')
        arrows.append('<polygon points="' + " ".join(f"{x:.6f},{y:.6f}" for x, y in arrow_polygon(end)) + '"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="#fff"/>
  <g fill="#111" font-family="Noto Sans CJK KR, Pretendard, sans-serif">
    {svg_text_lines(card["title"], 96, 172, 62, 700, 80)}
  </g>
  <g fill="none" stroke="#111" stroke-width="{STROKE}" stroke-linecap="butt">
    {''.join(paths)}
  </g>
  <g fill="#111">{''.join(arrows)}</g>
  <g fill="#111" font-family="Noto Sans CJK KR, Pretendard, sans-serif">
    {svg_text_lines(card["body"], 96, 1110, 34, 400, 52)}
  </g>
</svg>
'''
    (OUT / f'{card["slug"]}.svg').write_text(svg, encoding="utf-8")


def draw_multiline(draw: ImageDraw.ImageDraw, lines: list[str], xy: tuple[int, int], font: ImageFont.FreeTypeFont, leading: int) -> None:
    x, y = xy
    for i, line in enumerate(lines):
        draw.text((x, y + i * leading), line, fill=(17, 17, 17), font=font)


def write_png(card: dict) -> None:
    im = Image.new("RGB", (W * SCALE, H * SCALE), "white")
    draw = ImageDraw.Draw(im)
    title_font = ImageFont.truetype(FONT_BOLD, 62 * SCALE)
    body_font = ImageFont.truetype(FONT_REGULAR, 34 * SCALE)

    def spt(p: tuple[float, float]) -> tuple[int, int]:
        return round(p[0] * SCALE), round(p[1] * SCALE)

    draw_multiline(draw, card["title"], (96 * SCALE, 172 * SCALE), title_font, 80 * SCALE)
    for start in STARTS:
        end = start + SEGMENT_DEG
        draw.line([spt(p) for p in arc_points(start, end)], fill=(17, 17, 17), width=STROKE * SCALE, joint="curve")
    for start in STARTS:
        end = start + SEGMENT_DEG
        draw.polygon([spt(p) for p in arrow_polygon(end)], fill=(17, 17, 17))
    draw_multiline(draw, card["body"], (96 * SCALE, 1110 * SCALE), body_font, 52 * SCALE)
    im = im.resize((W, H), Image.Resampling.LANCZOS)
    im.save(OUT / f'{card["slug"]}.png', "PNG")


def main() -> None:
    for card in CARDS:
        write_svg(card)
        write_png(card)
    manifest = {
        "renderer": "Pillow supersampled 3x + matching SVG source",
        "canvas": [W, H],
        "geometry": {
            "center": [CX, CY],
            "radius": R,
            "sector_spacing_degrees": 120,
            "visible_arc_degrees_each": SEGMENT_DEG,
            "gap_degrees_each": GAP_DEG,
            "stroke_width": STROKE,
            "arrow_tip_rule": "arc endpoint; tangent-derived; generated mathematically",
        },
        "assets": [f'{card["slug"]}.png' for card in CARDS],
        "public_posted": False,
        "profile_changed": False,
        "external_uploaded": False,
    }
    (OUT / "render-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
