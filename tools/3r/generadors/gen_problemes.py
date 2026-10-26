"""Dossiers de problemes (exercicis i preguntes teoricopràctiques) per SdA, amb els resultats al final.
   Ús: CURS=3r|2n|4t OUT=dir python3 -B gen_problemes.py [1 2 …]  → sdaN-00-dossier-de-problemes.pdf"""
import os, sys, importlib
import gen_sda1 as G
import gen_teoria as GT
import gen_teoria_curs as GC
from playwright.sync_api import sync_playwright

COL3 = {n: (t, c) for n, (t, c, _) in GT.COL.items()}

CSS = GT.EXTRA + """
.pr{display:grid;grid-template-columns:8mm 1fr;gap:0 1.5mm;margin:0 0 2.6mm;break-inside:avoid;font-size:10.2pt}
.pr .n{font-weight:700;color:#fff;background:var(--acc);border-radius:1.4mm;height:5.2mm;line-height:5.2mm;text-align:center;font-size:9.5pt;margin-top:.3mm}
.pr .lv{font-size:8pt;color:var(--acc);letter-spacing:.05em;margin-left:1.5mm;white-space:nowrap}
.pr p{margin:0 0 1mm}
.pr ol.sub{margin:.5mm 0 0;padding-left:5.5mm}.pr ol.sub li{margin:0 0 .6mm}
.pr table{margin:1.2mm 0 1mm;font-size:9.4pt}
.leg{font-size:9pt;color:var(--muted);margin:0 0 3mm}
.res h2{margin-top:2mm}
.res .grid{columns:2;column-gap:8mm;font-size:9.4pt}
.res .grid p{break-inside:avoid;margin:0 0 1.6mm}
.res .grid b{color:var(--acc)}
.dades{font-size:9.4pt;background:var(--soft);border-radius:2mm;padding:1.8mm 3mm;margin:0 0 3mm}
"""

def nf(x, d=2, sci=False):
    """Nombre en format català: coma decimal, espai fi als milers, sense zeros sobrers."""
    if sci:
        import math
        e = int(math.floor(math.log10(abs(x)))); m = x / 10 ** e
        sup = str(e).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
        return f"{nf(m, d)} · 10{sup}"
    s = f"{round(x, d):,.{d}f}"
    if "." in s: s = s.rstrip("0").rstrip(".")
    ip, _, dp = s.partition(".")
    ip = ip.replace(",", "\u202f") if len(ip.replace(",", "").lstrip("-")) > 4 else ip.replace(",", "")
    return ip + ("," + dp if dp else "")

LV = {1: "●○○", 2: "●●○", 3: "●●●"}

def head(n, sub):
    t = GT.COL[n][0]
    return (f'<div class="dh"><div><div class="kick">Física i química · {GT.CURS} · SdA {n} · {t}</div><h1>Dossier de problemes</h1>'
            f'<p class="intro" style="margin:1mm 0 0">{sub}</p></div><span class="tag">Pràctica</span></div>'
            '<p class="leg">Exercicis per practicar, ordenats per apartats i de més fàcil a més difícil (●○○ bàsic · ●●○ mitjà · ●●● repte). '
            'Fes-los a la llibreta: escriu les dades, la fórmula, el càlcul i el resultat amb unitats, i justifica les respostes. Els resultats són a l\'última pàgina.</p>')

def render(n, spec):
    """spec = {"sub": str, "dades": str|None, "seccions": [(titol, [(nivell, html, resultat), …]), …]}"""
    b = head(n, spec["sub"])
    if spec.get("dades"): b += f'<div class="dades">{spec["dades"]}</div>'
    k = 0; res = []
    for si, (tit, items) in enumerate(spec["seccions"], 1):
        b += GT.S(si, tit)
        for lv, html, r in items:
            k += 1
            b += f'<div class="pr"><div class="n">{k}</div><div>{html.replace("§", f"<span class=lv>{LV[lv]}</span>", 1) if "§" in html else html + ""}</div></div>'
            res.append((k, r))
    b += '<div class="pb"></div><div class="res">' + GT.S("✓", "Resultats") + '<div class="grid">' + "".join(f"<p><b>{k}.</b> {r}</p>" for k, r in res) + "</div></div>"
    return b, k

def Q(lv, title, text, *subs, table=""):
    """Un exercici: títol en negreta + nivell + enunciat + apartats a), b)…"""
    h = f"<p><b>{title}</b>§ {text}</p>" if title else f"<p>§ {text}</p>"
    h = h.replace("§", f'<span class="lv">{LV[lv]}</span>', 1)
    if table: h += table
    if subs and all(len(x) < 40 for x in subs):
        h += "<p>" + " · ".join(f"{chr(97+i)}) {x}" for i, x in enumerate(subs)) + "</p>"
    elif subs: h += '<ol class="sub" type="a">' + "".join(f"<li>{s}</li>" for s in subs) + "</ol>"
    return h

def build(curs, ns, out_dir):
    if curs == "3r":
        GT.CURS = "3r ESO"
        COL = {n: (t, c, tint) for n, (t, c, tint) in GT.COL.items()}
    else:
        GT.CURS = f"{curs} ESO"
        COL = {n: (t, c, GC.mix(c)) for n, (t, c) in GC.CURSOS[curs].items()}
    GT.COL = COL
    mod = importlib.import_module("problemes_" + curs)
    foot = G.FOOT.replace("3r ESO", f"{curs} ESO")
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for n in ns:
            t, c, tint = COL[n]
            G.SDA.update({"n": n, "title": t, "color": c, "tint": tint})
            body, k = render(n, mod.FUNCS[n]())
            body = GT.FR(body)
            html = G.page(body, CSS)
            path = os.path.join(out_dir, f"sda{n}-prob.html"); open(path, "w", encoding="utf-8").write(html)
            pg.goto("file://" + path)
            pg.wait_for_function('document.body.dataset.math==="ok"', timeout=15000); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pdf = os.path.join(out_dir, f"sda{n}-00-dossier-de-problemes.pdf")
            pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True, display_header_footer=True,
                   header_template="<div></div>", footer_template=foot.format(n=n, t=t))
            if not os.environ.get("KEEP"): os.remove(path)
            print("ok", pdf, k, "exercicis")
        br.close()

if __name__ == "__main__":
    curs = os.environ.get("CURS", "3r")
    build(curs, [int(x) for x in sys.argv[1:]] or [1, 2, 3, 4, 5, 6], os.environ["OUT"])
