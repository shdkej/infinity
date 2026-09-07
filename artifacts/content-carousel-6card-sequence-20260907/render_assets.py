#!/usr/bin/env python3
"""Render generated SVG cards with local Chromium; no network access."""
from pathlib import Path
import subprocess, json, hashlib, shutil
from PIL import Image
OUT=Path(__file__).parent; CHROMIUM='/snap/bin/chromium'; scratch=Path('/home/ubuntu/carousel-render.O5mG3A'); profile=scratch/'profile'
for n in range(1,7):
    svg=(OUT/f'card-{n:02d}.svg').resolve(); png=OUT/f'card-{n:02d}.png'
    # Snap Chromium cannot read the /tmp worktree. Mirror only this local SVG into its permitted scratch directory.
    scratch_svg=scratch/f'card-{n:02d}.svg'; scratch_html=scratch/f'render-{n:02d}.html'
    shutil.copy2(svg,scratch_svg)
    shutil.copy2(OUT/'travel-record-base.png',scratch/'travel-record-base.png')
    scratch_html.write_text(f'<style>html,body,img{{margin:0;width:1080px;height:1350px;overflow:hidden}}</style><img src="file://{scratch_svg}">',encoding='utf-8')
    scratch_png=scratch/f'card-{n:02d}.png'
    subprocess.run([CHROMIUM,'--headless','--no-sandbox','--allow-file-access-from-files',f'--user-data-dir={profile}','--disable-gpu','--hide-scrollbars','--window-size=1080,1350',f'--screenshot={scratch_png}',f'file://{scratch_html.resolve()}'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    shutil.move(scratch_png,png)
    im=Image.open(png).convert('RGB'); im.save(png); im.resize((270,338)).save(OUT/f'preview-{n:02d}.png')
manifest=json.loads((OUT/'render-manifest.json').read_text())
for card in manifest['cards']:
    for k in ('png','preview'):
        p=OUT/card[k]; card['sha256_'+k]=hashlib.sha256(p.read_bytes()).hexdigest()
    card['dimensions']=list(Image.open(OUT/card['png']).size); card['mode']=Image.open(OUT/card['png']).mode
manifest['renderer']='Chromium headless local'; manifest['renderer_path']=CHROMIUM
(OUT/'render-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
