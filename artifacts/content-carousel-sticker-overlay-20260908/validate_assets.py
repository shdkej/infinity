#!/usr/bin/env python3
"""Static guardrails; Red still directly reviews the rendered PNG."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
manifest = json.loads((ROOT / "render-manifest.json").read_text())
card = ROOT / "card-01.png"
preview = ROOT / "preview-25pct.png"
assert card.exists() and preview.exists()
assert Image.open(card).size == (1080, 1350) and Image.open(card).mode == "RGB"
assert Image.open(preview).size == (270, 338)
assert hashlib.sha256(card.read_bytes()).hexdigest() == manifest["sha256"]["card-01.png"]
assert hashlib.sha256(preview.read_bytes()).hexdigest() == manifest["sha256"]["preview-25pct.png"]
assert manifest["round_table"] is False
assert all(value is False for key, value in manifest["private_boundary"].items() if key != "publication_scope")
hook = manifest["overlays"]["hook"]["bbox"]; memo = manifest["overlays"]["memo"]["bbox"]; photo = manifest["protected_photo_region"]
for box in (hook, memo): assert 0 <= box[0] < box[2] <= 1080 and 0 <= box[1] < box[3] <= 1350
assert hook[3] < memo[1]  # hierarchy is spatially separated.
assert memo[3] < photo[1]  # memo does not cover the protected lower photo region.
print("PASS: one RGB 1080x1350 private card; manifest/hash/overlay/no-round-table assertions hold")
