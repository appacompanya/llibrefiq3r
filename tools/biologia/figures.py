"""Registre de figures del llibre de Biologia: clau → dibuix (SVG propi) o imatge de Commons + peu."""
from pathlib import Path
import figs1, figs2, figs3, figs4, figs5, figs6

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "biologia" / "img"

# Peus. Les figures pròpies són esquemes fets per a aquest llibre (domini públic, CC0).
FIG = {
    # tema 1
    "aigua": (figs1.fig_aigua, "La molècula d’aigua és angular (104,5°) i polar. Cada molècula pot fer fins a quatre ponts d’hidrogen (línia discontínua) amb les veïnes: dos pels hidrògens (δ+) i dos pels parells d’electrons de l’oxigen (δ−)."),
    "anomers": (figs1.fig_anomers, "Anòmers α i β de la D-glucopiranosa en projecció de Haworth. Només canvia la posició de l’OH del carboni anomèric (C1): avall en l’α i amunt en la β. Els hidrògens no s’han dibuixat."),
    "disacarids": (figs1.fig_disacarids, "Tres disacàrids. La maltosa i la lactosa conserven un carboni anomèric lliure i són reductores; a la sacarosa l’enllaç uneix els dos carbonis anomèrics (C1 de la glucosa i C2 de la fructosa) i no ho és."),
    "lipids": (figs1.fig_lipids, "Triacilglicerol (tres àcids grassos esterificats amb glicerol: apolar, de reserva) i fosfolípid (dos àcids grassos i un grup fosfat amb un grup polar: amfipàtic, forma bicapes)."),
    "aminoacid": (figs1.fig_aminoacid, "Un aminoàcid a pH fisiològic és un zwitterió (–NH₃⁺ i –COO⁻). L’enllaç peptídic es forma per condensació entre el carboxil d’un aminoàcid i l’amino del següent."),
    "proteina": (figs1.fig_proteina, "Els quatre nivells d’estructura d’una proteïna. La desnaturalització destrueix la secundària, la terciària i la quaternària; la primària (la seqüència) es conserva."),
    "nucleotid": (figs1.fig_nucleotid, "Un nucleòtid (fosfat + pentosa + base) i un tram de DNA desplegat: les dues cadenes són antiparal·leles i les bases s’aparellen per complementarietat, A–T amb dos ponts d’hidrogen i G–C amb tres."),
    "dna_quimica": ("commons:dna_quimica", "Estructura química d’un fragment de DNA de doble cadena: esquelet de fosfat i desoxiribosa, i parelles de bases unides per ponts d’hidrogen (línies de punts)."),
    "vs": (lambda: figs1.fig_vs("tres"), "Velocitat inicial d’un enzim en funció de la concentració de substrat. Un inhibidor competitiu manté la V<sub>max</sub> i augmenta la K<sub>m</sub> aparent; un de no competitiu fa baixar la V<sub>max</sub>."),
    "vs_aut": (lambda: figs1.fig_vs("aut"), "Gràfic de l’exercici: velocitat de la reacció en funció de la concentració de substrat, sense fàrmac i amb fàrmac."),
    "map1": (figs4.map1, "Mapa del tema 1."),
    # tema 2
    "pro_euc": (figs5.fig_pro_euc, "Cèl·lula procariota i cèl·lula eucariota (no a escala: la eucariota sol ser unes deu vegades més gran)."),
    "membrana": ("commons:membrana", "Model del mosaic fluid de la membrana plasmàtica."),
    "bomba": (figs5.fig_bomba, "Bomba de sodi i potassi (Na⁺/K⁺-ATPasa): per cada ATP hidrolitzat treu 3 Na⁺ i entra 2 K⁺, tots dos en contra del seu gradient."),
    "osmosi": (figs5.fig_osmosi, "Osmosi en una cèl·lula animal (eritròcit) i en una cèl·lula vegetal segons la concentració de soluts del medi."),
    "nucli": (figs5.fig_nucli, "El nucli: embolcall nuclear doble amb porus, continu amb el reticle endoplasmàtic rugós; a dins, la cromatina i el nuclèol."),
    "mitocondri": (figs5.fig_mitocondri, "Estructura del mitocondri: membrana externa, espai intermembranós, membrana interna plegada en crestes i matriu amb DNA circular i ribosomes 70S."),
    "cloroplast": (figs5.fig_cloroplast, "Estructura del cloroplast: doble membrana, estroma (amb DNA circular i ribosomes 70S) i tilacoides apilats en grana."),
    "animal": (figs5.fig_animal, "Cèl·lula animal: no té paret ni cloroplasts, té centríols i lisosomes."),
    "vegetal": (figs5.fig_vegetal, "Cèl·lula vegetal: paret de cel·lulosa, vacúol gran, cloroplasts i plasmodesmes; no té centríols."),
    "cicle": (figs2.fig_cicle, "El cicle cel·lular. La interfase (G1, S i G2) ocupa la major part del cicle; la fase M és la mitosi més la citocinesi."),
    "mitosi": (figs5.fig_mitosi, "Fases de la mitosi en una cèl·lula 2n = 4: un parell de cromosomes llargs i un de curts (d’origen matern en vermell i patern en blau). A l’anafase se separen les cromàtides germanes i en surten dues cèl·lules 2n idèntiques."),
    "meiosi": (figs5.fig_meiosi, "Fases de la meiosi en una cèl·lula 2n = 4. A la profase I els homòlegs s’aparellen i fan entrecreuaments (puntes de l’altre color). A l’anafase I se separen els homòlegs (amb dues cromàtides); a l’anafase II, les cromàtides germanes. En surten quatre cèl·lules n diferents."),
    "map2": (figs4.map2, "Mapa del tema 2."),
    # tema 3
    "atp": (figs3.fig_atp, "L’ATP és un nucleòtid: adenina, ribosa i tres fosfats. La cèl·lula aprofita l’energia de la hidròlisi dels enllaços entre fosfats."),
    "cat_anab": (figs6.fig_cat_anab, "El catabolisme i l’anabolisme queden lligats per l’ATP i pels coenzims reduïts."),
    "glucolisi": (figs6.fig_glucolisi, "Balanç de la glucòlisi: es gasten 2 ATP, se’n formen 4 i es redueixen 2 NAD⁺. Net per glucosa: 2 ATP, 2 NADH i 2 piruvats, al citosol."),
    "respiracio": (figs3.fig_respiracio, "Visió de conjunt de la respiració cel·lular aeròbica en una cèl·lula eucariota."),
    "krebs": (figs6.fig_krebs, "El cicle de Krebs, a la matriu mitocondrial. Cada acetil-CoA que entra s’uneix a l’oxalacetat; en una volta surten 2 CO₂, 3 NADH, 1 FADH₂ i 1 GTP, i es regenera l’oxalacetat."),
    "cadena": (figs6.fig_cadena, "Cadena respiratòria i fosforilació oxidativa. Els complexos I, III i IV bombegen protons cap a l’espai intermembranós; el retorn dels protons per l’ATP-sintasa fa l’ATP."),
    "fermentacions": (figs6.fig_fermentacions, "Les fermentacions reoxiden el NADH de la glucòlisi sense cadena respiratòria. El rendiment és el de la glucòlisi: 2 ATP per glucosa."),
    "fase_lluminosa": (figs6.fig_fase_lluminosa, "Fase lluminosa a la membrana del tilacoide (flux acíclic d’electrons). Els protons s’acumulen al lumen i tornen a l’estroma per l’ATP-sintasa."),
    "zeta": (figs3.fig_zeta, "Esquema en Z: energia dels electrons al llarg de la fase lluminosa. Cada fotosistema absorbeix llum i aixeca els electrons."),
    "calvin": (figs3.fig_calvin, "Cicle de Calvin, a l’estroma del cloroplast (valors per a 3 CO₂ fixats)."),
    "map3": (figs4.map3, "Mapa del tema 3."),
    # tema 4
    "punnett_mono": (figs4.fig_punnett_mono, "Quadre de Punnett de l’encreuament Aa × Aa."),
    "punnett_di": (figs4.fig_punnett_di, "Dihibridisme amb gens independents: AaBb × AaBb dona 9 : 3 : 3 : 1 en els fenotips."),
    "lligament": (figs4.fig_lligament, "Gens lligats: si no hi ha entrecreuament entre els dos loci, els gàmetes són parentals; l’entrecreuament produeix gàmetes recombinants."),
    "punnett_x": (figs4.fig_punnett_x, "Herència recessiva lligada al cromosoma X: mare portadora i pare sa."),
    "pedigri": (figs4.fig_pedigri, "Pedigrí compatible amb una herència autosòmica recessiva."),
    "map4": (figs4.map4, "Mapa del tema 4."),
    # tema 5
    "dogma": (figs4.fig_dogma, "Flux de la informació genètica."),
    "trna": (figs4.fig_trna, "Esquema de l’RNA de transferència en forma de trèvol."),
    "transcripcio": (figs4.fig_transcripcio, "La cadena motlle es llegeix 3′→5′; l’RNA missatger és complementari del motlle i té la mateixa seqüència que la cadena codificant, amb U en lloc de T."),
    "forquilla": (figs4.fig_forquilla, "Forquilla de replicació. La cadena líder es fa de manera contínua cap a la forquilla; la retardada, en fragments d’Okazaki que comencen amb un encebador d’RNA."),
    "traduccio": (figs4.fig_traduccio, "Traducció al ribosoma: l’anticodó de cada RNAt s’aparella amb el codó de l’RNAm, que es llegeix 5′→3′."),
    "operon": (figs4.fig_operon, "L’operó lac de E. coli, un operó inducible."),
    "recombinant": (figs4.fig_recombinant, "Passos per obtenir DNA recombinant i clonar un gen en un bacteri."),
    "pcr": (figs4.fig_pcr, "Les tres etapes d’un cicle de PCR."),
    "crispr": (figs4.fig_crispr, "CRISPR-Cas9: l’RNA guia porta la nucleasa Cas9 a la seqüència diana, al costat d’un PAM. La reparació del tall decideix el resultat."),
    "map5": (figs4.map5, "Mapa del tema 5."),
    # tema 6
    "homologia": (figs5.fig_homologia, "Òrgans homòlegs: l’extremitat anterior de l’ésser humà, el ratpenat, la balena i l’ocell té el mateix pla ossi (húmer, radi i cúbit, carp, metacarp i falanges, cada os amb el mateix color) encara que la funció sigui diferent."),
    "seleccio": (figs4.fig_seleccio, "Les tres condicions de la selecció natural han de donar-se alhora."),
    "forces": (figs4.fig_forces, "Factors que canvien les freqüències al·lèliques d’una població."),
    "especiacio": (figs4.fig_especiacio, "Especiació al·lopàtrica i simpàtrica."),
    "map6": (figs4.map6, "Mapa del tema 6."),
    # tema 7
    "bacteri": (figs5.fig_bacteri, "Estructura d’una cèl·lula bacteriana: càpsula, paret, membrana plasmàtica, nucleoide amb el cromosoma circular, plasmidis, ribosomes 70S, inclusions, fímbries, pilus sexual i flagel. No té nucli ni orgànuls amb membrana."),
    "gram": (figs4.fig_gram, "Paret dels bacteris gram positius i gram negatius."),
    "nitrogen": (figs4.fig_nitrogen, "Cicle del nitrogen: els passos que fan els microorganismes."),
    "fag": (figs5.fig_fag, "Bacteriòfag de tipus T4: càpsida (cap) amb DNA, coll, cua, placa basal i fibres de la cua."),
    "cicles_virus": (figs5.fig_cicles_virus, "Cicle lític i cicle lisogènic d’un bacteriòfag."),
    "acel": (figs4.fig_acel, "Tres agents infecciosos acel·lulars."),
    "map7": (figs4.map7, "Mapa del tema 7."),
    # tema 8
    "humoral_cel": (figs4.fig_humoral_cel, "Resposta immunitària específica humoral i cel·lular."),
    "anticos": (figs4.fig_anticos, "Estructura d’un anticòs IgG."),
    "resposta": (figs5.fig_resposta, "Concentració d’anticossos després del primer i del segon contacte amb el mateix antigen."),
    "tipus_immunitat": (figs4.fig_tipus_immunitat, "Tipus d’immunitat adquirida."),
    "map8": (figs4.map8, "Mapa del tema 8."),
    # tema 9
    "disseny": (figs4.fig_disseny, "Les peces d’un disseny experimental."),
    "map9": (figs4.map9, "Mapa del tema 9."),
}

# Figures de Commons: clau → (fitxer processat a biologia/img/, autoria i llicència) i alternativa pròpia
import json
COMMONS = json.load(open(IMG / "commons.json", encoding="utf-8")) if (IMG / "commons.json").exists() else {}
FALLBACK = {"membrana": figs2.fig_mosaic, "nucli": figs2.fig_nucli, "mitocondri": figs2.fig_mitocondri, "cloroplast": figs2.fig_cloroplast,
            "animal": figs2.fig_animal, "vegetal": figs2.fig_vegetal, "bacteri": figs2.fig_pro_euc, "dna_quimica": None, "homologia": None, "fag": None}


def render(key):
    """Retorna (html_de_la_imatge, peu, crèdit) o None si s'ha de suprimir."""
    fn, cap = FIG[key]
    credit = ""
    if isinstance(fn, str) and fn.startswith("commons:"):
        k = fn.split(":")[1]
        if k in COMMONS:
            c = COMMONS[k]
            img = f'<img src="{{IMG}}/{c["file"]}" alt="{cap}" loading="lazy" decoding="async" width="{c["w"]}" height="{c["h"]}">'
            return img, cap, c["credit"]
        fb = FALLBACK.get(k)
        if fb is None:
            return None
        return fb(), cap, credit
    return fn(), cap, credit
