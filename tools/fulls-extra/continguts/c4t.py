"""Activitats afegides als fulls de 4t ESO: més preguntes a les fitxes (continuen la numeració
de la fitxa, no són un full a part). Els dossiers d'ampliació són a d4t.py.
Cada pregunta es pot resoldre amb la informació del full; quan cal una dada que no hi és, la pregunta la dona."""
from estil import renumber, q, h2, table, resources
from .fixes import FIXES_4T as FIXES
from .d4t import DOSSIER


def mes(*qs):
    return renumber("".join(qs))

PHET = "https://phet.colorado.edu/ca/"
BOX = lambda h: f'<div class="box" style="min-height:{h}mm"></div>'

EXTRA = {}

# ================================================================== SdA 1 · Els colors de la Mercè
EXTRA["sda1-03-fitxa-1-models-atomics.pdf"] = mes(
    q(7, "<b>Si Thomson tingués raó…</b> Si l'àtom fos una esfera positiva amb electrons incrustats, què hauria passat amb les partícules alfa que llançava l'equip de Rutherford? Què van observar que ho desmentia? Fes-ne un dibuix.", 3, BOX(26)),
    q(8, "<b>Les mides.</b> Un àtom fa uns 1 · 10⁻¹⁰ m i el seu nucli, uns 1 · 10⁻¹⁵ m. Quantes vegades és més gran l'àtom que el nucli? Coincideix amb la dada de la fitxa?", 2),
    q(9, "<b>Vertader o fals?</b> Corregeix les falses. a) Dalton ja sabia que hi havia electrons. b) Segons Rutherford, la major part de l'àtom és buit. c) En el model actual sabem exactament per on passa cada electró. d) Bohr explicava per què cada element emet uns colors concrets.", 4),
)

EXTRA["sda1-04-fitxa-2-ions-i-isotops.pdf"] = mes(
    q(7, "<b>La massa del clor.</b> El clor natural té dos isòtops: ³⁵Cl (34,97 u, 75,8 %) i ³⁷Cl (36,97 u, 24,2 %). Calcula la massa atòmica mitjana. Per què no és un nombre enter?", 3),
    q(8, "<b>Guanyar o perdre.</b> El magnesi forma l'ió Mg²⁺ i l'oxigen, l'ió O²⁻. Quants electrons perd o guanya cada àtom? Quants electrons té cada ió?", 3),
    q(9, "<b>Quin element és?</b> Una partícula té 20 protons, 20 neutrons i 18 electrons. De quin element és? Quin és el seu nombre màssic? És un àtom neutre, un catió o un anió?", 2),
)

EXTRA["sda1-06-fitxa-3-salts-d-electrons.pdf"] = mes(
    q(6, "<b>Ordena per energia.</b> Ordena aquests colors de llum visible de menys a més energia: verd, violeta, vermell, groc, blau.", 1),
    q(7, "<b>Quantes línies?</b> Un àtom té tres nivells, E₁ &lt; E₂ &lt; E₃. Un electró és al nivell 3. Quins salts cap avall pot fer? Quantes línies diferents pot tenir l'espectre? Quin salt fa la llum de més energia?", 3, BOX(22)),
    q(8, "<b>Liti o sodi?</b> El liti fa una flama vermella (línia de 671 nm) i el sodi, groga (589 nm). Quin dels dos salts té més energia? Com ho saps?", 2),
    q(9, "<b>Llum dels estels.</b> Quan la llum blanca d'un estel travessa un gas, el gas absorbeix els mateixos colors que emetria i a l'espectre hi queden ratlles fosques. Com ho va aprofitar Cecilia Payne per saber de què estan fets els estels?", 3),
)

EXTRA["sda1-07-fitxa-4-configuracio-electronica.pdf"] = mes(
    q(5, "<b>Configuracions.</b> Escriu la configuració electrònica i encercla els electrons de valència.") +
    table(["Element", "Z", "Configuració electrònica", "Electrons de valència"], [
        ["Nitrogen", "7", "", ""], ["Magnesi", "12", "", ""], ["Alumini", "13", "", ""], ["Sofre", "16", "", ""], ["Argó", "18", "", ""]],
        empty_cols=(2, 3), widths=["18%", "8%", "52%", "22%"]),
    q(6, "<b>Ions estables.</b> Escriu la configuració del Ca²⁺ i de l'O²⁻. Amb quin gas noble coincideix cadascuna?", 2),
    q(7, "<b>Quin element és?</b> a) 1s² 2s² 2p⁶ 3s² 3p⁶ 4s². b) Té 7 electrons de valència al nivell 3. c) L'últim subnivell és 2p³.", 3),
)

EXTRA["sda1-08-fitxa-5-taula-periodica.pdf"] = mes(
    q(5, "<b>Període i grup.</b> Sense mirar la taula, digues el període, el grup i el bloc dels elements que acaben en: a) 3s¹; b) 2s² 2p⁴; c) 4s² 3d¹⁰ 4p⁶. Quins elements són?", 3),
    q(6, "<b>Quin ió forma?</b> Prediu l'ió que formen el liti, el magnesi, l'alumini, l'oxigen i el clor. Justifica-ho amb els electrons de valència.", 3),
    q(7, "<b>Famílies.</b> El sodi i el potassi reaccionen amb aigua d'una manera semblant. El neó i l'argó gairebé no reaccionen amb res. Explica-ho amb la configuració de l'últim nivell.", 3),
    q(8, "<b>Metall o no metall?</b> Classifica, amb la taula: Ca, S, Fe, Br, K, P, Zn, Ne.", 1),
)

EXTRA["sda1-10-fitxa-6-enllac-i-propietats.pdf"] = mes(
    q(5, "<b>La sal i el corrent.</b> Per què la sal sòlida no condueix el corrent però la sal dissolta o fosa sí? Explica-ho amb els ions.", 3),
    q(6, "<b>Diamant i metà.</b> Tots dos tenen enllaços covalents, però el diamant és el material natural més dur i el metà és un gas. Per què?", 3),
)

EXTRA["sda1-11-fitxa-7-formulacio-binaris.pdf"] = mes(
    q(4, "<b>Anomena</b> (amb prefixos i amb el nombre d'oxidació quan calgui).") +
    table(["Fórmula", "Nom amb prefixos", "Nom amb nombre d'oxidació"], [["Na₂O", "", ""], ["CaCl₂", "", ""], ["FeCl₂", "", ""],
                                                                         ["CuS", "", ""], ["AlCl₃", "", ""], ["SnO₂", "", ""], ["KI", "", ""]], empty_cols=(1, 2)),
    q(5, "<b>Formula.</b>") +
    table(["Nom", "Fórmula", "Nom", "Fórmula"], [["Òxid d'alumini", "", "Bromur de potassi", ""], ["Clorur de magnesi", "", "Òxid de plom(IV)", ""],
                                                ["Òxid de coure(I)", "", "Hidrur de calci", ""], ["Sulfur de sodi", "", "Fluorur de liti", ""]], empty_cols=(1, 3)),
)

EXTRA["sda1-12-fitxa-8-formulacio-sals.pdf"] = mes(
    q(5, "<b>Anomena.</b>") +
    table(["Fórmula", "Nom", "Fórmula", "Nom"], [["Ca(NO₃)₂", "", "Na₂CO₃", ""], ["Al₂(SO₄)₃", "", "NH₄Cl", ""],
                                                ["Mg(OH)₂", "", "Fe(OH)₃", ""], ["K₂SO₄", "", "LiClO₄", ""]], empty_cols=(1, 3)),
    q(7, "<b>Els colors.</b> El nitrat d'estronci i el clorur d'estronci fan el mateix color a la flama. Què tenen en comú? Quin ió dona el color?", 2),
)

EXTRA["sda1-13-fitxa-9-la-cara-fosca-dels-focs.pdf"] = mes(
    q(7, "<b>Llegir bé les dades.</b> L'estronci va arribar a ser unes 86 vegades més alt del normal. Si el valor normal fos de 0,5 ng/m³ (suposem), quin valor es va mesurar? Per què és important saber quin era el valor normal abans de treure conclusions?", 3),
)

# ================================================================== SdA 2 · Aixeta o ampolla?
EXTRA["sda2-03-fitxa-1-l-etiqueta.pdf"] = mes(
    q(5, "<b>Quina mineralització?</b> Classifica aquestes aigües segons el residu sec: A) 35 mg/L; B) 180 mg/L; C) 520 mg/L; D) 1.800 mg/L.", 2),
    q(6, "<b>El calci.</b> Una aigua té 60 mg/L de calci. Quants mg en beus amb 1,5 L? Si suposem que un adult necessita uns 800 mg de calci al dia, quin percentatge hi aporta l'aigua?", 3),
    q(8, "<b>Ions i residu sec.</b> Si sumes els mg/L de tots els ions d'una etiqueta, normalment no dona exactament el residu sec. Una raó és que, en escalfar a 180 °C, l'hidrogencarbonat es descompon i perd diòxid de carboni i aigua. Escriu una altra raó possible.", 2),
)

EXTRA["sda2-04-fitxa-2-concentracio.pdf"] = mes(
    q(6, "<b>Percentatge en massa.</b> Dissolem 25 g de sucre en 225 g d'aigua. Quin és el % en massa?", 2),
    q(7, "<b>Parts per milió.</b> Una mostra de 2 kg d'aigua conté 0,5 mg de plom. Quantes ppm són?", 2),
    q(9, "<b>Diluir el sèrum.</b> Agafem 100 mL de sèrum de 9 g/L i hi afegim aigua fins a 300 mL. Quina massa de sal hi ha? Quina és la concentració nova?", 3),
)

EXTRA["sda2-06-fitxa-3-la-mol.pdf"] = mes(
    q(7, "<b>Mols i grams.</b> a) Quants mols hi ha en 100 g de CaCO₃? b) Quants grams són 0,50 mol de NaCl?", 3),
    q(8, "<b>Un terròs de sucre.</b> Un terròs té 4 g de sacarosa, C₁₂H₂₂O₁₁ (M = 342 g/mol). Quants mols i quantes molècules hi ha?", 3),
    q(9, "<b>Compara.</b> Què té més molècules: 18 g d'aigua o 44 g de diòxid de carboni? Justifica-ho amb els mols.", 2),
)

EXTRA["sda2-07-fitxa-4-molaritat.pdf"] = mes(
    q(6, "<b>Calcula la molaritat:</b> 5,85 g de NaCl en 500 mL de dissolució.", 2),
    q(7, "<b>Prepara.</b> Quants grams de KCl (M = 74,6 g/mol) calen per preparar 250 mL de dissolució 0,10 mol/L?", 2),
    q(9, "<b>De mg/L a mmol/L.</b> Una aigua té 80 mg/L de calci. Passa-ho a mol/L i a mmol/L.", 2),
)

EXTRA["sda2-10-fitxa-5-sistemes-dispersos.pdf"] = mes(
    q(6, "<b>La boira i els fars.</b> Per què els fars d'un cotxe fan un «con» de llum visible quan hi ha boira i no quan l'aire és net?", 2),
    q(7, "<b>Unitats de mida.</b> Passa a metres i escriu-ho en notació científica: 1 nm, 1 µm, 500 nm. Quantes vegades és més gran 1 µm que 1 nm?", 2),
    q(8, "<b>Filtrar no sempre funciona.</b> Per què un filtre de paper separa la sorra de l'aigua però no separa la llet de l'aigua?", 2),
)

EXTRA["sda2-11-fitxa-6-aigua-del-barri.pdf"] = mes(
    q(6, "<b>Ter o Llobregat?</b> Amb la informació de la fitxa, quina aigua esperes que tingui més conductivitat: la d'un barri que rep sobretot aigua del Ter o la d'un que la rep del Llobregat? Per què?", 3),
)

EXTRA["sda2-12-fitxa-7-preu-i-plastic.pdf"] = mes(
    q(6, "<b>Si no tens el rebut.</b> Suposem que el metre cúbic d'aigua de l'aixeta costa 2 € (amb tots els conceptes) i que l'aigua embotellada costa 0,30 € el litre. Quantes vegades més cara és l'embotellada?", 3),
    q(8, "<b>Gerra amb filtre.</b> Algunes famílies fan servir una gerra amb filtre de carbó actiu. Què creus que pot retenir el carbó actiu (gust de clor, sals dissoltes, calç)? Com ho podries comprovar amb el conductímetre del laboratori 2?", 3),
)

# ================================================================== SdA 3 · Quant CO₂ costa venir a l'institut?
EXTRA["sda3-03-fitxa-1-equacio-en-mols.pdf"] = mes(
    q(5, "<b>Llegeix-la.</b> Per a l'equació 2 CO + O₂ → 2 CO₂, escriu què vol dir en molècules, en mols i en grams. Es conserva la massa?", 3),
    q(7, "<b>Ajusta i llegeix.</b> Ajusta Al + O₂ → Al₂O₃ (Al = 27,0) i escriu-ne les proporcions en mols i en grams.", 3),
    q(8, "<b>Vertader o fals?</b> a) En una reacció sempre hi ha els mateixos mols abans i després. b) Els coeficients indiquen proporcions de mols. c) 1 mol de qualsevol substància té la mateixa massa.", 3),
)

EXTRA["sda3-04-fitxa-2-carboni-i-combustibles.pdf"] = mes(
    q(5, "<b>Anomena:</b> a) CH₃–CH₃; b) CH≡CH; c) CH₃–CH₂–CH₂–CH₃; d) CH₃OH; e) CH₂=CH₂.", 3),
    q(6, "<b>Formula</b> (semidesenvolupada i molecular): hexà, propè, pentà, butè (doble enllaç al primer carboni).", 3),
    q(8, "<b>Alcohol o hidrocarbur?</b> Classifica: C₂H₆, C₂H₅OH, C₃H₈, CH₃OH, C₄H₁₀. Com ho has sabut?", 2),
)

EXTRA["sda3-05-fitxa-3-combustions.pdf"] = mes(
    q(5, "<b>Ajusta</b> les combustions completes: a) C₅H₁₂ + O₂ → CO₂ + H₂O; b) CH₃OH + O₂ → CO₂ + H₂O; c) C₆H₁₄ + O₂ → CO₂ + H₂O.", 4),
    q(6, "<b>Sutge.</b> Escriu i ajusta la combustió molt incompleta del metà en què només es formen carboni (C) i aigua.", 2),
    q(7, "<b>L'aigua del propà.</b> Quants mols d'aigua es formen en cremar 1 mol de propà? Quants grams són?", 2),
    q(8, "<b>Per què blau?</b> La flama d'un fogó ben regulat és blava; si li falta aire, es torna groga i embruta les cassoles de negre. Explica-ho amb la combustió completa i incompleta.", 3),
)

EXTRA["sda3-07-fitxa-4-estequiometria.pdf"] = mes(
    q(6, "<b>El propà.</b> Quants grams de CO₂ es formen en cremar 44 g de propà (C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O)?", 2),
    q(8, "<b>L'alt forn.</b> Al ferro s'obté així: Fe₂O₃ + 3 CO → 2 Fe + 3 CO₂. Quina massa de ferro s'obté d'1 tona de Fe₂O₃? Quant CO₂ s'emet?", 3),
)

EXTRA["sda3-09-fitxa-5-litre-de-gasolina.pdf"] = mes(
    q(6, "<b>Un dipòsit.</b> Quants kg de CO₂ s'emeten en cremar un dipòsit de 50 L de gasolina (factor del MITECO)?", 2),
    q(7, "<b>La moto.</b> Una moto gasta 3,0 L de gasolina cada 100 km. Quants grams de CO₂ emet per km? Compara-ho amb el cotxe de l'exercici 4.", 3),
)

EXTRA["sda3-10-fitxa-6-energia-de-les-reaccions.pdf"] = mes(
    q(5, "<b>La bombona.</b> Una bombona té 12,5 kg de butà. Quanta energia desprèn quan es crema tota, en kJ i en kWh (1 kWh = 3.600 kJ)?", 3),
    q(7, "<b>Diagrama.</b> Dibuixa el diagrama d'energia d'una reacció endotèrmica i assenyala-hi l'energia d'activació i l'energia absorbida.", 0, BOX(30)),
)

EXTRA["sda3-12-fitxa-7-co2-per-km.pdf"] = mes(
    q(6, "<b>Tot l'institut.</b> Si 100 alumnes venen en cotxe des de 3 km de mitjana (anada i tornada, 175 dies), quantes tones de CO₂ fan en un curs? Quant s'estalviaria si vinguessin amb autobús?", 3),
    q(7, "<b>Per persona.</b> Un autobús amb 40 persones emet molt més CO₂ per km que un cotxe. Per què, aleshores, el factor per persona i km de l'autobús de la taula és més baix?", 3),
)

EXTRA["sda3-13-fitxa-8-calculadora.pdf"] = mes(
    q(4, "<b>La fórmula, pas a pas.</b> Si a la cel·la C2 hi ha els km d'anada i a la D2 els dies a la setmana, escriu la fórmula que calcula els km del curs (35 setmanes). Comprova-la amb 4 km i 5 dies.", 3),
    q(6, "<b>Revisa.</b> Un grup ha obtingut que un alumne que ve a peu fa 5 kg de CO₂ en un curs. Quin error pot haver-hi al full de càlcul?", 2),
)

EXTRA["sda3-14-fitxa-9-aire-i-salut.pdf"] = mes(
    q(7, "<b>Contra-argument.</b> Algú diu: «El NO₂ no és un problema perquè no escalfa el planeta». Respon-li amb les dades de la fitxa.", 3),
)

# ================================================================== SdA 4 · El patrimoni que es desfà
EXTRA["sda4-03-fitxa-1-acids-bases-ph.pdf"] = mes(
    q(5, "<b>Del pH a l'H⁺.</b> Una dissolució de pH 3 té una concentració d'H⁺ de 10⁻³ mol/L. Quina concentració té una de pH 5? Quantes vegades més àcida és la de pH 3?", 3),
    q(6, "<b>Diluir.</b> Si diluïm 10 vegades una dissolució àcida de pH 2, quin pH tindrà aproximadament? Per molt que la diluïm, pot arribar a pH 8?", 3),
    q(8, "<b>La pluja.</b> La pluja natural té un pH d'uns 5,6 i la pluja àcida pot tenir pH 4. Quantes vegades més H⁺ té la pluja àcida?", 2),
)

EXTRA["sda4-05-fitxa-2-neutralitzacio.pdf"] = mes(
    q(6, "<b>La valoració.</b> Per neutralitzar 20,0 mL d'àcid clorhídric 0,50 mol/L, quants mL de NaOH 0,25 mol/L calen?", 3),
    q(7, "<b>Un altre antiàcid.</b> Una pastilla té 0,50 g d'hidròxid de magnesi, Mg(OH)₂. Quants mols d'HCl pot neutralitzar (Mg(OH)₂ + 2 HCl → MgCl₂ + 2 H₂O)?", 3),
)

EXTRA["sda4-06-fitxa-3-aire-acid-i-pedra.pdf"] = mes(
    q(5, "<b>El guix.</b> Quants grams de sulfat de calci (CaSO₄) es formen quan 100 g de marbre (CaCO₃) reaccionen amb àcid sulfúric? (S = 32,1.)", 3),
    q(7, "<b>Abans i ara.</b> Escriu dues raons per les quals avui a Barcelona hi ha molt menys SO₂ que fa cinquanta anys, i per què el NO₂ continua sent un problema.", 3),
)

EXTRA["sda4-08-fitxa-4-col-lisions.pdf"] = mes(
    q(5, "<b>Dos camins.</b> Dibuixa en un mateix diagrama d'energia una reacció exotèrmica amb catalitzador i sense. Què canvia i què no canvia?", 0, BOX(30)),
    q(7, "<b>Prou energia.</b> Per què un llumí no s'encén sol, però sí quan el freguem? Fes servir la paraula energia d'activació.", 2),
)

EXTRA["sda4-09-fitxa-5-corrosio.pdf"] = mes(
    q(6, "<b>Qui es sacrifica?</b> Amb la sèrie de reactivitat, digues quin metall protegiria el ferro i quin no: magnesi, coure, zinc, plata.", 2),
    q(7, "<b>La massa del rovell.</b> Quina massa d'òxid de ferro(III) es forma si es rovellen del tot 112 g de ferro (4 Fe + 3 O₂ → 2 Fe₂O₃)?", 3),
    q(8, "<b>Les baranes del mar.</b> Per què les baranes del passeig marítim es rovellen més de pressa que les d'un barri de muntanya? Proposa dues maneres de protegir-les.", 3),
)

EXTRA["sda4-12-fitxa-6-ciencia-a-la-cuina.pdf"] = mes(
    q(8, "<b>Experiment de cuina.</b> Posa aigua en un plat, empolvora-hi pebre i toca el centre amb un dit amb una gota de sabó. Què passa? Relaciona-ho amb el que estudiava Agnes Pockels.", 3),
)

# ================================================================== SdA 5 · Com es tanca una ferida?
EXTRA["sda5-03-fitxa-1-vectors.pdf"] = mes(
    q(7, "<b>El dron.</b> Un dron vola 300 m cap a l'est i després 400 m cap al nord en 50 s. Calcula les components i el mòdul del desplaçament i el mòdul de la velocitat mitjana.", 3),
)

EXTRA["sda5-04-fitxa-2-el-front-avanca.pdf"] = mes(
    q(7, "<b>L'àrea sota la gràfica v–t.</b> Amb la teva gràfica, calcula quants µm avança el front durant l'altiplà, de les 8 h a les 12 h. Per què l'àrea sota la gràfica v–t és la distància recorreguda?", 3),
)

EXTRA["sda5-05-fitxa-3-mrua-amb-rigor.pdf"] = mes(
    q(7, "<b>Sortir del semàfor.</b> Una moto passa de 0 a 72 km/h en 5 s. Calcula'n l'acceleració i la distància que recorre.", 3),
)

EXTRA["sda5-07-fitxa-4-caiguda-lliure.pdf"] = mes(
    q(8, "<b>El pou.</b> Deixem caure una pedra en un pou i sentim l'impacte al cap de 2,0 s. Si no tenim en compte el temps que triga el so, quina fondària té el pou? El resultat real serà una mica més gran o més petit? Per què?", 3),
    q(9, "<b>A la Lluna.</b> A la Lluna g = 1,6 m/s². Quant trigaria a caure des de 20 m? Compara-ho amb la Terra.", 2),
)

EXTRA["sda5-09-fitxa-5-forces-com-a-vectors.pdf"] = mes(
    q(6, "<b>Perpendiculars.</b> Dues forces de 60 N i 80 N actuen sobre un cos i són perpendiculars. Quin mòdul té la resultant?", 2),
)

EXTRA["sda5-10-fitxa-6-newton-amb-calcul.pdf"] = mes(
    q(9, "<b>El paracaigudista.</b> Un paracaigudista baixa a velocitat constant amb el paracaigudes obert. Dibuixa'n el diagrama de forces. Quant val la força resultant? Quina llei de Newton fas servir?", 2, BOX(22)),
)

EXTRA["sda5-13-fitxa-7-hooke-i-el-gel.pdf"] = mes(
    q(6, "<b>La molla.</b> Una molla té k = 40 N/m. Quina força cal per allargar-la 5 cm? Quant s'allarga amb una força de 3 N?", 3),
    q(8, "<b>El gel.</b> Amb k<sub>gel</sub> = 2,0 nN/µm, quin desplaçament de les boletes correspon a una força de 7 nN? I quina força fa una cèl·lula si les boletes es desplacen 0,8 µm?", 3),
)

# ================================================================== SdA 6 · L'Ictineo de Monturiol
EXTRA["sda6-03-fitxa-1-pressio.pdf"] = mes(
    q(6, "<b>L'elefant.</b> Un elefant de 5.000 kg es recolza en quatre potes de 0,10 m² cadascuna. Quina pressió fa sobre el terra? Compara-la amb la del taló d'agulla de l'exercici 2.", 3),
    q(7, "<b>El ganivet.</b> El tall d'un ganivet fa 20 cm de llarg i 0,2 mm d'ample. Quina pressió fa si l'empenyem amb 20 N? (Passa les mides a metres.)", 3),
    q(9, "<b>El maó.</b> Un maó de 2,5 kg fa 24 cm × 11,5 cm × 5 cm. Calcula la pressió que fa sobre la taula recolzat sobre la cara més gran i sobre la més petita.", 3),
)

EXTRA["sda6-04-fitxa-2-pressio-hidrostatica.pdf"] = mes(
    q(5, "<b>La piscina.</b> Calcula la pressió hidrostàtica i la total al fons d'una piscina de 2 m d'aigua dolça.", 2),
    q(6, "<b>El més profund.</b> La fossa de les Mariannes té uns 11.000 m de fondària. Quina pressió hidrostàtica hi ha? Quantes atmosferes són?", 3),
    q(8, "<b>El mercuri.</b> Quina pressió fa una columna de 10 cm de mercuri (13.600 kg/m³)? I una de 10 cm d'aigua? Quantes vegades més?", 2),
)

EXTRA["sda6-06-fitxa-3-pascal.pdf"] = mes(
    q(5, "<b>La premsa.</b> Una premsa hidràulica té èmbols de 5 cm² i de 500 cm². Si fem 100 N sobre el petit, quina força fa el gran? Quina massa pot aixecar?", 3),
    q(6, "<b>Quant es mou?</b> Si l'èmbol gran de l'exercici 5 puja 2 cm, quants cm ha baixat el petit? Per què diem que «no es guanya feina gratis»?", 3),
    q(7, "<b>El tub de pasta de dents.</b> Explica amb el principi de Pascal per què surt pasta de dents per la boca del tub encara que premem el tub pel mig.", 2),
)

EXTRA["sda6-07-fitxa-4-pressio-atmosferica.pdf"] = mes(
    q(6, "<b>La força de l'aire.</b> Quina força fa l'atmosfera sobre la cara de dalt d'una taula d'1 m²? Quants kg pesarien el mateix? Per què la taula no s'esfondra?", 3),
    q(8, "<b>Els hemisferis de Magdeburg.</b> El 1654, Otto von Guericke va treure l'aire de dins de dues mitges esferes de metall ajuntades, i ni tirant amb cavalls les van poder separar. Suposem que la unió de les dues mitges esferes és un cercle de 25 cm de radi: quina força fa l'atmosfera sobre cada hemisferi (S = π r²)?", 3),
)

EXTRA["sda6-08-fitxa-5-arquimedes.pdf"] = mes(
    q(6, "<b>Una persona al mar.</b> Una persona de 70 kg té un volum de 0,068 m³. Quina empenta rep totalment submergida al mar? Compara-la amb el pes. Sura?", 3),
    q(7, "<b>El globus d'heli.</b> Un globus d'heli de 0,5 m³ desplaça aire (1,2 kg/m³). Quina empenta rep?", 2),
    q(8, "<b>La corona, a la manera de Galileu.</b> Una corona d'or pur de 1.000 g (19.300 kg/m³) es penja d'una balança dins l'aigua. Quina empenta rep? Quant «pesaria» dins l'aigua, en grams?", 3),
)

EXTRA["sda6-10-fitxa-6-surar.pdf"] = mes(
    q(5, "<b>La fusta.</b> Un bloc de fusta de 600 kg/m³ sura. Quin percentatge en queda submergit a l'aigua dolça? I al mar?", 3),
    q(7, "<b>Del riu al mar.</b> Un vaixell de 2.000 tones passa del riu (aigua dolça) al mar. Quin volum d'aigua desplaça a cada lloc? On s'enfonsa més?", 3),
)

EXTRA["sda6-11-fitxa-7-monturiol.pdf"] = mes(
    q(7, "<b>Finançament popular.</b> L'Ictineo es va pagar en part amb aportacions de molta gent. Com es diu avui aquesta manera de finançar projectes? Posa'n un exemple i digues un avantatge i un risc.", 3),
)

