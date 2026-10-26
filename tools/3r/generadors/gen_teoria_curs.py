"""Dossiers de teoria de 2n i 4t d'ESO (mateix disseny que els de 3r).
   Ús: CURS=2n OUT=dir python3 -B gen_teoria_curs.py [1 2 …]"""
import os, sys, importlib
import gen_sda1 as G
import gen_teoria as GT
from playwright.sync_api import sync_playwright

def mix(h, f=0.87):
    r, g, b = (int(h[i:i+2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % tuple(round(c + (255 - c) * f) for c in (r, g, b))

CURSOS = {
 "2n": {1: ("L'institut en xifres", "#12857A"), 2: ("Un arc de Sant Martí dins d'un got", "#B83A7A"), 3: ("La pilota que no bota", "#D9731A"),
        4: ("Aigua neta del riu", "#2F6FB5"), 5: ("La química de la coca de Sant Joan", "#B7791F"), 6: ("La carmanyola calenta", "#C63D3D")},
 "4t": {1: ("Els colors de la Mercè", "#7A4CC2"), 2: ("Aixeta o ampolla?", "#1F8FB8"), 3: ("Quant CO₂ costa venir a l'institut?", "#4E8A2E"),
        4: ("El patrimoni que es desfà", "#B8742A"), 5: ("Com es tanca una ferida?", "#D14B66"), 6: ("L'Ictineo de Monturiol", "#1D5C8C")},
}

def build(curs, ns, out_dir):
    GT.CURS = f"{curs} ESO"
    GT.COL = {n: (t, c, mix(c)) for n, (t, c) in CURSOS[curs].items()}
    mod = importlib.import_module("teoria_" + curs)
    foot = G.FOOT.replace("3r ESO", f"{curs} ESO")
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for n in ns:
            t, c, tint = GT.COL[n]
            G.SDA.update({"n": n, "title": t, "color": c, "tint": tint})
            body = GT.FR(mod.FUNCS[n]())
            html = G.page(body, GT.EXTRA)
            path = os.path.join(out_dir, f"sda{n}-teoria.html"); open(path, "w", encoding="utf-8").write(html)
            pg.goto("file://" + path)
            pg.wait_for_function('document.body.dataset.math==="ok"', timeout=15000); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pdf = os.path.join(out_dir, f"sda{n}-00-dossier-de-teoria.pdf")
            pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True, display_header_footer=True,
                   header_template="<div></div>", footer_template=foot.format(n=n, t=t))
            os.remove(path); print("ok", pdf)
        br.close()

if __name__ == "__main__":
    curs = os.environ.get("CURS", "2n")
    build(curs, [int(x) for x in sys.argv[1:]] or [1, 2, 3, 4, 5, 6], os.environ["OUT"])
