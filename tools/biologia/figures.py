"""Figures SVG originals (no copiades) del dossier de Biologia."""
from pathlib import Path

from svg import arr, box, cover, defs_arrow, svg, tx

FIGS: dict[str, str] = {}


def add(fid: str, w: int, h: int, body: str) -> None:
    FIGS[fid] = svg(w, h, defs_arrow() + body)


# ---------- 1 Biomolècules ----------
add(
    "fig-1.1",
    700,
    320,
    '<circle cx="150" cy="120" r="28" fill="#1F6AA5"/><circle cx="108" cy="78" r="16" fill="#d9dde3"/>'
    '<circle cx="198" cy="86" r="16" fill="#d9dde3"/>'
    '<line x1="128" y1="100" x2="136" y2="108" stroke="#1b1f24" stroke-width="3"/>'
    '<line x1="172" y1="104" x2="184" y2="96" stroke="#1b1f24" stroke-width="3"/>'
    + tx(150, 126, "O", 16, "#fff", "middle", "700")
    + tx(100, 70, "δ+", 14, "#B23A52", "middle", "700")
    + tx(210, 74, "δ+", 14, "#B23A52", "middle", "700")
    + tx(150, 168, "δ−", 14, "#1F6AA5", "middle", "700")
    + tx(150, 200, "molècula d’aigua", 13, "#59606a", "middle")
    + '<line x1="214" y1="86" x2="300" y2="86" stroke="#0E7C66" stroke-width="2" stroke-dasharray="5 4"/>'
    + tx(250, 74, "enllaç d’hidrogen", 12, "#0E7C66", "middle")
    + '<circle cx="360" cy="110" r="28" fill="#1F6AA5"/><circle cx="318" cy="68" r="16" fill="#d9dde3"/>'
    + '<circle cx="408" cy="70" r="16" fill="#d9dde3"/>'
    + tx(360, 116, "O", 16, "#fff", "middle", "700")
    + tx(80, 250, "L’oxigen (electronegatiu) estira els electrons: càrrega parcial negativa.", 13)
    + tx(80, 272, "Els hidrògens queden amb càrrega parcial positiva i formen ponts d’hidrogen.", 13)
    + tx(80, 300, "Per això l’aigua és un dissolvent polar i té una calor específica alta.", 13),
)

add(
    "fig-1.2",
    740,
    360,
    # alpha and beta glucopyranose, Haworth, simplified but substituents correct
    tx(180, 28, "α-D-glucopiranosa", 15, "#0E7C66", "middle", "700")
    + tx(540, 28, "β-D-glucopiranosa", 15, "#1F6AA5", "middle", "700")
    # alpha ring
    + '<polygon points="120,150 180,90 280,90 340,150 280,210 180,210" fill="#e7f5f2" stroke="#0E7C66" stroke-width="2"/>'
    + tx(230, 155, "O", 16, "#0E7C66", "middle", "700")
    + tx(300, 118, "C1", 12, "#59606a", "middle")
    + tx(300, 200, "OH", 14, "#B23A52", "middle", "700")
    + tx(300, 230, "α: OH avall", 12, "#B23A52", "middle")
    + tx(230, 78, "C5", 12, "#59606a", "middle")
    + tx(230, 58, "CH₂OH", 13, "#1b1f24", "middle", "700")
    + tx(160, 118, "C4", 12, "#59606a", "middle")
    + tx(130, 118, "OH", 13, "#1b1f24", "middle")
    + tx(160, 188, "C3", 12, "#59606a", "middle")
    + tx(160, 248, "OH", 13, "#1b1f24", "middle")
    + tx(300, 188, "C2", 12, "#59606a", "middle")
    # beta
    + '<polygon points="480,150 540,90 640,90 700,150 640,210 540,210" fill="#e8f1fa" stroke="#1F6AA5" stroke-width="2"/>'
    + tx(590, 155, "O", 16, "#1F6AA5", "middle", "700")
    + tx(660, 118, "C1", 12, "#59606a", "middle")
    + tx(690, 78, "OH", 14, "#1F6AA5", "middle", "700")
    + tx(690, 60, "β: OH amunt", 12, "#1F6AA5", "middle")
    + tx(590, 78, "C5", 12, "#59606a", "middle")
    + tx(590, 58, "CH₂OH", 13, "#1b1f24", "middle", "700")
    + tx(80, 310, "D-glucosa, forma cíclica de 6 àtoms (piranosa). En dissolució, α i β es converteixen l’una en l’altra (mutarotació) pel carboni anomèric C1.", 13)
    + tx(80, 334, "C2: OH avall · C3: OH amunt · C4: OH avall · C5: CH₂OH amunt. El carboni anomèric és el que pot obrir l’anell.", 13),
)

add(
    "fig-1.3",
    740,
    280,
    tx(370, 28, "Enllaç glicosídic α(1→4) de la maltosa", 16, "#0E7C66", "middle", "700")
    + '<rect x="40" y="70" width="200" height="90" rx="12" fill="#e7f5f2" stroke="#0E7C66" stroke-width="2"/>'
    + tx(140, 122, "α-D-glucosa", 15, "#0E7C66", "middle", "700")
    + tx(140, 144, "carboni 1", 12, "#59606a", "middle")
    + '<rect x="500" y="70" width="200" height="90" rx="12" fill="#e7f5f2" stroke="#0E7C66" stroke-width="2"/>'
    + tx(600, 122, "D-glucosa", 15, "#0E7C66", "middle", "700")
    + tx(600, 144, "carboni 4", 12, "#59606a", "middle")
    + '<line x1="240" y1="110" x2="330" y2="110" stroke="#1b1f24" stroke-width="2"/>'
    + '<circle cx="370" cy="110" r="18" fill="#1F6AA5"/>'
    + tx(370, 116, "O", 16, "#fff", "middle", "700")
    + '<line x1="388" y1="110" x2="500" y2="110" stroke="#1b1f24" stroke-width="2"/>'
    + tx(370, 160, "pont d’oxigen", 12, "#1F6AA5", "middle")
    + tx(40, 210, "És un enllaç èter entre el C1 (anomèric) d’un monosacàrid i un OH d’un altre, amb pèrdua d’aigua.", 13)
    + tx(40, 234, "Maltosa: α(1→4). Cel·lulosa: β(1→4). Amilopectina i glicogen: α(1→4) i ramificacions α(1→6).", 13)
    + tx(40, 258, "Sacarosa: α-Glc(1→2)β-Fru. El C1 queda lligat: la sacarosa no és reductora.", 13),
)

add(
    "fig-1.4",
    740,
    340,
    tx(180, 28, "Triacilglicerol", 15, "#C4651A", "middle", "700")
    + tx(540, 28, "Fosfolípid", 15, "#1F6AA5", "middle", "700")
    + '<rect x="70" y="50" width="220" height="36" rx="8" fill="#f8e6d4" stroke="#C4651A" stroke-width="2"/>'
    + tx(180, 74, "glicerol", 14, "#C4651A", "middle", "700")
    + '<rect x="70" y="110" width="30" height="150" rx="6" fill="#f3d2a8" stroke="#C4651A"/>'
    + '<rect x="160" y="110" width="30" height="170" rx="6" fill="#e7b98a" stroke="#C4651A"/>'
    + '<rect x="250" y="110" width="30" height="130" rx="6" fill="#f3d2a8" stroke="#C4651A"/>'
    + tx(180, 300, "3 àcids grassos (èster)", 12, "#59606a", "middle")
    + '<circle cx="540" cy="78" r="28" fill="#1F6AA5"/>'
    + tx(540, 83, "cap", 12, "#fff", "middle", "700")
    + tx(540, 120, "fosfat + grup polar", 12, "#1F6AA5", "middle")
    + '<rect x="500" y="140" width="26" height="140" rx="6" fill="#f3d2a8" stroke="#C4651A"/>'
    + '<rect x="554" y="140" width="26" height="120" rx="6" fill="#e7b98a" stroke="#C4651A"/>'
    + tx(540, 310, "2 cues hidròfobes", 12, "#59606a", "middle")
    + tx(40, 328, "El triacilglicerol és apolar (reserva). El fosfolípid és amfipàtic: forma la bicapa.", 13),
)

add(
    "fig-1.5",
    740,
    300,
    tx(160, 30, "Aminoàcid (pH fisiològic)", 15, "#0E7C66", "middle", "700")
    + tx(520, 30, "Enllaç peptídic", 15, "#B23A52", "middle", "700")
    + tx(70, 120, "⁺H₃N", 16, "#1F6AA5", "middle", "700")
    + tx(150, 120, "—", 18, "#1b1f24", "middle")
    + tx(200, 110, "Cα", 16, "#1b1f24", "middle", "700")
    + tx(200, 78, "R", 16, "#C4651A", "middle", "700")
    + tx(200, 150, "H", 14, "#59606a", "middle")
    + tx(270, 120, "—", 18, "#1b1f24", "middle")
    + tx(340, 120, "COO⁻", 16, "#B23A52", "middle", "700")
    + tx(200, 200, "zwitterió: el grup amino protonat,", 13, "#59606a", "middle")
    + tx(200, 220, "el carboxil desprotonat", 13, "#59606a", "middle")
    + tx(470, 110, "…C", 16, "#1b1f24", "start", "700")
    + tx(530, 100, "O", 14, "#B23A52", "middle", "700")
    + '<line x1="510" y1="108" x2="530" y2="92" stroke="#1b1f24" stroke-width="2"/>'
    + tx(560, 120, "C—N", 16, "#1b1f24", "middle", "700")
    + tx(620, 120, "Cα…", 16, "#1b1f24", "start", "700")
    + tx(575, 150, "H", 13, "#1F6AA5", "middle")
    + tx(540, 200, "condensació: surt H₂O", 13, "#59606a", "middle")
    + tx(540, 222, "enllaç amida, pla, trans", 13, "#59606a", "middle")
    + tx(40, 268, "Sentit de la cadena: extrem N (⁺H₃N—) a l’esquerra, extrem C (—COO⁻) a la dreta.", 13),
)

add(
    "fig-1.6",
    840,
    280,
    tx(40, 36, "Primària", 14, "#0E7C66", "start", "700")
    + tx(40, 58, "seqüència", 12, "#59606a")
    + tx(40, 100, "—Ala—Gly—Ser—Val—", 14, "#1b1f24", "start", "700")
    + tx(230, 36, "Secundària", 14, "#1F6AA5", "start", "700")
    + tx(230, 58, "α-hèlix / full β", 12, "#59606a")
    + '<path d="M240 90 q20 -30 40 0 t40 0 t40 0" fill="none" stroke="#1F6AA5" stroke-width="3"/>'
    + tx(240, 140, "ponts d’H de l’esquelet", 12, "#59606a")
    + tx(470, 36, "Terciària", 14, "#C4651A", "start", "700")
    + '<circle cx="540" cy="110" r="40" fill="none" stroke="#C4651A" stroke-width="3"/>'
    + tx(500, 170, "R: hidròfobs, iònics,", 12, "#59606a")
    + tx(500, 188, "H, ponts S–S", 12, "#59606a")
    + tx(640, 36, "Quaternària", 14, "#5C4B8A", "start", "700")
    + '<circle cx="680" cy="100" r="22" fill="#efe8fb" stroke="#5C4B8A" stroke-width="2"/>'
    + '<circle cx="710" cy="130" r="22" fill="#efe8fb" stroke="#5C4B8A" stroke-width="2"/>'
    + tx(640, 188, "dues cadenes o més", 12, "#59606a")
    + tx(40, 240, "L’hèlix α: pont d’hidrogen entre el C=O del residu i i l’N–H del residu i+4. El full β: ponts entre cadenes veïnes.", 13)
    + tx(40, 262, "Desnaturalitzar trenca les estructures 2a, 3a i 4a; la seqüència (1a) es manté. No tots els pròtids tenen estructura quaternària.", 13),
)

add(
    "fig-1.7",
    760,
    340,
    tx(40, 28, "Nucleòtid", 15, "#5C4B8A", "start", "700")
    + box(40, 70, 120, 44, "#efe8fb", "#5C4B8A", text="fosfat", tfill="#5C4B8A")
    + box(40, 130, 160, 44, "#e7f5f2", "#0E7C66", text="pentosa", tfill="#0E7C66")
    + box(40, 190, 180, 44, "#fde8ec", "#B23A52", text="base nitrogenada", tfill="#B23A52")
    + tx(40, 270, "DNA: desoxiribosa, A T G C", 13)
    + tx(40, 292, "RNA: ribosa, A U G C", 13)
    + tx(40, 314, "Enllaç fosfodièster 3′–5′", 13)
    + tx(430, 28, "Doble hèlix (B-DNA)", 15, "#1F6AA5", "middle", "700")
    + '<path d="M400 60 C 470 100, 470 140, 400 180 C 330 220, 330 260, 400 300" fill="none" stroke="#1F6AA5" stroke-width="4"/>'
    + '<path d="M500 60 C 430 100, 430 140, 500 180 C 570 220, 570 260, 500 300" fill="none" stroke="#0E7C66" stroke-width="4"/>'
    + tx(392, 52, "5′", 13, "#1F6AA5", "middle", "700")
    + tx(508, 52, "3′", 13, "#0E7C66", "middle", "700")
    + tx(392, 322, "3′", 13, "#1F6AA5", "middle", "700")
    + tx(508, 322, "3′", 13, "#0E7C66", "middle", "700")
    + '<line x1="410" y1="110" x2="490" y2="110" stroke="#C4651A" stroke-width="2"/>'
    + '<line x1="410" y1="170" x2="490" y2="170" stroke="#5C4B8A" stroke-width="3"/>'
    + tx(560, 114, "A–T : 2 ponts d’H", 12, "#C4651A")
    + tx(560, 174, "G–C : 3 ponts d’H", 12, "#5C4B8A")
    + tx(330, 250, "antiparal·leles", 12, "#59606a", "middle"),
)

add(
    "fig-1.8",
    760,
    300,
    tx(380, 28, "Mapa: biomolècules", 16, "#0E7C66", "middle", "700")
    + box(300, 46, 160, 40, "#0E7C66", "#0E7C66", text="biomolècula", tfill="#fff")
    + box(20, 130, 140, 40, "#e8f1fa", "#1F6AA5", text="aigua i sals", tfill="#1F6AA5", size=12)
    + box(175, 130, 120, 40, "#e7f5f2", "#0E7C66", text="glúcids", tfill="#0E7C66", size=12)
    + box(310, 130, 120, 40, "#f8e6d4", "#C4651A", text="lípids", tfill="#C4651A", size=12)
    + box(445, 130, 130, 40, "#fde8ec", "#B23A52", text="pròtids", tfill="#B23A52", size=12)
    + box(590, 130, 150, 40, "#efe8fb", "#5C4B8A", text="àcids nucleics", tfill="#5C4B8A", size=12)
    + arr(360, 86, 90, 130, "#59606a")
    + arr(370, 86, 230, 130, "#59606a")
    + arr(380, 86, 370, 130, "#59606a")
    + arr(400, 86, 500, 130, "#59606a")
    + arr(430, 86, 660, 130, "#59606a")
    + tx(40, 210, "Funció energètica: glúcids, triacilglicerols.", 13)
    + tx(40, 232, "Funció estructural: cel·lulosa, fosfolípids, col·lagen, queratina.", 13)
    + tx(40, 254, "Funció reguladora: enzims, hormones proteiques, esteroides.", 13)
    + tx(40, 276, "Informació: DNA i RNA.", 13),
)

# ---------- 2 Cèl·lula ----------
add(
    "fig-2.1",
    740,
    300,
    tx(160, 28, "Cèl·lula procariota", 15, "#A67C12", "middle", "700")
    + tx(530, 28, "Cèl·lula eucariota", 15, "#1F6AA5", "middle", "700")
    + '<ellipse cx="160" cy="150" rx="130" ry="80" fill="#fff8e8" stroke="#A67C12" stroke-width="3"/>'
    + '<ellipse cx="150" cy="150" rx="40" ry="22" fill="none" stroke="#C4651A" stroke-width="2" stroke-dasharray="4 3"/>'
    + tx(150, 154, "nucleoide", 12, "#C4651A", "middle", "700")
    + tx(40, 250, "DNA circular, ribosomes 70S,", 12)
    + tx(40, 268, "sense orgànuls amb membrana", 12)
    + '<ellipse cx="540" cy="150" rx="140" ry="90" fill="#e8f1fa" stroke="#1F6AA5" stroke-width="3"/>'
    + '<circle cx="520" cy="140" r="32" fill="#efe8fb" stroke="#5C4B8A" stroke-width="2"/>'
    + tx(520, 144, "nucli", 12, "#5C4B8A", "middle", "700")
    + '<ellipse cx="600" cy="175" rx="22" ry="12" fill="#fde8ec" stroke="#B23A52"/>'
    + tx(400, 250, "DNA lineal dins el nucli,", 12)
    + tx(400, 268, "ribosomes 80S, orgànuls", 12),
)

add(
    "fig-2.2",
    740,
    320,
    tx(370, 26, "Mosaic fluid", 16, "#1F6AA5", "middle", "700")
    + '<rect x="40" y="70" width="660" height="28" fill="#d6e6f5"/>'
    + '<rect x="40" y="150" width="660" height="28" fill="#d6e6f5"/>'
    # heads and tails
    + "".join(
        f'<circle cx="{x}" cy="84" r="8" fill="#1F6AA5"/><circle cx="{x}" cy="164" r="8" fill="#1F6AA5"/>'
        f'<line x1="{x}" y1="92" x2="{x-6}" y2="130" stroke="#C4651A" stroke-width="2"/>'
        f'<line x1="{x}" y1="92" x2="{x+6}" y2="130" stroke="#C4651A" stroke-width="2"/>'
        f'<line x1="{x}" y1="156" x2="{x-6}" y2="118" stroke="#C4651A" stroke-width="2"/>'
        f'<line x1="{x}" y1="156" x2="{x+6}" y2="118" stroke="#C4651A" stroke-width="2"/>'
        for x in range(60, 700, 28)
    )
    + '<rect x="250" y="78" width="36" height="92" rx="8" fill="#5C4B8A"/>'
    + tx(268, 130, "P", 12, "#fff", "middle", "700")
    + tx(250, 60, "proteïna integral", 11, "#5C4B8A", "middle")
    + '<rect x="430" y="150" width="50" height="22" rx="6" fill="#0E7C66"/>'
    + tx(455, 190, "perifèrica", 11, "#0E7C66", "middle")
    + '<circle cx="560" cy="70" r="10" fill="#B23A52"/>'
    + tx(590, 58, "glicocàlix", 11, "#B23A52")
    + tx(120, 210, "colesterol (animals)", 11, "#A67C12")
    + '<rect x="80" y="118" width="10" height="22" rx="2" fill="#A67C12"/>'
    + tx(40, 250, "Bicapa de fosfolípids. Cues hidròfobes a l’interior, caps polars cap a l’aigua.", 13)
    + tx(40, 272, "Les proteïnes i els lípids es desplacen lateralment: la membrana és fluida, no rígida.", 13)
    + tx(40, 294, "El glicocàlix (oligosacàrids) és al costat extracel·lular i intervé en el reconeixement.", 13),
)

add(
    "fig-2.3",
    760,
    380,
    tx(180, 24, "Cèl·lula animal", 15, "#B23A52", "middle", "700")
    + tx(560, 24, "Cèl·lula vegetal", 15, "#3E7A32", "middle", "700")
    + '<ellipse cx="180" cy="190" rx="150" ry="120" fill="#fff5f7" stroke="#B23A52" stroke-width="2"/>'
    + '<circle cx="180" cy="170" r="36" fill="#efe8fb" stroke="#5C4B8A" stroke-width="2"/>'
    + tx(180, 174, "nucli", 12, "#5C4B8A", "middle", "700")
    + '<ellipse cx="100" cy="150" rx="22" ry="12" fill="#fde8ec" stroke="#B23A52"/>'
    + tx(70, 140, "mitocondri", 11, "#B23A52")
    + '<rect x="230" y="140" width="40" height="16" rx="3" fill="#e7f5f2" stroke="#0E7C66"/>'
    + tx(210, 130, "Golgi", 11, "#0E7C66")
    + '<circle cx="250" cy="230" r="10" fill="#f8e6d4" stroke="#C4651A"/>'
    + tx(230, 258, "lisosoma", 11, "#C4651A")
    + '<circle cx="120" cy="230" r="4" fill="#1F6AA5"/><circle cx="132" cy="230" r="4" fill="#1F6AA5"/>'
    + tx(90, 268, "centríols", 11, "#1F6AA5")
    + '<rect x="420" y="70" width="300" height="250" rx="8" fill="none" stroke="#3E7A32" stroke-width="8"/>'
    + '<rect x="436" y="86" width="268" height="218" rx="6" fill="#f3faf0" stroke="#3E7A32" stroke-width="2"/>'
    + '<ellipse cx="620" cy="200" rx="70" ry="50" fill="#e7f5f2" stroke="#0E7C66" stroke-width="2"/>'
    + tx(620, 204, "vacuol", 12, "#0E7C66", "middle", "700")
    + '<ellipse cx="500" cy="150" rx="28" ry="16" fill="#cfe8c4" stroke="#3E7A32" stroke-width="2"/>'
    + tx(470, 130, "cloroplast", 11, "#3E7A32")
    + '<circle cx="520" cy="240" r="22" fill="#efe8fb" stroke="#5C4B8A"/>'
    + tx(520, 244, "nucli", 11, "#5C4B8A", "middle")
    + tx(40, 340, "La paret vegetal és de cel·lulosa, per fora de la membrana. Els centríols són típics de la cèl·lula animal.", 13)
    + tx(40, 362, "Totes dues tenen nucli, mitocondris, reticle, Golgi i ribosomes 80S.", 13),
)

add(
    "fig-2.4",
    720,
    300,
    tx(360, 24, "Mitocondri", 16, "#B23A52", "middle", "700")
    + '<ellipse cx="340" cy="150" rx="250" ry="100" fill="#fff5f7" stroke="#B23A52" stroke-width="3"/>'
    + '<ellipse cx="340" cy="150" rx="210" ry="70" fill="none" stroke="#1F6AA5" stroke-width="3"/>'
    + '<path d="M220 150 q30 -40 60 0 t60 0 t60 0 t60 0" fill="none" stroke="#1F6AA5" stroke-width="3"/>'
    + tx(80, 70, "membrana externa", 12, "#B23A52")
    + tx(200, 100, "espai intermembranós", 12, "#59606a")
    + tx(250, 200, "membrana interna (crestes): cadena i ATP-sintasa", 12, "#1F6AA5")
    + tx(250, 250, "matriu: cicle de Krebs, β-oxidació, DNA propi, ribosomes 70S", 12, "#1b1f24"),
)

add(
    "fig-2.5",
    720,
    300,
    tx(360, 24, "Cloroplast", 16, "#3E7A32", "middle", "700")
    + '<ellipse cx="350" cy="150" rx="260" ry="100" fill="#f3faf0" stroke="#3E7A32" stroke-width="3"/>'
    + '<ellipse cx="350" cy="150" rx="230" ry="78" fill="none" stroke="#0E7C66" stroke-width="2"/>'
    + "".join(
        f'<rect x="{x}" y="120" width="70" height="14" rx="3" fill="#7dbe63" stroke="#3E7A32"/>'
        f'<rect x="{x}" y="138" width="70" height="14" rx="3" fill="#7dbe63" stroke="#3E7A32"/>'
        f'<rect x="{x}" y="156" width="70" height="14" rx="3" fill="#7dbe63" stroke="#3E7A32"/>'
        for x in (180, 280, 400)
    )
    + tx(180, 110, "granum (tilacoides)", 12, "#3E7A32")
    + tx(80, 250, "Fase lluminosa: membrana del tilacoide.", 13)
    + tx(80, 272, "Cicle de Calvin: estroma. El cloroplast té DNA propi i ribosomes 70S.", 13),
)

add(
    "fig-2.6",
    780,
    250,
    tx(390, 22, "Mitosi (una cèl·lula 2n = 4, esquema)", 15, "#1F6AA5", "middle", "700")
    + "".join(
        box(20 + i * 150, 50, 130, 150, "#f7fafc", "#1F6AA5", sw=1.2, rx=10)
        + tx(85 + i * 150, 74, name, 13, "#1F6AA5", "middle", "700")
        + tx(85 + i * 150, 160, sub, 11, "#59606a", "middle")
        for i, (name, sub) in enumerate(
            [
                ("Profase", "cromosomes\ncondensats"),
                ("Metafase", "placa equatorial"),
                ("Anafase", "es separen les\ncromàtides"),
                ("Telofase", "dos nuclis"),
                ("Citocinesi", "dues cèl·lules 2n"),
            ]
        )
    )
    # fix multiline - the \n won't render. I'll overlay short labels only. The sub with newline is bad.
    ,
)

# The mitosis labels with \n are ugly. I'll rebuild fig-2.6 and meiosis more carefully below by overwriting.
FIGS["fig-2.6"] = svg(
    780,
    230,
    defs_arrow()
    + tx(390, 24, "Mitosi · se separen cromàtides germanes · dues cèl·lules 2n idèntiques", 14, "#1F6AA5", "middle", "700")
    + "".join(
        box(16 + i * 154, 46, 140, 150, "#f7fafc", "#1F6AA5", sw=1.2, rx=10)
        + tx(86 + i * 154, 78, name, 14, "#1F6AA5", "middle", "700")
        + tx(86 + i * 154, 120, a, 12, "#1b1f24", "middle")
        + tx(86 + i * 154, 142, b, 12, "#59606a", "middle")
        for i, (name, a, b) in enumerate(
            [
                ("Profase", "es condensen", "desapareix l’embolcall"),
                ("Metafase", "a l’equador", "fus unit al cinetocor"),
                ("Anafase", "cromàtides", "cap als pols"),
                ("Telofase", "dos nuclis", "es descondensen"),
                ("Citocinesi", "dues cèl·lules", "cadascuna 2n"),
            ]
        )
    ),
)

FIGS["fig-2.7"] = svg(
    780,
    280,
    defs_arrow()
    + tx(390, 22, "Meiosi · una cèl·lula 2n dona quatre cèl·lules n diferents", 14, "#5C4B8A", "middle", "700")
    + box(20, 46, 360, 90, "#f7f4fb", "#5C4B8A", sw=1.2)
    + tx(200, 78, "Meiosi I (reduccional)", 14, "#5C4B8A", "middle", "700")
    + tx(200, 104, "Profase I: entrecreuament. Anafase I: se separen els homòlegs.", 12, "#1b1f24", "middle")
    + box(400, 46, 360, 90, "#f7f4fb", "#5C4B8A", sw=1.2)
    + tx(580, 78, "Meiosi II (equacional)", 14, "#5C4B8A", "middle", "700")
    + tx(580, 104, "Com una mitosi: se separen cromàtides germanes.", 12, "#1b1f24", "middle")
    + tx(40, 180, "Resultat: 4 nuclis haploides, genèticament diferents (entrecreuament + repartiment a l’atzar).", 13)
    + tx(40, 206, "Funció: gàmetes (animals) o espores (plantes, en el cicle que toqui). No és per créixer.", 13)
    + tx(40, 232, "La mitosi conserva 2n i fa còpies. La meiosi redueix a n i genera variació.", 13)
    + tx(40, 258, "Lligament: gens del mateix cromosoma. La recombinació es mesura a la profase I.", 13),
)

add(
    "fig-2.8",
    740,
    240,
    tx(370, 24, "Mapa de la cèl·lula", 16, "#1F6AA5", "middle", "700")
    + box(270, 44, 200, 36, "#1F6AA5", "#1F6AA5", text="cèl·lula", tfill="#fff")
    + box(30, 120, 150, 36, "#fff8e8", "#A67C12", text="procariota", tfill="#A67C12", size=13)
    + box(200, 120, 150, 36, "#e8f1fa", "#1F6AA5", text="animal", tfill="#1F6AA5", size=13)
    + box(370, 120, 150, 36, "#f3faf0", "#3E7A32", text="vegetal", tfill="#3E7A32", size=13)
    + box(540, 120, 170, 36, "#f7f4fb", "#5C4B8A", text="cicle: mitosi / meiosi", tfill="#5C4B8A", size=12)
    + arr(340, 80, 100, 120, "#59606a")
    + arr(360, 80, 270, 120, "#59606a")
    + arr(390, 80, 440, 120, "#59606a")
    + arr(420, 80, 610, 120, "#59606a")
    + tx(30, 190, "Membrana: mosaic fluid. Transport: difusió, facilitat, actiu, endocitosi i exocitosi.", 13)
    + tx(30, 214, "Mitocondri: respiració. Cloroplast: fotosíntesi. Nucli: DNA lineal, només eucariotes.", 13),
)

# ---------- 3 Metabolisme ----------
add(
    "fig-3.1",
    760,
    280,
    tx(380, 24, "Esquema general", 16, "#C4651A", "middle", "700")
    + box(40, 60, 200, 50, "#fde8ec", "#B23A52", text="catabolisme", tfill="#B23A52")
    + tx(140, 140, "oxida, allibera energia", 12, "#59606a", "middle")
    + box(280, 60, 200, 50, "#fff8e8", "#A67C12", text="ATP, NADH", tfill="#A67C12")
    + box(520, 60, 200, 50, "#e7f5f2", "#0E7C66", text="anabolisme", tfill="#0E7C66")
    + tx(620, 140, "redueix, consumeix energia", 12, "#59606a", "middle")
    + arr(240, 85, 280, 85, "#59606a")
    + arr(480, 85, 520, 85, "#59606a")
    + tx(40, 190, "Una via és una seqüència de reaccions amb enzims. Una reacció n’és només un pas.", 13)
    + tx(40, 214, "L’ATP transporta energia química. NADH, NADPH i FADH₂ transporten poder reductor.", 13)
    + tx(40, 238, "NADH i FADH₂ van sobretot al catabolisme. El NADPH va sobretot a l’anabolisme.", 13)
    + tx(40, 262, "La síntesi de proteïnes (traducció) es tracta al tema de genètica molecular.", 13),
)

add(
    "fig-3.2",
    760,
    250,
    tx(380, 24, "Glucòlisi al citosol", 16, "#C4651A", "middle", "700")
    + box(20, 70, 140, 50, "#fff", "#1b1f24", text="glucosa", size=14)
    + box(200, 70, 150, 50, "#f8e6d4", "#C4651A", text="−2 ATP", tfill="#C4651A")
    + box(390, 70, 160, 50, "#e7f5f2", "#0E7C66", text="+4 ATP, +2 NADH", tfill="#0E7C66", size=13)
    + box(590, 70, 150, 50, "#e8f1fa", "#1F6AA5", text="2 piruvat", tfill="#1F6AA5")
    + arr(160, 95, 200, 95)
    + arr(350, 95, 390, 95)
    + arr(550, 95, 590, 95)
    + tx(40, 170, "Balanç net per glucosa: 2 ATP i 2 NADH. No cal oxigen. El producte són dos piruvats (3C).", 13)
    + tx(40, 194, "Inversió: hexocinasa i fosfofructocinasa. Guany: fosforilació a nivell de substrat.", 13)
    + tx(40, 218, "Els tres passos irreversibles (hexocinasa, fosfofructocinasa, piruvat-cinasa) regulen la via.", 13),
)

add(
    "fig-3.3",
    760,
    320,
    tx(380, 22, "Cicle de Krebs (matriu), per cada acetil-CoA", 15, "#C4651A", "middle", "700")
    + '<circle cx="370" cy="160" r="78" fill="none" stroke="#C4651A" stroke-width="3"/>'
    + tx(370, 150, "Krebs", 16, "#C4651A", "middle", "700")
    + tx(370, 172, "oxaloacetat", 12, "#59606a", "middle")
    + tx(370, 190, "es regenera", 12, "#59606a", "middle")
    + box(20, 70, 160, 44, "#f8e6d4", "#C4651A", text="acetil-CoA", tfill="#C4651A", size=13)
    + arr(180, 92, 292, 130, "#C4651A")
    + tx(560, 80, "2 CO₂", 14, "#1b1f24", "start", "700")
    + tx(560, 110, "3 NADH", 14, "#1F6AA5", "start", "700")
    + tx(560, 140, "1 FADH₂", 14, "#5C4B8A", "start", "700")
    + tx(560, 170, "1 GTP (≈ 1 ATP)", 14, "#0E7C66", "start", "700")
    + tx(20, 240, "Abans: piruvat (matriu) → acetil-CoA + CO₂ + NADH. Per glucosa, el cicle gira dues vegades.", 13)
    + tx(20, 264, "Ordre dels intermedis: citrat, isocitrat, α-cetoglutarat, succinil-CoA, succinat, fumarat, malat, oxaloacetat.", 12)
    + tx(20, 288, "El CO₂ d’aquesta fase no és el que «respirem» com a objectiu: l’objectiu és extreure electrons (NADH, FADH₂).", 13),
)

add(
    "fig-3.4",
    760,
    280,
    tx(380, 22, "Cadena respiratòria · membrana interna", 15, "#1F6AA5", "middle", "700")
    + "".join(
        box(40 + i * 140, 60, 110, 44, col, col, text=name, tfill="#fff", size=13)
        for i, (name, col) in enumerate(
            [("I", "#1F6AA5"), ("II", "#5C4B8A"), ("III", "#0E7C66"), ("IV", "#B23A52"), ("ATP-sintasa", "#C4651A")]
        )
    )
    + tx(40, 130, "NADH entra pel complex I. El FADH₂ (succinat) entra pel complex II i salta el I.", 13)
    + tx(40, 154, "L’acceptor final és l’O₂, al complex IV: ½ O₂ + 2 e⁻ + 2 H⁺ → H₂O (per cada parell d’electrons).", 13)
    + tx(40, 178, "El gradient de protons torna a la matriu per l’ATP-sintasa (quimiosmosi).", 13)
    + tx(40, 210, "P/O actual: NADH ≈ 2,5 ATP; FADH₂ ≈ 1,5 ATP. Per això una glucosa rendeix uns 30–32 ATP.", 13)
    + tx(40, 234, "Balanç clàssic (3 i 2): 38 ATP (llançadora malat-aspartat o procariota) o 36 (llançadora del glicerol-fosfat).", 13)
    + tx(40, 258, "Sense O₂ la cadena s’atura, el NADH no es reoxida i el Krebs s’atura.", 13),
)

add(
    "fig-3.5",
    740,
    240,
    tx(370, 24, "Fermentacions: regeneren el NAD⁺", 15, "#C4651A", "middle", "700")
    + box(40, 60, 150, 44, "#fff", "#1b1f24", text="2 piruvat")
    + box(230, 50, 220, 40, "#fde8ec", "#B23A52", text="làctica → 2 lactat", tfill="#B23A52", size=13)
    + box(230, 110, 280, 40, "#f8e6d4", "#C4651A", text="alcohòlica → 2 etanol + 2 CO₂", tfill="#C4651A", size=13)
    + arr(190, 82, 230, 70, "#B23A52")
    + arr(190, 90, 230, 130, "#C4651A")
    + tx(40, 180, "Balanç net des de glucosa: 2 ATP. El NADH de la glucòlisi es consumeix; no hi ha cadena.", 13)
    + tx(40, 204, "Làctica: múscul en dèficit d’oxigen, iogurt. Alcohòlica: llevat, pa i vi. Són degradacions parcials.", 13)
    + tx(40, 228, "No és el mateix que la respiració anaeròbica bacteriana (cadena amb un acceptor inorgànic diferent de l’O₂).", 12),
)

add(
    "fig-3.6",
    760,
    300,
    tx(380, 22, "Esquema en Z (fase lluminosa acíclica)", 15, "#3E7A32", "middle", "700")
    + '<polyline points="60,200 140,80 220,170 300,70 400,160 500,60 620,150" fill="none" stroke="#3E7A32" stroke-width="3"/>'
    + tx(50, 230, "H₂O", 13, "#1F6AA5", "middle", "700")
    + tx(140, 70, "P680*", 12, "#3E7A32", "middle", "700")
    + tx(230, 190, "PQ", 12, "#59606a", "middle")
    + tx(310, 60, "b₆f", 12, "#0E7C66", "middle", "700")
    + tx(410, 180, "PC / P700*", 12, "#1F6AA5", "middle")
    + tx(560, 50, "ferredoxina", 12, "#C4651A", "middle")
    + tx(640, 170, "NADPH", 13, "#0E7C66", "middle", "700")
    + tx(40, 260, "L’aigua es trenca al fotosistema II (fotòlisi) i l’O₂ surt d’aquí, no del CO₂.", 13)
    + tx(40, 282, "Electrons: PSII → plastoquinona → citocrom b₆f → plastocianina → PSI → NADP⁺.", 13),
)

add(
    "fig-3.7",
    740,
    260,
    tx(370, 22, "Cicle de Calvin (estroma), per cada CO₂", 15, "#3E7A32", "middle", "700")
    + '<circle cx="300" cy="130" r="70" fill="none" stroke="#3E7A32" stroke-width="3"/>'
    + tx(300, 126, "RuBP", 14, "#3E7A32", "middle", "700")
    + tx(300, 146, "5C", 12, "#59606a", "middle")
    + tx(80, 80, "CO₂", 14, "#1b1f24", "middle", "700")
    + arr(110, 90, 230, 120, "#3E7A32")
    + tx(150, 70, "rubisco", 12, "#3E7A32", "middle")
    + tx(500, 80, "3-PGA → G3P", 14, "#1F6AA5", "start", "700")
    + tx(500, 110, "gasta ATP i NADPH", 13, "#59606a")
    + tx(500, 150, "una part de G3P surt", 13)
    + tx(500, 174, "(sucre). La resta", 13)
    + tx(500, 198, "regenera RuBP (ATP).", 13)
    + tx(40, 230, "Per fixar 1 CO₂ calen 2 NADPH i 3 ATP. Per a una glucosa (6 CO₂): 12 NADPH i 18 ATP.", 13),
)

add(
    "fig-3.8",
    760,
    220,
    tx(380, 22, "On passa cada via (eucariota)", 15, "#C4651A", "middle", "700")
    + box(20, 50, 170, 70, "#fff8e8", "#A67C12", text="", size=12)
    + tx(105, 80, "citosol", 14, "#A67C12", "middle", "700")
    + tx(105, 100, "glucòlisi", 12, "#1b1f24", "middle")
    + box(210, 50, 250, 70, "#fde8ec", "#B23A52")
    + tx(335, 78, "mitocondri", 14, "#B23A52", "middle", "700")
    + tx(335, 98, "piruvat, Krebs, β-oxidació, cadena", 11, "#1b1f24", "middle")
    + box(480, 50, 250, 70, "#f3faf0", "#3E7A32")
    + tx(605, 78, "cloroplast", 14, "#3E7A32", "middle", "700")
    + tx(605, 98, "fase lluminosa i Calvin", 12, "#1b1f24", "middle")
    + tx(20, 160, "Fermentació: citosol. Lipogènesi: citosol (gasta NADPH). Fotosíntesi bacteriana: membrana.", 13)
    + tx(20, 184, "Quimiosíntesi: bacteris, sense llum; oxiden un compost inorgànic i fixen CO₂.", 13)
    + tx(20, 208, "Respiració aeròbica ≈ 30–32 ATP/glucosa. Fermentació = 2 ATP/glucosa.", 13),
)

# ---------- 4 Mendel ----------
add(
    "fig-4.1",
    640,
    280,
    tx(320, 24, "Quadre de Punnett · Aa × Aa", 15, "#5C4B8A", "middle", "700")
    + box(180, 50, 80, 40, "#efe8fb", "#5C4B8A", text="A", tfill="#5C4B8A")
    + box(260, 50, 80, 40, "#efe8fb", "#5C4B8A", text="a", tfill="#5C4B8A")
    + box(100, 90, 80, 50, "#efe8fb", "#5C4B8A", text="A", tfill="#5C4B8A")
    + box(100, 140, 80, 50, "#efe8fb", "#5C4B8A", text="a", tfill="#5C4B8A")
    + box(180, 90, 80, 50, "#e7f5f2", "#0E7C66", text="AA", tfill="#0E7C66")
    + box(260, 90, 80, 50, "#e8f1fa", "#1F6AA5", text="Aa", tfill="#1F6AA5")
    + box(180, 140, 80, 50, "#e8f1fa", "#1F6AA5", text="Aa", tfill="#1F6AA5")
    + box(260, 140, 80, 50, "#fde8ec", "#B23A52", text="aa", tfill="#B23A52")
    + tx(40, 230, "Genotips 1:2:1. Si A domina completament, fenotips 3:1.", 14)
    + tx(40, 254, "Encreuament prova Aa × aa → 1:1. No és el mateix que la F2.", 14),
)

add(
    "fig-4.3",
    700,
    280,
    tx(350, 24, "Pedigrí · autosòmic recessiu (exemple)", 15, "#5C4B8A", "middle", "700")
    + '<rect x="80" y="60" width="28" height="28" fill="#fff" stroke="#1b1f24" stroke-width="2"/>'
    + '<circle cx="160" cy="74" r="14" fill="#fff" stroke="#1b1f24" stroke-width="2"/>'
    + '<line x1="108" y1="74" x2="146" y2="74" stroke="#1b1f24" stroke-width="2"/>'
    + '<line x1="134" y1="74" x2="134" y2="120" stroke="#1b1f24" stroke-width="2"/>'
    + '<line x1="80" y1="120" x2="220" y2="120" stroke="#1b1f24"/>'
    + '<rect x="66" y="120" width="28" height="28" fill="#5C4B8A" stroke="#1b1f24" stroke-width="2"/>'
    + '<circle cx="160" cy="134" r="14" fill="#fff" stroke="#1b1f24" stroke-width="2"/>'
    + '<rect x="206" y="120" width="28" height="28" fill="#fff" stroke="#1b1f24" stroke-width="2"/>'
    + tx(80, 200, "Quadrat: home. Cercle: dona. Ple: afectat.", 13)
    + tx(80, 224, "Dos pares no afectats amb un fill afectat: l’al·lel és recessiu i tots dos són portadors.", 13)
    + tx(80, 248, "Si afecta homes i dones i el pare afectat té filles no afectades, no és lligat a l’X dominant.", 13),
)

add(
    "fig-4.4",
    720,
    240,
    tx(360, 24, "Lligat a l’X recessiu · mare portadora × pare sa", 15, "#B23A52", "middle", "700")
    + tx(40, 70, "XᴴXʰ  ×  XᴴY", 18, "#1b1f24", "start", "700")
    + tx(40, 110, "Fills: ½ XᴴXᴴ noia sana, ½ XᴴXʰ noia portadora,", 14)
    + tx(40, 136, "½ XᴴY noi sa, ½ XʰY noi afectat.", 14)
    + tx(40, 176, "Un home és hemizigot: un sol al·lel, el de l’X, ja es manifesta.", 14)
    + tx(40, 202, "No hi ha transmissió home → fill home: el pare dona l’Y als fills.", 14)
    + tx(40, 228, "Exemples clàssics: hemofília i daltonisme.", 14),
)

add(
    "fig-4.5",
    720,
    180,
    tx(360, 24, "Mapa de l’herència", 15, "#5C4B8A", "middle", "700")
    + box(20, 60, 150, 40, "#efe8fb", "#5C4B8A", text="1 gen", tfill="#5C4B8A", size=13)
    + box(190, 60, 160, 40, "#e8f1fa", "#1F6AA5", text="2 gens lliures", tfill="#1F6AA5", size=13)
    + box(370, 60, 150, 40, "#f8e6d4", "#C4651A", text="lligats", tfill="#C4651A", size=13)
    + box(540, 60, 160, 40, "#fde8ec", "#B23A52", text="lligats a l’X", tfill="#B23A52", size=13)
    + tx(20, 140, "Lliures: 9:3:3:1. Lligats: més parentals que recombinants. 50 % de recombinació = es comporten com a lliures.", 13)
    + tx(20, 164, "Codominància (ABO) i dominància incompleta donen 1:2:1, no 3:1.", 13),
)

# ---------- 5 Molecular ----------
add(
    "fig-5.1",
    720,
    180,
    tx(360, 24, "Dogma central (amb l’excepció dels retrovirus)", 14, "#B23A52", "middle", "700")
    + box(40, 60, 120, 44, "#e8f1fa", "#1F6AA5", text="DNA", tfill="#1F6AA5")
    + box(280, 60, 120, 44, "#e7f5f2", "#0E7C66", text="RNA", tfill="#0E7C66")
    + box(520, 60, 150, 44, "#fde8ec", "#B23A52", text="proteïna", tfill="#B23A52")
    + arr(160, 82, 280, 82, "#1b1f24")
    + arr(400, 82, 520, 82, "#1b1f24")
    + tx(190, 70, "transcripció", 12, "#59606a", "middle")
    + tx(450, 70, "traducció", 12, "#59606a", "middle")
    + tx(40, 140, "Replicació: DNA → DNA. Retrotranscripció (retrovirus): RNA → DNA. No és el camí habitual de la cèl·lula.", 13)
    + tx(40, 164, "El RNA no es tradueix «sencer»: es llegeix el marc de lectura de l’RNAm, de l’AUG fins al codó de parada.", 13),
)

add(
    "fig-5.2",
    760,
    280,
    tx(380, 22, "Forquilla de replicació (model procariota)", 15, "#1F6AA5", "middle", "700")
    + '<line x1="40" y1="90" x2="420" y2="90" stroke="#1F6AA5" stroke-width="4"/>'
    + '<line x1="40" y1="170" x2="300" y2="170" stroke="#0E7C66" stroke-width="4"/>'
    + '<line x1="300" y1="170" x2="360" y2="130" stroke="#0E7C66" stroke-width="4"/>'
    + '<line x1="360" y1="130" x2="420" y2="90" stroke="#C4651A" stroke-width="3"/>'
    + tx(40, 78, "3′", 13, "#1F6AA5", "start", "700")
    + tx(430, 94, "5′  cadena líder, contínua", 13, "#1F6AA5")
    + tx(40, 190, "5′", 13, "#0E7C66", "start", "700")
    + tx(40, 220, "cadena retardada: fragments d’Okazaki, cadascun amb encebador de RNA", 13)
    + tx(40, 246, "Helicasa obre. Primasa posa l’encebador. DNA-polimerasa III allarga només en sentit 5′→3′.", 13)
    + tx(40, 268, "DNA-polimerasa I treu l’encebador i omple. La ligasa tanca el fosfodièster. La topoisomerasa destensa.", 12),
)

add(
    "fig-5.3",
    740,
    200,
    tx(370, 24, "Transcripció", 15, "#0E7C66", "middle", "700")
    + tx(40, 70, "Cadena motlle  3′–TAC AAA GGG–5′", 16, "#1b1f24", "start", "700")
    + tx(40, 110, "RNAm          5′–AUG UUU CCC–3′", 16, "#0E7C66", "start", "700")
    + tx(40, 150, "La polimerasa llegeix el motlle 3′→5′ i sintetitza 5′→3′. L’RNAm coincideix amb la cadena codificant, amb U per T.", 13)
    + tx(40, 178, "Procariotes: un RNA-polimerasa i factor σ. Eucariotes: maduració (cap 5′, cua poli-A, eliminació d’introns).", 12),
)

add(
    "fig-5.4",
    740,
    240,
    tx(370, 22, "Ribosoma", 15, "#B23A52", "middle", "700")
    + '<ellipse cx="360" cy="90" rx="180" ry="36" fill="#fde8ec" stroke="#B23A52" stroke-width="2"/>'
    + '<ellipse cx="360" cy="130" rx="200" ry="28" fill="#fff" stroke="#B23A52" stroke-width="2"/>'
    + tx(250, 96, "E", 14, "#59606a", "middle", "700")
    + tx(360, 96, "P", 14, "#1F6AA5", "middle", "700")
    + tx(470, 96, "A", 14, "#0E7C66", "middle", "700")
    + tx(40, 180, "A: entra l’aminoacil-RNAt. P: porta la cadena. E: surt l’RNAt buit.", 13)
    + tx(40, 204, "El ribosoma llegeix l’RNAm 5′→3′. L’enllaç peptídic el fa el centre peptidil-transferasa.", 13)
    + tx(40, 228, "Inici: AUG (Met; en bacteris, formilmetionina). Parada: UAA, UAG o UGA, amb factor d’alliberament.", 12),
)

add(
    "fig-5.5",
    740,
    200,
    tx(370, 24, "PCR: un cicle", 15, "#C4651A", "middle", "700")
    + box(30, 60, 200, 70, "#fde8ec", "#B23A52", text="94–95 °C", tfill="#B23A52")
    + tx(130, 150, "desnaturalitzar", 12, "#59606a", "middle")
    + box(260, 60, 200, 70, "#e8f1fa", "#1F6AA5", text="50–65 °C", tfill="#1F6AA5")
    + tx(360, 150, "hibridació dels encebadors", 12, "#59606a", "middle")
    + box(490, 60, 210, 70, "#e7f5f2", "#0E7C66", text="72 °C", tfill="#0E7C66")
    + tx(595, 150, "extensió (Taq)", 12, "#59606a", "middle")
    + tx(30, 184, "Cal motlle, dos encebadors, dNTP, Mg²⁺ i polimerasa termostable. Després de n cicles, fins a 2ⁿ còpies.", 13),
)

add(
    "fig-5.6",
    740,
    210,
    tx(370, 24, "CRISPR-Cas9", 15, "#5C4B8A", "middle", "700")
    + '<rect x="80" y="70" width="420" height="16" rx="6" fill="#e8f1fa" stroke="#1F6AA5"/>'
    + tx(290, 64, "DNA diana", 12, "#1F6AA5", "middle")
    + '<path d="M120 86 C 200 140, 300 140, 460 86" fill="none" stroke="#5C4B8A" stroke-width="3"/>'
    + tx(250, 150, "RNA guia", 13, "#5C4B8A", "middle", "700")
    + '<circle cx="520" cy="90" r="26" fill="#efe8fb" stroke="#5C4B8A" stroke-width="2"/>'
    + tx(520, 95, "Cas9", 12, "#5C4B8A", "middle", "700")
    + tx(40, 180, "El Cas9 talla les dues cadenes al costat d’un motiu PAM. NHEJ: errors i gen inactivat. HDR: reparació amb motlle.", 13),
)

add(
    "fig-5.7",
    740,
    160,
    tx(370, 22, "Eines", 15, "#B23A52", "middle", "700")
    + box(20, 50, 160, 40, "#e8f1fa", "#1F6AA5", text="restricció", tfill="#1F6AA5", size=13)
    + box(200, 50, 150, 40, "#e7f5f2", "#0E7C66", text="lligasa", tfill="#0E7C66", size=13)
    + box(370, 50, 150, 40, "#fff8e8", "#A67C12", text="plasmidi", tfill="#A67C12", size=13)
    + box(540, 50, 170, 40, "#fde8ec", "#B23A52", text="PCR / CRISPR", tfill="#B23A52", size=13)
    + tx(20, 120, "DNA recombinant = vector + insert, units per la ligasa. Tot OMG no és transgènic: un knockout propi és OMG i no transgènic.", 12)
    + tx(20, 144, "Clonació molecular (copiar un fragment) no és el mateix que la clonació reproductiva (SCNT).", 13),
)

# ---------- 6 Evolució ----------
add(
    "fig-6.1",
    740,
    200,
    tx(370, 24, "Evidències (no són «proves» aïllades: es reforcen)", 14, "#3E7A32", "middle", "700")
    + "".join(
        box(20 + (i % 4) * 180, 50 + (i // 4) * 60, 165, 44, "#f3faf0", "#3E7A32", text=name, tfill="#3E7A32", size=12)
        for i, name in enumerate(["fòssils", "homòlegs", "anàlegs", "vestigials", "embrió", "biogeografia", "DNA", "observació directa"])
    ),
)

add(
    "fig-6.2",
    720,
    180,
    tx(360, 24, "Selecció natural: tres condicions", 15, "#3E7A32", "middle", "700")
    + box(20, 60, 210, 50, "#f3faf0", "#3E7A32", text="variació", tfill="#3E7A32")
    + box(250, 60, 210, 50, "#e8f1fa", "#1F6AA5", text="heretable", tfill="#1F6AA5")
    + box(480, 60, 220, 50, "#f8e6d4", "#C4651A", text="èxit reproductiu diferent", tfill="#C4651A", size=12)
    + tx(20, 150, "No és «el fort sobreviu». És qui deixa més descendents en aquell ambient. La mutació no apareix «per necessitat».", 13),
)

add(
    "fig-6.3",
    720,
    180,
    tx(360, 24, "Especiació", 15, "#3E7A32", "middle", "700")
    + box(30, 60, 300, 70, "#f3faf0", "#3E7A32", text="al·lopàtrica", tfill="#3E7A32")
    + tx(180, 150, "barrera geogràfica", 12, "#59606a", "middle")
    + box(380, 60, 300, 70, "#e8f1fa", "#1F6AA5", text="simpàtrica", tfill="#1F6AA5")
    + tx(530, 150, "sense separar el territori", 12, "#59606a", "middle"),
)

add(
    "fig-6.4",
    740,
    160,
    tx(370, 22, "Què canvia les freqüències al·lèliques", 14, "#3E7A32", "middle", "700")
    + "".join(
        box(16 + i * 145, 50, 135, 40, "#f3faf0", "#3E7A32", text=n, tfill="#3E7A32", size=12)
        for i, n in enumerate(["selecció", "mutació", "deriva", "flux gènic", "selecció sexual"])
    )
    + tx(16, 120, "L’aparellament no aleatori canvia les freqüències genotípiques, no per si sol les al·lèliques.", 13)
    + tx(16, 144, "Si es compleix Hardy-Weinberg, les freqüències no canvien: no hi ha evolució en aquell locus.", 13),
)

# ---------- 7 Micro ----------
add(
    "fig-7.1",
    740,
    250,
    tx(360, 22, "Bacteri (esquema)", 15, "#A67C12", "middle", "700")
    + '<ellipse cx="360" cy="130" rx="200" ry="80" fill="#fff8e8" stroke="#A67C12" stroke-width="6"/>'
    + '<ellipse cx="360" cy="130" rx="170" ry="60" fill="#fff" stroke="#C4651A" stroke-width="2"/>'
    + '<ellipse cx="330" cy="130" rx="36" ry="18" fill="none" stroke="#1F6AA5" stroke-width="2"/>'
    + tx(330, 126, "nucleoide", 11, "#1F6AA5", "middle")
    + '<circle cx="420" cy="120" r="8" fill="none" stroke="#5C4B8A" stroke-width="2"/>'
    + tx(450, 116, "plasmidi", 11, "#5C4B8A")
    + tx(40, 230, "Paret amb peptidoglicà (bacteris). Els arqueus no en tenen. Càpsula, fímbries i flagel no sempre hi són.", 13),
)

add(
    "fig-7.2",
    740,
    240,
    tx(200, 22, "Virus amb embolcall", 14, "#B23A52", "middle", "700")
    + tx(540, 22, "Bacteriòfag", 14, "#1F6AA5", "middle", "700")
    + '<circle cx="190" cy="120" r="60" fill="#fde8ec" stroke="#B23A52" stroke-width="3"/>'
    + '<circle cx="190" cy="120" r="28" fill="#efe8fb" stroke="#5C4B8A" stroke-width="2"/>'
    + tx(190, 124, "RNA o DNA", 11, "#5C4B8A", "middle")
    + tx(190, 200, "càpsida + embolcall + espines", 12, "#59606a", "middle")
    + '<polygon points="500,70 580,70 560,120 520,120" fill="#e8f1fa" stroke="#1F6AA5" stroke-width="2"/>'
    + '<rect x="534" y="120" width="12" height="50" fill="#1F6AA5"/>'
    + '<line x1="520" y1="170" x2="500" y2="190" stroke="#1F6AA5" stroke-width="2"/>'
    + '<line x1="560" y1="170" x2="580" y2="190" stroke="#1F6AA5" stroke-width="2"/>'
    + tx(540, 214, "cap + cua + fibres", 12, "#59606a", "middle"),
)

add(
    "fig-7.3",
    740,
    230,
    tx(370, 22, "Cicles d’un bacteriòfag", 15, "#A67C12", "middle", "700")
    + box(30, 60, 300, 130, "#fff8e8", "#A67C12")
    + tx(180, 90, "Lític", 16, "#A67C12", "middle", "700")
    + tx(180, 120, "adsorció, entrada,", 13, "#1b1f24", "middle")
    + tx(180, 140, "replicació, acoblament,", 13, "#1b1f24", "middle")
    + tx(180, 160, "lisi", 13, "#1b1f24", "middle")
    + box(380, 60, 330, 130, "#e8f1fa", "#1F6AA5")
    + tx(545, 90, "Lisogènic", 16, "#1F6AA5", "middle", "700")
    + tx(545, 120, "el DNA víric s’integra", 13, "#1b1f24", "middle")
    + tx(545, 140, "(pròfag) i es copia amb", 13, "#1b1f24", "middle")
    + tx(545, 160, "l’hoste fins a la inducció", 13, "#1b1f24", "middle"),
)

add(
    "fig-7.4",
    760,
    250,
    tx(380, 22, "Cicle del nitrogen (paper dels bacteris)", 15, "#3E7A32", "middle", "700")
    + box(20, 50, 170, 40, "#e8f1fa", "#1F6AA5", text="N₂ atmosfèric", tfill="#1F6AA5", size=13)
    + box(220, 50, 200, 40, "#e7f5f2", "#0E7C66", text="NH₄⁺ fixació", tfill="#0E7C66", size=13)
    + box(450, 50, 280, 40, "#f3faf0", "#3E7A32", text="NO₂⁻ → NO₃⁻ nitrificació", tfill="#3E7A32", size=13)
    + box(220, 140, 250, 40, "#f8e6d4", "#C4651A", text="desnitrificació → N₂", tfill="#C4651A", size=13)
    + arr(190, 70, 220, 70, "#0E7C66")
    + arr(420, 70, 450, 70, "#3E7A32")
    + arr(500, 90, 400, 140, "#C4651A")
    + tx(20, 210, "Fixació: Rhizobium, Azotobacter (nitrogenasa). Nitrificació: Nitrosomonas i Nitrobacter.", 13)
    + tx(20, 234, "Desnitrificació torna N₂. L’amonificació la fan descomponedors a partir de la matèria orgànica.", 13),
)

add(
    "fig-7.5",
    740,
    150,
    tx(370, 22, "Formes acel·lulars", 15, "#A67C12", "middle", "700")
    + box(20, 50, 200, 50, "#fde8ec", "#B23A52", text="virus: àcid nucleic + càpsida", tfill="#B23A52", size=12)
    + box(250, 50, 220, 50, "#efe8fb", "#5C4B8A", text="viroide: RNA, sense càpsida", tfill="#5C4B8A", size=12)
    + box(500, 50, 220, 50, "#fff8e8", "#A67C12", text="prió: proteïna, sense àcid nucleic", tfill="#A67C12", size=11)
    + tx(20, 130, "Cap dels tres és una cèl·lula. El virus només es replica dins un hoste.", 13),
)

# ---------- 8 Immuno ----------
add(
    "fig-8.1",
    740,
    260,
    tx(370, 22, "Resposta primària i secundària", 15, "#8E3A55", "middle", "700")
    + '<line x1="60" y1="200" x2="700" y2="200" stroke="#1b1f24" stroke-width="1.5"/>'
    + '<line x1="60" y1="200" x2="60" y2="40" stroke="#1b1f24" stroke-width="1.5"/>'
    + '<path d="M80 200 C 120 200, 140 150, 180 140 C 220 130, 240 190, 280 198" fill="none" stroke="#1F6AA5" stroke-width="3"/>'
    + '<path d="M300 198 C 340 120, 380 60, 460 55 C 540 50, 600 90, 660 170" fill="none" stroke="#B23A52" stroke-width="3"/>'
    + tx(150, 230, "1r contacte", 12, "#1F6AA5", "middle")
    + tx(430, 230, "2n contacte", 12, "#B23A52", "middle")
    + tx(70, 36, "anticòs", 12, "#59606a")
    + tx(40, 252, "La secundària és més ràpida, més alta i sobretot IgG, gràcies als limfòcits de memòria.", 13),
)

add(
    "fig-8.2",
    640,
    280,
    tx(320, 22, "Anticòs (IgG)", 15, "#8E3A55", "middle", "700")
    + '<path d="M320 200 L240 80 L200 40" fill="none" stroke="#8E3A55" stroke-width="10" stroke-linecap="round"/>'
    + '<path d="M320 200 L400 80 L440 40" fill="none" stroke="#8E3A55" stroke-width="10" stroke-linecap="round"/>'
    + '<path d="M250 90 L220 70" fill="none" stroke="#1F6AA5" stroke-width="6" stroke-linecap="round"/>'
    + '<path d="M390 90 L420 70" fill="none" stroke="#1F6AA5" stroke-width="6" stroke-linecap="round"/>'
    + tx(180, 30, "variable (antigen)", 12, "#1F6AA5", "middle")
    + tx(460, 30, "variable", 12, "#1F6AA5", "middle")
    + tx(320, 230, "constant · 2 cadenes pesants + 2 de lleugeres · ponts disulfur", 13, "#59606a", "middle")
    + tx(40, 262, "IgM: pentàmer, resposta primària. IgG: monòmer, secundària, travessa la placenta. IgA: secrecions. IgE: al·lèrgia.", 12),
)

add(
    "fig-8.3",
    740,
    200,
    tx(370, 22, "Dues branques de la immunitat específica", 14, "#8E3A55", "middle", "700")
    + box(30, 50, 320, 90, "#fde8ec", "#B23A52")
    + tx(190, 84, "Humoral", 16, "#B23A52", "middle", "700")
    + tx(190, 110, "limfòcits B → cèl·lules plasmàtiques → anticossos", 12, "#1b1f24", "middle")
    + box(380, 50, 330, 90, "#e8f1fa", "#1F6AA5")
    + tx(545, 84, "Cel·lular", 16, "#1F6AA5", "middle", "700")
    + tx(545, 110, "T col·laboradors (CD4) i T citotòxics (CD8)", 12, "#1b1f24", "middle")
    + tx(30, 170, "Els T col·laboradors reconeixen l’antigen presentat amb MHC II. Els citotòxics, amb MHC I.", 13),
)

add(
    "fig-8.4",
    740,
    170,
    tx(370, 22, "Mapa de la immunitat", 15, "#8E3A55", "middle", "700")
    + box(20, 50, 160, 40, "#fff8e8", "#A67C12", text="barreres", tfill="#A67C12", size=13)
    + box(200, 50, 150, 40, "#f8e6d4", "#C4651A", text="innata", tfill="#C4651A", size=13)
    + box(370, 50, 160, 40, "#fde8ec", "#B23A52", text="específica", tfill="#B23A52", size=13)
    + box(550, 50, 170, 40, "#e7f5f2", "#0E7C66", text="memòria", tfill="#0E7C66", size=13)
    + tx(20, 120, "Artificial activa: vacuna. Artificial passiva: seroteràpia. Natural passiva: IgG de la mare i IgA de la llet.", 13)
    + tx(20, 146, "El VIH infecta limfòcits T CD4. La sida és la immunodeficiència que en resulta, no el nom del virus.", 13),
)

add(
    "fig-9.1",
    740,
    180,
    tx(370, 22, "Un disseny que la PAU dona per vàlid", 15, "#5f6670", "middle", "700")
    + "".join(
        box(16 + i * 145, 50, 135, 44, "#f6f5f2", "#5f6670", text=n, tfill="#1b1f24", size=12)
        for i, n in enumerate(["hipòtesi", "VI", "VD", "control", "rèpliques"])
    )
    + tx(16, 130, "La variable independent és la que es canvia. La dependent, la que es mesura.", 13)
    + tx(16, 154, "El control rep el mateix tractament sense la variable que es vol provar. Una sola observació no basta.", 13),
)

from chemfigs import molecules

FIGS.update(molecules())

# Làmines amb llicència oberta (traduïdes al català quan el text és editable).
_ART = Path(__file__).resolve().parent / "art"
if _ART.is_dir():
    for _p in _ART.glob("*.svg"):
        FIGS[_p.stem] = _p.read_text(encoding="utf-8", errors="replace")
    if "fig-2.3a" in FIGS:
        FIGS["fig-2.3"] = FIGS.pop("fig-2.3a")

COVERS = {
    "biomolecules": cover("1", "Biomolècules", "#0E7C66", '<circle cx="980" cy="520" r="70" fill="#fff" opacity=".9"/><text x="980" y="530" text-anchor="middle" font-size="28" fill="#0E7C66" font-weight="700">H₂O</text>'),
    "cellula": cover("2", "La cèl·lula", "#1F6AA5", '<ellipse cx="980" cy="520" rx="120" ry="80" fill="none" stroke="#fff" stroke-width="8"/><circle cx="980" cy="520" r="28" fill="#fff"/>'),
    "metabolisme": cover("3", "Metabolisme", "#C4651A", '<text x="980" y="540" text-anchor="middle" font-size="42" fill="#fff" font-weight="700">ATP</text>'),
    "mendel": cover("4", "Mendel", "#5C4B8A", '<rect x="900" y="460" width="50" height="50" fill="#fff"/><circle cx="1020" cy="485" r="26" fill="none" stroke="#fff" stroke-width="6"/>'),
    "molecular": cover("5", "Molecular", "#B23A52", '<text x="900" y="540" font-size="36" fill="#fff" font-weight="700">DNA → proteïna</text>'),
    "evolucio": cover("6", "Evolució", "#3E7A32", '<text x="980" y="540" text-anchor="middle" font-size="40" fill="#fff" font-weight="700">p²+2pq+q²</text>'),
    "microbiologia": cover("7", "Microbis", "#A67C12", '<ellipse cx="980" cy="520" rx="90" ry="50" fill="none" stroke="#fff" stroke-width="8"/>'),
    "immunologia": cover("8", "Immunitat", "#8E3A55", '<path d="M900 560 L960 460 L1040 560" fill="none" stroke="#fff" stroke-width="10"/>'),
    "disseny": cover("9", "Disseny", "#5f6670", '<text x="980" y="540" text-anchor="middle" font-size="36" fill="#fff" font-weight="700">VI → VD</text>'),
}
