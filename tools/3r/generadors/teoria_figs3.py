"""Il·lustracions vectorials dels dossiers de teoria de 2n d'ESO (mateix estil que teoria_figs i teoria_figs2)."""
import math, random
from teoria_figs import svg, txt, arrow_defs, INK, MUT, WATER, WATER2, OIL, GLASS
from teoria_figs2 import axes, BLUE, RED, ORA, GRN, PUR, GRY

LIQ = "#d6eaf8"

# ================================================================= 2n · SdA 1
def material_lab(A="#12857A"):
    """Material bàsic del laboratori, amb el nom i per a què serveix."""
    b = ""
    def lab(x, t, s):
        return txt(x, 168, t, 10.5, weight=700) + txt(x, 182, s, 9, fill=MUT)
    # vas de precipitats
    x = 50
    b += f'<path d="M{x-28} 70 L{x-28} 145 Q{x-28} 150 {x-23} 150 L{x+23} 150 Q{x+28} 150 {x+28} 145 L{x+28} 70" fill="none" stroke="{INK}" stroke-width="1.8"/><path d="M{x-32} 66 L{x-28} 70" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<path d="M{x-26.5} 110 L{x+26.5} 110 L{x+26.5} 145 Q{x+26.5} 148.5 {x+23} 148.5 L{x-23} 148.5 Q{x-26.5} 148.5 {x-26.5} 145 Z" fill="{LIQ}"/>'
    for k in range(3): b += f'<line x1="{x-26}" y1="{125-k*15}" x2="{x-16}" y2="{125-k*15}" stroke="{MUT}" stroke-width="1"/>'
    b += lab(x, "Vas de precipitats", "escalfar, dissoldre")
    # erlenmeyer
    x = 150
    b += f'<path d="M{x-8} 60 L{x-8} 92 L{x-32} 146 Q{x-34} 150 {x-29} 150 L{x+29} 150 Q{x+34} 150 {x+32} 146 L{x+8} 92 L{x+8} 60" fill="none" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<path d="M{x-21} 122 L{x+21} 122 L{x+31} 145 Q{x+32} 148.5 {x+28} 148.5 L{x-28} 148.5 Q{x-32} 148.5 {x-31} 145 Z" fill="{LIQ}"/>'
    b += lab(x, "Erlenmeyer", "agitar sense vessar")
    # proveta
    x = 245
    b += f'<rect x="{x-11}" y="30" width="22" height="115" fill="none" stroke="{INK}" stroke-width="1.8"/><path d="M{x-26} 150 L{x+26} 150 L{x+20} 144 L{x-20} 144 Z" fill="#eef0f2" stroke="{INK}" stroke-width="1.4"/>'
    b += f'<rect x="{x-10}" y="85" width="20" height="59" fill="{LIQ}"/>'
    for k in range(10): b += f'<line x1="{x-11}" y1="{40+k*10}" x2="{x-3 if k % 5 else x+2}" y2="{40+k*10}" stroke="{MUT}" stroke-width=".9"/>'
    b += lab(x, "Proveta", "mesurar volums")
    # pipeta i pera
    x = 330
    b += f'<line x1="{x}" y1="40" x2="{x}" y2="150" stroke="{INK}" stroke-width="5"/><line x1="{x}" y1="40" x2="{x}" y2="150" stroke="#fff" stroke-width="2.4"/><line x1="{x}" y1="110" x2="{x}" y2="150" stroke="{LIQ}" stroke-width="2.4"/>'
    b += f'<ellipse cx="{x}" cy="30" rx="11" ry="14" fill="{RED}" stroke="{INK}" stroke-width="1.4"/>'
    b += lab(x, "Pipeta i pera", "volums petits i exactes")
    # balança
    x = 425
    b += f'<rect x="{x-40}" y="118" width="80" height="32" rx="5" fill="#eef0f2" stroke="{INK}" stroke-width="1.8"/><rect x="{x-24}" y="128" width="48" height="14" rx="2" fill="#2f3a40"/>'
    b += txt(x, 139, "12,40 g", 10, fill="#7fffd4", weight=700) + f'<rect x="{x-32}" y="110" width="64" height="6" rx="2" fill="#c9ced3" stroke="{INK}" stroke-width="1.2"/><line x1="{x}" y1="116" x2="{x}" y2="118" stroke="{INK}"/>'
    b += lab(x, "Balança", "mesurar masses")
    # embut i filtre
    x = 520
    b += f'<path d="M{x-30} 70 L{x+30} 70 L{x+4} 112 L{x+4} 150 L{x-4} 150 L{x-4} 112 Z" fill="#fff" stroke="{INK}" stroke-width="1.8"/><path d="M{x-24} 74 L{x+24} 74 L{x} 108 Z" fill="#f5f0e1" stroke="{MUT}" stroke-width="1"/>'
    b += lab(x, "Embut i paper", "filtrar")
    return svg(570, 190, b, "165mm")

def escala_longitud(A="#12857A"):
    """Unitats de longitud: cada unitat val 10 vegades la següent."""
    b = arrow_defs("el", A) + arrow_defs("el2", MUT)
    U = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    for i, u in enumerate(U):
        x = 20 + i * 84
        b += f'<rect x="{x}" y="60" width="62" height="34" rx="6" fill="{"#fff" if u != "m" else A}" stroke="{INK}" stroke-width="1.5"/>'
        b += txt(x + 31, 82, u, 13, fill=("#fff" if u == "m" else INK), weight=700)
        if i < 6:
            b += f'<path d="M{x+40} 98 Q{x+73} 124 {x+104} 98" fill="none" stroke="{A}" stroke-width="1.8" marker-end="url(#el)"/>' + txt(x + 73, 128, "· 10", 10, fill=A, weight=700)
            b += f'<path d="M{x+104} 56 Q{x+73} 30 {x+40} 56" fill="none" stroke="{MUT}" stroke-width="1.4" marker-end="url(#el2)"/>' + txt(x + 73, 34, ": 10", 10, fill=MUT)
    b += txt(20, 160, "Cap a la dreta (unitat més petita) multipliquem per 10 a cada salt; cap a l'esquerra, dividim per 10.", 10.5, "start")
    b += txt(20, 178, "Superfície (m²): cada salt · 100.   Volum (m³): cada salt · 1 000.", 10.5, "start", A, 700)
    return svg(610, 186, b, "155mm")

def litre_dm3(A="#12857A"):
    """Un cub d'1 dm d'aresta: hi cap exactament 1 litre i s'hi poden posar 1 000 cubets d'1 cm³."""
    b = ""
    s, dx, dy = 120, 50, -36
    x0, y0 = 60, 70
    def P(x, y): return f"{x:.0f},{y:.0f}"
    # cub en perspectiva
    b += f'<polygon points="{P(x0,y0)} {P(x0+s,y0)} {P(x0+s,y0+s)} {P(x0,y0+s)}" fill="{LIQ}" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<polygon points="{P(x0,y0)} {P(x0+dx,y0+dy)} {P(x0+s+dx,y0+dy)} {P(x0+s,y0)}" fill="#e8f3fb" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<polygon points="{P(x0+s,y0)} {P(x0+s+dx,y0+dy)} {P(x0+s+dx,y0+s+dy)} {P(x0+s,y0+s)}" fill="#bcdcf1" stroke="{INK}" stroke-width="1.8"/>'
    for k in range(1, 10):
        b += f'<line x1="{x0+k*s/10:.0f}" y1="{y0}" x2="{x0+k*s/10:.0f}" y2="{y0+s}" stroke="#9cc9e8" stroke-width=".6"/><line x1="{x0}" y1="{y0+k*s/10:.0f}" x2="{x0+s}" y2="{y0+k*s/10:.0f}" stroke="#9cc9e8" stroke-width=".6"/>'
    b += txt(x0 + s / 2, y0 + s + 18, "1 dm = 10 cm", 10.5) + txt(x0 + s + dx + 8, y0 + s / 2 + dy / 2 + 4, "1 dm", 10.5, "start")
    b += txt(300, 80, "V = 1 dm · 1 dm · 1 dm = 1 dm³", 11.5, "start", INK, 700)
    b += txt(300, 104, "Hi cap exactament 1 litre d'aigua:", 10.5, "start") + txt(300, 122, "1 dm³ = 1 L", 12, "start", A, 700)
    b += txt(300, 150, "Hi caben 10 · 10 · 10 = 1 000 cubets d'1 cm³:", 10.5, "start") + txt(300, 168, "1 cm³ = 1 mL", 12, "start", A, 700)
    b += txt(300, 196, "I en un cub d'1 m hi caben 1 000 L: 1 m³ = 1 000 L", 10.5, "start", MUT)
    return svg(600, 220, b, "150mm")

# ================================================================= 2n · SdA 2
def grafica_massa_volum(A="#B83A7A"):
    b = arrow_defs("ax")
    x0, y0 = 60, 210
    b += axes(x0, y0, 300, 190, "V (mL)", "m (g)")
    for k in range(1, 5):
        b += f'<line x1="{x0+k*65}" y1="{y0}" x2="{x0+k*65}" y2="{y0+5}" stroke="{INK}"/>' + txt(x0 + k * 65, y0 + 17, str(20 * k), 9.5)
        b += f'<line x1="{x0-5}" y1="{y0-k*40}" x2="{x0}" y2="{y0-k*40}" stroke="{INK}"/>' + txt(x0 - 8, y0 - k * 40 + 4, str(25 * k), 9.5, "end")
    # glicerina d = 1,26 ; oli d = 0,92
    for d, col, lab in ((1.26, A, "glicerina: d = 1,26 g/mL"), (0.92, "#c4921c", "oli: d = 0,92 g/mL")):
        sc = 40 / 25
        pts = [(x0 + k * 65, y0 - d * 20 * k * sc) for k in range(0, 5)]
        b += f'<line x1="{pts[0][0]}" y1="{pts[0][1]:.0f}" x2="{pts[4][0]+14}" y2="{pts[4][1]+(pts[4][1]-pts[3][1])*14/65:.0f}" stroke="{col}" stroke-width="2.4"/>'
        for (px, py) in pts[1:]: b += f'<circle cx="{px}" cy="{py:.0f}" r="4.5" fill="#fff" stroke="{col}" stroke-width="2"/>'
        b += txt(pts[4][0] + 20, pts[4][1] + (-14 if d > 1 else 22), lab, 10, "start", col, 700)
    b += txt(500, 100, "Els punts de cada líquid", 10.5, "start") + txt(500, 115, "fan una recta que passa", 10.5, "start") + txt(500, 130, "per l'origen.", 10.5, "start")
    b += txt(500, 155, "Pendent = m / V = densitat.", 10.5, "start", INK, 700) + txt(500, 170, "Més pendent, més dens.", 10.5, "start", MUT)
    return svg(650, 232, b, "155mm")

def sura_enfonsa(A="#B83A7A"):
    """Objectes en aigua: suren si la seva densitat és menor que la de l'aigua."""
    b = ""
    b += f'<path d="M30 60 L30 200 Q30 210 40 210 L540 210 Q550 210 550 200 L550 60" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<rect x="31.5" y="90" width="517" height="118.5" fill="{LIQ}"/><line x1="31.5" y1="90" x2="548.5" y2="90" stroke="#9cc9e8" stroke-width="1.5"/>'
    items = [("suro", 0.24, "#c99a5b"), ("fusta de pi", 0.5, "#e1b878"), ("gel", 0.92, "#eaf6ff"), ("plàstic PET", 1.38, "#8fd1c1"), ("ferro", 7.87, "#8c9096")]
    for i, (n, d, c) in enumerate(items):
        x = 80 + i * 105
        if d < 1:
            sub = 40 * d; y = 90 - (40 - sub)
        else:
            y = 208 - 40
        if n == "gel":
            b += f'<path d="M{x-24} {y} L{x+22} {y-2} L{x+26} {y+40} L{x-20} {y+40} Z" fill="{c}" stroke="{INK}" stroke-width="1.4"/>'
        else:
            b += f'<rect x="{x-24}" y="{y}" width="48" height="40" rx="{4 if n != "ferro" else 2}" fill="{c}" stroke="{INK}" stroke-width="1.4"/>'
        b += txt(x, 38, n, 10.5, weight=700) + txt(x, 52, f"d = {str(d).replace('.', ',')} g/cm³", 9, fill=MUT)
    b += f'<rect x="31.5" y="90" width="517" height="118.5" fill="{LIQ}" opacity=".35"/>'
    b += txt(290, 232, "aigua: d = 1,00 g/cm³ · els menys densos que l'aigua suren; els més densos s'enfonsen", 10, fill=MUT)
    return svg(580, 242, b, "160mm")

def densimetre(A="#B83A7A"):
    """El densímetre s'enfonsa menys com més dens és el líquid. L'ou sura en aigua salada."""
    b = ""
    def prov(x, top, col, lab, lvl):
        s = f'<path d="M{x-35} 40 L{x-35} 210 Q{x-35} 216 {x-29} 216 L{x+29} 216 Q{x+35} 216 {x+35} 210 L{x+35} 40" fill="none" stroke="{INK}" stroke-width="1.8"/>'
        s += f'<rect x="{x-33.5}" y="70" width="67" height="144.5" fill="{col}"/>'
        # densímetre
        s += f'<rect x="{x-5}" y="{top}" width="10" height="70" rx="2" fill="#fff" stroke="{INK}" stroke-width="1.3"/>'
        for k in range(6): s += f'<line x1="{x-5}" y1="{top+8+k*10}" x2="{x}" y2="{top+8+k*10}" stroke="{MUT}" stroke-width=".8"/>'
        s += f'<ellipse cx="{x}" cy="{top+88}" rx="13" ry="20" fill="#fff" stroke="{INK}" stroke-width="1.3"/><circle cx="{x}" cy="{top+104}" r="6" fill="#555"/>'
        s += f'<line x1="{x-33.5}" y1="70" x2="{x+33.5}" y2="70" stroke="#9cc9e8" stroke-width="1.5"/>'
        s += txt(x, 236, lab, 10.5, weight=700) + txt(x, 250, lvl, 9.5, fill=MUT)
        return s
    b += prov(70, 30, "#eaf2f9", "alcohol", "s'enfonsa més") + prov(180, 10, LIQ, "aigua", "1,00") + prov(290, -6, "#bfe0f2", "aigua salada", "sura més")
    # ous
    def got(x, col, ouy, lab):
        s = f'<path d="M{x-40} 110 L{x-34} 214 L{x+34} 214 L{x+40} 110" fill="none" stroke="{INK}" stroke-width="1.8"/><path d="M{x-38} 130 L{x+38} 130 L{x+33.5} 212.5 L{x-33.5} 212.5 Z" fill="{col}"/>'
        s += f'<ellipse cx="{x}" cy="{ouy}" rx="14" ry="18" fill="#f6ead7" stroke="{INK}" stroke-width="1.4"/>' + txt(x, 236, lab, 10.5, weight=700)
        return s
    b += got(430, LIQ, 194, "aigua de l'aixeta") + got(540, "#b5d9f0", 140, "aigua amb molta sal")
    b += txt(485, 252, "l'ou (d ≈ 1,03 g/cm³) sura si el líquid és més dens", 9.5, fill=MUT)
    return svg(600, 262, b, "160mm")

# ================================================================= 2n · SdA 3
def canvis_estat(A="#D9731A"):
    b = arrow_defs("ce", A) + arrow_defs("cf", BLUE)
    pos = {"Sòlid": (90, 180), "Líquid": (300, 40), "Gas": (510, 180)}
    for k, (x, y) in pos.items():
        b += f'<rect x="{x-55}" y="{y-20}" width="110" height="40" rx="20" fill="#fff" stroke="{INK}" stroke-width="1.8"/>' + txt(x, y + 5, k, 13, weight=700)
    def arr(x1, y1, x2, y2, lab, col, mk, dx=0, dy=0, anchor="middle"):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2.2" marker-end="url(#{mk})"/>' + txt((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, lab, 10.5, anchor, col, 700)
    b += arr(120, 156, 250, 62, "fusió", A, "ce", -30, -6)
    b += arr(258, 74, 132, 166, "solidificació", BLUE, "cf", 34, 22)
    b += arr(350, 62, 480, 156, "vaporització", A, "ce", 40, -10)
    b += arr(470, 166, 342, 74, "condensació", BLUE, "cf", -30, 24)
    b += arr(150, 176, 450, 176, "sublimació", A, "ce", 0, -8)
    b += arr(450, 192, 150, 192, "sublimació inversa", BLUE, "cf", 0, 20)
    b += txt(20, 250, "Taronja: absorbeix calor (cal escalfar).", 10, "start", A, 700) + txt(330, 250, "Blau: desprèn calor (es refreda).", 10, "start", BLUE, 700)
    return svg(620, 260, b, "150mm")

def pressio_pilota(A="#D9731A"):
    """L'aire de dins de la pilota: amb fred, partícules més lentes, menys xocs i menys pressió."""
    random.seed(4)
    b = arrow_defs("pp", INK)
    for j, (t, n, L, lab, sub) in enumerate(((0, 14, 10, "Pilota freda (5 °C)", "més lentes: xocs menys forts i menys sovint"), (1, 14, 20, "Pilota a 25 °C", "més ràpides: més xocs contra la paret"))):
        cx, cy, R = 120 + j * 300, 110, 85
        b += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{"#eef5fb" if j == 0 else "#fdf0e4"}" stroke="{INK}" stroke-width="3"/>'
        pts = []
        while len(pts) < n:
            a, r = random.uniform(0, 6.28), random.uniform(0, R - 10 - L)
            p = (cx + r * math.cos(a), cy + r * math.sin(a))
            if all((p[0]-q[0])**2 + (p[1]-q[1])**2 > 300 for q in pts): pts.append(p)
        for (px, py) in pts:
            ang = random.uniform(0, 6.28)
            b += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="6" fill="{BLUE if j == 0 else A}" stroke="{INK}" stroke-width=".8"/>'
            b += f'<line x1="{px+8*math.cos(ang):.0f}" y1="{py+8*math.sin(ang):.0f}" x2="{px+(8+L)*math.cos(ang):.0f}" y2="{py+(8+L)*math.sin(ang):.0f}" stroke="{INK}" stroke-width="1.2" marker-end="url(#pp)"/>'
        b += txt(cx, 215, lab, 11.5, weight=700) + txt(cx, 230, sub, 9.5, fill=MUT)
    return svg(540, 238, b, "145mm")

def escales_temperatura(A="#D9731A"):
    b = ""
    def term(x, lab, vals):
        s = f'<rect x="{x-9}" y="20" width="18" height="190" rx="9" fill="#fff" stroke="{INK}" stroke-width="1.6"/><circle cx="{x}" cy="222" r="15" fill="{RED}" stroke="{INK}" stroke-width="1.6"/><rect x="{x-4}" y="120" width="8" height="100" fill="{RED}"/>'
        for (y, v) in vals: s += f'<line x1="{x+9}" y1="{y}" x2="{x+20}" y2="{y}" stroke="{INK}" stroke-width="1.2"/>' + txt(x + 24, y + 4, v, 10.5, "start")
        return s + txt(x, 256, lab, 11.5, weight=700)
    ys = [(40, "100"), (120, "0"), (190, "−273")]
    b += term(110, "Celsius (°C)", [(40, "100 °C"), (120, "0 °C"), (190, "−273 °C")])
    b += term(330, "Kelvin (K)", [(40, "373 K"), (120, "273 K"), (190, "0 K")])
    for (y, t) in ((40, "l'aigua bull"), (120, "el gel es fon"), (190, "zero absolut")):
        b += f'<line x1="180" y1="{y}" x2="320" y2="{y}" stroke="{MUT}" stroke-width=".9" stroke-dasharray="4 3"/>' + txt(250, y - 5, t, 9.5, fill=MUT)
    b += txt(440, 110, "T (K) = t (°C) + 273", 12.5, "start", A, 700)
    b += txt(440, 135, "Al zero absolut les partícules", 10, "start") + txt(440, 150, "pràcticament no es mouen.", 10, "start")
    b += txt(440, 175, "No hi ha temperatures negatives", 10, "start") + txt(440, 190, "en kelvin.", 10, "start")
    return svg(640, 266, b, "150mm")

# ================================================================= 2n · SdA 4
def dissolucio(A="#2F6FB5"):
    random.seed(9)
    b = arrow_defs("ds")
    def got(x, sal, aigua):
        s = f'<path d="M{x-48} 40 L{x-42} 160 Q{x-41} 166 {x-35} 166 L{x+35} 166 Q{x+41} 166 {x+42} 160 L{x+48} 40" fill="none" stroke="{INK}" stroke-width="1.8"/>'
        if aigua: s += f'<path d="M{x-46.5} 70 L{x+46.5} 70 L{x+40.5} 160 Q{x+40} 164.5 {x+35} 164.5 L{x-35} 164.5 Q{x-40} 164.5 {x-40.5} 160 Z" fill="{LIQ}"/>'
        return s
    b += got(80, 0, 1) + txt(80, 186, "dissolvent (aigua)", 10.5, weight=700)
    b += txt(160, 110, "+", 22, weight=700)
    # sal
    b += f'<path d="M210 150 L250 150 L240 120 L220 120 Z" fill="#fff" stroke="{INK}" stroke-width="1.4"/>'
    for k in range(9): b += f'<rect x="{214+(k%5)*7}" y="{140-(k//5)*7}" width="5" height="5" fill="#fff" stroke="{MUT}" stroke-width=".8"/>'
    b += txt(230, 186, "solut (sal)", 10.5, weight=700)
    b += f'<line x1="275" y1="105" x2="325" y2="105" stroke="{INK}" stroke-width="2" marker-end="url(#ds)"/>'
    b += got(400, 1, 1)
    for k in range(60):
        px, py = 400 + random.uniform(-36, 36), 78 + random.uniform(0, 80)
        b += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="2" fill="{BLUE}" opacity=".55"/>'
    for k in range(14):
        px, py = 400 + random.uniform(-34, 34), 82 + random.uniform(0, 76)
        b += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="3.2" fill="{ORA}" stroke="{INK}" stroke-width=".5"/>'
    b += txt(400, 186, "dissolució (aigua salada)", 10.5, weight=700)
    b += txt(470, 100, "Les partícules de solut es", 10, "start") + txt(470, 114, "reparteixen entre les de", 10, "start") + txt(470, 128, "l'aigua: no es veuen, però", 10, "start") + txt(470, 142, "hi són (la massa es conserva).", 10, "start")
    return svg(640, 196, b, "150mm")

def corba_solubilitat(A="#2F6FB5"):
    b = arrow_defs("ax")
    x0, y0 = 70, 230
    b += axes(x0, y0, 330, 205, "T (°C)", "")
    b += txt(x0 - 6, 14, "solubilitat (g en 100 g d'aigua)", 10.5, "start")
    sx, sy = 3, 0.75
    for k in range(0, 6):
        b += f'<line x1="{x0+k*60}" y1="{y0}" x2="{x0+k*60}" y2="{y0+5}" stroke="{INK}"/>' + txt(x0 + k * 60, y0 + 17, str(20 * k), 9.5)
    for k in range(1, 6):
        b += f'<line x1="{x0-5}" y1="{y0-k*50*sy}" x2="{x0+320}" y2="{y0-k*50*sy}" stroke="#e3e6ea"/>' + txt(x0 - 8, y0 - k * 50 * sy + 4, str(50 * k), 9.5, "end")
    def curve(data, col, lab, lx, ly):
        pts = " ".join(f"{x0+t*sx:.0f},{y0-v*sy:.0f}" for t, v in data)
        return f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.6" stroke-linejoin="round"/>' + txt(lx, ly, lab, 10.5, "start", col, 700)
    kno3 = [(0, 13.3), (10, 20.9), (20, 31.6), (30, 45.8), (40, 63.9), (50, 85.5), (60, 110), (70, 138), (80, 169), (90, 202), (100, 246)]
    kno3 = [(t, v) for t, v in kno3 if v <= 255]
    b += curve(kno3, A, "nitrat de potassi", x0 + 150, 50)
    b += curve([(0, 35.7), (20, 35.9), (40, 36.4), (60, 37.1), (80, 38.0), (100, 39.2)], ORA, "sal (clorur de sodi)", x0 + 200, y0 - 40 * sy - 6)
    px, py = x0 + 40 * sx, y0 - 63.9 * sy
    b += f'<line x1="{px}" y1="{y0}" x2="{px}" y2="{py:.0f}" stroke="{MUT}" stroke-dasharray="4 3"/><line x1="{x0}" y1="{py:.0f}" x2="{px}" y2="{py:.0f}" stroke="{MUT}" stroke-dasharray="4 3"/><circle cx="{px}" cy="{py:.0f}" r="4.5" fill="{A}"/>'
    b += txt(430, 90, "A 40 °C es dissolen fins a", 10, "start") + txt(430, 104, "64 g de nitrat de potassi", 10, "start") + txt(430, 118, "en 100 g d'aigua.", 10, "start")
    b += txt(430, 145, "Damunt de la corba: saturada", 10, "start", INK, 700) + txt(430, 159, "(el que sobra queda al fons).", 10, "start", MUT)
    b += txt(430, 186, "La sal gairebé no canvia", 10, "start") + txt(430, 200, "amb la temperatura.", 10, "start")
    return svg(640, 252, b, "150mm")

def destillacio(A="#2F6FB5"):
    b = arrow_defs("dt", BLUE)
    # matràs i flama
    b += f'<circle cx="90" cy="130" r="42" fill="#fff" stroke="{INK}" stroke-width="1.8"/><path d="M52 145 A42 42 0 0 0 128 145 Z" fill="{LIQ}"/><rect x="82" y="40" width="16" height="52" fill="#fff" stroke="{INK}" stroke-width="1.8"/><rect x="83.5" y="90" width="13" height="6" fill="#fff"/>'
    b += f'<path d="M90 200 q-14 -10 -7 -26 q3 9 7 5 q-3 -12 5 -19 q3 12 9 16 q5 15 -14 24 Z" fill="#f5a142" stroke="{ORA}" stroke-width="1.2"/><rect x="80" y="200" width="20" height="18" fill="#8c9096" stroke="{INK}" stroke-width="1.2"/><rect x="66" y="218" width="48" height="6" rx="2" fill="#6b7076" stroke="{INK}"/>' + txt(130, 214, "escalfem", 10, "start", MUT)
    b += f'<rect x="76" y="28" width="28" height="12" rx="2" fill="#c9ced3" stroke="{INK}"/><line x1="90" y1="18" x2="90" y2="60" stroke="{INK}" stroke-width="1.4"/>' + txt(112, 22, "termòmetre", 9.5, "start", MUT)
    # refrigerant
    b += f'<line x1="98" y1="62" x2="360" y2="150" stroke="{INK}" stroke-width="7"/><line x1="98" y1="62" x2="360" y2="150" stroke="#fff" stroke-width="4"/>'
    b += f'<polygon points="150,62 330,122 320,152 140,92" fill="#e6f2fb" stroke="{INK}" stroke-width="1.5"/><line x1="98" y1="62" x2="360" y2="150" stroke="{INK}" stroke-width="7" opacity=".0"/>'
    b += f'<line x1="135" y1="74" x2="345" y2="144" stroke="#fff" stroke-width="4"/><line x1="135" y1="71.5" x2="345" y2="141.5" stroke="{INK}" stroke-width="1"/><line x1="135" y1="76.5" x2="345" y2="146.5" stroke="{INK}" stroke-width="1"/>'
    b += f'<line x1="318" y1="150" x2="318" y2="172" stroke="{INK}" stroke-width="1.4" marker-end="url(#dt)"/>' + txt(318, 186, "entra aigua freda", 9.5, fill=BLUE)
    b += f'<line x1="160" y1="70" x2="160" y2="44" stroke="{INK}" stroke-width="1.4" marker-end="url(#dt)"/>' + txt(170, 40, "surt aigua tèbia", 9.5, "start", BLUE)
    b += txt(240, 70, "refrigerant", 10.5, weight=700)
    # recollida
    b += f'<path d="M350 150 L380 158" stroke="{INK}" stroke-width="2"/><path d="M360 170 L366 230 L414 230 L420 170" fill="none" stroke="{INK}" stroke-width="1.8"/><path d="M362 205 L418 205 L414 228.5 L366 228.5 Z" fill="#eaf5fd"/>'
    for k in range(3): b += f'<circle cx="381" cy="{166+k*12}" r="2.5" fill="{BLUE}"/>'
    b += txt(390, 250, "líquid destil·lat", 10, weight=700)
    b += txt(440, 70, "1. El líquid bull i es fa vapor.", 10, "start") + txt(440, 90, "2. El vapor es refreda al", 10, "start") + txt(440, 104, "   refrigerant i condensa.", 10, "start") + txt(440, 124, "3. Recollim el líquid pur;", 10, "start") + txt(440, 138, "   les sals queden al matràs.", 10, "start")
    return svg(640, 260, b, "155mm")

def potabilitzadora(A="#2F6FB5"):
    b = arrow_defs("pt", A)
    steps = [("Captació", "aigua del riu"), ("Decantació", "els fangs es dipositen"), ("Filtració", "sorra i carbó actiu"), ("Desinfecció", "clor o ozó"), ("Dipòsit", "aigua potable a l'aixeta")]
    for i, (t, s) in enumerate(steps):
        x = 20 + i * 122
        b += f'<rect x="{x}" y="30" width="104" height="70" rx="8" fill="{"#fff" if i < 4 else LIQ}" stroke="{A}" stroke-width="1.8"/>' + txt(x + 52, 58, t, 11, weight=700) + txt(x + 52, 76, s.split(" ")[0] + " " + " ".join(s.split(" ")[1:2]), 9, fill=MUT) + txt(x + 52, 89, " ".join(s.split(" ")[2:]), 9, fill=MUT)
        if i < 4: b += f'<line x1="{x+106}" y1="65" x2="{x+120}" y2="65" stroke="{A}" stroke-width="2" marker-end="url(#pt)"/>'
    b += txt(320, 128, "ETAP (potabilitzadora): fa l'aigua apta per beure.  EDAR (depuradora): neteja l'aigua bruta abans de tornar-la al riu.", 9.5, fill=MUT)
    return svg(640, 140, b, "165mm")

# ================================================================= 2n · SdA 5
def evidencies(A="#B7791F"):
    b = ""
    items = [("canvi de color", "pa que es torra"), ("gas (bombolles)", "bicarbonat + vinagre"), ("calor", "una combustió"), ("llum", "una espurna"), ("sòlid nou", "un precipitat"), ("olor nova", "aliment que es fa malbé")]
    for i, (t, s) in enumerate(items):
        x = 15 + i * 100
        cx, cy = x + 45, 55
        b += f'<circle cx="{cx}" cy="{cy}" r="34" fill="#fff" stroke="{A}" stroke-width="2"/>'
        if i == 0:
            b += f'<rect x="{cx-22}" y="{cy-16}" width="20" height="32" rx="6" fill="#f3dfb5" stroke="{INK}"/><rect x="{cx+2}" y="{cy-16}" width="20" height="32" rx="6" fill="#9c5a1f" stroke="{INK}"/>'
        elif i == 1:
            b += f'<path d="M{cx-14} {cy-12} L{cx-12} {cy+20} L{cx+12} {cy+20} L{cx+14} {cy-12}" fill="none" stroke="{INK}" stroke-width="1.4"/><rect x="{cx-12.5}" y="{cy}" width="25" height="19" fill="{LIQ}"/>'
            for k in range(5): b += f'<circle cx="{cx-8+k*4}" cy="{cy-2-k*5 % 14}" r="2.6" fill="#fff" stroke="{INK}" stroke-width=".8"/>'
        elif i == 2:
            b += f'<path d="M{cx} {cy+22} q-16 -10 -8 -26 q2 10 8 6 q-4 -14 6 -22 q2 14 10 18 q6 16 -16 24 Z" fill="#f5a142" stroke="{ORA}" stroke-width="1.2"/>'
        elif i == 3:
            for k in range(8):
                a = k * math.pi / 4
                b += f'<line x1="{cx+8*math.cos(a):.0f}" y1="{cy+8*math.sin(a):.0f}" x2="{cx+22*math.cos(a):.0f}" y2="{cy+22*math.sin(a):.0f}" stroke="#e8b923" stroke-width="3"/>'
            b += f'<circle cx="{cx}" cy="{cy}" r="7" fill="#ffd84a"/>'
        elif i == 4:
            b += f'<path d="M{cx-12} {cy-18} L{cx-12} {cy+16} Q{cx-12} {cy+22} {cx-6} {cy+22} L{cx+6} {cy+22} Q{cx+12} {cy+22} {cx+12} {cy+16} L{cx+12} {cy-18}" fill="none" stroke="{INK}" stroke-width="1.4"/><rect x="{cx-10.5}" y="{cy-4}" width="21" height="20" fill="{LIQ}"/><path d="M{cx-10.5} {cy+12} q10 -6 21 0 L{cx+10.5} {cy+16} Q{cx+10} {cy+20.5} {cx+6} {cy+20.5} L{cx-6} {cy+20.5} Q{cx-10} {cy+20.5} {cx-10.5} {cy+16} Z" fill="#f2f2f2" stroke="{MUT}" stroke-width=".8"/>'
        else:
            b += f'<path d="M{cx-14} {cy+10} q-6 -14 6 -18 q0 -10 12 -6 q12 -6 14 8 q10 6 0 16 Z" fill="#b9d98c" stroke="{INK}" stroke-width="1"/>' + "".join(f'<path d="M{cx-8+k*8} {cy-14} q-4 -6 0 -12 q4 -6 0 -12" fill="none" stroke="{MUT}" stroke-width="1.2"/>' for k in range(3))
        b += txt(cx, 108, t, 10, weight=700) + txt(cx, 122, s, 8.6, fill=MUT)
    return svg(615, 130, b, "165mm")

def reaccio_model(A="#B7791F"):
    """En una reacció els àtoms es reorganitzen: metà + oxigen → diòxid de carboni + aigua."""
    b = arrow_defs("rm")
    C, O, Hh = "#3a3f45", RED, "#ffffff"
    def at(x, y, c, r=11): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{INK}" stroke-width="1.2"/>'
    def metà(x, y): return at(x - 15, y - 13, Hh, 7) + at(x + 15, y - 13, Hh, 7) + at(x - 15, y + 13, Hh, 7) + at(x + 15, y + 13, Hh, 7) + at(x, y, C, 12)
    def o2(x, y): return at(x - 9, y, O) + at(x + 9, y, O)
    def co2(x, y): return at(x - 18, y, O) + at(x + 18, y, O) + at(x, y, C, 12)
    def h2o(x, y): return at(x, y, O) + at(x - 13, y + 10, Hh, 7) + at(x + 13, y + 10, Hh, 7)
    b += metà(60, 70) + txt(105, 76, "+", 18, weight=700) + o2(150, 50) + o2(150, 92)
    b += f'<line x1="190" y1="70" x2="250" y2="70" stroke="{INK}" stroke-width="2" marker-end="url(#rm)"/>'
    b += co2(300, 70) + txt(345, 76, "+", 18, weight=700) + h2o(390, 46) + h2o(390, 88)
    b += txt(105, 135, "REACTIUS: metà + oxigen", 10.5, weight=700) + txt(350, 135, "PRODUCTES: diòxid de carboni + aigua", 10.5, weight=700)
    b += txt(230, 160, "Abans i després hi ha els mateixos àtoms: 1 C, 4 H i 4 O. Només canvien els enllaços.", 10, fill=MUT)
    b += at(480, 40, C, 8) + txt(494, 44, "carboni", 9.5, "start") + at(480, 62, O, 8) + txt(494, 66, "oxigen", 9.5, "start") + at(480, 84, Hh, 6) + txt(494, 88, "hidrogen", 9.5, "start")
    return svg(560, 170, b, "150mm")

def lavoisier_globus(A="#B7791F"):
    b = ""
    def balanca(x, val):
        return f'<rect x="{x-60}" y="190" width="120" height="30" rx="5" fill="#eef0f2" stroke="{INK}" stroke-width="1.6"/><rect x="{x-30}" y="198" width="60" height="14" rx="2" fill="#2f3a40"/>' + txt(x, 209, val, 10, fill="#7fffd4", weight=700) + f'<rect x="{x-48}" y="182" width="96" height="7" rx="2" fill="#c9ced3" stroke="{INK}"/>'
    # got obert
    x = 120
    b += f'<path d="M{x-30} 110 L{x-26} 182 L{x+26} 182 L{x+30} 110" fill="none" stroke="{INK}" stroke-width="1.8"/><path d="M{x-28.5} 140 L{x+28.5} 140 L{x+25} 180.5 L{x-25} 180.5 Z" fill="#f1e7c9"/>'
    for k in range(7): b += f'<circle cx="{x-18+k*6}" cy="{130-(k*7)%30}" r="3" fill="#fff" stroke="{MUT}" stroke-width=".8"/>'
    for k in range(3): b += f'<path d="M{x-14+k*14} 96 q-5 -8 0 -16 q5 -8 0 -16" fill="none" stroke="{MUT}" stroke-width="1.3"/>'
    b += balanca(x, "146,90 g") + txt(x, 240, "Recipient obert", 11, weight=700) + txt(x, 255, "abans: 148,20 g · el CO₂ s'escapa", 9.5, fill=MUT)
    # ampolla amb globus
    x = 400
    b += f'<path d="M{x-12} 92 L{x-12} 110 Q{x-32} 120 {x-32} 140 L{x-32} 178 Q{x-32} 182 {x-28} 182 L{x+28} 182 Q{x+32} 182 {x+32} 178 L{x+32} 140 Q{x+32} 120 {x+12} 110 L{x+12} 92" fill="none" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<path d="M{x-30.5} 150 L{x+30.5} 150 L{x+30.5} 178 Q{x+30.5} 180.5 {x+28} 180.5 L{x-28} 180.5 Q{x-30.5} 180.5 {x-30.5} 178 Z" fill="#f1e7c9"/>'
    b += f'<path d="M{x-12} 94 Q{x-46} 60 {x-30} 30 Q{x} 6 {x+30} 30 Q{x+46} 60 {x+12} 94 Z" fill="#f08a8a" stroke="{INK}" stroke-width="1.5" opacity=".9"/>'
    b += balanca(x, "152,40 g") + txt(x, 240, "Recipient tancat amb un globus", 11, weight=700) + txt(x, 255, "abans: 152,40 g · el gas queda dins", 9.5, fill=MUT)
    return svg(560, 262, b, "150mm")

def triangle_foc(A="#B7791F"):
    b = ""
    b += f'<polygon points="150,25 40,210 260,210" fill="#fff4e3" stroke="{A}" stroke-width="3"/>'
    b += f'<path d="M150 190 q-34 -20 -16 -60 q4 22 16 14 q-8 -30 12 -48 q4 30 20 38 q12 34 -32 56 Z" fill="#f5a142" stroke="{ORA}" stroke-width="1.3"/><path d="M150 186 q-14 -10 -6 -28 q4 10 8 6 q4 12 10 8 q2 12 -12 14 Z" fill="#ffd84a"/>'
    b += txt(150, 230, "COMBUSTIBLE (fusta, gas, paper)", 10.5, weight=700)
    b += txt(70, 110, "OXIGEN", 10.5, "end", INK, 700) + txt(70, 124, "(de l'aire)", 9.5, "end", MUT)
    b += txt(232, 110, "CALOR", 10.5, "start", INK, 700) + txt(232, 124, "(energia d'activació)", 9.5, "start", MUT)
    b += txt(330, 60, "Si en treiem un costat, el foc s'apaga:", 10.5, "start", INK, 700)
    b += txt(330, 85, "• sense combustible: tallafocs, tancar el gas", 10, "start") + txt(330, 105, "• sense oxigen: manta ignífuga, tapa, sorra", 10, "start") + txt(330, 125, "• sense calor: aigua (mai en oli ni en endolls!)", 10, "start")
    b += txt(330, 160, "Combustió completa: CO₂ + H₂O.", 10, "start", A, 700) + txt(330, 176, "Amb poc oxigen: monòxid de carboni (CO),", 10, "start") + txt(330, 191, "un gas tòxic que no fa olor.", 10, "start")
    return svg(640, 240, b, "155mm")

# ================================================================= 2n · SdA 6
def equilibri_termic(A="#C63D3D"):
    random.seed(3)
    b = arrow_defs("et", A) + arrow_defs("et2", INK)
    def caixa(x, w, col, n, L, t):
        s = f'<rect x="{x}" y="30" width="{w}" height="110" rx="6" fill="{col}" stroke="{INK}" stroke-width="1.6"/>'
        cols = max(2, int(w / 40)); rows = math.ceil(n / cols)
        for k in range(n):
            px = x + (k % cols + 0.5) * w / cols + random.uniform(-8, 8); py = 30 + ((k // cols) + 0.5) * 110 / rows + random.uniform(-6, 6)
            L = min(L, 14)
            a = random.uniform(0, 6.28)
            s += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="5" fill="#fff" stroke="{INK}"/><line x1="{px+6*math.cos(a):.0f}" y1="{py+6*math.sin(a):.0f}" x2="{px+(6+L)*math.cos(a):.0f}" y2="{py+(6+L)*math.sin(a):.0f}" stroke="{INK}" stroke-width="1" marker-end="url(#et2)"/>'
        return s + txt(x + w / 2, 158, t, 11, weight=700)
    b += caixa(20, 100, "#fbd5cf", 8, 14, "70 °C") + caixa(120, 100, "#d7e8f7", 8, 5, "20 °C")
    b += f'<line x1="80" y1="18" x2="160" y2="18" stroke="{A}" stroke-width="3" marker-end="url(#et)"/>' + txt(120, 12, "calor", 10.5, fill=A, weight=700)
    b += f'<line x1="245" y1="85" x2="300" y2="85" stroke="{INK}" stroke-width="2" marker-end="url(#et2)"/>' + txt(272, 76, "temps", 9.5, fill=MUT)
    b += caixa(320, 200, "#f0e2ec", 16, 9, "45 °C (equilibri tèrmic)")
    b += txt(270, 190, "La calor passa sempre del cos calent al fred fins que tenen la mateixa temperatura.", 10, fill=MUT)
    return svg(545, 200, b, "150mm")

def transmissio_calor(A="#C63D3D"):
    b = arrow_defs("tc", A)
    # conducció: barra
    b += f'<defs><linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="#e5533d"/><stop offset="1" stop-color="#f6e3c8"/></linearGradient></defs>'
    b += f'<rect x="30" y="80" width="150" height="16" rx="3" fill="url(#gb)" stroke="{INK}" stroke-width="1.4"/>'
    b += f'<path d="M30 130 q-8 -22 4 -34 q2 12 8 8 q-2 -14 8 -20 q2 14 10 18 q6 18 -14 28 Z" fill="#f5a142" stroke="{ORA}"/>'
    for k in range(4): b += f'<circle cx="{60+k*30}" cy="88" r="4" fill="#fff" stroke="{INK}" stroke-width=".8"/>'
    b += f'<line x1="70" y1="66" x2="170" y2="66" stroke="{A}" stroke-width="2.2" marker-end="url(#tc)"/>'
    b += txt(105, 196, "Conducció", 12, weight=700) + txt(105, 212, "per contacte, sobretot en sòlids", 9.5, fill=MUT)
    # convecció: olla amb dues cel·les
    x = 300
    b += arrow_defs("tcb", BLUE)
    b += f'<path d="M{x-60} 40 L{x-60} 140 Q{x-60} 146 {x-54} 146 L{x+54} 146 Q{x+60} 146 {x+60} 140 L{x+60} 40" fill="{LIQ}" stroke="{INK}" stroke-width="1.8"/>'
    for sg in (-1, 1):
        b += f'<path d="M{x+sg*6} 132 L{x+sg*6} 62 Q{x+sg*6} 54 {x+sg*16} 54 L{x+sg*34} 54" fill="none" stroke="{A}" stroke-width="2.2" marker-end="url(#tc)"/>'
        b += f'<path d="M{x+sg*48} 60 L{x+sg*48} 126 Q{x+sg*48} 134 {x+sg*38} 134 L{x+sg*18} 134" fill="none" stroke="{BLUE}" stroke-width="2.2" marker-end="url(#tcb)"/>'
    b += f'<path d="M{x} 172 q-12 -8 -6 -22 q3 8 6 4 q-3 -10 4 -16 q3 10 8 13 q4 13 -12 21 Z" fill="#f5a142" stroke="{ORA}" stroke-width="1.2"/>'
    b += txt(x, 196, "Convecció", 12, weight=700) + txt(x, 212, "el fluid calent puja i el fred baixa", 9.5, fill=MUT)
    # radiació: sol
    x = 500
    b += f'<circle cx="{x-40}" cy="80" r="22" fill="#ffd84a" stroke="#e8b923" stroke-width="2"/>'
    for k in range(3):
        y = 64 + k * 16
        b += f'<path d="M{x-12} {y} q6 -6 12 0 t12 0 t12 0 t12 0" fill="none" stroke="{A}" stroke-width="2" marker-end="url(#tc)"/>'
    b += f'<rect x="{x+48}" y="60" width="12" height="44" rx="3" fill="#8c9096" stroke="{INK}"/>'
    b += txt(x, 196, "Radiació", 12, weight=700) + txt(x, 212, "ones, fins i tot pel buit (el Sol)", 9.5, fill=MUT)
    return svg(600, 220, b, "160mm")

def termo(A="#C63D3D"):
    b = arrow_defs("tm", A)
    x = 140
    b += f'<rect x="{x-60}" y="30" width="120" height="200" rx="18" fill="#eef0f2" stroke="{INK}" stroke-width="2"/>'
    b += f'<rect x="{x-48}" y="44" width="96" height="174" rx="12" fill="#fff" stroke="{MUT}" stroke-width="1.2" stroke-dasharray="3 3"/>'
    b += f'<rect x="{x-40}" y="52" width="80" height="158" rx="10" fill="#e9eef3" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<rect x="{x-36}" y="90" width="72" height="116" rx="7" fill="#f6c99a"/>'
    b += f'<rect x="{x-30}" y="16" width="60" height="22" rx="5" fill="#8c9096" stroke="{INK}" stroke-width="1.6"/>'
    def lab(y, x2, t, s):
        return f'<line x1="{x2}" y1="{y}" x2="250" y2="{y}" stroke="{MUT}" stroke-width=".9"/>' + txt(256, y + 4, t, 10.5, "start", INK, 700) + txt(256, y + 18, s, 9.5, "start", MUT)
    b += lab(27, x + 30, "Tap aïllant", "evita la convecció per dalt")
    b += lab(70, x + 54, "Buit entre les dues parets", "sense partícules no hi ha conducció ni convecció")
    b += lab(120, x + 40, "Parets platejades (mirall)", "reflecteixen la radiació")
    b += lab(180, x + 36, "Sopa calenta", "perd calor molt a poc a poc")
    return svg(520, 240, b, "135mm")

def casa_perdues(A="#C63D3D"):
    b = arrow_defs("cp", A)
    b += f'<polygon points="120,40 240,110 0,110" fill="#f3d9c8" stroke="{INK}" stroke-width="1.8"/><rect x="20" y="110" width="200" height="110" fill="#fff6ee" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<rect x="45" y="135" width="44" height="36" fill="#d6eaf8" stroke="{INK}" stroke-width="1.4"/><rect x="150" y="135" width="44" height="36" fill="#d6eaf8" stroke="{INK}" stroke-width="1.4"/><rect x="103" y="170" width="34" height="50" fill="#c9a27a" stroke="{INK}" stroke-width="1.4"/>'
    def a(x1, y1, x2, y2, t, tx, ty, an="start"):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{A}" stroke-width="2.4" marker-end="url(#cp)"/>' + txt(tx, ty, t, 10.5, an, A, 700)
    b += a(120, 70, 120, 18, "teulada 25–30 %", 132, 30)
    b += a(222, 160, 280, 160, "parets 25–35 %", 286, 164)
    b += a(194, 150, 280, 120, "finestres 10–20 %", 286, 118)
    b += a(120, 220, 120, 250, "terra 7–15 %", 132, 252)
    b += a(138, 200, 280, 205, "ventilació i escletxes 10–20 %", 286, 209)
    b += txt(286, 60, "Per on perd calor una casa", 11, "start", INK, 700) + txt(286, 76, "sense aïllar (valors orientatius)", 9.5, "start", MUT)
    return svg(560, 262, b, "140mm")
