"""Utilitats per a figures SVG originals del dossier de Biologia."""
from __future__ import annotations


def svg(w: int, h: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif">'
        f'<rect width="{w}" height="{h}" fill="#fff"/>{body}</svg>'
    )


def tx(x, y, s, size=13, fill="#1b1f24", anchor="start", weight="400", style="normal"):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" '
        f'font-weight="{weight}" font-style="{style}">{s}</text>'
    )


def box(x, y, w, h, fill, stroke="#1b1f24", sw=1.5, rx=8, text="", tfill="#1b1f24", size=13):
    label = ""
    if text:
        label = tx(x + w / 2, y + h / 2 + 4, text, size=size, fill=tfill, anchor="middle", weight="700")
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"/>{label}'
    )


def arr(x1, y1, x2, y2, color="#1b1f24", sw=1.6):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" '
        f'marker-end="url(#ah)"/>'
    )


def defs_arrow(color="#1b1f24"):
    return (
        '<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">'
        f'<path d="M0,0 L8,3 L0,6 Z" fill="{color}"/></marker>'
        '<marker id="ahg" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">'
        '<path d="M0,0 L8,3 L0,6 Z" fill="#0E7C66"/></marker>'
        '<marker id="ahr" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">'
        '<path d="M0,0 L8,3 L0,6 Z" fill="#B23A52"/></marker>'
        '<marker id="ahb" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">'
        '<path d="M0,0 L8,3 L0,6 Z" fill="#1F6AA5"/></marker>'
        "</defs>"
    )


def cover(n: str, title: str, color: str, motif: str) -> str:
    return svg(
        1200,
        800,
        f'<rect width="1200" height="800" fill="{color}"/>'
        f'<circle cx="980" cy="140" r="220" fill="#fff" opacity=".08"/>'
        f'<circle cx="160" cy="680" r="180" fill="#000" opacity=".08"/>'
        f'<text x="72" y="180" fill="#fff" font-size="42" font-weight="700" opacity=".9">TEMA {n}</text>'
        f'<text x="72" y="280" fill="#fff" font-size="78" font-weight="700">{title}</text>'
        f"{motif}"
        f'<text x="72" y="720" fill="#fff" font-size="28" opacity=".9">Biologia · 2n de Batxillerat · PAU</text>',
    )
