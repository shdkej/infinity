from __future__ import annotations
import hashlib, json, math, re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
CX, CY, R = 540, 650, 260
SVG_NAMES = ["card-01-experiment.svg", "card-02-evidence.svg", "card-03-next.svg"]

def polar(deg, radius=R):
    t = math.radians(deg); return CX + radius * math.cos(t), CY + radius * math.sin(t)

def main():
    rows = []
    for svg_name in SVG_NAMES:
        png_name = svg_name.replace('.svg', '.png')
        svg = (ROOT / svg_name).read_text(encoding='utf-8')
        assert 'width="1080" height="1350" viewBox="0 0 1080 1350"' in svg
        paths = re.findall(r'<path d="M ([0-9.-]+) ([0-9.-]+) A (\d+) (\d+) 0 0 1 ([0-9.-]+) ([0-9.-]+)" />', svg)
        assert len(paths) == 3
        for idx, m in enumerate(paths):
            assert int(m[2]) == R and int(m[3]) == R
            sx, sy = polar(idx * 120); ex, ey = polar(idx * 120 + 120)
            assert max(abs(float(m[0])-sx), abs(float(m[1])-sy), abs(float(m[4])-ex), abs(float(m[5])-ey)) < 1e-4
        arrows = re.findall(r'<polygon points="([^"]+)" />', svg); assert len(arrows) == 3
        for idx, raw in enumerate(arrows):
            tip = tuple(map(float, raw.split()[0].split(','))); ex, ey = polar(idx * 120 + 120)
            assert math.hypot(tip[0]-ex, tip[1]-ey) < 1e-4
        im = Image.open(ROOT / png_name); assert im.size == (1080, 1350)
        rows.append({'svg': svg_name, 'png': png_name, 'png_size': list(im.size), 'sha256_svg': hashlib.sha256((ROOT/svg_name).read_bytes()).hexdigest(), 'sha256_png': hashlib.sha256((ROOT/png_name).read_bytes()).hexdigest()})
    (ROOT/'render-manifest.json').write_text(json.dumps({'renderer':'Chromium headless SVG screenshot','canvas':[1080,1350],'geometry':{'center':[CX,CY],'radius':R,'segments':[120,120,120],'stroke_width':32,'arrow_tip_rule':'arc endpoint; tangent-derived'},'assets':rows,'public_posted':False,'profile_changed':False,'external_uploaded':False}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('PASS', len(rows), 'cards geometry and PNG dimensions')

if __name__ == '__main__': main()
