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


def frame(w: int, draw_h: int, title: str, drawing: str, notes: list[str] | None = None) -> str:
    """El dibuix, sense el bloc de notes: l'explicació va al text o al peu."""
    del notes
    y0 = 30
    total = y0 + draw_h + 6
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {total}" '
        f'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif">'
        f'<rect width="{w}" height="{total}" fill="#fff"/>'
        f'<text x="16" y="20" font-size="15" font-weight="700" fill="#0E7C66">{title}</text>'
        f'<g transform="translate(0,{y0})">{drawing}</g>'
        f'</svg>'
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

    def glue(anchor, direction, text, fill, dist):
        """La càrrega queda enganxada a l'àtom. No s'allunya cap al buit entre molècules."""
        px, py = direction
        n = math.hypot(px, py) or 1
        q = (anchor[0] + px / n * dist, anchor[1] + py / n * dist)
        taken.append((q, 26, 16))
        return _atom(q, text, fill, dy=5, size=14)

    taken = []
    charges = []
    for m in mols:
        h1, h2 = m["h"]
        for h, sib in ((h1, h2), (h2, h1)):
            px, py = _perp(m["o"], h)
            # Costat de fora de l'angle, no cap a l'altre hidrogen ni cap al pont.
            if (sib[0] - h[0]) * px + (sib[1] - h[1]) * py > 0:
                px, py = -px, -py
            charges.append(glue(h, (px, py), "δ+", "#8E2438", rh + 20))
        if m["kind"] == "don":
            # Els parells no enllaçants miren enfora: el pont és a l'hidrogen de dins.
            direction = (m["o"][0] - centre[0], m["o"][1] - centre[1])
        elif m["kind"] == "acc":
            # Al costat de l'oxigen, una mica cap al parell que rep el pont, mai sobre la línia.
            ix, iy = centre[0] - m["o"][0], centre[1] - m["o"][1]
            inn = math.hypot(ix, iy) or 1
            ix, iy = ix / inn, iy / inn
            px, py = _perp(centre, m["o"])
            if (h1[0] - m["o"][0]) * px + (h1[1] - m["o"][1]) * py > 0:
                px, py = -px, -py
            direction = (ix * 0.2 + px, iy * 0.2 + py)
        else:
            # Bisectriu dels dos parells, enganxada a l'oxigen central (cap amunt).
            direction = (0.0, -1.0)
        charges.append(glue(m["o"], direction, "δ−", "#C0392B", ro + 20))

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

    extents = [(p[0] - r - 2, p[1] - r - 2, p[0] + r + 2, p[1] + r + 2) for p, r in atoms]
    extents += [(q[0] - qw / 2 - 2, q[1] - qh / 2 - 2, q[0] + qw / 2 + 2, q[1] + 6) for q, qw, qh in taken]
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


def _haworth_glc(ox: float, oy: float, anomer: str = "alpha", c1: str = "oh", c4: str = "oh") -> tuple[str, dict]:
    """Projecció de Haworth de la D-glucopiranosa.

    Hexàgon en perspectiva: O darrere a la dreta, C1 a la dreta, C2–C3
    l'aresta de davant (traç gruixut), C4 a l'esquerra, C5 darrere a l'esquerra.
    Cada substituent és una línia vertical. L'H va al costat oposat.
    c1: 'oh' o 'link' (el pont α el dibuixa qui crida, cap avall).
    c4: 'oh' o 'link'.
    """
    pts = {
        "C5": (ox + 86, oy + 34),
        "O": (ox + 176, oy + 26),
        "C1": (ox + 228, oy + 96),
        "C2": (ox + 186, oy + 162),
        "C3": (ox + 76, oy + 162),
        "C4": (ox + 34, oy + 96),
    }
    parts: list[str] = []
    thin = [("C5", "O"), ("O", "C1"), ("C1", "C2"), ("C3", "C4"), ("C4", "C5")]
    for a, b in thin:
        x1, y1 = pts[a]
        x2, y2 = pts[b]
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#1b1f24" stroke-width="2.2" stroke-linecap="round"/>'
        )
    x1, y1 = pts["C2"]
    x2, y2 = pts["C3"]
    parts.append(
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="#1b1f24" stroke-width="6" stroke-linecap="round"/>'
    )

    def vertical(atom: str, up: bool, label: str, color: str = "#1b1f24") -> None:
        x, y = pts[atom]
        y2 = y - 38 if up else y + 38
        parts.append(
            f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>'
        )
        ty = y2 - 6 if up else y2 + 16
        parts.append(
            f'<text x="{x:.1f}" y="{ty:.1f}" font-size="14" text-anchor="middle" '
            f'fill="{color}" font-weight="700">{label}</text>'
        )

    # Substituents de la D-glucosa. L'H és gris i va al costat oposat.
    vertical("C5", True, "CH₂OH", "#0E7C66")
    vertical("C5", False, "H", "#8b939e")
    vertical("C4", True, "H", "#8b939e")
    if c4 == "oh":
        vertical("C4", False, "OH")
    vertical("C3", False, "H", "#8b939e")
    vertical("C3", True, "OH")
    vertical("C2", True, "H", "#8b939e")
    vertical("C2", False, "OH")
    if c1 == "oh" and anomer == "alpha":
        vertical("C1", True, "H", "#8b939e")
        vertical("C1", False, "OH", "#B23A52")
    elif c1 == "oh" and anomer == "beta":
        vertical("C1", False, "H", "#8b939e")
        vertical("C1", True, "OH", "#1F6AA5")
    elif c1 == "link":
        vertical("C1", True, "H", "#8b939e")

    # Els números queden dins l'anell, fora de la línia vertical de l'H o de l'OH.
    for name, num, dx, dy in (
        ("C1", "1", -22, 2),
        ("C2", "2", -18, -18),
        ("C3", "3", 20, -18),
        ("C4", "4", 26, -6),
        ("C5", "5", 36, 18),
    ):
        x, y = pts[name]
        parts.append(f'<circle cx="{x+dx:.1f}" cy="{y+dy-4:.1f}" r="8" fill="#fff"/>')
        parts.append(
            f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="12" text-anchor="middle" '
            f'fill="#5c6570" font-weight="700">{num}</text>'
        )
    ox_, oy_ = pts["O"]
    parts.append(f'<circle cx="{ox_:.1f}" cy="{oy_:.1f}" r="11" fill="#fff"/>')
    parts.append(
        f'<text x="{ox_:.1f}" y="{oy_+5:.1f}" font-size="16" text-anchor="middle" '
        f'fill="#1F6AA5" font-weight="700">O</text>'
    )
    return "".join(parts), pts


def _svg(w: float, h: float, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
        f'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif">'
        f'<rect width="{w:.0f}" height="{h:.0f}" fill="#fff"/>{body}</svg>'
    )


def fig_glucose() -> str:
    a, _ = _haworth_glc(28, 52, "alpha")
    b, _ = _haworth_glc(352, 52, "beta")
    body = (
        '<text x="156" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="#0E7C66">α-D-glucopiranosa</text>'
        '<text x="480" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="#1F6AA5">β-D-glucopiranosa</text>'
        + a + b
    )
    return _svg(620, 292, body)


def fig_maltose() -> str:
    left, p1 = _haworth_glc(16, 52, "alpha", c1="link", c4="oh")
    right, p2 = _haworth_glc(268, 52, "beta", c1="oh", c4="link")
    c1, c4 = p1["C1"], p2["C4"]
    # Dos trams curts cap avall i l'oxigen entremig, a la mateixa alçada.
    yb = c1[1] + 28
    bridge = (
        f'<line x1="{c1[0]:.1f}" y1="{c1[1]:.1f}" x2="{c1[0]:.1f}" y2="{yb:.1f}" stroke="#B23A52" stroke-width="2.2"/>'
        f'<line x1="{c1[0]:.1f}" y1="{yb:.1f}" x2="{c4[0]:.1f}" y2="{yb:.1f}" stroke="#B23A52" stroke-width="2.2"/>'
        f'<line x1="{c4[0]:.1f}" y1="{yb:.1f}" x2="{c4[0]:.1f}" y2="{c4[1]:.1f}" stroke="#B23A52" stroke-width="2.2"/>'
        f'<circle cx="{(c1[0]+c4[0])/2:.1f}" cy="{yb:.1f}" r="11" fill="#fff" stroke="#B23A52" stroke-width="1.4"/>'
        f'<text x="{(c1[0]+c4[0])/2:.1f}" y="{yb+5:.1f}" font-size="15" text-anchor="middle" fill="#B23A52" font-weight="700">O</text>'
    )
    body = (
        '<text x="148" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="#0E7C66">α-D-glucopiranosa</text>'
        '<text x="400" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="#1F6AA5">D-glucosa, extrem reductor</text>'
        + left + right + bridge
    )
    return _svg(540, 292, body)


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
