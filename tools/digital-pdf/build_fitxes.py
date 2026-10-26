"""Converteix l'HTML reconstruït dels fulls de 2n o 4t (pdf2html.py → _html/<nivell>/) en fitxes digitals.
Adaptació de build_fitxes_auto.py del llibre de 3r: mateixes regles (línies → resposta, cel·les buides → camps,
requadres de dibuix → foto, caselles → checkbox, diana → valoració 1-4).
Sortida: ../../<nivell>/digital/js/fitxes-auto.js
Ús: python3 pdf2html.py 2n && python3 build_fitxes.py 2n"""
import os, re, sys, json
from bs4 import BeautifulSoup, NavigableString

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from nivell import LEVEL, ROOT, TMP
OUTJS = os.path.join(ROOT, LEVEL, "digital", "js", "fitxes-auto.js")
os.makedirs(os.path.dirname(OUTJS), exist_ok=True)
tpl = open(os.path.join(ROOT, LEVEL, "index.html"), encoding="utf-8").read()
DD = json.loads(re.search(r"^const D = (\{.*?\});$", tpl, re.M).group(1))
D = {k: (v["f"], bool(v.get("t"))) for k, v in DD.items()}
SKIP_KEYS = set()
SKIP_FILE = re.compile(r"mapa-conceptual|rubriques|formulari|glossari|enquesta|lamines|solucionari|prova|adaptada|equivalencies|dossier-de-")

def extra_widgets(key, body):
    pass


# ---------------- widgets adaptats a cada tipus de pregunta ----------------
UT = r"(?:°C|mmHg|kWh|kcal|cal|atm|bar|hPa|kPa|Pa|mol|min|dies|dia|[kKhdcmµn]?(?:m|g|L|s|J|W|N)|h|K|t)[²³]?"
UNIT = UT + r"(?:/" + UT + r")?"
NUM = r"-?\d[\d.]*(?:,\d+)?(?:\s?·\s?10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)?"
QTY = re.compile(r"(?<![\w,.·])(" + NUM + r")\s?(" + UNIT + r")(?![\w/²³])")
TGT = re.compile(r"(?:\b(?:a|en)\s+|passa-ho a\s+)(" + UNIT + r")(?![\w/²³])")
SP = r"(?:\d+\s)?(?:[A-Z][a-z]?[₀-₉]*|\((?:[A-Z][a-z]?[₀-₉]*)+\)[₀-₉]*)+"
EQN = re.compile(r"(" + SP + r"(?:\s*\+\s*" + SP + r")*)\s*→\s*((?:" + SP + r"(?:\s*\+\s*" + SP + r")*)?(?:\s*…)?(?:\s*\+\s*" + SP + r")*)")
CALCV = re.compile(r"\b(calcula|calculeu|quant[ae]?s?|quina|quines|quin|quins|troba|determina|a quina|en quant|quanta)\b", re.I)
CONV = re.compile(r"\bfactors?\b|(?<!li )(?<!què )\bpassa(?:-ho|-la|-les|-los)?\s+(?:a|en)\b|(?<!li )(?<!què )\bpassa a\b|\bpasseu\b|\bexpressa\b|converteix|canvia d'unitat|unitats? del SI", re.I)
CALCQ = re.compile(r"\b(calcula|calculeu|quant[ae]?s?\b|quin(?:a|s|es)? (?:volum|massa|pressió|temperatura|concentració|densitat|velocitat|energia|calor|força|distància|temps|molaritat|percentatge|potència|acceleració|empenta|altura|superfície|cost|preu|rendiment|intensitat)|a quina (?:temperatura|altura|velocitat|profunditat)|de quin (?:metall|material|líquid)|quin pot ser|és d'or|troba|determina)", re.I)
NOCALC = re.compile(r"dissenya|variable|classifica|ordena|hipòtesi|en quin estat|creieu|creus|prediu|marca", re.I)
EXPL = re.compile(r"per què|explica|justifica|raona|què passa|compara|interpreta|conclusió|com ", re.I)

def plain(el):
    """Text pla d'un fragment HTML, amb les unitats apilades (span.uf) escrites com a a/b."""
    frag = BeautifulSoup(str(el), "html.parser")
    for uf in frag.select("span.uf"):
        sp = uf.find_all("span", recursive=False)
        if len(sp) == 2: uf.replace_with(f"{sp[0].get_text()}/{sp[1].get_text()}")
    return re.sub(r"\s+", " ", frag.get_text(" ", strip=True)).replace(" /", "/").replace("/ ", "/")

def num_si(v):
    v = v.replace(" ", "")
    return v.replace(".", "") if re.fullmatch(r"-?\d{1,3}(\.\d{3})+(,\d+)?", v) else v

def split_subs(html):
    """Separa «a) … b) …» (o «a. … b. …») d'un paràgraf. Retorna (intro, [(lletra, html), …]) o None."""
    marks = []; want = "a"; pos = 0
    for m in re.finditer(r"(?:(?<=^)|(?<=[\s>(;:.,]))([a-h])[).]\s", html):
        if m.group(1) == want and m.start() >= pos:
            marks.append(m); want = chr(ord(want) + 1); pos = m.end()
    if len(marks) < 2: return None
    intro = html[:marks[0].start()]
    subs = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(html)
        subs.append((m.group(1), html[m.end():end].strip().rstrip(";").strip()))
    # tanca etiquetes obertes a la introducció (p. ex. <b> sense tancar)
    return BeautifulSoup(intro, "html.parser").decode(), [(l, BeautifulSoup(h, "html.parser").decode()) for l, h in subs]

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


    sn = [0]
    def sfid(kind, q, **kw):
        sn[0] += 1; i = f"s{sn[0]}"; fields[i] = {"k": kind, "q": q, **kw}; return i
    def eq_widget(frag_html, q, ctx):
        """Equació per ajustar: casella per al coeficient davant de cada espècie i, si cal, casella per als productes."""
        txt = plain(frag_html)
        ms = list(EQN.finditer(txt))
        if not ms: return None
        def side(sd):
            out = []
            for sp in [x.strip() for x in sd.split("+") if x.strip()]:
                if sp == "…":
                    i = sfid("cell", q, wide=1, ph="productes"); out.append(f'<span class="fld" data-fid="{i}"></span>'); continue
                mm = re.match(r"(\d+)\s(.+)", sp)
                if mm: out.append(f'<span class="eqc fixed">{mm.group(1)}</span><span class="eqs">{mm.group(2)}</span>')
                else:
                    i = sfid("cell", q, coef=1); out.append(f'<span class="fld" data-fid="{i}"></span><span class="eqs">{sp}</span>')
            return '<span class="eqp">+</span>'.join(out)
        w = ""
        for m in ms:
            lhs, rhs = m.group(1), m.group(2).strip()
            if not rhs or rhs == "…":
                i = sfid("cell", q, wide=1, ph="productes"); R = f'<span class="fld" data-fid="{i}"></span>'
            else: R = side(rhs)
            w += f'<div class="eqw">{side(lhs)}<span class="eqa">→</span>{R}</div>'
        rest = (txt[:ms[0].start()] + " " + txt[ms[-1].end():]).strip(" .;:,")
        return w, rest

    def chain_init(t, ctx):
        """Factors de conversió preparats: quantitat de partida i unitat a què cal passar."""
        if "\\(" in t: return None
        qm = QTY.search(t)
        if not qm: return None
        if qm.group(2) in ("°C", "K") or "×" in t: return None
        tg = [x for x in TGT.findall(t[qm.end():]) if x != qm.group(2) and x not in ("°C", "K")]
        if not tg and not CONV.search(t) and not CONV.search(ctx): return None
        if CALCQ.search(t) and not CONV.search(t): return None
        if not tg and re.search(r"unitats? del SI", ctx, re.I): tg = ["SI"]
        tg = tg or [""]
        return [{"t": "chain", "sv": num_si(qm.group(1)), "su": qm.group(2), "rt": x or "unitat", "lab": "Factors de conversió" + (f" → {x}" if x else "")} for x in tg[:2]]

    def scaffold(t, ctx, sub=False):
        if sub: return [{"t": "math", "lab": "Càlcul"}, {"t": "res", "lab": "Resultat"}]
        lines = [{"t": "text", "lab": "Dades", "rows": 1, "ph": "Dades amb unitats i què et demanen"},
                 {"t": "math", "lab": "Fórmula i càlcul"}, {"t": "res", "lab": "Resultat"}]
        if EXPL.search(t): lines.append({"t": "text", "lab": "Explicació", "rows": 2})
        return lines

    def smart(qdiv, q, ctx_title):
        """Adapta la resposta al tipus de pregunta. Retorna True si ha creat els camps."""
        d = qdiv.find("div", recursive=False)
        if not d: return False
        p = d.find("p", recursive=False)
        others = [c for c in d.find_all(recursive=False) if c is not p]
        if not p or not others or any(not (c.name == "div" and "lines" in (c.get("class") or [])) for c in others): return False
        if PLAIN: return False
        ptxt = plain(p); ctx = ctx_title + " " + ptxt
        if DRAW.search(ptxt) or GRAPH.search(ptxt): return False
        nlines = sum(len(c.find_all("div", class_="l")) for c in others)
        inner = p.decode_contents(); sp = split_subs(inner)
        def remove_lines():
            leg = ""
            for c in others:
                ls = c.find_all("div", class_="l", recursive=False)
                if ls:
                    i = fid("work", q, rows=max(2, len(ls)), legacy=1); leg += f'<div class="fld" data-fid="{i}"></div>'
                c.decompose()
            if leg: d.append(BeautifulSoup(leg, "html.parser"))
        if sp:
            intro, subs = sp
            if len(subs) > 8: return False
            rows = []
            for letter, h in subs:
                t = plain(h); w = ""
                if "→" in t and re.search(r"ajust|complet|formula", ctx, re.I):
                    r = eq_widget(h, q, ctx)
                    if r:
                        ew, rest = r
                        rows.append(f'<div class="subq"><span class="sl">{letter})</span><div class="st">{ew}' + (f'<div class="small">{rest}</div>' if rest and len(rest) > 2 else "") + "</div></div>"); continue
                if (CONV.search(ctx) or TGT.search(t)) and QTY.search(t):
                    init = chain_init(t, ctx)
                    if init: i = sfid("work", q, init=init, sub=1); w = f'<div class="fld" data-fid="{i}"></div>'
                if not w and CALCQ.search(t) and re.search(r"\d", t + ptxt) and not NOCALC.search(t):
                    i = sfid("work", q, init=scaffold(t, ctx, True), sub=1); w = f'<div class="fld" data-fid="{i}"></div>'
                if not w:
                    i = sfid("work", q, rows=1, sub=1); w = f'<div class="fld" data-fid="{i}"></div>'
                rows.append(f'<div class="subq"><span class="sl">{letter})</span><div class="st">{h}</div><div class="sa">{w}</div></div>')
            extra = ""
            if re.search(r"ajust|complet", ctx, re.I) and re.search(r"escriu|proporci|llegeix|quants|per què|explica", intro + " " + ptxt.split("a)")[-1][-120:], re.I):
                i = sfid("work", q, rows=2); extra = f'<div class="fld" data-fid="{i}"></div>'
            new = BeautifulSoup(f'<p>{intro}</p><div class="subs">{"".join(rows)}</div>{extra}', "html.parser")
            p.replace_with(new); remove_lines(); return True
        # sense apartats
        if "→" in ptxt and re.search(r"ajusta", ptxt, re.I) and not re.search(r"escriu i ajusta", ptxt, re.I):
            r = eq_widget(inner, q, ctx)
            if r:
                ew, rest = r
                i = sfid("work", q, rows=2)
                p.insert_after(BeautifulSoup(ew + f'<div class="fld" data-fid="{i}"></div>', "html.parser")); remove_lines(); return True
        if re.search(r"escriu i ajusta|escriu.{0,40}equació", ptxt, re.I):
            init = [{"t": "text", "lab": "Equació ajustada", "rows": 1, "ph": "Ex.: 2 H₂ + O₂ → 2 H₂O"}]
            if "?" in ptxt or EXPL.search(ptxt): init.append({"t": "text", "lab": "Resposta", "rows": 2})
            i = sfid("work", q, init=init); p.insert_after(BeautifulSoup(f'<div class="fld" data-fid="{i}"></div>', "html.parser")); remove_lines(); return True
        if CONV.search(ptxt) and len(QTY.findall(ptxt)) == 1 and not CALCV.search(ptxt):
            init = chain_init(ptxt, ctx)
            if init:
                i = sfid("work", q, init=init); p.insert_after(BeautifulSoup(f'<div class="fld" data-fid="{i}"></div>', "html.parser")); remove_lines(); return True
        if CALCQ.search(ptxt) and QTY.search(ptxt) and nlines >= 2 and not NOCALC.search(ptxt):
            i = sfid("work", q, init=scaffold(ptxt, ctx)); p.insert_after(BeautifulSoup(f'<div class="fld" data-fid="{i}"></div>', "html.parser")); remove_lines(); return True
        return False

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
        try: smart(b["els"][0], q, title + " " + sec)
        except Exception as ex: print("  avís smart", key, q, ex)
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
