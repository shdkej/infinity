#!/usr/bin/env python3
"""Generate deterministic private layout-study SVG cards; no network or external assets."""
from pathlib import Path
import json, hashlib, shutil, base64

OUT = Path(__file__).parent
W, H, MX, MB = 1080, 1350, 84, 110
BASE = OUT.parent / 'marketing-129' / 'travel-record-base.png'
shutil.copy2(BASE, OUT / 'travel-record-base.png')
BASE_DATA = 'data:image/png;base64,' + base64.b64encode(BASE.read_bytes()).decode('ascii')
cards = [
  ("01", "dense", "여섯 장의\n기록", ["비공개 레이아웃 시안.", "정보가 많은 장면부터", "천천히 덜어내 본다.", "첫 장은 메모가 많다."], "photo"),
  ("02", "dense", "처음의\n메모", ["아직 정리하지 않은 문장.", "같은 장면 안에서", "먼저 읽을 말을 고른다.", "작은 줄들이 남는다."], "photo"),
  ("03", "organized", "한 장,\n한 문장", ["남길 내용을", "한 줄씩 나눈다.", "앞의 메모는 정리한다."], "photo"),
  ("04", "organized", "여기서는\n한 문장만.", ["설명 대신", "판단이 보이게 둔다."], "narrative"),
  ("05", "spacious", "남는 자리", ["문장 사이를", "비워 둔다."], "photo"),
  ("06", "spacious", "마지막\n질문", ["이 장면에서", "꼭 남길 말은?"], "photo"),
]

def esc(s): return s.replace('&','&amp;').replace('<','&lt;')
def text_lines(lines, x, y, size, weight, cls, gap):
    return ''.join(f'<text x="{x}" y="{y+i*gap}" class="{cls}" font-size="{size}" font-weight="{weight}">{esc(line)}</text>' for i,line in enumerate(lines))

def photo_bg(i, dense):
    # non-evidentiary, anonymous record-like fixture: paper, fabric, note fragments, and sunlight.
    step = 120 if dense else 175
    width = 150 if dense else 110
    height = 220 if dense else 125
    fragments = ''.join(f'<rect x="{84+j*step}" y="{150+(j%2)*90}" width="{width}" height="{height}" rx="4" transform="rotate({-8+j*7} {160+j*step} 220)" fill="#d7c9ae" opacity=".{32+j}"/>' for j in range(4 if dense else 2))
    rails = ''.join(f'<line x1="{88+j*10}" y1="118" x2="{88+j*10}" y2="{410 if dense else 230}" stroke="#e7dcc6" stroke-width="2" opacity=".45"/>' for j in range(4 if dense else 1))
    return f'''<rect width="1080" height="1350" fill="#55584e"/>
<image href="{BASE_DATA}" width="1080" height="1350" preserveAspectRatio="xMidYMid slice" filter="url(#photo)" opacity=".92"/>
<rect width="1080" height="1350" fill="url(#wash)" opacity=".24"/>
<circle cx="{730-i*48}" cy="{220+i*40}" r="430" fill="#d8c49c" opacity=".12" filter="url(#blur)"/>
<path d="M0 840 C290 700 620 830 1080 640 L1080 1350 L0 1350Z" fill="#30352f" opacity=".48"/>
<path d="M0 955 C330 820 710 970 1080 805" fill="none" stroke="#b4a887" stroke-width="68" opacity=".26"/>
{fragments}{rails}<rect x="0" y="0" width="1080" height="1350" fill="url(#grain)" opacity=".22"/>'''

def svg(no, rhythm, title, body, kind):
    title_lines=title.split('\n'); dense=rhythm=='dense'; spacious=rhythm=='spacious'
    if kind=='narrative':
      bg='<rect width="1080" height="1350" fill="#121212"/><rect x="84" y="84" width="912" height="1182" fill="none" stroke="#5f5b52" stroke-width="1"/>'
      title_y=530; body_y=815; anchor='middle'; x=540
      label='<text x="540" y="164" class="meta" text-anchor="middle">PRIVATE SEQUENCE / 04</text>'
    else:
      bg=photo_bg(int(no), dense)
      title_y=970 if not spacious else 1020; body_y=1140 if not spacious else 1190; anchor='start'; x=MX
      label=f'<text x="84" y="118" class="meta">PRIVATE STUDY / {no}</text>'
    title_svg=text_lines(title_lines,x,title_y, (82 if not spacious else 92),700,'title',94)
    body_svg=text_lines(body,x,body_y, (35 if not spacious else 37),400,'body',51)
    density=f'<text x="996" y="118" class="meta" text-anchor="end">{rhythm.upper()}</text>' if kind!='narrative' else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
<defs><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#827c68"/><stop offset=".6" stop-color="#5c6057"/><stop offset="1" stop-color="#232724"/></linearGradient><filter id="blur"><feGaussianBlur stdDeviation="34"/></filter><filter id="photo"><feColorMatrix type="saturate" values=".38"/><feComponentTransfer><feFuncR type="linear" slope=".82"/><feFuncG type="linear" slope=".82"/><feFuncB type="linear" slope=".82"/></feComponentTransfer></filter><filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity=".35"/></filter><pattern id="grain" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="3" r=".7" fill="#f5eedc"/><circle cx="7" cy="6" r=".55" fill="#131511"/></pattern><style>.title,.body{{font-family:'Noto Sans CJK KR','Noto Sans KR',sans-serif;fill:#fff;filter:url(#shadow)}}.meta{{font-family:'Noto Sans CJK KR',sans-serif;font-size:22px;letter-spacing:3px;fill:#f4eddb;opacity:.82}}</style></defs>
{bg}{label}{density}<g text-anchor="{anchor}">{title_svg}{body_svg}</g></svg>'''

manifest={'intent':'content-carousel-6card-sequence-20260907','canvas':{'width':W,'height':H,'ratio':'4:5'},'fixed_design':{'safe_margin_px':{'horizontal':MX,'bottom':MB},'text_shadow':'black 35%, 2px blur','private_layout_only':True,'public_posted':False,'external_uploaded':False,'profile_changed':False},'source_provenance':'approved internal low-saturation travel-record visual base from marketing-129; no location, date, person, handle, CTA, price, or publishing claim; used as a layout fixture only','cards':[]}
for no,rhythm,title,body,kind in cards:
    path=OUT/f'card-{no}.svg'; path.write_text(svg(no,rhythm,title,body,kind),encoding='utf-8')
    manifest['cards'].append({'number':int(no),'svg':path.name,'png':f'card-{no}.png','preview':f'preview-{no}.png','rhythm':rhythm,'kind':kind,'copy_anchor':'center' if kind=='narrative' else 'lower-left','title':title.replace('\n',' / '),'safe_margin_checked':True,'sha256_svg':hashlib.sha256(path.read_bytes()).hexdigest()})
(OUT/'render-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
