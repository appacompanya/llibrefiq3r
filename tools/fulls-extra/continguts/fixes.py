"""Correccions de text als PDF de 2n i 4t (revisió científica, ortogràfica i de maquetació, octubre 2026)."""

FIXES_2N = [
    {"id": "2n-s1f6-punt", "file": "sda1-11-fitxa-6-l-aigua-de-l-institut.pdf", "type": "line",
     "old": "un institut com el nostre. valors", "new": "un institut com el nostre; valors"},
    # etiquetes de sota els dos requadres de dibuix, que se sobreposaven i sortien del marge
    {"id": "2n-s3repte-etiquetes", "file": "sda3-02-full-del-repte.pdf", "type": "redact", "rect": [30, 475.5, 400, 500.5]},
    {"id": "2n-s3repte-et1", "file": "sda3-02-full-del-repte.pdf", "type": "text", "x": 124.8, "y": 487.0, "align": "center",
     "font": "bold", "size": 10.5, "text": "Pilota calenta"},
    {"id": "2n-s3repte-et2", "file": "sda3-02-full-del-repte.pdf", "type": "text", "x": 124.8, "y": 498.5, "align": "center",
     "size": 9.5, "text": "(pavelló, 20 °C)"},
    {"id": "2n-s3repte-et3", "file": "sda3-02-full-del-repte.pdf", "type": "text", "x": 294.9, "y": 487.0, "align": "center",
     "font": "bold", "size": 10.5, "text": "Pilota freda"},
    {"id": "2n-s3repte-et4", "file": "sda3-02-full-del-repte.pdf", "type": "text", "x": 294.9, "y": 498.5, "align": "center",
     "size": 9.5, "text": "(pati, 2 °C)"},
    {"id": "2n-s4f5-aigua", "file": "sda4-10-fitxa-5-separacio.pdf", "type": "line", "old": "aigu", "new": "aigua"},
]

FIXES_4T = [
    {"id": "4t-s1f2-apostrof", "file": "sda1-04-fitxa-2-ions-i-isotops.pdf", "type": "line", "old": "n\\'ha", "new": "n'ha"},
    {"id": "4t-s2f3-mols1", "file": "sda2-06-fitxa-3-la-mol.pdf", "type": "line", "old": "Quantes mols d'aigua", "new": "Quants mols d'aigua"},
    {"id": "4t-s2f3-mols2", "file": "sda2-06-fitxa-3-la-mol.pdf", "type": "line", "old": "Quantes mols de NaCl", "new": "Quants mols de NaCl"},
    {"id": "4t-s2f3-mols3", "file": "sda2-06-fitxa-3-la-mol.pdf", "type": "line", "old": "Quantes mols d'ions", "new": "Quants mols d'ions"},
    # la solubilitat del NaCl és per litre d'aigua, no de dissolució; per calcular la molaritat cal la densitat
    {"id": "4t-s2amp-solubilitat-a", "file": "sda2-21-ampliacio.pdf", "type": "redact", "rect": [122.6, 459.5, 548, 482.5], "graphics": True},
    {"id": "4t-s2amp-solubilitat-b", "file": "sda2-21-ampliacio.pdf", "type": "redact", "rect": [64, 482.5, 548, 504.5], "graphics": True},
    {"id": "4t-s2amp-solubilitat-c", "file": "sda2-21-ampliacio.pdf", "type": "text", "x": 121.8, "y": 474.0,
     "text": " A 20 °C, 1 L d'aigua dissol uns 360 g de NaCl, i la dissolució saturada té una"},
    {"id": "4t-s2amp-solubilitat-d", "file": "sda2-21-ampliacio.pdf", "type": "text", "x": 65.2, "y": 495.0,
     "text": "densitat d'1,20 g/mL. Quina és la seva molaritat? Per què no podem fer un sèrum de 400 g/L?"},
    {"id": "4t-s3f1-calen", "file": "sda3-03-fitxa-1-equacio-en-mols.pdf", "type": "line", "old": " cal per fabricar", "new": " calen per fabricar"},
    {"id": "4t-s3f8-venen", "file": "sda3-13-fitxa-8-calculadora.pdf", "type": "line", "old": "vénen", "new": "venen"},
    {"id": "4t-s5lab3-apostrof1", "file": "sda5-11-laboratori-3-fregament.pdf", "type": "line", "old": "l\\'anem", "new": "l'anem"},
    {"id": "4t-s5lab3-apostrof2", "file": "sda5-11-laboratori-3-fregament.pdf", "type": "line", "old": "l\\'iguala", "new": "l'iguala"},
    {"id": "4t-s5lab3-apostrof3", "file": "sda5-11-laboratori-3-fregament.pdf", "type": "line", "old": "l\\'extrem s\\'ha", "new": "l'extrem s'ha"},
    {"id": "4t-s5f7-apostrof", "file": "sda5-13-fitxa-7-hooke-i-el-gel.pdf", "type": "line", "old": "s\\'allarga", "new": "s'allarga"},
]
