"""Construeix la versió web i el HTML d'impressió d'Iniciació a la física."""
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from teoria import TEMES
from banc import tots
from esquemes import dibuixa

ARREL = Path(__file__).resolve().parents[2] / "iniciaciofisica"
AUTOR = "Macià Esteve Pallarès Pallarès"


def esc(s):
    return html.escape(s, quote=True)


def figura_de(esq, etiqueta):
    nom, kw, peu = esq
    svg = dibuixa(nom, **kw)
    return f'<figure>{svg}<figcaption><b>{etiqueta}</b> {peu}</figcaption></figure>'


def numera(texte, prefix):
    i = 0

    def sub(_m):
        nonlocal i
        i += 1
        return f"Figura {prefix}.{i}."

    import re
    return re.sub(r"FIGURA", sub, texte), i


def problemes_de(tema):
    return [p for p in tots() if p["tema"] == tema]


def html_problemes(tema):
    trossos = []
    for p in problemes_de(tema):
        fig = figura_de(p["esq"], f"Figura {p['id']}.")
        sol_fig = ""
        if p.get("esq_sol"):
            sol_fig = figura_de(p["esq_sol"], "Diagrama de la solució.")
        trossos.append(
            f'<div class="qa" id="p-{p["id"].replace(".", "-")}">'
            f'<article class="prob"><h4><span class="pno">{p["id"]}</span> {esc(p["titol"])}'
            f'<span class="niv">{esc(p["nivell"])}</span></h4>'
            f'{fig}{p["enunciat"]}</article>'
            f'<div class="box ex sol"><p class="lead">Solució</p>{sol_fig}{p["solucio"]}</div>'
            f'</div>'
        )
    return "\n".join(trossos)


def capitol_html(tema, amb_portada=True):
    seccions = []
    for s in tema["seccions"]:
        cos, _n = numera(s["html"], s["num"])
        seccions.append(f'<section id="{tema["slug"]}-{s["id"]}"><h3><span class="secno">{s["num"]}</span> {esc(s["titol"])}</h3>{cos}</section>')
    probs = html_problemes(tema["slug"])
    nprob = len(problemes_de(tema["slug"]))
    portada = ""
    if amb_portada:
        portada = f'''<header class="cover"><div class="cover-band"><div class="cover-num"><small>Tema</small>{tema["n"]}</div><div><div class="cover-kick">{esc(tema["grup"])}</div><h1>{esc(tema["titol"])}</h1></div></div>
<div class="cover-body"><p>{esc(tema["resum"])}</p></div></header>'''
    return portada + "\n".join(seccions) + f'<h3 id="{tema["slug"]}-problemes"><span class="secno">P</span> Problemes</h3><p>Els problemes van de més senzills a més complets. Cada solució explica el plantejament, les equacions, el càlcul i el resultat amb unitats. Si no es diu una altra cosa, g = 9,8 m/s².</p>' + probs


def mixtos_html():
    return f'''<header class="cover"><div class="cover-band"><div class="cover-num"><small>Recull</small>7</div><div><div class="cover-kick">Problemes</div><h1>Problemes que barregen temes</h1></div></div>
<div class="cover-body"><p>Forces i energia en pistes llises, tir i energia, pèndol, lòpping i molles. En cap d’aquests enunciats hi ha fregament: quan es fa servir l’energia, es conserva.</p></div></header>
<h3 id="mixtos-problemes"><span class="secno">P</span> Problemes</h3>
''' + html_problemes("mixtos")


NAV_EXTRA = [
    ("cinematica", "1", "Cinemàtica", "b-cin", "Moviment"),
    ("tir", "2", "Tir parabòlic", "b-tir", "Moviment"),
    ("mcu", "3", "Moviment circular uniforme", "b-mcu", "Moviment"),
    ("newton", "4", "Lleis de Newton", "b-new", "Dinàmica"),
    ("forces", "5", "Forces i balanços", "b-for", "Dinàmica"),
    ("energia", "6", "Energia", "b-ene", "Energia"),
    ("mixtos", "7", "Problemes que barregen temes", "b-mix", "Recull"),
]


def sidebar(actual):
    grup = None
    items = []
    for slug, n, titol, classe, g in NAV_EXTRA:
        if g != grup:
            items.append(f'<li class="grp" aria-hidden="true">{esc(g)}</li>')
            grup = g
        cur = " cur" if slug == actual else ""
        secs = ""
        tema = next((t for t in TEMES if t["slug"] == slug), None)
        if tema:
            secs = "<ol>" + "".join(
                f'<li><a href="{slug}.html#{slug}-{s["id"]}" data-short="{esc(s["num"])}">{esc(s["num"])} {esc(s["titol"])}</a></li>'
                for s in tema["seccions"]
            ) + f'<li><a href="{slug}.html#{slug}-problemes" data-short="Problemes">Problemes</a></li></ol>'
        elif slug == "mixtos":
            secs = '<ol><li><a href="mixtos.html#mixtos-problemes" data-short="Problemes">Problemes</a></li></ol>'
        items.append(
            f'<li class="{classe}{cur}"><details{" open" if slug == actual else ""}><summary><a class="tl" href="{slug}.html"><span class="n">{n}</span><span>{esc(titol)}</span></a></summary>{secs}</details></li>'
        )
    items.append('<li><a class="plain" href="credits.html"><span class="n">©</span>Crèdits</a></li>')
    return f'''<aside class="side" id="side" aria-label="Índex del llibre"><div class="side-in">
<a class="side-book" href="./"><span class="logo">F1</span><span><b>Iniciació a la física</b><small>1r de batxillerat</small></span></a>
<nav aria-label="Temes"><ol class="toc">{"".join(items)}</ol></nav></div></aside>'''


CAP = '''<!DOCTYPE html>
<html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titol}</title><meta name="description" content="Iniciació a la física, 1r de batxillerat.">
<meta name="theme-color" content="#f6f5f2">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect x='4' y='4' width='56' height='56' rx='8' fill='white' stroke='%231f2328' stroke-width='5'/%3E%3Ctext x='32' y='43' font-family='Arial' font-weight='700' font-size='22' text-anchor='middle' fill='%231f2328'%3EF1%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="assets/book.css"></head>
<body class="{classe} doc-teoria" id="top"><a class="skip" href="#contingut">Salta al contingut</a>
<div class="layout">{side}<div class="scrim" aria-hidden="true"></div><div class="main">
<header class="top"><button class="menu" type="button" aria-controls="side" aria-expanded="false"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Índex</button>
<nav class="crumbs" aria-label="Ruta"><a href="./">Iniciació a la física</a><span class="sep">/</span><span class="last">{crumb}</span></nav>
<div class="progress" aria-hidden="true"></div></header>
<main class="page" id="contingut">{cos}</main></div></div>
<a class="totop" href="#top" aria-label="Torna a dalt">↑</a>
<script src="assets/book.js" defer></script></body></html>'''


def escriu(nom, titol, classe, crumb, cos, actual):
    text = CAP.format(titol=esc(titol), classe=classe, side=sidebar(actual), crumb=esc(crumb), cos=cos)
    (ARREL / nom).write_text(text, encoding="utf-8")


def index():
    cartes = []
    for t in TEMES:
        lis = "".join(f'<li><a href="{t["slug"]}.html#{t["slug"]}-{s["id"]}"><span>{s["num"]}</span>{esc(s["titol"])}</a></li>' for s in t["seccions"])
        lis += f'<li><a href="{t["slug"]}.html#{t["slug"]}-problemes"><span>P</span>Problemes</a></li>'
        cartes.append(f'<article class="card {t["classe"]}"><a class="card-h" href="{t["slug"]}.html"><span class="big">{t["n"]}</span><span><small>{esc(t["grup"])}</small><b>{esc(t["titol"])}</b></span></a><ol>{lis}</ol></article>')
    cartes.append('<article class="card b-mix"><a class="card-h" href="mixtos.html"><span class="big">7</span><span><small>Recull</small><b>Problemes que barregen temes</b></span></a><ol><li><a href="mixtos.html#mixtos-problemes"><span>P</span>Forces, tir, pèndol, lòpping i molles, sense fregament</a></li></ol></article>')
    cos = f'''<header class="hero"><div class="eyebrow">1r de batxillerat</div><h1>Iniciació a la física</h1>
<p>Teoria i problemes de cinemàtica, forces i energia. Cada tema porta el raonament sencer, els esquemes de les situacions i els problemes resolts pas a pas.</p>
<p class="credit">Llibre digital creat per <b>{AUTOR}</b></p>
<nav class="altres" aria-label="Altres llibres"><a href="../">3r d’ESO</a><a href="../2n/">2n d’ESO</a><a href="../4t/">4t d’ESO</a><a href="../btx/">Física II</a><a href="../biologia/">Biologia</a></nav>
<p class="dprint">Descarrega el PDF: <a href="iniciacio-fisica.pdf" download>iniciacio-fisica.pdf</a></p></header>
<h2 class="sec-h">Els temes</h2>
<div class="cards">{"".join(cartes)}</div>
<div class="intro-sec"><section id="convenir"><h2>Com s’ha escrit aquest llibre</h2>
<p>La coma és el signe decimal. Les unitats són les del Sistema Internacional. Si un enunciat no diu una altra cosa, g val 9,8 m/s². En els moviments verticals l’eix apunta cap amunt, de manera que l’acceleració de la gravetat és negativa, excepte quan un enunciat avisa que pren el sentit positiu cap avall.</p>
<p>Al tema d’energia tots els balanços són de conservació de l’energia mecànica: només hi treballen el pes i, si n’hi ha, les molles. El fregament es tracta al tema de forces, als diagrames de cos lliure i als balanços de forces, i no es fa servir per restar energia.</p>
<p>Els esquemes mostren la situació de l’enunciat. Quan la solució ho necessita, el diagrama de cos lliure va amb la resolució.</p>
</section></div>'''
    text = CAP.format(titol="Iniciació a la física", classe="b-cin", side=sidebar(""), crumb="Portada", cos=cos)
    text = text.replace('class="page"', 'class="page wide"', 1)
    (ARREL / "index.html").write_text(text, encoding="utf-8")


def credits():
    cos = f'''<header class="hero"><div class="eyebrow">Crèdits</div><h1>Crèdits</h1>
<p>Iniciació a la física. Llibre de teoria i problemes de 1r de batxillerat.</p>
<p>Autor: <b>{AUTOR}</b>. Publicat a llibrefiq3r.cat/iniciaciofisica.</p></header>
<div class="intro-sec"><section>
<p>Els esquemes i les gràfiques d’aquest llibre són originals.</p>
<p>Tipografies, amb llicència SIL Open Font License 1.1: Source Serif (Adobe), Atkinson Hyperlegible (Braille Institute of America) i Bricolage Grotesque.</p>
<p>En tot el llibre, si no es diu una altra cosa, l’acceleració de la gravetat és 9,8 m/s².</p>
</section></div>'''
    escriu("credits.html", "Crèdits – Iniciació a la física", "b-cin", "Crèdits", cos, "")


def llibre_impremta():
    parts = [f'''<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Iniciació a la física</title>
<link rel="stylesheet" href="assets/book.css"></head><body class="print-book b-cin">
<article><header class="hero"><div class="eyebrow">1r de batxillerat</div><h1>Iniciació a la física</h1>
<p>Teoria i problemes.</p><p class="credit">{AUTOR} · llibrefiq3r.cat/iniciaciofisica</p>
<p>Coma decimal. Unitats del Sistema Internacional. Si no es diu una altra cosa, g = 9,8 m/s². A l’energia només es conserva l’energia mecànica: no hi ha fregament en aquests balanços.</p></header></article>''']
    for t in TEMES:
        parts.append(f'<article class="chapter {t["classe"]}">{capitol_html(t)}</article>')
    parts.append(f'<article class="chapter b-mix">{mixtos_html()}</article>')
    parts.append(f'''<article class="chapter"><h2>Crèdits</h2><p>Autor: {AUTOR}.</p>
<p>Esquemes originals del llibre. Tipografies amb llicència SIL Open Font License 1.1: Source Serif, Atkinson Hyperlegible i Bricolage Grotesque.</p></article></body></html>''')
    (ARREL / "llibre.html").write_text("\n".join(parts), encoding="utf-8")


def main():
    index()
    credits()
    for t in TEMES:
        escriu(f'{t["slug"]}.html', f'{t["titol"]} – Iniciació a la física', t["classe"], t["titol"], capitol_html(t), t["slug"])
    escriu("mixtos.html", "Problemes que barregen temes – Iniciació a la física", "b-mix", "Problemes mixtos", mixtos_html(), "mixtos")
    llibre_impremta()
    from collections import Counter
    c = Counter(p["tema"] for p in tots())
    sense = [p["id"] for p in tots() if not p.get("esq")]
    print("pàgines escrites. Problemes", dict(c), "sense esquema", sense)


if __name__ == "__main__":
    main()
