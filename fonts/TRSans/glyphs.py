# 7セグメントで文字を描く → 中が埋まらない
SEG = {
 'A': [1,1,1,0,1,1,1], 'B':[0,0,1,1,1], #...簡略化
}
def draw_char(g, pattern, cfg):
    # 上・左上・右上・中・左下・右下・下
    coords = [(100,600,500,680),(80,350,160,600),(440,350,520,600),
              (100,310,500,390),(80,80,160,330),(440,80,520,330),(100,0,500,80)]
    pen = g.glyphPen()
    for i,on in enumerate(pattern):
        if on:
            x1,y1,x2,y2 = coords[i]
            pen.moveTo((x1,y1)); pen.lineTo((x2,y1))
            pen.lineTo((x2,y2)); pen.lineTo((x1,y2)); pen.closePath()
    g.stroke(cfg.STROKE) # ← 線を太らせる、塗りつぶさない

def build(font, cfg):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for ch in chars:
        g = font.createChar(ord(ch))
        # 簡易パターン（全部同じだと黒くなるのでAだけ例）
        pat = SEG.get(ch.upper(), [1,1,1,1,1])
        draw_char(g, pat, cfg)
        g.width = 600
