"""Renderitza els fulls de mostra dels annexos en Arial i amb tota la lletra a 9 pt o més.
Ús: python3 annex_samples.py <nom>   (cada mostra en un procés propi perquè els generadors tenen estat de mòdul)"""
import os, sys, re, subprocess
from playwright.sync_api import sync_playwright

SCR = "/tmp/claude-0/-home-claude/ab93dd98-bb64-5312-88e5-d8a23c91bc1c/scratchpad"
OUT = os.path.join(SCR, "annex", "mostres"); os.makedirs(OUT, exist_ok=True)

OVR = """<style id="annexovr">
body, body *:not(.katex):not(.katex *):not(svg):not(svg *){font-family:Arial,"Liberation Sans",Helvetica,sans-serif !important}
</style>"""
MINJS = """() => {
  const MIN = 12;  // 9 pt
  let n = 0;
  for (const el of document.querySelectorAll('body *')) {
    if (el.closest('svg') || el.closest('.katex')) continue;
    const hasText = [...el.childNodes].some(c => c.nodeType === 3 && c.textContent.trim());
    if (!hasText) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs < MIN - 0.01) { el.style.setProperty('font-size', MIN + 'px', 'important'); n++; }
  }
  // text dins d'SVG (etiquetes de figures): mínim 9 pt a l'escala real del dibuix
  for (const t of document.querySelectorAll('svg text')) {
    const r = t.getBoundingClientRect(), fs = parseFloat(getComputedStyle(t).fontSize);
    const svg = t.ownerSVGElement; if (!svg) continue;
    const ctm = t.getScreenCTM(); if (!ctm) continue;
    const real = fs * ctm.a;
    if (real < MIN - 0.01 && real > 0) { t.style.setProperty('font-size', (fs * MIN / real) + 'px'); n++; }
    t.style.setProperty('font-family', 'Arial, "Liberation Sans", sans-serif');
  }
  return n;
}"""
FOOT = '<div style="font-family:Arial,\'Liberation Sans\',sans-serif;font-size:9pt;color:#6b7280;width:100%;padding:0 14mm;display:flex;justify-content:space-between"><span>Física i química · 3r ESO · {t}</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span></div>'


def get(name):
    if name == "ruta5":
        import gen_cel as M; return M.full_de_ruta()[0], "SdA 5 · Full de ruta"
    if name == "sondeig":
        import gen_curs as M; return M.sessio0()[0], "Sessió 0"
    if name == "tanc":
        import gen_curs as M; return M.tancament_annex()[0], "Sessió de tancament"
    if name == "rub2":
        import gen_sda1 as M; return M.rubriques()[0], "SdA 2 · Rúbriques"
    if name == "recup1":
        import mn_recup as M; return M.recup_ce1()[0], "Tasca de recuperació de la CE1"
    if name == "basic":
        import gen_sda1, mn_adapt as M
        from mn_common import use; use(2)
        return M.adapt_basic()[0], "SdA 2 · Fitxa 1 (continguts bàsics)"
    raise KeyError(name)


def render(name):
    html, t = get(name)
    html = html.replace("</head>", OVR + "</head>", 1)
    path = os.path.join(OUT, name + ".html"); open(path, "w", encoding="utf-8").write(html)
    pdf = os.path.join(OUT, name + ".pdf")
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        pg.goto("file://" + path)
        try:
            pg.wait_for_function('document.body.dataset.math==="ok"', timeout=8000)
        except Exception:
            pass
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        n = pg.evaluate(MINJS); pg.wait_for_timeout(100)
        pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True,
               display_header_footer=True, header_template="<div></div>", footer_template=FOOT.format(t=t))
        br.close()
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    print(name, "pàgines", pages, "elements ampliats", n)


if __name__ == "__main__":
    for nm in sys.argv[1:]:
        render(nm)
