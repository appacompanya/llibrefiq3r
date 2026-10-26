"""Dossiers de problemes de 2n d'ESO (exercicis del tipus de les fitxes de cada SdA)."""
from gen_problemes import Q, nf
from gen_teoria import T

# ======================================================================== SdA 1
def sda1():
    S = []
    S.append(("Seguretat i material de laboratori", [
        (1, Q(1, "Normes de seguretat.", "Explica per què cada norma és important: a) portar els cabells recollits; b) no menjar al laboratori; c) olorar apropant el vapor amb la mà; d) avisar de seguida si hi ha un accident."), "a) no s'encenen ni s'enganxen · b) podríem ingerir un producte tòxic · c) no inhalem directament vapors perillosos · d) es pot actuar ràpid i evitar mals més grans."),
        (1, Q(1, "Pictogrames.", "Descriu el pictograma i el perill de: inflamable, corrosiu, toxicitat aguda i perillós per al medi ambient. Busca a casa un producte que en porti algun."), "Flama (crema fàcilment) · mà i superfície que es desfan (destrueix la pell i els metalls) · calavera (pot matar) · arbre i peix (perjudica els éssers vius). Ex.: lleixiu, desembussador, alcohol."),
        (1, Q(1, "Quin material?", "Quin material de laboratori faries servir per: a) mesurar 35 mL d'aigua amb exactitud; b) escalfar aigua; c) agitar una dissolució sense que vessi; d) filtrar; e) mesurar la massa d'una pedra; f) agafar 5 mL exactes d'un líquid?"), "a) proveta · b) vas de precipitats · c) erlenmeyer · d) embut i paper de filtre · e) balança · f) pipeta amb pera"),
        (2, Q(2, "Què faries?", "Durant una pràctica, a una companya li esquitxa a la mà una gota d'un producte de neteja. Què ha de fer? I si el producte cau a terra?"), "Rentar-se amb molta aigua i avisar el professor · avisar, no tocar-ho i netejar-ho com indiqui el professor."),
    ]))
    S.append(("Magnituds, unitats i instruments", [
        (1, Q(1, "Magnitud o no?", "Quines són magnituds? L'alçada, la por, la massa, el color preferit, el temps, la temperatura, l'avorriment, el volum. Escriu la unitat del SI de les que ho siguin."), "Alçada (m), massa (kg), temps (s), temperatura (K), volum (m³). No: por, color preferit, avorriment."),
        (1, Q(1, "Fonamental o derivada?", "Longitud, superfície, massa, volum, temps, velocitat, temperatura."), "Fonamentals: longitud, massa, temps, temperatura · derivades: superfície, volum, velocitat"),
        (1, Q(1, "Prefixos.", "Completa: 1 km = ___ m · 1 m = ___ cm · 1 kg = ___ g · 1 L = ___ mL · 1 m = ___ mm · 1 g = ___ mg."), "1 000 · 100 · 1 000 · 1 000 · 1 000 · 1 000"),
        (2, Q(2, "Sensibilitat.", "Quina és la sensibilitat d'un regle mil·limetrat, d'una proveta amb ratlles cada 2 mL i d'una balança que mostra 12,40 g? Quin instrument triaries per mesurar el gruix d'un llibre? I la llargada del passadís?"), "1 mm · 2 mL · 0,01 g · regle · cinta mètrica"),
        (2, Q(2, "La mitjana.", "Mesurem la llargada de la classe quatre vegades: 7,84 m · 7,86 m · 7,85 m · 8,40 m. a) Hi ha alguna mesura que s'hagi de descartar? b) Calcula la mitjana de les vàlides."), "a) 8,40 m · b) 7,85 m"),
        (2, Q(2, "Mesurar el que és petit.", "100 fulls d'un llibre fan 9 mm de gruix. Quin gruix té un full? 20 gotes d'aigua fan 1 mL: quin volum té una gota?"), "0,09 mm · 0,05 mL"),
        (2, Q(2, "L'error.", "La llargada real d'un passadís és de 20,00 m i un grup mesura 20,30 m. Calcula l'error absolut i l'error relatiu en percentatge."), "Eₐ = 0,30 m · Eᵣ = 1,5 %"),
    ]))
    S.append(("Canvis d'unitats amb factors de conversió", [
        (1, Q(1, "Un factor.", "Passa:", "2,5 km a m", "350 g a kg", "1,8 L a mL", "45 min a h", "750 mL a L", "3 h a min"), "a) 2 500 m · b) 0,35 kg · c) 1 800 mL · d) 0,75 h · e) 0,75 L · f) 180 min"),
        (2, Q(2, "Factors encadenats.", "Passa:", "1 dia a s", "5 km a cm", "2 h a s", "0,5 kg a mg"), "a) 86 400 s · b) 500 000 cm · c) 7 200 s · d) 500 000 mg"),
        (2, Q(2, "Unitats compostes.", "Passa: a) 90 km/h a m/s · b) 20 m/s a km/h · c) 1,3 g/cm³ a kg/m³ · d) 120 km/h a m/s."), f"a) 25 m/s · b) 72 km/h · c) 1 300 kg/m³ · d) {nf(120/3.6, 1)} m/s"),
        (3, Q(3, "Qui va més de pressa?", "Un guepard corre a 30 m/s i un cotxe a 100 km/h. Qui va més ràpid? Fes servir un factor de conversió."), f"Guepard: 108 km/h (el cotxe va a {nf(100/3.6, 1)} m/s): el guepard."),
        (2, Q(2, "Troba l'error.", "Un alumne passa 3 km a m així: 3 km · (1 km / 1 000 m) = 0,003 m. Què ha fet malament? Fes-ho bé."), "Ha posat el factor al revés: 3 km · (1 000 m / 1 km) = 3 000 m."),
    ]))
    S.append(("Superfície i volum", [
        (1, Q(1, "Superfícies.", "Passa: a) 3 m² a cm² · b) 25 000 cm² a m² · c) 2 km² a m² · d) 450 dm² a m²."), "a) 30 000 cm² · b) 2,5 m² · c) 2 000 000 m² · d) 4,5 m²"),
        (1, Q(1, "Volums i litres.", "Passa: a) 2 m³ a L · b) 500 cm³ a L · c) 3,5 L a cm³ · d) 0,25 dm³ a mL · e) 4 500 L a m³."), "a) 2 000 L · b) 0,5 L · c) 3 500 cm³ · d) 250 mL · e) 4,5 m³"),
        (2, Q(2, "L'aula.", "Una aula fa 8 m de llarg, 6 m d'ample i 3 m d'alt. Calcula la superfície del terra i el volum de l'aula. Quants litres d'aire hi caben?"), "48 m² · 144 m³ · 144 000 L"),
        (2, Q(2, "L'aquari.", "Un aquari fa 60 cm × 30 cm × 40 cm. Quants litres d'aigua hi caben?"), "72 000 cm³ = 72 L"),
        (3, Q(3, "La piscina.", "Una piscina de 25 m × 12 m té 1,5 m de fondària. a) Quin és el volum en m³ i en L? b) Si una aixeta aboca 20 L cada minut, quantes hores tardaria a omplir-la?"), f"a) 450 m³ = 450 000 L · b) {nf(450000/20/60, 0)} h (més de 15 dies)"),
    ]))
    S.append(("Notació científica i problemes", [
        (1, Q(1, "En notació científica.", "a) 300 000 000 m/s · b) 0,000 005 m · c) 45 000 L · d) 0,02 g · e) 7 800 000 000 persones."), "a) 3 · 10⁸ m/s · b) 5 · 10⁻⁶ m · c) 4,5 · 10⁴ L · d) 2 · 10⁻² g · e) 7,8 · 10⁹"),
        (1, Q(1, "En notació decimal.", "a) 4 · 10³ · b) 2,5 · 10⁻² · c) 1,2 · 10⁶ · d) 6 · 10⁻⁴."), "a) 4 000 · b) 0,025 · c) 1 200 000 · d) 0,000 6"),
        (2, Q(2, "Opera", "en notació científica: a) (2 · 10³) · (4 · 10⁵) · b) (6 · 10⁸) / (3 · 10²) · c) (5 · 10⁻²) · (2 · 10⁶)."), "a) 8 · 10⁸ · b) 2 · 10⁶ · c) 1 · 10⁵"),
        (3, Q(3, "L'aixeta que goteja.", "Una aixeta perd una gota cada 2 segons i cada gota fa 0,05 mL. Quants litres perd en un dia? I en un any? Expressa'l en m³."), f"{nf(86400/2*0.05/1000, 2)} L/dia · {nf(86400/2*0.05/1000*365, 0)} L/any ≈ {nf(86400/2*0.05/1000*365/1000, 2)} m³"),
        (3, Q(3, "Gotes en un metre cúbic.", "Si una gota fa 0,05 mL, quantes gotes hi ha en 1 m³ d'aigua? Expressa-ho en notació científica."), "1 m³ = 10⁶ mL → 2 · 10⁷ gotes"),
    ]))
    return {"sub": "Seguretat i material, magnituds i instruments, factors de conversió, superfície i volum, notació científica.", "seccions": S}

# ======================================================================== SdA 2
def sda2():
    S = []
    S.append(("La massa, el volum i les propietats", [
        (1, Q(1, "General o característica?", "Classifica com a propietat general o característica: massa, densitat, volum, temperatura d'ebullició, temperatura, color, solubilitat. Quines serveixen per identificar una substància?"), "Generals: massa, volum, temperatura · característiques (identifiquen): densitat, temperatura d'ebullició, solubilitat, color (orientatiu)"),
        (1, Q(1, "La tara.", "Un vas buit té una massa de 52,4 g i amb oli, 144,4 g. Quina massa d'oli hi ha?"), "92,0 g"),
        (1, Q(1, "Volum d'un sòlid irregular.", "En una proveta hi ha 40 mL d'aigua. Hi posem una pedra i l'aigua puja a 52 mL. Quin volum té la pedra, en mL i en cm³?"), "12 mL = 12 cm³"),
        (2, Q(2, "Volum d'un sòlid regular.", "Calcula el volum d'un cub de 3 cm d'aresta i d'un prisma de 5 cm × 2 cm × 4 cm."), "27 cm³ · 40 cm³"),
        (1, Q(1, "Massa o pes?", "Un astronauta té una massa de 70 kg a la Terra. Quina massa té a la Lluna? I el pes, és el mateix? Per què?"), "70 kg · el pes és més petit a la Lluna perquè l'atrau menys."),
    ]))
    S.append(("La densitat", [
        (1, Q(1, "Calcula la densitat.", "a) 50 g d'un líquid ocupen 40 mL · b) un cub de 2 cm d'aresta té 64 g · c) 2 kg d'un material ocupen 0,5 L."), "a) 1,25 g/mL · b) 8 g/cm³ · c) 4 g/cm³ = 4 kg/L"),
        (1, Q(1, "Identifica la substància", "amb la taula: un tros de metall de 54 g ocupa 20 cm³; un líquid de 158 g ocupa 200 mL; un sòlid de 9,2 g ocupa 10 cm³.", table=T(["Substància", "d (g/cm³)"], [["Alumini", "2,70"], ["Etanol", "0,79"], ["Gel", "0,92"], ["Ferro", "7,87"], ["Glicerina", "1,26"]])),
         "2,7 g/cm³: alumini · 0,79 g/mL: etanol · 0,92 g/cm³: gel"),
        (2, Q(2, "Calcula la massa.", "Quina massa tenen: a) 2 L d'aigua de mar (1,03 g/mL); b) 250 mL de glicerina (1,26 g/mL); c) un cub de ferro de 5 cm d'aresta (7,87 g/cm³)?"), f"a) 2 060 g · b) 315 g · c) {nf(125*7.87, 1)} g"),
        (2, Q(2, "Calcula el volum.", "Quin volum ocupen: a) 100 g d'etanol (0,79 g/mL); b) 1 kg de gel (0,92 g/cm³); c) 19,3 g d'or (19,3 g/cm³)?"), f"a) {nf(100/0.79, 1)} mL · b) {nf(1000/0.92, 0)} cm³ · c) 1 cm³"),
        (2, Q(2, "La gràfica massa–volum.", "Hem mesurat la massa de diferents volums d'un líquid:", "Dibuixa la gràfica m–V.", "Com és la gràfica?", "Calcula la densitat.", "Quina massa tindrien 100 mL?",
              table=T(["V (mL)", "20", "40", "60", "80"], [["m (g)", "18,4", "36,8", "55,2", "73,6"]])), "b) una recta que passa per l'origen · c) 0,92 g/mL · d) 92 g"),
        (2, Q(2, "Canvia d'unitats.", "Expressa en kg/m³: 1 g/cm³ · 0,79 g/cm³ · 13,6 g/cm³. Expressa en g/cm³: 2 700 kg/m³ · 1,2 kg/m³ (aire)."), "1 000 · 790 · 13 600 kg/m³ · 2,7 · 0,0012 g/cm³"),
        (3, Q(3, "L'aire de l'aula.", "Una aula fa 9 m × 7 m × 3 m. L'aire té una densitat d'1,2 kg/m³. Quina massa d'aire hi ha a l'aula? Compara-la amb la teva."), f"{nf(9*7*3*1.2, 1)} kg"),
        (3, Q(3, "Per què es trenca l'ampolla?", "Omplim una ampolla amb 1 L d'aigua (1,00 g/mL) i la posem al congelador. a) Quina massa d'aigua hi ha? b) Quin volum ocupa quan es converteix en gel (0,92 g/cm³)? c) Per què es pot trencar l'ampolla?"), f"a) 1 000 g · b) {nf(1000/0.92, 0)} cm³ · c) el gel ocupa més volum que l'aigua líquida."),
        (2, Q(2, "L'anell.", "Un anell té una massa de 5,25 g i fa pujar l'aigua d'una proveta 0,5 mL. Pot ser de plata (10,5 g/cm³) o d'or (19,3 g/cm³)?"), "10,5 g/cm³: de plata"),
    ]))
    S.append(("Sura o s'enfonsa?", [
        (1, Q(1, "Prediu.", "Amb la taula de densitats de l'apartat 2, digues què passa a l'aigua amb: un tros de gel, un clau de ferro, un tap de suro (0,24 g/cm³), una gota d'oli (0,92 g/mL) i una gota de glicerina."), "Suren: gel, suro, oli · s'enfonsen: ferro, glicerina"),
        (2, Q(2, "La torre de líquids.", "Tenim mel (1,42 g/mL), oli (0,92 g/mL), aigua (1,00 g/mL), alcohol (0,79 g/mL) i glicerina (1,26 g/mL). En quin ordre quedaran les capes si no es barregen? Què passaria amb l'alcohol i l'aigua?"), "De baix a dalt: mel, glicerina, aigua, oli, alcohol. L'alcohol i l'aigua es barregen (són miscibles)."),
        (2, Q(2, "L'ou que sura.", "Un ou s'enfonsa en aigua de l'aixeta però sura en aigua amb molta sal. Explica per què."), "La sal augmenta la densitat de l'aigua; quan supera la de l'ou (≈ 1,03 g/cm³), l'ou sura."),
        (2, Q(2, "El vaixell d'acer.", "L'acer té una densitat de 7,8 g/cm³. Explica per què sura un vaixell d'acer i per què s'enfonsa si hi entra aigua."), "La seva densitat mitjana (amb l'aire de dins) és menor que la de l'aigua. Si entra aigua, la densitat mitjana augmenta i supera la de l'aigua."),
        (3, Q(3, "La barca de plastilina.", "Una bola de plastilina de 30 g (1,5 g/cm³) s'enfonsa. Amb la mateixa plastilina fem una barca que, amb l'aire de dins, ocupa 50 cm³. a) Calcula el volum de la bola. b) Calcula la densitat mitjana de la barca. c) Sura?"), "a) 20 cm³ · b) 0,6 g/cm³ · c) sí"),
        (2, Q(2, "L'iceberg.", "El gel té una densitat de 0,92 g/cm³ i l'aigua de mar, 1,03 g/cm³. Per què la major part d'un iceberg queda sota l'aigua?"), "Perquè les dues densitats són semblants: com més s'acosta la del cos a la del líquid, més part submergida (≈ 89 %)."),
        (2, Q(2, "Al mar Mort.", "L'aigua del mar Mort té una densitat d'1,24 g/mL i el cos humà, d'uns 1,01 g/cm³. Per què és tan fàcil surar-hi? Suraríem en aigua dolça si omplim els pulmons d'aire?"), "La densitat de l'aigua és molt més gran que la del cos. Sí: amb aire als pulmons la densitat mitjana baixa per sota d'1 g/cm³."),
    ]))
    S.append(("Arquimedes, el densímetre i la ciència", [
        (2, Q(2, "La corona.", "Una corona té una massa de 1 500 g i en submergir-la fa pujar l'aigua 100 cm³. a) Calcula'n la densitat. b) És d'or pur (19,3 g/cm³)? c) Quin seria el volum d'una corona d'or pur de la mateixa massa?"), f"a) 15 g/cm³ · b) no · c) {nf(1500/19.3, 1)} cm³"),
        (2, Q(2, "El densímetre.", "En quin líquid s'enfonsarà més un densímetre: en alcohol, en aigua o en aigua salada? Per què?"), "En alcohol: com menys dens és el líquid, més s'enfonsa."),
        (1, Q(1, "Fet o llegenda?", "De la història d'Arquimedes, quines parts creus que són fets i quines llegenda? Com podríem saber-ho?"), "Fet: el mètode de mesurar el volum per desplaçament. Llegenda probable: sortir nu cridant «Eureka!». Consultant fonts històriques fiables."),
        (2, Q(2, "Biaixos de gènere.", "Què és un biaix de gènere en la ciència? Posa l'exemple d'Hipàtia d'Alexandria i el d'una científica actual que coneguis."), "Oblidar o infravalorar la feina de les dones. Hipàtia, matemàtica i astrònoma; una científica actual (resposta oberta)."),
        (3, Q(3, "Dissenya l'experiment.", "Vols saber si un anell és de plata (10,5 g/cm³). Explica pas a pas com ho comprovaries al laboratori, quins instruments necessites i com calcularies el resultat."), "Balança (massa), proveta amb aigua (volum per desplaçament), d = m / V i comparar-la amb 10,5 g/cm³ (millor amb diverses mesures)."),
    ]))
    return {"sub": "La massa i el volum, la densitat, la flotació i la densitat mitjana, Arquimedes i el densímetre.", "seccions": S}

# ======================================================================== SdA 3
def sda3():
    S = []
    S.append(("Estats de la matèria i model de partícules", [
        (1, Q(1, "Completa la taula.", "Escriu si tenen forma fixa, volum fix i si es poden comprimir els sòlids, els líquids i els gasos."), "Sòlid: forma i volum fixos, no es comprimeix · líquid: volum fix, forma variable, gairebé no · gas: ni forma ni volum fixos, sí"),
        (1, Q(1, "El model.", "Escriu les idees del model de partícules."), "Partícules molt petites · buit entre elles · en moviment, més ràpid com més temperatura · s'atrauen"),
        (2, Q(2, "Vertader o fals?", "Justifica:", "Les partícules d'un sòlid estan quietes.", "Entre les partícules d'un gas hi ha aire.", "En escalfar, les partícules es fan més grans.", "Els gasos es comprimeixen perquè hi ha buit entre les partícules."), "a) F: vibren · b) F: buit · c) F: es mouen més i se separen · d) V"),
        (2, Q(2, "Les xeringues.", "Tenim tres xeringues tapades: una amb aire, una amb aigua i una amb sorra. Quina es pot comprimir? Explica-ho amb el model."), "Només la d'aire: entre les partícules d'un gas hi ha molt de buit."),
        (2, Q(2, "La gota de colorant.", "Una gota de colorant es reparteix més de pressa en aigua calenta que en aigua freda. Explica-ho."), "A més temperatura les partícules es mouen més ràpid i es barregen abans (difusió)."),
        (2, Q(2, "Dibuixa.", "Dibuixa les partícules d'un sòlid, d'un líquid i d'un gas, i indica amb fletxes com es mouen."), "Sòlid ordenat (vibren) · líquid juntes desordenades (llisquen) · gas separades i ràpides en totes direccions"),
    ]))
    S.append(("Canvis d'estat i corbes d'escalfament", [
        (1, Q(1, "Els noms.", "Com es diu el canvi: a) el gel es fon · b) els vidres s'entelen · c) l'aigua del toll desapareix · d) la naftalina desapareix sense fondre's · e) l'aigua es congela."), "a) fusió · b) condensació · c) evaporació (vaporització) · d) sublimació · e) solidificació"),
        (1, Q(1, "Evaporació i ebullició.", "Escriu dues diferències entre l'evaporació i l'ebullició."), "Evaporació: a qualsevol T, només a la superfície · ebullició: a T fixa, a tot el líquid amb bombolles"),
        (2, Q(2, "Quin estat?", "Digues l'estat de cada substància a 25 °C i a −50 °C:", table=T(["Substància", "T de fusió (°C)", "T d'ebullició (°C)"], [["Aigua", "0", "100"], ["Etanol", "−114", "78"], ["Butà", "−138", "−1"], ["Mercuri", "−39", "357"]])),
         "25 °C: aigua, etanol, mercuri líquids; butà gas · −50 °C: aigua i mercuri sòlids; etanol i butà líquids"),
        (2, Q(2, "Llegeix la corba.", "En una corba d'escalfament, la temperatura es manté constant a 80 °C de 5 a 10 minuts i a 218 °C de 20 a 35 minuts. a) Quins canvis d'estat hi ha? b) Quina és la temperatura de fusió i la d'ebullició? c) És una substància pura?"), "a) fusió i ebullició · b) 80 °C i 218 °C · c) sí (trams horitzontals). És el naftalè."),
        (2, Q(2, "Dibuixa la corba.", "Dibuixa la corba d'escalfament de l'aigua des de −10 °C fins a 110 °C i indica l'estat a cada tram."), "Puja fins a 0 °C (sòlid) · horitzontal a 0 °C (sòlid + líquid) · puja fins a 100 °C (líquid) · horitzontal a 100 °C (líquid + gas) · puja (gas)"),
        (3, Q(3, "Per què no puja la temperatura?", "Mentre el gel es fon, encara que l'escalfem, la temperatura es manté a 0 °C. On va l'energia? Com seria la corba d'una mescla d'aigua i sal?"), "Serveix per separar les partícules (vèncer les atraccions). Una mescla no té trams horitzontals: canvia d'estat en un interval de temperatures."),
    ]))
    S.append(("Temperatura i pressió", [
        (1, Q(1, "Kelvin.", "Passa a K: 0 °C · 20 °C · 37 °C · −20 °C · 100 °C. Passa a °C: 300 K · 250 K · 373 K."), "273 · 293 · 310 · 253 · 373 K · 27 · −23 · 100 °C"),
        (1, Q(1, "Unitats de pressió.", "Passa: a) 2 atm a mmHg · b) 1 520 mmHg a atm · c) 0,5 atm a Pa · d) 1 013 hPa a atm."), "a) 1 520 mmHg · b) 2 atm · c) 50 662,5 Pa · d) 1 atm"),
        (2, Q(2, "Què és la pressió?", "Explica amb el model de partícules què és la pressió d'un gas i per què augmenta quan l'escalfem."), "Són els xocs de les partícules contra les parets. En escalfar, es mouen més de pressa: xocs més freqüents i més forts."),
        (2, Q(2, "La pilota freda.", "Explica per què una pilota que ha passat la nit al pati bota menys. Fes un dibuix de les partícules de l'aire de dins al matí i a la tarda."), "Amb fred les partícules es mouen més lentes, xoquen menys: menys pressió i la pilota és més tova."),
    ]))
    S.append(("Les lleis dels gasos", [
        (1, Q(1, "Quina llei?", "a) Un globus s'encongeix a l'aigua amb gel · b) una olla tancada augmenta de pressió quan s'escalfa · c) en prémer una xeringa tapada augmenta la pressió. Què es manté constant en cada cas?"), "a) Charles (P) · b) Gay-Lussac (V) · c) Boyle-Mariotte (T)"),
        (1, Q(1, "Boyle-Mariotte.", "Un gas ocupa 6 L a 1 atm. Quin volum ocuparà a 3 atm a la mateixa temperatura?"), "2 L"),
        (2, Q(2, "La xeringa.", "Una xeringa tapada té 40 mL d'aire a 1 atm. Quina pressió hi haurà si empenyem l'èmbol fins a 10 mL? I fins a 20 mL?"), "4 atm · 2 atm"),
        (2, Q(2, "El globus.", "Un globus té 2,0 L a 27 °C. Quin volum tindrà a 87 °C, a pressió constant? I dins del congelador, a −18 °C?"), f"2,4 L · {nf(2*255/300, 2)} L"),
        (2, Q(2, "El pneumàtic.", "Un pneumàtic té 2,2 atm a 17 °C. Després d'un viatge, la temperatura de l'aire de dins és de 47 °C. Quina pressió té (el volum no canvia)?"), f"{nf(2.2*320/290, 2)} atm"),
        (2, Q(2, "La pilota.", "Una pilota té 1,5 atm a 25 °C. Quina pressió té a 5 °C?"), f"{nf(1.5*278/298, 2)} atm"),
        (3, Q(3, "La taula de dades.", "Hem recollit aquestes dades d'un gas a temperatura constant:", "Comprova la llei de Boyle-Mariotte.", "Quina pressió hi hauria amb 15 mL?", "Dibuixa la gràfica P–V.",
              table=T(["V (mL)", "60", "40", "30", "20"], [["P (atm)", "1,0", "1,5", "2,0", "3,0"]])), "a) P · V = 60 sempre · b) 4,0 atm · c) corba descendent"),
        (3, Q(3, "L'error del kelvin.", "Un alumne calcula la pressió d'una olla tancada que passa de 20 °C a 40 °C i diu que es duplica. Per què s'equivoca? Calcula el resultat correcte si al principi la pressió és d'1 atm."), f"Cal passar a kelvin: {nf(313/293, 2)} atm (augmenta un 7 %)."),
        (2, Q(2, "Charles al revés.", "A quina temperatura (en °C) cal refredar un globus de 3,0 L a 27 °C perquè ocupi 2,5 L?"), "250 K = −23 °C"),
    ]))
    return {"sub": "Els estats i el model de partícules, els canvis d'estat i les corbes, la temperatura, la pressió i les lleis dels gasos.", "seccions": S}

# ======================================================================== SdA 4
def sda4():
    S = []
    S.append(("Substàncies pures i mescles", [
        (1, Q(1, "Classifica", "com a substància pura (element o compost) o mescla (homogènia o heterogènia): aigua destil·lada, aigua de l'aixeta, ferro, aire, amanida, sal, llet, granit, oxigen, vinagre."), "Elements: ferro, oxigen · compostos: aigua destil·lada, sal · homogènies: aigua de l'aixeta, aire, vinagre · heterogènies: amanida, granit (la llet és un col·loide)"),
        (2, Q(2, "Dibuixa", "amb el model de partícules (boletes de colors): un element, un compost, una mescla de dos elements i una mescla d'un element i un compost."), "Element: boles iguals · compost: grups iguals de boles diferents · mescles: partícules de tipus diferents barrejades."),
        (2, Q(2, "Pura o mescla?", "Una substància es fon a 0 °C i bull exactament a 100 °C. Una altra comença a bullir a 101 °C i la temperatura va pujant mentre bull. Quina és pura?"), "La primera (temperatures fixes). La segona és una mescla (aigua amb sal)."),
        (1, Q(1, "L'aigua de l'aixeta.", "Per què diem que l'aigua de l'aixeta és una mescla, encara que sigui transparent? Quines substàncies porta?"), "Porta sals minerals dissoltes (calci, magnesi, sodi…) i una mica de clor: és una mescla homogènia."),
        (1, Q(1, "Element o compost?", "Classifica: O₂, H₂O, Fe, CO₂, NaCl, He, N₂, CH₄."), "Elements: O₂, Fe, He, N₂ · compostos: H₂O, CO₂, NaCl, CH₄"),
    ]))
    S.append(("Dissolucions i concentració", [
        (1, Q(1, "Solut i dissolvent.", "Identifica el solut i el dissolvent: a) aigua amb sucre · b) un refresc amb gas · c) l'aire (78 % nitrogen) · d) el bronze (90 % coure, 10 % estany)."), "a) sucre / aigua · b) CO₂ (i sucre) / aigua · c) oxigen i altres / nitrogen · d) estany / coure"),
        (1, Q(1, "Calcula la concentració", "en g/L: a) 20 g de sal en 500 mL de dissolució · b) 5 g de sucre en 250 mL · c) 0,3 g en 2 L."), "a) 40 g/L · b) 20 g/L · c) 0,15 g/L"),
        (2, Q(2, "Calcula la massa de solut.", "a) Quanta sal hi ha en 3 L d'aigua de mar (35 g/L)? b) Quant de sucre hi ha en una llauna de 330 mL d'un refresc de 105 g/L?"), f"a) 105 g · b) {nf(105*0.33, 1)} g"),
        (2, Q(2, "Calcula el volum.", "Quin volum d'una dissolució de 25 g/L conté 10 g de solut?"), "0,4 L = 400 mL"),
        (2, Q(2, "L'etiqueta de l'aigua.", "Una aigua mineral té 12 mg/L de sodi i 60 mg/L de calci. a) Quants mil·ligrams de calci hi ha en una ampolla d'1,5 L? b) I en grams? c) Quant sodi prens si beus 2 L al dia?"), "a) 90 mg · b) 0,09 g · c) 24 mg"),
        (2, Q(2, "Els nitrats.", "La llei permet com a màxim 50 mg/L de nitrats a l'aigua de boca. Una mostra d'un pou té 0,07 g de nitrats en 1 L. És potable?"), "70 mg/L &gt; 50 mg/L: no és potable."),
        (2, Q(2, "Prepara una dissolució.", "Explica pas a pas com prepararies 250 mL d'una dissolució de sal de 20 g/L. Quina massa de sal necessites?"), "5 g: pesar, dissoldre en poca aigua, passar al matràs aforat de 250 mL, enrasar i agitar."),
        (3, Q(3, "La dilució.", "Tenim 100 mL d'una dissolució de 40 g/L i hi afegim aigua fins a 500 mL. a) Quina massa de solut hi ha? b) Quina és la nova concentració? c) Ha desaparegut part del solut?"), "a) 4 g · b) 8 g/L · c) no: el mateix solut en més volum."),
        (2, Q(2, "Compara.", "Quina dissolució és més concentrada: A) 10 g de sal en 200 mL o B) 30 g de sal en 1 L?"), "A) 50 g/L &gt; B) 30 g/L"),
    ]))
    S.append(("La solubilitat", [
        (1, Q(1, "Saturada?", "Què vol dir que una dissolució està saturada? Com ho pots veure?"), "No admet més solut a aquella temperatura: el que hi afegim queda al fons."),
        (2, Q(2, "Llegeix la corba.", "Amb aquestes dades de solubilitat del nitrat de potassi (g en 100 g d'aigua): a) quant se'n dissol a 40 °C? b) Si dissolem 60 g en 100 g d'aigua a 60 °C i refredem fins a 20 °C, quina massa cristal·litza?",
              table=T(["T (°C)", "0", "20", "40", "60", "80"], [["Solubilitat", "13", "32", "64", "110", "169"]])), "a) 64 g · b) 60 − 32 = 28 g"),
        (2, Q(2, "Els gasos.", "Per què un refresc calent perd el gas abans que un de fred? Per què els peixos ho passen malament quan l'aigua d'un riu s'escalfa?"), "La solubilitat dels gasos disminueix amb la temperatura: el CO₂ s'escapa i hi ha menys oxigen dissolt."),
        (2, Q(2, "Sòlids i temperatura.", "Per què el sucre es dissol millor en llet calenta? És així per a tots els sòlids? Posa un exemple."), "Per a la majoria de sòlids la solubilitat augmenta amb T. La sal gairebé no canvia."),
    ]))
    S.append(("Tècniques de separació i aigua potable", [
        (1, Q(1, "Quina tècnica?", "a) sorra i aigua · b) oli i aigua · c) sal i aigua (vull la sal) · d) sal i aigua (vull l'aigua) · e) llimadures de ferro i sofre · f) grava i sorra."), "a) filtració o decantació · b) embut de decantació · c) evaporació · d) destil·lació · e) imant · f) tamisatge"),
        (2, Q(2, "Separa la mescla.", "Tens una mescla de sorra, sal i llimadures de ferro. Escriu els passos per separar-la i el material."), "1) imant · 2) afegir aigua i remenar (la sal es dissol) · 3) filtrar (sorra al paper) · 4) evaporar el líquid (sal)"),
        (2, Q(2, "La destil·lació.", "Explica com funciona una destil·lació i quina propietat aprofita. Per què l'aigua destil·lada no té sals?"), "Escalfem, el líquid bull, el vapor es refreda al refrigerant i condensa. Aprofita la temperatura d'ebullició. Les sals no s'evaporen i queden al matràs."),
        (2, Q(2, "La potabilitzadora.", "Ordena les etapes d'una potabilitzadora: desinfecció, captació, filtració, decantació, dipòsit. Què fa cadascuna?"), "Captació (agafa l'aigua) → decantació (els fangs es dipositen) → filtració (sorra i carbó actiu) → desinfecció (clor o ozó) → dipòsit"),
        (3, Q(3, "La depuradora casolana.", "Una depuradora de grava, sorra i carbó actiu deixa l'aigua transparent. Per què no la podem beure? Què li falta?"), "No elimina les sals dissoltes ni els microorganismes: caldria desinfectar-la i controlar-ne la composició."),
        (1, Q(1, "Què llencem?", "Digues on s'ha de llençar: oli de cuinar, tovalloletes, medicaments, restes de pintura, aigua amb sabó."), "Oli: deixalleria · tovalloletes: brossa · medicaments: farmàcia (SIGRE) · pintura: deixalleria · aigua amb sabó: aigüera"),
        (2, Q(2, "Les salines.", "Com s'obté la sal a les salines? Quina tècnica de separació és? Quina propietat aprofita?"), "S'evapora l'aigua de mar amb el sol i el vent i la sal cristal·litza: evaporació i cristal·lització (l'aigua s'evapora i la sal no)."),
    ]))
    return {"sub": "Substàncies pures i mescles, dissolucions i concentració, solubilitat, tècniques de separació i l'aigua potable.", "seccions": S}

# ======================================================================== SdA 5
def sda5():
    S = []
    S.append(("Canvis físics i canvis químics", [
        (1, Q(1, "Físic o químic?", "a) fondre xocolata · b) torrar pa · c) dissoldre sucre · d) coure un ou · e) trencar un got · f) un clau que es rovella · g) bullir aigua · h) la llet que es fa iogurt."), "Físics: a, c, e, g · químics: b, d, f, h"),
        (1, Q(1, "Evidències.", "Quina evidència de canvi químic hi ha en cada cas? a) el bicarbonat i el vinagre fan bombolles · b) la poma tallada s'enfosqueix · c) un llumí s'encén · d) la llet agra fa mala olor."), "a) gas · b) canvi de color · c) llum i calor · d) olor nova"),
        (2, Q(2, "Compte amb les evidències.", "Quan bullim aigua surten bombolles. Vol dir que és un canvi químic? Per què una sola evidència no sempre és suficient?"), "No: és vapor d'aigua (canvi físic). Cal pensar si s'ha format una substància nova."),
        (2, Q(2, "El sucre que es crema.", "Explica la diferència entre fondre sucre i caramel·litzar-lo. Quin és físic i quin químic? Com ho saps?"), "Fondre: físic (continua sent sucre, en refredar torna a ser sòlid i dolç). Caramel·litzar: químic (color marró, olor i gust nous)."),
    ]))
    S.append(("La reacció química", [
        (1, Q(1, "Reactius i productes.", "Identifica els reactius i els productes: a) carbó + oxigen → diòxid de carboni · b) ferro + oxigen + aigua → rovell · c) bicarbonat + vinagre → acetat de sodi + aigua + diòxid de carboni."), "Reactius a l'esquerra de la fletxa; productes a la dreta."),
        (2, Q(2, "Escriu la reacció", "amb paraules: a) el metà crema amb l'oxigen i forma diòxid de carboni i aigua; b) el llevat transforma el sucre en diòxid de carboni i alcohol."), "a) metà + oxigen → diòxid de carboni + aigua · b) sucre → diòxid de carboni + alcohol"),
        (2, Q(2, "Els àtoms es reorganitzen.", "En la reacció hidrogen + oxigen → aigua, compta els àtoms abans i després en el model: 2 molècules d'hidrogen (H₂) i 1 d'oxigen (O₂) formen 2 molècules d'aigua (H₂O). Hi ha els mateixos àtoms?"), "Sí: 4 H i 2 O abans i després."),
        (3, Q(3, "Dibuixa el model", "de la reacció del carboni amb l'oxigen: C + O₂ → CO₂. Fes servir boles de colors i comprova que es conserven els àtoms."), "1 C i 2 O abans i després; només canvien els enllaços."),
        (2, Q(2, "Vertader o fals?", "Justifica:", "En una reacció química es creen àtoms nous.", "Els productes tenen propietats diferents dels reactius.", "Totes les reaccions són ràpides.", "Cremar un paper és una reacció química."), "a) F: es reorganitzen · b) V · c) F · d) V"),
    ]))
    S.append(("La conservació de la massa", [
        (1, Q(1, "Calcula.", "a) 12 g de carboni reaccionen amb 32 g d'oxigen. Quant diòxid de carboni es forma? b) 56 g de ferro i 32 g de sofre formen sulfur de ferro. Quina massa se n'obté?"), "a) 44 g · b) 88 g"),
        (1, Q(1, "Quin reactiu falta?", "En una reacció es formen 18 g d'aigua a partir de 2 g d'hidrogen. Quanta massa d'oxigen ha reaccionat?"), "16 g"),
        (2, Q(2, "El clau rovellat.", "Un clau de 10,0 g es rovella i passa a 10,6 g. S'ha creat massa? Explica d'on surt la massa que ha guanyat."), "No: el ferro s'ha combinat amb oxigen (i aigua) de l'aire, 0,6 g."),
        (2, Q(2, "Lavoisier i el globus.", "Fem reaccionar bicarbonat i vinagre en un got obert sobre la balança: abans 150,0 g i després 148,9 g. En una ampolla tancada amb un globus: 152,4 g i 152,4 g. Explica els dos resultats."), "Obert: s'escapen 1,1 g de CO₂. Tancat: el gas queda dins i la massa es conserva."),
        (3, Q(3, "La foguera.", "Cremem 10 kg de fusta i queden 0,2 kg de cendres. On és la resta de massa? La massa dels productes és més petita, igual o més gran que 10 kg? Per què?"), "A l'aire, com a CO₂ i vapor d'aigua. Els productes pesen més de 10 kg perquè també hi ha l'oxigen que ha reaccionat."),
    ]))
    S.append(("La velocitat de les reaccions", [
        (1, Q(1, "Ràpida o lenta?", "Ordena de més ràpida a més lenta: el rovell d'un clau, l'explosió d'un petard, la fermentació del raïm, la combustió d'un llumí."), "Petard → llumí → fermentació → rovell"),
        (2, Q(2, "Quin factor?", "Quin factor explica cada cas? a) Guardem la llet a la nevera · b) els trossos petits de llenya s'encenen abans que un tronc · c) el vinagre fort reacciona més de pressa · d) els enzims del cos fan anar les reaccions molt ràpid."), "a) temperatura · b) superfície de contacte · c) concentració · d) catalitzador"),
        (2, Q(2, "El llevat.", "Posem llevat amb sucre i aigua en tres ampolles amb un globus: a 10 °C, a 35 °C i a 70 °C. Quin globus s'inflarà més? Per què el de 70 °C gairebé no s'infla?"), "El de 35 °C. A 70 °C els fongs del llevat moren."),
        (3, Q(3, "Dissenya l'experiment.", "Vols comprovar si la mida dels trossos influeix en la velocitat de la reacció entre el marbre i el vinagre. Quina és la variable independent, la dependent i les controlades?"), "Independent: mida dels trossos · dependent: temps o gas que es desprèn · controlades: massa de marbre, volum i concentració del vinagre, temperatura."),
        (2, Q(2, "La pastilla efervescent.", "Una pastilla efervescent sencera triga 60 s a dissoldre's en aigua a 20 °C. Prediu si trigarà més o menys: a) triturada · b) en aigua a 50 °C · c) en aigua amb gel. Justifica-ho."), "a) menys (més superfície) · b) menys (més T) · c) més (menys T)"),
    ]))
    S.append(("Química de la cuina, combustió i seguretat", [
        (1, Q(1, "Maillard o caramel·lització?", "a) la crosta del pa · b) el sucre que es fa caramel · c) la carn a la planxa · d) les galetes daurades."), "a) Maillard · b) caramel·lització · c) Maillard · d) Maillard (i caramel·lització)"),
        (2, Q(2, "El triangle del foc.", "Quins són els tres costats del triangle del foc? Quin costat treus en cada cas? a) tapar una paella que crema · b) fer un tallafocs · c) tirar aigua a una foguera."), "Combustible, oxigen i calor · a) oxigen · b) combustible · c) calor"),
        (2, Q(2, "Per què no aigua?", "Per què no s'ha de tirar mai aigua a una paella d'oli encesa ni a un aparell endollat que crema?"), "L'aigua bull de cop i escampa l'oli encès; en un aparell, l'aigua condueix el corrent (electrocució)."),
        (2, Q(2, "El monòxid de carboni.", "Quan es forma el monòxid de carboni? Per què és tan perillós? Com el podem evitar?"), "En combustions amb poc oxigen. És tòxic i no fa olor. Ventilant i revisant els aparells de gas."),
        (2, Q(2, "Conservar aliments.", "Explica per què cada mètode alenteix que els aliments es facin malbé: nevera, assecar, pasteuritzar, envasar al buit."), "Fred (reaccions més lentes), sense aigua (no hi creixen microorganismes), calor que mata microorganismes, sense oxigen."),
        (3, Q(3, "Productes de neteja.", "Per què no s'han de barrejar mai el lleixiu i l'amoníac (o el lleixiu i el salfumant)? Quines normes segueixes per fer servir productes de neteja?"), "Desprenen gasos tòxics (cloramines, clor). Llegir l'etiqueta, no barrejar, ventilar, guardar-los a l'envàs original lluny dels infants."),
    ]))
    return {"sub": "Canvis físics i químics, la reacció química, la conservació de la massa, la velocitat de les reaccions, la combustió i la química de casa.", "seccions": S}

# ======================================================================== SdA 6
def sda6():
    S = []
    S.append(("L'energia: formes, transformacions i unitats", [
        (1, Q(1, "Formes d'energia.", "Quina forma d'energia té: a) una bicicleta en moviment · b) l'aigua d'un embassament · c) un entrepà · d) una molla comprimida · e) el Sol · f) la sopa calenta?"), "a) cinètica · b) potencial · c) química · d) elàstica · e) lluminosa (i nuclear) · f) tèrmica"),
        (1, Q(1, "Transformacions.", "Escriu la transformació d'energia: a) una torradora · b) un ventilador · c) una placa solar · d) una llanterna amb pila · e) una persona que puja escales."), "a) elèctrica → tèrmica · b) elèctrica → cinètica · c) lluminosa → elèctrica · d) química → elèctrica → lluminosa · e) química → potencial"),
        (2, Q(2, "Unitats.", "Passa: a) 200 kcal a kJ · b) 5 kWh a J · c) 8 360 J a kcal · d) 7,2 · 10⁶ J a kWh."), f"a) 836 kJ · b) 1,8 · 10⁷ J · c) 2 kcal · d) 2 kWh"),
        (2, Q(2, "Conservació i degradació.", "Si l'energia es conserva, per què diem que «gastem» energia? Explica-ho amb una bombeta antiga i una LED."), "Una part acaba com a calor que s'escampa i no podem aprofitar (es degrada). La LED en converteix més en llum."),
    ]))
    S.append(("Calor, temperatura i equilibri tèrmic", [
        (1, Q(1, "Calor o temperatura?", "Completa amb calor o temperatura: a) La ___ es mesura amb un termòmetre. b) La ___ passa del cos calent al fred. c) La ___ es mesura en joules. d) La ___ indica com es mouen les partícules."), "a) temperatura · b) calor · c) calor · d) temperatura"),
        (2, Q(2, "Vertader o fals?", "Justifica:", "Un jersei ens dona calor.", "La barana de metall és més freda que la de fusta, al mateix lloc.", "Dos cossos en contacte arriben a la mateixa temperatura.", "La calor passa del fred al calent."), "a) F: evita que perdem calor · b) F: estan a la mateixa T, però el metall condueix més i ens treu calor més de pressa · c) V · d) F"),
        (2, Q(2, "Prediu la temperatura.", "Barregem 200 g d'aigua a 80 °C amb 200 g d'aigua a 20 °C. Quina temperatura final esperes? I si fossin 100 g a 80 °C i 300 g a 20 °C?"), "50 °C · 35 °C"),
        (2, Q(2, "La sopa a la carmanyola.", "Explica què passa amb les partícules de la sopa i de l'aire mentre la sopa es refreda. Quan s'atura el procés?"), "Les partícules de la sopa s'alenteixen i les de l'aire s'acceleren; s'atura quan arriben a la mateixa temperatura (equilibri tèrmic)."),
    ]))
    S.append(("Calcular la calor", [
        (1, Q(1, "La sopa.", "Quanta calor cal per escalfar 0,5 kg de sopa (c = 4 180 J/(kg·°C)) de 20 °C a 70 °C?"), f"{nf(0.5*4180*50, 0)} J ≈ {nf(0.5*4180*50/1000, 1)} kJ"),
        (2, Q(2, "Oli o aigua?", "Escalfem 1 kg d'aigua i 1 kg d'oli (c = 1 970 J/(kg·°C)) amb 41 800 J cadascun. Quant augmenta la temperatura de cada un? Quin s'escalfa més?"), f"Aigua: 10 °C · oli: {nf(41800/1970, 1)} °C (l'oli)"),
        (2, Q(2, "La paella.", "Una paella de ferro de 1,2 kg (c = 450 J/(kg·°C)) passa de 20 °C a 180 °C. Quanta calor ha absorbit?"), f"{nf(1.2*450*160, 0)} J"),
        (2, Q(2, "Calor perduda.", "La sopa d'una carmanyola (0,4 kg) passa de 75 °C a 40 °C. Quanta calor perd? Per què surt negativa?"), f"Q = {nf(0.4*4180*-35, 0)} J: és calor que perd."),
        (3, Q(3, "Quina massa?", "Amb 167 200 J, quanta aigua podem escalfar de 20 °C a 60 °C?"), "1 kg"),
        (3, Q(3, "El clima.", "Per què a Barcelona les temperatures són més suaus que a Lleida? Relaciona-ho amb la calor específica de l'aigua."), "L'aigua té una c molt alta: el mar s'escalfa i es refreda a poc a poc i suavitza la temperatura de la costa."),
        (2, Q(2, "La dutxa.", "Una dutxa fa servir 40 kg d'aigua que s'escalfa de 15 °C a 40 °C. Quanta energia cal? Passa-la a kWh (1 kWh = 3,6 · 10⁶ J)."), f"{nf(40*4180*25, 0)} J ≈ {nf(40*4180*25/3.6e6, 2)} kWh"),
    ]))
    S.append(("Com es transmet la calor", [
        (1, Q(1, "Conducció, convecció o radiació?", "a) el mànec d'una cullera s'escalfa · b) l'aire calent puja per sobre del radiador · c) notem la calor del Sol · d) l'aigua d'una olla circula · e) ens cremem amb una paella."), "a) conducció · b) convecció · c) radiació · d) convecció · e) conducció"),
        (1, Q(1, "Conductor o aïllant?", "Coure, fusta, plàstic, alumini, llana, aire quiet, acer, suro, porexpan."), "Conductors: coure, alumini, acer · aïllants: fusta, plàstic, llana, aire quiet, suro, porexpan"),
        (2, Q(2, "El termo.", "Explica com evita el termo la conducció, la convecció i la radiació."), "Buit entre parets (sense conducció ni convecció), tap aïllant (convecció), parets platejades (reflecteixen la radiació)."),
        (2, Q(2, "Dissenya la carmanyola.", "Tria materials per fer una carmanyola que mantingui calenta la sopa i justifica cada tria amb les tres maneres de transmetre la calor."), "Resposta oberta: capa d'aire o porexpan (conducció), tapa ben tancada (convecció), paper d'alumini brillant (radiació)."),
        (2, Q(2, "Roba d'estiu.", "Per què a l'estiu ens vestim amb roba de colors clars?"), "Els colors clars reflecteixen més la radiació del Sol i absorbeixen menys."),
    ]))
    S.append(("Aïllament, fonts d'energia i estalvi", [
        (2, Q(2, "La casa.", "Per on perd més calor una casa sense aïllar? Proposa tres mesures per aïllar-la."), "Teulada i parets (també finestres i escletxes). Aïllar la teulada i les parets, doble vidre, tapar escletxes."),
        (1, Q(1, "Renovable o no?", "Solar, petroli, eòlica, gas natural, hidràulica, carbó, biomassa, urani."), "Renovables: solar, eòlica, hidràulica, biomassa · no renovables: petroli, gas natural, carbó, urani"),
        (2, Q(2, "Avantatges i inconvenients.", "Escriu un avantatge i un inconvenient de l'energia eòlica i del carbó."), "Eòlica: no emet CO₂ / depèn del vent · carbó: produeix quan cal / emet molt CO₂ i contamina"),
        (3, Q(3, "Estalvi a l'institut.", "Classifica aquestes mesures en hàbits, eficiència o renovables: a) apagar els llums al pati · b) canviar els fluorescents per LED · c) posar plaques solars · d) tancar les portes amb la calefacció · e) aïllar el terrat. Quina et sembla més important? Argumenta-ho."), "Hàbits: a, d · eficiència: b, e · renovables: c. Argumentació oberta."),
        (2, Q(2, "Els combustibles fòssils.", "Per què cremar petroli, carbó i gas contribueix al canvi climàtic? Què vol dir transició energètica?"), "Emeten CO₂, que augmenta l'efecte d'hivernacle. Passar a fonts renovables i gastar menys energia."),
    ]))
    return {"sub": "Formes i transformacions de l'energia, calor i temperatura, calcular la calor, la propagació de la calor, l'aïllament i les fonts d'energia.", "seccions": S}

FUNCS = {1: sda1, 2: sda2, 3: sda3, 4: sda4, 5: sda5, 6: sda6}
