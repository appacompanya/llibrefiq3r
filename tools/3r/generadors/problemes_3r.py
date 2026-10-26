"""Dossiers de problemes de 3r d'ESO (exercicis del tipus de les fitxes de cada SdA)."""
from gen_problemes import Q, nf
from gen_teoria import T

# ======================================================================== SdA 1
def sda1():
    S = []
    S.append(("Magnituds i unitats", [
        (1, Q(1, "Magnitud o no?", "Indica quines d'aquestes propietats són magnituds i, per a les que ho siguin, escriu-ne la unitat del SI: la massa, la simpatia, el volum, el color, la temperatura, el temps, la bellesa, la densitat."),
         "Magnituds: massa (kg), volum (m³), temperatura (K), temps (s), densitat (kg/m³). No ho són: simpatia, color, bellesa."),
        (1, Q(1, "Fonamental o derivada?", "Classifica com a fonamentals o derivades: longitud, superfície, massa, velocitat, temps, volum, intensitat de corrent, densitat. Per a les derivades, escriu com s'obtenen a partir de les fonamentals."),
         "Fonamentals: longitud, massa, temps, intensitat de corrent. Derivades: superfície (L·L), velocitat (L/t), volum (L·L·L), densitat (m/V)."),
        (1, Q(1, "Prefixos.", "Escriu l'equivalència en metres o en grams: 1 km · 1 cm · 1 mm · 1 µm · 1 mg · 1 kg · 1 hm · 1 dg."),
         "1 000 m · 0,01 m · 0,001 m · 10⁻⁶ m · 0,001 g · 1 000 g · 100 m · 0,1 g"),
        (2, Q(2, "L'instrument adequat.", "Quin instrument faries servir i amb quina unitat donaries el resultat per mesurar: a) el volum d'una cullerada de xarop; b) la massa d'un anell; c) la llargada del pati; d) el temps que triga a bullir l'aigua; e) la temperatura d'una sopa?"),
         "a) xeringa o pipeta, mL · b) balança, g · c) cinta mètrica, m · d) cronòmetre, s o min · e) termòmetre, °C"),
    ]))
    S.append(("Canvis d'unitats amb factors de conversió", [
        (1, Q(1, "Un sol factor.", "Expressa amb un factor de conversió:", "3,5 km en m", "250 mL en L", "4,2 kg en g", "45 min en h", "0,75 L en cm³"),
         "a) 3 500 m · b) 0,25 L · c) 4 200 g · d) 0,75 h · e) 750 cm³"),
        (2, Q(2, "Factors encadenats.", "Expressa:", "2 h en s", "3,6 · 10⁶ mm en km", "1 dia en minuts", "5 000 cm² en m²"),
         "a) 7 200 s · b) 3,6 km · c) 1 440 min · d) 0,5 m²"),
        (2, Q(2, "Unitats compostes.", "Passa a unitats del SI:", "108 km/h", "1,2 g/mL", "0,79 g/cm³", "36 km/h"),
         "a) 30 m/s · b) 1 200 kg/m³ · c) 790 kg/m³ · d) 10 m/s"),
        (2, Q(2, "I al revés.", "Expressa 25 m/s en km/h i 2 700 kg/m³ en g/cm³."), "90 km/h · 2,7 g/cm³"),
        (3, Q(3, "Quina és més ràpida?", "Ordena de més lenta a més ràpida: una tortuga que fa 0,30 km/h, un caragol que fa 1,5 mm/s i una formiga que recorre 10 m en 5 minuts. Fes servir factors de conversió per passar-ho tot a m/s."),
         f"Tortuga: {nf(0.3/3.6, 3)} m/s · caragol: 0,0015 m/s · formiga: {nf(10/300, 3)} m/s. Ordre: caragol &lt; formiga &lt; tortuga."),
    ]))
    S.append(("Notació científica i xifres significatives", [
        (1, Q(1, "Escriu en notació científica:", "a) 150 000 000 km (distància Terra–Sol) · b) 0,000 000 1 m (mida d'un virus) · c) 602 000 · d) 0,004 5 g."),
         "a) 1,5 · 10⁸ km · b) 1 · 10⁻⁷ m · c) 6,02 · 10⁵ · d) 4,5 · 10⁻³ g"),
        (1, Q(1, "Escriu en notació decimal:", "a) 3,2 · 10⁴ · b) 7 · 10⁻³ · c) 1,05 · 10⁶ · d) 2,5 · 10⁻⁵."), "a) 32 000 · b) 0,007 · c) 1 050 000 · d) 0,000 025"),
        (2, Q(2, "Opera", "i dona el resultat en notació científica: a) (3 · 10⁵) · (2 · 10³) · b) (8 · 10⁶) / (4 · 10²) · c) (5 · 10⁻³) · (6 · 10⁻²) · d) (9 · 10⁴) / (3 · 10⁻²)."),
         "a) 6 · 10⁸ · b) 2 · 10⁴ · c) 3 · 10⁻⁴ · d) 3 · 10⁶"),
        (2, Q(2, "Xifres significatives.", "Quantes xifres significatives té cada mesura? a) 12,40 g · b) 0,0052 m · c) 305 mL · d) 2,0 · 10³ kg. Si divideixes 15,2 g entre 3,0 mL a la calculadora surt 5,0666667: com has d'escriure el resultat?"),
         "a) 4 · b) 2 · c) 3 · d) 2. Resultat: 5,1 g/mL (dues xifres significatives, com 3,0)."),
    ]))
    S.append(("La mesura i els errors", [
        (1, Q(1, "Llegeix la proveta.", "Una proveta té ratlles cada 2 mL i el menisc queda entre les ratlles de 46 mL i 48 mL, més a prop de la de 48. Quina és la sensibilitat de la proveta? Quin volum escriuries? On has de posar els ulls?"),
         "Sensibilitat 2 mL; uns 48 mL (47–48 mL); a l'altura de la part de baix del menisc."),
        (2, Q(2, "Sistemàtic o aleatori?", "Classifica cada error: a) la balança marca 0,3 g sense res a sobre; b) quan fem cinc vegades la mateixa mesura de temps, uns cops surt més i uns cops menys; c) sempre llegim la proveta mirant des de dalt; d) el corrent d'aire fa oscil·lar la balança. Com reduiries cada un?"),
         "a) sistemàtic (calibrar/tarar) · b) aleatori (repetir i fer la mitjana) · c) sistemàtic (llegir a l'altura del menisc) · d) aleatori (tancar la finestra, repetir)."),
        (2, Q(2, "La mitjana i l'error.", "Cinc grups mesuren la densitat d'un líquid i obtenen 0,81 · 0,79 · 0,80 · 0,95 · 0,80 g/mL. a) Hi ha algun valor que s'hauria de descartar? b) Calcula la mitjana dels valors vàlids. c) Si el valor de referència és 0,79 g/mL, calcula l'error absolut i l'error relatiu."),
         f"a) 0,95 · b) {nf((0.81+0.79+0.80+0.80)/4, 3)} g/mL · c) Eₐ = {nf((0.81+0.79+0.80+0.80)/4-0.79, 3)} g/mL; Eᵣ = {nf(((0.81+0.79+0.80+0.80)/4-0.79)/0.79*100, 1)} %"),
        (3, Q(3, "Exacta o precisa?", "Dos alumnes mesuren tres vegades la massa d'una moneda de 7,50 g. L'Arnau obté 7,49 · 7,51 · 7,50 g i la Fàtima, 7,82 · 7,81 · 7,83 g. Quines mesures són precises? Quines són exactes? Quin tipus d'error pot tenir la balança de la Fàtima?"),
         "Les dues sèries són precises; només les de l'Arnau són exactes. La de la Fàtima té un error sistemàtic (≈ +0,32 g: balança mal calibrada)."),
    ]))
    S.append(("La densitat", [
        (1, Q(1, "Calcula la densitat", "d'un cub de 2 cm d'aresta que té una massa de 21,6 g. De quin material pot ser? (alumini 2,7 g/cm³, ferro 7,9 g/cm³, plom 11,3 g/cm³)"), "V = 8 cm³; ρ = 2,7 g/cm³: alumini."),
        (1, Q(1, "Massa i volum.", "Quina massa té 1,5 L d'oli (ρ = 0,92 g/mL)? Quin volum ocupen 500 g d'etanol (ρ = 0,79 g/mL)?"), f"1 380 g · {nf(500/0.79, 0)} mL"),
        (2, Q(2, "El pot buit i el pot ple.", "Un pot buit té una massa de 48,2 g. Ple d'un líquid desconegut, 127,2 g. El volum del pot és de 100 mL. Calcula la densitat del líquid i digues si pot ser aigua (1,00 g/mL), etanol (0,79 g/mL) o glicerina (1,26 g/mL)."),
         "m = 79,0 g; ρ = 0,790 g/mL: pot ser etanol."),
        (2, Q(2, "El desplaçament.", "En una proveta hi ha 60,0 mL d'aigua. Hi submergim una peça metàl·lica de 89,0 g i l'aigua puja fins a 70,0 mL. Calcula la densitat de la peça i expressa-la en kg/m³."),
         "V = 10,0 cm³; ρ = 8,90 g/cm³ = 8 900 kg/m³ (pot ser coure)."),
        (2, Q(2, "Sura o s'enfonsa?", "Tenim tres objectes de densitats 0,24 g/cm³ (suro), 0,92 g/cm³ (gel) i 1,38 g/cm³ (plàstic PET). Què passa amb cadascun a l'aigua? I a l'oli (0,92 g/cm³)?"),
         "A l'aigua: suro i gel suren, el PET s'enfonsa. A l'oli: el suro sura, el gel queda en equilibri (densitat igual) i el PET s'enfonsa."),
        (3, Q(3, "Proves convergents.", "Un líquid incolor té una densitat de 0,80 g/mL. Per què no podem assegurar que és etanol només amb aquesta dada? Quines altres proves faries per confirmar-ho?"),
         "Altres líquids poden tenir densitats semblants i l'etanol amb aigua en té una de diferent. Altres proves: miscibilitat amb aigua, temperatura d'ebullició (78 °C), conductivitat, combustió…"),
    ]))
    S.append(("Mescles, dissolucions i separació", [
        (1, Q(1, "Classifica", "com a element, compost, mescla homogènia o mescla heterogènia: aigua destil·lada, aire, granit, oxigen, aigua de mar, sal de cuina, llet amb cereals, coure, vinagre, oli i aigua."),
         "Elements: oxigen, coure · Compostos: aigua destil·lada, sal · Homogènies: aire, aigua de mar, vinagre · Heterogènies: granit, llet amb cereals, oli i aigua."),
        (2, Q(2, "Concentració.", "Dissolem 15 g de sal en aigua fins a obtenir 250 mL de dissolució. a) Quin és el solut i quin el dissolvent? b) Calcula la concentració en g/L. c) Quina massa de sal hi ha en 40 mL d'aquesta dissolució?"),
         "a) Solut: sal; dissolvent: aigua · b) 60 g/L · c) 2,4 g"),
        (2, Q(2, "Quina tècnica?", "Proposa la tècnica de separació i la propietat en què es basa: a) llimadures de ferro i sorra; b) oli i aigua; c) sorra i aigua salada; d) la sal de l'aigua salada; e) els pigments d'una tinta."),
         "a) imant (magnetisme) · b) embut de decantació (densitat, no miscibles) · c) filtració (mida) · d) evaporació/cristal·lització (l'aigua s'evapora) · e) cromatografia (avancen diferent)."),
        (3, Q(3, "Planifica una separació.", "Tens una mescla de sorra, sal, serradures i llimadures de ferro. Escriu, en ordre, els passos per separar els quatre components i el material que necessites."),
         "1) Imant (ferro). 2) Aigua: les serradures suren (flotació, les recollim). 3) Remenar perquè es dissolgui la sal i filtrar (sorra al paper). 4) Evaporar el filtrat (sal)."),
    ]))
    S.append(("Conductivitat, canvis i seguretat", [
        (2, Q(2, "Condueix o no?", "Expliquen per què l'aigua salada encén el LED d'un circuit i l'aigua amb sucre no. Escriu l'equació de la dissociació del clorur de sodi."),
         "La sal es dissocia en ions que es mouen i transporten la càrrega; el sucre es dissol però no forma ions. NaCl → Na⁺ + Cl⁻."),
        (1, Q(1, "Físic o químic?", "a) Fondre gel · b) cremar paper · c) dissoldre sucre · d) rovellar-se un clau · e) trencar un got · f) un clau de ferro que es recobreix de coure en sulfat de coure. Justifica dos dels casos amb evidències."),
         "Físics: a, c, e · Químics: b, d, f (es formen substàncies noves: canvi de color, gas, calor…)."),
        (1, Q(1, "Pictogrames.", "Què vol dir cada pictograma: flama, calavera, corrosió (mà i superfície que es desfan), signe d'exclamació, medi ambient (peix i arbre)? Posa un producte de casa que pugui portar cadascun."),
         "Inflamable (alcohol), toxicitat aguda (alguns raticides), corrosiu (desembussador, lleixiu), perill per a la salut/irritant (detergents), perill per al medi ambient (alguns insecticides)."),
    ]))
    return {"sub": "Magnituds i unitats, factors de conversió, notació científica, mesura i errors, densitat, mescles i separació, canvis i seguretat.", "seccions": S}

# ======================================================================== SdA 2
def sda2():
    S = []
    S.append(("El model cineticomolecular", [
        (1, Q(1, "Els postulats.", "Escriu els quatre postulats del model cineticomolecular."), "Partícules molt petites · entre elles hi ha buit · es mouen contínuament, més de pressa com més temperatura · s'atrauen (més com més a prop)."),
        (1, Q(1, "Vertader o fals?", "Justifica-ho amb el model:", "Quan escalfem un gas, les partícules es fan més grans.", "Entre les partícules d'un gas hi ha aire.", "En un sòlid, les partícules estan quietes.", "Els gasos es poden comprimir perquè hi ha molt de buit entre les partícules."),
         "a) F: es mouen més de pressa i se separen · b) F: hi ha buit · c) F: vibren · d) V."),
        (2, Q(2, "Explica amb el model", "per què: a) sentim l'olor d'un perfum a l'altra punta de l'aula; b) una gota de colorant es reparteix més de pressa en aigua calenta; c) una xeringa tapada plena d'aire es pot comprimir, però una plena d'aigua gairebé no."),
         "a) difusió: les partícules es mouen i es barregen amb les de l'aire · b) a més temperatura es mouen més ràpid · c) en un gas hi ha molt de buit; en un líquid les partícules estan juntes."),
        (2, Q(2, "Dibuixa", "les partícules d'un sòlid, un líquid i un gas, i indica amb fletxes com es mouen. Afegeix una frase que expliqui la forma i el volum de cada estat."),
         "Sòlid ordenat i juntes (vibren): forma i volum fixos · líquid juntes i desordenades (llisquen): volum fix · gas separades i ràpides: ni forma ni volum fixos."),
    ]))
    S.append(("Temperatura i pressió", [
        (1, Q(1, "Kelvin i Celsius.", "Passa a kelvin: 0 °C · 25 °C · 100 °C · −40 °C · −273 °C. Passa a graus Celsius: 300 K · 373 K · 77 K."), "273 K · 298 K · 373 K · 233 K · 0 K · 27 °C · 100 °C · −196 °C"),
        (1, Q(1, "Unitats de pressió.", "Expressa: a) 2 atm en mmHg · b) 380 mmHg en atm · c) 1,5 atm en Pa · d) 1 013 hPa en atm."), "a) 1 520 mmHg · b) 0,5 atm · c) 151 988 Pa ≈ 1,52 · 10⁵ Pa · d) ≈ 1 atm"),
        (2, Q(2, "Què és la pressió d'un gas?", "Explica-ho amb el model i digues dues maneres d'augmentar la pressió d'un gas tancat."), "Són els xocs de les partícules contra les parets. Augmenta si escalfem (xocs més forts i freqüents) o si reduïm el volum (xocs més freqüents) o hi afegim gas."),
        (2, Q(2, "El globus al congelador.", "Un globus inflat a l'aula es fa més petit al congelador. Explica què passa amb les partícules i fes un dibuix abans i després."), "Es mouen més a poc a poc, xoquen menys i amb menys força: la pressió de dins baixa i el globus es contrau fins que s'iguala amb la de fora."),
        (2, Q(2, "Calcula la pressió.", "Una persona de 600 N es recolza sobre dues sabates de 150 cm² cadascuna. Quina pressió fa sobre el terra, en Pa? I si es posa de puntetes sobre 20 cm² en total?"), "20 000 Pa · 300 000 Pa"),
    ]))
    S.append(("Les lleis dels gasos", [
        (1, Q(1, "Quina llei?", "Digues quina llei explica cada situació i què es manté constant: a) un pneumàtic té més pressió després d'un viatge llarg; b) un globus s'infla si el posem al sol; c) en prémer l'èmbol d'una xeringa tapada, l'aire es comprimeix i costa més prémer."),
         "a) Gay-Lussac (V constant) · b) Charles (P constant) · c) Boyle-Mariotte (T constant)"),
        (1, Q(1, "Boyle-Mariotte.", "Un gas ocupa 4,0 L a 1,0 atm. Quin volum ocuparà a 2,0 atm, si la temperatura no canvia?"), "2,0 L"),
        (2, Q(2, "La xeringa.", "Una xeringa conté 60 mL d'aire a 1,0 atm. La tapem i empenyem l'èmbol fins a 20 mL. Quina és la pressió? I si l'estirem fins a 90 mL?"), "3,0 atm · 0,67 atm"),
        (2, Q(2, "Charles.", "Un globus té un volum de 2,5 L a 20 °C. Quin volum tindrà si l'escalfem fins a 60 °C a pressió constant?"), f"{nf(2.5*333/293, 2)} L"),
        (2, Q(2, "Gay-Lussac.", "Un esprai té una pressió de 3,0 atm a 20 °C. Quina pressió tindrà dins d'un cotxe a 60 °C? I si arriba a 300 °C en un foc?"), f"{nf(3*333/293, 2)} atm · {nf(3*573/293, 1)} atm (pot explotar)"),
        (2, Q(2, "La bombolla del submarinista.", "Una bombolla d'aire de 1,5 cm³ surt d'un submarinista on la pressió és de 4 atm. Quin volum tindrà en arribar a la superfície (1 atm), si la temperatura no canvia?"), "6,0 cm³"),
        (3, Q(3, "La llei combinada.", "Un gas ocupa 10 L a 1 atm i 27 °C. Quin volum ocuparà a 2 atm i 127 °C? (P₁ · V₁ / T₁ = P₂ · V₂ / T₂)"), f"{nf(1*10/300*400/2, 2)} L"),
        (3, Q(3, "Llegeix la taula.", "Hem mesurat la pressió i el volum d'un gas a temperatura constant:", "Comprova que es compleix la llei de Boyle-Mariotte.", "Quin volum tindria a 2,5 atm?", "Com seria la gràfica P–V?",
              table=T(["P (atm)", "1,0", "1,5", "2,0", "3,0"], [["V (mL)", "60", "40", "30", "20"]])),
         "a) P · V = 60 atm·mL sempre · b) 24 mL · c) una corba (hipèrbola): si P augmenta, V disminueix."),
        (3, Q(3, "Per què en kelvin?", "Un alumne diu: «Si passo un gas tancat de 10 °C a 20 °C, la pressió es duplica.» Explica per què s'equivoca i calcula quant augmenta realment, en percentatge."), f"Cal fer-ho en kelvin: 283 K → 293 K; P augmenta un {nf((293/283-1)*100, 1)} %."),
        (2, Q(2, "La pilota a l'hivern.", "Una pilota té una pressió de 1,6 atm a 25 °C. Quina pressió tindrà a 0 °C, si el volum no canvia?"), f"{nf(1.6*273/298, 2)} atm"),
        (3, Q(3, "Quina temperatura?", "A quina temperatura (en °C) cal escalfar un gas que ocupa 3 L a 27 °C perquè ocupi 4 L a la mateixa pressió?"), "400 K = 127 °C"),
    ]))
    S.append(("Els canvis d'estat i les corbes d'escalfament", [
        (1, Q(1, "Els noms.", "Escriu el nom de cada canvi d'estat i si absorbeix o desprèn calor: sòlid → líquid · líquid → gas · gas → líquid · líquid → sòlid · sòlid → gas · gas → sòlid."),
         "fusió (absorbeix) · vaporització (abs.) · condensació (desprèn) · solidificació (desp.) · sublimació (abs.) · sublimació inversa (desp.)"),
        (1, Q(1, "Evaporació o ebullició?", "Escriu dues diferències entre l'evaporació i l'ebullició i un exemple de cadascuna."), "Evaporació: a qualsevol temperatura i només a la superfície (roba que s'asseca). Ebullició: a una temperatura fixa i a tot el líquid, amb bombolles (aigua que bull)."),
        (2, Q(2, "Quin estat?", "Amb la taula, digues en quin estat és cada substància a 20 °C i a 90 °C:", table=T(["Substància", "T de fusió (°C)", "T d'ebullició (°C)"], [["Aigua", "0", "100"], ["Etanol", "−114", "78"], ["Mercuri", "−39", "357"], ["Oxigen", "−218", "−183"]])),
         "A 20 °C: aigua, etanol i mercuri líquids; oxigen gas. A 90 °C: aigua i mercuri líquids; etanol i oxigen gasos."),
        (2, Q(2, "La corba d'escalfament.", "Escalfem una substància sòlida a −20 °C i n'anotem la temperatura cada minut: la temperatura puja fins a 0 °C, es manté a 0 °C de 3 a 8 minuts, puja fins a 100 °C als 15 minuts i s'hi manté fins al minut 25.", "Dibuixa la gràfica temperatura–temps.", "Quin estat hi ha a cada tram?", "Quina substància pot ser?", "Per què la temperatura no puja als trams horitzontals?"),
         "b) sòlid · sòlid + líquid (fusió) · líquid · líquid + gas (ebullició) · c) aigua · d) l'energia serveix per separar les partícules (vèncer les atraccions)."),
        (3, Q(3, "Pura o mescla?", "Una substància A es fon sempre a 80 °C i la temperatura es manté constant mentre es fon. Una substància B comença a fondre's a 70 °C i acaba a 76 °C. Quina és una substància pura i quina una mescla? Com seria la corba de cadascuna?"),
         "A pura (tram horitzontal) · B mescla (canvia d'estat en un interval: tram inclinat)."),
        (2, Q(2, "La suor.", "Per què ens refreda la suor quan s'evapora? Explica-ho amb el model de partícules i amb l'energia."), "En evaporar-se, escapen les partícules més ràpides i el líquid absorbeix calor de la pell: la pell es refreda."),
    ]))
    return {"sub": "El model cineticomolecular, la temperatura i la pressió, les lleis dels gasos i els canvis d'estat.", "seccions": S}

# ======================================================================== SdA 3
def sda3():
    S = []
    S.append(("Elements i models atòmics", [
        (1, Q(1, "Símbols.", "Escriu el símbol: sodi, potassi, calci, ferro, coure, plata, or, liti, cobalt, níquel, silici, fòsfor. I el nom: Mg, Al, Zn, Sn, Pb, Hg, S, Cl."),
         "Na, K, Ca, Fe, Cu, Ag, Au, Li, Co, Ni, Si, P · magnesi, alumini, zinc, estany, plom, mercuri, sofre, clor"),
        (1, Q(1, "Ordena els models", "de Dalton, Bohr, Thomson i Rutherford cronològicament i escriu una frase que descrigui com és l'àtom en cadascun."),
         "Dalton (esfera massissa) → Thomson (esfera positiva amb electrons) → Rutherford (nucli petit i dens, electrons al voltant, molt buit) → Bohr (electrons en capes d'energia fixa)."),
        (2, Q(2, "L'experiment de Rutherford.", "En bombardejar una làmina d'or amb partícules alfa (positives), gairebé totes la travessen, però unes poques es desvien molt o reboten. Quines dues conclusions en va treure Rutherford? Per què aquest resultat no encaixava amb el model de Thomson?"),
         "L'àtom és gairebé tot buit i té un nucli molt petit amb tota la càrrega positiva i gairebé tota la massa. Amb Thomson la càrrega estaria repartida i cap partícula rebotaria."),
        (2, Q(2, "Els models i les proves.", "Per què va caldre canviar el model de Dalton? I el de Rutherford? Relaciona cada canvi amb el descobriment o l'experiment que el va provocar."), "Dalton: el descobriment de l'electró (Thomson). Rutherford: els espectres de línies i l'estabilitat de l'àtom (Bohr)."),
    ]))
    S.append(("Les partícules de l'àtom: Z, A, isòtops i ions", [
        (1, Q(1, "Completa la taula.", "", table=T(["Àtom", "Z", "A", "Protons", "Neutrons", "Electrons"], [["¹²C", "6", "", "", "", ""], ["²⁷Al", "13", "", "", "", ""], ["", "", "23", "11", "", ""], ["⁵⁶Fe", "26", "", "", "", ""], ["", "", "", "17", "18", "17"]])),
         "¹²C: 6 p, 6 n, 6 e · ²⁷Al: 13 p, 14 n, 13 e · ²³Na (Z = 11): 12 n, 11 e · ⁵⁶Fe: 26 p, 30 n, 26 e · ³⁵Cl: Z = 17, A = 35"),
        (1, Q(1, "Isòtops.", "El carboni-12 i el carboni-14 són isòtops. Què tenen igual i què tenen diferent? Quants neutrons té cada un?"), "Mateix Z (6 protons i 6 electrons); diferent nombre de neutrons: 6 i 8."),
        (2, Q(2, "La massa atòmica.", "El clor natural té un 75,8 % de ³⁵Cl (34,97 u) i un 24,2 % de ³⁷Cl (36,97 u). Calcula la massa atòmica del clor. Per què no és un nombre enter?"), f"{nf(0.758*34.97+0.242*36.97, 2)} u. És una mitjana ponderada dels isòtops."),
        (1, Q(1, "Ions.", "Completa la taula.", table=T(["Ió", "Z", "Protons", "Electrons", "Catió o anió"], [["Li⁺", "3", "", "", ""], ["Mg²⁺", "12", "", "", ""], ["O²⁻", "8", "", "", ""], ["Cl⁻", "17", "", "", ""], ["Al³⁺", "13", "", "", ""]])),
         "Li⁺: 3 p, 2 e, catió · Mg²⁺: 12 p, 10 e, catió · O²⁻: 8 p, 10 e, anió · Cl⁻: 17 p, 18 e, anió · Al³⁺: 13 p, 10 e, catió"),
        (2, Q(2, "Vertader o fals?", "Justifica:", "Un catió s'ha format perquè l'àtom ha guanyat protons.", "L'ió Na⁺ i l'àtom de neó tenen el mateix nombre d'electrons.", "Dos isòtops tenen propietats químiques molt diferents.", "Quasi tota la massa de l'àtom és al nucli."),
         "a) F: ha perdut electrons · b) V: 10 electrons · c) F: són molt semblants · d) V."),
        (2, Q(2, "Quin àtom és?", "Un ió té 20 protons, 20 neutrons i 18 electrons. Quin element és? Quina és la seva càrrega i el seu nombre màssic? Escriu-ne el símbol complet."), "Calci; càrrega 2+; A = 40: ⁴⁰Ca²⁺"),
        (3, Q(3, "La mida de l'àtom.", "El nucli d'un àtom fa uns 10⁻¹⁵ m i l'àtom, uns 10⁻¹⁰ m. Quantes vegades és més gran l'àtom que el nucli? Si el nucli fos una bola d'1 cm, quina mida tindria l'àtom?"), "10⁵ vegades · 1 km"),
    ]))
    S.append(("Les capes d'electrons i la taula periòdica", [
        (1, Q(1, "Distribueix els electrons en capes", "(2, 8, 8…): He, C, O, Na, Mg, Cl, Ar, K, Ca."), "He 2 · C 2,4 · O 2,6 · Na 2,8,1 · Mg 2,8,2 · Cl 2,8,7 · Ar 2,8,8 · K 2,8,8,1 · Ca 2,8,8,2"),
        (2, Q(2, "On és a la taula?", "Amb la distribució en capes, indica el període i el grup de: a) 2, 8, 3 · b) 2, 5 · c) 2, 8, 8, 2 · d) 2, 8, 7. De quin element es tracta en cada cas?"), "a) període 3, grup 13: Al · b) 2, grup 15: N · c) 4, grup 2: Ca · d) 3, grup 17: Cl"),
        (1, Q(1, "Famílies.", "Escriu el nom de la família i dos elements de cada grup: 1, 2, 17 i 18. Quina propietat comparteixen els elements d'un mateix grup?"), "Alcalins (Na, K), alcalinoterris (Mg, Ca), halògens (F, Cl), gasos nobles (He, Ne). Tenen els mateixos electrons a l'última capa i propietats químiques semblants."),
        (2, Q(2, "Metall o no metall?", "Classifica: Fe, S, Na, O, Cu, C, Al, Cl, Au, N. Escriu tres propietats dels metalls."), "Metalls: Fe, Na, Cu, Al, Au · No metalls: S, O, C, Cl, N. Brillants, condueixen el corrent i la calor, dúctils i mal·leables."),
        (2, Q(2, "Quin ió forma?", "Quin ió tendeix a formar cada element i per què? Li, Mg, Al, O, F, S. Relaciona-ho amb el gas noble més proper."), "Li⁺, Mg²⁺, Al³⁺ (perden electrons) · O²⁻, F⁻, S²⁻ (en guanyen): així queden amb l'última capa com un gas noble."),
        (2, Q(2, "L'assaig a la flama.", "En escalfar sals de liti, sodi i coure a la flama s'observen colors diferents. Explica d'on surt la llum amb el model de Bohr. Per què cada element fa un color diferent?"), "Els electrons absorbeixen energia, salten a capes superiors i en tornar emeten llum. Les capes de cada element tenen energies diferents: cada element emet uns colors propis."),
        (1, Q(1, "Períodes i grups.", "Digues el període i el grup de: Na, Ca, Al, C, S, Ne, K, Br. Quin és un gas noble? I un halogen?"), "Na 3/1 · Ca 4/2 · Al 3/13 · C 2/14 · S 3/16 · Ne 2/18 (gas noble) · K 4/1 · Br 4/17 (halogen)"),
    ]))
    S.append(("L'enllaç químic i les substàncies", [
        (1, Q(1, "Quin enllaç?", "Digues si l'enllaç és iònic, covalent o metàl·lic: NaCl, H₂O, Cu, CO₂, MgO, Fe, CH₄, KBr, O₂, Al."), "Iònic: NaCl, MgO, KBr · Covalent: H₂O, CO₂, CH₄, O₂ · Metàl·lic: Cu, Fe, Al"),
        (2, Q(2, "Propietats.", "Tenim tres substàncies: A és un sòlid dur que es fon a 800 °C i condueix dissolt en aigua; B és un gas a temperatura ambient que no condueix; C és un sòlid brillant que condueix sòlid. Quin tipus d'enllaç té cadascuna? Posa'n un exemple."),
         "A iònic (NaCl) · B covalent molecular (O₂, CO₂) · C metàl·lic (Cu)"),
        (2, Q(2, "La fórmula d'un compost iònic.", "Escriu la fórmula del compost que formen: a) Na⁺ i Cl⁻ · b) Mg²⁺ i Cl⁻ · c) Al³⁺ i O²⁻ · d) Ca²⁺ i O²⁻ · e) Li⁺ i O²⁻."), "a) NaCl · b) MgCl₂ · c) Al₂O₃ · d) CaO · e) Li₂O"),
        (3, Q(3, "Iònic o covalent: explica-ho.", "Explica, amb un dibuix dels electrons de l'última capa, com es forma l'enllaç en el fluorur de sodi (NaF) i en la molècula de fluor (F₂). Per què una és sòlida i l'altra un gas?"),
         "NaF: el Na cedeix 1 electró al F; els ions s'atrauen i formen una xarxa (sòlid). F₂: comparteixen un parell d'electrons; molècules poc atretes entre elles (gas)."),
        (2, Q(2, "Vertader o fals?", "Justifica:", "Els compostos iònics condueixen el corrent en estat sòlid.", "El diamant és covalent i molt dur.", "Els metalls condueixen perquè tenen electrons lliures.", "L'aigua és un compost iònic."), "a) F: només fosos o dissolts · b) V: xarxa covalent · c) V · d) F: covalent (molècules)."),
        (2, Q(2, "Substàncies del mòbil.", "Al mòbil hi ha coure (cables), silici (xips), vidre (SiO₂) i òxid de cobalt i liti (bateria). Indica el tipus d'enllaç de cadascuna i una propietat que expliqui per què s'hi fa servir."), "Coure: metàl·lic, condueix · silici: covalent (xarxa), semiconductor · vidre: covalent (xarxa), dur i transparent · òxid: iònic, conté ions Li⁺."),
    ]))
    S.append(("Elements, recursos i reciclatge", [
        (2, Q(2, "Reaccions de la bateria.", "Quan fem servir el mòbil, a l'ànode de la bateria cada àtom de liti perd un electró. Escriu l'equació. Per on van els ions i per on van els electrons?"), "Li → Li⁺ + e⁻. Els ions Li⁺ passen per l'electròlit fins al càtode; els electrons, pel circuit exterior (el mòbil)."),
        (3, Q(3, "Per què reciclar?", "Un mòbil conté uns 0,034 g d'or. Quants mòbils caldria reciclar per obtenir 1 kg d'or? Dona dos arguments a favor del reciclatge dels mòbils."), f"{nf(1000/0.034, 0)} mòbils (≈ 29 400). Arguments: recursos limitats, mineria contaminant i amb impacte social, residus tòxics."),
    ]))
    return {"sub": "Elements i models atòmics, Z i A, isòtops i ions, capes d'electrons, taula periòdica i enllaç químic.", "seccions": S}

# ======================================================================== SdA 4
def sda4():
    S = []
    S.append(("Reaccions químiques i col·lisions", [
        (1, Q(1, "Físic o químic?", "Indica si és un canvi físic o químic: a) l'aigua es congela · b) el gas d'una cuina crema · c) el ferro es rovella · d) la sal es dissol · e) l'electròlisi de l'aigua · f) es fon la cera d'una espelma."), "Químics: b, c, e · Físics: a, d, f"),
        (1, Q(1, "Evidències.", "Escriu quatre evidències que indiquen que hi ha hagut una reacció química."), "Gas, canvi de color, precipitat, calor o llum, olor nova."),
        (2, Q(2, "La teoria de les col·lisions.", "Explica les dues condicions que ha de complir un xoc entre partícules perquè sigui eficaç. Per què no reaccionen totes les partícules que xoquen?"), "Prou energia cinètica (≥ energia d'activació) i orientació adequada. Molts xocs no tenen prou energia o la bona orientació."),
        (2, Q(2, "Reactius i productes.", "En la reacció hidrogen + oxigen → aigua, quins enllaços es trenquen i quins es formen? Hi ha els mateixos àtoms abans i després?"), "Es trenquen H–H i O=O; es formen O–H. Sí: només es reorganitzen."),
    ]))
    S.append(("Formulació i nomenclatura", [
        (1, Q(1, "Simple o compost?", "H₂, H₂O, O₂, CO₂, Mg, MgCl₂, He, CH₄, N₂, NaCl."), "Simples: H₂, O₂, Mg, He, N₂ · Compostos: H₂O, CO₂, MgCl₂, CH₄, NaCl"),
        (1, Q(1, "Ions.", "Escriu el nom o el símbol: Na⁺ · ió magnesi · Al³⁺ · ió calci · Cu²⁺ · ió fluorur · O²⁻ · ió sulfur · Cl⁻ · ió ferro(III)."), "ió sodi · Mg²⁺ · ió alumini · Ca²⁺ · ió coure(II) · F⁻ · ió òxid · S²⁻ · ió clorur · Fe³⁺"),
        (2, Q(2, "Compostos iònics.", "Escriu el nom o la fórmula: CaO · clorur de potassi · Al₂O₃ · òxid de ferro(II) · MgCl₂ · sulfur de sodi · FeCl₃ · bromur de calci · CuO · òxid de liti."), "òxid de calci · KCl · òxid d'alumini · FeO · clorur de magnesi · Na₂S · clorur de ferro(III) · CaBr₂ · òxid de coure(II) · Li₂O"),
        (2, Q(2, "Compostos covalents.", "Escriu el nom o la fórmula: CO · diòxid de sofre · NO₂ · triòxid de sofre · CCl₄ · monòxid de dinitrogen · NH₃ · pentaòxid de difòsfor · CH₄ · sulfur d'hidrogen."), "monòxid de carboni · SO₂ · diòxid de nitrogen · SO₃ · tetraclorur de carboni · N₂O · amoníac · P₂O₅ · metà · H₂S"),
        (2, Q(2, "Troba l'error.", "Corregeix: a) clorur de magnesi = MgCl · b) Al₃O₂ = òxid d'alumini · c) CO₂ = òxid de carboni · d) NaCl₂ = clorur de sodi."), "a) MgCl₂ · b) Al₂O₃ · c) diòxid de carboni · d) NaCl"),
    ]))
    S.append(("Equacions químiques i conservació de la massa", [
        (1, Q(1, "Compta els àtoms", "i digues si l'equació està ajustada: a) 2 H₂ + O₂ → 2 H₂O · b) CH₄ + O₂ → CO₂ + 2 H₂O · c) N₂ + 3 H₂ → 2 NH₃."), "a) sí · b) no (4 O a la dreta i 2 a l'esquerra: cal 2 O₂) · c) sí"),
        (2, Q(2, "Ajusta.", "a) H₂O → H₂ + O₂ · b) Mg + HCl → MgCl₂ + H₂ · c) C₃H₈ + O₂ → CO₂ + H₂O · d) Al + O₂ → Al₂O₃ · e) Na + Cl₂ → NaCl · f) C₄H₁₀ + O₂ → CO₂ + H₂O."),
         "a) 2 H₂O → 2 H₂ + O₂ · b) Mg + 2 HCl → MgCl₂ + H₂ · c) C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O · d) 4 Al + 3 O₂ → 2 Al₂O₃ · e) 2 Na + Cl₂ → 2 NaCl · f) 2 C₄H₁₀ + 13 O₂ → 8 CO₂ + 10 H₂O"),
        (1, Q(1, "Lavoisier.", "Cremem 2,4 g de magnesi i obtenim 4,0 g d'òxid de magnesi. Quanta massa d'oxigen ha reaccionat? Per què l'òxid pesa més que el magnesi?"), "1,6 g. S'hi ha afegit l'oxigen de l'aire: la massa total es conserva."),
        (2, Q(2, "Recipient obert o tancat?", "Fem reaccionar bicarbonat i vinagre en un got obert i la massa baixa 1,1 g. Expliqueu què ha passat. Què passaria en una ampolla tancada amb un globus?"), "Ha sortit CO₂ a l'aire. En un recipient tancat la massa no canviaria."),
        (2, Q(2, "Molècules i equacions.", "Interpreta amb paraules l'equació N₂ + 3 H₂ → 2 NH₃: quantes molècules de cada reactiu calen i quantes de producte es formen? Si tinguéssim 10 molècules de N₂, quantes d'H₂ caldrien?"), "1 de N₂ i 3 d'H₂ formen 2 d'amoníac · 30 d'H₂"),
    ]))
    S.append(("Masses moleculars i càlculs de massa", [
        (1, Q(1, "Massa molecular.", "Calcula la massa molecular de: H₂O, CO₂, CH₄, NH₃, C₃H₈, NaCl, CaCO₃, H₂SO₄."), "18 u · 44 u · 16 u · 17 u · 44 u · 58,5 u · 100 u · 98 u"),
        (2, Q(2, "La proporció en massa.", "2 H₂ + O₂ → 2 H₂O. a) Calcula la massa de cada terme (en u) i comprova la llei de Lavoisier. b) Quina massa d'aigua es forma amb 10 g d'hidrogen? c) Quanta massa d'oxigen cal?"), "a) 4 + 32 = 36 u · b) 90 g · c) 80 g"),
        (2, Q(2, "La combustió del metà.", "CH₄ + 2 O₂ → CO₂ + 2 H₂O. Quina massa de CO₂ es forma en cremar 80 g de metà? I d'aigua?"), "220 g de CO₂ · 180 g d'aigua"),
        (2, Q(2, "La bombona de propà.", "C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O. Quina massa de CO₂ s'allibera en cremar 11 kg de propà? Quin oxigen cal?"), "33 kg de CO₂ · 40 kg d'O₂"),
        (2, Q(2, "Magnesi i àcid.", "Mg + 2 HCl → MgCl₂ + H₂. Quina massa d'hidrogen es desprèn quan reaccionen 6 g de magnesi?"), "0,5 g"),
        (3, Q(3, "Reactiu limitant.", "Fem reaccionar 8 g d'hidrogen amb 32 g d'oxigen: 2 H₂ + O₂ → 2 H₂O. Quin reactiu s'acaba primer? Quina massa d'aigua es forma? Quant sobra de l'altre reactiu?"), "Limitant: oxigen (els 32 g d'O₂ només reaccionen amb 4 g d'H₂) · 36 g d'aigua · sobren 4 g d'H₂"),
        (3, Q(3, "La calç.", "En escalfar pedra calcària: CaCO₃ → CaO + CO₂. Quina massa de calç (CaO) i de CO₂ s'obtenen de 500 kg de pedra calcària pura?"), "280 kg de CaO · 220 kg de CO₂"),
    ]))
    S.append(("Energia i velocitat de les reaccions", [
        (1, Q(1, "Exo o endo?", "Classifica com a exotèrmica o endotèrmica: a) la combustió del butà · b) l'electròlisi de l'aigua · c) la fotosíntesi · d) el magnesi amb àcid clorhídric · e) la respiració cel·lular · f) bicarbonat i vinagre (el got es refreda)."), "Exotèrmiques: a, d, e · Endotèrmiques: b, c, f"),
        (2, Q(2, "Diagrama d'energia.", "Dibuixa el diagrama d'energia d'una reacció exotèrmica i marca-hi els reactius, els productes, l'energia d'activació i l'energia alliberada. Com canviaria amb un catalitzador?"), "Productes més avall que els reactius; «muntanya» = energia d'activació. Amb catalitzador la muntanya és més baixa i el resultat és el mateix."),
        (2, Q(2, "Factors de la velocitat.", "Explica amb la teoria de les col·lisions per què: a) els aliments es conserven més a la nevera; b) la pols de farina pot explotar i un tros de pa no; c) el vinagre concentrat reacciona més de pressa amb el bicarbonat que el diluït."), "a) a menys T, menys xocs i menys energètics · b) més superfície de contacte · c) més concentració, més xocs."),
        (3, Q(3, "Dissenya l'experiment.", "Vols estudiar com afecta la temperatura a la velocitat de la reacció entre una pastilla efervescent i l'aigua. Indica la variable independent, la dependent, tres variables controlades i què mesuraries."), "Independent: temperatura de l'aigua · dependent: temps que triga a dissoldre's · controlades: volum d'aigua, mida de la pastilla, agitació · mesuraríem el temps amb un cronòmetre a 3–4 temperatures."),
        (2, Q(2, "L'hidrogen com a combustible.", "Escriu l'equació ajustada de la combustió de l'hidrogen. Quins avantatges té respecte de la gasolina? Quin és el problema de com s'obté avui la major part de l'hidrogen?"), "2 H₂ + O₂ → 2 H₂O. No emet CO₂ ni contaminants en l'ús. La majoria s'obté del gas natural (amb emissions de CO₂); l'hidrogen verd surt de l'electròlisi amb renovables."),
    ]))
    return {"sub": "Reaccions i col·lisions, formulació, ajust d'equacions, conservació de la massa, càlculs de massa, energia i velocitat de reacció.",
            "dades": "Masses atòmiques (u): H = 1 · C = 12 · N = 14 · O = 16 · Na = 23 · Mg = 24 · Al = 27 · S = 32 · Cl = 35,5 · Ca = 40 · Fe = 56", "seccions": S}

# ======================================================================== SdA 5
def sda5():
    S = []
    S.append(("Posició, desplaçament i velocitat", [
        (1, Q(1, "Relatiu.", "Un passatger va assegut en un tren que avança a 100 km/h. Està en repòs o en moviment? Respon segons dos sistemes de referència diferents."), "En repòs respecte del tren; en moviment (100 km/h) respecte de l'andana."),
        (1, Q(1, "Distància i desplaçament.", "Surts de casa, camines 300 m cap a l'est fins a la fleca i tornes 100 m cap a l'oest fins al quiosc. Quina distància has recorregut? Quin és el desplaçament?"), "400 m · 200 m cap a l'est"),
        (1, Q(1, "Escalar o vectorial?", "Classifica: massa, velocitat, temps, desplaçament, temperatura, força, distància, acceleració."), "Escalars: massa, temps, temperatura, distància · Vectorials: velocitat, desplaçament, força, acceleració"),
        (1, Q(1, "Canvia d'unitats.", "Passa a m/s: 36 km/h · 72 km/h · 18 km/h. Passa a km/h: 5 m/s · 30 m/s."), "10 · 20 · 5 m/s · 18 · 108 km/h"),
    ]))
    S.append(("El moviment rectilini uniforme (MRU)", [
        (1, Q(1, "El patinet.", "Un patinet circula a 18 km/h en línia recta. a) Expressa la velocitat en m/s. b) Quina distància recorre en 2 minuts? c) Quant triga a recórrer 1,5 km?"), "a) 5 m/s · b) 600 m · c) 300 s = 5 min"),
        (2, Q(2, "L'equació de posició.", "Un autobús passa pel punt x = 50 m a 36 km/h i manté la velocitat. a) Escriu l'equació de posició. b) On és al cap de 8 s? c) Quan passa per x = 250 m?"), "a) x = 50 + 10 t · b) 130 m · c) 20 s"),
        (2, Q(2, "Moto o cotxe?", "Una moto a 72 km/h i un cotxe a 54 km/h han de recórrer 3 km. Quant triga cadascun? Quants segons abans arriba la moto?"), "150 s i 200 s · 50 s abans"),
        (2, Q(2, "La gràfica x–t.", "Un ciclista és a x = 0 a t = 0 s, a x = 40 m a t = 5 s i a x = 80 m a t = 10 s. a) Dibuixa la gràfica x–t. b) Quin moviment té? c) Calcula la velocitat a partir del pendent."), "b) MRU · c) 8 m/s"),
        (3, Q(3, "Trobada.", "Dos amics són a 600 m l'un de l'altre i caminen l'un cap a l'altre: l'Anna a 1,5 m/s i en Pau a 1,0 m/s. Quan i on es troben (des de la posició de l'Anna)?"), "t = 240 s; a 360 m de l'Anna"),
    ]))
    S.append(("L'acceleració i el MRUA", [
        (1, Q(1, "Quin moviment és?", "MRU, MRUA o cap dels dos: a) un patinet a 20 km/h per un carril recte; b) una pilota que cau; c) un patinet que pren un revolt a velocitat constant; d) un cotxe que frena davant d'un pas de vianants."), "a) MRU · b) MRUA · c) cap (trajectòria corba) · d) MRUA"),
        (1, Q(1, "Calcula l'acceleració.", "a) Un cotxe passa de 0 a 27 m/s en 9 s. b) Un patinet que va a 6 m/s s'atura en 3 s. Per què una és negativa?"), "a) 3 m/s² · b) −2 m/s² (frena: la velocitat disminueix)"),
        (2, Q(2, "La moto del semàfor.", "Una moto surt del repòs amb una acceleració de 2,5 m/s² durant 8 s. a) Quina velocitat té, en m/s i en km/h? b) Quina distància ha recorregut?"), "a) 20 m/s = 72 km/h · b) 80 m"),
        (2, Q(2, "La frenada.", "Un patinet que va a 6 m/s frena i s'atura en 3 s. Quina distància recorre mentre frena?"), "9 m"),
        (2, Q(2, "Per què 30 km/h?", "Un cotxe frena amb a = −5 m/s². a) Calcula el temps i la distància de frenada a 50 km/h i a 30 km/h. b) El conductor triga 1 s a reaccionar. Calcula la distància total en cada cas."),
         f"a) 50 km/h: {nf(50/3.6/5, 2)} s, {nf((50/3.6)**2/10, 1)} m · 30 km/h: {nf(30/3.6/5, 2)} s, {nf((30/3.6)**2/10, 1)} m · b) {nf(50/3.6+(50/3.6)**2/10, 1)} m i {nf(30/3.6+(30/3.6)**2/10, 1)} m"),
        (3, Q(3, "La gràfica v–t.", "Un cotxe surt d'un pàrquing: la velocitat augmenta uniformement de 0 a 15 m/s en 6 s i després es manté constant 4 s. a) Dibuixa la gràfica v–t. b) Calcula l'acceleració del primer tram. c) Calcula la distància de cada tram (àrea sota la gràfica)."), "b) 2,5 m/s² · c) 45 m i 60 m (105 m en total)"),
        (2, Q(2, "Caiguda lliure.", "Deixem caure una pedra des d'un pont i triga 2,0 s a arribar a l'aigua. Amb g = 9,8 m/s², a quina velocitat arriba i quina altura té el pont?"), "19,6 m/s · 19,6 m"),
    ]))
    S.append(("Escales, difusió i gradient", [
        (1, Q(1, "Mida de les coses.", "Ordena de més petit a més gran i expressa-ho en metres amb notació científica: un neutròfil (12 µm), un virus de la grip (100 nm), un bacteri (2 µm), un àtom (0,1 nm), un cabell (70 µm)."), "àtom 1 · 10⁻¹⁰ m &lt; virus 1 · 10⁻⁷ m &lt; bacteri 2 · 10⁻⁶ m &lt; neutròfil 1,2 · 10⁻⁵ m &lt; cabell 7 · 10⁻⁵ m"),
        (2, Q(2, "Velocitat d'una cèl·lula.", "Un neutròfil recorre 60 µm en 3 minuts. Calcula la velocitat en µm/min i en m/s. Quant trigaria a recórrer 1 mm?"), f"20 µm/min · {nf(60e-6/180, 2, True)} m/s · 50 min"),
        (2, Q(2, "El gradient.", "La concentració d'una substància és de 10 unitats a 0 µm i de 2 unitats a 40 µm. Calcula el gradient (variació / distància). Cap a on es mouria una cèl·lula que segueix la substància?"), "−0,2 unitats/µm · cap a on és més concentrada (cap a 0 µm)"),
        (2, Q(2, "Variables.", "Volem estudiar si la temperatura afecta la velocitat de difusió d'una gota de tinta en aigua. Quina és la variable independent, la dependent i dues de controlades?"), "Independent: temperatura · dependent: temps fins que el color és uniforme · controlades: volum d'aigua, quantitat de tinta, recipient."),
    ]))
    S.append(("Les forces i les lleis de Newton", [
        (1, Q(1, "Força resultant.", "Calcula la força resultant: a) 30 N i 20 N en el mateix sentit; b) 30 N i 20 N en sentits contraris; c) 3 N i 4 N perpendiculars."), "a) 50 N · b) 10 N · c) 5 N"),
        (2, Q(2, "La llei de Hooke.", "Una molla s'allarga 4 cm quan hi pengem 2 N. a) Calcula la constant elàstica en N/m. b) Quant s'allargarà amb 5 N? c) Quina força cal per allargar-la 10 cm?"), "a) 50 N/m · b) 10 cm · c) 5 N"),
        (1, Q(1, "Quina llei?", "a) Quan l'autobús frena de cop, ens anem endavant. b) Un patinet més carregat costa més d'accelerar. c) Per nedar empenyem l'aigua cap enrere. d) Una cèl·lula avança estirant el substrat cap enrere."), "a) 1a (inèrcia) · b) 2a · c) 3a · d) 3a"),
        (2, Q(2, "La força de frenada.", "Un patinet amb el conductor (80 kg) frena amb una acceleració de −3 m/s². Calcula la força de frenada."), "240 N (en sentit contrari al moviment)"),
        (2, Q(2, "Accelerar.", "Un patinet amb el conductor (80 kg) passa de 0 a 6 m/s en 4 s. a) Calcula l'acceleració. b) Calcula la força resultant. c) Quina força caldria si la massa fos de 60 kg?"), "a) 1,5 m/s² · b) 120 N · c) 90 N"),
        (3, Q(3, "Acció i reacció.", "Dibuixa un llibre sobre una taula i les forces que hi actuen. El pes i la normal són una parella d'acció i reacció? Justifica-ho."), "No: actuen sobre el mateix cos (el llibre). La reacció del pes és la força que el llibre fa sobre la Terra; la de la normal, la que el llibre fa sobre la taula."),
    ]))
    return {"sub": "Posició i velocitat, MRU, MRUA i caiguda lliure, gràfiques, escales i gradients, forces, Hooke i les lleis de Newton.", "seccions": S}

# ======================================================================== SdA 6
def sda6():
    S = []
    S.append(("L'energia i les seves transformacions", [
        (1, Q(1, "Transformacions.", "Indica la transformació principal d'energia: a) un ventilador · b) una placa fotovoltaica · c) un altaveu · d) una estufa elèctrica · e) una pila que encén un llum · f) una central hidràulica."),
         "a) elèctrica → cinètica · b) lluminosa → elèctrica · c) elèctrica → sonora · d) elèctrica → tèrmica · e) química → elèctrica → lluminosa · f) potencial → cinètica → elèctrica"),
        (2, Q(2, "Cinètica.", "Calcula l'energia cinètica (E<sub>c</sub> = ½ · m · v²) d'una persona de 60 kg que corre a 5 m/s i d'un cotxe de 1 200 kg a 72 km/h."), "750 J · 240 000 J"),
        (2, Q(2, "Potencial.", "Calcula l'energia potencial (E<sub>p</sub> = m · g · h, g = 9,8 m/s²) d'una motxilla de 5 kg al tercer pis (9 m). Quina energia cinètica tindria just abans de tocar a terra si la deixéssim caure (sense fregament)?"), "441 J · 441 J"),
        (3, Q(3, "Conservació.", "Una pilota de 0,5 kg cau des de 5 m. a) Quina energia potencial té a dalt? b) Amb quina velocitat arriba a terra si no hi ha fregament? c) Després del bot puja només fins a 3,5 m. On és l'energia que falta?"), f"a) 24,5 J · b) {nf((2*9.8*5)**0.5, 1)} m/s · c) s'ha transformat en energia tèrmica i sonora (degradació)."),
        (1, Q(1, "Unitats d'energia.", "Expressa en joules: 2 kJ · 500 cal · 1,5 kcal · 0,5 kWh."), "2 000 J · 2 090 J · 6 270 J · 1,8 · 10⁶ J"),
    ]))
    S.append(("Rendiment, potència i consum", [
        (1, Q(1, "Rendiment.", "Una bombeta d'incandescència de 60 W fa 3 J de llum cada segon. Una LED de 8 W fa la mateixa llum. Calcula el rendiment de cadascuna."), "5 % · 37,5 %"),
        (1, Q(1, "Potència.", "Un microones transforma 54 000 J en 1 minut. Quina és la seva potència?"), "900 W"),
        (2, Q(2, "En joules i en kWh.", "Una estufa de 2 000 W funciona 3 hores. Calcula l'energia consumida en kWh i en J."), "6 kWh · 2,16 · 10⁷ J"),
        (2, Q(2, "El cost.", "Amb un preu de 0,15 €/kWh, calcula el cost mensual (30 dies) de: a) una nevera de 150 W que funciona 8 h al dia; b) un carregador de 10 W endollat tot el dia; c) un forn de 2 500 W, 1 h al dia."), "a) 36 kWh, 5,40 € · b) 7,2 kWh, 1,08 € · c) 75 kWh, 11,25 €"),
        (2, Q(2, "Incandescència o LED?", "Una bombeta està encesa 5 h al dia. Quant estalvies en un any (365 dies) si canvies una de 60 W per una LED de 8 W? (0,15 €/kWh)"), f"{nf(52*5*365/1000, 1)} kWh · {nf(52*5*365/1000*0.15, 2)} €"),
        (3, Q(3, "El consum en espera.", "A l'institut hi ha 30 ordinadors que es queden en espera (3 W cadascun) 16 h al dia, 180 dies a l'any. Quanta energia es gasta així en un any? Quant costa?"), f"{nf(30*3*16*180/1000, 1)} kWh · {nf(30*3*16*180/1000*0.15, 2)} €"),
        (2, Q(2, "La factura.", "Una família consumeix 270 kWh en un mes. Si el preu és de 0,15 €/kWh, quant paga d'energia? Quina potència mitjana representa (mes de 30 dies)?"), "40,50 € · 375 W"),
    ]))
    S.append(("El circuit elèctric", [
        (1, Q(1, "Magnituds.", "Relaciona cada magnitud amb la unitat i l'instrument: intensitat, tensió, resistència — volt, ampere, ohm — amperímetre, voltímetre, ohmímetre. Com es connecta l'amperímetre? I el voltímetre?"), "Intensitat: A, amperímetre (en sèrie) · tensió: V, voltímetre (en paral·lel) · resistència: Ω, ohmímetre"),
        (1, Q(1, "Llei d'Ohm.", "a) Quina intensitat passa per una resistència de 60 Ω connectada a 12 V? b) Quina tensió cal per fer passar 0,5 A per 20 Ω? c) Quina resistència té un aparell que, a 230 V, deixa passar 2 A?"), "a) 0,2 A · b) 10 V · c) 115 Ω"),
        (2, Q(2, "Potència elèctrica.", "Un assecador de 1 150 W es connecta a 230 V. Quina intensitat hi passa (P = V · I)? Quina resistència té?"), "5 A · 46 Ω"),
        (2, Q(2, "Sèrie o paral·lel?", "Tenim dues bombetes iguals i una pila. a) Dibuixa-les en sèrie i en paral·lel. b) Què passa amb l'altra bombeta si se'n fon una, en cada cas? c) Com estan connectats els aparells de casa? Per què?"), "b) en sèrie s'apaga; en paral·lel continua encesa · c) en paral·lel: cada aparell rep 230 V i funciona independentment."),
        (3, Q(3, "Resistències.", "Dues resistències de 10 Ω i 20 Ω es connecten a 6 V. Calcula la resistència total i la intensitat que surt de la pila: a) en sèrie; b) en paral·lel."), f"a) 30 Ω, 0,2 A · b) {nf(1/(1/10+1/20), 2)} Ω, 0,9 A"),
        (2, Q(2, "Seguretat.", "Per què és perillós endollar molts aparells de molta potència en un sol lladre? Per a què serveixen el magnetotèrmic i el diferencial?"), "Passa molta intensitat, els cables s'escalfen i pot haver-hi un incendi. Magnetotèrmic: talla si hi ha sobrecàrrega o curtcircuit. Diferencial: talla si hi ha una fuita de corrent (per una persona)."),
        (2, Q(2, "Llegeix la placa.", "Una torradora porta escrit «230 V · 920 W». Quina intensitat hi passa? Quanta energia consumeix en 3 minuts (en J i en kWh)?"), "4 A · 165 600 J = 0,046 kWh"),
        (1, Q(1, "Conductors i aïllants.", "Classifica com a conductors o aïllants: coure, plàstic, aigua salada, vidre, alumini, fusta seca, grafit, goma. Per què els cables són de coure recobert de plàstic?"), "Conductors: coure, aigua salada, alumini, grafit · aïllants: plàstic, vidre, fusta seca, goma. El coure porta el corrent i el plàstic ens aïlla."),
    ]))
    S.append(("La generació d'electricitat i les fonts d'energia", [
        (1, Q(1, "Renovable o no?", "Classifica: solar, carbó, eòlica, nuclear, hidràulica, gas natural, biomassa, geotèrmica, petroli."), "Renovables: solar, eòlica, hidràulica, biomassa, geotèrmica · No renovables: carbó, nuclear, gas natural, petroli"),
        (2, Q(2, "Cadena de transformacions.", "Escriu la cadena de transformacions d'energia en una central de cicle combinat i en un parc eòlic. Quina peça tenen en comú?"), "Cicle combinat: química → tèrmica → cinètica (turbina) → elèctrica · eòlica: cinètica del vent → cinètica (turbina) → elèctrica. Comú: turbina i alternador."),
        (2, Q(2, "Llegeix les dades.", "Les renovables van generar 7 160 GWh, el 19,1 % de l'electricitat de Catalunya. Calcula l'electricitat total generada."), f"{nf(7160/0.191, 0)} GWh"),
        (2, Q(2, "Avantatges i inconvenients.", "Escriu un avantatge i un inconvenient de l'energia nuclear, de la solar i del gas natural."), "Nuclear: no emet CO₂ / residus radioactius · solar: renovable i neta / depèn del sol, cal emmagatzemar · gas: produeix quan cal / emet CO₂ i s'esgota."),
        (3, Q(3, "Pla d'estalvi.", "Proposa tres mesures per reduir el consum elèctric d'una aula, classificades en hàbits, eficiència i generació renovable, i estima l'estalvi d'una d'elles amb dades."), "Resposta oberta: p. ex. apagar llums al pati (hàbit), canviar fluorescents per LED (eficiència), plaques solars (renovable), amb un càlcul de kWh i €."),
        (2, Q(2, "Fonts fiables.", "Llegeixes a les xarxes que «les plaques solars gasten més energia per fabricar-les que la que produeixen». Quines quatre preguntes et faries per avaluar la font?"), "Qui ho diu, quan, per què (interès) i amb quines proves (dades i referències)."),
    ]))
    return {"sub": "L'energia i les seves formes, conservació i rendiment, potència i consum, el circuit elèctric i les fonts d'energia.", "seccions": S}

FUNCS = {1: sda1, 2: sda2, 3: sda3, 4: sda4, 5: sda5, 6: sda6}
