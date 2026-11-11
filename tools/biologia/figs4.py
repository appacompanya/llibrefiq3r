"""Figures dels temes 4 a 9 i mapes conceptuals de cada tema."""
import math
from svg import Fig, INK, MUTED, LINE, col, light, textw


# ---------------- genètica ----------------
def punnett(f, x, y, top, left, cells, cw=78, ch=50, colors=None, size=16):
    for j, g in enumerate(top):
        f.rect(x + cw * (j + 1), y, cw, ch, fill="#f3f4f6", stroke=LINE, rx=0)
        f.text(x + cw * (j + 1.5), y + ch / 2, g, size=size, weight=700, fill=col("blau"))
    for i, g in enumerate(left):
        f.rect(x, y + ch * (i + 1), cw, ch, fill="#f3f4f6", stroke=LINE, rx=0)
        f.text(x + cw / 2, y + ch * (i + 1.5), g, size=size, weight=700, fill=col("vermell"))
        for j in range(len(top)):
            c = colors[i][j] if colors else None
            f.rect(x + cw * (j + 1), y + ch * (i + 1), cw, ch, fill=light(c) if c else "#fff", stroke=LINE, rx=0)
            f.text(x + cw * (j + 1.5), y + ch * (i + 1.5), cells[i][j], size=size, weight=700)


def fig_punnett_mono():
    f = Fig(640, 250, "Quadre de Punnett d'Aa × Aa")
    f.text(170, 22, "Aa × Aa", size=17, weight=700, fill=col("teal"))
    punnett(f, 50, 45, ["A", "a"], ["A", "a"], [["AA", "Aa"], ["Aa", "aa"]], cw=80, ch=56,
            colors=[["verd", "verd"], ["verd", "groc"]], size=18)
    x = 340
    f.text(x, 70, "Gàmetes: ½ A i ½ a de cada progenitor", size=13, anchor="start")
    f.text(x, 110, "Genotips  1 AA : 2 Aa : 1 aa", size=14, weight=700, anchor="start")
    f.rect(x, 140, 18, 18, fill=light("verd"), stroke=col("verd"), rx=3); f.text(x + 26, 149, "fenotip dominant: ¾", size=14, anchor="start")
    f.rect(x, 172, 18, 18, fill=light("groc"), stroke=col("groc"), rx=3); f.text(x + 26, 181, "fenotip recessiu: ¼", size=14, anchor="start")
    f.text(x, 220, "Amb dominància completa → 3 : 1", size=14, weight=700, anchor="start", fill=col("teal"))
    return f.svg()


def fig_punnett_di():
    f = Fig(640, 380, "Dihibridisme AaBb × AaBb")
    g = ["AB", "Ab", "aB", "ab"]
    cells, colors = [], []
    ph = {"AB": "verd", "Ab": "blau", "aB": "taronja", "ab": "groc"}
    for a in g:
        row, rc = [], []
        for b in g:
            A = "A" if "A" in a + b else "a"
            B = "B" if "B" in a + b else "b"
            gen = "".join(sorted(a[0] + b[0], key=lambda c: (c.lower(), c.islower()))) + "".join(sorted(a[1] + b[1], key=lambda c: (c.lower(), c.islower())))
            row.append(gen); rc.append(ph[A + B])
        cells.append(row); colors.append(rc)
    f.text(220, 20, "AaBb × AaBb (gens independents)", size=16, weight=700, fill=col("teal"))
    punnett(f, 20, 40, g, g, cells, cw=78, ch=62, colors=colors, size=15)
    x = 440
    for k, (c, t) in enumerate([("verd", "A_B_  9/16"), ("blau", "A_bb  3/16"), ("taronja", "aaB_  3/16"), ("groc", "aabb  1/16")]):
        f.rect(x, 90 + k * 40, 22, 22, fill=light(c), stroke=col(c), rx=4)
        f.text(x + 32, 101 + k * 40, t, size=15, weight=700, anchor="start")
    f.text(x, 280, "9 : 3 : 3 : 1", size=20, weight=700, anchor="start", fill=col("teal"))
    f.text(x, 330, "= (3 : 1) × (3 : 1)\nnomés si els gens són\nindependents i hi ha\ndominància completa", size=13, anchor="start", fill=MUTED)
    return f.svg()


def fig_punnett_x():
    f = Fig(640, 260, "Herència recessiva lligada al cromosoma X")
    f.text(170, 22, "Xᴴ Xʰ (portadora) × Xᴴ Y (sa)", size=15, weight=700, fill=col("teal"))
    punnett(f, 40, 45, ["Xᴴ", "Y"], ["Xᴴ", "Xʰ"], [["Xᴴ Xᴴ", "Xᴴ Y"], ["Xᴴ Xʰ", "Xʰ Y"]], cw=90, ch=56,
            colors=[["verd", "verd"], ["groc", "vermell"]], size=16)
    x = 360
    f.text(x, 60, "Pare (columnes) · mare (files)", size=12, anchor="start", fill=MUTED)
    for k, (c, t) in enumerate([("verd", "sans"), ("groc", "filla portadora"), ("vermell", "fill afectat")]):
        f.rect(x, 90 + k * 34, 20, 20, fill=light(c), stroke=col(c), rx=4)
        f.text(x + 30, 100 + k * 34, t, size=14, anchor="start")
    f.text(x, 210, "Fills homes: ½ afectats\nFilles: cap afectada, ½ portadores", size=13, weight=700, anchor="start")
    return f.svg()


def fig_pedigri():
    f = Fig(640, 345, "Pedigrí compatible amb herència autosòmica recessiva")
    s = 34

    def male(x, y, aff=False, carrier=False):
        f.rect(x - s / 2, y - s / 2, s, s, fill=INK if aff else "#fff", stroke=INK, sw=2, rx=2)
        if carrier:
            f.circle(x, y, 5, fill=INK, stroke="none")

    def female(x, y, aff=False, carrier=False):
        f.circle(x, y, s / 2, fill=INK if aff else "#fff", stroke=INK, sw=2)
        if carrier:
            f.circle(x, y, 5, fill=INK, stroke="none")
    # I
    male(200, 50); female(300, 50); f.line(217, 50, 283, 50, sw=2)
    f.line(250, 50, 250, 90, sw=2); f.line(150, 90, 400, 90, sw=2)
    # II
    for x, kind in ((150, "m"), (250, "f"), (400, "m")):
        f.line(x, 90, x, 133, sw=2)
    male(150, 150); female(250, 150); male(400, 150, carrier=True)
    female(500, 150, carrier=True); f.line(417, 150, 483, 150, sw=2)
    f.line(450, 150, 450, 200, sw=2); f.line(390, 200, 510, 200, sw=2)
    for x in (390, 450, 510):
        f.line(x, 200, x, 233, sw=2)
    male(390, 250); female(450, 250, aff=True); male(510, 250)
    for x, y, t in ((200, 50, "1"), (300, 50, "2"), (150, 150, "1"), (250, 150, "2"), (400, 150, "3"), (500, 150, "4"),
                    (390, 250, "1"), (450, 250, "2"), (510, 250, "3")):
        f.text(x, y + 30, t, size=11, fill=MUTED)
    for y, t in ((50, "I"), (150, "II"), (250, "III")):
        f.text(40, y, t, size=16, weight=700, fill=MUTED)
    lx = 560
    f.rect(lx - 10, 40, 16, 16, fill="#fff", stroke=INK, rx=1); f.text(lx + 14, 48, "home", size=12, anchor="start")
    f.circle(lx - 2, 74, 8, fill="#fff", stroke=INK); f.text(lx + 14, 74, "dona", size=12, anchor="start")
    f.rect(lx - 10, 92, 16, 16, fill=INK, stroke=INK, rx=1); f.text(lx + 14, 100, "afectat", size=12, anchor="start")
    f.circle(lx - 2, 128, 8, fill="#fff", stroke=INK); f.circle(lx - 2, 128, 3, fill=INK, stroke="none"); f.text(lx + 14, 128, "portador\n(deduït)", size=12, anchor="start")
    f.text(320, 318, "II-3 i II-4 no estan afectats però tenen una filla afectada (III-2): tots dos són portadors obligats.\nLa resta d’individus no afectats poden ser portadors o no (no es pot deduir).", size=12, fill=MUTED)
    return f.svg()


def fig_lligament():
    f = Fig(640, 270, "Gens lligats: gàmetes parentals i recombinants")

    def cr(x, y, a, b, ca, cb):
        f.rect(x - 8, y - 70, 16, 140, fill=light(ca), stroke=col(ca), sw=1.6, rx=8)
        f.line(x - 12, y - 30, x + 12, y - 30, stroke=INK, sw=2); f.text(x + 18, y - 30, a, size=14, weight=700, anchor="start")
        f.line(x - 12, y + 30, x + 12, y + 30, stroke=INK, sw=2); f.text(x + 18, y + 30, b, size=14, weight=700, anchor="start")
    f.text(110, 22, "Dihíbrid en cis (AB/ab)", size=14, weight=700, fill=col("teal"))
    cr(80, 130, "A", "B", "blau", "blau"); cr(140, 130, "a", "b", "vermell", "vermell")
    f.path("M75,140 C100,150 125,130 150,140", stroke=col("groc"), sw=3)
    f.text(110, 220, "entrecreuament\nentre els dos loci", size=12, fill=col("groc"), weight=700)
    f.arrow(200, 130, 260, 130, color=MUTED)
    x0 = 300
    gam = [("A", "B", "blau", "blau", "parental"), ("a", "b", "vermell", "vermell", "parental"),
           ("A", "b", "blau", "vermell", "recombinant"), ("a", "B", "vermell", "blau", "recombinant")]
    for k, (a, b, ca, cb, t) in enumerate(gam):
        x = x0 + k * 85
        f.rect(x - 8, 60, 16, 70, fill=light(ca), stroke=col(ca), sw=1.6, rx=8)
        f.rect(x - 8, 130, 16, 70, fill=light(cb), stroke=col(cb), sw=1.6, rx=8)
        f.text(x + 18, 100, a, size=14, weight=700, anchor="start"); f.text(x + 18, 160, b, size=14, weight=700, anchor="start")
        f.text(x + 8, 225, t, size=12, weight=700, fill=col("teal") if t == "parental" else col("groc"))
    f.text(320, 255, "Freqüència de recombinació = recombinants / total · 1 % = 1 cM", size=12, fill=MUTED)
    return f.svg()


# ---------------- genètica molecular ----------------
def fig_dogma():
    f = Fig(640, 200, "Flux de la informació genètica")
    f.box(20, 70, 110, 60, "DNA", color="blau", size=20)
    f.box(265, 70, 110, 60, "RNA", color="vermell", size=20)
    f.box(510, 70, 110, 60, "proteïna", color="verd", size=18)
    f.arrow(132, 90, 263, 90, color=INK, sw=2.4); f.text(197, 78, "transcripció", size=12, weight=700)
    f.arrow(263, 112, 132, 112, color=col("taronja"), sw=2.2, dash="6 4"); f.text(197, 128, "retrotranscripció", size=12, weight=700, fill=col("taronja"))
    f.arrow(377, 100, 508, 100, color=INK, sw=2.4); f.text(442, 86, "traducció", size=12, weight=700)
    f.arrowpath("M50,68 C30,10 120,10 100,68", color=INK, sw=2.2); f.text(124, 30, "replicació", anchor="start", size=12, weight=700)
    f.arrowpath("M295,68 C275,10 365,10 345,68", color=col("taronja"), sw=1.8, dash="6 4"); f.text(369, 30, "replicació de l’RNA (alguns virus)", anchor="start", size=11, weight=700, fill=col("taronja"))
    f.text(320, 175, "Línies discontínues: només en virus (retrovirus, virus RNA). La proteïna no torna mai a àcid nucleic.", size=12, fill=MUTED)
    return f.svg()


def fig_transcripcio():
    f = Fig(690, 250, "Cadena motlle, cadena codificant i RNA missatger")
    mono = 'font-family="ui-monospace,Menlo,Consolas,monospace"'
    rows = [("cadena codificant", "5′– A T G T T T G G A T A A –3′", "blau"),
            ("cadena motlle", "3′– T A C A A A C C T A T T –5′", "vermell"),
            ("RNA missatger", "5′– A U G U U U G G A U A A –3′", "lila")]
    for k, (lab, seq, c) in enumerate(rows):
        y = 50 + k * 60
        f.text(150, y, lab, size=14, weight=700, fill=col(c), anchor="end")
        f.raw(f'<text x="170" y="{y}" font-size="19" {mono} fill="{col(c)}" font-weight="700" dominant-baseline="central">{seq}</text>')
    f.arrow(170, 130, 520, 130, color=col("vermell"), sw=1.4, dash="3 3")
    f.text(345, 145, "l’RNA-polimerasa llegeix el motlle 3′→5′", size=12, fill=col("vermell"))
    cw = 19 * 0.6
    for k, aa in enumerate(["Met", "Phe", "Gly", "stop"]):
        xc = 170 + cw * (4 + 6 * k + 2.5)
        f.line(xc - 2.5 * cw, 200, xc + 2.5 * cw, 200, stroke=col("lila"), sw=1.6)
        f.raw(f'<text x="{xc:.1f}" y="225" font-size="16" {mono} fill="{INK}" font-weight="700" text-anchor="middle" dominant-baseline="central">{aa}</text>')
    f.text(150, 225, "proteïna", size=14, weight=700, anchor="end")
    f.text(570, 50, "igual que l’RNA\n(T en lloc d’U)", size=11, fill=MUTED, anchor="start")
    f.text(570, 170, "complementari\ndel motlle", size=11, fill=MUTED, anchor="start")
    return f.svg()


def fig_trna():
    f = Fig(640, 360, "RNA de transferència en forma de trèvol")
    cx = 250
    f.rect(cx - 12, 30, 24, 120, fill=light("blau"), stroke=col("blau"), sw=2, rx=6)
    f.text(cx + 40, 40, "extrem 3′ (–CCA):\nhi s’uneix l’aminoàcid", size=12, anchor="start")
    f.circle(cx, 22, 13, fill=light("verd"), stroke=col("verd"), sw=2); f.text(cx, 22, "aa", size=11, weight=700)
    f.circle(cx - 110, 170, 42, fill=light("lila"), stroke=col("lila"), sw=2); f.text(cx - 110, 170, "braç D", size=12, weight=700)
    f.circle(cx + 110, 170, 42, fill=light("lila"), stroke=col("lila"), sw=2); f.text(cx + 110, 170, "braç T", size=12, weight=700)
    f.line(cx - 68, 170, cx - 12, 160, sw=3, stroke=col("blau")); f.line(cx + 68, 170, cx + 12, 160, sw=3, stroke=col("blau"))
    f.rect(cx - 12, 150, 24, 90, fill=light("blau"), stroke=col("blau"), sw=2, rx=6)
    f.circle(cx, 285, 46, fill=light("taronja"), stroke=col("taronja"), sw=2)
    f.text(cx, 278, "anticodó", size=12, weight=700)
    f.text(cx, 298, "3′–UAC–5′", size=14, weight=700, fill=col("vermell"))
    f.text(cx, 348, "s’aparella amb el codó 5′–AUG–3′ de l’RNAm", size=12, fill=MUTED)
    x = 430
    f.text(x, 140, "Cada aminoàcid s’uneix al\nseu RNAt per una\naminoacil-RNAt-sintetasa\n(gasta ATP).", size=13, anchor="start")
    f.text(x, 250, "L’aparellament codó–anticodó\nés antiparal·lel.", size=13, anchor="start", fill=MUTED)
    return f.svg()


def fig_traduccio():
    f = Fig(640, 320, "Traducció al ribosoma")
    f.ellipse(320, 105, 190, 75, fill="#efe6d6", stroke=col("marro"), sw=2)
    f.text(320, 46, "subunitat gran", size=12, fill=col("marro"), weight=700)
    f.ellipse(320, 225, 190, 45, fill="#f6efe2", stroke=col("marro"), sw=2)
    f.text(320, 258, "subunitat petita", size=12, fill=col("marro"), weight=700)
    mono = 'font-family="ui-monospace,Menlo,Consolas,monospace"'
    f.line(60, 200, 600, 200, stroke=col("lila"), sw=4)
    f.text(40, 200, "5′", size=13, weight=700, fill=col("lila")); f.text(620, 200, "3′", size=13, weight=700, fill=col("lila"))
    cod = ["AUG", "GCA", "UUU", "GGA", "UAA"]
    for k, c in enumerate(cod):
        f.raw(f'<text x="{150+k*85}" y="214" font-size="15" {mono} text-anchor="middle" font-weight="700" fill="{col("lila")}">{c}</text>')
    for lab, x in (("E", 235), ("P", 320), ("A", 405)):
        f.rect(x - 38, 115, 76, 70, fill="none", stroke=LINE, dash="4 3", rx=8)
        f.text(x - 26, 128, lab, size=15, weight=700, fill=col("teal"))
    # tRNA a P i A
    for x, aa, anti in ((320, "Phe", "AAA"), (405, "Gly", "CCU")):
        f.rect(x - 14, 130, 28, 48, fill=light("blau"), stroke=col("blau"), sw=1.6, rx=6)
        f.text(x, 190, anti, size=10, weight=700, fill=col("blau"))
    # cadena
    for k, (aa, c) in enumerate([("Met", "verd"), ("Ala", "taronja"), ("Phe", "blau")]):
        f.circle(250 + k * 33, 95 - (2 - k) * 0, 15, fill=light(c), stroke=col(c), sw=1.6); f.text(250 + k * 33, 95, aa, size=10, weight=700)
    f.line(316, 110, 320, 128, stroke=MUTED); f.circle(405, 108, 15, fill=light("lila"), stroke=col("lila")); f.text(405, 108, "Gly", size=10, weight=700)
    f.line(405, 123, 405, 128, stroke=MUTED)
    f.arrow(530, 40, 610, 40, color=INK); f.text(520, 40, "el ribosoma avança", size=12, anchor="end")
    f.text(320, 300, "E: surt l’RNAt buit · P: porta la cadena · A: entra l’RNAt carregat", size=12, fill=MUTED)
    return f.svg()


def fig_forquilla():
    f = Fig(640, 335, "Forquilla de replicació")
    # motlle obert
    f.line(20, 165, 230, 165, stroke=col("blau"), sw=5); f.line(20, 177, 230, 177, stroke=col("vermell"), sw=5)
    f.text(20, 150, "5′", size=12, weight=700, fill=col("blau")); f.text(20, 195, "3′", size=12, weight=700, fill=col("vermell"))
    f.path("M230,165 C280,160 330,100 620,90", stroke=col("blau"), sw=5)
    f.path("M230,177 C280,182 330,240 620,250", stroke=col("vermell"), sw=5)
    f.text(630, 90, "3′", size=12, weight=700, fill=col("blau")); f.text(630, 250, "5′", size=12, weight=700, fill=col("vermell"))
    f.ellipse(235, 171, 22, 30, fill=light("groc"), stroke=col("groc"), sw=2); f.text(235, 171, "Hel", size=11, weight=700)
    f.text(235, 215, "helicasa", size=11, fill=col("groc"), weight=700)
    f.ellipse(130, 171, 16, 22, fill=light("gris"), stroke=col("gris")); f.text(130, 145, "topoisomerasa", size=11, fill=MUTED)
    # cadena líder: sobre el motlle blau (5′ a l'esquerra), creix cap a la forquilla
    f.arrowpath("M600,104 C450,110 330,128 270,158", color=col("verd"), sw=4)
    f.text(450, 70, "cadena líder (contínua)", size=13, weight=700, fill=col("verd"))
    # cadena retardada: sobre el motlle vermell, fragments que s'allunyen de la forquilla
    for x0 in (300, 410, 520):
        yy = 205 + (x0 - 300) * 0.12
        f.rect(x0, yy - 3, 14, 6, fill=col("vermell"), stroke="none", rx=2)
        f.arrow(x0 + 14, yy, x0 + 92, yy + 6, color=col("verd"), sw=4)
    f.text(450, 290, "cadena retardada: fragments d’Okazaki", size=13, weight=700, fill=col("verd"))
    f.text(300, 236, "encebador\nd’RNA", size=11, fill=col("vermell"), weight=700)
    f.text(320, 318, "La DNA-polimerasa només allarga 5′→3′. La ligasa uneix els fragments.", size=12, fill=MUTED)
    f.arrow(150, 260, 60, 260, color=MUTED); f.text(155, 260, "avanç de la forquilla", size=11, fill=MUTED, anchor="start")
    return f.svg()


def fig_operon():
    f = Fig(640, 360, "L'operó lac")
    y = 70
    parts = [("lacI", 30, 70, "gris"), ("P", 130, 40, "verd"), ("O", 170, 40, "vermell"), ("lacZ", 210, 120, "blau"), ("lacY", 330, 110, "blau"), ("lacA", 440, 100, "blau")]
    f.line(10, y, 560, y, sw=3)
    for t, x, w, c in parts:
        f.rect(x, y - 18, w, 36, fill=light(c), stroke=col(c), sw=1.8, rx=4); f.text(x + w / 2, y, t, size=13, weight=700)
    f.text(130, 30, "promotor", size=11, fill=col("verd")); f.text(190, 30, "operador", size=11, fill=col("vermell"))
    f.text(375, 30, "gens estructurals", size=11, fill=col("blau"))
    # sense lactosa
    y2 = 170
    f.text(10, y2 - 40, "Sense lactosa", size=14, weight=700, anchor="start", fill=col("vermell"))
    f.line(10, y2, 560, y2, sw=3)
    for t, x, w, c in parts[1:3]:
        f.rect(x, y2 - 18, w, 36, fill=light(c), stroke=col(c), sw=1.8, rx=4); f.text(x + w / 2, y2, t, size=13, weight=700)
    f.path(f"M165,{y2-14} q25,-40 50,0 z", fill=light("vermell"), stroke=col("vermell"), sw=2)
    f.text(240, y2 - 30, "repressor", size=11, weight=700, fill=col("vermell"), anchor="start")
    f.text(400, y2 - 26, "la RNA-polimerasa no avança:\nno es transcriu", size=12, anchor="middle", fill=MUTED)
    # amb lactosa
    y3 = 300
    f.text(10, y3 - 52, "Amb lactosa (i poca glucosa)", size=14, weight=700, anchor="start", fill=col("verd"))
    f.line(10, y3, 560, y3, sw=3)
    for t, x, w, c in parts[1:]:
        f.rect(x, y3 - 18, w, 36, fill=light(c), stroke=col(c), sw=1.8, rx=4); f.text(x + w / 2, y3, t, size=13, weight=700)
    f.path(f"M420,{y3-24} q25,-40 50,0 z", fill=light("vermell"), stroke=col("vermell"), sw=2)
    f.circle(445, y3 - 30, 7, fill=col("groc"), stroke="none")
    f.text(410, y3 - 42, "repressor + al·lolactosa (inactiu)", size=11, weight=700, fill=col("vermell"), anchor="end")
    f.arrow(210, y3 + 30, 550, y3 + 30, color=col("lila"), sw=3); f.text(380, y3 + 46, "un sol RNAm (policistrònic)", size=12, fill=col("lila"), weight=700)
    f.ellipse(115, y3 + 4, 22, 12, fill=light("groc"), stroke=col("groc")); f.text(115, y3 + 4, "CAP", size=9, weight=700)
    return f.svg()


def fig_recombinant():
    f = Fig(640, 300, "Obtenció de DNA recombinant i clonació molecular")
    steps = [("1", "Tallar", "el gen i el plasmidi\namb el mateix enzim\nde restricció"), ("2", "Unir", "extrems cohesius\n+ DNA-ligasa"),
             ("3", "Transformar", "el bacteri capta\nel plasmidi"), ("4", "Seleccionar", "medi amb antibiòtic;\ncomprovar l’insert")]
    for k, (n, t, s) in enumerate(steps):
        x = 15 + k * 157
        f.rect(x, 30, 145, 240, fill="#fafbfc", stroke=LINE, rx=12)
        f.circle(x + 22, 52, 14, fill=col("teal"), stroke="none"); f.text(x + 22, 52, n, size=13, weight=700, fill="#fff")
        f.text(x + 85, 52, t, size=14, weight=700, fill=col("teal"))
        f.text(x + 72, 232, s, size=11, fill=MUTED)
        cx, cy = x + 72, 130
        if k == 0:
            f.circle(cx, cy, 34, stroke=col("blau"), sw=5)
            f.rect(cx + 26, cy - 8, 16, 16, fill="#fff", stroke="none", rx=0)
            f.rect(cx - 50, cy + 52, 100, 10, fill=col("vermell"), stroke="none", rx=3)
            f.text(cx, cy - 50, "✂", size=18)
        elif k == 1:
            f.circle(cx, cy, 34, stroke=col("blau"), sw=5)
            f.path(f"M{cx+30},{cy-16} q14,16 0,32", stroke=col("vermell"), sw=7)
            f.text(cx, cy, "plasmidi\nrecombinant", size=10, weight=700)
        elif k == 2:
            f.rect(cx - 52, cy - 30, 104, 60, fill=light("verd"), stroke=col("verd"), sw=2, rx=30)
            f.circle(cx + 10, cy, 14, stroke=col("blau"), sw=3)
        else:
            f.circle(cx, cy, 46, fill="#fff7e6", stroke=MUTED, sw=2)
            for (dx, dy) in ((-18, -10), (12, -20), (16, 14), (-10, 20)):
                f.circle(cx + dx, cy + dy, 7, fill=light("verd"), stroke=col("verd"))
    for k in range(3):
        f.arrow(15 + k * 157 + 145, 130, 15 + (k + 1) * 157, 130, color=MUTED)
    return f.svg()


def fig_pcr():
    f = Fig(640, 300, "Un cicle de PCR")
    temps = [("Desnaturalització", "94–95 °C", "es separen\nles cadenes", "vermell"), ("Hibridació", "50–65 °C", "els encebadors\ns’uneixen", "blau"), ("Extensió", "72 °C", "la Taq polimerasa\nallarga 5′→3′", "verd")]
    for k, (t, T, s, c) in enumerate(temps):
        x = 20 + k * 205
        f.rect(x, 40, 190, 200, fill=light(c), stroke=col(c), sw=2, rx=14)
        f.text(x + 95, 62, t, size=14, weight=700, fill=col(c))
        f.text(x + 95, 86, T, size=18, weight=700)
        f.text(x + 95, 210, s, size=12, fill=MUTED)
        y = 140
        if k == 0:
            f.line(x + 25, y - 18, x + 165, y - 18, stroke=col("blau"), sw=4); f.line(x + 25, y + 18, x + 165, y + 18, stroke=col("vermell"), sw=4)
        elif k == 1:
            f.line(x + 25, y - 18, x + 165, y - 18, stroke=col("blau"), sw=4); f.line(x + 25, y + 18, x + 165, y + 18, stroke=col("vermell"), sw=4)
            f.line(x + 130, y - 8, x + 160, y - 8, stroke=col("taronja"), sw=5); f.line(x + 30, y + 8, x + 60, y + 8, stroke=col("taronja"), sw=5)
        else:
            f.line(x + 25, y - 18, x + 165, y - 18, stroke=col("blau"), sw=4); f.line(x + 25, y + 18, x + 165, y + 18, stroke=col("vermell"), sw=4)
            f.arrow(x + 160, y - 8, x + 30, y - 8, color=col("verd"), sw=4); f.arrow(x + 30, y + 8, x + 160, y + 8, color=col("verd"), sw=4)
    f.arrow(212, 140, 225, 140, color=MUTED); f.arrow(417, 140, 430, 140, color=MUTED)
    f.arrowpath("M520,245 C520,290 120,290 120,245", color=MUTED, sw=1.8)
    f.text(320, 290, "es repeteix 25–35 vegades: cada cicle dobla el nombre de còpies (2ⁿ)", size=12, fill=MUTED)
    f.text(320, 20, "Encebadors en taronja · nova cadena en verd", size=12, fill=MUTED)
    return f.svg()


def fig_crispr():
    f = Fig(640, 300, "Edició amb CRISPR-Cas9")
    f.ellipse(200, 120, 150, 70, fill=light("lila"), stroke=col("lila"), sw=2)
    f.text(200, 70, "Cas9", size=16, weight=700, fill=col("lila"))
    f.line(70, 130, 330, 130, stroke=col("blau"), sw=4); f.line(70, 150, 330, 150, stroke=col("blau"), sw=4)
    f.path("M120,122 L230,122", stroke=col("vermell"), sw=4)
    f.text(140, 100, "RNA guia", size=12, weight=700, fill=col("vermell"))
    f.rect(235, 154, 34, 12, fill=col("groc"), stroke="none", rx=2); f.text(252, 178, "PAM (NGG)", size=11, fill=col("groc"), weight=700)
    f.text(214, 140, "✂", size=20)
    f.text(200, 210, "talla les dues cadenes\nde la seqüència diana", size=12, fill=MUTED)
    f.arrow(360, 140, 400, 80, color=MUTED); f.arrow(360, 140, 400, 210, color=MUTED)
    f.box(410, 40, 220, 80, "Unió d’extrems no homòloga\nerrors (indels)\n→ gen inactivat", color="taronja", size=12)
    f.box(410, 175, 220, 80, "Reparació per homologia\namb un motlle\n→ canvi precís", color="verd", size=12)
    return f.svg()


# ---------------- evolució ----------------
def fig_seleccio():
    f = Fig(640, 250, "Selecció natural")
    items = [("Variació", "els individus\nno són iguals", "blau"), ("Herència", "part de la variació\nes transmet", "lila"), ("Reproducció\ndiferencial", "uns deixen més\ndescendents", "taronja")]
    for k, (t, s, c) in enumerate(items):
        x = 20 + k * 205
        f.box(x, 30, 190, 70, t, color=c, size=15)
        f.text(x + 95, 130, s, size=12, fill=MUTED)
        f.arrow(x + 95, 160, 320, 180, color=col(c), sw=2)
    f.box(170, 180, 300, 50, "canvien les freqüències al·lèliques", color="verd", size=14)
    return f.svg()


def fig_forces():
    f = Fig(640, 292, "Factors que canvien les freqüències al·lèliques")
    f.box(230, 110, 180, 60, "p i q\n(freqüències al·lèliques)", color="gris", size=13)
    forces = [("Selecció natural", "adaptativa", "verd", 20, 20), ("Deriva", "atzar; forta en\npoblacions petites", "blau", 430, 20),
              ("Mutació", "crea al·lels nous;\nefecte lent", "lila", 20, 200), ("Flux gènic", "migració entre\npoblacions", "taronja", 430, 200)]
    for t, s, c, x, y in forces:
        f.box(x, y, 190, 60, f"{t}\n{s}", color=c, size=12)
        f.arrow(x + 95 + (95 if x < 300 else -95), y + 30, 320 + (-90 if x < 300 else 90), 140 + (-20 if y < 100 else 20), color=col(c), sw=2)
    f.text(320, 282, "L’aparellament no aleatori canvia els genotips, no p ni q.", size=12, fill=MUTED)
    return f.svg()


def fig_especiacio():
    f = Fig(640, 300, "Especiació al·lopàtrica i simpàtrica")
    f.text(160, 22, "Al·lopàtrica", size=16, weight=700, fill=col("teal"))
    f.text(480, 22, "Simpàtrica", size=16, weight=700, fill=col("teal"))
    for k, y in enumerate((70, 150, 230)):
        # al·lopàtrica
        if k == 0:
            f.ellipse(160, y, 110, 28, fill=light("blau"), stroke=col("blau"))
        else:
            f.ellipse(95, y, 55, 26, fill=light("blau"), stroke=col("blau"))
            f.ellipse(225, y, 55, 26, fill=light("vermell") if k == 2 else light("blau"), stroke=col("vermell") if k == 2 else col("blau"))
            if k == 1:
                f.path(f"M160,{y-34} q-10,34 0,68", stroke="#7a5a2b", sw=5)
        # simpàtrica
        if k == 0:
            f.ellipse(480, y, 110, 28, fill=light("blau"), stroke=col("blau"))
        else:
            f.ellipse(480, y, 110, 28, fill=light("blau"), stroke=col("blau"))
            for j in range(5 if k == 1 else 9):
                xx = 400 + j * 18
                f.circle(xx, y, 6, fill=col("vermell"), stroke="none")
    f.text(160, 112, "barrera geogràfica", size=11, fill="#7a5a2b", weight=700)
    f.text(160, 275, "quan la barrera desapareix,\nja hi ha aïllament reproductiu", size=11, fill=MUTED)
    f.text(480, 275, "aïllament reproductiu sense separació\n(p. ex. poliploïdia en plantes)", size=11, fill=MUTED)
    return f.svg()


# ---------------- microbiologia ----------------
def fig_gram():
    f = Fig(640, 280, "Paret dels bacteris gram positius i gram negatius")
    for k, (t, c) in enumerate([("Gram positiu (lila)", "lila"), ("Gram negatiu (rosa)", "rosa")]):
        x = 20 + k * 320
        f.text(x + 140, 22, t, size=15, weight=700, fill=col(c))
        y = 200
        f.rect(x, y, 280, 22, fill="#fde7c7", stroke=col("taronja"), rx=4); f.text(x + 140, y + 11, "membrana plasmàtica", size=11)
        if k == 0:
            f.rect(x, y - 110, 280, 106, fill="#e8dcf5", stroke=col("lila"), rx=4)
            for j in range(6):
                f.line(x + 6, y - 100 + j * 16, x + 274, y - 100 + j * 16, stroke=col("lila"), sw=1, dash="6 4")
            f.text(x + 140, y - 57, "peptidoglicà gruixut", size=13, weight=700)
        else:
            f.rect(x, y - 30, 280, 26, fill="#e8dcf5", stroke=col("lila"), rx=4); f.text(x + 140, y - 17, "peptidoglicà prim", size=11, weight=700)
            f.rect(x, y - 70, 280, 22, fill="#fde7c7", stroke=col("taronja"), rx=4); f.text(x + 140, y - 59, "membrana externa", size=11, weight=700)
            for j in range(12):
                f.line(x + 12 + j * 23, y - 70, x + 12 + j * 23, y - 90, stroke=col("verd"), sw=2)
            f.text(x + 140, y - 102, "lipopolisacàrid (LPS)", size=11, fill=col("verd"), weight=700)
        f.text(x + 140, 250, "reté el cristall violeta" if k == 0 else "l’alcohol el decolora;\nla safranina el tenyeix", size=12, fill=MUTED)
    return f.svg()


def fig_nitrogen():
    f = Fig(640, 360, "Cicle del nitrogen")
    nodes = {"N2": (320, 50, "N₂ atmosfèric", "gris"), "NH4": (120, 190, "NH₄⁺ (amoni)", "blau"), "NO2": (320, 300, "NO₂⁻ (nitrit)", "taronja"),
             "NO3": (520, 190, "NO₃⁻ (nitrat)", "verd"), "ORG": (320, 175, "N orgànic\n(proteïnes, àcids nucleics)", "lila")}
    for k, (x, y, t, c) in nodes.items():
        w = 170 if k == "ORG" else 140
        f.box(x - w / 2, y - 24, w, 48, t, color=c, size=13)
    def a(p, q, lab, lx, ly, curve=None, anchor="middle"):
        f.arrow(*p, *q, color=INK, sw=2, curve=curve)
        f.text(lx, ly, lab, size=12, weight=700, fill=col("teal"), anchor=anchor)
    a((250, 60), (130, 164), "fixació\n(Rhizobium, cianobacteris)", 120, 90, curve=(150, 70))
    a((130, 216), (250, 300), "nitrificació\n(Nitrosomonas)", 110, 290, curve=(150, 300))
    a((390, 300), (510, 216), "nitrificació\n(Nitrobacter)", 530, 290, curve=(490, 300))
    a((520, 164), (395, 58), "desnitrificació\n(anaerobiosi)", 545, 90, curve=(500, 70))
    a((450, 190), (408, 180), "assimilació", 440, 138)
    a((235, 180), (192, 188), "amonificació", 205, 138)
    return f.svg()


def fig_cicles_virus():
    f = Fig(640, 330, "Cicle lític i cicle lisogènic d'un bacteriòfag")
    def bact(x, y, w=110, h=56):
        f.rect(x - w / 2, y - h / 2, w, h, fill=light("blau"), stroke=col("blau"), sw=2, rx=h / 2)
    f.text(320, 18, "1. Adsorció i entrada del DNA víric", size=13, weight=700)
    bact(320, 60)
    f.path("M300,58 c10,-10 20,10 40,0", stroke=col("vermell"), sw=2.5)
    f.arrow(250, 80, 160, 120, color=MUTED); f.arrow(390, 80, 480, 120, color=MUTED)
    f.text(160, 110, "Cicle lític", size=15, weight=700, fill=col("vermell"), anchor="end")
    f.text(480, 110, "Cicle lisogènic", size=15, weight=700, fill=col("verd"), anchor="start")
    bact(140, 170)
    for dx in (-30, -10, 10, 30):
        f.rect(140 + dx - 5, 162, 10, 14, fill=col("vermell"), stroke="none", rx=2)
    f.text(140, 210, "replicació i síntesi\nde peces víriques", size=11, fill=MUTED)
    f.arrow(140, 230, 140, 260, color=MUTED)
    f.path("M85,290 l20,-20 l20,20 l20,-20 l20,20 l20,-20", stroke=col("blau"), sw=2)
    for dx in (-40, 0, 40):
        f.rect(140 + dx - 5, 290, 10, 14, fill=col("vermell"), stroke="none", rx=2)
    f.text(140, 322, "lisi: s’alliberen virus", size=11, fill=MUTED)
    bact(500, 170, w=130)
    f.path("M445,170 c20,-12 40,12 60,0 c20,-12 40,12 50,0", stroke=col("blau"), sw=2)
    f.rect(480, 164, 28, 12, fill=col("vermell"), stroke="none", rx=2)
    f.text(500, 210, "el DNA víric s’integra:\npròfag", size=11, fill=MUTED)
    f.arrow(500, 230, 500, 260, color=MUTED)
    bact(450, 285, w=80, h=40); bact(550, 285, w=80, h=40)
    f.text(500, 322, "es copia amb el bacteri", size=11, fill=MUTED)
    f.arrowpath("M430,250 C350,250 260,240 210,220", color=col("taronja"), sw=2, dash="6 4")
    f.text(320, 236, "inducció (estrès)", size=12, weight=700, fill=col("taronja"))
    return f.svg()


def fig_acel():
    f = Fig(640, 230, "Virus, viroide i prió")
    f.text(110, 20, "Virus", size=15, weight=700, fill=col("teal"))
    pts = [(110 + 55 * math.cos(math.radians(a)), 110 + 55 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
    f.poly(pts, fill=light("blau"), stroke=col("blau"), sw=3)
    f.path("M85,105 c10,-15 20,15 30,0 s20,15 25,5", stroke=col("vermell"), sw=2.5)
    f.text(110, 190, "àcid nucleic (DNA o RNA)\n+ càpsida (± embolcall)", size=11, fill=MUTED)
    f.text(320, 20, "Viroide", size=15, weight=700, fill=col("teal"))
    f.ellipse(320, 110, 60, 30, stroke=col("vermell"), sw=3)
    f.text(320, 190, "RNA circular nu\nsense càpsida (plantes)", size=11, fill=MUTED)
    f.text(530, 20, "Prió", size=15, weight=700, fill=col("teal"))
    f.path("M490,110 c10,-40 30,-10 40,-30 s30,20 20,40 s-40,30 -30,0 s-30,10 -30,-10", fill=light("lila"), stroke=col("lila"), sw=2.5)
    f.text(530, 190, "proteïna mal plegada\nsense àcid nucleic", size=11, fill=MUTED)
    return f.svg()


# ---------------- immunologia ----------------
def fig_resposta():
    f = Fig(640, 320, "Resposta primària i resposta secundària")
    x0, y0, W, H = 70, 260, 540, 200
    f.line(x0, y0, x0 + W, y0, sw=1.8); f.line(x0, y0, x0, y0 - H, sw=1.8)
    f.text(x0 + W / 2, y0 + 34, "temps (dies)", size=13)
    f.text(x0 - 40, y0 - H / 2, "anticossos a la sang", size=13, rot=-90)
    def bump(t0, peak, width, height, color, dash=None):
        pts = []
        for i in range(0, 121):
            t = t0 + i / 120 * width * 3
            v = height * math.exp(-((t - (t0 + peak)) / (width * 0.55)) ** 2)
            pts.append((x0 + t * 5, y0 - v))
        f.path("M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts), stroke=color, sw=3, dash=dash)
    bump(5, 9, 10, 45, col("taronja"))
    bump(8, 13, 12, 30, col("lila"), dash="6 4")
    bump(58, 5, 8, 50, col("taronja"))
    bump(58, 7, 12, 180, col("lila"), dash="6 4")
    for t, lab in ((5, "1r contacte"), (58, "2n contacte")):
        f.arrow(x0 + t * 5, y0 + 18, x0 + t * 5, y0 + 2, color=INK)
        f.text(x0 + t * 5, y0 + 50, lab, size=12, weight=700)
    f.line(x0 + 400, 70, x0 + 430, 70, stroke=col("taronja"), sw=3); f.text(x0 + 436, 70, "IgM", size=13, anchor="start")
    f.line(x0 + 400, 95, x0 + 430, 95, stroke=col("lila"), sw=3, dash="6 4"); f.text(x0 + 436, 95, "IgG", size=13, anchor="start")
    f.text(x0 + 110, y0 - 85, "primària:\nlenta, baixa, IgM", size=12, fill=MUTED)
    f.text(x0 + 180, y0 - 170, "secundària: ràpida, alta, IgG\n(cèl·lules de memòria)", size=12, fill=MUTED)
    return f.svg()


def fig_humoral_cel():
    f = Fig(640, 330, "Resposta humoral i resposta cel·lular")
    f.box(230, 20, 180, 50, "cèl·lula presentadora\n(antigen + MHC II)", color="gris", size=12)
    f.arrow(320, 72, 320, 100)
    f.box(240, 100, 160, 44, "T col·laborador (CD4)", color="teal", size=13)
    f.arrow(270, 146, 150, 180); f.arrow(370, 146, 490, 180)
    f.text(150, 165, "Humoral", size=15, weight=700, fill=col("blau"), anchor="end")
    f.text(490, 165, "Cel·lular", size=15, weight=700, fill=col("vermell"), anchor="start")
    f.box(60, 184, 180, 40, "limfòcit B", color="blau", size=13)
    f.arrow(110, 226, 90, 256); f.arrow(190, 226, 210, 256)
    f.box(20, 258, 140, 40, "plasmàtica →\nanticossos", color="blau", size=11)
    f.box(170, 258, 110, 40, "B de memòria", color="blau", size=11)
    f.box(400, 184, 200, 40, "T citotòxic (CD8)", color="vermell", size=13)
    f.arrow(500, 226, 500, 256)
    f.box(400, 258, 200, 40, "mata la cèl·lula infectada\n(pèptid + MHC I)", color="vermell", size=11)
    f.text(320, 320, "Els T col·laboradors no fan anticossos ni maten: activen B, T citotòxics i macròfags.", size=11, fill=MUTED)
    return f.svg()


def fig_anticos():
    f = Fig(640, 320, "Estructura d'un anticòs (IgG)")
    cx = 260
    # cadenes pesants
    f.path(f"M{cx-10},300 L{cx-10},170 L{cx-100},60", stroke=col("blau"), sw=18, extra='stroke-linecap="round"')
    f.path(f"M{cx+10},300 L{cx+10},170 L{cx+100},60", stroke=col("blau"), sw=18, extra='stroke-linecap="round"')
    # lleugeres
    f.path(f"M{cx-60},160 L{cx-130},75", stroke=col("verd"), sw=14, extra='stroke-linecap="round"')
    f.path(f"M{cx+60},160 L{cx+130},75", stroke=col("verd"), sw=14, extra='stroke-linecap="round"')
    for s in (-1, 1):
        f.circle(cx + s * 120, 55, 22, fill="none", stroke=col("vermell"), sw=3, dash="5 3")
    f.line(cx - 10, 185, cx + 10, 185, stroke=col("groc"), sw=3); f.line(cx - 10, 195, cx + 10, 195, stroke=col("groc"), sw=3)
    f.text(cx + 120, 20, "regió variable: lloc d’unió a l’antigen", size=12, weight=700, fill=col("vermell"))
    f.text(450, 120, "cadena pesant (H) ×2", size=13, weight=700, fill=col("blau"), anchor="start")
    f.text(450, 150, "cadena lleugera (L) ×2", size=13, weight=700, fill=col("verd"), anchor="start")
    f.text(450, 180, "ponts disulfur", size=13, weight=700, fill=col("groc"), anchor="start")
    f.text(450, 240, "regió constant (Fc):\ndefineix la classe\n(IgG, IgM, IgA, IgE, IgD)", size=12, fill=MUTED, anchor="start")
    f.line(cx + 20, 270, 440, 250, stroke=MUTED, sw=1)
    return f.svg()


def fig_tipus_immunitat():
    f = Fig(640, 230, "Tipus d'immunitat adquirida")
    f.text(260, 20, "Natural", size=14, weight=700, fill=col("teal"))
    f.text(500, 20, "Artificial", size=14, weight=700, fill=col("teal"))
    f.text(70, 85, "Activa\n(memòria)", size=14, weight=700, fill=col("verd"))
    f.text(70, 175, "Passiva\n(sense memòria)", size=14, weight=700, fill=col("taronja"))
    cells = [((150, 40), "passar la infecció", "verd"), ((390, 40), "vacuna", "verd"), ((150, 130), "IgG de la placenta,\nIgA de la llet", "taronja"), ((390, 130), "sèrum / anticossos\nmonoclonals", "taronja")]
    for (x, y), t, c in cells:
        f.box(x, y, 220, 80, t, color=c, size=13, weight=600)
    return f.svg()


# ---------------- disseny experimental ----------------
def fig_disseny():
    f = Fig(640, 250, "Peces d'un disseny experimental")
    items = [("Hipòtesi", "es pot\ncontradir", "lila"), ("Variable\nindependent", "la que es\ncanvia", "blau"), ("Variable\ndependent", "la que es\nmesura", "verd"),
             ("Control", "tot igual\nmenys la VI", "taronja"), ("Rèpliques", "unitats\nindependents", "vermell")]
    for k, (t, s, c) in enumerate(items):
        x = 10 + k * 126
        f.box(x, 40, 116, 70, t, color=c, size=13)
        f.text(x + 58, 140, s, size=12, fill=MUTED)
        if k < 4:
            f.arrow(x + 117, 75, x + 125, 75, color=MUTED)
    f.box(170, 185, 300, 44, "Conclusió: només el que diuen les dades", color="gris", size=13)
    f.arrow(320, 170, 320, 184, color=MUTED)
    return f.svg()


# ---------------- mapes conceptuals ----------------
def concept_map(title, color, branches, footer=None):
    """branches: llista de (títol, color, [línies]). Disposició en 2 columnes al voltant del títol."""
    n = len(branches)
    rows = math.ceil(n / 2)
    bh = []
    for t, c, lines in branches:
        bh.append(56 + 22 * len(lines))
    rowh = [max(bh[2 * r:2 * r + 2]) for r in range(rows)]
    H = 110 + sum(rowh) + 24 * rows + (40 if footer else 10)
    f = Fig(640, H, "Mapa del tema: " + title)
    f.rect(170, 18, 300, 54, fill=col(color), stroke="none", rx=27)
    f.text(320, 45, title, size=19, weight=700, fill="#fff")
    y = 110
    last_y = 110 + sum(rowh[:-1]) + 24 * (rows - 1) + 19 if rows else 110
    if n % 2 == 1:
        last_y -= rowh[-2] + 24 if rows > 1 else 0
    f.line(320, 72, 320, last_y, stroke=col(color), sw=3)
    for r in range(rows):
        for k in range(2):
            i = 2 * r + k
            if i >= n:
                continue
            t, c, lines = branches[i]
            x = 16 + k * 316
            w = 292 if n - 2 * r > 1 or True else 608
            if n % 2 == 1 and i == n - 1:
                x, w = 16 + 158, 292
            h = rowh[r]
            sx = x + w if k == 0 and not (n % 2 == 1 and i == n - 1) else x
            if not (n % 2 == 1 and i == n - 1):
                f.line(320, y + 19, sx, y + 19, stroke=col(color), sw=3)
                f.circle(320, y + 19, 6, fill=col(color), stroke="#fff", sw=2)
            f.rect(x, y, w, h, fill="#fff", stroke=col(c), sw=2, rx=14)
            f.rect(x, y, w, 38, fill=col(c), stroke=col(c), sw=2, rx=14)
            f.rect(x, y + 24, w, 14, fill=col(c), stroke="none", rx=0)
            f.text(x + w / 2, y + 19, t, size=15, weight=700, fill="#fff")
            for j, l in enumerate(lines):
                f.circle(x + 16, y + 56 + j * 22, 3, fill=col(c), stroke="none")
                f.text(x + 26, y + 56 + j * 22, l, size=12.5, anchor="start")
        y += rowh[r] + 24
    if footer:
        f.text(320, H - 22, footer, size=12, fill=MUTED, italic=True)
    return f.svg()


def map1():
    return concept_map("Biomolècules", "teal", [
        ("Aigua i sals", "blau", ["molècula polar, ponts d’hidrogen", "dissolvent, tèrmica, cohesió", "sals: osmosi, pH (tampons), cofactors"]),
        ("Glúcids", "verd", ["monosacàrids: glucosa, ribosa", "enllaç O-glicosídic α o β", "midó i glicogen (α): reserva", "cel·lulosa i quitina (β): estructura"]),
        ("Lípids", "taronja", ["saponificables: TAG (reserva),", "  fosfolípids (membranes), ceres", "insaponificables: esteroides, terpens", "enllaç èster"]),
        ("Proteïnes", "vermell", ["aminoàcids (zwitterió), enllaç peptídic", "estructura 1a, 2a, 3a i 4a", "desnaturalització ≠ hidròlisi", "funció depèn de la forma"]),
        ("Enzims", "lila", ["baixen l’energia d’activació", "Vmax i Km; òptims de T i pH", "inhibició competitiva / no competitiva", "cofactors i coenzims (vitamines B)"]),
        ("Àcids nucleics", "blau", ["nucleòtid: pentosa + base + fosfat", "enllaç fosfodièster, polaritat 5′→3′", "DNA: doble hèlix antiparal·lela", "Chargaff: A = T, G = C"]),
    ], footer="Funcions que cal saber assignar: energètica, estructural, reguladora i informativa.")


def map2():
    return concept_map("La cèl·lula", "teal", [
        ("Teoria cel·lular", "gris", ["tot ésser viu és fet de cèl·lules", "unitat estructural i funcional", "tota cèl·lula ve d’una altra", "microscopi òptic (~0,2 µm) i electrònic"]),
        ("Procariotes i eucariotes", "blau", ["procariota: nucleoide, 70S, sense orgànuls", "eucariota: nucli, 80S, endomembranes", "bacteris ≠ arqueus"]),
        ("Membrana", "taronja", ["mosaic fluid: bicapa + proteïnes", "difusió simple i facilitada", "transport actiu (bomba Na⁺/K⁺)", "osmosi; endocitosi i exocitosi"]),
        ("Orgànuls", "verd", ["nucli, reticle, Golgi, lisosomes", "mitocondri: respiració", "cloroplast: fotosíntesi", "endosimbiosi: DNA propi i 70S"]),
        ("Cicle i mitosi", "lila", ["interfase: G1, S (2C→4C), G2", "punts de control (ciclines-CDK)", "mitosi: 2 cèl·lules 2n idèntiques"]),
        ("Meiosi", "vermell", ["meiosi I: se separen homòlegs", "entrecreuament a la profase I", "meiosi II: se separen cromàtides", "4 cèl·lules n diferents"]),
    ])


def map3():
    return concept_map("Metabolisme", "taronja", [
        ("Conceptes", "gris", ["catabolisme (oxida) i anabolisme (redueix)", "ATP: moneda; NADH, FADH₂, NADPH", "via ≠ reacció"]),
        ("Respiració aeròbica", "vermell", ["glucòlisi (citosol): 2 ATP, 2 NADH", "piruvat → acetil-CoA (matriu)", "Krebs (matriu): NADH, FADH₂, GTP, CO₂", "cadena i ATP-sintasa: ~30–32 ATP"]),
        ("Fermentacions", "groc", ["regeneren NAD⁺ sense cadena", "làctica: lactat, sense CO₂", "alcohòlica: etanol + CO₂", "2 ATP per glucosa"]),
        ("Lípids", "taronja", ["β-oxidació (matriu): acetil-CoA", "lipogènesi (citosol): NADPH", "els àcids grassos no fan glucosa"]),
        ("Fotosíntesi", "verd", ["fase lluminosa (tilacoide): O₂ de l’aigua,", "  ATP i NADPH", "Calvin (estroma): rubisco fixa CO₂", "3 ATP i 2 NADPH per CO₂"]),
        ("Quimiosíntesi", "blau", ["energia: oxidar compostos inorgànics", "nitrificants (NH₄⁺ → NO₂⁻ → NO₃⁻)", "fixen CO₂ sense llum"]),
    ])


def map4():
    return concept_map("Genètica mendeliana", "lila", [
        ("Conceptes", "gris", ["gen, al·lel, genotip, fenotip", "homozigot, heterozigot, hemizigot", "dominant ≠ freqüent ni «bo»"]),
        ("Lleis de Mendel", "blau", ["segregació: un al·lel per gàmeta", "transmissió independent: gens", "  en cromosomes diferents", "base cel·lular: anafase I"]),
        ("Monohibridisme", "verd", ["Aa × Aa → 3:1 (1:2:1 genotips)", "encreuament prova: × aa", "dominància incompleta i codominància", "grups ABO"]),
        ("Dihibridisme i lligament", "taronja", ["AaBb × AaBb → 9:3:3:1", "gens lligats: més parentals", "recombinants/total → cM"]),
        ("Lligada al sexe", "vermell", ["X recessiu: més homes afectats", "pare → totes les filles portadores", "no passa de pare a fill home"]),
        ("Pedigrís i probabilitat", "teal", ["dos sans amb fill afectat → recessiu", "producte (i) i suma (o)", "«com a mínim un» = 1 − «cap»"]),
    ])


def map5():
    return concept_map("Genètica molecular", "blau", [
        ("Flux de la informació", "gris", ["DNA → RNA → proteïna", "retrotranscripció (retrovirus)", "genomes procariota i eucariota"]),
        ("Replicació", "blau", ["semiconservativa, 5′→3′", "helicasa, primasa, polimerases, ligasa", "líder i retardada (Okazaki)", "telòmers i telomerasa"]),
        ("Expressió", "lila", ["transcripció: motlle 3′→5′", "maduració: cap, poli-A, splicing", "codi: triplets, degenerat, AUG", "traducció: ribosoma, llocs A-P-E"]),
        ("Regulació", "verd", ["operó lac (inducible)", "promotor, intensificadors, factors", "epigenètica i diferenciació"]),
        ("Mutacions i càncer", "vermell", ["silenciosa, canvi de sentit, sense sentit", "insercions/delecions: canvi de marc", "oncogens i gens supressors (p53)"]),
        ("Biotecnologia", "taronja", ["restricció, ligasa, plasmidi", "PCR i CRISPR-Cas9", "OMG ≠ transgènic; teràpia gènica"]),
    ])


def map6():
    return concept_map("Evolució", "verd", [
        ("Evidències", "gris", ["fòssils, anatomia comparada", "homologia ≠ analogia", "embriologia, biogeografia", "seqüències de DNA i proteïnes"]),
        ("Teories", "blau", ["Lamarck: herència d’adquirits (no)", "Darwin i Wallace: selecció natural", "teoria sintètica: genètica de poblacions"]),
        ("Hardy-Weinberg", "lila", ["p + q = 1; p² + 2pq + q² = 1", "condicions: població gran, sense", "  selecció, mutació ni migració", "hipòtesi nul·la"]),
        ("Forces evolutives", "taronja", ["selecció natural i sexual", "deriva (coll d’ampolla, fundador)", "mutació i flux gènic"]),
        ("Variabilitat", "vermell", ["mutació: única font d’al·lels nous", "recombinació: noves combinacions", "somàtica vs. germinal"]),
        ("Especiació", "verd", ["espècie biològica (Mayr)", "barreres pre i postzigòtiques", "al·lopàtrica i simpàtrica", "equilibri puntuat, evo-devo"]),
    ])


def map7():
    return concept_map("Microbiologia", "groc", [
        ("Procariotes", "blau", ["bacteris i arqueus (dominis diferents)", "mida 1–5 µm; augments", "Gram + i Gram −"]),
        ("Tècniques", "gris", ["esterilització (autoclau) ≠ desinfecció", "pasteurització no esterilitza", "cultiu, aïllament, colònies"]),
        ("Metabolisme i cicles", "verd", ["foto/quimio, auto/heteròtrofs", "cicle del nitrogen", "simbiosi: Rhizobium"]),
        ("Microbiota i aplicacions", "taronja", ["microbiota normal i oportunistes", "aliments, fàrmacs, bioremediació", "zoonosi, epidèmia, pandèmia"]),
        ("Transferència horitzontal", "vermell", ["transformació, transducció, conjugació", "plasmidis R: resistències", "l’antibiòtic selecciona, no crea"]),
        ("Formes acel·lulars", "lila", ["virus: àcid nucleic + càpsida", "cicle lític i lisogènic; retrovirus", "viroides (RNA) i prions (proteïna)"]),
    ])


def map8():
    return concept_map("Immunologia", "vermell", [
        ("Barreres", "gris", ["físiques: pell i mucoses", "químiques: pH, lisozim", "biològiques: microbiota"]),
        ("Immunitat innata", "taronja", ["fagòcits: neutròfils, macròfags", "inflamació i histamina", "complement (3 vies); NK", "sense memòria"]),
        ("Immunitat específica", "blau", ["presentació: MHC I i MHC II", "humoral: B → plasmàtiques", "cel·lular: T CD4 i T CD8", "selecció clonal i memòria"]),
        ("Anticossos", "lila", ["2 cadenes H + 2 L; regió variable", "IgM, IgG, IgA, IgE, IgD", "primària (IgM) i secundària (IgG)"]),
        ("Immunitat artificial", "verd", ["vacuna: activa, deixa memòria", "sèrum: passiva, immediata", "immunitat de grup; monoclonals"]),
        ("Alteracions", "vermell", ["al·lèrgia (IgE), autoimmunitat", "rebuig de trasplantaments", "immunodeficiències: VIH i sida"]),
    ])


def map9():
    return concept_map("Disseny experimental", "gris", [
        ("Hipòtesi", "lila", ["concreta i que es pugui contradir", "no és el tema de l’estudi"]),
        ("Variables", "blau", ["independent: la que es canvia", "dependent: la que es mesura", "controlades: iguals a tot arreu"]),
        ("Control", "taronja", ["tot igual menys la VI", "control negatiu i positiu", "inclou el dissolvent (vehicle)"]),
        ("Rèpliques", "vermell", ["unitats independents", "no 5 lectures del mateix tub"]),
        ("Gràfics i taules", "verd", ["VI a l’eix x, VD a l’eix y, unitats", "òptims, altiplans, barres d’error"]),
        ("Conclusió", "teal", ["només el que diuen les dades", "sense extrapolar ni generalitzar"]),
    ])
