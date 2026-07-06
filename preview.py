"""
preview.py
==========
output/TRSans-Regular.ttf を実際に読み込み、サンプル文字列を描画した
preview/preview.png を生成する。「フォントとして実際に使える」ことの確認用。

実行方法:
    python preview.py
"""

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "output/TRSans-Regular.ttf"
OUTPUT_PATH = "preview/preview.png"

LINES = [
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 55),
    ("abcdefghijklmnopqrstuvwxyz", 55),
    ("0123456789", 55),
    (".,:;!?%#@&+-=/\\()[]{}<>\"'_*^~", 50),
    ("∞ √ ≈ ≤ ≥ ± × ÷ → ← ↑ ↓", 55),
    ("Σ Δ Θ Λ Π Φ Ω  α β γ δ λ μ π θ φ ω", 55),
    ("Truth-Science / TR Font / GitHub / v0.1", 60),
]

PADDING = 50
LINE_GAP = 30


def main():
    fonts = [ImageFont.truetype(FONT_PATH, size) for _, size in LINES]

    # 必要な高さを計算
    heights = []
    for font, (text, size) in zip(fonts, LINES):
        bbox = font.getbbox(text)
        heights.append(bbox[3] - bbox[1])
    total_height = sum(heights) + LINE_GAP * (len(LINES) - 1) + PADDING * 2

    width = 1600
    img = Image.new("RGB", (width, total_height), "white")
    draw = ImageDraw.Draw(img)

    y = PADDING
    for font, (text, size) in zip(fonts, LINES):
        draw.text((PADDING, y), text, font=font, fill="black")
        bbox = font.getbbox(text)
        y += (bbox[3] - bbox[1]) + LINE_GAP

    img.save(OUTPUT_PATH)
    print(f"✅ プレビュー生成完了: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
