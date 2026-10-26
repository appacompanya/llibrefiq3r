"""Il·lustracions vectorials dels dossiers de teoria de les SdA 2–6 (mateix estil que teoria_figs)."""
import math, random
from teoria_figs import svg, txt, arrow_defs, INK, MUT, WATER, WATER2, OIL

def ac(c): return c  # color d'accent de la SdA (es passa a cada funció)
BLUE = "#4d8fd6"; RED = "#d9534f"; ORA = "#e0782f"; GRN = "#5aa45a"; PUR = "#8f7ad9"; GRY = "#9aa1a8"

def axes(x0, y0, w, h, xl, yl, col=INK, idm="ax"):
    s = f'<line x1="{x0}" y1="{y0}" x2="{x0+w}" y2="{y0}" stroke="{col}" stroke-width="1.5" marker-end="url(#{idm})"/>'
    s += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-h}" stroke="{col}" stroke-width="1.5" marker-end="url(#{idm})"/>'
    s += txt(x0 + w, y0 + 16, xl, 10.5, "end") + txt(x0 - 6, y0 - h + 4, yl, 10.5, "end")
    return s

# ================================================================= SdA 2
def estats_particules(A="#E0782F"):
    random.seed(2)
    b = ""
    for i, (t, sub) in enumerate((("Sòlid", "ordenades, vibren"), ("Líquid", "juntes, llisquen"), ("Gas", "separades, molt ràpides"))):
        x0 = 15 + i * 175
        b += f'<rect x="{x0}" y="10" width="150" height="130" rx="8" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
        if i == 0:
            for r in range(5):
                for c in range(6):
                    cx, cy = x0 + 22 + c * 21, 32 + r * 21
                    b += f'<circle cx="{cx}" cy="{cy}" r="9" fill="{A}" stroke="{INK}" stroke-width="1"/>'
                    if (r + c) % 4 == 0: b += f'<path d="M{cx-13} {cy-11} q2 -3 4 0 M{cx+9} {cy-11} q2 -3 4 0" stroke="{MUT}" fill="none" stroke-width="1"/>'
        elif i == 1:
            pts = []
            while len(pts) < 24:
                p = (x0 + 14 + random.uniform(0, 122), 55 + random.uniform(0, 75))
                if all((p[0]-q[0])**2 + (p[1]-q[1])**2 > 300 for q in pts): pts.append(p)
            b += f'<rect x="{x0+2}" y="44" width="146" height="94" fill="#fbeadd"/>'
            for (cx, cy) in pts: b += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="9" fill="{A}" stroke="{INK}" stroke-width="1"/>'
        else:
            b += arrow_defs("ag")
            for k in range(8):
                cx, cy = x0 + 20 + random.uniform(0, 110), 25 + random.uniform(0, 100)
                ang = random.uniform(0, 6.28)
                b += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="9" fill="{A}" stroke="{INK}" stroke-width="1"/><line x1="{cx+11*math.cos(ang):.0f}" y1="{cy+11*math.sin(ang):.0f}" x2="{cx+28*math.cos(ang):.0f}" y2="{cy+28*math.sin(ang):.0f}" stroke="{INK}" stroke-width="1.3" marker-end="url(#ag)"/>'
        b += txt(x0 + 75, 160, t, 12, weight=700) + txt(x0 + 75, 175, sub, 10, fill=MUT)
    return svg(530, 182, b, "150mm")

def evaporacio_ebullicio(A="#E0782F"):
    random.seed(5)
    b = arrow_defs("ae")
    for i, (t, sub) in enumerate((("Evaporació", "només a la superfície, a qualsevol temperatura"), ("Ebullició", "a tot el líquid, amb bombolles, a una temperatura fixa"))):
        x0 = 30 + i * 260
        b += f'<path d="M{x0} 40 L{x0} 160 Q{x0} 170 {x0+10} 170 L{x0+170} 170 Q{x0+180} 170 {x0+180} 160 L{x0+180} 40" fill="none" stroke="{INK}" stroke-width="1.8"/>'
        b += f'<rect x="{x0+1}" y="80" width="178" height="89" fill="{WATER}"/>'
        for k in range(26):
            cx, cy = x0 + 12 + random.uniform(0, 156), 88 + random.uniform(0, 74)
            b += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="4.5" fill="{BLUE}" stroke="{INK}" stroke-width=".7"/>'
        if i == 0:
            for cx in (x0 + 40, x0 + 100, x0 + 150):
                b += f'<circle cx="{cx}" cy="58" r="4.5" fill="{BLUE}" stroke="{INK}" stroke-width=".7"/><line x1="{cx}" y1="78" x2="{cx}" y2="66" stroke="{INK}" stroke-width="1.2" marker-end="url(#ae)"/>'
        else:
            for (cx, cy, r) in ((x0 + 50, 140, 9), (x0 + 95, 115, 12), (x0 + 140, 145, 8), (x0 + 120, 95, 7)):
                b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="1.1"/>'
            b += f'<path d="M{x0+60} 192 L{x0+120} 192 L{x0+90} 176 Z" fill="{A}"/><path d="M{x0+78} 182 Q{x0+90} 166 {x0+102} 182" fill="#f3b23a"/>'
        b += txt(x0 + 90, 26, t, 12, weight=700) + txt(x0 + 90, 212, sub, 9.5, fill=MUT)
    return svg(520, 220, b, "145mm")

def corba_escalfament(A="#E0782F"):
    b = arrow_defs("ax")
    x0, y0 = 60, 220
    b += axes(x0, y0, 440, 200, "temps", "T (°C)")
    def Y(t): return y0 - (t + 30) * 1.3
    pts = [(x0, Y(-20)), (x0 + 60, Y(0)), (x0 + 150, Y(0)), (x0 + 250, Y(100)), (x0 + 380, Y(100)), (x0 + 430, Y(125))]
    b += '<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f'" fill="none" stroke="{A}" stroke-width="3" stroke-linejoin="round"/>'
    for t in (0, 100):
        b += f'<line x1="{x0}" y1="{Y(t):.0f}" x2="{x0+430}" y2="{Y(t):.0f}" stroke="{GRY}" stroke-dasharray="3 4"/>' + txt(x0 - 6, Y(t) + 4, str(t), 10, "end")
    labs = [((x0 + 34), Y(-10) + 24, "sòlid"), ((x0 + 105), Y(0) + 18, "fusió"), ((x0 + 105), Y(0) + 31, "sòlid + líquid"), ((x0 + 232), Y(50) + 16, "líquid"), ((x0 + 315), Y(100) + 18, "ebullició"), ((x0 + 315), Y(100) + 31, "líquid + gas"), ((x0 + 392), Y(125) - 6, "gas")]
    for x, y, t in labs: b += txt(x, y, t, 10, fill=MUT if "+" in t else INK, weight=400 if "+" in t else 700)
    return svg(520, 240, b, "140mm")

def lleis_gasos(A="#E0782F"):
    b = arrow_defs("ax")
    # Boyle
    x0, y0 = 40, 170
    b += axes(x0, y0, 140, 140, "V", "P")
    b += '<path d="' + "M" + " L".join(f"{x0+12+t:.0f},{y0-1800/(t+14):.0f}" for t in range(0, 125, 4)) + f'" fill="none" stroke="{A}" stroke-width="3"/>'
    b += txt(x0 + 70, 200, "Boyle-Mariotte (T constant)", 10.5, weight=700) + txt(x0 + 70, 214, "P · V = constant", 10, fill=MUT)
    # Charles
    x0 = 230
    b += axes(x0, y0, 150, 140, "T (K)", "V")
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0+140}" y2="{y0-120}" stroke="{A}" stroke-width="3"/>'
    b += txt(x0 + 75, 200, "Charles (P constant)", 10.5, weight=700) + txt(x0 + 75, 214, "recta que passa per 0 K", 10, fill=MUT)
    # Gay-Lussac
    x0 = 430
    b += axes(x0, y0, 150, 140, "T (K)", "P")
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0+140}" y2="{y0-110}" stroke="{A}" stroke-width="3"/>'
    b += txt(x0 + 75, 200, "Gay-Lussac (V constant)", 10.5, weight=700) + txt(x0 + 75, 214, "recta que passa per 0 K", 10, fill=MUT)
    return svg(600, 222, b, "160mm")

def boyle_embol(A="#E0782F"):
    random.seed(11)
    b = arrow_defs("ab")
    for i, (h, n) in enumerate(((150, 10), (75, 10))):
        x0 = 40 + i * 230
        top = 190 - h
        b += f'<path d="M{x0} 30 L{x0} 190 L{x0+140} 190 L{x0+140} 30" fill="none" stroke="{INK}" stroke-width="2"/>'
        b += f'<rect x="{x0+2}" y="{top-14}" width="136" height="14" fill="{GRY}" stroke="{INK}" stroke-width="1.2"/><rect x="{x0+62}" y="10" width="16" height="{top-24}" fill="{GRY}" stroke="{INK}" stroke-width="1.2"/>'
        b += f'<rect x="{x0+2}" y="{top}" width="136" height="{h-1}" fill="#fbeadd"/>'
        for k in range(n):
            cx, cy = x0 + 16 + random.uniform(0, 108), top + 12 + random.uniform(0, h - 24)
            b += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="6" fill="{A}" stroke="{INK}" stroke-width="1"/>'
        b += txt(x0 + 70, 212, ("Volum gran: pocs xocs, pressió baixa" if i == 0 else "Meitat de volum: el doble de xocs"), 10.5, weight=700)
        if i == 1: b += txt(x0 + 70, 226, "i el doble de pressió", 10.5, weight=700)
    b += f'<line x1="200" y1="110" x2="250" y2="110" stroke="{INK}" stroke-width="1.6" marker-end="url(#ab)"/>' + txt(225, 100, "empenyem", 10, fill=MUT)
    return svg(460, 232, b, "120mm")

# ================================================================= SdA 3
def rutherford(A="#6C5CC9"):
    b = arrow_defs("ar", INK)
    b += f'<rect x="20" y="95" width="70" height="50" rx="6" fill="{GRY}" stroke="{INK}" stroke-width="1.4"/>' + txt(55, 160, "font α", 10.5)
    b += f'<rect x="250" y="30" width="10" height="180" fill="#e9c46a" stroke="{INK}" stroke-width="1.2"/>' + txt(255, 226, "làmina d'or", 10.5)
    for y in (100, 110, 120, 130, 140):
        b += f'<line x1="92" y1="{y}" x2="250" y2="{y}" stroke="{RED}" stroke-width="1.3"/>'
    for y in (100, 110, 130, 140): b += f'<line x1="260" y1="{y}" x2="470" y2="{y+ (y-120)*0.15:.0f}" stroke="{RED}" stroke-width="1.3" marker-end="url(#ar)"/>'
    b += f'<path d="M260 120 Q300 120 330 60" fill="none" stroke="{RED}" stroke-width="1.3" marker-end="url(#ar)"/>'
    b += f'<path d="M255 121 Q230 126 190 160" fill="none" stroke="{RED}" stroke-width="1.3" marker-end="url(#ar)"/>'
    b += txt(480, 95, "la majoria travessen", 10.5, "start") + txt(338, 55, "unes poques es desvien", 10.5, "start") + txt(150, 180, "algunes reboten", 10.5, "start")
    # zoom
    b += f'<circle cx="690" cy="120" r="70" fill="#fff" stroke="{INK}" stroke-width="1.4"/><circle cx="690" cy="120" r="5" fill="{A}" stroke="{INK}"/>'
    for a in (0.6, 2.3, 4.1, 5.4): b += f'<circle cx="{690+48*math.cos(a):.0f}" cy="{120+48*math.sin(a):.0f}" r="3.5" fill="{BLUE}" stroke="{INK}" stroke-width=".8"/>'
    b += txt(690, 205, "àtom: nucli petit i positiu,", 10, fill=MUT) + txt(690, 218, "la resta gairebé buit", 10, fill=MUT)
    return svg(770, 230, b, "170mm")

def bohr(Z, label, A="#6C5CC9", ion=0, cx=0):
    caps = [2, 8, 8, 2]; e = Z - ion; shells = []
    for c in caps:
        if e <= 0: break
        shells.append(min(c, e)); e -= c
    s = f'<circle cx="{cx}" cy="0" r="14" fill="{A}" stroke="{INK}" stroke-width="1.2"/>' + f'<text x="{cx}" y="4" font-size="9" text-anchor="middle" fill="#fff" font-weight="700">{Z}+</text>'
    for i, n in enumerate(shells):
        r = 28 + i * 18
        s += f'<circle cx="{cx}" cy="0" r="{r}" fill="none" stroke="{GRY}" stroke-width="1.1"/>'
        for k in range(n):
            a = 2 * math.pi * k / n - math.pi / 2
            s += f'<circle cx="{cx + r*math.cos(a):.1f}" cy="{r*math.sin(a):.1f}" r="4" fill="{BLUE}" stroke="{INK}" stroke-width=".8"/>'
    return s

def bohr_atoms(A="#6C5CC9"):
    b = '<g transform="translate(0,100)">'
    for i, (Z, nm, conf) in enumerate(((3, "Liti", "2, 1"), (8, "Oxigen", "2, 6"), (11, "Sodi", "2, 8, 1"), (17, "Clor", "2, 8, 7"))):
        cx = 80 + i * 150
        b += bohr(Z, nm, A, cx=cx) + txt(cx, 96, f"{nm} (Z = {Z})", 11, weight=700) + txt(cx, 110, conf, 10.5, fill=MUT)
    return svg(600, 220, b + "</g>", "160mm")

def ions_formacio(A="#6C5CC9"):
    b = arrow_defs("ai") + '<g transform="translate(0,95)">'
    b += bohr(11, "Na", A, cx=75) + bohr(11, "Na+", A, ion=1, cx=262)
    b += f'<line x1="148" y1="0" x2="206" y2="0" stroke="{INK}" stroke-width="1.6" marker-end="url(#ai)"/>' + txt(177, -10, "perd 1 e⁻", 10, fill=MUT)
    b += txt(75, 95, "Na (11 e⁻)", 11, weight=700) + txt(262, 95, "Na⁺ (10 e⁻): catió", 11, weight=700)
    b += bohr(17, "Cl", A, cx=450) + bohr(17, "Cl-", A, ion=-1, cx=650)
    b += f'<line x1="520" y1="0" x2="578" y2="0" stroke="{INK}" stroke-width="1.6" marker-end="url(#ai)"/>' + txt(549, -10, "guanya 1 e⁻", 10, fill=MUT)
    b += txt(450, 95, "Cl (17 e⁻)", 11, weight=700) + txt(650, 95, "Cl⁻ (18 e⁻): anió", 11, weight=700)
    return svg(725, 205, b + "</g>", "170mm")

def enllacos(A="#6C5CC9"):
    b = ""
    # iònic: xarxa
    for i in range(5):
        for j in range(4):
            na = (i + j) % 2 == 0
            cx, cy = 30 + i * 26, 40 + j * 26
            b += f'<circle cx="{cx}" cy="{cy}" r="{8 if na else 11}" fill="{PUR if na else GRN}" stroke="{INK}" stroke-width="1"/>' + txt(cx, cy + 4, "+" if na else "−", 10, weight=700)
    b += txt(82, 160, "Iònic", 12, weight=700) + txt(82, 175, "xarxa de cations i anions", 9.5, fill=MUT)
    # covalent: H2O amb parells compartits
    ox, oy = 280, 85
    b += f'<circle cx="{ox}" cy="{oy}" r="26" fill="{RED}" stroke="{INK}" stroke-width="1.2"/>' + txt(ox, oy + 5, "O", 14, fill="#fff", weight=700)
    for dx in (-44, 44):
        hx, hy = ox + dx, oy + 30
        b += f'<circle cx="{hx}" cy="{hy}" r="16" fill="#fff" stroke="{INK}" stroke-width="1.2"/>' + txt(hx, hy + 4, "H", 12, weight=700)
        mx, my = ox + dx * 0.5, oy + 15
        b += f'<circle cx="{mx-3:.0f}" cy="{my:.0f}" r="3" fill="{BLUE}"/><circle cx="{mx+3:.0f}" cy="{my+3:.0f}" r="3" fill="{BLUE}"/>'
    b += txt(ox, 160, "Covalent", 12, weight=700) + txt(ox, 175, "parells d'electrons compartits", 9.5, fill=MUT)
    # metàl·lic
    random.seed(1)
    b += f'<rect x="400" y="25" width="150" height="110" rx="8" fill="#eef3fb" stroke="{INK}" stroke-width="1.2"/>'
    for i in range(5):
        for j in range(4):
            cx, cy = 418 + i * 29, 42 + j * 27
            b += f'<circle cx="{cx}" cy="{cy}" r="10" fill="{GRY}" stroke="{INK}" stroke-width="1"/>' + txt(cx, cy + 4, "+", 10, weight=700)
    for k in range(18): b += f'<circle cx="{404+random.uniform(0,142):.0f}" cy="{28+random.uniform(0,104):.0f}" r="2.6" fill="{BLUE}"/>'
    b += txt(475, 160, "Metàl·lic", 12, weight=700) + txt(475, 175, "cations i núvol d'electrons lliures", 9.5, fill=MUT)
    return svg(570, 182, b, "155mm")

def bateria_liti(A="#6C5CC9"):
    b = arrow_defs("al")
    b += f'<rect x="60" y="70" width="420" height="140" rx="12" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    b += f'<rect x="72" y="82" width="110" height="116" rx="6" fill="#3d3f44"/>' + txt(127, 228, "ànode (grafit)", 10.5, weight=700)
    b += f'<rect x="358" y="82" width="110" height="116" rx="6" fill="#4d6fa8"/>' + txt(413, 228, "càtode (LiCoO₂)", 10.5, weight=700)
    b += f'<rect x="182" y="82" width="176" height="116" fill="#e7f1fb"/>' + txt(270, 228, "electròlit", 10.5, fill=MUT)
    b += f'<line x1="270" y1="82" x2="270" y2="198" stroke="{INK}" stroke-width="2" stroke-dasharray="5 4"/>' + txt(270, 76, "separador", 9.5, fill=MUT)
    for y in (110, 140, 170):
        b += f'<circle cx="205" cy="{y}" r="8" fill="#f2c94c" stroke="{INK}" stroke-width="1"/>' + txt(205, y + 3.5, "Li⁺", 7.5, weight=700)
        b += f'<line x1="216" y1="{y}" x2="336" y2="{y}" stroke="{ORA}" stroke-width="1.8" marker-end="url(#al)"/>'
    b += f'<path d="M127 70 L127 30 L413 30 L413 70" fill="none" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<rect x="240" y="16" width="60" height="28" rx="5" fill="#fff" stroke="{INK}" stroke-width="1.5"/>' + txt(270, 35, "mòbil", 10.5, weight=700)
    b += f'<line x1="150" y1="22" x2="225" y2="22" stroke="{BLUE}" stroke-width="2" marker-end="url(#al)"/><line x1="315" y1="22" x2="395" y2="22" stroke="{BLUE}" stroke-width="2" marker-end="url(#al)"/>'
    b += txt(185, 14, "electrons pel circuit", 9.5, fill=BLUE) + txt(355, 14, "e⁻", 10, fill=BLUE)
    b += txt(270, 250, "En descàrrega: Li → Li⁺ + e⁻ a l'ànode; els Li⁺ van pel electròlit i els e⁻ pel circuit.", 9.5, fill=MUT)
    return svg(540, 258, b, "145mm")

# ================================================================= SdA 4
def col_lisions(A="#3F9A5A"):
    b = arrow_defs("ac")
    def mol(x, y, rot=0):
        return f'<g transform="translate({x},{y}) rotate({rot})"><circle cx="-9" cy="0" r="11" fill="{RED}" stroke="{INK}" stroke-width="1"/><circle cx="9" cy="0" r="11" fill="{RED}" stroke="{INK}" stroke-width="1"/></g>'
    def atom2(x, y, rot=0, c1=BLUE, c2="#fff"):
        return f'<g transform="translate({x},{y}) rotate({rot})"><circle cx="-8" cy="0" r="9" fill="{c1}" stroke="{INK}" stroke-width="1"/><circle cx="8" cy="0" r="9" fill="{c2}" stroke="{INK}" stroke-width="1"/></g>'
    cases = [("Xoc eficaç", "prou energia i bona orientació", True, 0), ("Orientació incorrecta", "reboten sense reaccionar", False, 90), ("Poca energia", "xoquen massa a poc a poc", False, 0)]
    for i, (t, sub, ok, rot) in enumerate(cases):
        x0 = 20 + i * 200
        b += f'<rect x="{x0}" y="10" width="180" height="150" rx="10" fill="#fff" stroke="{INK}" stroke-width="1.3"/>'
        r1, r2 = (90, 90) if i in (0, 2) else (0, 90)
        b += atom2(x0 + 45, 60, r1) + mol(x0 + 135, 60, r2)
        w = 2.4 if i != 2 else 1.1
        b += f'<line x1="{x0+(60 if r1==90 else 66)}" y1="60" x2="{x0+86}" y2="60" stroke="{INK}" stroke-width="{w}" marker-end="url(#ac)"/><line x1="{x0+120}" y1="60" x2="{x0+98}" y2="60" stroke="{INK}" stroke-width="{w}" marker-end="url(#ac)"/>'
        if ok: b += f'<text x="{x0+90}" y="113" font-size="20" text-anchor="middle" fill="{A}" font-weight="700">✓</text>' + atom2(x0 + 58, 138, 0, BLUE, RED) + atom2(x0 + 122, 138, 0, "#fff", RED)
        else: b += f'<text x="{x0+90}" y="125" font-size="22" text-anchor="middle" fill="{RED}" font-weight="700">✗</text>'
        b += txt(x0 + 90, 178, t, 11, weight=700) + txt(x0 + 90, 192, sub, 9.5, fill=MUT)
    return svg(620, 200, b, "160mm")

def diagrames_energia(A="#3F9A5A"):
    b = arrow_defs("ax") + arrow_defs("ad2", A)
    for i, (t, r, p) in enumerate((("Reacció exotèrmica", 150, 195), ("Reacció endotèrmica", 190, 140))):
        x0, y0 = 50 + i * 300, 230
        b += axes(x0, y0, 240, 200, "avenç de la reacció", "energia", idm="ax")
        peak = 60
        b += f'<path d="M{x0+10} {r} L{x0+60} {r} C{x0+95} {r} {x0+100} {peak} {x0+125} {peak} C{x0+150} {peak} {x0+155} {p} {x0+190} {p} L{x0+230} {p}" fill="none" stroke="{A}" stroke-width="3"/>'
        b += txt(x0 + 35, r - 8, "reactius", 10) + txt(x0 + 178, p - 8, "productes", 10, "end" if i == 0 else "middle")
        b += f'<line x1="{x0+125}" y1="{r}" x2="{x0+125}" y2="{peak+4}" stroke="{INK}" stroke-width="1.2" marker-end="url(#ax)"/>' + txt(x0 + 130, (r + peak) / 2 + 4, "Eₐ", 12, "start", weight=700)
        b += f'<line x1="{x0+60}" y1="{r}" x2="{x0+125}" y2="{r}" stroke="{GRY}" stroke-dasharray="3 3"/>'
        b += f'<line x1="{x0+228}" y1="{r}" x2="{x0+228}" y2="{p}" stroke="{ORA}" stroke-width="1.6" marker-end="url(#ax)"/>' + f'<line x1="{x0+190}" y1="{r}" x2="{x0+230}" y2="{r}" stroke="{GRY}" stroke-dasharray="3 3"/>'
        b += txt(x0 + 120, 268, t, 11.5, weight=700) + txt(x0 + 120, 283, "desprèn energia (l'entorn s'escalfa)" if i == 0 else "absorbeix energia (l'entorn es refreda)", 9.5, fill=MUT)
    return svg(600, 290, b, "160mm")

def sistema_obert_tancat(A="#3F9A5A"):
    b = ""
    for i, (t, m1, m2, closed) in enumerate((("Sistema obert", "150,0 g", "147,8 g", False), ("Sistema tancat", "250,0 g", "250,0 g", True))):
        x0 = 30 + i * 280
        b += f'<rect x="{x0}" y="150" width="200" height="34" rx="6" fill="#e6e8eb" stroke="{INK}" stroke-width="1.4"/><rect x="{x0+60}" y="158" width="80" height="18" rx="3" fill="#1f2328"/>' + f'<text x="{x0+100}" y="172" font-size="12" text-anchor="middle" fill="#7CFC9A" font-family="monospace">{m2}</text>'
        if closed:
            b += f'<path d="M{x0+75} 150 L{x0+75} 90 Q{x0+75} 70 {x0+90} 64 L{x0+90} 44 L{x0+110} 44 L{x0+110} 64 Q{x0+125} 70 {x0+125} 90 L{x0+125} 150 Z" fill="#fff" stroke="{INK}" stroke-width="1.6"/><rect x="{x0+86}" y="34" width="28" height="12" rx="2" fill="{A}" stroke="{INK}"/>'
            b += f'<rect x="{x0+77}" y="120" width="46" height="28" fill="#f3efe0"/>'
            for k in range(5): b += f'<circle cx="{x0+85+k*8}" cy="{100-k%2*14}" r="3" fill="#fff" stroke="{MUT}"/>'
        else:
            b += f'<path d="M{x0+60} 90 L{x0+60} 150 L{x0+140} 150 L{x0+140} 90" fill="none" stroke="{INK}" stroke-width="1.6"/><rect x="{x0+62}" y="118" width="76" height="30" fill="#f3efe0"/>'
            for k in range(6): b += f'<circle cx="{x0+72+k*11}" cy="{80-k%3*16}" r="3.5" fill="#fff" stroke="{MUT}"/>'
            b += txt(x0 + 160, 60, "el CO₂ s'escapa", 10, "start", MUT)
        b += txt(x0 + 100, 205, t, 11.5, weight=700) + txt(x0 + 100, 220, ("abans " + m1 + " → la massa baixa" if not closed else "abans " + m1 + " → la massa es conserva"), 9.5, fill=MUT)
    return svg(540, 228, b, "140mm")

def factors_velocitat(A="#3F9A5A"):
    random.seed(6)
    b = ""
    titles = [("Temperatura", "més ràpides → més xocs eficaços"), ("Concentració", "més partícules → més xocs"), ("Superfície de contacte", "trossos petits → més superfície")]
    for i, (t, sub) in enumerate(titles):
        x0 = 15 + i * 200
        for j in range(2):
            bx = x0 + j * 92
            b += f'<rect x="{bx}" y="15" width="84" height="84" rx="6" fill="#fff" stroke="{INK}" stroke-width="1.2"/>'
            if i == 0:
                for k in range(7):
                    cx, cy = bx + 12 + random.uniform(0, 60), 27 + random.uniform(0, 60)
                    L = 8 if j == 0 else 18
                    a = random.uniform(0, 6.28)
                    b += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="5" fill="{A}"/><line x1="{cx:.0f}" y1="{cy:.0f}" x2="{cx+L*math.cos(a):.0f}" y2="{cy+L*math.sin(a):.0f}" stroke="{INK}" stroke-width="1.1"/>'
            elif i == 1:
                for k in range(5 if j == 0 else 14):
                    b += f'<circle cx="{bx+12+random.uniform(0,60):.0f}" cy="{27+random.uniform(0,60):.0f}" r="5" fill="{A}"/>'
            else:
                if j == 0: b += f'<rect x="{bx+22}" y="37" width="40" height="40" fill="{GRY}" stroke="{INK}"/>'
                else:
                    for a in range(4):
                        for c in range(4): b += f'<rect x="{bx+12+c*17}" y="{27+a*17}" width="11" height="11" fill="{GRY}" stroke="{INK}" stroke-width=".8"/>'
            b += txt(bx + 42, 114, ("baixa" if i < 2 else "un tros") if j == 0 else ("alta" if i < 2 else "triturat"), 9.5, fill=MUT)
        b += txt(x0 + 88, 136, t, 11, weight=700) + txt(x0 + 88, 150, sub, 9.5, fill=MUT)
    return svg(610, 158, b, "160mm")

# ================================================================= SdA 5
def trajectoria_desplacament(A="#D14B66"):
    b = arrow_defs("at", A)
    b += f'<path d="M50 150 C100 40 170 190 230 90 S330 30 380 110" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>'
    b += f'<line x1="50" y1="150" x2="378" y2="111" stroke="{A}" stroke-width="2.6" marker-end="url(#at)"/>'
    b += f'<circle cx="50" cy="150" r="6" fill="{INK}"/><circle cx="380" cy="110" r="6" fill="{INK}"/>' + txt(50, 172, "inici", 10.5) + txt(392, 106, "final", 10.5, "start")
    b += f'<line x1="40" y1="200" x2="80" y2="200" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>' + txt(88, 204, "trajectòria (la seva longitud és la distància recorreguda)", 10.5, "start")
    b += f'<line x1="40" y1="222" x2="80" y2="222" stroke="{A}" stroke-width="2.6" marker-end="url(#at)"/>' + txt(88, 226, "desplaçament Δx (de la posició inicial a la final)", 10.5, "start", A, 700)
    return svg(470, 235, b, "120mm")

def grafiques_moviment(A="#D14B66"):
    b = arrow_defs("ax")
    plots = [("MRU · x–t", "x", lambda t: 20 + 0.9 * t, "recta: pendent = v"), ("MRU · v–t", "v", lambda t: 70, "horitzontal: v constant"),
             ("MRUA · x–t", "x", lambda t: 0.009 * t * t + 10, "corba (paràbola)"), ("MRUA · v–t", "v", lambda t: 10 + 0.75 * t, "recta: pendent = a")]
    for i, (t, yl, f, sub) in enumerate(plots):
        x0, y0 = 40 + i * 150, 140
        b += axes(x0, y0, 115, 115, "t", yl)
        pts = " ".join(f"{x0+tt:.0f},{y0-min(108,f(tt)):.0f}" for tt in range(0, 106, 3))
        b += f'<polyline points="{pts}" fill="none" stroke="{A}" stroke-width="2.6"/>'
        if i == 3: b += f'<polygon points="{x0},{y0} {pts} {x0+105},{y0}" fill="{A}" opacity=".15"/>'
        b += txt(x0 + 55, 165, t, 10.5, weight=700) + txt(x0 + 55, 179, sub, 9, fill=MUT)
    b += txt(330, 196, "A la gràfica v–t, l'àrea sota la línia és la distància recorreguda.", 9.5, fill=MUT)
    return svg(640, 202, b, "165mm")

def forces_resultant(A="#D14B66"):
    b = arrow_defs("af", A) + arrow_defs("ar2", INK)
    def box(x, y): return f'<rect x="{x-16}" y="{y-16}" width="32" height="32" rx="4" fill="#eef0f2" stroke="{INK}" stroke-width="1.3"/>'
    # mateix sentit
    b += box(80, 80) + f'<line x1="96" y1="72" x2="150" y2="72" stroke="{INK}" stroke-width="2" marker-end="url(#ar2)"/><line x1="96" y1="88" x2="130" y2="88" stroke="{INK}" stroke-width="2" marker-end="url(#ar2)"/>'
    b += f'<line x1="64" y1="125" x2="160" y2="125" stroke="{A}" stroke-width="3" marker-end="url(#af)"/>' + txt(110, 145, "R = 3 N + 2 N = 5 N", 10.5, weight=700) + txt(110, 160, "mateix sentit: se sumen", 9.5, fill=MUT)
    # sentits contraris
    x = 280
    b += box(x, 80) + f'<line x1="{x+16}" y1="80" x2="{x+70}" y2="80" stroke="{INK}" stroke-width="2" marker-end="url(#ar2)"/><line x1="{x-16}" y1="80" x2="{x-50}" y2="80" stroke="{INK}" stroke-width="2" marker-end="url(#ar2)"/>'
    b += f'<line x1="{x}" y1="125" x2="{x+20}" y2="125" stroke="{A}" stroke-width="3" marker-end="url(#af)"/>' + txt(x, 145, "R = 3 N − 2 N = 1 N", 10.5, weight=700) + txt(x, 160, "sentits contraris: es resten", 9.5, fill=MUT)
    # perpendiculars
    x = 470
    b += box(x, 100) + f'<line x1="{x+16}" y1="100" x2="{x+76}" y2="100" stroke="{INK}" stroke-width="2" marker-end="url(#ar2)"/><line x1="{x}" y1="84" x2="{x}" y2="30" stroke="{INK}" stroke-width="2" marker-end="url(#ar2)"/>'
    b += f'<line x1="{x+10}" y1="90" x2="{x+74}" y2="36" stroke="{A}" stroke-width="3" marker-end="url(#af)"/>' + txt(x + 82, 104, "4 N", 10, "start") + txt(x - 8, 40, "3 N", 10, "end")
    b += txt(x + 30, 145, "R = √(4² + 3²) = 5 N", 10.5, weight=700) + txt(x + 30, 160, "perpendiculars: Pitàgores", 9.5, fill=MUT)
    return svg(600, 168, b, "155mm")

def hooke(A="#D14B66"):
    b = arrow_defs("ax")
    b += f'<rect x="20" y="15" width="300" height="10" fill="{GRY}" stroke="{INK}"/>'
    def spring(x, L, m):
        n = 10; s = f'<line x1="{x}" y1="25" x2="{x}" y2="35" stroke="{INK}" stroke-width="1.6"/>'
        pts = [f"{x},35"] + [f"{x + (12 if k % 2 else -12)},{35 + (k + 0.5) * L / n:.0f}" for k in range(n)] + [f"{x},{35+L}"]
        s += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="1.6"/>'
        for j in range(m): s += f'<rect x="{x-14}" y="{35+L+j*16}" width="28" height="14" rx="2" fill="{A}" stroke="{INK}" stroke-width="1"/>'
        return s
    for i, (L, m) in enumerate(((60, 0), (85, 1), (110, 2), (135, 3))): b += spring(50 + i * 80, L, m)
    b += f'<line x1="20" y1="95" x2="320" y2="95" stroke="{GRY}" stroke-dasharray="3 3"/>' + txt(330, 98, "longitud inicial", 9.5, "start", MUT)
    b += txt(170, 250, "Cada massa igual allarga la molla el mateix: Δx és proporcional a F", 9.5, fill=MUT)
    # gràfica
    x0, y0 = 450, 210
    b += axes(x0, y0, 160, 170, "Δx (m)", "F (N)")
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0+140}" y2="{y0-150}" stroke="{A}" stroke-width="3"/>'
    for k in range(1, 4): b += f'<circle cx="{x0+k*40}" cy="{y0-k*43}" r="4" fill="{INK}"/>'
    b += txt(x0 + 95, y0 - 55, "pendent = k", 10.5, "start", A, 700)
    return svg(640, 258, b, "160mm")

def accio_reaccio(A="#D14B66"):
    b = arrow_defs("aa", A) + arrow_defs("ab3", BLUE)
    # patinador que empeny el terra
    b += f'<line x1="20" y1="170" x2="300" y2="170" stroke="{INK}" stroke-width="2"/>'
    b += f'<circle cx="120" cy="60" r="14" fill="#f2c9a0" stroke="{INK}"/><line x1="120" y1="74" x2="120" y2="120" stroke="{INK}" stroke-width="3"/><line x1="120" y1="120" x2="105" y2="160" stroke="{INK}" stroke-width="3"/><line x1="120" y1="120" x2="150" y2="166" stroke="{INK}" stroke-width="3"/>'
    b += f'<line x1="120" y1="90" x2="100" y2="110" stroke="{INK}" stroke-width="3"/><line x1="120" y1="90" x2="140" y2="108" stroke="{INK}" stroke-width="3"/>'
    b += f'<rect x="85" y="160" width="45" height="6" rx="3" fill="{GRY}"/><circle cx="92" cy="168" r="3" fill="{INK}"/><circle cx="123" cy="168" r="3" fill="{INK}"/>'
    b += f'<line x1="150" y1="178" x2="100" y2="178" stroke="{A}" stroke-width="2.4" marker-end="url(#aa)"/>' + txt(125, 196, "el peu empeny el terra enrere", 9.5, fill=A)
    b += f'<line x1="156" y1="150" x2="206" y2="150" stroke="{BLUE}" stroke-width="2.4" marker-end="url(#ab3)"/>' + txt(212, 146, "el terra empeny", 9.5, "start", BLUE) + txt(212, 159, "el patinador endavant", 9.5, "start", BLUE)
    b += f'<line x1="40" y1="40" x2="90" y2="40" stroke="{INK}" stroke-width="1.4" marker-end="url(#aa)"/>' + txt(40, 30, "sentit del moviment", 9, "start", MUT)
    # cèl·lula
    x0 = 360
    b += f'<rect x="{x0}" y="150" width="260" height="20" fill="#e6ddf3" stroke="{INK}"/>' + txt(x0 + 130, 188, "substrat", 9.5, fill=MUT)
    b += f'<path d="M{x0+40} 150 Q{x0+40} 95 {x0+120} 92 Q{x0+210} 95 {x0+230} 150 Z" fill="#f6d5dc" stroke="{INK}" stroke-width="1.5"/><circle cx="{x0+110}" cy="125" r="16" fill="#c98aa0" stroke="{INK}"/>'
    for xa in (x0 + 80, x0 + 180): b += f'<rect x="{xa-6}" y="146" width="12" height="6" fill="{INK}"/>'
    b += f'<line x1="{x0+175}" y1="160" x2="{x0+120}" y2="160" stroke="{A}" stroke-width="2.4" marker-end="url(#aa)"/>' + txt(x0 + 148, 208, "la cèl·lula estira el substrat enrere", 9.5, fill=A)
    b += f'<line x1="{x0+190}" y1="135" x2="{x0+250}" y2="135" stroke="{BLUE}" stroke-width="2.4" marker-end="url(#ab3)"/>' + txt(x0 + 225, 72, "el substrat estira", 9.5, "middle", BLUE) + txt(x0 + 225, 85, "la cèl·lula endavant", 9.5, "middle", BLUE)
    b += txt(320, 228, "Les dues forces són iguals, de sentit contrari i actuen sobre cossos diferents.", 9.5, fill=MUT)
    return svg(640, 232, b, "165mm")

def quimiotaxi(A="#D14B66"):
    random.seed(12)
    b = arrow_defs("aq", A)
    # gradient: punts més densos a prop dels bacteris (dreta)
    bx, by = 520, 110
    for k in range(260):
        r = abs(random.gauss(0, 110)); a = random.uniform(0, 6.28)
        x, y = bx + r * math.cos(a), by + r * math.sin(a) * 0.7
        if 20 < x < 620 and 15 < y < 205: b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.3" fill="#e9b949"/>'
    for (dx, dy, rot) in ((0, 0, 20), (22, -14, -30), (14, 18, 60)):
        b += f'<rect x="{bx+dx-14}" y="{by+dy-6}" width="28" height="12" rx="6" fill="{GRN}" stroke="{INK}" transform="rotate({rot} {bx+dx} {by+dy})"/>'
    b += txt(bx + 10, by + 52, "bacteris", 10.5, weight=700)
    # neutròfil
    nx, ny = 150, 115
    b += f'<path d="M{nx-50} {ny} Q{nx-55} {ny-40} {nx-5} {ny-42} Q{nx+50} {ny-45} {nx+60} {ny} Q{nx+50} {ny+42} {nx-5} {ny+40} Q{nx-50} {ny+38} {nx-50} {ny} Z" fill="#efe3f6" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<path d="M{nx+20} {ny-30} Q{nx+60} {ny-10} {nx+58} {ny+5} Q{nx+60} {ny+20} {nx+20} {ny+30}" fill="none" stroke="{A}" stroke-width="3"/>'
    for (x, y) in ((nx - 30, ny - 5), (nx - 15, ny + 10), (nx - 5, ny - 12)): b += f'<circle cx="{x}" cy="{y}" r="8" fill="#b48cc8" stroke="{INK}" stroke-width=".8"/>'
    b += f'<line x1="{nx+70}" y1="{ny}" x2="{nx+150}" y2="{ny}" stroke="{A}" stroke-width="3" marker-end="url(#aq)"/>'
    b += txt(nx, ny + 62, "neutròfil", 10.5, weight=700) + txt(nx + 112, ny + 22, "avança cap on n'hi ha més", 9.5, fill=A)
    b += txt(320, 222, "Els punts grocs són les molècules que alliberen els bacteris: la concentració és més alta a prop seu (gradient).", 9.5, fill=MUT)
    return svg(640, 230, b, "165mm")

# ================================================================= SdA 6
def energia_mecanica(A="#2F6DB5"):
    b = ""
    b += f'<path d="M30 40 Q120 40 170 140 Q220 230 300 230 Q380 230 430 140 Q470 70 530 70" fill="none" stroke="{INK}" stroke-width="3"/>'
    def bars(x, y, ep, lab):
        s = f'<line x1="{x-4}" y1="{y}" x2="{x+40}" y2="{y}" stroke="{INK}"/>'
        s += f'<rect x="{x}" y="{y-60*ep:.0f}" width="16" height="{60*ep:.0f}" fill="{ORA}"/><rect x="{x+20}" y="{y-60*(1-ep):.0f}" width="16" height="{60*(1-ep):.0f}" fill="{BLUE}"/>'
        return s + txt(x + 18, y + 14, lab, 9.5, fill=MUT)
    b += f'<circle cx="38" cy="29" r="10" fill="{A}" stroke="{INK}"/>' + bars(70, 120, 1.0, "a dalt")
    b += f'<circle cx="300" cy="219" r="10" fill="{A}" stroke="{INK}"/>' + bars(282, 180, 0.0, "a baix")
    b += f'<circle cx="452" cy="96" r="10" fill="{A}" stroke="{INK}"/>' + bars(470, 175, 0.72, "a mitja altura")
    b += f'<rect x="400" y="12" width="12" height="12" fill="{ORA}"/>' + txt(417, 22, "Eₚ (potencial)", 10, "start") + f'<rect x="400" y="30" width="12" height="12" fill="{BLUE}"/>' + txt(417, 40, "E꜀ (cinètica)", 10, "start")
    return svg(560, 250, b, "145mm")

def circuit_mesura(A="#2F6DB5"):
    b = ""
    b += f'<path d="M60 60 L400 60 L400 200 L60 200 Z" fill="none" stroke="{INK}" stroke-width="2"/>'
    # pila
    b += f'<rect x="210" y="190" width="40" height="20" fill="#fff"/><line x1="222" y1="184" x2="222" y2="216" stroke="{INK}" stroke-width="2.4"/><line x1="236" y1="190" x2="236" y2="210" stroke="{INK}" stroke-width="4"/>' + txt(230, 232, "generador (pila)", 10)
    # interruptor
    b += f'<rect x="70" y="110" width="0" height="0"/><circle cx="60" cy="100" r="3" fill="{INK}"/><circle cx="60" cy="150" r="3" fill="{INK}"/><rect x="54" y="103" width="12" height="44" fill="#fff"/><line x1="60" y1="100" x2="80" y2="140" stroke="{INK}" stroke-width="2"/>' + txt(86, 132, "interruptor", 10, "start")
    # bombeta
    b += f'<circle cx="210" cy="60" r="14" fill="#fff6c9" stroke="{INK}" stroke-width="1.8"/><line x1="200" y1="50" x2="220" y2="70" stroke="{INK}" stroke-width="1.4"/><line x1="220" y1="50" x2="200" y2="70" stroke="{INK}" stroke-width="1.4"/>' + txt(210, 32, "receptor (bombeta)", 10)
    # amperímetre en sèrie
    b += f'<circle cx="320" cy="60" r="14" fill="#fff" stroke="{A}" stroke-width="2"/>' + txt(320, 65, "A", 13, fill=A, weight=700) + txt(320, 95, "amperímetre", 9.5, fill=A) + txt(320, 108, "(en sèrie)", 9.5, fill=A)
    # voltímetre en paral·lel a la bombeta
    b += f'<path d="M180 60 L180 120 L195 120 M225 120 L240 120 L240 60" fill="none" stroke="{A}" stroke-width="1.6"/><circle cx="210" cy="120" r="14" fill="#fff" stroke="{A}" stroke-width="2"/>' + txt(210, 125, "V", 13, fill=A, weight=700) + txt(210, 150, "voltímetre (en paral·lel)", 9.5, fill=A)
    b += f'<path d="M400 120 l-6 -10 l12 0 Z" fill="{INK}"/>' + txt(412, 124, "sentit del corrent", 9.5, "start", MUT)
    return svg(520, 240, b, "135mm")

def fonts_energia(A="#2F6DB5"):
    b = ""
    items = [("Hidràulica", "renovable"), ("Eòlica", "renovable"), ("Solar fotovoltaica", "renovable"), ("Nuclear", "no renovable"), ("Cicle combinat (gas)", "no renovable")]
    for i, (t, r) in enumerate(items):
        x = 60 + i * 120; y = 70
        b += f'<circle cx="{x}" cy="{y}" r="44" fill="{"#e3f1e6" if r == "renovable" else "#f3e7e3"}" stroke="{INK}" stroke-width="1.3"/>'
        if i == 0:
            b += f'<path d="M{x-30} {y+20} L{x-30} {y-10} L{x-5} {y-25} L{x-5} {y+20} Z" fill="{GRY}" stroke="{INK}"/><rect x="{x-5}" y="{y-5}" width="35" height="25" fill="{WATER}"/>'
        elif i == 1:
            b += f'<line x1="{x}" y1="{y+30}" x2="{x}" y2="{y-8}" stroke="{INK}" stroke-width="3"/>'
            for a in (-90, 30, 150): b += f'<line x1="{x}" y1="{y-8}" x2="{x+26*math.cos(math.radians(a)):.0f}" y2="{y-8+26*math.sin(math.radians(a)):.0f}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
        elif i == 2:
            b += f'<circle cx="{x+18}" cy="{y-22}" r="9" fill="#f2c94c"/><polygon points="{x-30},{y+18} {x+20},{y+18} {x+30},{y-4} {x-20},{y-4}" fill="#3d5a99" stroke="{INK}"/>'
            for k in range(1, 4): b += f'<line x1="{x-30+k*12.5:.0f}" y1="{y+18}" x2="{x-20+k*12.5:.0f}" y2="{y-4}" stroke="#9fb6e6" stroke-width="1"/>'
        elif i == 3:
            b += f'<path d="M{x-28} {y+24} Q{x-18} {y-5} {x-24} {y-24} L{x+4} {y-24} Q{x-2} {y-5} {x+8} {y+24} Z" fill="#cfd3d8" stroke="{INK}"/><path d="M{x-14} {y-30} q8 -10 0 -16 q10 4 6 16" fill="#e8ecf0" stroke="{MUT}"/>'
        else:
            b += f'<rect x="{x-26}" y="{y-6}" width="36" height="30" fill="#cfd3d8" stroke="{INK}"/><rect x="{x+14}" y="{y-30}" width="9" height="54" fill="#9aa1a8" stroke="{INK}"/><path d="M{x-10} {y+6} q6 -12 12 0 q-6 6 -12 0" fill="{ORA}"/>'
        b += txt(x, y + 62, t, 10.5, weight=700) + txt(x, y + 76, r, 9.5, fill=GRN if r == "renovable" else RED)
    return svg(600, 155, b, "160mm")


def electrolisi_neta(A="#3F9A5A"):
    random.seed(8)
    LIQ = "#d6eaf8"
    b = arrow_defs("ael")
    # recipient i líquid (un sol color)
    b += f'<path d="M80 110 L80 250 Q80 266 96 266 L424 266 Q440 266 440 250 L440 110" fill="none" stroke="{INK}" stroke-width="2.2"/>'
    b += f'<path d="M82 140 L438 140 L438 250 Q438 264 424 264 L96 264 Q82 264 82 250 Z" fill="{LIQ}"/>'
    b += f'<line x1="82" y1="140" x2="438" y2="140" stroke="#9cc9e8" stroke-width="1.5"/>'
    # tubs capgirats: plens de líquid i amb el gas a dalt (H2 = el doble de volum que O2)
    def tub(cx, gas_h, lab):
        top, bot, r = 50, 230, 16
        s = f'<path d="M{cx-r} {bot} L{cx-r} {top+r} A{r} {r} 0 0 1 {cx+r} {top+r} L{cx+r} {bot}" fill="{LIQ}" stroke="none"/>'
        g = f'M{cx-r+1.5} {top+gas_h} L{cx-r+1.5} {top+r} A{r-1.5} {r-1.5} 0 0 1 {cx+r-1.5} {top+r} L{cx+r-1.5} {top+gas_h} Z'
        s += f'<path d="{g}" fill="#ffffff"/>'
        s += f'<line x1="{cx-r+1.5}" y1="{top+gas_h}" x2="{cx+r-1.5}" y2="{top+gas_h}" stroke="#9cc9e8" stroke-width="1.5"/>'
        for k in range(7):
            s += f'<circle cx="{cx+random.uniform(-9,9):.1f}" cy="{top+gas_h+12+k*(bot-top-gas_h-20)/7:.1f}" r="{random.uniform(1.6,3):.1f}" fill="#fff" stroke="#7fb3d9" stroke-width=".8"/>'
        s += f'<path d="M{cx-r} {bot} L{cx-r} {top+r} A{r} {r} 0 0 1 {cx+r} {top+r} L{cx+r} {bot}" fill="none" stroke="{INK}" stroke-width="1.8"/>'
        s += txt(cx, top + gas_h / 2 + 8, lab, 12, weight=700)
        # elèctrode
        s += f'<rect x="{cx-4}" y="205" width="8" height="59" fill="#8c9096" stroke="{INK}" stroke-width="1"/>'
        return s
    b += tub(200, 92, "H₂") + tub(320, 46, "O₂")
    # connexions i pila
    b += f'<path d="M200 264 L200 290 L40 290 L40 30 L190 30" fill="none" stroke="{INK}" stroke-width="1.6"/><path d="M320 264 L320 290 L480 290 L480 30 L330 30" fill="none" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<rect x="190" y="14" width="140" height="32" rx="5" fill="#f4f5f7" stroke="{INK}" stroke-width="1.8"/>' + txt(260, 35, "pila", 13, weight=700) + txt(202, 36, "−", 17, weight=700) + txt(318, 36, "+", 17, weight=700)
    b += txt(200, 310, "càtode (−)", 10.5) + txt(320, 310, "ànode (+)", 10.5)
    b += txt(500, 90, "hidrogen: el doble", 10.5, "start", INK, 700) + txt(500, 104, "de volum que l'oxigen", 10.5, "start") + f'<line x1="218" y1="100" x2="552" y2="96" stroke="{MUT}" stroke-width=".8" stroke-dasharray="3 3" opacity=".0"/>'
    b += txt(500, 150, "2 H₂O → 2 H₂ + O₂", 12, "start", A, 700)
    b += txt(500, 200, "aigua amb una mica de", 10, "start", MUT) + txt(500, 214, "carbonat de sodi", 10, "start", MUT) + txt(500, 228, "(perquè condueixi)", 10, "start", MUT)
    return svg(660, 318, b, "150mm")


def circuits_serie_paralel(A="#2F6DB5"):
    """Dues bombetes en sèrie i en paral·lel (amb la pila en una branca lateral, com als llibres)."""
    def bulb(x, y):
        return (f'<circle cx="{x}" cy="{y}" r="13" fill="#fff6c9" stroke="{INK}" stroke-width="1.8"/>'
                f'<line x1="{x-9}" y1="{y-9}" x2="{x+9}" y2="{y+9}" stroke="{INK}" stroke-width="1.5"/><line x1="{x-9}" y1="{y+9}" x2="{x+9}" y2="{y-9}" stroke="{INK}" stroke-width="1.5"/>')
    def pila_v(x, y):  # pila en un fil vertical: plaques horitzontals, + a dalt
        return (f'<rect x="{x-14}" y="{y-8}" width="28" height="16" fill="#fff"/><line x1="{x-16}" y1="{y-6}" x2="{x+16}" y2="{y-6}" stroke="{INK}" stroke-width="2.4"/>'
                f'<line x1="{x-9}" y1="{y+6}" x2="{x+9}" y2="{y+6}" stroke="{INK}" stroke-width="4.5"/>' + txt(x - 24, y - 6, "+", 12, weight=700) + txt(x - 24, y + 14, "−", 13, weight=700))
    b = ""
    # sèrie: rectangle amb la pila a l'esquerra i les dues bombetes a dalt
    b += f'<path d="M50 40 L250 40 L250 150 L50 150 Z" fill="none" stroke="{INK}" stroke-width="2"/>' + pila_v(50, 95) + bulb(115, 40) + bulb(190, 40)
    b += txt(115, 70, "B1", 11) + txt(190, 70, "B2", 11) + txt(150, 18, "Circuit en sèrie", 13, weight=700) + txt(150, 175, "un sol camí per al corrent", 10, fill=MUT)
    # paral·lel: escala amb la pila a l'esquerra i una bombeta a cada graó
    b += f'<path d="M340 40 L540 40 L540 150 L340 150 Z M440 40 L440 150" fill="none" stroke="{INK}" stroke-width="2"/>' + pila_v(340, 95) + bulb(440, 95) + bulb(540, 95)
    for x in (440, 540): b += f'<circle cx="{x}" cy="40" r="3" fill="{INK}"/><circle cx="{x}" cy="150" r="3" fill="{INK}"/>' if x == 440 else ""
    b += txt(462, 99, "B1", 11, "start") + txt(562, 99, "B2", 11, "start") + txt(450, 18, "Circuit en paral·lel", 13, weight=700) + txt(450, 175, "cada bombeta en una branca", 10, fill=MUT)
    return svg(600, 185, b, "140mm")
