from __future__ import annotations

import json
import math
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
CX, CY, R = 540, 660, 286
SEGMENT_DEG = 102
GAP_DEG = 18
STARTS = [-90 + GAP_DEG / 2, 30 + GAP_DEG / 2, 150 + GAP_DEG / 2]
SLUGS = ["card-01-experiment", "card-02-evidence", "card-03-next"]


def polar(deg: float, radius: float = R) -> tuple[float, float]:
    rad = math.radians(deg)
    return CX + radius * math.cos(rad), CY + radius * math.sin(rad)


def main() -> None:
    manifest = json.loads((ROOT / "render-manifest.json").read_text(encoding="utf-8"))
    assert manifest["geometry"]["center"] == [CX, CY]
    assert manifest["geometry"]["radius"] == R
    assert manifest["geometry"]["sector_spacing_degrees"] == 120
    assert manifest["geometry"]["visible_arc_degrees_each"] == SEGMENT_DEG
    assert manifest["geometry"]["gap_degrees_each"] == GAP_DEG
    assert manifest["public_posted"] is False
    assert manifest["profile_changed"] is False
    assert manifest["external_uploaded"] is False

    for slug in SLUGS:
        svg = (ROOT / f"{slug}.svg").read_text(encoding="utf-8")
        paths = re.findall(r'<path d="M ([0-9.-]+) ([0-9.-]+) A (\d+) (\d+) 0 0 1 ([0-9.-]+) ([0-9.-]+)"/>', svg)
        assert len(paths) == 3, slug
        for idx, match in enumerate(paths):
            assert int(match[2]) == R and int(match[3]) == R
            sx, sy = polar(STARTS[idx])
            ex, ey = polar(STARTS[idx] + SEGMENT_DEG)
            observed = [float(match[0]), float(match[1]), float(match[4]), float(match[5])]
            expected = [sx, sy, ex, ey]
            assert max(abs(a - b) for a, b in zip(observed, expected)) < 1e-4

        arrows = re.findall(r'<polygon points="([^"]+)"/>', svg)
        assert len(arrows) == 3, slug
        for idx, raw in enumerate(arrows):
            tip = tuple(map(float, raw.split()[0].split(",")))
            ex, ey = polar(STARTS[idx] + SEGMENT_DEG)
            assert math.hypot(tip[0] - ex, tip[1] - ey) < 1e-4

        image = Image.open(ROOT / f"{slug}.png")
        assert image.size == (1080, 1350)

    print("PASS marketing-125 geometry, tangent arrows, manifest, PNG dimensions")


if __name__ == "__main__":
    main()
