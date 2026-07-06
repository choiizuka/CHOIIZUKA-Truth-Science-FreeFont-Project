from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ===== ここだけ変えればOK =====
PREFIX = "TRSans_"
TTF = "fonts/DejaVuSans-Bold.ttf"
CANVAS = (200, 300)
BG = "#FFFFFF"
FG = "#000000"
CAP_H_RATIO = 0.85
X_H_RATIO = 0.65
CHARS = "0123456789Ee" # 0-9とEe
# =============================

BASE = Path(__file__).parent
out_dir = BASE / "output"
out_dir.mkdir(exist_ok=True)

W, H = CANVAS
cap_h = int(H * CAP_H_RATIO)
x_h = int(H * X_H_RATIO)
ttf_path = BASE / TTF

for ch in CHARS:
    target = x_h if ch.islower() else cap_h
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    size = 10
    while True:
        font = ImageFont.truetype(str(ttf_path), size)
        h = draw.textbbox((0,0), ch, font=font)[3]
        if h >= target: break
        size += 2
    bbox = draw.textbbox((0,0), ch, font=font)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    x = (W-w)//2 - bbox[0]
    y = (H-h)//2 - bbox[1]
    draw.text((x, y), ch, font=font, fill=FG)
    img.save(out_dir / f"{PREFIX}{ch}.png")

print(f"done {PREFIX}")
