"""Estructures moleculars i projeccions de Haworth.

La plantilla de Haworth situa l'oxigen com a vèrtex de l'anell, entre C5 i C1.
"""
from __future__ import annotations

import math

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

# SMILES de les estructures que es dibuixen. El codi no els mostra a l'alumne.
PUBCHEM = {
    "water": (962, "O"),
    "a-glc": (79025, "C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O"),
    "b-glc": (64689, "C([C@@H]1[C@H]([C@@H]([C@H]([C@@H](O1)O)O)O)O)O"),
    "tag": (11147, "CCCCCCCCCCCCCCCC(=O)OCC(COC(=O)CCCCCCCCCCCCCCC)OC(=O)CCCCCCCCCCCCCCC"),
    # Mateix cap i els mateixos èsters que un fosfolípid; cues de 6 carbonis perquè el dibuix es llegeixi.
    "pc6": (10072611, "CCCCCC(=O)OC[C@H](COP(=O)([O-])OCC[N+](C)(C)C)OC(=O)CCCCC"),
    "chol": (5997, "C[C@H](CCCC(C)C)[C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CC=C4[C@@]3(CC[C@@H](C4)O)C)C"),
    "ala": (5950, "C[C@@H](C(=O)O)N"),
    "glygly": (11163, "C(C(=O)NCC(=O)O)N"),
    "damp": (12599, "C1[C@@H]([C@H](O[C@H]1N2C=NC3=C(N=CN=C32)N)COP(=O)(O)O)O"),
    "atp": (5957, "C1=NC(=C2C(=N1)N(C=N2)[C@H]3[C@@H]([C@@H]([C@H](O3)COP(=O)(O)OP(=O)(O)OP(=O)(O)O)O)O)N"),
    "nad": (5892, "C1=CC(=C[N+](=C1)[C@H]2[C@@H]([C@@H]([C@H](O2)COP(=O)([O-])OP(=O)(O)OC[C@@H]3[C@H]([C@H]([C@@H](O3)N4C=NC5=C(N=CN=C54)N)O)O)O)O)C(=O)N"),
    "palm": (985, "CCCCCCCCCCCCCCCC(=O)O"),
    "oleic": (445639, r"CCCCCCCC/C=C\CCCCCCCC(=O)O"),
}

# Formes a pH fisiològic: mateixa connectivitat, amb les càrregues del zwitterió.
CHARGED = {
    "ala_z": (5950, "C[C@@H]([NH3+])C(=O)[O-]"),
    "glygly_z": (11163, "[NH3+]CC(=O)NCC(=O)[O-]"),
    "gly_z": (750, "[NH3+]CC(=O)[O-]"),
}


def _mol(smi: str, add_h: bool = False):
    m = Chem.MolFromSmiles(smi)
    if m is None:
        raise SystemExit(f"estructura invàlida")
    if add_h:
        m = Chem.AddHs(m)
    from rdkit.Chem import rdDepictor
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(m)
    return m


def rdkit_svg(smi: str, w: int, h: int, add_h: bool = False) -> str:
    m = _mol(smi, add_h=add_h)
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    opt = d.drawOptions()
    opt.bondLineWidth = 2.0
    opt.padding = 0.08
    opt.fixedFontSize = 16
    opt.clearBackground = True
    opt.backgroundColour = (1, 1, 1)
    rdMolDraw2D.PrepareAndDrawMolecule(d, m)
    d.FinishDrawing()
    svg = d.GetDrawingText()
    i = svg.find("<svg")
    svg = svg[i:]
    # El fitxer publicat no ha de dur el nom de l'eina ni metadades internes.
    svg = svg.replace(" xmlns:rdkit='http://www.rdkit.org/xml'", "")
    svg = svg.replace(' xmlns:rdkit="http://www.rdkit.org/xml"', "")
    return svg


def frame(w: int, draw_h: int, title: str, drawing: str, notes: list[str]) -> str:
    """draw_h és l'alçada reservada al dibuix, sota el títol i per damunt de les notes."""
    y0 = 36
    note_y = y0 + draw_h + 22
    note = "".join(
        f'<text x="16" y="{note_y + 18*i}" font-size="13" fill="#3b4148" '
        f'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif">{t}</text>'
        for i, t in enumerate(notes)
    )
    total = note_y + 18 * len(notes) + 10
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {total}" '
        f'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif">'
        f'<rect width="{w}" height="{total}" fill="#fff"/>'
        f'<text x="16" y="22" font-size="15" font-weight="700" fill="#0E7C66">{title}</text>'
        f'<g transform="translate(0,{y0})">{drawing}</g>'
        f'{note}</svg>'
    )


def panel(title: str, smi: str, w: int, h: int, add_h: bool = False) -> str:
    raw = rdkit_svg(smi, w, h - 28, add_h=add_h)
    # treu l'amplada fixa del svg intern perquè s'escali dins el grup
    return (
        f'<g>'
        f'<text x="8" y="16" font-size="14" font-weight="700" fill="#1b1f24" '
        f'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif">{title}</text>'
        f'<g transform="translate(0,20)">{raw}</g></g>'
    )


def _at(origin, length, deg):
    """Angle matemàtic: 0° cap a la dreta, positiu cap amunt (y de pantalla cap avall)."""
    a = math.radians(deg)
    return (origin[0] + length * math.cos(a), origin[1] - length * math.sin(a))


def _inset(p, q, pad):
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy) or 1
    return (p[0] + pad * dx / n, p[1] + pad * dy / n)


def _bond(p, q, dash=False, color="#1b1f24", width=2.6, pad=14):
    a, b = _inset(p, q, pad), _inset(q, p, pad)
    extra = ' stroke-dasharray="7 5"' if dash else ""
    return (
        f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
        f'stroke="{color}" stroke-width="{width}" stroke-linecap="round"{extra}/>'
    )


def _atom(p, label, fill, dx=0, dy=5, size=16):
    return (
        f'<text x="{p[0]+dx:.1f}" y="{p[1]+dy:.1f}" text-anchor="middle" '
        f'font-size="{size}" font-weight="700" fill="{fill}">{label}</text>'
    )


def _perp(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy) or 1
    return (-dy / n, dx / n)


def fig_water() -> str:
    """Cinc aigües, angle 104,5°, cada pont O–H···O col·lineal. ViewBox ajustat al dibuix."""
    L = 82.0
    gap = 74.0
    half = 52.25
    ro, rh = 26.0, 18.0
    centre = (0.0, 0.0)

    def water_at(o, bisector):
        return {"o": o, "h": (_at(o, L, bisector + half), _at(o, L, bisector - half)), "bis": bisector, "kind": "acc"}

    mols = [water_at(centre, -90) | {"kind": "centre"}]
    hbonds = []
    for theta in (-90 + half, -90 - half):
        acc = water_at(_at(centre, L + gap, theta), theta)
        mols.append(acc)
        hbonds.append((_at(centre, L, theta), acc["o"]))
    for phi in (90 - half, 90 + half):
        h = _at(centre, gap, phi)
        o = _at(centre, gap + L, phi)
        alpha = phi + 180
        alts = (_at(o, L, alpha + 104.5), _at(o, L, alpha - 104.5))
        alt = max(alts, key=lambda p: math.hypot(p[0] - centre[0], p[1] - centre[1]))
        mols.append({"o": o, "h": (h, alt), "bis": alpha, "kind": "don"})
        hbonds.append((h, centre))

    atoms = [(m["o"], ro) for m in mols] + [(h, rh) for m in mols for h in m["h"]]

    def hits(p, w, hgt, taken):
        x0, y0, x1, y1 = p[0] - w / 2, p[1] - hgt / 2, p[0] + w / 2, p[1] + hgt / 2
        for (ax, ay), r in atoms:
            cx, cy = min(max(ax, x0), x1), min(max(ay, y0), y1)
            if math.hypot(cx - ax, cy - ay) < r + 10:
                return True
        for q, qw, qh in taken:
            if abs(p[0] - q[0]) < (w + qw) / 2 + 16 and abs(p[1] - q[1]) < (hgt + qh) / 2 + 10:
                return True
        return False

    def park(anchor, direction, text, fill, taken, base):
        px, py = direction
        n = math.hypot(px, py) or 1
        px, py = px / n, py / n
        w, hgt = (32, 18) if "−" in text else (28, 18)
        for dist in range(int(base), int(base) + 90, 3):
            q = (anchor[0] + px * dist, anchor[1] + py * dist)
            if not hits(q, w, hgt, taken):
                taken.append((q, w, hgt))
                return _atom(q, text, fill, dy=5, size=15)
        q = (anchor[0] + px * (base + 90), anchor[1] + py * (base + 90))
        taken.append((q, w, hgt))
        return _atom(q, text, fill, dy=5, size=15)

    taken = []
    charges = []
    for m in mols:
        h1, h2 = m["h"]
        # δ+ fora de l'angle H–O–H, al costat oposat de l'altre hidrogen.
        for h, sib in ((h1, h2), (h2, h1)):
            px, py = _perp(m["o"], h)
            if (sib[0] - h[0]) * px + (sib[1] - h[1]) * py > 0:
                px, py = -px, -py
            charges.append(park(h, (px, py), "δ+", "#8E2438", taken, rh + 18))
        if m["kind"] == "don":
            # Més enllà de l'oxigen, a l'exterior: el pont queda a l'altre costat.
            direction = (m["o"][0] - centre[0], m["o"][1] - centre[1])
        elif m["kind"] == "acc":
            # Perpendicular al pont, no sobre la línia discontínua.
            px, py = _perp(centre, m["o"])
            if (h1[0] - m["o"][0]) * px + (h1[1] - m["o"][1]) * py > 0:
                px, py = -px, -py
            direction = (px, py)
        else:
            direction = (-1.0, 0.15)  # buit entre els dos ponts de l'esquerra
        charges.append(park(m["o"], direction, "δ−", "#C0392B", taken, ro + 16))

    # Pont de dalt a la dreta: el rètol surt en perpendicular, cap al buit.
    phi = 90 - half
    bridge_h = _at(centre, gap, phi)
    a = _inset(bridge_h, centre, rh + 2)
    b = _inset(centre, bridge_h, ro + 2)
    mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    px, py = _perp(centre, bridge_h)

    obstacles = [p for p, _r in atoms] + [q for q, _w, _h in taken]

    def clearance(sign, dist):
        q = (mid[0] + sign * px * dist, mid[1] + sign * py * dist)
        return min(math.hypot(q[0] - p[0], q[1] - p[1]) for p in obstacles)

    sign = 1 if clearance(1, 130) >= clearance(-1, 130) else -1
    lx, ly_ = sign * px, sign * py
    label_at = (mid[0] + lx * 132, mid[1] + ly_ * 132)
    leader = (
        f'<line x1="{mid[0]+lx*8:.1f}" y1="{mid[1]+ly_*8:.1f}" x2="{label_at[0]-lx*46:.1f}" y2="{label_at[1]-ly_*10:.1f}" '
        f'stroke="#0E7C66" stroke-width="1.3"/>'
        f'<circle cx="{mid[0]:.1f}" cy="{mid[1]:.1f}" r="2.6" fill="#0E7C66"/>'
        + _atom(label_at, "pont d’hidrogen", "#0E7C66", dy=4, size=14)
    )

    parts = []
    for h, o_acc in hbonds:
        a, b = _inset(h, o_acc, rh + 2), _inset(o_acc, h, ro + 2)
        parts.append(
            f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
            f'stroke="#0E7C66" stroke-width="2.8" stroke-linecap="round" stroke-dasharray="9 6"/>'
        )
    for m in mols:
        for h in m["h"]:
            a, b = _inset(m["o"], h, ro + 1), _inset(h, m["o"], rh + 1)
            parts.append(
                f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                f'stroke="#1b1f24" stroke-width="3.4" stroke-linecap="round"/>'
            )
    for m in mols:
        ox, oy = m["o"]
        parts.append(f'<circle cx="{ox:.1f}" cy="{oy:.1f}" r="{ro:.0f}" fill="#C0392B"/>')
        parts.append(_atom(m["o"], "O", "#fff", dy=6, size=20))
        for h in m["h"]:
            parts.append(
                f'<circle cx="{h[0]:.1f}" cy="{h[1]:.1f}" r="{rh:.0f}" fill="#F2F3F5" stroke="#5c6570" stroke-width="1.7"/>'
            )
            parts.append(_atom(h, "H", "#1b1f24", dy=5, size=16))
    parts.extend(charges)
    parts.append(leader)

    extents = [(p[0] - r - 2, p[1] - r - 2, p[0] + r + 2, p[1] + r + 2) for p, r in atoms]
    extents += [(q[0] - qw / 2 - 2, q[1] - qh / 2 - 2, q[0] + qw / 2 + 2, q[1] + 6) for q, qw, qh in taken]
    extents.append((label_at[0] - 68, label_at[1] - 14, label_at[0] + 68, label_at[1] + 6))
    minx = min(a[0] for a in extents)
    maxx = max(a[2] for a in extents)
    miny = min(a[1] for a in extents)
    maxy = max(a[3] for a in extents)
    # Llegenda en dues files, centrada, sense allargar el requadre.
    cx = (minx + maxx) / 2
    row1, row2 = maxy + 36, maxy + 64
    legend = (
        f'<circle cx="{cx-168:.1f}" cy="{row1:.1f}" r="9" fill="#C0392B"/>'
        f'<text x="{cx-154:.1f}" y="{row1+4:.1f}" font-size="14" fill="#1b1f24">oxigen (δ−)</text>'
        f'<circle cx="{cx+28:.1f}" cy="{row1:.1f}" r="8" fill="#F2F3F5" stroke="#5c6570" stroke-width="1.4"/>'
        f'<text x="{cx+42:.1f}" y="{row1+4:.1f}" font-size="14" fill="#1b1f24">hidrogen (δ+)</text>'
        f'<line x1="{cx-168:.1f}" y1="{row2:.1f}" x2="{cx-124:.1f}" y2="{row2:.1f}" stroke="#1b1f24" stroke-width="3.2"/>'
        f'<text x="{cx-116:.1f}" y="{row2+4:.1f}" font-size="14" fill="#1b1f24">enllaç covalent</text>'
        f'<line x1="{cx+36:.1f}" y1="{row2:.1f}" x2="{cx+84:.1f}" y2="{row2:.1f}" stroke="#0E7C66" stroke-width="2.8" stroke-dasharray="9 6"/>'
        f'<text x="{cx+92:.1f}" y="{row2+4:.1f}" font-size="14" fill="#1b1f24">pont d’hidrogen</text>'
    )
    parts.append(legend)
    pad = 10
    vx, vy = minx - pad, miny - pad
    vw, vh = (maxx - minx) + 2 * pad, (row2 + 14) - miny + pad
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.1f} {vy:.1f} {vw:.1f} {vh:.1f}" '
        f'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif">'
        f'<rect x="{vx:.1f}" y="{vy:.1f}" width="{vw:.1f}" height="{vh:.1f}" fill="#fff"/>'
        f'{"".join(parts)}</svg>'
    )


# --- Haworth: hexàgon regular. L'oxigen és el vèrtex superior dret (entre C5 i C1). ---
def _regular_ring():
    cx, cy, r = 160, 130, 56
    names = ["C1", "C2", "C3", "C4", "C5", "O"]
    pts = {}
    for name, ang in zip(names, (0, 60, 120, 180, 240, 300)):
        a = math.radians(ang)
        pts[name] = (cx + r * math.cos(a), cy + r * math.sin(a))
    return pts


_RING = _regular_ring()


def _haworth_glc(ox: int, oy: int, anomer: str, c1="oh", c4="oh") -> str:
    """α: OH del C1 avall. β: OH del C1 amunt. La resta és D-glucosa.

    c1: 'oh' | 'alpha-link' (el substituent de baix el dibuixa qui crida).
    c4: 'oh' | 'link'.
    Els H no es rotulen: cada carboni de l'anell en porta un al costat oposat de l'OH.
    """
    pts = {k: (ox + x - 160, oy + y - 40) for k, (x, y) in _RING.items()}
    parts = []
    order = ["C5", "O", "C1", "C2", "C3", "C4", "C5"]
    for a, b in zip(order, order[1:]):
        x1, y1 = pts[a]
        x2, y2 = pts[b]
        parts.append(
            f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#1b1f24" stroke-width="2.4" stroke-linecap="round"/>'
        )
    # números fora de l'anell, lluny dels substituents
    labels = {"C1": (16, -10, "1"), "C2": (16, 4, "2"), "C3": (10, 16, "3"), "C4": (14, -12, "4"), "C5": (12, 14, "5")}
    for name, (dx, dy, lab) in labels.items():
        x, y = pts[name]
        parts.append(
            f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" font-size="11" text-anchor="middle" fill="#5c6570" font-weight="700">{lab}</text>'
        )
    x, y = pts["O"]
    parts.append(f'<text x="{x:.0f}" y="{y-14:.0f}" font-size="15" text-anchor="middle" fill="#1F6AA5" font-weight="700">O</text>')

    def arm(atom, up, label, color="#1b1f24"):
        x, y = pts[atom]
        # Direccions explícites, fora de l'anell: C3 amunt-esquerra, C4 avall, C2 avall, C1 α avall / β amunt, C5 amunt.
        vx, vy = {
            ("C5", True): (0.0, -1.0),
            ("C2", False): (0.05, 1.0),
            ("C3", True): (-1.0, -0.2),
            ("C4", False): (0.0, 1.0),
            ("C1", False): (0.25, 1.0),
            ("C1", True): (0.55, -0.85),
        }[(atom, up)]
        n2 = math.hypot(vx, vy) or 1
        vx, vy = vx / n2, vy / n2
        x2, y2 = x + vx * 40, y + vy * 40
        # C3 i C4 són veïns: el rètol de l'un va cap a l'esquerra i el de l'altre cap avall.
        if atom == "C3" and up:
            # Gairebé horitzontal, una mica amunt: queda a l'alçada del C3, no del C4.
            x2, y2 = x - 36, y - 8
            tx, ty = x - 64, y - 4
        elif atom == "C4" and not up:
            # Gairebé horitzontal, una mica avall: separat del substituent del C3.
            x2, y2 = x - 36, y + 10
            tx, ty = x - 64, y + 16
        else:
            tx, ty = x2 + vx * 16, y2 + vy * 14 + 4
        parts.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#1b1f24" stroke-width="1.8"/>')
        parts.append(
            f'<text x="{tx:.0f}" y="{ty:.0f}" font-size="13" text-anchor="middle" fill="{color}" font-weight="700">{label}</text>'
        )

    arm("C5", True, "CH₂OH", "#0E7C66")
    arm("C2", False, "OH")
    arm("C3", True, "OH")
    if c4 == "oh":
        arm("C4", False, "OH")
    if c1 == "oh" and anomer == "alpha":
        arm("C1", False, "OH", "#B23A52")
    elif c1 == "oh" and anomer == "beta":
        arm("C1", True, "OH", "#1F6AA5")
    return "".join(parts), pts


def fig_glucose() -> str:
    a, _ = _haworth_glc(170, 48, "alpha")
    b, _ = _haworth_glc(520, 48, "beta")
    body = (
        '<text x="220" y="16" font-size="14" font-weight="700" text-anchor="middle" fill="#0E7C66">α-D-glucopiranosa</text>'
        '<text x="580" y="16" font-size="14" font-weight="700" text-anchor="middle" fill="#1F6AA5">β-D-glucopiranosa</text>'
        + a + b
    )
    return frame(
        820, 280, "Haworth de la D-glucopiranosa",
        body,
        [
            "L’oxigen és un vèrtex de l’anell, entre C5 i C1. C1 a la dreta; C2 i C3 a baix; C4 a l’esquerra.",
            "Sèrie D: el CH₂OH del C5 mira amunt. α: l’OH del C1 és avall. β: l’OH del C1 és amunt.",
            "C2–OH avall, C3–OH amunt, C4–OH avall. L’H de cada carboni, no escrit, és al costat oposat de l’OH.",
        ],
    )


def fig_maltose() -> str:
    left, p1 = _haworth_glc(150, 56, "alpha", c1="alpha-link", c4="oh")
    right, p2 = _haworth_glc(520, 56, "beta", c1="oh", c4="link")
    c1, c4 = p1["C1"], p2["C4"]
    # El pont baixa per sota dels OH del C2, perquè l'enllaç α surt cap avall.
    low = max(p1["C2"][1], p1["C3"][1], p2["C2"][1], p2["C3"][1]) + 78
    ox, oy = (c1[0] + c4[0]) / 2, low
    bridge = (
        f'<line x1="{c1[0]:.0f}" y1="{c1[1]:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="#B23A52" stroke-width="2.3"/>'
        f'<line x1="{ox:.0f}" y1="{oy:.0f}" x2="{c4[0]:.0f}" y2="{c4[1]:.0f}" stroke="#B23A52" stroke-width="2.3"/>'
        f'<text x="{ox:.0f}" y="{oy+18:.0f}" font-size="14" text-anchor="middle" fill="#B23A52" font-weight="700">O</text>'
    )
    body = (
        '<text x="200" y="16" font-size="14" font-weight="700" fill="#0E7C66">α-D-Glc</text>'
        '<text x="570" y="16" font-size="14" font-weight="700" fill="#1F6AA5">D-Glc, extrem reductor</text>'
        + left + right + bridge
    )
    return frame(
        860, 360, "Maltosa: enllaç glicosídic α(1→4)",
        body,
        [
            "L’oxigen vermell surt del C1 (posició α, avall) i arriba al C4 de la segona glucosa.",
            "És una condensació: en formar-se l’enllaç surt aigua. L’anomèric de la dreta queda lliure.",
            "La cel·lulosa fa servir els mateixos carbonis, però l’enllaç és β(1→4).",
        ],
    )


def fig_lipids() -> str:
    trihex = "CCCCCC(=O)OCC(COC(=O)CCCCC)OC(=O)CCCCC"
    w, h = 360, 250
    a = rdkit_svg(trihex, w, h)
    b = rdkit_svg(PUBCHEM["pc6"][1], w, h)
    c = rdkit_svg(PUBCHEM["chol"][1], 300, 200)
    drawing = (
        f'<text x="180" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="#C4651A">Triacilglicerol (cues de 6 C)</text>'
        f'<g transform="translate(0,18)">{a}</g>'
        f'<text x="560" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="#1F6AA5">Fosfolípid (PC, cues de 6 C)</text>'
        f'<g transform="translate(380,18)">{b}</g>'
        f'<text x="560" y="290" text-anchor="middle" font-size="13" font-weight="700" fill="#5c6570">Colesterol</text>'
        f'<g transform="translate(430,300)">{c}</g>'
    )
    return frame(
        780, 520, "Tres lípids",
        drawing,
        [
            "El triacilglicerol té tres cues unides al glicerol per èsters. És reserva i no fa membranes.",
            "El fosfolípid té dues cues i un cap polar: és amfipàtic i forma la bicapa.",
            "El colesterol és un esteroide de quatre anells, insaponificable. No és un triacilglicerol.",
        ],
    )


def fig_peptide() -> str:
    a = rdkit_svg(CHARGED["ala_z"][1], 340, 200)
    b = rdkit_svg(CHARGED["glygly_z"][1], 400, 180)
    drawing = (
        f'<text x="170" y="16" text-anchor="middle" font-size="13" font-weight="700">L-alanina, zwitterió (pH 7)</text>'
        f'<g transform="translate(0,20)">{a}</g>'
        f'<text x="560" y="16" text-anchor="middle" font-size="13" font-weight="700">Glicilglicina: enllaç peptídic</text>'
        f'<g transform="translate(360,24)">{b}</g>'
    )
    return frame(
        780, 250, "Aminoàcid i enllaç peptídic",
        drawing,
        [
            "A pH 7 el grup amino és NH₃⁺ i el carboxil és COO⁻.",
            "A la glicilglicina l’enllaç amida és el peptídic. L’extrem N és el que porta NH₃⁺; l’extrem C, el COO⁻.",
        ],
    )


def fig_nucleotide() -> str:
    a = rdkit_svg(PUBCHEM["damp"][1], 460, 280)
    drawing = (
        f'<text x="230" y="16" text-anchor="middle" font-size="13" font-weight="700">dAMP: desoxiadenosina 5′-monofosfat</text>'
        f'<g transform="translate(0,18)">{a}</g>'
        f'<text x="620" y="40" font-size="13" font-weight="700" fill="#1F6AA5">Aparellament</text>'
        f'<text x="520" y="78" font-size="15" font-weight="700">5′– A ··· T –3′</text>'
        f'<text x="520" y="102" font-size="13" fill="#C4651A">dos ponts d’hidrogen</text>'
        f'<text x="520" y="140" font-size="15" font-weight="700">3′– T ··· A –5′</text>'
        f'<text x="520" y="178" font-size="15" font-weight="700">5′– G ≡ C –3′</text>'
        f'<text x="520" y="202" font-size="13" fill="#5C4B8A">tres ponts d’hidrogen</text>'
        f'<text x="520" y="226" font-size="15" font-weight="700">3′– C ≡ G –5′</text>'
    )
    return frame(
        780, 340, "Nucleòtid i aparellament",
        drawing,
        [
            "El dAMP porta desoxiribosa (no hi ha OH al C2′), adenina al C1′ i fosfat al C5′.",
            "Les cadenes són antiparal·leles: el 5′ d’una queda enfront del 3′ de l’altra. A–T fa dos ponts; G–C, tres.",
        ],
    )


def fig_atp() -> str:
    drawing = rdkit_svg(PUBCHEM["atp"][1], 640, 280)
    return frame(
        860, 300, "ATP",
        drawing,
        [
            "Adenina, ribosa i tres fosfats. La hidròlisi ATP → ADP + Pᵢ allibera l’energia que gasten les vies.",
            "No és un magatzem: la cèl·lula el recicla. El NADPH, no dibuixat aquí, és el poder reductor de l’anabolisme.",
        ],
    )


def molecules() -> dict[str, str]:
    return {
        "fig-1.1": fig_water(),
        "fig-1.2": fig_glucose(),
        "fig-1.3": fig_maltose(),
        "fig-1.4": fig_lipids(),
        "fig-1.5": fig_peptide(),
        "fig-1.7": fig_nucleotide(),
        "fig-3.9": fig_atp(),
    }
