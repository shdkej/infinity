#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps, ImageFont
import hashlib, json

ROOT=Path(__file__).parent; CANVAS=(1080,1350)
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; BOLD='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
INPUT=Path('/home/ubuntu/.openclaw/workspace/media/inbound/openclaw-staged-5ad90ad8-3dea-451e-a518-233ab8cad2b3')
sources=['input-06208009-f173-4988-880f-82c0ce06c940.jpg','input-d439726d-c0c8-4c45-988f-c0d2b71aa984.jpg','input-1f0916b8-54cd-4f2a-9621-e0b97dd4032f.jpg','input-32728ae3-1a81-4268-8b93-4b30b6d40187.jpg','input-5dd2e069-a3d3-4622-977a-20949216ddd3.jpg','input-e0fae03b-d284-4ab1-9aa0-891cb168a692.jpg']
cards=[
 ('카타니아에서\n보낸 하루','돈 쓴 장면과\n쉬었던 순간들','dense',(0.25,0.45)),
 ('시장 생해산물은\n비싸게 느껴졌다','가격보다 먼저\n확인할 기준을 생각했다','dense',(0.5,0.5)),
 ('벨리니 공원에서는\n잘 쉬었다','하루에 이런\n한 장면은 남겨두기','ordered',(0.5,0.35)),
 ('음료도 비싸게 느꼈다','버스 티켓은\n확인하고 사서 아꼈다','ordered',(0.52,0.5)),
 ('버스 티켓은\n확인하고 사서 아꼈다','', 'spacious',(0.5,0.45)),
 ('저녁 3코스는\n만족스러웠다','', 'spacious',(0.55,0.48)),
]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def f(path,size): return ImageFont.truetype(path,size,index=0)
def main():
 ROOT.mkdir(parents=True,exist_ok=True); manifest={'intent_id':'content-catania-day-carousel-20260908','canvas':[1080,1350],'private_boundary':{'public_posted':False,'external_uploaded':False,'profile_changed':False,'publication_scope':'private-only'},'source_inputs':[],'cards':[]}
 for i,(src,(title,body,rhythm,center)) in enumerate(zip(sources,cards),1):
  p=INPUT/src; im=Image.open(p).convert('RGB'); im=ImageOps.fit(im,CANVAS,Image.Resampling.LANCZOS,centering=center)
  if i==1: im.paste(Image.new('RGB',(320,1350),(18,18,18)),(760,0))
  if i==3: im.paste(im.crop((0,690,1080,1350)).filter(ImageFilter.GaussianBlur(20)),(0,690))
  if i==5: im.paste(im.crop((0,0,1080,310)).filter(ImageFilter.GaussianBlur(20)),(0,0))
  if i==4: im.paste(im.crop((0,990,370,1350)).filter(ImageFilter.GaussianBlur(24)),(0,990))
  im=ImageEnhance.Color(im).enhance(.48); im=ImageEnhance.Brightness(im).enhance(.66); im=ImageEnhance.Contrast(im).enhance(.90); im=im.filter(ImageFilter.GaussianBlur(.15))
  ov=Image.new('RGBA',CANVAS,(0,0,0,0)); d=ImageDraw.Draw(ov); d.rectangle((0,0,1080,1350),fill=(18,18,18,68))
  # Card-specific density uses text amount, never decoration or a new claim.
  if rhythm=='dense':
   d.rectangle((70,74,277,114),fill=(18,18,18,185)); d.text((88,79),f'{i:02d} / 06',font=f(FONT,23),fill='white')
  if i==4:
   # Keep card 4 ordered but use a restrained near-black text field, not a new visual language.
   d.rectangle((64,540,1016,1005),fill=(18,18,18,198))
  tx,ty=(84,875) if rhythm!='spacious' else (84,940)
  if i==4: tx,ty=108,610
  shadow=(0,0,0,130); fill=(250,249,244,255)
  d.multiline_text((tx+3,ty+3),title,font=f(BOLD,76 if rhythm!='spacious' else 64),fill=shadow,spacing=10)
  d.multiline_text((tx,ty),title,font=f(BOLD,76 if rhythm!='spacious' else 64),fill=fill,spacing=10)
  if body:
   by=ty+(185 if rhythm!='spacious' else 160)
   d.multiline_text((tx+2,by+2),body,font=f(FONT,39),fill=shadow,spacing=12)
   d.multiline_text((tx,by),body,font=f(FONT,39),fill=fill,spacing=12)
  out=ROOT/f'card-{i:02d}.png'; Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB').save(out,quality=95)
  preview=ROOT/f'preview-{i:02d}.png'; Image.open(out).resize((270,338),Image.Resampling.LANCZOS).save(preview,quality=92)
  treatment={1:'right phone-holder region removed',2:'none',3:'lower pedestrian region blurred',4:'lower arm/hand region blurred',5:'upper reflection/person region blurred',6:'none'}[i]
  manifest['source_inputs'].append({'card':i,'filename':src,'sha256':sha(p),'provenance':'user-provided local production input; private-only','privacy_treatment':treatment})
  manifest['cards'].append({'card':i,'png':out.name,'preview':preview.name,'sha256':sha(out),'rhythm':rhythm,'copy':[title,body],'source':src,'round_table_checked':True})
 manifest['claims']='Limited to user record: raw seafood and vending drink felt expensive; Bellini park rest; bus-ticket checking/purchase saved money; dinner three-course satisfaction. No amounts, vendor names, safety, or third-party claims.'
 manifest['privacy']='Private-only. Faces/signage/precise timestamps are not cleared for public release.'
 (ROOT/'render-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__': main()
