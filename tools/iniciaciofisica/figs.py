"""Figures del llibre, dibuixades com a esquemes de text. Rètols en català."""
import math
from svgutil import (
    Svg, INK, MUTED, BLUE, RED, GREEN, ORANGE, PURPLE, TEAL, GRID, PALE, PAPER,
)

def _plot(svg, data, X, Y, color, sw=2.4):
    pts = [(X(x), Y(y)) for x, y in data]
    svg.polyline(pts, color, sw)


def eixos_graf(xmin, xmax, ymin, ymax, xlabel, ylabel, w=680, h=340):
    s = Svg(w, h)
    s.rect(0, 0, w, h, PAPER, "none", 0)
    left, right, top, bot = 72, w - 28, 40, h - 52
    def X(x):
        return left + (x - xmin) / (xmax - xmin) * (right - left)
    def Y(y):
        return bot - (y - ymin) / (ymax - ymin) * (bot - top)
    # graella
    for i in range(1, 5):
        xx = xmin + (xmax - xmin) * i / 5
        s.line(X(xx), top, X(xx), bot, GRID, 1)
        s.text(X(xx), bot + 18, _tick(xx), 14, "middle", MUTED, it=False, halo=False)
    for i in range(1, 5):
        yy = ymin + (ymax - ymin) * i / 5
        s.line(left, Y(yy), right, Y(yy), GRID, 1)
        s.text(left - 10, Y(yy), _tick(yy), 14, "end", MUTED, it=False, halo=False)
    s.axes(left, bot, right + 8, top - 6, xlabel, ylabel)
    s.text(left - 8, bot + 16, "0", 14, "end", MUTED, it=False, halo=False)
    return s, X, Y


def _tick(v):
    if abs(v - round(v)) < 1e-6:
        return str(int(round(v)))
    return f"{v:.1f}".replace(".", ",")


def f_xt_mru():
    s, X, Y = eixos_graf(0, 10, 0, 40, "t (s)", "x (m)")
    _plot(s, [(t, 4 * t + 4) for t in (0, 8)], X, Y, BLUE)
    s.circle(X(0), Y(4), 4.5, BLUE, BLUE, 1)
    s.circle(X(8), Y(36), 4.5, BLUE, BLUE, 1)
    s.label(X(4) + 8, Y(20) - 16, "x = 4 + 4t", 16, "start", BLUE)
    return s.svg(), "Gràfica posició-temps d’un moviment rectilini uniforme. El pendent és la velocitat, constant."


def f_xt_mrua():
    s, X, Y = eixos_graf(0, 6, 0, 30, "t (s)", "x (m)")
    pts = [(t, 0.5 * 1.5 * t * t) for t in [i * 0.25 for i in range(0, 25)]]
    _plot(s, pts, X, Y, BLUE)
    s.label(X(3.3), Y(8) - 8, "x = ½ a t²", 16, "start", BLUE)
    return s.svg(), "Gràfica posició-temps d’un MRUA que surt del repòs. La corba és una paràbola i el pendent, que és la velocitat, creix."


def f_vt_mrua():
    s, X, Y = eixos_graf(0, 8, 0, 16, "t (s)", "v (m/s)")
    _plot(s, [(0, 2), (6, 14)], X, Y, BLUE)
    # àrea
    s.polygon([(X(0), Y(0)), (X(0), Y(2)), (X(6), Y(14)), (X(6), Y(0))], fill=BLUE, stroke="none", op=0.12)
    s.label(X(3), Y(4), "àrea = Δx", 15, "middle", BLUE, it=False, bold=True)
    s.label(X(3), Y(8) + 18, "pendent = a", 15, "middle", RED, it=False)
    return s.svg(), "Gràfica velocitat-temps d’un MRUA. El pendent és l’acceleració i l’àrea sota la recta és el desplaçament."


def f_at():
    s, X, Y = eixos_graf(0, 8, -2, 4, "t (s)", "a (m/s²)")
    _plot(s, [(0, 2), (7, 2)], X, Y, RED)
    s.label(X(3.5), Y(2) - 22, "a constant", 16, "middle", RED, it=False)
    return s.svg(), "Gràfica acceleració-temps d’un MRUA. L’acceleració no canvia, i per això la gràfica és una recta horitzontal."


def f_desplacament():
    s = Svg(680, 220)
    s.rect(0, 0, 680, 220, PAPER, "none", 0)
    y = 120
    s.arrow(50, y, 640, y, INK, 1.6, 10)
    s.label(650, y + 18, "x", 16, "start")
    s.line(90, y - 8, 90, y + 8, INK, 1.6)
    s.line(250, y - 8, 250, y + 8, INK, 1.6)
    s.line(520, y - 8, 520, y + 8, INK, 1.6)
    s.circle(250, y, 7, BLUE, BLUE)
    s.circle(520, y, 7, ORANGE, ORANGE)
    s.label(90, y + 28, "origen", 14, "middle", MUTED, it=False)
    s.label(250, y - 28, "x₁", 18)
    s.label(520, y - 28, "x₂", 18)
    s.arrow(250, y - 58, 520, y - 58, GREEN, 2.2, 11)
    s.label(385, y - 76, "desplaçament Δx = x₂ − x₁", 16, "middle", GREEN, it=False)
    s.label(385, y + 52, "posició", 14, "middle", MUTED, it=False)
    return s.svg(), "La posició es mesura des de l’origen. El desplaçament és la diferència de posicions, amb signe."


def f_caiguda():
    s = Svg(680, 340)
    s.rect(0, 0, 680, 340, PAPER, "none", 0)
    # edifici
    s.rect(70, 40, 150, 260, "#f7f1e6", INK, 1.8, 2)
    s.rect(90, 60, 36, 28, PALE, MUTED, 1.2)
    s.rect(140, 60, 36, 28, PALE, MUTED, 1.2)
    s.rect(90, 110, 36, 28, PALE, MUTED, 1.2)
    s.rect(140, 110, 36, 28, PALE, MUTED, 1.2)
    s.line(40, 300, 300, 300, INK, 2)
    # pedra en tres instants
    xs = [360, 470, 580]
    ys = [70, 150, 250]
    vs = [36, 70, 110]
    labs = ["v = 0", "v", "v més gran"]
    for i, (x, y, vl, lab) in enumerate(zip(xs, ys, vs, labs)):
        s.circle(x, y, 11, ORANGE, "#f6d7b0", 2)
        if vl:
            s.arrow(x, y + 14, x, y + 14 + vl, BLUE, 2.2, 11)
        s.label(x + 28, y + 20 + vl / 2, lab if i else "v₀ = 0", 15, "start", BLUE, it=False)
    s.arrow(330, 40, 330, 290, INK, 1.5, 9)
    s.label(318, 300, "y", 16, "end")
    s.label(250, 28, "es deixa anar", 15, "middle", MUTED, it=False)
    s.label(360, 48, "A", 16, "middle", INK, it=False, bold=True)
    s.label(470, 128, "B", 16, "middle", INK, it=False, bold=True)
    s.label(580, 228, "C", 16, "middle", INK, it=False, bold=True)
    return s.svg(), "Caiguda lliure des del repòs. La velocitat, cap avall, creix de manera uniforme; l’acceleració val g en tots els punts."


def f_llancament():
    s = Svg(680, 360)
    s.rect(0, 0, 680, 360, PAPER, "none", 0)
    s.line(40, 310, 300, 310, INK, 2)
    s.arrow(120, 300, 120, 36, INK, 1.5, 9)
    s.label(108, 28, "y", 16, "end")
    # pujada
    s.circle(200, 250, 10, ORANGE, "#f6d7b0", 2)
    s.arrow(200, 236, 200, 150, BLUE, 2.2, 11)
    s.label(218, 190, "v cap amunt", 15, "start", BLUE, it=False)
    # dalt
    s.circle(320, 70, 10, ORANGE, "#f6d7b0", 2)
    s.label(348, 70, "v = 0", 16, "start", BLUE, it=False)
    s.label(320, 44, "alçada màxima", 15, "middle", MUTED, it=False)
    # baixada
    s.circle(460, 180, 10, ORANGE, "#f6d7b0", 2)
    s.arrow(460, 194, 460, 280, RED, 2.2, 11)
    s.label(478, 240, "v cap avall", 15, "start", RED, it=False)
    s.label(200, 280, "A", 15, "middle", INK, it=False, bold=True)
    s.label(320, 96, "B", 15, "middle", INK, it=False, bold=True)
    s.label(460, 160, "C", 15, "middle", INK, it=False, bold=True)
    s.label(80, 332, "a = −g en tot el recorregut (eix cap amunt)", 15, "start", MUTED, it=False)
    return s.svg(), "Llançament vertical cap amunt. Al punt més alt la velocitat és nul·la, però l’acceleració continua sent −g."


def f_tir_horitzontal():
    s = Svg(700, 340)
    s.rect(0, 0, 700, 340, PAPER, "none", 0)
    s.rect(36, 36, 90, 230, "#f3efe6", INK, 1.6)
    s.line(30, 266, 680, 266, INK, 2)
    # paràbola: h=4.9 equivalent visual, v constant horizontal
    pts = []
    for i in range(0, 41):
        t = i / 40
        x = 140 + t * 480
        y = 50 + t * t * 200
        pts.append((x, y))
    s.polyline(pts, ORANGE, 2.4)
    # vectors en 3 punts
    for t, name in ((0.05, "A"), (0.45, "B"), (0.92, "C")):
        x = 140 + t * 480
        y = 50 + t * t * 200
        s.circle(x, y, 5, ORANGE, ORANGE, 1)
        s.arrow(x, y, x + 54, y, BLUE, 2, 9)  # vx
        vy = 18 + t * 70
        s.arrow(x, y, x, y + vy, RED, 2, 9)  # vy
        s.label(x - 14, y - 12, name, 15, "end", INK, it=False, bold=True)
    s.label(430, 78, "vₓ constant", 15, "start", BLUE, it=False)
    s.label(520, 210, "vᵧ creix", 15, "start", RED, it=False)
    s.label(200, 300, "abast", 15, "middle", MUTED, it=False)
    s.arrow(140, 286, 140 + 0.92 * 480, 286, TEAL, 1.8, 9)
    return s.svg(), "Tir horitzontal. La component horitzontal de la velocitat no canvia; la vertical creix com en una caiguda lliure."


def f_tir_parabolic():
    s = Svg(700, 360)
    s.rect(0, 0, 700, 360, PAPER, "none", 0)
    s.line(40, 310, 680, 310, INK, 1.8)
    s.arrow(70, 310, 70, 28, INK, 1.5, 9)
    s.label(54, 24, "y", 16, "end")
    s.label(676, 328, "x", 16, "start")
    # paràbola simètrica
    pts = []
    for i in range(0, 61):
        u = i / 60
        x = 90 + u * 540
        y = 300 - math.sin(math.pi * u) * 230
        pts.append((x, y))
    s.polyline(pts, ORANGE, 2.6)
    # punts
    marks = [(0.0, "sortida"), (0.5, "dalt"), (1.0, "arribada")]
    for u, name in ((0.08, None), (0.5, None), (0.92, None)):
        x = 90 + u * 540
        y = 300 - math.sin(math.pi * u) * 230
        s.circle(x, y, 5, ORANGE, ORANGE)
        # tangent aproximada
        du = 0.015
        x2 = 90 + (u + du) * 540
        y2 = 300 - math.sin(math.pi * (u + du)) * 230
        ang = math.atan2(y2 - y, x2 - x)
        L = 58
        s.arrow(x, y, x + L * math.cos(ang), y + L * math.sin(ang), BLUE, 2.1, 10)
        # components
        s.arrow(x, y, x + 40, y, TEAL, 1.6, 8)
        s.line(x + 40, y, x + 40, y + L * math.sin(ang), TEAL, 1.2, "5 4")
    s.label(150, 250, "v₀", 16, "start", BLUE)
    s.label(360, 52, "H", 16, "middle", PURPLE, it=False, bold=True)
    s.line(360, 70, 360, 300, PURPLE, 1.3, "4 4")
    s.label(360, 328, "abast R", 15, "middle", MUTED, it=False)
    s.arrow(96, 328, 90 + 540, 328, GREEN, 1.6, 8)
    s.label(200, 200, "vₓ", 15, "start", TEAL)
    return s.svg(), "Tir parabòlic des del terra. Al punt més alt la velocitat és horitzontal. L’abast R i l’alçada màxima H es llegeixen sobre els eixos."


def f_trajectoria():
    s = Svg(680, 300)
    s.rect(0, 0, 680, 300, PAPER, "none", 0)
    s.arrow(50, 250, 640, 250, INK, 1.5, 9)
    s.arrow(70, 270, 70, 30, INK, 1.5, 9)
    s.label(652, 268, "x", 16, "start")
    s.label(52, 28, "y", 16, "end")
    pts = []
    for i in range(0, 50):
        u = i / 49
        x = 80 + u * 520
        # y = x tan - b x^2 , visual
        uu = u
        y = 240 - (uu * 1.15 - uu * uu) * 280
        pts.append((x, y))
    s.polyline(pts, ORANGE, 2.4)
    s.rect(300, 36, 340, 78, "#fff", "#d9d3c6", 1.2, 8)
    s.label(470, 62, "y = x tan θ − gx² / (2 v₀² cos² θ)", 15, "middle", INK, it=False)
    s.label(470, 90, "equació de la trajectòria", 14, "middle", MUTED, it=False)
    return s.svg(), "La trajectòria és una paràbola. L’equació dona l’altura y de cada posició horitzontal x, sense haver de passar pel temps."


def f_mcu_angle():
    s = Svg(680, 320)
    s.rect(0, 0, 680, 320, PAPER, "none", 0)
    cx, cy, r = 250, 168, 110
    s.circle(cx, cy, r, INK, "none", 1.8)
    s.circle(cx, cy, 4, INK, INK)
    # radi inicial i final
    a0, a1 = -0.4, -2.2
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    s.line(cx, cy, x0, y0, MUTED, 1.5)
    s.arrow(cx, cy, x1, y1, BLUE, 2, 10)
    # arc
    s.path(f"M {x0:.1f} {y0:.1f} A {r} {r} 0 0 0 {x1:.1f} {y1:.1f}", TEAL, 2.4)
    s.label(cx + 36, cy + 8, "θ", 18, "start", TEAL)
    s.label(cx + 70, cy - 78, "arc = r θ", 16, "start", TEAL, it=False)
    s.label(cx, cy + r + 28, "sentit del moviment", 14, "middle", MUTED, it=False)
    # fórmules a la dreta
    s.label(500, 90, "ω = Δθ / Δt", 18, "middle", BLUE, it=False)
    s.label(500, 130, "ω = 2π / T = 2π f", 18, "middle", INK, it=False)
    s.label(500, 170, "T = 1 / f", 18, "middle", INK, it=False)
    s.label(500, 220, "θ en radiants", 15, "middle", MUTED, it=False)
    return s.svg(), "En un MCU l’angle creix de manera uniforme. La velocitat angular ω és el ritme d’aquest angle."


def f_mcu_vectors():
    s = Svg(680, 340)
    s.rect(0, 0, 680, 340, PAPER, "none", 0)
    cx, cy, r = 330, 175, 105
    s.circle(cx, cy, r, "#c5ccd6", "none", 1.6, "7 6")
    s.circle(cx, cy, 4, INK, INK)
    for k in range(4):
        ang = -math.pi / 2 + k * math.pi / 2  # dalt, esquerra? start at right, go counterclockwise in math but screen y down
        # screen angle: 0 right, clockwise positive if we use +sin because y down... use standard math with y up converted
        ang = k * math.pi / 2
        x = cx + r * math.cos(ang)
        y = cy - r * math.sin(ang)
        s.circle(x, y, 7, ORANGE, "#f6d7b0", 2)
        # v tangent: direction (-sin, cos) in math = screen (-sin, -cos)? 
        # math tangent for increasing angle (ccw): (-sin, cos) with y up
        # screen: tx = -sin, ty = -cos
        tx, ty = -math.sin(ang), -math.cos(ang)
        s.arrow(x, y, x + 52 * tx, y + 52 * ty, BLUE, 2.2, 10)
        # ac cap al centre
        cxu, cyu = cx - x, cy - y
        n = math.hypot(cxu, cyu)
        s.arrow(x, y, x + 48 * cxu / n, y + 48 * cyu / n, PURPLE, 2.2, 10)
    s.label(cx + r + 62, cy - 8, "v", 16, "start", BLUE)
    s.label(cx + 28, cy - r - 18, "a_c", 16, "middle", PURPLE)
    s.label(cx, 322, "v és tangent; a_c apunta sempre al centre", 15, "middle", MUTED, it=False)
    return s.svg(), "En quatre posicions del MCU: la velocitat és tangent a la circumferència i l’acceleració centrípeta apunta al centre."


def f_v_omega():
    s = Svg(680, 240)
    s.rect(0, 0, 680, 240, PAPER, "none", 0)
    cx, cy, r = 180, 120, 78
    s.circle(cx, cy, r, INK, PALE, 1.8)
    s.circle(cx, cy, 4, INK, INK)
    s.line(cx, cy, cx + r, cy, MUTED, 1.5)
    s.label(cx + r / 2, cy - 14, "r", 16, "middle")
    s.arrow(cx + r, cy, cx + r, cy - 56, BLUE, 2.2, 10)
    s.label(cx + r + 16, cy - 36, "v", 16, "start", BLUE)
    s.path(f"M {cx+36} {cy} A 36 36 0 0 0 {cx+36*math.cos(-0.9):.1f} {cy+36*math.sin(0.9):.1f}", TEAL, 2)
    s.label(cx + 48, cy + 28, "ω", 16, "start", TEAL)
    s.label(430, 90, "v = ω r", 22, "middle", INK, it=False, bold=True)
    s.label(430, 132, "a_c = v² / r = ω² r", 18, "middle", PURPLE, it=False)
    return s.svg(), "La velocitat lineal i la velocitat angular es relacionen per v = ωr. Qui és més lluny del centre va més de pressa."


def f_newton_parells():
    s = Svg(680, 280)
    s.rect(0, 0, 680, 280, PAPER, "none", 0)
    # llibre sobre taula
    s.rect(70, 150, 200, 22, "#e7e1d6", INK, 1.6)
    s.rect(120, 108, 90, 42, "#d7e6f5", INK, 1.8, 3)
    s.arrow(165, 108, 165, 62, RED, 2.2, 10)
    s.label(180, 78, "N", 16, "start", RED)
    s.arrow(165, 150, 165, 196, BLUE, 2.2, 10)
    s.label(180, 186, "P", 16, "start", BLUE)
    s.label(165, 230, "sobre el llibre", 14, "middle", MUTED, it=False)
    # parella: llibre empeny la taula
    s.arrow(400, 120, 400, 168, ORANGE, 2.2, 10)
    s.arrow(460, 168, 460, 120, GREEN, 2.2, 10)
    s.rect(370, 168, 120, 18, "#e7e1d6", INK, 1.6)
    s.label(430, 96, "parell acció-reacció", 15, "middle", MUTED, it=False)
    s.label(392, 148, "llibre → taula", 13, "end", ORANGE, it=False)
    s.label(472, 148, "taula → llibre", 13, "start", GREEN, it=False)
    s.label(430, 220, "iguals i oposades, sobre cossos diferents", 14, "middle", MUTED, it=False)
    return s.svg(), "El pes i la normal que actuen sobre el llibre no són un parell acció-reacció: totes dues actuen sobre el mateix cos. El parell de la normal és la força amb què el llibre empeny la taula."


def f_fma():
    s = Svg(680, 240)
    s.rect(0, 0, 680, 240, PAPER, "none", 0)
    # mateix F, masses diferents
    s.rect(80, 90, 70, 50, PALE, INK, 1.8, 4)
    s.arrow(150, 115, 250, 115, RED, 2.4, 11)
    s.label(115, 78, "m petita", 15, "middle", MUTED, it=False)
    s.label(200, 96, "F", 16, "middle", RED)
    s.label(115, 168, "a gran", 16, "middle", BLUE, it=False, bold=True)
    s.rect(400, 78, 110, 74, "#e7eef8", INK, 1.8, 4)
    s.arrow(510, 115, 610, 115, RED, 2.4, 11)
    s.label(455, 64, "m gran", 15, "middle", MUTED, it=False)
    s.label(560, 96, "la mateixa F", 15, "middle", RED, it=False)
    s.label(455, 180, "a petita", 16, "middle", BLUE, it=False, bold=True)
    return s.svg(), "La segona llei: amb la mateixa força resultant, el cos de menys massa adquireix més acceleració."


def f_dcl_horitzontal(amb_f=False, amb_F=True):
    s = Svg(680, 300)
    s.rect(0, 0, 680, 300, PAPER, "none", 0)
    s.line(40, 210, 640, 210, INK, 2)
    # bloc
    s.rect(250, 150, 90, 60, PALE, INK, 2, 4)
    cx, cy = 295, 180
    s.arrow(cx, cy, cx, cy + 78, BLUE, 2.3, 11)
    s.label(cx + 14, cy + 58, "P", 16, "start", BLUE)
    s.arrow(cx, cy, cx, cy - 78, GREEN, 2.3, 11)
    s.label(cx + 14, cy - 58, "N", 16, "start", GREEN)
    if amb_F:
        s.arrow(340, cy, 460, cy, RED, 2.3, 11)
        s.label(400, cy - 16, "F", 16, "middle", RED)
    if amb_f:
        s.arrow(250, cy, 150, cy, ORANGE, 2.3, 11)
        s.label(190, cy - 16, "f", 16, "middle", ORANGE)
    s.label(295, 250, "pla horitzontal", 15, "middle", MUTED, it=False)
    return s.svg(), (
        "Diagrama de cos lliure en un pla horitzontal amb fregament. El pes i la normal es compensen; la resultant horitzontal és F − f."
        if amb_f else
        "Diagrama de cos lliure en un pla horitzontal llis. La normal equilibra el pes i la força F és la resultant."
    )


def f_inclinat(alpha=30, fregament=True):
    s = Svg(720, 360)
    s.rect(0, 0, 720, 360, PAPER, "none", 0)
    a = math.radians(alpha)
    # tascó
    x0, y0 = 90, 300
    L = 340
    x1 = x0 + L * math.cos(a)
    y1 = y0 - L * math.sin(a)
    s.polygon([(x0, y0), (x1, y1), (x1, y0)], fill="#f6f1e6", stroke=INK, sw=1.8)
    s.label(x1 - 30, y0 + 22, f"{alpha}°", 16, "middle", MUTED, it=False)
    # arc de l'angle
    s.path(f"M {x0+48} {y0} A 48 48 0 0 0 {x0+48*math.cos(a):.1f} {y0-48*math.sin(a):.1f}", TEAL, 1.6)
    # bloc
    along = 0.55 * L
    bx = x0 + along * math.cos(a)
    by = y0 - along * math.sin(a)
    # normal i tangent
    tx, ty = math.cos(a), -math.sin(a)  # pujant el pla, screen
    nx, ny = -math.sin(a), -math.cos(a)  # cap a fora (amunt perpendicular): screen y component negative if cos>0... 
    # math normal (-sin, cos) y-up -> screen (-sin, -cos)
    nx, ny = -math.sin(a), -math.cos(a)
    s.rect(bx - 22, by - 36, 44, 32, "#d9e8f8", INK, 1.8, 3)
    # forces des del centre del bloc
    cxs, cys = bx, by - 18
    s.arrow(cxs, cys, cxs + 70 * nx, cys + 70 * ny, GREEN, 2.2, 10)
    s.label(cxs + 78 * nx, cys + 78 * ny, "N", 16, "middle", GREEN)
    s.arrow(cxs, cys, cxs, cys + 78, BLUE, 2.2, 10)
    s.label(cxs + 16, cys + 70, "P", 16, "start", BLUE)
    if fregament:
        # fregament pendent amunt (s'oposa a baixar)
        s.arrow(cxs, cys, cxs + 64 * tx, cys + 64 * ty, ORANGE, 2.2, 10)
        s.label(cxs + 76 * tx, cys + 76 * ty, "f", 16, "middle", ORANGE)
    # components a la dreta
    s.label(560, 70, "eix x al llarg del pla", 14, "middle", MUTED, it=False)
    s.label(560, 110, "Pₓ = P sin α", 18, "middle", BLUE, it=False)
    s.label(560, 146, "Pᵧ = P cos α", 18, "middle", BLUE, it=False)
    s.label(560, 182, "N = P cos α", 18, "middle", GREEN, it=False)
    if fregament:
        s.label(560, 218, "f = μ N", 18, "middle", ORANGE, it=False)
    else:
        s.label(560, 218, "sense fregament", 16, "middle", MUTED, it=False)
    return s.svg(), (
        f"Pla inclinat de {alpha}° amb les forces sobre el bloc. El pes es descompon en una component al llarg del pla i una de perpendicular."
        if fregament else
        f"Pla inclinat llis de {alpha}°. Sense fregament, la resultant val P sin α, pendent avall."
    )


def f_dos_blocs():
    s = Svg(700, 260)
    s.rect(0, 0, 700, 260, PAPER, "none", 0)
    s.line(30, 180, 520, 180, INK, 2)
    s.rect(80, 130, 80, 50, PALE, INK, 1.8, 3)
    s.rect(280, 124, 100, 56, "#e7eef8", INK, 1.8, 3)
    s.line(160, 155, 280, 155, ORANGE, 2.2)
    s.label(210, 140, "T", 16, "middle", ORANGE)
    s.label(120, 118, "m₁", 16, "middle")
    s.label(330, 110, "m₂", 16, "middle")
    s.arrow(380, 152, 500, 152, RED, 2.3, 11)
    s.label(440, 136, "F", 16, "middle", RED)
    s.label(330, 214, "corda horitzontal, pla llis o amb fregament", 14, "middle", MUTED, it=False)
    return s.svg(), "Dos blocs lligats per una corda en un pla horitzontal. La tensió és interna al sistema dels dos blocs i externa per a cadascun."


def f_atwood():
    s = Svg(680, 360)
    s.rect(0, 0, 680, 360, PAPER, "none", 0)
    # sostre i politja
    s.line(200, 36, 480, 36, INK, 3)
    cx, cy, r = 340, 78, 28
    s.circle(cx, cy, r, INK, PAPER, 2.2)
    s.circle(cx, cy, 4, INK, INK)
    # cordes
    s.line(cx - r, cy, cx - r, 200, ORANGE, 2)
    s.line(cx + r, cy, cx + r, 250, ORANGE, 2)
    s.rect(cx - r - 32, 200, 64, 48, PALE, INK, 1.8, 3)
    s.rect(cx + r - 36, 250, 72, 54, "#e7eef8", INK, 1.8, 3)
    s.label(cx - r, 188, "m₁", 16, "middle")
    s.label(cx + r, 238, "m₂", 16, "middle")
    s.label(cx, 36, "politja ideal", 14, "middle", MUTED, it=False)
    # fletxes moviment
    s.arrow(cx - r - 48, 230, cx - r - 48, 190, GREEN, 2, 9)
    s.arrow(cx + r + 52, 250, cx + r + 52, 300, GREEN, 2, 9)
    s.label(150, 300, "si m₂ > m₁, m₂ baixa", 15, "middle", MUTED, it=False)
    s.label(520, 140, "T igual als dos costats", 15, "start", ORANGE, it=False)
    s.label(520, 170, "a = (m₂ − m₁) g / (m₁ + m₂)", 15, "start", INK, it=False)
    return s.svg(), "Màquina d’Atwood senzilla: dos cossos units per una corda que passa per una politja ideal. La tensió és la mateixa als dos extrems."


def f_taula_politja():
    s = Svg(700, 280)
    s.rect(0, 0, 700, 280, PAPER, "none", 0)
    s.polygon([(40, 70), (430, 70), (430, 200), (40, 200)], fill="#f7f3ea", stroke=INK, sw=1.8)
    s.circle(430, 70, 22, INK, PAPER, 2)
    s.rect(120, 28, 90, 42, PALE, INK, 1.8, 3)
    s.label(165, 18, "M", 16, "middle")
    s.line(210, 49, 430, 49, ORANGE, 2)
    s.line(452, 70, 452, 150, ORANGE, 2)
    s.rect(424, 150, 56, 48, "#e7eef8", INK, 1.8, 3)
    s.label(452, 214, "m", 16, "middle")
    s.arrow(452, 198, 452, 248, BLUE, 2, 9)
    s.label(470, 230, "P", 16, "start", BLUE)
    s.label(250, 110, "corda i politja a la vora de la taula", 15, "middle", MUTED, it=False)
    return s.svg(), "Un bloc damunt la taula, lligat a un altre que penja. Si la taula és llisa, l’únic motor del moviment és el pes del bloc que penja."


def f_molla():
    s = Svg(680, 220)
    s.rect(0, 0, 680, 220, PAPER, "none", 0)
    s.line(40, 40, 40, 180, INK, 3)
    # molla en ziga-zaga
    pts = [(40, 110)]
    x = 40
    for i in range(8):
        x += 28
        y = 78 if i % 2 == 0 else 142
        pts.append((x, y))
    pts.append((x + 28, 110))
    s.polyline(pts, TEAL, 2.2)
    s.rect(x + 28, 86, 70, 48, PALE, INK, 1.8, 3)
    s.arrow(x + 98, 110, x + 180, 110, RED, 2.2, 10)
    s.label(x + 140, 92, "F = k x", 16, "middle", RED, it=False)
    s.label(160, 180, "allargament x", 15, "middle", MUTED, it=False)
    s.arrow(70, 168, x + 20, 168, MUTED, 1.4, 8)
    return s.svg(), "Força elàstica d’una molla. La força recuperadora és proporcional a la deformació: F = kx, i s’oposa a la deformació."


def f_revolt():
    s = Svg(680, 280)
    s.rect(0, 0, 680, 280, PAPER, "none", 0)
    # arc de la corba vist des de dalt
    s.path("M 80 200 Q 250 20 520 200", "#c5ccd6", 8)
    s.circle(300, 118, 16, ORANGE, "#f6d7b0", 2)
    s.arrow(300, 118, 390, 70, BLUE, 2.2, 10)
    s.label(400, 64, "v", 16, "start", BLUE)
    s.arrow(300, 118, 230, 150, PURPLE, 2.2, 10)
    s.label(210, 168, "f (cap al centre)", 15, "end", PURPLE, it=False)
    s.label(300, 230, "vista des de dalt", 14, "middle", MUTED, it=False)
    s.label(300, 256, "en un revolt pla, el fregament fa de força centrípeta", 15, "middle", INK, it=False)
    return s.svg(), "Cotxe en un revolt pla, vist des de dalt. El fregament de les rodes apunta cap al centre i proporciona l’acceleració centrípeta."


def f_corda():
    s = Svg(680, 300)
    s.rect(0, 0, 680, 300, PAPER, "none", 0)
    cx, cy, r = 250, 160, 90
    s.circle(cx, cy, 5, INK, INK)
    s.circle(cx + r, cy, 14, ORANGE, "#f6d7b0", 2)
    s.line(cx, cy, cx + r, cy, ORANGE, 2)
    s.label(cx + r / 2, cy - 14, "T", 16, "middle", ORANGE)
    s.arrow(cx + r, cy, cx + r, cy - 60, BLUE, 2.2, 10)
    s.label(cx + r + 16, cy - 36, "v", 16, "start", BLUE)
    s.path(f"M {cx+r} {cy-30} A {r} {r} 0 0 0 {cx+r*math.cos(0.8):.0f} {cy-r*math.sin(0.8):.0f}", "#c5ccd6", 1.4, "6 5")
    s.label(480, 120, "T = m v² / r", 18, "middle", INK, it=False)
    s.label(480, 160, "pla horitzontal llis", 15, "middle", MUTED, it=False)
    return s.svg(), "Massa lligada a una corda que gira en un pla horitzontal. La tensió és l’única força horitzontal i fa de força centrípeta."


def f_peralt():
    s = Svg(680, 300)
    s.rect(0, 0, 680, 300, PAPER, "none", 0)
    # secció del peralt
    s.polygon([(80, 230), (420, 230), (420, 200), (160, 80)], fill="#f6f1e6", stroke=INK, sw=1.8)
    s.label(300, 258, "peralt", 15, "middle", MUTED, it=False)
    # cotxe
    s.rect(230, 112, 70, 32, "#d9e8f8", INK, 1.8, 3)
    s.arrow(265, 112, 265, 50, GREEN, 2.2, 10)
    s.label(280, 74, "N", 16, "start", GREEN)
    s.arrow(265, 128, 265, 190, BLUE, 2.2, 10)
    s.label(280, 176, "P", 16, "start", BLUE)
    s.label(500, 110, "sense fregament:", 15, "middle", MUTED, it=False)
    s.label(500, 146, "tan θ = v² / (r g)", 18, "middle", INK, it=False)
    s.label(500, 186, "θ angle del peralt", 14, "middle", MUTED, it=False)
    return s.svg(), "Secció d’un revolt peraltat. Si no hi ha fregament, la component horitzontal de la normal és la força centrípeta."


def f_loop():
    s = Svg(680, 360)
    s.rect(0, 0, 680, 360, PAPER, "none", 0)
    cx, cy, r = 300, 200, 100
    s.circle(cx, cy, r, INK, "none", 2.2)
    s.line(40, cy + r, cx, cy + r, INK, 2.2)
    # cotxe dalt i baix
    s.rect(cx - 16, cy - r - 26, 32, 22, ORANGE, INK, 1.6, 3)
    s.rect(cx - 18, cy + r - 22, 36, 20, ORANGE, INK, 1.6, 3)
    # forces dalt
    s.arrow(cx, cy - r - 4, cx, cy - r + 40, BLUE, 2, 8)
    s.label(cx + 18, cy - r + 10, "P", 15, "start", BLUE)
    s.arrow(cx, cy - r - 4, cx, cy - r + 28, GREEN, 2, 8)
    s.label(cx - 28, cy - r + 24, "N", 15, "end", GREEN)
    # forces baix
    s.arrow(cx, cy + r - 2, cx, cy + r + 46, BLUE, 2, 8)
    s.label(cx + 20, cy + r + 36, "P", 15, "start", BLUE)
    s.arrow(cx, cy + r - 24, cx, cy + r - 70, GREEN, 2, 9)
    s.label(cx + 22, cy + r - 60, "N", 15, "start", GREEN)
    s.label(520, 120, "dalt: N + P = m v² / r", 15, "middle", INK, it=False)
    s.label(520, 156, "baix: N − P = m v² / r", 15, "middle", INK, it=False)
    s.label(520, 200, "mínim dalt: N = 0", 15, "middle", MUTED, it=False)
    s.label(520, 232, "v = √(g r)", 18, "middle", PURPLE, it=False)
    return s.svg(), "Lòpping vertical. Al capdamunt el pes i la normal apunten tots dos cap al centre; la velocitat mínima s’assoleix quan la normal s’anul·la."


def f_barres(etapes, titol_peu):
    """etapes: llista de (nom, Ec, Ep, Em) en joules, ja a escala relativa."""
    s = Svg(700, 320)
    s.rect(0, 0, 700, 320, PAPER, "none", 0)
    maxe = max(e[3] for e in etapes) or 1
    base = 250
    gap = 640 / len(etapes)
    colors = (BLUE, GREEN, INK)
    names = ("E_c", "E_p", "E_m")
    for i, (nom, ec, ep, em) in enumerate(etapes):
        x = 50 + i * gap
        vals = (ec, ep, em)
        for k, val in enumerate(vals):
            h = 180 * val / maxe
            xx = x + k * 28
            col = colors[k]
            s.rect(xx, base - h, 22, h, col if k < 2 else PAPER, col, 1.8, 2)
        s.label(x + 36, base + 24, nom, 15, "middle", INK, it=False, bold=True)
    s.rect(520, 36, 18, 14, BLUE, BLUE, 1)
    s.label(548, 43, "E_c", 15, "start", BLUE)
    s.rect(520, 60, 18, 14, GREEN, GREEN, 1)
    s.label(548, 67, "E_p", 15, "start", GREEN)
    s.rect(520, 84, 18, 14, PAPER, INK, 1.6)
    s.label(548, 91, "E_m", 15, "start", INK)
    return s.svg(), titol_peu


def f_barres_caiguda():
    return f_barres(
        [("dalt", 0, 100, 100), ("a mig camí", 50, 50, 100), ("terra", 100, 0, 100)],
        "Balanç d’energia en una caiguda sense fregament. L’energia mecànica es manté: el que perd l’energia potencial ho guanya la cinètica.",
    )


def f_barres_tir():
    return f_barres(
        [("sortida", 80, 20, 100), ("dalt", 40, 60, 100), ("mateixa altura", 80, 20, 100)],
        "Energia en un tir parabòlic sense fregament de l’aire. Al punt més alt l’energia cinètica no és zero: queda la part horitzontal de la velocitat.",
    )


def f_muntanya():
    s = Svg(700, 300)
    s.rect(0, 0, 700, 300, PAPER, "none", 0)
    perfil = [(40, 250), (120, 250), (230, 80), (340, 160), (470, 60), (600, 230), (670, 230)]
    s.polyline(perfil, INK, 2.4)
    s.line(40, 250, 670, 250, "#e4dfd4", 1)
    punts = [(120, 250, "A"), (230, 80, "B"), (340, 160, "C"), (470, 60, "D")]
    for x, y, nom in punts:
        s.circle(x, y, 7, ORANGE, "#f6d7b0", 2)
        s.label(x, y - 18, nom, 16, "middle", INK, it=False, bold=True)
    s.label(120, 272, "h = 0", 14, "middle", MUTED, it=False)
    s.label(250, 70, "més alt", 14, "start", MUTED, it=False)
    s.label(360, 250, "sense fregament, E_m constant", 15, "start", GREEN, it=False)
    return s.svg(), "Muntanya russa sense fregament. L’altura de cada punt fixa l’energia potencial; la velocitat es troba conservant l’energia mecànica."


def f_pendol():
    s = Svg(680, 340)
    s.rect(0, 0, 680, 340, PAPER, "none", 0)
    cx, cy = 230, 40
    L = 200
    s.line(cx - 30, cy, cx + 30, cy, INK, 3)
    # posició extrema
    ang = math.radians(50)
    x1 = cx + L * math.sin(ang)
    y1 = cy + L * math.cos(ang)
    s.line(cx, cy, x1, y1, MUTED, 1.5, )
    s.circle(x1, y1, 12, ORANGE, "#f6d7b0", 2)
    s.label(x1 + 18, y1, "es deixa anar", 14, "start", MUTED, it=False)
    # vertical
    s.line(cx, cy, cx, cy + L, "#c5ccd6", 1.3, "5 4")
    s.circle(cx, cy + L, 12, ORANGE, "#f6d7b0", 2)
    s.label(cx + 20, cy + L, "baix, v màxima", 14, "start", BLUE, it=False)
    s.path(f"M {cx} {cy+70} A 70 70 0 0 1 {cx+70*math.sin(ang):.0f} {cy+70*math.cos(ang):.0f}", TEAL, 1.6)
    s.label(cx + 36, cy + 78, "θ", 16, "start", TEAL)
    s.label(500, 120, "h = L (1 − cos θ)", 18, "middle", INK, it=False)
    s.label(500, 164, "v = √(2 g h) al punt baix", 16, "middle", BLUE, it=False)
    s.label(500, 210, "l’altura es mesura", 14, "middle", MUTED, it=False)
    s.label(500, 232, "des del punt més baix", 14, "middle", MUTED, it=False)
    return s.svg(), "Pèndol que es deixa anar des d’un angle θ. L’altura respecte del punt més baix és L(1 − cos θ). Sense fregament, l’energia mecànica es conserva."


def f_molla_energia():
    s = Svg(680, 240)
    s.rect(0, 0, 680, 240, PAPER, "none", 0)
    s.line(40, 40, 40, 200, INK, 3)
    def molla(x_end, y, color):
        pts = [(40, y)]
        x = 40
        n = 7
        while x < x_end - 20:
            x += (x_end - 60) / n
            yy = y - 22 if len(pts) % 2 == 0 else y + 22
            pts.append((x, yy))
        pts.append((x_end, y))
        s.polyline(pts, color, 2)
        s.rect(x_end, y - 20, 46, 40, PALE, INK, 1.6, 3)
    molla(220, 70, TEAL)
    s.label(300, 70, "comprimida: molta E_p elàstica", 15, "start", TEAL, it=False)
    molla(360, 160, BLUE)
    s.label(430, 160, "equilibri: E_c màxima", 15, "start", BLUE, it=False)
    return s.svg(), "Molla horitzontal sense fregament. A l’amplitud tota l’energia és potencial elàstica; en passar per l’equilibri, tota és cinètica."


def f_treball():
    s = Svg(680, 200)
    s.rect(0, 0, 680, 200, PAPER, "none", 0)
    s.arrow(80, 110, 420, 110, MUTED, 1.6, 9)
    s.label(430, 128, "desplaçament", 14, "start", MUTED, it=False)
    s.arrow(80, 110, 300, 48, RED, 2.4, 11)
    s.label(250, 52, "F", 16, "middle", RED)
    s.path("M 150 110 A 70 70 0 0 0 132 78", TEAL, 1.6)
    s.label(156, 86, "φ", 16, "start", TEAL)
    s.label(480, 80, "W = F Δx cos φ", 18, "start", INK, it=False)
    return s.svg(), "Treball d’una força constant. Només compta la component de la força en la direcció del desplaçament."


FIGURES = {
    "xt-mru": f_xt_mru,
    "xt-mrua": f_xt_mrua,
    "vt-mrua": f_vt_mrua,
    "at": f_at,
    "desplacament": f_desplacament,
    "caiguda": f_caiguda,
    "llancament": f_llancament,
    "tir-h": f_tir_horitzontal,
    "tir-p": f_tir_parabolic,
    "trajectoria": f_trajectoria,
    "mcu-angle": f_mcu_angle,
    "mcu-vec": f_mcu_vectors,
    "v-omega": f_v_omega,
    "parells": f_newton_parells,
    "fma": f_fma,
    "dcl": lambda: f_dcl_horitzontal(False, True),
    "dcl-f": lambda: f_dcl_horitzontal(True, True),
    "inclinat": lambda: f_inclinat(30, True),
    "inclinat-llis": lambda: f_inclinat(30, False),
    "dos-blocs": f_dos_blocs,
    "atwood": f_atwood,
    "taula": f_taula_politja,
    "molla": f_molla,
    "revolt": f_revolt,
    "corda": f_corda,
    "peralt": f_peralt,
    "loop": f_loop,
    "barres-caiguda": f_barres_caiguda,
    "barres-tir": f_barres_tir,
    "muntanya": f_muntanya,
    "pendol": f_pendol,
    "molla-e": f_molla_energia,
    "treball": f_treball,
}


def svg_de(clau):
    svg, peu = FIGURES[clau]()
    return svg, peu
