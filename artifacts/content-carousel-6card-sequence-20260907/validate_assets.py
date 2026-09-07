#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import json, hashlib
root=Path(__file__).parent
m=json.loads((root/'render-manifest.json').read_text())
assert len(m['cards'])==6
for c in m['cards']:
    p=root/c['png']; assert p.exists() and p.stat().st_size>0
    im=Image.open(p); assert im.size==(1080,1350); assert im.mode=='RGB'
    assert hashlib.sha256(p.read_bytes()).hexdigest()==c['sha256_png']
assert [c['rhythm'] for c in m['cards']]==['dense','dense','organized','organized','spacious','spacious']
assert m['cards'][3]['kind']=='narrative'
assert all(m['fixed_design'][x] is False for x in ('public_posted','external_uploaded','profile_changed'))
print('PASS: 6 rendered cards, fixed dimensions/rhythm/private boundary')
