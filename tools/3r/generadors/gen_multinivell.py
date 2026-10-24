"""Genera els materials multinivell: ampliació, solucionaris, materials adaptats i recuperació."""
import os, sys
import gen_sda1 as G
from playwright.sync_api import sync_playwright
import mn_ampl as A, mn_adapt as D, mn_recup as R

OUT = G.OUT
DOCS = [
    (1, "sda1-18-ampliacio.pdf", A.ampl1), (1, "sda1-19-solucionari-ampliacio.pdf", A.sol1), (1, "sda1-20-adaptada-dislexia-fitxa-1.pdf", D.adapt1),
    (2, "sda2-15-ampliacio.pdf", A.ampl2), (2, "sda2-16-solucionari-ampliacio.pdf", A.sol2), (2, "sda2-17-adaptada-nouvingut-glossari-visual.pdf", D.adapt2), (2, "sda2-18-adaptada-continguts-basics-fitxa-1.pdf", D.adapt_basic), (2, "sda2-19-avaluem-els-videos.pdf", D.coaval),
    (3, "sda3-18-ampliacio.pdf", A.ampl3), (3, "sda3-19-solucionari-ampliacio.pdf", A.sol3), (3, "sda3-20-adaptada-pi-atom-i-taula-periodica.pdf", D.adapt3),
    (4, "sda4-16-ampliacio.pdf", A.ampl4), (4, "sda4-17-solucionari-ampliacio.pdf", A.sol4), (4, "sda4-18-adaptada-discalculia-equacions-i-masses.pdf", D.adapt4),
    (5, "sda5-20-ampliacio.pdf", A.ampl5), (5, "sda5-21-solucionari-ampliacio.pdf", A.sol5), (5, "sda5-22-adaptada-tdah-problemes-de-moviment.pdf", D.adapt5),
    (6, "sda6-14-ampliacio.pdf", A.ampl6), (6, "sda6-15-solucionari-ampliacio.pdf", A.sol6), (6, "sda6-16-adaptada-tea-guio-del-debat.pdf", D.adapt6),
    (0, "curs-06-recuperacio-ce1.pdf", R.recup_ce1), (0, "curs-07-recuperacio-ce2.pdf", R.recup_ce2), (0, "curs-08-recuperacio-ce3.pdf", R.recup_ce3),
    (0, "curs-09-recuperacio-ce4.pdf", R.recup_ce4), (0, "curs-10-recuperacio-ce5.pdf", R.recup_ce5), (0, "curs-11-recuperacio-ce6.pdf", R.recup_ce6),
]

if __name__ == "__main__":
    only = sys.argv[1:]
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for n, fn, f in DOCS:
            if only and not any(o in fn for o in only):
                continue
            html, _ = f()
            path = os.path.join(OUT, fn.replace(".pdf", ".html"))
            open(path, "w", encoding="utf-8").write(html)
            pg.goto("file://" + path)
            pg.wait_for_function('document.body.dataset.math==="ok"', timeout=8000); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pg.pdf(path=os.path.join(OUT, fn), format="A4", print_background=True, prefer_css_page_size=True,
                   display_header_footer=True, header_template="<div></div>", footer_template=(G.FOOT.format(n=n, t=G.SDA["title"]) if n else G.FOOT.replace("SdA {n} · {t}", "Tasques de recuperació")))
            os.remove(path)
            print("ok", fn)
        br.close()
