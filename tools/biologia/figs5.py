"""Figures refetes a la segona revisió (cèl·lules, cromosomes, virus, homologia…)."""
import math
from svg import Fig, INK, MUTED, LINE, col, light

MEMB = "#d98c3a"
CYTO = "#fdf7ec"
RED, BLU = "#d0453b", "#3b74c4"


# ------------------------------------------------------------ etiquetes
def leader(f, x1, y1, x2, y2, label, anchor="start", size=13):
    f.line(x1, y1, x2, y2, stroke="#6b7280", sw=1)
    f.circle(x1, y1, 2.4, fill=INK, stroke="none")
    f.line(x2, y2, x2 + (6 if anchor == "start" else -6), y2, stroke="#6b7280", sw=1)
    f.text(x2 + (10 if anchor == "start" else -10), y2, label, size=size, anchor=anchor)


def labels(f, items, x, y0, y1, anchor="start", size=13):
    """Columna d'etiquetes ordenades per l'altura del punt: les línies no es creuen."""
    items = sorted(items, key=lambda t: t[1])
    lines = [lab.count("\n") + 1 for _, _, lab in items]
    tot, acc = sum(lines), 0
    for (tx, ty, lab), n in zip(items, lines):
        c = acc + n / 2
        acc += n
        yy = y0 + (y1 - y0) * c / tot if len(items) > 1 else (y0 + y1) / 2
        leader(f, tx, ty, x, yy, lab, anchor, size)


def two_sides(f, items, xmid, xl, xr, y0, y1, size=13):
    labels(f, [i for i in items if i[0] < xmid], xl, y0, y1, "end", size)
    labels(f, [i for i in items if i[0] >= xmid], xr, y0, y1, "start", size)


# ------------------------------------------------------------ orgànuls
def ribos(f, pts, r=2.6, color="#6b4c9a"):
    for x, y in pts:
        f.circle(x, y, r, fill=color, stroke="none")


def mito(f, cx, cy, w, h, rot=0):
    """Mitocondri: les crestes són plecs de la membrana interna i queden sempre a dins."""
    f.raw(f'<g transform="rotate({rot} {cx} {cy})">')
    f.ellipse(cx, cy, w / 2, h / 2, fill="#fbe3cf", stroke="#c4651a", sw=1.6)
    a, b = w / 2 - 3.5, h / 2 - 3.5
    f.ellipse(cx, cy, a, b, fill="#fff3e6", stroke="#c4651a", sw=1.1)
    n = max(3, int(w / 11))
    for i in range(n):
        x = cx - a * 0.72 + i * (2 * a * 0.72) / (n - 1)
        yy = b * math.sqrt(max(0.0, 1 - ((x - cx) / a) ** 2))
        top = i % 2 == 0
        y0 = cy - yy if top else cy + yy
        depth = yy * 1.25
        y1 = y0 + depth if top else y0 - depth
        f.path(f"M{x:.1f},{y0:.1f} L{x:.1f},{y1:.1f}", stroke="#c4651a", sw=2.6)
    f.raw("</g>")


def chloro(f, cx, cy, w, h, rot=0):
    f.raw(f'<g transform="rotate({rot} {cx} {cy})">')
    f.ellipse(cx, cy, w / 2, h / 2, fill="#e3f2e8", stroke="#2e7d4f", sw=1.6)
    f.ellipse(cx, cy, w / 2 - 3, h / 2 - 3, fill="#eef8f1", stroke="#2e7d4f", sw=0.8)
    for k in (-1, 0, 1):
        x = cx + k * w * 0.26
        for j in range(4):
            f.rect(x - 6, cy - 8 + j * 4, 12, 3.2, fill="#4caf6e", stroke="none", rx=1.5)
    f.line(cx - w * 0.26 + 6, cy, cx + w * 0.26 - 6, cy, stroke="#2e7d4f", sw=1)
    f.raw("</g>")


def golgi(f, x, y, s=1.0, n=4):
    for k in range(n):
        w = (52 - k * 6) * s
        f.path(f"M{x - w/2:.1f},{y + k*8*s:.1f} q{w/2:.1f},{-12*s:.1f} {w:.1f},0", stroke=col("taronja"), sw=3.4 * s)
    f.circle(x + 34 * s, y - 2 * s, 4 * s, fill="#fbd3b0", stroke=col("taronja"), sw=1.2)
    f.circle(x + 30 * s, y + 30 * s, 4 * s, fill="#fbd3b0", stroke=col("taronja"), sw=1.2)


def rer(f, x, y, w=90, rows=3, s=1.0):
    pts = []
    for k in range(rows):
        yy = y + k * 11 * s
        f.path(f"M{x},{yy} q{w/4},{-7*s} {w/2},0 t{w/2},0", stroke="#2f6fb5", sw=2.6 * s, extra='stroke-opacity="0.9"')
        pts += [(x + 6 + j * (w - 12) / 6, yy - 3.4 * s * (1 if j % 2 else -1) * 0.2 - 3) for j in range(7)]
    ribos(f, pts, r=1.8 * s)


def ser(f, x, y, s=1.0):
    for k in range(3):
        f.path(f"M{x},{y + k*10*s} q12,-9 24,0 t24,0 t24,0", stroke="#2fa0b5", sw=2.4 * s)


def centriols(f, x, y):
    f.rect(x - 4, y - 11, 8, 22, fill="#374151", stroke="none", rx=2)
    f.rect(x + 6, y - 4, 22, 8, fill="#374151", stroke="none", rx=2)


# ------------------------------------------------------------ cèl·lules
def fig_bacteri():
    f = Fig(720, 330, "Estructura d'una cèl·lula bacteriana")
    cx, cy = 360, 160
    # flagel
    f.path(f"M{cx+150},{cy+45} c20,8 22,30 45,32 s30,22 52,28 s28,24 48,30", stroke=INK, sw=2.4)
    # fímbries
    for a in range(-160, 170, 22):
        r = math.radians(a)
        x0, y0 = cx + 172 * math.cos(r), cy + 74 * math.sin(r)
        x1, y1 = cx + 192 * math.cos(r), cy + 90 * math.sin(r)
        if abs(a) < 15:
            continue
        f.line(x0, y0, x1, y1, stroke="#8b7a5a", sw=1.2)
    # càpsula, paret, membrana
    f.rect(cx - 180, cy - 82, 360, 164, fill="#f4eedb", stroke="#c8b98c", sw=1.2, rx=82, dash="4 3")
    f.rect(cx - 166, cy - 68, 332, 136, fill="#dbe8f6", stroke=col("blau"), sw=4.5, rx=68)
    f.rect(cx - 159, cy - 61, 318, 122, fill="#eef5fb", stroke="#d98c3a", sw=2, rx=61)
    # pilus sexual
    f.line(cx - 80, cy - 68, cx - 120, cy - 128, stroke="#8b7a5a", sw=3)
    # nucleoide
    f.path(f"M{cx-70},{cy+5} c15,-40 55,-10 70,-30 s45,25 25,45 s-55,20 -70,0 s-45,5 -25,-15", stroke=col("lila"), sw=2.2)
    f.path(f"M{cx-50},{cy+18} c20,8 35,-22 60,-5", stroke=col("lila"), sw=2)
    # plasmidis
    f.circle(cx + 90, cy - 22, 11, stroke=col("lila"), sw=2)
    f.circle(cx + 115, cy + 25, 8, stroke=col("lila"), sw=2)
    # ribosomes i inclusions
    ribos(f, [(cx - 120, cy - 30), (cx - 130, cy + 20), (cx - 100, cy + 40), (cx - 40, cy - 45), (cx + 20, cy + 45), (cx + 60, cy - 45), (cx + 140, cy - 10), (cx + 70, cy + 30), (cx - 10, cy + 50), (cx + 40, cy - 30), (cx - 145, cy - 5), (cx + 135, cy + 40)])
    f.circle(cx - 110, cy + 5, 9, fill="#f2e3a6", stroke="#b39b3a", sw=1.2)
    items = [(cx - 160, cy - 40, "membrana plasmàtica"), (cx - 168, cy + 30, "paret cel·lular"), (cx - 176, cy + 66, "càpsula"),
             (cx - 120, cy - 128, "pilus sexual"), (cx - 110, cy + 5, "inclusió (reserva)"), (cx + 135, cy + 40, "ribosomes 70S"),
             (cx + 30, cy - 20, "nucleoide: DNA circular"), (cx + 90, cy - 22, "plasmidi"), (cx + 150, cy - 80, "fímbries"),
             (cx + 230, cy + 98, "flagel")]
    two_sides(f, items, cx - 60, 150, 560, 30, 300)
    return f.svg()


def fig_pro_euc():
    f = Fig(780, 330, "Cèl·lula procariota i cèl·lula eucariota")
    # procariota (a escala relativa: més petita)
    f.text(210, 22, "Procariota (bacteri)", size=16, weight=700, fill=col("teal"))
    f.text(210, 42, "1–5 µm · sense nucli", size=12, fill=MUTED)
    bx, by = 210, 170
    f.rect(bx - 85, by - 34, 170, 68, fill="#dbe8f6", stroke=col("blau"), sw=3.5, rx=34)
    f.rect(bx - 80, by - 29, 160, 58, fill="#eef5fb", stroke="#d98c3a", sw=1.6, rx=29)
    f.path(f"M{bx-35},{by+2} c10,-20 25,0 35,-12 s25,12 15,22 s-30,8 -50,-10", stroke=col("lila"), sw=2)
    f.circle(bx + 45, by - 8, 6, stroke=col("lila"), sw=1.6)
    ribos(f, [(bx - 60, by - 10), (bx - 55, by + 12), (bx + 10, by + 20), (bx + 55, by + 14), (bx + 25, by - 18), (bx - 15, by - 20)], r=2.2)
    f.path(f"M{bx+85},{by} c12,-10 22,10 34,0 s22,10 30,2", stroke=INK, sw=2)
    labels(f, [(bx - 85, by - 20, "paret i membrana"), (bx - 55, by + 12, "ribosomes 70S"), (bx - 20, by + 5, "nucleoide\n(DNA circular)")], 110, 90, 270, "end", 12)
    labels(f, [(bx + 45, by - 8, "plasmidi"), (bx + 140, by + 2, "flagel")], 300, 100, 240, "start", 12)
    # eucariota
    X, Y = 580, 175
    f.text(X, 22, "Eucariota (cèl·lula animal)", size=16, weight=700, fill=col("teal"))
    f.text(X, 42, "10–30 µm · nucli i orgànuls", size=12, fill=MUTED)
    f.ellipse(X, Y, 115, 112, fill=CYTO, stroke=MEMB, sw=2.5)
    f.circle(X - 15, Y - 10, 38, fill="#e9e2f5", stroke=col("lila"), sw=2.4)
    f.circle(X - 22, Y - 16, 11, fill="#b9a6dd", stroke="none")
    rer(f, X - 70, Y + 45, w=70, rows=2)
    golgi(f, X + 55, Y + 30, s=0.8)
    mito(f, X + 60, Y - 55, 44, 20, 20)
    mito(f, X - 70, Y - 55, 40, 18, -30)
    labels(f, [(X - 15, Y - 45, "nucli\n(doble membrana)"), (X - 40, Y + 47, "reticle\nendoplasmàtic")], 445, 215, 295, "end", 12)
    labels(f, [(X + 60, Y - 55, "mitocondri"), (X + 55, Y + 35, "aparell de\nGolgi"), (X + 112, Y + 20, "membrana\nplasmàtica")], 708, 80, 290, "start", 12)
    f.text(30, 312, "La procariota s’ha dibuixat més petita, però a escala seria unes 10 vegades menor.", size=11, fill=MUTED, anchor="start")
    return f.svg()


def fig_animal():
    f = Fig(760, 380, "Cèl·lula animal")
    cx, cy = 380, 190
    f.path(f"M{cx-190},{cy} C{cx-195},{cy-150} {cx+170},{cy-165} {cx+192},{cy-15} C{cx+210},{cy+150} {cx-180},{cy+160} {cx-190},{cy} z", fill=CYTO, stroke=MEMB, sw=2.6)
    # nucli
    f.circle(cx - 30, cy - 5, 58, fill="#e9e2f5", stroke=col("lila"), sw=3)
    for a in range(0, 360, 45):
        r = math.radians(a + 20)
        f.circle(cx - 30 + 58 * math.cos(r), cy - 5 + 58 * math.sin(r), 3.2, fill="#fff", stroke=col("lila"), sw=1.2)
    f.circle(cx - 40, cy - 15, 17, fill="#a58bd0", stroke="none")
    for k in range(5):
        f.path(f"M{cx-70+k*14},{cy+25-k*4} q8,-10 16,0 t16,0", stroke="#8b6fc0", sw=1.2)
    rer(f, cx - 120, cy + 70, w=100, rows=3)
    ser(f, cx - 160, cy - 60)
    golgi(f, cx + 90, cy - 55)
    mito(f, cx + 120, cy + 55, 70, 30, 15)
    mito(f, cx - 150, cy + 20, 58, 26, 80)
    mito(f, cx + 30, cy - 110, 54, 24, -10)
    f.circle(cx + 40, cy + 105, 13, fill="#f6d2d2", stroke=col("vermell"), sw=1.8)   # lisosoma
    f.circle(cx + 165, cy - 15, 9, fill="#fff2c2", stroke=col("groc"), sw=1.5)       # peroxisoma
    centriols(f, cx + 60, cy + 10)
    ribos(f, [(cx + 90, cy + 110), (cx + 10, cy + 80), (cx + 140, cy - 100), (cx - 80, cy - 110), (cx + 170, cy + 90)], r=2)
    items = [(cx - 30, cy - 63, "embolcall nuclear\n(doble membrana, porus)"), (cx - 40, cy - 15, "nuclèol"), (cx - 55, cy + 20, "cromatina"),
             (cx - 130, cy - 50, "reticle endoplasmàtic llis"), (cx - 100, cy + 75, "reticle endoplasmàtic rugós"), (cx - 150, cy + 20, "mitocondri"),
             (cx - 188, cy - 40, "membrana plasmàtica"),
             (cx + 90, cy - 55, "aparell de Golgi"), (cx + 165, cy - 15, "peroxisoma"), (cx + 70, cy + 10, "centríols (centrosoma)"),
             (cx + 120, cy + 55, "mitocondri"), (cx + 40, cy + 105, "lisosoma"), (cx + 170, cy + 90, "ribosomes lliures"), (cx + 30, cy - 110, "mitocondri")]
    items = [i for i in items if not (i[2] == "mitocondri" and i[0] == cx + 30)]
    two_sides(f, items, cx - 20, 175, 585, 30, 355, size=12.5)
    return f.svg()


def fig_vegetal():
    f = Fig(760, 360, "Cèl·lula vegetal")
    cx, cy = 380, 180
    W, H = 330, 270
    f.rect(cx - W / 2, cy - H / 2, W, H, fill="#e7f2da", stroke="#5c8a2e", sw=8, rx=14)
    f.rect(cx - W / 2 + 7, cy - H / 2 + 7, W - 14, H - 14, fill=CYTO, stroke=MEMB, sw=2, rx=10)
    for y in (cy - 70, cy + 50):     # plasmodesmes
        f.line(cx - W / 2 - 6, y, cx - W / 2 + 8, y, stroke="#3d5f1d", sw=2.4)
    f.rect(cx - 40, cy - 90, 175, 170, fill="#dcecf8", stroke=col("blau"), sw=2, rx=40)
    f.circle(cx - 100, cy - 60, 38, fill="#e9e2f5", stroke=col("lila"), sw=2.4)
    f.circle(cx - 106, cy - 66, 11, fill="#a58bd0", stroke="none")
    chloro(f, cx - 110, cy + 55, 60, 30, -20)
    chloro(f, cx + 40, cy + 108, 60, 28, 5)
    chloro(f, cx + 120, cy - 108, 56, 26, 0)
    mito(f, cx - 40, cy + 108, 44, 20, 0)
    golgi(f, cx - 120, cy + 5, s=0.7)
    rer(f, cx - 150, cy - 112, w=70, rows=2, s=0.8)
    items = [(cx - W / 2 - 4, cy - 70, "plasmodesme"), (cx - 100, cy - 60, "nucli"), (cx - 115, cy - 112, "reticle endoplasmàtic"),
             (cx - 120, cy + 5, "aparell de Golgi"), (cx - 110, cy + 55, "cloroplast"), (cx - 40, cy + 108, "mitocondri"),
             (cx + 160, cy + 100, "paret de cel·lulosa"), (cx + 150, cy + 20, "membrana plasmàtica"), (cx + 70, cy - 20, "vacúol (tonoplast)"),
             (cx + 120, cy - 108, "cloroplast")]
    # paret i membrana a la dreta: punts a les vores
    items[6] = (cx + W / 2 + 1, cy + 100, "paret de cel·lulosa")
    items[7] = (cx + W / 2 - 7, cy + 20, "membrana plasmàtica")
    two_sides(f, items, cx - 20, 195, 565, 30, 330)
    f.text(cx, 352, "Sense centríols ni lisosomes típics. Fora de la paret hi ha la cèl·lula veïna.", size=11, fill=MUTED)
    return f.svg()


def fig_mitocondri():
    f = Fig(760, 290, "El mitocondri")
    cx, cy, w, h = 260, 145, 400, 190
    f.ellipse(cx, cy, w / 2, h / 2, fill="#fbe3cf", stroke="#c4651a", sw=3)
    a, b = w / 2 - 12, h / 2 - 12
    f.ellipse(cx, cy, a, b, fill="#fff3e6", stroke="#c4651a", sw=2.2)
    xs = [cx - a * 0.75 + i * (1.5 * a) / 7 for i in range(8)]
    for i, x in enumerate(xs):
        top = i % 2 == 0
        yy = b * math.sqrt(1 - ((x - cx) / a) ** 2)
        y0 = cy - yy if top else cy + yy
        y1 = y0 + yy * 1.3 if top else y0 - yy * 1.3
        f.path(f"M{x-6:.1f},{y0+(1 if top else -1):.1f} L{x-6:.1f},{y1:.1f} Q{x:.1f},{y1 + (9 if top else -9):.1f} {x+6:.1f},{y1:.1f} L{x+6:.1f},{y0+(1 if top else -1):.1f}", fill="#fbe3cf", stroke="#c4651a", sw=2)
    f.path(f"M{cx-30},{cy+8} c12,-22 30,20 44,0 c10,-14 22,-8 18,8 c-5,18 -36,22 -62,-8", stroke=col("lila"), sw=2)
    ribos(f, [(cx + 100, cy - 20), (cx + 120, cy + 35), (cx - 110, cy - 15), (cx - 95, cy + 40), (cx + 40, cy + 55), (cx - 30, cy - 50)])
    labels(f, [(cx - w / 2 * 0.6, cy - h / 2 * 0.8, "membrana externa"), (xs[1] + 6, cy + 30, "membrana interna: crestes\n(cadena respiratòria i ATP-sintasa)"),
               (cx - a * 0.98, cy, "espai intermembranós (H⁺)"), (cx + 20, cy + 10, "DNA circular propi"),
               (cx + 95, cy + 55, "matriu: Krebs, β-oxidació,\ndescarboxilació del piruvat"), (cx + 120, cy + 35, "ribosomes 70S")], 500, 25, 270)
    return f.svg()


def fig_cloroplast():
    f = Fig(760, 300, "El cloroplast")
    cx, cy, w, h = 260, 150, 410, 210
    f.ellipse(cx, cy, w / 2, h / 2, fill="#d9efc9", stroke="#2e7d4f", sw=3)
    f.ellipse(cx, cy, w / 2 - 10, h / 2 - 10, fill="#eef8e8", stroke="#2e7d4f", sw=2)
    gr = [(140, 125), (225, 105), (310, 130), (185, 195), (275, 200), (355, 185)]
    for gx, gy in gr:
        for j in range(5):
            f.rect(gx - 22, gy - 14 + j * 7, 44, 6, fill="#5aa36f", stroke="#2e7d4f", sw=0.8, rx=3)
    for (a, b) in ((0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (2, 5)):
        f.line(gr[a][0] + 22 * (1 if gr[b][0] > gr[a][0] else 0), gr[a][1], gr[b][0] - 22 * (1 if gr[b][0] > gr[a][0] else 0), gr[b][1], stroke="#2e7d4f", sw=3)
    f.path(f"M{cx-80},{cy+70} c10,-10 20,10 30,0", stroke=col("lila"), sw=2)
    ribos(f, [(cx - 130, cy + 40), (cx + 130, cy - 70), (cx + 160, cy + 20), (cx - 60, cy - 75), (cx - 60, cy + 75)])
    f.ellipse(cx + 20, cy + 15, 18, 10, fill="#fff", stroke=MUTED, sw=1)
    labels(f, [(cx - 150, cy - 75, "embolcall: doble membrana"), (247, 112, "tilacoide: fase lluminosa\n(fotosistemes, ATP-sintasa)"),
               (310, 140, "granum: pila de tilacoides"), (cx + 160, cy - 20, "estroma: cicle de Calvin"),
               (cx - 65, cy + 70, "DNA circular i ribosomes 70S"), (cx + 20, cy + 15, "grànul de midó")], 510, 30, 280)
    return f.svg()


def fig_nucli():
    f = Fig(720, 320, "El nucli")
    cx, cy = 230, 160
    # reticle rugós continu amb la membrana externa
    f.path(f"M{cx+128},{cy-30} q45,-18 60,15 q-35,12 -15,38 q35,0 32,45", stroke="#2f6fb5", sw=4)
    ribos(f, [(cx + 150, cy - 44), (cx + 170, cy - 38), (cx + 185, cy - 18), (cx + 173, cy + 25), (cx + 200, cy + 55)])
    f.circle(cx, cy, 128, fill="#f3eefa", stroke=col("lila"), sw=3)
    f.circle(cx, cy, 120, fill="#f8f5fc", stroke=col("lila"), sw=2)
    for a in range(0, 360, 40):
        r = math.radians(a)
        f.circle(cx + 124 * math.cos(r), cy + 124 * math.sin(r), 6, fill="#fff", stroke=col("lila"), sw=1.5)
    f.circle(cx + 20, cy - 10, 32, fill="#a58bd0", stroke="none")
    for k in range(9):
        f.path(f"M{cx-80+k*14},{cy+60-k*6} q15,-20 30,0 t30,0", stroke="#8b6fc0", sw=1.4)
    labels(f, [(cx - 90, cy - 85, "embolcall: doble membrana"), (cx + 124 * math.cos(math.radians(320)), cy + 124 * math.sin(math.radians(320)), "porus nuclear"),
               (cx + 20, cy - 10, "nuclèol (RNAr i subunitats\ndels ribosomes)"), (cx + 190, cy + 20, "reticle rugós, continu\namb la membrana externa"),
               (cx - 40, cy + 40, "cromatina (DNA + histones)")], 440, 30, 300)
    return f.svg()


# ------------------------------------------------------------ membrana
def fig_bomba():
    f = Fig(640, 320, "Bomba de sodi i potassi")
    y1, y2 = 120, 200
    f.rect(0, y1, 640, y2 - y1, fill="#f5e7d0", stroke="none", rx=0)
    f.line(0, y1, 640, y1, stroke=MEMB, sw=2); f.line(0, y2, 640, y2, stroke=MEMB, sw=2)
    f.text(16, 34, "Exterior: Na⁺ alt, K⁺ baix", size=14, weight=700, anchor="start", fill=col("blau"))
    f.text(16, 302, "Citoplasma: K⁺ alt, Na⁺ baix", size=14, weight=700, anchor="start", fill=col("taronja"))
    px = 300
    f.rect(px - 72, y1 - 28, 144, y2 - y1 + 56, fill="#e3d7f3", stroke=col("lila"), sw=2.2, rx=24)
    f.text(px, (y1 + y2) / 2, "Na⁺/K⁺-\nATPasa", size=14, weight=700)

    def ion(x, y, t, c):
        f.circle(x, y, 12, fill=light(c), stroke=col(c), sw=1.5)
        f.text(x, y, t, size=9.5, weight=700)
    # Na+: de dins cap a fora, per l'esquerra de la proteïna
    for k in range(3):
        ion(165 + k * 28, 245, "Na⁺", "groc")
        ion(165 + k * 28, 72, "Na⁺", "groc")
    f.arrowpath(f"M{px-56},{y2+40} L{px-56},{y1-40}", color="#a67c12", sw=3)
    f.text(140, 72, "3 Na⁺ surten", size=13, weight=700, anchor="end", fill="#a67c12")
    # K+: de fora cap a dins, per la dreta
    for k in range(2):
        ion(400 + k * 28, 72, "K⁺", "blau")
        ion(400 + k * 28, 245, "K⁺", "blau")
    f.arrowpath(f"M{px+56},{y1-40} L{px+56},{y2+40}", color=col("blau"), sw=3)
    f.text(462, 245, "2 K⁺ entren", size=13, weight=700, anchor="start", fill=col("blau"))
    f.box(470, 280, 70, 28, "ATP", color="vermell", size=13)
    f.arrow(470, 288, px + 74, 224, color=col("vermell"))
    f.text(548, 294, "→ ADP + P_{i}", size=12, fill=col("vermell"), anchor="start")
    return f.svg()


def fig_osmosi():
    f = Fig(640, 500, "Osmosi en una cèl·lula animal i en una cèl·lula vegetal")
    heads = [("Medi hipertònic", "l’aigua surt"), ("Medi isotònic", "entra i surt igual"), ("Medi hipotònic", "l’aigua entra")]
    for i, (t, s) in enumerate(heads):
        x = 130 + i * 200
        f.text(x, 22, t, size=15, weight=700, fill=col("teal"))
        f.text(x, 42, s, size=12, fill=MUTED)
    W = col("blau")
    y = 130
    f.text(8, y - 64, "Cèl·lula animal (eritròcit)", size=12, anchor="start", fill=MUTED, weight=700)
    pts = []
    for k in range(40):
        a = 2 * math.pi * k / 40
        r = 34 + (7 if k % 4 == 0 else 0)
        pts.append((130 + r * math.cos(a), y + r * math.sin(a)))
    f.poly(pts, fill="#f2a59e", stroke="#b03a2e", sw=2)
    f.ellipse(330, y, 50, 44, fill="#f2a59e", stroke="#b03a2e", sw=2)
    f.ellipse(330, y, 22, 17, fill="#f7c4bf", stroke="none")
    f.circle(530, y, 58, fill="#f7c4bf", stroke="#b03a2e", sw=2, dash="6 4")
    f.arrow(160, y - 26, 192, y - 52, color=W); f.arrow(160, y + 26, 192, y + 52, color=W)
    f.arrow(268, y - 6, 282, y - 6, color=W); f.arrow(282, y + 6, 268, y + 6, color=W)
    f.arrow(378, y - 6, 392, y - 6, color=W); f.arrow(392, y + 6, 378, y + 6, color=W)
    f.arrow(452, y - 50, 480, y - 34, color=W); f.arrow(452, y + 50, 480, y + 34, color=W)
    f.text(130, y + 75, "es crena", size=13, weight=700)
    f.text(330, y + 75, "forma normal", size=13, weight=700)
    f.text(530, y + 80, "s’infla i pot lisar-se", size=13, weight=700)
    y = 360
    f.text(8, y - 108, "Cèl·lula vegetal", size=12, anchor="start", fill=MUTED, weight=700)
    for i, cx in enumerate((130, 330, 530)):
        f.rect(cx - 62, y - 70, 124, 140, fill="#eef7e6", stroke="#4f7a2b", sw=5, rx=8)
        if i == 0:
            f.rect(cx - 32, y - 36, 64, 72, fill="#d9efc9", stroke=col("verd"), sw=1.8, rx=22)
            f.rect(cx - 16, y - 20, 32, 40, fill="#cfe4f7", stroke=W, sw=1.2, rx=12)
        else:
            m = 6 if i == 2 else 12
            f.rect(cx - 62 + m, y - 70 + m, 124 - 2 * m, 140 - 2 * m, fill="#d9efc9", stroke=col("verd"), sw=1.8, rx=6)
            v = 20 if i == 2 else 34
            f.rect(cx - 62 + v, y - 70 + v, 124 - 2 * v, 140 - 2 * v, fill="#cfe4f7", stroke=W, sw=1.2, rx=10)
    f.arrow(165, y, 196, y, color=W)
    f.arrow(258, y - 6, 278, y - 6, color=W); f.arrow(278, y + 6, 258, y + 6, color=W)
    f.arrow(442, y, 466, y, color=W); f.arrow(618, y, 594, y, color=W)
    f.text(130, y + 90, "plasmòlisi", size=13, weight=700)
    f.text(330, y + 90, "flàccida", size=13, weight=700)
    f.text(530, y + 90, "turgent", size=13, weight=700)
    leader(f, 100, y - 20, 70, y - 88, "membrana", "start", 12)
    leader(f, 190, y - 50, 215, y - 88, "paret", "start", 12)
    leader(f, 545, y + 10, 575, y - 88, "vacúol", "start", 12)
    f.text(320, 490, "Les fletxes blaves indiquen el moviment de l’aigua; al medi isotònic, el flux net és zero.", size=12, fill=MUTED)
    return f.svg()


# ------------------------------------------------------------ cromosomes
def chrom(f, x, y, color, sister=True, h=34, ang=0, w=7, tip=None, tipside=1):
    """Cromosoma: dues cromàtides o una. tip: color d'un tros final d'una cromàtide (recombinant)."""
    f.raw(f'<g transform="rotate({ang} {x} {y})">')
    xs = [x - w - 1, x + 1] if sister else [x - w / 2]
    for k, xx in enumerate(xs):
        f.rect(xx, y - h / 2, w, h, fill=color, stroke="none", rx=w / 2)
        if tip and k == (1 if tipside > 0 else 0) and sister:
            f.rect(xx, y + h / 2 - h * 0.32, w, h * 0.32, fill=tip, stroke="none", rx=w / 2)
        if tip and not sister:
            f.rect(xx, y + h / 2 - h * 0.32, w, h * 0.32, fill=tip, stroke="none", rx=w / 2)
    f.circle(x, y, 3.4 if sister else 3, fill=INK, stroke="none")
    f.raw("</g>")


def cellcirc(f, cx, cy, r=62, spindle=False, nucleus=False):
    f.circle(cx, cy, r, fill="#f6f1e6", stroke=MEMB, sw=2)
    if nucleus:
        f.circle(cx, cy, r * 0.66, fill="none", stroke=col("lila"), sw=1.8, dash="5 3")
    if spindle:
        for k in (-0.5, -0.25, 0, 0.25, 0.5):
            f.path(f"M{cx},{cy-r+9} Q{cx + k*r*1.6},{cy} {cx},{cy+r-9}", stroke="#e0b44a", sw=1.1)
        for py in (cy - r + 9, cy + r - 9):
            f.circle(cx, py, 5, fill="#e0b44a", stroke="none")


L, S = 34, 20   # longitud dels cromosomes llargs i curts


def fig_mitosi():
    f = Fig(660, 270, "Fases de la mitosi (2n = 4)")
    names = [("Profase", "els cromosomes es\ncondensen (2 cromàtides)"), ("Metafase", "a la placa\nequatorial"),
             ("Anafase", "se separen les\ncromàtides germanes"), ("Telofase i\ncitocinesi", "dues cèl·lules 2n\nidèntiques")]
    cy = 125
    for i, (n, s) in enumerate(names):
        cx = 85 + i * 163
        f.text(cx, 24, n, size=14, weight=700, fill=col("teal"))
        f.text(cx, 228, s, size=11.5, fill=MUTED)
        if i == 0:
            cellcirc(f, cx, cy, nucleus=True)
            chrom(f, cx - 14, cy - 8, RED, h=L, ang=20); chrom(f, cx + 14, cy - 10, BLU, h=L, ang=-25)
            chrom(f, cx - 10, cy + 20, BLU, h=S, ang=70); chrom(f, cx + 16, cy + 18, RED, h=S, ang=-10)
        elif i == 1:
            cellcirc(f, cx, cy, spindle=True)
            f.line(cx - 55, cy, cx + 55, cy, stroke=LINE, dash="3 3", sw=1)
            for xx, (c, h) in zip((-36, -12, 10, 36), [(RED, L), (BLU, S), (BLU, L), (RED, S)]):
                chrom(f, cx + xx, cy, c, h=h * 0.62, ang=90, w=6)
        elif i == 2:
            cellcirc(f, cx, cy, spindle=True)
            for k, (c, h) in enumerate([(RED, L), (BLU, S), (BLU, L), (RED, S)]):
                xx = cx - 30 + k * 20
                chrom(f, xx, cy - 32, c, sister=False, h=h * 0.75)
                chrom(f, xx, cy + 32, c, sister=False, h=h * 0.75)
        else:
            for yy in (cy - 32, cy + 32):
                f.ellipse(cx, yy, 62, 30, fill="#f6f1e6", stroke=MEMB, sw=2)
                f.ellipse(cx, yy, 34, 18, stroke=col("lila"), sw=1.5, dash="4 3")
                for k, (c, h) in enumerate([(RED, L), (BLU, S), (BLU, L), (RED, S)]):
                    chrom(f, cx - 18 + k * 12, yy, c, sister=False, h=h * 0.6, w=5)
        if i < 3:
            f.arrow(cx + 68, cy, cx + 94, cy, color=MUTED)
    return f.svg()


def fig_meiosi():
    f = Fig(660, 520, "Fases de la meiosi (2n = 4)")
    f.text(10, 20, "Meiosi I (reduccional): se separen els cromosomes homòlegs", size=14, weight=700, anchor="start", fill=col("vermell"))
    f.text(10, 268, "Meiosi II (equacional): se separen les cromàtides germanes", size=14, weight=700, anchor="start", fill=col("blau"))
    labs1 = [("Profase I", "aparellament (bivalents)\ni entrecreuament"), ("Metafase I", "bivalents a la\nplaca equatorial"),
             ("Anafase I", "cada homòleg cap\na un pol"), ("Telofase I", "2 cèl·lules n,\ncromosomes de 2 cromàtides")]
    labs2 = [("Profase II", "sense replicació\nprèvia"), ("Metafase II", "cromosomes a la\nplaca equatorial"),
             ("Anafase II", "cromàtides cap\na pols oposats"), ("Telofase II", "4 cèl·lules n\ngenèticament diferents")]
    cy = 130
    for i, (n, s) in enumerate(labs1):
        cx = 85 + i * 163
        f.text(cx, 48, n, size=13, weight=700)
        f.text(cx, 226, s, size=11, fill=MUTED)
        if i == 0:
            cellcirc(f, cx, cy, nucleus=True)
            chrom(f, cx - 12, cy - 8, RED, h=L, ang=-12); chrom(f, cx + 6, cy - 6, BLU, h=L, ang=-12)
            chrom(f, cx - 8, cy + 26, BLU, h=S, ang=80); chrom(f, cx - 6, cy + 40, RED, h=S, ang=80)
            f.circle(cx - 3, cy - 2, 9, stroke="#a67c12", sw=1.8, dash="2 2")
        elif i == 1:
            cellcirc(f, cx, cy, spindle=True)
            f.line(cx - 56, cy, cx + 56, cy, stroke=LINE, dash="3 3", sw=1)
            chrom(f, cx - 18, cy - L / 2 - 3, RED, h=L, tip=BLU); chrom(f, cx - 18, cy + L / 2 + 3, BLU, h=L, tip=RED, tipside=-1)
            chrom(f, cx + 20, cy - S / 2 - 3, BLU, h=S); chrom(f, cx + 20, cy + S / 2 + 3, RED, h=S)
        elif i == 2:
            cellcirc(f, cx, cy, spindle=True)
            chrom(f, cx - 18, cy - 30, RED, h=L, tip=BLU); chrom(f, cx - 18, cy + 30, BLU, h=L, tip=RED, tipside=-1)
            chrom(f, cx + 20, cy - 32, BLU, h=S); chrom(f, cx + 20, cy + 32, RED, h=S)
        else:
            for yy, (a, b, ta, tb) in ((cy - 38, (RED, BLU, BLU, 1)), (cy + 38, (BLU, RED, RED, -1))):
                f.ellipse(cx, yy, 60, 33, fill="#f6f1e6", stroke=MEMB, sw=2)
                chrom(f, cx - 14, yy, a, h=L * 0.85, tip=ta, tipside=tb); chrom(f, cx + 16, yy, b, h=S)
        if i < 3:
            f.arrow(cx + 68, cy, cx + 94, cy, color=MUTED)
    f.text(330, 252, "↓ cadascuna de les dues cèl·lules fa la meiosi II", size=12, fill=MUTED)
    cy = 375
    # es mostra la cèl·lula de dalt de la telofase I
    for i, (n, s) in enumerate(labs2):
        cx = 85 + i * 163
        f.text(cx, 295, n, size=13, weight=700)
        f.text(cx, 474, s, size=11, fill=MUTED)
        if i == 3:
            f.text(cx, 500, "(+ 2 de l’altra cèl·lula)", size=10.5, fill=MUTED)
        r = 50
        if i == 0:
            f.circle(cx, cy, r, fill="#f6f1e6", stroke=MEMB, sw=2)
            chrom(f, cx - 12, cy - 4, RED, h=L, tip=BLU, ang=25); chrom(f, cx + 16, cy + 6, BLU, h=S, ang=-20)
        elif i == 1:
            cellcirc(f, cx, cy, r=r, spindle=True)
            chrom(f, cx - 14, cy, RED, h=L, tip=BLU, ang=90); chrom(f, cx + 16, cy, BLU, h=S, ang=90)
        elif i == 2:
            cellcirc(f, cx, cy, r=r, spindle=True)
            chrom(f, cx - 12, cy - 26, RED, sister=False, h=L * 0.6)
            chrom(f, cx - 12, cy + 26, RED, sister=False, h=L * 0.6, tip=BLU)
            chrom(f, cx + 12, cy - 26, BLU, sister=False, h=S * 0.7); chrom(f, cx + 12, cy + 26, BLU, sister=False, h=S * 0.7)
        else:
            for yy, tipc in ((cy - 28, None), (cy + 28, BLU)):
                f.ellipse(cx, yy, 44, 24, fill="#f6f1e6", stroke=MEMB, sw=2)
                chrom(f, cx - 9, yy, RED, sister=False, h=L * 0.55, tip=tipc); chrom(f, cx + 10, yy, BLU, sister=False, h=S * 0.6)
        if i < 3:
            f.arrow(cx + 58, cy, cx + 100, cy, color=MUTED)
    f.text(330, 512, "Vermell: cromosomes d’origen matern · blau: patern · el tros de l’altre color és el resultat de l’entrecreuament.", size=10.5, fill=MUTED)
    return f.svg()


# ------------------------------------------------------------ virus
def fig_fag():
    f = Fig(640, 340, "Bacteriòfag T4")
    cx = 250
    # cap icosaèdric (vista: hexàgon allargat)
    pts = [(cx, 20), (cx + 48, 48), (cx + 48, 118), (cx, 146), (cx - 48, 118), (cx - 48, 48)]
    f.poly(pts, fill=light("blau"), stroke=col("blau"), sw=3)
    f.line(cx - 48, 48, cx + 48, 118, stroke=col("blau"), sw=1, ); f.line(cx + 48, 48, cx - 48, 118, stroke=col("blau"), sw=1)
    f.path(f"M{cx-25},{70} c12,-15 25,15 38,0 s15,20 -5,30 s-30,-5 -20,15 s30,5 32,-5", stroke=col("vermell"), sw=2)
    f.rect(cx - 14, 146, 28, 12, fill="#c9d6ea", stroke=col("blau"), sw=1.5, rx=2)          # coll
    f.rect(cx - 12, 158, 24, 96, fill="#dfe8f5", stroke=col("blau"), sw=2, rx=3)            # beina
    for y in range(164, 252, 8):
        f.line(cx - 12, y, cx + 12, y, stroke=col("blau"), sw=1)
    f.poly([(cx - 34, 254), (cx + 34, 254), (cx + 26, 268), (cx - 26, 268)], fill="#c9d6ea", stroke=col("blau"), sw=2)   # placa basal
    for s in (-1, 1):
        for k, (dx, dy) in enumerate(((60, 30), (90, 50))):
            f.path(f"M{cx + s*26},{262} L{cx + s*(26+dx*0.55)},{262 - 18 + k*6} L{cx + s*(26+dx)},{262 + dy}", stroke=col("blau"), sw=2)
    labels(f, [(cx + 30, 40, "càpsida (cap): proteïnes"), (cx + 10, 90, "DNA de doble cadena"), (cx + 12, 152, "coll"),
               (cx + 12, 200, "beina contràctil de la cua"), (cx + 30, 262, "placa basal"), (cx + 115, 312, "fibres de la cua\n(s’uneixen al bacteri)")], 420, 30, 320)
    f.text(cx, 330, "≈ 200 nm", size=12, fill=MUTED)
    return f.svg()


def fig_cicles_virus():
    f = Fig(640, 360, "Cicle lític i cicle lisogènic d'un bacteriòfag")

    def bact(x, y, w=110, h=54):
        f.rect(x - w / 2, y - h / 2, w, h, fill=light("blau"), stroke=col("blau"), sw=2, rx=h / 2)
        f.path(f"M{x - w*0.25},{y} c{w*0.08},-10 {w*0.16},10 {w*0.25},0 s{w*0.16},10 {w*0.25},-2", stroke="#7a8aa8", sw=1.6)

    def phage(x, y, s=0.5, ang=0):
        f.raw(f'<g transform="rotate({ang} {x} {y})">')
        f.poly([(x, y - 20 * s), (x + 12 * s, y - 13 * s), (x + 12 * s, y + 3 * s), (x, y + 10 * s), (x - 12 * s, y + 3 * s), (x - 12 * s, y - 13 * s)], fill="#fff", stroke=col("vermell"), sw=1.4)
        f.line(x, y + 10 * s, x, y + 34 * s, stroke=col("vermell"), sw=2)
        f.path(f"M{x-10*s},{y+40*s} L{x},{y+34*s} L{x+10*s},{y+40*s}", stroke=col("vermell"), sw=1.4)
        f.raw("</g>")
    f.text(400, 30, "1. El fag s’uneix al bacteri\ni hi injecta el DNA", size=13, weight=700, anchor="start")
    bact(320, 72)
    phage(320, 26, 0.7)
    f.path("M318,68 c6,-6 12,6 20,0", stroke=col("vermell"), sw=2.4)
    f.arrow(260, 100, 170, 140, color=MUTED); f.arrow(380, 100, 470, 140, color=MUTED)
    f.text(150, 128, "Cicle lític", size=15, weight=700, fill=col("vermell"), anchor="end")
    f.text(490, 128, "Cicle lisogènic", size=15, weight=700, fill=col("verd"), anchor="start")
    bact(130, 185)
    for dx in (-30, -10, 10, 30):
        phage(130 + dx, 182, 0.45)
    f.text(130, 228, "2. es replica el DNA víric i\nes fabriquen càpsides noves", size=11, fill=MUTED)
    f.arrow(130, 250, 130, 272, color=MUTED)
    # lisi: bacteri trencat
    f.path("M80,300 q20,-22 40,-6 M140,294 q20,-16 40,6 M80,300 q15,24 40,12 M142,312 q18,10 38,-12", stroke=col("blau"), sw=2)
    for (dx, dy, a) in ((-45, -8, -30), (0, -20, 0), (45, -8, 30), (-30, 30, -150), (30, 30, 150)):
        phage(130 + dx, 300 + dy, 0.4, a)
    f.text(130, 345, "3. lisi: surten molts virus", size=11, fill=MUTED)
    bact(510, 185, w=130)
    f.rect(495, 179, 30, 12, fill=col("vermell"), stroke="none", rx=2)
    f.text(510, 228, "2. el DNA víric s’integra al\ncromosoma bacterià (pròfag)", size=11, fill=MUTED)
    f.arrow(510, 250, 510, 272, color=MUTED)
    bact(460, 300, w=84, h=40); bact(560, 300, w=84, h=40)
    f.rect(450, 296, 20, 8, fill=col("vermell"), stroke="none", rx=2); f.rect(550, 296, 20, 8, fill=col("vermell"), stroke="none", rx=2)
    f.text(510, 345, "3. el pròfag es copia amb el bacteri", size=11, fill=MUTED)
    f.arrowpath("M440,196 C360,200 260,180 196,184", color=col("taronja"), sw=2, dash="6 4")
    f.text(318, 172, "inducció (p. ex. dany al DNA)", size=12, weight=700, fill=col("taronja"))
    return f.svg()


# ------------------------------------------------------------ evolució
def limb(f, x, y, kind):
    """Extremitat anterior esquemàtica: húmer (taronja), radi i cúbit (blau), carp (verd), metacarps i falanges (lila)."""
    H, R, C, M = "#e08a3c", "#3b74c4", "#2e9d5a", "#7d5bb5"

    def bone(x1, y1, x2, y2, w, c):
        f.line(x1, y1, x2, y2, stroke=c, sw=w)
    if kind == "huma":
        bone(x, y, x, y + 90, 11, H)
        bone(x - 5, y + 98, x - 9, y + 175, 6, R); bone(x + 5, y + 98, x + 9, y + 175, 6, R)
        for k in range(3):
            f.circle(x - 8 + k * 8, y + 185, 4.5, fill=C, stroke="none")
        for k, a in enumerate((-30, -12, 0, 12, 26)):
            r = math.radians(a + 90)
            ln = 50 if k else 38
            bone(x - 12 + k * 6, y + 194, x - 12 + k * 6 + ln * math.cos(r) * 0.6, y + 194 + ln * math.sin(r), 3.4, M)
    elif kind == "ratpenat":
        tips = [(x + 20, y + 260), (x + 80, y + 285), (x + 140, y + 262), (x + 170, y + 205)]
        f.poly([(x + 4, y + 10), (x - 10, y + 200)] + tips + [(x + 110, y + 120)], fill="#efe9f7", stroke="#d6cce6", sw=1)
        bone(x, y, x + 30, y + 70, 11, H)
        bone(x + 34, y + 78, x + 70, y + 150, 6, R)
        f.circle(x + 74, y + 158, 5, fill=C, stroke="none")
        for tx, ty in tips:
            bone(x + 74, y + 158, tx, ty, 3, M)
        bone(x + 74, y + 158, x + 92, y + 150, 3, M)
    elif kind == "balena":
        f.path(f"M{x-22},{y} C{x-40},{y+120} {x-25},{y+230} {x+5},{y+250} C{x+30},{y+220} {x+35},{y+110} {x+22},{y} z", fill="#e6eef6", stroke="#9fb3c8", sw=1.5)
        bone(x, y + 5, x, y + 50, 13, H)
        bone(x - 6, y + 56, x - 7, y + 95, 8, R); bone(x + 6, y + 56, x + 7, y + 95, 8, R)
        for k in range(4):
            f.circle(x - 9 + k * 6, y + 104, 4, fill=C, stroke="none")
        for k in range(4):
            xx = x - 12 + k * 8
            for j in range(5 if k in (1, 2) else 3):
                f.line(xx, y + 114 + j * 22, xx, y + 130 + j * 22, stroke=M, sw=4)
    elif kind == "ocell":
        # contorn de l'ala (plomes) per sota dels ossos
        f.path(f"M{x-6},{y+4} C{x+60},{y+60} {x+120},{y+170} {x+110},{y+270} C{x+70},{y+240} {x+20},{y+170} {x-14},{y+40} z", fill="#f1edf7", stroke="#c9c2d9", sw=1.2)
        bone(x, y, x + 25, y + 70, 10, H)
        bone(x + 28, y + 78, x + 55, y + 150, 5, R); bone(x + 36, y + 76, x + 62, y + 146, 5, R)
        f.circle(x + 62, y + 158, 5, fill=C, stroke="none")
        bone(x + 62, y + 162, x + 82, y + 235, 5, M); bone(x + 66, y + 162, x + 92, y + 212, 3, M); bone(x + 58, y + 162, x + 60, y + 190, 3, M)


def fig_homologia():
    f = Fig(700, 360, "Òrgans homòlegs: extremitat anterior de vertebrats")
    for x, k, t, fn in ((80, "huma", "Humà", "agafar"), (230, "ratpenat", "Ratpenat", "volar"), (450, "balena", "Balena", "nedar"), (570, "ocell", "Ocell", "volar")):
        limb(f, x, 50, k)
        f.text(x + (50 if k in ("ratpenat",) else 20 if k == "ocell" else 0), 22, t, size=14, weight=700)
        f.text(x + (50 if k in ("ratpenat",) else 20 if k == "ocell" else 0), 330, fn, size=12, fill=MUTED)
    lx = 20
    for k, (c, t) in enumerate((("#e08a3c", "húmer"), ("#3b74c4", "radi i cúbit"), ("#2e9d5a", "carp"), ("#7d5bb5", "metacarps i falanges"))):
        f.rect(lx + k * 160, 344, 14, 10, fill=c, stroke="none", rx=2)
        f.text(lx + 20 + k * 160, 349, t, size=11.5, anchor="start")
    return f.svg()


# ------------------------------------------------------------ immunologia
def fig_resposta():
    f = Fig(640, 330, "Resposta primària i resposta secundària")
    x0, y0, W, H = 70, 250, 540, 200
    f.line(x0, y0, x0 + W, y0, sw=1.8); f.line(x0, y0, x0, y0 - H, sw=1.8)
    f.text(x0 + W / 2, y0 + 62, "temps (dies)", size=13)
    f.text(x0 - 40, y0 - H / 2, "anticossos a la sang", size=13, rot=-90)

    def curve(t0, tp, A, k, color, tail=0.0, dash=None):
        pts = []
        for i in range(0, 201):
            t = i / 200 * 100
            if t < t0:
                v = 0
            else:
                u = (t - t0) / tp
                v = A * (u ** k) * math.exp(k * (1 - u))
                if tail and u > 1:
                    v = A * (tail * math.exp(-(u - 1) * 0.03) + (1 - tail) * math.exp(-1.2 * (u - 1) ** 2))
            pts.append((x0 + t / 100 * W, y0 - v))
        f.path("M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts), stroke=color, sw=3, dash=dash)
    # 1r contacte (t=5): IgM primer, poca IgG; 2n contacte (t=55): molta IgG, ràpida i duradora
    curve(5, 9, 40, 3, col("taronja"))
    curve(9, 11, 22, 3, col("lila"), dash="6 4")
    curve(55, 4, 45, 3, col("taronja"))
    curve(55, 6, 175, 2.5, col("lila"), tail=0.35, dash="6 4")
    for t, lab in ((5, "1r contacte"), (55, "2n contacte")):
        f.arrow(x0 + t / 100 * W, y0 + 22, x0 + t / 100 * W, y0 + 3, color=INK)
        f.text(x0 + t / 100 * W, y0 + 34, lab, size=12, weight=700)
    f.line(x0 + 420, 60, x0 + 450, 60, stroke=col("taronja"), sw=3); f.text(x0 + 456, 60, "IgM", size=13, anchor="start")
    f.line(x0 + 420, 85, x0 + 450, 85, stroke=col("lila"), sw=3, dash="6 4"); f.text(x0 + 456, 85, "IgG", size=13, anchor="start")
    f.text(x0 + 100, y0 - 80, "primària: lenta,\nbaixa, sobretot IgM", size=12, fill=MUTED)
    f.text(x0 + 205, y0 - 165, "secundària: ràpida, intensa,\nsobretot IgG (memòria)", size=12, fill=MUTED)
    return f.svg()
