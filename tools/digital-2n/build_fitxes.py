"""Converteix l'HTML reconstruït dels fulls de 2n (pdf2html.py → _html/) en fitxes digitals.
Adaptació de build_fitxes_auto.py del llibre de 3r: mateixes regles (línies → resposta, cel·les buides → camps,
requadres de dibuix → foto, caselles → checkbox, diana → valoració 1-4).
Sortida: ../../2n/digital/js/fitxes-auto.js
Ús: python3 pdf2html.py && python3 build_fitxes.py"""
import os, re, sys, json
from bs4 import BeautifulSoup, NavigableString

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
OUTJS = os.path.join(ROOT, "2n", "digital", "js", "fitxes-auto.js")
TMP = os.path.join(HERE, "_html")
tpl = open(os.path.join(ROOT, "2n", "index.html"), encoding="utf-8").read()
DD = json.loads(re.search(r"^const D = (\{.*?\});$", tpl, re.M).group(1))
D = {k: (v["f"], bool(v.get("t"))) for k, v in DD.items()}
SKIP_KEYS = set()
SKIP_FILE = re.compile(r"mapa-conceptual|rubriques|formulari|glossari|enquesta|lamines|solucionari|prova|adaptada|equivalencies")

def extra_widgets(key, body):
    pass

DRAW = re.compile(r"\b(pinta|esbós|representeu|dibuixa|dibuixeu|dibuix|esquema|representa gràficament|enganxa|fes la gràfica|dibuixa la gràfica|construeix la gràfica|traça)", re.I)
GRAPH = re.compile(r"\b(Representa (la|les|el|els) |Dibuixa la gràfica|fes (la|una) gràfica|construeix (la|una) gràfica|fes un dibuix|fes un esquema)", re.I)

out = {}

def text(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True))

for key, (fn, teacher) in D.items():
    if teacher or key in SKIP_KEYS or SKIP_FILE.search(fn): continue
    path = os.path.join(TMP, key + ".html")
    if not os.path.exists(path): continue
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    body = soup.body
    for bd in body.select(".head h1 .badge"): bd.decompose()
    title = DD[key]["l"] if key in DD else (text(body.select_one(".head h1")) if body.select_one(".head h1") else key)
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
                        vf = ci < len(hdr) and (re.fullmatch(r"V\s*/\s*F|T\s*/\s*F|Sí\s*/\s*no", hdr[ci] or "", re.I) or
                                                (2 <= len(hdr[ci].split(" / ")) <= 4 and all(0 < len(x.strip()) <= 22 for x in hdr[ci].split(" / "))))
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
            if False:
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
