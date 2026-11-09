"""Molècules amb RDKit (SMILES verificats a PubChem) i projeccions de Haworth amb plantilla fixa.

La plantilla de Haworth no és un hexàgon improvisat: els substituents amunt/avall
són els de la convenció estàndard de la D-glucopiranosa (α: OH anomèric trans al CH₂OH).
"""
from __future__ import annotations

import math

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

# SMILES: camp retornat per PubChem property/IsomericSMILES (novembre 2026).
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

# Formes a pH fisiològic: mateixa connectivitat i estereoquímica que el CID, amb les càrregues del zwitterió.
CHARGED = {
    "ala_z": (5950, "C[C@@H]([NH3+])C(=O)[O-]"),
    "glygly_z": (11163, "[NH3+]CC(=O)NCC(=O)[O-]"),
    "gly_z": (750, "[NH3+]CC(=O)[O-]"),
}


def _mol(smi: str, add_h: bool = False):
    m = Chem.MolFromSmiles(smi)
    if m is None:
        raise SystemExit(f"SMILES invàlid: {smi}")
    if add_h:
        m = Chem.AddHs(m)
    AllChem.Compute2DCoords(m)
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
    # RDKit posa xml header i un fons; ens quedem el fragment <svg>
    i = svg.find("<svg")
    return svg[i:]


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


def fig_water() -> str:
    one = rdkit_svg(PUBCHEM["water"][1], 240, 160, add_h=True)
    drawing = (
        f'<g transform="translate(20,10)">{one}</g>'
        f'<g transform="translate(360,10)">{one}</g>'
        f'<line x1="236" y1="62" x2="480" y2="117" stroke="#0E7C66" stroke-width="2" stroke-dasharray="7 5"/>'
        f'<text x="330" y="48" text-anchor="middle" font-size="13" font-weight="700" fill="#0E7C66">enllaç d’hidrogen</text>'
        f'<text x="140" y="175" text-anchor="middle" font-size="12" fill="#1F6AA5">δ− a l’oxigen</text>'
        f'<text x="500" y="175" text-anchor="middle" font-size="12" fill="#B23A52">δ+ a cada hidrogen</text>'
    )
    return frame(
        680, 190, "Dues molècules d’aigua",
        drawing,
        [
            "Cada molècula (RDKit, CID 962) té dos enllaços O–H. L’oxigen és δ− i cada hidrogen és δ+.",
            "El pont d’hidrogen, en verd, va d’un H d’una molècula a l’O de l’altra. No és un enllaç covalent.",
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
    labels = {"C1": (16, 4, "1"), "C2": (12, 18, "2"), "C3": (-14, 20, "3"), "C4": (-18, -12, "4"), "C5": (0, 16, "5")}
    for name, (dx, dy, lab) in labels.items():
        x, y = pts[name]
        parts.append(
            f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" font-size="11" text-anchor="middle" fill="#5c6570" font-weight="700">{lab}</text>'
        )
    x, y = pts["O"]
    parts.append(f'<text x="{x:.0f}" y="{y-14:.0f}" font-size="15" text-anchor="middle" fill="#1F6AA5" font-weight="700">O</text>')

    def arm(atom, up, label, color="#1b1f24"):
        x, y = pts[atom]
        y2 = y - 34 if up else y + 34
        parts.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x:.0f}" y2="{y2:.0f}" stroke="#1b1f24" stroke-width="1.8"/>')
        ty = y2 - 6 if up else y2 + 14
        parts.append(
            f'<text x="{x:.0f}" y="{ty:.0f}" font-size="13" text-anchor="middle" fill="{color}" font-weight="700">{label}</text>'
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
    a, _ = _haworth_glc(130, 48, "alpha")
    b, _ = _haworth_glc(480, 48, "beta")
    body = (
        '<text x="180" y="16" font-size="14" font-weight="700" text-anchor="middle" fill="#0E7C66">α-D-glucopiranosa</text>'
        '<text x="540" y="16" font-size="14" font-weight="700" text-anchor="middle" fill="#1F6AA5">β-D-glucopiranosa</text>'
        + a + b
    )
    return frame(
        760, 250, "Haworth de la D-glucopiranosa",
        body,
        [
            "L’oxigen és un vèrtex de l’anell, entre C5 i C1. C1 a la dreta; C2 i C3 a baix; C4 a l’esquerra.",
            "Sèrie D: el CH₂OH del C5 mira amunt. α: l’OH del C1 és avall. β: l’OH del C1 és amunt.",
            "C2–OH avall, C3–OH amunt, C4–OH avall. L’H de cada carboni, no escrit, és al costat oposat de l’OH.",
        ],
    )


def fig_maltose() -> str:
    left, p1 = _haworth_glc(90, 56, "alpha", c1="alpha-link", c4="oh")
    right, p2 = _haworth_glc(470, 56, "beta", c1="oh", c4="link")
    c1, c4 = p1["C1"], p2["C4"]
    ox, oy = (c1[0] + c4[0]) / 2, c1[1] + 36
    bridge = (
        f'<line x1="{c1[0]:.0f}" y1="{c1[1]:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="#B23A52" stroke-width="2.3"/>'
        f'<line x1="{ox:.0f}" y1="{oy:.0f}" x2="{c4[0]:.0f}" y2="{c4[1]:.0f}" stroke="#B23A52" stroke-width="2.3"/>'
        f'<text x="{ox:.0f}" y="{oy+18:.0f}" font-size="14" text-anchor="middle" fill="#B23A52" font-weight="700">O</text>'
    )
    body = (
        '<text x="150" y="16" font-size="14" font-weight="700" fill="#0E7C66">α-D-Glc</text>'
        '<text x="520" y="16" font-size="14" font-weight="700" fill="#1F6AA5">D-Glc, extrem reductor</text>'
        + left + right + bridge
    )
    return frame(
        800, 270, "Maltosa: enllaç glicosídic α(1→4)",
        body,
        [
            "L’oxigen vermell surt del C1 (posició α, avall) i arriba al C4 de la segona glucosa.",
            "És una condensació: en formar-se l’enllaç surt aigua. L’anomèric de la dreta queda lliure.",
            "La cel·lulosa fa servir els mateixos carbonis, però l’enllaç és β(1→4). Referència: maltosa, CID 439186.",
        ],
    )


def fig_lipids() -> str:
    # Tres molècules reals, una sota l'altra seria massa alt. Dos panells: TAG escurçat? 
    # El tripalmitin és correcte però il·legible. Fem servir el CID del tripalmitin al crèdit
    # i dibuixem un trihexanoin només si el declarem. Millor: àcid palmític + PC curt + colesterol,
    # i el text ja explica el triacilglicerol com a tres èsters. Afegiré un triacilglicerol de cadenes C6
    # generat amb la mateixa lògica que el tripalmitin (CID 11147) però amb cues de 6, i ho diré.
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
        f'<text x="560" y="290" text-anchor="middle" font-size="13" font-weight="700" fill="#5c6570">Colesterol (CID 5997)</text>'
        f'<g transform="translate(430,300)">{c}</g>'
    )
    return frame(
        780, 520, "Lípids generats amb RDKit",
        drawing,
        [
            "Cues de 6 carbonis perquè es llegeixin; el tripalmitin real (CID 11147) té el mateix èster i cues de 16.",
            "Fosfolípid: 1,2-dihexanoïl-sn-glicero-3-fosfocolina (CID 10072611), cap polar i dues cues.",
            "Colesterol (CID 5997): esteroide de quatre anells, insaponificable. No és un triacilglicerol.",
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
        780, 250, "Aminoàcid i enllaç peptídic (RDKit)",
        drawing,
        [
            "A pH 7 el grup amino és NH₃⁺ i el carboxil és COO⁻. L’estereocentre de la L-alanina és el del CID 5950.",
            "A la glicilglicina (CID 11163) l’enllaç amida és el peptídic. L’extrem N és el que porta NH₃⁺; l’extrem C, el COO⁻.",
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
        780, 340, "Nucleòtid (RDKit, CID 12599) i aparellament",
        drawing,
        [
            "El dAMP porta desoxiribosa (no hi ha OH al C2′), adenina al C1′ i fosfat al C5′.",
            "Les cadenes són antiparal·leles: el 5′ d’una queda enfront del 3′ de l’altra. A–T fa dos ponts; G–C, tres.",
        ],
    )


def fig_atp() -> str:
    drawing = rdkit_svg(PUBCHEM["atp"][1], 640, 280)
    return frame(
        700, 300, "ATP (PubChem CID 5957)",
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
