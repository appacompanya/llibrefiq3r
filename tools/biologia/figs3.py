"""Figures del tema 3 (Metabolisme)."""
import math
from svg import Fig, INK, MUTED, LINE, col, light


def fig_atp():
    f = Fig(640, 230, "Estructura de l'ATP")
    y = 120
    f.box(30, y - 34, 110, 68, "adenina", color="blau", size=15)
    f.poly([(185, y - 30), (235, y - 46), (270, y - 8), (245, y + 34), (195, y + 30)], fill=light("vermell"), stroke=col("vermell"), sw=2)
    f.text(228, y, "ribosa", size=14, weight=700)
    f.line(140, y, 185, y - 4, sw=2)
    for k in range(3):
        cx = 320 + k * 90
        f.circle(cx, y, 28, fill=light("groc"), stroke=col("groc"), sw=2)
        f.text(cx, y, "P", size=17, weight=700)
        f.line(cx - 28 - (22 if k else 26), y, cx - 28, y, sw=2)
        f.text(cx, y + 46, "αβγ"[k], size=14, fill=MUTED, weight=700)
    f.line(262, y - 4, 292, y, sw=2)
    for k in (1, 2):
        x = 320 + k * 90 - 45
        f.text(x, y - 34, "≈", size=18, weight=700, fill=col("taronja"))
    f.text(410, 34, "enllaços fosfoanhídrid: la hidròlisi allibera energia", size=13, weight=700, fill=col("taronja"))
    f.rect(25, 70, 255, 100, stroke=col("teal"), dash="5 4", rx=12)
    f.text(152, 190, "adenosina (nucleòsid)", size=13, fill=col("teal"), weight=700)
    f.text(410, 200, "ATP + H₂O → ADP + P_{i}  (ΔG < 0)", size=15, weight=700)
    return f.svg()


def fig_cat_anab():
    f = Fig(640, 260, "Catabolisme i anabolisme")
    f.box(20, 30, 230, 70, "Catabolisme\nmolècules grans → petites\n(oxidació)", color="taronja", size=14)
    f.box(390, 30, 230, 70, "Anabolisme\nmolècules petites → grans\n(reducció)", color="blau", size=14)
    f.box(240, 160, 160, 70, "ATP\nNADH · NADPH · FADH₂", color="groc", size=14)
    f.arrow(135, 102, 250, 170, color=col("taronja"), sw=2.4)
    f.arrow(390, 170, 505, 102, color=col("blau"), sw=2.4)
    f.text(150, 160, "allibera energia\ni poder reductor", size=12, fill=col("taronja"), anchor="end")
    f.text(490, 160, "en gasta", size=12, fill=col("blau"), anchor="start")
    f.text(135, 125, "", size=12)
    f.text(320, 22, "exemples: glucosa → CO₂ (respiració) · CO₂ → glucosa (Calvin)", size=12, fill=MUTED)
    return f.svg()


def fig_glucolisi():
    f = Fig(640, 330, "Balanç de la glucòlisi")
    f.text(320, 20, "Glucòlisi · citosol · sense O₂", size=15, weight=700, fill=col("teal"))
    f.box(240, 40, 160, 40, "glucosa (6C)", color="verd", size=14)
    f.arrow(320, 82, 320, 116)
    f.pill(470, 99, "−2 ATP", color="vermell", size=13, solid=True)
    f.text(360, 99, "fase de despesa", size=12, fill=MUTED, anchor="start")
    f.box(210, 118, 220, 40, "fructosa-1,6-bisfosfat", color="verd", size=14)
    f.arrow(300, 160, 230, 196); f.arrow(340, 160, 410, 196)
    for x in (160, 400):
        f.box(x, 198, 100, 36, "triosa-P", color="verd", size=13)
        f.arrow(x + 50, 236, x + 50, 266)
        f.box(x, 268, 100, 36, "piruvat (3C)", color="taronja", size=13)
    f.pill(70, 250, "+2 NADH", color="lila", size=13, solid=True)
    f.pill(570, 250, "+4 ATP", color="verd", size=13, solid=True)
    f.text(320, 250, "fase de guany", size=12, fill=MUTED)
    f.rect(470, 288, 160, 36, fill="#fff", stroke=INK, sw=2, rx=8)
    f.text(550, 306, "net: 2 ATP + 2 NADH", size=13, weight=700)
    return f.svg()


def fig_respiracio():
    f = Fig(640, 470, "Visió de conjunt de la respiració cel·lular")
    # citosol i mitocondri
    f.rect(10, 30, 620, 430, fill="#fdf7ec", stroke=LINE, rx=16)
    f.text(30, 50, "CITOSOL", size=12, weight=700, fill=MUTED, anchor="start")
    f.rect(210, 70, 410, 380, fill="#fbe3cf", stroke=col("taronja"), sw=3, rx=40)
    f.rect(222, 82, 386, 356, fill="#fff3e6", stroke=col("taronja"), sw=2, rx=32)
    f.text(600, 100, "MITOCONDRI", size=12, weight=700, fill=col("taronja"), anchor="end")
    f.text(420, 118, "matriu", size=12, fill=MUTED)
    f.box(30, 80, 150, 40, "glucosa", color="verd", size=14)
    f.arrow(105, 122, 105, 160)
    f.box(30, 162, 150, 54, "Glucòlisi", color="verd", size=16)
    f.pill(105, 238, "2 ATP · 2 NADH", color="verd", size=12)
    f.arrow(105, 254, 105, 288)
    f.box(30, 290, 150, 40, "2 piruvat", color="taronja", size=14)
    f.arrow(180, 310, 250, 180, color=INK)
    f.box(250, 150, 150, 50, "2 acetil-CoA", color="taronja", size=14)
    f.pill(325, 222, "2 NADH · 2 CO₂", color="taronja", size=12)
    f.arrow(325, 236, 325, 262)
    f.circle(325, 320, 56, fill=light("vermell"), stroke=col("vermell"), sw=2.5)
    f.text(325, 312, "Cicle de", size=14, weight=700); f.text(325, 330, "Krebs", size=14, weight=700)
    f.text(325, 400, "×2: 6 NADH · 2 FADH₂\n2 GTP · 4 CO₂", size=12, weight=700, fill=col("vermell"))
    # cadena
    f.rect(470, 140, 120, 280, fill=light("lila"), stroke=col("lila"), sw=2, rx=12)
    f.text(530, 162, "Cadena\nrespiratòria", size=13, weight=700)
    f.text(530, 200, "membrana\ninterna", size=11, fill=MUTED)
    for k in range(4):
        f.rect(490, 225 + k * 26, 80, 18, fill="#fff", stroke=col("lila"), rx=4)
        f.text(530, 234 + k * 26, ["complex I", "complex II · Q", "complex III · cit c", "complex IV"][k], size=10)
    f.text(530, 345, "½ O₂ → H₂O", size=12, weight=700, fill=col("blau"))
    f.box(490, 365, 80, 36, "ATP-sintasa", color="groc", size=11)
    f.arrow(395, 280, 470, 250, color=col("lila"), sw=2.2)
    f.text(430, 245, "NADH,\nFADH₂", size=11, fill=col("lila"), weight=700)
    f.arrow(325, 175, 470, 200, color=col("lila"), sw=1.6, dash="5 4")
    f.pill(530, 425, "≈ 26–28 ATP", color="groc", size=12, solid=True)
    f.text(320, 18, "Total per glucosa: ≈ 30–32 ATP (2 + 2 de substrat, la resta de la fosforilació oxidativa)", size=12, fill=INK, weight=700)
    return f.svg()


def fig_krebs():
    f = Fig(640, 430, "El cicle de Krebs")
    cx, cy, R = 300, 225, 150
    names = [("citrat", "6C"), ("isocitrat", "6C"), ("α-cetoglutarat", "5C"), ("succinil-CoA", "4C"), ("succinat", "4C"), ("fumarat", "4C"), ("malat", "4C"), ("oxalacetat", "4C")]
    pos = []
    for i in range(8):
        a = math.radians(-90 + i * 45 + 22.5)
        pos.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    f.circle(cx, cy, R, stroke=col("vermell"), sw=2, dash="2 6")
    for i in range(8):
        a0 = math.radians(-90 + i * 45 + 22.5 + 9)
        a1 = math.radians(-90 + (i + 1) * 45 + 22.5 - 9)
        f.arrowpath(f"M{cx+R*math.cos(a0):.1f},{cy+R*math.sin(a0):.1f} A{R},{R} 0 0 1 {cx+R*math.cos(a1):.1f},{cy+R*math.sin(a1):.1f}", color=col("vermell"), sw=2.4)
    for (n, c), (x, y) in zip(names, pos):
        w = max(80, len(n) * 8.2)
        f.rect(x - w / 2, y - 18, w, 36, fill="#fff", stroke=col("vermell"), sw=1.8, rx=10)
        f.text(x, y - 5, n, size=13, weight=700); f.text(x, y + 9, c, size=10, fill=MUTED)
    # entrada
    f.box(20, 22, 130, 38, "acetil-CoA (2C)", color="taronja", size=13)
    f.arrow(150, 41, pos[0][0] - 30, pos[0][1] - 18, color=col("taronja"), sw=2.2)
    f.text(cx, cy - 8, "matriu", size=13, fill=MUTED)
    f.text(cx, cy + 12, "1 volta per acetil-CoA", size=12, fill=MUTED)

    def out(i, j, label, color, dx, dy):
        a = math.radians(-90 + (i + 0.5) * 45 + 22.5)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        f.arrow(x, y, x + dx * 0.6, y + dy * 0.6, color=col(color), sw=1.8)
        f.pill(x + dx, y + dy, label, color=color, size=12, solid=True)

    out(1, 2, "NADH + CO₂", "lila", 95, 10)
    out(2, 3, "NADH + CO₂", "lila", 70, 55)
    out(3, 4, "GTP", "verd", 0, 70)
    out(4, 5, "FADH₂", "blau", -75, 50)
    out(6, 7, "NADH", "lila", -85, -12)
    f.text(560, 400, "per volta: 2 CO₂, 3 NADH,\n1 FADH₂, 1 GTP", size=13, weight=700, anchor="end")
    return f.svg()


def fig_cadena():
    f = Fig(640, 340, "Cadena respiratòria i ATP-sintasa a la membrana mitocondrial interna")
    y1, y2 = 120, 200
    f.rect(0, y1, 640, y2 - y1, fill="#f5e7d0", stroke="none", rx=0)
    f.line(0, y1, 640, y1, stroke="#c4651a", sw=2); f.line(0, y2, 640, y2, stroke="#c4651a", sw=2)
    f.text(10, 30, "Espai intermembranós: molts H⁺", size=14, weight=700, anchor="start", fill=col("vermell"))
    f.text(10, 300, "Matriu", size=14, weight=700, anchor="start", fill=col("taronja"))
    comps = [(70, "I"), (170, "II"), (290, "III"), (430, "IV")]
    for x, n in comps:
        h = 110 if n != "II" else 60
        y = y1 - 15 if n != "II" else y2 - 40
        f.rect(x - 34, y, 68, h, fill=light("lila"), stroke=col("lila"), sw=2, rx=14)
        f.text(x, y + h / 2, n, size=18, weight=700, fill=col("lila"))
    f.circle(230, 160, 14, fill=light("groc"), stroke=col("groc"), sw=1.6); f.text(230, 160, "Q", size=13, weight=700)
    f.circle(360, 108, 13, fill=light("vermell"), stroke=col("vermell"), sw=1.6); f.text(360, 108, "c", size=13, weight=700)
    # electrons
    f.arrowpath("M100,215 C150,240 200,190 222,170", color=col("blau"), sw=2)
    f.arrowpath("M195,195 C205,185 212,178 218,172", color=col("blau"), sw=2)
    f.arrowpath("M244,160 C262,160 262,160 256,160", color=col("blau"), sw=2)
    f.arrowpath("M325,110 C335,104 340,104 347,106", color=col("blau"), sw=2)
    f.arrowpath("M373,108 C390,110 395,112 398,118", color=col("blau"), sw=2)
    f.text(70, 255, "NADH → NAD⁺", size=12, weight=700, fill=col("lila"))
    f.text(170, 255, "FADH₂ → FAD", size=12, weight=700, fill=col("lila"))
    f.text(430, 255, "½ O₂ + 2 H⁺ → H₂O", size=12, weight=700, fill=col("blau"))
    for x in (70, 290, 430):
        f.arrow(x, y2 + 30, x, y1 - 40, color=col("vermell"), sw=2)
        f.text(x + 12, y1 - 50, "H⁺", size=13, weight=700, fill=col("vermell"), anchor="start")
    # ATP-sintasa
    X = 560
    f.rect(X - 22, y1 - 10, 44, y2 - y1 + 20, fill=light("groc"), stroke=col("groc"), sw=2, rx=8)
    f.circle(X, y2 + 40, 34, fill=light("groc"), stroke=col("groc"), sw=2)
    f.text(X, y2 + 40, "ATP-\nsintasa", size=11, weight=700)
    f.arrow(X, y1 - 50, X, y2 + 2, color=col("vermell"), sw=2.4)
    f.text(X + 14, y1 - 58, "H⁺", size=13, weight=700, fill=col("vermell"), anchor="start")
    f.text(X, 300, "ADP + P_{i} → ATP", size=13, weight=700, fill=col("groc"))
    f.text(320, 330, "e⁻: I o II → Q → III → citocrom c → IV → O₂", size=13, fill=col("blau"), weight=700)
    return f.svg()


def fig_fermentacions():
    f = Fig(640, 300, "Fermentació làctica i fermentació alcohòlica")
    f.box(230, 20, 180, 40, "glucosa", color="verd", size=14)
    f.arrow(320, 62, 320, 92)
    f.text(330, 77, "glucòlisi: 2 ATP nets", size=12, anchor="start", fill=MUTED)
    f.box(230, 94, 180, 40, "2 piruvat", color="taronja", size=14)
    f.pill(320, 152, "2 NADH", color="lila", size=12, solid=True)
    # làctica
    f.arrow(250, 136, 130, 196)
    f.box(40, 198, 180, 44, "2 lactat", color="vermell", size=15)
    f.text(130, 262, "Làctica: múscul, Lactobacillus\nsense CO₂", size=12, fill=MUTED)
    f.text(170, 165, "NADH → NAD⁺", size=12, weight=700, fill=col("lila"), anchor="end")
    # alcohòlica
    f.arrow(390, 136, 470, 180)
    f.box(430, 180, 160, 36, "2 acetaldehid", color="groc", size=13)
    f.pill(610, 155, "2 CO₂", color="gris", size=12, solid=True)
    f.arrow(510, 218, 510, 236)
    f.box(430, 238, 160, 40, "2 etanol", color="groc", size=15)
    f.text(510, 292, "Alcohòlica: llevats (pa, vi, cervesa)", size=12, fill=MUTED)
    f.text(420, 228, "NADH → NAD⁺", size=12, weight=700, fill=col("lila"), anchor="end")
    return f.svg()


def fig_fase_lluminosa():
    f = Fig(640, 380, "Fase lluminosa a la membrana del tilacoide")
    y1, y2 = 140, 220
    f.rect(0, y1, 640, y2 - y1, fill="#dbeed8", stroke="none", rx=0)
    f.line(0, y1, 640, y1, stroke=col("verd"), sw=2); f.line(0, y2, 640, y2, stroke=col("verd"), sw=2)
    f.text(10, 30, "Estroma", size=14, weight=700, anchor="start", fill=col("verd"))
    f.text(10, 350, "Lumen del tilacoide: molts H⁺", size=14, weight=700, anchor="start", fill=col("vermell"))
    def cx(x, w, t, c):
        f.rect(x - w / 2, y1 - 20, w, y2 - y1 + 40, fill=light(c), stroke=col(c), sw=2, rx=12)
        f.text(x, (y1 + y2) / 2, t, size=13, weight=700)
    cx(90, 80, "FS II\nP680", "verd")
    cx(250, 70, "cit\nb₆f", "lila")
    cx(400, 80, "FS I\nP700", "verd")
    f.circle(170, 180, 13, fill=light("groc"), stroke=col("groc")); f.text(170, 180, "PQ", size=10, weight=700)
    f.circle(325, 232, 13, fill=light("blau"), stroke=col("blau")); f.text(325, 232, "PC", size=10, weight=700)
    for x in (90, 400):
        f.text(x, 60, "☀", size=26, fill="#e6a700")
        f.arrow(x, 76, x, 112, color="#e6a700", sw=2.2)
    f.text(90, 290, "2 H₂O → O₂ + 4 H⁺ + 4 e⁻", size=12, weight=700, fill=col("blau"))
    f.arrow(90, 278, 90, 245, color=col("blau"))
    f.arrowpath("M130,190 C150,195 155,185 160,182", color=col("blau"))
    f.arrowpath("M183,180 C205,180 215,180 214,180", color=col("blau"))
    f.arrowpath("M285,200 C300,225 305,230 311,232", color=col("blau"))
    f.arrowpath("M339,232 C352,230 357,215 359,210", color=col("blau"))
    f.arrowpath("M420,120 C430,95 450,80 470,75", color=col("blau"))
    f.box(470, 55, 150, 40, "NADP⁺ → NADPH", color="lila", size=12)
    f.arrow(250, y2 + 25, 250, y1 - 35, color=col("vermell"), sw=2)
    f.text(262, y1 - 40, "H⁺", size=13, weight=700, fill=col("vermell"), anchor="start")
    X = 560
    f.rect(X - 22, y1 - 10, 44, y2 - y1 + 20, fill=light("groc"), stroke=col("groc"), sw=2, rx=8)
    f.circle(X, y1 - 50, 32, fill=light("groc"), stroke=col("groc"), sw=2)
    f.text(X, y1 - 50, "ATP-\nsintasa", size=11, weight=700)
    f.arrow(X, y2 + 40, X, y1 - 16, color=col("vermell"), sw=2.4)
    f.text(X + 14, y2 + 46, "H⁺", size=13, weight=700, fill=col("vermell"), anchor="start")
    f.text(X, 20, "ADP + P_{i} → ATP", size=12, weight=700, fill=col("groc"))
    f.text(320, 372, "L’O₂ surt de l’aigua (fotòlisi al FS II). Productes cap a l’estroma: ATP i NADPH.", size=12, fill=MUTED)
    return f.svg()


def fig_zeta():
    f = Fig(640, 330, "Esquema en Z de la fase lluminosa")
    f.line(50, 300, 50, 30, sw=1.6); f.text(30, 165, "potencial redox (energia dels e⁻)", size=12, rot=-90, fill=MUTED)
    f.text(56, 36, "més reductor", size=11, anchor="start", fill=MUTED); f.text(56, 294, "més oxidant", size=11, anchor="start", fill=MUTED)
    pts = [(110, 270, "H₂O"), (170, 250, "P680"), (210, 70, "P680*"), (280, 130, "PQ"), (340, 170, "cit b₆f"), (400, 200, "PC"), (440, 210, "P700"), (480, 50, "P700*"), (540, 90, "Fd"), (600, 120, "NADP⁺")]
    for (x, y, t), (x2, y2, _) in zip(pts, pts[1:]):
        if t in ("P680", "P700"):
            f.arrow(x, y - 8, x2, y2 + 10, color="#e6a700", sw=4)
        else:
            f.arrow(x + 10, y, x2 - 12, y2, color=col("blau"), sw=2)
    for x, y, t in pts:
        f.text(x, y + (16 if t in ("H₂O", "P680", "P700", "PC") else -14), t, size=12, weight=700)
    f.text(190, 160, "llum", size=12, fill="#b38600", weight=700, anchor="end")
    f.text(462, 140, "llum", size=12, fill="#b38600", weight=700, anchor="end")
    f.text(110, 300, "O₂ + H⁺", size=11, fill=col("blau"))
    f.text(600, 150, "NADPH", size=12, weight=700, fill=col("lila"))
    f.text(320, 315, "Els e⁻ baixen entre fotosistemes i això bombeja H⁺ (ATP). En la fosforilació cíclica, tornen del FS I al cit b₆f.", size=11, fill=MUTED)
    return f.svg()


def fig_calvin():
    f = Fig(640, 380, "Cicle de Calvin")
    cx, cy, R = 320, 200, 120
    f.circle(cx, cy, R, stroke=col("verd"), sw=2.5, dash="2 6")
    nodes = [(-90, "RuBP (5C)\n×3"), (30, "3-fosfoglicerat\n×6"), (150, "gliceraldehid-3-P\n×6")]
    P = {}
    for a, t in nodes:
        r = math.radians(a)
        x, y = cx + R * math.cos(r), cy + R * math.sin(r)
        P[a] = (x, y)
        f.rect(x - 75, y - 24, 150, 48, fill="#fff", stroke=col("verd"), sw=2, rx=12)
        f.text(x, y, t, size=13, weight=700)
    def arcc(a0, a1):
        f.arrowpath(f"M{cx+R*math.cos(math.radians(a0)):.1f},{cy+R*math.sin(math.radians(a0)):.1f} A{R},{R} 0 0 1 {cx+R*math.cos(math.radians(a1)):.1f},{cy+R*math.sin(math.radians(a1)):.1f}", color=col("verd"), sw=2.6)
    arcc(-60, 5); arcc(55, 125); arcc(175, 250)
    f.text(cx + 160, cy - 115, "1. Fixació (rubisco)", size=13, weight=700, fill=col("verd"), anchor="start")
    f.pill(cx + 215, cy - 80, "3 CO₂", color="gris", size=12, solid=True)
    f.text(cx + 115, cy + 140, "2. Reducció", size=13, weight=700, fill=col("verd"), anchor="start")
    f.pill(cx + 200, cy + 115, "6 ATP · 6 NADPH", color="lila", size=12)
    f.text(cx - 210, cy - 40, "3. Regeneració", size=13, weight=700, fill=col("verd"), anchor="end")
    f.pill(cx - 240, cy - 12, "3 ATP", color="groc", size=12)
    f.arrow(P[150][0] - 40, P[150][1] + 24, 120, 335, color=col("taronja"), sw=2.4)
    f.pill(200, 352, "1 G3P surt → glucosa, midó, sacarosa", color="taronja", size=12, solid=True)
    f.text(cx, cy, "estroma", size=13, fill=MUTED)
    f.text(cx, 20, "Per cada CO₂: 3 ATP i 2 NADPH · per glucosa (6 CO₂): 18 ATP i 12 NADPH", size=12, weight=700)
    return f.svg()
