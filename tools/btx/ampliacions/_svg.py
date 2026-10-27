"""Petites eines per dibuixar les figures noves en SVG amb el mateix estil que les del llibre."""
import math

FONT = 'font-family="DejaVu Sans, Noto Sans, Arial, sans-serif"'
INK, GREY, RED, BLUE, GREEN, ORANGE, PURPLE = "#111", "#555", "#b3261e", "#1f5fbf", "#2e7d32", "#c26a00", "#6a3fa0"


def f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


class Svg:
    def __init__(self, w, h):
        self.w, self.h, self.items = w, h, [f'<rect width="{w}" height="{h}" fill="#fff"/>']

    def line(self, x1, y1, x2, y2, c=INK, w=1.6, dash=None, op=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' stroke-opacity="{op}"' if op else ""
        self.items.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{c}" stroke-width="{w}"{d}{o} stroke-linecap="round"/>')

    def head(self, x, y, ang, c=INK, size=10):
        a1, a2 = ang + math.pi - 0.42, ang + math.pi + 0.42
        pts = [(x, y), (x + size * math.cos(a1), y + size * math.sin(a1)), (x + size * math.cos(a2), y + size * math.sin(a2))]
        self.items.append(f'<polygon points="{" ".join(f(p[0]) + "," + f(p[1]) for p in pts)}" fill="{c}" stroke="{c}" stroke-width="1" stroke-linejoin="round"/>')

    def arrow(self, x1, y1, x2, y2, c=INK, w=1.8, size=10, dash=None):
        ang = math.atan2(y2 - y1, x2 - x1)
        self.line(x1, y1, x2 - (size - 2) * math.cos(ang), y2 - (size - 2) * math.sin(ang), c, w, dash)
        self.head(x2, y2, ang, c, size)

    def mid_arrow(self, x1, y1, x2, y2, c=INK, w=1.7, t=0.5, dash=None):
        """segment amb una fletxeta al mig (raigs de llum)"""
        self.line(x1, y1, x2, y2, c, w, dash)
        ang = math.atan2(y2 - y1, x2 - x1)
        self.head(x1 + (x2 - x1) * t + 5 * math.cos(ang), y1 + (y2 - y1) * t + 5 * math.sin(ang), ang, c, 9)

    def poly(self, pts, c=INK, w=1.8, fill="none", dash=None, op=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' fill-opacity="{op}"' if op else ""
        self.items.append(f'<polyline points="{" ".join(f(x) + "," + f(y) for x, y in pts)}" fill="{fill}"{o} stroke="{c}" stroke-width="{w}"{d} stroke-linejoin="round" stroke-linecap="round"/>')

    def polygon(self, pts, fill, c="none", op=0.25):
        self.items.append(f'<polygon points="{" ".join(f(x) + "," + f(y) for x, y in pts)}" fill="{fill}" fill-opacity="{op}" stroke="{c}"/>')

    def circle(self, x, y, r, c=INK, fill="none", w=1.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}" stroke="{c}" stroke-width="{w}"{d}/>')

    def path(self, d, c=INK, w=1.8, fill="none", dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}"{da} stroke-linecap="round" stroke-linejoin="round"/>')

    def text(self, x, y, s, size=13, anchor="middle", c=INK, it=False, bold=False):
        st = (' font-style="italic"' if it else "") + (' font-weight="700"' if bold else "")
        self.items.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{size}" text-anchor="{anchor}" fill="{c}"{st}>{s}</text>')

    def svg(self):
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" {FONT}>' + "".join(self.items) + "</svg>"
