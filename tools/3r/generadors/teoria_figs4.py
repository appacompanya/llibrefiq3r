"""Il·lustracions vectorials dels dossiers de teoria de 4t d'ESO (mateix estil que teoria_figs*)."""
import math, random
from teoria_figs import svg, txt, arrow_defs, INK, MUT
from teoria_figs2 import axes, BLUE, RED, ORA, GRN, PUR, GRY

LIQ = "#d6eaf8"
def sfrac(x, y, num, den, size=12, fill=INK, anchor="start", weight=700):
    """Fracció en dues fileres dins d'un SVG (x = vora esquerra si anchor=start)."""
    w = max(len(num), len(den)) * size * 0.62
    cx = x + w / 2 if anchor == "start" else x
    return (txt(cx, y - 4, num, size, "middle", fill, weight) + f'<line x1="{cx-w/2:.0f}" y1="{y}" x2="{cx+w/2:.0f}" y2="{y}" stroke="{fill}" stroke-width="1.2"/>'
            + txt(cx, y + size + 1, den, size, "middle", fill, weight)), w
def at(x, y, c, r=11, sw=1.2): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{INK}" stroke-width="{sw}"/>'

# ================================================================= 4t · SdA 1
def models_atomics(A="#7A4CC2"):
    random.seed(1)
    b = ""
    labs = [("Dalton (1808)", "esfera massissa i indivisible"), ("Thomson (1904)", "esfera positiva amb electrons"), ("Rutherford (1911)", "nucli petit i dens; electrons al voltant"),
            ("Bohr (1913)", "electrons en òrbites; d'energia fixa"), ("Actual", "orbitals: zones on és; probable trobar l'electró")]
    for i, (t, s) in enumerate(labs):
        cx, cy = 62 + i * 124, 70
        if i == 0:
            b += f'<defs><radialGradient id="gd" cx=".35" cy=".35"><stop offset="0" stop-color="#e9e3f6"/><stop offset="1" stop-color="#8f7ad9"/></radialGradient></defs><circle cx="{cx}" cy="{cy}" r="40" fill="url(#gd)" stroke="{INK}" stroke-width="1.5"/>'
        elif i == 1:
            b += f'<circle cx="{cx}" cy="{cy}" r="40" fill="#f6d6dd" stroke="{INK}" stroke-width="1.5"/>'
            for k in range(9):
                a, r = k * 0.7 + 0.3, 12 + (k % 3) * 9
                b += f'<circle cx="{cx+r*math.cos(a):.0f}" cy="{cy+r*math.sin(a):.0f}" r="4.5" fill="{BLUE}" stroke="{INK}" stroke-width=".8"/>'
            b += txt(cx - 26, cy - 22, "+", 10, fill=RED, weight=700) + txt(cx + 24, cy + 28, "+", 10, fill=RED, weight=700) + txt(cx + 26, cy - 18, "+", 10, fill=RED, weight=700)
        elif i == 2:
            for k in range(3):
                b += f'<ellipse cx="{cx}" cy="{cy}" rx="42" ry="14" fill="none" stroke="{MUT}" stroke-width="1" transform="rotate({k*60} {cx} {cy})"/>'
            b += f'<circle cx="{cx}" cy="{cy}" r="5" fill="{RED}" stroke="{INK}"/>'
            for k in range(3):
                a = math.radians(k * 60)
                b += f'<circle cx="{cx+42*math.cos(a):.0f}" cy="{cy+42*math.sin(a)*0.0+ (14*math.sin(a)):.0f}" r="3.5" fill="{BLUE}"/>'
        elif i == 3:
            for r in (16, 28, 40):
                b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MUT}" stroke-width="1"/>'
            b += f'<circle cx="{cx}" cy="{cy}" r="6" fill="{RED}" stroke="{INK}"/>'
            for r, a in ((16, 0.5), (16, 3.6), (28, 1.2), (28, 2.5), (28, 4.4), (40, 5.5)):
                b += f'<circle cx="{cx+r*math.cos(a):.0f}" cy="{cy+r*math.sin(a):.0f}" r="3.5" fill="{BLUE}"/>'
        else:
            for k in range(260):
                r = abs(random.gauss(0, 15)); a = random.uniform(0, 6.28)
                if r < 42: b += f'<circle cx="{cx+r*math.cos(a):.1f}" cy="{cy+r*math.sin(a):.1f}" r="1.2" fill="{A}" opacity=".55"/>'
            b += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{RED}"/>'
        b += txt(cx, 130, t, 10.5, weight=700) + txt(cx, 145, s.split("; ")[0], 8.6, fill=MUT) + (txt(cx, 157, s.split("; ")[1], 8.6, fill=MUT) if "; " in s else "")
        if i < 4: b += txt(cx + 62, cy + 4, "→", 16, fill=A, weight=700)
    return svg(625, 165, b, "165mm")

def isotops(A="#7A4CC2"):
    b = ""
    data = [("hidrogen-1 (proti)", 1, 0), ("hidrogen-2 (deuteri)", 1, 1), ("hidrogen-3 (triti)", 1, 2)]
    for i, (t, p, n) in enumerate(data):
        cx, cy = 90 + i * 180, 75
        b += f'<circle cx="{cx}" cy="{cy}" r="48" fill="none" stroke="{MUT}" stroke-width="1" stroke-dasharray="3 3"/>'
        b += f'<circle cx="{cx+48*math.cos(-0.8):.0f}" cy="{cy+48*math.sin(-0.8):.0f}" r="5" fill="{BLUE}" stroke="{INK}"/>'
        pts = [(0, 0), (9, 5), (-6, 8)][: p + n]
        for k, (dx, dy) in enumerate(pts):
            b += at(cx + dx, cy + dy, RED if k < p else "#c9ced3", 8, 1)
        b += txt(cx, 145, t, 10.5, weight=700) + txt(cx, 160, f"1 protó · {n} neutró{'ns' if n != 1 else ''} · A = {p+n}", 9.5, fill=MUT)
    b += at(560, 40, RED, 6) + txt(572, 44, "protó", 9.5, "start") + at(560, 60, "#c9ced3", 6) + txt(572, 64, "neutró", 9.5, "start") + f'<circle cx="560" cy="80" r="4" fill="{BLUE}" stroke="{INK}"/>' + txt(572, 84, "electró", 9.5, "start")
    b += txt(330, 182, "Mateix element (Z = 1), diferent nombre de neutrons: isòtops.", 10, fill=A, weight=700)
    return svg(640, 190, b, "155mm")

def espectres(A="#7A4CC2"):
    b = '<defs><linearGradient id="spc" x1="0" x2="1"><stop offset="0" stop-color="#6a2fb5"/><stop offset=".18" stop-color="#2b4fd6"/><stop offset=".35" stop-color="#1fb3d6"/><stop offset=".5" stop-color="#2fbf4a"/><stop offset=".65" stop-color="#f2e22b"/><stop offset=".8" stop-color="#f39a1f"/><stop offset="1" stop-color="#d62828"/></linearGradient></defs>'
    x0, w = 170, 400
    def nm2x(nm): return x0 + (nm - 400) / 300 * w
    b += txt(160, 42, "Espectre continu", 10.5, "end", INK, 700) + txt(160, 56, "(sòlid incandescent, Sol)", 9, "end", MUT)
    b += f'<rect x="{x0}" y="28" width="{w}" height="34" fill="url(#spc)" stroke="{INK}"/>'
    for (lab, sub, y, lines) in (("Hidrogen", "espectre d'emissió", 82, [(410, "#6a2fb5"), (434, "#3b3fd9"), (486, "#1fa0d6"), (656, "#d62828")]),
                                  ("Sodi", "espectre d'emissió", 136, [(589, "#f2b51f"), (589.6, "#f2b51f")])):
        b += txt(160, y + 14, lab, 10.5, "end", INK, 700) + txt(160, y + 28, sub, 9, "end", MUT)
        b += f'<rect x="{x0}" y="{y}" width="{w}" height="34" fill="#111" stroke="{INK}"/>'
        for nm, c in lines: b += f'<rect x="{nm2x(nm)-1.5:.1f}" y="{y}" width="3" height="34" fill="{c}"/>'
    for nm in (400, 500, 600, 700):
        b += f'<line x1="{nm2x(nm)}" y1="172" x2="{nm2x(nm)}" y2="177" stroke="{INK}"/>' + txt(nm2x(nm), 190, f"{nm} nm", 9)
    b += txt(x0 + w / 2, 206, "Cada element emet només unes línies de colors: és la seva «empremta dactilar».", 10, fill=MUT)
    return svg(600, 214, b, "160mm")

def salts_electrons(A="#7A4CC2"):
    b = arrow_defs("se", A) + arrow_defs("se2", INK)
    levels = [(200, "n = 1"), (130, "n = 2"), (92, "n = 3"), (72, "n = 4")]
    for y, l in levels:
        b += f'<line x1="60" y1="{y}" x2="300" y2="{y}" stroke="{INK}" stroke-width="1.6"/>' + txt(306, y + 4, l, 10, "start")
    b += f'<line x1="30" y1="215" x2="30" y2="50" stroke="{INK}" stroke-width="1.3" marker-end="url(#se2)"/>' + txt(26, 44, "Energia", 9.5, "start")
    # absorció
    b += f'<line x1="110" y1="196" x2="110" y2="96" stroke="{INK}" stroke-width="2" marker-end="url(#se2)"/>' + txt(118, 150, "absorbeix", 9.5, "start") + txt(118, 162, "energia", 9.5, "start")
    b += f'<path d="M70 170 q6 -8 12 0 t12 0 t12 0" fill="none" stroke="{ORA}" stroke-width="1.8"/>' + txt(70, 186, "calor", 9, fill=ORA)
    # emissió
    b += f'<line x1="230" y1="94" x2="230" y2="194" stroke="{A}" stroke-width="2.4" marker-end="url(#se)"/>' + txt(222, 150, "torna i", 9.5, "end", A, 700) + txt(222, 162, "emet llum", 9.5, "end", A, 700)
    b += f'<path d="M240 150 q6 -8 12 0 t12 0 t12 0 t12 0" fill="none" stroke="#d62828" stroke-width="2.2" marker-end="url(#se)"/>'
    b += f'<circle cx="110" cy="200" r="5" fill="{BLUE}"/><circle cx="230" cy="92" r="5" fill="{BLUE}"/>'
    b += txt(365, 80, "1. L'electró absorbeix energia (flama,", 10, "start") + txt(365, 94, "   corrent) i salta a un nivell superior.", 10, "start")
    b += txt(365, 120, "2. És inestable i torna a baixar.", 10, "start") + txt(365, 146, "3. Emet l'energia en forma de llum.", 10, "start")
    b += txt(365, 160, "   El color depèn de la mida del salt.", 10, "start")
    b += txt(365, 190, "E llum = E nivell superior − E nivell inferior", 10, "start", A, 700)
    return svg(640, 225, b, "155mm")

def moeller(A="#7A4CC2"):
    b = arrow_defs("mo", A)
    rows = [["1s"], ["2s", "2p"], ["3s", "3p", "3d"], ["4s", "4p", "4d", "4f"], ["5s", "5p", "5d", "5f"], ["6s", "6p", "6d"], ["7s", "7p"]]
    for i, r in enumerate(rows):
        for j, o in enumerate(r):
            x, y = 50 + j * 58, 28 + i * 30
            b += f'<rect x="{x-20}" y="{y-12}" width="40" height="22" rx="5" fill="#fff" stroke="{INK}" stroke-width="1.2"/>' + txt(x, y + 4, o, 11, weight=700)
    for m in range(7):
        jt = min(m // 2, 3); it = m - jt
        if it > 6: continue
        sx, sy = 50 + jt * 58 + 30, 28 + it * 30 - 15
        ex, ey = 50 - 30, 28 + m * 30 + 15
        b += f'<line x1="{sx}" y1="{sy}" x2="{ex}" y2="{ey}" stroke="{A}" stroke-width="1.6" opacity=".75" marker-end="url(#mo)"/>'
    b += txt(290, 40, "Ordre d'ompliment (diagonals):", 10.5, "start", INK, 700)
    b += txt(290, 60, "1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p…", 10, "start")
    b += txt(290, 92, "Capacitat de cada subnivell:", 10.5, "start", INK, 700)
    b += txt(290, 112, "s: 2 e⁻   p: 6 e⁻   d: 10 e⁻   f: 14 e⁻", 10, "start")
    b += txt(290, 144, "Exemple: Na (Z = 11)", 10.5, "start", A, 700) + txt(290, 162, "1s² 2s² 2p⁶ 3s¹", 11, "start", A, 700)
    b += txt(290, 182, "1 electró de valència (nivell 3):", 10, "start") + txt(290, 196, "és del grup 1 i del període 3.", 10, "start")
    return svg(560, 238, b, "145mm")

def blocs_taula(A="#7A4CC2"):
    cw, ch, L, Tp = 26, 20, 24, 30
    COLS = {"s": "#F6C2B5", "p": "#BFD8F4", "d": "#F3E9A6", "f": "#D9EBB5"}
    b = ""
    def cell(per, g, blk, y_off=0):
        x, y = L + (g - 1) * cw, Tp + (per - 1) * ch + y_off
        return f'<rect x="{x+1}" y="{y+1}" width="{cw-2}" height="{ch-2}" rx="2" fill="{COLS[blk]}" stroke="#7a8088" stroke-width=".5"/>'
    for per in range(1, 8):
        for g in range(1, 19):
            if per == 1 and g not in (1, 18): continue
            if per in (2, 3) and 3 <= g <= 12: continue
            blk = "s" if g <= 2 or (per == 1 and g == 18) else ("d" if g <= 12 else "p")
            b += cell(per, g, blk)
    for per in (6, 7):
        for k in range(14): b += cell(per + 2.6 - 0, 3 + k + 1, "f", 4)
    b += txt(L + cw, Tp - 8, "bloc s", 10, weight=700) + txt(L + 7.5 * cw, Tp + ch * 3 - 4, "bloc d", 10, weight=700) + txt(L + 15.5 * cw, Tp - 8, "bloc p", 10, weight=700) + txt(L + 3.4 * cw, Tp + 8.6 * ch + 12, "bloc f", 10, "end", INK, 700)
    b += txt(530, 60, "L'últim electró que entra", 10, "start", INK, 700) + txt(530, 74, "decideix el bloc:", 10, "start", INK, 700)
    b += txt(530, 96, "s: grups 1 i 2 (i l'heli)", 10, "start") + txt(530, 112, "p: grups 13 a 18", 10, "start") + txt(530, 128, "d: metalls de transició", 10, "start") + txt(530, 144, "f: lantànids i actínids", 10, "start")
    b += txt(530, 172, "Període = nivell més alt", 10, "start", A, 700) + txt(530, 186, "ocupat per electrons.", 10, "start", A, 700)
    return svg(700, 230, b, "165mm")

# ================================================================= 4t · SdA 2
def preparar_dissolucio(A="#1F8FB8"):
    b = arrow_defs("pd", A)
    def bal(x):
        return f'<rect x="{x-36}" y="150" width="72" height="26" rx="5" fill="#eef0f2" stroke="{INK}" stroke-width="1.5"/><rect x="{x-22}" y="157" width="44" height="12" rx="2" fill="#2f3a40"/>' + txt(x, 166.5, "0,90 g", 9, fill="#7fffd4", weight=700) + f'<rect x="{x-28}" y="143" width="56" height="6" rx="2" fill="#c9ced3" stroke="{INK}"/><path d="M{x-14} 143 L{x-10} 134 L{x+10} 134 L{x+14} 143 Z" fill="#fff" stroke="{INK}"/>'
    def vas(x):
        return f'<path d="M{x-26} 100 L{x-26} 170 Q{x-26} 175 {x-21} 175 L{x+21} 175 Q{x+26} 175 {x+26} 170 L{x+26} 100" fill="none" stroke="{INK}" stroke-width="1.6"/><path d="M{x-24.5} 140 L{x+24.5} 140 L{x+24.5} 170 Q{x+24.5} 173.5 {x+21} 173.5 L{x-21} 173.5 Q{x-24.5} 173.5 {x-24.5} 170 Z" fill="{LIQ}"/><line x1="{x+6}" y1="90" x2="{x-8}" y2="165" stroke="#8c9096" stroke-width="3"/>'
    def matras(x, full):
        s = f'<path d="M{x-6} 40 L{x-6} 110 Q{x-36} 122 {x-36} 148 Q{x-36} 176 {x} 176 Q{x+36} 176 {x+36} 148 Q{x+36} 122 {x+6} 110 L{x+6} 40" fill="none" stroke="{INK}" stroke-width="1.6"/>'
        lvl = 70 if full else 140
        if not full: s += f'<path d="M{x-34.5} {max(lvl,128)} Q{x-34.5} 174.5 {x} 174.5 Q{x+34.5} 174.5 {x+34.5} {max(lvl,128)} Z" fill="{LIQ}"/>'
        if full: s = f'<path d="M{x-4.5} 70 L{x-4.5} 111 Q{x-34.5} 122 {x-34.5} 148 Q{x-34.5} 174.5 {x} 174.5 Q{x+34.5} 174.5 {x+34.5} 148 Q{x+34.5} 122 {x+4.5} 111 L{x+4.5} 70 Z" fill="{LIQ}"/>' + s
        s += f'<line x1="{x-10}" y1="70" x2="{x+10}" y2="70" stroke="{RED}" stroke-width="1.6"/>'
        return s
    steps = [(70, bal(70), "1. Pesem;el solut"), (220, vas(220), "2. El dissolem;amb poca aigua"), (370, matras(370, False), "3. Ho passem al;matràs aforat"), (520, matras(520, True), "4. Enrasem fins;a la marca")]
    for i, (x, s, t) in enumerate(steps):
        b += s + txt(x, 198, t.split(";")[0], 10, weight=700) + txt(x, 211, t.split(";")[1], 10, weight=700)
        if i < 3: b += f'<line x1="{x+48}" y1="120" x2="{x+100}" y2="120" stroke="{A}" stroke-width="2" marker-end="url(#pd)"/>'
    b += txt(300, 234, "Exemple: 100 mL de sèrum fisiològic (0,9 %) → 0,90 g de NaCl en un matràs de 100 mL.", 9.5, fill=MUT)
    return svg(600, 242, b, "155mm")

def dilucio(A="#1F8FB8"):
    random.seed(6)
    b = arrow_defs("dl", A)
    def got(x, h, n, lab, sub):
        s = f'<path d="M{x-40} 40 L{x-40} 170 Q{x-40} 176 {x-34} 176 L{x+34} 176 Q{x+40} 176 {x+40} 170 L{x+40} 40" fill="none" stroke="{INK}" stroke-width="1.6"/>'
        s += f'<path d="M{x-38.5} {176-h} L{x+38.5} {176-h} L{x+38.5} 170 Q{x+38.5} 174.5 {x+34} 174.5 L{x-34} 174.5 Q{x-38.5} 174.5 {x-38.5} 170 Z" fill="#cbe6f4"/>'
        for k in range(n): s += f'<circle cx="{x+random.uniform(-32,32):.0f}" cy="{176-random.uniform(6,h-6):.0f}" r="3.4" fill="{A}"/>'
        return s + txt(x, 196, lab, 10.5, weight=700) + txt(x, 211, sub, 9.5, fill=MUT)
    b += got(90, 40, 12, "c₁ = 2 mol/L", "V₁ = 50 mL") + f'<line x1="150" y1="110" x2="215" y2="110" stroke="{A}" stroke-width="2" marker-end="url(#dl)"/>' + txt(182, 100, "+ aigua", 10, fill=A, weight=700)
    b += got(280, 120, 12, "c₂ = 0,5 mol/L", "V₂ = 200 mL")
    b += txt(360, 80, "El solut no canvia:", 10.5, "start", INK, 700) + txt(360, 98, "n = c₁ · V₁ = c₂ · V₂", 12, "start", A, 700)
    b += txt(360, 126, "2 · 0,050 = 0,5 · 0,200 = 0,1 mol", 10, "start") + txt(360, 150, "Volum 4 vegades més gran,", 10, "start") + txt(360, 164, "concentració 4 vegades més petita.", 10, "start")
    return svg(580, 220, b, "150mm")

def mol_mostres(A="#1F8FB8"):
    b = ""
    items = [("aigua", "H₂O", "18 g", "#cbe6f4"), ("sal", "NaCl", "58,5 g", "#ffffff"), ("sucre", "C₁₂H₂₂O₁₁", "342 g", "#f6ecd6"), ("ferro", "Fe", "55,8 g", "#9aa1a8"), ("carboni", "C", "12 g", "#3a3f45")]
    for i, (n, f, m, c) in enumerate(items):
        x = 60 + i * 115
        h = {0: 30, 1: 26, 2: 60, 3: 12, 4: 18}[i]
        if i == 0:
            b += f'<path d="M{x-24} 70 L{x-22} 130 L{x+22} 130 L{x+24} 70" fill="none" stroke="{INK}" stroke-width="1.5"/><path d="M{x-23} {130-h} L{x+23} {130-h} L{x+22} 130 L{x-22} 130 Z" fill="{c}"/>'
        else:
            b += f'<path d="M{x-30} 130 Q{x} {130-h*2} {x+30} 130 Z" fill="{c}" stroke="{INK}" stroke-width="1.3"/>'
        b += f'<line x1="{x-40}" y1="131" x2="{x+40}" y2="131" stroke="{INK}" stroke-width="1.5"/>'
        b += txt(x, 152, f"1 mol de {n}", 10.5, weight=700) + txt(x, 167, f, 10) + txt(x, 183, m, 11, fill=A, weight=700)
    b += txt(290, 30, "Cada mostra té el mateix nombre de partícules: 6,022 · 10²³ (nombre d'Avogadro)", 10.5, weight=700)
    b += txt(290, 48, "però masses diferents: la massa molar (M), en g/mol.", 10, fill=MUT)
    return svg(600, 192, b, "155mm")

def recta_calibratge(A="#1F8FB8"):
    b = arrow_defs("ax")
    x0, y0 = 70, 220
    b += axes(x0, y0, 330, 190, "", "") + txt(x0 + 165, y0 + 34, "concentració de NaCl (g/L)", 10.5)
    b += txt(x0 - 6, 20, "conductivitat (µS/cm)", 10.5, "start")
    for k in range(1, 6):
        b += f'<line x1="{x0+k*60}" y1="{y0}" x2="{x0+k*60}" y2="{y0+5}" stroke="{INK}"/>' + txt(x0 + k * 60, y0 + 17, f"{k*0.2:.1f}".replace(".", ","), 9.5)
        b += f'<line x1="{x0-5}" y1="{y0-k*34}" x2="{x0+320}" y2="{y0-k*34}" stroke="#e3e6ea"/>' + txt(x0 - 8, y0 - k * 34 + 4, str(k * 400), 9.5, "end")
    pts = [(0.2, 410), (0.4, 790), (0.6, 1210), (0.8, 1590), (1.0, 2010)]
    X = lambda c: x0 + c / 0.2 * 60; Y = lambda s: y0 - s / 400 * 34
    b += f'<line x1="{X(0)}" y1="{Y(5)}" x2="{X(1.05)}" y2="{Y(2105)}" stroke="{A}" stroke-width="2"/>'
    for c, s in pts: b += f'<circle cx="{X(c):.0f}" cy="{Y(s):.0f}" r="4.5" fill="#fff" stroke="{A}" stroke-width="2"/>'
    s = 1100; c = s / 2000
    b += f'<line x1="{x0}" y1="{Y(s):.0f}" x2="{X(c):.0f}" y2="{Y(s):.0f}" stroke="{RED}" stroke-dasharray="4 3" stroke-width="1.4"/><line x1="{X(c):.0f}" y1="{Y(s):.0f}" x2="{X(c):.0f}" y2="{y0}" stroke="{RED}" stroke-dasharray="4 3" stroke-width="1.4"/><circle cx="{X(c):.0f}" cy="{Y(s):.0f}" r="4.5" fill="{RED}"/>'
    b += txt(430, 80, "1. Mesurem patrons de", 10, "start") + txt(430, 94, "concentració coneguda.", 10, "start") + txt(430, 116, "2. Dibuixem la recta.", 10, "start")
    b += txt(430, 138, "3. Mesurem la mostra (vermell)", 10, "start", RED, 700) + txt(430, 152, "i llegim la concentració a l'eix x.", 10, "start", RED, 700)
    return svg(640, 260, b, "150mm")

def tyndall(A="#1F8FB8"):
    random.seed(2)
    b = ""
    for i, (lab, sub, col, part) in enumerate((("Dissolució", "aigua amb sal: el feix no es veu", "#e8f4fb", False), ("Col·loide", "aigua amb una mica de llet: el feix es veu", "#f3f3ef", True))):
        x = 150 + i * 270
        b += f'<rect x="{x-70}" y="40" width="140" height="110" rx="6" fill="{col}" stroke="{INK}" stroke-width="1.6"/>'
        b += f'<rect x="{x-150}" y="88" width="34" height="14" rx="3" fill="#555"/><line x1="{x-116}" y1="95" x2="{x-70}" y2="95" stroke="#e33" stroke-width="2.5"/>'
        if part:
            b += f'<line x1="{x-70}" y1="95" x2="{x+70}" y2="95" stroke="#e33" stroke-width="5" opacity=".75"/>'
            for k in range(40): b += f'<circle cx="{x+random.uniform(-66,66):.0f}" cy="{random.uniform(46,144):.0f}" r="1.6" fill="#bbb"/>'
        b += f'<line x1="{x+70}" y1="95" x2="{x+100}" y2="95" stroke="#e33" stroke-width="2.5"/>'
        b += txt(x, 172, lab, 11, weight=700) + txt(x, 187, sub, 9.5, fill=MUT)
    return svg(560, 196, b, "140mm")

# ================================================================= 4t · SdA 3
def hidrocarburs(A="#4E8A2E"):
    b = ""
    def bond(x1, y1, x2, y2, n=1):
        s = ""
        dx, dy = y2 - y1, x1 - x2; L = math.hypot(dx, dy) or 1; dx, dy = dx / L * 3.2, dy / L * 3.2
        offs = [0] if n == 1 else ([-0.5, 0.5] if n == 2 else [-1, 0, 1])
        for o in offs: s += f'<line x1="{x1+o*dx:.1f}" y1="{y1+o*dy:.1f}" x2="{x2+o*dx:.1f}" y2="{y2+o*dy:.1f}" stroke="{INK}" stroke-width="1.4"/>'
        return s
    def lab(x, y, t, c=INK): return txt(x, y + 5, t, 13, fill=c, weight=700)
    # metà
    x, y = 70, 75
    b += bond(x, y - 8, x, y - 26) + bond(x, y + 8, x, y + 26) + bond(x - 9, y, x - 26, y) + bond(x + 9, y, x + 26, y)
    b += lab(x, y, "C") + lab(x, y - 34, "H") + lab(x, y + 34, "H") + lab(x - 34, y, "H") + lab(x + 34, y, "H")
    b += txt(x, 140, "metà", 10.5, weight=700) + txt(x, 154, "CH₄ · alcà", 9.5, fill=MUT)
    # età
    x = 200
    for cx in (x - 20, x + 20):
        b += lab(cx, y, "C") + bond(cx, y - 8, cx, y - 26) + bond(cx, y + 8, cx, y + 26) + lab(cx, y - 34, "H") + lab(cx, y + 34, "H")
    b += bond(x - 11, y, x + 11, y) + bond(x - 29, y, x - 46, y) + bond(x + 29, y, x + 46, y) + lab(x - 54, y, "H") + lab(x + 54, y, "H")
    b += txt(x, 140, "età", 10.5, weight=700) + txt(x, 154, "C₂H₆ · alcà (enllaços simples)", 9.5, fill=MUT)
    # etè
    x = 350
    b += lab(x - 20, y, "C") + lab(x + 20, y, "C") + bond(x - 11, y, x + 11, y, 2)
    for sg in (-1, 1):
        cx = x + sg * 20
        b += bond(cx + sg * 6, y - 7, cx + sg * 22, y - 22) + bond(cx + sg * 6, y + 7, cx + sg * 22, y + 22) + lab(cx + sg * 28, y - 28, "H") + lab(cx + sg * 28, y + 28, "H")
    b += txt(x, 140, "etè", 10.5, weight=700) + txt(x, 154, "C₂H₄ · alquè (doble)", 9.5, fill=MUT)
    # etí
    x = 480
    b += lab(x - 20, y, "C") + lab(x + 20, y, "C") + bond(x - 11, y, x + 11, y, 3) + bond(x - 29, y, x - 46, y) + bond(x + 29, y, x + 46, y) + lab(x - 54, y, "H") + lab(x + 54, y, "H")
    b += txt(x, 140, "etí", 10.5, weight=700) + txt(x, 154, "C₂H₂ · alquí (triple)", 9.5, fill=MUT)
    # etanol
    x = 640
    for cx in (x - 30, x + 10):
        b += lab(cx, y, "C") + bond(cx, y - 8, cx, y - 26) + bond(cx, y + 8, cx, y + 26) + lab(cx, y - 34, "H") + lab(cx, y + 34, "H")
    b += bond(x - 21, y, x + 1, y) + bond(x - 39, y, x - 56, y) + lab(x - 64, y, "H") + bond(x + 19, y, x + 38, y) + lab(x + 46, y, "O", RED) + bond(x + 55, y, x + 70, y) + lab(x + 78, y, "H")
    b += txt(x + 6, 140, "etanol", 10.5, weight=700) + txt(x + 6, 154, "CH₃–CH₂OH · alcohol (-OH)", 9.5, fill=MUT)
    return svg(740, 162, b, "170mm")

def estequiometria(A="#4E8A2E"):
    b = arrow_defs("eq", A)
    box = [("grams de A", "dada"), ("mols de A", ""), ("mols de B", ""), ("grams de B", "resultat")]
    ops = ["÷ M(A)", "proporció de l'equació", "· M(B)"]
    for i, (t, s) in enumerate(box):
        x = 20 + i * 160
        b += f'<rect x="{x}" y="30" width="120" height="50" rx="10" fill="{"#fff" if i in (1, 2) else A}" stroke="{A}" stroke-width="2"/>' + txt(x + 60, 60, t, 12, fill=(INK if i in (1, 2) else "#fff"), weight=700)
        if s: b += txt(x + 60, 98, s, 9.5, fill=MUT)
        if i < 3: b += f'<line x1="{x+122}" y1="55" x2="{x+158}" y2="55" stroke="{A}" stroke-width="2.2" marker-end="url(#eq)"/>' + txt(x + 140, 22, ops[i], 9.5, fill=A, weight=700)
    b += txt(330, 125, "Pas 0: escriu l'equació ajustada. Pas 1: grams → mols. Pas 2: mols de A → mols de B amb els coeficients. Pas 3: mols → grams.", 9.5, fill=MUT)
    return svg(660, 135, b, "165mm")

def calorimetre(A="#4E8A2E"):
    b = arrow_defs("cl", A)
    # suport
    b += f'<line x1="40" y1="230" x2="40" y2="20" stroke="{INK}" stroke-width="3"/><rect x="20" y="228" width="140" height="8" fill="#8c9096" stroke="{INK}"/><line x1="40" y1="60" x2="110" y2="60" stroke="{INK}" stroke-width="2.5"/>'
    # llauna
    b += f'<rect x="80" y="60" width="64" height="80" rx="4" fill="#d0d4d8" stroke="{INK}" stroke-width="1.6"/><rect x="82" y="80" width="60" height="58" fill="{LIQ}"/>'
    b += f'<line x1="124" y1="20" x2="124" y2="128" stroke="{INK}" stroke-width="2"/><circle cx="124" cy="130" r="4" fill="{RED}"/>' + txt(132, 26, "termòmetre", 9.5, "start", MUT)
    # cremador
    b += f'<path d="M112 210 q-14 -12 -6 -30 q3 10 7 6 q-3 -14 6 -22 q3 14 10 18 q5 18 -17 28 Z" fill="#f5a142" stroke="{ORA}" stroke-width="1.2"/><rect x="96" y="208" width="34" height="22" rx="4" fill="#fff" stroke="{INK}" stroke-width="1.4"/>' + txt(113, 223, "etanol", 8, fill=MUT)
    b += txt(190, 50, "Calor que guanya l'aigua:", 10.5, "start", INK, 700) + txt(190, 68, "Q = m · c · ΔT", 12, "start", A, 700)
    b += txt(190, 100, "Pesem el cremador abans i després:", 10, "start") + txt(190, 114, "sabem quants grams d'etanol han cremat.", 10, "start")
    fr, w = sfrac(286, 146, "Q", "massa cremada", 10)
    b += txt(190, 150, "Calor per gram =", 10, "start", INK, 700) + fr
    b += txt(190, 184, "Surt menys que el valor teòric: part de", 10, "start") + txt(190, 198, "la calor escalfa l'aire i la llauna", 10, "start") + txt(190, 212, "(rendiment < 100 %).", 10, "start")
    return svg(520, 240, b, "135mm")

# ================================================================= 4t · SdA 4
def escala_ph(A="#B8742A"):
    cols = ["#d7191c", "#e5402a", "#f07c2f", "#f6a733", "#f9cf3a", "#e6e13f", "#a8d05a", "#5cb85c", "#3aa58f", "#2f8fc2", "#3a6fc4", "#4b57b8", "#5b45a8", "#6a3596", "#5a2a7a"]
    b = ""
    x0, w = 30, 40
    for i, c in enumerate(cols):
        b += f'<rect x="{x0+i*w}" y="70" width="{w}" height="34" fill="{c}" stroke="#fff"/>' + txt(x0 + i * w + w / 2, 92, str(i), 11, fill="#fff", weight=700)
    items = [(0, "àcid de bateria"), (2, "suc de llimona"), (3, "vinagre"), (5.5, "pluja àcida < 5,6"), (7, "aigua pura"), (8.3, "aigua de mar"), (9, "bicarbonat"), (11.5, "amoníac"), (13, "lleixiu, desembussador")]
    for k, (ph, t) in enumerate(items):
        x = x0 + ph * w + w / 2
        y = 58 - (k % 2) * 22
        b += f'<line x1="{x}" y1="{y+3}" x2="{x}" y2="70" stroke="{MUT}" stroke-width=".9"/>' + txt(x, y, t, 9, fill=INK)
    b += txt(x0 + 3.5 * w, 126, "ÀCID", 12, fill="#d7191c", weight=700) + txt(x0 + 7.5 * w, 126, "NEUTRE", 12, fill="#5cb85c", weight=700) + txt(x0 + 11.5 * w, 126, "BÀSIC", 12, fill="#4b57b8", weight=700)
    b += txt(x0 + 7.5 * w, 146, "Cada unitat de pH és 10 vegades més àcid o més bàsic que la següent.", 9.5, fill=MUT)
    return svg(660, 154, b, "165mm")

def neutralitzacio(A="#B8742A"):
    b = arrow_defs("nt")
    def ion(x, y, t, c, r=14): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{INK}" stroke-width="1.1"/>' + txt(x, y + 4, t, 9.5, weight=700)
    b += ion(40, 50, "H⁺", "#f6c2b5") + ion(80, 50, "Cl⁻", "#cfe8c2") + txt(60, 85, "àcid clorhídric", 9.5, fill=MUT)
    b += txt(118, 54, "+", 18, weight=700)
    b += ion(160, 50, "Na⁺", "#d6e4f7") + ion(205, 50, "OH⁻", "#f3e9a6", 16) + txt(182, 85, "hidròxid de sodi", 9.5, fill=MUT)
    b += f'<line x1="240" y1="50" x2="290" y2="50" stroke="{INK}" stroke-width="2" marker-end="url(#nt)"/>'
    b += ion(330, 50, "Na⁺", "#d6e4f7") + ion(372, 50, "Cl⁻", "#cfe8c2") + txt(351, 85, "sal (clorur de sodi)", 9.5, fill=MUT)
    b += txt(406, 54, "+", 18, weight=700) + at(450, 46, RED, 11) + at(437, 58, "#fff", 7) + at(463, 58, "#fff", 7) + txt(450, 85, "aigua", 9.5, fill=MUT)
    b += txt(250, 118, "L'essencial: H⁺ + OH⁻ → H₂O. L'àcid i la base s'anul·len i el pH s'acosta a 7.", 10, fill=A, weight=700)
    return svg(500, 128, b, "140mm")

def pluja_acida(A="#B8742A"):
    b = arrow_defs("pa", MUT)
    b += f'<rect x="0" y="0" width="640" height="230" fill="#f4f8fb"/><rect x="0" y="200" width="640" height="30" fill="#d9cfbf"/>'
    # cotxe i fàbrica
    b += f'<rect x="40" y="120" width="40" height="80" fill="#9aa1a8" stroke="{INK}"/><rect x="52" y="80" width="14" height="40" fill="#9aa1a8" stroke="{INK}"/>' + txt(60, 216, "indústria", 9.5)
    b += f'<rect x="110" y="176" width="64" height="18" rx="6" fill="{BLUE}" stroke="{INK}"/><path d="M122 176 L132 162 L156 162 L166 176" fill="#cfe2f5" stroke="{INK}"/><circle cx="124" cy="196" r="6" fill="{INK}"/><circle cx="160" cy="196" r="6" fill="{INK}"/>' + txt(142, 216, "trànsit", 9.5)
    for (x, y) in ((62, 70), (104, 184)):
        b += f'<path d="M{x} {y} q-10 -20 10 -30 q-6 -16 16 -22 q10 -10 26 -4" fill="none" stroke="{MUT}" stroke-width="2"/>'
    b += txt(150, 40, "SO₂ i NOₓ", 11, weight=700)
    b += f'<line x1="200" y1="44" x2="290" y2="60" stroke="{MUT}" stroke-width="1.6" marker-end="url(#pa)"/>'
    # núvol
    b += f'<path d="M300 80 q-10 -30 25 -32 q10 -26 45 -14 q30 -10 40 18 q30 4 20 28 Z" fill="#dfe3e8" stroke="{INK}" stroke-width="1.2"/>' + txt(360, 72, "+ aigua → àcids", 10, weight=700)
    for k in range(9):
        x = 320 + k * 12
        b += f'<line x1="{x}" y1="{96+(k%3)*8}" x2="{x-6}" y2="{116+(k%3)*8}" stroke="{BLUE}" stroke-width="1.6"/>'
    b += txt(360, 150, "pluja àcida (pH < 5,6)", 10, fill=BLUE, weight=700)
    # monument
    b += f'<rect x="470" y="110" width="110" height="90" fill="#efe9dc" stroke="{INK}" stroke-width="1.4"/><polygon points="460,110 590,110 525,74" fill="#efe9dc" stroke="{INK}" stroke-width="1.4"/>'
    for k in range(4): b += f'<rect x="{484+k*24}" y="118" width="10" height="82" fill="#e3dccb" stroke="{MUT}" stroke-width=".7"/>'
    b += f'<path d="M470 110 q10 18 0 40 M580 110 q-8 20 0 46 M500 112 q4 6 0 12" stroke="#3a3f45" stroke-width="5" fill="none" opacity=".55"/>'
    b += txt(525, 216, "pedra calcària (CaCO₃)", 9.5)
    b += txt(320, 186, "CaCO₃ + H₂SO₄ → CaSO₄ (guix) + CO₂ + H₂O", 10, weight=700, fill=A)
    return svg(640, 230, b, "160mm")

def sis_claus(A="#B8742A"):
    b = ""
    tubs = [("aire sec", "clorur de calci", False, False, "no"), ("aigua bullida i oli", "sense oxigen", True, False, "no"), ("aigua i aire", "", True, True, "sí"),
            ("aigua salada", "", True, True, "molt"), ("pintat, aigua i aire", "", True, False, "no"), ("embolicat amb zinc", "", True, False, "no")]
    for i, (t, s, aigua, rov, res) in enumerate(tubs):
        x = 50 + i * 95
        b += f'<path d="M{x-16} 30 L{x-16} 150 Q{x-16} 166 {x} 166 Q{x+16} 166 {x+16} 150 L{x+16} 30" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
        if aigua: b += f'<path d="M{x-14.5} 80 L{x+14.5} 80 L{x+14.5} 150 Q{x+14.5} 164.5 {x} 164.5 Q{x-14.5} 164.5 {x-14.5} 150 Z" fill="{"#cfe3f1" if i != 3 else "#bcd8ec"}"/>'
        if i == 1: b += f'<rect x="{x-14.5}" y="70" width="29" height="10" fill="#f3d77a"/>'
        if i == 0: b += f'<path d="M{x-14.5} 140 L{x+14.5} 140 L{x+14.5} 150 Q{x+14.5} 164.5 {x} 164.5 Q{x-14.5} 164.5 {x-14.5} 150 Z" fill="#fff" stroke="{MUT}" stroke-dasharray="2 2"/>'
        nail = "#8c9096" if i != 4 else "#2f6fb5"
        if i == 5: nail = "#b8bfc6"
        b += f'<rect x="{x-3}" y="50" width="6" height="96" fill="{nail}" stroke="{INK}" stroke-width=".8"/><rect x="{x-8}" y="46" width="16" height="5" fill="{nail}" stroke="{INK}" stroke-width=".8"/>'
        if rov:
            for k in range(6 if i == 3 else 3): b += f'<circle cx="{x+(-3 if k%2 else 3)}" cy="{90+k*9}" r="{3.4 if i == 3 else 2.6}" fill="#b5541b"/>'
        b += f'<rect x="{x-18}" y="26" width="36" height="8" rx="2" fill="#7a5c3a"/>' if i in (0, 1) else ""
        b += txt(x, 184, t.split(", ")[0] if len(t) < 16 else t[:t.find(" ", 8)], 9, weight=700) + txt(x, 196, t[t.find(" ", 8)+1:] if len(t) >= 16 else s, 8.5, fill=MUT) + txt(x, 212, f"rovell: {res}", 9.5, fill=(RED if res != "no" else GRN), weight=700)
    return svg(590, 220, b, "160mm")

def pila_daniell(A="#B8742A"):
    b = arrow_defs("pdn", BLUE)
    def vas(x, col, metal, lab, ion):
        s = f'<path d="M{x-55} 90 L{x-55} 200 Q{x-55} 206 {x-49} 206 L{x+49} 206 Q{x+55} 206 {x+55} 200 L{x+55} 90" fill="none" stroke="{INK}" stroke-width="1.6"/><path d="M{x-53.5} 120 L{x+53.5} 120 L{x+53.5} 200 Q{x+53.5} 204.5 {x+49} 204.5 L{x-49} 204.5 Q{x-53.5} 204.5 {x-53.5} 200 Z" fill="{col}"/>'
        s += f'<rect x="{x-9}" y="60" width="18" height="120" fill="{metal}" stroke="{INK}" stroke-width="1.2"/>' + txt(x, 226, lab, 10.5, weight=700) + txt(x, 241, ion, 9.5, fill=MUT)
        return s
    b += vas(110, "#eef0f2", "#b8bfc6", "ànode (−): zinc", "Zn → Zn²⁺ + 2 e⁻ (s'oxida)") + vas(370, "#9cc7ea", "#c8743a", "càtode (+): coure", "Cu²⁺ + 2 e⁻ → Cu (es redueix)")
    b += f'<path d="M150 140 L150 100 Q150 86 164 86 L316 86 Q330 86 330 100 L330 140" fill="none" stroke="#e8e0c8" stroke-width="16"/><path d="M150 140 L150 100 Q150 86 164 86 L316 86 Q330 86 330 100 L330 140" fill="none" stroke="{INK}" stroke-width="1" stroke-dasharray="0"/>' + txt(240, 80, "pont salí", 9.5, fill=MUT)
    b += f'<path d="M110 60 L110 30 L370 30 L370 60" fill="none" stroke="{INK}" stroke-width="1.6"/><circle cx="240" cy="30" r="16" fill="#fff" stroke="{INK}" stroke-width="1.6"/>' + txt(240, 35, "V", 12, weight=700)
    b += f'<line x1="150" y1="20" x2="210" y2="20" stroke="{BLUE}" stroke-width="2" marker-end="url(#pdn)"/>' + txt(180, 14, "e⁻", 10, fill=BLUE, weight=700)
    b += txt(240, 262, "Els electrons van del metall més reactiu (Zn) al menys reactiu (Cu): ≈ 1,1 V.", 9.5, fill=MUT)
    return svg(480, 270, b, "130mm")

# ================================================================= 4t · SdA 5
def vector_components(A="#D14B66"):
    b = arrow_defs("vc", A) + arrow_defs("vc2", INK) + arrow_defs("ax")
    x0, y0 = 60, 200
    b += axes(x0, y0, 300, 180, "x (m)", "y (m)")
    for k in range(1, 6):
        b += f'<line x1="{x0+k*50}" y1="{y0}" x2="{x0+k*50}" y2="{y0-170}" stroke="#eef0f2"/>' + txt(x0 + k * 50, y0 + 15, str(k * 100), 9)
        if k < 4: b += f'<line x1="{x0}" y1="{y0-k*50}" x2="{x0+290}" y2="{y0-k*50}" stroke="#eef0f2"/>' + txt(x0 - 6, y0 - k * 50 + 4, str(k * 100), 9, "end")
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0+200}" y2="{y0}" stroke="{INK}" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#vc2)"/>' + txt(x0 + 100, y0 - 8, "Δx = 400 m", 10)
    b += f'<line x1="{x0+200}" y1="{y0}" x2="{x0+200}" y2="{y0-150}" stroke="{INK}" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#vc2)"/>' + txt(x0 + 208, y0 - 75, "Δy = 300 m", 10, "start")
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0+198}" y2="{y0-148}" stroke="{A}" stroke-width="3" marker-end="url(#vc)"/>' + txt(x0 + 80, y0 - 80, "Δr", 12, fill=A, weight=700)
    b += f'<path d="M{x0+36} {y0} A36 36 0 0 0 {x0+29} {y0-22}" fill="none" stroke="{MUT}"/>' + txt(x0 + 44, y0 - 8, "α", 10, "start", MUT)
    b += txt(400, 60, "Δr = (400, 300) m", 11, "start", INK, 700)
    b += txt(400, 86, "Mòdul (Pitàgores):", 10, "start") + txt(400, 102, "|Δr| = √(400² + 300²) = 500 m", 10.5, "start", A, 700)
    b += txt(400, 130, "La distància pels carrers", 10, "start") + txt(400, 144, "de l'Eixample és 700 m;", 10, "start") + txt(400, 158, "el desplaçament, 500 m.", 10, "start")
    return svg(620, 220, b, "150mm")

def distancia_aturada(A="#D14B66"):
    b = arrow_defs("da", INK)
    def car(x, y):
        return f'<rect x="{x}" y="{y}" width="56" height="18" rx="6" fill="{BLUE}" stroke="{INK}"/><path d="M{x+10} {y} L{x+18} {y-12} L{x+40} {y-12} L{x+48} {y}" fill="#cfe2f5" stroke="{INK}"/><circle cx="{x+12}" cy="{y+20}" r="6" fill="{INK}"/><circle cx="{x+44}" cy="{y+20}" r="6" fill="{INK}"/>'
    for row, (v, dr, df) in enumerate(((50, 14, 14), (30, 8.3, 5))):
        y = 50 + row * 90
        sc = 13
        b += f'<rect x="20" y="{y+26}" width="600" height="6" fill="#9aa1a8"/>'
        b += car(20, y)
        xr = 76 + dr * sc; xf = xr + df * sc
        b += f'<rect x="76" y="{y+34}" width="{dr*sc}" height="12" fill="#f6c99a"/><rect x="{xr}" y="{y+34}" width="{df*sc}" height="12" fill="{A}" opacity=".8"/>'
        b += txt(76 + dr * sc / 2, y + 62, f"reacció {str(dr).replace('.', ',')} m", 9.5) + txt(xr + df * sc / 2, y + 62, f"frenada {df} m", 9.5)
        b += f'<rect x="{xf}" y="{y-14}" width="6" height="40" fill="{RED}"/>' + txt(xf + 12, y + 4, f"{v} km/h → s'atura a {str(round(dr+df,1)).replace('.', ',')} m", 10.5, "start", INK, 700)
    b += txt(320, 225, "Temps de reacció 1 s · frenada amb a = −7 m/s². A 50 km/h la distància d'aturada és el doble que a 30 km/h.", 9.5, fill=MUT)
    return svg(640, 235, b, "165mm")

def caiguda_lliure(A="#D14B66"):
    b = arrow_defs("cll", A) + arrow_defs("ax")
    for k, d in enumerate([0, 4.9, 19.6, 44.1]):
        y = 26 + d * 3.9
        b += f'<circle cx="80" cy="{y:.0f}" r="7" fill="{A}" stroke="{INK}"/>' + txt(100, y + 4, f"t = {k} s · {str(d).replace('.', ',')} m", 9.5, "start")
        if k: b += f'<line x1="62" y1="{y-6:.0f}" x2="62" y2="{y-6+k*9:.0f}" stroke="{A}" stroke-width="2" marker-end="url(#cll)"/>'
    b += txt(30, 120, "v creix", 9, "start", A, 700)
    x0, y0 = 260, 210
    b += axes(x0, y0, 220, 175, "t (s)", "v (m/s)")
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0+200}" y2="{y0-160}" stroke="{A}" stroke-width="2.6"/>'
    for k in range(1, 5): b += f'<line x1="{x0+k*50}" y1="{y0}" x2="{x0+k*50}" y2="{y0+5}" stroke="{INK}"/>' + txt(x0 + k * 50, y0 + 16, str(k), 9) + txt(x0 - 6, y0 - k * 40 + 4, f"{k*9.8:.1f}".replace(".", ","), 9, "end")
    b += txt(510, 70, "v = g · t", 11, "start", A, 700) + txt(510, 90, "y = ½ · g · t²", 11, "start", A, 700) + txt(510, 110, "g = 9,8 m/s²", 10, "start")
    b += txt(510, 140, "Sense aire, tots els cossos", 9.5, "start", MUT) + txt(510, 153, "cauen igual de de pressa.", 9.5, "start", MUT)
    return svg(680, 232, b, "155mm")

def velocitat_limit(A="#D14B66"):
    b = arrow_defs("vl", A) + arrow_defs("vl2", BLUE) + arrow_defs("vl3", GRN) + arrow_defs("ax")
    b += f'<path d="M40 20 L40 220 Q40 228 48 228 L132 228 Q140 228 140 220 L140 20" fill="#f6efc9" stroke="{INK}" stroke-width="1.6"/>' + txt(90, 246, "bola en glicerina", 10, weight=700)
    cx, cy = 90, 120
    b += at(cx, cy, "#8c9096", 14)
    b += f'<line x1="{cx}" y1="{cy+14}" x2="{cx}" y2="{cy+74}" stroke="{A}" stroke-width="2.6" marker-end="url(#vl)"/>' + txt(cx + 8, cy + 70, "P", 11, "start", A, 700)
    b += f'<line x1="{cx-5}" y1="{cy-14}" x2="{cx-5}" y2="{cy-44}" stroke="{BLUE}" stroke-width="2.6" marker-end="url(#vl2)"/>' + txt(cx - 14, cy - 18, "E (empenta)", 9.5, "end", BLUE, 700)
    b += f'<line x1="{cx+5}" y1="{cy-14}" x2="{cx+5}" y2="{cy-44}" stroke="{GRN}" stroke-width="2.6" marker-end="url(#vl3)"/>' + txt(cx + 12, cy - 48, "F (fregament)", 9.5, "start", GRN, 700)
    x0, y0 = 250, 200
    b += axes(x0, y0, 260, 160, "t", "v")
    pts = " ".join(f"{x0+t:.0f},{y0-130*(1-math.exp(-t/45)):.0f}" for t in range(0, 251, 5))
    b += f'<polyline points="{pts}" fill="none" stroke="{A}" stroke-width="2.6"/><line x1="{x0}" y1="{y0-130}" x2="{x0+250}" y2="{y0-130}" stroke="{MUT}" stroke-dasharray="4 3"/>' + txt(x0 + 255, y0 - 126, "v límit", 10, "start", MUT, 700)
    b += txt(x0 + 10, 232, "Quan P = E + F, la força resultant és zero:", 10, "start") + txt(x0 + 10, 246, "la bola baixa a velocitat constant.", 10, "start")
    return svg(580, 254, b, "145mm")

def pla_inclinat(A="#D14B66"):
    b = arrow_defs("pi", A) + arrow_defs("pi2", BLUE) + arrow_defs("pi3", MUT) + arrow_defs("pi4", GRN)
    ang = math.radians(25)
    b += f'<polygon points="40,220 400,220 400,{220-360*math.tan(ang):.0f}" fill="#eef0f2" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<path d="M100 220 A60 60 0 0 0 {40+60*math.cos(ang)+0:.0f} {220-60*math.sin(ang):.0f}" fill="none" stroke="{INK}"/>' + txt(110, 212, "α", 11, "start")
    cx, cy = 260, 220 - 220 * math.tan(ang) - 22
    rot = -25
    b += f'<g transform="rotate({rot} {cx} {cy+2})"><rect x="{cx-28}" y="{cy-20}" width="56" height="40" rx="3" fill="#f6c99a" stroke="{INK}" stroke-width="1.4"/></g>'
    ux, uy = math.cos(ang), -math.sin(ang)   # al llarg del pla (amunt)
    nx, ny = math.sin(ang), math.cos(ang)    # perpendicular cap avall (cap al pla)
    L = 90
    b += f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+L}" stroke="{A}" stroke-width="2.6" marker-end="url(#pi)"/>' + txt(cx + 6, cy + L + 4, "P", 11, "start", A, 700)
    px, py = cx - ux * L * math.sin(ang), cy - uy * L * math.sin(ang)
    b += f'<line x1="{cx}" y1="{cy}" x2="{px:.0f}" y2="{py:.0f}" stroke="{MUT}" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#pi3)"/>' + txt(px - 6, py + 2, "Pₓ = P · sin α", 9.5, "end", MUT, 700)
    qx, qy = cx + nx * L * math.cos(ang), cy + ny * L * math.cos(ang)
    b += f'<line x1="{cx}" y1="{cy}" x2="{qx:.0f}" y2="{qy:.0f}" stroke="{MUT}" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#pi3)"/>' + txt(qx + 6, qy + 10, "Pᵧ = P · cos α", 9.5, "start", MUT, 700)
    b += f'<line x1="{cx}" y1="{cy}" x2="{cx-nx*L*math.cos(ang):.0f}" y2="{cy-ny*L*math.cos(ang):.0f}" stroke="{BLUE}" stroke-width="2.6" marker-end="url(#pi2)"/>' + txt(cx - nx * L * math.cos(ang) - 4, cy - ny * L * math.cos(ang) - 6, "N", 11, "middle", BLUE, 700)
    b += f'<line x1="{cx}" y1="{cy}" x2="{cx+ux*55:.0f}" y2="{cy+uy*55:.0f}" stroke="{GRN}" stroke-width="2.6" marker-end="url(#pi4)"/>' + txt(cx + ux * 55 + 6, cy + uy * 55 - 4, "f (fregament)", 10, "start", GRN, 700)
    b += txt(440, 70, "N = Pᵧ = m · g · cos α", 10.5, "start", INK, 700) + txt(440, 92, "f = μ · N", 10.5, "start", INK, 700)
    b += txt(440, 122, "A l'angle límit, just abans", 10, "start") + txt(440, 136, "de lliscar: μ = tan α", 10, "start", A, 700)
    return svg(640, 235, b, "150mm")

def diagrama_cotxe(A="#D14B66"):
    b = arrow_defs("dc", A) + arrow_defs("dc2", BLUE) + arrow_defs("dc3", GRN) + arrow_defs("dc4", ORA)
    b += f'<rect x="20" y="135" width="520" height="6" fill="#9aa1a8"/>'
    x, y = 220, 80
    b += f'<rect x="{x}" y="{y}" width="140" height="40" rx="10" fill="{BLUE}" stroke="{INK}" stroke-width="1.5"/><path d="M{x+25} {y} L{x+45} {y-28} L{x+100} {y-28} L{x+120} {y}" fill="#cfe2f5" stroke="{INK}" stroke-width="1.5"/><circle cx="{x+30}" cy="{y+42}" r="13" fill="{INK}"/><circle cx="{x+110}" cy="{y+42}" r="13" fill="{INK}"/>'
    cx, cy = x + 70, y + 20
    b += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{INK}"/>'
    b += f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+70}" stroke="{A}" stroke-width="2.6" marker-end="url(#dc)"/>' + txt(cx + 6, cy + 72, "P (pes)", 10.5, "start", A, 700)
    b += f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-70}" stroke="{BLUE}" stroke-width="2.6" marker-end="url(#dc2)"/>' + txt(cx + 6, cy - 62, "N (normal)", 10.5, "start", BLUE, 700)
    b += f'<line x1="{cx}" y1="{cy}" x2="{cx+130}" y2="{cy}" stroke="{GRN}" stroke-width="2.6" marker-end="url(#dc3)"/>' + txt(cx + 134, cy + 4, "F motor", 10.5, "start", GRN, 700)
    b += f'<line x1="{cx}" y1="{cy}" x2="{cx-90}" y2="{cy}" stroke="{ORA}" stroke-width="2.6" marker-end="url(#dc4)"/>' + txt(cx - 94, cy + 4, "f (fregament i aire)", 10.5, "end", ORA, 700)
    b += txt(280, 205, "ΣF = F motor − f = m · a   ·   en vertical, N = P", 10.5, weight=700)
    return svg(560, 214, b, "145mm")

# ================================================================= 4t · SdA 6
def pressio_superficie(A="#1D5C8C"):
    b = arrow_defs("ps", A)
    # sabata vs raqueta a la neu
    b += f'<rect x="20" y="150" width="560" height="60" fill="#f2f6fa" stroke="{MUT}"/>'
    for i, (x, w, dep, lab, sub) in enumerate(((120, 40, 40, "bota", "S petita: molta pressió, s'enfonsa"), (330, 150, 8, "raqueta de neu", "S gran: poca pressió, no s'enfonsa"))):
        b += f'<path d="M{x-w/2} {150} L{x-w/2} {150+dep} L{x+w/2} {150+dep} L{x+w/2} 150" fill="#e3ebf3" stroke="{MUT}" stroke-dasharray="3 2"/>'
        b += f'<rect x="{x-w/2}" y="{150+dep-10}" width="{w}" height="10" rx="3" fill="{"#7a5c3a" if i == 0 else "#c9a27a"}" stroke="{INK}"/>'
        b += f'<line x1="{x}" y1="40" x2="{x}" y2="{140+dep-12}" stroke="{A}" stroke-width="3" marker-end="url(#ps)"/>' + txt(x + 8, 60, "F = 600 N", 10, "start", A, 700)
        b += txt(x, 230, lab, 10.5, weight=700) + txt(x, 244, sub, 9.5, fill=MUT)
    fr, w = sfrac(495, 82, "F", "S", 14, A)
    b += txt(470, 87, "p =", 14, "start", A, 700) + fr + txt(470, 120, "p en pascals (Pa)", 10, "start") + txt(470, 134, "1 Pa = 1 N/m²", 10, "start")
    return svg(600, 252, b, "150mm")

def pressio_hidrostatica(A="#1D5C8C"):
    b = arrow_defs("ph", A)
    b += f'<rect x="40" y="20" width="200" height="200" fill="{LIQ}" stroke="{INK}" stroke-width="1.8"/><line x1="40" y1="40" x2="240" y2="40" stroke="#9cc9e8" stroke-width="2"/>'
    for k, (h, L) in enumerate(((40, 14), (85, 28), (130, 42), (170, 54))):
        y = 40 + h * 0.95
        b += f'<line x1="{140-L}" y1="{y:.0f}" x2="{140+L}" y2="{y:.0f}" stroke="{A}" stroke-width="2" marker-start="url(#ph)" marker-end="url(#ph)"/>'
    b += f'<path d="M40 225 L240 225" stroke="{INK}"/>'
    b += f'<line x1="255" y1="40" x2="255" y2="210" stroke="{INK}" stroke-width="1" marker-end="url(#ph)"/>' + txt(262, 130, "h", 11, "start", INK, 700)
    b += txt(310, 60, "p = ρ · g · h", 14, "start", A, 700) + txt(310, 82, "ρ: densitat del líquid (kg/m³)", 10, "start") + txt(310, 98, "g = 9,8 m/s² · h: profunditat (m)", 10, "start")
    b += txt(310, 128, "Com més avall, més pressió.", 10, "start", INK, 700) + txt(310, 144, "A una mateixa profunditat, la pressió", 10, "start") + txt(310, 158, "és igual en totes direccions.", 10, "start")
    b += txt(310, 188, "Cada 10 m d'aigua: ≈ +1 atm.", 10, "start", A, 700)
    return svg(590, 235, b, "145mm")

def premsa_hidraulica(A="#1D5C8C"):
    b = arrow_defs("pr", A)
    b += f'<path d="M60 60 L60 180 L420 180 L420 100 L300 100 L300 160 L110 160 L110 60" fill="{LIQ}" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<rect x="58" y="92" width="54" height="14" fill="#8c9096" stroke="{INK}"/><rect x="298" y="86" width="124" height="14" fill="#8c9096" stroke="{INK}"/>'
    b += f'<line x1="85" y1="30" x2="85" y2="88" stroke="{A}" stroke-width="3" marker-end="url(#pr)"/>' + txt(95, 40, "F₁ petita", 10.5, "start", A, 700)
    b += f'<rect x="320" y="40" width="80" height="46" rx="4" fill="{BLUE}" stroke="{INK}"/>' + txt(360, 68, "cotxe", 10, fill="#fff", weight=700)
    b += f'<line x1="360" y1="130" x2="360" y2="102" stroke="{A}" stroke-width="3" marker-end="url(#pr)"/>' + txt(368, 125, "F₂ gran", 10.5, "start", A, 700)
    b += txt(85, 200, "S₁ petita", 10) + txt(360, 200, "S₂ gran", 10)
    b += txt(450, 90, "Pascal: la pressió es transmet", 10, "start") + txt(450, 104, "igual a tot el líquid.", 10, "start")
    f1, w1 = sfrac(450, 136, "F₁", "S₁", 13, A); f2, w2 = sfrac(450 + w1 + 22, 136, "F₂", "S₂", 13, A)
    b += f1 + txt(450 + w1 + 11, 141, "=", 13, "middle", A, 700) + f2
    b += txt(450, 176, "Si S₂ = 50 · S₁, F₂ = 50 · F₁.", 10, "start")
    return svg(640, 210, b, "150mm")

def torricelli(A="#1D5C8C"):
    b = arrow_defs("to", A)
    b += f'<path d="M60 200 L60 240 L220 240 L220 200" fill="none" stroke="{INK}" stroke-width="1.8"/><rect x="61.5" y="210" width="157" height="28.5" fill="#b9bec4"/>'
    b += f'<rect x="125" y="20" width="30" height="210" fill="#fff" stroke="{INK}" stroke-width="1.8"/><rect x="126.5" y="58" width="27" height="171" fill="#b9bec4"/>'
    b += txt(166, 40, "buit", 9.5, "start", MUT)
    b += f'<line x1="245" y1="58" x2="245" y2="210" stroke="{INK}" stroke-width="1" marker-start="url(#to)" marker-end="url(#to)"/>' + txt(252, 140, "760 mm", 10.5, "start", INK, 700)
    for x in (80, 200): b += f'<line x1="{x}" y1="170" x2="{x}" y2="204" stroke="{A}" stroke-width="2.4" marker-end="url(#to)"/>'
    b += txt(70, 150, "pressió", 9.5, fill=A, weight=700) + txt(70, 163, "atmosfèrica", 9.5, fill=A, weight=700)
    b += txt(320, 60, "Torricelli (1643): l'aire empeny el", 10, "start") + txt(320, 74, "mercuri de la cubeta i aguanta una", 10, "start") + txt(320, 88, "columna de 760 mm al nivell del mar.", 10, "start")
    b += txt(320, 118, "1 atm = 760 mmHg = 101 325 Pa", 11, "start", A, 700)
    b += txt(320, 148, "A dalt d'una muntanya hi ha menys", 10, "start") + txt(320, 162, "aire a sobre: la columna baixa.", 10, "start")
    return svg(580, 250, b, "145mm")

def empenta(A="#1D5C8C"):
    b = arrow_defs("em", A) + arrow_defs("em2", RED)
    b += f'<rect x="30" y="30" width="260" height="200" fill="{LIQ}" stroke="{INK}" stroke-width="1.8"/><line x1="30" y1="50" x2="290" y2="50" stroke="#9cc9e8" stroke-width="2"/>'
    b += f'<rect x="120" y="100" width="80" height="80" fill="#f6c99a" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<line x1="160" y1="70" x2="160" y2="98" stroke="{A}" stroke-width="2.4" marker-end="url(#em)"/>' + txt(168, 82, "F dalt (p petita)", 9.5, "start", A)
    b += f'<line x1="160" y1="232" x2="160" y2="182" stroke="{A}" stroke-width="3.4" marker-end="url(#em)"/>' + txt(168, 222, "F baix (p més gran)", 9.5, "start", A)
    for y in (125, 155):
        b += f'<line x1="92" y1="{y}" x2="118" y2="{y}" stroke="{A}" stroke-width="2" marker-end="url(#em)"/><line x1="228" y1="{y}" x2="202" y2="{y}" stroke="{A}" stroke-width="2" marker-end="url(#em)"/>'
    b += txt(330, 70, "Les forces laterals s'anul·len.", 10, "start") + txt(330, 88, "La de baix és més gran que la de dalt:", 10, "start") + txt(330, 102, "en resulta una força cap amunt, l'empenta.", 10, "start")
    b += txt(330, 134, "Principi d'Arquimedes:", 10.5, "start", INK, 700) + txt(330, 152, "E = ρ líquid · V submergit · g", 12, "start", A, 700)
    b += txt(330, 174, "L'empenta és igual al pes del", 10, "start") + txt(330, 188, "líquid desallotjat.", 10, "start")
    b += txt(330, 214, "Pes aparent = P − E", 10.5, "start", INK, 700)
    return svg(620, 240, b, "150mm")

def flotacio(A="#1D5C8C"):
    b = arrow_defs("fl", RED) + arrow_defs("fl2", A)
    b += f'<rect x="20" y="30" width="540" height="180" fill="{LIQ}" stroke="{INK}" stroke-width="1.8"/><line x1="20" y1="50" x2="560" y2="50" stroke="#9cc9e8" stroke-width="2"/>'
    cases = [("s'enfonsa", "P > E · ρ objecte > ρ líquid", 165, 46, 30), ("equilibri", "P = E · ρ objecte = ρ líquid", 110, 38, 38), ("sura", "P = E amb part fora · ρ objecte < ρ líquid", 54, 26, 26)]
    for i, (t, s, y, lp, le) in enumerate(cases):
        x = 110 + i * 180
        b += f'<rect x="{x-22}" y="{y-22}" width="44" height="44" rx="4" fill="{"#8c9096" if i == 0 else ("#f6c99a" if i == 1 else "#e1b878")}" stroke="{INK}" stroke-width="1.4"/>'
        b += f'<line x1="{x+8}" y1="{y}" x2="{x+8}" y2="{y+lp}" stroke="{RED}" stroke-width="2.4" marker-end="url(#fl)"/><line x1="{x-8}" y1="{y}" x2="{x-8}" y2="{y-le}" stroke="{A}" stroke-width="2.4" marker-end="url(#fl2)"/>'
        b += txt(x + 14, y + lp - 2, "P", 10, "start", RED, 700) + txt(x - 14, y - le + 8, "E", 10, "end", A, 700)
        b += txt(x, 232, t, 11, weight=700) + txt(x, 247, s, 9, fill=MUT)
    return svg(580, 254, b, "155mm")

def submari(A="#1D5C8C"):
    b = arrow_defs("sb", A)
    for i, (t, w, s) in enumerate((("Per baixar", 0.8, "s'omplen els tancs d'aigua: més massa, ρ mitjana > ρ aigua"), ("Per pujar", 0.15, "s'expulsa l'aigua amb aire: ρ mitjana < ρ aigua"))):
        x, y = 160 + i * 320, 100
        b += f'<ellipse cx="{x}" cy="{y}" rx="110" ry="40" fill="#e8e2c8" stroke="{INK}" stroke-width="1.8"/><rect x="{x-20}" y="{y-62}" width="40" height="26" rx="6" fill="#e8e2c8" stroke="{INK}" stroke-width="1.6"/>'
        for sx in (-1, 1):
            tx = x + sx * 62
            b += f'<rect x="{tx-24}" y="{y-20}" width="48" height="40" rx="8" fill="#fff" stroke="{INK}" stroke-width="1.2"/>'
            h = 40 * w
            b += f'<rect x="{tx-23}" y="{y+20-h:.0f}" width="46" height="{h:.0f}" rx="6" fill="#7fb6df"/>'
        b += txt(x, y + 4, "tripulació", 9, fill=MUT)
        b += f'<line x1="{x}" y1="{y+(48 if i == 0 else -70)}" x2="{x}" y2="{y+(78 if i == 0 else -100)}" stroke="{A}" stroke-width="2.6" marker-end="url(#sb)"/>'
        b += txt(x, 196, t, 11, weight=700) + txt(x, 211, s, 9, fill=MUT)
    return svg(640, 220, b, "160mm")

def manometre(A="#1D5C8C"):
    b = arrow_defs("mn", A)
    b += f'<rect x="30" y="40" width="150" height="190" fill="{LIQ}" stroke="{INK}" stroke-width="1.8"/><line x1="30" y1="60" x2="180" y2="60" stroke="#9cc9e8" stroke-width="2"/>'
    b += f'<path d="M100 170 L200 170 L200 30 M100 170 L100 178" fill="none" stroke="{INK}" stroke-width="2"/><circle cx="100" cy="170" r="8" fill="#fff" stroke="{INK}" stroke-width="1.6"/>' + txt(70, 196, "càpsula", 9.5, fill=MUT)
    b += f'<path d="M200 30 L200 210 Q200 230 220 230 Q240 230 240 210 L240 30" fill="none" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<path d="M201 120 L201 210 Q201 228.5 220 228.5 Q239 228.5 239 210 L239 80 L231 80 L231 210 Q231 220 220 220 Q209 220 209 210 L209 120 Z" fill="{RED}" opacity=".8"/>'
    b += f'<line x1="250" y1="80" x2="250" y2="120" stroke="{INK}" marker-start="url(#mn)" marker-end="url(#mn)"/>' + txt(256, 104, "Δh", 11, "start", INK, 700)
    b += txt(290, 70, "Com més avall posem la càpsula,", 10, "start") + txt(290, 84, "més empeny el líquid acolorit", 10, "start") + txt(290, 98, "del tub en U: Δh augmenta.", 10, "start")
    b += txt(290, 128, "Si girem la càpsula a la mateixa", 10, "start") + txt(290, 142, "profunditat, Δh no canvia.", 10, "start")
    b += txt(290, 172, "En aigua salada (més densa), Δh", 10, "start") + txt(290, 186, "és més gran a la mateixa profunditat.", 10, "start")
    return svg(560, 240, b, "140mm")
