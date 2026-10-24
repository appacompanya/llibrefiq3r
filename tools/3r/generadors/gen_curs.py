"""Genera els fulls de curs: sondeig de la sessió 0, full de tancament i enquesta de valoració."""
import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..", "lib"))
import imatges as IM
import os, sys
import gen_sda1 as G
from gen_sda1 import q, lines, page
from playwright.sync_api import sync_playwright

G.SDA.update({"n": 0, "title": "Curs 2026-2027", "color": "#334155", "tint": "#E8ECF1"})
OUT = G.OUT

def head(title, intro=None, anonim=False):
    who = '<div class="who"><span style="justify-content:flex-end;font-weight:700;color:var(--acc)">Enquesta anònima</span></div>' if anonim else '<div class="who"><span>Nom <i></i></span><span>Grup <i></i></span><span>Data <i></i></span></div>'
    h = f'<div class="head"><div><div class="kick">Física i química · 3r ESO · Curs 2026-2027</div><h1>{title}</h1></div>{who}</div>'
    if intro:
        h += f'<p class="intro">{intro}</p>'
    return h

SEG = "<div class='small' style='margin:1mm 0 2mm 8mm'>Com n'estàs de segur? &nbsp; ☐ Molt segur/a &nbsp; ☐ Una mica &nbsp; ☐ No ho sé</div>"

PREG = [
    ("Dos líquids transparents", "Tens dos gots amb un líquid transparent: un és aigua i l'altre és alcohol. Com podries saber quin és quin sense tastar-los ni olorar-los?"),
    ("El globus al congelador", "Poses un globus inflat al congelador durant una hora. Què li passa? Per què? Dibuixa com t'imagines l'aire de dins del globus abans i després."),
    ("Com és un àtom?", "De què està fet un àtom? Dibuixa com te l'imagines i posa nom a les parts que coneguis."),
    ("Cremem paper", "Cremem un full de paper dins d'un pot de vidre ben tancat. La massa total del pot després de cremar el paper és més gran, més petita o igual que abans? Per què?"),
    ("La pilota", "Llances una pilota cap amunt. Mentre puja, quines forces actuen sobre la pilota? Dibuixa-les amb fletxes al costat de la pilota."),
    ("La bombeta", "Quan una bombeta fa llum, l'energia es gasta? On va a parar?"),
]

LIKERT = ["M'agrada fer experiments i descobrir per què passen les coses.", "Em sento capaç d'entendre la física i la química.", "La ciència em serveix per entendre el que passa al meu voltant.", "M'imagino treballant en alguna cosa relacionada amb la ciència."]

def likert_table(items, title="1 = gens d'acord · 4 = molt d'acord"):
    t = f"<table style='font-size:9.5pt'><tr><th style='width:70%'>{title}</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>"
    t += "".join(f"<tr><td>{x}</td><td style='text-align:center'>☐</td><td style='text-align:center'>☐</td><td style='text-align:center'>☐</td><td style='text-align:center'>☐</td></tr>" for x in items)
    return t + "</table>"

def sessio0():
    b = head("Sessió 0 · Què en sé de física i química?", intro="Respon el que pensis ara: no s'avalua: serveix per saber d'on partim. Hi ha una pregunta per a cada repte que farem durant el curs. Guarda aquest full al portafoli: el recuperaràs a l'última sessió del curs.")
    b += "<h2><span class='k'>A</span> Les meves idees</h2>"
    for i, (t, p) in enumerate(PREG, 1):
        b += q(i, f"<b>{t}{'' if t[-1] in '?!' else '.'}</b> {p}" + lines(3 if i in (2, 3, 5) else 2)) + SEG
    b += "<h2><span class='k'>B</span> Què aprendré?</h2>"
    b += q(7, "<b>Què creus que aprendràs aquest curs a Física i química?</b>" + lines(3))
    b += q(8, "<b>Què t'agradaria aprendre?</b> Escriu una pregunta sobre el món que t'agradaria poder respondre a final de curs." + lines(3))
    b += "<h2><span class='k'>C</span> La ciència i jo</h2>"
    b += likert_table(LIKERT)
    b += q(9, "<b>Una cosa que vulguis que el professor sàpiga</b> sobre com aprens millor (per exemple, si t'ajuden els dibuixos, si prefereixes treballar sol/a o en grup, si et costa llegir enunciats llargs)." + lines(3))
    return page(b), True

def tancament():
    b = head("Sessió de tancament · Què he après?", intro="Torna a respondre les preguntes de la sessió 0 sense mirar el full de setembre. Després compara-les amb el que vas escriure aleshores.")
    b += "<h2><span class='k'>A</span> Les meves idees, ara</h2>"
    for i, (t, p) in enumerate(PREG, 1):
        b += q(i, f"<b>{t}{'' if t[-1] in '?!' else '.'}</b> {p}" + lines(2)) + SEG
    b += "<div class='pb'></div><h2><span class='k'>B</span> Compara amb la sessió 0</h2>"
    b += q(7, "<b>On has canviat més d'idea?</b> Tria una pregunta: què pensaves al setembre i què en saps ara? Quin experiment o activitat et va fer canviar d'idea?" + lines(4))
    b += q(8, "<b>El que esperava i el que he après.</b> Rellegeix què creies que aprendries i què t'agradaria aprendre. Ho has après? Has pogut respondre la teva pregunta?" + lines(3))
    b += "<h2><span class='k'>C</span> Les meves dianes</h2>"
    b += q(9, "<b>Mira les dianes de les sis SdA.</b> En quin aspecte has millorat més durant el curs? Quin et costa encara?" + lines(3))
    b += "<h2><span class='k'>D</span> La ciència i jo, ara</h2>"
    b += likert_table(LIKERT)
    b += q(10, "<b>Compara-ho amb la sessió 0.</b> Ha canviat la teva relació amb la ciència? Per què?" + lines(2))
    b += q(11, "<b>Tres coses que m'emporto</b> d'aquesta matèria (coneixements, maneres de treballar o actituds)." + lines(3))
    return page(b), True

def tancament_annex():
    b = head("Sessió de tancament · Què he après?", intro="Part A (no reproduïda): l'alumnat torna a respondre les sis preguntes del sondeig de la sessió 0 (annex 7), sense mirar el full de setembre, i hi indica el grau de seguretat.")
    b += "<h2><span class='k'>B</span> Compara amb la sessió 0</h2>"
    b += q(7, "<b>On has canviat més d'idea?</b> Tria una pregunta: què pensaves al setembre i què en saps ara? Quin experiment o activitat et va fer canviar d'idea?" + lines(3))
    b += q(8, "<b>El que esperava i el que he après.</b> Rellegeix què creies que aprendries i què t'agradaria aprendre. Ho has après? Has pogut respondre la teva pregunta?" + lines(2))
    b += "<h2><span class='k'>C</span> Les meves dianes</h2>"
    b += q(9, "<b>Mira les dianes de les sis SdA.</b> En quin aspecte has millorat més durant el curs? Quin et costa encara?" + lines(2))
    b += "<h2><span class='k'>D</span> La ciència i jo, ara</h2>"
    b += likert_table(LIKERT)
    b += q(10, "<b>Compara-ho amb la sessió 0.</b> Ha canviat la teva relació amb la ciència? Per què?" + lines(2))
    b += q(11, "<b>Tres coses que m'emporto</b> d'aquesta matèria (coneixements, maneres de treballar o actituds)." + lines(2))
    return page(b), True

ENQ = ["El ritme de les sessions ha estat adequat.", "Les explicacions del professor han estat clares.", "Les fitxes i els fulls de treball m'han ajudat a aprendre.", "Els laboratoris m'han ajudat a entendre la teoria.", "Els reptes de les SdA m'han semblat interessants.", "Sabia des del principi com m'avaluarien (rúbriques).", "Corregir amb bolígraf verd m'ha ajudat a aprendre dels errors.", "El treball en grup ha funcionat bé.", "M'he sentit respectat/da i escoltat/da a l'aula.", "He après coses útils per a la meva vida."]

def enquesta():
    b = head("Enquesta de valoració de la matèria", intro="Aquesta enquesta és anònima. Les teves respostes serveixen per millorar la matèria. Sigues sincer/a.", anonim=True)
    b += "<p><b>Trimestre:</b> &nbsp; ☐ 1r &nbsp; ☐ 2n &nbsp; ☐ 3r i final de curs</p>"
    b += likert_table(ENQ, "1 = gens d'acord · 2 = poc d'acord · 3 = bastant d'acord · 4 = molt d'acord")
    b += q(1, "<b>Què mantindries?</b> Quina activitat, laboratori o manera de treballar t'ha agradat més o t'ha ajudat més?" + lines(4))
    b += q(2, "<b>Què canviaries?</b> Què milloraries de les classes, dels materials o de l'avaluació?" + lines(4))
    return page(b), True

DOCS = [
    ("curs-01-sessio-0-sondeig-idees-previes.pdf", sessio0),
    ("curs-02-sessio-de-tancament.pdf", tancament),
    ("curs-03-enquesta-de-valoracio.pdf", enquesta),
]

FOOT = '<div style="font-family:Verdana,sans-serif;font-size:8pt;color:#6b7280;width:100%;padding:0 14mm;display:flex;justify-content:space-between"><span>Física i química · 3r ESO · Curs 2026-2027</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span></div>'

if __name__ == "__main__":
    only = sys.argv[1:]
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for fn, f in DOCS:
            if only and not any(o in fn for o in only):
                continue
            html, _ = f()
            path = os.path.join(OUT, fn.replace(".pdf", ".html"))
            open(path, "w", encoding="utf-8").write(html)
            pg.goto("file://" + path)
            pg.wait_for_function('document.body.dataset.math==="ok"', timeout=8000); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pg.pdf(path=os.path.join(OUT, fn), format="A4", print_background=True, prefer_css_page_size=True,
                   display_header_footer=True, header_template="<div></div>", footer_template=FOOT)
            os.remove(path)
            IM.registra_us(fn, html)
            print("ok", fn)
        br.close()
