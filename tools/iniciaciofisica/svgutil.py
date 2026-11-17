"""Dibuix de figures del llibre. Les mides de lletra es trien perquè, a l'amplada
impresa d'una pàgina, el text quedi per sobre de 9 pt."""
import math
from html import escape

INK = "#1b1f24"
MUTED = "#5c6570"
BLUE = "#1f5fbf"
RED = "#b3261e"
GREEN = "#1b7a3a"
ORANGE = "#c26a00"
PURPLE = "#6a3fa0"
TEAL = "#0e7c86"
GRID = "#e6e2d8"
PALE = "#f4f7fb"
PAPER = "#ffffff"
FONT = 'Atkinson Hyperlegible, DejaVu Sans, sans-serif'


def f(x):
    return f"{float(x):.2f}".rstrip("0").rstrip(".")


class Svg:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.items = []
        self.defs = []

    def raw(self, s):
        self.items.append(s)
        return self

    def rect(self, x, y, w, h, fill=PAPER, stroke=INK, sw=1.6, rx=0, dash=None, op=None):
        extra = ""
        if dash:
            extra += f' stroke-dasharray="{dash}"'
        if op is not None:
            extra += f' fill-opacity="{op}"'
        self.items.append(
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(rx)}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'
        )
        return self

    def line(self, x1, y1, x2, y2, c=INK, sw=1.7, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{c}" '
            f'stroke-width="{sw}" stroke-linecap="round"{d}/>'
        )
        return self

    def circle(self, x, y, r, c=INK, fill="none", sw=1.7, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}" stroke="{c}" stroke-width="{sw}"{d}/>'
        )
        return self

    def polygon(self, pts, fill="none", stroke=INK, sw=1.7, op=None):
        p = " ".join(f"{f(x)},{f(y)}" for x, y in pts)
        o = f' fill-opacity="{op}"' if op is not None else ""
        self.items.append(
            f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round"{o}/>'
        )
        return self

    def polyline(self, pts, c=INK, sw=2, dash=None, fill="none"):
        p = " ".join(f"{f(x)},{f(y)}" for x, y in pts)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<polyline points="{p}" fill="{fill}" stroke="{c}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="round"{d}/>'
        )
        return self

    def path(self, d, c=INK, sw=2, fill="none", dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"{da}/>'
        )
        return self

    def arrow(self, x1, y1, x2, y2, c=INK, sw=2.1, size=11):
        ang = math.atan2(y2 - y1, x2 - x1)
        # escurça la línia perquè no tapi la punta
        x2b = x2 - (size * 0.72) * math.cos(ang)
        y2b = y2 - (size * 0.72) * math.sin(ang)
        self.line(x1, y1, x2b, y2b, c, sw)
        a1, a2 = ang + math.pi - 0.42, ang + math.pi + 0.42
        pts = [
            (x2, y2),
            (x2 + size * math.cos(a1), y2 + size * math.sin(a1)),
            (x2 + size * math.cos(a2), y2 + size * math.sin(a2)),
        ]
        self.polygon(pts, fill=c, stroke=c, sw=1)
        return self

    def axes(self, x0, y0, x1, y1, xlabel="", ylabel="", sw=1.7):
        """Eixos amb fletxa. x cap a la dreta, y cap amunt (y1 < y0 en coordenades de pantalla)."""
        self.arrow(x0, y0, x1, y0, INK, sw, 10)
        self.arrow(x0, y0, x0, y1, INK, sw, 10)
        if xlabel:
            self.text(x1 - 2, y0 + 20, xlabel, 16, "end", INK, it=False, halo=False)
        if ylabel:
            self.text(x0 + 12, y1 + 14, ylabel, 16, "start", INK, it=False, halo=False)
        return self

    def text(self, x, y, s, size=16, anchor="middle", c=INK, it=False, bold=False, halo=True):
        st = ""
        if it:
            st += ' font-style="italic"'
        if bold:
            st += ' font-weight="700"'
        body = escape(s).replace("\n", " ")
        common = (
            f'x="{f(x)}" y="{f(y)}" font-size="{size}" text-anchor="{anchor}" '
            f'font-family="{FONT}" dominant-baseline="middle"{st}'
        )
        if halo:
            self.items.append(
                f'<text {common} fill="#ffffff" stroke="#ffffff" stroke-width="4" '
                f'stroke-linejoin="round">{body}</text>'
            )
        self.items.append(f'<text {common} fill="{c}">{body}</text>')
        return self

    def label(self, x, y, s, size=16, anchor="middle", c=INK, it=True, bold=False):
        return self.text(x, y, s, size, anchor, c, it, bold, True)

    def svg(self):
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'role="img" font-family="{FONT}">'
            + "".join(self.items)
            + "</svg>"
        )
