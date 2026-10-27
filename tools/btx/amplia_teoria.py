#!/usr/bin/env python3
"""Amplia el llibre de teoria de Física II (btx/teoria/*.html i btx/teoria.html) amb els blocs de
tools/btx/ampliacions/*.py: definicions, demostracions, exemples i figures noves.

Cada bloc es desa entre comentaris <!--amp:ID--> … <!--/amp:ID-->, de manera que l'script es pot tornar
a executar: primer treu els blocs antics i després hi posa els actuals.

Fórmules: $…$ (en línia) i $$…$$ (en bloc), renderitzades amb KaTeX 0.16.47 (la versió de btx/assets/katex.css):
    cd tools/btx && npm i katex@0.16.47     (o bé KATEX_DIR=<carpeta node_modules>)
Ús:  python3 tools/btx/amplia_teoria.py
     node tools/btx/pdf_teoria.js && python3 tools/btx/pdf_portada.py      (PDF descarregable)
"""
from __future__ import annotations

import hashlib
import html
import importlib.util
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BTX = ROOT / "btx"
TEO = BTX / "teoria"
FIG = BTX / "assets" / "fig"
AMP = Path(__file__).resolve().parent / "ampliacions"

CSS_EXTRA = """/*amp-css*/.box.def{--k:#0b6e6e;--ico:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z'/%3E%3Cpath d='M9 9h6M9 13h6'/%3E%3C/svg%3E")}
.box.def dl{margin:.4em 0}.box.def dt{font-weight:700;margin-top:.5em}.box.def dd{margin:.15em 0 0 1.2em}
.amp-tab td,.amp-tab th{vertical-align:top}
h4.amp{font-family:var(--sans);font-size:1.12rem;margin:1.9em 0 .6em;padding:.1em 0 .1em .6em;border-left:4px solid var(--c,#1b1f24);color:var(--c,#1b1f24)}/*/amp-css*/"""

# només per al llibre sencer (btx/teoria.html), que és el que es fa servir per al PDF: títols més diferenciats i
# regles de paginació (el títol no queda mai sol a final de pàgina; els blocs curts no es parteixen, els llargs sí)
CSS_BOOK = """/*amp-book*/
/* colors de cada bloc, els mateixos de la web (btx/assets/book.css) */
.chap{--c:#1f3f7f}
#mhs,#ones,#fen{--c:#12857A}#grav{--c:#2F6FB5}#elec{--c:#C7651A}#mag,#ind{--c:#B83A7A}
#quant,#rel,#nucl{--c:#C63D3D}#opt{--c:#A86F12}#formulari{--c:#5f6670}
h2,h3,h4,.box .lead{font-family:"DejaVu Sans",Arial,Helvetica,sans-serif}
h2{font-size:1.7em;color:var(--c);border-bottom:3px solid var(--c);padding-bottom:.2em;letter-spacing:-.01em}
h3{font-size:1.22em;color:#fff;background:var(--c);padding:.28em .65em;border-radius:4px;margin:1.9em 0 .7em}
h4,h4.amp{font-size:1.06em;color:var(--c);border:0;border-bottom:1.5px solid color-mix(in srgb,var(--c) 40%,#fff);padding:0 0 .15em;margin:1.5em 0 .55em}
.box .lead{font-size:.93em;color:#1b1f24;margin-bottom:.45em}
.box.def{border-left-color:var(--c)}.box.def .lead,.box.def dt{color:var(--c)}
.box.dem{border-left-color:var(--c)}
h2,h3,h4,.box .lead,dt{break-after:avoid;page-break-after:avoid}
h2,h3,h4{break-inside:avoid;page-break-inside:avoid}
p,li,dd{orphans:3;widows:3}
.kd,.katex-display,tr,dt,figure{break-inside:avoid;page-break-inside:avoid}
p:has(+ .kd){break-after:avoid;page-break-after:avoid}
.box{break-inside:auto;page-break-inside:auto}
.box.keep,table.keep,figure.keep{break-inside:avoid;page-break-inside:avoid}
/*/amp-book*/"""


def load_blocks():
    blocks, figs = [], {}
    for f in sorted(AMP.glob("*.py")):
        if f.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        blocks += getattr(mod, "BLOCKS", [])
        figs.update(getattr(mod, "FIGS", {}))
    return blocks, figs


# ---------- fórmules ----------
MATH = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def render_math(htmls: list[str]) -> list[str]:
    exprs = []
    for h in htmls:
        for m in MATH.finditer(h):
            exprs.append([m.group(1) if m.group(1) is not None else m.group(2), m.group(1) is not None])
    if not exprs:
        return htmls
    r = subprocess.run(["node", str(Path(__file__).with_name("katex_render.js"))], input=json.dumps(exprs),
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr)
    out = iter(json.loads(r.stdout))
    res = []
    for h in htmls:
        def rep(m):
            k = next(out)
            return f'<div class="kd">{k}</div>' if m.group(1) is not None else k
        res.append(MATH.sub(rep, h))
    return res


# ---------- figures ----------
def fig_html(fid: str, svg: str, cap: str, inline: bool) -> str:
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    w, h = (vb.group(1), vb.group(2)) if vb else ("700", "300")
    num = fid.replace("fig-", "")
    capt = f"<figcaption><b>Figura {num}.</b> {cap}</figcaption>"
    if inline:
        return f'<figure id="{fid}">{svg}{capt}</figure>'
    v = hashlib.sha1(svg.encode()).hexdigest()[:8]
    alt = html.escape(f"Figura {num}. " + re.sub(r"<[^>]+>", "", cap), quote=True)
    return (f'<figure id="{fid}"><img src="../assets/fig/{fid}.svg?v={v}" alt="{alt}" loading="lazy" '
            f'decoding="async" width="{w}" height="{h}">{capt}</figure>')


# ---------- inserció ----------
def strip_old(s: str) -> str:
    return re.sub(r"<!--amp:[\w.-]+-->.*?<!--/amp:[\w.-]+-->", "", s, flags=re.S)


def end_of_element(s: str, i: int) -> int:
    tag = re.match(r"<(\w+)", s[i:]).group(1)
    depth, j = 0, i
    pat = re.compile(rf"<{tag}\b|</{tag}>")
    for m in pat.finditer(s, i):
        depth += 1 if m.group(0) != f"</{tag}>" else -1
        if depth == 0:
            return m.end()
        j = m.end()
    raise ValueError("element sense tancar")


def find_pos(s: str, where, label: str) -> int:
    kind, arg = where
    if kind == "end":
        i = s.find(f'<section id="{arg}">')
        if i < 0:
            raise SystemExit(f"[{label}] no trobo la secció {arg}")
        return end_of_element(s, i) - len("</section>")
    if kind == "start":
        i = s.find(f'<section id="{arg}">')
        m = re.compile(r"</h3>").search(s, i)
        return m.end()
    i = s.find(arg)
    if i < 0 or s.find(arg, i + 1) >= 0:
        raise SystemExit(f"[{label}] el fragment no hi és o no és únic: {arg[:80]!r}")
    if kind == "before":
        return i
    if kind == "after":
        return end_of_element(s, i)
    raise SystemExit(kind)


def main():
    blocks, figs = load_blocks()
    rendered = render_math([b["html"] for b in blocks])
    for b, h in zip(blocks, rendered):
        b["out"] = h
    # figures
    for fid, (svg, _cap) in figs.items():
        (FIG / f"{fid}.svg").write_text(svg, encoding="utf-8")

    def expand(h: str, inline: bool) -> str:
        return re.sub(r"\[\[(fig-[\d.]+)\]\]", lambda m: fig_html(m.group(1), figs[m.group(1)][0], figs[m.group(1)][1], inline), h)

    files = sorted({b["file"] for b in blocks})
    big = strip_old((BTX / "teoria.html").read_text(encoding="utf-8"))
    for f in files:
        p = TEO / f"{f}.html"
        s = strip_old(p.read_text(encoding="utf-8"))
        for b in [x for x in blocks if x["file"] == f]:
            frag = f'<!--amp:{b["id"]}-->{expand(b["out"], False)}<!--/amp:{b["id"]}-->'
            i = find_pos(s, b["where"], b["id"])
            s = s[:i] + frag + s[i:]
            where = b["where"]
            fragb = f'<!--amp:{b["id"]}-->{expand(b["out"], True)}<!--/amp:{b["id"]}-->'
            j = find_pos(big, where, b["id"] + " (llibre sencer)")
            big = big[:j] + fragb + big[j:]
        p.write_text(s, encoding="utf-8")
        print(f"teoria/{f}.html: {sum(1 for x in blocks if x['file'] == f)} blocs")

    # CSS
    css = BTX / "assets" / "book.css"
    c = re.sub(r"/\*amp-css\*/.*?/\*/amp-css\*/", "", css.read_text(encoding="utf-8"), flags=re.S).rstrip() + "\n" + CSS_EXTRA + "\n"
    css.write_text(c, encoding="utf-8")
    big = re.sub(r"/\*amp-css\*/.*?/\*/amp-css\*/", "", big, flags=re.S)
    big = re.sub(r"/\*amp-book\*/.*?/\*/amp-book\*/", "", big, flags=re.S)
    k = big.find("</style>")
    big = big[:k] + CSS_EXTRA + CSS_BOOK + big[k:]
    (BTX / "teoria.html").write_text(big, encoding="utf-8")
    v = hashlib.sha1(c.encode()).hexdigest()[:8]
    for p in BTX.rglob("*.html"):
        t = p.read_text(encoding="utf-8")
        t2 = re.sub(r"book\.css\?v=\w+", f"book.css?v={v}", t)
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
    print("figures:", ", ".join(sorted(figs)) or "cap")


if __name__ == "__main__":
    main()
