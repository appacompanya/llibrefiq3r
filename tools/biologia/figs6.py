"""Figures de metabolisme refetes a la segona revisió."""
import math
from svg import Fig, INK, MUTED, LINE, col, light


def fig_cat_anab():
    f = Fig(640, 270, "Catabolisme i anabolisme")
    f.text(320, 18, "exemples: glucosa → CO₂ (respiració) · CO₂ → glucosa (cicle de Calvin)", size=12, fill=MUTED)
    f.box(20, 40, 230, 76, "Catabolisme\nmolècules grans → petites\n(sobretot oxidacions)", color="taronja", size=14)
    f.box(390, 40, 230, 76, "Anabolisme\nmolècules petites → grans\n(sobretot reduccions)", color="blau", size=14)
    f.box(190, 170, 260, 76, "ATP\ncoenzims reduïts\nNADH · FADH₂ · NADPH", color="groc", size=14)
    f.arrow(140, 118, 230, 168, color=col("taronja"), sw=2.4)
    f.arrow(410, 168, 500, 118, color=col("blau"), sw=2.4)
    f.text(160, 160, "els produeix", size=12, fill=col("taronja"), anchor="end", weight=700)
    f.text(482, 160, "els gasta", size=12, fill=col("blau"), anchor="start", weight=700)
    return f.svg()


def fig_glucolisi():
    f = Fig(640, 390, "Balanç de la glucòlisi")
    f.text(320, 20, "Glucòlisi · citosol · no necessita O₂", size=15, weight=700, fill=col("teal"))
    f.box(240, 40, 160, 40, "glucosa (6C)", color="verd", size=14)
    f.arrow(320, 82, 320, 118)
    f.pill(380, 100, "−2 ATP", color="vermell", size=13, solid=True)
    f.text(424, 100, "fase de preparació (inversió)", size=12, fill=MUTED, anchor="start")
    f.box(210, 120, 220, 40, "fructosa-1,6-bisfosfat (6C)", color="verd", size=13)
    f.arrow(290, 162, 210, 198); f.arrow(350, 162, 430, 198)
    for x in (110, 400):
        f.box(x, 200, 130, 36, "G3P (3C)", color="verd", size=13)
        f.arrow(x + 65, 238, x + 65, 290)
        f.box(x, 292, 130, 38, "piruvat (3C)", color="taronja", size=13)
    f.text(320, 218, "2 × gliceraldehid-3-fosfat", size=11, fill=MUTED)
    f.pill(320, 250, "+2 NADH", color="lila", size=13, solid=True)
    f.pill(320, 282, "+4 ATP", color="verd", size=13, solid=True)
    f.text(320, 312, "fase de rendiment", size=12, fill=MUTED)
    f.rect(180, 344, 280, 36, fill="#fff", stroke=INK, sw=2, rx=8)
    f.text(320, 362, "balanç net: 2 ATP · 2 NADH · 2 piruvat", size=14, weight=700)
    return f.svg()


def fig_krebs():
    f = Fig(640, 520, "El cicle de Krebs")
    cx, cy, R = 300, 270, 150
    names = [("citrat", "6C"), ("isocitrat", "6C"), ("α-cetoglutarat", "5C"), ("succinil-CoA", "4C"),
             ("succinat", "4C"), ("fumarat", "4C"), ("malat", "4C"), ("oxalacetat", "4C")]
    ang = [-90 + 22.5 + i * 45 for i in range(8)]
    pos = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in ang]
    for i in range(8):
        a0, a1 = math.radians(ang[i] + 10), math.radians(ang[i] + 35)
        f.arrowpath(f"M{cx+R*math.cos(a0):.1f},{cy+R*math.sin(a0):.1f} A{R},{R} 0 0 1 {cx+R*math.cos(a1):.1f},{cy+R*math.sin(a1):.1f}", color=col("vermell"), sw=2.4)
    for (n, c), (x, y) in zip(names, pos):
        w = max(84, len(n) * 8.3)
        f.rect(x - w / 2, y - 19, w, 38, fill="#fff", stroke=col("vermell"), sw=1.8, rx=10)
        f.text(x, y - 5, n, size=13, weight=700); f.text(x, y + 10, c, size=10, fill=MUTED)
    f.text(cx, cy - 10, "matriu mitocondrial", size=13, fill=MUTED)
    f.text(cx, cy + 12, "1 volta per acetil-CoA", size=12, fill=MUTED)
    # entrada
    f.box(20, 30, 140, 38, "acetil-CoA (2C)", color="taronja", size=13)
    f.arrowpath(f"M160,49 C{pos[0][0]-40},40 {pos[0][0]-60},{pos[0][1]-50} {pos[0][0]-34},{pos[0][1]-20}", color=col("taronja"), sw=2.2)
    f.text(20, 88, "+ oxalacetat (4C) → citrat (6C)", size=11, fill=MUTED, anchor="start")

    def out(i, label, color, r_off=95, da=0):
        a = math.radians(ang[i] + 22.5 + da)
        x0, y0 = cx + (R + 6) * math.cos(a), cy + (R + 6) * math.sin(a)
        x1, y1 = cx + (R + r_off - 30) * math.cos(a), cy + (R + r_off - 30) * math.sin(a)
        f.arrow(x0, y0, x1, y1, color=col(color), sw=1.8)
        f.pill(cx + (R + r_off) * math.cos(a), cy + (R + r_off) * math.sin(a), label, color=color, size=12, solid=True)

    out(1, "NADH + CO₂", "lila")          # isocitrat → α-cetoglutarat
    out(2, "NADH + CO₂", "lila")          # α-cetoglutarat → succinil-CoA
    out(3, "GTP (≈ ATP)", "verd", 70)     # succinil-CoA → succinat
    out(4, "FADH₂", "blau", 75)           # succinat → fumarat
    out(5, "H₂O entra", "gris", 80)       # fumarat → malat
    out(6, "NADH", "lila", 70)            # malat → oxalacetat
    f.text(630, 30, "Per volta: 2 CO₂ · 3 NADH\n1 FADH₂ · 1 GTP", size=13, weight=700, anchor="end")
    return f.svg()


def fig_cadena():
    f = Fig(640, 360, "Cadena respiratòria i ATP-sintasa a la membrana mitocondrial interna")
    y1, y2 = 130, 210
    f.rect(0, y1, 640, y2 - y1, fill="#f5e7d0", stroke="none", rx=0)
    f.line(0, y1, 640, y1, stroke="#c4651a", sw=2); f.line(0, y2, 640, y2, stroke="#c4651a", sw=2)
    f.text(10, 26, "Espai intermembranós: molts H⁺ (pH més baix)", size=14, weight=700, anchor="start", fill=col("vermell"))
    f.text(10, 345, "Matriu", size=14, weight=700, anchor="start", fill=col("taronja"))
    comps = {"I": 70, "III": 300, "IV": 440}
    for n, x in comps.items():
        f.rect(x - 34, y1 - 16, 68, y2 - y1 + 32, fill=light("lila"), stroke=col("lila"), sw=2, rx=14)
        f.text(x - 10, (y1 + y2) / 2, n, size=18, weight=700, fill=col("lila"))
        f.arrow(x + 18, y2 + 26, x + 18, y1 - 34, color=col("vermell"), sw=2.2)
        f.text(x + 30, y1 - 44, "H⁺", size=13, weight=700, fill=col("vermell"), anchor="start")
    x2 = 175
    f.rect(x2 - 30, y2 - 34, 60, 62, fill=light("lila"), stroke=col("lila"), sw=2, rx=12)
    f.text(x2, y2 - 3, "II", size=17, weight=700, fill=col("lila"))
    f.circle(235, 170, 14, fill=light("groc"), stroke=col("groc"), sw=1.6); f.text(235, 170, "Q", size=13, weight=700)
    f.circle(370, 112, 13, fill=light("vermell"), stroke=col("vermell"), sw=1.6); f.text(370, 112, "c", size=13, weight=700)
    E = col("blau")
    f.arrowpath("M90,180 C140,190 190,176 219,172", color=E, sw=2.2)
    f.arrowpath("M197,186 C210,182 216,178 221,175", color=E, sw=2.2)
    f.arrowpath("M249,168 C262,166 270,166 280,166", color=E, sw=2.2)
    f.arrowpath("M318,120 C334,112 345,110 355,111", color=E, sw=2.2)
    f.arrowpath("M384,113 C400,115 410,122 416,128", color=E, sw=2.2)
    f.text(70, 268, "NADH → NAD⁺ + H⁺", size=12, weight=700, fill=col("lila"))
    f.text(185, 268, "FADH₂ → FAD", size=12, weight=700, fill=col("lila"))
    f.text(440, 268, "½ O₂ + 2 H⁺ → H₂O", size=12, weight=700, fill=E)
    # ATP-sintasa: F0 a la membrana, F1 a la matriu
    X = 570
    f.rect(X - 22, y1 - 8, 44, y2 - y1 + 16, fill=light("groc"), stroke=col("groc"), sw=2, rx=8)
    f.line(X, y2 + 8, X, y2 + 26, stroke=col("groc"), sw=6)
    f.circle(X, y2 + 58, 34, fill=light("groc"), stroke=col("groc"), sw=2)
    f.text(X, y2 + 58, "ATP-\nsintasa", size=11, weight=700)
    f.arrow(X + 38, y1 - 40, X + 38, y2 + 10, color=col("vermell"), sw=2.6)
    f.text(X + 38, y1 - 50, "H⁺", size=13, weight=700, fill=col("vermell"))
    f.text(X, y2 + 112, "ADP + P_{i} → ATP", size=13, weight=700, fill="#8a6a0e")
    f.text(10, 302, "e⁻: NADH → I → Q → III → cit c → IV → O₂ (el FADH₂ entra pel II)", size=12, fill=E, weight=700, anchor="start")
    return f.svg()


def fig_fermentacions():
    f = Fig(640, 320, "Fermentació làctica i fermentació alcohòlica")
    f.box(230, 16, 180, 40, "glucosa", color="verd", size=14)
    f.arrow(320, 58, 320, 88)
    f.text(332, 73, "glucòlisi: 2 ATP nets i 2 NADH", size=12, anchor="start", fill=MUTED)
    f.box(230, 90, 180, 40, "2 piruvat", color="taronja", size=14)
    # làctica
    f.arrow(250, 132, 140, 200)
    f.text(176, 156, "2 NADH → 2 NAD⁺", size=12, weight=700, fill=col("lila"), anchor="end")
    f.box(40, 202, 190, 44, "2 lactat", color="vermell", size=15)
    f.text(135, 270, "Làctica: múscul en anaerobiosi,\nLactobacillus (iogurt) · sense CO₂", size=12, fill=MUTED)
    # alcohòlica
    f.arrow(390, 132, 470, 168)
    f.arrow(436, 146, 508, 150, color=MUTED, sw=1.6)
    f.pill(564, 150, "2 CO₂ surten", color="gris", size=12, solid=True)
    f.box(410, 170, 170, 36, "2 acetaldehid", color="groc", size=13)
    f.arrow(495, 208, 495, 232)
    f.text(484, 220, "2 NADH → 2 NAD⁺", size=12, weight=700, fill=col("lila"), anchor="end")
    f.box(410, 234, 170, 40, "2 etanol", color="groc", size=15)
    f.text(495, 296, "Alcohòlica: llevats (pa, vi, cervesa)", size=12, fill=MUTED)
    return f.svg()


def fig_fase_lluminosa():
    f = Fig(700, 400, "Fase lluminosa a la membrana del tilacoide")
    y1, y2 = 150, 230
    f.rect(0, y1, 700, y2 - y1, fill="#dbeed8", stroke="none", rx=0)
    f.line(0, y1, 700, y1, stroke=col("verd"), sw=2); f.line(0, y2, 700, y2, stroke=col("verd"), sw=2)
    f.text(10, 24, "Estroma", size=14, weight=700, anchor="start", fill=col("verd"))
    f.text(10, 385, "Lumen del tilacoide: molts H⁺", size=14, weight=700, anchor="start", fill=col("vermell"))

    def cx(x, w, t, c):
        f.rect(x - w / 2, y1 - 20, w, y2 - y1 + 40, fill=light(c), stroke=col(c), sw=2, rx=12)
        f.text(x - (12 if t.startswith("cit") else 0), (y1 + y2) / 2, t, size=13 if not t.startswith("cit") else 12, weight=700)
    cx(90, 82, "FS II\nP680", "verd")
    cx(260, 72, "cit b₆f", "lila")
    cx(420, 82, "FS I\nP700", "verd")
    f.circle(175, 190, 14, fill=light("groc"), stroke=col("groc")); f.text(175, 190, "PQ", size=10, weight=700)
    f.circle(340, 244, 14, fill=light("blau"), stroke=col("blau")); f.text(340, 244, "PC", size=10, weight=700)
    f.circle(470, 108, 13, fill=light("vermell"), stroke=col("vermell")); f.text(470, 108, "Fd", size=10, weight=700)
    for x in (90, 420):
        f.text(x - 30, 70, "llum", size=12, fill="#b38600", weight=700, anchor="end")
        f.arrow(x - 26, 76, x - 8, 122, color="#e6a700", sw=3)
    E = col("blau")
    f.text(90, 300, "2 H₂O → O₂ + 4 H⁺ + 4 e⁻", size=12, weight=700, fill=E)
    f.arrow(90, 288, 90, 256, color=E)
    f.arrowpath("M131,196 C148,198 152,194 160,192", color=E)
    f.arrowpath("M189,190 C205,190 215,190 222,190", color=E)
    f.arrowpath("M286,232 C305,246 315,246 325,245", color=E)
    f.arrowpath("M355,243 C368,240 374,234 378,228", color=E)
    f.arrowpath("M440,128 C448,118 452,112 456,110", color=E)
    f.arrowpath("M482,100 C496,80 510,60 526,50", color=E)
    f.box(470, 18, 130, 30, "NADP⁺ → NADPH", color="lila", size=12)
    # bombament de H+ pel cit b6f: de l'estroma cap al lumen
    f.arrow(284, y1 - 44, 284, y2 + 30, color=col("vermell"), sw=2.4)
    f.text(296, y1 - 50, "H⁺", size=13, weight=700, fill=col("vermell"), anchor="start")
    # ATP-sintasa: F0 a la membrana, F1 a l'estroma; H+ del lumen cap a l'estroma
    X = 640
    f.rect(X - 20, y1 - 6, 40, y2 - y1 + 12, fill=light("groc"), stroke=col("groc"), sw=2, rx=8)
    f.line(X, y1 - 6, X, y1 - 24, stroke=col("groc"), sw=6)
    f.circle(X, y1 - 54, 30, fill=light("groc"), stroke=col("groc"), sw=2)
    f.text(X, y1 - 54, "ATP-\nsintasa", size=10.5, weight=700)
    f.arrow(X - 38, y2 + 44, X - 38, y1 - 8, color=col("vermell"), sw=2.6)
    f.text(X - 50, y2 + 50, "H⁺", size=13, weight=700, fill=col("vermell"), anchor="end")
    f.text(X - 10, y1 - 96, "ADP + P_{i} → ATP", size=12, weight=700, fill="#8a6a0e")
    f.text(350, 345, "L’O₂ prové de l’aigua (fotòlisi al FS II). L’ATP i el NADPH queden a l’estroma per al cicle de Calvin.", size=11.5, fill=MUTED)
    return f.svg()


def fig_homolegs():
    """Parella de cromosomes homòlegs: mateixos loci, al·lels iguals o diferents."""
    f = Fig(640, 360, "Una parella de cromosomes homòlegs amb dos gens")
    RED, BLU = "#c0504d", "#3d6fb0"
    xs = {"m": 230, "p": 330}
    w, top, bot, cen = 46, 50, 320, 150
    for k, c in (("m", RED), ("p", BLU)):
        x = xs[k]
        f.path(f"M{x-w/2},{top+20} Q{x-w/2},{top} {x},{top} Q{x+w/2},{top} {x+w/2},{top+20} L{x+w/2},{cen-10} "
               f"Q{x+w/2-12},{cen} {x+w/2},{cen+10} L{x+w/2},{bot-20} Q{x+w/2},{bot} {x},{bot} Q{x-w/2},{bot} {x-w/2},{bot-20} "
               f"L{x-w/2},{cen+10} Q{x-w/2+12},{cen} {x-w/2},{cen-10} Z", fill=light("vermell") if k == "m" else light("blau"), stroke=c, sw=2.2)
    # loci
    loci = [(100, "Y", "y"), (240, "A", "A")]
    for y, am, ap in loci:
        f.line(150 if y > 200 else xs["m"] - w / 2 - 8, y, xs["p"] + w / 2 + 8, y, stroke=MUTED, sw=1, dash="3 3")
        for k, a in (("m", am), ("p", ap)):
            x = xs[k]
            f.rect(x - w / 2 + 2, y - 9, w - 4, 18, fill="#fff", stroke=INK, sw=1.4, rx=3)
            f.text(x, y, a, size=15, weight=700, italic=True)
    f.text(xs["m"], top - 22, "de la mare", size=13, weight=700, fill=RED)
    f.text(xs["p"], top - 22, "del pare", size=13, weight=700, fill=BLU)
    f.text(118, cen, "centròmer", size=12, fill=MUTED, anchor="end")
    f.line(122, cen, xs["m"] - w / 2 - 2, cen, stroke=MUTED, sw=1)
    f.text(372, 92, "locus del gen del color de la llavor", size=13, weight=700, anchor="start")
    f.text(372, 110, "al·lels diferents (Y i y): heterozigot", size=12.5, fill=MUTED, anchor="start")
    f.text(372, 232, "locus del gen del color de la flor", size=13, weight=700, anchor="start")
    f.text(372, 250, "al·lels iguals (A i A): homozigot", size=12.5, fill=MUTED, anchor="start")
    f.text(30, 206, "mateix gen,\nmateixa posició\nals dos homòlegs", size=12, fill=MUTED, anchor="start")
    f.text(320, 348, "Genotip per a aquests dos gens: YyAA", size=14, weight=700)
    return f.svg()
