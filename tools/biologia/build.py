#!/usr/bin/env python3
"""Genera el dossier /biologia (HTML, figures SVG i llibre per al PDF) a partir de tools/biologia/caps.

Ús:  python3 tools/biologia/build.py
     node tools/biologia/pdf_teoria.js
"""
from __future__ import annotations

import hashlib
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BIO = ROOT / "biologia"
CAPS = Path(__file__).resolve().parent / "caps"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import figures  # noqa: E402
from depth import deepen  # noqa: E402

ICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect x='4' y='4' width='56' height='56' rx='8' fill='%230E7C66'/%3E"
    "%3Ctext x='32' y='42' font-family='Arial' font-weight='700' font-size='22' "
    "text-anchor='middle' fill='white'%3EBio%3C/text%3E%3C/svg%3E"
)

# (id, short, títol visible a l'índex)
CHAPTERS = [
    {
        "slug": "biomolecules",
        "file": "01-biomolecules.html",
        "id": "bio",
        "n": "1",
        "cls": "b-mol",
        "group": "Biomolècules",
        "title": "Biomolècules",
        "kick": "Teoria · Biomolècules i metabolisme",
        "blurb": "Aigua, sals, glúcids, lípids, proteïnes, enzims i àcids nucleics: estructura i funció.",
        "secs": [
            ("bio-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("bio-s1", "1.1", "1.1 Aigua i sals minerals"),
            ("bio-s2", "1.2", "1.2 Glúcids"),
            ("bio-s3", "1.3", "1.3 Lípids"),
            ("bio-s4", "1.4", "1.4 Proteïnes i l’enllaç peptídic"),
            ("bio-s5", "1.5", "1.5 Enzims"),
            ("bio-s6", "1.6", "1.6 Àcids nucleics: estructura"),
            ("bio-s7", "1.7", "1.7 Mapa del tema"),
            ("bio-fm", "Resum", "Resum"),
            ("bio-err", "Errors típics", "Errors típics a la PAU"),
            ("bio-glos", "Glossari", "Glossari"),
            ("bio-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "cellula",
        "file": "02-cellula.html",
        "id": "cel",
        "n": "2",
        "cls": "b-cel",
        "group": "La cèl·lula",
        "title": "La cèl·lula",
        "kick": "Teoria · Cèl·lula i cicle cel·lular",
        "blurb": "Teoria cel·lular, membrana, transport, orgànuls, cicle, mitosi i meiosi.",
        "secs": [
            ("cel-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("cel-s1", "2.1", "2.1 Teoria cel·lular i microscòpia"),
            ("cel-s2", "2.2", "2.2 Procariotes i eucariotes"),
            ("cel-s3", "2.3", "2.3 La membrana: mosaic fluid"),
            ("cel-s4", "2.4", "2.4 Transport i osmosi"),
            ("cel-s5", "2.5", "2.5 Orgànuls"),
            ("cel-s6", "2.6", "2.6 Cicle cel·lular"),
            ("cel-s7", "2.7", "2.7 Mitosi"),
            ("cel-s8", "2.8", "2.8 Meiosi"),
            ("cel-s9", "2.9", "2.9 Mapa del tema"),
            ("cel-fm", "Resum", "Resum"),
            ("cel-err", "Errors típics", "Errors típics a la PAU"),
            ("cel-glos", "Glossari", "Glossari"),
            ("cel-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "metabolisme",
        "file": "03-metabolisme.html",
        "id": "met",
        "n": "3",
        "cls": "b-met",
        "group": "Metabolisme",
        "title": "Metabolisme",
        "kick": "Teoria · Biomolècules i metabolisme",
        "blurb": "Catabolisme (glucòlisi, Krebs, cadena, fermentacions, β-oxidació) i anabolisme (fotosíntesi, quimiosíntesi).",
        "secs": [
            ("met-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("met-s1", "3.1", "3.1 Visió general"),
            ("met-s2", "3.2", "3.2 Glucòlisi"),
            ("met-s3", "3.3", "3.3 Destí del piruvat i cicle de Krebs"),
            ("met-s4", "3.4", "3.4 Cadena respiratòria i balanç d’ATP"),
            ("met-s5", "3.5", "3.5 Fermentacions"),
            ("met-s6", "3.6", "3.6 β-oxidació"),
            ("met-s7", "3.7", "3.7 Anabolisme heteròtrof"),
            ("met-s8", "3.8", "3.8 Fotosíntesi"),
            ("met-s9", "3.9", "3.9 Quimiosíntesi i fotosíntesi bacteriana"),
            ("met-s10", "3.10", "3.10 Mapa del tema"),
            ("met-fm", "Resum", "Resum"),
            ("met-err", "Errors típics", "Errors típics a la PAU"),
            ("met-glos", "Glossari", "Glossari"),
            ("met-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "mendel",
        "file": "04-mendel.html",
        "id": "men",
        "n": "4",
        "cls": "b-men",
        "group": "Genètica",
        "title": "Genètica mendeliana",
        "kick": "Teoria · Genètica i cicle cel·lular",
        "blurb": "Lleis de Mendel, lligament, herència lligada al sexe, pedigrís i probabilitat.",
        "secs": [
            ("men-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("men-s1", "4.1", "4.1 Conceptes i lleis de Mendel"),
            ("men-s2", "4.2", "4.2 Monohibridisme"),
            ("men-s3", "4.3", "4.3 Dihibridisme i lligament"),
            ("men-s4", "4.4", "4.4 Herència lligada al sexe"),
            ("men-s5", "4.5", "4.5 Pedigrís i probabilitat"),
            ("men-s6", "4.6", "4.6 Caràcters quantitatius"),
            ("men-s7", "4.7", "4.7 Mapa del tema"),
            ("men-fm", "Resum", "Resum"),
            ("men-err", "Errors típics", "Errors típics a la PAU"),
            ("men-glos", "Glossari", "Glossari"),
            ("men-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "molecular",
        "file": "05-molecular.html",
        "id": "gen",
        "n": "5",
        "cls": "b-gen",
        "group": "Genètica",
        "title": "Genètica molecular i biotecnologia",
        "kick": "Teoria · Genètica, biotecnologia",
        "blurb": "Replicació, expressió gènica, codi, mutacions, PCR, CRISPR, OMG i clonació.",
        "secs": [
            ("gen-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("gen-s1", "5.1", "5.1 Dogma i genomes"),
            ("gen-s2", "5.2", "5.2 Replicació"),
            ("gen-s3", "5.3", "5.3 Transcripció i codi genètic"),
            ("gen-s4", "5.4", "5.4 Traducció"),
            ("gen-s5", "5.5", "5.5 Regulació i diferenciació"),
            ("gen-s6", "5.6", "5.6 Mutacions i càncer"),
            ("gen-s7", "5.7", "5.7 Enginyeria genètica"),
            ("gen-s8", "5.8", "5.8 PCR, CRISPR, OMG i clonació"),
            ("gen-s9", "5.9", "5.9 Aplicacions i teràpia gènica"),
            ("gen-s10", "5.10", "5.10 Mapa del tema"),
            ("gen-fm", "Resum", "Resum"),
            ("gen-err", "Errors típics", "Errors típics a la PAU"),
            ("gen-glos", "Glossari", "Glossari"),
            ("gen-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "evolucio",
        "file": "06-evolucio.html",
        "id": "evo",
        "n": "6",
        "cls": "b-evo",
        "group": "Evolució",
        "title": "Evolució",
        "kick": "Teoria · Evolució",
        "blurb": "Fet evolutiu, Darwin i Lamarck, Hardy-Weinberg, especiació i evo-devo al nivell de la PAU.",
        "secs": [
            ("evo-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("evo-s1", "6.1", "6.1 L’evolució és un fet"),
            ("evo-s2", "6.2", "6.2 Lamarck, Darwin i la teoria sintètica"),
            ("evo-s3", "6.3", "6.3 Hardy-Weinberg i les forces evolutives"),
            ("evo-s4", "6.4", "6.4 Variabilitat: mutació i recombinació"),
            ("evo-s5", "6.5", "6.5 Especiació"),
            ("evo-s6", "6.6", "6.6 Perspectives actuals"),
            ("evo-s7", "6.7", "6.7 Mapa del tema"),
            ("evo-fm", "Resum", "Resum"),
            ("evo-err", "Errors típics", "Errors típics a la PAU"),
            ("evo-glos", "Glossari", "Glossari"),
            ("evo-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "microbiologia",
        "file": "07-micro.html",
        "id": "mic",
        "n": "7",
        "cls": "b-mic",
        "group": "Microbiologia",
        "title": "Microbiologia",
        "kick": "Teoria · Microorganismes i formes acel·lulars",
        "blurb": "Bacteris, arqueus, virus, viroides, prions, cicles, cicles biogeoquímics i biotecnologia microbiana.",
        "secs": [
            ("mic-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("mic-s1", "7.1", "7.1 Bacteris i arqueus"),
            ("mic-s2", "7.2", "7.2 Mida, Gram, cultiu i esterilització"),
            ("mic-s3", "7.3", "7.3 Metabolisme, simbiosi i cicles"),
            ("mic-s4", "7.4", "7.4 Microbiota, malaltia i indústria"),
            ("mic-s5", "7.5", "7.5 Transferència horitzontal i antibiòtics"),
            ("mic-s6", "7.6", "7.6 Virus: estructura i cicles"),
            ("mic-s7", "7.7", "7.7 Viroides, prions i fongs"),
            ("mic-s8", "7.8", "7.8 Mapa del tema"),
            ("mic-fm", "Resum", "Resum"),
            ("mic-err", "Errors típics", "Errors típics a la PAU"),
            ("mic-glos", "Glossari", "Glossari"),
            ("mic-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "immunologia",
        "file": "08-immuno.html",
        "id": "imm",
        "n": "8",
        "cls": "b-imm",
        "group": "Immunologia",
        "title": "Immunologia",
        "kick": "Teoria · Immunologia",
        "blurb": "Immunitat innata i específica, anticossos, limfòcits, vacunes, al·lèrgies, autoimmunitat i VIH.",
        "secs": [
            ("imm-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("imm-s1", "8.1", "8.1 Immunitat i barreres"),
            ("imm-s2", "8.2", "8.2 Immunitat innata i complement"),
            ("imm-s3", "8.3", "8.3 Immunitat específica"),
            ("imm-s4", "8.4", "8.4 Anticossos i respostes"),
            ("imm-s5", "8.5", "8.5 Immunitat artificial: vacunes i sèrums"),
            ("imm-s6", "8.6", "8.6 Alteracions i VIH"),
            ("imm-s7", "8.7", "8.7 Fases de la malaltia infecciosa"),
            ("imm-s8", "8.8", "8.8 Mapa del tema"),
            ("imm-fm", "Resum", "Resum"),
            ("imm-err", "Errors típics", "Errors típics a la PAU"),
            ("imm-glos", "Glossari", "Glossari"),
            ("imm-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
    {
        "slug": "disseny",
        "file": "09-disseny.html",
        "id": "dis",
        "n": "9",
        "cls": "b-annex",
        "group": "Annex PAU",
        "title": "Disseny experimental",
        "kick": "Annex · Disseny experimental",
        "blurb": "Hipòtesi, variables, controls, rèpliques i lectura de resultats, com a la PAU.",
        "secs": [
            ("dis-s0", "Què entra a la PAU", "Què entra a la PAU"),
            ("dis-s1", "9.1", "9.1 El mètode en una pregunta de PAU"),
            ("dis-s2", "9.2", "9.2 Variables, control i rèpliques"),
            ("dis-s3", "9.3", "9.3 Gràfics, taules i errades"),
            ("dis-fm", "Resum", "Resum"),
            ("dis-err", "Errors típics", "Errors típics a la PAU"),
            ("dis-glos", "Glossari", "Glossari"),
            ("dis-auto", "Autoavaluació", "Autoavaluació"),
        ],
    },
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def toc_side(current: str | None, prefix: str) -> str:
    """prefix '' des de biologia/, '../' des de biologia/teoria/."""
    groups_done = []
    items = []
    for ch in CHAPTERS:
        if ch["group"] not in groups_done:
            groups_done.append(ch["group"])
            items.append(f'<li class="grp" aria-hidden="true">{esc(ch["group"])}</li>')
        cur = " cur" if ch["slug"] == current else ""
        open_attr = " open" if ch["slug"] == current else ""
        here = ' aria-current=page' if ch["slug"] == current else ""
        href = f'{prefix}{ch["slug"]}.html'
        subs = []
        for sid, short, title in ch["secs"]:
            sh = esc(short)
            subs.append(
                f'<li><a href="{href}#{sid}" data-short="{sh}">{esc(title)}</a></li>'
            )
        items.append(
            f'<li class="{ch["cls"]}{cur}"><details{open_attr}><summary>'
            f'<a class="tl" href="{href}"{here}><span class="n">{esc(ch["n"])}</span>'
            f'<span>{esc(ch["title"])}</span></a></summary><ol>{"".join(subs)}</ol></details></li>'
        )
    items.append(
        f'<li><a class="plain" href="{prefix}../glossari.html"><span class="n">G</span>Glossari general</a></li>'
    )
    items.append(
        f'<li><a class="plain" href="{prefix}../cobertura.html"><span class="n">✓</span>Cobertura del currículum</a></li>'
    )
    return "".join(items)


def shell(title: str, body_cls: str, main: str, current: str | None, depth: int, crumb: str) -> str:
    """depth 0 = biologia/, 1 = biologia/teoria/."""
    pre = "../" * depth
    asset = pre + "assets/"
    side_prefix = "" if depth == 1 else "teoria/"
    # side links to chapters: from index (depth 0) they are teoria/slug.html; from chapter (depth 1) slug.html
    tabs_teoria = "teoria/" if depth == 0 else "./"
    return f"""<!DOCTYPE html>
<html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="Biologia, 2n de Batxillerat (PAU Catalunya, LOMLOE). Dossier de teoria."><meta name="theme-color" content="#f6f5f2"><link rel="icon" href="{ICON}"><link rel="stylesheet" href="{asset}book.css?v=bio1"></head><body class="{body_cls} doc-teoria" id="top"><a class="skip" href="#contingut">Salta al contingut</a><div class="layout"><aside class="side" id="side" aria-label="Índex del llibre"><div class="side-in"><a class="side-book" href="{pre}"><span class="logo bio">Bio</span><span><b>Biologia</b><small>2n de Batxillerat · PAU</small></span></a><nav class="side-tabs" aria-label="Documents"><a href="{pre}{tabs_teoria}" {"aria-current=page" if current else ""}>Teoria</a><a href="{pre}teoria/disseny.html">Annex</a><a href="{pre}glossari.html">Glossari</a><a href="{pre}biologia-teoria.pdf" download>PDF</a></nav><nav aria-label="Temes"><ol class="toc">{toc_side(current, side_prefix if depth == 0 else "")}</ol></nav></div></aside><div class="scrim" aria-hidden="true"></div><div class="main"><header class="top"><button class="menu" type="button" aria-controls="side" aria-expanded="false"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Índex</button><nav class="crumbs" aria-label="Ruta">{crumb}</nav><div class="progress" aria-hidden="true"></div></header><main class="page{' wide' if current is None else ''}" id="contingut">
{main}
</main></div></div><a class="totop" href="#top" aria-label="Torna a dalt">↑</a><script src="{asset}book.js?v=bio1" defer></script><script src="{asset}zoom.js?v=bio1" defer></script></body></html>
"""


def fig_tag(fid: str, cap: str, svg: str) -> str:
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    w, h = (vb.group(1), vb.group(2)) if vb else ("700", "400")
    digest = hashlib.sha1(svg.encode()).hexdigest()[:8]
    alt = esc(re.sub(r"<[^>]+>", "", cap))
    return (
        f'<figure id="{fid}"><img src="../assets/fig/{fid}.svg?v={digest}" alt="{alt}" '
        f'data-zoom="../assets/fig/{fid}.svg?v={digest}" data-zoom-alt="{alt}" '
        f'width="{w}" height="{h}" loading="lazy" decoding="async">'
        f"<figcaption><b>Figura {fid.removeprefix('fig-')}.</b> {cap}</figcaption></figure>"
    )


def expand_figs(fragment: str, inline: bool) -> str:
    def repl(m: re.Match) -> str:
        fid, cap = m.group(1), m.group(2)
        svg = figures.FIGS[fid]
        if inline:
            return f'<figure id="{fid}">{svg}<figcaption><b>Figura {fid.removeprefix("fig-")}.</b> {cap}</figcaption></figure>'
        return fig_tag(fid, cap, svg)

    out = re.sub(r"\{\{fig:([\w.-]+)\|(.*?)\}\}", repl, fragment, flags=re.S)
    missing = re.findall(r"\{\{fig:([^|}]+)", out)
    if missing:
        raise SystemExit(f"Figures sense definir: {missing}")
    return out


def cover_toc(ch: dict) -> str:
    lis = []
    for sid, short, title in ch["secs"]:
        span = "nn" if not short[:1].isdigit() else ""
        label = short if short[:1].isdigit() else "·"
        cls = ' class="nn"' if span else ""
        # title without leading number if short is the number
        text = title
        lis.append(f'<li><a href="#{sid}"><span{cls}>{esc(label) if not span else "·"}</span>{esc(text)}</a></li>')
    return "".join(lis)


def neighbor(i: int) -> str:
    parts = ['<nav class="pn" aria-label="Temes veïns">']
    if i > 0:
        p = CHAPTERS[i - 1]
        parts.append(
            f'<a href="{p["slug"]}.html" rel="prev"><small>← Tema {esc(p["n"])}</small><b>{esc(p["title"])}</b></a>'
        )
    else:
        parts.append("<span></span>")
    if i + 1 < len(CHAPTERS):
        n = CHAPTERS[i + 1]
        parts.append(
            f'<a class="next" href="{n["slug"]}.html" rel="next"><small>Tema {esc(n["n"])} →</small><b>{esc(n["title"])}</b></a>'
        )
    parts.append("</nav><p class=\"foot\">Biologia · 2n de Batxillerat · dossier de teoria</p>")
    return "".join(parts)


def index_main() -> str:
    cards = []
    for ch in CHAPTERS:
        lis = []
        for sid, short, title in ch["secs"]:
            lab = short if short[:1].isdigit() else "·"
            cls = "" if short[:1].isdigit() else ' class="nn"'
            lis.append(
                f'<li><a href="teoria/{ch["slug"]}.html#{sid}"><span{cls}>{esc(lab)}</span>{esc(title)}</a></li>'
            )
        cards.append(
            f'<article class="card {ch["cls"]} has-pic" id="tema-{ch["slug"]}">'
            f'<button type="button" class="card-pic" data-zoom="assets/covers/{ch["slug"]}.svg" '
            f'data-zoom-alt="Tema {esc(ch["n"])}. {esc(ch["title"])}" '
            f'aria-label="Amplia la portada: Tema {esc(ch["n"])}. {esc(ch["title"])}">'
            f'<img src="assets/covers/{ch["slug"]}.svg" alt="" width="600" height="400">'
            f'<span class="zoom-ic" aria-hidden="true">⤢</span></button>'
            f'<a class="card-h" href="teoria/{ch["slug"]}.html"><span class="big">{esc(ch["n"])}</span>'
            f'<span><small>Tema {esc(ch["n"])} · {esc(ch["group"])}</small><b>{esc(ch["title"])}</b></span></a>'
            f'<ol>{"".join(lis)}</ol></article>'
        )
    return f"""<header class="hero"><div class="eyebrow">2n de Batxillerat · PAU Catalunya · LOMLOE</div><h1>Biologia</h1><p>Dossier de teoria per a 2n de Batxillerat: els sabers del Decret 171/2022 i les orientacions de la PAU de Biologia, amb figures originals, exemples resolts i autoavaluació.</p><p class="credit">Mateix format que el llibre de Física II · <a href="../btx/">Física II</a> · <a href="../">Llibre de 3r d’ESO</a></p><nav class="docs" aria-label="Documents"><div class="dpills"><a class="dpill" style="--c:#0E7C66" href="#temes"><span>1</span>Teoria</a><a class="dpill" style="--c:#5f6670" href="teoria/disseny.html"><span>2</span>Disseny experimental</a><a class="dpill" style="--c:#1F6AA5" href="glossari.html"><span>3</span>Glossari</a><a class="dpill" style="--c:#B23A52" href="cobertura.html"><span>4</span>Cobertura</a></div><p class="dprint">Descarrega el PDF: <a href="biologia-teoria.pdf" download>Biologia · dossier de teoria</a></p></nav></header><h2 id="temes" class="sec-h">Els temes</h2><p class="note sec-note">Teoria de Biologia de 2n de Batxillerat (PAU Catalunya). L’annex de disseny experimental és un bloc propi de la prova.</p><div class="cards">{''.join(cards)}</div><div class="intro-sec"><section id="abast"><h2>Sobre l’abast</h2><p>El dossier cobreix els sabers de Biologia de 2n de batxillerat del Decret 171/2022 i la concreció de les orientacions de la PAU. Les orientacions recorden que alguns sabers de 1r (aigua i sals, estructura dels glúcids i els lípids, ultraestructura cel·lular) estan imbricats amb els de 2n i fan falta per respondre preguntes de localització i d’identificació: hi són, marcats com a tals. La fisiologia d’aparells, la petjada ecològica i la resta del bloc d’ecologia de 1r no són un bloc de la PAU de 2n; dels ecosistemes només entra el que el decret de 2n demana: el paper dels microorganismes en les simbiosis i els cicles biogeoquímics.</p><ul><li><a href="https://universitats.gencat.cat/ca/pau/materies-pau/biologia/">Biologia. Canal Universitats (estructura de l’examen i sabers)</a></li><li><a href="https://universitats.gencat.cat/web/.content/01_acces_i_admissio/proves-acces-PAU-PAP/ambits/biologia/02.-Altra-info-de-materia-Orientacions_Biologia_2025_Corr_CA.pdf">Orientacions per a l’examen de Biologia (document corregit vigent al canal; convocatòries 2025 i 2026)</a></li><li><a href="https://dogc.gencat.cat/ca/document-del-dogc/?documentId=938007">Decret 171/2022 (DOG)</a></li><li><a href="cobertura.html">Taula de cobertura: cada saber, una secció</a></li>
<li><a href="galeria.html">Galeria de figures, amb el peu i la comprovació</a></li>
<li><a href="credits.html">Crèdits i llicències de les figures</a></li></ul></section></div><div class="intro-sec"><section id="intro"><h2>Com fer servir aquest dossier</h2><p>Cada tema obre amb el quadre «Què entra a la PAU», segueix amb l’explicació, les figures, les idees clau, un exemple resolt i un mini-exercici a l’estil de la prova (context, apartats curts, càlcul o esquema). Al final hi ha el resum, els errors típics, el glossari i l’autoavaluació: la resposta és dins el desplegable. Els requadres «Per ampliar» no són matèria d’examen.</p><p>Convencions: coma decimal; noms segons l’ús de les orientacions (DNA, RNA, RNAm, RNAt, RNAr) i, quan el Termcat té una forma pròpia, aquesta (glucòlisi, arqueus, citosol). El rendiment de la respiració s’explica amb el valor actual, uns 30–32 ATP per glucosa, i es recorda el balanç clàssic de 36–38.</p><p>L’examen oficial són quatre exercicis obligatoris de 2,50 punts, cadascun amb cinc apartats (entre 0,30 i 0,70). Es pot dur calculadora no programable. Les respostes definitives van en bolígraf blau o negre.</p></section></div>"""


def glossari_main(bodies: dict[str, str]) -> str:
    blocks = []
    for ch in CHAPTERS:
        dts = re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", bodies[ch["slug"]], flags=re.S)
        # only the glossary section
        glos = re.search(rf'id="{ch["id"]}-glos".*', bodies[ch["slug"]], flags=re.S)
        if not glos:
            continue
        chunk = glos.group(0).split("</section>", 1)[0]
        dts = re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", chunk, flags=re.S)
        lis = "".join(
            f'<dt><a href="teoria/{ch["slug"]}.html#{ch["id"]}-glos">{t}</a></dt><dd>{d}</dd>'
            for t, d in dts
        )
        blocks.append(
            f'<section><h3><span class="secno">{esc(ch["n"])}</span> {esc(ch["title"])}</h3><dl>{lis}</dl></section>'
        )
    return (
        '<header class="hero"><div class="eyebrow">Biologia · 2n de Batxillerat</div><h1>Glossari</h1>'
        '<p>Tots els termes dels glossaris de tema. La definició completa és al capítol.</p></header>'
        + "".join(blocks)
    )


def check_coverage(pages: str, built: set[str]) -> None:
    from coverage_data import ROWS

    missing = []
    pending = 0
    for block, saber, anchor, _note in ROWS:
        slug = anchor.split("#", 1)[0].replace(".html", "")
        if slug not in built:
            pending += 1
            continue
        frag = anchor.split("#")[-1]
        if f'id="{frag}"' not in pages:
            missing.append(f"{block}: {saber} → {anchor}")
    if missing:
        raise SystemExit("Cobertura incompleta:\n" + "\n".join(missing))
    if pending:
        print(f"Avís WIP: {pending} sabers encara sense capítol generat")


def cobertura_main() -> str:
    from coverage_data import ROWS

    rows = []
    last = None
    for block, saber, anchor, note in ROWS:
        b = esc(block) if block != last else ""
        last = block
        href = "teoria/" + anchor if not anchor.startswith("http") else anchor
        rows.append(
            f"<tr><td>{b}</td><td>{esc(saber)}</td><td><a href=\"{esc(href)}\">{esc(anchor)}</a></td><td>{esc(note)}</td></tr>"
        )
    return (
        '<header class="hero"><div class="eyebrow">Decret 171/2022 · orientacions PAU</div>'
        "<h1>Cobertura</h1><p>Cada saber de Biologia de 2n i cada concreció de les orientacions de la PAU, amb la secció on es tracta. Els sabers de 1r que les orientacions declaren imbricats hi consten a part. No hi ha cap fila sense destí.</p></header>"
        '<table><thead><tr><th>Bloc</th><th>Saber o concreció PAU</th><th>On</th><th>Nota de nivell</th></tr></thead><tbody>'
        + "".join(rows)
        + "</tbody></table>"
    )


def write_figures() -> None:
    figdir = BIO / "assets" / "fig"
    cov = BIO / "assets" / "covers"
    figdir.mkdir(parents=True, exist_ok=True)
    cov.mkdir(parents=True, exist_ok=True)
    for fid, svg in figures.FIGS.items():
        (figdir / f"{fid}.svg").write_text(svg)
    for slug, svg in figures.COVERS.items():
        (cov / f"{slug}.svg").write_text(svg)


def print_book(bodies: dict[str, str]) -> str:
    """Document únic per al PDF, amb el mateix criteri que btx/teoria.html."""
    colors = {
        "bio": "#0E7C66",
        "cel": "#1F6AA5",
        "met": "#C4651A",
        "men": "#5C4B8A",
        "gen": "#B23A52",
        "evo": "#3E7A32",
        "mic": "#A67C12",
        "imm": "#8E3A55",
        "dis": "#5f6670",
    }
    css_link_fonts = (ROOT / "biologia" / "assets" / "book.css").read_text()
    # El PDF és autosuficient: reutilitza els requadres de book.css i hi afegeix paginació.
    extra = """
body{max-width:180mm;margin:0 auto;padding:0 0 24px;background:#fff}
h1{font-family:"Bricolage Grotesque","Atkinson Hyperlegible",sans-serif;font-weight:800;font-size:2rem;margin:.2em 0}
h2{font-size:1.55em;color:var(--c);border-bottom:3px solid var(--c);padding-bottom:.15em;break-before:auto;page-break-before:auto}
h2.first{break-before:auto}
h3{font-size:1.05em;color:#fff;background:var(--c);padding:.28em .6em;border-radius:6px;break-after:avoid}
.box{break-inside:auto;page-break-inside:auto}
ol.qlist>li{break-inside:avoid;page-break-inside:avoid}
ol.qlist>li .q{break-after:avoid;page-break-after:avoid}
details.sol{break-before:avoid;page-break-before:avoid}
figure{break-inside:avoid;page-break-inside:avoid}
.qa-fig{display:block;width:min(100%,440px);height:auto;margin:.5em auto .8em;background:#fff}
figure svg,figure img{max-width:100%}
nav.toc ol{font-family:"Atkinson Hyperlegible",sans-serif}
"""
    color_css = "".join(f"#{k}{{--c:{v}}}" for k, v in colors.items())
    toc = "".join(
        f'<li><a href="#{ch["id"]}">{esc(ch["n"])}. {esc(ch["title"])}</a></li>' for ch in CHAPTERS
    )
    parts = [
        f'<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Biologia · dossier de teoria</title><style>{css_link_fonts}\n{extra}\n{color_css}</style></head><body>',
        '<header><h1>Biologia</h1><p class="src">Dossier de teoria · 2n de Batxillerat · PAU Catalunya.</p></header>',
        f'<nav class="toc"><h2 class="first">Índex</h2><ol>{toc}</ol></nav>',
    ]
    for ch in CHAPTERS:
        body = expand_figs(bodies[ch["slug"]], inline=True).replace(
            '<details class="sol">', '<details class="sol" open>'
        )
        parts.append(f'<section class="chap" id="{ch["id"]}"><h2>{esc(ch["n"])}. {esc(ch["title"])}</h2>{body}</section>')
    parts.append("</body></html>")
    return "".join(parts)


# Només les làmines de tercers amb llicència que exigeix atribució.
CC_CREDIT = {
    "fig-2.5": ("Kelvinsong, Chloroplast II. https://commons.wikimedia.org/wiki/File:Chloroplast_II.svg", "CC BY 3.0", "correspon a 2.5 i 3.8 Cloroplast: tilacoide (fase lluminosa) i estroma (Calvin)"),
    "fig-2.6": ("Jpablo cad i Juliana Osorio. https://commons.wikimedia.org/wiki/File:Mitosis_schematic_diagram-en.svg", "CC BY-SA 3.0", "correspon a 2.7 Mitosi: profase, prometafase, metafase, anafase i telofase"),
    "fig-2.7": ("Ali Zifan, Meiosis Stages. https://commons.wikimedia.org/wiki/File:Meiosis_Stages.svg", "CC BY-SA 4.0", "correspon a 2.8 Meiosi: meiosi I (se separen homòlegs) i meiosi II (se separen cromàtides)"),
    "fig-7.2": ("Adenosine, a partir de Pbroks13, Tevenphage. https://commons.wikimedia.org/wiki/File:Tevenphage.svg", "CC BY-SA 2.5", "correspon a 7.6 Virus: bacteriòfag amb cap, cua, placa basal i fibres"),
}


def write_credits_and_gallery(bodies: dict[str, str]) -> None:
    caps = {}
    for raw in bodies.values():
        for fid, cap in re.findall(r"\{\{fig:([\w.-]+)\|(.*?)\}\}", raw, flags=re.S):
            caps[fid] = re.sub(r"\s+", " ", cap).strip()
    rows = []
    cards = []
    for fid in sorted(figures.FIGS):
        cap = caps.get(fid, "")
        comp = CC_CREDIT[fid][2] if fid in CC_CREDIT else "correspon al peu del capítol"
        cards.append(
            f'<article class="card" style="padding:12px"><h3>{esc(fid)}</h3>'
            f'<img src="assets/fig/{fid}.svg" alt="{esc(cap)}" style="width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:12px">'
            f'<p>{esc(cap)}</p></article>'
        )
    for fid in sorted(CC_CREDIT):
        font, lic, comp = CC_CREDIT[fid]
        cap = caps.get(fid, "")
        rows.append(
            f"<tr><td>{esc(fid)}</td><td>{esc(cap)}</td><td>{esc(font)}</td><td>{esc(lic)}</td>"
            f"<td>comprovat: {esc(comp)}</td></tr>"
        )
    table = (
        '<header class="hero"><div class="eyebrow">Figures</div><h1>Crèdits</h1>'
        '<p>Les il·lustracions de tercers amb llicència CC BY o CC BY-SA. La resta de figures del dossier són elaboració pròpia i no requereixen crèdit.</p></header>'
        '<table><thead><tr><th>Figura</th><th>Peu</th><th>Font</th><th>Llicència</th><th>Comprovació</th></tr></thead><tbody>'
        + "".join(rows) + "</tbody></table>"
    )
    gallery = (
        '<header class="hero"><div class="eyebrow">Per revisar</div><h1>Galeria de figures</h1>'
        '<p>Cada figura al costat del peu amb què surt al capítol, i la línia de comprovació.</p></header>'
        f'<div class="cards">{"".join(cards)}</div>'
    )
    (BIO / "credits.html").write_text(shell(
        "Crèdits de les figures – Biologia", "b-annex", table, None, 0,
        '<a href="./">Llibre</a><span class="sep">›</span><span class="last">Crèdits</span>',
    ))
    (BIO / "galeria.html").write_text(shell(
        "Galeria de figures – Biologia", "b-annex", gallery, None, 0,
        '<a href="./">Llibre</a><span class="sep">›</span><span class="last">Galeria</span>',
    ))
    # còpia llegible fora de l'HTML, amb la columna que ha demanat el professorat
    lines = ["figura\tpeu\tfont\tllicencia\tcomprovat"]
    for fid in sorted(CC_CREDIT):
        font, lic, comp = CC_CREDIT[fid]
        cap = caps.get(fid, "")
        lines.append("\t".join(x.replace("\t", " ") for x in (fid, cap, font, lic, f"comprovat: {comp}")))
    (ROOT / "tools" / "biologia" / "credits.tsv").write_text("\n".join(lines) + "\n")


def main() -> None:
    global CHAPTERS
    CHAPTERS = [ch for ch in CHAPTERS if (CAPS / ch["file"]).is_file()]
    if not CHAPTERS:
        raise SystemExit("No hi ha cap capítol a tools/biologia/caps")
    write_figures()
    (BIO / "teoria").mkdir(parents=True, exist_ok=True)
    bodies = {}
    for ch in CHAPTERS:
        raw = deepen((CAPS / ch["file"]).read_text())
        bodies[ch["slug"]] = raw
        body = expand_figs(raw, inline=False)
        cover = (
            f'<header class="cover"><div class="cover-band"><div class="cover-num"><small>Tema {esc(ch["n"])}</small>{esc(ch["n"])}</div>'
            f'<div class="cover-kick">{esc(ch["kick"])}</div><h1>{esc(ch["title"])}</h1></div>'
            f'<figure class="cover-pic"><img src="../assets/covers/{ch["slug"]}.svg" alt="Portada del tema {esc(ch["title"])}" width="1200" height="800"></figure>'
            f'<div class="cover-body"><p>{esc(ch["blurb"])}</p><nav class="cover-toc" aria-label="En aquest tema"><h2>En aquest tema</h2><ol>{cover_toc(ch)}</ol></nav></div></header>'
        )
        i = CHAPTERS.index(ch)
        crumb = (
            f'<a href="../">Llibre</a><span class="sep">›</span><a href="./" class="hide-s">Teoria</a>'
            f'<span class="sep hide-s">›</span><a href="{ch["slug"]}.html" class="cur-t">Tema {esc(ch["n"])}</a>'
            f'<span class="sep" hidden>›</span><span class="last" id="crumb-sub" hidden></span>'
        )
        page = shell(
            f'Tema {ch["n"]}. {ch["title"]} – Biologia',
            ch["cls"],
            cover + body + neighbor(i),
            ch["slug"],
            1,
            crumb,
        )
        (BIO / "teoria" / f'{ch["slug"]}.html').write_text(page)
        # ids present
        for sid, _short, title in ch["secs"]:
            if f'id="{sid}"' not in body and f"id='{sid}'" not in body:
                raise SystemExit(f'{ch["slug"]}: falta la secció {sid} ({title})')

    all_text = "\n".join(bodies.values())
    check_coverage(all_text, {ch["slug"] for ch in CHAPTERS})
    # index of theory mirrors the book home, like /btx/teoria/
    idx = index_main().replace('href="teoria/', 'href="').replace('src="assets/', 'src="../assets/').replace(
        'data-zoom="assets/', 'data-zoom="../assets/'
    ).replace('href="glossari.html"', 'href="../glossari.html"').replace(
        'href="cobertura.html"', 'href="../cobertura.html"'
    ).replace('href="biologia-teoria.pdf"', 'href="../biologia-teoria.pdf"').replace(
        'href="../btx/"', 'href="../../btx/"'
    ).replace('href="../"', 'href="../../"').replace(
        'href="galeria.html"', 'href="../galeria.html"'
    ).replace('href="credits.html"', 'href="../credits.html"')
    (BIO / "teoria" / "index.html").write_text(
        shell(
            "Llibre de teoria – Biologia",
            "b-annex",
            idx,
            None,
            1,
            '<a href="../">Llibre</a><span class="sep">›</span><span class="last">Teoria</span>',
        )
    )
    (BIO / "index.html").write_text(
        shell(
            "Biologia – 2n de Batxillerat",
            "b-annex",
            index_main(),
            None,
            0,
            '<span class="last">Portada</span>',
        )
    )
    (BIO / "glossari.html").write_text(
        shell(
            "Glossari – Biologia",
            "b-annex",
            glossari_main(bodies),
            None,
            0,
            '<a href="./">Llibre</a><span class="sep">›</span><span class="last">Glossari</span>',
        )
    )
    (BIO / "cobertura.html").write_text(
        shell(
            "Cobertura del currículum – Biologia",
            "b-annex",
            cobertura_main(),
            None,
            0,
            '<a href="./">Llibre</a><span class="sep">›</span><span class="last">Cobertura</span>',
        )
    )
    (BIO / "teoria.html").write_text(print_book(bodies))
    write_credits_and_gallery(bodies)
    # unknown figure ids
    used = set(re.findall(r"\{\{fig:([\w.-]+)\|", "\n".join(bodies.values())))
    extra = set(figures.FIGS) - used
    if extra:
        print("Avís: figures no usades:", ", ".join(sorted(extra)))
    print(f"OK {len(CHAPTERS)} temes, {len(figures.FIGS)} figures")


if __name__ == "__main__":
    main()
