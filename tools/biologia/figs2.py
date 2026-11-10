"""Figures del tema 2 (La cèl·lula)."""
import math
from svg import Fig, INK, MUTED, LINE, col, light

MEMB = "#d98c3a"
CYTO = "#fdf7ec"


def leader(f, x1, y1, x2, y2, label, anchor="start", size=13):
    f.line(x1, y1, x2, y2, stroke=MUTED, sw=1)
    f.circle(x1, y1, 2.2, fill=INK, stroke="none")
    dx = 6 if anchor == "start" else -6
    f.text(x2 + dx, y2, label, size=size, anchor=anchor)


def ribos(f, pts, r=2.6, color="#6b4c9a"):
    for x, y in pts:
        f.circle(x, y, r, fill=color, stroke="none")


def mito(f, cx, cy, w, h, rot=0):
    g = f"rotate({rot} {cx} {cy})"
    f.raw(f'<g transform="{g}">')
    f.ellipse(cx, cy, w / 2, h / 2, fill="#fbe3cf", stroke="#c4651a", sw=1.8)
    f.ellipse(cx, cy, w / 2 - 4, h / 2 - 4, fill="#fff3e6", stroke="#c4651a", sw=1.2)
    n = max(3, int(w / 14))
    for i in range(n):
        x = cx - w / 2 + 10 + i * (w - 20) / (n - 1)
        top = i % 2 == 0
        y0 = cy - h / 2 + 4 if top else cy + h / 2 - 4
        y1 = cy + (h * 0.12 if top else -h * 0.12)
        f.path(f"M{x-3},{y0} L{x-3},{y1} Q{x},{y1 + (4 if top else -4)} {x+3},{y1} L{x+3},{y0}", stroke="#c4651a", sw=1.2, fill="#fbe3cf")
    f.raw("</g>")


def chloro(f, cx, cy, w, h, rot=0):
    f.raw(f'<g transform="rotate({rot} {cx} {cy})">')
    f.ellipse(cx, cy, w / 2, h / 2, fill="#e3f2e8", stroke="#2e7d4f", sw=1.8)
    f.ellipse(cx, cy, w / 2 - 4, h / 2 - 4, fill="#eef8f1", stroke="#2e7d4f", sw=1)
    for k in range(-1, 2):
        x = cx + k * w * 0.27
        for j in range(4):
            f.rect(x - 7, cy - 10 + j * 5, 14, 4, fill="#4caf6e", stroke="#2e7d4f", sw=0.6, rx=2)
    f.line(cx - w * 0.27 + 7, cy, cx + w * 0.27 - 7, cy, stroke="#2e7d4f", sw=1)
    f.raw("</g>")


def fig_pro_euc():
    f = Fig(680, 330, "Cèl·lula procariota i cèl·lula eucariota")
    # procariota
    f.text(150, 22, "Procariota (bacteri)", size=16, weight=700, fill=col("teal"))
    f.text(150, 42, "1–5 µm", size=12, fill=MUTED)
    f.rect(40, 90, 220, 110, fill="#eef5fb", stroke=col("blau"), sw=5, rx=55)
    f.rect(40, 90, 220, 110, fill="none", stroke="#9cc1e6", sw=1.5, rx=55)
    f.path("M120,140 c20,-25 40,25 60,0 s30,20 10,25 s-50,-10 -70,-25", stroke=col("lila"), sw=2)
    f.circle(215, 125, 9, stroke=col("lila"), sw=1.6)
    ribos(f, [(70, 120), (85, 170), (100, 115), (150, 180), (205, 170), (230, 150), (75, 145), (190, 110)])
    f.path("M260,145 c20,-10 30,10 50,0 s30,10 40,0", stroke=INK, sw=2)
    leader(f, 150, 140, 120, 250, "nucleoide (DNA circular)", "middle")
    leader(f, 215, 125, 290, 70, "plasmidi")
    leader(f, 85, 170, 50, 240, "ribosomes 70S", "middle")
    leader(f, 46, 112, 20, 70, "paret i membrana", "start")
    leader(f, 320, 145, 300, 200, "flagel", "middle")
    f.text(150, 300, "sense nucli ni orgànuls membranosos", size=13, fill=MUTED)
    # eucariota
    X = 370
    f.text(X + 130, 22, "Eucariota (cèl·lula animal)", size=16, weight=700, fill=col("teal"))
    f.text(X + 130, 42, "10–30 µm", size=12, fill=MUTED)
    f.ellipse(X + 130, 170, 120, 105, fill=CYTO, stroke=MEMB, sw=2.5)
    f.circle(X + 120, 160, 40, fill="#e9e2f5", stroke=col("lila"), sw=2.5)
    f.circle(X + 112, 152, 12, fill="#b9a6dd", stroke="none")
    mito(f, X + 200, 120, 46, 22, 20)
    mito(f, X + 70, 230, 46, 22, -15)
    for k in range(4):
        f.path(f"M{X+170},{190+k*9} q20,-8 40,0", stroke="#2f6fb5", sw=2.5)
    ribos(f, [(X + 60, 140), (X + 200, 240), (X + 160, 250), (X + 50, 190)])
    leader(f, X + 120, 160, X + 130, 300, "nucli amb embolcall", "middle")
    leader(f, X + 200, 120, X + 250, 70, "mitocondri")
    leader(f, X + 190, 200, X + 250, 250, "Golgi")
    f.text(X + 130, 318, "compartiments: nucli, orgànuls, endomembranes", size=12, fill=MUTED)
    return f.svg()


def fig_mosaic():
    f = Fig(640, 340, "Model del mosaic fluid")
    top, bot = 120, 210
    f.text(320, 22, "Medi extracel·lular", size=14, weight=700, fill=col("blau"))
    f.text(320, 322, "Citoplasma", size=14, weight=700, fill=col("taronja"))
    xs = [40 + i * 18 for i in range(32)]
    skip = set()
    prot = [(150, 185), (330, 380), (470, 510)]
    for x in xs:
        if any(a - 6 < x < b + 6 for a, b in prot):
            continue
        for y, d in ((top, 1), (bot, -1)):
            f.line(x - 3, y + 8 * d, x - 3, y + 38 * d, stroke="#b48a52", sw=1.6)
            f.line(x + 3, y + 8 * d, x + 3, y + 38 * d, stroke="#b48a52", sw=1.6)
            f.circle(x, y, 7, fill="#7fb3e0", stroke="#2f6fb5", sw=1.2)
    # colesterol
    for x in (113, 257, 437):
        f.rect(x - 4, top + 10, 8, 26, fill=col("groc"), stroke="none", rx=3)
    # proteïnes integrals
    f.path(f"M150,{top-30} q-10,60 0,{bot-top+60} h35 q10,-60 0,{-(bot-top+60)} z", fill="#d7c7ee", stroke=col("lila"), sw=2)
    f.rect(330, top - 26, 50, bot - top + 52, fill="#d7c7ee", stroke=col("lila"), sw=2, rx=18)
    f.rect(350, top - 26, 10, bot - top + 52, fill="#fff", stroke=col("lila"), sw=1, rx=4)
    f.path(f"M470,{top-20} q-12,55 0,{bot-top+40} h40 q12,-55 0,{-(bot-top+40)} z", fill="#d7c7ee", stroke=col("lila"), sw=2)
    # perifèrica
    f.ellipse(560, bot + 22, 30, 14, fill="#f3d5e4", stroke=col("rosa"), sw=2)
    # glicocàlix
    for x, h in ((167, 60), (494, 55), (95, 45)):
        y0 = top - 30 if x != 95 else top - 7
        for k in range(4):
            yy = y0 - k * 11
            f.circle(x + (k % 2) * 6 - 3, yy, 4.5, fill="#9ad1a8", stroke=col("verd"), sw=1)
    # citoesquelet
    f.path(f"M440,{bot+48} q60,15 160,5", stroke=col("vermell"), sw=3)
    leader(f, 167, top - 50, 120, 60, "glicoproteïna (glicocàlix)", "middle")
    leader(f, 95, top - 30, 40, 85, "glicolípid", "start")
    leader(f, 113, top + 22, 60, 270, "colesterol", "middle")
    leader(f, 167, 165, 230, 275, "proteïna integral", "start")
    leader(f, 355, 165, 360, 275, "proteïna de canal", "middle")
    leader(f, 560, bot + 22, 590, 290, "perifèrica", "middle")
    leader(f, 600, bot + 52, 600, 315, "citoesquelet", "end")
    leader(f, 220, top, 280, 70, "cap polar", "start")
    leader(f, 240, top + 26, 270, 165, "cues hidròfobes", "start", 12)
    return f.svg()


def fig_bomba():
    f = Fig(640, 300, "Bomba de sodi i potassi")
    y1, y2 = 110, 190
    f.rect(0, y1, 640, y2 - y1, fill="#f5e7d0", stroke="none", rx=0)
    f.line(0, y1, 640, y1, stroke=MEMB, sw=2); f.line(0, y2, 640, y2, stroke=MEMB, sw=2)
    f.text(20, 40, "Exterior: Na⁺ alt, K⁺ baix", size=14, weight=700, anchor="start", fill=col("blau"))
    f.text(20, 265, "Citoplasma: K⁺ alt, Na⁺ baix", size=14, weight=700, anchor="start", fill=col("taronja"))
    f.rect(270, y1 - 30, 100, y2 - y1 + 60, fill="#d7c7ee", stroke=col("lila"), sw=2.2, rx=22)
    f.text(320, 150, "Na⁺/K⁺\nATPasa", size=14, weight=700)
    # Na fora
    for k in range(3):
        f.circle(250 - k * 26, 220, 11, fill="#fde3a7", stroke=col("groc"), sw=1.5); f.text(250 - k * 26, 220, "Na⁺", size=9, weight=700)
    f.arrowpath("M300,230 C300,80 300,80 300,70", color=col("groc"), sw=2.5)
    for k in range(3):
        f.circle(250 - k * 26, 70, 11, fill="#fde3a7", stroke=col("groc"), sw=1.5); f.text(250 - k * 26, 70, "Na⁺", size=9, weight=700)
    f.text(160, 70, "3 Na⁺ surten", size=13, weight=700, anchor="end", fill=col("groc"))
    for k in range(2):
        f.circle(400 + k * 26, 70, 11, fill="#cfe4f7", stroke=col("blau"), sw=1.5); f.text(400 + k * 26, 70, "K⁺", size=10, weight=700)
    f.arrowpath("M345,70 C345,200 345,220 345,232", color=col("blau"), sw=2.5)
    for k in range(2):
        f.circle(400 + k * 26, 232, 11, fill="#cfe4f7", stroke=col("blau"), sw=1.5); f.text(400 + k * 26, 232, "K⁺", size=10, weight=700)
    f.text(460, 232, "2 K⁺ entren", size=13, weight=700, anchor="start", fill=col("blau"))
    f.box(520, 200, 90, 30, "ATP", color="vermell", size=14)
    f.arrow(520, 215, 372, 200, color=col("vermell"))
    f.text(565, 252, "ADP + P_{i}", size=13, fill=col("vermell"))
    f.text(320, 290, "Transport actiu primari: tots dos ions van en contra del seu gradient.", size=13, fill=MUTED)
    return f.svg()


def fig_osmosi():
    f = Fig(640, 470, "Osmosi en una cèl·lula animal i en una cèl·lula vegetal")
    cols = [("Medi hipertònic", "l’aigua surt"), ("Medi isotònic", "sense flux net"), ("Medi hipotònic", "l’aigua entra")]
    for i, (t, s) in enumerate(cols):
        x = 110 + i * 210
        f.text(x, 22, t, size=15, weight=700, fill=col("teal"))
        f.text(x, 42, s, size=12, fill=MUTED)
    # fila animal: eritròcits
    y = 125
    f.text(8, y, "Animal\n(eritròcit)", size=12, anchor="start", fill=MUTED, weight=700)
    # crenat
    pts = []
    for k in range(36):
        a = 2 * math.pi * k / 36
        r = 36 + (6 if k % 3 == 0 else 0)
        pts.append((110 + r * math.cos(a), y + r * math.sin(a)))
    f.poly(pts, fill="#f2a59e", stroke="#b03a2e", sw=2)
    f.ellipse(320, y, 52, 46, fill="#f2a59e", stroke="#b03a2e", sw=2)
    f.ellipse(320, y, 24, 18, fill="#f7c4bf", stroke="none")
    f.circle(530, y, 60, fill="#f7c4bf", stroke="#b03a2e", sw=2, dash="6 4")
    for i, cx in enumerate((110, 320, 530)):
        pass
    f.arrow(140, y - 30, 185, y - 55, color=col("blau")); f.arrow(140, y + 30, 185, y + 55, color=col("blau"))
    f.arrow(250, y, 268, y, color=col("blau")); f.arrow(390, y, 372, y, color=col("blau"))
    f.arrow(458, y - 52, 482, y - 38, color=col("blau")); f.arrow(458, y + 52, 482, y + 38, color=col("blau"))
    f.text(110, y + 72, "crenada", size=13, weight=700)
    f.text(320, y + 72, "normal", size=13, weight=700)
    f.text(530, y + 80, "s’infla i pot lisar-se", size=13, weight=700)
    # fila vegetal
    y = 330
    f.text(8, y, "Vegetal", size=12, anchor="start", fill=MUTED, weight=700)
    for i, cx in enumerate((110, 320, 530)):
        f.rect(cx - 62, y - 70, 124, 140, fill="#eef7e6", stroke="#4f7a2b", sw=5, rx=8)
        if i == 0:
            f.rect(cx - 30, y - 35, 60, 72, fill="#d9efc9", stroke=col("verd"), sw=1.8, rx=22)
            f.rect(cx - 16, y - 20, 32, 40, fill="#cfe4f7", stroke=col("blau"), sw=1.2, rx=12)
        else:
            m = 6 if i == 2 else 10
            f.rect(cx - 62 + m, y - 70 + m, 124 - 2 * m, 140 - 2 * m, fill="#d9efc9", stroke=col("verd"), sw=1.8, rx=6)
            v = 22 if i == 2 else 32
            f.rect(cx - 62 + v, y - 70 + v, 124 - 2 * v, 140 - 2 * v, fill="#cfe4f7", stroke=col("blau"), sw=1.2, rx=10)
    f.arrow(110, y, 160, y, color=col("blau")); f.text(80, y + 0, "", size=10)
    f.arrow(320 - 70, y, 320 - 50, y, color=col("blau")); f.arrow(320 + 70, y, 320 + 50, y, color=col("blau"))
    f.arrow(530 - 90, y, 530 - 66, y, color=col("blau")); f.arrow(530 + 90, y, 530 + 66, y, color=col("blau"))
    f.text(110, y + 88, "plasmòlisi", size=13, weight=700)
    f.text(320, y + 88, "flàccida", size=13, weight=700)
    f.text(530, y + 88, "turgent", size=13, weight=700)
    leader(f, 110 - 30, y - 10, 30, y - 92, "membrana", "start", 12)
    leader(f, 110 + 60, y - 40, 190, y - 92, "paret", "start", 12)
    leader(f, 530, y, 600, y - 92, "vacúol", "end", 12)
    f.text(320, 458, "Les fletxes blaves indiquen el sentit net de l’aigua.", size=12, fill=MUTED)
    return f.svg()


def fig_nucli():
    f = Fig(720, 320, "El nucli")
    cx, cy = 230, 165
    f.circle(cx, cy, 128, fill="#f3eefa", stroke=col("lila"), sw=3)
    f.circle(cx, cy, 120, fill="#f8f5fc", stroke=col("lila"), sw=2)
    for a in range(0, 360, 40):
        r = math.radians(a)
        x, y = cx + 124 * math.cos(r), cy + 124 * math.sin(r)
        f.circle(x, y, 6, fill="#fff", stroke=col("lila"), sw=1.5)
    f.circle(cx + 20, cy - 10, 32, fill="#a58bd0", stroke="none")
    for k in range(9):
        a = k * 0.7
        f.path(f"M{cx-80+k*14},{cy+60-k*6} q15,-20 30,0 t30,0", stroke="#8b6fc0", sw=1.4)
    # RER continu
    f.path(f"M{cx+128},{cy-40} q50,-10 60,20 q-40,10 -20,40 q40,0 40,40", stroke="#2f6fb5", sw=3)
    ribos(f, [(cx + 150, cy - 46), (cx + 170, cy - 40), (cx + 188, cy - 20), (cx + 172, cy + 22), (cx + 195, cy + 50)])
    leader(f, cx + 20, cy - 10, 470, 70, "nuclèol (RNAr i subunitats\ndels ribosomes)")
    leader(f, cx - 40, cy + 40, 470, 270, "cromatina (DNA + histones)")
    leader(f, cx + 124 * math.cos(math.radians(320)), cy + 124 * math.sin(math.radians(320)), 470, 115, "porus nuclear")
    leader(f, cx - 90, cy - 85, 40, 20, "embolcall: doble membrana", "start")
    leader(f, cx + 185, cy + 10, 470, 175, "reticle rugós, continu\namb l’embolcall")
    return f.svg()


def fig_mitocondri():
    f = Fig(760, 300, "El mitocondri")
    cx, cy, w, h = 250, 150, 380, 180
    f.ellipse(cx, cy, w / 2, h / 2, fill="#fbe3cf", stroke="#c4651a", sw=3)
    f.ellipse(cx, cy, w / 2 - 12, h / 2 - 12, fill="#fff3e6", stroke="#c4651a", sw=2.2)
    for i in range(8):
        x = cx - 150 + i * 42
        top = i % 2 == 0
        y0 = cy - h / 2 + 12 if top else cy + h / 2 - 12
        y1 = cy + (18 if top else -18)
        f.path(f"M{x-7},{y0} L{x-7},{y1} Q{x},{y1 + (10 if top else -10)} {x+7},{y1} L{x+7},{y0}", stroke="#c4651a", sw=2, fill="#fbe3cf")
    f.path(f"M{cx-40},{cy+5} c15,-25 35,25 50,0 c10,-15 25,-10 20,8 c-5,20 -40,25 -70,-8", stroke=col("lila"), sw=2)
    ribos(f, [(cx + 60, cy - 30), (cx + 80, cy + 40), (cx - 100, cy - 25), (cx - 80, cy + 45), (cx + 110, cy + 10)])
    leader(f, cx - 160, cy - 60, 30, 20, "membrana externa", "start")
    leader(f, cx - 120, cy - 52, 160, 20, "espai intermembranós (H⁺)", "start")
    leader(f, cx + 8, cy - 55, 500, 40, "membrana interna: crestes,\ncadena respiratòria i ATP-sintasa")
    leader(f, cx + 120, cy + 30, 500, 140, "matriu: Krebs, β-oxidació,\ndescarboxilació del piruvat")
    leader(f, cx - 10, cy + 5, 500, 205, "DNA circular propi")
    leader(f, cx + 80, cy + 40, 500, 260, "ribosomes 70S")
    return f.svg()


def fig_cloroplast():
    f = Fig(760, 320, "El cloroplast")
    cx, cy, w, h = 250, 165, 400, 210
    f.ellipse(cx, cy, w / 2, h / 2, fill="#d9efc9", stroke="#2e7d4f", sw=3)
    f.ellipse(cx, cy, w / 2 - 10, h / 2 - 10, fill="#eef8e8", stroke="#2e7d4f", sw=2)
    for k, (gx, gy) in enumerate([(130, 140), (215, 120), (300, 145), (175, 210), (265, 215), (345, 200)]):
        for j in range(5):
            f.rect(gx - 22, gy - 14 + j * 7, 44, 6, fill="#5aa36f", stroke="#2e7d4f", sw=0.8, rx=3)
    f.path("M152,155 L193,135 M237,135 L278,160 M197,225 L243,230 M287,230 L323,215", stroke="#2e7d4f", sw=3)
    f.path(f"M{cx-60},{cy+50} c10,-10 20,10 30,0", stroke=col("lila"), sw=2)
    ribos(f, [(cx - 120, cy + 40), (cx + 100, cy - 60), (cx + 140, cy + 30), (cx - 60, cy - 70)])
    f.ellipse(cx + 40, cy + 55, 18, 10, fill="#fff", stroke=MUTED, sw=1)
    leader(f, cx - 150, cy - 70, 30, 25, "embolcall: doble membrana", "start")
    leader(f, 215, 106, 500, 40, "tilacoide: fase lluminosa\n(fotosistemes, ATP-sintasa)")
    leader(f, 300, 150, 500, 110, "granum (pila de tilacoides)")
    leader(f, cx + 150, cy + 10, 500, 175, "estroma: cicle de Calvin")
    leader(f, cx - 45, cy + 50, 500, 235, "DNA circular i ribosomes 70S")
    leader(f, cx + 40, cy + 55, 500, 290, "grànul de midó")
    return f.svg()


def cell_common(f, cx, cy, plant=False):
    if plant:
        f.rect(cx - 205, cy - 135, 410, 270, fill="#e7f2da", stroke="#5c8a2e", sw=7, rx=14)
        f.rect(cx - 196, cy - 126, 392, 252, fill=CYTO, stroke=MEMB, sw=2, rx=10)
    else:
        f.path(f"M{cx-200},{cy} C{cx-200},{cy-150} {cx+180},{cy-160} {cx+200},{cy-10} C{cx+215},{cy+140} {cx-190},{cy+150} {cx-200},{cy} z", fill=CYTO, stroke=MEMB, sw=2.5)


def fig_animal():
    f = Fig(720, 340, "Cèl·lula animal")
    cx, cy = 240, 170
    cell_common(f, cx, cy)
    f.circle(cx - 20, cy, 52, fill="#e9e2f5", stroke=col("lila"), sw=2.5)
    f.circle(cx - 28, cy - 8, 15, fill="#b9a6dd", stroke="none")
    # RER i REL
    for k in range(3):
        f.path(f"M{cx-80-k*10},{cy+60+k*12} q30,10 60,0 t60,0", stroke="#2f6fb5", sw=2.2)
    ribos(f, [(cx - 70, cy + 62), (cx - 45, cy + 66), (cx - 20, cy + 63), (cx + 5, cy + 66), (cx - 60, cy + 87), (cx - 30, cy + 90)])
    for k in range(3):
        f.path(f"M{cx-130},{cy-50-k*14} q15,-10 30,0 q15,10 30,0", stroke="#2fa0b5", sw=2.2)
    # Golgi
    for k in range(4):
        f.path(f"M{cx+70},{cy-60+k*10} q30,-10 60,0", stroke=col("taronja"), sw=3)
    f.circle(cx + 140, cy - 62, 5, fill="#fbd3b0", stroke=col("taronja"))
    mito(f, cx + 120, cy + 50, 60, 28, 10)
    mito(f, cx - 140, cy + 30, 54, 26, 70)
    f.circle(cx + 50, cy + 95, 14, fill="#f6d2d2", stroke=col("vermell"), sw=1.8)
    f.circle(cx + 160, cy, 9, fill="#fff2c2", stroke=col("groc"), sw=1.5)
    # centríols
    f.rect(cx + 35, cy - 85, 8, 22, fill=INK, stroke="none", rx=2)
    f.rect(cx + 46, cy - 76, 22, 8, fill=INK, stroke="none", rx=2)
    leader(f, cx - 20, cy - 40, 480, 30, "nucli")
    leader(f, cx - 28, cy - 8, 480, 62, "nuclèol")
    leader(f, cx + 55, cy - 75, 480, 95, "centríols (centrosoma)")
    leader(f, cx + 100, cy - 50, 480, 128, "aparell de Golgi")
    leader(f, cx + 160, cy, 480, 160, "peroxisoma")
    leader(f, cx + 140, cy + 50, 480, 192, "mitocondri")
    leader(f, cx + 50, cy + 95, 480, 225, "lisosoma")
    leader(f, cx - 30, cy + 66, 480, 258, "reticle endoplasmàtic rugós")
    leader(f, cx - 100, cy - 60, 480, 290, "reticle endoplasmàtic llis")
    leader(f, cx - 205, cy + 20, 20, 320, "membrana plasmàtica", "start")
    return f.svg()


def fig_vegetal():
    f = Fig(760, 340, "Cèl·lula vegetal")
    cx, cy = 230, 170
    cell_common(f, cx, cy, plant=True)
    f.rect(cx - 60, cy - 90, 230, 175, fill="#dcecf8", stroke=col("blau"), sw=2, rx=40)
    f.circle(cx - 125, cy - 55, 40, fill="#e9e2f5", stroke=col("lila"), sw=2.5)
    f.circle(cx - 132, cy - 60, 11, fill="#b9a6dd", stroke="none")
    chloro(f, cx - 140, cy + 60, 64, 32, -20)
    chloro(f, cx + 50, cy + 105, 64, 30, 5)
    chloro(f, cx + 150, cy - 105, 60, 28, 0)
    mito(f, cx - 50, cy + 100, 46, 22, 0)
    for k in range(3):
        f.path(f"M{cx-185},{cy+5+k*9} q20,-8 40,0", stroke=col("taronja"), sw=2.6)
    leader(f, cx + 200, cy + 60, 470, 30, "paret de cel·lulosa")
    leader(f, cx + 196, cy - 20, 470, 65, "membrana plasmàtica")
    leader(f, cx + 120, cy, 470, 100, "vacúol (tonoplast)")
    leader(f, cx + 150, cy - 105, 470, 135, "cloroplast")
    leader(f, cx - 50, cy + 100, 470, 170, "mitocondri")
    leader(f, cx - 125, cy - 55, 470, 205, "nucli")
    leader(f, cx - 165, cy + 10, 470, 240, "aparell de Golgi")
    leader(f, cx - 205, cy - 120, 470, 290, "plasmodesmes a la paret · sense centríols")
    for y in (cy - 60, cy + 40):
        f.line(cx - 210, y, cx - 196, y, stroke="#5c8a2e", sw=2)
    return f.svg()


def chrom(f, x, y, color, sister=True, h=34, ang=0, w=7):
    """Cromosoma: dues cromàtides (X) o una sola (|) amb centròmer al mig."""
    g = f'<g transform="rotate({ang} {x} {y})">'
    f.raw(g)
    if sister:
        f.rect(x - w - 1, y - h / 2, w, h, fill=color, stroke="none", rx=w / 2)
        f.rect(x + 1, y - h / 2, w, h, fill=color, stroke="none", rx=w / 2)
        f.circle(x, y, 3.5, fill=INK, stroke="none")
    else:
        f.rect(x - w / 2, y - h / 2, w, h, fill=color, stroke="none", rx=w / 2)
        f.circle(x, y, 3, fill=INK, stroke="none")
    f.raw("</g>")


RED = "#d0453b"; BLU = "#3b74c4"


def cellcirc(f, cx, cy, r=62, spindle=False, nucleus=False, poles="h"):
    f.circle(cx, cy, r, fill="#f6f1e6", stroke=MEMB, sw=2)
    if nucleus:
        f.circle(cx, cy, r * 0.62, fill="none", stroke=col("lila"), sw=1.8, dash="5 3")
    if spindle:
        for k in (-0.5, -0.25, 0, 0.25, 0.5):
            if poles == "h":
                f.path(f"M{cx-r+8},{cy} Q{cx},{cy + k*r*1.6} {cx+r-8},{cy}", stroke="#e0b44a", sw=1.2)
            else:
                f.path(f"M{cx},{cy-r+8} Q{cx + k*r*1.6},{cy} {cx},{cy+r-8}", stroke="#e0b44a", sw=1.2)
        for px, py in ((cx - r + 8, cy), (cx + r - 8, cy)) if poles == "h" else ((cx, cy - r + 8), (cx, cy + r - 8)):
            f.circle(px, py, 5, fill="#e0b44a", stroke="none")


def fig_mitosi():
    f = Fig(640, 260, "Fases de la mitosi (2n = 4)")
    names = [("Profase", "condensació"), ("Metafase", "pla equatorial"), ("Anafase", "se separen\nles cromàtides"), ("Telofase i\ncitocinesi", "dos nuclis 2n")]
    for i, (n, s) in enumerate(names):
        cx = 82 + i * 158
        f.text(cx, 22, n, size=14, weight=700, fill=col("teal"))
        f.text(cx, 225, s, size=12, fill=MUTED)
        cy = 120
        if i == 0:
            cellcirc(f, cx, cy, nucleus=True)
            for (dx, dy, c, a) in [(-14, -12, RED, 20), (12, -10, BLU, -30), (-10, 14, BLU, 70), (14, 14, RED, -10)]:
                chrom(f, cx + dx, cy + dy, c, h=26, ang=a)
        elif i == 1:
            cellcirc(f, cx, cy, spindle=True, poles="v")
            for k, c in enumerate([RED, BLU, RED, BLU]):
                chrom(f, cx - 33 + k * 22, cy, c, h=26, ang=90)
        elif i == 2:
            cellcirc(f, cx, cy, spindle=True, poles="v")
            for k, c in enumerate([RED, BLU, RED, BLU]):
                xx = cx - 30 + k * 20
                chrom(f, xx, cy - 30, c, sister=False, h=22)
                chrom(f, xx, cy + 30, c, sister=False, h=22)
        else:
            f.path(f"M{cx-60},{cy} C{cx-60},{cy-70} {cx+60},{cy-70} {cx+60},{cy} C{cx+60},{cy+70} {cx-60},{cy+70} {cx-60},{cy}", fill="#f6f1e6", stroke=MEMB, sw=2)
            f.line(cx - 58, cy, cx + 58, cy, stroke=MEMB, sw=2, dash="6 3")
            for yy in (cy - 32, cy + 32):
                f.ellipse(cx, yy, 36, 22, stroke=col("lila"), sw=1.6, dash="5 3")
                for k, c in enumerate([RED, BLU, RED, BLU]):
                    f.path(f"M{cx-20+k*13},{yy-12} q6,12 0,24", stroke=c, sw=3)
        if i < 3:
            f.arrow(cx + 68, 120, cx + 88, 120, color=MUTED)
    return f.svg()


def fig_meiosi():
    f = Fig(640, 470, "Fases de la meiosi (2n = 4)")
    f.text(10, 20, "Meiosi I (reduccional): se separen els homòlegs", size=14, weight=700, anchor="start", fill=col("vermell"))
    f.text(10, 250, "Meiosi II (equacional): se separen les cromàtides germanes", size=14, weight=700, anchor="start", fill=col("blau"))
    labs1 = [("Profase I", "aparellament i\nentrecreuament"), ("Metafase I", "bivalents a l’equador"), ("Anafase I", "homòlegs cap\na pols oposats"), ("Telofase I", "2 cèl·lules n,\ncromosomes dobles")]
    labs2 = [("Profase II", ""), ("Metafase II", "cromosomes\na l’equador"), ("Anafase II", "cromàtides cap\na pols oposats"), ("Telofase II", "4 cèl·lules n,\ncromosomes simples")]
    cy = 125
    for i, (n, s) in enumerate(labs1):
        cx = 82 + i * 158
        f.text(cx, 46, n, size=13, weight=700)
        f.text(cx, 214, s, size=11, fill=MUTED)
        if i == 0:
            cellcirc(f, cx, cy, nucleus=True)
            # bivalent amb quiasma
            chrom(f, cx - 12, cy - 14, RED, h=28, ang=-15); chrom(f, cx + 2, cy - 12, BLU, h=28, ang=-15)
            chrom(f, cx - 6, cy + 18, BLU, h=20, ang=80); chrom(f, cx - 4, cy + 30, RED, h=20, ang=80)
            f.circle(cx - 5, cy - 13, 8, stroke=col("groc"), sw=1.8, dash="2 2")
        elif i == 1:
            cellcirc(f, cx, cy, spindle=True, poles="v")
            for k, (a, b) in enumerate([(RED, BLU), (BLU, RED)]):
                xx = cx - 18 + k * 36
                chrom(f, xx, cy - 11, a, h=20, ang=90); chrom(f, xx, cy + 11, b, h=20, ang=90)
            f.line(cx - 60, cy, cx + 60, cy, stroke=LINE, dash="3 3", sw=1)
        elif i == 2:
            cellcirc(f, cx, cy, spindle=True, poles="v")
            for k, (a, b) in enumerate([(RED, BLU), (BLU, RED)]):
                xx = cx - 18 + k * 36
                chrom(f, xx, cy - 34, a, h=20, ang=90); chrom(f, xx, cy + 34, b, h=20, ang=90)
        else:
            for yy, cs in ((cy - 34, (RED, BLU)), (cy + 34, (BLU, RED))):
                f.ellipse(cx, yy, 58, 30, fill="#f6f1e6", stroke=MEMB, sw=2)
                chrom(f, cx - 14, yy, cs[0], h=20, ang=90); chrom(f, cx + 14, yy, cs[1], h=20, ang=90)
        if i < 3:
            f.arrow(cx + 68, cy, cx + 88, cy, color=MUTED)
    cy = 360
    for i, (n, s) in enumerate(labs2):
        cx = 82 + i * 158
        f.text(cx, 276, n, size=13, weight=700)
        f.text(cx, 448, s, size=11, fill=MUTED)
        r = 48
        if i == 0:
            f.circle(cx, cy, r, fill="#f6f1e6", stroke=MEMB, sw=2)
            chrom(f, cx - 12, cy - 6, RED, h=24, ang=30); chrom(f, cx + 12, cy + 6, BLU, h=24, ang=-20)
        elif i == 1:
            cellcirc(f, cx, cy, r=r, spindle=True, poles="v")
            chrom(f, cx - 14, cy, RED, h=24, ang=90); chrom(f, cx + 14, cy, BLU, h=24, ang=90)
        elif i == 2:
            cellcirc(f, cx, cy, r=r, spindle=True, poles="v")
            for xx, c in ((cx - 14, RED), (cx + 14, BLU)):
                chrom(f, xx, cy - 25, c, sister=False, h=18); chrom(f, xx, cy + 25, c, sister=False, h=18)
        else:
            for yy in (cy - 26, cy + 26):
                f.ellipse(cx, yy, 40, 22, fill="#f6f1e6", stroke=MEMB, sw=2)
                chrom(f, cx - 9, yy, RED, sister=False, h=16, ang=0); chrom(f, cx + 9, yy, BLU, sister=False, h=16)
            f.text(cx + 52, cy, "×2", size=13, weight=700, fill=MUTED)
        if i < 3:
            f.arrow(cx + 58, cy, cx + 98, cy, color=MUTED)
    f.text(320, 236, "↓ cada una de les dues cèl·lules fa la meiosi II (sense fase S abans)", size=12, fill=MUTED)
    return f.svg()


def fig_cicle():
    f = Fig(640, 320, "El cicle cel·lular")
    cx, cy, R = 200, 160, 120
    segs = [("G1", 0, 150, "verd", "creixement"), ("S", 150, 250, "blau", "replicació del DNA"), ("G2", 250, 320, "taronja", "preparació"), ("M", 320, 360, "vermell", "mitosi i citocinesi")]
    for name, a0, a1, c, desc in segs:
        r0, r1 = math.radians(a0 - 90), math.radians(a1 - 90)
        x0, y0 = cx + R * math.cos(r0), cy + R * math.sin(r0)
        x1, y1 = cx + R * math.cos(r1), cy + R * math.sin(r1)
        large = 1 if a1 - a0 > 180 else 0
        f.path(f"M{cx},{cy} L{x0:.1f},{y0:.1f} A{R},{R} 0 {large} 1 {x1:.1f},{y1:.1f} z", fill=light(c), stroke="#fff", sw=3)
        am = math.radians((a0 + a1) / 2 - 90)
        f.text(cx + R * 0.66 * math.cos(am), cy + R * 0.66 * math.sin(am), name, size=20, weight=700, fill=col(c))
    f.circle(cx, cy, 44, fill="#fff", stroke=LINE)
    f.text(cx, cy, "interfase:\nG1 + S + G2", size=11, fill=MUTED)
    f.arrowpath(f"M{cx + (R+12)*math.cos(math.radians(-80))},{cy + (R+12)*math.sin(math.radians(-80))} A{R+12},{R+12} 0 0 1 {cx + (R+12)*math.cos(math.radians(40))},{cy + (R+12)*math.sin(math.radians(40))}", color=MUTED, sw=2)
    x = 360
    rows = [("G1", "verd", "creix; DNA 2C; si no es divideix → G0"), ("S", "blau", "replica el DNA: 2C → 4C"), ("G2", "taronja", "cromosomes de 2 cromàtides"), ("M", "vermell", "mitosi + citocinesi")]
    for k, (n, c, t) in enumerate(rows):
        f.pill(x + 18, 50 + k * 40, n, color=c, size=13, solid=True)
        f.text(x + 46, 50 + k * 40, t, size=13, anchor="start")
    f.text(x, 230, "Punts de control:", size=13, weight=700, anchor="start")
    f.text(x, 264, "· final de G1 (dany, mida)\n· final de G2 (replicació acabada)\n· metafase (cromosomes units al fus)", size=12, anchor="start", fill=MUTED, lh=1.35)
    return f.svg()
