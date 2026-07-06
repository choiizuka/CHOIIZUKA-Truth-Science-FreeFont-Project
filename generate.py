# フォント画像ジェネレーター
# 2026.7.7
import os
from pathlib import Path
import yaml
from PIL import Image, ImageDraw, ImageFont

def expand(items):
    out = ""
    for it in items:
        if len(it) == 3 and it[1] == "-":
            out += "".join(chr(c) for c in range(ord(it[0]), ord(it[2]) + 1))
        else:
            out += it
    return out

BASE = Path(__file__).parent
for cfg_path in BASE.glob("imagefonts/**/config.yaml"):
    cfg = yaml.safe_load(open(cfg_path, encoding="utf-8"))
    cfg_dir = cfg_path.parent

    W, H = cfg["canvas"]
    BG, FG = cfg["background"], cfg["foreground"]

    for f in cfg["fonts"]:
        out_dir = cfg_dir / cfg["output_dir"] / f["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)

        chars = expand(f["chars"])
        cap_h = int(H * f["cap_height_ratio"])
        x_h = int(H * f["x_height_ratio"])
        ttf_path = cfg_dir / f["ttf"]

        for ch in chars:
            target = x_h if ch.islower() else cap_h
            img = Image.new("RGB", (W, H), BG)
            draw = ImageDraw.Draw(img)
            size = 10
            while True:
                font = ImageFont.truetype(str(ttf_path), size)
                h = draw.textbbox((0, 0), ch, font=font)[3]
                if h >= target:
                    break
                size += 2
            bbox = draw.textbbox((0, 0), ch, font=font)
            w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            x = (W - w) // 2 - bbox[0]
            y = (H - h) // 2 - bbox[1]
            draw.text((x, y), ch, font=font, fill=FG)
            img.save(out_dir / f"{f['prefix']}{ch}.png")

print("done")
