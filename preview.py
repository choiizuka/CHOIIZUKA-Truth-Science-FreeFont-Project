#!/usr/bin/env python3
"""
TR Font Prototype - preview.py
仕様書通りのプレビュー画像を生成
"""
from PIL import Image, ImageDraw, ImageFont

# 出力フォント
FONT_PATH = "output/TRSans-Regular.ttf"
OUTPUT = "preview.png"

# 仕様書で指定されたテキスト
lines = [
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "",
    "Truth-Science",
    "TR Font",
    "GitHub",
    "Version 0.1",
    "",
    "Σ Δ π λ μ Ω"
]

# 画像作成
img = Image.new('RGB', (1200, 800), 'white')
draw = ImageDraw.Draw(img)

try:
    font_lg = ImageFont.truetype(FONT_PATH, 48)
    font_sm = ImageFont.truetype(FONT_PATH, 36)
except:
    # フォント読み込み失敗時はデフォルト
    font_lg = ImageFont.load_default()
    font_sm = ImageFont.load_default()

y = 40
for i, line in enumerate(lines):
    f = font_lg if i < 3 else font_sm
    draw.text((40, y), line, fill='black', font=f)
    y += 60 if line else 30

img.save(OUTPUT)
print(f"✅ Preview generated: {OUTPUT}")
