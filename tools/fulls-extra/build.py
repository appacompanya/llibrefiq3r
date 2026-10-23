"""Amplia i corregeix els fulls en PDF de 2n i 4t sense tornar-los a fer de zero.

- Correccions (continguts/<nivell>.py, FIXES): canvis de text petits fets directament al PDF, amb la mateixa
  tipografia (errades, frases poc precises). S'apliquen una sola vegada: el PDF en guarda el registre.
- Activitats afegides (continguts/<nivell>.py, EXTRA): més preguntes a les fitxes i més reptes i recursos als
  materials d'ampliació. No són un full a part: continuen la fitxa just després de l'última pregunta, a l'espai
  que queda lliure a l'última pàgina, i si no hi caben segueixen en pàgines noves. Es generen en HTML amb el
  mateix estil (estil.py) i es passen a PDF amb Chromium (render.js). L'última pàgina original es guarda dins
  del PDF (fitxer adjunt), de manera que si es torna a executar es restaura i res no s'acumula. Els peus de
  pàgina es tornen a numerar («1/2», «2/2»…).

Després, l'acció de GitHub «Regenera el llibre digital» actualitza les fitxes digitals a partir dels PDF.
Ús: python3 build.py 2n|4t [fitxers…]   (cal haver fet «npm install» en aquesta carpeta)"""
import os, re, sys, json, subprocess, importlib, tempfile
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import estil

FONTS = {
    "reg": os.path.join(HERE, "fonts", "AtkinsonHyperlegible-Regular.ttf"),
    "bold": os.path.join(HERE, "fonts", "AtkinsonHyperlegible-Bold.ttf"),
    "ital": os.path.join(HERE, "fonts", "AtkinsonHyperlegible-Italic.ttf"),
    "alt": "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "foot": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
}
_F = {}
def font(k):
    if k not in _F: _F[k] = pymupdf.Font(fontfile=FONTS[k])
    return _F[k]

TAG = "fq-extra:"


def meta_get(doc):
    kw = doc.metadata.get("keywords") or ""
    if kw.startswith(TAG):
        try: return json.loads(kw[len(TAG):])
        except ValueError: pass
    return {"orig": doc.page_count, "fixes": []}


def meta_set(doc, m):
    md = dict(doc.metadata); md["keywords"] = TAG + json.dumps(m, ensure_ascii=False)
    doc.set_metadata(md)


def style_of(fontname):
    f = fontname.split("+")[-1]
    if "Atkinson" not in f: return "alt"
    if "Bol" in f: return "bold"
    if "Ital" in f: return "ital"
    return "reg"


def write_run(page, x, y, text, st, size, color):
    """Escriu text a partir de (x, y) amb la tipografia st; els caràcters que no hi són, amb la de reserva."""
    run, rs = "", st
    def flush(run, rs, x):
        if not run: return x
        page.insert_text((x, y), run, fontname="fx" + rs, fontfile=FONTS[rs], fontsize=size, color=color)
        return x + font(rs).text_length(run, size)
    for ch in text:
        s = st if font(st).has_glyph(ord(ch)) else "alt"
        if s != rs:
            x = flush(run, rs, x); run, rs = "", s
        run += ch
    return flush(run, rs, x)


def fix_line(page, old, new):
    """Substitueix «old» per «new» en una línia de text i torna a escriure la resta de la línia."""
    for b in page.get_text("rawdict")["blocks"]:
        for l in b.get("lines", []):
            chars = [(c, sp) for sp in l["spans"] for c in sp["chars"]]
            txt = "".join(c["c"] for c, _ in chars)
            i = txt.find(old)
            if i < 0: continue
            tail = chars[i:]
            styles = [style_of(sp["font"]) for _, sp in tail]
            sizes = [sp["size"] for _, sp in tail]
            colors = [sp["color"] for _, sp in tail]
            ttxt = txt[i:]
            ntxt = new + ttxt[len(old):]
            nst = [styles[0]] * len(new) + styles[len(old):]
            nsz = [sizes[0]] * len(new) + sizes[len(old):]
            ncol = [colors[0]] * len(new) + colors[len(old):]
            r = pymupdf.Rect(tail[0][0]["bbox"])
            for c, _ in tail: r.include_rect(c["bbox"])
            h = r.height
            page.add_redact_annot(pymupdf.Rect(r.x0, r.y0 + h * .18, r.x1 + .5, r.y1 - h * .18))
            page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
            x, y = tail[0][0]["origin"]
            j = 0
            while j < len(ntxt):
                k = j
                while k < len(ntxt) and (nst[k], nsz[k], ncol[k]) == (nst[j], nsz[j], ncol[j]): k += 1
                col = tuple(((ncol[j] >> s) & 255) / 255 for s in (16, 8, 0))
                x = write_run(page, x, y, ntxt[j:k], nst[j], nsz[j], col)
                j = k
            if x > page.rect.width - 36:
                print("  ! la línia corregida passa del marge:", ntxt[:50])
            return True
    return False


def apply_fix(doc, f):
    p = doc[f.get("page", 0)]
    t = f["type"]
    if t == "line":
        if not fix_line(p, f["old"], f["new"]): raise SystemExit(f"No trobo «{f['old']}» a {doc.name}")
    elif t == "redact":
        p.add_redact_annot(pymupdf.Rect(f["rect"]))
        p.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                           graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_TOUCHED if f.get("graphics") else pymupdf.PDF_REDACT_LINE_ART_NONE)
    elif t == "text":
        st, size = f.get("font", "reg"), f.get("size", 10.99)
        w = font(st).text_length(f["text"], size)
        x = f["x"] - w / 2 if f.get("align") == "center" else f["x"]
        write_run(p, x, f["y"], f["text"], st, size, (0x1f / 255, 0x23 / 255, 0x28 / 255))
    else:
        raise SystemExit("tipus de correcció desconegut: " + t)


def footer_numbers(doc):
    """Torna a escriure «i/N» a tots els peus de pàgina, amb N = pàgines del full."""
    n = doc.page_count
    base = None
    for pno, p in enumerate(doc):
        found = None
        for b in p.get_text("rawdict")["blocks"]:
            for l in b.get("lines", []):
                t = "".join(c["c"] for sp in l["spans"] for c in sp["chars"]).strip()
                if l["bbox"][1] > p.rect.height - 40 and re.fullmatch(r"\d+/\d+", t):
                    found = l
        if found:
            r = pymupdf.Rect(found["bbox"])
            base = (r.x1, found["spans"][0]["chars"][0]["origin"][1], found["spans"][0]["size"])
            p.add_redact_annot(r + (-1, 0, 1, 0))
            p.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
        x1, y, size = base or (555.6, 824.4, 8.0)
        s = f"{pno + 1}/{n}"
        w = font("foot").text_length(s, size)
        p.insert_text((x1 - w, y), s, fontname="fxfoot", fontfile=FONTS["foot"], fontsize=size, color=(0x24 / 255, 0x27 / 255, 0x2c / 255))


BACKUP = "fq-extra-pagina-original.pdf"
GAP = 16          # espai (pt) entre l'última pregunta original i la primera afegida
MIN_FREE = 70     # si queda menys espai lliure, les activitats comencen en una pàgina nova


def restore(doc, m):
    """Deixa el PDF com era abans d'afegir-hi activitats (amb les correccions ja fetes)."""
    if doc.page_count > m["orig"]:
        doc.delete_pages(from_page=m["orig"], to_page=doc.page_count - 1)
    if BACKUP in doc.embfile_names():
        b = pymupdf.open("pdf", doc.embfile_get(BACKUP))
        last = m["orig"] - 1
        doc.delete_page(last)
        doc.insert_pdf(b, start_at=last)
        doc.embfile_del(BACKUP)


def content_bottom(page):
    """Coordenada y on acaba el contingut de la pàgina (sense el peu)."""
    H = page.rect.height
    ys = [b[3] for b in page.get_text("blocks") if b[3] < H - 40]
    ys += [d["rect"].y1 for d in page.get_drawings() if d["rect"].y1 < H - 40]
    ys += [r.y1 for im in page.get_images() for r in page.get_image_rects(im[0]) if r.y1 < H - 40]
    return max(ys) if ys else 0


def main():
    args = sys.argv[1:]
    level = args.pop(0) if args and args[0] in ("2n", "4t") else None
    if not level: raise SystemExit(__doc__)
    C = importlib.import_module(f"continguts.c{level}")
    only = set(args)
    docs = os.path.join(ROOT, level, "docs")
    files = sorted(set(C.EXTRA) | {f["file"] for f in C.FIXES})
    if only: files = [f for f in files if f in only or any(o in f for o in only)]
    tmp = tempfile.mkdtemp(prefix="fulls-extra-")
    opened, jobs = {}, []
    for fn in files:
        doc = pymupdf.open(os.path.join(docs, fn))
        m = meta_get(doc)
        restore(doc, m)
        for f in [f for f in C.FIXES if f["file"] == fn]:
            if f["id"] in m["fixes"]: continue
            apply_fix(doc, f); m["fixes"].append(f["id"])
        top = None
        if fn in C.EXTRA:
            last = doc[m["orig"] - 1]
            y = content_bottom(last) + GAP
            if last.rect.height - 43 - y >= MIN_FREE: top = y
            sda = int(re.match(r"sda(\d)", fn).group(1))
            hp = os.path.join(tmp, fn.replace(".pdf", ".html"))
            open(hp, "w", encoding="utf-8").write(estil.page(level, sda, C.EXTRA[fn], top))
            jobs.append({"html": hp, "pdf": hp.replace(".html", ".pdf"), "footer": estil.footer(level, sda)})
        opened[fn] = (doc, m, top)
    if jobs:
        jp = os.path.join(tmp, "feines.json"); json.dump(jobs, open(jp, "w"))
        subprocess.run(["node", os.path.join(HERE, "render.js"), jp], check=True)
    for fn in files:
        doc, m, top = opened[fn]
        path = os.path.join(docs, fn)
        extra = 0
        if fn in C.EXTRA:
            e = pymupdf.open(os.path.join(tmp, fn))
            first = 0
            if top is not None:
                # la primera pàgina generada continua l'última pàgina del full: s'hi superposa (sense el peu)
                last = doc[m["orig"] - 1]
                src = pymupdf.open(); src.insert_pdf(last.parent, from_page=last.number, to_page=last.number)
                doc.embfile_add(BACKUP, src.tobytes(), desc="Última pàgina original (per a build.py)")
                if e[0].get_text().strip():
                    W, H = last.rect.width, last.rect.height
                    r = pymupdf.Rect(0, top - 4, W, H - 43)
                    last.show_pdf_page(r, e, 0, clip=r)
                first = 1
            if e.page_count > first:
                doc.insert_pdf(e, from_page=first, to_page=e.page_count - 1)
                extra = e.page_count - first
        if fn in C.EXTRA or m.get("extra"):
            footer_numbers(doc)
        m["extra"] = extra
        meta_set(doc, m)
        out = path + ".tmp"
        doc.save(out, garbage=3, deflate=True); doc.close()
        os.replace(out, path)
        print(f"{level}/{fn}: {m['orig']} + {extra} pàgines{' (continua a la pàg. ' + str(m['orig']) + ')' if top is not None else ''}, {len(m['fixes'])} correccions")


if __name__ == "__main__":
    main()
