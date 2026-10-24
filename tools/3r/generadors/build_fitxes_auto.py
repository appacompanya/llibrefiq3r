"""Converteix els fulls de l'alumnat (HTML dels generadors) en fitxes digitals per al llibre digital.
Sortida: ../llibrefiq3r/digital/js/fitxes-auto.js i ../llibrefiq3r/digital/fimg/ (imatges).
Regles: línies -> resposta (text + equacions + factors de conversió); cel·les buides de taula -> camps;
requadres de dibuix i preguntes que demanen dibuixar -> pujar foto; caselles de verificació -> checkbox;
diana -> valoració 1-4 amb diana dinàmica."""
import os, re, sys, json, shutil, importlib, subprocess
from bs4 import BeautifulSoup, NavigableString

HERE = os.path.dirname(os.path.abspath(__file__))
OUTJS = os.path.join(HERE, "..", "llibrefiq3r", "digital", "js", "fitxes-auto.js")
IMGDIR = os.path.join(HERE, "..", "llibrefiq3r", "digital", "fimg")
TMP = os.path.join(HERE, "_html_fitxes")

# ---- mapa clau -> fitxer (del llibre) ----
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
D = {k: (f, bool(t)) for k, f, t in re.findall(r'(\w+):\s*\{f:"([^"]+)"[^}]*?(t:1)?\}', tpl)}
SKIP_KEYS = {"d1f1", "d1f2", "d1ellen", "dcF", "dcG", "dcE", "dannex"}
SKIP_FILE = re.compile(r"mapa-conceptual|rubriques|formulari|glossari|enquesta|lamines|solucionari|prova|model-de-mobil|targetes")

# ---- genera l'HTML de cada full ----
os.makedirs(TMP, exist_ok=True)
dump = r'''
import sys, os, importlib
sys.path.insert(0, %r); os.chdir(%r)
mod = importlib.import_module(sys.argv[1])
for row in mod.DOCS:
    fn, f = (row[1], row[2]) if len(row) == 3 else row
    try: html, _ = f()
    except Exception as e: print("ERR", fn, e); continue
    open(os.path.join(%r, fn.replace(".pdf", ".html")), "w").write(html)
''' % (HERE, HERE, TMP)
for m in ["gen_detectius", "gen_sda1", "gen_mobil", "gen_hidrogen", "gen_cel", "gen_energia", "gen_curs", "gen_multinivell"]:
    subprocess.run([sys.executable, "-c", dump, m], check=True, cwd=HERE)


# ---- eines digitals que substitueixen el material manipulatiu ----
sys.path.insert(0, HERE)
import gen_cel, gen_mobil

def _frag(html):
    return BeautifulSoup(html, "html.parser")

def extra_widgets(key, body):
    if key in ("d5f4", "d5tfm"):
        for sv in body.find_all("svg"):
            w = (sv.get("width") or "")
            vb = (sv.get("viewBox") or sv.get("viewbox") or "").split()
            if w.endswith("mm") and len(vb) == 4 and abs(float(vb[2]) - float(w[:-2])) < 0.6:
                sv["data-ruler"] = "1"
    if key == "d5tfm":
        cfg = {"sc": gen_cel.SC, "cell": [gen_cel.CELL_C[0], gen_cel.CELL_C[1], 11.5, 9],
               "field": [[round(x, 3), round(y, 3)] for x, y in gen_cel.bead_field()],
               "marked": {n: [x, y, dx, dy] for n, ((x, y), (dx, dy)) in gen_cel.BEADS.items()}}
        tips = body.find_all("div", class_="tip")
        anchor = tips[1] if len(tips) > 1 else tips[0]
        anchor.insert_after(_frag('<div class="tip"><b>Al llibre digital.</b> En lloc del paper (làmina A) i l\'acetat (làmina B), fes servir el laboratori virtual: arrossega la làmina B fins que coincideixin les creus i, amb el regle, dibuixa la fletxa de cada boleta verda fins a la mateixa boleta magenta. El regle et dona la longitud en mm de la làmina.</div>'
                                 f"<div data-widget=\"tfm\" data-cfg='{json.dumps(cfg)}'></div>"))
    if key == "d3f1":
        cards = ""
        for i, (nom, kind, labs) in enumerate(gen_mobil.PECES):
            cards += (f'<details class="mob"><summary><span class="mobn">{i+1}</span>{nom}</summary><div class="mobb">'
                      f'<div class="mobpic">{gen_mobil.icon(kind, 220, 141)}</div><div class="moblab"><div class="moblt">Etiqueta tècnica</div><ul>'
                      + "".join(f"<li>{x}</li>" for x in labs) + "</ul></div></div></details>")
        css = ("<style>.mobw{border:1px solid #d8dde3;border-radius:12px;padding:10px 12px;background:#fff;margin:10px 0}"
               ".mob{border-top:1px dashed #c9ccd1;padding:6px 0}.mob:first-of-type{border-top:0}.mob summary{cursor:pointer;font-weight:700;display:flex;gap:8px;align-items:center}"
               ".mobn{width:24px;height:24px;border-radius:50%;background:#685AD2;color:#fff;display:inline-grid;place-items:center;font-size:13px}"
               ".mobb{display:grid;grid-template-columns:minmax(120px,220px) 1fr;gap:12px;align-items:start;margin-top:6px}.mobpic svg{width:100%;height:auto}"
               ".moblab{border:1px solid #1f2328;border-radius:8px;padding:8px 10px;font-size:14px}.moblt{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#5d646d}"
               ".moblab ul{margin:4px 0 0;padding-left:18px}@media(max-width:560px){.mobb{grid-template-columns:1fr}}</style>")
        h2 = body.find("h2")
        h2.insert_after(_frag(css + '<div class="mobw"><b>El mòbil desmuntable.</b> Obre cada peça (en l\'ordre en què desmuntaries un mòbil real) i llegeix-ne l\'etiqueta tècnica.' + cards + "</div>"))

DRAW = re.compile(r"\b(pinta|esbós|representeu|dibuixa|dibuixeu|dibuix|esquema|representa gràficament|enganxa|fes la gràfica|dibuixa la gràfica|construeix la gràfica|traça)", re.I)
GRAPH = re.compile(r"\b(Representa (la|les|el|els) |Dibuixa la gràfica|fes la gràfica)")
os.makedirs(IMGDIR, exist_ok=True)
out = {}

def text(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True))

for key, (fn, teacher) in D.items():
    if teacher or key in SKIP_KEYS or SKIP_FILE.search(fn): continue
    path = os.path.join(TMP, fn.replace(".pdf", ".html"))
    if not os.path.exists(path): continue
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    body = soup.body
    for bd in body.select(".head h1 .badge"): bd.decompose()
    title = text(body.select_one(".head h1")) if body.select_one(".head h1") else key
    sub = body.select_one(".head .q2")
    m = re.match(r"sda(\d)", fn); sda = int(m.group(1)) if m else 0
    if "full-de-ruta" in fn: title = "Full de ruta · " + title
    for el in body.select(".head, .pb, .who, .teacher, script, style"): el.decompose()
    extra_widgets(key, body)
    for el in body.find_all(string=re.compile(r"\(continuació\)")):
        par = el.parent
        if par and par.name != "body" and len(text(par)) < 140: par.decompose()
    PLAIN = bool(re.search(r"full-de-ruta|diana|sessio|guio-del-video|pla-de-campanya|registre|seguretat", fn))
    intro = body.select_one("p.intro"); intro_txt = text(intro) if intro else ""
    if intro: intro.decompose()
    if sub: body.insert(0, BeautifulSoup(f'<p class="ws-sub-q"><b>{sub.decode_contents()}</b></p>', "html.parser"))

    fields = {}; qs = {}; n = [0]
    def fid(kind, q, **kw):
        n[0] += 1; i = f"a{n[0]}"; fields[i] = {"k": kind, "q": q, **kw}; return i

    # agrupa cada pregunta amb el contingut que la segueix fins a la propera pregunta o títol
    sec = ""
    nodes = [c for c in list(body.children) if not (isinstance(c, NavigableString) and not c.strip())]
    blocks = []; cur = None
    for c in nodes:
        name = getattr(c, "name", None); cls = c.get("class", []) if name else []
        if name == "h2":
            k = c.select_one(".k"); sec = text(k) if k else ""; cur = None; blocks.append(("raw", c)); continue
        if name == "div" and "q" in cls:
            num = text(c.select_one(".n")) if c.select_one(".n") else str(len(qs) + 1)
            qid = num if num not in qs else f"{sec}{num}"
            while qid in qs: qid += "'"
            qs[qid] = ""
            cur = {"q": qid, "els": [c]}; blocks.append(("q", cur)); continue
        if name == "div" and "tip" in cls: cur = None; blocks.append(("raw", c)); continue
        if cur is not None and name in ("table", "div", "svg", "img", "ol", "ul", "p"):
            cur["els"].append(c); continue
        blocks.append(("raw", c))

    def convert(el, q):
        # línies -> resposta
        cands = el.find_all(lambda t: t.find("div", class_="l", recursive=False) is not None)
        if getattr(el, "find", None) and el.find("div", class_="l", recursive=False) is not None: cands = [el] + cands
        for grp_parent in cands:
            ls = grp_parent.find_all("div", class_="l", recursive=False)
            if not ls: continue
            i = fid("work", q, rows=max(2, len(ls)), **({"plain": 1} if PLAIN else {}))
            ls[0].replace_with(BeautifulSoup(f'<div class="fld" data-fid="{i}"></div>', "html.parser"))
            for x in ls[1:]: x.decompose()
        if el.name == "div" and "l" in el.get("class", []):
            pass
        # taules: cel·les buides -> camps
        for tb in ([el] if el.name == "table" else []) + el.find_all("table"):
            hdr = [text(th) for th in (tb.find("tr").find_all("th") if tb.find("tr") else [])]
            for tr in tb.find_all("tr"):
                for ci, td in enumerate(tr.find_all(["td", "th"])):
                    if td.name == "th": continue
                    if re.fullmatch(r"\w{1,2}", text(td)) and "height" in (td.get("style") or "") and not td.find(["img", "svg", "input"]):
                        i = fid("cell", q); td.append(BeautifulSoup(f' <span class="fld" data-fid="{i}"></span>', "html.parser")); continue
                    if not text(td) and not td.find(["img", "svg", "input"]):
                        vf = ci < len(hdr) and re.fullmatch(r"V\s*/\s*F|T\s*/\s*F|Sí\s*/\s*no", hdr[ci] or "", re.I)
                        i = fid("cell", q, **({"opts": [x.strip() for x in hdr[ci].split("/")]} if vf else {}))
                        td.clear(); td.append(BeautifulSoup(f'<span class="fld" data-fid="{i}"></span>', "html.parser"))
        # requadres: dibuix -> foto; requadre de text -> resposta; requadre amb contingut donat -> igual
        for bx in ([el] if "box" in el.get("class", []) else []) + el.find_all(class_="box"):
            lab = text(bx)
            if "color:var(--ink)" in (bx.get("style") or ""): continue
            draw = bool(DRAW.search(qs.get(q, "") or "")) or bool(DRAW.search(lab))
            i = fid("photo" if draw else "work", q, label=lab, rows=2)
            bx.clear(); bx["class"] = ["box", "boxd" if draw else "boxt"]
            if lab: bx.append(BeautifulSoup(f'<div class="boxl">{lab}</div>', "html.parser"))
            bx.append(BeautifulSoup(f'<div class="fld" data-fid="{i}"></div>', "html.parser"))
        # buits dins del text
        for bl in el.find_all(class_="blank"):
            i = fid("cell", q); bl.replace_with(BeautifulSoup(f'<span class="fld blankf" data-fid="{i}"></span>', "html.parser"))
        # buits amb guions baixos
        for t in list(el.find_all(string=re.compile("_{3,}"))):
            if t.find_parent(["svg", "script", "style"]): continue
            parts = re.split("_{3,}", str(t)); frag = parts[0]
            for ptxt in parts[1:]:
                i = fid("cell", q); frag += f'<span class="fld blankf" data-fid="{i}"></span>' + ptxt
            t.replace_with(BeautifulSoup(frag, "html.parser"))
        # caselles ☐ dins del text
        for t in list(el.find_all(string=re.compile("☐"))):
            parts = re.split("☐", str(t)); frag = parts[0]
            for ptxt in parts[1:]:
                i = fid("check", q); frag += f'<span class="fld" data-fid="{i}"></span>' + ptxt
            t.replace_with(BeautifulSoup(frag, "html.parser"))
        # caselles
        for ck in el.find_all(class_="ck"):
            i = fid("check", q); ck.replace_with(BeautifulSoup(f'<span class="fld" data-fid="{i}"></span>', "html.parser"))
        # imatges locals
        for im in el.find_all("img"):
            src = im.get("src", "")
            if src.startswith("file://"):
                p = src[7:]
                if os.path.exists(p):
                    shutil.copy2(p, os.path.join(IMGDIR, os.path.basename(p))); im["src"] = "fimg/" + os.path.basename(p)
        return el

    html = []
    for kind, b in blocks:
        if kind == "raw":
            el = b
            if getattr(el, "name", None):
                # diana: taula d'aspectes -> valoració 1-4
                if el.name == "table" and "diana" in fn and el.find("th") and text(el.find("th")) == "#":
                    for tr in el.find_all("tr")[1:]:
                        tds = tr.find_all("td")
                        if len(tds) >= 2:
                            i = fid("rate", "diana", label=text(tds[1]))
                            nt = soup.new_tag("td"); nt.append(BeautifulSoup(f'<span class="fld" data-fid="{i}"></span>', "html.parser")); tr.append(nt)
                    th = soup.new_tag("th"); th.string = "1 = encara no · 4 = ho domino"; el.find("tr").append(th)
                    qs["diana"] = "Diana d'autoavaluació"
                    html.append('<section class="ws-block" data-qblock="diana"><div class="radar" data-radar></div>' + str(el) + "</section>"); continue
                if el.name == "svg" and "diana" in fn: continue
                if el.name == "div" and "list" in el.get("class", []):  # full de ruta
                    for card in el.find_all(class_="c", recursive=False):
                        nb = card.select_one(".t .b"); q = text(nb) if nb else str(len(qs) + 1)
                        qs[q] = text(card.select_one("h3")) if card.select_one("h3") else ""
                        convert(card, q); card["data-qblock"] = q
                    html.append(str(el)); continue
                convert(el, "_")
            html.append(str(el)); continue
        q = b["q"]
        qs[q] = text(b["els"][0])[:1200]  # (s'actualitza abans de convertir: el text de dibuix decideix foto)
        inner = []
        for el in b["els"]: inner.append(str(convert(el, q)))
        has_photo = any(f["k"] == "photo" and f["q"] == q for f in fields.values())
        if not has_photo and (DRAW.search(qs[q]) or GRAPH.search(qs[q])):
            i = fid("photo", q, label="Foto del teu dibuix o gràfica")
            inner.append(f'<div class="fld" data-fid="{i}"></div>')
        kinds_q = [f["k"] for f in fields.values() if f["q"] == q]
        if kinds_q and all(k == "photo" for k in kinds_q) and re.search(r"\b(escriu|escriviu|explica|expliqueu|justifica|comenta|digues|respon|descriu|descriviu)|\?", qs[q], re.I):
            i = fid("work", q, rows=3, **({"plain": 1} if PLAIN else {}))
            inner.insert(1, f'<div class="fld" data-fid="{i}"></div>')
        if not any(f["q"] == q for f in fields.values()):
            i = fid("work", q, rows=3, **({"plain": 1} if PLAIN else {}))
            inner.append(f'<div class="fld" data-fid="{i}"></div>')
        html.append(f'<section class="ws-block" data-qblock="{q}">' + "".join(inner) + "</section>")
    if not fields: continue
    out[key] = {"title": title, "sda": sda, "intro": intro_txt, "html": "".join(html), "fields": fields, "qs": {k: v for k, v in qs.items() if any(f["q"] == k for f in fields.values())}, "auto": True}

js = "/* Generat automàticament per build_fitxes_auto.py a partir dels fulls de l'alumnat. No editar a mà. */\nwindow.FITXES = Object.assign(window.FITXES || {}, " + json.dumps(out, ensure_ascii=False) + ");\n"
open(OUTJS, "w", encoding="utf-8").write(js)
print(len(out), "fitxes ·", len(js) // 1024, "KB")
for k, v in out.items():
    kinds = {}
    for f in v["fields"].values(): kinds[f["k"]] = kinds.get(f["k"], 0) + 1
    print(f"  {k:9s} {v['title'][:48]:48s} {kinds}")
