"""Classificació temàtica dels exercicis de la PAU de Química per paraules clau."""
import re

BLOCS = [
    ("estructura", "Estructura atòmica i taula periòdica"),
    ("enllac", "Enllaç químic i forces intermoleculars"),
    ("termo", "Termoquímica i espontaneïtat"),
    ("cinetica", "Cinètica química"),
    ("equilibri", "Equilibri químic"),
    ("solubilitat", "Equilibris de solubilitat"),
    ("acidbase", "Reaccions àcid-base"),
    ("redox", "Reaccions redox i electroquímica"),
    ("organica", "Química orgànica"),
]
NOMS = dict(BLOCS)

KW = {
    "estructura": [r"configuraci[óo] electr[òo]nica", r"nombres? qu[àa]ntics?", r"orbitals?\b", r"energia d.ionitzaci[óo]",
                   r"radi (at[òo]mic|i[òo]nic)", r"afinitat electr[òo]nica", r"espectre", r"longitud d.ona", r"\bfot[óo]", r"Planck",
                   r"model at[òo]mic", r"\bBohr\b", r"taula peri[òo]dica", r"electronegativitat", r"freq[üu][èe]ncia", r"is[òo]top",
                   r"espectrometria de masses", r"\bnivells? d.energia"],
    "enllac": [r"enlla[çc] (i[òo]nic|covalent|met[àa]l·?l?ic)", r"estructura de Lewis", r"diagrama de Lewis", r"RPECV", r"geometria molecular",
               r"geometria", r"polaritat", r"molècula (polar|apolar)", r"forces? intermolecular", r"for[çc]es? de (London|Van der Waals)",
               r"enlla[çc]os? d.hidrogen", r"pont d.hidrogen", r"punt d.(ebullici[óo]|fusi[óo])", r"energia (reticular|de xarxa)",
               r"Born.Haber", r"hibridaci[óo]", r"s[òo]lid (i[òo]nic|covalent|molecular|met[àa]l)", r"conductivitat el[èe]ctrica", r"dipol"],
    "termo": [r"entalpia", r"\bHess\b", r"entropia", r"energia (lliure|de Gibbs)", r"\bGibbs\b", r"espontàni", r"espontani", r"calorímetr",
              r"exot[èe]rmic", r"endot[èe]rmic", r"calor de (combusti|reacci|formaci)", r"\bΔH", r"\bΔS", r"\bΔG", r"energies d.enlla[çc]",
              r"capacitat calor[íi]fica", r"poder calor[íi]fic"],
    "cinetica": [r"velocitat de (la )?reacci[óo]", r"ordre de reacci[óo]", r"ordre (parcial|total)", r"constant de velocitat", r"energia d.activaci[óo]",
                 r"catalitzador", r"mecanisme de reacci", r"\bArrhenius", r"equaci[óo] de velocitat", r"llei de velocitat", r"model (cin[èe]tic )?de col·lisions",
                 r"teoria de col·lisions", r"estat de transici[óo]", r"complex activat", r"velocitat inicial", r"cin[èe]tica"],
    "equilibri": [r"\bK_?c\b", r"\bK_?p\b", r"constant d.equilibri", r"Le Ch[âa]telier", r"quocient de reacci[óo]", r"grau de dissociaci[óo]",
                  r"en (l.)?equilibri", r"desplaça (l.)?equilibri", r"rendiment de la reacci[óo]", r"\bpressi[óo] parcial"],
    "solubilitat": [r"\bK_?ps\b", r"producte de solubilitat", r"\bsolubilitat", r"precipit", r"efecte de l.i[óo] com[úu]", r"\bi[óo] com[úu]",
                    r"poc solubles?", r"insoluble"],
    "acidbase": [r"\bpH\b", r"\bpOH\b", r"\bK_?a\b", r"\bK_?b\b", r"constant d.(acidesa|basicitat)", r"[àa]cid (feble|fort)", r"base (feble|forta)",
                 r"valoraci[óo]", r"indicador", r"(soluci[óo]|dissoluci[óo]) (amortidora|reguladora|tamp[óo])", r"\btamp[óo]\b", r"hidr[òo]lisi",
                 r"punt d.equival[èe]ncia", r"neutralitzaci[óo]", r"Br[øo]nsted", r"\b[àa]cid conjugat", r"base conjugada", r"\bhidr[òo]xid de"],
    "redox": [r"oxidaci[óo]", r"reducci[óo]", r"\boxidant", r"\breductor", r"potencial (est[àa]ndard )?de reducci[óo]", r"\bE\s*[°º]", r"\bpila\b",
              r"electr[òo]lisi", r"\bFaraday", r"[àa]node", r"c[àa]tode", r"semireacci", r"pont salí", r"cel·la (galv[àa]nica|electrol[íi]tica)",
              r"corrosi[óo]", r"nombre d.oxidaci[óo]", r"estat d.oxidaci[óo]", r"bateria", r"electrode", r"redox", r"m[èe]tode de l.i[óo].electr[óo]"],
    "organica": [r"is[òo]mer", r"IUPAC", r"grup funcional", r"\bals?coh?ol\b", r"[èe]ster", r"[àa]cid carbox[íi]lic", r"\bamin[ae]\b", r"\bamida",
                 r"alqu[èe]", r"alc[àa]", r"alqu[íi]", r"hidrocarbur", r"pol[íi]mer", r"mon[òo]mer", r"polimeritzaci[óo]", r"reacci[óo] d.(addici[óo]|substituci[óo]|eliminaci[óo]|condensaci[óo])",
                 r"esterificaci[óo]", r"quiral", r"carboni asim[èe]tric", r"estereoisom", r"[òo]ptica", r"benz[èe]", r"arom[àa]tic", r"\bcetona", r"aldehid",
                 r"espectre (d.)?(IR|infraroig|RMN)", r"infraroig", r"\bRMN\b", r"formuleu", r"anomeneu"],
}
KWC = {k: [re.compile(p, re.I) for p in v] for k, v in KW.items()}


def scores(text):
    t = re.sub(r"\s+", " ", text)
    return {k: sum(len(p.findall(t)) for p in ps) for k, ps in KWC.items()}


def classify(text):
    s = scores(text)
    # «reducció» i «oxidació» apareixen en contextos orgànics i d'àcid-base; pesen menys si hi ha poc més de redox
    best = max(s, key=lambda k: s[k])
    if s[best] == 0:
        return "equilibri", []
    extra = [k for k, v in sorted(s.items(), key=lambda kv: -kv[1]) if k != best and v >= max(2, 0.45 * s[best])]
    return best, extra[:2]
