"""Esquemes paramètrics del llibre. Cada funció dibuixa una situació concreta
amb els valors de l'enunciat, vectors amb fletxa i rètols en català."""
import math
from svgutil import Svg, INK, MUTED, BLUE, RED, GREEN, ORANGE, PURPLE, TEAL, PALE, PAPER


def _s(w, h):
    s = Svg(w, h)
    s.rect(0, 0, w, h, PAPER, "none", 0)
    return s


def cota_h(s, x1, x2, y, text, color=TEAL):
    if x2 < x1:
        x1, x2 = x2, x1
    s.line(x1, y - 6, x1, y + 6, color, 1.3)
    s.line(x2, y - 6, x2, y + 6, color, 1.3)
    s.arrow(x1, y, x2, y, color, 1.5, 8)
    s.label((x1 + x2) / 2, y - 14, text, 16, "middle", color, it=False)


def cota_v(s, x, y1, y2, text, color=PURPLE):
    if y2 < y1:
        y1, y2 = y2, y1
    s.line(x - 6, y1, x + 6, y1, color, 1.3)
    s.line(x - 6, y2, x + 6, y2, color, 1.3)
    s.arrow(x, y2, x, y1, color, 1.5, 8)
    s.label(x + 12, (y1 + y2) / 2, text, 16, "start", color, it=False)


def eix(punts, cota=None):
    """punts: llista (x_si, etiqueta, color). cota: (x1, x2, text) en les mateixes unitats de pantalla relatives 0..1."""
    s = _s(700, 200)
    y = 100
    s.arrow(36, y, 660, y, INK, 1.7, 10)
    s.label(668, y + 4, "x", 16, "start")
    for u, et, col in punts:
        x = 70 + u * 540
        s.line(x, y - 9, x, y + 9, INK, 1.6)
        s.circle(x, y, 6, col, col)
        s.label(x, y - 28, et, 16, "middle", col, it=False, bold=True)
    if cota:
        u1, u2, txt = cota
        cota_h(s, 70 + u1 * 540, 70 + u2 * 540, 148, txt, GREEN)
    return s.svg()


def grafica(trams, xlabel, ylabel, xmin, xmax, ymin, ymax, marca=None):
    """trams: llista de polilínies [(x,y), ...] en unitats de dades. marca: (x, y, text) opcional."""
    s = _s(680, 340)
    left, right, top, bot = 78, 640, 46, 286
    def X(x):
        return left + (x - xmin) / (xmax - xmin) * (right - left)
    def Y(y):
        return bot - (y - ymin) / (ymax - ymin) * (bot - top)
    for i in range(1, 5):
        xx = xmin + (xmax - xmin) * i / 5
        s.line(X(xx), top, X(xx), bot, "#ece7dc", 1)
        s.text(X(xx), bot + 18, _tick(xx), 15, "middle", MUTED, halo=False)
    for i in range(1, 4):
        yy = ymin + (ymax - ymin) * i / 4
        s.line(left, Y(yy), right, Y(yy), "#ece7dc", 1)
        s.text(left - 8, Y(yy), _tick(yy), 15, "end", MUTED, halo=False)
    s.text(left - 8, bot + 16, "0", 15, "end", MUTED, halo=False)
    s.axes(left, bot, right + 6, top - 4, xlabel, ylabel)
    colors = (BLUE, ORANGE, GREEN, RED)
    for k, pts in enumerate(trams):
        s.polyline([(X(x), Y(y)) for x, y in pts], colors[k % 4], 2.6)
    if marca:
        x, y, txt = marca
        s.label(X(x), Y(y) - 18, txt, 16, "middle", BLUE, it=False)
    return s.svg()


def _tick(v):
    if abs(v - round(v)) < 0.05:
        return str(int(round(v)))
    return f"{v:.1f}".replace(".", ",")


def caiguda(h_txt="h"):
    s = _s(640, 360)
    s.rect(48, 48, 120, 250, "#f7f1e6", INK, 1.8)
    for (x, y) in ((68, 70), (112, 70), (68, 118), (112, 118)):
        s.rect(x, y, 32, 26, PALE, MUTED, 1.2)
    s.line(30, 298, 250, 298, INK, 2)
    s.arrow(230, 56, 230, 286, INK, 1.5, 9)
    s.label(214, 44, "y", 16, "end")
    dades = [(340, 70, 0, "A  v = 0"), (450, 150, 48, "B"), (560, 240, 78, "C")]
    for x, y, vl, lab in dades:
        s.circle(x, y, 11, ORANGE, "#f6d7b0", 2)
        if vl:
            s.arrow(x, y + 14, x, min(y + 14 + vl, 320), BLUE, 2.2, 10)
        s.label(x, y - 22, lab, 16, "middle", INK, it=False, bold=True)
    cota_v(s, 300, 70, 290, h_txt)
    return s.svg()


def llancament():
    s = _s(680, 360)
    s.line(40, 310, 250, 310, INK, 2)
    s.arrow(90, 300, 90, 36, INK, 1.5, 9)
    s.label(74, 28, "y", 16, "end")
    s.circle(200, 250, 11, ORANGE, "#f6d7b0", 2)
    s.arrow(200, 236, 200, 150, BLUE, 2.3, 11)
    s.label(200, 276, "A", 16, "middle", INK, it=False, bold=True)
    s.label(222, 190, "v₀", 16, "start", BLUE)
    s.circle(360, 70, 11, ORANGE, "#f6d7b0", 2)
    s.label(360, 44, "B   v = 0", 16, "middle", INK, it=False, bold=True)
    s.circle(520, 190, 11, ORANGE, "#f6d7b0", 2)
    s.arrow(520, 204, 520, 280, RED, 2.3, 11)
    s.label(520, 164, "C", 16, "middle", INK, it=False, bold=True)
    s.label(542, 246, "v", 16, "start", RED)
    cota_v(s, 400, 70, 300, "h")
    s.label(200, 332, "a = −g durant tot el vol", 16, "middle", MUTED, it=False)
    return s.svg()


def tir_horitzontal(h_txt="h", v_txt="v₀"):
    s = _s(700, 360)
    terra = 292
    s.rect(36, 36, 100, terra - 36, "#f3efe6", INK, 1.7)
    s.line(28, terra, 670, terra, INK, 2)
    pts = []
    for i in range(41):
        t = i / 40
        pts.append((160 + t * 460, 52 + t * t * 210))
    s.polyline(pts, ORANGE, 2.6)
    for t, name, vy in ((0.0, "A", 26), (0.48, "B", 52), (1.0, "C", 36)):
        x = 160 + t * 460
        y = 52 + t * t * 210
        s.circle(x, y, 5.5, ORANGE, ORANGE)
        s.arrow(x, y, x + 42, y, BLUE, 2.1, 9)
        y_fi = min(y + vy, terra - 8)
        if y_fi > y + 12:
            s.arrow(x, y, x, y_fi, RED, 2.1, 9)
        s.label(x - 14, y - 16, name, 16, "end", INK, it=False, bold=True)
    s.label(230, 36, v_txt, 16, "start", BLUE)
    cota_v(s, 148, 52, terra - 8, h_txt)
    cota_h(s, 160, 620, 328, "abast")
    return s.svg()


def tir_parabolic(theta=40, h_txt="H", r_txt="R"):
    s = _s(700, 400)
    th = math.radians(min(max(theta, 18), 72))
    ybase = 320
    Hpx = min(200, 120 * math.tan(th) + 60)
    Rpx = min(500, Hpx * 4 / math.tan(th))
    Hpx = Rpx * math.tan(th) / 4
    x0 = 90
    s.line(40, ybase, 670, ybase, INK, 1.8)
    s.arrow(64, ybase, 64, 22, INK, 1.5, 9)
    s.label(48, 18, "y", 16, "end")
    s.label(662, ybase + 16, "x", 16, "start")
    pts = []
    for i in range(61):
        u = i / 60.0
        y = ybase - (4 * u * (1 - u)) * Hpx
        pts.append((x0 + u * Rpx, y))
    s.polyline(pts, ORANGE, 2.6)
    xa, ya = pts[0]
    s.arrow(xa, ya, xa + 64 * math.cos(th), ya - 64 * math.sin(th), BLUE, 2.2, 10)
    s.label(xa + 74 * math.cos(th), ya - 74 * math.sin(th), "v₀", 16, "start", BLUE)
    arc = 46
    s.path(
        f"M {xa+arc:.1f} {ya:.1f} A {arc} {arc} 0 0 0 {xa+arc*math.cos(th):.1f} {ya-arc*math.sin(th):.1f}",
        TEAL, 1.7,
    )
    s.label(xa + 78, ya + 18, f"{theta}°", 16, "start", TEAL, it=False)
    xm, ym = pts[30]
    s.circle(xm, ym, 5, ORANGE, ORANGE)
    s.arrow(xm, ym, xm + 44, ym, BLUE, 2, 9)
    s.label(xm, ym - 16, "vₓ", 16, "middle", BLUE)
    cota_v(s, min(xm + 86, 640), ym, ybase, h_txt)
    cota_h(s, x0, x0 + Rpx, ybase + 40, r_txt)
    return s.svg()


def mcu(txt_r="r"):
    s = _s(680, 320)
    cx, cy, r = 230, 160, 108
    s.circle(cx, cy, r, INK, "none", 1.8)
    s.circle(cx, cy, 4, INK, INK)
    a0, a1 = -0.3, -2.1
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    s.line(cx, cy, x0, y0, MUTED, 1.4)
    s.line(cx, cy, x1, y1, BLUE, 1.8)
    s.path(f"M {x0:.1f} {y0:.1f} A {r} {r} 0 0 0 {x1:.1f} {y1:.1f}", TEAL, 2.4)
    s.label(cx + 40, cy + 6, "θ", 18, "start", TEAL)
    s.label((cx + x1) / 2 - 8, (cy + y1) / 2, txt_r, 16, "end", BLUE)
    s.label(500, 100, "ω = Δθ / Δt", 18, "middle", INK, it=False)
    s.label(500, 140, "T període", 16, "middle", MUTED, it=False)
    s.label(500, 172, "f freqüència", 16, "middle", MUTED, it=False)
    s.label(500, 214, "v = ω r", 18, "middle", BLUE, it=False)
    return s.svg()


def mcu_vectors():
    s = _s(680, 340)
    cx, cy, r = 330, 170, 100
    s.circle(cx, cy, r, "#c5ccd6", "none", 1.6, "7 6")
    s.circle(cx, cy, 4, INK, INK)
    for k in range(4):
        ang = k * math.pi / 2
        x = cx + r * math.cos(ang)
        y = cy - r * math.sin(ang)
        s.circle(x, y, 7, ORANGE, "#f6d7b0", 2)
        tx, ty = -math.sin(ang), -math.cos(ang)
        s.arrow(x, y, x + 50 * tx, y + 50 * ty, BLUE, 2.2, 10)
        ux, uy = cx - x, cy - y
        nrm = math.hypot(ux, uy)
        s.arrow(x, y, x + 46 * ux / nrm, y + 46 * uy / nrm, PURPLE, 2.2, 10)
    s.label(cx + r + 58, cy + 6, "v", 17, "start", BLUE)
    s.label(cx, cy - r + 36, "a_c", 17, "middle", PURPLE)
    return s.svg()


def bloc(cx, cy, w=78, h=48):
    return  # placeholder, no es fa servir


def dcl_pla(fregament=False, força=True, etiqueta_F="F"):
    s = _s(640, 300)
    s.line(36, 210, 600, 210, INK, 2)
    s.rect(250, 148, 100, 62, PALE, INK, 2, 4)
    cx, cy = 300, 179
    s.arrow(cx, 148, cx, 78, GREEN, 2.3, 11)
    s.label(cx + 16, 100, "N", 17, "start", GREEN)
    s.arrow(cx, 210, cx, 268, BLUE, 2.3, 11)
    s.label(cx + 16, 248, "pes", 16, "start", BLUE, it=False)
    if força:
        s.arrow(350, cy, 470, cy, RED, 2.3, 11)
        s.label(410, cy - 18, etiqueta_F, 17, "middle", RED)
    if fregament:
        s.arrow(250, cy, 150, cy, ORANGE, 2.3, 11)
        s.label(190, cy - 18, "f", 17, "middle", ORANGE)
    return s.svg()


def _bloc_inclinat(s, alpha, along=0.58, L=300, x0=70, y0=300):
    a = math.radians(alpha)
    x1 = x0 + L * math.cos(a)
    y1 = y0 - L * math.sin(a)
    s.polygon([(x0, y0), (x1, y1), (x1, y0)], fill="#f6f1e6", stroke=INK, sw=1.8)
    s.path(
        f"M {x0+46} {y0} A 46 46 0 0 0 {x0+46*math.cos(a):.1f} {y0-46*math.sin(a):.1f}",
        TEAL, 1.7,
    )
    s.label(x0 + 62, y0 - 16, f"{alpha}°", 16, "start", TEAL, it=False)
    bx = x0 + along * L * math.cos(a)
    by = y0 - along * L * math.sin(a)
    t = (math.cos(a), -math.sin(a))
    n = (-math.sin(a), -math.cos(a))
    w, h = 26, 32
    c = (bx + n[0] * (h + 2), by + n[1] * (h + 2))
    corners = []
    for sx in (-1, 1):
        for sy in (0, 1):
            pass
    # rectangle: centre c, eixos t i n
    pts = []
    for ex, ey in ((-w, 0), (w, 0), (w, h), (-w, h)):
        # ey al llarg de n, ex al llarg de t; la base toca el pla si ey va de 0 cap a fora? 
        # n apunta cap a fora. Base a ey=4 (una mica separat), sostre a ey=h
        pass
    base = 6
    for ex, ey in ((-w, base), (w, base), (w, base + h), (-w, base + h)):
        pts.append((bx + ex * t[0] + ey * n[0], by + ex * t[1] + ey * n[1]))
    s.polygon(pts, fill="#d9e8f8", stroke=INK, sw=1.8)
    centre = (bx + (base + h / 2) * n[0], by + (base + h / 2) * n[1])
    return centre, t, n, (x0, y0, x1, y1)


def inclinat(alpha=30, fregament=True, força=False, components=False):
    s = _s(720, 380)
    centre, t, n, _ = _bloc_inclinat(s, alpha)
    cx, cy = centre
    # pes
    s.arrow(cx, cy, cx, cy + 78, BLUE, 2.3, 11)
    s.label(cx + 14, cy + 64, "pes", 16, "start", BLUE, it=False)
    # normal
    s.arrow(cx, cy, cx + 72 * n[0], cy + 72 * n[1], GREEN, 2.3, 11)
    s.label(cx + 88 * n[0], cy + 88 * n[1], "N", 17, "middle", GREEN)
    if fregament:
        # s'oposa a baixar: sentit de pujada
        s.arrow(cx, cy, cx + 66 * t[0], cy + 66 * t[1], ORANGE, 2.3, 11)
        s.label(cx + 84 * t[0], cy + 84 * t[1], "f", 17, "middle", ORANGE)
    if força:
        s.arrow(cx, cy, cx - 70 * t[0], cy - 70 * t[1], RED, 2.2, 10)
        s.label(cx - 88 * t[0], cy - 88 * t[1], "F", 17, "middle", RED)
    if components:
        # component del pes al llarg del pla (baixant) i perpendicular, a traços
        s.arrow(cx, cy, cx - 58 * t[0], cy - 58 * t[1], BLUE, 1.6, 8)
        s.label(cx - 74 * t[0], cy - 74 * t[1], "Pₓ", 16, "middle", BLUE)
        s.arrow(cx, cy, cx - 50 * n[0], cy - 50 * n[1], BLUE, 1.5, 8)
        s.label(cx - 66 * n[0], cy - 66 * n[1], "Pᵧ", 16, "middle", BLUE)
    return s.svg()


def dcl_inclinat(alpha=30, fregament=True):
    """Només el cos lliure, amb els eixos del pla i les components del pes."""
    s = _s(640, 360)
    a = math.radians(alpha)
    t = (math.cos(a), -math.sin(a))
    n = (-math.sin(a), -math.cos(a))
    cx, cy = 300, 180
    w, h = 34, 40
    pts = []
    for ex, ey in ((-w, -h), (w, -h), (w, h), (-w, h)):
        pts.append((cx + ex * t[0] + ey * n[0], cy + ex * t[1] + ey * n[1]))
    s.polygon(pts, fill=PALE, stroke=INK, sw=1.8)
    # eixos
    s.arrow(cx, cy, cx + 120 * t[0], cy + 120 * t[1], MUTED, 1.3, 8)
    s.label(cx + 132 * t[0], cy + 132 * t[1], "x", 16, "middle", MUTED)
    s.arrow(cx, cy, cx + 110 * n[0], cy + 110 * n[1], MUTED, 1.3, 8)
    s.label(cx + 124 * n[0], cy + 124 * n[1], "y", 16, "middle", MUTED)
    s.arrow(cx, cy, cx, cy + 86, BLUE, 2.2, 10)
    s.label(cx + 18, cy + 74, "pes", 16, "start", BLUE, it=False)
    s.arrow(cx, cy, cx + 78 * n[0], cy + 78 * n[1], GREEN, 2.2, 10)
    s.label(cx + 96 * n[0], cy + 96 * n[1], "N", 17, "middle", GREEN)
    # components a part, amb marge perquè les etiquetes no surtin del requadre
    ox, oy = 150, 250
    s.line(ox, oy, ox - 70 * t[0], oy - 70 * t[1], BLUE, 1.7, "6 4")
    s.label(ox - 92 * t[0], oy - 92 * t[1], "P sin α", 16, "middle", BLUE, it=False)
    s.line(ox, oy, ox - 58 * n[0], oy - 58 * n[1], BLUE, 1.6, "6 4")
    s.label(ox - 80 * n[0], oy - 80 * n[1] + 16, "P cos α", 16, "middle", BLUE, it=False)
    s.label(ox, 336, "components del pes", 15, "middle", MUTED, it=False)
    if fregament:
        s.arrow(cx, cy, cx + 74 * t[0], cy + 74 * t[1], ORANGE, 2.2, 10)
        s.label(cx + 92 * t[0], cy + 92 * t[1], "f", 17, "middle", ORANGE)
    s.label(80, 36, f"α = {alpha}°", 16, "start", TEAL, it=False)
    return s.svg()


def dos_blocs(m1="m₁", m2="m₂"):
    s = _s(700, 250)
    s.line(30, 175, 560, 175, INK, 2)
    s.rect(90, 122, 86, 53, PALE, INK, 1.8, 3)
    s.rect(300, 116, 100, 59, "#e7eef8", INK, 1.8, 3)
    s.line(176, 148, 300, 148, ORANGE, 2.3)
    s.label(230, 132, "tensió", 16, "middle", ORANGE, it=False)
    s.label(133, 108, m1, 17, "middle")
    s.label(350, 102, m2, 17, "middle")
    s.arrow(400, 145, 520, 145, RED, 2.3, 11)
    s.label(460, 128, "F", 17, "middle", RED)
    return s.svg()


def atwood(m1="m₁", m2="m₂", baixa="m₂"):
    s = _s(640, 380)
    s.line(160, 36, 470, 36, INK, 4)
    cx, cy, r = 310, 78, 26
    s.circle(cx, cy, r, INK, PAPER, 2.2)
    s.circle(cx, cy, 3.5, INK, INK)
    y1, y2 = (168, 268) if baixa == "m₂" else (268, 168)
    s.line(cx - r, cy, cx - r, y1, ORANGE, 2.2)
    s.line(cx + r, cy, cx + r, y2, ORANGE, 2.2)
    s.rect(cx - r - 24, y1, 48, 46, PALE, INK, 1.8, 3)
    s.rect(cx + r - 24, y2, 48, 46, "#e7eef8", INK, 1.8, 3)
    s.label(cx - r, y1 + 23, m1, 15, "middle", INK, it=False, bold=True)
    s.label(cx + r, y2 + 23, m2, 15, "middle", INK, it=False, bold=True)
    if baixa == "m₂":
        s.arrow(cx + r + 56, y2 + 10, cx + r + 56, y2 + 58, GREEN, 2.1, 9)
        s.arrow(cx - r - 56, y1 + 40, cx - r - 56, y1 - 8, GREEN, 2.1, 9)
    s.label(cx, 22, "politja", 15, "middle", MUTED, it=False)
    return s.svg()


def taula(M="M", m="m"):
    s = _s(700, 280)
    s.polygon([(40, 78), (440, 78), (440, 200), (40, 200)], fill="#f7f3ea", stroke=INK, sw=1.8)
    s.circle(440, 78, 20, INK, PAPER, 2)
    s.rect(150, 32, 96, 46, PALE, INK, 1.8, 3)
    s.label(198, 20, M, 17, "middle")
    s.line(246, 55, 440, 55, ORANGE, 2.2)
    s.line(460, 78, 460, 150, ORANGE, 2.2)
    s.rect(432, 150, 56, 48, "#e7eef8", INK, 1.8, 3)
    s.label(460, 214, m, 17, "middle")
    s.arrow(490, 174, 490, 236, BLUE, 2.1, 9)
    s.label(508, 210, "pes", 16, "start", BLUE, it=False)
    return s.svg()


def molla(comprimida=False):
    s = _s(680, 220)
    s.line(40, 36, 40, 180, INK, 4)
    x_end = 200 if comprimida else 360
    pts = [(40, 108)]
    x = 40
    n = 8
    pas = (x_end - 70) / n
    for i in range(n):
        x += pas
        pts.append((x, 76 if i % 2 == 0 else 140))
    pts.append((x_end, 108))
    s.polyline(pts, TEAL, 2.3)
    s.rect(x_end, 84, 64, 48, PALE, INK, 1.8, 3)
    s.label(x_end + 32, 70, "m", 17, "middle")
    if not comprimida:
        s.arrow(x_end + 64, 108, x_end + 150, 108, RED, 2.2, 10)
        s.label(x_end + 108, 90, "F = kx", 16, "middle", RED, it=False)
    cota_h(s, 48, x_end, 178, "x" if not comprimida else "compressió")
    return s.svg()


def revolt():
    s = _s(680, 280)
    s.path("M 70 210 Q 250 30 560 210", "#d5dbe3", 14)
    s.circle(300, 112, 15, ORANGE, "#f6d7b0", 2)
    s.arrow(300, 112, 400, 62, BLUE, 2.3, 11)
    s.label(412, 56, "v", 17, "start", BLUE)
    s.arrow(300, 112, 236, 156, PURPLE, 2.3, 11)
    s.label(210, 176, "F_c", 17, "end", PURPLE)
    s.label(300, 248, "vist des de dalt", 15, "middle", MUTED, it=False)
    return s.svg()


def corda(r_txt="r"):
    s = _s(680, 300)
    cx, cy, r = 250, 160, 96
    s.circle(cx, cy, 5, INK, INK)
    s.circle(cx + r, cy, 14, ORANGE, "#f6d7b0", 2)
    s.line(cx, cy, cx + r, cy, ORANGE, 2.2)
    s.label(cx + r / 2, cy - 28, "tensió", 16, "middle", ORANGE, it=False)
    s.arrow(cx + r, cy, cx + r, cy - 64, BLUE, 2.2, 10)
    s.label(cx + r + 16, cy - 40, "v", 17, "start", BLUE)
    s.arrow(cx + r, cy + 16, cx + 36, cy + 16, PURPLE, 2, 9)
    s.label(cx + r / 2, cy + 36, "a_c", 16, "middle", PURPLE)
    cota_h(s, cx, cx + r, cy + 70, r_txt)
    return s.svg()


def peralt(theta=25):
    s = _s(720, 360)
    centre, t, n, _ = _bloc_inclinat(s, theta, along=0.48, L=340, x0=70, y0=300)
    cx, cy = centre
    s.arrow(cx, cy, cx + 74 * n[0], cy + 74 * n[1], GREEN, 2.3, 11)
    s.label(cx + 92 * n[0], cy + 92 * n[1], "N", 17, "middle", GREEN)
    s.arrow(cx, cy, cx, cy + 74, BLUE, 2.3, 11)
    s.label(cx + 16, cy + 62, "pes", 16, "start", BLUE, it=False)
    return s.svg()


def loop():
    s = _s(680, 380)
    cx, cy, r = 250, 200, 110
    s.circle(cx, cy, r, INK, "none", 2.2)
    s.line(30, cy + r, cx, cy + r, INK, 2.2)
    s.rect(cx - 16, cy - r - 26, 32, 20, ORANGE, INK, 1.6, 2)
    s.label(cx + 36, cy - r - 14, "dalt", 16, "start", MUTED, it=False)
    s.rect(cx - 18, cy + r - 36, 36, 18, ORANGE, INK, 1.6, 2)
    s.label(cx + 70, cy + r + 8, "baix", 16, "start", MUTED, it=False)
    s.arrow(cx, cy - r - 6, cx, cy - r + 42, BLUE, 2, 8)
    s.label(cx - 40, cy - r + 22, "pes", 15, "end", BLUE, it=False)
    s.arrow(cx, cy + r - 38, cx, cy + r - 90, GREEN, 2, 9)
    s.label(cx - 36, cy + r - 70, "N", 16, "end", GREEN)
    cota_v(s, cx + r + 36, cy - r, cy + r, "2r")
    return s.svg()


def muntanya(hA="h_A", hB="h_B", hC="h_C"):
    s = _s(720, 320)
    perfil = [(36, 260), (110, 260), (230, 90), (360, 170), (500, 70), (640, 250), (690, 250)]
    s.polyline(perfil, INK, 2.6)
    s.line(36, 260, 690, 260, "#e4dfd4", 1.2)
    for x, y, nom in ((110, 260, "A"), (230, 90, "B"), (360, 170, "C"), (500, 70, "D")):
        s.circle(x, y - 2, 7, ORANGE, "#f6d7b0", 2)
        s.label(x, y - 22, nom, 17, "middle", INK, it=False, bold=True)
    cota_v(s, 250, 90, 260, hB)
    cota_v(s, 390, 170, 260, hC)
    s.label(110, 286, hA, 15, "middle", MUTED, it=False)
    return s.svg()


def pendol(theta=50):
    s = _s(680, 360)
    cx, cy = 250, 40
    L = 230
    s.line(cx - 40, cy, cx + 40, cy, INK, 4)
    ang = math.radians(theta)
    x1 = cx + L * math.sin(ang)
    y1 = cy + L * math.cos(ang)
    s.line(cx, cy, x1, y1, MUTED, 1.6)
    s.circle(x1, y1, 13, ORANGE, "#f6d7b0", 2)
    s.label(x1 + 20, y1, "A", 16, "start", INK, it=False, bold=True)
    s.line(cx, cy, cx, cy + L, "#c8cdd4", 1.3, "5 4")
    s.circle(cx, cy + L, 13, ORANGE, "#f6d7b0", 2)
    s.label(cx + 22, cy + L + 4, "B", 16, "start", INK, it=False, bold=True)
    s.path(f"M {cx} {cy+78} A 78 78 0 0 1 {cx+78*math.sin(ang):.1f} {cy+78*math.cos(ang):.1f}", TEAL, 1.8)
    s.label(cx + 52, cy + 96, f"{theta}°", 16, "start", TEAL, it=False)
    yb = cy + L
    s.line(x1, y1, 78, y1, PURPLE, 1.2, "4 3")
    s.line(cx - 13, yb, 78, yb, PURPLE, 1.2, "4 3")
    cota_v(s, 64, y1, yb, "h")
    return s.svg()


def barres(etapes):
    """etapes: llista (nom, ec, ep) relatius. Em = ec+ep."""
    s = _s(700, 320)
    maxe = max(ec + ep for _, ec, ep in etapes) or 1
    base = 250
    gap = 620 / max(len(etapes), 1)
    for i, (nom, ec, ep) in enumerate(etapes):
        x = 48 + i * gap
        for k, val, col in ((0, ec, BLUE), (1, ep, GREEN), (2, ec + ep, INK)):
            if val <= 0:
                continue
            h = 170 * val / maxe
            xx = x + k * 30
            fill = col if k < 2 else PAPER
            s.rect(xx, base - h, 24, h, fill, col, 1.8, 2)
        s.label(x + 40, base + 22, nom, 16, "middle", INK, it=False, bold=True)
    s.rect(36, 28, 16, 14, BLUE, BLUE)
    s.label(60, 35, "cinètica", 15, "start", BLUE, it=False)
    s.rect(160, 28, 16, 14, GREEN, GREEN)
    s.label(184, 35, "potencial", 15, "start", GREEN, it=False)
    s.rect(310, 28, 16, 14, PAPER, INK, 1.6)
    s.label(334, 35, "mecànica", 15, "start", INK, it=False)
    return s.svg()


def treball():
    s = _s(680, 210)
    s.arrow(70, 120, 430, 120, MUTED, 1.7, 10)
    s.label(450, 138, "desplaçament", 15, "start", MUTED, it=False)
    s.arrow(70, 120, 280, 48, RED, 2.4, 11)
    s.label(230, 46, "F", 17, "middle", RED)
    s.path("M 140 120 A 70 70 0 0 0 118 86", TEAL, 1.7)
    s.label(150, 92, "φ", 17, "start", TEAL)
    return s.svg()


def newton_fma():
    s = _s(680, 230)
    s.rect(60, 80, 70, 50, PALE, INK, 1.8, 3)
    s.arrow(130, 105, 230, 105, RED, 2.4, 11)
    s.label(95, 66, "massa petita", 15, "middle", MUTED, it=False)
    s.label(180, 88, "F", 17, "middle", RED)
    s.label(95, 156, "acceleració gran", 15, "middle", BLUE, it=False)
    s.rect(390, 64, 120, 78, "#e7eef8", INK, 1.8, 3)
    s.arrow(510, 103, 630, 103, RED, 2.4, 11)
    s.label(450, 48, "massa gran", 15, "middle", MUTED, it=False)
    s.label(450, 168, "acceleració petita", 15, "middle", BLUE, it=False)
    return s.svg()


def parells():
    s = _s(680, 280)
    s.rect(60, 160, 210, 20, "#e7e1d6", INK, 1.6)
    s.rect(115, 112, 96, 48, "#d7e6f5", INK, 1.8, 3)
    s.arrow(163, 112, 163, 62, RED, 2.2, 10)
    s.label(180, 78, "N", 17, "start", RED)
    s.arrow(163, 160, 163, 214, BLUE, 2.2, 10)
    s.label(180, 200, "pes", 16, "start", BLUE, it=False)
    s.label(163, 248, "les dues forces actuen sobre el llibre", 14, "middle", MUTED, it=False)
    s.rect(400, 170, 140, 18, "#e7e1d6", INK, 1.6)
    s.arrow(450, 120, 450, 168, ORANGE, 2.2, 10)
    s.arrow(510, 168, 510, 120, GREEN, 2.2, 10)
    s.label(480, 88, "parell acció-reacció", 15, "middle", MUTED, it=False)
    s.label(400, 108, "sobre la taula", 14, "end", ORANGE, it=False)
    return s.svg()


def v_omega():
    s = _s(680, 240)
    cx, cy, r = 180, 120, 80
    s.circle(cx, cy, r, INK, PALE, 1.8)
    s.circle(cx, cy, 4, INK, INK)
    s.line(cx, cy, cx + r, cy, MUTED, 1.5)
    s.label(cx + r / 2, cy - 14, "r", 17, "middle")
    s.arrow(cx + r, cy, cx + r, cy - 58, BLUE, 2.2, 10)
    s.label(cx + r + 16, cy - 36, "v", 17, "start", BLUE)
    s.label(460, 100, "v = ω r", 22, "middle", INK, it=False, bold=True)
    s.label(460, 142, "a_c = v² / r", 18, "middle", PURPLE, it=False)
    return s.svg()


# Registre: nom -> funció que rep un dict i torna svg
def dibuixa(nom, **kw):
    fn = {
        "eix": lambda **k: eix(k["punts"], k.get("cota")),
        "grafica": lambda **k: grafica(k["trams"], k["xlabel"], k["ylabel"], k["xmin"], k["xmax"], k["ymin"], k["ymax"], k.get("marca")),
        "caiguda": lambda **k: caiguda(k.get("h", "h")),
        "llancament": lambda **k: llancament(),
        "tir_h": lambda **k: tir_horitzontal(k.get("h", "h"), k.get("v", "v₀")),
        "tir_p": lambda **k: tir_parabolic(k.get("theta", 40), k.get("h", "H"), k.get("r", "R")),
        "mcu": lambda **k: mcu(k.get("r", "r")),
        "mcu_vec": lambda **k: mcu_vectors(),
        "dcl": lambda **k: dcl_pla(k.get("fregament", False), k.get("força", True), k.get("F", "F")),
        "inclinat": lambda **k: inclinat(k.get("alpha", 30), k.get("fregament", True), k.get("força", False), k.get("components", False)),
        "dcl_inclinat": lambda **k: dcl_inclinat(k.get("alpha", 30), k.get("fregament", True)),
        "dos_blocs": lambda **k: dos_blocs(k.get("m1", "m₁"), k.get("m2", "m₂")),
        "atwood": lambda **k: atwood(k.get("m1", "m₁"), k.get("m2", "m₂"), k.get("baixa", "m₂")),
        "taula": lambda **k: taula(k.get("M", "M"), k.get("m", "m")),
        "molla": lambda **k: molla(k.get("comprimida", False)),
        "revolt": lambda **k: revolt(),
        "corda": lambda **k: corda(k.get("r", "r")),
        "peralt": lambda **k: peralt(k.get("theta", 25)),
        "loop": lambda **k: loop(),
        "muntanya": lambda **k: muntanya(k.get("hA", "h_A"), k.get("hB", "h_B"), k.get("hC", "h_C")),
        "pendol": lambda **k: pendol(k.get("theta", 50)),
        "barres": lambda **k: barres(k["etapes"]),
        "treball": lambda **k: treball(),
        "fma": lambda **k: newton_fma(),
        "parells": lambda **k: parells(),
        "v_omega": lambda **k: v_omega(),
    }[nom]
    return fn(**kw)
