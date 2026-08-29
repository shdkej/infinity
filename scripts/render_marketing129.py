from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

root = Path(__file__).resolve().parents[1]
source = Path('/home/ubuntu/.openclaw/agents/genie/agent/codex-home/generated_images/01a049c2-de45-7091-80a2-a4a039f8aa7b/exec-cc938957-96ec-47ff-94dc-af874cb10f7b.png')
outdir = root / 'artifacts' / 'marketing-129'
outdir.mkdir(parents=True, exist_ok=True)
base_path = outdir / 'travel-record-base.png'
final_path = outdir / 'world-travel-instagram-first-slide-v2.png'

base = Image.open(source).convert('RGB').resize((1080, 1350), Image.Resampling.LANCZOS)
base.save(base_path, icc_profile=base.info.get('icc_profile'))

# Warm translucent bands keep text legible without turning the cover into a card UI.
overlay = Image.new('RGBA', base.size, (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
od.rectangle((0, 0, 1080, 540), fill=(246, 240, 222, 222))
od.rectangle((0, 1090, 1080, 1350), fill=(246, 240, 222, 215))
overlay = overlay.filter(ImageFilter.GaussianBlur(0.45))
canvas = Image.alpha_composite(base.convert('RGBA'), overlay)
d = ImageDraw.Draw(canvas)

bold = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
regular = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
small = ImageFont.truetype(bold, 25, index=0)
title = ImageFont.truetype(bold, 88, index=0)
sub = ImageFont.truetype(regular, 29, index=0)
ink = (35, 36, 30, 255)
muted = (87, 84, 73, 255)
rust = (166, 83, 43, 255)

def centered(text, font, y, fill, spacing=0):
    box = d.multiline_textbbox((0, 0), text, font=font, spacing=spacing, align='center')
    x = (1080 - (box[2] - box[0])) / 2
    d.multiline_text((x, y), text, font=font, fill=fill, spacing=spacing, align='center')

d.line((90, 112, 152, 112), fill=rust, width=5)
centered('TRAVEL NOTES  /  01', small, 154, muted)
centered('적게 들고,\n오래 남기기', title, 232, ink, spacing=8)
centered('여행에서 남기는 기록', sub, 1178, muted)

canvas.convert('RGB').save(final_path, quality=96)
print(final_path)
