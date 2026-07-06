# fonts/TRSans/glyphs.py
# Generated to match TRUTH-SCIENCE FONT design brief
# Uses FontForge Python API: createChar, glyphPen, moveTo, lineTo, curveTo, closePath
# Metrics: UPM=1000, glyph width=600, ascent=800, descent=-200
# Only uppercase Latin A-Z, digits 0-9, specified symbols, Greek uppercase, and math symbols are created.
# No lowercase Latin or Greek glyphs are generated.

import fontforge

UPM = 1000
GLYPH_WIDTH = 600
ASCENT = 800
DESCENT = -200

# Helper drawing primitives using glyphPen() methods (moveTo, lineTo, curveTo, closePath)
def _rounded_rect(pen, x0, y0, x1, y1, r):
    # Draw rectangle with corner radius r using 4 cubic bezier segments
    if r <= 0:
        pen.moveTo((x0, y0))
        pen.lineTo((x1, y0))
        pen.lineTo((x1, y1))
        pen.lineTo((x0, y1))
        pen.closePath()
        return
    # Control point factor for approximating quarter circle with cubic bezier
    k = 0.5522847498307936
    pen.moveTo((x0 + r, y0))
    # bottom edge
    pen.lineTo((x1 - r, y0))
    # bottom-right corner
    pen.curveTo((x1 - r + r * k, y0), (x1, y0 + r - r * k), (x1, y0 + r))
    # right edge
    pen.lineTo((x1, y1 - r))
    # top-right corner
    pen.curveTo((x1, y1 - r + r * k), (x1 - r + r * k, y1), (x1 - r, y1))
    # top edge
    pen.lineTo((x0 + r, y1))
    # top-left corner
    pen.curveTo((x0 + r - r * k, y1), (x0, y1 - r + r * k), (x0, y1 - r))
    # left edge
    pen.lineTo((x0, y0 + r))
    # bottom-left corner
    pen.curveTo((x0, y0 + r - r * k), (x0 + r - r * k, y0), (x0 + r, y0))
    pen.closePath()

def _circle(pen, cx, cy, r):
    k = 0.5522847498307936
    pen.moveTo((cx + r, cy))
    pen.curveTo((cx + r, cy + r * k), (cx + r * k, cy + r), (cx, cy + r))
    pen.curveTo((cx - r * k, cy + r), (cx - r, cy + r * k), (cx - r, cy))
    pen.curveTo((cx - r, cy - r * k), (cx - r * k, cy - r), (cx, cy - r))
    pen.curveTo((cx + r * k, cy - r), (cx + r, cy - r * k), (cx + r, cy))
    pen.closePath()

def _oval(pen, cx, cy, rx, ry):
    # approximate oval by scaling circle control points
    k = 0.5522847498307936
    pen.moveTo((cx + rx, cy))
    pen.curveTo((cx + rx, cy + ry * k), (cx + rx * k, cy + ry), (cx, cy + ry))
    pen.curveTo((cx - rx * k, cy + ry), (cx - rx, cy + ry * k), (cx - rx, cy))
    pen.curveTo((cx - rx, cy - ry * k), (cx - rx * k, cy - ry), (cx, cy - ry))
    pen.curveTo((cx + rx * k, cy - ry), (cx + rx, cy - ry * k), (cx + rx, cy))
    pen.closePath()

def _triangle(pen, x0, y0, x1, y1, x2, y2, r=0):
    # simple triangle; r ignored for now (keeps corners sharp)
    pen.moveTo((x0, y0))
    pen.lineTo((x1, y1))
    pen.lineTo((x2, y2))
    pen.closePath()

def _stroke_rect(pen, x0, y0, x1, y1, thickness, r=0):
    # Draw a stroked rectangle by drawing outer rounded rect then inner reversed path
    _rounded_rect(pen, x0, y0, x1, y1, r)
    # inner hole
    inner_x0 = x0 + thickness
    inner_y0 = y0 + thickness
    inner_x1 = x1 - thickness
    inner_y1 = y1 - thickness
    if inner_x1 > inner_x0 and inner_y1 > inner_y0:
        pen.moveTo((inner_x0 + r, inner_y0))
        # inner rectangle (reverse direction)
        # We'll draw as a simple rectangle (no rounding for inner to keep code simple)
        pen.lineTo((inner_x1, inner_y0))
        pen.lineTo((inner_x1, inner_y1))
        pen.lineTo((inner_x0, inner_y1))
        pen.closePath()

def _stroke_oval(pen, cx, cy, rx, ry, thickness):
    # Outer oval
    _oval(pen, cx, cy, rx, ry)
    # Inner oval (hole)
    inner_rx = rx - thickness
    inner_ry = ry - thickness
    if inner_rx > 0 and inner_ry > 0:
        pen.moveTo((cx + inner_rx, cy))
        pen.curveTo((cx + inner_rx, cy + inner_ry * 0.5522847), (cx + inner_rx * 0.5522847, cy + inner_ry), (cx, cy + inner_ry))
        pen.curveTo((cx - inner_rx * 0.5522847, cy + inner_ry), (cx - inner_rx, cy + inner_ry * 0.5522847), (cx - inner_rx, cy))
        pen.curveTo((cx - inner_rx, cy - inner_ry * 0.5522847), (cx - inner_rx * 0.5522847, cy - inner_ry), (cx, cy - inner_ry))
        pen.curveTo((cx + inner_rx * 0.5522847, cy - inner_ry), (cx + inner_rx, cy - inner_ry * 0.5522847), (cx + inner_rx, cy))
        pen.closePath()

# Basic stem and bar geometry helpers tuned for high x-height, low contrast
def _stem_x_positions():
    # returns left and right stem x positions for a 600-wide glyph
    left = 120
    right = GLYPH_WIDTH - 120
    return left, right

def _bar_y_positions():
    # returns baseline, x-height, cap-height, ascender
    baseline = 0
    xh = 560  # high x-height
    cap = 700
    asc = ASCENT
    return baseline, xh, cap, asc

# Create a simple geometric sans-serif uppercase glyphs approximations
def _create_A(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 140
    right = GLYPH_WIDTH - 140
    top = cap
    mid = xh - 120
    # outer triangle
    pen.moveTo((left, baseline))
    pen.lineTo(((GLYPH_WIDTH) / 2, top))
    pen.lineTo((right, baseline))
    pen.closePath()
    # crossbar hole
    pen.moveTo((left + 80, mid))
    pen.lineTo((right - 80, mid))
    pen.lineTo((right - 80, mid - 40))
    pen.lineTo((left + 80, mid - 40))
    pen.closePath()
    return g

def _create_B(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    stem_x = 140
    # vertical stem
    _rounded_rect(pen, stem_x - 20, baseline, stem_x + 60, cap, 20)
    # upper bowl
    _oval(pen, stem_x + 180, cap - 180, 160, 140)
    # lower bowl
    _oval(pen, stem_x + 180, cap - 420, 160, 140)
    # carve holes by drawing inner shapes (reverse direction)
    pen.moveTo((stem_x + 80, cap - 80))
    pen.lineTo((stem_x + 260, cap - 80))
    pen.lineTo((stem_x + 260, cap - 260))
    pen.lineTo((stem_x + 80, cap - 260))
    pen.closePath()
    pen.moveTo((stem_x + 80, cap - 360))
    pen.lineTo((stem_x + 260, cap - 360))
    pen.lineTo((stem_x + 260, cap - 540))
    pen.lineTo((stem_x + 80, cap - 540))
    pen.closePath()
    return g

def _create_C(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    cx = GLYPH_WIDTH / 2
    cy = cap - 300
    _oval(pen, cx + 20, cy, 260, 320)
    # carve inner to make C open
    pen.moveTo((cx + 260, cy + 20))
    pen.lineTo((cx + 260, cy - 20))
    pen.lineTo((cx - 40, cy - 320))
    pen.lineTo((cx - 40, cy + 320))
    pen.closePath()
    return g

def _create_D(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    stem_x = 120
    _rounded_rect(pen, stem_x - 20, baseline, stem_x + 60, cap, 20)
    _oval(pen, stem_x + 200, cap / 2, 220, cap / 2 - 40)
    # inner carve
    pen.moveTo((stem_x + 80, cap - 80))
    pen.lineTo((stem_x + 320, cap - 80))
    pen.lineTo((stem_x + 320, 80))
    pen.lineTo((stem_x + 80, 80))
    pen.closePath()
    return g

def _create_E(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 120
    right = GLYPH_WIDTH - 120
    # vertical stem
    _rounded_rect(pen, left - 20, baseline, left + 60, cap, 18)
    # top bar
    pen.moveTo((left + 60, cap - 40))
    pen.lineTo((right, cap - 40))
    pen.lineTo((right, cap - 100))
    pen.lineTo((left + 60, cap - 100))
    pen.closePath()
    # middle bar
    mid = xh
    pen.moveTo((left + 60, mid + 20))
    pen.lineTo((right - 120, mid + 20))
    pen.lineTo((right - 120, mid - 40))
    pen.lineTo((left + 60, mid - 40))
    pen.closePath()
    # bottom bar
    pen.moveTo((left + 60, baseline + 40))
    pen.lineTo((right, baseline + 40))
    pen.lineTo((right, baseline))
    pen.lineTo((left + 60, baseline))
    pen.closePath()
    return g

def _create_F(font, code):
    g = _create_E(font, code)  # start from E
    # remove bottom bar by clearing and redrawing without bottom
    # We'll recreate F explicitly
    g.clear()
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 120
    right = GLYPH_WIDTH - 120
    _rounded_rect(pen, left - 20, baseline, left + 60, cap, 18)
    pen.moveTo((left + 60, cap - 40))
    pen.lineTo((right, cap - 40))
    pen.lineTo((right, cap - 100))
    pen.lineTo((left + 60, cap - 100))
    pen.closePath()
    mid = xh
    pen.moveTo((left + 60, mid + 20))
    pen.lineTo((right - 120, mid + 20))
    pen.lineTo((right - 120, mid - 40))
    pen.lineTo((left + 60, mid - 40))
    pen.closePath()
    return g

def _create_G(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    cx = GLYPH_WIDTH / 2 - 20
    cy = cap - 300
    _oval(pen, cx, cy, 260, 320)
    # inner cut to make G opening and spur
    pen.moveTo((cx + 40, cy - 40))
    pen.lineTo((cx + 260, cy - 40))
    pen.lineTo((cx + 260, cy + 40))
    pen.lineTo((cx + 120, cy + 40))
    pen.lineTo((cx + 120, cy + 120))
    pen.lineTo((cx + 40, cy + 120))
    pen.closePath()
    return g

def _create_H(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 120
    right = GLYPH_WIDTH - 120
    _rounded_rect(pen, left - 20, baseline, left + 60, cap, 18)
    _rounded_rect(pen, right - 60, baseline, right + 20, cap, 18)
    # crossbar
    mid = xh
    pen.moveTo((left + 60, mid + 20))
    pen.lineTo((right - 60, mid + 20))
    pen.lineTo((right - 60, mid - 20))
    pen.lineTo((left + 60, mid - 20))
    pen.closePath()
    return g

def _create_I(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = GLYPH_WIDTH / 2 - 40
    right = GLYPH_WIDTH / 2 + 40
    _rounded_rect(pen, left, baseline, right, cap, 12)
    return g

def _create_J(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    top_left = GLYPH_WIDTH / 2 - 120
    top_right = GLYPH_WIDTH / 2 + 120
    pen.moveTo((top_left, cap - 40))
    pen.lineTo((top_right, cap - 40))
    pen.lineTo((top_right, cap - 100))
    pen.lineTo((top_left + 40, cap - 100))
    pen.lineTo((top_left + 40, baseline + 160))
    # hook
    pen.curveTo((top_left + 40, baseline + 80), (top_left - 40, baseline + 80), (top_left - 40, baseline + 160))
    pen.lineTo((top_left - 40, baseline + 200))
    pen.lineTo((top_left + 40, baseline + 200))
    pen.closePath()
    return g

def _create_K(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 120
    _rounded_rect(pen, left - 20, baseline, left + 60, cap, 18)
    # diagonals
    pen.moveTo((left + 60, xh + 160))
    pen.lineTo((GLYPH_WIDTH - 120, cap - 40))
    pen.lineTo((GLYPH_WIDTH - 120 - 40, cap - 40))
    pen.lineTo((left + 60, xh + 40))
    pen.closePath()
    pen.moveTo((left + 60, xh - 40))
    pen.lineTo((GLYPH_WIDTH - 120, baseline + 40))
    pen.lineTo((GLYPH_WIDTH - 120 - 40, baseline + 40))
    pen.lineTo((left + 60, xh - 160))
    pen.closePath()
    return g

def _create_L(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 120
    _rounded_rect(pen, left - 20, baseline, left + 60, cap, 18)
    pen.moveTo((left + 60, baseline + 40))
    pen.lineTo((GLYPH_WIDTH - 120, baseline + 40))
    pen.lineTo((GLYPH_WIDTH - 120, baseline))
    pen.lineTo((left + 60, baseline))
    pen.closePath()
    return g

def _create_M(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 120
    right = GLYPH_WIDTH - 120
    pen.moveTo((left, baseline))
    pen.lineTo((left + 60, cap))
    pen.lineTo((GLYPH_WIDTH / 2, xh))
    pen.lineTo((right - 60, cap))
    pen.lineTo((right, baseline))
    pen.lineTo((right - 60, baseline))
    pen.lineTo((GLYPH_WIDTH / 2, xh - 40))
    pen.lineTo((left + 60, baseline))
    pen.closePath()
    return g

def _create_N(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    left = 120
    right = GLYPH_WIDTH - 120
    _rounded_rect(pen, left - 20, baseline, left + 60, cap, 18)
    pen.moveTo((left + 60, cap))
    pen.lineTo((right - 60, baseline))
    pen.lineTo((right + 20, baseline))
    pen.lineTo((right - 20, cap))
    pen.lineTo((left + 60, cap))
    pen.closePath()
    _rounded_rect(pen, right - 60, baseline, right + 20, cap, 18)
    return g

def _create_O(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    cx = GLYPH_WIDTH / 2
    cy = 420
    _stroke_oval(pen, cx, cy, 260, 320, 80)
    return g

def _create_P(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    left = 120
    baseline, xh, cap, asc = _bar_y_positions()
    _rounded_rect(pen, left - 20, baseline, left + 60, cap, 18)
    _oval(pen, left + 180, cap - 220, 160, 140)
    # carve inner
    pen.moveTo((left + 80, cap - 80))
    pen.lineTo((left + 260, cap - 80))
    pen.lineTo((left + 260, cap - 260))
    pen.lineTo((left + 80, cap - 260))
    pen.closePath()
    return g

def _create_Q(font, code):
    g = _create_O(font, code)
    # add tail
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2 + 120, 200))
    pen.lineTo((GLYPH_WIDTH / 2 + 220, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 180, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 80, 200))
    pen.closePath()
    return g

def _create_R(font, code):
    g = _create_P(font, code)
    # add leg
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2 + 40, 320))
    pen.lineTo((GLYPH_WIDTH - 120, baseline := 0 + 40))
    pen.lineTo((GLYPH_WIDTH - 160, baseline))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 280))
    pen.closePath()
    return g

def _create_S(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    cx = GLYPH_WIDTH / 2
    cy = 420
    # S as two opposing ovals carved
    _oval(pen, cx + 40, cy + 120, 180, 120)
    _oval(pen, cx - 40, cy - 120, 180, 120)
    # carve middle to create S shape
    pen.moveTo((cx + 220, cy + 120))
    pen.lineTo((cx - 220, cy - 120))
    pen.lineTo((cx - 180, cy - 160))
    pen.lineTo((cx + 180, cy + 80))
    pen.closePath()
    return g

def _create_T(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    pen.moveTo((120, cap - 40))
    pen.lineTo((GLYPH_WIDTH - 120, cap - 40))
    pen.lineTo((GLYPH_WIDTH - 120, cap - 100))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, cap - 100))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, baseline))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, baseline))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, cap - 100))
    pen.lineTo((120, cap - 100))
    pen.closePath()
    return g

def _create_U(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    left = 120
    right = GLYPH_WIDTH - 120
    baseline, xh, cap, asc = _bar_y_positions()
    pen.moveTo((left, cap - 40))
    pen.lineTo((left + 40, baseline + 200))
    pen.curveTo((GLYPH_WIDTH / 2 - 40, baseline + 40), (GLYPH_WIDTH / 2 + 40, baseline + 40), (right - 40, baseline + 200))
    pen.lineTo((right, cap - 40))
    pen.closePath()
    return g

def _create_V(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, cap := 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2, 80))
    pen.lineTo((GLYPH_WIDTH - 120, cap))
    pen.lineTo((GLYPH_WIDTH - 120 - 40, cap))
    pen.lineTo((GLYPH_WIDTH / 2, 160))
    pen.lineTo((120 + 40, cap))
    pen.closePath()
    return g

def _create_W(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 - 80, 120))
    pen.lineTo((GLYPH_WIDTH / 2, 420))
    pen.lineTo((GLYPH_WIDTH / 2 + 80, 120))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 160, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 160))
    pen.lineTo((GLYPH_WIDTH / 2, 520))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 160))
    pen.lineTo((120 + 40, 700 - 40))
    pen.closePath()
    return g

def _create_X(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 420))
    pen.lineTo((120, 80))
    pen.lineTo((180, 80))
    pen.lineTo((GLYPH_WIDTH / 2, 360))
    pen.lineTo((GLYPH_WIDTH - 180, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 180, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2, 460))
    pen.lineTo((180, 700 - 40))
    pen.closePath()
    return g

def _create_Y(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2, 420))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 160, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2, 460))
    pen.lineTo((160, 700 - 40))
    pen.closePath()
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 420))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420))
    pen.closePath()
    return g

def _create_Z(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((120 + 80, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 40))
    pen.lineTo((120, 40))
    pen.closePath()
    return g

# Digits 0-9 (geometric)
def _create_0(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _stroke_oval(pen, GLYPH_WIDTH / 2, 420, 240, 320, 80)
    return g

def _create_1(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 80))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 80))
    pen.closePath()
    pen.moveTo((GLYPH_WIDTH / 2 - 120, 120))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 80))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 160))
    pen.lineTo((GLYPH_WIDTH / 2 - 120, 200))
    pen.closePath()
    return g

def _create_2(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((120 + 80, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 160))
    pen.lineTo((120 + 80, 160))
    pen.closePath()
    return g

def _create_3(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _oval(pen, GLYPH_WIDTH / 2 + 40, 520, 160, 140)
    _oval(pen, GLYPH_WIDTH / 2 + 40, 280, 160, 140)
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 220, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 220, 640))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 640))
    pen.closePath()
    return g

def _create_4(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH - 200, 80))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 360))
    pen.closePath()
    return g

def _create_5(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((120, 700 - 40))
    pen.lineTo((120, 520))
    pen.lineTo((GLYPH_WIDTH - 120, 520))
    pen.lineTo((GLYPH_WIDTH - 120, 440))
    pen.lineTo((120, 440))
    pen.lineTo((120, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 120))
    pen.lineTo((200, 120))
    pen.closePath()
    return g

def _create_6(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _oval(pen, GLYPH_WIDTH / 2 - 40, 360, 200, 260)
    pen.moveTo((GLYPH_WIDTH / 2 + 160, 560))
    pen.lineTo((GLYPH_WIDTH / 2 + 80, 640))
    pen.lineTo((GLYPH_WIDTH / 2 - 80, 640))
    pen.lineTo((GLYPH_WIDTH / 2 - 160, 560))
    pen.closePath()
    return g

def _create_7(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 80))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 80))
    pen.closePath()
    return g

def _create_8(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _stroke_oval(pen, GLYPH_WIDTH / 2, 520, 160, 140, 60)
    _stroke_oval(pen, GLYPH_WIDTH / 2, 280, 160, 140, 60)
    return g

def _create_9(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _oval(pen, GLYPH_WIDTH / 2 + 40, 520, 200, 260)
    pen.moveTo((GLYPH_WIDTH / 2 - 160, 320))
    pen.lineTo((GLYPH_WIDTH / 2 - 80, 240))
    pen.lineTo((GLYPH_WIDTH / 2 + 80, 240))
    pen.lineTo((GLYPH_WIDTH / 2 + 160, 320))
    pen.closePath()
    return g

# Symbols (a subset approximated)
def _create_percent(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    # two circles and a slash
    _circle(pen, 160, 520, 60)
    _circle(pen, GLYPH_WIDTH - 160, 160, 60)
    pen.moveTo((140, 140))
    pen.lineTo((GLYPH_WIDTH - 140, 640))
    pen.lineTo((GLYPH_WIDTH - 120, 640))
    pen.lineTo((120, 140))
    pen.closePath()
    return g

def _create_per_mille(font, code):
    # approximate per mille as percent with extra small circle
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _create_percent(font, ord('%'))
    _circle(pen, GLYPH_WIDTH - 120, 520, 30)
    return g

def _create_dot(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _circle(pen, GLYPH_WIDTH / 2, 200, 30)
    return g

def _create_comma(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _circle(pen, GLYPH_WIDTH / 2 + 40, 160, 30)
    pen.moveTo((GLYPH_WIDTH / 2 + 40, 120))
    pen.lineTo((GLYPH_WIDTH / 2 + 20, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 60, 80))
    pen.closePath()
    return g

def _create_colon(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _circle(pen, GLYPH_WIDTH / 2, 520, 30)
    _circle(pen, GLYPH_WIDTH / 2, 200, 30)
    return g

def _create_semicolon(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _circle(pen, GLYPH_WIDTH / 2, 520, 30)
    _circle(pen, GLYPH_WIDTH / 2 + 40, 160, 30)
    pen.moveTo((GLYPH_WIDTH / 2 + 40, 120))
    pen.lineTo((GLYPH_WIDTH / 2 + 20, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 60, 80))
    pen.closePath()
    return g

def _create_exclam(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 160))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 160))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 520))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 520))
    pen.closePath()
    _circle(pen, GLYPH_WIDTH / 2, 80, 30)
    return g

def _create_question(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    # simple question mark: curve and dot
    pen.moveTo((GLYPH_WIDTH / 2 - 80, 560))
    pen.curveTo((GLYPH_WIDTH / 2 - 40, 700), (GLYPH_WIDTH / 2 + 80, 700), (GLYPH_WIDTH / 2 + 80, 620))
    pen.curveTo((GLYPH_WIDTH / 2 + 80, 560), (GLYPH_WIDTH / 2 - 20, 520), (GLYPH_WIDTH / 2 - 20, 460))
    pen.lineTo((GLYPH_WIDTH / 2 - 20, 420))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 460))
    pen.closePath()
    _circle(pen, GLYPH_WIDTH / 2, 120, 30)
    return g

def _create_paren(font, code, left=True):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    if left:
        pen.moveTo((GLYPH_WIDTH / 2 + 120, 700 - 40))
        pen.curveTo((GLYPH_WIDTH / 2 - 40, 520), (GLYPH_WIDTH / 2 - 40, 160), (GLYPH_WIDTH / 2 + 120, 80))
        pen.lineTo((GLYPH_WIDTH / 2 + 160, 80))
        pen.curveTo((GLYPH_WIDTH / 2 - 20, 160), (GLYPH_WIDTH / 2 - 20, 520), (GLYPH_WIDTH / 2 + 160, 700 - 40))
        pen.closePath()
    else:
        pen.moveTo((GLYPH_WIDTH / 2 - 120, 700 - 40))
        pen.curveTo((GLYPH_WIDTH / 2 + 40, 520), (GLYPH_WIDTH / 2 + 40, 160), (GLYPH_WIDTH / 2 - 120, 80))
        pen.lineTo((GLYPH_WIDTH / 2 - 160, 80))
        pen.curveTo((GLYPH_WIDTH / 2 + 20, 160), (GLYPH_WIDTH / 2 + 20, 520), (GLYPH_WIDTH / 2 - 160, 700 - 40))
        pen.closePath()
    return g

def _create_bracket(font, code, left=True):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    baseline, xh, cap, asc = _bar_y_positions()
    if left:
        pen.moveTo((GLYPH_WIDTH / 2 + 120, cap))
        pen.lineTo((GLYPH_WIDTH / 2 + 40, cap))
        pen.lineTo((GLYPH_WIDTH / 2 + 40, baseline))
        pen.lineTo((GLYPH_WIDTH / 2 + 120, baseline))
        pen.closePath()
    else:
        pen.moveTo((GLYPH_WIDTH / 2 - 120, cap))
        pen.lineTo((GLYPH_WIDTH / 2 - 40, cap))
        pen.lineTo((GLYPH_WIDTH / 2 - 40, baseline))
        pen.lineTo((GLYPH_WIDTH / 2 - 120, baseline))
        pen.closePath()
    return g

def _create_brace(font, code, left=True):
    # simple approximation of brace
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    if left:
        pen.moveTo((GLYPH_WIDTH / 2 + 120, 700 - 40))
        pen.curveTo((GLYPH_WIDTH / 2 + 40, 560), (GLYPH_WIDTH / 2 + 40, 440), (GLYPH_WIDTH / 2 + 120, 320))
        pen.curveTo((GLYPH_WIDTH / 2 + 40, 200), (GLYPH_WIDTH / 2 + 40, 80), (GLYPH_WIDTH / 2 + 120, 80))
        pen.lineTo((GLYPH_WIDTH / 2 + 160, 80))
        pen.curveTo((GLYPH_WIDTH / 2 + 80, 200), (GLYPH_WIDTH / 2 + 80, 320), (GLYPH_WIDTH / 2 + 160, 440))
        pen.curveTo((GLYPH_WIDTH / 2 + 80, 560), (GLYPH_WIDTH / 2 + 80, 700 - 40), (GLYPH_WIDTH / 2 + 160, 700 - 40))
        pen.closePath()
    else:
        pen.moveTo((GLYPH_WIDTH / 2 - 120, 700 - 40))
        pen.curveTo((GLYPH_WIDTH / 2 - 40, 560), (GLYPH_WIDTH / 2 - 40, 440), (GLYPH_WIDTH / 2 - 120, 320))
        pen.curveTo((GLYPH_WIDTH / 2 - 40, 200), (GLYPH_WIDTH / 2 - 40, 80), (GLYPH_WIDTH / 2 - 120, 80))
        pen.lineTo((GLYPH_WIDTH / 2 - 160, 80))
        pen.curveTo((GLYPH_WIDTH / 2 - 80, 200), (GLYPH_WIDTH / 2 - 80, 320), (GLYPH_WIDTH / 2 - 160, 440))
        pen.curveTo((GLYPH_WIDTH / 2 - 80, 560), (GLYPH_WIDTH / 2 - 80, 700 - 40), (GLYPH_WIDTH / 2 - 160, 700 - 40))
        pen.closePath()
    return g

def _create_plus(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 420 + 120))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420 + 120))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420 + 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 120, 420 + 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 120, 420 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420 - 120))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 420 - 120))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 420 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 - 120, 420 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 - 120, 420 + 40))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 420 + 40))
    pen.closePath()
    return g

def _create_minus(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 420 + 40))
    pen.lineTo((GLYPH_WIDTH - 120, 420 + 40))
    pen.lineTo((GLYPH_WIDTH - 120, 420 - 40))
    pen.lineTo((120, 420 - 40))
    pen.closePath()
    return g

def _create_times(font, code):
    # multiplication × as an X
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2, 420))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 160, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2, 460))
    pen.lineTo((160, 700 - 40))
    pen.closePath()
    pen.moveTo((120, 80))
    pen.lineTo((GLYPH_WIDTH / 2, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH - 160, 80))
    pen.lineTo((GLYPH_WIDTH / 2, 320))
    pen.lineTo((160, 80))
    pen.closePath()
    return g

def _create_divide(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _circle(pen, GLYPH_WIDTH / 2, 520, 30)
    _circle(pen, GLYPH_WIDTH / 2, 200, 30)
    pen.moveTo((120, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 320))
    pen.lineTo((120, 320))
    pen.closePath()
    return g

def _create_equal(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 460))
    pen.lineTo((GLYPH_WIDTH - 120, 460))
    pen.lineTo((GLYPH_WIDTH - 120, 420))
    pen.lineTo((120, 420))
    pen.closePath()
    pen.moveTo((120, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 320))
    pen.lineTo((120, 320))
    pen.closePath()
    return g

def _create_tilde(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 520))
    pen.curveTo((220, 600), (380, 460), (480, 540))
    pen.curveTo((520, 560), (580, 520), (GLYPH_WIDTH - 120, 520))
    pen.lineTo((GLYPH_WIDTH - 120, 480))
    pen.curveTo((580, 500), (520, 540), (480, 520))
    pen.curveTo((380, 440), (220, 580), (120, 500))
    pen.closePath()
    return g

def _create_at(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _oval(pen, GLYPH_WIDTH / 2, 420, 260, 260)
    _circle(pen, GLYPH_WIDTH / 2 + 80, 420, 80)
    return g

def _create_hash(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    # two vertical bars
    pen.moveTo((GLYPH_WIDTH / 2 - 160, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 80))
    pen.lineTo((GLYPH_WIDTH / 2 - 80, 80))
    pen.closePath()
    pen.moveTo((GLYPH_WIDTH / 2 + 40, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 80, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 160, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 120, 80))
    pen.closePath()
    # two horizontal bars
    pen.moveTo((120, 520))
    pen.lineTo((GLYPH_WIDTH - 120, 520))
    pen.lineTo((GLYPH_WIDTH - 120, 480))
    pen.lineTo((120, 480))
    pen.closePath()
    pen.moveTo((120, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 360))
    pen.lineTo((GLYPH_WIDTH - 120, 320))
    pen.lineTo((120, 320))
    pen.closePath()
    return g

def _create_dollar(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 700 - 40))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 80))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 80))
    pen.closePath()
    _oval(pen, GLYPH_WIDTH / 2, 420, 160, 260)
    return g

def _create_ampersand(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _oval(pen, GLYPH_WIDTH / 2 - 40, 420, 160, 120)
    _oval(pen, GLYPH_WIDTH / 2 + 80, 280, 120, 100)
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 520))
    pen.lineTo((GLYPH_WIDTH / 2 + 160, 120))
    pen.lineTo((GLYPH_WIDTH / 2 + 120, 120))
    pen.lineTo((GLYPH_WIDTH / 2 - 80, 480))
    pen.closePath()
    return g

def _create_star(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    cx = GLYPH_WIDTH / 2
    cy = 420
    r = 160
    # simple 5-point star
    pts = []
    for i in range(5):
        angle = i * 2 * 3.14159265 / 5 - 3.14159265 / 2
        pts.append((cx + r * 0.95 * __import__('math').cos(angle), cy + r * 0.95 * __import__('math').sin(angle)))
    pen.moveTo(pts[0])
    pen.lineTo(pts[2])
    pen.lineTo(pts[4])
    pen.lineTo(pts[1])
    pen.lineTo(pts[3])
    pen.closePath()
    return g

def _create_slash(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 80))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 160, 700 - 40))
    pen.lineTo((160, 80))
    pen.closePath()
    return g

def _create_backslash(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH - 160, 80))
    pen.lineTo((160, 700 - 40))
    pen.closePath()
    return g

# Greek uppercase mapping: reuse Latin shapes where visually similar
GREEK_MAP = {
    0x0391: _create_A,  # Α
    0x0392: _create_B,  # Β
    0x0393: lambda f,c: _create_Lambda_like(f,c) if False else _create_LikeGamma(f,c)  # placeholder mapping below
}

# We'll implement a few Greek-specific shapes and fallback to Latin equivalents
def _create_Greek_simple(font, code, latin_creator):
    # fallback: create glyph using latin equivalent creator
    return latin_creator(font, code)

def _create_Greek_Delta(font, code):
    # Δ triangle
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((120, 80))
    pen.closePath()
    # crossbar
    pen.moveTo((GLYPH_WIDTH / 2 - 120, 360))
    pen.lineTo((GLYPH_WIDTH / 2 + 120, 360))
    pen.lineTo((GLYPH_WIDTH / 2 + 120, 320))
    pen.lineTo((GLYPH_WIDTH / 2 - 120, 320))
    pen.closePath()
    return g

def _create_Greek_Pi(font, code):
    # Π like H with top bar
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    left = 120
    right = GLYPH_WIDTH - 120
    pen.moveTo((left, 700 - 40))
    pen.lineTo((right, 700 - 40))
    pen.lineTo((right, 640))
    pen.lineTo((right - 80, 640))
    pen.lineTo((right - 80, 80))
    pen.lineTo((left + 80, 80))
    pen.lineTo((left + 80, 640))
    pen.lineTo((left, 640))
    pen.closePath()
    return g

def _create_Greek_Sigma(font, code):
    # Σ as three bars
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((120, 700 - 40))
    pen.lineTo((120, 640))
    pen.lineTo((GLYPH_WIDTH - 120, 640))
    pen.lineTo((GLYPH_WIDTH - 120, 520))
    pen.lineTo((120, 520))
    pen.lineTo((120, 460))
    pen.lineTo((GLYPH_WIDTH - 120, 460))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((GLYPH_WIDTH - 160, 80))
    pen.lineTo((160, 460))
    pen.lineTo((GLYPH_WIDTH - 160, 460))
    pen.closePath()
    return g

def _create_Greek_Omega(font, code):
    # Ω as O with feet
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _stroke_oval(pen, GLYPH_WIDTH / 2, 420, 260, 260, 80)
    pen.moveTo((GLYPH_WIDTH / 2 - 120, 80))
    pen.lineTo((GLYPH_WIDTH / 2 - 40, 200))
    pen.lineTo((GLYPH_WIDTH / 2 - 80, 200))
    pen.lineTo((GLYPH_WIDTH / 2 - 160, 80))
    pen.closePath()
    pen.moveTo((GLYPH_WIDTH / 2 + 120, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 200))
    pen.lineTo((GLYPH_WIDTH / 2 + 80, 200))
    pen.lineTo((GLYPH_WIDTH / 2 + 160, 80))
    pen.closePath()
    return g

# Math symbols
def _create_infinity(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _oval(pen, GLYPH_WIDTH / 2 - 120, 420, 120, 80)
    _oval(pen, GLYPH_WIDTH / 2 + 120, 420, 120, 80)
    pen.moveTo((GLYPH_WIDTH / 2 - 40, 420))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 420))
    pen.closePath()
    return g

def _create_sqrt(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    # radical: check-like shape
    pen.moveTo((120, 360))
    pen.lineTo((220, 240))
    pen.lineTo((320, 420))
    pen.lineTo((GLYPH_WIDTH - 120, 420))
    pen.lineTo((GLYPH_WIDTH - 120, 480))
    pen.lineTo((320, 480))
    pen.lineTo((220, 300))
    pen.lineTo((120, 420))
    pen.closePath()
    return g

def _create_integral(font, code):
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    # elongated S-like shape
    pen.moveTo((GLYPH_WIDTH / 2 + 80, 700 - 40))
    pen.curveTo((GLYPH_WIDTH / 2 - 40, 560), (GLYPH_WIDTH / 2 - 40, 440), (GLYPH_WIDTH / 2 + 80, 320))
    pen.curveTo((GLYPH_WIDTH / 2 + 200, 240), (GLYPH_WIDTH / 2 + 200, 160), (GLYPH_WIDTH / 2 + 80, 80))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 80))
    pen.curveTo((GLYPH_WIDTH / 2 + 160, 160), (GLYPH_WIDTH / 2 + 160, 240), (GLYPH_WIDTH / 2 + 40, 320))
    pen.curveTo((GLYPH_WIDTH / 2 - 80, 440), (GLYPH_WIDTH / 2 - 80, 560), (GLYPH_WIDTH / 2 + 40, 700 - 40))
    pen.closePath()
    return g

def _create_partial(font, code):
    # ∂ stylized as small d-like shape
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _oval(pen, GLYPH_WIDTH / 2 - 40, 420, 140, 160)
    pen.moveTo((GLYPH_WIDTH / 2 + 40, 420))
    pen.lineTo((GLYPH_WIDTH / 2 + 160, 420))
    pen.lineTo((GLYPH_WIDTH / 2 + 160, 360))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 360))
    pen.closePath()
    return g

def _create_nabla(font, code):
    # ∇ triangle
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH / 2, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 80))
    pen.lineTo((120, 80))
    pen.closePath()
    return g

def _create_Sigma(font, code):
    return _create_Greek_Sigma(font, code)

def _create_Product(font, code):
    # ∏ like Pi but taller
    return _create_Greek_Pi(font, code)

def _create_approx(font, code):
    # ≈ two wavy lines
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 520))
    pen.curveTo((220, 600), (380, 460), (480, 540))
    pen.curveTo((520, 560), (580, 520), (GLYPH_WIDTH - 120, 520))
    pen.closePath()
    pen.moveTo((120, 420))
    pen.curveTo((220, 500), (380, 360), (480, 440))
    pen.curveTo((520, 460), (580, 420), (GLYPH_WIDTH - 120, 420))
    pen.closePath()
    return g

def _create_not_equal(font, code):
    # ≠ equals with slash
    g = _create_equal(font, code)
    pen = g.glyphPen()
    pen.moveTo((120, 520))
    pen.lineTo((GLYPH_WIDTH - 120, 320))
    pen.lineTo((GLYPH_WIDTH - 120, 360))
    pen.lineTo((120, 560))
    pen.closePath()
    return g

def _create_identical(font, code):
    # ≡ three bars
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    for y in (480, 420, 360):
        pen.moveTo((120, y + 20))
        pen.lineTo((GLYPH_WIDTH - 120, y + 20))
        pen.lineTo((GLYPH_WIDTH - 120, y - 20))
        pen.lineTo((120, y - 20))
        pen.closePath()
    return g

def _create_le(font, code):
    # ≤
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 420))
    pen.lineTo((GLYPH_WIDTH / 2, 520))
    pen.lineTo((GLYPH_WIDTH - 120, 420))
    pen.lineTo((GLYPH_WIDTH - 120, 360))
    pen.lineTo((GLYPH_WIDTH / 2, 460))
    pen.lineTo((120, 360))
    pen.closePath()
    return g

def _create_ge(font, code):
    # ≥ mirror of ≤
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((GLYPH_WIDTH - 120, 420))
    pen.lineTo((GLYPH_WIDTH / 2, 520))
    pen.lineTo((120, 420))
    pen.lineTo((120, 360))
    pen.lineTo((GLYPH_WIDTH / 2, 460))
    pen.lineTo((GLYPH_WIDTH - 120, 360))
    pen.closePath()
    return g

def _create_pm(font, code):
    # ± plus minus: plus on top, minus below
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    _create_plus(font, ord('+'))
    pen = g.glyphPen()
    pen.moveTo((120, 320))
    pen.lineTo((GLYPH_WIDTH - 120, 320))
    pen.lineTo((GLYPH_WIDTH - 120, 280))
    pen.lineTo((120, 280))
    pen.closePath()
    return g

# Map creators for Latin A-Z
LATIN_CREATORS = {
    'A': _create_A, 'B': _create_B, 'C': _create_C, 'D': _create_D, 'E': _create_E,
    'F': _create_F, 'G': _create_G, 'H': _create_H, 'I': _create_I, 'J': _create_J,
    'K': _create_K, 'L': _create_L, 'M': _create_M, 'N': _create_N, 'O': _create_O,
    'P': _create_P, 'Q': _create_Q, 'R': _create_R, 'S': _create_S, 'T': _create_T,
    'U': _create_U, 'V': _create_V, 'W': _create_W, 'X': _create_X, 'Y': _create_Y,
    'Z': _create_Z
}

DIGIT_CREATORS = {
    '0': _create_0, '1': _create_1, '2': _create_2, '3': _create_3, '4': _create_4,
    '5': _create_5, '6': _create_6, '7': _create_7, '8': _create_8, '9': _create_9
}

SYMBOL_CREATORS = {
    '%': _create_percent,
    '\u2030': _create_per_mille,  # per mille
    '.': _create_dot,
    ',': _create_comma,
    ':': _create_colon,
    ';': _create_semicolon,
    '!': _create_exclam,
    '?': _create_question,
    '(': lambda f,c: _create_paren(f,c,left=True),
    ')': lambda f,c: _create_paren(f,c,left=False),
    '[': lambda f,c: _create_bracket(f,c,left=True),
    ']': lambda f,c: _create_bracket(f,c,left=False),
    '{': lambda f,c: _create_brace(f,c,left=True),
    '}': lambda f,c: _create_brace(f,c,left=False),
    '+': _create_plus,
    '-': _create_minus,
    '×': _create_times,
    '÷': _create_divide,
    '=': _create_equal,
    '~': _create_tilde,
    '@': _create_at,
    '#': _create_hash,
    '$': _create_dollar,
    '&': _create_ampersand,
    '*': _create_star,
    '/': _create_slash,
    '\\': _create_backslash
}

# Greek uppercase creators mapping (explicit for key ones, fallback to Latin shapes)
GREEK_CREATORS = {
    0x0391: _create_A,  # Α
    0x0392: _create_B,  # Β
    0x0393: lambda f,c: _create_LikeGamma(f,c) if False else _create_LikeGamma_fallback(f,c)  # placeholder fallback
}

# We'll implement a fallback for Gamma-like shapes and other Greek letters by mapping to visually similar Latin glyphs
def _create_LikeGamma_fallback(font, code):
    # simple Gamma: like an L with top bar
    g = font.createChar(code)
    g.width = GLYPH_WIDTH
    pen = g.glyphPen()
    pen.moveTo((120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 700 - 40))
    pen.lineTo((GLYPH_WIDTH - 120, 640))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 640))
    pen.lineTo((GLYPH_WIDTH / 2 + 40, 80))
    pen.lineTo((120, 80))
    pen.closePath()
    return g

# For simplicity, map most Greek uppercase to Latin equivalents where shapes are similar
GREEK_EQUIVALENTS = {
    0x0391: 'A', 0x0392: 'B', 0x0393: None, 0x0394: None, 0x0395: 'E', 0x0396: 'Z',
    0x0397: 'H', 0x0398: None, 0x0399: 'I', 0x039A: 'K', 0x039B: None, 0x039C: 'M',
    0x039D: 'N', 0x039E: None, 0x039F: 'O', 0x03A0: None, 0x03A1: 'P', 0x03A3: None,
    0x03A4: 'T', 0x03A5: 'Y', 0x03A6: None, 0x03A7: 'X', 0x03A8: None, 0x03A9: None
}

# Math creators mapping
MATH_CREATORS = {
    '∞': _create_infinity,
    '√': _create_sqrt,
    '∫': _create_integral,
    '∂': _create_partial,
    '∇': _create_nabla,
    'Σ': _create_Sigma,
    '∏': _create_Product,
    '≈': _create_approx,
    '≠': _create_not_equal,
    '≡': _create_identical,
    '≤': _create_le,
    '≥': _create_ge,
    '±': _create_pm
}

# Utility to create glyph by unicode codepoint and creator function
def _create_by_code(font, codepoint, creator):
    try:
        return creator(font, codepoint)
    except Exception:
        # If creator expects char code differently, try calling with char
        try:
            return creator(font, chr(codepoint))
        except Exception:
            # best-effort: create empty glyph with width
            g = font.createChar(codepoint)
            g.width = GLYPH_WIDTH
            return g

def build(font, cfg):
    # Set font metrics
    try:
        font.upm = UPM
    except Exception:
        pass
    try:
        font.ascent = ASCENT
        font.descent = -DESCENT if DESCENT < 0 else DESCENT
    except Exception:
        # some environments use different attribute names
        try:
            font.ascent = ASCENT
            font.descent = DESCENT
        except Exception:
            pass

    # Create Latin uppercase A-Z
    for ch, creator in LATIN_CREATORS.items():
        code = ord(ch)
        _create_by_code(font, code, creator)

    # Create digits 0-9
    for ch, creator in DIGIT_CREATORS.items():
        code = ord(ch)
        _create_by_code(font, code, creator)

    # Create symbols
    for sym, creator in SYMBOL_CREATORS.items():
        code = ord(sym)
        _create_by_code(font, code, creator)

    # Per-mille symbol (U+2030)
    try:
        _create_by_code(font, 0x2030, _create_per_mille)
    except Exception:
        pass

    # Math symbols
    for sym, creator in MATH_CREATORS.items():
        code = ord(sym)
        _create_by_code(font, code, creator)

    # Additional math and symbol codepoints that may be requested explicitly
    extra_symbols = {
        '%': ord('%'),
        '\u2030': 0x2030,
        '.': ord('.'),
        ',': ord(','),
        ':': ord(':'),
        ';': ord(';'),
        '!': ord('!'),
        '?': ord('?'),
        '(': ord('('),
        ')': ord(')'),
        '[': ord('['),
        ']': ord(']'),
        '{': ord('{'),
        '}': ord('}'),
        '+': ord('+'),
        '-': ord('-'),
        '×': ord('×'),
        '÷': ord('÷'),
        '=': ord('='),
        '~': ord('~'),
        '@': ord('@'),
        '#': ord('#'),
        '$': ord('$'),
        '&': ord('&'),
        '*': ord('*'),
        '/': ord('/'),
        '\\': ord('\\')
    }
    for sym, code in extra_symbols.items():
        if code in font:
            continue
        creator = SYMBOL_CREATORS.get(sym)
        if creator:
            _create_by_code(font, code, creator)

    # Greek uppercase: create by mapping to Latin equivalents or specific Greek creators
    greek_range = list(range(0x0391, 0x03AA))  # includes uppercase Greek
    for code in greek_range:
        # Skip lowercase Greek (not in this range) and ensure uppercase only
        if code < 0x0391 or code > 0x03A9:
            continue
        # Avoid creating lowercase alpha/omega etc.
        eq = GREEK_EQUIVALENTS.get(code)
        if eq:
            creator = LATIN_CREATORS.get(eq)
            if creator:
                _create_by_code(font, code, creator)
                continue
        # Specific Greek shapes
        if code == 0x0394:  # Δ
            _create_by_code(font, code, _create_Greek_Delta)
        elif code == 0x03A0:  # Π
            _create_by_code(font, code, _create_Greek_Pi)
        elif code == 0x03A3:  # Σ
            _create_by_code(font, code, _create_Greek_Sigma)
        elif code == 0x03A9:  # Ω
            _create_by_code(font, code, _create_Greek_Omega)
        else:
            # fallback: try to map visually to Latin by name similarity
            # map common ones
            fallback_map = {
                0x0391: 'A', 0x0395: 'E', 0x0396: 'Z', 0x0397: 'H', 0x0399: 'I',
                0x039A: 'K', 0x039C: 'M', 0x039D: 'N', 0x039F: 'O', 0x03A1: 'P',
                0x03A4: 'T', 0x03A5: 'Y', 0x03A7: 'X'
            }
            if code in fallback_map:
                creator = LATIN_CREATORS.get(fallback_map[code])
                if creator:
                    _create_by_code(font, code, creator)
                    continue
            # last resort: create empty glyph with width
            if not code in font:
                g = font.createChar(code)
                g.width = GLYPH_WIDTH

    # Ensure required math symbols exist; if not, create placeholders
    required_math = ['∞', '√', '∫', '∂', '∇', 'Σ', '∏', '≈', '≠', '≡', '≤', '≥', '±']
    for sym in required_math:
        code = ord(sym)
        if not code in font:
            creator = MATH_CREATORS.get(sym)
            if creator:
                _create_by_code(font, code, creator)
            else:
                # placeholder: simple box
                g = font.createChar(code)
                g.width = GLYPH_WIDTH
                pen = g.glyphPen()
                _rounded_rect(pen, 160, 160, GLYPH_WIDTH - 160, 640, 20)

    # Final pass: set width for any created glyphs without width
    for glyph in font.glyphs():
        try:
            if glyph.width == 0:
                glyph.width = GLYPH_WIDTH
        except Exception:
            pass
