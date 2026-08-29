"""Small, deterministic acceptance check for the marketing-129 image asset."""

from __future__ import annotations

import hashlib
from pathlib import Path

from PIL import Image


asset = Path(__file__).resolve().parents[1] / "artifacts/marketing-129/world-travel-instagram-first-slide-v2.png"
with Image.open(asset) as image:
    image.verify()
with Image.open(asset) as image:
    assert image.format == "PNG", image.format
    assert image.size == (1080, 1350), image.size
    assert image.mode == "RGB", image.mode

print(f"PASS format=PNG size=1080x1350 mode=RGB sha256={hashlib.file_digest(asset.open('rb'), 'sha256').hexdigest()}")
