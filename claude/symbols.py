"""
symbols.py
==========
仕様書(TR Font Prototype Drawing Specification v0.1)に基づく追加グリフ:
  - 基本記号 . , : ; ! ? % # @ & + - = / \\ ( ) [ ] { } < > " ' _ * ^ ~
  - 科学記号 ∞ √ ≈ ≤ ≥ ± × ÷ → ← ↑ ↓

既存の primitives.py（bar_path / ellipse_path / bowl / combine）だけで構成。
"""

from primitives import bar_path, rect_path, ellipse_path, bowl, combine


def _mid(c):
    return c.X_HEIGHT / 2


# ---------------------------------------------------------------------
# 基本記号
# ---------------------------------------------------------------------
def build_period(c):
    sw = c.STROKE_WIDTH
    r = sw / 2 + 10
    pos = [ellipse_path(150, r, r, r)]
    return combine(pos), 300


def build_comma(c):
    sw = c.STROKE_WIDTH
    r = sw / 2 + 10
    pos = [ellipse_path(150, r, r, r), bar_path(150, r, 90, -120, sw * 0.7)]
    return combine(pos), 300


def build_colon(c):
    sw = c.STROKE_WIDTH
    r = sw / 2 + 10
    mid = _mid(c)
    pos = [ellipse_path(150, r, r, r), ellipse_path(150, mid, r, r)]
    return combine(pos), 300


def build_semicolon(c):
    sw = c.STROKE_WIDTH
    r = sw / 2 + 10
    mid = _mid(c)
    pos = [
        ellipse_path(150, mid, r, r),
        ellipse_path(150, r, r, r),
        bar_path(150, r, 90, -120, sw * 0.7),
    ]
    return combine(pos), 300


def build_exclam(c):
    sw = c.STROKE_WIDTH
    r = sw / 2 + 10
    pos = [
        ellipse_path(150, r, r, r),
        bar_path(150, r * 2 + 30, 150, c.CAP_HEIGHT, sw),
    ]
    return combine(pos), 300


def build_question(c):
    sw = c.STROKE_WIDTH
    r = sw / 2 + 10
    pos = [ellipse_path(160, r, r, r)]
    p, n = bowl(160, c.CAP_HEIGHT - 130, 130, 130, sw, open_side="bottom")
    pos += p
    pos.append(bar_path(220, c.CAP_HEIGHT - 250, 160, 200, sw))
    return combine(pos, n), 340


def build_percent(c):
    sw = c.STROKE_WIDTH
    r = 90
    pos, neg = bowl(120, c.CAP_HEIGHT - 90, r, r, sw)
    p2, n2 = bowl(400, 90, r, r, sw)
    pos += p2
    neg += n2
    pos.append(bar_path(80, 0, 460, c.CAP_HEIGHT, sw * 0.7))
    return combine(pos, neg), 520


def build_numbersign(c):
    sw = c.STROKE_WIDTH * 0.8
    pos = [
        bar_path(140, -40, 200, c.CAP_HEIGHT + 40, sw),
        bar_path(320, -40, 380, c.CAP_HEIGHT + 40, sw),
        bar_path(40, 460, 480, 460, sw),
        bar_path(40, 200, 480, 200, sw),
    ]
    return combine(pos), 520


def build_at(c):
    sw = c.STROKE_WIDTH * 0.7
    mid = _mid(c)
    pos, neg = bowl(250, mid, 230, 230, sw)
    p2, n2 = bowl(280, mid, 90, 90, sw, open_side="left")
    pos += p2
    neg += n2
    pos.append(bar_path(370, mid, 370, mid + 90, sw))
    return combine(pos, neg), 560


def build_ampersand(c):
    sw = c.STROKE_WIDTH
    pos, neg = bowl(230, 150, 150, 150, sw, open_side="right")
    pos.append(bar_path(230, 300, 480, 0, sw))
    pos.append(ellipse_path(280, 480, 100, 100))
    neg.append(ellipse_path(280, 480, 100 - sw, 100 - sw))
    return combine(pos, neg), 560


def build_plus(c):
    sw = c.STROKE_WIDTH
    mid = _mid(c)
    pos = [bar_path(60, mid, 440, mid, sw), bar_path(250, mid - 190, 250, mid + 190, sw)]
    return combine(pos), 500


def build_hyphen(c):
    sw = c.STROKE_WIDTH
    mid = _mid(c)
    pos = [bar_path(70, mid, 410, mid, sw)]
    return combine(pos), 480


def build_equal(c):
    sw = c.STROKE_WIDTH
    mid = _mid(c)
    pos = [bar_path(70, mid + 80, 410, mid + 80, sw), bar_path(70, mid - 80, 410, mid - 80, sw)]
    return combine(pos), 480


def build_slash(c):
    sw = c.STROKE_WIDTH
    pos = [bar_path(80, -80, 420, c.CAP_HEIGHT + 80, sw)]
    return combine(pos), 500


def build_backslash(c):
    sw = c.STROKE_WIDTH
    pos = [bar_path(80, c.CAP_HEIGHT + 80, 420, -80, sw)]
    return combine(pos), 500


def build_parenleft(c):
    sw = c.STROKE_WIDTH * 0.8
    p, n = bowl(340, 250, 260, 350, sw, open_side="right")
    return combine(p, n), 380


def build_parenright(c):
    sw = c.STROKE_WIDTH * 0.8
    p, n = bowl(20, 250, 260, 350, sw, open_side="left")
    return combine(p, n), 360


def build_bracketleft(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(160, -50, 160, c.CAP_HEIGHT + 50, sw),
        bar_path(160, c.CAP_HEIGHT + 50 - sw / 2, 320, c.CAP_HEIGHT + 50 - sw / 2, sw),
        bar_path(160, -50 + sw / 2, 320, -50 + sw / 2, sw),
    ]
    return combine(pos), 380


def build_bracketright(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(220, -50, 220, c.CAP_HEIGHT + 50, sw),
        bar_path(220, c.CAP_HEIGHT + 50 - sw / 2, 60, c.CAP_HEIGHT + 50 - sw / 2, sw),
        bar_path(220, -50 + sw / 2, 60, -50 + sw / 2, sw),
    ]
    return combine(pos), 380


def build_braceleft(c):
    sw = c.STROKE_WIDTH * 0.8
    mid = _mid(c)
    p1, n1 = bowl(340, c.CAP_HEIGHT - 130, 150, 150, sw, open_side="right")
    p2, n2 = bowl(340, 130, 150, 150, sw, open_side="right")
    pos = p1 + p2 + [bar_path(210, c.CAP_HEIGHT - 260, 210, mid + 40, sw), bar_path(210, mid - 40, 210, 260, sw)]
    neg = n1 + n2
    return combine(pos, neg), 400


def build_braceright(c):
    sw = c.STROKE_WIDTH * 0.8
    mid = _mid(c)
    p1, n1 = bowl(60, c.CAP_HEIGHT - 130, 150, 150, sw, open_side="left")
    p2, n2 = bowl(60, 130, 150, 150, sw, open_side="left")
    pos = p1 + p2 + [bar_path(190, c.CAP_HEIGHT - 260, 190, mid + 40, sw), bar_path(190, mid - 40, 190, 260, sw)]
    neg = n1 + n2
    return combine(pos, neg), 400


def build_less(c):
    sw = c.STROKE_WIDTH
    mid = _mid(c)
    pos = [bar_path(420, mid + 190, 100, mid, sw), bar_path(100, mid, 420, mid - 190, sw)]
    return combine(pos), 500


def build_greater(c):
    sw = c.STROKE_WIDTH
    mid = _mid(c)
    pos = [bar_path(100, mid + 190, 420, mid, sw), bar_path(420, mid, 100, mid - 190, sw)]
    return combine(pos), 500


def build_quotedbl(c):
    sw = c.STROKE_WIDTH * 0.8
    top = c.CAP_HEIGHT
    pos = [bar_path(140, top, 120, top - 160, sw), bar_path(280, top, 260, top - 160, sw)]
    return combine(pos), 380


def build_quotesingle(c):
    sw = c.STROKE_WIDTH * 0.8
    top = c.CAP_HEIGHT
    pos = [bar_path(180, top, 160, top - 160, sw)]
    return combine(pos), 260


def build_underscore(c):
    sw = c.STROKE_WIDTH * 0.8
    pos = [bar_path(40, -100, 460, -100, sw)]
    return combine(pos), 500


def build_asterisk(c):
    sw = c.STROKE_WIDTH * 0.7
    cy = c.CAP_HEIGHT - 130
    pos = [
        bar_path(250, cy - 130, 250, cy + 130, sw),
        bar_path(250 - 115, cy - 65, 250 + 115, cy + 65, sw),
        bar_path(250 - 115, cy + 65, 250 + 115, cy - 65, sw),
    ]
    return combine(pos), 500


def build_asciicircum(c):
    sw = c.STROKE_WIDTH
    top = c.CAP_HEIGHT
    pos = [bar_path(250, top, 100, top - 220, sw), bar_path(250, top, 400, top - 220, sw)]
    return combine(pos), 500


def build_asciitilde(c):
    sw = c.STROKE_WIDTH * 0.8
    mid = _mid(c)
    pos = [
        bar_path(60, mid - 40, 190, mid + 60, sw),
        bar_path(190, mid + 60, 310, mid - 60, sw),
        bar_path(310, mid - 60, 440, mid + 40, sw),
    ]
    return combine(pos), 500


# ---------------------------------------------------------------------
# 科学記号
# ---------------------------------------------------------------------
def build_infinity(c):
    sw = c.STROKE_WIDTH * 0.8
    cy = _mid(c)
    r = 110
    cx1 = 150
    cx2 = cx1 + 2 * r - sw * 0.6
    p1, n1 = bowl(cx1, cy, r, r, sw)
    p2, n2 = bowl(cx2, cy, r, r, sw)
    pos = p1 + p2
    neg = n1 + n2
    return combine(pos, neg), 560


def build_radical(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(20, 120, 90, 40, sw),
        bar_path(90, 40, 220, c.CAP_HEIGHT, sw),
        bar_path(220, c.CAP_HEIGHT, 480, c.CAP_HEIGHT, sw * 0.8),
    ]
    return combine(pos), 500


def build_approxequal(c):
    sw = c.STROKE_WIDTH * 0.75
    mid = _mid(c)
    def wave(y):
        return [
            bar_path(60, y - 30, 170, y + 40, sw),
            bar_path(170, y + 40, 280, y - 40, sw),
            bar_path(280, y - 40, 390, y + 30, sw),
        ]
    pos = wave(mid + 70) + wave(mid - 70)
    return combine(pos), 460


def build_lessequal(c):
    sw = c.STROKE_WIDTH * 0.85
    mid = _mid(c)
    pos = [
        bar_path(400, mid + 210, 100, mid + 40, sw),
        bar_path(100, mid + 40, 400, mid - 110, sw),
        bar_path(80, -60, 420, -60, sw),
    ]
    return combine(pos), 500


def build_greaterequal(c):
    sw = c.STROKE_WIDTH * 0.85
    mid = _mid(c)
    pos = [
        bar_path(100, mid + 210, 400, mid + 40, sw),
        bar_path(400, mid + 40, 100, mid - 110, sw),
        bar_path(80, -60, 420, -60, sw),
    ]
    return combine(pos), 500


def build_plusminus(c):
    sw = c.STROKE_WIDTH * 0.85
    mid = _mid(c)
    pos = [
        bar_path(60, mid + 130, 440, mid + 130, sw),
        bar_path(250, mid, 250, mid + 260, sw),
        bar_path(60, mid - 130, 440, mid - 130, sw),
    ]
    return combine(pos), 500


def build_multiply(c):
    sw = c.STROKE_WIDTH * 0.85
    mid = _mid(c)
    pos = [
        bar_path(90, mid - 150, 410, mid + 150, sw),
        bar_path(90, mid + 150, 410, mid - 150, sw),
    ]
    return combine(pos), 500


def build_divide(c):
    sw = c.STROKE_WIDTH * 0.85
    mid = _mid(c)
    r = sw / 2 + 8
    pos = [
        bar_path(70, mid, 430, mid, sw),
        ellipse_path(250, mid + 130, r, r),
        ellipse_path(250, mid - 130, r, r),
    ]
    return combine(pos), 500


def build_arrowright(c):
    sw = c.STROKE_WIDTH * 0.85
    mid = _mid(c)
    pos = [
        bar_path(60, mid, 420, mid, sw),
        bar_path(420, mid, 300, mid + 120, sw),
        bar_path(420, mid, 300, mid - 120, sw),
    ]
    return combine(pos), 500


def build_arrowleft(c):
    sw = c.STROKE_WIDTH * 0.85
    mid = _mid(c)
    pos = [
        bar_path(440, mid, 80, mid, sw),
        bar_path(80, mid, 200, mid + 120, sw),
        bar_path(80, mid, 200, mid - 120, sw),
    ]
    return combine(pos), 500


def build_arrowup(c):
    sw = c.STROKE_WIDTH * 0.85
    pos = [
        bar_path(250, 0, 250, c.CAP_HEIGHT, sw),
        bar_path(250, c.CAP_HEIGHT, 130, c.CAP_HEIGHT - 180, sw),
        bar_path(250, c.CAP_HEIGHT, 370, c.CAP_HEIGHT - 180, sw),
    ]
    return combine(pos), 500


def build_arrowdown(c):
    sw = c.STROKE_WIDTH * 0.85
    pos = [
        bar_path(250, c.CAP_HEIGHT, 250, 0, sw),
        bar_path(250, 0, 130, 180, sw),
        bar_path(250, 0, 370, 180, sw),
    ]
    return combine(pos), 500


# =====================================================================
# レジストリ
# =====================================================================
SYMBOL_BUILDERS = {
    "period": build_period, "comma": build_comma, "colon": build_colon,
    "semicolon": build_semicolon, "exclam": build_exclam, "question": build_question,
    "percent": build_percent, "numbersign": build_numbersign, "at": build_at,
    "ampersand": build_ampersand, "plus": build_plus, "hyphen": build_hyphen,
    "equal": build_equal, "slash": build_slash, "backslash": build_backslash,
    "parenleft": build_parenleft, "parenright": build_parenright,
    "bracketleft": build_bracketleft, "bracketright": build_bracketright,
    "braceleft": build_braceleft, "braceright": build_braceright,
    "less": build_less, "greater": build_greater,
    "quotedbl": build_quotedbl, "quotesingle": build_quotesingle,
    "underscore": build_underscore, "asterisk": build_asterisk,
    "asciicircum": build_asciicircum, "asciitilde": build_asciitilde,
    "infinity": build_infinity, "radical": build_radical,
    "approxequal": build_approxequal, "lessequal": build_lessequal,
    "greaterequal": build_greaterequal, "plusminus": build_plusminus,
    "multiply": build_multiply, "divide": build_divide,
    "arrowright": build_arrowright, "arrowleft": build_arrowleft,
    "arrowup": build_arrowup, "arrowdown": build_arrowdown,
}

SYMBOL_UNICODES = {
    "period": 0x2E, "comma": 0x2C, "colon": 0x3A, "semicolon": 0x3B,
    "exclam": 0x21, "question": 0x3F, "percent": 0x25, "numbersign": 0x23,
    "at": 0x40, "ampersand": 0x26, "plus": 0x2B, "hyphen": 0x2D,
    "equal": 0x3D, "slash": 0x2F, "backslash": 0x5C,
    "parenleft": 0x28, "parenright": 0x29, "bracketleft": 0x5B, "bracketright": 0x5D,
    "braceleft": 0x7B, "braceright": 0x7D, "less": 0x3C, "greater": 0x3E,
    "quotedbl": 0x22, "quotesingle": 0x27, "underscore": 0x5F, "asterisk": 0x2A,
    "asciicircum": 0x5E, "asciitilde": 0x7E,
    "infinity": 0x221E, "radical": 0x221A, "approxequal": 0x2248,
    "lessequal": 0x2264, "greaterequal": 0x2265, "plusminus": 0x00B1,
    "multiply": 0x00D7, "divide": 0x00F7,
    "arrowright": 0x2192, "arrowleft": 0x2190, "arrowup": 0x2191, "arrowdown": 0x2193,
}
