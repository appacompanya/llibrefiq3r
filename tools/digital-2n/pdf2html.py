"""Reconstrueix l'HTML dels fulls de l'alumnat de 2n d'ESO a partir dels PDF (2n/docs/*.pdf).

Els fulls de 2n es van generar amb el mateix tipus de generador que els de 3r (HTML + Chromium → PDF), però
l'HTML original no es va conservar. Aquest script en refà un HTML equivalent, amb les mateixes peces que feien
servir els generadors de 3r, perquè després build_fitxes.py el converteixi en fitxes digitals:

  pregunta numerada   → <div class="q"><span class="n">N</span><div>…</div></div>
  línies de resposta  → <div class="lines"><div class="l"></div>…</div>
  títol de secció     → <h2><span class="k">A</span> …</h2>
  requadre de nota    → <div class="tip">…</div>
  taula               → <table> (les cel·les buides seran camps)
  requadre de dibuix  → <div class="box">etiqueta</div>
  espai en blanc      → <span class="blank"></span>
  casella             → ☐
  fórmules            → \\( … \\) (LaTeX, ho mostra KaTeX)
  unitats en fracció  → g/cm³ (unitfrac.py ho apila)
  figures i imatges   → <img src="fimg/…"> retallades del PDF

Ús: python3 pdf2html.py  (escriu _html/<clau>.html i ../../2n/digital/fimg/*.webp)
"""
import os, re, sys, json, io, html as H
import fitz
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
DOCS = os.path.join(ROOT, "2n", "docs")
OUTHTML = os.path.join(HERE, "_html")
IMGDIR = os.path.join(ROOT, "2n", "digital", "fimg")
sys.path.insert(0, HERE)
import unitfrac

INK = (0.12, 0.14, 0.16)
DOT = (0.73, 0.75, 0.77)
GRID = (0.6, 0.63, 0.66)
SOFT = (0.96, 0.96, 0.97)
WHITE = (1.0, 1.0, 1.0)

def rgb(c):
    return tuple(round(v, 2) for v in c) if c else None

def near(a, b, t=0.03):
    return a is not None and b is not None and all(abs(x - y) <= t for x, y in zip(a, b))

def esc(s):
    return H.escape(s, quote=False)

def inside(r, box, pad=1.5):
    return r.x0 >= box.x0 - pad and r.y0 >= box.y0 - pad and r.x1 <= box.x1 + pad and r.y1 <= box.y1 + pad

def center_in(r, box, pad=1.0):
    cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
    return box.x0 - pad <= cx <= box.x1 + pad and box.y0 - pad <= cy <= box.y1 + pad


# ---------------------------------------------------------------- spans de text
class Span:
    __slots__ = ("r", "t", "font", "size", "color", "bold", "math", "used", "y", "raw", "chip")
    def __init__(self, r, t, font, size, color):
        self.r = r; self.t = t; self.font = font; self.size = size; self.color = color
        self.bold = "Bold" in font or "Bol" in font
        self.math = font.startswith("KaTeX")
        self.used = False; self.raw = False; self.chip = False
        self.y = (r.y0 + r.y1) / 2


class Ch:
    __slots__ = ("r", "c", "font", "size", "color", "used", "by")
    def __init__(self, r, c, font, size, color, by=None):
        self.r = r; self.c = c; self.font = font; self.size = size; self.color = color; self.used = False
        self.by = by if by is not None else r.y1


def page_chars(p):
    out = []
    for b in p.get_text("rawdict")["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            for s in l["spans"]:
                font = s["font"].split("+")[-1]
                if (font.startswith("Type3") and s["bbox"][1] > 800) or s["size"] <= 1.5: continue      # peu de pàgina i separadors de KaTeX
                for c in s["chars"]:
                    if c["c"] == "\u200b": continue
                    out.append(Ch(fitz.Rect(c["bbox"]), c["c"], font, s["size"], s["color"], c["origin"][1]))
    # accents dibuixats a part (KaTeX): s'uneixen a la vocal de sota
    import unicodedata
    for a in [c for c in out if c.c in ACC]:
        cx = (a.r.x0 + a.r.x1) / 2
        v = [c for c in out if c is not a and c.c in "aeiouAEIOU" and c.r.x0 - 1 <= cx <= c.r.x1 + 1 and 0 <= c.by - a.by < 12]
        if v:
            t = min(v, key=lambda c: c.by - a.by); t.c = unicodedata.normalize("NFC", t.c + ACC[a.c]); a.used = True
    return [c for c in out if not c.used]


def spans_from(chars):
    """Caràcters (en ordre del PDF) → trossos contigus de la mateixa lletra."""
    out = []; cur = []
    def flush():
        if not cur: return
        t = "".join(c.c for c in cur)
        if t.strip():
            ink = [c for c in cur if c.c.strip()] or cur          # la caixa, sense els espais dels extrems
            r = fitz.Rect(ink[0].r); [r.include_rect(c.r) for c in ink]
            out.append(Span(r, t, cur[0].font, cur[0].size, cur[0].color))
    for c in chars:
        if c.used: continue
        if cur:
            a = cur[-1]
            same = (c.font == a.font and abs(c.size - a.size) < 0.3 and c.color == a.color)
            gap = c.r.x0 - a.r.x1
            ya, yc = (a.r.y0 + a.r.y1) / 2, (c.r.y0 + c.r.y1) / 2
            kxs = a.font.startswith("KaTeX")
            if not same or (kxs and a.c == " " and c.c != " ") or gap > a.size * (0.25 if kxs else 0.9) or gap < -a.size * (0.15 if kxs else 0.5) or abs(ya - yc) > a.size * 0.35:
                flush(); cur = []
        cur.append(c)
    flush()
    return out


ACC = {"ˊ": "\u0301", "´": "\u0301", "ˋ": "\u0300", "`": "\u0300", "¨": "\u0308", "ˆ": "\u0302"}

def merge_accents(spans):
    """Accents dibuixats a part (KaTeX: dissoluci + ˊ) → lletra accentuada."""
    import unicodedata
    for a in [s for s in spans if s.t.strip() in ACC]:
        cx = (a.r.x0 + a.r.x1) / 2
        tgt = [s for s in spans if s is not a and s.r.x0 - 1 <= cx <= s.r.x1 + 1 and 0 <= s.r.y1 - a.r.y1 < 14 and s.t.strip() not in ACC]
        if not tgt: continue
        t = min(tgt, key=lambda s: abs(s.y - a.y))
        n = len(t.t); i = max(0, min(n - 1, int((cx - t.r.x0) / max(1, t.r.width) * n)))
        # la lletra més propera que pot portar accent
        cand = [j for j in range(max(0, i - 2), min(n, i + 3)) if t.t[j] in "aeiouAEIOU"]
        if not cand: continue
        j = min(cand, key=lambda j: abs(j - i))
        t.t = t.t[:j] + unicodedata.normalize("NFC", t.t[j] + ACC[a.t.strip()]) + t.t[j + 1:]
        a.used = True
    return [s for s in spans if not s.used]


def page_spans(p, bars=()):
    chars = page_chars(p)
    extra = merge_fraction_chars(chars, bars)
    return spans_from(chars) + extra


# ---------------------------------------------------------------- dibuixos
class Draw:
    def __init__(self, d):
        self.d = d; self.r = fitz.Rect(d["rect"]); self.fill = rgb(d.get("fill")); self.stroke = rgb(d.get("color"))
        self.w = d.get("width") or 0; self.n = len(d["items"]); self.used = False


def classify(p, acc):
    D = [Draw(d) for d in p.get_drawings()]
    out = {"dots": [], "grid": [], "bars": [], "badges": [], "fills": [], "boxes": [], "checks": [], "rule": [], "frames": [], "chips": [], "other": []}
    for x in D:
        r = x.r
        if near(x.fill, DOT) and (r.height < 1.6): out["dots"].append(x); continue
        if near(x.fill, DOT) and x.n > 50 and r.width > 100:
            # zona de línies de punts dibuixada en un sol camí: una fila per cada altura
            ys = sorted({round(it[1].y) for it in x.d["items"] if it[0] == "l"})
            for y in ys:
                d = Draw({"rect": fitz.Rect(r.x0, y - 0.4, r.x1, y + 0.4), "fill": x.d.get("fill"), "color": None, "items": [], "width": 0})
                out["dots"].append(d)
            continue
        if near(x.fill, GRID) and (r.width < 1.6 or r.height < 1.6): out["grid"].append(x); continue
        if near(x.stroke, GRID) and x.w < 1.0 and (r.width < 1.6 or r.height < 1.6): out["grid"].append(x); continue
        if near(x.fill, acc) and r.height < 3.5 and r.width > 300: out["rule"].append(x); continue
        if (near(x.fill, INK) or near(x.fill, acc)) and r.height < 1.6 and r.width > 3: out["bars"].append(x); continue
        if near(x.fill, acc) and 10 < r.width < 26 and 10 < r.height < 26 and x.n > 8: out["badges"].append(x); continue
        if near(x.fill, acc) and r.height < 3.5 and r.width > 300: out["rule"].append(x); continue
        if near(x.fill, WHITE) and near(x.stroke, INK) and r.width > 30 and r.height > 25: out["boxes"].append(x); continue
        # xips: requadres petits amb vora i text a dins («fusió», «solidificació»…)
        if x.stroke and x.fill in (None, WHITE) and 9 < r.height < 24 and 14 < r.width < 160 and sum(1 for i in x.d["items"] if i[0] == "c") >= 4:
            out["chips"].append(x); continue
        if x.fill and r.width > 25 and r.height > 12 and x.n > 8 and not near(x.fill, (0, 0, 0)): out["fills"].append(x); continue
        if near(x.stroke, INK) and r.width > 30 and r.height > 25 and x.w >= 0.6 and x.fill is None: out["boxes"].append(x); continue
        # requadre de color (p. ex. «Seguretat» en vermell): nota amb vora
        if x.stroke and not near(x.stroke, INK) and x.fill is None and r.width > 120 and r.height > 30 and x.w >= 0.9 and sum(1 for i in x.d["items"] if i[0] == "c") >= 4:
            out["frames"].append(x); continue
        if x.stroke and 7 < r.width < 18 and 7 < r.height < 18 and abs(r.width - r.height) < 2 and x.fill is None: out["checks"].append(x); continue
        out["other"].append(x)
    return out


def dot_rows(dots, pad=2):
    """Agrupa els puntets en línies de resposta: [(y, x0, x1)]."""
    rows = {}
    for x in dots:
        y = round((x.r.y0 + x.r.y1) / 2)
        k = next((k for k in rows if abs(k - y) <= 1), y)
        rows.setdefault(k, []).append(x.r)
    out = []
    for y, rs in rows.items():
        x0 = min(r.x0 for r in rs); x1 = max(r.x1 for r in rs)
        if x1 - x0 > 40: out.append((y, x0, x1))
    return sorted(out)


# ---------------------------------------------------------------- fórmules i fraccions
KX_MAP = {"⋅": r"\cdot ", "×": r"\times ", "−": "-", "→": r"\rightarrow ", "≈": r"\approx ", "Δ": r"\Delta ", "ρ": r"\rho ",
          "°": r"^{\circ}", "π": r"\pi ", "≤": r"\le ", "≥": r"\ge ", "·": r"\cdot ", "µ": r"\mu ", "∆": r"\Delta ", "→": r"\to "}

def kx(t):
    o = ""
    for ch in t:
        if ch == "​": continue
        o += KX_MAP.get(ch, ch)
    return o


def merge_fraction_chars(chars, bars):
    """Fraccions apilades: caràcters damunt i sota d'una barra curta → un sol span «num/den» o \\dfrac."""
    out = []
    for b in bars:
        if b.used: continue
        br = b.r
        if br.width > 160 or br.width < 3: continue
        cx = lambda c: (c.r.x0 + c.r.x1) / 2
        cy = lambda c: (c.r.y0 + c.r.y1) / 2
        # numerador: línia base just damunt de la barra; denominador: línia base una lletra per sota
        kx_ = lambda c: c.font.startswith("KaTeX")
        up = [c for c in chars if not c.used and br.x0 - 1.5 <= cx(c) <= br.x1 + 1.5 and
              ((br.y0 - 5 <= c.by <= br.y0 + 0.8) or (kx_(c) and br.y0 - c.size * 0.95 <= cy(c) <= br.y0 - 0.5))]
        dn = [c for c in chars if not c.used and br.x0 - 1.5 <= cx(c) <= br.x1 + 1.5 and
              ((br.y1 + 2.5 <= c.by <= br.y1 + c.size * 1.05 + 1) or (kx_(c) and br.y1 + 0.5 <= cy(c) <= br.y1 + c.size * 0.95))]
        # caràcters enganxats a esquerra i dreta amb la mateixa línia base (cm³ és més ample que la barra)
        for grp in (up, dn):
            grow = True
            while grow and grp:
                grow = False
                lo = min(grp, key=lambda x: x.r.x0); hi = max(grp, key=lambda x: x.r.x1)
                for c in chars:
                    if c.used or c in grp or not c.c.strip(): continue
                    if abs(c.by - hi.by) < 1.6 or ((c.c in "²³⁻¹" or (c.font.startswith("KaTeX") and c.size < hi.size * 0.85)) and abs(c.by - hi.by) < 6):
                        if -1.5 <= c.r.x0 - hi.r.x1 < 2.2 or -1.5 <= lo.r.x0 - c.r.x1 < 1.6:
                            grp.append(c); grow = True; break
        if not [c for c in up if c.c.strip()] or not [c for c in dn if c.c.strip()]: continue
        # cada costat ha de ser una sola tira seguida (si no, són línies veïnes)
        def one_run(g):
            g = sorted(g, key=lambda c: c.r.x0)
            return all(g[i + 1].r.x0 - g[i].r.x1 < g[i].size * 0.6 for i in range(len(g) - 1))
        if not one_run(up) or not one_run(dn): continue
        up.sort(key=lambda c: c.r.x0); dn.sort(key=lambda c: c.r.x0)
        math = any(c.font.startswith("KaTeX") for c in up + dn)
        su = spans_from(up); sd = spans_from(dn)
        for c in up + dn: c.used = True
        b.used = True
        if math:
            t = r"\dfrac{" + kxjoin(su).strip() + "}{" + kxjoin(sd).strip() + "}"
        else:
            nt = "".join(c.c for c in up).strip(); dt = "".join(c.c for c in dn).strip()
            t = nt + "/" + (f"({dt})" if "·" in dt else dt)
        r = fitz.Rect(br.x0, br.y0 - 5, br.x1, br.y0 + 5)
        f0 = (up + dn)[0]
        sp = Span(r, t, "KaTeX_Main-Regular" if math else f0.font, max(c.size for c in up + dn) * (1 if math else 1.12), f0.color)
        sp.math = math; sp.raw = math
        out.append(sp)
    return out


def kxjoin(ss):
    """Uneix trossos de KaTeX amb exponents (més petits i més amunt)."""
    if not ss: return ""
    base = max(s.size for s in ss)
    o = ""
    for s in ss:
        if s.raw:
            t = s.t
        elif s.math and "Main" in s.font and re.search(r"[^\W\d_]", s.t):
            # unitats i paraules: lletra dreta, amb els espais
            parts = re.split(r"((?:[^\W\d_]|[°Ω])+[²³]?)", s.t)
            t = "".join((r"\mathrm{" + kx(x) + "}") if re.match(r"(?:[^\W\d_]|[°Ω])", x) else kx(x).replace(" ", r"\ ") for x in parts)
            t = re.sub(r"(\\[a-zA-Z]+)\\ ", r"\1 ", t)
        elif s.math:
            t = kx(s.t).replace(" ", r"\ ") if "Main" in s.font else kx(s.t).replace(" ", "")
            t = re.sub(r"(\\[a-zA-Z]+)\\ ", r"\1 ", t)
        else:
            t = s.t
        if s.size < base * 0.8 and s.math:
            big = [x for x in ss if x.size >= base * 0.95]
            bc = sum((x.r.y0 + x.r.y1) / 2 for x in big) / len(big) if big else s.y
            o = re.sub(r"(\\ |\s)+$", "", o)
            o += ("_{" if (s.r.y0 + s.r.y1) / 2 > bc else "^{") + t.strip() + "}"
        else:
            o += t
    o = re.sub(r"(\d)\\ (?=\d{3}\b)", r"\1\\,", o)      # 1 000 000 → 1\,000\,000
    o = re.sub(r"\\ ([=+\-]|\\cdot|\\times|\\rightarrow|\\to|\\approx)", r" \1", o)
    o = re.sub(r"([=+]|\\cdot |\\times |\\rightarrow |\\to |\\approx )\\ ", r"\1 ", o)
    o = re.sub(r"(\d)\s*\\mathrm", r"\1\\,\\mathrm", o)          # 1 kg → 1\,\mathrm{kg}
    o = re.sub(r"(\d),(\d)", r"\1{,}\2", o)                          # 2,7 sense espai després de la coma
    o = re.sub(r"(\\ |\s)+$", "", o)                                 # cap «\ » penjat al final
    return o


# ---------------------------------------------------------------- línies i paràgrafs
def lines_of(spans):
    """Agrupa els spans en línies visuals (mateixa alçada)."""
    ss = sorted(spans, key=lambda s: (s.y, s.r.x0))
    rows = []
    for s in ss:
        for row in rows:
            if abs(row["y"] - s.y) <= max(3.2, s.size * 0.6) or (s.math and abs(row["y"] - s.y) <= s.size * 0.7):
                row["s"].append(s); break
        else:
            rows.append({"y": s.y, "s": [s]})
    for row in rows:
        row["s"].sort(key=lambda s: s.r.x0)
        row["x0"] = min(s.r.x0 for s in row["s"]); row["x1"] = max(s.r.x1 for s in row["s"])
        row["y0"] = min(s.r.y0 for s in row["s"]); row["y1"] = max(s.r.y1 for s in row["s"])
        row["size"] = max(s.size for s in row["s"] if not s.math) if any(not s.math for s in row["s"]) else row["s"][0].size
    rows.sort(key=lambda r: r["y"])
    return rows


def row_html(row, acc_hex):
    """Una línia de text en HTML, amb negretes, fórmules i espais."""
    out = []; prev = None; math_buf = []
    def flush_math():
        if math_buf:
            out.append(r"\(" + kxjoin(math_buf).strip() + r"\)")
            math_buf.clear()
    base = row["size"]
    for s in row["s"]:
        gap = (s.r.x0 - prev.r.x1) if prev else 0
        if s.math:
            if prev is not None and not prev.math and gap > 1: out.append(" ")
            if prev is not None and prev.math and gap > base * 1.6:      # fórmules separades (en columnes)
                flush_math(); out.append(" &nbsp; ")
            # exponent d'un text normal (p. ex. cm³ ja és unicode; aquí només KaTeX)
            math_buf.append(s); prev = s; continue
        flush_math()
        t = s.t
        if prev is not None and gap > base * 0.18 and not out[-1:] == [" "] and not t.startswith(" "): out.append(" ")
        small = s.size < base * 0.84 and len(t.strip()) <= 12
        cy = (s.r.y0 + s.r.y1) / 2
        ref = [x for x in row["s"] if not x.math and x.size >= base * 0.95]
        rc = sum((x.r.y0 + x.r.y1) / 2 for x in ref) / len(ref) if ref else row["y"]
        sup = small and cy < rc - base * 0.12
        sub = small and cy > rc + base * 0.12
        txt = esc(t)
        if sup: txt = "<sup>" + txt.strip() + "</sup>"
        if sub: txt = "<sub>" + txt.strip() + "</sub>"
        if (sup or sub) and out and out[-1] == " ": out.pop()
        if s.bold or (s.color == acc_hex and s.bold): txt = "<b>" + txt + "</b>"
        if s.chip: txt = '<span class="chip">' + txt.strip() + "</span>"
        out.append(txt); prev = s
    flush_math()
    h = "".join(out)
    h = re.sub(r"</b>(\s*)<b>", r"\1", h)
    return h.strip()


def paragraphs(rows, acc_hex):
    """Línies → paràgrafs (i llistes amb pics)."""
    paras = []; cur = None
    for r in rows:
        t = row_html(r, acc_hex)
        if not t: continue
        allmath = all(s.math for s in r["s"])
        if allmath or (cur and cur.get("math")):
            cur = {"t": t, "y0": r["y0"], "y1": r["y1"], "x0": r["x0"], "size": r["size"], "li": False, "hard": True, "math": allmath}
            paras.append(cur); continue
        bullet = re.match(r"^(•|·|–|-)\s+", re.sub(r"<[^>]+>", "", t))
        if cur and not bullet and r["y0"] - cur["y1"] < cur["size"] * 0.95 and abs(r["x0"] - cur["x0"]) < 30 and not cur.get("hard"):
            cur["t"] += " " + t; cur["y1"] = r["y1"]; continue
        if cur and cur.get("li") and not bullet and r["y0"] - cur["y1"] < cur["size"] * 0.95 and r["x0"] > cur["x0"] + 2:
            cur["t"] += " " + t; cur["y1"] = r["y1"]; continue
        cur = {"t": re.sub(r"^(<b>)?(•|·)\s*", r"\1", t) if bullet else t, "y0": r["y0"], "y1": r["y1"], "x0": r["x0"] + (8 if bullet else 0), "size": r["size"], "li": bool(bullet)}
        paras.append(cur)
    out = []; ul = []
    for p in paras:
        if p["li"]: ul.append(f"<li>{p['t']}</li>"); continue
        if ul: out.append("<ul>" + "".join(ul) + "</ul>"); ul = []
        out.append(p["t"])
    if ul: out.append("<ul>" + "".join(ul) + "</ul>")
    return out


# ---------------------------------------------------------------- taules
def build_table(grid, fills, spans, acc_hex, tint_ok):
    xs = sorted({round(g.r.x0) for g in grid if g.r.width < 1.6} | {round(g.r.x1) for g in grid if g.r.width < 1.6})
    ys = sorted({round(g.r.y0) for g in grid if g.r.height < 1.6} | {round(g.r.y1) for g in grid if g.r.height < 1.6})
    def dedup(v):
        o = []
        for a in v:
            if not o or a - o[-1] > 2.5: o.append(a)
            else: o[-1] = a
        return o
    xs = dedup(xs); ys = dedup(ys)
    if len(xs) < 2 or len(ys) < 2: return None, None
    box = fitz.Rect(xs[0], ys[0], xs[-1], ys[-1])
    # parets verticals: per detectar cel·les combinades
    vert = [g.r for g in grid if g.r.width < 1.6]
    def has_wall(x, y0, y1):
        return any(abs((v.x0 + v.x1) / 2 - x) < 2.5 and v.y0 <= y0 + 2 and v.y1 >= y1 - 2 for v in vert)
    head_rows = set()
    for f in fills:
        if inside(f.r, box, 2) and f.r.height < 60:
            for i in range(len(ys) - 1):
                if abs(f.r.y0 - ys[i]) < 3 and f.r.width > (box.width / max(1, len(xs) - 1)) * 0.5: head_rows.add(i)
    rows = []
    for i in range(len(ys) - 1):
        tr = []; j = 0
        while j < len(xs) - 1:
            k = j + 1
            while k < len(xs) - 1 and not has_wall(xs[k], ys[i], ys[i + 1]): k += 1
            cell = fitz.Rect(xs[j], ys[i], xs[k], ys[i + 1])
            ins = [s for s in spans if not s.used and center_in(s.r, cell)]
            for s in ins: s.used = True
            txt = " ".join(paragraphs(lines_of(ins), acc_hex)) if ins else ""
            th = i in head_rows
            span = f' colspan="{k - j}"' if k - j > 1 else ""
            h = cell.height
            tag = "th" if th else "td"
            attr = span + (' style="height:9mm"' if not th and not txt and h > 18 else "")
            tr.append(f"<{tag}{attr}>{txt}</{tag}>")
            j = k
        rows.append("<tr>" + "".join(tr) + "</tr>")
    return "<table>" + "".join(rows) + "</table>", box


# ---------------------------------------------------------------- figures
def crop(p, rect, key, n, marks=(), dpi=170):
    rect = fitz.Rect(rect) & p.rect
    pix = p.get_pixmap(clip=rect, dpi=dpi, alpha=False)
    im = Image.open(io.BytesIO(pix.tobytes("png")))
    if marks:
        # números als espais en blanc del diagrama, per relacionar-los amb les caselles de sota
        from PIL import ImageDraw, ImageFont
        dr = ImageDraw.Draw(im); k = dpi / 72; R = round(6.5 * k)
        try: fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", round(8 * k))
        except Exception: fnt = ImageFont.load_default()
        for x, y, t in marks:
            cx, cy = (x - rect.x0) * k - R * 0.2, (y - rect.y0) * k - R * 1.1
            cx = max(R, cx); cy = max(R, cy)
            dr.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(31, 35, 40))
            dr.text((cx, cy), t, fill=(255, 255, 255), font=fnt, anchor="mm")
    name = f"{key}-{n}.webp"
    os.makedirs(IMGDIR, exist_ok=True)
    im.save(os.path.join(IMGDIR, name), "WEBP", quality=82, method=6)
    w_mm = rect.width / 72 * 25.4
    return f'<img src="fimg/{name}" alt="" style="width:{round(w_mm * 1.3, 1)}mm;max-width:100%">'


def cluster(rects, gap=8):
    # les línies de gruix zero són rectangles «buits» per a PyMuPDF: els engruixim una mica
    rs = [fitz.Rect(r.x0 - 0.5, r.y0 - 0.5, r.x1 + 0.5, r.y1 + 0.5) for r in rects]
    changed = True
    while changed:
        changed = False
        out = []
        while rs:
            a = rs.pop()
            i = 0
            while i < len(rs):
                b = rs[i]
                if (a.x0 - gap <= b.x1 and b.x0 - gap <= a.x1 and a.y0 - gap <= b.y1 and b.y0 - gap <= a.y1):
                    a.include_rect(b); rs.pop(i); changed = True
                else: i += 1
            out.append(a)
        rs = out
    return rs


# ---------------------------------------------------------------- composició d'una pàgina
def closed(x):
    it = x.d["items"]
    return (len(it) == 1 and it[0][0] == "re") or sum(1 for i in it if i[0] == "c") >= 4 or (len(it) >= 4 and it[0][0] == "l" and x.n <= 6 and abs(x.r.width) > 30)


class El:
    """Element de la pàgina en ordre de lectura."""
    def __init__(self, kind, r, **kw):
        self.kind = kind; self.r = fitz.Rect(r); self.__dict__.update(kw)


def page_elements(p, key, acc, acc_hex, state, first, plain_figs=True):
    C = classify(p, acc)
    spans = merge_accents(page_spans(p, C["bars"]))
    for c in C["chips"]:
        for s in spans:
            if center_in(s.r, c.r, 1): s.chip = True
    els = []
    top = 0
    # capçalera (només a la primera pàgina): fins a la ratlla de color
    if first:
        rule = min(C["rule"], key=lambda x: x.r.y0, default=None)
        top = rule.r.y1 + 1 if rule else 100
        head = [s for s in spans if s.r.y0 < top - 3]
        big = [s for s in head if s.size >= max(x.size for x in head) - 0.5] if head else []
        state["title"] = re.sub(r"\s+", " ", " ".join(s.t for s in sorted(big, key=lambda s: (round(s.y), s.r.x0)))).strip()
        for s in head: s.used = True
        # entradeta: text gris just a sota de la ratlla
        intro = [s for s in spans if not s.used and s.color == 0x5d646d and s.r.y0 < top + 40 and s.r.y0 >= top]
        if intro:
            y1 = max(s.r.y1 for s in intro)
            more = [s for s in spans if not s.used and s.color == 0x5d646d and y1 <= s.r.y0 < y1 + 14]
            intro += more
            state["intro"] = " ".join(paragraphs(lines_of(intro), acc_hex))
            for s in intro: s.used = True
    else:
        # capçalera de continuació (p. ex. full de ruta) i ratlla
        rule = min(C["rule"], key=lambda x: x.r.y0, default=None)
        if rule and rule.r.y0 < 120:
            for s in spans:
                if s.r.y0 < rule.r.y0 - 3: s.used = True
            top = rule.r.y1
    spans = [s for s in spans if not s.used and s.r.y0 < 805]

    # insígnies: preguntes (número) i seccions (lletra)
    for b in C["badges"]:
        if b.r.y0 < top: continue
        lab = [s for s in spans if center_in(s.r, b.r, 1) and s.color == 0xffffff]
        t = "".join(s.t for s in lab).strip()
        for s in lab: s.used = True
        if not t: continue
        if t.isdigit():
            els.append(El("q", b.r, n=t))
        else:
            row = [s for s in spans if not s.used and abs(s.y - (b.r.y0 + b.r.y1) / 2) < 6 and s.r.x0 > b.r.x1 - 1 and s.r.x0 < b.r.x1 + 400]
            for s in row: s.used = True
            els.append(El("h2", fitz.Rect(b.r).include_rect(fitz.Rect(min([s.r for s in row], key=lambda r: r.x0) if row else b.r)), k=t, text=esc(" ".join(s.t for s in sorted(row, key=lambda s: s.r.x0)).strip())))

    # taules
    groups = []
    for g in C["grid"]:
        for gr in groups:
            if fitz.Rect(gr["r"]).intersects(fitz.Rect(g.r.x0 - 3, g.r.y0 - 3, g.r.x1 + 3, g.r.y1 + 3)):
                gr["g"].append(g); gr["r"].include_rect(g.r); break
        else:
            groups.append({"g": [g], "r": fitz.Rect(g.r)})
    # fusiona grups que es toquen
    merged = True
    while merged:
        merged = False
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                a, b = groups[i]["r"], groups[j]["r"]
                if fitz.Rect(a.x0 - 3, a.y0 - 3, a.x1 + 3, a.y1 + 3).intersects(b):
                    groups[i]["g"] += groups[j]["g"]; groups[i]["r"].include_rect(b); groups.pop(j); merged = True; break
            if merged: break
    tables = []
    for gr in groups:
        if gr["r"].width < 40 or gr["r"].height < 12: continue
        tfills = [x for x in C["fills"] + C["other"] if x.fill and not near(x.fill, WHITE) and not near(x.fill, INK) and x.r.height > 6]
        h, box = build_table(gr["g"], tfills, spans, acc_hex, True)
        if h:
            els.append(El("table", box, html=h)); tables.append(box)
    spans = [s for s in spans if not s.used]
    fills = [f for f in C["fills"] if not any(inside(f.r, t, 3) for t in tables) and f.r.y0 >= top - 2]

    # línies de resposta
    rows = [r for r in dot_rows(C["dots"]) if r[0] > top]
    used_rows = set()
    for i, (y, x0, x1) in enumerate(rows):
        if i in used_rows: continue
        grp = [(y, x0, x1)]; used_rows.add(i)
        for j in range(i + 1, len(rows)):
            y2, a, b = rows[j]
            if j in used_rows: continue
            if abs(a - x0) < 4 and abs(b - x1) < 4 and 0 < y2 - grp[-1][0] < 30 and not any(s for s in spans if grp[-1][0] + 3 < s.y < y2 - 3 and s.r.x0 < x1 and s.r.x1 > x0):
                grp.append((y2, a, b)); used_rows.add(j)
        n = len(grp)
        if n > 2 and (grp[-1][0] - grp[0][0]) / (n - 1) < 12:     # quadriculat de punts, no línies
            n = max(2, round((grp[-1][0] - grp[0][0]) / 21) + 1)
        els.append(El("lines", fitz.Rect(x0, grp[0][0] - 14, x1, grp[-1][0] + 1), n=n))

    # caselles
    for c in C["checks"]:
        els.append(El("text", c.r, span=Span(c.r, "☐", "AH", 10, 0x1f2328)))

    # figures: la resta de dibuixos i les imatges
    figr = [x.r for x in C["other"] if x.r.y0 >= top and x.r.y1 < 805 and x.r.width + x.r.height > 4 and not any(inside(x.r, t, 2) for t in tables)]
    # eixos de gràfiques (línies llargues o verticals d'inxa)
    figr += [b.r for b in C["bars"] if not b.used and b.r.y0 >= top and (b.r.width > 260)]
    figr += [x.r for x in C["other"] if near(x.stroke, INK) and x.r.height > 40 and x.r.width < 2]
    figr += [x.r for x in C["boxes"] if not closed(x) and x.r.y0 >= top]
    for b in p.get_text("dict")["blocks"]:
        if b["type"] == 1 and b["bbox"][1] >= top: figr.append(fitz.Rect(b["bbox"]))
    frs = [fr for fr in cluster(figr, 6) if fr.width * fr.height >= 120]
    # figures petites de la mateixa fila (p. ex. tres gots A, B, C) → una sola figura
    merged = True
    while merged:
        merged = False
        for i in range(len(frs)):
            for j in range(i + 1, len(frs)):
                a, b = frs[i], frs[j]
                ov = min(a.y1, b.y1) - max(a.y0, b.y0)
                gap = max(a.x0, b.x0) - min(a.x1, b.x1)
                txt_between = any(not s.used and s.size >= 9 and s.r.y0 < max(a.y1, b.y1) and s.r.y1 > min(a.y0, b.y0) and min(a.x1, b.x1) < s.r.x0 < max(a.x0, b.x0) and len(s.t.strip()) > 14 for s in spans)
                if ov > 0.5 * min(a.height, b.height) and gap < 160 and not txt_between:
                    frs[i] = fitz.Rect(a).include_rect(b); frs.pop(j); merged = True; break
            if merged: break
    for fr in frs:
        if fr.width * fr.height < 500 or fr.width < 14 or fr.height < 14: continue
        # diagrames: caixes de color petites i espais en blanc enganxats a la figura en formen part
        grow = True
        while grow:
            grow = False
            ex = fitz.Rect(fr.x0 - 14, fr.y0 - 14, fr.x1 + 14, fr.y1 + 14)
            for f in fills:
                if getattr(f, "infig", False) or near(f.fill, WHITE): continue
                if f.r.width < 170 and f.r.height < 70 and f.r.intersects(ex):
                    fr.include_rect(f.r); f.infig = True; grow = True
        ex = fitz.Rect(fr.x0 - 14, fr.y0 - 14, fr.x1 + 14, fr.y1 + 14)
        blanks = [s for s in spans if not s.used and re.fullmatch(r"\s*_{3,}\s*", s.t) and inside(s.r, fitz.Rect(ex.x0 - 30, ex.y0, ex.x1 + 30, ex.y1))]
        for b in blanks: fr.include_rect(b.r); b.used = True
        tipz = [f.r for f in fills if not getattr(f, "infig", False) and not near(f.fill, WHITE) and not inside(fr, f.r, 2)]
        # etiquetes petites dins de la figura (o enganxades) en formen part
        lab = [s for s in spans if not s.used and not any(center_in(s.r, t) for t in tipz) and ((((not s.bold and s.size < 10) or s.size < 7 or (s.size < 9 and len(s.t.strip()) <= 24)) and inside(s.r, fitz.Rect(fr.x0 - 42, fr.y0 - 10, fr.x1 + 60, fr.y1 + 16))) or
                                               (len(s.t.strip()) <= 14 and inside(s.r, fitz.Rect(fr.x0 - 6, fr.y0 - 6, fr.x1 + 6, fr.y1 + 6))) or
                                               (len(s.t.strip()) <= 3 and inside(s.r, fitz.Rect(fr.x0 - 6, fr.y0 - 6, fr.x1 + 6, fr.y1 + 22))) or
                                               (not s.bold and len(s.t.strip()) <= 12 and inside(s.r, fitz.Rect(fr.x0 - 42, fr.y0 - 10, fr.x1 + 60, fr.y1 + 26))))]
        r = fitz.Rect(fr)
        for s in lab: r.include_rect(s.r); s.used = True
        for s in spans:
            if not s.used and center_in(s.r, r, 0): s.used = True
        els.append(El("fig", r, src=None, blanks=[fitz.Rect(b.r.x0, b.r.y1 - 2, b.r.x1, b.r.y1) for b in sorted(blanks, key=lambda b: (round(b.r.y0 / 8), b.r.x0))]))
    # espais en blanc dins del text (línia fina d'inxa d'uns quants mm)
    for b in C["bars"]:
        if b.used or b.r.y0 < top or not (25 < b.r.width < 260): continue
        if any(inside(b.r, t, 2) for t in tables): continue
        sp = Span(fitz.Rect(b.r.x0, b.r.y0 - 9, b.r.x1, b.r.y0), "\x00", "AH", 10, 0x1f2328)
        els.append(El("text", sp.r, span=sp)); b.used = True

    # requadres de nota (fons de color) i requadres de dibuix (vora negra)
    for f in fills:
        if near(f.fill, WHITE) or getattr(f, "infig", False): continue
        els.append(El("tip", f.r, fill=f.fill))
    for f in C["frames"]:
        if f.r.y0 >= top: els.append(El("tip", f.r, fill=None, border=f.stroke))
    figs = [e.r for e in els if e.kind == "fig"]
    for b in C["boxes"]:
        if b.r.y0 < top or not closed(b): continue
        if any(inside(b.r, t, 2) for t in tables): continue
        # un requadre que toca una figura (got, balança…) és part del dibuix
        hit = [e for e in els if e.kind == "fig" and b.r.intersects(e.r)]
        if hit:
            hit[0].r.include_rect(b.r); continue
        # etiqueta just a sota del requadre (p. ex. «Aigua líquida»)
        lab = [s for s in spans if not s.used and b.r.y1 - 2 <= s.r.y0 <= b.r.y1 + 18 and s.r.x0 >= b.r.x0 - 10 and s.r.x1 <= b.r.x1 + 10 and len(s.t.strip()) < 40]
        for s in lab: s.used = True
        els.append(El("box", b.r, label=" ".join(x.t.strip() for x in sorted(lab, key=lambda x: x.r.x0))))

    # una figura dins d'una altra (p. ex. una fila de molècules dins d'un requadre absorbit) és la mateixa
    fe = [e for e in els if e.kind == "fig"]
    for e in fe:
        if any(o is not e and o in els and inside(e.r, o.r, 3) and o.r.width * o.r.height > e.r.width * e.r.height for o in fe):
            els.remove(e)
    # etiquetes curtes just a sota d'una figura que ha crescut amb els requadres
    for e in els:
        if e.kind != "fig": continue
        y1 = e.r.y1
        for s in spans:
            if not s.used and s.size < 10 and len(s.t.strip()) <= 24 and -2 <= s.r.y0 - y1 <= 7 and s.r.x0 >= e.r.x0 - 6 and s.r.x1 <= e.r.x1 + 6:
                e.r.include_rect(s.r); s.used = True

    if state.get("skipfig"):
        # diana: els números del voltant del gràfic (la diana la dibuixa el llibre digital)
        for s in spans:
            if s.t.strip().isdigit() and len(s.t.strip()) <= 2 and s.bold: s.used = True
    spans = [s for s in spans if not s.used]
    for s in spans: els.append(El("text", s.r, span=s))
    return els


def render(p, els, key, acc_hex, state, region=None, depth=0):
    """Ordena i converteix en HTML els elements d'una regió."""
    out = []
    if region is None: region = p.rect
    # contenidors: notes i requadres; el que hi ha dins s'hi renderitza
    conts = [e for e in els if e.kind in ("tip", "box")]
    conts.sort(key=lambda e: e.r.width * e.r.height, reverse=True)
    owned = {}
    for e in els:
        if e.kind in ("tip", "box"):
            parent = next((c for c in reversed(conts) if c is not e and inside(e.r, c.r, 1) and c.r.width * c.r.height > e.r.width * e.r.height), None)
        else:
            parent = next((c for c in reversed(conts) if inside(e.r, c.r, 2)), None)
        owned.setdefault(id(parent) if parent else None, []).append(e)
    top = owned.get(None, [])
    return render_flow(p, top, owned, key, acc_hex, state)


def render_flow(p, items, owned, key, acc_hex, state):
    items = sorted(items, key=lambda e: (e.r.y0, e.r.x0))
    out = []
    qs = [e for e in items if e.kind == "q"]
    # cos de cada pregunta: el que hi ha a la dreta de la insígnia fins a la pregunta o secció següent
    stops = sorted([e.r.y0 for e in items if e.kind in ("q", "h2")])
    body_of = {}
    claimed = set()
    for q in qs:
        nxt = min([y for y in stops if y > q.r.y0 + 2], default=1e9)
        body = []
        for e in items:
            if e is q or id(e) in claimed: continue
            if e.r.y0 >= q.r.y0 - 4 and e.r.y0 < nxt - 2 and e.r.x0 >= q.r.x1 - 2:
                body.append(e)
        # el cos s'acaba al primer element que comença al marge esquerre (a l'altura de la insígnia)
        lefts = [e.r.y0 for e in items if e.r.y0 > q.r.y1 + 2 and e.r.y0 < nxt and e.r.x0 < q.r.x1 - 2 and e.kind != "q"]
        if lefts:
            cut = min(lefts); body = [e for e in body if e.r.y0 < cut]
        for e in body: claimed.add(id(e))
        body_of[id(q)] = body
    seq = [e for e in items if id(e) not in claimed]
    out = render_seq(p, seq, owned, key, acc_hex, state, body_of)
    return out


def render_seq(p, seq, owned, key, acc_hex, state, body_of):
    """Elements en ordre vertical; els que queden de costat van en columnes."""
    seq = sorted(seq, key=lambda e: (e.r.y0, e.r.x0))
    html = []
    i = 0
    while i < len(seq):
        e = seq[i]
        # banda: elements que se solapen verticalment amb aquest
        band = [e]; y1 = e.r.y1
        j = i + 1
        while j < len(seq) and seq[j].r.y0 < y1 - 3:
            band.append(seq[j]); y1 = max(y1, seq[j].r.y1); j += 1
        cols = split_cols(band)
        if len(cols) > 1 and not all(x.kind == "text" for x in band) and not any(x.kind == "q" for x in band):
            html.append('<div class="two" style="grid-template-columns:' + " ".join(f"{max(1, round(c[1] - c[0]))}fr" for c in cols) + '">' +
                        "".join("<div>" + "".join(render_seq(p, c[2], owned, key, acc_hex, state, body_of)) + "</div>" for c in cols) + "</div>")
            i = j; continue
        # text seguit → paràgrafs
        if e.kind == "text":
            run = []
            while i < len(seq) and seq[i].kind == "text":
                run.append(seq[i].span); i += 1
            for t in paragraphs(lines_of(run), acc_hex):
                html.append(t if t.startswith("<ul>") else f"<p>{t}</p>")
            continue
        html.append(render_one(p, e, owned, key, acc_hex, state, body_of)); i += 1
    return html


def split_cols(band):
    """Divideix una banda en columnes si hi ha un buit vertical que la travessa."""
    xs = sorted(band, key=lambda e: e.r.x0)
    cols = []
    for e in xs:
        for c in cols:
            if e.r.x0 < c[1] - 4 and e.r.x1 > c[0] + 4:
                c[0] = min(c[0], e.r.x0); c[1] = max(c[1], e.r.x1); c[2].append(e); break
        else:
            cols.append([e.r.x0, e.r.x1, [e]])
    # re-fusiona columnes que ara se solapen
    cols.sort(key=lambda c: c[0])
    out = []
    for c in cols:
        if out and c[0] < out[-1][1] - 4:
            out[-1][1] = max(out[-1][1], c[1]); out[-1][2] += c[2]
        else: out.append(c)
    return out


def render_one(p, e, owned, key, acc_hex, state, body_of):
    k = e.kind
    if k == "q":
        inner = render_seq(p, body_of.get(id(e), []), owned, key, acc_hex, state, body_of)
        return f'<div class="q"><span class="n">{e.n}</span><div>{"".join(inner)}</div></div>'
    if k == "h2":
        return f'<h2><span class="k">{esc(e.k)}</span> {e.text}</h2>'
    if k == "table":
        return e.html
    if k == "lines":
        return '<div class="lines">' + '<div class="l"></div>' * e.n + "</div>"
    if k == "fig":
        state["nimg"] += 1
        if state.get("skipfig"): return ""
        rr = fitz.Rect(e.r.x0 - 2, e.r.y0 - 2, e.r.x1 + 2, e.r.y1 + 2)
        bl = getattr(e, "blanks", [])
        h = "<figure>" + crop(p, rr, key, state["nimg"], [(b.x0, b.y0, str(i + 1)) for i, b in enumerate(bl)]) + "</figure>"
        if bl:
            h += "<p>" + " ".join(f"<b>{i + 1}</b> \x00" for i in range(len(bl))) + "</p>"
        return h
    if k in ("tip", "box"):
        kids = owned.get(id(e), [])
        inner = "".join(render_flow(p, kids, owned, key, acc_hex, state))
        if k == "box":
            # requadre de dibuix: només l'etiqueta
            lab = re.sub(r"<[^>]+>", "", inner).strip()
            if kids and any(x.kind in ("table", "lines", "q") for x in kids):
                return f'<div class="tip" style="background:#fff;border:1px solid var(--line)">{inner}</div>'
            return f'<div class="box">{esc(lab or getattr(e, "label", ""))}</div>'
        style = ""
        if getattr(e, "border", None):
            c = e.border
            style = f' style="background:var(--surface);border:2px solid rgb({round(c[0]*255)},{round(c[1]*255)},{round(c[2]*255)})"'
        elif e.fill and not near(e.fill, SOFT):
            style = f' style="background:rgb({round(e.fill[0]*255)},{round(e.fill[1]*255)},{round(e.fill[2]*255)})"'
        if not re.sub(r"<[^>]+>", "", inner).strip() and "<img" not in inner: return ""
        return f'<div class="tip"{style}>{inner}</div>'
    if k == "text":
        return f"<p>{esc(e.span.t)}</p>"
    return ""


def fix_blanks(h):
    return h.replace("\x00", '<span class="blank"></span>')


# ---------------------------------------------------------------- full de ruta
def ruta_html(d, key, sda, acc, acc_hex):
    cards = []
    for pn, p in enumerate(d):
        spans = page_spans(p)
        C = classify(p, acc)
        boxes = sorted([b for b in C["boxes"] if b.r.width > 300 and b.r.height > 50], key=lambda b: b.r.y0)
        for b in boxes:
            inn = [s for s in spans if center_in(s.r, b.r)]
            badge = next((x for x in C["badges"] if inside(x.r, b.r, 2)), None)
            n = "".join(s.t for s in inn if badge and center_in(s.r, badge.r, 1)).strip()
            ttl = [s for s in inn if s.bold and s.color == 0x1f2328 and badge and abs(s.y - (badge.r.y0 + badge.r.y1) / 2) < 6]
            tag = [s for s in inn if s.bold and s.color == acc_hex and badge and abs(s.y - (badge.r.y0 + badge.r.y1) / 2) < 6]
            labs = [s for s in inn if s.bold and s.color == 0x1f2328 and s not in ttl]
            l1 = next((s.t for s in labs if s.r.x0 < b.r.x0 + (b.r.width / 2)), "Avui he fet").strip()
            l2 = next((s.t for s in labs if s.r.x0 >= b.r.x0 + (b.r.width / 2)), "He après").strip()
            nl = len([r for r in dot_rows(C["dots"]) if b.r.y0 < r[0] < b.r.y1 and r[1] < b.r.x0 + b.r.width * 0.6 and r[1] > b.r.x0 + b.r.width * 0.2])
            L = '<div class="l"></div>' * max(2, nl)
            img = f"../img/sda{sda}-s{n}.webp"
            if not os.path.exists(os.path.join(ROOT, "2n", "img", f"sda{sda}-s{n}.webp")): img = ""
            cards.append(f'<div class="c"><div class="t"><span class="b">{esc(n)}</span><h3>{esc(" ".join(s.t for s in ttl).strip())}</h3>'
                         f'<span class="tag">{esc(" ".join(s.t for s in tag).strip())}</span><span class="ck"></span></div>'
                         f'<div class="im">{f"<img src={chr(34)}{img}{chr(34)} alt={chr(34)}{chr(34)}>" if img else ""}</div>'
                         f'<div class="w"><div class="col"><div class="lb">{esc(l1)}</div>{L}</div>'
                         f'<div class="col"><div class="lb">{esc(l2)}</div>{L}</div></div></div>')
    return '<div class="list">' + "".join(cards) + "</div>"


# ---------------------------------------------------------------- document sencer
def convert(path, key):
    d = fitz.open(path)
    sda = int(re.search(r"sda(\d)", os.path.basename(path)).group(1))
    # color de la SdA: el de les insígnies
    from collections import Counter
    cnt = Counter()
    for p in d:
        white = [fitz.Rect(s["bbox"]) for b in p.get_text("dict")["blocks"] if b["type"] == 0 for l in b["lines"] for s in l["spans"] if s["color"] == 0xffffff and s["text"].strip()]
        for x in p.get_drawings():
            r = x["rect"]
            if x.get("fill") and 10 < r.width < 26 and 10 < r.height < 26 and len(x["items"]) > 8 and any(center_in(w, r, 1) for w in white): cnt[rgb(x["fill"])] += 1
    acc = cnt.most_common(1)[0][0] if cnt else (0.72, 0.23, 0.48)
    acc_hex = (round(acc[0] * 255) << 16) | (round(acc[1] * 255) << 8) | round(acc[2] * 255)
    # el color del text pot diferir en una unitat: el prenem del títol de capçalera
    sp0 = page_spans(d[0])
    kick = next((s for s in sp0 if s.bold and s.size < 10 and s.r.y0 < 60 and s.color not in (0x1f2328, 0xffffff)), None)
    if kick: acc_hex = kick.color
    state = {"title": key, "intro": "", "nimg": 0, "skipfig": "diana" in path}
    body = []
    if "full-de-ruta" in path:
        page_elements(d[0], key, acc, acc_hex, state, True)
        q2 = state.get("intro", "")
        body.append(ruta_html(d, key, sda, acc, acc_hex))
        h = f'<div class="head"><div><h1>{esc(state["title"])}</h1><p class="q2">{esc(re.sub("<[^>]+>", "", q2))}</p></div></div>' + "".join(body)
        return finish(h, state)
    for pn, p in enumerate(d):
        els = page_elements(p, key, acc, acc_hex, state, pn == 0)
        body += render(p, els, key, acc_hex, state)
    h = f'<div class="head"><div><h1>{esc(state["title"])}</h1></div></div>'
    if state.get("intro"): h += f'<p class="intro">{state["intro"]}</p>'
    h += "".join(body)
    return finish(h, state)


def finish(h, state):
    h = fix_blanks(h)
    h = unitfrac.frac_units(h)
    return f'<!doctype html><html lang="ca"><head><meta charset="utf-8"></head><body>{h}</body></html>'


SKIP = re.compile(r"rubriques|mapa-conceptual|adaptada|equivalencies")

def main(only=None):
    os.makedirs(OUTHTML, exist_ok=True)
    tpl = open(os.path.join(ROOT, "2n", "index.html"), encoding="utf-8").read()
    D = json.loads(re.search(r"^const D = (\{.*?\});$", tpl, re.M).group(1))
    for k, v in D.items():
        if v.get("t") or SKIP.search(v["f"]): continue
        if only and k not in only: continue
        try:
            h = convert(os.path.join(DOCS, v["f"]), "n2" + k)
        except Exception as e:
            import traceback; traceback.print_exc(); print("ERR", k, e); continue
        open(os.path.join(OUTHTML, k + ".html"), "w", encoding="utf-8").write(h)
        print(k, len(h))


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
