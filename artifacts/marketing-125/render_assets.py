"""Render the generated SVG cards to exact 1080x1350 PNGs with Chromium."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).parent
CHROMIUM = "/snap/bin/chromium"

for svg in sorted(ROOT.glob("card-*.svg")):
    png = svg.with_suffix(".png")
    subprocess.run([
        CHROMIUM, "--headless", "--no-sandbox", "--disable-gpu",
        "--hide-scrollbars", "--window-size=1080,1350",
        f"--screenshot={png}", f"file://{svg}",
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"rendered {png.name}")
