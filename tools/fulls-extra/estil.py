"""Estil de les pàgines afegides als fulls de 2n i 4t: el mateix que els generadors del llibre de 3r
(tipografia Atkinson Hyperlegible, fórmules amb KaTeX, insígnies de pregunta, línies de punts, requadres)."""
import os, html

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "node_modules/@fontsource/atkinson-hyperlegible/files/atkinson-hyperlegible")
KX = "file://" + os.path.join(HERE, "node_modules/katex/dist")

# color de cada SdA i to clar (taules i requadres), els mateixos dels PDF originals
SDA = {
    "2n": {1: ("L'institut en xifres", "#12857A", "#DDF1EE"), 2: ("Un arc de Sant Martí dins d'un got", "#B83A7A", "#F7E1EC"),
           3: ("La pilota que no bota", "#D9731A", "#FCEBD9"), 4: ("Aigua neta del riu", "#2F6FB5", "#E0EAF6"),
           5: ("La química de la coca de Sant Joan", "#B7791F", "#F8EBD5"), 6: ("La carmanyola calenta", "#C63D3D", "#F9E0E0")},
    "4t": {1: ("Els colors de la Mercè", "#7A4CC2", "#EFE7FA"), 2: ("Aixeta o ampolla?", "#1F8FB8", "#DDF0F7"),
           3: ("Quant CO₂ costa venir a l'institut?", "#4E8A2E", "#E5F0DC"), 4: ("El patrimoni que es desfà", "#B8742A", "#F7EBDD"),
           5: ("Com es tanca una ferida?", "#D14B66", "#FBE3E8"), 6: ("L'Ictineo de Monturiol", "#1D5C8C", "#DDE9F3")},
}

CSS = """
@font-face{font-family:AH;src:url('file://%(f)s-latin-400-normal.woff2') format('woff2');font-weight:400;unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:AH;src:url('file://%(f)s-latin-700-normal.woff2') format('woff2');font-weight:700;unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:AH;src:url('file://%(f)s-latin-ext-400-normal.woff2') format('woff2');font-weight:400;unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:AH;src:url('file://%(f)s-latin-ext-700-normal.woff2') format('woff2');font-weight:700;unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}
@page{size:A4;margin:13mm 14mm 15mm}
:root{--ink:#1f2328;--muted:#5d646d;--acc:%(c)s;--tint:%(t)s;--rule:#b9bec4;--soft:#f5f6f7}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:AH,"Liberation Sans",sans-serif;font-size:11pt;line-height:1.38;color:var(--ink);margin:0}
.intro{font-size:10.5pt;color:var(--muted);margin:0 0 3.5mm}
h2{font-size:13pt;margin:1mm 0 2.5mm;display:flex;gap:2.5mm;align-items:center;break-after:avoid}
h2 .k{background:var(--acc);color:#fff;border-radius:1.6mm;padding:.3mm 2.2mm;font-size:10pt}
h3{font-size:11.5pt;margin:3.5mm 0 1.5mm;break-after:avoid}
p{margin:0 0 2mm}
.q{display:grid;grid-template-columns:7mm 1fr;gap:0 2mm;margin:0 0 3.5mm;break-inside:avoid}
.q .n{width:6.5mm;height:6.5mm;border-radius:50%%;background:var(--acc);color:#fff;font-weight:700;font-size:9.5pt;display:grid;place-items:center;margin-top:.3mm}
.l{border-bottom:.7pt dotted var(--rule);height:7.5mm}
.box{border:1pt solid var(--ink);border-radius:2.5mm;min-height:40mm;padding:2mm 3mm;font-size:9.5pt;color:var(--muted);margin:1mm 0 8mm}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
table{border-collapse:collapse;width:100%%;font-size:9.5pt;margin:1mm 0 3mm;break-inside:avoid}
th,td{border:.7pt solid #9aa1a8;padding:1.6mm 2mm;vertical-align:top;text-align:left}
th{background:var(--tint);font-weight:700}
td.e{height:9mm}
.tip{background:var(--soft);border-radius:2mm;padding:2.5mm 3.5mm;font-size:10pt;margin:2mm 0 3mm;break-inside:avoid}
.tip b{color:var(--acc)}
ul,ol{margin:0 0 2mm;padding-left:6mm}li{margin-bottom:1mm}
.ri{padding-left:4mm;text-indent:-4mm;margin:0 0 4.5mm;break-inside:avoid}
.ri .u{font-size:9pt;color:var(--muted);word-break:break-all}
.font{font-size:8.5pt;color:var(--muted);margin-top:3mm}
.katex{font-size:1.08em}
"""

KATEX_HEAD = (f'<link rel="stylesheet" href="{KX}/katex.min.css"><script src="{KX}/katex.min.js"></script>'
              f'<script src="{KX}/contrib/auto-render.min.js"></script>'
              '<script>document.addEventListener("DOMContentLoaded",()=>{renderMathInElement(document.body,{delimiters:[{left:"\\\\(",right:"\\\\)",display:false}]});document.body.dataset.math="ok";});</script>')


def page(level, sda, body, top=None):
    """Pàgina HTML; amb top (pt), la primera pàgina comença més avall per continuar l'última pàgina del full."""
    _, c, t = SDA[level][sda]
    first = f"@page:first{{margin-top:{top:.1f}pt}}" if top is not None else ""
    return (f'<!doctype html><html lang="ca"><head><meta charset="utf-8"><style>{CSS % {"f": FONT, "c": c, "t": t}}{first}</style>'
            f'{KATEX_HEAD}</head><body>{body}</body></html>')


def footer(level, sda):
    title = SDA[level][sda][0]
    return ('<div style="font-family:\'DejaVu Sans\',sans-serif;font-size:8pt;color:#24272c;width:100%;padding:0 14mm;'
            f'display:flex;justify-content:space-between"><span>Física i química · {level} ESO · SdA {sda} · {html.escape(title)}</span><span></span></div>')


# ---------- peces de contingut ----------
def lines(n):
    return '<div class="l"></div>' * n


def q(n, body, nlines=0, extra=""):
    return f'<div class="q"><span class="n">{n}</span><div>{body}{lines(nlines)}{extra}</div></div>'


def h2(k, title):
    return f'<h2><span class="k">{k}</span>{title}</h2>'


def tip(html_):
    return f'<div class="tip">{html_}</div>'


def table(head, rows, empty_cols=(), widths=None):
    """Taula amb capçalera; les columnes de empty_cols queden en blanc per respondre."""
    cg = "".join(f'<col style="width:{w}">' for w in widths) if widths else ""
    h = "<tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    b = ""
    for r in rows:
        b += "<tr>" + "".join(('<td class="e"></td>' if i in empty_cols and (i >= len(r) or not r[i]) else f"<td>{r[i] if i < len(r) else ''}</td>") for i in range(len(head))) + "</tr>"
    return f"<table>{('<colgroup>' + cg + '</colgroup>') if cg else ''}{h}{b}</table>"


def resources(items):
    """Llista de recursos: (títol, descripció, enllaç)."""
    return "".join(f'<p class="ri">•&nbsp;<b>{t}.</b> {d}<br><span class="u">{u}</span></p>' for t, d, u in items)
