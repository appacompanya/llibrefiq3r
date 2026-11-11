"""Revisió didàctica (novembre 2026): cada secció explica els conceptes previs abans de fer-los servir.

Mateix format que revisio.py: ("set", camí, html), ("ins", camí, element) (abans), ("after", camí, element),
("sub", camí, vell, nou), ("del", camí).
"""


def P(h):
    return {"t": "p", "html": h}


def H(h):
    return {"t": "h4", "html": h}


def LI(*items):
    return [{"t": "li", "html": x} for x in items]


def BOX(title, *children, color="#0c6957"):
    ch = [c if isinstance(c, dict) else P(c) for c in children]
    return {"t": "box", "title": title, "tcolor": color, "children": ch}


def UL(*items):
    return {"t": "ul", "items": list(items)}


D = []

# =====================================================================================
# TEMA 4 · GENÈTICA MENDELIANA
# =====================================================================================
D += [
    # ---- 4.1: de l'herència als cromosomes homòlegs, gens i al·lels, i després les lleis
    ("ins", "499", H("Què estudia la genètica")),
    ("ins", "499", P(
        "Els fills s’assemblen als pares, però no en són còpies: dos germans poden tenir els ulls de colors diferents, "
        "i un caràcter que no tenia cap dels pares pot reaparèixer en un net. La <b>genètica</b> estudia com es transmeten "
        "els <b>caràcters hereditaris</b> (el color de la llavor d’un pèsol, el grup sanguini, una malaltia hereditària) "
        "d’una generació a la següent, i per què apareixen les diferències. Cada caràcter pot presentar-se de maneres diferents, "
        "que s’anomenen <b>variants</b> o formes del caràcter: la llavor del pèsol pot ser groga o verda; el grup sanguini, A, B, AB o O.")),
    ("ins", "499", P(
        "Gregor Mendel (1822–1884) va estudiar-ho creuant plantes de pèsol (<i>Pisum sativum</i>) i comptant la descendència. "
        "Va triar caràcters amb dues formes ben diferents i va partir de <b>línies pures</b>: plantes que, autofecundades durant generacions, "
        "sempre donen descendents iguals a elles. D’aquests recomptes va deduir que l’herència no és una barreja de líquids, sinó que es fa "
        "per unitats discretes, que avui anomenem gens. Mendel no sabia res dels cromosomes ni del DNA; aquí partim del que sabem ara, "
        "i després veurem que les seves lleis se n’expliquen per la meiosi.")),
    ("ins", "499", H("Cromosomes homòlegs: dues còpies de cada informació")),
    ("ins", "499", P(
        "La informació hereditària és al DNA, empaquetat en <b>cromosomes</b> (tema 2). Les cèl·lules del cos humà són <b>diploides</b> (2n = 46): "
        "tenen els cromosomes per parelles. De cada parella, un cromosoma ve de l’òvul de la mare i l’altre de l’espermatozoide del pare. "
        "Els dos cromosomes d’una parella s’anomenen <b>cromosomes homòlegs</b>: tenen la mateixa mida i forma i porten <b>els mateixos gens "
        "en el mateix ordre</b>, però no necessàriament les mateixes versions d’aquests gens. Els gàmetes (òvuls i espermatozoides) són "
        "<b>haploides</b> (n = 23): porten un sol cromosoma de cada parella, i la fecundació torna a formar les parelles.")),
    ("ins", "499", P(
        "En els humans hi ha 22 parelles d’<b>autosomes</b>, iguals en homes i dones, i una parella de <b>cromosomes sexuals</b>: XX en les dones i XY "
        "en els homes. De moment pensarem en gens dels autosomes; els dels cromosomes sexuals tenen un comportament especial (apartat 4.4).")),
    ("ins", "499", H("Gen, locus i al·lel")),
    ("set", "499",
        "Un <b>gen</b> és un fragment de DNA que conté la informació per fabricar un producte, generalment una proteïna (de vegades un RNA funcional). "
        "Aquest producte influeix en un o més caràcters: per exemple, el gen que determina el color de la llavor del pèsol codifica una proteïna (SGR) "
        "necessària per degradar la clorofil·la quan la llavor madura. El lloc fix que ocupa un gen dins d’un cromosoma és el seu <b>locus</b> (plural, <i>loci</i>), "
        "i és el mateix als dos homòlegs."),
    ("after", "499", P(
        "Un mateix gen pot existir en versions lleugerament diferents en la seqüència de nucleòtids, sorgides per <b>mutació</b>: són els <b>al·lels</b>. "
        "En el pèsol, l’al·lel <i>Y</i> fa la llavor groga perquè la proteïna funciona i la clorofil·la es degrada; l’al·lel <i>y</i> en fa una versió que no funciona, "
        "i la llavor es queda verda. Com que una cèl·lula diploide té dos homòlegs, té <b>dos al·lels de cada gen autosòmic</b>, un a cada cromosoma "
        "de la parella. En una població hi pot haver més de dos al·lels d’un gen (al grup sanguini ABO n’hi ha tres), però cada persona en porta, com a màxim, dos.")),
    ("after", "499", {"t": "fig", "key": "homolegs"}),
    ("after", "499", P(
        "Si els dos al·lels són iguals (<i>YY</i> o <i>yy</i>), l’individu és <b>homozigot</b> per a aquell gen; si són diferents (<i>Yy</i>), és <b>heterozigot</b>. "
        "El <b>genotip</b> és la combinació d’al·lels que porta (<i>YY</i>, <i>Yy</i> o <i>yy</i>); el <b>fenotip</b> és el caràcter que s’observa o es mesura "
        "(llavor groga o verda, però també un grup sanguini o la concentració d’un enzim). El fenotip depèn del genotip i, en molts caràcters, també de l’ambient.")),
    ("after", "499", P(
        "Què passa en un heterozigot, si cada al·lel «diu» una cosa diferent? Sovint un dels dos al·lels determina tot sol el fenotip: és l’al·lel "
        "<b>dominant</b>, i l’altre, que queda amagat, és el <b>recessiu</b>. Un al·lel recessiu només es manifesta en homozigosi. En el pèsol, <i>Yy</i> fa "
        "la llavor groga com <i>YY</i>: amb una sola còpia funcional del gen n’hi ha prou per degradar la clorofil·la. Aquest és el cas més freqüent: "
        "l’al·lel recessiu sol ser una versió que no fa la seva funció, i una còpia bona compensa la que falla. Dominant no vol dir «el bo» "
        "(hi ha malalties dominants, com la malaltia de Huntington) ni «el més freqüent» a la població. Hi ha altres relacions entre al·lels, la dominància "
        "incompleta i la codominància, que es veuen a l’apartat 4.2.")),
    ("after", "499", P(
        "Per anomenar les generacions d’un experiment: <b>P</b> són els progenitors (parentals), <b>F1</b> la primera generació filial (els seus fills) "
        "i <b>F2</b> la segona (els fills de creuar individus de la F1 entre si).")),
    ("ins", "500", H("Les lleis de Mendel i la seva explicació per la meiosi")),
    ("ins", "500", P(
        "<b>Llei de la uniformitat de la F1.</b> Mendel va creuar dues línies pures, de llavor groga (<i>YY</i>) i de llavor verda (<i>yy</i>). "
        "Totes les plantes de la F1 van tenir llavors grogues. Avui ho entenem així: cada progenitor homozigot només pot donar un tipus de gàmeta "
        "(<i>Y</i> o <i>y</i>), i per tant tots els fills són <i>Yy</i>, iguals entre si, i mostren el fenotip de l’al·lel dominant.")),
    ("set", "500",
        "<b>Llei de la segregació.</b> En autofecundar la F1, a la F2 va reaparèixer el verd, en una proporció d’1 verd per cada 3 grocs "
        "(Mendel va comptar 6.022 llavors grogues i 2.001 de verdes). La conclusió és que els dos al·lels d’un individu no es barregen: "
        "<b>se separen (segreguen) en formar els gàmetes, i cada gàmeta en rep només un</b>. Un heterozigot <i>Yy</i> fa la meitat dels gàmetes <i>Y</i> "
        "i la meitat <i>y</i>. La base cel·lular és la <b>meiosi</b>: a l’anafase I se separen els cromosomes homòlegs, i cada un porta un dels dos al·lels "
        "(si hi ha hagut un entrecreuament entre el gen i el centròmer, la separació definitiva es fa a l’anafase II, quan se separen les cromàtides)."),
    ("after", "500", P(
        "<b>Llei de la transmissió independent.</b> Quan Mendel va seguir dos caràcters alhora (color i textura de la llavor), va veure que s’heretaven "
        "sense influir-se: tenir llavor groga no fa més probable tenir-la llisa. Els al·lels de <b>gens situats en parelles de cromosomes diferents</b> "
        "es reparteixen als gàmetes amb independència, perquè a la metafase I cada parella d’homòlegs s’orienta a l’atzar, sense dependre de les altres. "
        "Un individu <i>AaBb</i> fa quatre tipus de gàmetes, <i>AB</i>, <i>Ab</i>, <i>aB</i> i <i>ab</i>, cadascun amb probabilitat ¼. "
        "Si els dos gens són al mateix cromosoma, en canvi, tendeixen a viatjar junts: estan <b>lligats</b> i aquesta llei no s’hi aplica, "
        "llevat que un entrecreuament els separi (apartat 4.3).")),
    ("after", "500", P(
        "Alguns llibres en compten només dues lleis (segregació i transmissió independent) i d’altres en compten tres, amb la uniformitat de la F1 "
        "com a primera. Per no confondre’s, a la PAU és millor anomenar-les pel nom que pel número.")),
    ("sub", "505.0", "Per què la segona llei de Mendel falla", "Per què la llei de la transmissió independent falla"),
]

# 4.2 Monohibridisme: més explicació del quadre de Punnett i de l'encreuament prova
D += [
    ("set", "509",
        "El <b>monohibridisme</b> estudia l’herència d’un sol caràcter, controlat per un sol gen. Per predir la descendència d’un encreuament es fan tres passos: "
        "(1) s’escriu el genotip de cada progenitor; (2) s’escriuen els gàmetes que pot fer cada un, amb la seva probabilitat (un homozigot <i>AA</i> només fa gàmetes <i>A</i>; "
        "un heterozigot <i>Aa</i> fa ½ <i>A</i> i ½ <i>a</i>); (3) es combinen tots els gàmetes d’un progenitor amb tots els de l’altre, perquè la fecundació els uneix a l’atzar. "
        "La taula que fa aquesta combinació és el <b>quadre de Punnett</b>: els gàmetes d’un progenitor van a les files, els de l’altre a les columnes, i cada casella és un zigot possible."),
    ("after", "509", P(
        "Amb dominància completa, <i>Aa</i> × <i>Aa</i> dona els genotips ¼ <i>AA</i>, ½ <i>Aa</i> i ¼ <i>aa</i>. Com que <i>AA</i> i <i>Aa</i> tenen el mateix fenotip, "
        "els fenotips surten en proporció <b>3 dominants : 1 recessiu</b>. <i>AA</i> × <i>aa</i> dona tota la descendència <i>Aa</i>, de fenotip dominant. "
        "Aquestes proporcions són probabilitats per a cada fill, no un resultat garantit en cada família: amb pocs descendents, l’atzar pot donar altres xifres.")),
    ("after", "509", P(
        "Un individu de fenotip dominant pot ser <i>AA</i> o <i>Aa</i>, i a simple vista no es distingeixen. Per saber-ho es fa un <b>encreuament prova</b>: "
        "es creua amb un homozigot recessiu <i>aa</i>, que només aporta gàmetes <i>a</i> i, per tant, deixa veure directament quin al·lel ha aportat l’altre progenitor. "
        "Si surt algun fill de fenotip recessiu, el progenitor era <i>Aa</i> (s’espera 1:1); si tota la descendència és dominant i és nombrosa, el més probable és que sigui <i>AA</i>.")),
    ("set", "511",
        "No sempre un al·lel domina completament l’altre. A la <b>dominància incompleta</b>, l’heterozigot té un fenotip intermedi entre els dos homozigots: "
        "en la planta de nit (<i>Mirabilis jalapa</i>), flor vermella <i>RR</i> × blanca <i>rr</i> dona una F1 rosa <i>Rr</i>, perquè una sola còpia de l’al·lel <i>R</i> "
        "fa la meitat de pigment. A la F2 els fenotips surten 1 vermella : 2 roses : 1 blanca, la mateixa proporció que els genotips. "
        "A la <b>codominància</b>, en canvi, l’heterozigot manifesta sencers els dos al·lels alhora, no un intermedi. És el cas del grup sanguini ABO: "
        "l’al·lel <i>I</i><sup>A</sup> posa l’antigen A a la superfície dels glòbuls vermells, <i>I</i><sup>B</sup> hi posa l’antigen B, i <i>i</i> no en posa cap. "
        "<i>I</i><sup>A</sup> i <i>I</i><sup>B</sup> són codominants entre si (una persona <i>I</i><sup>A</sup><i>I</i><sup>B</sup> té els dos antígens) i tots dos són dominants sobre <i>i</i>. "
        "Els genotips són <i>I</i><sup>A</sup><i>I</i><sup>A</sup> i <i>I</i><sup>A</sup><i>i</i> (grup A), <i>I</i><sup>B</sup><i>I</i><sup>B</sup> i <i>I</i><sup>B</sup><i>i</i> (grup B), "
        "<i>I</i><sup>A</sup><i>I</i><sup>B</sup> (grup AB) i <i>ii</i> (grup O). Un pare A i una mare B poden tenir fills dels quatre grups si tots dos són heterozigots "
        "(<i>I</i><sup>A</sup><i>i</i> × <i>I</i><sup>B</sup><i>i</i>). Aquest gen és també un exemple d’<b>al·lelisme múltiple</b>: tres al·lels a la població."),
]

# 4.3 Dihibridisme: explicar d'on surt el 9:3:3:1 i què és l'entrecreuament
D += [
    ("set", "520",
        "El <b>dihibridisme</b> estudia dos caràcters alhora, controlats per dos gens. Si els gens són en cromosomes diferents, cada un segueix la seva pròpia segregació "
        "i les probabilitats es multipliquen. Un doble heterozigot <i>AaBb</i> fa quatre tipus de gàmetes equiprobables (<i>AB</i>, <i>Ab</i>, <i>aB</i>, <i>ab</i>, ¼ cadascun), "
        "i per això el quadre de Punnett de <i>AaBb</i> × <i>AaBb</i> té 4 × 4 = 16 caselles igualment probables. Comptant fenotips, surt "
        "<b>9 <i>A_B_</i> : 3 <i>A_bb</i> : 3 <i>aaB_</i> : 1 <i>aabb</i></b> (el guió vol dir «qualsevol al·lel»). És el mateix que multiplicar les proporcions de cada gen per separat: "
        "¾ × ¾ = 9/16 dominants per als dos caràcters, ¾ × ¼ = 3/16, ¼ × ¾ = 3/16 i ¼ × ¼ = 1/16. Un encreuament prova <i>AaBb</i> × <i>aabb</i> dona quatre fenotips en proporció 1:1:1:1, "
        "perquè cada gàmeta del dihíbrid es veu directament al fill."),
    ("set", "521",
        "Cada cromosoma porta centenars o milers de gens. Dos gens situats al mateix cromosoma estan <b>lligats</b>: tendeixen a passar junts al mateix gàmeta, "
        "perquè viatgen al mateix tros de DNA. La combinació d’al·lels que el dihíbrid va rebre de cada progenitor es diu <b>parental</b>. "
        "Per exemple, si va rebre <i>AB</i> en un cromosoma i <i>ab</i> en l’homòleg (disposició en <b>cis</b>), fa sobretot gàmetes parentals <i>AB</i> i <i>ab</i>. "
        "Els gàmetes <b>recombinants</b> (<i>Ab</i> i <i>aB</i>) només apareixen si a la profase I de la meiosi hi ha hagut un <b>entrecreuament</b> entre els dos loci: "
        "dues cromàtides no germanes dels homòlegs es trenquen i s’intercanvien els trossos. Com més separats són els gens, més probable és que hi caigui un entrecreuament entre ells, "
        "i més recombinants surten. Per això la <b>freqüència de recombinació</b> (descendents recombinants dividit pel total) serveix per mesurar la distància entre gens. "
        "S’expressa en <b>centimorgans</b> (cM): 1 % de recombinació = 1 cM. No és una distància en nucleòtids, i amb un 50 % (el màxim que es pot observar) "
        "els gens es comporten com si no estiguessin lligats."),
]

# 4.4 Herència lligada al sexe: explicar abans els cromosomes sexuals
D += [
    ("set", "535",
        "En els humans, el sexe cromosòmic el determina la parella de <b>cromosomes sexuals</b>: les dones són XX i els homes XY. Totes les dones fan òvuls amb un cromosoma X; "
        "els homes fan la meitat d’espermatozoides amb X i la meitat amb Y, i per això cada fill té ½ de probabilitat de ser noi o noia. El cromosoma Y és petit i porta pocs gens, "
        "entre ells <i>SRY</i>, que inicia el desenvolupament dels testicles. L’X és gran i porta més de 800 gens que codifiquen proteïnes, la majoria sense cap relació amb el sexe "
        "(coagulació de la sang, visió dels colors…). X i Y només comparteixen dos trossos petits als extrems (les regions pseudoautosòmiques), que els permeten aparellar-se a la meiosi; "
        "la resta de l’X és la <b>regió diferencial</b>, sense equivalent a l’Y."),
    ("after", "535", P(
        "D’aquí surt la particularitat de l’<b>herència lligada a l’X</b>: una dona té dos al·lels de cada gen de la regió diferencial de l’X (com en un autosoma), "
        "però un home només en té un, perquè l’Y no porta aquell gen. Es diu que l’home és <b>hemizigot</b> per a aquests gens. Per tant, un sol al·lel recessiu a l’X ja es manifesta en un home, "
        "mentre que una dona només el manifesta si és homozigota; si és heterozigota, és <b>portadora</b>: no té la malaltia però la pot transmetre. "
        "Per això les malalties recessives lligades a l’X són molt més freqüents en homes. Un home sempre rep l’X de la mare (del pare rep l’Y) i sempre passa el seu X a totes les filles.")),
]

# 4.5 Pedigrís
D += [
    ("ins", "549", P(
        "En humans no es poden fer encreuaments experimentals. Per estudiar com s’hereta un caràcter es fan servir els <b>pedigrís</b> o arbres genealògics: "
        "es dibuixa una família durant diverses generacions i es marca qui manifesta el caràcter. A partir de qui l’hereta de qui es dedueix el patró d’herència "
        "(dominant o recessiu, autosòmic o lligat a l’X) i, després, la probabilitat que un futur fill l’hereti.")),
    ("set", "549",
        "Els símbols són estàndard: el quadrat és un home i el cercle una dona; el símbol ple indica una persona afectada; un punt al mig (o mig farcit), un portador conegut. "
        "La línia horitzontal uneix una parella; la vertical baixa cap als fills, que s’ordenen d’esquerra a dreta per ordre de naixement. Les generacions es numeren amb xifres romanes "
        "(I, II, III…) i els individus de cada generació, d’esquerra a dreta (II-3 és la tercera persona de la generació II). Una persona morta es marca amb una barra diagonal. "
        "Com es llegeix el patró:"),
    ("ins", "552", P(
        "Per calcular riscos cal una mica de probabilitat. Cada fecundació és un fet a l’atzar: quin espermatozoide i quin òvul s’uneixen no depèn dels fills anteriors. "
        "Les proporcions mendelianes (¼, ½, ¾) són, doncs, la probabilitat de cada fill per separat.")),
]

# 4.6 Caràcters quantitatius
D += [
    ("set", "563",
        "Els caràcters que ha estudiat aquest tema tenen unes poques classes ben separades (groc o verd, A, B, AB o O). Són <b>caràcters qualitatius</b>. Però molts caràcters, com l’alçada, "
        "el color de la pell o el rendiment d’un cultiu, varien de manera gradual i es mesuren amb un número: són <b>caràcters quantitatius</b>. Hi intervenen molts gens, cadascun amb un efecte petit "
        "que se suma al dels altres (<b>herència poligènica</b>), i sovint també l’ambient (la nutrició influeix en l’alçada). Cada un d’aquests gens segueix les lleis de Mendel, però com que les "
        "combinacions possibles són moltes i l’ambient les difumina, el fenotip de la població fa una distribució contínua en forma de campana, no una proporció 3:1. "
        "A la PAU n’hi ha prou amb aquesta idea i amb saber que les proporcions d’un problema de Mendel clàssic no s’apliquen directament a un caràcter quantitatiu. "
        "No es demana l’heretabilitat ni la variància."),
]

# =====================================================================================
# TEMA 1 · BIOMOLÈCULES
# =====================================================================================
D += [
    ("ins", "8", H("De què estan fets els éssers vius")),
    ("ins", "8", P(
        "Tots els éssers vius estan fets de les mateixes poques peces químiques. Els elements químics que formen la matèria viva són els <b>bioelements</b>: "
        "el carboni (C), l’hidrogen (H), l’oxigen (O) i el nitrogen (N), amb el fòsfor (P) i el sofre (S), en sumen més del 98 % de la massa. "
        "Altres elements hi són en quantitats molt petites però imprescindibles (ferro, magnesi, iode, zinc…): són els <b>oligoelements</b>.")),
    ("ins", "8", P(
        "Aquests elements s’uneixen formant <b>biomolècules</b>. Les <b>inorgàniques</b> també existeixen fora dels éssers vius: l’aigua i les sals minerals. "
        "Les <b>orgàniques</b> tenen un esquelet de carboni i són de quatre grups: <b>glúcids</b>, <b>lípids</b>, <b>proteïnes</b> (pròtids) i <b>àcids nucleics</b>. "
        "El carboni és la base perquè forma quatre enllaços covalents i pot unir-se a altres carbonis fent cadenes i anells de qualsevol llargada.")),
    ("ins", "8", P(
        "Moltes biomolècules grans són <b>polímers</b>: cadenes llargues fetes de la repetició d’unitats petites, els <b>monòmers</b>. Els polisacàrids són polímers de monosacàrids; "
        "les proteïnes, d’aminoàcids; els àcids nucleics, de nucleòtids. Dos monòmers s’uneixen per <b>condensació</b>: s’uneixen amb un enllaç covalent i s’allibera una molècula d’aigua. "
        "La reacció inversa, que trenca l’enllaç afegint-hi una molècula d’aigua, és la <b>hidròlisi</b>: és el que fa la digestió.")),
    ("ins", "8", P(
        "Per entendre la forma i el comportament de les biomolècules cal distingir dos tipus d’unions. Els <b>enllaços covalents</b> (els àtoms comparteixen electrons) "
        "són forts i formen l’esquelet de la molècula. Les <b>interaccions febles</b> —enllaços d’hidrogen, atraccions entre càrregues (enllaços iònics) i interaccions hidrofòbiques— "
        "són molt més dèbils una per una, però n’hi ha moltes: determinen com es plega una proteïna, com s’aparellen les dues cadenes del DNA o com es forma una membrana, "
        "i es poden fer i desfer sense trencar la molècula. Una molècula o una part d’una molècula és <b>polar</b> si té càrregues parcials (perquè hi ha àtoms com O o N, que atrauen més els electrons); "
        "les parts polars interaccionen bé amb l’aigua (són <b>hidròfiles</b>), i les apolars, com les cadenes de C i H, no (són <b>hidròfobes</b>).")),
    ("ins", "8", H("L’aigua: una molècula polar")),
    ("ins", "8", P(
        "L’aigua és la molècula més abundant dels éssers vius (entre el 60 i el 90 % de la massa d’un organisme) i és el medi on passen gairebé totes les reaccions cel·lulars. "
        "Les seves propietats, molt poc corrents per a una molècula tan petita, s’expliquen per la seva estructura.")),
]

D += [
    ("ins", "25", P(
        "Els <b>glúcids</b> són la principal font d’energia immediata de les cèl·lules (la glucosa), la forma de guardar-la (el midó i el glicogen) i el material de parets i esquelets "
        "(la cel·lulosa i la quitina). També formen part dels nucleòtids i, units a proteïnes i lípids de la membrana, serveixen perquè les cèl·lules es reconeguin.")),
    ("ins", "26", P(
        "Els <b>monosacàrids</b> són els glúcids més simples: no es poden hidrolitzar en glúcids més petits. Són dolços i solubles en aigua. Es classifiquen pel grup carbonil "
        "(aldoses o cetoses) i pel nombre de carbonis (triosa, 3; pentosa, 5; hexosa, 6). La glucosa és una aldohexosa: una aldosa de sis carbonis, C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>. "
        "Els carbonis es numeren des de l’extrem més proper al carbonil: a la glucosa, el C1 és el de l’aldehid.")),
    ("set", "26",
        "Els monosacàrids de més pes a la PAU són les pentoses (ribosa i desoxiribosa, als àcids nucleics) i les hexoses (glucosa, fructosa, galactosa). "
        "En dissolució aquosa, les pentoses i les hexoses gairebé no es troben en forma de cadena oberta: el grup carbonil reacciona amb un grup OH de la mateixa molècula i la cadena es tanca en un <b>anell</b>. "
        "A la glucosa, l’oxigen del C5 s’uneix al C1 i es forma un anell de sis vèrtexs (cinc carbonis i un oxigen), la <b>piranosa</b>; la fructosa forma sobretot un anell de cinc, la <b>furanosa</b>. "
        "En tancar-se l’anell, el carboni que era el carbonil (el C1 a la glucosa, el C2 a la fructosa) passa a tenir un grup OH nou, que pot quedar a un costat o a l’altre de l’anell: "
        "aquest carboni s’anomena <b>carboni anomèric</b>, i les dues formes resultants són els <b>anòmers</b> α i β. En dissolució es converteixen l’una en l’altra; "
        "la diferència es fixa quan el carboni anomèric forma un enllaç amb un altre sucre."),
    ("after", "26", P(
        "Per dibuixar els anells es fa servir la <b>projecció de Haworth</b>: l’anell es dibuixa pla i perpendicular al paper, i cada substituent queda per sobre o per sota del pla. "
        "A la D-glucosa, si l’OH del carboni anomèric queda cap avall (al costat contrari del CH<sub>2</sub>OH del C5), és l’α-D-glucosa; si queda cap amunt, la β-D-glucosa. "
        "Els altres substituents de la D-glucosa no canvien: OH del C2 avall, del C3 amunt, del C4 avall, i el CH<sub>2</sub>OH del C5 amunt. "
        "(D i L indiquen dues formes que són imatges especulars; els éssers vius fan servir gairebé exclusivament D-sucres.)")),
    ("ins", "28", P(
        "Quan dos monosacàrids s’uneixen per condensació es forma un <b>disacàrid</b>; si se n’uneixen molts, un <b>polisacàrid</b>. "
        "Els disacàrids més comuns són la maltosa (que surt de digerir el midó), la lactosa (el sucre de la llet) i la sacarosa (el sucre de taula).")),
]

D += [
    ("ins", "53", P(
        "Els <b>lípids</b> fan funcions molt diferents: són la reserva d’energia més concentrada (els greixos), formen les membranes cel·lulars (els fosfolípids i el colesterol), "
        "impermeabilitzen (les ceres) i fan de senyals (les hormones esteroides). Per això no es poden definir per una funció ni per una estructura comuna, sinó per una propietat física.")),
    ("ins", "70", P(
        "Les <b>proteïnes</b> són les molècules que fan la major part de la feina de la cèl·lula: acceleren reaccions (enzims), transporten substàncies (l’hemoglobina porta oxigen), "
        "donen suport (el col·lagen, la queratina), defensen (els anticossos), transmeten senyals (moltes hormones, com la insulina, i els receptors), permeten el moviment (l’actina i la miosina "
        "del múscul) i regulen quins gens s’expressen. Totes són polímers d’aminoàcids, i el que les fa tan diferents és la seqüència d’aminoàcids i la forma tridimensional que en resulta.")),
    ("ins", "87", P(
        "Les reaccions químiques de la cèl·lula, per si soles, serien massa lentes a 37 °C per mantenir la vida. Perquè una reacció comenci, els reactius han de superar una barrera d’energia, "
        "l’<b>energia d’activació</b>: encara que la reacció alliberi energia, cal una «empenta» inicial per trencar els enllaços. Un <b>catalitzador</b> és una substància que fa la barrera més baixa, "
        "i per tant accelera la reacció, sense consumir-se. Els catalitzadors biològics són els <b>enzims</b>. La molècula sobre la qual actua l’enzim és el <b>substrat</b>, "
        "i la que en surt, el <b>producte</b>: E + S ⇄ ES → E + P (ES és el complex enzim-substrat).")),
    ("ins", "106", P(
        "Els <b>àcids nucleics</b> (DNA i RNA) guarden i transmeten la informació genètica: el DNA conté les instruccions per fabricar les proteïnes de la cèl·lula i es copia per passar-les a les cèl·lules filles; "
        "l’RNA és la còpia de treball d’aquestes instruccions i participa en la síntesi de proteïnes. Tots dos són polímers de <b>nucleòtids</b>.")),
]

# =====================================================================================
# TEMA 2 · LA CÈL·LULA
# =====================================================================================
D += [
    ("ins", "165", P(
        "Una <b>cèl·lula</b> és la porció de matèria viva més petita capaç de fer per si mateixa les funcions vitals: nodrir-se (obtenir matèria i energia i transformar-les), "
        "relacionar-se amb el medi i reproduir-se. Està envoltada per una membrana que la separa de l’exterior, conté un medi intern aquós (el citoplasma) i porta la informació genètica en forma de DNA. "
        "Hi ha éssers vius d’una sola cèl·lula (<b>unicel·lulars</b>, com els bacteris o els llevats) i d’altres fets de milions de cèl·lules especialitzades que cooperen (<b>pluricel·lulars</b>).")),
    ("ins", "166", P(
        "Les cèl·lules són tan petites que es mesuren en <b>micròmetres</b> (1 µm = una mil·lèsima de mil·límetre) i les seves parts, en <b>nanòmetres</b> (1 nm = una mil·lèsima de micròmetre). "
        "Una cèl·lula animal típica fa 10–30 µm; un bacteri, 1–5 µm; un ribosoma, uns 25 nm. L’ull humà només distingeix objectes d’unes 100 µm (0,1 mm), i per això la descoberta de les cèl·lules "
        "va dependre del microscopi. En un microscopi cal distingir dues coses: els <b>augments</b> (quantes vegades es fa més gran la imatge) i el <b>poder de resolució</b> "
        "(la distància mínima a què han d’estar dos punts perquè es vegin separats). El que limita el que es pot veure és la resolució, no els augments.")),
    ("ins", "176", P(
        "Totes les cèl·lules tenen membrana plasmàtica, citoplasma, ribosomes (on es fabriquen les proteïnes) i DNA. Segons on és el DNA es distingeixen dos tipus d’organització. "
        "Les cèl·lules <b>procariotes</b> (del grec <i>pro</i>, abans, i <i>karyon</i>, nucli) no tenen nucli: el DNA és lliure al citoplasma. Les <b>eucariotes</b> (<i>eu</i>, veritable) "
        "tenen el DNA tancat dins un <b>nucli</b> envoltat de membrana, i a més tenen <b>orgànuls</b>: compartiments interns, limitats per membranes, especialitzats en funcions concretes. "
        "Les procariotes són més petites i simples i van aparèixer abans; les eucariotes formen protists, fongs, plantes i animals.")),
    ("ins", "191", P(
        "Tota cèl·lula està envoltada per la <b>membrana plasmàtica</b>, una làmina d’uns 7–8 nm de gruix que separa el citoplasma del medi extern. No és una simple bossa: "
        "és <b>selectivament permeable</b> (decideix què entra i què surt), rep senyals de fora i permet que les cèl·lules es reconeguin i s’uneixin entre si. "
        "Les membranes dels orgànuls tenen la mateixa estructura bàsica. Està feta sobretot de lípids (fosfolípids i, en animals, colesterol) i proteïnes, amb glúcids units a la cara externa.")),
    ("ins", "202", P(
        "Per entendre el transport cal la idea de <b>gradient de concentració</b>: la diferència de concentració d’una substància entre dos llocs. Les molècules d’una dissolució es mouen a l’atzar "
        "i, de mitjana, passen del lloc on n’hi ha més al lloc on n’hi ha menys, fins que la concentració s’iguala. Aquest moviment espontani és la <b>difusió</b>, i no gasta energia de la cèl·lula: "
        "es diu que va <b>a favor de gradient</b>. Moure una substància cap on ja n’hi ha més (<b>en contra de gradient</b>) no passa sol: cal gastar energia. "
        "Aquests dos criteris, el sentit respecte del gradient i si hi intervé una proteïna, classifiquen tots els tipus de transport.")),
    ("ins", "206", P(
        "Una <b>dissolució</b> té un <b>solut</b> (la substància dissolta: sals, sucres…) i un <b>dissolvent</b> (a la cèl·lula, l’aigua). Una membrana <b>semipermeable</b> deixa passar l’aigua però no el solut. "
        "Si a cada costat d’aquesta membrana hi ha concentracions de solut diferents, el solut no pot igualar-les passant d’un costat a l’altre, i és l’aigua la que es mou. "
        "Per comparar dos medis es parla de medi <b>hipertònic</b> (més concentrat en solut), <b>hipotònic</b> (menys concentrat) i <b>isotònic</b> (la mateixa concentració). "
        "Són termes relatius: un medi és hipertònic <i>respecte de</i> l’interior de la cèl·lula.")),
    ("ins", "220", P(
        "El citoplasma d’una cèl·lula eucariota està format pel <b>citosol</b>, un medi aquós ple de proteïnes on passen moltes reaccions (com la glucòlisi), "
        "els <b>ribosomes</b> (partícules de RNA i proteïna, sense membrana, que fabriquen les proteïnes), el <b>citoesquelet</b> (una xarxa de filaments proteics que dona forma a la cèl·lula i mou els orgànuls) "
        "i els <b>orgànuls</b> amb membrana. Cada orgànul és un compartiment amb un medi intern propi, i això permet fer alhora reaccions incompatibles en llocs diferents "
        "(per exemple, digerir molècules dins els lisosomes sense digerir la cèl·lula). Per a la PAU, el que importa de cada orgànul és <b>quina funció hi passa</b>, perquè gairebé totes les preguntes de metabolisme demanen on té lloc una via.")),
    ("ins", "222", P(
        "Diversos orgànuls formen el <b>sistema d’endomembranes</b>: l’embolcall nuclear, el reticle endoplasmàtic, l’aparell de Golgi, els lisosomes i les vesícules. "
        "Estan comunicats per vesícules que es desprenen d’un i es fusionen amb el següent, de manera que les proteïnes i els lípids hi circulen en un ordre fix.")),
]

D += [
    ("ins", "246", H("Cromatina, cromosomes i cromàtides")),
    ("ins", "246", P(
        "Una cèl·lula que es divideix ha de fer una còpia de tot el seu DNA i repartir-ne una a cada cèl·lula filla. Per entendre com ho fa cal conèixer com està organitzat el DNA. "
        "En una cèl·lula eucariota, el DNA del nucli no és una sola molècula, sinó diverses molècules llargues i lineals. Cada una, enrotllada al voltant de proteïnes anomenades <b>histones</b>, "
        "forma un <b>cromosoma</b>. Mentre la cèl·lula no es divideix, els cromosomes estan descondensats i formen una massa de filaments al nucli, la <b>cromatina</b>, que no es distingeix al microscopi òptic. "
        "Quan la cèl·lula es divideix, cada cromosoma es plega i s’empaqueta molt (es <b>condensa</b>) i es fa visible com un bastonet.")),
    ("ins", "246", P(
        "Abans de dividir-se, la cèl·lula replica el DNA. A partir d’aquest moment, cada cromosoma està format per dues molècules de DNA idèntiques, les <b>cromàtides germanes</b>, "
        "que queden unides per una zona estreta, el <b>centròmer</b>. Al centròmer hi ha el <b>cinetocor</b>, l’estructura proteica on s’enganxen els microtúbuls que estiraran les cromàtides. "
        "Un cromosoma amb dues cromàtides continua comptant com <b>un</b> cromosoma: el nombre de cromosomes es compta pels centròmers.")),
    ("ins", "246", P(
        "Les cèl·lules del cos (cèl·lules <b>somàtiques</b>) de la majoria d’animals i plantes són <b>diploides</b> (2n): tenen els cromosomes per parelles. Els dos cromosomes de cada parella són <b>homòlegs</b>: "
        "un prové del progenitor matern i l’altre del patern, tenen la mateixa forma i porten els mateixos gens en el mateix ordre (tot i que poden portar versions diferents, els al·lels, tema 4). "
        "Els <b>gàmetes</b> són <b>haploides</b> (n): porten un sol cromosoma de cada parella. En humans, 2n = 46 (23 parelles) i n = 23. El conjunt de cromosomes d’una espècie, ordenats per parelles, és el <b>cariotip</b>.")),
    ("ins", "246", H("Les fases del cicle")),
    ("ins", "246", P(
        "El <b>cicle cel·lular</b> és la seqüència d’etapes que viu una cèl·lula des que neix, per divisió d’una altra, fins que es divideix ella mateixa.")),
    ("ins", "257", P(
        "Una cèl·lula eucariota es pot dividir de dues maneres. La <b>mitosi</b> fa dues cèl·lules filles genèticament iguals a la mare, i és la divisió que fa créixer un organisme i en renova els teixits. "
        "La <b>meiosi</b> fa cèl·lules amb la meitat de cromosomes, diferents entre si, i serveix per formar els gàmetes (apartat 2.8). "
        "Per repartir els cromosomes, la cèl·lula munta el <b>fus mitòtic</b> (o fus acromàtic), un conjunt de microtúbuls que surt de dos pols oposats de la cèl·lula i s’enganxa als cinetocors.")),
    ("ins", "270", P(
        "A la <b>reproducció sexual</b>, un nou individu es forma per la unió de dos gàmetes, un de cada progenitor: és la <b>fecundació</b>, i en resulta el <b>zigot</b>, primera cèl·lula del nou individu. "
        "Perquè el nombre de cromosomes no es dupliqui a cada generació, els gàmetes han de tenir la meitat de cromosomes que les cèl·lules del cos. La divisió que fa aquesta reducció és la <b>meiosi</b>. "
        "Consisteix en dues divisions seguides (meiosi I i meiosi II) després d’una sola replicació del DNA.")),
]

# =====================================================================================
# TEMA 3 · METABOLISME
# =====================================================================================
D += [
    ("ins", "330", P(
        "El <b>metabolisme</b> és el conjunt de reaccions químiques d’un ésser viu. Cada reacció és un sol pas, catalitzat per un enzim. Una <b>via metabòlica</b> és una seqüència de reaccions en què el producte d’una "
        "és el substrat de la següent, des d’un substrat inicial fins a un producte final; les molècules intermèdies s’anomenen <b>metabòlits</b>.")),
    ("ins", "330", P(
        "Una cèl·lula necessita contínuament dues coses: <b>matèria</b>, per construir i renovar les seves molècules, i <b>energia</b>, per fer-ho i per moure’s, transportar substàncies o dividir-se. "
        "Segons d’on treuen el carboni, els éssers vius són <b>autòtrofs</b>, si fabriquen la seva matèria orgànica a partir de CO<sub>2</sub> (les plantes, les algues, molts bacteris), "
        "o <b>heteròtrofs</b>, si l’han de prendre ja feta d’altres éssers vius (els animals, els fongs, la majoria de bacteris). Segons d’on treuen l’energia, són <b>fotòtrofs</b> (llum) "
        "o <b>quimiòtrofs</b> (reaccions químiques). Una planta és fotoautòtrofa; un ésser humà, quimioheteròtrof.")),
    ("ins", "330", P(
        "L’energia que fan servir les cèl·lules està guardada als enllaços de les molècules orgàniques. S’allibera quan aquestes molècules s’<b>oxiden</b>. "
        "En química, <b>oxidar</b> una molècula és treure-li electrons, i <b>reduir-la</b> és donar-n’hi; les dues coses passen sempre alhora (una molècula s’oxida perquè una altra es redueix). "
        "En biologia, els electrons sovint viatgen acompanyats de protons, com a àtoms d’hidrogen: per això una molècula que perd hidrògens s’oxida (deshidrogenació) i una que en guanya es redueix. "
        "Una molècula molt reduïda, rica en enllaços C–H, com la glucosa o un àcid gras, té molta energia aprofitable; una molècula totalment oxidada, com el CO<sub>2</sub>, ja no en té.")),
    ("ins", "330", P(
        "Les reaccions que alliberen energia són <b>exergòniques</b> (passen espontàniament) i les que en necessiten són <b>endergòniques</b>. La cèl·lula fa les segones acoblant-les a les primeres, "
        "a través de molècules intermediàries que reben l’energia en un lloc i la lliuren en un altre: l’<b>ATP</b> i els <b>coenzims transportadors d’electrons</b>.")),
    ("set", "330",
        "El metabolisme té dues vessants. El <b>catabolisme</b> degrada molècules complexes en molècules més simples, les oxida i allibera energia, que queda en ATP i en coenzims reduïts. "
        "L’<b>anabolisme</b> construeix molècules complexes a partir de simples, les redueix i gasta ATP i poder reductor."),
    ("ins", "331", P(
        "L’<b>ATP</b> (adenosina trifosfat) és un nucleòtid: adenina, ribosa i tres grups fosfat en fila. Els dos últims fosfats estan units per enllaços que, en hidrolitzar-se, alliberen força energia. "
        "Quan la cèl·lula necessita energia, trenca l’últim enllaç (ATP → ADP + P<sub>i</sub>); quan n’obté, el refà (ADP + P<sub>i</sub> → ATP). "
        "Els coenzims <b>NAD⁺</b>, <b>FAD</b> i <b>NADP⁺</b> fan una feina semblant amb els electrons: en la forma oxidada els accepten (i passen a NADH, FADH<sub>2</sub> i NADPH, formes reduïdes) "
        "i els porten fins a la reacció que els necessita, on es tornen a oxidar. Es diu que porten <b>poder reductor</b>.")),
    ("ins", "342", P(
        "La <b>respiració cel·lular</b> és el catabolisme complet de la glucosa amb oxigen: la glucosa s’oxida del tot fins a CO<sub>2</sub>, i l’oxigen, que n’accepta els electrons, es redueix a aigua: "
        "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub> → 6 CO<sub>2</sub> + 6 H<sub>2</sub>O, i l’energia alliberada es guarda en ATP. No passa d’un sol cop, sinó en quatre etapes encadenades: "
        "la <b>glucòlisi</b> (al citosol), l’oxidació del piruvat a acetil-CoA i el <b>cicle de Krebs</b> (a la matriu del mitocondri), i la <b>cadena respiratòria</b> amb la síntesi d’ATP "
        "(a la membrana interna del mitocondri). Les tres primeres arrenquen els electrons de la glucosa i els carreguen en NADH i FADH<sub>2</sub>; la quarta els porta fins a l’oxigen i aprofita l’energia per fer la major part de l’ATP.")),
    ("ins", "374", P(
        "Al final del Krebs, la glucosa ja s’ha convertit tota en CO<sub>2</sub>, però s’han fet molt pocs ATP. La major part de l’energia de la glucosa és ara als electrons dels NADH i FADH<sub>2</sub>. "
        "La <b>cadena respiratòria</b> (o cadena de transport d’electrons) és una sèrie de proteïnes i molècules de la membrana mitocondrial interna que es passen aquests electrons l’una a l’altra, "
        "cada cop a un nivell d’energia més baix, fins a l’oxigen. L’energia que van perdent els electrons s’aprofita per bombar protons (H⁺) a través de la membrana, i aquest desequilibri de protons "
        "és el que després fa funcionar l’ATP-sintasa, com l’aigua d’una presa fa girar una turbina.")),
    ("ins", "409", P(
        "Els greixos es guarden com a triacilglicerols. Per aprofitar-los, unes lipases els hidrolitzen en glicerol i àcids grassos. El glicerol s’incorpora a la glucòlisi; "
        "els àcids grassos, que són la part més energètica, es degraden per una via pròpia, la β-oxidació, anomenada així perquè l’oxidació es fa al carboni β (el C3) de la cadena.")),
    ("ins", "429", P(
        "La <b>fotosíntesi</b> és el procés pel qual els organismes fotoautòtrofs fan servir l’energia de la llum per fabricar matèria orgànica a partir de CO<sub>2</sub> i aigua. "
        "És l’entrada de matèria i d’energia de gairebé tots els ecosistemes, i l’origen de l’oxigen de l’atmosfera. Té dues fases connectades: a la <b>fase lluminosa</b> la llum es converteix en energia química "
        "(ATP i NADPH), i a la <b>fase fosca</b> o <b>cicle de Calvin</b> aquests ATP i NADPH s’utilitzen per reduir el CO<sub>2</sub> a sucre.")),
    ("ins", "433", P(
        "La llum la capten els <b>pigments fotosintètics</b>, situats a la membrana dels tilacoides. El principal és la <b>clorofil·la</b>, que absorbeix sobretot la llum blava i la vermella i reflecteix la verda "
        "(per això les fulles són verdes); els carotenoides n’amplien l’espectre. Els pigments s’agrupen en <b>fotosistemes</b>: molts pigments fan d’antena i passen l’energia captada a una parella "
        "de clorofil·les especials, el <b>centre de reacció</b>. Quan el centre de reacció rep l’energia, un dels seus electrons s’excita i salta a una molècula acceptora: la llum ha convertit la clorofil·la en un donador d’electrons. "
        "Hi ha dos fotosistemes, el II (centre de reacció P680) i el I (P700), anomenats així per la longitud d’ona, en nm, que absorbeixen millor els seus centres de reacció.")),
]

# =====================================================================================
# TEMA 5 · GENÈTICA MOLECULAR I BIOTECNOLOGIA
# =====================================================================================
D += [
    ("ins", "606", P(
        "Al tema 4 hem vist <i>com</i> s’hereten els gens; aquí veurem <i>què</i> són i <i>com</i> actuen. Un gen és un tram de DNA amb la seqüència de nucleòtids necessària per fabricar un producte, "
        "gairebé sempre una proteïna. La seqüència de bases del gen determina la seqüència d’aminoàcids de la proteïna; la seqüència d’aminoàcids en determina el plegament, i el plegament, la funció "
        "(tema 1). Així és com el DNA controla els caràcters: una mutació que canvia la seqüència d’un gen pot canviar la proteïna i, per tant, el fenotip. "
        "El procés pel qual la informació d’un gen es converteix en una proteïna s’anomena <b>expressió gènica</b>. El conjunt de tot el DNA d’un organisme (o d’una cèl·lula) és el seu <b>genoma</b>.")),
    ("ins", "606", P(
        "El DNA no surt del nucli i no fabrica proteïnes directament. La cèl·lula en fa primer una còpia d’RNA, que actua com a missatge, i aquest missatge es llegeix als ribosomes. "
        "Francis Crick va resumir aquest flux d’informació en el que va anomenar <b>dogma central de la biologia molecular</b>:")),
    ("ins", "622", P(
        "Abans de dividir-se, una cèl·lula ha de fer una còpia exacta de tot el seu DNA perquè cada filla en rebi un joc complet: és la <b>replicació</b>. "
        "El principi el van proposar Watson i Crick en descobrir la doble hèlix: com que les bases s’aparellen de manera complementària (A amb T, G amb C), cada cadena conté la informació per refer l’altra. "
        "N’hi ha prou de separar les dues cadenes i fer servir cadascuna com a <b>motlle</b> per construir-ne una de nova. La replicació comença en un punt concret, l’<b>origen de replicació</b>, "
        "on s’obre la doble hèlix. La zona en forma de Y on les cadenes s’estan separant i copiant és la <b>forquilla de replicació</b>; a partir de l’origen n’avancen dues, en sentits oposats. "
        "L’enzim que fabrica el DNA nou és la <b>DNA-polimerasa</b>, que llegeix el motlle i hi va afegint nucleòtids complementaris.")),
    ("ins", "636", P(
        "La <b>transcripció</b> és la primera etapa de l’expressió d’un gen: la cèl·lula copia la seqüència del gen en una molècula d’RNA. Ho fa l’<b>RNA-polimerasa</b>, que s’uneix al DNA en una seqüència "
        "situada just abans del gen, el <b>promotor</b>, obre la doble hèlix en aquell tram, fabrica l’RNA i s’atura en una seqüència final, el <b>terminador</b>. "
        "Només es copia una de les dues cadenes del DNA, la <b>cadena motlle</b>; l’altra, la <b>cadena codificant</b>, té la mateixa seqüència que l’RNA (amb T en lloc d’U). "
        "Exemple: si la cadena motlle és 3′–TAC GGA–5′, l’RNA és 5′–AUG CCU–3′, i la cadena codificant, 5′–ATG CCT–3′.")),
    ("ins", "639", P(
        "Per passar d’RNA a proteïna cal un codi, perquè l’RNA té 4 «lletres» (A, U, G, C) i les proteïnes, 20 aminoàcids diferents. Si cada base codifiqués un aminoàcid, només n’hi hauria 4; "
        "amb parelles de bases, 4 × 4 = 16, encara massa poques. Amb grups de tres bases hi ha 4 × 4 × 4 = 64 combinacions, prou per als 20 aminoàcids i els senyals d’inici i de parada. "
        "Cada grup de tres bases de l’RNAm s’anomena <b>codó</b>.")),
    ("ins", "655", P(
        "La <b>traducció</b> és la síntesi d’una proteïna seguint les instruccions d’un RNAm. Hi intervenen tres tipus d’RNA. L’<b>RNAm</b> porta el missatge. Els <b>ribosomes</b>, fets d’RNAr i proteïnes, "
        "són la màquina que llegeix l’RNAm i uneix els aminoàcids. Els <b>RNAt</b> fan d’adaptadors: cadascun porta un aminoàcid concret en un extrem i, a l’altre, un grup de tres bases, l’<b>anticodó</b>, "
        "complementari d’un codó. Així, cada codó de l’RNAm rep l’RNAt que porta l’aminoàcid que li correspon.")),
    ("ins", "667", P(
        "Els bacteris han d’adaptar-se de pressa al medi: no tindria sentit fabricar els enzims per digerir la lactosa si no n’hi ha. Per això els seus gens solen estar organitzats en <b>operons</b>: "
        "un grup de gens que treballen en la mateixa via, transcrits plegats a partir d’un sol promotor, i controlats per un <b>operador</b>, un tros de DNA situat entre el promotor i els gens on es pot unir una proteïna reguladora. "
        "Quan un <b>repressor</b> ocupa l’operador, l’RNA-polimerasa no pot avançar i els gens no es transcriuen.")),
    ("ins", "676", P(
        "La replicació és molt precisa, però no perfecta, i el DNA també es pot danyar per agents externs (radiacions, algunes substàncies químiques). La major part d’aquests errors i danys es reparen; "
        "els que no es reparen queden fixats com a canvis de la seqüència.")),
    ("ins", "686", P(
        "La <b>biotecnologia</b> és l’ús d’éssers vius, o de les seves molècules, per obtenir productes o serveis útils: fer pa o iogurt amb microorganismes és biotecnologia antiga. "
        "L’<b>enginyeria genètica</b> és la part moderna: un conjunt de tècniques per aïllar un gen, modificar-lo, multiplicar-lo i introduir-lo en un altre organisme, de manera que el fabriqui. "
        "Per exemple, el gen humà de la insulina es pot introduir en bacteris perquè la produeixin. Per fer-ho calen eines per tallar el DNA en llocs precisos, per enganxar-ne els trossos i per fer-los entrar en una cèl·lula.")),
]

# =====================================================================================
# TEMA 6 · EVOLUCIÓ
# =====================================================================================
D += [
    ("ins", "756", P(
        "Fins al segle XVIII es pensava majoritàriament que les espècies havien aparegut tal com són i no canviaven (<b>fixisme</b>). L’<b>evolucionisme</b> sosté el contrari: les espècies actuals "
        "provenen d’altres espècies anteriors, de les quals s’han anat diferenciant a poc a poc, i totes les formes de vida estan emparentades per avantpassats comuns, com les branques d’un arbre.")),
    ("ins", "756", P(
        "Per parlar d’evolució cal tenir clars dos conceptes. Una <b>espècie</b> és, en organismes amb reproducció sexual, un conjunt d’individus que es poden creuar entre si i tenir descendència fèrtil (apartat 6.5). "
        "Una <b>població</b> és el conjunt d’individus d’una mateixa espècie que viuen en una mateixa zona i es reprodueixen entre ells. És important perquè <b>evolucionen les poblacions, no els individus</b>: "
        "un individu neix amb uns gens i no els canvia; el que canvia d’una generació a la següent és la proporció d’individus de cada tipus dins la població.")),
    ("ins", "769", P(
        "Charles Darwin va observar, durant el viatge del <i>Beagle</i> (1831–1836) i en anys posteriors, que els individus d’una mateixa espècie no són iguals, que moltes d’aquestes diferències s’hereten, "
        "i que neixen molts més individus dels que poden sobreviure i reproduir-se amb els recursos disponibles. Alfred R. Wallace va arribar a la mateixa idea de manera independent, i la van presentar junts el 1858.")),
    ("after", "769", P(
        "Una <b>adaptació</b> és un caràcter heretable que augmenta l’èxit reproductiu dels seus portadors en un ambient concret: el bec gruixut d’un pinsà que menja llavors dures, el pelatge blanc d’un animal de la neu. "
        "La selecció natural és el mecanisme que explica com sorgeixen: les variants que funcionen millor en aquell ambient es fan més freqüents generació rere generació. "
        "Una adaptació ho és sempre respecte d’un ambient; si l’ambient canvia, pot deixar de ser-ho.")),
    ("ins", "781", P(
        "La <b>genètica de poblacions</b> estudia l’evolució en termes de gens. El conjunt de tots els al·lels de tots els individus d’una població és el seu <b>fons genètic</b> (o <i>pool</i> gènic). "
        "Per a un gen amb dos al·lels, <i>A</i> i <i>a</i>, la <b>freqüència al·lèlica</b> de cada al·lel és la fracció que representa sobre el total de còpies d’aquell gen a la població. "
        "Exemple: en una població de 100 individus diploides hi ha 200 còpies del gen. Si hi ha 36 <i>AA</i>, 48 <i>Aa</i> i 16 <i>aa</i>, el nombre d’al·lels <i>A</i> és 2 × 36 + 48 = 120, "
        "i la freqüència de <i>A</i> és 120/200 = 0,6; la de <i>a</i>, 80/200 = 0,4. Des d’aquest punt de vista, <b>evolucionar</b> vol dir que les freqüències al·lèliques canvien d’una generació a la següent.")),
    ("ins", "809", P(
        "L’<b>especiació</b> és la formació d’espècies noves a partir d’una d’existent. Perquè una població es converteixi en una espècie diferent, ha de deixar d’intercanviar gens amb la resta: "
        "ha de quedar <b>aïllada reproductivament</b>. Mentre hi ha intercanvi de gens, les diferències que apareixen en una part de la població es barregen amb la resta i no s’acumulen.")),
]

# =====================================================================================
# TEMA 7 · MICROBIOLOGIA
# =====================================================================================
D += [
    ("ins", "864", P(
        "Els <b>microorganismes</b> són els éssers vius que, per la seva mida, només es poden veure amb microscopi. No formen un grup natural: hi ha procariotes (<b>bacteris</b> i <b>arqueus</b>) "
        "i eucariotes (<b>protists</b> com les amebes o les algues unicel·lulars, i <b>fongs</b> microscòpics com els llevats i les floridures). La microbiologia també estudia uns agents que no són cèl·lules "
        "i que, per tant, no es consideren éssers vius en sentit estricte: els <b>virus</b>, els <b>viroides</b> i els <b>prions</b> (apartats 7.6 i 7.7). "
        "Els microorganismes són a tot arreu, la immensa majoria són inofensius o beneficiosos, i són imprescindibles per als cicles de la matèria.")),
    ("ins", "883", P(
        "Per estudiar un bacteri cal fer-lo créixer al laboratori. Un <b>medi de cultiu</b> és una barreja de nutrients (font de carboni, de nitrogen, sals, vitamines) en aigua; si s’hi afegeix agar, "
        "un polisacàrid d’alga, queda sòlid com una gelatina. Sembrat en un medi sòlid, cada bacteri es divideix per bipartició i al cap d’unes hores forma un munt visible de milions de cèl·lules idèntiques, "
        "una <b>colònia</b>. Treballar en condicions <b>asèptiques</b> (material estèril, prop d’una flama) evita que s’hi contamini cap altre microorganisme.")),
    ("ins", "911", P(
        "Els bacteris es reprodueixen per bipartició, que fa dues cèl·lules idèntiques: no hi ha reproducció sexual ni meiosi. Tot i així, poden adquirir gens nous d’altres bacteris, fins i tot d’espècies diferents. "
        "Aquest pas de DNA entre cèl·lules que no són mare i filla s’anomena <b>transferència horitzontal</b> (la vertical és la de mare a filla) i és una font important de variació, per exemple de resistències a antibiòtics.")),
    ("ins", "912", P(
        "Un <b>antibiòtic</b> és una substància, produïda originalment per un microorganisme (la penicil·lina, pel fong <i>Penicillium</i>) o obtinguda per síntesi, que mata els bacteris (<b>bactericida</b>) "
        "o n’atura el creixement (<b>bacteriostàtic</b>) sense fer gaire mal a les cèl·lules de l’hoste. Això és possible perquè ataca estructures que els bacteris tenen i les nostres cèl·lules no, o que són diferents. "
        "Els antibiòtics no fan res contra els virus, que no tenen aquestes estructures.")),
    ("ins", "923", P(
        "Un virus no pot fer res fora d’una cèl·lula. Per multiplicar-se, ha d’entrar en una cèl·lula hoste i fer servir els seus ribosomes, enzims i energia per copiar el seu genoma i fabricar les seves proteïnes. "
        "El conjunt d’etapes d’aquesta multiplicació és el <b>cicle víric</b>. L’exemple clàssic són els <b>bacteriòfags</b> (o fags), virus que infecten bacteris.")),
]

# =====================================================================================
# TEMA 8 · IMMUNOLOGIA
# =====================================================================================
D += [
    ("ins", "983", P(
        "Contínuament entren al nostre cos microorganismes i partícules estranyes. La majoria són inofensius, però alguns, els <b>patògens</b> (bacteris, virus, fongs, protozous i cucs paràsits), causen malalties. "
        "El <b>sistema immunitari</b> és el conjunt d’òrgans, cèl·lules i molècules que ens en defensen. S’organitza en tres línies successives: "
        "(1) les <b>barreres</b> externes, que impedeixen l’entrada; (2) la <b>resposta innata</b>, ràpida i igual davant de qualsevol invasor; i (3) la <b>resposta específica</b> o adaptativa, "
        "més lenta la primera vegada però dirigida contra cada patogen concret, i amb memòria.")),
    ("ins", "983", P(
        "Les cèl·lules del sistema immunitari són els <b>leucòcits</b> o glòbuls blancs. Totes es formen a la medul·la òssia a partir de cèl·lules mare i circulen per la sang i la limfa, "
        "però moltes passen als teixits on hi ha una infecció. Es distingeixen pel que fan: uns <b>fagociten</b> (s’engoleixen i digereixen el que és estrany), d’altres alliberen substàncies que provoquen inflamació, "
        "i els <b>limfòcits</b> reconeixen molècules concretes i són els responsables de la resposta específica.")),
    ("ins", "1004", P(
        "La resposta específica la fan dos tipus de limfòcits. Els <b>limfòcits B</b> maduren a la medul·la òssia (<i>bone marrow</i>) i, quan s’activen, fabriquen anticossos. "
        "Els <b>limfòcits T</b> maduren al tim; no fabriquen anticossos, sinó que coordinen la resposta (T col·laboradors) o maten cèl·lules infectades (T citotòxics). "
        "Cada limfòcit porta a la membrana milers de còpies d’un <b>receptor</b> que reconeix un sol epítop. Els B reconeixen l’antigen sencer, tal com és; els T, en canvi, només el reconeixen "
        "trossejat i mostrat per una altra cèl·lula, que és el que s’explica a continuació.")),
    ("after", "1020", P(
        "La primera vegada que el cos troba un antigen es produeix una <b>resposta primària</b>: cal trobar el clon de limfòcits que el reconeix i fer-lo proliferar, i els anticossos (sobretot IgM) "
        "tarden uns dies a aparèixer i n’hi ha pocs. Aquesta resposta deixa <b>cèl·lules de memòria</b>, que són més abundants i s’activen més de pressa que els limfòcits originals. "
        "Si el mateix antigen torna a entrar, es produeix una <b>resposta secundària</b>: comença abans, arriba a una concentració d’anticossos molt més alta, dura més i és sobretot d’IgG. "
        "Sovint elimina el patogen abans que aparegui la malaltia: això és ser immune, i és el que aprofiten les vacunes.")),
]

# =====================================================================================
# TEMA 9 · DISSENY EXPERIMENTAL
# =====================================================================================
D += [
    ("ins", "1097", P(
        "La ciència avança fent preguntes que es poden respondre amb dades. El <b>mètode científic</b> no és una recepta rígida, però sol seguir uns passos: "
        "(1) una <b>observació</b> planteja un <b>problema</b> («per què aquest enzim deixa de funcionar quan s’escalfa?»); (2) es proposa una <b>hipòtesi</b> que l’expliqui; "
        "(3) se’n dedueix una <b>predicció</b>, el que hauria de passar en un experiment si la hipòtesi és certa; (4) es dissenya i es fa l’<b>experiment</b>; "
        "(5) s’analitzen els <b>resultats</b> i (6) se’n treu una <b>conclusió</b>: la hipòtesi queda reforçada o queda refutada. Les preguntes de disseny experimental de la PAU demanen alguna d’aquestes peces.")),
    ("ins", "1106", P(
        "Un exemple ajuda a fixar els termes. Es vol saber si el pH afecta la velocitat de la catalasa, l’enzim que descompon l’aigua oxigenada en aigua i oxigen. Es preparen tubs iguals, amb la mateixa quantitat "
        "d’enzim i d’aigua oxigenada, a la mateixa temperatura, i cada tub es posa a un pH diferent (4, 5, 6, 7, 8, 9). A cada tub es mesura el volum d’oxigen alliberat en dos minuts. "
        "El pH és el que es canvia; el volum d’oxigen és el que es mesura; la quantitat d’enzim, la d’aigua oxigenada i la temperatura es mantenen iguals.")),
]
