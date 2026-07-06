"""
TR Font (Truth-Science Font) 設計パラメータ設定
=================================================
この値を変更して build.py を再実行すれば、全グリフが新しい設計値で再生成される。
"""

# ---- フォントメタ情報 ----
FONT_NAME = "TRSans"
STYLE_NAME = "Regular"
FAMILY_NAME = "TR Sans"
FULL_NAME = f"{FAMILY_NAME} {STYLE_NAME}"
VERSION = "0.1.0 (Phase 1 prototype)"

# ---- 単位・縦方向メトリクス ----
UPM = 1000              # Units Per Em
BASELINE = 0
X_HEIGHT = 500
CAP_HEIGHT = 700
ASCENDER = 800
DESCENDER = -200

# ---- 字形設計ルール ----
STROKE_WIDTH = 70       # 均一線幅
CORNER_RADIUS = 15      # 角の丸め（Phase1では簡易対応。README参照）
SIDE_BEARING = 60       # 左右の基本サイドベアリング
DEFAULT_WIDTH = 600     # 汎用文字の目安送り幅（実際は文字ごとに個別指定）
