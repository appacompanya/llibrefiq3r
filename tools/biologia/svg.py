"""Petites eines per dibuixar les figures del llibre de Biologia en SVG.

Totes les figures fan servir la mateixa paleta i la mateixa tipografia (la del llibre, heretada
de la pàgina perquè l'SVG va incrustat). Les mides de text són en unitats del viewBox; les figures
es dissenyen a uns 640 px d'amplada i s'escalen.
"""
from html import escape

INK = "#1b1f24"
MUTED = "#5b636e"
LINE = "#9aa1aa"
PAPER = "#ffffff"

# colors de tema (forts i clars)
C = {
    "verd": ("#2e7d4f", "#e3f2e8"),
    "blau": ("#2f6fb5", "#e4eefa"),
    "teal": ("#12857a", "#dff3f0"),
    "taronja": ("#c4651a", "#fbeadb"),
    "vermell": ("#b23a3a", "#f9e1e1"),
    "lila": ("#6a4fa0", "#ece6f6"),
    "groc": ("#a67c12", "#fbf1d6"),
    "gris": ("#59606a", "#eef0f2"),
    "rosa": ("#b83a7a", "#f8e2ee"),
    "marro": ("#8a5a2b", "#f3e8dc"),
}


def col(name):
    return C[name][0]


def light(name):
    return C[name][1]


class Fig:
    def __init__(self, w, h, title=""):
        self.w, self.h, self.title = w, h, title
        self.items = []
        self.markers = set()

    # ---------- primitives ----------
    def raw(self, s):
        self.items.append(s)
        return self

    def rect(self, x, y, w, h, fill="none", stroke=INK, sw=1.6, rx=8, dash=None, op=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' opacity="{op}"' if op is not None else ""
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')
        return self

    def circle(self, cx, cy, r, fill="none", stroke=INK, sw=1.6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
        return self

    def ellipse(self, cx, cy, rx, ry, fill="none", stroke=INK, sw=1.6, dash=None, rot=0):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
        self.items.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{t}/>')
        return self

    def line(self, x1, y1, x2, y2, stroke=INK, sw=1.6, dash=None, cap="round"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')
        return self

    def path(self, d, fill="none", stroke=INK, sw=1.6, dash=None, extra=""):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{da} {extra}/>')
        return self

    def poly(self, pts, fill="none", stroke=INK, sw=1.6, close=True):
        p = " ".join(f"{x},{y}" for x, y in pts)
        tag = "polygon" if close else "polyline"
        self.items.append(f'<{tag} points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')
        return self

    def _marker(self, color):
        mid = "a" + color.replace("#", "")
        if mid not in self.markers:
            self.markers.add(mid)
        return mid

    def arrow(self, x1, y1, x2, y2, color=INK, sw=1.8, dash=None, both=False, curve=None):
        mid = self._marker(color)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        start = f' marker-start="url(#{mid}s)"' if both else ""
        if curve:
            cx, cy = curve
            self.items.append(f'<path d="M{x1},{y1} Q{cx},{cy} {x2},{y2}" fill="none" stroke="{color}" stroke-width="{sw}" marker-end="url(#{mid})"{start}{d}/>')
        else:
            self.items.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" marker-end="url(#{mid})"{start}{d}/>')
        return self

    def arrowpath(self, d, color=INK, sw=1.8, dash=None):
        mid = self._marker(color)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round" marker-end="url(#{mid})"{da}/>')
        return self

    def text(self, x, y, s, size=15, anchor="middle", weight=400, fill=INK, italic=False, lh=1.25, rot=None):
        """Text; «\\n» separa línies. Admet <tspan> amb subíndexs fets amb _{..} i ^{..}."""
        lines = s.split("\n")
        st = ' font-style="italic"' if italic else ""
        r = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
        if len(lines) == 1:
            body = fmt(lines[0], size)
        else:
            y0 = -(len(lines) - 1) * size * lh / 2
            body = "".join(f'<tspan x="{x}" dy="{(y0 if i == 0 else size * lh):.1f}">{fmt(l, size)}</tspan>' for i, l in enumerate(lines))
        self.items.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}" dominant-baseline="central"{st}{r}>{body}</text>')
        return self

    # ---------- composites ----------
    def box(self, x, y, w, h, label, color="gris", size=15, weight=700, rx=10, fill=None, tcolor=None, sw=1.8, dash=None):
        self.rect(x, y, w, h, fill=fill or light(color), stroke=col(color), sw=sw, rx=rx, dash=dash)
        self.text(x + w / 2, y + h / 2, label, size=size, weight=weight, fill=tcolor or INK)
        return self

    def pill(self, x, y, label, color="gris", size=14, pad=12, h=28, weight=700, solid=False):
        w = textw(label, size) + 2 * pad
        self.rect(x - w / 2, y - h / 2, w, h, fill=col(color) if solid else light(color), stroke=col(color), sw=1.5, rx=h / 2)
        self.text(x, y, label, size=size, weight=weight, fill="#fff" if solid else col(color))
        return w

    def svg(self, desc=""):
        defs = []
        for mid in self.markers:
            colr = "#" + mid[1:]
            defs.append(f'<marker id="{mid}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0.8 L9.5,5 L0,9.2 z" fill="{colr}"/></marker>')
            defs.append(f'<marker id="{mid}s" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0.8 L9.5,5 L0,9.2 z" fill="{colr}"/></marker>')
        t = f"<title>{escape(self.title)}</title>" if self.title else ""
        return (f'<svg class="bio" viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg" role="img" '
                f'aria-label="{escape(self.title or desc)}">{t}<defs>{"".join(defs)}</defs>'
                f'<rect width="{self.w}" height="{self.h}" fill="#fff"/>{"".join(self.items)}</svg>')


def fmt(s, size):
    """_{x} → subíndex, ^{x} → superíndex, **x** → negreta."""
    import re
    s = escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r'<tspan font-weight="700">\1</tspan>', s)
    s = re.sub(r"_\{(.+?)\}", lambda m: f'<tspan dy="{size*0.28:.1f}" font-size="{size*0.72:.1f}">{m.group(1)}</tspan><tspan dy="{-size*0.28:.1f}">​</tspan>', s)
    s = re.sub(r"\^\{(.+?)\}", lambda m: f'<tspan dy="{-size*0.38:.1f}" font-size="{size*0.72:.1f}">{m.group(1)}</tspan><tspan dy="{size*0.38:.1f}">​</tspan>', s)
    return s


def textw(s, size):
    import re
    s = re.sub(r"[_^]\{(.+?)\}", r"\1", s).replace("**", "")
    return len(s) * size * 0.56
