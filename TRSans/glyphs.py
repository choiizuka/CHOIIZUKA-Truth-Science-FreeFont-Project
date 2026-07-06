def build(font, cfg):
    for code in range(32, 127): # 基本ASCII
        g = font.createChar(code)
        pen = g.glyphPen()
        pen.moveTo((100,0))
        pen.lineTo((500,0))
        pen.lineTo((500,700))
        pen.lineTo((100,700))
        pen.closePath()
        g.width = 600
