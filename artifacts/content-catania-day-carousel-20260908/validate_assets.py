#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import hashlib,json
r=Path(__file__).parent;m=json.loads((r/'render-manifest.json').read_text())
assert len(m['cards'])==6 and [x['rhythm'] for x in m['cards']]==['dense','dense','ordered','ordered','spacious','spacious']
assert all(m['private_boundary'][x] is False for x in ('public_posted','external_uploaded','profile_changed'))
for c in m['cards']:
 p=r/c['png']; q=r/c['preview']; assert Image.open(p).size==(1080,1350) and Image.open(p).mode=='RGB'; assert Image.open(q).size==(270,338); assert hashlib.sha256(p.read_bytes()).hexdigest()==c['sha256']
print('PASS: six individual RGB 1080x1350 cards; sequence rhythm, hashes, previews, private boundary')
