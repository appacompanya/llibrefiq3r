"""Annexos de la programació: fitxa resum de cada SdA (1 pàgina) + sondeig, enquesta i rúbrica de recuperació."""
import os, re, sys, json, subprocess
import gen_sda1 as G
from mn_common import SD, use
from playwright.sync_api import sync_playwright

SCR = "/tmp/claude-0/-home-claude/ab93dd98-bb64-5312-88e5-d8a23c91bc1c/scratchpad"
MD = open(os.path.join(SCR, "prog/full.md"), encoding="utf-8").read()
for a, b in [("Prova escrita amb situacions noves", "Activitat de demostració d'assoliment amb situacions noves"), ("| 12 · Prova |", "| 12 · Demostració d'assoliment |"),
             ("· Prova |", "· Demostració d'assoliment |"), ("Prova (qualificadora)", "Activitat de demostració (evidència d'assoliment)"),
             ("Prova competencial", "Activitat de demostració d'assoliment"), ("qualificadora", "evidència d'assoliment"), ("qualificador", "evidència d'assoliment"),
             ("Qualificador", "D'assoliment"), ("esmena de la prova", "esmena de l'activitat de demostració"), ("de la prova", "de l'activitat de demostració"), (" prova", " activitat de demostració")]:
    MD = MD.replace(a, b)
import re as _re
MD = MD.replace("| Fotografia estroboscòpica d'un cotxe", "| Reactivació després de Setmana Santa. Fotografia estroboscòpica d'un cotxe").replace("Reactivació (15 min). Acceleració", "Acceleració")
MD = MD.replace("Fitxa per a l'alumne amb PI (", "Fitxa amb suport manipulatiu per a l'alumnat amb NESE que ho necessita (")
MD = _re.sub(r"\| (\d+) · Prova \|", r"| \1 · Demostració d'assoliment |", MD)
# La seqüència de la SdA 5 ja és la del web (6 problemes, 7 difusió en grup sencer, 8 quimiotaxi). No es reordena.
DATA = {d["n"]: d for d in json.load(open(os.path.join(SCR, "sdas.json"), encoding="utf-8"))}
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib"))
import imatges as IM
IMG = IM.DIR  # una sola còpia de cada imatge (img/ de l'arrel)

def md_inline(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)

def section(n):
    a = MD.index(f"### 5.{n} SdA {n}")
    b = MD.find("### 5.", a + 10)
    if b < 0:
        b = MD.index("## 6.", a)
    return MD[a:b]

def tables(sec):
    out, cur = [], []
    for line in sec.splitlines():
        if line.startswith("|"):
            cur.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif cur:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return [[r for r in t if not set("".join(r)) <= set("- ")] for t in out]

def field(sec, name):
    m = re.search(r"\*\*" + name + r"\.\*\* (.+)", sec)
    return md_inline(m.group(1)) if m else ""

def bullets_after(sec, label):
    a = sec.index(label)
    lines = []
    for line in sec[a:].splitlines()[1:]:
        if re.match(r"^(\d+\.|-) ", line.strip()):
            lines.append(re.sub(r"^(\d+\.|-) ", "", line.strip()))
        elif lines and not line.strip():
            break
        elif lines:
            break
    return lines

CSS = """
@page{size:A4;margin:11mm 13mm 11mm}
body, body *:not(.katex):not(.katex *){font-family:Arial,"Liberation Sans",Helvetica,sans-serif !important}
body{font-size:11pt;line-height:1.5}
.head{margin-bottom:1.5mm;padding-bottom:1.2mm}h1{font-size:14pt;line-height:1.2}.kick{font-size:9pt}
.rep{font-size:11pt;font-weight:700;margin:0;line-height:1.35}.meta{font-size:9pt;color:var(--muted);margin:.5mm 0 1.5mm;line-height:1.3}
table{font-size:9pt;line-height:1.22;margin:0 0 1.5mm;width:100%}th,td{padding:.55mm 1.3mm;vertical-align:top}
td.k{width:27mm;font-weight:700;color:var(--acc)}
.g{font-weight:700;font-size:9pt;border-radius:1mm;padding:0 1mm;white-space:nowrap}.gs{background:#eef0f2}.mg{background:var(--tint);color:var(--acc)}
a{color:inherit;text-decoration:none}td a.s{color:var(--acc);font-weight:700;text-decoration:underline;text-decoration-thickness:.4px}
.st{color:var(--acc);font-weight:700}
.uf{font-size:9pt !important}p.nt{font-size:9pt;line-height:1.3;margin:0;color:var(--muted)}p.nt a{color:var(--acc);text-decoration:underline}
"""

FASE = {"Exploració": "Inicial", "Introducció de nous coneixements": "Desenvolupament", "Estructuració i síntesi": "Estructuració", "Avaluació i regulació": "Avaluació"}


def page_sda(n, annex, tight=0):
    use(n)
    sec = section(n)
    tb = tables(sec)
    seq, ev = tb[0], tb[1]
    d = DATA[n]
    rows = ""
    for i, r in enumerate(seq[1:], 1):
        g = r[1]
        num, _, tit = md_inline(r[0]).partition(" · ")
        star = ' <span class="st">★</span>' if "evidència d'assoliment" in r[4] else ""
        rows += (f'<tr><td><a class="s" href="https://llibrefiq3r.cat/#sda{n}-s{i}">{num} · {tit}</a></td>'
                 f'<td><span class="g {"mg" if g=="MG" else "gs"}">{g}</span></td><td>{FASE.get(r[2], r[2])}</td><td>{md_inline(r[3])}{star}</td></tr>')
    seqt = (f'<table><tr><th style="width:27%">Sessió (enllaç al llibre)</th><th>Grup</th><th>Tipus</th><th>Què fem</th></tr>{rows}</table>')
    evs = " · ".join(f"{md_inline(r[0])} ({r[3]})" for r in ev[1:] if r[1].startswith("D'assoliment"))
    objs = bullets_after(sec, "**Objectius d'aprenentatge.**")
    elems = bullets_after(sec, "**Elements curriculars.**")
    crit = md_inline(elems[0]).replace("Criteris: ", "")
    sab = md_inline(elems[1]).replace("Sabers: ", "")
    vec = md_inline(elems[2]).replace("Vectors i ODS: ", "") if len(elems) > 2 else ""
    info = (f'<table><tr><td class="k">Criteris</td><td>{crit}</td></tr>'
            f'<tr><td class="k">Sabers</td><td>{sab}</td></tr>'
            + (f'<tr><td class="k">Vectors i ODS</td><td>{vec}</td></tr>' if vec and tight < 2 else "")
            + f'<tr><td class="k">Objectius</td><td>{" ".join(f"<b>O{k}</b> {md_inline(x)}" for k, x in enumerate(objs, 1))}</td></tr>'
            f'<tr><td class="k">Producte final</td><td>{field(sec, "Producte final")}</td></tr>'
            f'<tr><td class="k">Evidències d\'assoliment (criteris)</td><td>{evs}</td></tr>'
            f'<tr><td class="k">Atenció a la diversitat</td><td>{field(sec, "Atenció a la diversitat")}</td></tr></table>')
    title = SD[n]["title"] if n != 5 else "Cèl·lules immunitàries a la caça dels patògens"
    body = (f'<div class="head"><div><div class="kick">Annex {annex} · Fitxa resum de la SdA {n}</div><h1>{title}</h1></div>'
            f'<div class="who"><span style="justify-content:flex-end;font-weight:700;color:var(--acc);font-size:9pt">Programació FQ 3r ESO</span></div></div>'
            f'<p class="rep">Repte: {d["q"]}</p><p class="meta">{d["meta"]}</p>'
            f'{info}{seqt}'
            f'<p class="nt"><span class="st">★</span> Sessió amb evidència d\'assoliment. Cada evidència es valora amb NA, AS, AN o AE; el nivell de cada CE és la mitjana (1–4) arrodonida a l\'alça. '
            f'Tots els fulls de la SdA: <a href="https://llibrefiq3r.cat/#sda{n}">llibrefiq3r.cat/#sda{n}</a> · fitxes en línia: <a href="https://llibrefiq3r.cat/digital/">llibrefiq3r.cat/digital</a>.</p>')
    extra = ""
    if tight >= 1:
        extra += "th,td{padding:.35mm 1.1mm}table{line-height:1.17}"
    return G.page(body, CSS + extra)

if __name__ == "__main__":
    out = os.path.join(SCR, "annex")
    MO = os.path.join(out, "mostres")
    os.makedirs(out, exist_ok=True)
    parts = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for n in range(1, 7):
            for tight in range(3):
                html = page_sda(n, n, tight)
                path = os.path.join(out, f"a{n}.html"); open(path, "w", encoding="utf-8").write(html)
                pg.goto("file://" + path); pg.wait_for_function('document.body.dataset.math==="ok"', timeout=8000); pg.wait_for_timeout(300)
                pdf = os.path.join(out, f"a{n}.pdf")
                pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True)
                pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
                if pages == 1:
                    break
            print("SdA", n, "pàgines", pages, "tight", tight)
            parts.append(pdf)
        br.close()
    subprocess.run(["python3", "annex_samples.py", "ruta5", "sondeig", "tanc", "rub2", "recup1", "basic"], check=True)
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    D = os.path.join(G.ROOT, "docs")
    EX = os.path.join(G.ROOT, "annex", "annex-extra.pdf")
    CAL = os.path.join(G.ROOT, "annex", "calendari.pdf")
    mo = lambda nm: os.path.join(MO, nm + ".pdf")
    plan = [(parts[i], None, i + 1) for i in range(6)] + [
        (mo("ruta5"), None, 7), (mo("sondeig"), [0], 8), (mo("tanc"), None, 9), (mo("rub2"), [0], 10),
        (CAL, [0], 11), (EX, [0], 12), (EX, [1], 13), (EX, [2], 14),
        (mo("basic"), [0], 15), (EX, [3], 16), (mo("recup1"), [0, 3], 17),
    ]
    w = PdfWriter()
    for src, idx, num in plan:
        r = PdfReader(src)
        for k in (idx if idx is not None else range(len(r.pages))):
            pgo = r.pages[k]
            W_, H_ = float(pgo.mediabox.width), float(pgo.mediabox.height)
            stamp = os.path.join(out, "stamp.pdf")
            c = canvas.Canvas(stamp, pagesize=(W_, H_))
            c.setFillColor(HexColor("#1F4E79")); c.roundRect(W_ - 82, H_ - 23, 68, 16, 4, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF")); c.setFont("Helvetica-Bold", 9); c.drawCentredString(W_ - 48, H_ - 18, f"ANNEX {num}")
            c.save()
            pgo.merge_page(PdfReader(stamp).pages[0])
            w.add_page(pgo)
    final = os.path.join(D, "programacio-annexos.pdf")
    with open(final, "wb") as fh:
        w.write(fh)
    print("pages", len(w.pages))
