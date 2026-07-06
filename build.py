#!/usr/bin/env python3
"""
TR Font Prototype v0.1 - build.py
ChatGPT仕様書準拠
"""
import os
import fontforge
import config
import glyphs

print("🔨 TR Font Prototype ビルド開始...")

# 1. 新規フォント作成
font = fontforge.font()
font.encoding = 'UnicodeFull'

# 2. 名前設定（Macで「MPlus」にならないように）
font.fontname = "TRSans-Regular"
font.familyname = "TR Sans"
font.fullname = "TR Sans Regular"
font.version = "0.1"
font.copyright = "Truth-Science Font Prototype"

# 3. メトリクス（config.pyから）
font.em = config.UPM
font.ascent = config.ASCENDER
font.descent = abs(config.DESCENDER)

# 4. グリフ生成（glyphs.pyに全部任せる）
glyphs.build(font, config)

# 5. 出力
os.makedirs('output', exist_ok=True)
output_path = 'output/TRSans-Regular.ttf'
font.generate(output_path)

print(f"✅ 完成！ {output_path}")
print(f" - UPM: {font.em}")
print(f" - グリフ数: {len(list(font.glyphs()))}")
print("GitHub Actionsでもこのまま動きます")
