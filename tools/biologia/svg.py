"""Utilitats per a figures SVG originals del dossier de Biologia."""
from __future__ import annotations

import re


def _wrap_notes(body: str, width: int) -> tuple[str, int]:
    """Parteix els textos que surten del requadre i baixa el que hi ha a sota."""
    pat = re.compile(
        r'<text x="([\d.]+)" y="([\d.]+)" font-size="([\d.]+)" text-anchor="([^"]*)" fill="([^"]*)"'
        r'(?: font-weight="([^"]*)")?(?: font-style="([^"]*)")?>([^<]*)</text>'
    )
    plans = []
    for m in pat.finditer(body):
        if m.group(4) != "start":
            continue
        x = float(m.group(1))
        size = float(m.group(3))
        content = m.group(8)
        max_w = width - x - 12
        if max_w < 160 or len(content) * size * 0.52 <= max_w:
            continue
        limit = max(16, int(max_w / (size * 0.52)))
        lines, cur = [], ""
        for word in content.split():
            trial = (cur + " " + word).strip()
            if len(trial) <= limit:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        if len(lines) > 1:
            plans.append((m, lines, size + 4))
    extra_total = 0
    for m, lines, lh in sorted(plans, key=lambda p: -float(p[0].group(2))):
        y = float(m.group(2))
        extra = (len(lines) - 1) * lh
        extra_total += extra

        def bump(match, y=y, extra=extra):
            val = float(match.group(1))
            if val > y + 0.5:
                return f'y="{val + extra:.1f}"'
            return match.group(0)

        body = re.sub(r'y="([\d.]+)"', bump, body)
        chunks = []
        for i, line in enumerate(lines):
            node = m.group(0).replace(f'y="{m.group(2)}"', f'y="{y + i * lh:.1f}"', 1)
            node = node.replace(f'>{m.group(8)}</text>', f'>{line}</text>', 1)
            chunks.append(node)
        body = body.replace(m.group(0), "".join(chunks), 1)
    return body, int(extra_total + 8) if extra_total else 0


def svg(w: int, h: int, body: str) -> str:
    body, extra = _wrap_notes(body, w)
    h += extra
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
