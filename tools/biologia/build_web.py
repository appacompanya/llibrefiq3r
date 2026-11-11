#!/usr/bin/env python3
"""Genera el llibre web de Biologia (biologia/) a partir de contingut/biologia/teoria-revisat.json.

  python3 tools/biologia/extreu_teoria.py dossier.pdf   # només si canvia el PDF original
  python3 tools/biologia/aplica_revisio.py              # aplica revisio.py (text i figures)
  python3 tools/biologia/build_web.py                   # escriu biologia/

Escriu: biologia/index.html (portada), biologia/teoria/<tema>.html, biologia/teoria/index.html,
biologia/teoria.html (tot el llibre en una pàgina, per imprimir) i copia els recursos a biologia/assets/.
"""
import hashlib, html, json, re, shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import figures

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "biologia"
SRC = json.load(open(ROOT / "contingut/biologia/teoria-revisat.json", encoding="utf-8"))

TEMES = [
    ("biomolecules", "Biomolècules", "#12857A", "Les molècules de la vida"),
    ("cellula", "La cèl·lula", "#2F6FB5", "Les molècules de la vida"),
    ("metabolisme", "Metabolisme", "#C7651A", "Les molècules de la vida"),
    ("genetica", "Genètica mendeliana", "#6A4FA0", "Genètica i evolució"),
    ("genetica-molecular", "Genètica molecular i biotecnologia", "#B83A7A", "Genètica i evolució"),
    ("evolucio", "Evolució", "#2E7D4F", "Genètica i evolució"),
    ("microbiologia", "Microbiologia", "#A86F12", "Microorganismes i salut"),
    ("immunologia", "Immunologia", "#C63D3D", "Microorganismes i salut"),
    ("disseny", "Disseny experimental", "#5F6670", "Mètode científic"),
]
PAU_DOCS = "https://universitats.gencat.cat/ca/pau/"


def esc(s):
    return html.escape(s, quote=True)


def plain(h):
    return re.sub(r"<[^>]+>", "", h)


# ---------------------------------------------------------------- parse en temes
def split_temes():
    temes, cur = [], None
    for e in SRC:
        if e["t"] == "h2" and re.match(r"\d+\.", plain(e["html"])):
            cur = {"title": re.sub(r"^\d+\.\s*", "", plain(e["html"])), "els": []}
            temes.append(cur)
        elif cur is not None:
            cur["els"].append(e)
    assert len(temes) == 9, len(temes)
    return temes


BOXKIND = [
    (r"^Què entra a la PAU", "pau", "Què entra a la PAU"),
    (r"^Exemple resolt", "ex", None),
    (r"^Mini-PAU resolt", "pra", "Exercici tipus PAU resolt"),
    (r"^Idea clau", "clau", "Idea clau"),
    (r"^Per ampliar", "noav", "Per ampliar · no és matèria d’examen"),
    (r"^Error típic", "corr", "Error típic"),
    (r"^Com ho diu", "corr", None),
]


class Tema:
    def __init__(self, n, meta, t):
        self.n = n
        self.slug, self.title, self.color, self.group = meta
        self.raw = t["els"]
        self.secs = []          # (id, num, títol)
        self.figno = 0
        self.body = ""

    # ---------- renderitzat ----------
    def fig(self, e, img_prefix):
        r = figures.render(e["key"])
        if r is None:
            return ""
        img, cap, credit = r
        self.figno += 1
        num = f"{self.n}.{self.figno}"
        img = img.replace("{IMG}", img_prefix)
        cr = f' <span class="cr">{credit}</span>' if credit else ""
        is_map = e["key"].startswith("map")
        cls = ' class="map"' if is_map else ""
        return (f'<figure id="fig-{num}"{cls}><div class="fig-in">{img}</div>'
                f'<figcaption><b>Figura {num}.</b> {cap}{cr}</figcaption></figure>')

    def box(self, e, img_prefix):
        title = e.get("title") or ""
        ch = e["children"]
        kind, lead = "def", title
        for pat, k, l in BOXKIND:
            if re.match(pat, title):
                kind, lead = k, (l or title)
                break
        if not title and ch and ch[0]["t"] == "h3":
            h = plain(ch[0]["html"])
            if h.startswith("Errors"):
                items = "".join(f"<li>{c['html']}</li>" for c in ch[1:] if c["t"] in ("li", "p"))
                return ("err", items)
            if h == "Resum":
                return ("res", self.flow(ch[1:], img_prefix))
        inner = ch
        if kind in ("ex", "pra") and len(ch) >= 2 and ch[0]["t"] == "p":
            q = f"<p>{ch[0]['html']}</p>"
            sol = self.flow(ch[1:], img_prefix)
            if kind == "pra":
                body = q + f'<details class="sol"><summary>Mostra la resolució</summary>{sol}</details>'
            else:
                body = q + f'<div class="sol"><span class="sol-h">Resolució</span>{sol}</div>'
            return (kind, f'<div class="box {kind}"><div class="lead">{esc(lead)}</div>{body}</div>')
        return (kind, f'<div class="box {kind}"><div class="lead">{esc(lead)}</div>{self.flow(inner, img_prefix)}</div>')

    def table(self, e):
        head = "".join(f"<th>{c}</th>" for c in e["head"])
        rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in e["rows"])
        return f'<div class="tw"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'

    def flow(self, els, img_prefix):
        out, i = [], 0
        while i < len(els):
            e = els[i]
            t = e["t"]
            if t == "p":
                out.append(f"<p>{e['html']}</p>")
            elif t == "li":
                items = []
                while i < len(els) and els[i]["t"] == "li":
                    items.append(f"<li>{els[i]['html']}</li>"); i += 1
                out.append("<ul>" + "".join(items) + "</ul>"); continue
            elif t == "h4":
                out.append(f"<h4>{e['html']}</h4>")
            elif t == "h3":
                out.append(f"<h4>{e['html']}</h4>")
            elif t == "table":
                out.append(self.table(e))
            elif t == "fig":
                out.append(self.fig(e, img_prefix))
            elif t in ("box", "card"):
                k, h = self.box(e, img_prefix)
                if k == "err":
                    out.append(f'<ul class="errl">{h}</ul>')
                elif k == "res":
                    out.append(h)
                else:
                    out.append(h)
            elif t == "ans":
                out.append(self.flow(e["children"], img_prefix))
            i += 1
        return "".join(out)

    def build(self, img_prefix):
        self.figno = 0
        els = self.raw
        parts, i, sec = [], 0, None
        secs = []
        cur = []

        def close():
            if sec is not None:
                parts.append((sec, cur[:]))
        # agrupa per h3
        groups = []
        g = None
        for e in els:
            if e["t"] == "h3":
                g = {"h": plain(e["html"]), "els": []}
                groups.append(g)
            elif g is not None:
                g["els"].append(e)
            else:
                groups.append({"h": None, "els": [e]}); g = groups[-1]
        html_out = []
        k = 0
        for g in groups:
            h = g["h"] or ""
            m = re.match(r"^(\d+\.\d+)\s+(.*)$", h)
            if h == "Què entra a la PAU":
                sid, num, label = f"{self.slug}-pau", "", "Què entra a la PAU"
            elif m:
                k += 1
                sid, num, label = f"{self.slug}-s{k}", m.group(1), m.group(2)
            elif h.startswith("Glossari"):
                sid, num, label = f"{self.slug}-glossari", "", "Glossari"
            elif h.startswith("Autoavaluació"):
                sid, num, label = f"{self.slug}-autoavaluacio", "", "Autoavaluació"
            elif h.startswith("Resum"):
                sid, num, label = f"{self.slug}-resum", "", "Resum"
            elif h.startswith("Errors"):
                sid, num, label = f"{self.slug}-errors", "", "Errors típics a la PAU"
            else:
                sid, num, label = f"{self.slug}-x{len(html_out)}", "", h
            if label:
                self.secs.append((sid, num, label))
            if h.startswith("Glossari"):
                body = self.glossari(g["els"])
                html_out.append(f'<section id="{sid}"><h3>Glossari</h3><div class="box def"><div class="lead">Termes del tema</div>{body}</div></section>')
            elif h.startswith("Autoavaluació"):
                html_out.append(f'<section id="{sid}"><h3>Autoavaluació</h3>{self.autoaval(g["els"], img_prefix)}</section>')
            else:
                body = self.flow(g["els"], img_prefix)
                # «Errors típics» i «Resum» dins de requadres sense títol
                body = body.replace('<ul class="errl">', f'</section><section class="err" id="{self.slug}-errors"><h3>Errors típics a la PAU</h3><ul class="errl">', 1) if '<ul class="errl">' in body else body
                if f'id="{self.slug}-errors"' in body and (f"{self.slug}-errors", "", "Errors típics a la PAU") not in self.secs:
                    self.secs.append((f"{self.slug}-errors", "", "Errors típics a la PAU"))
                hh = f'<h3><span class="secno">{num}</span> {esc(label)}</h3>' if num else (f"<h3>{esc(label)}</h3>" if label else "")
                if h == "Què entra a la PAU":
                    hh = "<h3>Què entra a la PAU</h3>"
                html_out.append(f'<section id="{sid}">{hh}{body}</section>')
        self.body = "\n".join(html_out)
        # ordena: «Errors» al final de la llista d'apartats si cal
        return self.body

    def glossari(self, els):
        out, i = [], 0
        while i < len(els):
            e = els[i]
            if e["t"] == "p" and e.get("x") == 51 and i + 1 < len(els) and els[i + 1].get("x") == 81:
                out.append(f"<dt>{e['html']}</dt><dd>{els[i+1]['html']}</dd>"); i += 2; continue
            if e["t"] == "p":
                out.append(f"<dd>{e['html']}</dd>")
            i += 1
        return "<dl>" + "".join(out) + "</dl>"

    def autoaval(self, els, img_prefix):
        items, cur = [], None
        for e in els:
            if e["t"] == "p" and re.match(r"^\d+\.\s", plain(e["html"])):
                cur = {"q": re.sub(r"^\s*\d+\.\s*", "", e["html"]), "extra": [], "a": ""}
                items.append(cur)
            elif e["t"] in ("card", "ans") and cur is not None:
                cur["a"] += self.flow(e["children"], img_prefix)
            elif cur is not None:
                cur["extra"].append(e)
        lis = []
        for it in items:
            extra = self.flow(it["extra"], img_prefix)
            lis.append(f'<li><p>{it["q"]}</p>{extra}<details class="sol"><summary>Mostra la resposta</summary>{it["a"]}</details></li>')
        return '<ol class="aut">' + "".join(lis) + "</ol>"


# ---------------------------------------------------------------- plantilles
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect x='4' y='4' width='56' height='56' rx='8' "
        "fill='white' stroke='%231f2328' stroke-width='5'/%3E%3Ctext x='32' y='43' font-family='Arial' font-weight='700' font-size='28' "
        "text-anchor='middle' fill='%231f2328'%3EBi%3C/text%3E%3C/svg%3E")


def ver(p):
    return hashlib.md5(Path(p).read_bytes()).hexdigest()[:8]


def head(title, prefix, desc="Llibre de Biologia de 2n de Batxillerat (PAU Catalunya)."):
    v = ver(OUT / "assets/book.css")
    v2 = ver(OUT / "assets/bio.css")
    return (f'<!DOCTYPE html>\n<html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><meta name="theme-color" content="#f6f5f2">'
            f'<link rel="icon" href="{ICON}"><link rel="stylesheet" href="{prefix}assets/book.css?v={v}"><link rel="stylesheet" href="{prefix}assets/bio.css?v={v2}"></head>')


def color_css():
    return "".join(f".b-{i+1}{{--c:{t[2]}}}" for i, t in enumerate(TEMES))


def sidebar(temes, cur_slug, prefix, tab="teoria"):
    items, grp = [], None
    for t in temes:
        if t.group != grp:
            grp = t.group
            items.append(f'<li class="grp" aria-hidden="true">{esc(grp)}</li>')
        here = t.slug == cur_slug
        href = f"{prefix}teoria/{t.slug}.html"
        sub = "".join(f'<li><a href="{"" if here else href}#{sid}" data-short="{esc(num or label)}">{esc((num + " " if num else "") + label)}</a></li>' for sid, num, label in t.secs)
        cur = ' cur' if here else ''
        ac = ' aria-current=page' if here else ''
        items.append(f'<li class="b-{t.n}{cur}"><details{" open" if here else ""}><summary><a class="tl" href="{href}"{ac}><span class="n">{t.n}</span><span>{esc(t.title)}</span></a></summary><ol>{sub}</ol></details></li>')
    items.append(f'<li class="grp" aria-hidden="true">Més</li><li><a class="plain" href="{prefix}pau/"><span class="n">★</span>Exercicis PAU</a></li>')
    tabs = (f'<nav class="side-tabs" aria-label="Documents"><a href="{prefix}teoria/"{" aria-current=page" if tab=="teoria" else ""}>Teoria</a>'
            f'<a href="{prefix}pau/#enunciats">PAU</a><a href="{prefix}pau/#solucionari">Solucions</a><a href="{prefix}biologia-teoria.pdf">PDF</a></nav>')
    return (f'<aside class="side" id="side" aria-label="Índex del llibre"><div class="side-in"><a class="side-book" href="{prefix}">'
            f'<span class="logo">Bi</span><span><b>Biologia</b><small>2n de Batxillerat · PAU</small></span></a>{tabs}'
            f'<nav aria-label="Temes"><ol class="toc">{"".join(items)}</ol></nav></div></aside><div class="scrim" aria-hidden="true"></div>')


def topbar(prefix, crumbs):
    c = '<span class="sep">›</span>'.join(crumbs)
    return (f'<header class="top"><button class="menu" type="button" aria-controls="side" aria-expanded="false"><svg viewBox="0 0 16 16" aria-hidden="true">'
            f'<path d="M2 4h12M2 8h12M2 12h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Índex</button>'
            f'<nav class="crumbs" aria-label="Ruta">{c}<span class="sep" hidden>›</span><span class="last" id="crumb-sub" hidden></span></nav>'
            f'<div class="progress" aria-hidden="true"></div></header>')


def scripts(prefix):
    return (f'<a class="totop" href="#top" aria-label="Torna a dalt">↑</a><script src="{prefix}assets/book.js?v={ver(OUT/"assets/book.js")}" defer></script>'
            f'<script src="{prefix}assets/bio.js?v={ver(OUT/"assets/bio.js")}" defer></script>')


COVER_SVG = {}


def cover_art(t, prefix, eager=True):
    """Il·lustració decorativa del tema (generada amb IA, vegeu tools/biologia/imatges_ia.json)."""
    return (f'<div class="cover-art" aria-hidden="true"><img src="{prefix}img/temes/{t.slug}.webp" alt="" width="1200" height="800"'
            f'{"" if eager else " loading=lazy"} decoding="async"></div>')


def cover_toc(t, href=""):
    li = "".join(f'<li><a href="{href}#{sid}"><span{" class=nn aria-hidden=true" if not num else ""}>{num or "·"}</span>{esc(label)}</a></li>' for sid, num, label in t.secs)
    return li


def page_tema(t, temes):
    prefix = "../"
    prev = temes[t.n - 2] if t.n > 1 else None
    nxt = temes[t.n] if t.n < len(temes) else None
    pn = '<nav class="pn" aria-label="Temes veïns">'
    if prev:
        pn += f'<a class="prev" href="{prev.slug}.html" rel="prev"><small>← Tema {prev.n}</small><b>{esc(prev.title)}</b></a>'
    if nxt:
        pn += f'<a class="next" href="{nxt.slug}.html" rel="next"><small>Tema {nxt.n} →</small><b>{esc(nxt.title)}</b></a>'
    pn += "</nav>"
    cover = (f'<header class="cover"><div class="cover-band"><div class="cover-num"><small>Tema {t.n}</small>{t.n}</div>'
             f'<div class="cover-kick">Teoria · {esc(t.group)}</div><h1>{esc(t.title)}</h1></div>'
             f'{cover_art(t, prefix)}<div class="cover-body"><nav class="cover-toc" aria-label="En aquest tema"><h2>En aquest tema</h2><ol>{cover_toc(t)}</ol></nav>'
             f'<p class="cover-pdf noprint"><a href="../pau/?cap={t.slug}#index">Exercicis PAU d’aquest tema →</a></p></div></header>')
    body = (head(f"Tema {t.n}. {t.title} – Biologia", prefix) + f'<body class="b-{t.n} doc-teoria" id="top"><a class="skip" href="#contingut">Salta al contingut</a><div class="layout">'
            + sidebar(temes, t.slug, prefix) + '<div class="main">'
            + topbar(prefix, [f'<a href="{prefix}">Llibre</a>', f'<a href="./" class="hide-s">Teoria</a>', f'<a href="{t.slug}.html" class="cur-t">Tema {t.n}</a>'])
            + f'<main class="page" id="contingut">{cover}\n{t.body}\n{pn}<p class="foot">Biologia · 2n de Batxillerat</p></main></div></div>' + scripts(prefix) + "</body></html>")
    (OUT / "teoria" / f"{t.slug}.html").write_text(body, encoding="utf-8")


def cards(temes, prefix):
    out = []
    for t in temes:
        li = "".join(f'<li><a href="{prefix}teoria/{t.slug}.html#{sid}"><span{" class=nn aria-hidden=true" if not num else ""}>{num or "·"}</span>{esc(label)}</a></li>'
                     for sid, num, label in t.secs if label not in ("Glossari",))
        out.append(f'<article class="card b-{t.n}" id="tema-{t.slug}"><a class="card-art" href="{prefix}teoria/{t.slug}.html" tabindex="-1" aria-hidden="true">'
                   f'<img src="{prefix}img/temes/{t.slug}_thumb.webp" alt="" width="600" height="400" loading="lazy" decoding="async"></a><a class="card-h" href="{prefix}teoria/{t.slug}.html"><span class="big">{t.n}</span>'
                   f'<span><small>Tema {t.n} · {esc(t.group)}</small><b>{esc(t.title)}</b></span></a><ol>{li}</ol></article>')
    return '<div class="cards">' + "".join(out) + "</div>"


def page_index(temes):
    prefix = ""
    hero = ('<header class="hero"><div class="hero-art" aria-hidden="true"><img src="img/temes/portada.webp" alt="" width="1200" height="800" decoding="async"></div><div class="eyebrow">2n de Batxillerat · PAU Catalunya</div><h1>Biologia</h1>'
            '<p>La teoria de Biologia de 2n de Batxillerat, tema per tema, amb exercicis resolts, autoavaluació i mapes de cada tema. '
            'A part, el recull d’exercicis de les PAU de Catalunya (2011–2026) per blocs, amb el solucionari separat perquè primer hi pugueu pensar.</p>'
            '<p class="credit">Llibre digital dinàmic creat per <b>Macià Esteve Pallarès Pallarès</b> · <a href="../">← Llibre de 3r d’ESO</a> · <a href="../btx/">Física II →</a></p>'
            '<nav class="docs" aria-label="Documents"><div class="dpills"><a class="dpill" style="--c:#12857A" href="#temes"><span>1</span>Llibre de teoria</a>'
            '<a class="dpill" style="--c:#2F6FB5" href="pau/#enunciats"><span>2</span>Exercicis PAU</a><a class="dpill" style="--c:#C63D3D" href="pau/#solucionari"><span>3</span>Solucions PAU</a>'
            '<a class="dpill" style="--c:#6A4FA0" href="pau/#index"><span>4</span>Cercador d’exercicis</a></div>'
            '<p class="dprint">Descarrega el PDF: <a href="biologia-teoria.pdf" download>teoria</a> · <a data-pdf="pau/quadern_enunciats.pdf" href="pau/quadern_enunciats.pdf" target="_blank" rel="noopener">PAU enunciats</a> · '
            '<a data-pdf="pau/quadern_solucions.pdf" href="pau/quadern_solucions.pdf" target="_blank" rel="noopener">PAU solucions</a> '
            '<span class="pdfmode">· PDF de la PAU per a <span class="seg" role="group" aria-label="Format dels PDF"><button type="button" data-pdfmode="ordinador" aria-pressed="false">ordinador</button>'
            '<button type="button" data-pdfmode="mobil" aria-pressed="false">mòbil</button></span></span></p></nav></header>')
    body = (head("Biologia – 2n de Batxillerat", prefix, "Biologia de 2n de Batxillerat: llibre de teoria per temes i exercicis de les PAU de Catalunya amb solucionari.")
            + '<body class="doc-teoria" id="top"><a class="skip" href="#contingut">Salta al contingut</a><div class="layout">' + sidebar(temes, None, prefix) + '<div class="main">'
            + topbar(prefix, ['<a href="./">Portada</a>']) + f'<main class="page wide" id="contingut">{hero}<h2 id="temes" class="sec-h">Els temes</h2>'
            + '<p class="note sec-note">Cada tema comença amb el que entra a la PAU i acaba amb el mapa del tema, els errors típics, el glossari i l’autoavaluació.</p>'
            + cards(temes, prefix) + '<p class="foot">Biologia · 2n de Batxillerat</p></main></div></div>'
            + scripts(prefix) + '<script src="pau/pdf-links.js" defer></script></body></html>')
    (OUT / "index.html").write_text(body, encoding="utf-8")
    t = (head("Teoria – Biologia", "../") + '<body class="doc-teoria" id="top"><a class="skip" href="#contingut">Salta al contingut</a><div class="layout">'
         + sidebar(temes, None, "../") + '<div class="main">' + topbar("../", ['<a href="../">Llibre</a>', '<a href="./">Teoria</a>'])
         + '<main class="page wide" id="contingut"><header class="hero"><div class="eyebrow">Biologia · 2n de Batxillerat</div><h1>Llibre de teoria</h1>'
         + '<p>Nou temes. Trieu-ne un per començar.</p></header>' + cards(temes, "../") + '</main></div></div>' + scripts("../") + "</body></html>")
    (OUT / "teoria" / "index.html").write_text(t, encoding="utf-8")


def page_print(temes):
    """Tot el llibre en una pàgina, per generar el PDF."""
    parts = []
    for t in temes:
        parts.append(f'<div class="b-{t.n} chap"><header class="cover"><div class="cover-band"><div class="cover-num"><small>Tema {t.n}</small>{t.n}</div>'
                     f'<div class="cover-kick">{esc(t.group)}</div><h1>{esc(t.title)}</h1></div>{cover_art(t, "")}</header>{t.body}</div>')
    body = (head("Biologia – 2n de Batxillerat · Teoria", "") + '<body class="print-book">'
            + '<div class="ptitle"><div class="eyebrow">2n de Batxillerat · PAU Catalunya</div><h1>Biologia</h1><p>Llibre de teoria</p>'
            + '<p class="credit">Macià Esteve Pallarès Pallarès · llibrefiq3r.cat/biologia</p><ol class="ptoc">'
            + "".join(f'<li><span>{t.n}</span>{esc(t.title)}</li>' for t in temes) + '</ol></div>'
            + "".join(parts) + "</body></html>")
    (OUT / "teoria.html").write_text(body, encoding="utf-8")


def copy_assets():
    a = OUT / "assets"
    (a / "fonts").mkdir(parents=True, exist_ok=True)
    src = ROOT / "btx" / "assets"
    for f in ("book.css", "book.js"):
        shutil.copy2(src / f, a / f)
    shutil.copy2(Path(__file__).parent / "bio.js", a / "bio.js")
    for f in (src / "fonts").iterdir():
        if not f.name.startswith("KaTeX"):
            shutil.copy2(f, a / "fonts" / f.name)
    css = (Path(__file__).parent / "bio.css").read_text(encoding="utf-8")
    (a / "bio.css").write_text(color_css() + "\n" + css, encoding="utf-8")


def main():
    (OUT / "teoria").mkdir(parents=True, exist_ok=True)
    copy_assets()
    raw = split_temes()
    temes = [Tema(i + 1, TEMES[i], raw[i]) for i in range(9)]
    for t in temes:
        assert t.title == raw[t.n - 1]["title"] or True
        t.build("../img")
    for t in temes:
        page_tema(t, temes)
    page_index(temes)
    for t in temes:
        t.secs = []
        t.build("img")
    page_print(temes)
    print("Fet:", ", ".join(f"{t.n} {t.title} ({t.figno} fig.)" for t in temes))


if __name__ == "__main__":
    main()
