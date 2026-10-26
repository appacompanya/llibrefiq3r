"""Il·lustracions vectorials per als dossiers de teoria (SdA 1). Estil pla: traç fosc d'1,6 px, colors suaus i etiquetes curtes."""
INK = "#1f2328"; MUT = "#5d646d"; ACC = "#2F8F95"; TINT = "#E3F1F2"
WATER = "#cfe6f5"; WATER2 = "#a9d2ee"; GLASS = "#ffffff"; OIL = "#f3d77a"; HONEY = "#e7a13a"; GLY = "#e6ddf3"
FONT = 'font-family="Verdana,sans-serif"'

def svg(w, h, body, width="150mm"):
    return f'<svg viewBox="0 0 {w} {h}" width="{width}" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:0 auto;max-width:100%" {FONT}>{body}</svg>'
def txt(x, y, t, size=11, anchor="middle", fill=INK, weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}">{t}</text>'
def arrow_defs(id_="ar", col=INK):
    return f'<defs><marker id="{id_}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{col}"/></marker></defs>'

# ---------- 1. Lectura de la proveta: menisc i paral·laxi ----------
def proveta_menisc():
    b = arrow_defs("am")
    # proveta gran retallada (zoom)
    x0, w = 150, 120
    b += f'<rect x="{x0}" y="20" width="{w}" height="200" rx="4" fill="{GLASS}" stroke="{INK}" stroke-width="1.8"/>'
    b += f'<path d="M{x0+1} 126 Q{x0+w/2} 154 {x0+w-1} 126 L{x0+w-1} 219 L{x0+1} 219 Z" fill="{WATER}"/>'
    b += f'<path d="M{x0+1} 126 Q{x0+w/2} 154 {x0+w-1} 126" fill="none" stroke="{WATER2}" stroke-width="2.5"/>'
    for i, v in enumerate(range(40, 30, -1)):
        y = 40 + i * 20; L = 34 if v % 5 == 0 else 20
        b += f'<line x1="{x0}" y1="{y}" x2="{x0+L}" y2="{y}" stroke="{INK}" stroke-width="1.2"/>'
        if v % 5 == 0: b += txt(x0 + L + 6, y + 4, f"{v} mL", 10, "start")
    # ulls
    def eye(x, y, ok):
        col = ACC if ok else "#c2413a"
        return (f'<ellipse cx="{x}" cy="{y}" rx="16" ry="9" fill="#fff" stroke="{INK}" stroke-width="1.5"/><circle cx="{x+5}" cy="{y}" r="4.5" fill="{INK}"/>'
                f'<line x1="{x+18}" y1="{y}" x2="{x0-6}" y2="{140 if ok else 126}" stroke="{col}" stroke-width="1.6" stroke-dasharray="{"0" if ok else "4 3"}" marker-end="url(#am)"/>')
    b += eye(60, 140, True) + eye(60, 52, False)
    b += txt(60, 170, "Bé: ulls a l'altura", 10.5, fill=ACC, weight=700) + txt(60, 183, "de la base del menisc", 10.5, fill=ACC)
    b += txt(60, 30, "Malament: des de dalt", 10.5, fill="#c2413a", weight=700) + txt(60, 82, "llegeix de més", 10.5, fill="#c2413a")
    # etiqueta menisc
    b += f'<line x1="{x0+w/2}" y1="141" x2="{x0+w+40}" y2="160" stroke="{MUT}" stroke-width="1"/>' + txt(x0 + w + 44, 158, "menisc", 11, "start", MUT, 700) + txt(x0 + w + 44, 172, "(llegim la part de baix)", 10, "start", MUT)
    b += txt(x0 + w + 44, 60, "Lectura: 35 mL", 12, "start", INK, 700) + txt(x0 + w + 44, 76, "Sensibilitat: 1 mL", 11, "start", MUT)
    return svg(470, 230, b, "125mm")

# ---------- 2. Exactitud i precisió: quatre dianes ----------
def dianes():
    import random
    random.seed(4)
    cases = [("Exacta i precisa", 0, 0, 4), ("Precisa però no exacta", 26, -20, 4), ("Exacta però no precisa", 0, 0, 26), ("Ni exacta ni precisa", 22, 18, 26)]
    b = ""
    for i, (t, dx, dy, sp) in enumerate(cases):
        cx, cy = 70 + i * 140, 78
        for r, c in ((56, "#fff"), (42, TINT), (28, "#fff"), (14, ACC)):
            b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" stroke="{INK}" stroke-width="1.3"/>'
        for _ in range(6):
            x = cx + dx + random.uniform(-sp, sp); y = cy + dy + random.uniform(-sp, sp)
            b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="#e0782f" stroke="{INK}" stroke-width="1"/>'
        b += txt(cx, 152, t, 10.5, weight=700)
    return svg(560, 162, b, "160mm")

# ---------- 3. Densitat: columna de líquids i objectes ----------
def columna_densitat():
    b = ""
    x, w, top = 150, 150, 30
    layers = [("oli (0,92 g/cm³)", OIL, 70), ("aigua (1,00 g/cm³)", WATER, 70), ("glicerina (1,26 g/cm³)", GLY, 70), ("mel (1,4 g/cm³)", HONEY, 60)]
    y = top + 20
    for name, col, h in layers:
        b += f'<rect x="{x+2}" y="{y}" width="{w-4}" height="{h}" fill="{col}"/>'
        b += f'<line x1="{x+w+6}" y1="{y+h/2}" x2="{x+w+24}" y2="{y+h/2}" stroke="{MUT}" stroke-width="1"/>' + txt(x + w + 28, y + h / 2 + 4, name, 11, "start")
        y += h
    b += f'<path d="M{x} {top} L{x} {y+4} Q{x} {y+14} {x+12} {y+14} L{x+w-12} {y+14} Q{x+w} {y+14} {x+w} {y+4} L{x+w} {top}" fill="none" stroke="{INK}" stroke-width="2"/>'
    # objectes
    b += f'<rect x="{x+20}" y="{top+30}" width="34" height="18" rx="4" fill="#c9a26b" stroke="{INK}" stroke-width="1.3"/>' + txt(x - 10, top + 44, "suro", 11, "end") + f'<line x1="{x-6}" y1="{top+40}" x2="{x+18}" y2="{top+40}" stroke="{MUT}"/>'
    b += f'<circle cx="{x+95}" cy="{top+20+70+66}" r="11" fill="#7aa64a" stroke="{INK}" stroke-width="1.3"/>' + txt(x - 10, top + 160, "gra de raïm", 11, "end") + f'<line x1="{x-6}" y1="{top+156}" x2="{x+82}" y2="{top+156}" stroke="{MUT}"/>'
    b += f'<polygon points="{x+60},{y+6} {x+74},{y-2} {x+88},{y+6} {x+88},{y+10} {x+60},{y+10}" fill="#9aa1a8" stroke="{INK}" stroke-width="1.3"/>' + txt(x - 10, y + 8, "femella d'acer", 11, "end") + f'<line x1="{x-6}" y1="{y+4}" x2="{x+58}" y2="{y+4}" stroke="{MUT}"/>'
    return svg(520, y + 22, b, "140mm")

# ---------- 4. Volum d'un sòlid irregular (desplaçament) ----------
def desplacament():
    b = arrow_defs("ad")
    def prov(x, level, stone):
        s = f'<rect x="{x}" y="30" width="60" height="190" rx="3" fill="#fff" stroke="{INK}" stroke-width="1.8"/>'
        yl = 220 - level * 1.6
        s += f'<rect x="{x+1}" y="{yl}" width="58" height="{219-yl}" fill="{WATER}"/><line x1="{x+1}" y1="{yl}" x2="{x+59}" y2="{yl}" stroke="{WATER2}" stroke-width="2"/>'
        for v in range(0, 101, 10):
            y = 220 - v * 1.6
            s += f'<line x1="{x}" y1="{y}" x2="{x+(14 if v%50==0 else 8)}" y2="{y}" stroke="{INK}" stroke-width="1"/>'
            if v % 20 == 0: s += txt(x - 4, y + 4, str(v), 9, "end", MUT)
        if stone: s += f'<path d="M{x+18} 212 Q{x+14} 196 {x+28} 192 Q{x+44} 188 {x+44} 202 Q{x+46} 214 {x+30} 214 Z" fill="#8c8f94" stroke="{INK}" stroke-width="1.3"/>'
        return s
    b += prov(60, 50, False) + prov(250, 64, True)
    b += txt(90, 245, "Abans: 50 mL", 11, weight=700) + txt(280, 245, "Després: 64 mL", 11, weight=700)
    b += f'<line x1="140" y1="130" x2="230" y2="130" stroke="{INK}" stroke-width="1.6" marker-end="url(#ad)"/>' + txt(185, 122, "hi deixem caure", 10, fill=MUT) + txt(185, 146, "la pedra", 10, fill=MUT)
    b += f'<rect x="345" y="95" width="150" height="70" rx="10" fill="{TINT}" stroke="{ACC}" stroke-width="1.5"/>' + txt(420, 122, "V pedra = 64 − 50", 12, weight=700) + txt(420, 142, "= 14 mL = 14 cm³", 12, weight=700)
    return svg(510, 255, b, "130mm")

# ---------- 5. Classificació de la matèria amb partícules ----------
def particules_materia():
    b = ""
    boxes = [("Element", "un sol tipus d'àtom", "el"), ("Compost", "àtoms diferents units", "co"), ("Mescla homogènia", "partícules barrejades a tot arreu", "ho"), ("Mescla heterogènia", "zones diferents", "he")]
    import random
    random.seed(7)
    for i, (t, sub, k) in enumerate(boxes):
        x0 = 10 + i * 140
        b += f'<rect x="{x0}" y="10" width="125" height="110" rx="10" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
        pts = [(x0 + 18 + (j % 5) * 22 + random.uniform(-3, 3), 28 + (j // 5) * 22 + random.uniform(-3, 3)) for j in range(20)]
        for j, (x, y) in enumerate(pts):
            if k == "el": b += f'<circle cx="{x}" cy="{y}" r="7" fill="{ACC}" stroke="{INK}" stroke-width="1"/>'
            elif k == "co": b += f'<circle cx="{x-4}" cy="{y}" r="6.5" fill="#e0782f" stroke="{INK}" stroke-width="1"/><circle cx="{x+5}" cy="{y}" r="4.5" fill="#fff" stroke="{INK}" stroke-width="1"/>' if j % 2 == 0 else ""
            elif k == "ho": b += f'<circle cx="{x}" cy="{y}" r="{6.5 if j%3 else 5}" fill="{ACC if j%3 else "#e0782f"}" stroke="{INK}" stroke-width="1"/>'
            else:
                left = x < x0 + 62
                b += f'<circle cx="{x}" cy="{y}" r="6.5" fill="{ACC if left else "#c9a26b"}" stroke="{INK}" stroke-width="1"/>'
        if k == "he": b += f'<line x1="{x0+62}" y1="16" x2="{x0+62}" y2="114" stroke="{MUT}" stroke-dasharray="3 3"/>'
        b += txt(x0 + 62, 138, t, 11, weight=700) + txt(x0 + 62, 152, sub, 9.5, fill=MUT)
    b += f'<line x1="150" y1="164" x2="150" y2="164"/>'
    b += txt(140, 172, "Substàncies pures", 10.5, fill=ACC, weight=700) + txt(420, 172, "Mescles", 10.5, fill=ACC, weight=700)
    b += f'<path d="M15 160 L265 160" stroke="{ACC}" stroke-width="2"/><path d="M295 160 L555 160" stroke="{ACC}" stroke-width="2"/>'
    return svg(570, 180, b, "160mm")

# ---------- 6. Tècniques de separació ----------
def separacio():
    b = arrow_defs("as")
    # filtració
    x = 30
    b += f'<path d="M{x} 30 L{x+90} 30 L{x+52} 90 L{x+52} 120 L{x+38} 120 L{x+38} 90 Z" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<path d="M{x+8} 34 L{x+82} 34 L{x+45} 86 Z" fill="#f3efe6" stroke="{MUT}" stroke-width="1"/>'
    b += f'<path d="M{x+30} 70 Q{x+45} 60 {x+60} 70 L{x+45} 86 Z" fill="#c9a26b"/>'
    b += f'<rect x="{x+10}" y="140" width="70" height="70" rx="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/><rect x="{x+11}" y="175" width="68" height="34" fill="{WATER}"/>'
    b += f'<line x1="{x+45}" y1="122" x2="{x+45}" y2="172" stroke="{WATER2}" stroke-width="2" stroke-dasharray="3 4"/>'
    b += txt(x + 45, 232, "Filtració", 12, weight=700) + txt(x + 45, 246, "el sòlid queda al paper", 9.5, fill=MUT)
    # decantació
    x = 200
    b += f'<path d="M{x+20} 30 Q{x} 30 {x+5} 70 Q{x+15} 120 {x+42} 140 L{x+42} 175 L{x+48} 175 L{x+48} 140 Q{x+75} 120 {x+85} 70 Q{x+90} 30 {x+70} 30 Z" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<path d="M{x+6} 72 Q{x+15} 118 {x+42} 138 L{x+48} 138 Q{x+75} 118 {x+84} 72 Z" fill="{WATER}"/>'
    b += f'<path d="M{x+3} 50 Q{x+4} 64 {x+6} 72 L{x+84} 72 Q{x+86} 64 {x+87} 50 Z" fill="{OIL}"/>'
    b += f'<rect x="{x+38}" y="150" width="14" height="6" fill="{INK}"/>'
    b += txt(x + 98, 60, "oli", 10, "start") + txt(x + 98, 100, "aigua", 10, "start")
    b += txt(x + 45, 232, "Decantació", 12, weight=700) + txt(x + 45, 246, "líquids de densitat diferent", 9.5, fill=MUT)
    # destil·lació (simplificada)
    x = 360
    b += f'<circle cx="{x+40}" cy="150" r="32" fill="#fff" stroke="{INK}" stroke-width="1.6"/><path d="M{x+12} 160 A32 32 0 0 0 {x+68} 160 Z" fill="{WATER}"/>'
    b += f'<rect x="{x+34}" y="80" width="12" height="40" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<path d="M{x+46} 92 L{x+170} 150" stroke="{INK}" stroke-width="10" stroke-linecap="round"/><path d="M{x+46} 92 L{x+170} 150" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    b += f'<path d="M{x+70} 98 L{x+150} 136" stroke="{WATER2}" stroke-width="18" opacity=".5" stroke-linecap="round"/>'
    b += f'<path d="M{x+20} 196 L{x+60} 196 L{x+40} 186 Z" fill="#e0782f"/><path d="M{x+34} 186 Q{x+40} 172 {x+46} 186" fill="#f3b23a"/>'
    b += f'<rect x="{x+150}" y="160" width="40" height="44" rx="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/><rect x="{x+151}" y="186" width="38" height="17" fill="{WATER}"/>'
    b += txt(x + 110, 86, "refrigerant", 9.5, fill=MUT)
    b += txt(x + 95, 232, "Destil·lació", 12, weight=700) + txt(x + 95, 246, "temperatures d'ebullició diferents", 9.5, fill=MUT)
    # imant
    x = 590
    b += f'<path d="M{x} 40 L{x+20} 40 L{x+20} 100 Q{x+20} 120 {x+40} 120 Q{x+60} 120 {x+60} 100 L{x+60} 40 L{x+80} 40 L{x+80} 100 Q{x+80} 140 {x+40} 140 Q{x} 140 {x} 100 Z" fill="#d9534f" stroke="{INK}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="40" width="20" height="18" fill="#c9ced4" stroke="{INK}" stroke-width="1.2"/><rect x="{x+60}" y="40" width="20" height="18" fill="#c9ced4" stroke="{INK}" stroke-width="1.2"/>'
    import random
    random.seed(3)
    for _ in range(22): b += f'<line x1="{x+random.uniform(-5,85):.0f}" y1="{random.uniform(20,36):.0f}" x2="{x+random.uniform(-5,85):.0f}" y2="{random.uniform(22,38):.0f}" stroke="#555" stroke-width="1.4"/>'
    b += f'<ellipse cx="{x+40}" cy="200" rx="50" ry="10" fill="#e8d3a5" stroke="{INK}" stroke-width="1"/>'
    b += txt(x + 40, 232, "Separació magnètica", 12, weight=700) + txt(x + 40, 246, "l'imant atrau el ferro", 9.5, fill=MUT)
    return svg(700, 255, b, "170mm")

# ---------- 7. Dissociació iònica i conductivitat ----------
def dissociacio():
    b = arrow_defs("ai")
    # cristall
    for i in range(4):
        for j in range(4):
            na = (i + j) % 2 == 0
            b += f'<circle cx="{40+i*24}" cy="{60+j*24}" r="{8 if na else 11}" fill="{"#b9a3e3" if na else "#7cc47a"}" stroke="{INK}" stroke-width="1"/>'
    b += txt(76, 170, "Cristall de NaCl", 11, weight=700) + txt(76, 184, "(no condueix)", 10, fill=MUT)
    b += f'<line x1="140" y1="96" x2="200" y2="96" stroke="{INK}" stroke-width="1.6" marker-end="url(#ai)"/>' + txt(170, 88, "aigua", 10, fill=MUT)
    # dissolució
    b += f'<rect x="215" y="30" width="230" height="150" rx="10" fill="{WATER}" stroke="{INK}" stroke-width="1.6"/>'
    import random
    random.seed(9)
    for k in range(9):
        x = 235 + random.uniform(0, 190); y = 50 + random.uniform(0, 110)
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="#b9a3e3" stroke="{INK}" stroke-width="1"/>' + txt(x, y + 4, "+", 11, weight=700)
        x2 = 235 + random.uniform(0, 190); y2 = 50 + random.uniform(0, 110)
        b += f'<circle cx="{x2:.0f}" cy="{y2:.0f}" r="11" fill="#7cc47a" stroke="{INK}" stroke-width="1"/>' + txt(x2, y2 + 4, "−", 12, weight=700)
    b += txt(330, 200, "Dissolució: ions Na⁺ i Cl⁻ que es mouen (condueix)", 11, weight=700)
    b += f'<circle cx="480" cy="70" r="8" fill="#b9a3e3" stroke="{INK}" stroke-width="1"/>' + txt(495, 74, "Na⁺", 11, "start") + f'<circle cx="480" cy="100" r="11" fill="#7cc47a" stroke="{INK}" stroke-width="1"/>' + txt(497, 104, "Cl⁻", 11, "start")
    return svg(540, 210, b, "140mm")

# ---------- 8. Canvi químic: clau de ferro en sulfat de coure ----------
def clau_coure():
    b = arrow_defs("ac")
    def vas(x, blue, coat):
        s = f'<path d="M{x} 40 L{x} 175 Q{x} 185 {x+10} 185 L{x+90} 185 Q{x+100} 185 {x+100} 175 L{x+100} 40" fill="none" stroke="{INK}" stroke-width="1.8"/>'
        s += f'<rect x="{x+1}" y="80" width="98" height="104" fill="{blue}" opacity=".85"/>'
        s += f'<rect x="{x+44}" y="30" width="12" height="140" rx="2" fill="#8c9096" stroke="{INK}" stroke-width="1.2"/><rect x="{x+38}" y="26" width="24" height="8" rx="2" fill="#8c9096" stroke="{INK}" stroke-width="1.2"/>'
        if coat: s += f'<rect x="{x+43}" y="82" width="14" height="88" rx="2" fill="#b5653a" opacity=".9"/>'
        return s
    b += vas(40, "#4d8fd6", False) + vas(260, "#a8c7e8", True)
    b += f'<line x1="160" y1="110" x2="240" y2="110" stroke="{INK}" stroke-width="1.6" marker-end="url(#ac)"/>' + txt(200, 100, "uns minuts", 10, fill=MUT)
    b += txt(90, 205, "Sulfat de coure (blau)", 10.5, weight=700) + txt(310, 205, "El clau es recobreix de coure", 10.5, weight=700) + txt(310, 219, "i la dissolució perd color", 10, fill=MUT)
    b += f'<rect x="390" y="70" width="130" height="60" rx="10" fill="{TINT}" stroke="{ACC}" stroke-width="1.5"/>' + txt(455, 95, "Fe + CuSO₄ →", 11.5, weight=700) + txt(455, 114, "FeSO₄ + Cu", 11.5, weight=700)
    return svg(530, 228, b, "135mm")
