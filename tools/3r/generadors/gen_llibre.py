"""Llibre imprès de l'alumnat (A4, a color, enquadernació amb espiral o wire-o).
Munta els fulls de l'alumnat (versió sense notes del professorat), hi intercala píndoles d'informació,
portades de SdA, pàgines de recursos digitals amb codis QR, índex i matèria final.
Sortida: llibre/llibre-fq3-alumnat.pdf"""
import os, re, json, subprocess, html as H
import pymupdf, segno
from playwright.sync_api import sync_playwright
import gen_sda1 as G
from mn_common import SD, use
import llibre_pindoles as PI

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(os.path.dirname(HERE), "site-fq3", "docs")
OUT = os.path.join(HERE, "llibre"); TMP = os.path.join(OUT, "_tmp")
os.makedirs(TMP, exist_ok=True)
B = "https://llibrefiq3r.cat/"
LJ = json.load(open(os.path.join(HERE, "links.json")))
D, LL, SDAS = LJ["D"], LJ["L"], LJ["SDAS"]
DIG = set(json.load(open(os.path.join(HERE, "fitxes_keys.json"))))
SDJ = {d["n"]: d for d in json.load(open("/tmp/claude-0/-home-claude/ab93dd98-bb64-5312-88e5-d8a23c91bc1c/scratchpad/sdas.json"))}
COL = {n: SD[n]["color"] for n in SD}
NEUTRE = "#3B4A5C"

AMPL = {1: "sda1-18-ampliacio.pdf", 2: "sda2-15-ampliacio.pdf", 3: "sda3-18-ampliacio.pdf", 4: "sda4-16-ampliacio.pdf", 5: "sda5-20-ampliacio.pdf", 6: "sda6-14-ampliacio.pdf"}
NOMES_DIGITAL = {"d5tfm"}           # fulls que al llibre se substitueixen per una pàgina digital


def url_l(k):
    u = LL[k]["u"]
    return u if u.startswith("http") else B + u


def qr(url, px=26):
    return segno.make(url, error="m").svg_inline(scale=3, dark="#1f2328", border=1).replace("<svg ", f'<svg style="width:{px}mm;height:{px}mm" ', 1)


# ------------------------------------------------------------------ pàgines pròpies (HTML)
BOOK_CSS = """
.cv{position:relative;height:269mm;display:flex;flex-direction:column}
.cv img{width:100%;height:150mm;object-fit:cover;border-radius:4mm}
.cv h1{font-size:40pt;line-height:1;margin:10mm 0 3mm}
.cv .sub{font-size:16pt;color:var(--muted)}
.cv .who2{margin-top:auto;display:grid;gap:4mm;font-size:12pt}
.cv .who2 span{display:flex;gap:3mm;align-items:flex-end}.cv .who2 i{flex:1;border-bottom:1pt solid var(--ink);height:1.2em}
.op{display:flex;flex-direction:column;height:269mm}
.op img{width:100%;height:105mm;object-fit:cover;border-radius:4mm}
.op .num{font-size:12pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--acc);margin-top:6mm}
.op h1{font-size:28pt;line-height:1.05;margin:1mm 0 3mm}
.op .rep{font-size:14pt;font-weight:700;background:var(--tint);border-radius:3mm;padding:3mm 4mm;margin:0 0 4mm}
.op .cols{display:grid;grid-template-columns:1fr 1fr;gap:6mm;font-size:10.5pt}
.op h3{color:var(--acc);margin:0 0 1.5mm}
.op ol{padding-left:6mm}.op li{margin-bottom:.8mm}
.qrg{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm;margin-top:3mm}
.qri{border:1pt solid var(--rule);border-radius:3mm;padding:3mm;text-align:center;break-inside:avoid}
.qri .t{font-weight:700;font-size:10pt;margin-top:1.5mm;line-height:1.2}
.qri .s{font-size:9pt;color:var(--muted)}
.qri .u{font-size:7.5pt;color:var(--muted);word-break:break-all;margin-top:1mm}
.top{display:flex;align-items:center;gap:3mm;border-bottom:2.2pt solid var(--acc);padding-bottom:2mm;margin-bottom:4mm;flex-wrap:wrap}
.top .tag{background:var(--acc);color:#fff;font-weight:700;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;border-radius:1.6mm;padding:.8mm 2.4mm}
.top h1{font-size:19pt;margin:0;flex-basis:100%}
.legend{display:grid;grid-template-columns:22mm 1fr;gap:2.2mm 5mm;align-items:center;margin:2.5mm 0;font-size:10pt;line-height:1.3}
.ico{width:20mm;height:11mm;border-radius:2.5mm;display:grid;place-items:center;color:#fff;font-weight:700;font-size:9pt;text-align:center;line-height:1.1}
.idx{columns:2;column-gap:8mm;font-size:9.6pt}
.idx .h{break-after:avoid;font-weight:700;color:#fff;border-radius:1.6mm;padding:1mm 2mm;margin:2.5mm 0 1mm}
.idx .r{display:flex;gap:2mm;break-inside:avoid;line-height:1.3}.idx .r span:first-child{flex:1}.idx .r i{flex:0 0 auto;font-style:normal;font-weight:700}
.notes .l{height:8mm}
"""


def page_html(n, body, extra=""):
    if n:
        use(n)
    else:
        G.SDA.update({"n": 0, "title": "Física i química 3r ESO", "color": NEUTRE, "tint": "#E7EAEE"})
    return G.page(body, BOOK_CSS + extra)


def img(p):
    return "file://" + os.path.join(HERE, "img", p)


def cover():
    """Portada a sang: il·lustració a tota la pàgina i títol a sobre (sense marges ni escala)."""
    bars = "".join(f'<i style="background:{COL[n]}"></i>' for n in range(1, 7))
    css = """@page{size:A4;margin:0}html,body{margin:0;height:297mm}
.cvf{position:relative;width:210mm;height:297mm;overflow:hidden;background:#cfe6f3}
.cvf>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 0%}
.cvf .t{position:absolute;top:16mm;left:14mm;right:80mm}
.cvf .lv{display:inline-block;background:#1f2328;color:#fff;font-weight:700;font-size:15pt;letter-spacing:.06em;border-radius:2.5mm;padding:1.6mm 4.5mm}
.cvf h1{font-size:50pt;line-height:.95;margin:4mm 0 2.5mm;color:#fff;letter-spacing:-.01em;text-shadow:0 .8mm 0 rgba(20,60,110,.45),0 0 6mm rgba(20,60,110,.35)}
.cvf .s{font-size:17pt;font-weight:700;color:#1f2328;background:rgba(255,255,255,.78);display:inline-block;border-radius:2mm;padding:1.2mm 3.5mm}
.cvf .bars{display:flex;gap:1.6mm;margin-top:5mm}.cvf .bars i{width:14mm;height:3mm;border-radius:1.5mm;display:block}
.cvf .b{margin-top:3.5mm;width:78mm;background:rgba(255,255,255,.82);border-radius:3mm;padding:2.5mm 4mm;display:grid;gap:3mm;font-size:10pt}
.cvf .b span{display:flex;gap:2.5mm;align-items:flex-end}.cvf .b span i{flex:1;border-bottom:1pt solid #1f2328;height:1.2em}
.cvf .au{margin-top:3mm;font-size:8.5pt;font-weight:700;color:#fff;text-shadow:0 0 2mm rgba(20,50,90,.8);line-height:1.35}.cvf .ft{position:absolute;right:8mm;bottom:5mm;font-size:8pt;color:#fff;text-shadow:0 0 2mm rgba(0,0,0,.6);text-align:right;line-height:1.35}"""
    return page_html(0, f'<div class="cvf"><img src="file://{os.path.join(HERE, "img", "portada-llibre.jpg")}">'
                        f'<div class="t"><span class="lv">3r d\'ESO</span><h1>Física<br>i química</h1><div class="s">Sis reptes per entendre el món</div><div class="bars">{bars}</div>'
                        f'<div class="b"><span>Nom <i></i></span><span>Grup <i></i></span></div></div>'
                        '</div>', css)


def howto():
    cols = "".join(f'<div class="ico" style="background:{COL[n]}">SdA {n}</div><div><b>{SD[n]["title"]}</b> · {SDJ[n]["q"]}</div>' for n in range(1, 7))
    return page_html(0, '<div class="top"><span class="tag">Abans de començar</span><h1>Com funciona aquest llibre</h1></div>'
        '<p>Aquest llibre té sis <b>situacions d\'aprenentatge (SdA)</b>. Cadascuna comença amb un <b>repte</b> real: per respondre\'l, faràs experiments, fitxes, simulacions i un producte final. Cada SdA té un color, que també trobaràs a la pestanya de la vora de les pàgines.</p>'
        f'<div class="legend">{cols}</div>'
        '<h3>Què hi trobaràs</h3><div class="legend">'
        '<div class="ico" style="background:#3B4A5C">Full de ruta</div><div>Al principi de cada SdA. En acabar cada sessió hi escrius què has fet i què has après.</div>'
        '<div class="ico" style="background:#7A8594">Fitxes i labs</div><div>Es fan a classe en paper, sovint primer sol, després en parella i després en grup (1-2-4). Corregeix-les amb <b style="color:#1b6b3a">bolígraf verd</b>, sense esborrar.</div>'
        '<div class="ico" style="background:#B4570F">Píndola</div><div>Pàgina d\'informació amb la idea clau, un exemple resolt i els errors més freqüents. Llegeix-la abans de la fitxa i torna-hi quan estudiïs.</div>'
        '<div class="ico" style="background:#1F5FA8">Digital</div><div>Quan una activitat necessita l\'ordinador (una simulació, un vídeo, un full de càlcul o un laboratori virtual), hi trobaràs un <b>codi QR</b>. Escaneja\'l o escriu l\'adreça.</div>'
        '<div class="ico" style="background:#6B7280">Repte +</div><div>Al final de cada SdA, problemes d\'ampliació per a qui vulgui anar més enllà.</div></div>'
        '<h3>El llibre també és en línia</h3><div style="display:grid;grid-template-columns:auto 1fr auto 1fr;gap:4mm;align-items:center">'
        f'{qr(B, 24)}<div><b>Llibre web</b><br>llibrefiq3r.cat<br><span class="small">Totes les sessions i els fulls en PDF</span></div>'
        f'{qr(B + "digital/", 24)}<div><b>Llibre digital</b><br>llibrefiq3r.cat/digital<br><span class="small">Les fitxes en línia, amb el codi que et donarà el professor</span></div></div>'
        '<p class="small" style="margin-top:5mm">Llibre creat per Macià Esteve Pallarès Pallarès · Institut Anna Gironella de Mundet · Curs 2026-2027</p>')


def opener(n):
    import gen_annexos as A
    sec = A.section(n)
    objs = A.bullets_after(sec, "**Objectius d'aprenentatge.**")
    ses = "".join(f"<li>{H.escape(x['t'])}</li>" for x in SDAS[n - 1]["sessions"])
    return page_html(n, f'<div class="op"><img src="{img(f"coberta-sda{n}.webp")}"><div class="num">Situació d\'aprenentatge {n}</div>'
        f'<h1>{SD[n]["title"] if n != 5 else "Cèl·lules immunitàries a la caça dels patògens"}</h1><div class="rep">{SDJ[n]["q"]}</div>'
        f'<div class="cols"><div><h3>Què aprendràs</h3><ul>{"".join(f"<li>{A.md_inline(x)}</li>" for x in objs)}</ul>'
        f'<h3>Producte final</h3><p>{A.field(sec, "Producte final")}</p></div>'
        f'<div><h3>Sessions</h3><ol>{ses}</ol></div></div></div>')


def resources(n):
    items = []; seen = set()
    for i, x in enumerate(SDAS[n - 1]["sessions"], 1):
        for k in x["l"]:
            if k in seen: continue
            seen.add(k)
            items.append((i, LL[k]["l"], url_l(k)))
    if n == 5:
        items.append((11, "Laboratori virtual de forces de tracció (fitxa digital)", B + "digital/#fitxa-d5tfm"))
    cards = "".join(f'<div class="qri">{qr(u, 30)}<div class="t">{H.escape(t)}</div><div class="s">Sessió {s}</div><div class="u">{H.escape(u.replace("https://", ""))}</div></div>' for s, t, u in items)
    return page_html(n, f'<div class="top"><span class="tag">Digital</span><span class="s" style="font-size:9pt;font-weight:700;color:var(--acc)">SdA {n}</span><h1>Recursos digitals de la SdA</h1></div>'
        '<p>Aquestes activitats necessiten l\'ordinador o el mòbil del centre. Escaneja el codi QR o escriu l\'adreça. Les fitxes de la SdA també es poden fer en línia al <b>llibre digital</b> (llibrefiq3r.cat/digital), quan el professor ho indiqui.</p>'
        f'<div class="qrg">{cards}</div>')


def tfm_page():
    rows = "".join(f"<tr><td>{c}</td><td></td><td></td><td></td></tr>" for c in "ABCDEF")
    return page_html(5, '<div class="top"><span class="tag">Activitat digital</span><span style="font-size:9pt;font-weight:700;color:var(--acc)">SdA 5 · Sessió 11</span><h1>Les cèl·lules també fan forces: microscòpia de forces de tracció</h1></div>'
        '<div style="display:grid;grid-template-columns:auto 1fr;gap:6mm;align-items:center">' + qr(B + "digital/#fitxa-d5tfm", 42) +
        '<div><p>Aquesta activitat <b>no es pot fer en paper</b>: cal superposar dues imatges de microscòpia (abans i després que la cèl·lula estiri el gel) i mesurar el desplaçament de les boletes fluorescents. Fes-la al <b>llibre digital</b>:</p>'
        '<p style="font-size:12pt"><b>llibrefiq3r.cat/digital</b> → SdA 5 → <b>Full de forces cel·lulars</b></p>'
        '<p class="small">Si el professor us dona les làmines A (paper) i B (acetat), també la podeu fer a classe amb les làmines.</p></div></div>'
        '<h3>Què faràs</h3><ol><li>Alinea les dues làmines fent coincidir les creus de les cantonades.</li><li>Mesura amb el regle quant s\'ha desplaçat cada boleta (A–F) i passa-ho a micròmetres amb l\'escala.</li><li>Calcula la força amb la llei de Hooke del gel (F = k · Δx) i dibuixa el vector de cada força.</li><li>Observa cap on apunten les forces: totes van cap al centre de la cèl·lula?</li></ol>'
        '<h3>Anota aquí els resultats</h3><table><tr><th>Boleta</th><th>Desplaçament mesurat (mm)</th><th>Desplaçament real (µm)</th><th>Força</th></tr>' + rows + '</table>'
        '<h3>Què en conclous?</h3>' + G.lines(5))


def notes(n):
    return page_html(n, '<div class="top"><span class="tag">Notes</span><h1>Les meves notes</h1></div><div class="notes">' + G.lines(28) + "</div>")


def index(entries):
    rows = ""
    for e in entries:
        if e[0] == "h":
            rows += f'<div class="h" style="background:{e[2]}">{H.escape(e[1])}</div>'
        else:
            rows += f'<div class="r"><span>{H.escape(e[1])}</span><i>{e[2]}</i></div>'
    return page_html(0, '<div class="top"><span class="tag">Índex</span><h1>Què hi ha en aquest llibre</h1></div>' + f'<div class="idx">{rows}</div>')


def render_all(pages):
    """pages: llista de (nom, html) → PDF a TMP; retorna {nom: camí}"""
    out = {}
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for nom, h in pages:
            path = os.path.join(TMP, nom + ".html"); open(path, "w", encoding="utf-8").write(h)
            pg.goto("file://" + path)
            try:
                pg.wait_for_function('document.body.dataset.math==="ok"', timeout=8000)
            except Exception:
                pass
            pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(250)
            pdf = os.path.join(TMP, nom + ".pdf")
            pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True)
            out[nom] = pdf
        br.close()
    return out


# ------------------------------------------------------------------ pla del llibre
def plan():
    """Llista d'elements: (tipus, nom, sda, etiqueta per a l'índex, fitxer o None, clau de recursos?)"""
    items = [("own", "cover", 0, None), ("own", "howto", 0, "Com funciona aquest llibre"), ("own", "index", 0, "Índex"),
             ("pdf", "dc0", 0, "Sessió 0 · Què en sé de física i química?")]
    for s in SDAS:
        n = s["n"]
        items.append(("own", f"op{n}", n, f"Portada i repte"))
        items.append(("own", f"res{n}", n, "Recursos digitals (codis QR)"))
        placed = set()
        # full de ruta i rúbriques primer
        ks = [k for x in s["sessions"] for k in x["d"] if not D[k].get("t")]
        first = [k for k in ks if "full-de-ruta" in D[k]["f"]] + [k for k in ks if "rubriques" in D[k]["f"]]
        for k in first:
            items.append(("pdf", k, n, D[k]["l"])); placed.add(k)
        for i, x in enumerate(s["sessions"], 1):
            for k in x["d"]:
                if D[k].get("t") or k in placed:
                    continue
                for p in PI.P:
                    if p["n"] == n and p["before"] == k:
                        items.append(("pin", PI.P.index(p), n, "Píndola · " + p["title"]))
                if k in NOMES_DIGITAL:
                    items.append(("own", "tfm", n, "Forces cel·lulars (activitat digital)"))
                else:
                    items.append(("pdf", k, n, D[k]["l"] + (f" (sessió {i})" if not D[k]["l"].startswith(("Mapa", "Diana")) else "")))
                placed.add(k)
        # píndoles que no han trobat lloc
        for p in PI.P:
            if p["n"] == n and p["before"] not in placed:
                print("  píndola sense lloc:", p["title"])
        items.append(("amp", AMPL[n], n, "Repte + · Problemes d'ampliació"))
    items += [("pdf", "dcT", 0, "Sessió de tancament"), ("pdf", "dcF", 0, "Formulari del curs"), ("pdf", "dcG", 0, "Glossari del curs")]
    return items


def src_path(it):
    t, k = it[0], it[1]
    if t == "pdf":
        return os.path.join(SITE, D[k]["f"])
    if t == "amp":
        return os.path.join(SITE, k)
    return None


# ------------------------------------------------------------------ muntatge
MM = 72 / 25.4
W, Hh = 595.28, 841.89
S = 0.972                     # escala del contingut
INNER, CLIP = 18 * MM, 812     # marge interior (espiral) i retall del peu antic


def place(dst, src, pno, odd, own):
    sp = src[pno]
    r = sp.rect
    page = dst.new_page(width=W, height=Hh)
    if r.width > r.height:   # full apaïsat: girat dins de l'àrea útil
        area = pymupdf.Rect(INNER if odd else 10 * MM, 10 * MM, W - (10 * MM if odd else INNER), Hh - 16 * MM)
        page.show_pdf_page(area, src, pno, clip=pymupdf.Rect(0, 0, r.width, r.height - 24), rotate=90)
        return page
    clip = pymupdf.Rect(0, 0, r.width, CLIP)
    x0 = (INNER - 32 * S) if odd else (W - INNER - 563 * S)
    y0 = 8
    page.show_pdf_page(pymupdf.Rect(x0, y0, x0 + r.width * S, y0 + CLIP * S), src, pno, clip=clip)
    return page


def deco(page, num, n, odd, label, digital_page=None):
    col = COL.get(n, NEUTRE)
    rgb = tuple(int(col[i:i + 2], 16) / 255 for i in (1, 3, 5))
    # pestanya de color a la vora exterior
    if n:
        y = 28 * MM + (n - 1) * 24 * MM
        rect = pymupdf.Rect(W - 7 * MM, y, W, y + 20 * MM) if odd else pymupdf.Rect(0, y, 7 * MM, y + 20 * MM)
        page.draw_rect(rect, color=None, fill=rgb)
        cx = rect.x0 + 3.5 * MM - 3
        page.insert_text((cx, rect.y0 + 11 * MM), str(n), fontname="hebo", fontsize=11, color=(1, 1, 1))
    # peu: número a la vora exterior, nom de la SdA a la interior
    yb = Hh - 9 * MM
    ns = str(num)
    if odd:
        page.insert_text((W - 12 * MM - pymupdf.get_text_length(ns, "hebo", 10), yb), ns, fontname="hebo", fontsize=10, color=rgb)
        page.insert_text((INNER, yb), label, fontname="helv", fontsize=8, color=(.42, .45, .5))
    else:
        page.insert_text((12 * MM, yb), ns, fontname="hebo", fontsize=10, color=rgb)
        page.insert_text((W - INNER - pymupdf.get_text_length(label, "helv", 8), yb), label, fontname="helv", fontsize=8, color=(.42, .45, .5))
    if digital_page:
        t = f"Recursos digitals d'aquesta sessió: codis QR a la pàgina {digital_page}"
        x = (W - pymupdf.get_text_length(t, "helv", 7.5)) / 2
        page.insert_text((x, yb + 3.6 * MM), t, fontname="helv", fontsize=7.5, color=(.12, .37, .66))


def build():
    items = plan()
    # render pàgines pròpies i píndoles
    own = [("cover", cover()), ("howto", howto()), ("tfm", tfm_page())]
    own += [(f"op{n}", opener(n)) for n in range(1, 7)] + [(f"res{n}", resources(n)) for n in range(1, 7)]
    own += [(f"notes{n}", notes(n)) for n in range(0, 7)]
    pins = []
    for i, p in enumerate(PI.P):
        use(p["n"]); pins.append((f"pin{i}", PI.html(p)))
    R = render_all(own + pins)
    for nom, _ in pins:
        c = pymupdf.open(R[nom]).page_count
        if c > 1:
            print("  ATENCIÓ: píndola de", c, "pàgines:", nom)
    # sessions amb recursos digitals → avís al peu dels seus fulls
    dig_keys = {}
    for s in SDAS:
        for x in s["sessions"]:
            if x["l"]:
                for k in x["d"]:
                    dig_keys[k] = s["n"]
    IDX_PAGES = 2

    def layout():
        seq = []   # (src_pdf_path, pno, sda, label, index_label, kind, key)
        for it in items:
            t, k, n, lab = it
            if t == "own" and k == "index":
                for j in range(IDX_PAGES):
                    seq.append(("INDEX", j, 0, "Índex", lab if j == 0 else None, "own", k))
                continue
            if t == "own" and k.startswith("op"):
                # cada SdA comença en pàgina senar
                if len(seq) % 2 == 1:
                    seq.append((R[f"notes{n - 1 if n > 1 else 0}"], 0, n - 1, "Notes", None, "own", "notes"))
            path = R[k] if t == "own" else (R[f"pin{k}"] if t == "pin" else src_path(it))
            cnt = pymupdf.open(path).page_count
            for j in range(cnt):
                seq.append((path, j, n, SD[n]["title"] if n else "Física i química · 3r ESO", lab if j == 0 else None, t, k))
        if len(seq) % 2 == 1:
            seq.append((R["notes0"], 0, 0, "Notes", None, "own", "notes"))
        return seq

    seq = layout()
    # números de pàgina de cada recurs digital i índex
    respage = {}
    for i, e in enumerate(seq):
        if e[5] == "own" and str(e[6]).startswith("res"):
            respage[int(e[6][3:])] = i + 1
    entries = []; cur = None
    for i, e in enumerate(seq):
        if not e[4] or e[6] in ("cover", "index"):
            continue
        n = e[2]
        if n != cur:
            cur = n
            entries.append(("h", f"SdA {n} · {SD[n]['title']}" if n else "Curs", COL.get(n, NEUTRE)))
        entries.append(("r", e[4], i + 1))
    # el bloc «Curs» final (tancament, formulari, glossari) també surt amb capçalera
    R["INDEX"] = render_all([("index", index(entries))])["index"]
    ic = pymupdf.open(R["INDEX"]).page_count
    if ic != IDX_PAGES:
        print("  l'índex ocupa", ic, "pàgines; ajusta IDX_PAGES")
    # muntatge final
    dst = pymupdf.open(); cache = {}
    for i, e in enumerate(seq):
        path, pno, n, lab = e[0], e[1], e[2], e[3]
        path = R["INDEX"] if path == "INDEX" else path
        if path not in cache:
            cache[path] = pymupdf.open(path)
        src = cache[path]
        if pno >= src.page_count:   # índex més curt del previst
            page = dst.new_page(width=W, height=Hh)
        elif e[6] == "cover":
            page = dst.new_page(width=W, height=Hh)
            page.show_pdf_page(page.rect, src, pno)
        else:
            odd = (i % 2 == 0)
            page = place(dst, src, pno, odd, e[5] == "own")
        num = i + 1
        if e[6] == "cover":
            continue
        dp = respage.get(n) if (e[5] == "pdf" and e[6] in dig_keys and pno == 0) else None
        deco(page, num, n, num % 2 == 1, (f"SdA {n} · " if n else "") + lab, dp)
    final = os.path.join(OUT, "llibre-fq3-alumnat.pdf")
    dst.save(final, garbage=4, deflate=True)
    print("pàgines:", dst.page_count, "→", final)
    return final


if __name__ == "__main__":
    build()
