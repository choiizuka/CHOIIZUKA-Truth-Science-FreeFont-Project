# TRSans v0.1 - 7セグメント方式（黒塗り回避）
def draw_segments(g, pattern):
    # 7セグの座標 [x1,y1,x2,y2]
    segs = [
        (120, 620, 480, 700), # 上
        (80, 380, 160, 620), # 左上
        (440, 380, 520, 620), # 右上
        (120, 340, 480, 420), # 中
        (80, 100, 160, 340), # 左下
        (440, 100, 520, 340), # 右下
        (120, 60, 480, 140), # 下
    ]
    pen = g.glyphPen()
    for i, on in enumerate(pattern):
        if on and i < len(segs):
            x1,y1,x2,y2 = segs[i]
            pen.moveTo((x1,y1))
            pen.lineTo((x2,y1))
            pen.lineTo((x2,y2))
            pen.lineTo((x1,y2))
            pen.closePath()
    # ← stroke()は使わない。長方形をそのまま置くだけ

# 簡易パターン（A-Zだけ定義、他は数字用）
PATTERNS = {
    'A':[1,1,0], 'B':[0,0,1,1,1,1,1], 'C':[1,0,0,0,1,1,1],
    'D':[0,0,1,1,1,1,0], 'E':[1,0,0,0,1,1,1], 'F':[1,0,0,0,1,0,0],
    'G':[1,0,1,1,1], 'H':[0,1,1,1,1,0], 'I':[0,0,0,0,1,1,0],
    'T':[0,0,0,0,1,1,1], 'R':[1,1,1,1,1,0,0], 'U':[0,1,1,0,1,1,1],
    'S':[1,0,1,1,0,1,1], 'N':[1,1,1,0,1], 'O':[1,1,1,0,1,1,1],
}

def build(font, cfg):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
    for ch in chars:
        g = font.createChar(ord(ch))
        pat = PATTERNS.get(ch, [1,1,1,1,1,1,1]) # 未定義は全部点灯
        draw_segments(g, pat)
        g.width = 600
