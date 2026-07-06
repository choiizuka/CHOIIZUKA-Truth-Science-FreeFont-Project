"""
primitives.py
=============
グリフを「矩形バー」と「楕円(リング)」の組み合わせで組み立てるための最小ツールキット。

考え方:
  - まっすぐな線 → bar_path() で太さ STROKE_WIDTH の矩形として描く
  - 丸い部分(O, C, e の玉部分など) → ellipse_path() で外側の輪郭、
    内側を一回り小さい ellipse_path() で描いて「輪(リング)」にする
  - 開いた形(C, S, 数字の3 など) → リングから四角を差し引いて「欠け」を作る

すべての形は combine(positives, negatives) で最終的に1つのアウトラインへ
ブール演算（合体 → 差分）される。個々の図形の向き(時計回り/反時計回り)は
気にしなくてよい（skia-pathopsが自動で正規化する）。
"""

import math
import pathops
from fontTools.pens.recordingPen import RecordingPen


# ---------------------------------------------------------------------
# 基本図形
# ---------------------------------------------------------------------
def rect_path(x0, y0, x1, y1):
    path = pathops.Path()
    pen = path.getPen()
    pen.moveTo((x0, y0))
    pen.lineTo((x1, y0))
    pen.lineTo((x1, y1))
    pen.lineTo((x0, y1))
    pen.closePath()
    return path


def bar_path(x1, y1, x2, y2, width):
    """線分(x1,y1)-(x2,y2)を中心線とする、幅widthの矩形バー(端は直角カット)。"""
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        return rect_path(x1 - width / 2, y1 - width / 2, x1 + width / 2, y1 + width / 2)
    ux, uy = dx / length, dy / length
    px, py = -uy * width / 2, ux * width / 2
    path = pathops.Path()
    pen = path.getPen()
    pen.moveTo((x1 + px, y1 + py))
    pen.lineTo((x2 + px, y2 + py))
    pen.lineTo((x2 - px, y2 - py))
    pen.lineTo((x1 - px, y1 - py))
    pen.closePath()
    return path


def ellipse_path(cx, cy, rx, ry):
    """4本の3次ベジェによる楕円近似（真円の場合は rx == ry）。"""
    kx = 0.5522847498307936 * rx
    ky = 0.5522847498307936 * ry
    path = pathops.Path()
    pen = path.getPen()
    pen.moveTo((cx + rx, cy))
    pen.curveTo((cx + rx, cy + ky), (cx + kx, cy + ry), (cx, cy + ry))
    pen.curveTo((cx - kx, cy + ry), (cx - rx, cy + ky), (cx - rx, cy))
    pen.curveTo((cx - rx, cy - ky), (cx - kx, cy - ry), (cx, cy - ry))
    pen.curveTo((cx + kx, cy - ry), (cx + rx, cy - ky), (cx + rx, cy))
    pen.closePath()
    return path


# ---------------------------------------------------------------------
# 複合図形ヘルパー
# ---------------------------------------------------------------------
def bowl(cx, cy, rx, ry, sw, open_side=None, margin=20):
    """
    O, C, D, e などに使う「輪(リング)」を作るヘルパー。
    open_side を指定すると、その方向の半分を削って開いた形にする
    （'left' / 'right' / 'top' / 'bottom'）。
    戻り値: (positives, negatives) のタプル。呼び出し側でリストに += する。
    """
    pos = [ellipse_path(cx, cy, rx, ry)]
    neg = [ellipse_path(cx, cy, max(rx - sw, 1), max(ry - sw, 1))]

    if open_side == "right":
        neg.append(rect_path(cx, cy - ry - margin, cx + rx + margin, cy + ry + margin))
    elif open_side == "left":
        neg.append(rect_path(cx - rx - margin, cy - ry - margin, cx, cy + ry + margin))
    elif open_side == "top":
        neg.append(rect_path(cx - rx - margin, cy, cx + rx + margin, cy + ry + margin))
    elif open_side == "bottom":
        neg.append(rect_path(cx - rx - margin, cy - ry - margin, cx + rx + margin, cy))

    return pos, neg


def quadrant_bite(cx, cy, rx, ry, x_side, y_side, margin=20):
    """
    S字などに使う「1/4だけ削る」ヘルパー。
    x_side: 'left' or 'right'  /  y_side: 'top' or 'bottom'
    """
    x0 = cx - rx - margin if x_side == "left" else cx
    x1 = cx if x_side == "left" else cx + rx + margin
    y0 = cy - ry - margin if y_side == "bottom" else cy
    y1 = cy if y_side == "bottom" else cy + ry + margin
    return rect_path(x0, y0, x1, y1)


# ---------------------------------------------------------------------
# ブール演算合成
# ---------------------------------------------------------------------
def combine(positives, negatives=None):
    """
    positives(足す図形のリスト)を全部合体し、
    negatives(引く図形のリスト)を全部合体したもので差し引く。
    最終的な単純化されたアウトラインを RecordingPen で返す。
    """
    negatives = negatives or []

    union_out = RecordingPen()
    pathops.union(positives, union_out)

    if not negatives:
        return union_out

    union_path = pathops.Path()
    union_out.replay(union_path.getPen())

    neg_out = RecordingPen()
    pathops.union(negatives, neg_out)
    neg_path = pathops.Path()
    neg_out.replay(neg_path.getPen())

    final_out = RecordingPen()
    pathops.difference([union_path], [neg_path], final_out)
    return final_out


def draw_to_glyph(glyph, recording_pen):
    """RecordingPenの内容をufoLib2 Glyphに描画する。"""
    pen = glyph.getPen()
    recording_pen.replay(pen)
