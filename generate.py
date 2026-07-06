import os, yaml
from PIL import Image, ImageDraw, ImageFont

def expand(items):
    out = ""
    for it in items:
        if len(it)==3 and it[1]=="-":
            out += "".join(chr(c) for c in range(ord(it[0]), ord(it[2])+1))
        else:
            out += it
    return out

import glob
for cfg_path in glob.glob("imagefonts/**/config.yaml", recursive=True):
    cfg = yaml.safe_load(open(cfg_path))
    base = os.path.dirname(cfg_path) # ← TRSansフォルダ
    out_dir = os.path.join(base, "output") # 各フォントごとに出力
W, H = cfg["canvas"]
BG, FG = cfg["background"], cfg["foreground"]

for f in cfg["fonts"]:
    folder = os.path.join(cfg["output_dir"], f["folder"])
    os.makedirs(folder, exist_ok=True)
    chars = expand(f["chars"])
    cap_h = int(H * f["cap_height_ratio"])
    x_h = int(H * f["x_height_ratio"])

    for ch in chars:
        target = x_h if ch.islower() else cap_h
        img = Image.new("RGB", (W, H), BG)
        draw = ImageDraw.Draw(img)
        size = 10
        while True:
            font = ImageFont.truetype(f["ttf"], size)
            h = draw.textbbox((0,0), ch, font=font)[3]
            if h >= target: break
            size += 2
        bbox = draw.textbbox((0,0), ch, font=font)
        w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
        x = (W-w)//2 - bbox[0]
        y = (H-h)//2 - bbox[1]
        draw.text((x, y), ch, font=font, fill=FG)
        img.save(os.path.join(folder, f"{f['prefix']}{ch}.png"))

print("done")
