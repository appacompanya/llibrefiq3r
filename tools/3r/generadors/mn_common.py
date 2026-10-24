"""Eines comunes per als materials multinivell: ampliació, materials adaptats i recuperació."""
import gen_sda1 as G
from gen_sda1 import q, lines

SD = {
    1: {"n": 1, "title": "Detectius de la matèria", "color": "#2F8F95", "tint": "#E3F1F2"},
    2: {"n": 2, "title": "El desodorant kamikaze", "color": "#E0782F", "tint": "#FCE9DA"},
    3: {"n": 3, "title": "Què hi ha dins del meu mòbil?", "color": "#6C5CC9", "tint": "#ECE9FA"},
    4: {"n": 4, "title": "Un cotxe que només allibera aigua?", "color": "#3F9A5A", "tint": "#E2F2E6"},
    5: {"n": 5, "title": "Cèl·lules a la caça dels patògens", "color": "#D14B66", "tint": "#FBE3E8"},
    6: {"n": 6, "title": "L'energia del nostre institut", "color": "#2F6DB5", "tint": "#E1EBF7"},
}

def use(n):
    G.SDA.update(SD[n])

BADGE_CSS = ".badge{display:inline-block;font-size:9pt;font-weight:700;letter-spacing:.04em;text-transform:uppercase;border:1.2pt solid var(--acc);color:var(--acc);border-radius:1.6mm;padding:.4mm 2mm;margin-left:2mm;vertical-align:middle}.lvl{display:inline-block;font-size:8.5pt;font-weight:700;color:#fff;background:var(--acc);border-radius:1.2mm;padding:.2mm 1.6mm;margin-right:1.5mm}.teacher{border:1.2pt dashed var(--acc);border-radius:2.5mm;padding:3mm 4mm;margin-top:5mm;font-size:9.8pt;break-inside:avoid}.teacher h3{margin-top:0;color:var(--acc)}.sol h3{color:var(--acc)}.sol p,.sol li{font-size:10pt}"

def head(title, badge, student=True, intro=None):
    who = '<div class="who"><span>Nom <i></i></span><span>Grup <i></i></span><span>Data <i></i></span></div>' if student else '<div class="who"><span style="justify-content:flex-end;font-weight:700;color:var(--acc)">Material del professor</span></div>'
    h = f'<div class="head"><div><div class="kick">Física i química · 3r ESO · SdA {G.SDA["n"]} · {G.SDA["title"]}</div><h1>{title}<span class="badge">{badge}</span></h1></div>{who}</div>'
    if intro:
        h += f'<p class="intro">{intro}</p>'
    return h

def page(body, extra=""):
    return G.page(body, BADGE_CSS + extra)

def lv(t):
    return f'<span class="lvl">{t}</span>'

def grid_svg(w_mm, h_mm, nx, ny, xlab, ylab, xt=None, yt=None, pts=None):
    """Quadrícula per dibuixar gràfiques; pts = llista de (x_frac, y_frac) per marcar punts (solucionaris)."""
    W, H = 600, int(600 * h_mm / w_mm)
    L, B = 60, 40
    gw, gh = W - L - 15, H - B - 15
    s = f'<svg viewBox="0 0 {W} {H}" width="{w_mm}mm" height="{h_mm}mm" style="display:block;margin:1mm auto">'
    for i in range(nx + 1):
        x = L + gw * i / nx
        s += f'<line x1="{x:.1f}" y1="15" x2="{x:.1f}" y2="{15+gh}" stroke="#c9ccd1" stroke-width="{1.2 if i % 5 == 0 else .5}"/>'
    for j in range(ny + 1):
        y = 15 + gh * j / ny
        s += f'<line x1="{L}" y1="{y:.1f}" x2="{L+gw}" y2="{y:.1f}" stroke="#c9ccd1" stroke-width="{1.2 if j % 5 == 0 else .5}"/>'
    s += f'<line x1="{L}" y1="{15+gh}" x2="{L+gw+8}" y2="{15+gh}" stroke="#1f2328" stroke-width="2"/><line x1="{L}" y1="{15+gh}" x2="{L}" y2="8" stroke="#1f2328" stroke-width="2"/>'
    s += f'<text x="{L+gw}" y="{H-6}" text-anchor="end" font-size="15" fill="#1f2328">{xlab}</text>'
    s += f'<text x="14" y="{15+gh/2}" font-size="15" fill="#1f2328" transform="rotate(-90 14 {15+gh/2})" text-anchor="middle">{ylab}</text>'
    if xt:
        for i, t in enumerate(xt):
            if t != "":
                s += f'<text x="{L + gw * i / (len(xt)-1):.1f}" y="{15+gh+18}" text-anchor="middle" font-size="12" fill="#5d646d">{t}</text>'
    if yt:
        for j, t in enumerate(yt):
            if t != "":
                s += f'<text x="{L-6}" y="{15 + gh - gh * j / (len(yt)-1) + 4:.1f}" text-anchor="end" font-size="12" fill="#5d646d">{t}</text>'
    if pts:
        for series in pts:
            col, P, join = series
            xy = [(L + gw * a, 15 + gh - gh * b) for a, b in P]
            if join:
                s += '<polyline fill="none" stroke="%s" stroke-width="2.5" points="%s"/>' % (col, " ".join(f"{x:.1f},{y:.1f}" for x, y in xy))
            for x, y in xy:
                s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{col}"/>'
    return s + "</svg>"

def table(head_row, rows, widths=None, cls=""):
    t = f"<table class='{cls}'><tr>"
    for i, h in enumerate(head_row):
        st = ' style="width:%s"' % widths[i] if widths else ""
        t += f"<th{st}>{h}</th>"
    t += "</tr>"
    for r in rows:
        t += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return t + "</table>"

def teacher_note(items, title="Nota per al professorat · no s'imprimeix per a l'alumne", newpage=True):
    pb = '<div class="pb"></div>' if newpage else ""
    return pb + f'<div class="teacher"><h3>{title}</h3><ul>' + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>"

AMPL_INTRO = ("Aquests reptes amplien el que treballem a classe. Tria'n els que vulguis: no cal fer-los tots ni en ordre. "
              "Les etiquetes indiquen el tipus de repte. Escriu sempre les dades, el raonament i el resultat amb unitats. "
              "Quan acabis un repte, demana el solucionari al professor i corregeix-lo amb bolígraf verd.")
