"""Correccions de la revisió (rigor, concreció i format) sobre el text extret del dossier de teoria.

Cada entrada fa referència a un element per camí (índex de primer nivell i, dins dels requadres,
índex del fill: «19.1»). Tipus:
  ("sub", camí, vell, nou)   substitueix un fragment (ha d'existir: si no, error)
  ("set", camí, html)        reescriu l'element
  ("del", camí)              l'esborra (repeticions o contingut erroni)
  ("ins", camí, element)     insereix un element nou abans del camí
"""

# Correccions globals (expressions regulars) aplicades a tot el text
GLOBAL = [
    (r"(?<=[\wαβ′\)])- (?=[a-zà-úA-Z])", "-"),  # guionets partits pel salt de línia del PDF
    (r"\bdóna\b", "dona"), (r"\bDóna\b", "Dona"),
    (r"\bglucogen fosforilasa\b", "glicogen fosforilasa"),
    (r"\bEs escriu\b", "S’escriu"),
    (r"(?<=\d)– (?=\d)", "–"),
    (r"\bpatògen(s?)\b", r"patogen\1"),
    (r"PrPSc", "PrP<sup>Sc</sup>"),
    (r"\b[Uu]na enzima\b", "un enzim"),
]

C = []

# ---------- 1. Biomolècules ----------
C += [
    ("sub", "10", "L’aigua també és reactiu:", "L’aigua també és un reactiu:"),
    ("sub", "12", "i són cofactors (Mg²⁺ de la clorofil·la i de molts enzims, Fe²⁺ de l’hemoglobina i dels citocroms, Zn²⁺ d’algunes polimerases)",
     "i són cofactors (Mg²⁺ de molts enzims, el ferro de l’hemoglobina i dels citocroms, Zn²⁺ d’algunes polimerases); el Mg²⁺ és, a més, l’ió central de la clorofil·la"),
    ("sub", "17", "Les sals dissoltes són ions. No tenen calories: no es poden oxidar per fer ATP.", "Les sals dissoltes són ions i no aporten energia: no es poden oxidar per fer ATP."),
    ("sub", "17", "El Mg²⁺ entra a la clorofil·la i al complex de l’ATP amb l’enzim. El Fe²⁺ és al grup hemo i als centres ferro-sofre de la cadena.",
     "El Mg²⁺ és a la clorofil·la i forma el complex Mg-ATP, que és la forma d’ATP que fan servir els enzims. El ferro és al grup hemo i als centres ferro-sofre de la cadena respiratòria."),
    ("sub", "26", "El carboni que era el carbonil passa a ser el carboni anomèric, el C1.",
     "El carboni que era el carbonil passa a ser el carboni anomèric (el C1 a les aldoses com la glucosa; el C2 a la fructosa)."),
    ("sub", "33", "acetilglucosamina amb enllaços β.", "acetilglucosamina amb enllaços β(1→4)."),
    ("sub", "35", "estructural (cel·lulosa, quitina, ribosa dins l’RNA) i de reconeixement (oligosacàrids del glicocàlix). Els glúcids no són el material genètic.",
     "estructural (cel·lulosa, quitina) i de reconeixement (oligosacàrids del glicocàlix). La ribosa i la desoxiribosa formen part dels nucleòtids, però el material genètic és l’àcid nucleic, no el glúcid."),
    ("set", "36.1", "A és un glúcid (cel·lulosa): estructural, no de reserva. B és un lípid saponificable (triacilglicerol): és la reserva energètica principal dels animals, als adipòcits. C és un pròtid (pèptid o proteïna). La de reserva en animals és, per tant, la B; l’altra reserva animal, el glicogen, no és a la llista."),
    ("del", "39"),  # repeteix el paràgraf 28 i la taula 42
    ("del", "40"),  # repeteix el 45 i el 51
    ("sub", "42", "N- acetilglucosamina | β", "N-acetilglucosamina | β(1→4)"),
    ("sub", "46.1", "que és el que necessita el múscul. La planta no té tanta pressa i l’amilopectina en porta menys.",
     "que és el que necessita el múscul (i també una síntesi més ràpida). En el midó la mobilització no ha de ser tan ràpida i l’amilopectina té menys ramificacions (una cada 24–30 glucoses, davant d’una cada 8–12 al glicogen)."),
    ("sub", "55", "es guarda en vacúols o en el teixit adipós", "es guarda en gotes lipídiques del citoplasma (als adipòcits del teixit adipós i a moltes llavors)"),
    ("sub", "65.1", "reté uns dos grams d’aigua per gram de polisacàrid", "reté unes tres vegades el seu pes en aigua"),
    ("sub", "89", "queda forta unida", "queda fortament unida"),
    ("del", "93"),  # repetit al 97
    ("del", "94"),  # repetit al 100
    ("del", "99"),  # el 104 és el mateix amb més dades
    ("sub", "107", "Les bases hidròfobes queden a l’interior", "Les bases, planes i poc polars, queden a l’interior"),
    ("del", "113"),  # repeteix el 106
    ("del", "116"),  # mateix exercici que el 111
]

# ---------- 2. La cèl·lula ----------
C += [
    ("sub", "166", "Les mostres d’electrons van fixades", "Les mostres per al microscopi electrònic van fixades"),
    ("set", "167.1", "Amb la barra d’escala: 8 mm ÷ (5 mm/µm) = 1,6 µm. Si en lloc de l’escala l’enunciat dona els augments (per exemple ×4 000), la mida real és la mida a la foto dividida pels augments: 8 mm / 4 000 = 0,002 mm = 2 µm. Unitats: 1 mm = 10³ µm = 10⁶ nm."),
    ("del", "168"), ("del", "169"),  # repeteixen el 165 i el 166
    ("sub", "176", "Poden tenir càpsula, fímbries, pilus i flagel de tubulina diferent de l’eucariota.",
     "Poden tenir càpsula, fímbries, pilus i flagel; el flagel bacterià és de flagel·lina i gira com una hèlix, i no té res a veure amb el flagel eucariota, fet de microtúbuls."),
    ("del", "182"),  # el 184 diu el mateix
    ("sub", "187.1", "El efecte útil és sobre el bacteri; el efecte tòxic", "L’efecte útil és sobre el bacteri; l’efecte tòxic"),
    ("set", "188.1", "Ribosoma 80S (uns 25–30 nm), virus típic (de 20 a 300 nm; molts, al voltant de 100 nm), bacteri (1–5 µm), mitocondri (0,5–1 µm d’amplada i 1–3 µm de llarg; de l’ordre d’un bacteri petit), cèl·lula animal (10–30 µm). Amb l’òptic es veuen la cèl·lula, el bacteri i, al límit, el mitocondri com un grànul o un bastonet. El ribosoma i el virus, no."),
    ("sub", "188.0", "Ordeneu de petit a gran, amb un motiu: ribosoma 80S, virus típic, bacteri, mitocondri, cèl·lula animal.", "Ordeneu de petit a gran: ribosoma 80S, virus típic, bacteri, mitocondri, cèl·lula animal."),
    ("sub", "189.1", "«Bacteri» per a tot el que no té nucli és l’error que les orientacions volen evitar.", "Dir «bacteri» de tot el que no té nucli és un error."),
    ("del", "194"),  # repeteix el 191 i el 192
    ("sub", "200.1", "La asimetria", "L’asimetria"),
    ("sub", "202", "i, poc, l’aigua.", "i, poc, l’aigua, que passa sobretot per canals específics (aquaporines)."),
    ("del", "212"),  # repeteix el 206
    ("del", "216"),  # repeteix el 209
    ("sub", "217.1", "Al glòbul vermell hi ha més glucosa fora que dins just després d’un àpat, i GLUT és difusió facilitada.",
     "Al glòbul vermell la glucosa és més concentrada al plasma que a dins (la cèl·lula la consumeix tot seguit), i GLUT és difusió facilitada."),
    ("sub", "223", "La externa és permeable", "L’externa és permeable"),
    ("del", "233"),  # el 236 diu el mateix
    ("sub", "238", "El cloroplast en té tres espais: entre les dues membranes de l’embolcall, l’estroma, i el lumen del tilacoide.",
     "El cloroplast té tres compartiments: l’espai entre les dues membranes de l’embolcall, l’estroma i el lumen del tilacoide."),
    ("set", "249", "La interfase no és un descans: és G1, S i G2. A G1 la cèl·lula creix i fa la seva funció; si és diploide, el contingut de DNA és 2C (C és el contingut d’un joc haploide de cromosomes). A S es replica tot el genoma i el contingut passa a 4C. A G2 cada cromosoma ja té dues cromàtides, encara descondensades, i la cèl·lula comprova que la replicació s’ha acabat abans d’entrar a la mitosi. Un cromosoma amb dues cromàtides es compta com un sol cromosoma fins que les cromàtides se separen a l’anafase."),
    ("del", "250"),  # repeteix el 247
    ("sub", "254.0", "l’ensamblatge del fus", "el muntatge del fus"),
    ("del", "261"),  # repeteix el 258 i la taula 262
    ("sub", "264", "La mitosi conserva n.", "La mitosi conserva el nombre de cromosomes."),
    ("sub", "272", "En la espermatogènesi", "En l’espermatogènesi"),
    ("del", "275"),  # la mateixa taula que la 279
    ("sub", "284", "En humans, 2²³, més d’un milió,", "En humans, 2²³, més de 8 milions,"),
    ("sub", "288.1", "fa aparèixer els recombinants en una proporció igual a la distància.", "fa aparèixer els recombinants en una proporció que és la freqüència de recombinació (en cM, la distància entre els dos gens)."),
    ("sub", "289.1", "Una fase S hi tornaria a duplicar el DNA i els gàmetes no serien haploides en contingut, o el nombre es desquadraria.",
     "Una fase S hi tornaria a duplicar el DNA: cada gàmeta tindria n cromosomes però de dues cromàtides (2C), i no es reduiria el contingut de DNA."),
    ("del", "290"),  # repeteix el 282
]

# ---------- 3. Metabolisme ----------
C += [
    ("del", "335"),  # repeteix el 331 i el 334
    ("del", "340"),  # repeteix el 338
    ("del", "346"), ("del", "349"), ("del", "355"),  # glucòlisi explicada tres vegades
    ("sub", "354.0", "El resta de la via", "La resta de la via"),
    ("sub", "362", "el total és d’uns 30–32 ATP per", "el total és d’uns 30–32 ATP per glucosa."),
    ("del", "363"),  # final del peu de la figura, partit al PDF
    ("del", "367"), ("del", "368"),  # repeteixen el 358-364
    ("sub", "371.0", "ha de entrar", "ha d’entrar"),
    ("sub", "380.0", "El 2,5 i el 1,5", "El 2,5 i l’1,5"),
    ("sub", "380.0", "La c-subunitat de l’ATP- sintasa humana en té 8,", "L’anell c de l’ATP-sintasa dels mamífers té 8 subunitats,"),
    ("del", "381"),  # repeteix el 370
    ("del", "382"), ("del", "383"),  # repeteixen el 374-379
    ("del", "387"),  # repeteix el 379 i el 393
    ("del", "389"), ("del", "391"), ("del", "392"),  # el balanç ja és al requadre 379 i a la taula 384
    ("sub", "393.1", "i es bomba menys protons", "i es bombegen menys protons"),
    ("sub", "396", "A la fermentació làctica, el piruvat s’oxida? No: es redueix a lactat i el NADH passa a NAD⁺.", "A la fermentació làctica el piruvat es redueix a lactat i el NADH passa a NAD⁺."),
    ("del", "402"),  # repeteix el 395-398
    ("sub", "405.1", "Per això el lactat és un deute temporal d’oxigen, no un producte final com l’etanol del llevat, que el llevat excreta.",
     "Per això el lactat no és un producte final com l’etanol que excreta el llevat: és un intermedi que el fetge recicla."),
    ("del", "412"),  # repeteix el 409-411 (els cossos cetònics són al 416)
    ("sub", "414.1", "Per això el greix no torna a sucre, i el sucre sí que pot anar a greix.",
     "Per això els àcids grassos no tornen a sucre, i el sucre sí que pot anar a greix. (El glicerol dels triacilglicerols sí que pot fer glucosa al fetge, però és una part petita de la molècula.)"),
    ("sub", "418", "No fixa CO_2. Tres processos, i només això:", "No fixa CO<sub>2</sub>. Els processos que cal saber situar són aquests:"),
    ("del", "423"), ("del", "427"),  # repeteixen el 421
    ("sub", "435", "Una part del sucre surt del cicle; la resta, amb més ATP, regenera la RuBP.",
     "Una part de les trioses surt del cicle cap a midó (a l’estroma) o cap a sacarosa (al citosol); la resta, amb més ATP, regenera la RuBP."),
    ("del", "441"), ("del", "442"), ("del", "443"),  # repeteixen el 433-437
    ("sub", "444", "No és matèria nuclear de la prova, però si un enunciat en parla, la idea és aquesta: no és una fotosíntesi sense llum.", "No és matèria central de la prova; si un enunciat en parla, n’hi ha prou amb aquesta idea."),
    ("sub", "444", "a les cèl·lules de la beina", "a les cèl·lules de la beina del feix vascular"),
    ("del", "445"),  # mateix exercici que el 438
    ("del", "449"),  # repeteix el 435 i el 448
    ("del", "455"), ("del", "456"),  # repeteixen el 452 i el 453
    ("set", "462", "En un esquema general del metabolisme heu de saber assenyalar: la glucòlisi al citosol; el piruvat cap a acetil-CoA o cap a fermentació; l’acetil-CoA cap al Krebs o, en sentit biosintètic, cap a àcids grassos; el Krebs i la cadena al mitocondri; la β-oxidació abocant acetil-CoA; la fotosíntesi i la quimiosíntesi com a entrades de matèria inorgànica, i els aminoàcids entre el Krebs i les proteïnes. La fletxa «proteïnes» és la traducció (tema 5)."),
]

# ---------- 4. Genètica mendeliana ----------
C += [
    ("del", "502"), ("del", "503"),  # repeteixen el 499 i el 500
    ("del", "514"),  # repeteix el 509
    ("sub", "521", "i per damunt del 50 % els gens es comporten com si no estiguessin lligats.", "i amb un 50 % (el màxim que es pot observar) els gens es comporten com si no estiguessin lligats."),
    ("del", "524"),  # repeteix la idea clau 523
    ("del", "526"), ("del", "527"),  # repeteixen el 520 i el 521
    ("sub", "528.1", "Els parentals són gairebé deu vegades els recombinants.", "Els parentals són vuit vegades els recombinants."),
    ("set", "531.1", "Perquè les distàncies llargues no es mesuren directament: es construeixen sumant trams curts. Si A–C fa 30 cM i C–B 35 cM, A i B són al mateix cromosoma, a uns 65 cM de mapa, encara que entre ells la freqüència de recombinació observada no passi del 50 % i no es distingeixin de gens independents."),
    ("del", "539"),  # el 547 és el mateix problema, més complet
    ("del", "540"),  # mateix problema que el 543
    ("del", "541"),  # repeteix el 535 i el 536
    ("sub", "549", "Una persona que ja no hi és es ratlla. Llegir-ne el patró:", "Una persona morta es marca amb una barra diagonal. Com es llegeix el patró:"),
    ("del", "555"),  # repeteix el 550
    ("set", "556", "«Com a mínim un» es calcula més de pressa com 1 menys la probabilitat de «cap»."),
    ("del", "559"),  # mateix càlcul que el 553
    ("del", "565"),  # repeteix el 563
    ("sub", "567.1", "El fill és AA, AB o BB, és a dir A, AB o B, amb probabilitats ¼, ½ i ¼.", "El fill és IᴬIᴬ, IᴬIᴮ o IᴮIᴮ, és a dir del grup A, AB o B, amb probabilitats ¼, ½ i ¼."),
    ("sub", "568.1", "El que no s’hereta és un sol gen amb dominància completa.", "El que no hi ha és un sol gen amb dominància completa."),
    ("sub", "572.1", "fills homes 1/2 afectats; filles sanes", "fills homes 1/2 afectats; filles sanes (1/2 portadores)"),
    ("sub", "588", "Creuament amb", "Encreuament amb"),
]

# ---------- 5. Genètica molecular i biotecnologia ----------
C += [
    ("sub", "610", "Hi ha altres RNA (el de l’operó no es tradueix sencer; microRNA reguladors)", "Hi ha altres RNA (per exemple, els microRNA reguladors)"),
    ("del", "615"), ("del", "616"),  # repeteixen el 606-609
    ("sub", "622", "amb una sola origen", "amb un sol origen de replicació"),
    ("sub", "623", "la polimerasa va a batzegades, lluny de la forquilla,", "la polimerasa treballa a trossos, en sentit contrari a l’avanç de la forquilla,"),
    ("sub", "625", "hi ha moltes origens", "hi ha molts orígens"),
    ("sub", "625", "El principi — semiconservatiu", "El principi —semiconservatiu"),
    ("sub", "627", "Origens", "Orígens"),
    ("del", "629"), ("del", "630"),  # repeteixen el 622-625
    ("del", "631"),  # repeteix el 628
    ("sub", "637", "cua de poli-A a l’3′", "cua de poli-A a l’extrem 3′"),
    ("set", "640.0", "Motlle de DNA: 3′–TAC TTT GGG ATC–5′. Escriviu la cadena codificant, l’RNAm i els aminoàcids (AUG és Met, AAA és Lys, CCC és Pro i UAG és parada)."),
    ("set", "640.1", "Codificant: 5′–ATG AAA CCC TAG–3′. RNAm: 5′–AUG AAA CCC UAG–3′. Pèptid: Met–Lys–Pro; UAG atura la traducció i no codifica cap aminoàcid."),
    ("set", "645.0", "Motlle 3′–TAC GGA TTA ACT–5′. Escriviu l’RNAm i el pèptid, i digueu on comença i on s’atura la traducció (AUG és Met i inici, CCU és Pro, AAU és Asn, UGA és parada)."),
    ("set", "645.1", "RNAm 5′–AUG CCU AAU UGA–3′. Comença a l’AUG (Met) i s’atura a l’UGA, que no es tradueix. Pèptid: Met–Pro–Asn. El motlle començava per TAC, que és el complement de l’AUG: no cal buscar un altre marc."),
    ("del", "646"), ("del", "647"),  # repeteixen el 636-639
    ("set", "650.0", "Motlle 3′–TAC GGT ATT–5′. Escriviu l’RNAm 5′→3′ i el pèptid (AUG és Met, CCA és Pro i UAA és parada)."),
    ("set", "650.1", "RNAm 5′–AUG CCA UAA–3′. AUG és l’inici (Met), CCA és Pro i UAA és parada, que no es tradueix. El pèptid és Met–Pro. Cal llegir el motlle de 3′ a 5′ i escriure el complement amb U en lloc de T, no copiar-lo tal qual."),
    ("del", "659"),  # repeteix el 655 i el 658
    ("sub", "668", "L’splicing alternatiu, al tema 6, afegeix diversitat sense gens nous.", "L’splicing alternatiu (apartat 5.3) afegeix diversitat de proteïnes sense gens nous."),
    ("del", "669"), ("del", "670"),  # repeteixen el 666-668
    ("del", "678"), ("del", "679"),  # repeteixen el 676 i el 677
    ("sub", "680.1", "La segona és disbarat:", "La segona és una mutació sense sentit:"),
    ("set", "682.0", "Es delecionen dues bases al mig d’un exó. Més endavant, una inserció de dues bases restaura en part la funció, i una inserció d’una sola base no. Per què?"),
    ("set", "682.1", "La deleció de 2 bases desplaça el marc. Una inserció posterior d’1 base deixa un canvi net de −1: el marc continua desplaçat fins al final. Una inserció de 2 bases deixa un canvi net de 0 (múltiple de 3) i, a partir d’aquell punt, el marc es recupera. Només queda alterat el tram entre les dues mutacions; per això la funció es recupera en part. El que compta és el canvi net en mòdul 3."),
    ("del", "689"),  # repeteix el 686 i el 687
    ("del", "692"),  # repeteix el 690
    ("del", "701"), ("del", "702"), ("del", "703"),  # repeteixen el 695-700
    ("sub", "706.1", "encara que l’hibridació sigui bona", "encara que la hibridació sigui bona"),
    ("del", "713"),  # repeteix el 711
    ("sub", "714.1", "El bacteri que porta el gen humà és un organisme modificat, transgènic en el sentit ampli.", "El bacteri que porta el gen humà és transgènic: porta un gen d’una altra espècie."),
    ("del", "716"),  # mateix cas que el 714
]

# ---------- 6. Evolució ----------
C += [
    ("del", "761"), ("del", "762"),  # repeteixen el 756-760
    ("sub", "765.1", "L’ala del ratpenat és homòloga de la mà humana:", "L’ala del ratpenat és homòloga de l’extremitat anterior humana (braç i mà):"),
    ("del", "777"),  # repeteix el 774
    ("del", "779"),  # mateix raonament que el 775
    ("sub", "781", "Si se’n trenca alguna, hi ha evolució en aquell locus: canvi de p o de q.",
     "Si se’n trenca alguna, hi pot haver evolució en aquell locus: canvi de p o de q. Per això l’equilibri serveix d’hipòtesi nul·la: si les freqüències observades no hi encaixen, alguna condició falla, i aquella condició és una força evolutiva."),
    ("del", "788"), ("del", "790"),  # repeteixen el 781 i el 787
    ("set", "799", "Segons l’abast, una mutació pot ser: <b>nucleotídica</b> (gènica o puntual), que canvia una o poques bases (silenciosa, de canvi de sentit o sense sentit; una inserció o una deleció que no sigui múltiple de tres desplaça el marc); <b>cromosòmica</b> o estructural, que canvia l’estructura d’un cromosoma (deleció, duplicació, inversió o translocació d’un fragment; si el fragment és gran, es veu al cariotip); o <b>cariotípica</b> (genòmica o numèrica), que canvia el nombre de cromosomes: aneuploïdies com la trisomia 21 o poliploïdies (jocs sencers de més). Les causes són errades de la replicació no reparades, errades de la meiosi (no-disjunció), elements transposables, alguns virus i els agents mutàgens (radiacions ionitzants i ultraviolades, i algunes substàncies químiques)."),
    ("del", "803"),  # el 807 diu el mateix
    ("del", "806"),  # repeteix el 802
    ("del", "812"), ("del", "813"),  # repeteixen el 809 i el 810
    ("sub", "816.1", "és el mateix tipus de dada que el mul", "és el mateix tipus de dada que la de la mula"),
    ("sub", "820", "Els cianobacteris són el parent dels cloroplasts; un bacteri respirador, el dels mitocondris.", "Un cianobacteri és l’origen dels cloroplasts; un bacteri aerobi (un alfaproteobacteri), el dels mitocondris."),
    ("sub", "821", "El splicing alternatiu", "L’splicing alternatiu"),
    ("del", "826"),  # repeteix el 824
    ("sub", "851.0", "els portadors són unes vint vegades més nombrosos que els afectats", "els portadors són unes 40 vegades més nombrosos que els afectats"),
]

# ---------- 7. Microbiologia ----------
C += [
    ("del", "868"), ("del", "869"),  # la taula 872 ja ho compara
    ("del", "871"),  # repeteix el 864 (la penicil·lina és al 874)
    ("del", "875"),  # repeteix el 874
    ("sub", "880", "El cristall violeta i el lugol tenyeixen de lila. L’alcohol deshidrata.", "El cristall violeta tenyeix de lila i el lugol (mordent) el fixa. Després, l’alcohol decolora."),
    ("del", "881"), ("del", "882"),  # repeteixen el 880 i el 883
    ("del", "893"),
    ("del", "894"),  # repeteix el 889 i el 892
    ("sub", "898.1", "La fixació continua essent l’única entrada natural des de l’atmosfera.", "La fixació biològica és la principal entrada natural de nitrogen des de l’atmosfera (els llamps en fixen una part petita)."),
    ("sub", "902", "L’endèmia es manté de manera estable en una zona.", "L’endèmia es manté de manera estable en una zona. Un patogen oportunista només causa malaltia si les defenses o la microbiota fallen."),
    ("del", "904"), ("del", "905"),  # repeteixen el 901-903
    ("del", "908"),  # repeteix el 906
    ("del", "914"),  # repeteix el 911
    ("sub", "915", "No crear l’antibiòtic amb l’ús incorrecte: seleccionar-lo.", "L’ús incorrecte de l’antibiòtic no crea la resistència: la selecciona."),
    ("del", "916"), ("del", "918"),  # mateix cas que el 913
    ("sub", "917.1", "lisia la cèl·lula", "lisa la cèl·lula"),
    ("del", "928"), ("del", "929"), ("del", "930"),  # repeteixen el 921-925
    ("sub", "931.0", "Un cultiu bacterià es lisi", "Un cultiu bacterià es lisa"),
    ("del", "935"),  # repeteix la taula 927
    ("del", "941"),  # repeteix el 938 i el 939
    ("del", "946"),  # repeteix el 944
]

# ---------- 8. Immunologia ----------
C += [
    ("del", "985"),  # repeteix el 983 i el 984
    ("del", "996"),  # repeteix el 991, el 992 i el 1000
    ("del", "1011"),  # repeteix el 1006 i la taula 1008
    ("del", "1014"),  # repeteix el 1012
    ("del", "1023"), ("del", "1024"),  # repeteixen el 1018-1022
    ("sub", "1032", "o, en vacunes recents, l’RNA que fa fabricar la proteïna.", "o, en vacunes recents, un RNA missatger (o un vector víric) que fa fabricar la proteïna antigènica a les cèl·lules de la persona vacunada."),
    ("sub", "1034.0", "Activeu o passiva?", "Activa o passiva?"),
    ("del", "1035"), ("del", "1036"), ("del", "1037"),  # repeteixen el 1030-1033
    ("del", "1041"),  # repeteix el 1038
    ("sub", "1046", "Les leucèmies són càncers dels leucòcits.", "Les leucèmies són càncers de les cèl·lules que formen els leucòcits, a la medul·la òssia."),
    ("del", "1047"), ("del", "1048"),  # repeteixen el 1044-1046
    ("del", "1051"),  # repeteix el 1049
    ("set", "1054", "Les orientacions en demanen tres fases. La <b>incubació</b>: el patogen ja hi és i es multiplica, i encara no hi ha símptomes; sovint ja es pot transmetre. La <b>manifestació clínica</b>: apareixen els símptomes (alguns textos la divideixen en un període prodròmic, amb símptomes generals i inespecífics, i un període d’estat, amb el quadre propi de la malaltia). La <b>convalescència</b>: els símptomes cedeixen i els teixits es recuperen. Si la resposta específica ha deixat memòria, queda immunitat, però no totes les infeccions immunitzen de per vida."),
    ("del", "1056"),  # integrat al 1054
    ("del", "1060"),  # repeteix el 1058
]

# ---------- 9. Disseny experimental ----------
C += [
    ("del", "1100"),  # repeteix el 1097
    ("del", "1103"),  # mateix exercici que el 1101
    ("del", "1104"),  # repeteix el 1102
    ("del", "1109"),  # el 1111 diu el mateix, millor
    ("sub", "1119", "Exemples que ja han sortit al dossier i que tornen:", "Exemples típics:"),
    ("del", "1122"),  # repeteix el 1098
    ("del", "1125"),  # repeteix el 1129
    ("sub", "1130.1", "Extrapol·lar", "Extrapolar"),
]

# ---------- Figures: totes refetes (vegeu figures.py) ----------
def _f(key):
    return {"t": "fig", "key": key}

F = [
    ("rep", "9", _f("aigua")), ("rep", "27", _f("anomers")), ("del", "29"), ("del", "30"), ("del", "31"), ("rep", "32", _f("disacarids")),
    ("rep", "57", _f("lipids")), ("rep", "71", _f("aminoacid")), ("rep", "74", _f("proteina")), ("rep", "108", _f("nucleotid")),
    ("rep", "110", _f("dna_quimica")), ("rep", "124", _f("map1")),
    ("after", "88", _f("vs")),
    ("rep", "156", _f("vs_aut")), ("del", "157"), ("del", "158"), ("del", "159"),
    ("rep", "178", _f("pro_euc")), ("rep", "193", _f("membrana")), ("rep", "204", _f("bomba")), ("rep", "207", _f("osmosi")), ("del", "208"),
    ("rep", "221", _f("nucli")), ("rep", "224", _f("mitocondri")), ("rep", "225", _f("cloroplast")), ("rep", "227", _f("animal")), ("rep", "228", _f("vegetal")),
    ("after", "246", _f("cicle")),
    ("rep", "259", _f("mitosi")), ("rep", "273", _f("meiosi")), ("del", "274"), ("rep", "293", _f("map2")),
    ("rep", "332", _f("atp")), ("rep", "333", _f("cat_anab")), ("rep", "347", _f("glucolisi")), ("rep", "362", _f("respiracio")), ("rep", "365", _f("krebs")),
    ("rep", "377", _f("cadena")), ("del", "397"), ("rep", "399", _f("fermentacions")), ("rep", "432", _f("fase_lluminosa")), ("rep", "434", _f("zeta")),
    ("rep", "436", _f("calvin")), ("del", "454"), ("after", "462", _f("map3")),
    ("rep", "510", _f("punnett_mono")), ("after", "520", _f("punnett_di")), ("after", "521", _f("lligament")), ("rep", "537", _f("punnett_x")),
    ("rep", "551", _f("pedigri")), ("del", "564"), ("after", "571", _f("map4")),
    ("rep", "607", _f("dogma")), ("rep", "611", _f("trna")), ("rep", "612", _f("transcripcio")), ("rep", "624", _f("forquilla")), ("del", "638"),
    ("rep", "657", _f("traduccio")), ("after", "667", _f("operon")), ("rep", "688", _f("recombinant")), ("rep", "696", _f("pcr")), ("rep", "698", _f("crispr")),
    ("after", "719", _f("map5")),
    ("rep", "757", _f("homologia")), ("rep", "770", _f("seleccio")), ("rep", "782", _f("forces")), ("rep", "811", _f("especiacio")), ("after", "829", _f("map6")),
    ("rep", "865", _f("bacteri")), ("after", "880", _f("gram")), ("rep", "891", _f("nitrogen")), ("rep", "922", _f("fag")), ("rep", "924", _f("cicles_virus")),
    ("rep", "937", _f("acel")), ("after", "948", _f("map7")),
    ("rep", "1005", _f("humoral_cel")), ("rep", "1019", _f("anticos")), ("rep", "1021", _f("resposta")), ("rep", "1055", _f("tipus_immunitat")),
    ("after", "1062", _f("map8")),
    ("rep", "1107", _f("disseny")), ("ins", "1131", _f("map9")),
]
