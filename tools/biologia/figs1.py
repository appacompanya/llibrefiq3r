"""Figures del tema 1 (Biomolècules)."""
import math
from svg import Fig, INK, MUTED, LINE, col, light

RED = "#c0392b"


# ---------------- Haworth ----------------
def pyranose(f, x, y, subs, label=None, s=1.0, ring_o_label=True, nums=True):
    """Anell de piranosa en projecció de Haworth.
    x, y: vèrtex C4 (esquerra). subs: {carboni: (dalt, baix)} amb textos o None.
    Retorna les coordenades dels punts d'ancoratge dels substituents."""
    P = {
        "C4": (x, y + 34 * s), "C5": (x + 38 * s, y), "O": (x + 112 * s, y),
        "C1": (x + 150 * s, y + 34 * s), "C2": (x + 112 * s, y + 70 * s), "C3": (x + 38 * s, y + 70 * s),
    }
    order = ["C5", "O", "C1", "C2", "C3", "C4", "C5"]
    widths = {("C5", "O"): 1.8, ("O", "C1"): 1.8, ("C1", "C2"): 3.2, ("C2", "C3"): 6, ("C3", "C4"): 3.2, ("C4", "C5"): 1.8}
    for a, b in zip(order, order[1:]):
        (x1, y1), (x2, y2) = P[a], P[b]
        if a == "C5" and b == "O" or a == "O" and b == "C1":
            # deixem lloc per a la O
            pass
        f.line(x1, y1, x2, y2, sw=widths[(a, b)], cap="round")
    ox, oy = P["O"]
    f.rect(ox - 9, oy - 9, 18, 18, fill="#fff", stroke="none", rx=4)
    f.text(ox, oy, "O", size=16 * s, weight=700, fill=RED)
    anchors = {}
    L = 30 * s
    for c, (up, down) in subs.items():
        cx, cy = P[c]
        if up:
            f.line(cx, cy, cx, cy - L, sw=1.6)
            f.text(cx, cy - L - 10 * s, up, size=14 * s, weight=600)
            anchors[c + "u"] = (cx, cy - L)
        if down:
            f.line(cx, cy, cx, cy + L, sw=1.6)
            f.text(cx, cy + L + 11 * s, down, size=14 * s, weight=600)
            anchors[c + "d"] = (cx, cy + L)
    if nums:
        for c, (dx, dy) in {"C1": (12, -4), "C2": (10, 8), "C3": (-12, 8), "C4": (-13, -4), "C5": (-12, -8)}.items():
            cx, cy = P[c]
            f.text(cx + dx * s, cy + dy * s, c[1], size=11 * s, fill=MUTED, weight=700)
    if label:
        f.text(x + 75 * s, y - 70 * s, label, size=15, weight=700, fill=col("teal"))
    return P, anchors


def fig_anomers():
    f = Fig(640, 290, "α-D-glucopiranosa i β-D-glucopiranosa en projecció de Haworth")
    for i, (nom, a) in enumerate([("α-D-glucopiranosa", "α"), ("β-D-glucopiranosa", "β")]):
        x0 = 70 + i * 320
        up1, dn1 = ("OH", None) if a == "β" else (None, "OH")
        pyranose(f, x0, 110, {"C5": ("CH₂OH", None), "C4": (None, "OH"), "C3": ("OH", None), "C2": (None, "OH"), "C1": (up1, dn1)}, label=nom)
        cx = x0 + 150
        cy = 144 + (-30 if a == "β" else 30)
        f.circle(cx, cy + (-10 if a == "β" else 11), 17, stroke=col("taronja"), sw=2.2, dash="4 3")
        f.text(x0 + 75, 268, "OH del C1 " + ("amunt (cis respecte del C6)" if a == "β" else "avall (trans respecte del C6)"), size=13, fill=col("taronja"), weight=700)
    f.text(320, 24, "L’únic canvi és la posició de l’OH del carboni anomèric (C1)", size=14, fill=MUTED)
    return f.svg()


def furanose_flipped(f, x, y, s=1.0):
    """β-D-fructofuranosa girada 180° (com es dibuixa dins la sacarosa): C2 a l'esquerra.
    x,y: vèrtex C2. Retorna l'ancoratge de l'O anomèric (avall)."""
    P = {"C2": (x, y + 30), "C3": (x + 26, y + 66), "C4": (x + 94, y + 66), "C5": (x + 120, y + 30), "O": (x + 60, y)}
    seq = [("O", "C2", 1.8), ("C2", "C3", 3.2), ("C3", "C4", 6), ("C4", "C5", 3.2), ("C5", "O", 1.8)]
    for a, b, w in seq:
        f.line(*P[a], *P[b], sw=w)
    ox, oy = P["O"]
    f.rect(ox - 9, oy - 9, 18, 18, fill="#fff", stroke="none", rx=4)
    f.text(ox, oy, "O", size=16, weight=700, fill=RED)
    def sub(c, up, txt, L=30):
        cx, cy = P[c]
        yy = cy - L if up else cy + L
        f.line(cx, cy, cx, yy)
        if txt:
            f.text(cx, yy + (-10 if up else 11), txt, size=14, weight=600)
        return cx, yy
    sub("C2", True, "CH₂OH")
    a = sub("C2", False, None)
    sub("C3", False, "OH")
    sub("C4", True, "OH")
    sub("C5", False, "CH₂OH", L=46)
    for c, (dx, dy) in {"C2": (-14, -2), "C3": (-12, 8), "C4": (12, 8), "C5": (13, -4)}.items():
        cx, cy = P[c]
        f.text(cx + dx, cy + dy, c[1], size=11, fill=MUTED, weight=700)
    return a


def glyco_O(f, x, y):
    f.rect(x - 9, y - 9, 18, 18, fill="#fff", stroke="none", rx=4)
    f.text(x, y, "O", size=16, weight=700, fill=RED)


def fig_disacarids():
    f = Fig(640, 750, "Maltosa, lactosa i sacarosa en projecció de Haworth")
    glc = {"C5": ("CH₂OH", None), "C3": ("OH", None), "C2": (None, "OH")}
    # --- maltosa ---
    y = 40
    f.text(20, y - 14, "Maltosa", size=17, weight=700, anchor="start", fill=col("teal"))
    f.text(20, y + 8, "α-D-glucosa-(1→4)-D-glucosa · reductora", size=13, anchor="start", fill=MUTED)
    P1, A1 = pyranose(f, 40, y + 85, {**glc, "C4": (None, "OH"), "C1": (None, None)}, s=0.95)
    P2, A2 = pyranose(f, 330, y + 85, {**glc, "C4": (None, None), "C1": (None, "OH")}, s=0.95)
    c1 = P1["C1"]; c4 = P2["C4"]
    f.line(c1[0], c1[1], c1[0] + 40, c1[1] + 42, sw=1.6)
    f.line(c4[0], c4[1], c4[0] - 40, c4[1] + 42, sw=1.6)
    f.line(c1[0] + 40, c1[1] + 42, c4[0] - 40, c4[1] + 42, sw=1.6)
    glyco_O(f, (c1[0] + c4[0]) / 2, c1[1] + 42)
    f.text((c1[0] + c4[0]) / 2, c1[1] + 66, "enllaç α(1→4)", size=13, weight=700, fill=col("taronja"))
    f.text(P2["C1"][0] + 40, P2["C1"][1] + 14, "anomèric\nlliure", size=12, fill=col("verd"), weight=700, anchor="start")
    # --- lactosa ---
    y = 280
    f.text(20, y - 14, "Lactosa", size=17, weight=700, anchor="start", fill=col("teal"))
    f.text(20, y + 8, "β-D-galactosa-(1→4)-D-glucosa · reductora", size=13, anchor="start", fill=MUTED)
    P1, A1 = pyranose(f, 40, y + 85, {**glc, "C4": ("OH", None), "C1": (None, None)}, s=0.95)
    P2, A2 = pyranose(f, 330, y + 85, {**glc, "C4": (None, None), "C1": (None, "OH")}, s=0.95)
    c1 = P1["C1"]; c4 = P2["C4"]
    # β: l'enllaç surt amunt del C1 de la galactosa i arriba per sota al C4 de la glucosa
    ox, oy = c1[0] + 40, c1[1] - 40
    f.line(c1[0], c1[1], c1[0], oy, sw=1.6); f.line(c1[0], oy, ox - 9, oy, sw=1.6)
    glyco_O(f, ox, oy)
    f.path(f"M{ox+9},{oy} L{c4[0]-30},{oy} L{c4[0]-30},{c4[1]+40} L{c4[0]},{c4[1]+40} L{c4[0]},{c4[1]}", sw=1.6)
    f.text(ox + 40, oy - 16, "enllaç β(1→4)", size=13, weight=700, fill=col("taronja"))
    f.text(P1["C4"][0] + 75, P1["C4"][1] + 92, "galactosa: OH del C4 amunt", size=12, fill=MUTED)
    f.text(P2["C1"][0] + 40, P2["C1"][1] + 14, "anomèric\nlliure", size=12, fill=col("verd"), weight=700, anchor="start")
    # --- sacarosa ---
    y = 520
    f.text(20, y - 14, "Sacarosa", size=17, weight=700, anchor="start", fill=col("teal"))
    f.text(20, y + 8, "α-D-glucosa-(1↔2)-β-D-fructosa · no reductora", size=13, anchor="start", fill=MUTED)
    P1, A1 = pyranose(f, 40, y + 85, {**glc, "C4": (None, "OH"), "C1": (None, None)}, s=0.95)
    c1 = P1["C1"]
    fx, fy = 360, y + 89
    a = furanose_flipped(f, fx, fy)
    f.line(c1[0], c1[1], c1[0] + 40, c1[1] + 42)
    f.line(a[0], a[1], a[0] - 22, c1[1] + 42)
    f.line(c1[0] + 40, c1[1] + 42, a[0] - 22, c1[1] + 42)
    glyco_O(f, (c1[0] + 40 + a[0] - 22) / 2, c1[1] + 42)
    f.text((c1[0] + a[0]) / 2 + 10, c1[1] + 66, "enllaç α1↔β2: cap anomèric lliure", size=13, weight=700, fill=col("vermell"))
    f.text(fx + 60, fy - 52, "β-D-fructofuranosa (girada)", size=12, fill=MUTED)
    return f.svg()


def fig_aigua():
    f = Fig(640, 320, "Polaritat de l'aigua i ponts d'hidrogen")
    HB = col("blau")

    def mol(cx, cy, ang, lab=False):
        """ang: direcció (graus) de la bisectriu, dels H. Retorna les posicions dels H."""
        hs = []
        for d in (-52.25, 52.25):
            a = math.radians(ang + d)
            hs.append((cx + 36 * math.cos(a), cy + 36 * math.sin(a)))
        for hx, hy in hs:
            f.line(cx, cy, hx, hy, sw=6, stroke="#8c96a3")
        f.circle(cx, cy, 19, fill="#e05a4f", stroke="#a3332a", sw=1.5)
        f.text(cx, cy, "O", size=14, weight=700, fill="#fff")
        for hx, hy in hs:
            f.circle(hx, hy, 10, fill="#fff", stroke="#5b636e", sw=1.5)
            f.text(hx, hy, "H", size=11, weight=700)
        if lab:
            for hx, hy in hs:
                a2 = math.atan2(hy - cy, hx - cx)
                f.text(hx + 22 * math.cos(a2 + 0.6), hy + 22 * math.sin(a2 + 0.6), "δ+", size=14, weight=700, fill=HB)
            a3 = math.radians(ang + 180)
            f.text(cx + 34 * math.cos(a3), cy + 34 * math.sin(a3), "δ−", size=14, weight=700, fill="#b03a2e")
        return hs

    cx, cy = 240, 170
    hs = mol(cx, cy, 0, lab=True)
    # els H centrals apunten a l'O de dues molècules veïnes
    for (hx, hy) in hs:
        a = math.atan2(hy - cy, hx - cx)
        ox, oy = cx + 120 * math.cos(a), cy + 120 * math.sin(a)
        f.line(hx + 11 * math.cos(a), hy + 11 * math.sin(a), ox - 20 * math.cos(a), oy - 20 * math.sin(a), stroke=HB, sw=2.2, dash="5 4")
        mol(ox, oy, math.degrees(a) + (60 if a < 0 else -60))
    # l'O central accepta els H de dues molècules més
    for ang in (-130, 130):
        a = math.radians(ang)
        hx, hy = cx + 70 * math.cos(a), cy + 70 * math.sin(a)   # H de la molècula veïna
        f.line(cx + 20 * math.cos(a), cy + 20 * math.sin(a), hx - 10 * math.cos(a), hy - 10 * math.sin(a), stroke=HB, sw=2.2, dash="5 4")
        # O veí: a 36 del seu H, en la mateixa direcció
        ox, oy = hx + 36 * math.cos(a), hy + 36 * math.sin(a)
        mol(ox, oy, math.degrees(a) + 180 + 52.25)
    f.text(cx + 62, cy, "104,5°", size=12, fill=MUTED)
    lx = 470
    f.circle(lx, 80, 11, fill="#e05a4f", stroke="#a3332a"); f.text(lx + 20, 80, "oxigen (δ−)", size=14, anchor="start")
    f.circle(lx, 115, 9, fill="#fff", stroke=MUTED); f.text(lx + 20, 115, "hidrogen (δ+)", size=14, anchor="start")
    f.line(lx - 12, 150, lx + 10, 150, sw=6, stroke="#8c96a3"); f.text(lx + 20, 150, "enllaç covalent", size=14, anchor="start")
    f.line(lx - 12, 185, lx + 10, 185, sw=2.2, dash="5 4", stroke=HB); f.text(lx + 20, 185, "pont d’hidrogen", size=14, anchor="start")
    f.text(lx - 12, 245, "Cada molècula pot fer fins\na 4 ponts d’hidrogen:\n2 pels H i 2 per l’O.", size=13, anchor="start", fill=MUTED)
    return f.svg()


def zig(f, x, y, n, step=16, amp=7, color=INK, kink=None):
    pts = []
    xx, yy = x, y
    for i in range(n + 1):
        pts.append((xx, yy + (amp if i % 2 else 0)))
        xx += step
    d = "M" + " L".join(f"{a},{b}" for a, b in pts)
    f.path(d, stroke=color, sw=2)
    return pts[-1]


def fig_lipids():
    f = Fig(640, 360, "Triacilglicerol i fosfolípid")
    # triacilglicerol
    f.text(160, 24, "Triacilglicerol", size=16, weight=700, fill=col("taronja"))
    f.text(160, 44, "reserva · apolar · saponificable", size=13, fill=MUTED)
    f.box(30, 80, 70, 170, "glicerol", color="groc", size=14)
    for i, yy in enumerate((105, 165, 225)):
        f.rect(100, yy - 11, 46, 22, fill=light("vermell"), stroke=col("vermell"), rx=5)
        f.text(123, yy, "èster", size=11, weight=700, fill=col("vermell"))
        zig(f, 146, yy - 3, 9, step=14, amp=7, color=col("marro"))
    f.text(220, 285, "3 àcids grassos", size=13, fill=col("marro"), weight=700)
    # fosfolípid
    X = 360
    f.text(X + 130, 24, "Fosfolípid", size=16, weight=700, fill=col("blau"))
    f.text(X + 130, 44, "membranes · amfipàtic", size=13, fill=MUTED)
    f.circle(X + 40, 95, 26, fill=light("blau"), stroke=col("blau"), sw=2)
    f.text(X + 40, 88, "grup", size=11, weight=700); f.text(X + 40, 102, "polar", size=11, weight=700)
    f.box(X + 18, 132, 44, 30, "P", color="lila", size=15)
    f.box(X + 10, 172, 60, 100, "glicerol", color="groc", size=12)
    for yy in (200, 250):
        zig(f, X + 70, yy - 3, 11, step=14, amp=7, color=col("marro"))

    f.rect(X - 6, 60, 92, 112, fill="none", stroke=col("blau"), dash="5 4", rx=10)
    f.text(X + 40, 186 + 112, "cap hidròfil", size=12, fill=col("blau"), weight=700)
    f.text(X + 160, 290, "cues hidròfobes", size=12, fill=col("marro"), weight=700)
    # bicapa petita
    by = 322
    f.text(X + 40, by + 20, "en aigua → bicapa", size=12, fill=MUTED)
    for i in range(7):
        bx = X + 120 + i * 18
        f.circle(bx, by - 8, 6, fill=light("blau"), stroke=col("blau"))
        f.line(bx - 2, by - 2, bx - 2, by + 10, stroke=col("marro")); f.line(bx + 2, by - 2, bx + 2, by + 10, stroke=col("marro"))
        f.line(bx - 2, by + 14, bx - 2, by + 26, stroke=col("marro")); f.line(bx + 2, by + 14, bx + 2, by + 26, stroke=col("marro"))
        f.circle(bx, by + 32, 6, fill=light("blau"), stroke=col("blau"))
    return f.svg()


def fig_aminoacid():
    f = Fig(640, 300, "Aminoàcid en forma de zwitterió i formació de l'enllaç peptídic")
    f.text(130, 22, "Aminoàcid a pH ≈ 7 (zwitterió)", size=15, weight=700, fill=col("teal"))
    cx, cy = 130, 120
    f.text(cx, cy, "C", size=20, weight=700)
    f.text(cx, cy - 18, "α", size=11, fill=MUTED)
    f.line(cx - 12, cy, cx - 48, cy); f.text(cx - 75, cy, "H₃N⁺", size=18, weight=700, fill=col("blau"))
    f.line(cx + 12, cy, cx + 48, cy); f.text(cx + 75, cy, "COO⁻", size=18, weight=700, fill="#b03a2e")
    f.line(cx, cy + 12, cx, cy + 40); f.text(cx, cy + 54, "R", size=18, weight=700, fill=col("lila"))
    f.line(cx, cy - 12, cx, cy - 36); f.text(cx, cy - 46, "H", size=16, weight=700)
    f.text(cx, cy + 90, "grup amino protonat · carboxil desprotonat\nla cadena lateral R distingeix els 20 aminoàcids", size=12, fill=MUTED)
    # enllaç peptídic
    X = 300
    f.text(X + 165, 22, "Enllaç peptídic (condensació)", size=15, weight=700, fill=col("teal"))
    y = 95
    f.text(X + 20, y, "…–C", size=17, weight=700, anchor="start")
    f.text(X + 62, y - 30, "O", size=17, weight=700, fill="#b03a2e"); f.line(X + 58, y - 12, X + 58, y - 22, sw=1.6); f.line(X + 64, y - 12, X + 64, y - 22, sw=1.6)
    f.text(X + 75, y, "–OH  +  H–", size=17, weight=700, anchor="start")
    f.text(X + 172, y, "N–C–…", size=17, weight=700, anchor="start")
    f.text(X + 172, y + 30, "H", size=17, weight=700); f.line(X + 172, y + 11, X + 172, y + 20)
    f.rect(X + 74, y - 14, 92, 28, fill="none", stroke=col("taronja"), dash="4 3", rx=6)
    f.text(X + 120, y + 30, "surt H₂O", size=12, fill=col("taronja"), weight=700)
    f.arrow(X + 165, y + 50, X + 165, y + 82, color=INK)
    y2 = 200
    f.text(X + 70, y2, "…–C–N–…", size=19, weight=700, anchor="start")
    f.text(X + 96, y2 - 32, "O", size=17, weight=700, fill="#b03a2e"); f.line(X + 93, y2 - 12, X + 93, y2 - 22); f.line(X + 99, y2 - 12, X + 99, y2 - 22)
    f.text(X + 124, y2 + 30, "H", size=17, weight=700); f.line(X + 124, y2 + 11, X + 124, y2 + 20)
    f.rect(X + 84, y2 - 46, 56, 92, fill="none", stroke=col("teal"), sw=2, rx=10)
    f.text(X + 230, y2 - 10, "amida plana:\ncaràcter parcial\nde doble enllaç,\nno gira", size=12, fill=MUTED, anchor="start")
    f.text(X + 165, 280, "La cadena s’escriu de l’extrem N (amino) a l’extrem C (carboxil).", size=12, fill=MUTED)
    return f.svg()


def fig_proteina():
    f = Fig(640, 300, "Els quatre nivells d'estructura d'una proteïna")
    titles = [("Primària", "seqüència\n(enllaços peptídics)"), ("Secundària", "hèlix α i full β\n(ponts d’H de l’esquelet)"),
              ("Terciària", "plegament d’una cadena\n(interaccions de les R)"), ("Quaternària", "diverses cadenes\n(p. ex. hemoglobina)")]
    for i, (t, sub) in enumerate(titles):
        x = 10 + i * 157
        f.rect(x, 40, 148, 190, fill="#fafbfc", stroke=LINE, rx=12)
        f.text(x + 74, 22, t, size=15, weight=700, fill=col("teal"))
        f.text(x + 74, 262, sub, size=12, fill=MUTED)
    # primària
    cols = ["verd", "blau", "taronja", "lila", "vermell", "teal", "groc"]
    for j in range(7):
        bx, by = 32 + (j % 4) * 34, 90 + (j // 4) * 70
        if j < 6:
            nx, ny = 32 + ((j + 1) % 4) * 34, 90 + ((j + 1) // 4) * 70
            f.line(bx, by, nx, ny, stroke=MUTED, sw=2)
        f.circle(bx, by, 13, fill=light(cols[j]), stroke=col(cols[j]), sw=1.8)
        f.text(bx, by, "AGLKVDS"[j], size=12, weight=700)
    f.text(40, 195, "N", size=12, weight=700, fill=MUTED); f.text(130, 195, "C", size=12, weight=700, fill=MUTED)
    # secundària: hèlix i full
    x = 167
    d = "M" + " ".join(f"{x+20+ t*1.6},{70+14*math.sin(t/4.2)}" for t in range(0, 70))
    f.path(d, stroke=col("vermell"), sw=3)
    f.text(x + 74, 100, "hèlix α", size=12, fill=col("vermell"), weight=700)
    for k in range(3):
        yy = 135 + k * 26
        f.arrow(x + 22 if k != 1 else x + 128, yy, x + 128 if k != 1 else x + 22, yy, color=col("groc"), sw=7)
    f.text(x + 74, 214, "full β", size=12, fill=col("groc"), weight=700)
    # terciària
    x = 324
    f.path(f"M{x+20},{180} C{x+10},{80} {x+80},{60} {x+100},{100} S{x+150},{170} {x+90},{185} S{x+40},{120} {x+70},{110} S{x+120},{140} {x+110},{200}", stroke=col("lila"), sw=3.5)
    f.line(x + 62, 150, x + 98, 150, stroke=col("groc"), sw=2, dash="3 3")
    f.text(x + 80, 165, "S–S", size=11, fill=col("groc"), weight=700)
    # quaternària
    x = 481
    for (dx, dy, c) in [(45, 95, "vermell"), (105, 95, "blau"), (45, 160, "blau"), (105, 160, "vermell")]:
        f.circle(x + dx, dy, 28, fill=light(c), stroke=col(c), sw=2)
        f.circle(x + dx + 6, dy - 4, 6, fill=col("vermell") if c == "vermell" else col("blau"), stroke="none")
    f.text(x + 74, 210, "4 cadenes, 4 grups hemo", size=11, fill=MUTED)
    return f.svg()


def fig_nucleotid():
    f = Fig(640, 380, "Nucleòtid i doble hèlix antiparal·lela")
    # nucleòtid
    f.text(130, 22, "Nucleòtid", size=16, weight=700, fill=col("teal"))
    f.circle(50, 110, 24, fill=light("groc"), stroke=col("groc"), sw=2); f.text(50, 110, "P", size=16, weight=700)
    f.text(50, 146, "fosfat", size=12, fill=MUTED)
    pent = [(110, 92), (148, 82), (172, 112), (152, 145), (112, 140)]
    f.poly(pent, fill=light("vermell"), stroke=col("vermell"), sw=2)
    f.text(140, 116, "pentosa", size=12, weight=700)
    f.line(74, 110, 104, 98, sw=2)
    f.text(98, 80, "5′", size=11, fill=MUTED, weight=700)
    f.text(124, 160, "3′", size=11, fill=MUTED, weight=700)
    f.text(176, 135, "1′", size=11, fill=MUTED, weight=700)
    f.line(170, 108, 196, 96, sw=2)
    f.rect(196, 72, 70, 40, fill=light("blau"), stroke=col("blau"), sw=2, rx=6); f.text(231, 92, "base", size=13, weight=700)
    f.text(140, 200, "DNA: desoxiribosa (sense OH al C2′)\nRNA: ribosa", size=12, fill=MUTED)
    f.text(140, 250, "Púriques (2 anells): A, G\nPirimidíniques (1 anell): C, T, U", size=12, fill=MUTED)
    # doble cadena
    X = 330
    f.text(X + 145, 22, "Doble hèlix (desplegada)", size=16, weight=700, fill=col("teal"))
    f.text(X + 30, 50, "5′", size=14, weight=700, fill=col("blau")); f.text(X + 260, 50, "3′", size=14, weight=700, fill=col("vermell"))
    f.text(X + 30, 350, "3′", size=14, weight=700, fill=col("blau")); f.text(X + 260, 350, "5′", size=14, weight=700, fill=col("vermell"))
    f.line(X + 30, 62, X + 30, 338, stroke=col("blau"), sw=5)
    f.line(X + 260, 62, X + 260, 338, stroke=col("vermell"), sw=5)
    f.arrow(X + 14, 90, X + 14, 310, color=col("blau"), sw=1.6)
    f.arrow(X + 276, 310, X + 276, 90, color=col("vermell"), sw=1.6)
    pairs = [("A", "T"), ("G", "C"), ("T", "A"), ("C", "G"), ("A", "T")]
    for k, (a, b) in enumerate(pairs):
        y = 90 + k * 55
        n = 3 if a in "GC" else 2
        f.rect(X + 36, y - 15, 70, 30, fill=light("blau"), stroke=col("blau"), rx=5); f.text(X + 71, y, a, size=15, weight=700)
        f.rect(X + 184, y - 15, 70, 30, fill=light("vermell"), stroke=col("vermell"), rx=5); f.text(X + 219, y, b, size=15, weight=700)
        for m in range(n):
            yy = y + (m - (n - 1) / 2) * 7
            f.line(X + 110, yy, X + 180, yy, stroke=MUTED, sw=1.3, dash="4 3")
        f.text(X + 145, y + 19, f"{n} ponts d’H", size=10, fill=MUTED)
    return f.svg()


def fig_vs(variant="tres"):
    """Velocitat inicial en funció de [S]: sense inhibidor, competitiu i no competitiu."""
    f = Fig(640, 360, "Velocitat d'un enzim en funció de la concentració de substrat")
    x0, y0, W, H = 80, 300, 500, 240
    f.line(x0, y0, x0 + W, y0, sw=1.8); f.line(x0, y0, x0, y0 - H, sw=1.8)
    f.text(x0 + W / 2, y0 + 34, "concentració de substrat, [S]", size=14)
    f.text(x0 - 46, y0 - H / 2, "velocitat inicial, v", size=14, rot=-90)

    def curve(vmax, km, color, dash=None):
        pts = []
        for i in range(0, 101):
            s = i / 100 * 10
            v = vmax * s / (km + s)
            pts.append((x0 + s / 10 * W, y0 - v / 100 * H))
        f.path("M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts), stroke=color, sw=3, dash=dash)

    curve(90, 1, col("verd"))
    if variant == "tres":
        curve(90, 3.5, col("blau"), dash="8 5")
        curve(50, 1, col("vermell"), dash="2 5")
        # Vmax
        f.line(x0, y0 - 0.9 * H, x0 + W, y0 - 0.9 * H, stroke=LINE, dash="3 4", sw=1.2)
        f.text(x0 + W - 4, y0 - 0.9 * H - 12, "V_{max}", size=13, anchor="end", fill=MUTED)
        f.line(x0, y0 - 0.45 * H, x0 + 0.1 * W, y0 - 0.45 * H, stroke=col("verd"), dash="3 3", sw=1.2)
        f.line(x0 + 0.1 * W, y0, x0 + 0.1 * W, y0 - 0.45 * H, stroke=col("verd"), dash="3 3", sw=1.2)
        f.text(x0 + 0.1 * W, y0 + 14, "K_{m}", size=12, fill=col("verd"), weight=700)
        f.line(x0 + 0.35 * W, y0, x0 + 0.35 * W, y0 - 0.45 * H, stroke=col("blau"), dash="3 3", sw=1.2)
        f.text(x0 + 0.35 * W, y0 + 14, "K_{m} aparent", size=12, fill=col("blau"), weight=700)
        f.text(x0 - 8, y0 - 0.45 * H, "V_{max}/2", size=11, anchor="end", fill=MUTED)
        lx, ly = x0 + 300, y0 - 120
        for k, (c, d, t) in enumerate([("verd", None, "sense inhibidor"), ("blau", "8 5", "competitiu: V_{max} igual"), ("vermell", "2 5", "no competitiu: V_{max} baixa")]):
            f.line(lx, ly + k * 24, lx + 30, ly + k * 24, stroke=col(c), sw=3, dash=d)
            f.text(lx + 38, ly + k * 24, t, size=13, anchor="start")
    else:
        curve(50, 1, col("vermell"), dash="2 5")
        f.text(x0 + W - 4, y0 - 0.86 * H - 14, "sense fàrmac", size=13, anchor="end", fill=col("verd"), weight=700)
        f.text(x0 + W - 4, y0 - 0.48 * H - 14, "amb fàrmac", size=13, anchor="end", fill=col("vermell"), weight=700)
    return f.svg()
