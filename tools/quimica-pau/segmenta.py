"""Talla els exàmens i les pautes de la PAU de Química en exercicis (retalls vectorials de les pàgines originals)."""
import re
import pymupdf

# Línies que no formen part del contingut d'un exercici (capçaleres, peus, quadres de correcció)
SKIP = re.compile(
    r"^(Pàgina \d+ de \d+|Química|Prov(a|es) d.accés a la universitat.*|Districte Universitari.*|Oficina d.Accés.*|Criteris? (específics?|d.avaluació).*|proves|"
    r"Espai per a la correcció|Espai per a la revisió|Total|[a-d]|[–•]\s*\d+\s*[–•]|\d{1,2}|"
    r"Etiqueta de.*|Ubicació del tribunal.*|Número del tribunal.*|Qualificació.*|Comprovació|2a correcció|"
    r"Generalitat de Catalunya|Consell Interuniversitari de Catalunya|Pautes de correcció.*|"
    r"P[àa]gina \d+ de \d+.*|Convocatòria \d{4}.*|Sèrie \d\s*$|SERIE \d|SÈRIE \d|PAU \d{4}|\d{4})$", re.I
)


HEADER = re.compile(r"^(Pàgina \d+ de \d+|Química|Prov(a|es) d.accés a la universitat.*|Districte Universitari.*|Oficina d.Accés.*|"
                    r"Criteris? (específics?|d.avaluació).*|proves|PAU \d{4}.*|Pautes de correcció.*|Convocatòria \d{4}.*|\d{4})$", re.I)
FOOT = re.compile(r"^([–•]\s*\d+\s*[–•]|\d{1,2}|Pàgina \d+ de \d+)$")


def lines(page):
    """[(y0, y1, x0, x1, text, bold)] de la pàgina, en ordre de lectura."""
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"]).strip()
            if not t:
                continue
            bold = any(("Bold" in s["font"] or s["flags"] & 16) for s in l["spans"] if s["text"].strip())
            x0, y0, x1, y1 = l["bbox"]
            out.append((y0, y1, x0, x1, t, bold))
    out.sort()
    return out


def correction_boxes(page):
    """Rectangles dels quadres «Espai per a la correcció» (s'exclouen del retall)."""
    rs = []
    for r in page.search_for("Espai per a la correcció") + page.search_for("Espai per a la revisió"):
        rs.append(pymupdf.Rect(r.x0 - 60, r.y0 - 6, page.rect.x1, r.y1 + 130))
    # quadrets de puntuació d'apartat (2026): «Puntuació de l'apartat 2.1» + casella
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(sp["text"] for sp in l["spans"]).strip()
            x0, y0, x1, y1 = l["bbox"]
            if re.match(r"^(Puntuació (total )?de l.(apartat|exercici)|Puntuació apartat|parcial \d)", t) or (t == "Total" and x0 > 300):
                rs.append(pymupdf.Rect(x0 - 12, y0 - 6, x1 + 120, y1 + 6))
    # caselles grises de puntuació (encara que el text estigui partit)
    for d in page.get_drawings():
        r, f = d["rect"], d.get("fill")
        if f and all(0.85 < c < 0.95 for c in f[:3]) and 100 < r.width < 260 and 10 < r.height < 32 and r.x0 > 280:
            rs.append(pymupdf.Rect(r.x0 - 4, r.y0 - 4, r.x1 + 4, r.y1 + 4))
    # etiqueta de l'alumne a dalt de la pàgina de la darrera pregunta
    for r in page.search_for("Etiqueta de l"):
        if r.y0 < 140:
            rs.append(pymupdf.Rect(r.x0 - 12, r.y0 - 6, min(page.rect.x1, r.x0 + 230), r.y1 + 75))
    return rs


def content_bbox(page, y0, y1, extra_skip=None):
    """Caixa del contingut real (text, dibuixos i imatges) entre y0 i y1."""
    H = page.rect.height
    boxes = correction_boxes(page)
    ls = lines(page)
    # capçalera de pàgina: tot el que queda per sobre de l'última línia de capçalera (logo i filet inclosos)
    hl = [l[1] for l in ls if l[1] < 150 and HEADER.match(l[4])]
    head = max(hl) + 9 if hl else 0
    y0 = max(y0, head)
    top, bot = None, None
    xs0, xs1 = [], []
    # els rectangles «blancs» que tapen els quadres de correcció es pinten amb (1, 1, 0.996) per reconèixer-los
    whites = [d["rect"] for d in page.get_drawings() if d.get("fill") and d["fill"][0] > 0.999 and 0.99 < d["fill"][2] < 0.999
              and not d.get("color")]
    boxes = boxes + [pymupdf.Rect(w.x0 - 1, w.y0 - 1, w.x1 + 1, w.y1 + 1) for w in whites]

    def add(r):
        nonlocal top, bot
        if r.y1 <= y0 + 0.5 or r.y0 >= y1 - 0.5 or r.y0 > H - 45 and r.height < 20:
            return
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        if any(b.x0 <= cx <= b.x1 and b.y0 <= cy <= b.y1 for b in boxes):
            return
        a, b = max(r.y0, y0), min(r.y1, y1)
        top = a if top is None else min(top, a)
        bot = b if bot is None else max(bot, b)
        xs0.append(r.x0); xs1.append(r.x1)

    for (ly0, ly1, lx0, lx1, t, bold) in ls:
        if SKIP.match(t) or STOP.search(t) or (extra_skip and extra_skip.match(t)):
            continue
        add(pymupdf.Rect(lx0, ly0, lx1, ly1))
    for d in page.get_drawings():
        r = d["rect"]
        if r.width < 2 and r.height < 2 or r.width > page.rect.width * 0.95:
            continue
        f = d.get("fill")
        if f and all(c > 0.98 for c in f[:3]) and not d.get("color"):
            continue  # rectangles blancs (fons o tapes): no són contingut visible
        add(r)
    for info in page.get_image_info():
        add(pymupdf.Rect(info["bbox"]))
    if top is None:
        return None
    x0 = max(0, min(xs0) - 4)
    x1 = min(page.rect.width, max(xs1) + 4)
    # peu de pàgina: el número de pàgina o els crèdits de l'IEC marquen el límit inferior
    feet = [l[0] for l in ls if l[0] > bot - 1 and (FOOT.match(l[4]) and l[0] > H - 70 or STOP.search(l[4]))]
    cap = (min(feet) - 1) if feet else H - 18
    return pymupdf.Rect(x0, top - 3, x1, min(bot + 14, y1, cap))


STOP = re.compile(r"Podeu utilitzar aquest(es pàgines|a pàgina)|ha tingut cura de la correcció lingüística|Etiqueta de l.(estudiant|alumne)|Etiqueta de qualificació|Espai per a (les )?etiquet")


def useful_pages(doc, pages):
    """Descarta les pàgines de portada, de «podeu utilitzar aquesta pàgina…» i de crèdits, però no les que,
    a més d'aquests textos, tenen una pregunta (els fitxers compactats posen la sèrie i la pregunta 1 a la portada)."""
    out = []
    for p in pages:
        ls = lines(doc[p])
        long = [l for l in ls if len(l[4]) > 30 and not STOP.search(l[4]) and not SKIP.match(l[4])
                and not re.search(r"Ubicació del tribunal|Número del tribunal|\.{8}", l[4])]
        if not long and (not doc[p].get_image_info() or re.search(r"Espai per a (les )?etiquet", doc[p].get_text())):
            continue  # pàgina sense text llarg ni imatges: espai per respondre, quadres buits
        txt = doc[p].get_text()
        if re.search(r"Etiqueta de l", txt) and not any(re.match(r"^[1-7]\.(\s+\S.{20,}|\s*$)", l[4]) for l in ls):
            continue  # portada o contraportada
        if not any(STOP.search(l[4]) for l in ls) or len(long) >= 6:
            out.append(p)
    return out


def segment(doc, pages, heading, key, extra_skip=None, min_gap=0):
    """Talla les pàgines en blocs que comencen a cada capçalera.

    heading: regex aplicada a cada línia; key(m) torna la clau del bloc (p. ex. el número de l'exercici).
    Línies consecutives amb la mateixa clau continuen el mateix bloc.
    Torna [(clau, text_capçalera, [(pno, Rect)], text)]."""
    pages = useful_pages(doc, pages)
    marks = []
    last = 0
    for pno in pages:
        boxes = correction_boxes(doc[pno])
        for (y0, y1, x0, x1, t, bold) in lines(doc[pno]):
            m = heading.match(t)
            if m and not any(b.x0 <= (x0 + x1) / 2 <= b.x1 and b.y0 <= (y0 + y1) / 2 <= b.y1 for b in boxes):
                k = key(m)
                if k < last:
                    continue  # les claus van creixent: una de més petita és una repetició (contraportada, índex)
                last = k
                marks.append((pno, y0 - 2, k, t))
    # fusiona capçaleres consecutives amb la mateixa clau (p. ex. «Exercici 1a» i «Exercici 1b»)
    starts = []
    for mk in marks:
        if not starts or starts[-1][2] != mk[2]:
            starts.append(mk)
    out = []
    for i, (pno, y, k, t) in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else (pages[-1], doc[pages[-1]].rect.height, None, None)
        clips, text = [], []
        for p in range(pno, end[0] + 1):
            if p not in pages:
                continue
            ya = y if p == pno else 0
            yb = end[1] if p == end[0] else doc[p].rect.height
            r = content_bbox(doc[p], ya, yb, extra_skip)
            if r and r.height > 6:
                clips.append((p, r))
                text.append(doc[p].get_text("text", clip=r))
        if clips:
            out.append((k, t, clips, "\n".join(text)))
    return out


def neteja(path, out):
    """Còpia del PDF sense els quadres de correcció/puntuació.

    1) s'esborra el text que cau dins dels quadres (només les línies amb el centre a dins);
    2) s'esborren els dibuixos (caselles) totalment coberts pel quadre, sense pintar res al damunt."""
    doc = pymupdf.open(path)
    for page in doc:
        bs = correction_boxes(page)
        # textos verticals del marge (crèdits de l'IEC, «Districte Universitari…»): fora
        rot = []
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                if abs(l["dir"][1]) > 0.5:
                    rot.append(pymupdf.Rect(l["bbox"]))
        # logo de l'IEC al peu de l'última pàgina de cada sèrie (imatge petita i centrada)
        H = page.rect.height
        for im in page.get_image_info():
            b = pymupdf.Rect(im["bbox"])
            if b.y0 > H - 110 and b.width < 140 and b.height < 60 and abs((b.x0 + b.x1) / 2 - page.rect.width / 2) < 40:
                page.draw_rect(pymupdf.Rect(b.x0 - 1, b.y0 - 1, b.x1 + 1, b.y1 + 1), color=None, fill=(1, 1, 0.996), overlay=True)
        for r in rot:
            page.add_redact_annot(r, fill=False)
        if rot:
            page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                                  text=pymupdf.PDF_REDACT_TEXT_REMOVE)
        if not bs:
            continue
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                r = pymupdf.Rect(l["bbox"])
                cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
                if any(q.x0 <= cx <= q.x1 and q.y0 <= cy <= q.y1 for q in bs):
                    page.add_redact_annot(r, fill=False)
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                              text=pymupdf.PDF_REDACT_TEXT_REMOVE)
        # 2) es tapa amb blanc la caixa exacta dels dibuixos de cada quadre
        for q in bs:
            parts = [d["rect"] for d in page.get_drawings()
                     if q.x0 - 1 <= d["rect"].x0 and d["rect"].x1 <= q.x1 + 1 and q.y0 - 1 <= d["rect"].y0 and d["rect"].y1 <= q.y1 + 1]
            if parts:
                u = pymupdf.Rect(parts[0])
                for r in parts[1:]:
                    u |= r
                page.draw_rect(pymupdf.Rect(u.x0 - 1.5, u.y0 - 1.5, u.x1 + 1.5, u.y1 + 1.5), color=None, fill=(1, 1, 0.996), overlay=True)
    doc.save(out, garbage=3, deflate=True)
    return out
