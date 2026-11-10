#!/usr/bin/env python3
"""Extreu l'estructura del dossier de teoria de Biologia (PDF fet amb Chrome) a JSON.

El PDF original es va generar des d'HTML; aquí se'n recupera l'estructura: títols, paràgrafs,
requadres (Exemple resolt, Mini-PAU…), taules, figures (amb el peu), glossari, errors típics i
autoavaluació. El resultat (contingut/biologia/teoria-extret.json) és el punt de partida de la
revisió; el llibre web es genera a partir de contingut/biologia/teoria.json (ja revisat).

Ús: python3 tools/biologia/extreu_teoria.py dossier.pdf [sortida.json]
"""
import json, re, sys
from pathlib import Path
import pymupdf as fitz

SRC = sys.argv[1]
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else Path(__file__).resolve().parents[2] / "contingut/biologia/teoria-extret.json")
FIGDIR = OUT.parent / "fig-original"

BORDER = (0.890, 0.871, 0.831)
TABHEAD = (0.927, 0.949, 0.974)


def near(a, b, tol=0.02):
    return a is not None and b is not None and all(abs(x - y) <= tol for x, y in zip(a, b))


def lum(c):
    return 0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class R:
    def __init__(s, kind, rect, **kw):
        s.kind, s.rect = kind, fitz.Rect(rect)
        s.__dict__.update(kw)

    def contains(s, x, y, pad=1.5):
        r = s.rect
        return r.x0 - pad <= x <= r.x1 + pad and r.y0 - pad <= y <= r.y1 + pad


def regions(page):
    dr = page.get_drawings()
    out = []
    # requadres: el mateix rectangle ple repetit 3 o més vegades (vora)
    cnt = {}
    for d in dr:
        if d.get("fill") is None:
            continue
        r = d["rect"]
        key = (round(r.x0), round(r.y0), round(r.x1), round(r.y1), tuple(round(c, 3) for c in d["fill"]))
        cnt[key] = cnt.get(key, 0) + 1
    boxes = []
    for (x0, y0, x1, y1, f), n in cnt.items():
        if n >= 3 and x1 - x0 > 200 and y1 - y0 > 15:
            boxes.append(R("box", (x0, y0, x1, y1), color=f))
    # requadres amb vora feta d'un rectangle ple i un altre de més clar a dins
    fills = [d for d in dr if d.get("fill") is not None and d["rect"].width > 200 and d["rect"].height > 25 and d["rect"].width < 540]
    for a in fills:
        A = a["rect"]
        if any(abs(A.x0 - b.rect.x0) < 3 and abs(A.y0 - b.rect.y0) < 3 for b in boxes):
            continue
        for b in fills:
            B = b["rect"]
            if b is a or near(b["fill"], a["fill"]):
                continue
            if 0 <= B.x0 - A.x0 <= 4.5 and 0 <= B.y0 - A.y0 <= 4.5 and 0 <= A.x1 - B.x1 <= 4.5 and 0 <= A.y1 - B.y1 <= 4.5 and lum(a["fill"]) < lum(b["fill"]):
                boxes.append(R("box", A, color=tuple(a["fill"])))
                break
    out += boxes
    for d in dr:
        r, f, c = d["rect"], d.get("fill"), d.get("color")
        if r.width > 500 and r.height > 600:
            continue  # marc de pàgina
        if near(c, BORDER) and f is not None and near(f, (1, 1, 1)) and r.width > 80 and r.height > 30:
            out.append(R("fig", r))
        elif f is not None and c is not None and not near(c, BORDER) and lum(f) > 0.9 and r.width > 300 and r.height > 30:
            out.append(R("card", r, color=c))
        elif f is not None and c is None and lum(f) < 0.65 and 14 < r.height < 30 and r.width > 300:
            out.append(R("bar", r, color=f))
        elif f is not None and c is None and 0.9 < lum(f) < 0.99 and r.x0 > 75 and r.width > 300 and r.height > 20 and not near(f, TABHEAD):
            out.append(R("ans", r))
    # taules: cel·les de capçalera
    heads = [d["rect"] for d in dr if d.get("fill") is not None and near(d["fill"], TABHEAD, 0.006) and 12 < d["rect"].height < 40]
    rows = {}
    for h in heads:
        rows.setdefault(round(h.y0), []).append(h)
    whites = [d["rect"] for d in dr if d.get("fill") is not None and near(d["fill"], (1, 1, 1)) and d.get("color") is None and d["rect"].width > 150]
    for y, cells in rows.items():
        cells.sort(key=lambda r: r.x0)
        x0, x1 = cells[0].x0, cells[-1].x1
        cand = [w for w in whites if abs(w.y0 - y) < 3 and abs(w.x0 - x0) < 4 and abs(w.x1 - x1) < 4]
        y1 = max((w.y1 for w in cand), default=None)
        if y1 is None:
            continue
        seps = sorted({round(d["rect"].y0, 1) for d in dr if d.get("fill") is not None and near(d["fill"], BORDER) and d["rect"].height < 2 and x0 - 2 <= d["rect"].x0 <= x1})
        out.append(R("table", (x0, y, x1, y1), cols=[(c.x0, c.x1) for c in cells], head_y1=cells[0].y1, seps=seps))
    # taules sense capçalera (continuació a dalt de pàgina): rectangle blanc a dalt amb separadors
    return out


def line_info(l):
    spans = [s for s in l["spans"] if s["text"]]
    return {
        "bbox": l["bbox"],
        "spans": spans,
        "text": "".join(s["text"] for s in spans),
        "font": spans[0]["font"] if spans else "",
        "size": round(spans[0]["size"], 1) if spans else 0,
        "color": spans[0]["color"] if spans else 0,
    }


def span_html(spans):
    if not spans:
        return ""
    base = max(spans, key=lambda s: len(s["text"]))
    bsize, borig = base["size"], base["origin"][1]
    out = []
    for s in spans:
        t = esc(s["text"])
        f = s["font"]
        if s["size"] < bsize * 0.85 and t.strip():
            dy = s["origin"][1] - borig
            if dy < -1:
                t = f"<sup>{t}</sup>"
            elif dy > 1:
                t = f"<sub>{t}</sub>"
        if "Bold" in f and "Bold" not in base["font"] and t.strip():
            t = f"<b>{t}</b>"
        if "Italic" in f and "Italic" not in base["font"] and t.strip():
            t = f"<i>{t}</i>"
        out.append(t)
    h = "".join(out)
    return re.sub(r"</b>(\s*)<b>", r"\1", re.sub(r"</i>(\s*)<i>", r"\1", h))


def join_lines(lines):
    h = ""
    for l in lines:
        t = span_html(l["spans"]).strip()
        if not h:
            h = t
        elif h.endswith("-") and not h.endswith(" -") and re.match(r"[a-zà-ú]", t) and False:
            h = h[:-1] + t
        else:
            h += " " + t
    return re.sub(r"\s+", " ", h).strip()


def paragraphs(lines, gap=19.5):
    """Agrupa línies en paràgrafs pel salt vertical i pel sagnat."""
    paras, cur, last = [], [], None
    for l in lines:
        y, x = l["bbox"][1], l["bbox"][0]
        brk = False
        if cur:
            x0 = cur[0]["bbox"][0]
            px = cur[-1]["bbox"][0]
            if y - last > gap:
                brk = True
            elif abs(x - px) > 6:
                hanging = re.match(r"\d+\.\s", cur[0]["text"]) and 6 < x - x0 < 16
                brk = not hanging
        if l.get("bullet"):
            brk = bool(cur)
        if brk:
            paras.append(cur)
            cur = []
        cur.append(l)
        last = y
    if cur:
        paras.append(cur)
    return paras


def is_h4(l):
    return l["font"] == "Tinos-Bold" and l["size"] == 11.0 and all(s["font"] == "Tinos-Bold" for s in l["spans"])


def flow(lines):
    """Converteix línies d'un mateix contenidor en elements (p, h2, h4, li)."""
    # els «!» dels errors típics marquen l'inici d'un element de llista
    marks = [l for l in lines if l["text"].strip() == "!" and l["font"].startswith("NotoSans")]
    lines = [l for l in lines if l not in marks]
    for m in marks:
        for l in lines:
            if abs(l["bbox"][1] - m["bbox"][1]) < 4:
                l["bullet"] = True
                break
    els = []
    for para in paragraphs(lines):
        x = round(para[0]["bbox"][0])
        if para[0]["size"] >= 16:
            els.append({"t": "h2", "html": esc(" ".join(l["text"].strip() for l in para))})
            continue
        if len(para) == 1 and is_h4(para[0]):
            els.append({"t": "h4", "html": esc(para[0]["text"].strip())})
            continue
        if is_h4(para[0]) and len(para) > 1 and para[1]["bbox"][1] - para[0]["bbox"][1] > 17:
            els.append({"t": "h4", "html": esc(para[0]["text"].strip())})
            para = para[1:]
        e = {"t": "li" if para[0].get("bullet") else "p", "html": join_lines(para), "x": x}
        els.append(e)
    return els


def table_rows(reg, lines):
    cols = reg.cols
    head = [l for l in lines if l["bbox"][1] < reg.head_y1 - 1]
    body = [l for l in lines if l["bbox"][1] >= reg.head_y1 - 1]
    def cellify(ls, bounds):
        cells = [[] for _ in cols]
        for l in ls:
            cx = (l["bbox"][0] + 2)
            for i, (a, b) in enumerate(cols):
                if a - 3 <= cx <= b:
                    cells[i].append(l)
                    break
        return [join_lines(sorted(c, key=lambda l: (l["bbox"][1], l["bbox"][0]))) for c in cells]
    hrow = cellify(head, None)
    seps = [s for s in reg.seps if reg.head_y1 + 2 < s < reg.rect.y1 - 1]
    bounds = [reg.head_y1] + seps + [reg.rect.y1]
    rows = []
    for a, b in zip(bounds, bounds[1:]):
        ls = [l for l in body if a - 1 <= (l["bbox"][1] + l["bbox"][3]) / 2 <= b + 1]
        if ls:
            rows.append(cellify(ls, None))
    return {"t": "table", "head": hrow, "rows": rows}


def merge_pages(els):
    out = []
    for e in els:
        if out:
            prev = out[-1]
            if e["page"] == prev.get("page_end", prev["page"]) + 1 or e["page"] == prev["page"] + 1:
                pt = re.sub("<[^>]+>", "", prev.get("html", ""))
                if e["t"] == "p" and prev["t"] == "p" and e.get("x") == prev.get("x") and e.get("first") and not re.search(r"[.:?!»)]$", pt):
                    prev["html"] += " " + e["html"]; prev["page_end"] = e["page"]; continue
                if e["t"] in ("box", "card") and prev["t"] == e["t"] and e.get("first") and not e.get("title"):
                    # continuació del requadre
                    ch = e["children"]
                    if ch and prev["children"] and ch[0]["t"] == "p" and prev["children"][-1]["t"] == "p" and not re.search(r"[.:?!»)]$", re.sub("<[^>]+>", "", prev["children"][-1]["html"])):
                        prev["children"][-1]["html"] += " " + ch[0]["html"]; ch = ch[1:]
                    prev["children"] += ch; prev["page_end"] = e["page"]; continue
                if e["t"] == "table" and prev["t"] == "table" and e.get("first") and e["head"] == prev["head"]:
                    prev["rows"] += e["rows"]; prev["page_end"] = e["page"]; continue
        out.append(e)
    for e in out:
        e.pop("first", None)
    return out


def main():
    doc = fitz.open(SRC)
    FIGDIR.mkdir(parents=True, exist_ok=True)
    els = []  # elements de primer nivell
    for page in doc:
        pn = page.number + 1
        regs = regions(page)
        lines = []
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                li = line_info(l)
                if li["text"].strip():
                    lines.append(li)
        lines.sort(key=lambda l: (round(l["bbox"][1]), l["bbox"][0]))
        # assigna cada línia a la regió més interna
        def owner(l):
            cx = (l["bbox"][0] + l["bbox"][2]) / 2
            cy = (l["bbox"][1] + l["bbox"][3]) / 2
            best = None
            for r in regs:
                if r.kind in ("fig", "box", "card", "bar", "table", "ans") and r.contains(cx, cy):
                    if best is None or r.rect.get_area() < best.rect.get_area():
                        best = r
            return best
        for r in regs:
            r.lines = []
        top = []
        for l in lines:
            o = owner(l)
            if o is None:
                top.append(l)
            else:
                o.lines.append(l)
        # peus de figura
        figs = sorted([r for r in regs if r.kind == "fig"], key=lambda r: r.rect.y0)
        for f in list(figs):
            # un marc sense peu «Figura» és un requadre (p. ex. «Errors típics»), no una figura
            below = [l for l in top if f.rect.y1 - 2 < l["bbox"][1] < f.rect.y1 + 30 and l["text"].startswith("Figura")]
            if not below:
                f.kind = "box"
                figs.remove(f)
                continue
        for f in figs:
            cap = [l for l in top if f.rect.y1 - 2 < l["bbox"][1] < f.rect.y1 + 70 and l["font"].startswith("NotoSans")]
            # el peu són les línies NotoSans seguides just a sota
            cap_lines, last = [], f.rect.y1
            for l in sorted(cap, key=lambda l: l["bbox"][1]):
                if l["bbox"][1] - last < 20:
                    cap_lines.append(l)
                    last = l["bbox"][1]
            for l in cap_lines:
                top.remove(l)
            f.caption = join_lines(cap_lines)
            m = re.match(r"(?:<b>)?Figura (\d+\.\d+b?)\.", re.sub("<[^>]+>", "", f.caption))
            f.num = m.group(1) if m else f"p{pn}"
            clip = fitz.Rect(f.rect.x0 + 4, f.rect.y0 + 4, f.rect.x1 - 4, f.rect.y1 - 4)
            name = f"orig-{f.num}.png"
            page.get_pixmap(dpi=200, clip=clip).save(str(FIGDIR / name))
            f.file = name
        # construeix elements de la pàgina en ordre vertical
        items = []
        for r in regs:
            if r.kind in ("fig", "box", "card", "bar", "table", "ans"):
                # només regions de primer nivell (no contingudes en una altra regió no-barra)
                parent = None
                for q in regs:
                    if q is not r and q.kind in ("box", "card", "fig") and q.rect.contains(r.rect) and q.rect.get_area() > r.rect.get_area():
                        if parent is None or q.rect.get_area() < parent.rect.get_area():
                            parent = q
                r.parent = parent
        def build(container_lines, children, y0=None):
            """Combina línies soltes i regions filles en una llista ordenada."""
            seq = [("L", l["bbox"][1], l) for l in container_lines] + [("R", c.rect.y0, c) for c in children]
            seq.sort(key=lambda x: x[1])
            res, buf = [], []
            def flush():
                if buf:
                    res.extend(flow(buf))
                    buf.clear()
            for k, _, o in seq:
                if k == "L":
                    buf.append(o)
                else:
                    flush()
                    res.append(render(o))
            flush()
            return res
        def kids(r):
            return [c for c in regs if getattr(c, "parent", None) is r and c.kind in ("fig", "box", "card", "bar", "table", "ans")]
        def render(r):
            if r.kind == "fig":
                return {"t": "fig", "num": r.num, "file": r.file, "caption": r.caption, "page": pn, "h": round(r.rect.height)}
            if r.kind == "bar":
                return {"t": "h3", "html": join_lines(r.lines)}
            if r.kind == "table":
                return table_rows(r, r.lines)
            if r.kind == "ans":
                return {"t": "ans", "children": build(r.lines, kids(r))}
            # box / card: títol
            ls = list(r.lines)
            title = None
            if ls and ls[0]["font"] == "NotoSans-Bold" and ls[0]["size"] == 10.8:
                title = ls.pop(0)
            ch = build(ls, kids(r))
            return {"t": r.kind, "title": title["text"].strip() if title else None,
                    "tcolor": "#%06x" % title["color"] if title else None, "children": ch, "page": pn}
        roots = [r for r in regs if getattr(r, "parent", 1) is None and r.kind in ("fig", "box", "card", "bar", "table", "ans")]
        # línies de primer nivell
        page_items = build(top, roots)
        for it in page_items:
            it.setdefault("page", pn)
        if page_items:
            page_items[0]["first"] = True
        # h2 (títol de capítol) i portada
        for it in page_items:
            if it["t"] == "p":
                pass
        els.extend(page_items)
    els = merge_pages(els)
    json.dump(els, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(els), "elements ->", OUT)


if __name__ == "__main__":
    main()
