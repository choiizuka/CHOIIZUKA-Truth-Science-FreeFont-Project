"""
build.py
========
config.py の設計値と glyphs.py のグリフ定義から UFO を組み立て、
ufo2ft で output/TRSans-Regular.ttf にコンパイルする。

実行方法:
    python build.py
"""

import sys
import ufoLib2
import ufo2ft

import config as c
from glyphs import GLYPH_BUILDERS, GLYPH_UNICODES
from primitives import draw_to_glyph


def build_ufo():
    font = ufoLib2.Font()

    # ---- フォント情報 ----
    info = font.info
    info.unitsPerEm = c.UPM
    info.ascender = c.ASCENDER
    info.descender = c.DESCENDER
    info.capHeight = c.CAP_HEIGHT
    info.xHeight = c.X_HEIGHT
    info.familyName = c.FAMILY_NAME
    info.styleName = c.STYLE_NAME
    info.versionMajor = 0
    info.versionMinor = 1

    # ---- .notdef（必須） ----
    notdef = font.newGlyph(".notdef")
    notdef.width = c.DEFAULT_WIDTH
    pen = notdef.getPen()
    m = 50
    pen.moveTo((m, 0))
    pen.lineTo((c.DEFAULT_WIDTH - m, 0))
    pen.lineTo((c.DEFAULT_WIDTH - m, c.CAP_HEIGHT))
    pen.lineTo((m, c.CAP_HEIGHT))
    pen.closePath()

    # ---- 各グリフを生成 ----
    failed = []
    for name, builder in GLYPH_BUILDERS.items():
        try:
            recording_pen, width = builder(c)
        except Exception as e:
            print(f"  ⚠️ {name} の生成でエラー: {e}")
            failed.append(name)
            continue

        glyph = font.newGlyph(name)
        glyph.width = width
        draw_to_glyph(glyph, recording_pen)

        if name in GLYPH_UNICODES:
            glyph.unicodes = [GLYPH_UNICODES[name]]

    if failed:
        print(f"⚠️ 生成失敗グリフ: {failed}")

    print(f"✅ UFO作成完了: {len(font)}グリフ")
    return font


def compile_ttf(font, output_path):
    ttf = ufo2ft.compileTTF(
        font,
        removeOverlaps=False,         # combine()側で既にブール演算済みのため、二重処理を避ける
        convertCubics=True,           # 3次ベジェ → TrueType用の2次ベジェへ変換
    )

    # ---- name テーブル（フォント名情報）を明示的に設定 ----
    name_table = ttf["name"]
    name_table.setName(c.FAMILY_NAME, 1, 3, 1, 0x409)   # Family
    name_table.setName(c.STYLE_NAME, 2, 3, 1, 0x409)    # Subfamily
    name_table.setName(c.FULL_NAME, 4, 3, 1, 0x409)     # Full name
    name_table.setName(c.FONT_NAME + "-" + c.STYLE_NAME, 6, 3, 1, 0x409)  # PostScript name
    name_table.setName(c.VERSION, 5, 3, 1, 0x409)       # Version

    ttf.save(output_path)
    print(f"✅ TTF生成完了: {output_path}")


def main():
    print(f"--- {c.FULL_NAME} ({c.VERSION}) をビルド中 ---")
    font = build_ufo()

    output_path = "output/TRSans-Regular.ttf"
    compile_ttf(font, output_path)


if __name__ == "__main__":
    main()
