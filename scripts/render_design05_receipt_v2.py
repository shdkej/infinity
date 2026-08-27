#!/usr/bin/env python3
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "design-05"
OVERLAY = OUT / "egypt-giza-field-receipt-overlay-v2.png"
PREVIEW = OUT / "egypt-giza-field-receipt-overlay-v2-preview-1920x1080.png"
REFERENCE_PREVIEW = OUT / "egypt-giza-field-receipt-overlay-preview-1920x1080.png"
CONTEXT_CARD = (
    ROOT.parent
    / "source"
    / "openclaw-system"
    / "reports"
    / "youtube-explainer"
    / "egypt-giza-context-card.png"
)


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    paths = {
        "regular": "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "bold": "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
        "serif": "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
        "serif-bold": "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
    }
    return ImageFont.truetype(paths[weight], size=size)


def rough_edge_polygon(w: int, h: int, margin: int) -> list[tuple[int, int]]:
    rnd = random.Random(2105)
    left, right, top, bottom = margin + 24, w - margin - 12, margin + 20, h - margin - 32
    pts: list[tuple[int, int]] = []
    for x in range(left, right + 1, 24):
        pts.append((x, top + rnd.randint(-13, 9)))
    for y in range(top, bottom + 1, 25):
        pts.append((right + rnd.randint(-8, 11), y))
    for x in range(right, left - 1, -24):
        pts.append((x, bottom + rnd.randint(-15, 10)))
    for y in range(bottom, top - 1, -25):
        pts.append((left + rnd.randint(-9, 10), y))
    return pts


def add_grain(img: Image.Image, alpha: int = 30) -> Image.Image:
    original_alpha = img.getchannel("A") if img.mode == "RGBA" else None
    rnd = random.Random(4500)
    noise = Image.new("L", img.size)
    data = bytes(rnd.randrange(80, 176) for _ in range(img.size[0] * img.size[1]))
    noise.frombytes(data)
    noise = noise.filter(ImageFilter.GaussianBlur(0.35))
    tint = Image.new("RGBA", img.size, (92, 68, 36, alpha))
    mask = Image.eval(noise, lambda p: int((p - 80) / 96 * 255))
    img = Image.composite(Image.alpha_composite(img, tint), img, mask)
    if original_alpha is not None:
        img.putalpha(original_alpha)
    return img


def dashed(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill, width=2, dash=12, gap=9):
    x1, y1, x2, y2 = xy
    x = x1
    while x < x2:
        draw.line((x, y1, min(x + dash, x2), y2), fill=fill, width=width)
        x += dash + gap


def text(draw: ImageDraw.ImageDraw, xy, s: str, fnt, fill, anchor=None, spacing=4):
    draw.multiline_text(xy, s, font=fnt, fill=fill, anchor=anchor, spacing=spacing)


def stamp_layer(size: tuple[int, int]) -> Image.Image:
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    orange = (177, 83, 45, 132)
    box = (382, 884, 666, 966)
    d.rounded_rectangle(box, radius=8, outline=orange, width=4)
    text(d, (406, 902), "WALKED\nNOT BOUGHT", font(22, "bold"), orange, spacing=-1)
    d.line((392, 952, 648, 910), fill=(177, 83, 45, 64), width=5)
    return layer.rotate(-7, resample=Image.Resampling.BICUBIC, center=(524, 925))


def render_overlay() -> None:
    random.seed(2105)
    OUT.mkdir(parents=True, exist_ok=True)
    canvas_w, canvas_h = 820, 1500
    margin = 92
    paper_mask = Image.new("L", (canvas_w, canvas_h), 0)
    md = ImageDraw.Draw(paper_mask)
    md.polygon(rough_edge_polygon(canvas_w, canvas_h, margin), fill=245)
    paper_mask = paper_mask.filter(ImageFilter.GaussianBlur(0.45))

    shadow = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    sh = ImageChops.offset(paper_mask, 18, 26).filter(ImageFilter.GaussianBlur(22))
    shadow.putalpha(Image.eval(sh, lambda p: int(p * 0.32)))

    paper = Image.new("RGBA", (canvas_w, canvas_h), (241, 231, 205, 0))
    base = Image.new("RGBA", (canvas_w, canvas_h), (244, 235, 214, 245))
    warm = Image.new("RGBA", (canvas_w, canvas_h), (239, 211, 157, 62))
    grad = Image.new("L", (canvas_w, canvas_h))
    gd = ImageDraw.Draw(grad)
    for y in range(canvas_h):
        gd.line((0, y, canvas_w, y), fill=int(255 * y / canvas_h))
    base = Image.composite(Image.alpha_composite(base, warm), base, grad)
    paper = Image.composite(base, paper, paper_mask)
    paper = add_grain(paper, 26)

    wrinkle = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wrinkle)
    for x, a in [(260, 32), (585, 24), (418, 18)]:
        wd.line((x, margin + 18, x + random.randint(-18, 18), canvas_h - margin - 44), fill=(95, 73, 39, a), width=2)
        wd.line((x + 5, margin + 18, x + random.randint(-18, 18) + 5, canvas_h - margin - 44), fill=(255, 255, 238, a), width=1)
    for _ in range(34):
        x = random.randint(120, 690)
        y = random.randint(120, 1320)
        wd.arc((x, y, x + random.randint(35, 100), y + random.randint(16, 48)), 190, 330, fill=(95, 73, 39, random.randint(10, 34)), width=1)
    paper = Image.alpha_composite(paper, wrinkle)

    ink = (42, 55, 55, 222)
    faded = (42, 55, 55, 124)
    teal = (39, 116, 126, 196)
    orange = (210, 91, 48, 216)
    pencil = (47, 42, 37, 205)

    d = ImageDraw.Draw(paper)
    x = 154
    top = 148
    text(d, (x, top), "EGYPT · GIZA", font(26, "bold"), teal)
    d.ellipse((x - 30, top + 8, x - 12, top + 26), fill=orange)
    d.line((x - 34, top + 58, 636, top + 47), fill=(39, 116, 126, 165), width=2)
    text(d, (x - 1, top + 92), "FIELD\nRECEIPT", font(58, "serif-bold"), ink, spacing=-6)
    d.line((x - 32, top + 245, 630, top + 230), fill=(39, 116, 126, 110), width=2)

    y = 455
    for label, value in [
        ("PLACE", "GIZA PLATEAU"),
        ("AGE", "4,500 YEARS"),
        ("TYPE", "ROYAL NECROPOLIS"),
    ]:
        text(d, (x, y), label, font(20, "bold"), teal)
        text(d, (x, y + 35), value, font(34 if label != "AGE" else 42, "bold"), orange if label == "AGE" else ink)
        y += 150

    dashed(d, (x - 4, 884, 624, 884), fill=(44, 100, 104, 95), width=2)
    text(d, (x, 932), "사람이 만든 풍경이\n아직 여기 있어요.", font(28, "regular"), pencil, spacing=12)
    text(d, (x, 1038), "관광지가 아니라\n시간의 표면.", font(27, "serif"), (60, 48, 38, 182), spacing=10)
    paper = Image.alpha_composite(paper, stamp_layer((canvas_w, canvas_h)))
    d = ImageDraw.Draw(paper)
    dashed(d, (x - 4, 1185, 624, 1185), fill=(44, 100, 104, 80), width=2, dash=10, gap=12)
    text(d, (x, 1238), "EG-04  /  FIELD NOTE", font(22, "bold"), faded)
    text(d, (x, 1278), "keep the dust. keep the scale.", font(20, "serif"), (65, 70, 67, 128))

    # Sun fade and thumb smudge make the object feel photographed, not exported from a browser.
    smudge = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    sd = ImageDraw.Draw(smudge)
    sd.ellipse((370, 190, 740, 710), fill=(255, 255, 244, 72))
    sd.ellipse((68, 1150, 306, 1432), fill=(179, 121, 44, 38))
    smudge = smudge.filter(ImageFilter.GaussianBlur(38))
    smudge_alpha = ImageChops.multiply(smudge.getchannel("A"), paper.getchannel("A"))
    smudge.putalpha(smudge_alpha)
    paper = Image.alpha_composite(paper, smudge)

    composed = Image.alpha_composite(shadow, paper)
    composed = composed.rotate(-1.8, resample=Image.Resampling.BICUBIC, expand=False, fillcolor=(0, 0, 0, 0))
    composed.save(OVERLAY)


def render_preview() -> None:
    bg = Image.new("RGB", (1920, 1080), (215, 197, 164))
    bd = ImageDraw.Draw(bg)
    for y in range(1080):
        t = y / 1080
        if y < 520:
            r = int(126 + 104 * t)
            g = int(174 + 54 * t)
            b = int(210 + 24 * t)
        else:
            s = (y - 520) / 560
            r = int(214 + 27 * s)
            g = int(190 + 20 * s)
            b = int(144 + 9 * s)
        bd.line((0, y, 1920, y), fill=(r, g, b))
    bd.polygon([(770, 875), (1260, 185), (1720, 875)], fill=(188, 135, 72))
    bd.polygon([(1260, 185), (1420, 875), (1720, 875)], fill=(142, 93, 53))
    bd.polygon([(960, 875), (1260, 185), (1200, 875)], fill=(228, 180, 101))
    for yy in range(300, 850, 78):
        bd.line((860, yy + 170, 1650, yy), fill=(226, 189, 121), width=2)
    bd.rectangle((0, 790, 1920, 1080), fill=(205, 169, 115))
    bd.polygon([(0, 820), (520, 760), (980, 835), (1520, 775), (1920, 830), (1920, 1080), (0, 1080)], fill=(222, 190, 137))
    bg = add_grain(bg.convert("RGBA"), 16).convert("RGB")
    bg = bg.filter(ImageFilter.GaussianBlur(0.45))
    overlay = Image.open(OVERLAY).convert("RGBA")
    overlay = overlay.resize((430, int(430 * overlay.height / overlay.width)), Image.Resampling.LANCZOS)
    preview = bg.convert("RGBA")
    preview.alpha_composite(overlay, (92, 68))
    preview.save(PREVIEW)


if __name__ == "__main__":
    render_overlay()
    render_preview()
    print(OVERLAY)
    print(PREVIEW)
