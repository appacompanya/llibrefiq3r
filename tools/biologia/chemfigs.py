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


def _atom(p, label, fill, dx=0, dy=4):
    return (
        f'<text x="{p[0]+dx:.1f}" y="{p[1]+dy:.1f}" text-anchor="middle" '
        f'font-size="18" font-weight="700" fill="{fill}">{label}</text>'
    )


def fig_water() -> str:
    """Dues aigües angulars (104,5°). El pont és O–H···O: l'O d'una queda al costat de l'H de l'altra."""
    L = 58
    gap = 46
    o1 = (168, 132)
    h_don = _at(o1, L, 0)          # H donador, cap a la dreta
    h1b = _at(o1, L, 104.5)        # segon H, amunt i a l'esquerra
    o2 = _at(h_don, gap, 0)        # O acceptor, a continuació del mateix eix
    h2a = _at(o2, L, 52.25)        # els dos H de la segona molècula, lluny del pont
    h2b = _at(o2, L, -52.25)
    dash_a = _at(h_don, 16, 0)
    dash_b = _at(o2, 16, 180)
    drawing = "".join([
        _bond(o1, h_don),
        _bond(o1, h1b),
        _bond(o2, h2a),
        _bond(o2, h2b),
        _bond(dash_a, dash_b, dash=True, color="#0E7C66", width=2.2, pad=0),
        _atom(o1, "O", "#1F6AA5", dy=6),
        _atom(o2, "O", "#1F6AA5", dy=6),
        _atom(h_don, "H", "#1b1f24", dy=6),
        _atom(h1b, "H", "#1b1f24", dy=6),
        _atom(h2a, "H", "#1b1f24", dy=6),
        _atom(h2b, "H", "#1b1f24", dy=6),
        _atom(o1, "δ−", "#1F6AA5", dx=0, dy=28),
        _atom(o2, "δ−", "#1F6AA5", dx=0, dy=-20),
        _atom(h_don, "δ+", "#B23A52", dy=28),
        _atom(h1b, "δ+", "#B23A52", dx=-4, dy=-18),
        _atom(h2a, "δ+", "#B23A52", dx=16, dy=-16),
        _atom(h2b, "δ+", "#B23A52", dx=16, dy=26),
        '<text x="250" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="#0E7C66">pont d’hidrogen</text>',
    ])
    return frame(
        640, 250, "Dues molècules d’aigua",
        drawing,
        [
            "Cada molècula és angular, amb dos enllaços O–H. L’oxigen és δ− i cada hidrogen és δ+.",
            "El pont d’hidrogen (verd, discontinu) va de l’H d’una molècula a l’O de l’altra. No és covalent.",
        ],
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
    labels = {"C1": (18, 6, "1"), "C2": (14, 16, "2"), "C3": (2, 18, "3"), "C4": (-16, -14, "4"), "C5": (2, 16, "5")}
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
            x2, y2 = x - 8, y - 36
            tx, ty = x - 36, y - 40
        elif atom == "C4" and not up:
            x2, y2 = x - 6, y + 42
            tx, ty = x - 8, y + 60
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
    ox, oy = (c1[0] + c4[0]) / 2, c1[1] + 36
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
        860, 300, "Maltosa: enllaç glicosídic α(1→4)",
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
        700, 300, "ATP",
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
