def build(font, cfg):
    # ChatGPT仕様の文字セット
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?%#@&+-=/\\()[]{}<>\"'_*^~∞√≈≤≥±×÷→←↑↓ΣΔπλμΩαβγ"
    for ch in chars:
        code = ord(ch)
        g = font.createChar(code)
        pen = g.glyphPen()
        # 簡単な四角（プロトタイプなので）
        pen.moveTo((100, 0))
        pen.lineTo((500, 0))
        pen.lineTo((500, cfg.CAP_HEIGHT))
        pen.lineTo((100, cfg.CAP_HEIGHT))
        pen.closePath()
        g.width = 600
