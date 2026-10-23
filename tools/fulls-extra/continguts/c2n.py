"""Activitats afegides als fulls de 2n ESO: més preguntes a les fitxes (continuen la numeració
de la fitxa, no són un full a part). Els dossiers d'ampliació són a d2n.py.
Cada pregunta es pot resoldre amb la informació del full (i del full d'equivalències). Les dades són les
dels mateixos fulls o dades de llibre de text (densitats, calors específiques, temperatures de canvi d'estat)."""
from estil import renumber, q, h2, tip, table, resources, graf
from .fixes import FIXES_2N as FIXES
from .d2n import DOSSIER


def mes(*qs):
    return renumber("".join(qs))

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
    q(10, "<b>Gotes i gots.</b> Una gota d'aigua té uns 0,05 mL. Quantes gotes hi ha en un got de 250 mL? I en una ampolla d'1,5 L?", 2),
)

EXTRA["sda1-08-fitxa-4-superficie-i-volum.pdf"] = mes(
    q(6, "<b>L'aula.</b> Una aula fa 8 m × 6 m × 3 m. Calcula'n la superfície del terra (m² i cm²) i el volum (m³ i L).", 3),
    q(7, "<b>La llauna.</b> Una llauna de refresc diu 33 cL. Passa-ho a mL i a cm³. Cabria en un cub de 10 cm de costat?", 2),
    q(8, "<b>Les rajoles.</b> Volem cobrir 4 m² de terra amb rajoles de 20 cm × 20 cm. Quina superfície té cada rajola en cm²? Quantes en calen? (Passa els 4 m² a cm².)", 3),
    q(9, "<b>El dipòsit.</b> Un dipòsit d'aigua té 2 m³. Quantes galledes de 10 L s'hi poden omplir?", 2),
    q(10, "<b>Detecta l'error.</b> En Joan diu que 1 m² = 100 cm², «perquè 1 m són 100 cm». Explica-li l'error amb un dibuix d'un quadrat d'1 m de costat.", 3),
)

EXTRA["sda1-09-fitxa-5-notacio-cientifica.pdf"] = mes(
    q(7, "<b>Sense calculadora.</b> Calcula i escriu el resultat en notació científica: a) (2 · 10³) · (4 · 10²); b) (6 · 10⁸) : (3 · 10⁴); c) (5 · 10⁻³) · (2 · 10⁵). Pista: en multiplicar, els exponents se sumen; en dividir, es resten.", 3),
    q(8, "<b>Quin és més gran?</b> a) 3 · 10⁴ o 4 · 10³. b) 2 · 10⁻³ o 5 · 10⁻⁴. Justifica-ho escrivint els nombres sencers.", 2),
    q(9, "<b>Tot Catalunya.</b> A Catalunya hi viuen uns 8.000.000 de persones. Si cadascuna gasta uns 110 L d'aigua al dia a casa, quants litres es gasten en un dia? Escriu-ho en notació científica i passa-ho a m³.", 3),
    q(10, "<b>Ben escrit?</b> Quins d'aquests nombres estan ben escrits en notació científica? Corregeix els que no ho estan: 45 · 10³ · 4,5 · 10⁴ · 0,7 · 10⁻² · 7 · 10⁻³.", 2),
)

EXTRA["sda1-11-fitxa-6-l-aigua-de-l-institut.pdf"] = mes(
    q(7, "<b>Per persona.</b> Amb les dades d'exemple (520 persones i 1.350 m³ l'any), quants m³ gasta cada persona en un any? Passa-ho a litres.", 2),
    q(8, "<b>Estalviar un 15 %.</b> Si l'institut reduís el consum anual un 15 %, quants m³ estalviaria? Quantes ampolles d'1,5 L són?", 3),
    q(9, "<b>La cadena del vàter.</b> Una cisterna gasta 6 L cada vegada. Si, de mitjana, cada persona l'estira una vegada al dia a l'institut, quants litres es gasten en un dia? I en un curs (175 dies)? Passa-ho a m³. Quin percentatge del consum anual representa?", 4),
    q(10, "<b>La nostra proposta.</b> Una cisterna de doble descàrrega pot fer servir només 3 L per a la descàrrega curta. Si la meitat de les descàrregues de l'exercici anterior fossin curtes, quants m³ estalviaria l'institut en un curs? Escriu el càlcul amb factors de conversió.", 4),
)

# ================================================================== SdA 2 · Un arc de Sant Martí dins d'un got
EXTRA["sda2-03-fitxa-1-massa-i-volum.pdf"] = mes(
    q(6, "<b>El volum d'un cargol.</b> Una proveta té 40 mL d'aigua. Hi deixem caure un cargol i l'aigua puja fins a 52 mL. Quin volum té el cargol, en mL i en cm³?", 2),
    q(7, "<b>Volums de capses.</b> Calcula el volum d'un dau de 3 cm de costat i el d'una capsa de 12 cm × 6 cm × 3 cm. Quants daus caben a la capsa (sense deixar forats)? Comprova-ho dividint els volums.", 3),
    q(8, "<b>Ordena per massa</b> (passa-ho tot a g): 1,2 kg · 950 g · 0,08 kg · 120.000 mg.", 2),
    q(9, "<b>L'ampolla.</b> Una ampolla buida té una massa de 25 g i, plena d'aigua, de 525 g. Quina massa d'aigua conté? Si 1 mL d'aigua té una massa d'1 g, quin volum hi cap?", 3),
    q(10, "<b>Per què no?</b> Explica amb un exemple per què el volum no ens serveix per saber de quina substància està feta una cosa.", 2),
)

EXTRA["sda2-05-fitxa-2-la-densitat.pdf"] = mes(
    q(6, "<b>Quin metall és?</b> Una peça metàl·lica de 135 g fa pujar l'aigua d'una proveta de 50 mL a 100 mL. Calcula'n la densitat i busca a la taula de quin metall pot ser.", 3),
    q(7, "<b>La llet.</b> Quina massa tenen 2 L de llet? (Passa els litres a cm³.)", 2),
    q(9, "<b>El líquid misteriós.</b> 200 mL d'un líquid transparent tenen una massa de 158 g. Calcula'n la densitat. Quin líquid de la taula pot ser? Per què no pot ser aigua?", 2),
)

EXTRA["sda2-06-fitxa-3-practiquem.pdf"] = mes(
    q(7, "<b>La piscina olímpica.</b> Una piscina olímpica té 2.500 m³ d'aigua (1.000 kg/m³). Quina massa d'aigua conté, en kg i en tones (1 t = 1.000 kg)?", 2),
    q(8, "<b>El pot de mel.</b> Un pot conté 500 g de mel. Quin volum ocupa la mel, en mL?", 2),
    q(9, "<b>El bloc de gel.</b> Un bloc de gel fa 50 cm × 20 cm × 10 cm. Quina massa té, en kg?", 2),
    q(10, "<b>Dues boles iguals.</b> Una bola de ferro i una de plom tenen el mateix volum, 10 cm³. Quina massa té cadascuna? Quina diferència de massa hi ha?", 2),
    q(11, "<b>Repte.</b> Una proveta buida té una massa de 120 g. Amb 50 mL d'un líquid, la massa és de 166 g. Calcula la densitat del líquid i digues quin pot ser.", 3),
)

EXTRA["sda2-08-fitxa-4-sura-o-s-enfonsa.pdf"] = mes(
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

# ================================================================== SdA 3 · La pilota que no bota
EXTRA["sda3-03-fitxa-1-estats.pdf"] = mes(
    q(4, "<b>Gel, aigua i vapor.</b> Completa la taula amb el que diu el model de partícules.") +
    table(["", "Gel", "Aigua líquida", "Vapor"], [["Com estan les partícules?", "", "", ""], ["Com es mouen?", "", "", ""],
                                              ["Té forma pròpia?", "", "", ""], ["Es pot comprimir?", "", "", ""]], empty_cols=(1, 2, 3)),
    q(5, "<b>Explica amb el model:</b> a) per què un globus s'infla quan hi bufem; b) per què no podem comprimir una xeringa plena d'aigua tapada; c) per què una gota de tinta s'escampa sola dins d'un got d'aigua, sense remenar.", 3),
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
)

EXTRA["sda3-11-fitxa-6-charles-i-gay-lussac.pdf"] = mes(
    q(7, "<b>La roda calenta.</b> Una roda té una pressió total de 2,5 atm a 7 °C. Després d'una estona al sol, l'aire de dins és a 47 °C. Quina pressió té?", 2),
    q(8, "<b>L'esprai al cotxe.</b> Un esprai té una pressió d'1,5 atm a 20 °C. A l'estiu, dins d'un cotxe tancat, pot arribar a 60 °C. Quina pressió tindrà? Per què és perillós?", 3),
    q(9, "<b>El doble.</b> Un gas ocupa 2 L a 0 °C. A quina temperatura (en K i en °C) ocuparà 4 L, si la pressió no canvia?", 2),
)

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
)

EXTRA["sda4-06-fitxa-3-practiquem.pdf"] = mes(
    q(7, "<b>El sodi de l'ampolla.</b> Una aigua mineral té 12 mg/L de sodi. Quants mg de sodi hi ha en una ampolla d'1,5 L? Quantes ampolles caldria beure per arribar a 2 g de sodi?", 3),
    q(10, "<b>Preparar.</b> Tenim 10 g de sal i volem fer una dissolució de 40 g/L. Quin volum de dissolució podem preparar?", 2),
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
    q(7, "<b>Fiable o no?</b> Llegeix aquestes dues afirmacions i avalua-les amb els criteris de la fitxa: A) un vídeo anònim d'una xarxa social diu que «l'aigua de l'aixeta de Barcelona és tòxica»; B) Aigües de Barcelona publica les anàlisis de l'aigua per barris amb data i valors. Quina és més fiable? Per què?", 4),
)

EXTRA["sda4-13-fitxa-7-campanya.pdf"] = mes(
    q(8, "<b>L'eslògan.</b> Inventa un eslògan per a la campanya que porti una dada o una idea científica d'aquesta SdA.", 2),
)

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
    q(7, "<b>La poma no s'enfosqueix.</b> Si tirem unes gotes de llimona a la poma tallada, triga més a tornar-se marró. Quina variable creus que fa canviar la llimona? Com ho comprovaries amb un experiment?", 3),
)

# ================================================================== SdA 6 · La carmanyola calenta
EXTRA["sda6-03-fitxa-1-l-energia.pdf"] = mes(
    q(5, "<b>Cadenes de transformacions.</b> Escriu les transformacions d'energia: a) una central hidroelèctrica (l'aigua d'un embassament cau i fa girar una turbina); b) una llanterna amb piles; c) un cotxe que frena i els frens s'escalfen.", 3),
    q(7, "<b>La potència.</b> Un aparell de 1.000 W fa servir 1.000 J cada segon. Si funciona 3 hores, quanta energia gasta, en J i en kWh?", 3),
    q(8, "<b>On va l'energia?</b> En una pilota que bota, cada bot és més baix. S'ha perdut energia? On ha anat?", 2),
)

EXTRA["sda6-04-fitxa-2-calor-i-temperatura.pdf"] = mes(
    q(6, "<b>Cafè amb llet.</b> Aboquem llet freda de la nevera en un cafè calent. Cap on va la calor? Quan s'atura? Dibuixa-ho amb una fletxa.", 3),
    q(7, "<b>Dos recipients en contacte.</b> Posem un got de metall amb 200 g d'aigua calenta dins d'un recipient aïllat amb 200 g d'aigua freda, i mesurem les dues temperatures cada 2 minuts." +
      table(["t (min)", "0", "2", "4", "6", "8", "10", "12"], [["Aigua calenta (°C)", "70", "58", "50", "45", "42", "41", "40"], ["Aigua freda (°C)", "10", "22", "30", "35", "38", "39", "40"]]) +
      graf((0, 12, 2), (0, 80, 10), "t (min)", "T (°C)") +
      "<p>a) Representa les dues sèries a la quadrícula amb dos colors. b) Cap on va la calor? Quan s'atura? Quina és la temperatura d'equilibri? c) Suma les dues temperatures a cada moment. Què observes? Per què creus que passa, si les dues masses són iguals?</p>", 4),
    q(8, "<b>Amb partícules.</b> Dibuixa les partícules de l'aigua calenta i de l'aigua freda de l'exercici 7 al principi i a l'equilibri. Com dibuixes que es mouen més o menys?", 0, '<div class="box" style="min-height:34mm"></div>'),
)

EXTRA["sda6-06-fitxa-3-calculem-la-calor.pdf"] = mes(
    q(9, "<b>La banyera.</b> Quanta energia cal per escalfar 150 L d'aigua de 15 °C a 40 °C? Passa-ho a kWh.", 3),
    q(11, "<b>La barreja.</b> Barregem 200 g d'aigua a 80 °C i 300 g d'aigua a 20 °C. Quina temperatura final tindran? Fes servir la fórmula del laboratori 1: T<sub>f</sub> = (m₁·T₁ + m₂·T₂) ÷ (m₁ + m₂).", 3),
)

EXTRA["sda6-07-fitxa-4-propagacio.pdf"] = mes(
    q(7, "<b>Els mànecs.</b> Per què les paelles tenen el mànec de fusta o de plàstic? Per què la paella és de metall?", 2),
    q(8, "<b>Roba fosca.</b> Un dia de sol, una samarreta negra s'escalfa més que una de blanca. Quina forma de propagació hi intervé? Què faries servir per a la carmanyola: paper d'alumini brillant o paper negre? Per què?", 3),
    q(9, "<b>La nevera de platja.</b> Dibuixa una nevera portàtil per mantenir freds els refrescos i indica com lluita contra cada forma de propagació de la calor.", 0, '<div class="box" style="min-height:32mm"></div>'),
)

EXTRA["sda6-09-fitxa-5-aillar-una-casa.pdf"] = mes(
    q(6, "<b>Colors.</b> Per què a molts pobles de la Mediterrània les cases es pinten de blanc? Quina forma de propagació hi intervé?", 2),
    q(7, "<b>La cambra d'aire.</b> Per què el doble vidre té aire (o un altre gas) entre els dos vidres? Per què no serviria igual si l'aire es pogués moure molt?", 3),
)

EXTRA["sda6-11-fitxa-6-fonts-d-energia.pdf"] = mes(
    q(6, "<b>Una placa solar.</b> Una placa de 400 W produeix, de mitjana, com si funcionés 4 hores al dia a tota potència. Quants kWh fa en un dia? I en un any?", 3),
    q(8, "<b>El Sol a tot arreu.</b> Explica per què diem que l'energia del vent, la de la biomassa i la hidràulica venen, en el fons, del Sol.", 3),
)

EXTRA["sda6-13-fitxa-7-debat.pdf"] = mes(
    q(6, "<b>Respondre bé.</b> Imagina que algú diu: «Apagar els llums no serveix de res, és molt poca energia». Respon-li amb respecte i amb una dada o un càlcul.", 3),
)

