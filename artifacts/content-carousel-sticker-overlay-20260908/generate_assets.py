#!/usr/bin/env python3
"""Render one private, layout-only Instagram card with a deterministic overlay."""
from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).parent
CANVAS = (1080, 1350)
SOURCE = Path("/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/data/card-news/source-assets/morning-routine-2026-07-05/clean-01-scrapbook.jpg")
REGULAR = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def font(path: str, size: int):
    return ImageFont.truetype(path, size=size, index=0)


# Imported after constants so typefaces remain easy to audit in the manifest.
from PIL import ImageFont  # noqa: E402


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    # Crop away the source's hand and lower social UI; this is a private visual
    # fixture, not a claim about the original scene.
    source = source.crop((0, 80, source.width, 617))
    image = ImageOps.fit(source, CANVAS, method=Image.Resampling.LANCZOS, centering=(0.52, 0.50))
    image = ImageEnhance.Color(image).enhance(0.40)
    image = ImageEnhance.Brightness(image).enhance(0.58)
    image = ImageEnhance.Contrast(image).enhance(0.90)
    image = image.filter(ImageFilter.GaussianBlur(radius=0.22))

    # Deterministic, subtle record grain—never a decorative gradient.
    pixels = image.load(); noise = random.Random(20260908)
    for y in range(0, CANVAS[1], 2):
        for x in range(0, CANVAS[0], 2):
            r, g, b = pixels[x, y]; delta = noise.randint(-7, 7)
            pixels[x, y] = tuple(max(0, min(255, channel + delta)) for channel in (r, g, b))

    layer = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    # A quiet dark wash makes the image a record rather than an ad-like background.
    draw.rectangle((0, 0, 1080, 1350), fill=(18, 18, 18, 86))

    hook_font = font(BOLD, 165)
    memo_font = font(REGULAR, 42)
    label_font = font(BOLD, 27)
    # The small rotation and line offset deliberately suggest marker lettering
    # without pretending a font is a human signature.
    hook_lines = [("기록의", (87, 117), -3), ("첫 문장", (118, 286), 2)]
    for text, (x, y), angle in hook_lines:
        piece = Image.new("RGBA", (900, 230), (0, 0, 0, 0))
        piece_draw = ImageDraw.Draw(piece)
        piece_draw.text((18, 18), text, font=hook_font, fill=(201, 244, 109, 255), stroke_width=10, stroke_fill=(18, 18, 18, 255))
        piece = piece.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
        layer.alpha_composite(piece, (x - 15, y - 20))

    # The sole bright element: a square-corner fluorescent memo, intentionally
    # smaller than the hook and placed clear of the photo's book spread.
    memo_box = (126, 586, 948, 805)
    draw.rectangle(memo_box, fill=(201, 244, 109, 248))
    draw.text((166, 626), "LAYOUT ONLY  ·  PRIVATE SAMPLE", font=label_font, fill=(18, 18, 18, 255))
    draw.multiline_text((166, 678), "사진 위의 문장과 메모가\n서로 먼저 읽히는지 확인합니다.", font=memo_font, fill=(18, 18, 18, 255), spacing=12)

    image = Image.alpha_composite(image.convert("RGBA"), layer).convert("RGB")
    card = ROOT / "card-01.png"
    preview = ROOT / "preview-25pct.png"
    image.save(card, quality=95)
    image.resize((270, 338), Image.Resampling.LANCZOS).save(preview, quality=94)
    manifest = {
        "intent_id": "content-carousel-sticker-overlay-20260908",
        "renderer": "Pillow direct composition",
        "canvas": {"width": 1080, "height": 1350, "ratio": "4:5", "mode": "RGB"},
        "deliverables": ["card-01.png", "preview-25pct.png"],
        "private_boundary": {"public_posted": False, "external_uploaded": False, "profile_changed": False, "publication_scope": "private-only"},
        "style_references": [
            "/home/ubuntu/.openclaw/workspace/media/inbound/openclaw-staged-bbc08afa-a239-4c9b-a7e4-2c3711786445/input-3dda4330-d17d-401e-911a-b51a34e97fed.jpg",
            "/home/ubuntu/.openclaw/workspace/media/inbound/openclaw-staged-bbc08afa-a239-4c9b-a7e4-2c3711786445/input-339676f8-a3df-435b-9314-20462ce4f242.jpg",
        ],
        "background_provenance": {"path": str(SOURCE), "source_sha256": sha256(SOURCE), "use": "private layout fixture only; publication rights and scene claims not evaluated"},
        "overlays": {"hook": {"bbox": [72, 96, 860, 482], "style": "lime fill / near-black outline / marker-like line offsets"}, "memo": {"bbox": list(memo_box), "style": "single fluorescent-lime square-corner memo / near-black copy"}},
        "protected_photo_region": [40, 850, 1040, 1240],
        "round_table": False,
        "content_claims": "layout-only; no travel, location, safety, performance, or personal-experience claim",
        "sha256": {"card-01.png": sha256(card), "preview-25pct.png": sha256(preview)},
    }
    (ROOT / "render-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
