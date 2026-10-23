"""Activitats afegides als fulls de 2n ESO: més preguntes a les fitxes (continuen la numeració
de la fitxa, no són un full a part) i més reptes i recursos a l'ampliació.
Cada pregunta es pot resoldre amb la informació del full (i del full d'equivalències). Les dades són les
dels mateixos fulls o dades de llibre de text (densitats, calors específiques, temperatures de canvi d'estat)."""
from estil import q, h2, tip, table, resources
from .fixes import FIXES_2N as FIXES

REC = '<p class="intro">Recursos per continuar aprenent. Entra a l\'adreça i cerca el títol entre cometes.</p>'

def mes(*qs):
    return "".join(qs)

def amp(reptes, recursos):
    return "".join(reptes) + h2("R", "Recursos per anar més enllà") + REC + resources(recursos)

PHET = "https://phet.colorado.edu/ca/"
VIQUI = "https://ca.wikipedia.org"

EXTRA = {}

# ================================================================== SdA 1 · L'institut en xifres
EXTRA["sda1-03-fitxa-1-seguretat.pdf"] = mes(
    q(4, "<b>Quin pictograma?</b> Escriu el número (GHS01…GHS09) dels pictogrames que han de portar aquests productes, segons el que diu l'etiqueta.") +
    table(["Producte", "Què diu l'etiqueta", "Pictogrames"], [
        ["Desembussador de canonades", "Provoca cremades greus a la pell i lesions oculars greus.", ""],
        ["Recàrrega d'encenedor (butà)", "Gas extremadament inflamable. Conté gas a pressió: pot explotar si s'escalfa.", ""],
        ["Insecticida per a plantes", "Molt tòxic per als organismes aquàtics, amb efectes duradors.", ""],
        ["Netejavidres concentrat", "Provoca irritació ocular greu.", ""],
    ], empty_cols=(2,), widths=["28%", "52%", "20%"]),
    q(5, "<b>Detecta els errors.</b> Al laboratori, la Marta porta els cabells deixats anar, es menja un caramel mentre treballa, escalfa un tub d'assaig apuntant cap al seu company i, en acabar, llença les restes del producte a l'aigüera. Escriu cada error i com s'hauria de fer.", 4),
    q(6, "<b>Ordena els passos.</b> A un company li esquitxa una gota d'un producte a l'ull. Numera de l'1 al 4: ☐ avisar el professor o professora · ☐ rentar l'ull amb molta aigua durant uns minuts · ☐ mirar l'etiqueta per saber quin producte era · ☐ no fregar-se l'ull.", 1),
    q(7, "<b>Per què?</b> Explica per què al laboratori fem servir bata, ulleres i, de vegades, guants. Per a cadascun, digues de què ens protegeix.", 3),
)

EXTRA["sda1-05-fitxa-2-magnituds-i-unitats.pdf"] = mes(
    q(5, "<b>A unitats del SI.</b> Escriu l'equivalència i el factor de conversió, i passa a la unitat del SI: a) 25 cm; b) 3 h; c) 450 g; d) 2,5 km; e) 1.500 L (pista: 1 m³ = 1.000 L).", 4),
    q(6, "<b>Ordena</b> de més petita a més gran (passa-ho tot a cm): 0,5 m · 45 cm · 480 mm · 0,0004 km.", 2),
    q(7, "<b>Magnitud, unitat i instrument.</b> Completa la taula.") +
    table(["Què vull mesurar?", "Magnitud", "Unitat del SI", "Instrument"], [
        ["La teva alçada", "", "", ""], ["La temperatura de l'aula", "", "", ""], ["La durada d'una classe", "", "", ""],
        ["L'aigua d'una ampolla", "", "", ""], ["La massa de la motxilla", "", "", ""]], empty_cols=(1, 2, 3)),
    q(8, "<b>Falta la unitat!</b> En Pol diu: «Avui he corregut 3». Escriu tres coses diferents que podria voler dir. Per què un nombre sol no és una mesura?", 2),
    q(9, "<b>Completa</b> amb la taula dels prefixos: 1 kg = ____ g · 1 m = ____ mm · 1 L = ____ cL · 1 hm = ____ m · 1 g = ____ mg.", 1),
)

EXTRA["sda1-06-fitxa-3-factors-de-conversio.pdf"] = mes(
    q(7, "<b>L'aixeta oberta.</b> Una aixeta raja 12 L/min. Amb factors de conversió, calcula quants litres surten en 1 h i quants m³ en un dia.", 3),
    q(8, "<b>Velocitats.</b> a) Un cotxe va a 72 km/h: passa-ho a m/s. b) Un guepard corre a 30 m/s: passa-ho a km/h. Quin va més de pressa?", 3),
    q(9, "<b>El gruix d'un full.</b> Un full de paper fa 0,1 mm de gruix. Quants fulls caldria apilar per fer una pila d'1 m? (Passa el metre a mm.)", 2),
    q(10, "<b>Gotes i gots.</b> Una gota d'aigua té uns 0,05 mL. Quantes gotes hi ha en un got de 250 mL? I en una ampolla d'1,5 L?", 2),
    q(11, "<b>Escriu el factor que falta</b> (amb unitats): a) 3 h · ( ____ ) = 180 min. b) 5.000 g · ( ____ ) = 5 kg. c) 2 m² · ( ____ ) = 20.000 cm².", 2),
)

EXTRA["sda1-08-fitxa-4-superficie-i-volum.pdf"] = mes(
    q(6, "<b>L'aula.</b> Una aula fa 8 m × 6 m × 3 m. Calcula'n la superfície del terra (m² i cm²) i el volum (m³ i L).", 3),
    q(7, "<b>La llauna.</b> Una llauna de refresc diu 33 cL. Passa-ho a mL i a cm³. Cabria en un cub de 10 cm de costat?", 2),
    q(8, "<b>Les rajoles.</b> Volem cobrir 4 m² de terra amb rajoles de 20 cm × 20 cm. Quina superfície té cada rajola en cm²? Quantes en calen? (Passa els 4 m² a cm².)", 3),
    q(9, "<b>El dipòsit.</b> Un dipòsit d'aigua té 2 m³. Quantes galledes de 10 L s'hi poden omplir?", 2),
    q(10, "<b>Detecta l'error.</b> En Joan diu que 1 m² = 100 cm², «perquè 1 m són 100 cm». Explica-li l'error amb un dibuix d'un quadrat d'1 m de costat.", 3),
)

EXTRA["sda1-09-fitxa-5-notacio-cientifica.pdf"] = mes(
    q(6, "<b>Escriu en notació científica:</b> a) el diàmetre de la Terra, 12.700.000 m; b) la massa d'un gra de sorra, 0,000 06 kg; c) la velocitat de la llum, 300.000.000 m/s; d) el gruix d'un full, 0,0001 m.", 2),
    q(7, "<b>Sense calculadora.</b> Calcula i escriu el resultat en notació científica: a) (2 · 10³) · (4 · 10²); b) (6 · 10⁸) : (3 · 10⁴); c) (5 · 10⁻³) · (2 · 10⁵). Pista: en multiplicar, els exponents se sumen; en dividir, es resten.", 3),
    q(8, "<b>Quin és més gran?</b> a) 3 · 10⁴ o 4 · 10³. b) 2 · 10⁻³ o 5 · 10⁻⁴. Justifica-ho escrivint els nombres sencers.", 2),
    q(9, "<b>Tot Catalunya.</b> A Catalunya hi viuen uns 8.000.000 de persones. Si cadascuna gasta uns 110 L d'aigua al dia a casa, quants litres es gasten en un dia? Escriu-ho en notació científica i passa-ho a m³.", 3),
    q(10, "<b>Ben escrit?</b> Quins d'aquests nombres estan ben escrits en notació científica? Corregeix els que no ho estan: 45 · 10³ · 4,5 · 10⁴ · 0,7 · 10⁻² · 7 · 10⁻³.", 2),
)

EXTRA["sda1-11-fitxa-6-l-aigua-de-l-institut.pdf"] = mes(
    q(7, "<b>Per persona.</b> Amb les dades d'exemple (520 persones i 1.350 m³ l'any), quants m³ gasta cada persona en un any? Passa-ho a litres.", 2),
    q(8, "<b>Estalviar un 15 %.</b> Si l'institut reduís el consum anual un 15 %, quants m³ estalviaria? Quantes ampolles d'1,5 L són?", 3),
    q(9, "<b>La cadena del vàter.</b> Una cisterna gasta 6 L cada vegada. Si cada persona l'estira 3 vegades al dia, quants litres es gasten en un dia a l'institut? I en un curs (175 dies)? Passa-ho a m³. Quin percentatge del consum anual representa?", 4),
    q(10, "<b>La nostra proposta.</b> Una cisterna de doble descàrrega pot fer servir només 3 L per a la descàrrega curta. Si la meitat de les descàrregues fossin curtes, quant estalviaria l'institut en un curs? Escriu el càlcul amb factors de conversió.", 4),
)

EXTRA["sda1-19-ampliacio.pdf"] = amp([
    q(5, "<b>Fermi i el cor.</b> El cor batega unes 70 vegades per minut. Quantes vegades bategarà en una vida de 80 anys? Fes la cadena de factors (min → h → dia → any) i escriu el resultat en notació científica.", 4),
    q(6, "<b>Mesures antigues.</b> Abans del sistema mètric, a Barcelona es mesurava amb la cana (uns 1,555 m), que tenia 8 pams. Quants centímetres feia un pam? Quants pams fa la teva alçada? I l'aula?", 3),
    q(7, "<b>La font i la piscina.</b> Una font raja 0,2 L/s. Quant de temps trigaria a omplir una piscina olímpica de 50 m × 25 m × 2 m? Dona el resultat en dies.", 3),
    q(8, "<b>Mesurar el que és molt petit.</b> Com mesuraries el gruix d'un full amb un regle que només aprecia mil·límetres? Dissenya el mètode i explica per què és més precís.", 3),
], [
    ("El Sistema Internacional d'Unitats", "Viquipèdia en català: història del sistema mètric i definició actual de les set unitats bàsiques", VIQUI + " · «Sistema Internacional d'Unitats»"),
    ("The International System of Units (SI)", "Oficina Internacional de Pesos i Mesures (BIPM): el document oficial del SI, en anglès i francès", "https://www.bipm.org · «SI Brochure»"),
    ("Unitats de mesura tradicionals catalanes", "Viquipèdia en català: cana, pam, quartera, lliura… i com es passen al sistema mètric", VIQUI + " · «Unitats de mesura catalanes»"),
    ("L'aigua a Catalunya en dades", "Agència Catalana de l'Aigua: consums, embassaments i estat dels rius", "https://aca.gencat.cat"),
    ("Població de Catalunya", "Institut d'Estadística de Catalunya (Idescat): dades oficials per fer estimacions", "https://www.idescat.cat"),
])

# ================================================================== SdA 2 · Un arc de Sant Martí dins d'un got
EXTRA["sda2-03-fitxa-1-massa-i-volum.pdf"] = mes(
    q(6, "<b>El volum d'un cargol.</b> Una proveta té 40 mL d'aigua. Hi deixem caure un cargol i l'aigua puja fins a 52 mL. Quin volum té el cargol, en mL i en cm³?", 2),
    q(7, "<b>Volums de capses.</b> Calcula el volum d'un dau de 3 cm de costat i el d'una capsa de 10 cm × 5 cm × 2 cm. Quants daus caben a la capsa (sense deixar forats)?", 3),
    q(8, "<b>Ordena per massa</b> (passa-ho tot a g): 1,2 kg · 950 g · 0,08 kg · 120.000 mg.", 2),
    q(9, "<b>L'ampolla.</b> Una ampolla buida té una massa de 25 g i, plena d'aigua, de 525 g. Quina massa d'aigua conté? Si 1 mL d'aigua té una massa d'1 g, quin volum hi cap?", 3),
    q(10, "<b>Per què no?</b> Explica amb un exemple per què el volum no ens serveix per saber de quina substància està feta una cosa.", 2),
)

EXTRA["sda2-05-fitxa-2-la-densitat.pdf"] = mes(
    q(6, "<b>Quin metall és?</b> Una peça metàl·lica de 135 g fa pujar l'aigua d'una proveta de 50 mL a 100 mL. Calcula'n la densitat i busca a la taula de quin metall pot ser.", 3),
    q(7, "<b>La llet.</b> Quina massa tenen 2 L de llet? (Passa els litres a cm³.)", 2),
    q(8, "<b>Or i suro.</b> Quin volum ocupa 1 kg d'or? I 1 kg de suro? Quantes vegades més gran és el volum del suro?", 3),
    q(9, "<b>El líquid misteriós.</b> 200 mL d'un líquid transparent tenen una massa de 158 g. Calcula'n la densitat. Quin líquid de la taula pot ser? Per què no pot ser aigua?", 2),
    q(10, "<b>L'aire.</b> La densitat de l'aire és 1,2 kg/m³. Passa-la a g/L (1 m³ = 1.000 L) i a g/cm³. Per què tenim la sensació que l'aire «no pesa»?", 3),
)

EXTRA["sda2-06-fitxa-3-practiquem.pdf"] = mes(
    q(7, "<b>La piscina olímpica.</b> Una piscina olímpica té 2.500 m³ d'aigua (1.000 kg/m³). Quina massa d'aigua conté, en kg i en tones (1 t = 1.000 kg)?", 2),
    q(8, "<b>El pot de mel.</b> Un pot conté 500 g de mel. Quin volum ocupa la mel, en mL?", 2),
    q(9, "<b>El bloc de gel.</b> Un bloc de gel fa 50 cm × 20 cm × 10 cm. Quina massa té, en kg?", 2),
    q(10, "<b>Dues boles iguals.</b> Una bola de ferro i una de plom tenen el mateix volum, 10 cm³. Quina massa té cadascuna? Quina diferència de massa hi ha?", 2),
    q(11, "<b>Repte.</b> Una proveta buida té una massa de 120 g. Amb 50 mL d'un líquid, la massa és de 166 g. Calcula la densitat del líquid i digues quin pot ser.", 3),
)

EXTRA["sda2-08-fitxa-4-sura-o-s-enfonsa.pdf"] = mes(
    q(6, "<b>Sura o s'enfonsa?</b> Fes servir la taula de densitats de la fitxa 2.") +
    table(["Objecte", "Líquid", "Sura / s'enfonsa", "Per què?"], [
        ["Suro", "oli", "", ""], ["Moneda de plata", "mercuri (13,6 g/cm³)", "", ""], ["Gel", "alcohol", "", ""],
        ["Fusta de pi", "mel", "", ""], ["Alumini", "aigua de mar", "", ""], ["Or", "mercuri (13,6 g/cm³)", "", ""]], empty_cols=(2, 3)),
    q(7, "<b>La pilota.</b> Una pilota de platja té una massa de 400 g i un volum de 5.000 cm³. Calcula'n la densitat mitjana. Sura a l'aigua?", 2),
    q(8, "<b>L'ampolla.</b> Una ampolla tancada i buida té una massa de 30 g i un volum de 550 cm³. Sura? I si l'omplim de 550 g d'aigua i la tanquem? Calcula la densitat mitjana en els dos casos.", 3),
    q(9, "<b>Dibuixa</b> un got amb mel, aigua i oli en capes, i situa-hi un gra de raïm (1,05 g/cm³) i un tros de fusta de pi. Explica on s'atura cada objecte.", 1, '<div class="box" style="min-height:32mm"></div>'),
)

EXTRA["sda2-10-fitxa-5-arquimedes.pdf"] = mes(
    q(6, "<b>Una corona de plata.</b> Si la corona de 1.000 g fos de plata pura (10,5 g/cm³), quin volum tindria? Quanta aigua desplaçaria?", 2),
    q(7, "<b>Compara.</b> Fes una taula amb el volum que tindria la corona de 1.000 g si fos d'or pur, si fos de plata pura i el volum que va mesurar Arquimedes (64 cm³). Què en conclous?", 3),
    q(8, "<b>La banyera.</b> Una banyera fa 150 cm × 70 cm. Si hi submergim una corona de 64 cm³, quants centímetres puja l'aigua? (Pista: volum = superfície × altura.) Per què era tan difícil veure-ho?", 3),
    q(9, "<b>Com treballa la ciència.</b> Relaciona cada pas amb la història d'Arquimedes: pregunta, hipòtesi, experiment, conclusió.", 4),
)

EXTRA["sda2-11-fitxa-6-hipatia.pdf"] = mes(
    q(5, "<b>Dos líquids.</b> Un densímetre s'enfonsa més en el líquid A que en el líquid B. Quin dels dos és més dens? Explica-ho.", 2),
    q(6, "<b>Al celler.</b> Mentre el most es transforma en vi, el sucre es transforma en alcohol (0,79 g/cm³). Què creus que marcarà el densímetre a mesura que avança la fermentació: més o menys densitat? Per què?", 3),
    q(7, "<b>La llet aigualida.</b> La llet té una densitat d'1,03 g/cm³. Si algú hi afegeix aigua, el densímetre s'enfonsarà més o menys? Com ho podria fer servir una inspecció de consum?", 3),
    q(8, "<b>Línia del temps.</b> Situa en una línia del temps Arquimedes (287–212 aC), Hipàtia (cap al 355–415) i Galileu (que va proposar la balança hidrostàtica el 1586). Aproximadament, quants anys separen Arquimedes de Galileu?", 2, '<div class="box" style="min-height:18mm"></div>'),
)

EXTRA["sda2-19-ampliacio.pdf"] = amp([
    q(5, "<b>Aigua i alcohol.</b> Barregem 100 mL d'aigua (1,00 g/mL) i 100 mL d'alcohol (0,79 g/mL). Quina massa té la mescla? Si mesurem el volum, no dona 200 mL sinó uns 193 mL. Calcula la densitat de la mescla. Per què creus que el volum es redueix? (Pista: model de partícules i espai entre elles.)", 4),
    q(6, "<b>La punta de l'iceberg.</b> La fracció submergida d'un objecte que sura és la seva densitat dividida per la del líquid. Quin percentatge d'un iceberg (gel, 0,92 g/cm³) queda sota l'aigua de mar (1,03 g/cm³)? I d'un tros de fusta de pi a l'aigua dolça?", 3),
    q(7, "<b>Densitat d'una patata.</b> Dissenya un experiment per mesurar la densitat d'una patata amb una balança i una proveta (o un got graduat). Després, explica com podries fer que la patata quedés entre dues aigües.", 4),
], [
    ("Densitat", "Simulació PhET: compara masses i volums de blocs de materials diferents i descobreix quins suren", PHET + " · «Densitat» (Density)"),
    ("Flotabilitat", "Simulació PhET: l'empenta, el pes i per què uns objectes suren i d'altres no", PHET + " · «Flotabilitat» (Buoyancy)"),
    ("Principi d'Arquimedes", "Viquipèdia en català: l'enunciat, la història de la corona i aplicacions", VIQUI + " · «Principi d'Arquimedes»"),
    ("Hipàtia d'Alexandria", "Viquipèdia en català: la vida i l'obra de la matemàtica i astrònoma", VIQUI + " · «Hipàtia d'Alexandria»"),
    ("Densímetre", "Viquipèdia en català: com funciona i on es fa servir (vi, llet, bateries, aigua de mar)", VIQUI + " · «Densímetre»"),
])

# ================================================================== SdA 3 · La pilota que no bota
EXTRA["sda3-03-fitxa-1-estats.pdf"] = mes(
    q(4, "<b>Gel, aigua i vapor.</b> Completa la taula amb el que diu el model de partícules.") +
    table(["", "Gel", "Aigua líquida", "Vapor"], [["Com estan les partícules?", "", "", ""], ["Com es mouen?", "", "", ""],
                                              ["Té forma pròpia?", "", "", ""], ["Es pot comprimir?", "", "", ""]], empty_cols=(1, 2, 3)),
    q(5, "<b>Explica amb el model:</b> a) per què un globus s'infla quan hi bufem; b) per què no podem comprimir una xeringa plena d'aigua tapada; c) per què l'olor del perfum arriba de pressa a l'altra punta de l'aula.", 3),
    q(6, "<b>Vertader o fals?</b> Corregeix les falses. a) Les partícules del gel no es mouen. b) Entre les partícules d'un gas hi ha aire. c) Quan escalfem una substància, les partícules es fan més grans. d) Al gas, les partícules xoquen contra les parets del recipient.", 4),
    q(7, "<b>Dibuixa</b> les partícules d'una ampolla tancada plena d'aigua fins a la meitat: l'aigua a baix i l'aire a dalt.", 0, '<div class="box" style="min-height:30mm"></div>'),
)

EXTRA["sda3-05-fitxa-2-canvis-d-estat.pdf"] = mes(
    q(5, "<b>El cicle de l'aigua.</b> Escriu quin canvi d'estat passa a cada moment: a) l'aigua del mar s'escalfa amb el sol i passa a l'aire; b) el vapor es refreda i forma les gotetes dels núvols; c) a dalt de tot, les gotetes es glacen i fan neu; d) la neu de la muntanya es desfà a la primavera.", 4),
    q(6, "<b>L'estenedor.</b> Per què la roba s'asseca més de pressa un dia calorós i amb vent? Explica-ho amb el model de partícules.", 3),
    q(7, "<b>L'ampolla que «sua».</b> Treus una ampolla de la nevera i al cap d'una estona està mullada per fora. D'on surt l'aigua? Quin canvi d'estat és?", 2),
    q(8, "<b>Més foc?</b> Una olla d'aigua bull a 100 °C. Si apugem el foc, la temperatura de l'aigua continua pujant? Què passa, doncs, amb l'energia que hi afegim?", 3),
)

EXTRA["sda3-07-fitxa-3-corbes.pdf"] = mes(
    q(5, "<b>En quin estat?</b> Fes servir la taula de temperatures de fusió i d'ebullició.") +
    table(["Substància", "A −50 °C", "A 20 °C", "A 100 °C"], [["Alcohol (etanol)", "", "", ""], ["Mercuri", "", "", ""],
                                                        ["Àcid esteàric", "", "", ""], ["Oxigen", "", "", ""], ["Sal", "", "", ""]], empty_cols=(1, 2, 3)),
    q(6, "<b>Corba de l'alcohol.</b> Dibuixa a mà alçada la corba d'escalfament de l'alcohol des de −120 °C fins a 100 °C. Marca a quines temperatures hi ha trams horitzontals i quin canvi d'estat passa en cadascun.", 0, '<div class="box" style="min-height:34mm"></div>'),
    q(7, "<b>Termòmetres.</b> Un termòmetre de mercuri serveix per mesurar −50 °C? I un d'alcohol? Justifica-ho amb la taula.", 2),
    q(8, "<b>Identifica-la.</b> Una substància sòlida es fon a 69 °C i bull a 361 °C. Quina és? En quin estat és a l'aula? I dins d'aigua bullint?", 2),
)

EXTRA["sda3-08-fitxa-4-pressio-i-kelvin.pdf"] = mes(
    q(5, "<b>Unitats de pressió.</b> Escriu els factors de conversió i calcula: a) 1,5 atm a mmHg i a Pa; b) 2.026 hPa a atm; c) 50.000 Pa a atm.", 3),
    q(6, "<b>Kelvin.</b> a) Passa a K: 37 °C (el cos humà) i −196 °C (nitrogen líquid). b) Passa a °C: 373 K i 0 K.", 2),
    q(7, "<b>El mapa del temps.</b> Un anticicló té 1.030 hPa i una borrasca, 990 hPa. Quina diferència de pressió hi ha, en hPa i en Pa? I en atm?", 2),
    q(8, "<b>La pressió de la roda.</b> El manòmetre d'una benzinera marca 2,2 bar. Passa-ho a atm. Aquest aparell marca quanta pressió hi ha de més que a fora: quina és la pressió total dins la roda (suma-hi 1 atm)?", 3),
    q(9, "<b>Vertader o fals?</b> Corregeix les falses. a) 0 °C és la temperatura més baixa que hi pot haver. b) Al zero absolut les partícules es mourien el mínim possible. c) Una variació d'1 °C és igual que una variació d'1 K.", 3),
)

EXTRA["sda3-10-fitxa-5-boyle.pdf"] = mes(
    q(6, "<b>Comprimim.</b> Un gas ocupa 4 L a 1 atm. Quin volum ocuparà a 2 atm, si la temperatura no canvia?", 2),
    q(7, "<b>La xeringa.</b> Una xeringa tapada té 50 mL d'aire a 1 atm. Fins a quin volum l'hem d'empènyer perquè la pressió sigui de 2,5 atm?", 2),
    q(8, "<b>La bombolla que creix.</b> Una bombolla d'1 mL surt d'un bussejador a 30 m de fondària, on la pressió és de 4 atm. Quin volum tindrà a la superfície (1 atm)?", 2),
    q(9, "<b>Taula i gràfica.</b> Un gas compleix P · V = 12 atm·L. Completa la taula i dibuixa la gràfica P–V. Quina forma té?") +
    table(["P (atm)", "1", "2", "3", "4", "6"], [["V (L)", "", "", "", "", ""]], empty_cols=(1, 2, 3, 4, 5)) +
    '<div class="box" style="min-height:30mm"></div>',
    q(10, "<b>En mmHg.</b> Un gas ocupa 2 L a 760 mmHg. Quin volum ocuparà a 380 mmHg?", 2),
)

EXTRA["sda3-11-fitxa-6-charles-i-gay-lussac.pdf"] = mes(
    q(6, "<b>El globus al sol.</b> Un globus té 3 L a 27 °C. Quin volum tindrà a 87 °C, si la pressió no canvia? (Recorda: kelvin!)", 2),
    q(7, "<b>La roda calenta.</b> Una roda té una pressió total de 2,5 atm a 7 °C. Després d'una estona al sol, l'aire de dins és a 47 °C. Quina pressió té?", 2),
    q(8, "<b>L'esprai al cotxe.</b> Un esprai té una pressió d'1,5 atm a 20 °C. A l'estiu, dins d'un cotxe tancat, pot arribar a 60 °C. Quina pressió tindrà? Per què és perillós?", 3),
    q(9, "<b>El doble.</b> Un gas ocupa 2 L a 0 °C. A quina temperatura (en K i en °C) ocuparà 4 L, si la pressió no canvia?", 2),
    q(10, "<b>Error típic.</b> La Laia diu que si la temperatura d'un gas passa de 20 °C a 40 °C, la pressió es duplica. Té raó? Calcula-ho bé partint d'1 atm.", 3),
)

EXTRA["sda3-21-ampliacio.pdf"] = amp([
    q(4, "<b>Tot canvia alhora.</b> Un gas ocupa 2 L a 1 atm i 27 °C. Quin volum ocuparà a 3 atm i 127 °C? Fes servir la llei combinada.", 3),
    q(5, "<b>Per què puja l'aire calent?</b> 1 m³ d'aire a 15 °C es dilata en escalfar-se fins a 100 °C. Quin volum ocupa ara (Charles)? Si la massa és la mateixa (1,2 kg), quina densitat té? Explica per què un globus aerostàtic puja.", 4),
    q(6, "<b>L'olla a pressió.</b> Dins d'una olla a pressió hi ha uns 2 atm i l'aigua no bull fins a uns 120 °C. Per què els aliments s'hi couen més de pressa? Relaciona-ho amb l'Everest de la fitxa 3.", 3),
], [
    ("Propietats dels gasos", "Simulació PhET: canvia la temperatura, el volum i el nombre de partícules i mira què passa amb la pressió", PHET + " · «Propietats dels gasos» (Gas Properties)"),
    ("Estats de la matèria: conceptes bàsics", "Simulació PhET: escalfa i refreda aigua, neó o oxigen i observa les partícules", PHET + " · «Estats de la matèria: conceptes bàsics»"),
    ("Zero absolut", "Viquipèdia en català: què vol dir −273,15 °C i com ens hi hem acostat", VIQUI + " · «Zero absolut»"),
    ("Evangelista Torricelli", "Viquipèdia en català: el baròmetre de mercuri i la pressió atmosfèrica", VIQUI + " · «Evangelista Torricelli»"),
    ("La pressió atmosfèrica avui", "Servei Meteorològic de Catalunya: dades de pressió de les estacions i mapes del temps", "https://www.meteo.cat"),
])

# ================================================================== SdA 4 · Aigua neta del riu
EXTRA["sda4-03-fitxa-1-pures-i-mescles.pdf"] = mes(
    q(4, "<b>Classifica</b> com a substància pura, mescla homogènia o mescla heterogènia: aigua de mar, oxigen, bronze, sucre, vi, sopa de verdures, aire, iogurt amb trossos de fruita.", 3),
    q(5, "<b>Vertader o fals?</b> Corregeix les falses. a) L'aire és una substància pura. b) La sal de cuina és una mescla. c) L'aigua de l'aixeta és una substància pura. d) Una dissolució és una mescla homogènia.", 3),
    q(6, "<b>Dibuixa</b> amb partícules una mescla heterogènia d'aigua i sorra.", 0, '<div class="box" style="min-height:28mm"></div>'),
    q(7, "<b>Bullir aigua amb sal.</b> L'aigua destil·lada bull a 100 °C i la temperatura no canvia mentre bull. Amb aigua salada, comença a bullir una mica per sobre de 100 °C i la temperatura va pujant a poc a poc. Com ens ajuda això a distingir una substància pura d'una mescla?", 3),
)

EXTRA["sda4-05-fitxa-2-concentracio.pdf"] = mes(
    q(5, "<b>Calcula la concentració</b> en g/L: a) 15 g de sucre en 500 mL de dissolució; b) 2 g de sal en 250 mL.", 3),
    q(6, "<b>Quant solut?</b> Quina massa de sal hi ha en 250 mL de sèrum de 9 g/L?", 2),
    q(7, "<b>Quin volum?</b> Una llimonada té 80 g/L de sucre. Quin volum de llimonada conté 20 g de sucre? (V = m/c.)", 2),
    q(8, "<b>Ordena</b> de més diluïda a més concentrada (calcula la concentració de cadascuna): A) 10 g en 1 L; B) 5 g en 250 mL; C) 30 g en 2 L.", 3),
    q(9, "<b>Factors.</b> Passa 3,5 g/L a mg/L i 120 mg/L a g/L.", 2),
)

EXTRA["sda4-06-fitxa-3-practiquem.pdf"] = mes(
    q(7, "<b>El sodi de l'ampolla.</b> Una aigua mineral té 12 mg/L de sodi. Quants mg de sodi hi ha en una ampolla d'1,5 L? Quantes ampolles caldria beure per arribar a 2 g de sodi?", 3),
    q(8, "<b>El suc.</b> Un suc té 100 g de sucre per litre. Quants grams de sucre hi ha en un got de 200 mL? Quants terrossos de 4 g són?", 2),
    q(9, "<b>Diluïm.</b> Agafem 50 mL d'un xarop de 200 g/L i hi afegim aigua fins a 500 mL. Quina massa de sucre hi ha? Quina concentració té ara?", 3),
    q(10, "<b>Preparar.</b> Tenim 10 g de sal i volem fer una dissolució de 40 g/L. Quin volum de dissolució podem preparar?", 2),
    q(11, "<b>L'etiqueta.</b> Una aigua té 80 mg/L de calci i 25 mg/L de magnesi. Quants mg de cadascun beus amb 2 L? Passa-ho a grams.", 2),
)

EXTRA["sda4-08-fitxa-4-solubilitat.pdf"] = mes(
    q(6, "<b>Llegeix la gràfica.</b> a) Quants grams de nitrat de potassi es dissolen en 100 g d'aigua a 80 °C? b) I en 50 g d'aigua a la mateixa temperatura?", 2),
    q(7, "<b>Quina temperatura?</b> A quina temperatura la solubilitat del nitrat de potassi és de 100 g per 100 g d'aigua?", 1),
    q(8, "<b>Saturada?</b> A 20 °C dissolem 30 g de sal en 100 g d'aigua. Està saturada? Quanta sal més s'hi podria dissoldre (aproximadament)?", 2),
    q(9, "<b>Les salines.</b> L'aigua de mar té uns 38 g/L de sals. Explica, amb la paraula saturada, per què a les salines només es forma sal quan s'ha evaporat gairebé tota l'aigua.", 3),
)

EXTRA["sda4-10-fitxa-5-separacio.pdf"] = mes(
    q(4, "<b>Quina tècnica i per què?</b> Completa la taula.") +
    table(["Mescla", "Tècnica", "Propietat que aprofita"], [["Aigua i oli", "", ""], ["Sorra i llimadures de ferro", "", ""],
                                                           ["Aigua i alcohol (bull a 78 °C)", "", ""], ["Arròs bullit i aigua", "", ""],
                                                           ["Sal dissolta en aigua", "", ""]], empty_cols=(1, 2)),
    q(5, "<b>Sorra, sal i serradures.</b> Escriu els passos per separar aquests tres components. Pista: les serradures suren a l'aigua.", 4),
    q(6, "<b>A la cuina.</b> Quina tècnica de separació fas quan colem el cafè amb un filtre de paper? I quan escorres la pasta? Què passa per cada filtre i què s'hi queda?", 3),
    q(7, "<b>La cromatografia.</b> En una cromatografia d'un retolador negre surten tres taques de colors a altures diferents. Què vol dir? La tinta era una substància pura o una mescla?", 2),
)

EXTRA["sda4-11-fitxa-6-d-on-ve-l-aigua.pdf"] = mes(
    q(5, "<b>Quanta aigua a casa?</b> Una família de quatre persones gasta uns 110 L per persona i dia. Quants litres gasta en un any? Passa-ho a m³.", 3),
    q(6, "<b>Quant costa?</b> Si el metre cúbic d'aigua costés 1,50 € (suposem), quant pagaria aquesta família en un any?", 2),
    q(7, "<b>Fiable o no?</b> Llegeix aquestes dues afirmacions i avalua-les amb els criteris de la fitxa: A) un vídeo anònim d'una xarxa social diu que «l'aigua de l'aixeta de Barcelona és tòxica»; B) Aigües de Barcelona publica les anàlisis de l'aigua per barris amb data i valors. Quina és més fiable? Per què?", 4),
    q(8, "<b>Cita-la bé.</b> Escriu la cita completa (autor, any, títol, enllaç i data de consulta) d'una de les fonts que has fet servir a la fitxa.", 2),
)

EXTRA["sda4-13-fitxa-7-campanya.pdf"] = mes(
    q(5, "<b>L'oli i les canonades.</b> L'oli té una densitat de 0,92 g/cm³ i no es dissol a l'aigua. Explica què li passa a l'oli quan el llencem a l'aigüera i per què acaba fent taps a les canonades.", 3),
    q(6, "<b>Paper o tovalloleta?</b> Dissenya un experiment per comparar què passa amb un tros de paper higiènic i una tovalloleta humida en un pot amb aigua que remenem. Quina variable canvies? Quina observes? Quines mantens iguals?", 4),
    q(7, "<b>Fem números.</b> Si cadascuna de les 300 famílies de l'institut llencés una tovalloleta al dia al vàter, quantes en llençarien en un any? Escriu-ho en notació científica.", 2),
    q(8, "<b>L'eslògan.</b> Inventa un eslògan per a la campanya que porti una dada o una idea científica d'aquesta SdA.", 2),
)

EXTRA["sda4-20-ampliacio.pdf"] = amp([
    q(5, "<b>El sèrum en %.</b> Un litre de sèrum té 9 g de sal i una densitat d'1,005 g/mL. Quina massa té el litre de sèrum? Calcula'n el percentatge en massa de sal.", 3),
    q(6, "<b>Dutxa o banyera?</b> Suposem que una dutxa raja 10 L/min i que una banyera plena té 150 L. Quants minuts de dutxa equivalen a una banyera? Quanta aigua estalvia en un any una persona que es dutxa 5 minuts cada dia en lloc de banyar-se?", 3),
    q(7, "<b>La sal que surt.</b> Per obtenir 1 m³ d'aigua dolça d'aigua de mar (38 g/L de sals), quants kg de sal s'han de separar? On creus que va aquesta sal?", 3),
    q(8, "<b>Colors d'una fulla.</b> Dissenya una cromatografia per separar els pigments d'unes fulles d'espinac amb alcohol i paper de filtre. Què esperes veure?", 3),
], [
    ("Concentració", "Simulació PhET: afegeix solut, evapora aigua i observa quan la dissolució queda saturada", PHET + " · «Concentració» (Concentration)"),
    ("Agència Catalana de l'Aigua", "Estat dels rius i embassaments de Catalunya i dades de la sequera", "https://aca.gencat.cat"),
    ("Aigües de Barcelona", "Com es potabilitza l'aigua i anàlisi de la qualitat de l'aigua per adreça", "https://www.aiguesdebarcelona.cat"),
    ("Cromatografia", "Viquipèdia en català: el mètode de Mikhaïl Tsvet i els tipus de cromatografia", VIQUI + " · «Cromatografia»"),
    ("Dessalinització", "Viquipèdia en català: com es treu la sal de l'aigua de mar (osmosi inversa, destil·lació)", VIQUI + " · «Dessalinització»"),
])

# ================================================================== SdA 5 · La química de la coca de Sant Joan
EXTRA["sda5-03-fitxa-1-fisic-o-quimic.pdf"] = mes(
    q(4, "<b>Físic o químic?</b> Marca i justifica.") +
    table(["Canvi", "Físic", "Químic", "Evidència o raó"], [["Encendre un llumí", "", "", ""], ["Trencar un full de paper", "", "", ""],
                                                          ["Fer caramel amb sucre", "", "", ""], ["Evaporar alcohol", "", "", ""],
                                                          ["Digerir el menjar", "", "", ""], ["El most que fermenta i es fa vi", "", "", ""]], empty_cols=(1, 2, 3)),
    q(5, "<b>El sucre a l'aigua.</b> Quan dissolem sucre a l'aigua, el sucre «desapareix». Per què diem que és un canvi físic? Com podries recuperar el sucre?", 3),
    q(6, "<b>A la natura.</b> Escriu un exemple de canvi químic a la natura i un a la cuina, i l'evidència que el delata.", 2),
)

EXTRA["sda5-05-fitxa-2-la-reaccio-quimica.pdf"] = mes(
    q(5, "<b>Reactius i productes.</b> Identifica'ls: a) carbó + oxigen → diòxid de carboni. b) aigua oxigenada → aigua + oxigen. c) ferro + sofre → sulfur de ferro.") +
    table(["", "Reactius", "Productes"], [["a", "", ""], ["b", "", ""], ["c", "", ""]], empty_cols=(1, 2)),
    q(6, "<b>Boles.</b> Dibuixa la reacció: dues partícules de monòxid de carboni (●○) i una d'oxigen (○○) formen dues partícules de diòxid de carboni (○●○). Compta les boles de cada color abans i després.", 0, '<div class="box" style="min-height:28mm"></div>'),
    q(7, "<b>Peces noves?</b> Si els àtoms són els mateixos abans i després de la reacció, per què diem que es formen substàncies noves?", 3),
)

EXTRA["sda5-07-fitxa-3-conservacio-de-la-massa.pdf"] = mes(
    q(6, "<b>El magnesi que crema.</b> 2,4 g de magnesi cremen i formen 4,0 g d'òxid de magnesi. Quants grams d'oxigen han reaccionat?", 2),
    q(7, "<b>Sistema obert.</b> Un got amb vinagre i bicarbonat té una massa de 150,0 g abans de la reacció i de 147,8 g quan s'acaben les bombolles. Quin gas ha marxat? Quina massa en té?", 2),
    q(8, "<b>El carbó.</b> 6 g de carbó reaccionen exactament amb 16 g d'oxigen. Quina massa de diòxid de carboni es forma?", 2),
    q(9, "<b>L'espelma.</b> Una espelma té una massa de 20 g. Després de cremar una hora, en té 17 g. On són els 3 g que falten? La massa dels productes serà de 3 g, més o menys? Per què? (Pista: amb què reacciona la cera?)", 3),
)

EXTRA["sda5-09-fitxa-4-velocitat.pdf"] = mes(
    q(5, "<b>Les pastilles.</b> Una pastilla efervescent sencera en aigua a 20 °C triga 60 s a dissoldre's; triturada, a 20 °C, 20 s; sencera a 50 °C, 25 s. Quin factor canvia en cada comparació? Quin efecte té?", 3),
    q(6, "<b>A daus.</b> Per què les patates tallades a daus es couen abans que les patates senceres?", 2),
    q(7, "<b>Amb el model.</b> Explica amb els xocs entre partícules per què una reacció va més de pressa quan els reactius estan més concentrats.", 3),
    q(8, "<b>Dissenya.</b> Vols comprovar si el llevat fa pujar la massa més de pressa a 30 °C que a 20 °C. Quina variable canvies? Quina mesures? Quines has de mantenir iguals?", 3),
)

EXTRA["sda5-10-fitxa-5-quimica-de-la-cuina.pdf"] = mes(
    q(5, "<b>Quina reacció?</b> Classifica: torrar pa, fer caramel per al flam, fondre xocolata, daurar una truita. Quines són canvis químics? Quines són la reacció de Maillard o la caramel·lització?", 3),
    q(6, "<b>A l'olla no.</b> La reacció de Maillard passa sobretot a partir d'uns 140 °C. Per què unes patates bullides no es dauren, però unes de fregides sí? (Pista: a quina temperatura bull l'aigua?)", 3),
    q(7, "<b>Olor de torrat.</b> Per què l'olor del pa torrat és diferent de la del pa sense torrar? Què ens diu de les substàncies?", 2),
    q(8, "<b>Consells.</b> Escriu dos consells per «daurar, no cremar» i explica el perquè de cadascun.", 3),
)

EXTRA["sda5-11-fitxa-6-combustio.pdf"] = mes(
    q(5, "<b>Els extintors.</b> La manta ignífuga i l'extintor de diòxid de carboni apaguen el foc perquè no hi arribi oxigen. Quin costat del triangle del foc treuen? I l'aigua d'un ruixador, quin costat treu sobretot?", 3),
    q(6, "<b>Escriu l'equació amb paraules</b> de la combustió completa del gas butà de la cuina (el butà és un combustible fet de carboni i hidrogen).", 2),
    q(7, "<b>Lluny dels arbres.</b> Per què les fogueres de Sant Joan s'han de fer lluny d'arbres, cotxes i façanes? Fes servir el triangle del foc.", 3),
    q(8, "<b>El detector.</b> Per què hi ha cases amb un detector de monòxid de carboni a prop de l'escalfador? Per què no ens n'adonaríem sense el detector?", 2),
)

EXTRA["sda5-12-fitxa-7-quimica-i-salut.pdf"] = mes(
    q(5, "<b>Com conserva?</b> Explica per què cada mètode frena els microorganismes o les reaccions: a) salar el bacallà; b) fer melmelada; c) congelar; d) envasar al buit.", 4),
    q(6, "<b>El lleixiu.</b> Amb el que vas aprendre a la SdA 1, quins pictogrames porta el lleixiu (provoca cremades i és tòxic per als organismes aquàtics)? Què vol dir cadascun?", 2),
    q(7, "<b>La poma no s'enfosqueix.</b> Si tirem unes gotes de llimona a la poma tallada, triga més a tornar-se marró. Quina variable creus que fa canviar la llimona? Com ho comprovaries amb un experiment?", 3),
    q(8, "<b>Natural o químic?</b> Escriu un exemple d'una substància natural que és perillosa i un d'una substància fabricada pels humans que ens protegeix la salut.", 2),
)

EXTRA["sda5-20-ampliacio.pdf"] = amp([
    q(4, "<b>Qui sobra?</b> L'aigua sempre es forma amb 1 g d'hidrogen per cada 8 g d'oxigen. Tenim 3 g d'hidrogen i 30 g d'oxigen. Quin reactiu s'acaba primer? Quanta aigua es forma? Quant sobra de l'altre reactiu?", 4),
    q(5, "<b>Calor o fred?</b> Classifica com a exotèrmica (desprèn calor) o endotèrmica (n'absorbeix): la combustió d'una espelma, la bossa de fred instantani, la respiració cel·lular, coure un ou.", 2),
    q(6, "<b>Llegeix la gràfica.</b> Al laboratori 3, el globus de l'ampolla tèbia va créixer de pressa al principi i després cada cop més a poc a poc. Per què creus que la reacció es frena? (Pista: què li passa al sucre?)", 3),
], [
    ("Reactius, productes i sobrants", "Simulació PhET: fes reaccions i descobreix quin reactiu s'acaba primer", PHET + " · «Reactants, Products and Leftovers»"),
    ("Antoine Lavoisier", "Viquipèdia en català: la conservació de la massa i el treball amb Marie-Anne Paulze", VIQUI + " · «Antoine Lavoisier»"),
    ("Reacció de Maillard", "Viquipèdia en català: la química del pa torrat, la carn a la planxa i el cafè", VIQUI + " · «Reacció de Maillard»"),
    ("Acrilamida", "Autoritat Europea de Seguretat Alimentària (EFSA): què és i com reduir-la a casa", "https://www.efsa.europa.eu · «Acrylamide»"),
    ("Seguretat alimentària a casa", "Agència Catalana de Seguretat Alimentària: conservació dels aliments i consells", "https://acsa.gencat.cat"),
])

# ================================================================== SdA 6 · La carmanyola calenta
EXTRA["sda6-03-fitxa-1-l-energia.pdf"] = mes(
    q(5, "<b>Cadenes de transformacions.</b> Escriu les transformacions d'energia: a) una central hidroelèctrica (l'aigua d'un embassament cau i fa girar una turbina); b) una llanterna amb piles; c) un cotxe que frena i els frens s'escalfen.", 3),
    q(6, "<b>Factors de conversió.</b> a) Una persona necessita unes 2.000 kcal al dia: passa-ho a kJ. b) Passa 1 kWh a kJ. c) Quants kWh són 9.000 kJ?", 3),
    q(7, "<b>La potència.</b> Un aparell de 1.000 W fa servir 1.000 J cada segon. Si funciona 3 hores, quanta energia gasta, en J i en kWh?", 3),
    q(8, "<b>On va l'energia?</b> En una pilota que bota, cada bot és més baix. S'ha perdut energia? On ha anat?", 2),
)

EXTRA["sda6-04-fitxa-2-calor-i-temperatura.pdf"] = mes(
    q(6, "<b>Cafè amb llet.</b> Aboquem llet freda de la nevera en un cafè calent. Cap on va la calor? Quan s'atura? Dibuixa-ho amb una fletxa.", 3),
    q(7, "<b>Corregeix les frases:</b> a) «Posa't la jaqueta, que no entri el fred.» b) «El gel dona fred al refresc.» c) «Aquest radiador té molta temperatura.»", 3),
    q(8, "<b>Dues olles.</b> Una olla d'1 L i una de 5 L d'aigua són totes dues a 80 °C. Quina té més temperatura? Quina pot escalfar més una habitació en refredar-se? Per què?", 3),
    q(9, "<b>Completa</b> la taula de temperatures.") +
    table(["", "Aigua que bull", "Aigua que es glaça", "Dia d'estiu", "Nitrogen líquid"], [["°C", "100", "", "35", "−196"], ["K", "", "273", "", ""]], empty_cols=(1, 2, 3, 4)),
)

EXTRA["sda6-06-fitxa-3-calculem-la-calor.pdf"] = mes(
    q(7, "<b>La reixa de ferro.</b> Quanta calor cal per escalfar 2 kg de ferro de 20 °C a 220 °C?", 2),
    q(8, "<b>Sorra i aigua.</b> Calcula la calor per escalfar 5 kg de sorra de 20 °C a 50 °C. Amb aquesta mateixa calor, quants graus pujarien 5 kg d'aigua?", 3),
    q(9, "<b>La banyera.</b> Quanta energia cal per escalfar 150 L d'aigua de 15 °C a 40 °C? Passa-ho a kWh.", 3),
    q(10, "<b>Al revés.</b> Amb 418.000 J, quants kg d'aigua podem escalfar 50 °C?", 2),
    q(11, "<b>La barreja.</b> Barregem 200 g d'aigua a 80 °C i 300 g d'aigua a 20 °C. Quina temperatura final tindran? Fes servir la fórmula del laboratori 1: T<sub>f</sub> = (m₁·T₁ + m₂·T₂) ÷ (m₁ + m₂).", 3),
)

EXTRA["sda6-07-fitxa-4-propagacio.pdf"] = mes(
    q(6, "<b>Conducció, convecció o radiació?</b> a) La sorra de la platja crema als peus. b) L'aire calent d'un forn surt per dalt quan l'obrim. c) Ens escalfem al sol a l'hivern. d) La cullera de la xocolata calenta s'escalfa. e) L'aigua de la piscina està més calenta a dalt.", 3),
    q(7, "<b>Els mànecs.</b> Per què les paelles tenen el mànec de fusta o de plàstic? Per què la paella és de metall?", 2),
    q(8, "<b>Roba fosca.</b> Un dia de sol, una samarreta negra s'escalfa més que una de blanca. Quina forma de propagació hi intervé? Què faries servir per a la carmanyola: paper d'alumini brillant o paper negre? Per què?", 3),
    q(9, "<b>La nevera de platja.</b> Dibuixa una nevera portàtil per mantenir freds els refrescos i indica com lluita contra cada forma de propagació de la calor.", 0, '<div class="box" style="min-height:32mm"></div>'),
)

EXTRA["sda6-09-fitxa-5-aillar-una-casa.pdf"] = mes(
    q(5, "<b>Doble vidre.</b> Una casa gasta 6.000 kWh l'any en calefacció. Si posa finestres de doble vidre i estalvia un 20 %, quants kWh estalvia? Passa-ho a J (1 kWh = 3,6 · 10⁶ J) i escriu-ho en notació científica.", 3),
    q(6, "<b>Colors.</b> Per què a molts pobles de la Mediterrània les cases es pinten de blanc? Quina forma de propagació hi intervé?", 2),
    q(7, "<b>La cambra d'aire.</b> Per què el doble vidre té aire (o un altre gas) entre els dos vidres? Per què no serviria igual si l'aire es pogués moure molt?", 3),
    q(8, "<b>On hi posaries aïllant?</b> Fes una llista de tres llocs d'una casa i explica per què.", 3),
)

EXTRA["sda6-11-fitxa-6-fonts-d-energia.pdf"] = mes(
    q(5, "<b>Classifica</b> com a renovable o no renovable: urani, vent, gas natural, llenya, sol, carbó, onades, petroli, calor de l'interior de la Terra.", 2),
    q(6, "<b>Una placa solar.</b> Una placa de 400 W produeix, de mitjana, com si funcionés 4 hores al dia a tota potència. Quants kWh fa en un dia? I en un any?", 3),
    q(7, "<b>Una font no renovable.</b> Tria'n una i escriu-ne un avantatge i dos inconvenients.", 3),
    q(8, "<b>El Sol a tot arreu.</b> Explica per què diem que l'energia del vent, la de la biomassa i la hidràulica venen, en el fons, del Sol.", 3),
)

EXTRA["sda6-13-fitxa-7-debat.pdf"] = mes(
    q(5, "<b>Un argument amb dada.</b> Escriu un argument per a la teva postura que faci servir un càlcul d'aquesta SdA (per exemple, kWh estalviats o calor perduda).", 3),
    q(6, "<b>Respondre bé.</b> Imagina que algú diu: «Apagar els llums no serveix de res, és molt poca energia». Respon-li amb respecte i amb una dada o un càlcul.", 3),
    q(7, "<b>Resum del debat.</b> Escriu en tres frases les idees principals que ha acordat la classe.", 3),
)

EXTRA["sda6-20-ampliacio.pdf"] = amp([
    q(4, "<b>Evaporar costa molt.</b> Per evaporar 1 kg d'aigua que ja bull calen uns 2.260 kJ. Quanta energia cal per evaporar mig litre? Compara-ho amb l'energia per escalfar aquest mig litre de 20 °C a 100 °C. Per què suar ens refreda?", 4),
    q(5, "<b>La bombeta.</b> Suposem que una bombeta d'incandescència de 60 W converteix en llum un 5 % de l'energia. Quants W fa servir per fer llum? On va la resta? Una LED que fa la mateixa llum gasta uns 8 W: quina és més eficient?", 3),
    q(6, "<b>Un forn solar.</b> Dissenya un forn solar amb una capsa de sabates, paper d'alumini, cartolina negra i plàstic transparent. Explica què fa cada material amb la radiació, la conducció i la convecció.", 4),
], [
    ("Formes d'energia i canvis", "Simulació PhET: escalfa i refreda materials i segueix les transformacions d'energia", PHET + " · «Formes d'energia i canvis» (Energy Forms and Changes)"),
    ("Institut Català d'Energia", "Consells d'estalvi energètic a casa i dades de l'energia a Catalunya", "https://icaen.gencat.cat"),
    ("Passivhaus", "Viquipèdia en català: les cases de consum gairebé nul i com s'aïllen", VIQUI + " · «Passivhaus»"),
    ("Termo (ampolla de Dewar)", "Viquipèdia en català: l'invent de James Dewar i com evita les tres formes de propagació", VIQUI + " · «Ampolla de Dewar»"),
    ("Museu de la Ciència i de la Tècnica de Catalunya", "A Terrassa: màquines de vapor, energia i la història industrial de Catalunya", "https://mnactec.cat"),
])
