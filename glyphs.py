"""
glyphs.py
=========
各文字を「build_X(c) -> (RecordingPen, advance_width)」という関数で定義する。
c は config モジュール（STROKE_WIDTH等の設計値）。

すべて bar_path（直線）と bowl/ellipse（曲線）の組み合わせのみで構成。
Phase1のゴールは「完成度よりも実際に動くこと」なので、字形は幾何学的で
単純化されたスケッチレベル（後述README参照）。
"""

from primitives import bar_path, rect_path, ellipse_path, bowl, quadrant_bite, combine


# =====================================================================
# 大文字 A-Z
# =====================================================================
def build_A(c):
    sw = c.STROKE_WIDTH
    top = (300, c.CAP_HEIGHT)
    bl, br = (60, 0), (540, 0)
    t = 0.42
    xl = bl[0] + (top[0] - bl[0]) * t
    xr = br[0] + (top[0] - br[0]) * t
    y = c.CAP_HEIGHT * t
    pos = [
        bar_path(*bl, *top, sw),
        bar_path(*br, *top, sw),
        bar_path(xl, y, xr, y, sw),
    ]
    return combine(pos), 600


def build_B(c):
    sw = c.STROKE_WIDTH
    stem_x = 60
    pos = [bar_path(stem_x, 0, stem_x, c.CAP_HEIGHT, sw)]
    neg = []
    for cy, r in [(525, 175), (175, 175)]:
        p, n = bowl(stem_x, cy, r, r, sw, open_side="left")
        pos += p
        neg += n
    return combine(pos, neg), 560


def build_C(c):
    sw = c.STROKE_WIDTH
    cx, cy = 300, c.CAP_HEIGHT / 2
    pos, neg = bowl(cx, cy, 260, cy, sw, open_side="right")
    return combine(pos, neg), 600


def build_D(c):
    sw = c.STROKE_WIDTH
    stem_x = 60
    pos = [bar_path(stem_x, 0, stem_x, c.CAP_HEIGHT, sw)]
    p, n = bowl(stem_x, 350, 350, 350, sw, open_side="left")
    pos += p
    return combine(pos, n), 620


def build_E(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.CAP_HEIGHT, sw),
        bar_path(60, c.CAP_HEIGHT - sw / 2, 460, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(60, c.CAP_HEIGHT / 2, 420, c.CAP_HEIGHT / 2, sw),
        bar_path(60, sw / 2, 460, sw / 2, sw),
    ]
    return combine(pos), 560


def build_F(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.CAP_HEIGHT, sw),
        bar_path(60, c.CAP_HEIGHT - sw / 2, 460, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(60, c.CAP_HEIGHT / 2, 420, c.CAP_HEIGHT / 2, sw),
    ]
    return combine(pos), 540


def build_G(c):
    sw = c.STROKE_WIDTH
    cx, cy, r = 300, c.CAP_HEIGHT / 2, 260
    pos, neg = bowl(cx, cy, r, cy, sw, open_side="right")
    pos.append(bar_path(cx + r - sw, 300, cx + r - sw, 350, sw))
    pos.append(bar_path(cx + 40, 300, cx + r - sw, 300, sw))
    return combine(pos, neg), 620


def build_H(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.CAP_HEIGHT, sw),
        bar_path(540, 0, 540, c.CAP_HEIGHT, sw),
        bar_path(60, c.CAP_HEIGHT / 2, 540, c.CAP_HEIGHT / 2, sw),
    ]
    return combine(pos), 600


def build_I(c):
    sw = c.STROKE_WIDTH
    pos = [bar_path(180, 0, 180, c.CAP_HEIGHT, sw)]
    return combine(pos), 360


def build_J(c):
    sw = c.STROKE_WIDTH
    stem_x = 380
    pos = [bar_path(stem_x, c.CAP_HEIGHT, stem_x, 175, sw)]
    p, n = bowl(280, 175, 175, 175, sw, open_side="top")
    pos += p
    return combine(pos, n), 520


def build_K(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.CAP_HEIGHT, sw),
        bar_path(60, 320, 520, c.CAP_HEIGHT, sw),
        bar_path(60, 320, 520, 0, sw),
    ]
    return combine(pos), 580


def build_L(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.CAP_HEIGHT, sw),
        bar_path(60, sw / 2, 460, sw / 2, sw),
    ]
    return combine(pos), 520


def build_M(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.CAP_HEIGHT, sw),
        bar_path(580, 0, 580, c.CAP_HEIGHT, sw),
        bar_path(60, c.CAP_HEIGHT, 320, 260, sw),
        bar_path(580, c.CAP_HEIGHT, 320, 260, sw),
    ]
    return combine(pos), 640


def build_N(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.CAP_HEIGHT, sw),
        bar_path(540, 0, 540, c.CAP_HEIGHT, sw),
        bar_path(60, c.CAP_HEIGHT, 540, 0, sw),
    ]
    return combine(pos), 600


def build_O(c):
    sw = c.STROKE_WIDTH
    cx, cy = 300, 350
    pos, neg = bowl(cx, cy, 260, 350, sw)
    return combine(pos, neg), 620


def build_P(c):
    sw = c.STROKE_WIDTH
    stem_x = 60
    pos = [bar_path(stem_x, 0, stem_x, c.CAP_HEIGHT, sw)]
    p, n = bowl(stem_x, 525, 175, 175, sw, open_side="left")
    pos += p
    return combine(pos, n), 560


def build_Q(c):
    sw = c.STROKE_WIDTH
    cx, cy = 300, 350
    pos, neg = bowl(cx, cy, 260, 350, sw)
    pos.append(bar_path(340, 60, 460, -60, sw))
    return combine(pos, neg), 620


def build_R(c):
    sw = c.STROKE_WIDTH
    stem_x = 60
    pos = [bar_path(stem_x, 0, stem_x, c.CAP_HEIGHT, sw)]
    p, n = bowl(stem_x, 525, 175, 175, sw, open_side="left")
    pos += p
    pos.append(bar_path(150, 380, 540, 0, sw))
    return combine(pos, n), 580


def build_S(c):
    sw = c.STROKE_WIDTH
    r = 165
    pos = [ellipse_path(300, 525, r, r), ellipse_path(300, 175, r, r)]
    neg = [
        ellipse_path(300, 525, r - sw, r - sw),
        quadrant_bite(300, 525, r, r, "left", "bottom"),
        ellipse_path(300, 175, r - sw, r - sw),
        quadrant_bite(300, 175, r, r, "right", "top"),
    ]
    return combine(pos, neg), 580


def build_T(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.CAP_HEIGHT - sw / 2, 540, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(300, 0, 300, c.CAP_HEIGHT, sw),
    ]
    return combine(pos), 600


def build_U(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.CAP_HEIGHT, 60, 175, sw),
        bar_path(540, c.CAP_HEIGHT, 540, 175, sw),
    ]
    p, n = bowl(300, 175, 240, 175, sw, open_side="top")
    pos += p
    return combine(pos, n), 600


def build_V(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.CAP_HEIGHT, 300, 0, sw),
        bar_path(540, c.CAP_HEIGHT, 300, 0, sw),
    ]
    return combine(pos), 600


def build_W(c):
    sw = c.STROKE_WIDTH
    pts = [(40, c.CAP_HEIGHT), (190, 0), (320, 480), (450, 0), (600, c.CAP_HEIGHT)]
    pos = [bar_path(*pts[i], *pts[i + 1], sw) for i in range(len(pts) - 1)]
    return combine(pos), 660


def build_X(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 540, c.CAP_HEIGHT, sw),
        bar_path(60, c.CAP_HEIGHT, 540, 0, sw),
    ]
    return combine(pos), 600


def build_Y(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.CAP_HEIGHT, 300, 350, sw),
        bar_path(540, c.CAP_HEIGHT, 300, 350, sw),
        bar_path(300, 350, 300, 0, sw),
    ]
    return combine(pos), 600


def build_Z(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.CAP_HEIGHT - sw / 2, 540, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(540, c.CAP_HEIGHT, 60, 0, sw),
        bar_path(60, sw / 2, 540, sw / 2, sw),
    ]
    return combine(pos), 600


# =====================================================================
# 小文字 a-z （x-height = 500 基準、昇部/降部あり）
# =====================================================================
def build_a(c):
    sw = c.STROKE_WIDTH
    cy = c.X_HEIGHT / 2
    pos, neg = bowl(250, cy, 195, cy, sw)
    pos.append(bar_path(420, 0, 420, c.X_HEIGHT, sw))
    return combine(pos, neg), 480


def build_b(c):
    sw = c.STROKE_WIDTH
    stem_x = 60
    cy = c.X_HEIGHT / 2
    pos = [bar_path(stem_x, 0, stem_x, c.ASCENDER, sw)]
    p, n = bowl(stem_x + 190, cy, 190, cy, sw)
    pos += p
    return combine(pos, n), 500


def build_c(c):
    sw = c.STROKE_WIDTH
    cy = c.X_HEIGHT / 2
    pos, neg = bowl(250, cy, 190, cy, sw, open_side="right")
    return combine(pos, neg), 480


def build_d(c):
    sw = c.STROKE_WIDTH
    stem_x = 440
    cy = c.X_HEIGHT / 2
    pos = [bar_path(stem_x, 0, stem_x, c.ASCENDER, sw)]
    p, n = bowl(stem_x - 190, cy, 190, cy, sw)
    pos += p
    return combine(pos, n), 500


def build_e(c):
    sw = c.STROKE_WIDTH
    cx, cy, rx, ry = 250, c.X_HEIGHT / 2, 210, c.X_HEIGHT / 2
    pos = [ellipse_path(cx, cy, rx, ry), bar_path(cx - rx + 10, cy, cx + rx - 10, cy, sw)]
    neg = [ellipse_path(cx, cy, rx - sw, ry - sw), rect_path(cx, cy - ry - 20, cx + rx + 20, cy)]
    return combine(pos, neg), 480


def build_f(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(250, 0, 250, 700, sw),
        bar_path(150, c.X_HEIGHT, 350, c.X_HEIGHT, sw),
        bar_path(250, 700 - sw / 2, 380, 700 - sw / 2, sw),
    ]
    return combine(pos), 400


def build_g(c):
    sw = c.STROKE_WIDTH
    stem_x = 440
    cy = c.X_HEIGHT / 2
    pos = [bar_path(stem_x, -140, stem_x, c.X_HEIGHT, sw)]
    p, n = bowl(stem_x - 190, cy, 190, cy, sw)
    pos += p
    p2, n2 = bowl(stem_x - 100, -140, 100, 100, sw, open_side="top")
    pos += p2
    n += n2
    return combine(pos, n), 500


def build_h(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.ASCENDER, sw),
        bar_path(60, c.X_HEIGHT, 440, c.X_HEIGHT, sw),
        bar_path(440, 0, 440, c.X_HEIGHT, sw),
    ]
    return combine(pos), 500


def build_i(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(250, 0, 250, c.X_HEIGHT, sw),
        ellipse_path(250, 650, 45, 45),
    ]
    return combine(pos), 340


def build_j(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(300, -140, 300, c.X_HEIGHT, sw),
        ellipse_path(300, 650, 45, 45),
    ]
    p, n = bowl(210, -140, 90, 90, sw, open_side="top")
    pos += p
    return combine(pos, n), 360


def build_k(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.ASCENDER, sw),
        bar_path(60, 260, 460, c.X_HEIGHT, sw),
        bar_path(60, 260, 460, 0, sw),
    ]
    return combine(pos), 500


def build_l(c):
    sw = c.STROKE_WIDTH
    pos = [bar_path(180, 0, 180, c.ASCENDER, sw)]
    return combine(pos), 340


def build_m(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.X_HEIGHT, sw),
        bar_path(60, c.X_HEIGHT, 260, c.X_HEIGHT, sw),
        bar_path(260, 0, 260, c.X_HEIGHT, sw),
        bar_path(260, c.X_HEIGHT, 460, c.X_HEIGHT, sw),
        bar_path(460, 0, 460, c.X_HEIGHT, sw),
    ]
    return combine(pos), 620


def build_n(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.X_HEIGHT, sw),
        bar_path(60, c.X_HEIGHT, 440, c.X_HEIGHT, sw),
        bar_path(440, 0, 440, c.X_HEIGHT, sw),
    ]
    return combine(pos), 500


def build_o(c):
    sw = c.STROKE_WIDTH
    cy = c.X_HEIGHT / 2
    pos, neg = bowl(250, cy, 190, cy, sw)
    return combine(pos, neg), 480


def build_p(c):
    sw = c.STROKE_WIDTH
    stem_x = 60
    cy = c.X_HEIGHT / 2
    pos = [bar_path(stem_x, -140, stem_x, c.X_HEIGHT, sw)]
    p, n = bowl(stem_x + 190, cy, 190, cy, sw)
    pos += p
    return combine(pos, n), 500


def build_q(c):
    sw = c.STROKE_WIDTH
    stem_x = 440
    cy = c.X_HEIGHT / 2
    pos = [bar_path(stem_x, -140, stem_x, c.X_HEIGHT, sw)]
    p, n = bowl(stem_x - 190, cy, 190, cy, sw)
    pos += p
    return combine(pos, n), 500


def build_r(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 60, c.X_HEIGHT, sw),
        bar_path(60, c.X_HEIGHT, 300, c.X_HEIGHT, sw),
    ]
    return combine(pos), 380


def build_s(c):
    sw = c.STROKE_WIDTH
    r = 130
    pos = [ellipse_path(250, 370, r, r), ellipse_path(250, 130, r, r)]
    neg = [
        ellipse_path(250, 370, r - sw, r - sw),
        quadrant_bite(250, 370, r, r, "left", "bottom"),
        ellipse_path(250, 130, r - sw, r - sw),
        quadrant_bite(250, 130, r, r, "right", "top"),
    ]
    return combine(pos, neg), 460


def build_t(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(220, 0, 220, 650, sw),
        bar_path(100, c.X_HEIGHT, 380, c.X_HEIGHT, sw),
    ]
    return combine(pos), 400


def build_u(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.X_HEIGHT, 60, 175, sw),
        bar_path(440, c.X_HEIGHT, 440, 175, sw),
    ]
    p, n = bowl(250, 175, 190, 175, sw, open_side="top")
    pos += p
    return combine(pos, n), 500


def build_v(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.X_HEIGHT, 250, 0, sw),
        bar_path(440, c.X_HEIGHT, 250, 0, sw),
    ]
    return combine(pos), 500


def build_w(c):
    sw = c.STROKE_WIDTH
    pts = [(40, c.X_HEIGHT), (160, 0), (250, 350), (340, 0), (460, c.X_HEIGHT)]
    pos = [bar_path(*pts[i], *pts[i + 1], sw) for i in range(len(pts) - 1)]
    return combine(pos), 500


def build_x(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, 0, 440, c.X_HEIGHT, sw),
        bar_path(60, c.X_HEIGHT, 440, 0, sw),
    ]
    return combine(pos), 500


def build_y(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.X_HEIGHT, 250, 0, sw),
        bar_path(440, c.X_HEIGHT, 120, -140, sw),
    ]
    return combine(pos), 500


def build_z(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.X_HEIGHT - sw / 2, 440, c.X_HEIGHT - sw / 2, sw),
        bar_path(440, c.X_HEIGHT, 60, 0, sw),
        bar_path(60, sw / 2, 440, sw / 2, sw),
    ]
    return combine(pos), 500


# =====================================================================
# 数字 0-9
# =====================================================================
def build_zero(c):
    sw = c.STROKE_WIDTH
    pos, neg = bowl(300, 350, 220, 340, sw)
    return combine(pos, neg), 600


def build_one(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(300, 0, 300, c.CAP_HEIGHT, sw),
        bar_path(220, 560, 300, 700, sw),
        bar_path(200, sw / 2, 400, sw / 2, sw),
    ]
    return combine(pos), 500


def build_two(c):
    sw = c.STROKE_WIDTH
    r = 140
    pos = [ellipse_path(300, 560, r, r), bar_path(420, 480, 80, 0, sw), bar_path(80, sw / 2, 520, sw / 2, sw)]
    neg = [ellipse_path(300, 560, r - sw, r - sw), quadrant_bite(300, 560, r, r, "left", "bottom")]
    return combine(pos, neg), 580


def build_three(c):
    sw = c.STROKE_WIDTH
    r = 150
    pos, neg = [], []
    for cy in (525, 175):
        p, n = bowl(300, cy, r, r, sw, open_side="left")
        pos += p
        neg += n
    return combine(pos, neg), 580


def build_four(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(420, c.CAP_HEIGHT, 420, 0, sw),
        bar_path(420, c.CAP_HEIGHT, 80, 230, sw),
        bar_path(80, 230, 460, 230, sw),
    ]
    return combine(pos), 560


def build_five(c):
    sw = c.STROKE_WIDTH
    r = 150
    pos = [
        bar_path(80, c.CAP_HEIGHT - sw / 2, 460, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(80, c.CAP_HEIGHT - sw / 2, 80, 400, sw),
        bar_path(80, 400, 300, 400, sw),
        ellipse_path(300, 200, r, r),
    ]
    neg = [ellipse_path(300, 200, r - sw, r - sw), quadrant_bite(300, 200, r, r, "left", "top")]
    return combine(pos, neg), 580


def build_six(c):
    sw = c.STROKE_WIDTH
    r = 190
    pos = [
        bar_path(460, c.CAP_HEIGHT, 150, 300, sw),
        ellipse_path(300, 190, r, r),
    ]
    neg = [ellipse_path(300, 190, r - sw, r - sw)]
    return combine(pos, neg), 600


def build_seven(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.CAP_HEIGHT - sw / 2, 540, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(540, c.CAP_HEIGHT, 260, 0, sw),
    ]
    return combine(pos), 600


def build_eight(c):
    sw = c.STROKE_WIDTH
    r = 155
    pos = [ellipse_path(300, 525, r, r), ellipse_path(300, 175, r, r)]
    neg = [ellipse_path(300, 525, r - sw, r - sw), ellipse_path(300, 175, r - sw, r - sw)]
    return combine(pos, neg), 600


def build_nine(c):
    sw = c.STROKE_WIDTH
    r = 190
    pos = [
        bar_path(150, 0, 460, 400, sw),
        ellipse_path(300, 510, r, r),
    ]
    neg = [ellipse_path(300, 510, r - sw, r - sw)]
    return combine(pos, neg), 600


# =====================================================================
# ギリシャ文字（数学・科学表記でよく使われるものを厳選）
# =====================================================================
def build_Sigma(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(80, c.CAP_HEIGHT - sw / 2, 500, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(80, sw / 2, 500, sw / 2, sw),
        bar_path(80, c.CAP_HEIGHT, 320, c.CAP_HEIGHT / 2, sw),
        bar_path(320, c.CAP_HEIGHT / 2, 80, 0, sw),
    ]
    return combine(pos), 560


def build_Delta(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(300, c.CAP_HEIGHT, 60, 0, sw),
        bar_path(300, c.CAP_HEIGHT, 540, 0, sw),
        bar_path(60, sw / 2, 540, sw / 2, sw),
    ]
    return combine(pos), 600


def build_Theta(c):
    sw = c.STROKE_WIDTH
    pos, neg = bowl(300, 350, 260, 350, sw)
    pos.append(bar_path(60, 350, 540, 350, sw))
    return combine(pos, neg), 620


def build_Lambda(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(300, c.CAP_HEIGHT, 60, 0, sw),
        bar_path(300, c.CAP_HEIGHT, 540, 0, sw),
    ]
    return combine(pos), 600


def build_Pi(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.CAP_HEIGHT - sw / 2, 540, c.CAP_HEIGHT - sw / 2, sw),
        bar_path(80, 0, 80, c.CAP_HEIGHT, sw),
        bar_path(520, 0, 520, c.CAP_HEIGHT, sw),
    ]
    return combine(pos), 600


def build_Phi(c):
    sw = c.STROKE_WIDTH
    pos, neg = bowl(300, 350, 190, 260, sw)
    pos.append(bar_path(300, 0, 300, c.CAP_HEIGHT, sw))
    return combine(pos, neg), 600


def build_Omega(c):
    sw = c.STROKE_WIDTH
    p, n = bowl(300, 400, 220, 260, sw, open_side="bottom")
    pos = p + [bar_path(140, 0, 140, 260, sw), bar_path(460, 0, 460, 260, sw)]
    return combine(pos, n), 620


def build_alpha(c):
    sw = c.STROKE_WIDTH
    cy = c.X_HEIGHT / 2
    pos, neg = bowl(230, cy, 170, cy, sw)
    pos.append(bar_path(420, 0, 420, c.X_HEIGHT, sw))
    return combine(pos, neg), 480


def build_beta(c):
    sw = c.STROKE_WIDTH
    stem_x = 100
    pos = [bar_path(stem_x, -140, stem_x, c.ASCENDER, sw)]
    p, n = bowl(stem_x + 150, 350, 150, 150, sw, open_side="left")
    pos += p
    return combine(pos, n), 480


def build_gamma(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.X_HEIGHT, 250, -140, sw),
        bar_path(440, c.X_HEIGHT, 150, 260, sw),
    ]
    return combine(pos), 500


def build_delta_lower(c):
    sw = c.STROKE_WIDTH
    pos, neg = bowl(250, 150, 180, 150, sw)
    pos.append(bar_path(150, c.X_HEIGHT, 350, 330, sw))
    return combine(pos, neg), 480


def build_lambda_lower(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(220, c.X_HEIGHT, 60, 0, sw),
        bar_path(220, c.X_HEIGHT, 440, 0, sw),
    ]
    return combine(pos), 480


def build_mu(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(80, c.X_HEIGHT, 80, -140, sw),
        bar_path(400, c.X_HEIGHT, 400, 0, sw),
    ]
    p, n = bowl(240, 175, 160, 175, sw, open_side="top")
    pos += p
    return combine(pos, n), 500


def build_pi_lower(c):
    sw = c.STROKE_WIDTH
    pos = [
        bar_path(60, c.X_HEIGHT - sw / 2, 440, c.X_HEIGHT - sw / 2, sw),
        bar_path(100, 0, 100, c.X_HEIGHT, sw),
        bar_path(400, 0, 400, c.X_HEIGHT, sw),
    ]
    return combine(pos), 500


def build_theta_lower(c):
    sw = c.STROKE_WIDTH
    pos, neg = bowl(250, 250, 175, 250, sw)
    pos.append(bar_path(80, 250, 420, 250, sw))
    return combine(pos, neg), 500


def build_phi_lower(c):
    sw = c.STROKE_WIDTH
    pos, neg = bowl(250, 175, 175, 175, sw)
    pos.append(bar_path(250, -140, 250, c.X_HEIGHT, sw))
    return combine(pos, neg), 500


def build_omega_lower(c):
    sw = c.STROKE_WIDTH
    p, n = bowl(230, 175, 160, 175, sw, open_side="top")
    pos = p + [bar_path(90, 0, 90, 175, sw), bar_path(370, 0, 370, 175, sw)]
    return combine(pos, n), 460


# =====================================================================
# レジストリ
# =====================================================================
GLYPH_BUILDERS = {
    "A": build_A, "B": build_B, "C": build_C, "D": build_D, "E": build_E,
    "F": build_F, "G": build_G, "H": build_H, "I": build_I, "J": build_J,
    "K": build_K, "L": build_L, "M": build_M, "N": build_N, "O": build_O,
    "P": build_P, "Q": build_Q, "R": build_R, "S": build_S, "T": build_T,
    "U": build_U, "V": build_V, "W": build_W, "X": build_X, "Y": build_Y,
    "Z": build_Z,
    "a": build_a, "b": build_b, "c": build_c, "d": build_d, "e": build_e,
    "f": build_f, "g": build_g, "h": build_h, "i": build_i, "j": build_j,
    "k": build_k, "l": build_l, "m": build_m, "n": build_n, "o": build_o,
    "p": build_p, "q": build_q, "r": build_r, "s": build_s, "t": build_t,
    "u": build_u, "v": build_v, "w": build_w, "x": build_x, "y": build_y,
    "z": build_z,
    "zero": build_zero, "one": build_one, "two": build_two, "three": build_three,
    "four": build_four, "five": build_five, "six": build_six, "seven": build_seven,
    "eight": build_eight, "nine": build_nine,
    # ギリシャ文字（数学・科学表記で頻出のもの）
    "Sigma": build_Sigma, "Delta": build_Delta, "Theta": build_Theta,
    "Lambda": build_Lambda, "Pi": build_Pi, "Phi": build_Phi, "Omega": build_Omega,
    "alpha": build_alpha, "beta": build_beta, "gamma": build_gamma,
    "delta": build_delta_lower, "lambda": build_lambda_lower, "mu": build_mu,
    "pi": build_pi_lower, "theta": build_theta_lower, "phi": build_phi_lower,
    "omega": build_omega_lower,
}

# グリフ名 → Unicodeコードポイント（cmap用）
GLYPH_UNICODES = {
    **{chr(ord("A") + i): ord("A") + i for i in range(26)},
    **{chr(ord("a") + i): ord("a") + i for i in range(26)},
    "zero": 0x30, "one": 0x31, "two": 0x32, "three": 0x33, "four": 0x34,
    "five": 0x35, "six": 0x36, "seven": 0x37, "eight": 0x38, "nine": 0x39,
    "Sigma": 0x03A3, "Delta": 0x0394, "Theta": 0x0398, "Lambda": 0x039B,
    "Pi": 0x03A0, "Phi": 0x03A6, "Omega": 0x03A9,
    "alpha": 0x03B1, "beta": 0x03B2, "gamma": 0x03B3, "delta": 0x03B4,
    "lambda": 0x03BB, "mu": 0x03BC, "pi": 0x03C0, "theta": 0x03B8,
    "phi": 0x03C6, "omega": 0x03C9,
}

# 記号・科学記号（symbols.py）をマージ
from symbols import SYMBOL_BUILDERS, SYMBOL_UNICODES  # noqa: E402
GLYPH_BUILDERS.update(SYMBOL_BUILDERS)
GLYPH_UNICODES.update(SYMBOL_UNICODES)
