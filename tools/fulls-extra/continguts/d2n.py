"""Dossiers d'ampliació de 2n ESO (un per SdA), amb la mateixa estructura que els de 3r: reptes amb etiqueta
(Càlcul, Dades, Raonament, Experiment, Fermi, Història, Investiga), apartats i, al final, recursos.
Substitueixen el contingut del full d'ampliació original (se'n conserva la capçalera).
Les dades que no surten als fulls del curs són de llibre de text o s'indiquen com a suposició."""
from estil import rep, tip, table, graf, resources, h2, DOSSIER_INTRO

PHET = "https://phet.colorado.edu/ca/"
REC = '<p class="intro">Recursos per continuar aprenent: institucions científiques, museus i simulacions. Si al costat de l\'adreça hi ha un títol entre cometes, cerca\'l a la pàgina.</p>'
BOX = lambda h: f'<div class="box" style="min-height:{h}mm"></div>'


def dossier(reptes, recursos):
    return DOSSIER_INTRO + "".join(reptes) + resources(recursos, h2("R", "Recursos per anar més enllà") + REC)


DOSSIER = {}

# ================================================================== SdA 1 · L'institut en xifres
DOSSIER["sda1-19-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "Polzades i pantalles.", "Les pantalles es mesuren per la diagonal, en polzades (1 polzada = 2,54 cm). "
        "Una pantalla de televisor fa 55 polzades i té una proporció 16:9 (per cada 16 parts d'ample, 9 d'alt).", [
        "Quants centímetres fa la diagonal? Escriu el factor de conversió.",
        "Amb el teorema de Pitàgores, calcula l'ample i l'alt de la pantalla en cm. (Pista: si l'ample és 16·k i l'alt 9·k, la diagonal és k·√(16² + 9²).)",
        "Quina superfície té la pantalla, en cm² i en m²?"], 7),
    rep(2, "Càlcul", "Nusos i peus.", "Al mar i a l'aire encara es fan servir unitats que no són del SI: 1 nus = 1 milla nàutica per hora, "
        "1 milla nàutica = 1.852 m i 1 peu = 0,3048 m.", [
        "Un vaixell va a 20 nusos. Passa-ho a km/h i a m/s.",
        "Un avió vola a 35.000 peus d'altura. Quants metres són? Compara-ho amb l'Everest (8.849 m).",
        "Per què creus que l'aviació i la navegació no han canviat a les unitats del SI?"], 6),
    rep(3, "Fermi", "Quantes gotes hi ha al Mediterrani?", "Una estimació de Fermi és un càlcul aproximat amb dades arrodonides. "
        "El Mediterrani té una superfície d'uns 2,5 · 10⁶ km² i una profunditat mitjana d'uns 1.500 m. Una gota té uns 0,05 mL.", [
        "Passa la superfície a m² i calcula el volum aproximat del mar en m³ (volum = superfície × profunditat).",
        "Passa el volum a litres i a mL. Escriu-ho tot en notació científica.",
        "Quantes gotes hi ha al Mediterrani? Per què diem que el resultat només és un «ordre de magnitud»?"], 7),
    rep(4, "Càlcul", "L'any llum.", "La llum recorre uns 300.000 km cada segon. Un any llum és la distància que recorre la llum en un any "
        "(1 any ≈ 3,15 · 10⁷ s). L'estrella més propera al Sol, Pròxima del Centaure, és a uns 4,2 anys llum.", [
        "Quants km són un any llum? Escriu-ho en notació científica.",
        "A quants km és Pròxima del Centaure?",
        "Si hi poguéssim anar amb un cotxe a 100 km/h, quants anys trigaríem? Què en conclous?"], 7),
    rep(5, "Fermi", "Els batecs d'una vida.", "El cor batega unes 70 vegades per minut i a cada batec impulsa uns 70 mL de sang.", [
        "Quants batecs fa en un dia? Fes la cadena de factors (min → h → dia).",
        "Quants batecs fa en una vida de 80 anys? Escriu-ho en notació científica.",
        "Quants litres de sang impulsa en tota la vida? Quantes piscines olímpiques (2.500 m³) podria omplir?"], 7),
    rep(6, "Història", "La cana i el pam.", "Abans del sistema mètric, a Barcelona les llargades es mesuraven amb la cana, d'uns 1,555 m, "
        "que tenia 8 pams. Cada ciutat tenia les seves unitats, i una cana de Barcelona no feia el mateix que una de València. "
        "El sistema mètric va arribar a Espanya per llei el 1849.", [
        "Quants centímetres feia un pam de Barcelona?",
        "Mesura la teva alçada i la llargada de l'aula i passa-les a pams.",
        "Escriu dos problemes que tenia el comerç quan cada ciutat feia servir unitats diferents."], 6),
    rep(7, "Experiment", "Mesurar el que és molt petit.", "Amb un regle que només aprecia mil·límetres no podem mesurar el gruix d'un full. "
        "Però sí que podem mesurar el gruix d'un paquet de 500 fulls.", [
        "Explica el mètode pas a pas.",
        "Si el paquet fa 5,0 cm, quant fa cada full, en mm i en m? Escriu-ho en notació científica.",
        "Per què aquest mètode és més precís que mesurar un sol full? Com podries mesurar la massa d'un gra d'arròs amb una balança que aprecia 1 g?"], 6),
    rep(8, "Dades", "L'aigua de casa.", "Aquest és el consum d'aigua d'una família de quatre persones en un any, segons les factures (dades d'exemple):",
        [], 0,
        table(["Trimestre", "1r (gen–mar)", "2n (abr–jun)", "3r (jul–set)", "4t (oct–des)"], [["Consum (m³)", "28", "31", "39", "30"]]),
        '<div class="parts"><p>a) Calcula el consum anual en m³ i en litres.</p><p>b) Quants litres gasta cada persona en un dia? '
        'Compara-ho amb els 110 L per persona i dia de la fitxa 5.</p><p>c) Per què creus que el tercer trimestre és el que gasta més? '
        'Proposa dues maneres d\'estalviar i calcula quant estalviarien en un any.</p></div>' + '<div class="l"></div>' * 6),
], [
    ("Història del Sistema Internacional", "Oficina Internacional de Pesos i Mesures (BIPM): d'on surten el metre, el quilogram i les set unitats bàsiques", "https://www.bipm.org/en/history-si/"),
    ("The International System of Units (SI)", "Oficina Internacional de Pesos i Mesures (BIPM): el document oficial del SI, en anglès i francès", "https://www.bipm.org · «SI Brochure»"),
    ("L'aigua a Catalunya en dades", "Agència Catalana de l'Aigua: consums, embassaments i estat dels rius", "https://aca.gencat.cat"),
    ("Població de Catalunya", "Institut d'Estadística de Catalunya (Idescat): dades oficials per fer estimacions", "https://www.idescat.cat"),
])

# ================================================================== SdA 2 · Un arc de Sant Martí dins d'un got
DOSSIER["sda2-19-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "L'aliatge de la corona.", "La corona del rei Hieró té una massa de 1.000 g i un volum de 64 cm³. Suposem que és un aliatge "
        "d'or (19,3 g/cm³) i plata (10,5 g/cm³) i que el volum total és la suma dels volums dels dos metalls.",
        ["Escriu les dues condicions: m(or) + m(plata) = 1.000 g i V(or) + V(plata) = 64 cm³. Posa-hi m = d · V.",
         "Resol-les (pista: si el volum d'or és V, el de plata és 64 − V). Quants grams d'or i de plata té la corona?",
         "Quin percentatge d'or té? Els joiers diuen que l'or pur és de 24 quirats: de quants quirats seria la corona?"], 8,
        tip("<b>Pista.</b> 19,3 · V + 10,5 · (64 − V) = 1.000. Aïlla V.")),
    rep(2, "Dades", "Quanta sal per fer surar un ou?", "Un grup ha dissolt quantitats creixents de sal en 100 mL d'aigua i ha mesurat la "
        "densitat de cada dissolució:", [
        "Representa la densitat en funció de la sal a la quadrícula i traça la línia que s'ajusta millor als punts.",
        "Quina densitat esperes amb 12 g de sal?",
        "Un ou fresc té una densitat d'uns 1,08 g/cm³. Quants grams de sal cal posar, com a mínim, perquè suri?"], 4,
        table(["Sal en 100 mL d'aigua (g)", "0", "5", "10", "15", "20"], [["Densitat (g/cm³)", "1,00", "1,03", "1,07", "1,10", "1,14"]]) +
        graf((0, 20, 5), (1.0, 1.15, 0.05), "sal (g)", "d (g/cm³)")),
    rep(3, "Càlcul", "El submarinista.", "Una persona de 70 kg té un volum de 72 L. L'aigua dolça té 1,00 g/cm³; la de mar, 1,03 g/cm³; el plom, 11,3 g/cm³.", [
        "Calcula la densitat mitjana de la persona. Sura a l'aigua dolça? I al mar?",
        "Al mar, quina massa ha de tenir la persona amb el plom perquè la seva densitat mitjana sigui 1,03 g/cm³? (Pista: el plom també ocupa volum.)",
        "Quants kg de plom ha de portar per quedar entre dues aigües? Per què el volum d'una persona canvia una mica quan respira?"], 7,
        tip("<b>Pista.</b> Si el plom té un volum V (en L), la seva massa és 11,3 · V (en kg). Ha de complir-se: 70 + 11,3 · V = 1,03 · (72 + V).")),
    rep(4, "Raonament", "El globus d'heli.", "L'aire té una densitat d'uns 1,2 kg/m³ i l'heli, d'uns 0,18 kg/m³.", [
        "Quina massa tenen 10 L d'aire? I 10 L d'heli?",
        "Explica per què un globus d'heli puja i un de bufat no.",
        "Quants grams, com a màxim, podria aixecar un globus de 10 L (sense comptar la goma)?",
        "Un globus d'heli que s'escapa no puja indefinidament. Per què? (Pista: com canvia la densitat de l'aire amb l'altura?)"], 7),
    rep(5, "Raonament", "Aigua i alcohol: 1 + 1 no fa 2.", "Barregem 100 mL d'aigua (1,00 g/mL) i 100 mL d'alcohol (0,79 g/mL). "
        "En mesurar el volum de la mescla, no dona 200 mL sinó uns 193 mL.", [
        "Quina massa té la mescla? S'ha conservat la massa?",
        "Calcula la densitat de la mescla.",
        "Explica amb el model de partícules per què el volum és més petit que la suma. Dibuixa-ho (pots pensar en una galleda de pilotes i una de sorra)."], 6),
    rep(6, "Història", "Galileu i la balança dins l'aigua.", "El 1586, Galileu va proposar que Arquimedes devia comparar la corona i un "
        "tros d'or pur penjats d'una balança i submergits a l'aigua. Un cos submergit «perd» tants grams com grams d'aigua desplaça "
        "(1 cm³ d'aigua = 1 g).", [
        "Quant «pesaria» dins l'aigua la corona de 1.000 g que desplaça 64 cm³?",
        "Quant «pesaria» dins l'aigua 1.000 g d'or pur (19,3 g/cm³)?",
        "La diferència són uns 12 g. Per què és molt més fàcil detectar 12 g amb una balança que veure com puja l'aigua d'una banyera (fitxa 5)?"], 6),
    rep(7, "Experiment", "Un densímetre casolà.", "Amb una canyeta de beure, plastilina i un retolador pots fer un densímetre.", [
        "Explica com el faries i com el calibraries amb aigua (1,00 g/mL) i amb aigua saturada de sal (1,20 g/mL).",
        "En quin dels dos líquids s'enfonsarà més? Per què?",
        "Com el faries servir per saber si una llet té aigua afegida (fitxa 6)? Quin resultat esperaries?"], 6, after=BOX(28)),
    rep(8, "Investiga", "Marie Tharp, la cartògrafa del fons del mar.", "La geòloga Marie Tharp (1920–2006) va dibuixar, amb Bruce Heezen, "
        "els primers mapes del fons de l'oceà Atlàntic a partir de mesures de profunditat fetes des de vaixells. Durant anys no la "
        "deixaven embarcar en els vaixells de recerca perquè era dona.", [
        "Busca què va descobrir al mig de l'Atlàntic i per què va ser important per a la geologia. Cita la font.",
        "Com es mesura la profunditat del mar des d'un vaixell?",
        "Quina relació té la seva història amb la d'Hipàtia (fitxa 6)?"], 6),
], [
    ("Densitat", "Simulació PhET: compara masses i volums de blocs de materials diferents i descobreix quins suren", PHET + " · «Densitat» (Density)"),
    ("Flotabilitat", "Simulació PhET: l'empenta, el pes i per què uns objectes suren i d'altres no", PHET + " · «Flotabilitat» (Buoyancy)"),
    ("Les balances hidrostàtiques", "Museo Galileo (Florència): la balança d'Arquimedes i la corona de Hieró, i la bilancetta de Galileu", "https://catalogue.museogalileo.it/indepth/WeighingInstruments.html"),
    ("Hipàcia d'Alexandria", "Gran Enciclopèdia Catalana: la vida i l'obra de la matemàtica i astrònoma", "https://www.enciclopedia.cat/gran-enciclopedia-catalana/hipacia"),
    ("Marie Tharp i el mapa del fons de l'oceà", "Biblioteca del Congrés dels EUA (en anglès): el mapa del fons de l'oceà i la seva autora", "https://www.loc.gov/loc/lcib/0211/tharp.html"),
])

# ================================================================== SdA 3 · La pilota que no bota
DOSSIER["sda3-21-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "El globus sonda.", "Un globus meteorològic té 5,0 m³ d'heli a nivell del mar, a 1,0 atm i 15 °C. Puja fins a una altura on "
        "la pressió és de 0,30 atm i la temperatura, −45 °C.", [
        "Passa les dues temperatures a kelvin.",
        "Calcula el volum del globus a l'altura final.",
        "Per què els globus sonda es deixen anar poc inflats? Què li acaba passant al globus?"], 6,
        tip("Quan canvien alhora la pressió, el volum i la temperatura d'una mateixa quantitat de gas, es compleix la "
            "<b>llei combinada dels gasos</b>: \\(\\dfrac{P_1 V_1}{T_1} = \\dfrac{P_2 V_2}{T_2}\\), amb la temperatura en kelvin.")),
    rep(2, "Dades", "A la recerca del zero absolut.", "Escalfem un gas a pressió constant i mesurem el volum:", [
        "Representa el volum en funció de la temperatura. L'eix horitzontal arriba fins a −300 °C.",
        "Allarga la recta fins que el volum sigui zero. A quina temperatura passa? Com s'anomena?",
        "Per què un gas real no pot arribar mai a tenir volum zero? (Pista: què li passa abans de refredar-se tant?)"], 4,
        table(["Temperatura (°C)", "0", "25", "50", "75", "100"], [["Volum (L)", "1,00", "1,09", "1,18", "1,27", "1,37"]]) +
        graf((-300, 100, 50), (0, 1.5, 0.25), "T (°C)", "V (L)")),
    rep(3, "Dades", "Quina substància és?", "Fonem una substància sòlida, la deixem refredar i n'apuntem la temperatura cada minut:", [
        "Representa la corba de refredament.",
        "A quina temperatura se solidifica? Mira la taula de la fitxa 3: quina substància pot ser?",
        "En quin estat és en cada tram? Per què la temperatura no baixa mentre se solidifica?"], 4,
        table(["t (min)", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
              [["T (°C)", "90", "82", "75", "70", "69", "69", "69", "69", "69", "62", "55"]]) +
        graf((0, 10, 1), (40, 100, 10), "t (min)", "T (°C)")),
    rep(4, "Raonament", "L'olla a pressió i la muntanya.", "Dins d'una olla a pressió l'aire i el vapor arriben a unes 2 atm i l'aigua bull a uns 120 °C. "
        "Al cim de l'Everest, on la pressió és d'una tercera part d'atmosfera, l'aigua bull a uns 70 °C.", [
        "Explica amb el model de partícules per què la temperatura d'ebullició depèn de la pressió de l'aire.",
        "Per què a l'olla a pressió els aliments es couen més de pressa?",
        "Per què costa tant coure un ou dur a dalt d'una muntanya molt alta?"], 6),
    rep(5, "Càlcul", "Torricelli amb aigua i amb oli.", "El 1643, Evangelista Torricelli va veure que la pressió de l'aire aguanta una columna "
        "de mercuri de 76 cm. Una columna de líquid fa la mateixa pressió si té la mateixa massa per sobre de cada cm². "
        "Densitats: mercuri 13,6 g/cm³, aigua 1,00 g/cm³, oli 0,92 g/cm³.", [
        "Quantes vegades és més dens el mercuri que l'aigua?",
        "Quina altura tindria la columna si Torricelli hagués fet servir aigua? I oli?",
        "Per què el baròmetre de Torricelli es feia amb mercuri?"], 5),
    rep(6, "Càlcul", "La pilota del pati.", "Una pilota de bàsquet té una pressió total d'1,6 atm a l'aula, a 20 °C. La deixem a la nevera, a 4 °C. "
        "El volum gairebé no canvia.", [
        "Quina llei dels gasos fas servir? Quina pressió tindrà a 4 °C?",
        "Explica amb el model de partícules per què una pilota freda bota menys.",
        "Les instruccions de les pilotes indiquen la pressió «a temperatura ambient». Per què?"], 6),
    rep(7, "Experiment", "El globus que s'infla sol.", "Posa un globus desinflat a la boca d'una ampolla buida (plena d'aire). Fica l'ampolla "
        "en un recipient amb aigua calenta de l'aixeta i, després, en un d'aigua amb gel.", [
        "Què esperes que passi amb el globus en cada cas? Escriu-ho abans de fer-ho.",
        "Explica-ho amb la llei de Charles i amb el model de partícules.",
        "Com podries mesurar quant ha canviat el volum? Quines variables has de controlar?"], 6),
], [
    ("Propietats dels gasos", "Simulació PhET: canvia la temperatura, el volum i el nombre de partícules i mira què passa amb la pressió", PHET + " · «Propietats dels gasos» (Gas Properties)"),
    ("Estats de la matèria: conceptes bàsics", "Simulació PhET: escalfa i refreda aigua, neó o oxigen i observa les partícules", PHET + " · «Estats de la matèria: conceptes bàsics»"),
    ("La llei de Charles i Gay-Lussac", "NASA, Centre de Recerca Glenn (en anglès): el volum i la temperatura d'un gas, amb animacions", "https://www.grc.nasa.gov/www/k-12/airplane/glussac.html"),
    ("La llei de Boyle", "NASA, Centre de Recerca Glenn (en anglès): la pressió i el volum d'un gas, amb una animació", "https://www.grc.nasa.gov/www/k-12/airplane/aboyle.html"),
    ("La pressió atmosfèrica avui", "Servei Meteorològic de Catalunya: dades de pressió de les estacions i mapes del temps", "https://www.meteo.cat"),
])

# ================================================================== SdA 4 · Aigua neta del riu
DOSSIER["sda4-20-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "Tres maneres de dir la concentració.", "Dissolem 20 g de sal en 180 g d'aigua. La dissolució té una densitat d'1,07 g/mL.", [
        "Quina massa té la dissolució? Calcula'n el percentatge en massa: % = massa de solut ÷ massa de dissolució · 100.",
        "Quin volum té la dissolució (V = m/d)? Calcula'n la concentració en g/L.",
        "Per què per calcular el percentatge en massa no cal saber el volum, i per a la concentració en g/L sí?"], 7),
    rep(2, "Dades", "La corba de solubilitat.", "Aquesta és la solubilitat del nitrat de potassi en aigua (grams que es dissolen en 100 g d'aigua):", [
        "Representa la corba de solubilitat.",
        "Quina és la solubilitat a 50 °C? I a quina temperatura es dissolen 100 g?",
        "Tenim una dissolució saturada en 100 g d'aigua a 80 °C i la refredem fins a 20 °C. Quants grams de cristalls es formen?",
        "Els químics fan servir aquest mètode (la recristal·lització) per purificar sòlids. Per què creus que funciona?"], 6,
        table(["Temperatura (°C)", "0", "20", "40", "60", "80", "100"], [["Solubilitat (g/100 g d'aigua)", "13", "32", "64", "110", "169", "246"]]) +
        graf((0, 100, 20), (0, 250, 50), "T (°C)", "solubilitat (g/100 g)")),
    rep(3, "Experiment", "La cromatografia dels retoladors.", "Volem saber quins colorants porta la tinta de tres retoladors negres de marques diferents.", [
        "Quin material necessites? Dibuixa el muntatge i explica els passos.",
        "En un paper, l'aigua ha pujat 8,0 cm i una taca blava ha pujat 2,4 cm. El factor de retenció és Rf = distància de la taca ÷ distància de l'aigua. Calcula'l.",
        "Una taca groga té Rf = 0,75. Quants cm ha pujat? Per què cada colorant puja una distància diferent?"], 6, after=BOX(26)),
    rep(4, "Dades", "L'anàlisi d'un pou.", "Aquesta és l'anàlisi de l'aigua d'un pou d'una masia (dades d'exemple). Els valors paramètrics són els "
        "màxims que fixa la llei (Reial decret 3/2023) per a l'aigua de consum.", [
        "Quins paràmetres compleixen la llei i quins no?",
        "Es podria treure el nitrat amb un filtre de sorra? Per què? Quin tipus de mescla és l'aigua del pou?",
        "Quants mg de nitrat beuria una persona que en pren 2 L al dia?"], 5,
        table(["Paràmetre", "Nitrat", "Sodi", "Clorur", "Calci"], [["Valor del pou (mg/L)", "62", "45", "120", "95"],
                                                                ["Valor paramètric (mg/L)", "50", "200", "250", "—"]])),
    rep(5, "Càlcul", "La dessalinitzadora.", "Suposem que una dessalinitzadora produeix 200.000 m³ d'aigua dolça al dia. L'aigua de mar té uns 38 g de sals per litre.", [
        "Si cada persona gasta 110 L al dia, quantes persones podria abastir?",
        "Quants kg de sals hi ha en 1 m³ d'aigua de mar?",
        "Les sals separades surten de la planta en una aigua molt salada (la salmorra), que es torna al mar. Quin problema pot causar? Com es podria reduir?"], 6),
    rep(6, "Experiment", "Una potabilitzadora a l'aula.", "Amb una ampolla de plàstic tallada, cotó, sorra fina, grava i carbó actiu pots filtrar aigua tèrbola.", [
        "En quin ordre posaries les capes, de baix a dalt? Per què?",
        "Què reté cada capa?",
        "L'aigua que surt és transparent. Es pot beure? Quines etapes de la potabilitzadora de la fitxa 5 falten?"], 6),
    rep(7, "Investiga", "La petjada hídrica.", "La petjada hídrica és tota l'aigua que cal per produir un aliment o un objecte, des del camp fins a la botiga.", [
        "Busca en una font fiable la petjada hídrica d'1 kg de carn de vedella, d'1 kg de tomàquets i d'una samarreta de cotó. Cita la font.",
        "Quantes dutxes de 50 L equivalen a cadascuna?",
        "Què en conclous? Proposa un canvi d'hàbit i calcula quanta aigua estalviaria en un any."], 6),
], [
    ("Concentració", "Simulació PhET: afegeix solut, evapora aigua i observa quan la dissolució queda saturada", PHET + " · «Concentració» (Concentration)"),
    ("Agència Catalana de l'Aigua", "Estat dels rius i embassaments de Catalunya i dades de la sequera", "https://aca.gencat.cat"),
    ("Aigües de Barcelona", "Com es potabilitza l'aigua i anàlisi de la qualitat de l'aigua per adreça", "https://www.aiguesdebarcelona.cat"),
    ("Cromatografia en paper", "Royal Society of Chemistry (en anglès): vídeo i fitxes per separar els colorants de les tintes", "https://edu.rsc.org/resources/paper-chromatography-practical-videos-14-16-students/4011446.article"),
    ("Fàbriques d'aigua per salvar-nos de la sequera", "3Cat: com funcionen la dessalinitzadora del Llobregat i la regeneració d'aigua", "https://www.3cat.cat/3catinfo/fabriques-daigua-per-salvar-nos-de-la-sequera/noticia/3230125/"),
    ("Water Footprint Network", "La petjada hídrica de centenars d'aliments i productes (en anglès)", "https://www.waterfootprint.org · «Product gallery»"),
])

# ================================================================== SdA 5 · La química de la coca de Sant Joan
DOSSIER["sda5-20-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "Qui sobra?", "El carboni crema i forma diòxid de carboni. Sempre reaccionen en la mateixa proporció: 12 g de carboni amb 32 g d'oxigen.", [
        "Quants grams de diòxid de carboni es formen amb 12 g de carboni? Quina llei fas servir?",
        "Tenim 30 g de carboni i 64 g d'oxigen. Quin dels dos s'acaba primer? Quants grams sobren de l'altre?",
        "Quants grams de diòxid de carboni es formen?"], 7),
    rep(2, "Càlcul", "L'aigua i les proporcions.", "L'aigua sempre es forma amb 1 g d'hidrogen per cada 8 g d'oxigen.", [
        "Quanta aigua es forma amb 2 g d'hidrogen i 16 g d'oxigen?",
        "Tenim 3 g d'hidrogen i 30 g d'oxigen. Quin reactiu s'acaba primer? Quanta aigua es forma? Quant sobra de l'altre reactiu?",
        "Dibuixa amb boles les partícules de la reacció (2 H₂ + O₂ → 2 H₂O) i explica per què la proporció sempre és la mateixa."], 7),
    rep(3, "Dades", "La pastilla i la temperatura.", "Un grup ha mesurat quant triga a dissoldre's una pastilla efervescent sencera en aigua a diferents temperatures:", [
        "Representa el temps en funció de la temperatura.",
        "Quant creus que trigaria a 35 °C? I a 5 °C?",
        "Explica la forma de la gràfica amb els xocs entre partícules. La relació és una recta?"], 4,
        table(["Temperatura (°C)", "10", "20", "30", "40", "50", "60"], [["Temps (s)", "95", "60", "42", "30", "24", "19"]]) +
        graf((0, 60, 10), (0, 100, 20), "T (°C)", "t (s)")),
    rep(4, "Experiment", "La saliva i el midó.", "La saliva té un enzim, l'amilasa, que trenca el midó. El iode (la solució de Lugol) es torna blau fosc amb el midó.", [
        "Dissenya un experiment per comprovar que la saliva digereix el midó. Quins tubs prepararies? Quin és el tub de control?",
        "Quina variable canvies, quina observes i quines mantens iguals?",
        "Què esperes veure al cap de 10 minuts a 37 °C? Per què fem l'experiment a 37 °C?"], 7),
    rep(5, "Raonament", "Bosses de fred i escalfadors de mans.", "Les bosses de fred de les farmacioles porten una sal (sovint nitrat d'amoni) i aigua "
        "separades: quan les premem, la sal es dissol i la bossa es refreda. Els escalfadors de mans d'un sol ús porten pols de ferro que, "
        "en obrir el paquet, reacciona amb l'oxigen de l'aire i s'escalfa.", [
        "Quin dels dos desprèn calor (exotèrmic) i quin n'absorbeix (endotèrmic)?",
        "En quin dels dos es forma una substància nova? Quina evidència en tens?",
        "Per què l'escalfador no s'escalfa fins que no obrim el paquet hermètic?"], 6),
    rep(6, "Història", "Boyle, Lavoisier i l'estany.", "Al segle XVII, Robert Boyle va escalfar estany en un recipient tancat, el va obrir i va veure "
        "que el metall pesava més: va pensar que el foc tenia massa. Cap al 1774, Antoine Lavoisier va pesar el recipient abans d'obrir-lo i "
        "va veure que la massa total no canviava. En obrir-lo, hi entrava aire.", [
        "D'on surt la massa que guanya l'estany?",
        "Per què era tan important pesar el recipient tancat?",
        "11,9 g d'estany es converteixen en 15,1 g d'òxid d'estany. Quants grams d'oxigen han reaccionat?"], 6),
    rep(7, "Investiga", "Daurar, no cremar.", "L'acrilamida es forma quan els aliments rics en midó es couen a temperatures molt altes.", [
        "Busca a la web de l'Autoritat Europea de Seguretat Alimentària (EFSA) o de l'Agència Catalana de Seguretat Alimentària què recomanen per reduir-la a casa. Cita la font.",
        "Per què unes patates bullides no en fan i unes de fregides sí?",
        "Fes un cartell petit per a la cuina de casa amb tres consells i el perquè científic."], 6),
], [
    ("Reactius, productes i sobrants", "Simulació PhET: fes reaccions i descobreix quin reactiu s'acaba primer", PHET + " · «Reactants, Products and Leftovers»"),
    ("Acrilamida", "Autoritat Europea de Seguretat Alimentària (EFSA): què és i com reduir-la a casa", "https://www.efsa.europa.eu · «Acrylamide»"),
    ("Seguretat alimentària a casa", "Agència Catalana de Seguretat Alimentària: conservació dels aliments i consells", "https://acsa.gencat.cat"),
])

# ================================================================== SdA 6 · La carmanyola calenta
DOSSIER["sda6-20-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "Del gel a l'aigua de beure.", "Volem passar 200 g de gel a −10 °C a aigua a 20 °C.", [
        "Calcula la calor per escalfar el gel de −10 °C a 0 °C.",
        "Calcula la calor per fondre'l.",
        "Calcula la calor per escalfar l'aigua de 0 °C a 20 °C, i la calor total. Quina etapa en necessita més?"], 7,
        tip("Per escalfar: \\(Q = m \\cdot c \\cdot \\Delta T\\). Per fondre a 0 °C: \\(Q = m \\cdot L_f\\). "
            "\\(c_{\\text{gel}} = 2.100\\ \\text{J/(kg}\\cdot{}^{\\circ}\\text{C)}\\); \\(c_{\\text{aigua}} = 4.180\\ \\text{J/(kg}\\cdot{}^{\\circ}\\text{C)}\\); \\(L_f = 334.000\\ \\text{J/kg}\\).")),
    rep(2, "Càlcul", "El bullidor i el rendiment.", "Un bullidor de 2.000 W (gasta 2.000 J cada segon) escalfa 1 L d'aigua de 20 °C a 100 °C en 3 minuts.", [
        "Quanta energia elèctrica ha gastat?",
        "Quanta calor ha rebut l'aigua?",
        "El rendiment és l'energia útil dividida per l'energia gastada, en %. Calcula'l. On va la resta d'energia?"], 6),
    rep(3, "Càlcul", "Suar ens refreda.", "Per evaporar 1 kg d'aigua calen uns 2.260 kJ.", [
        "Quanta energia cal per evaporar mig litre d'aigua?",
        "Compara-ho amb l'energia per escalfar aquest mig litre de 20 °C a 100 °C. Quantes vegades més és?",
        "D'on treu la suor l'energia per evaporar-se? Per què ens refreda?"], 6),
    rep(4, "Dades", "Quina carmanyola aïlla més?", "Hem posat aigua a 80 °C en quatre recipients i n'hem mesurat la temperatura cada 10 minuts:", [
        "Representa les quatre corbes a la mateixa quadrícula, amb colors diferents.",
        "Ordena els recipients de més a menys aïllant. Explica-ho amb la conducció, la convecció i la radiació.",
        "Quin recipient triaries per a la carmanyola? Quina millora hi faries?"], 4,
        table(["t (min)", "0", "10", "20", "30"], [["Alumini (°C)", "80", "62", "50", "42"], ["Plàstic (°C)", "80", "69", "61", "54"],
                                                  ["Porexpan (°C)", "80", "75", "70", "66"], ["Termo (°C)", "80", "78", "76", "74"]]) +
        graf((0, 30, 5), (30, 80, 10), "t (min)", "T (°C)")),
    rep(5, "Raonament", "El mar i el clima.", "La calor específica de l'aigua és 4.180 J/(kg·°C) i la de la sorra, 830 J/(kg·°C).", [
        "Si donem la mateixa energia a 1 kg d'aigua i a 1 kg de sorra, quantes vegades més puja la temperatura de la sorra?",
        "De dia, a la platja, bufa una brisa del mar cap a terra. Explica-ho amb la convecció de l'aire.",
        "Per què a Barcelona els hiverns són més suaus que a Lleida?"], 6),
    rep(6, "Història", "Joule i l'aigua que s'escalfa.", "Cap al 1845, James Prescott Joule va demostrar que el treball mecànic es converteix en calor: "
        "uns pesos que queien feien girar unes paletes dins d'aigua i l'aigua s'escalfava una mica. L'energia d'un pes que baixa és E = m · g · h, amb g = 9,8 m/s².", [
        "Un pes de 10 kg baixa 2 m. Quanta energia allibera? I si l'aixequem i el deixem baixar 20 vegades?",
        "Si tota aquesta energia escalfa 0,5 kg d'aigua, quants graus puja la temperatura?",
        "Per què creus que la unitat d'energia del SI porta el nom de Joule?"], 6),
    rep(7, "Experiment", "Un forn solar.", "Amb una capsa de sabates, paper d'alumini, cartolina negra i plàstic transparent pots fer un forn solar.", [
        "Dibuixa el forn i explica què fa cada material amb la radiació, la conducció i la convecció.",
        "Com mesuraries si funciona? Quines variables controlaries?",
        "Suposem que una placa solar de 400 W produeix uns 560 kWh l'any a Catalunya. Quantes en caldrien per a una casa que gasta 3.000 kWh l'any?"], 6, after=BOX(30)),
], [
    ("Formes d'energia i canvis", "Simulació PhET: escalfa i refreda materials i segueix les transformacions d'energia", PHET + " · «Formes d'energia i canvis» (Energy Forms and Changes)"),
    ("Institut Català d'Energia", "Consells d'estalvi energètic a casa i dades de l'energia a Catalunya", "https://icaen.gencat.cat"),
    ("Passive House", "Govern d'Austràlia, Your Home (en anglès): com s'aïlla una casa que gairebé no necessita calefacció", "https://yourhome.gov.au/passive-design/passive-house"),
    ("James Dewar i el termo", "Royal Institution (en anglès): l'inventor de l'ampolla de buit, que va crear el 1892", "https://www.rigb.org/explore-science/explore/person/james-dewar-1842-1923"),
    ("Museu de la Ciència i de la Tècnica de Catalunya", "A Terrassa: màquines de vapor, energia i la història industrial de Catalunya", "https://mnactec.cat"),
])
