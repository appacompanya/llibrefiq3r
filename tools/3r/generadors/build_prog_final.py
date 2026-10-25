"""Versió final de la programació: format legal (Arial 11, interlineat 1,5, marges d'1,8 cm, taules a 9 punts)
i continguts actualitzats (avaluació sense notes, activitat de demostració d'assoliment, recuperació per CE,
grups heterogenis, 1-2-4, dossier, inclusió per perfils, calendari i annexos nous)."""
import re, sys, shutil
from docx import Document
from prog_edit import *

SRC = "Programacio-FQ-3ESO-Mundet.docx"
OUT = sys.argv[1] if len(sys.argv) > 1 else "Programacio-FQ-3ESO-Mundet-final.docx"
doc = Document(SRC)
body = doc.element.body

# ------------------------------------------------------------------ 1. Format de pàgina (format legal)
MAR = 1021  # 1,8 cm
for sp in body.iter(W + 'pgMar'):
    for k in ("top", "bottom", "left", "right"):
        sp.set(W + k, str(MAR))
# les taules mantenen l'amplada del format legal (16 cm)
# interlineat del format legal: 17 punts com a mínim a tot el document (text d'11 i taules de 9 punts)
for sp in body.iter(W + 'spacing'):
    if sp.getparent().tag == W + 'pPr':
        sp.set(W + 'line', '340'); sp.set(W + 'lineRule', 'atLeast')
for st in doc.styles.element.iter(W + 'spacing'):
    st.set(W + 'line', '340'); st.set(W + 'lineRule', 'atLeast')

# ------------------------------------------------------------------ 2. Paraules: activitat de demostració d'assoliment, sense notes
ADA = "activitat de demostració d'assoliment"
R = [
    (r"prova del so a la flama", "assaig del so a la flama"),
    (r"Prova escrita competencial amb situacions noves \((\d) exercicis, 10 punts\)", r"Activitat de demostració d'assoliment, individual, amb situacions noves (\1 activitats)"),
    (r"Prova escrita competencial \((\d) exercicis, 10 punts\)", r"Activitat de demostració d'assoliment, individual (\1 activitats)"),
    (r"Prova escrita competencial", "Activitat de demostració d'assoliment"),
    (r"(Sessió \d+ · )Prova\b", r"\1Demostració d'assoliment"),
    (r"Prova i versió esmenada", "Activitat de demostració i versió esmenada"),
    (r"Prova \(qualificadora\)", "Activitat de demostració (evidència d'assoliment)"),
    (r"Prova competencial amb situacions noves", "Activitat de demostració d'assoliment amb situacions noves"),
    (r"Prova competencial, esmena", "Activitat de demostració d'assoliment, esmena"),
    (r"prova competencial", ADA),
    (r"Correcció de la prova", "Correcció de l'activitat de demostració"),
    (r"[Ee]smena de la prova", lambda m: ("E" if m.group(0)[0] == "E" else "e") + "smena de l'activitat de demostració"),
    (r"per preparar la prova", "per preparar l'activitat de demostració"),
    (r"temps addicional a la prova", "temps addicional a l'activitat de demostració"),
    (r"més de temps a la prova", "més de temps a l'activitat de demostració"),
    (r"no entra a la prova", "no entra a l'activitat de demostració"),
    (r"s'avaluen a la seva prova", "s'avaluen a la seva activitat de demostració"),
    (r"a la prova de la SdA 1", "a l'activitat de demostració de la SdA 1"),
    (r"correcció de la prova", "correcció de l'activitat de demostració"),
    (r"amb els resultats de la prova", "amb els resultats de l'activitat de demostració"),
    (r"La prova i el pla d'estalvi", "L'activitat de demostració i el pla d'estalvi"),
    (r"temps addicional a les proves", "temps addicional a les activitats de demostració"),
    (r"El formulari es pot fer servir a les proves", "El formulari es pot fer servir a les activitats de demostració"),
    (r"intercanvi d'hores per a les proves", "intercanvi d'hores per a les activitats de demostració"),
    (r"zona del professorat amb proves, solucionaris", "zona del professorat amb activitats de demostració, solucionaris"),
    (r"i les proves i les demostracions, amb el grup sencer", "i les activitats de demostració d'assoliment i les demostracions experimentals, amb el grup sencer"),
    (r"situa una prova en una hora desdoblada", "situa una activitat de demostració en una hora desdoblada"),
    (r"la prova es fa en dues versions", "l'activitat de demostració es fa en dues versions"),
    (r"(rúbriques|dossier), prova, diana", r"\1, activitat de demostració, diana"),
    (r", prova \(exercicis? ", ", activitat de demostració (activitats "),
    (r", prova \(exercici", ", activitat de demostració (activitat"),
    (r", prova\b", ", activitat de demostració"),
    (r"^Prova$", "Activitat de demostració"),
    (r"de la prova i diana", "de l'activitat de demostració i diana"),
    (r"prova i diana", "activitat de demostració i diana"),
    (r"\(exercicis (\d) i (\d)\)", r"(activitats \1 i \2)"),
    (r"\(exercicis (\d) i (\d) en coavaluació\)", r"(activitats \1 i \2 en coavaluació)"),
    (r"no per mitjana d'exàmens", "sense notes numèriques ni mitjanes d'exàmens"),
    (r"qualificació per criteris", "nivells d'assoliment per criteris"),
    (r"\(qualificadora, rúbrica", "(evidència d'assoliment, rúbrica"),
    (r"\(qualificador, rúbrica", "(evidència d'assoliment, rúbrica"),
    (r"\(qualificador, hetero i co\)", "(evidència d'assoliment, hetero i co)"),
    (r"\(qualificadora\)", "(evidència d'assoliment)"),
    (r"\(qualificador\)", "(evidència d'assoliment)"),
    (r"campanya \(qualificadora\)", "campanya (evidència d'assoliment)"),
    (r"Formativa o qualificadora", "Formativa o d'assoliment"),
    (r"Formativa i qualificadora", "Formativa i d'assoliment"),
    (r"^Qualificadora$", "D'assoliment"),
    (r"^Qualificador$", "D'assoliment"),
    (r"fulls de laboratori no qualificats", "fulls de laboratori formatius"),
    (r"Sondeig \(diagnòstic, no qualificat\)", "Sondeig (diagnòstic)"),
    (r"Lectura \(qualificadora, rúbrica\)", "Lectura (evidència d'assoliment, rúbrica)"),
    (r"Fitxa 3 \(qualificadora", "Fitxa 3 (evidència d'assoliment"),
    (r"fitxes 1 i 2 i la cerca", "fitxes 1 i 2 i la cerca"),
    (r"Esmena \(formadora\)", "Esmena (formadora)"),
    (r"prova del so a la flama", "assaig del so a la flama"),
]
cnt = {}
for pat, rep in R:
    cnt[pat] = sub_all(doc, pat, rep)

# ------------------------------------------------------------------ 3. Taules d'instruments: sense pesos
for p in list(body.iter(W + 'p')):
    if re.match(r"Taula \d+\. Instruments d'avaluació de la SdA", ptext(p)):
        tbl = table_after_par(p)
        hdr = [ptext(tc) for tc in tbl.find(W + 'tr').findall(W + 'tc')]
        if "Pes" in hdr:
            remove_col(tbl, hdr.index("Pes"))
            # amplada: repartim la columna eliminada a la primera
        sub_in_par(tbl.find(W + 'tr').findall(W + 'tc')[1].find(W + 'p'), r"^Tipus$", "Tipus d'evidència")

# ------------------------------------------------------------------ 4. Capítol 1 i 2
p = find_par(doc, "Horari. La matèria té 2 hores setmanals.")
set_par(p, [("Horari. ", True), ("La matèria té 2 hores setmanals per a l'alumnat i 3 de docència per al professor. Dilluns i dimecres són hores desdoblades i compartides amb Biologia i geologia: el professor fa la mateixa sessió amb cada meitat del grup (15 alumnes), mentre l'altra meitat fa Biologia. Dijous és l'hora de grup sencer. Així, cada alumne fa una sessió de mig grup i una de grup sencer cada setmana, i el laboratori es fa amb seguretat i atenció individualitzada (apartat 5.3 i calendari de l'annex 11).", False)])

tbl = table_after_par(find_par(doc, "Taula 3. Diversitat prevista al grup i mesures"))
add_row(tbl, ["Alumnat amb retard en l'aprenentatge", "2", "Mesura addicional: fitxes amb continguts bàsics, banc de paraules, company de suport (SdA 2)"], like=4)
for tr in tbl.findall(W + 'tr'):
    t = ptext(tr)
    if t.startswith("Alumnat nouvingut"):
        cell_set(tr.findall(W + 'tc')[2], [("Suport lingüístic coordinat amb l'aula d'acollida: vocabulari traduït a la llengua d'origen, diccionari i company de suport (SdA 2)", False)])

# ------------------------------------------------------------------ 5. Capítol 3: criteris i sabers
p = find_par(doc, "Pla d'avaluació de les competències.")
clone_after(table_after_par(p), [("Criteris de 1r a 3r. ", True), ("Les taules 4 a 9 recullen tots els criteris d'avaluació de la matèria per als cursos de 1r a 3r. En aquesta programació tots s'avaluen almenys en una SdA de 3r. Els criteris que en algun curs no es poguessin treballar en les sis SdA es treballen a 1r i 2n d'ESO, dins de la matèria de Ciències de la naturalesa, d'acord amb la distribució del departament.", False)], ref=p)

p = find_par(doc, "El decret deixa al professorat la gradació dels sabers entre 1r i 3r.")
set_par(p, [("El decret deixa al professorat la gradació dels sabers entre 1r i 3r. A 3r es treballen tots els sabers del bloc, amb una mica més de profunditat que a 1r i 2n: molts ja es van treballar en aquells cursos i es recorden ràpidament, i així l'alumnat que no els va poder treballar (per exemple, perquè ha canviat de centre i no ha cursat mai Física i química) té l'oportunitat de demostrar-ne el domini. Dins de l'àmbit cientificotecnològic, el departament acorda on es treballa i s'avalua més cada saber. En aquesta programació:", False)])

# ------------------------------------------------------------------ 6. Capítol 4: calendari
p = find_par(doc, "El curs 2026-2027 comença el 8 de setembre de 2026")
set_par(p, [("El curs 2026-2027 comença el 8 de setembre de 2026 i acaba el 21 de juny de 2027. Les vacances de Nadal van del 22 de desembre al 7 de gener, i les de Setmana Santa, del 20 al 29 de març. Cada setmana hi ha una sessió de mig grup (dilluns i dimecres, una meitat cada dia) i una de grup sencer (dijous). Descomptant festius i dies de lliure disposició, hi ha 67 sessions possibles per a l'alumnat (98 hores de docència per al professor): 26 al primer trimestre, 19 al segon i 22 al tercer.", False)])
p = find_par(doc, "La programació ocupa 62 sessions")
set_par(p, [("La programació ocupa 62 sessions (sessió 0, 60 sessions de SdA i sessió de tancament) i deixa un marge de 5 sessions per a sortides, activitats del centre, imprevistos o una SdA que s'allargui. Per mantenir l'ordre de les sessions, quatre sessions de grup sencer es fan en dilluns amb tot el grup (intercanvi d'hora amb Biologia) i quatre sessions pensades per a mig grup que no són de laboratori es fan un dijous amb el grup sencer. El calendari complet, amb cada sessió pintada del color de la seva SdA, és a l'annex 11.", False)])
tbl = table_after_par(find_par(doc, "Taula 21. Hores per trimestre i marge"))
rows = tbl.findall(W + 'tr')
vals = [["1r (set.–des.)", "Sessió 0 · SdA 1 · SdA 2 · SdA 3 (sessions 1–3)", "24", "26", "2"],
        ["2n (gen.–març)", "SdA 3 (sessions 4–10) · SdA 4 · SdA 5 (sessió 1)", "18", "19", "1"],
        ["3r (abr.–juny)", "SdA 5 (sessions 2–13) · SdA 6 · sessió de tancament", "20", "22", "2"],
        ["Total", "", "62", "67", "5"]]
for tr, v in zip(rows[1:], vals):
    for tc, x in zip(tr.findall(W + 'tc'), v):
        cell_set(tc, [(x, tr is rows[-1] and x != "")])
cell_set(rows[0].findall(W + 'tc')[3], [("Sessions disponibles", True)])

p = find_par(doc, "Pla B del 2n trimestre (1 hora de marge).")
set_par(p, [("Pla B del 2n trimestre (1 sessió de marge). ", True), ("Si es perd més d'una sessió, el taller de problemes de la SdA 4 (sessió 7) es fa a casa amb el solucionari i es corregeix en 10 minuts a la sessió 8, i la sessió 1 de la SdA 5 passa al 3r trimestre, que té 2 sessions de marge.", False)])
p = find_par(doc, "Calendari de la tasca de recuperació.")
set_par(p, [("Calendari de les tasques de recuperació. ", True), ("Hi ha una tasca de recuperació per a cada competència específica. L'alumnat amb una CE en NA la rep en acabar la darrera SdA on s'avalua aquella CE (CE2 i CE3 a la SdA 4; CE1 i CE5 a la SdA 5; CE4 i CE6 a la SdA 6). El termini és de deu dies, amb una tutoria de 10 minuts a mitja tasca, i la defensa oral es fa abans de la sessió d'avaluació final. Si la SdA 6 acaba després del 7 de juny, les tasques de la CE4 i la CE6 es redueixen als apartats essencials i la defensa es fa a la sessió de tancament.", False)])

# ------------------------------------------------------------------ 7. Capítol 5: metodologia
p = find_par(doc, "Analogies. A les activitats de modelització")
clone_after(p, [("Mètode 1-2-4. ", True), ("Les fitxes de desenvolupament i de pràctica es fan en tres moments: primer cada alumne la resol individualment (1), després la contrasta i la corregeix amb el company o companya (2) i finalment el grup de quatre posa en comú els dubtes i les respostes (4) abans de la correcció amb el solucionari. Així tothom pensa abans de parlar, l'error es comenta entre iguals i el professor atén els dubtes que el grup no ha pogut resoldre. L'annex 13 en mostra un exemple de cada tipus d'activitat.", False)])
p = find_par(doc, "Agrupaments. Grups de treball heterogenis")
set_par(p, [("Agrupaments. ", True), ("Tant els dos grups de desdoblament com els grups de treball són heterogenis i es formen de manera estratègica, no per ordre alfabètic: es barreja alumnat que té més facilitat amb alumnat que en té menys, perquè s'ajudin i es coregulin, i es tenen en compte el gènere, la llengua i les necessitats de suport. Els grups de treball són de tres o quatre alumnes, estables durant una SdA, amb rols rotatius (coordinació, material i seguretat, registre de dades, portaveu) repartits de manera equilibrada per gènere i per perfil. A la SdA 4 es fa servir el trencaclosques (cada membre és expert en una part del dossier) i a la SdA 6, grups de tres per al pla.", False)])

# ------------------------------------------------------------------ 8. SdA 2: coavaluació del vídeo i continguts bàsics
sub_all(doc, r"Presentació dels vídeos i coavaluació amb la rúbrica \(els vídeos seleccionats es passen a 1r\)\.",
        "Presentació dels vídeos amb el full «Avaluem els vídeos»: m'avaluo (autoavaluació), t'avaluo (coavaluació entre iguals), ens avaluem (el grup) i us avaluem (un altre grup, amb la rúbrica del professor). Els vídeos seleccionats es passen a 1r.")
p = find_par(doc, "Taula 38.") if False else None
for tr in body.iter(W + 'tr'):
    t = ptext(tr)
    if t.startswith("Addicionals") and "Glossari visual trilingüe" in t:
        cell_set(tr.findall(W + 'tc')[1], [("Glossari visual trilingüe i fitxa 1 amb suport visual per a l'alumnat nouvingut (banc de paraules, frases model, vocabulari traduït a la llengua d'origen, diccionari i company de suport); fitxa 1 amb continguts bàsics per a l'alumnat amb retard en l'aprenentatge; versió guiada de la fitxa 2 i de l'informe; temps addicional a l'activitat de demostració.", False)])

# ------------------------------------------------------------------ 9. Capítol 7: avaluació
p = find_par(doc, "Cada rúbrica descriu quatre nivells (AE, AN, AS i NA)")
n1 = clone_after(p, [("Autoavaluació i coavaluació. ", True), ("L'alumnat participa en la seva avaluació de quatre maneres: m'avaluo (autoavaluació: diana, esmena amb bolígraf verd), t'avaluo (coavaluació entre iguals, amb un punt fort i una proposta de millora), ens avaluem (avaluació del propi grup) i us avaluem (un grup avalua el producte d'un altre grup amb la mateixa rúbrica del professor). Per exemple, a la sessió 10 de la SdA 2 cada alumne s'autoavalua, avalua un company, el grup avalua el seu vídeo i el d'un altre grup (annex 16). Aquestes valoracions són formatives i complementen la del professor.", False)])
clone_after(n1, [("Dossier de la SdA. ", True), ("A cada SdA, l'alumne fa un dossier on guarda i presenta totes les fitxes i fulls que ha fet, en ordre, amb el full de ruta a la portada, les esmenes amb bolígraf verd i la diana. El dossier és el registre del procés d'aprenentatge de l'alumne: el revisa el professor en acabar cada SdA i el fa servir l'alumne per preparar l'activitat de demostració d'assoliment.", False)])
for tr in body.iter(W + 'tr'):
    if ptext(tr).startswith("Full de ruta i portafoli"):
        cell_set(tr.findall(W + 'tc')[0], [("Full de ruta i dossier de la SdA", False)])

p = find_par(doc, "7.3 Instruments qualificadors i pesos", style="Heading2")
set_par(p, [("7.3 Evidències d'assoliment de cada SdA", False)])
p = find_par(doc, "A cada SdA es qualifiquen el producte final")
set_par(p, [("A cada SdA es recullen tres o quatre evidències d'assoliment: el producte final, un o dos fulls o laboratoris i una activitat de demostració d'assoliment, individual i amb situacions noves. Cap evidència no té un pes en percentatge: totes es valoren amb els mateixos quatre nivells i cap evidència aïllada no decideix el nivell, perquè cada criteri es valora a partir de diverses evidències. Les evidències i els criteris de cada SdA són a les taules «Instruments d'avaluació» del capítol 6.", False)])

p = find_par(doc, "7.4 Procediment de qualificació", style="Heading2")
set_par(p, [("7.4 Com s'obté el nivell d'assoliment", False)])
p = find_par(doc, "La qualificació s'expressa en els nivells d'assoliment")
set_par(p, [("No avaluem amb notes numèriques: avaluem assoliments. Apliquem els criteris d'avaluació, treballem els sabers i l'alumnat assoleix les competències. El resultat s'expressa en els nivells d'assoliment de l'article 29.2 del Decret 175/2022: no assoliment (NA), assoliment satisfactori (AS), assoliment notable (AN) i assoliment excel·lent (AE). Per combinar evidències, cada nivell es converteix en un valor de l'1 al 4 (NA = 1, AS = 2, AN = 3, AE = 4), i es fa en tres passos:", False)])
p = find_par(doc, "De les evidències al criteri.")
set_par(p, [("De les evidències al criteri. ", True), ("Cada aspecte d'una rúbrica i cada activitat de demostració d'assoliment dona un nivell al criteri que avalua. El nivell del criteri és la mitjana dels seus valors, arrodonida a l'alça.", False)])
p = find_par(doc, "Dels criteris a la competència.")
set_par(p, [("Dels criteris a la competència. ", True), ("El nivell de cada CE és la mitjana dels valors dels seus criteris, arrodonida a l'alça (per exemple, 2,3 → AN). Si un criteri o una CE s'han recuperat (apartat 7.6), compta el nivell més alt.", False)])
p = find_par(doc, "De les competències a la matèria.")
set_par(p, [("De les competències a la matèria. ", True), ("El nivell de la matèria és la mitjana dels valors de les sis CE, que compten igual, arrodonida a l'alça, amb les condicions de la taula següent.", False)])
tbl = table_after_par(find_par(doc, "Taula 63. Nivell de la matèria segons el perfil"))
newrows = [("Assoliment satisfactori (AS)", "Mitjana de les CE superior a 1 (arrodonida a l'alça, 2) i com a mínim 4 de les 6 CE en AS o més"),
           ("Assoliment notable (AN)", "Mitjana superior a 2 (arrodonida a l'alça, 3) i cap CE en NA"),
           ("Assoliment excel·lent (AE)", "Mitjana superior a 3 (arrodonida a l'alça, 4) i cap CE per sota d'AN"),
           ("No assoliment (NA)", "No es compleixen les condicions de l'AS")]
for tr, (a, b) in zip(tbl.findall(W + 'tr')[1:], newrows):
    tcs = tr.findall(W + 'tc'); cell_set(tcs[0], [(a, False)]); cell_set(tcs[1], [(b, False)])
p = find_par(doc, "Així, una CE no assolida no suspèn la matèria")
set_par(p, [("Així, una CE no assolida no impedeix assolir la matèria si les altres la compensen, però l'assoliment demana una base sòlida a la majoria de competències. Exemples:", False)])
ex = [("2 CE en AN, 2 en AS i 2 en NA: mitjana (3 + 3 + 2 + 2 + 1 + 1) / 6 = 2,0 i 4 CE assolides → AS.", False),
      ("4 CE en AS i 2 en NA: mitjana 1,7, que arrodonida a l'alça dona 2, però només hi ha 4 CE assolides → AS; amb 3 CE en NA no s'arriba a les 4 CE assolides → NA, i cal fer les tasques de recuperació (apartat 7.6).", False),
      ("3 CE en AE i 3 en AN: mitjana 3,5 → AE, perquè cap CE no és per sota d'AN.", False)]
for (t, _), pp in zip(ex, [find_par(doc, "2 CE en AN, 2 en AS i 2 en NA"), find_par(doc, "4 CE en AS i 2 en NA"), find_par(doc, "3 CE en AE i 3 en AN")]):
    set_par(pp, [(t, False)])
p = find_par(doc, "Quan l'evolució del curs mostra una millora clara")
set_par(p, [("Els valors de l'1 al 4 són només una eina interna de càlcul: el que es comunica a l'alumnat i a les famílies és el nivell d'assoliment (art. 29.2). El procediment s'ajusta als criteris que fixi el centre en el seu projecte educatiu (art. 23.3) i té en compte el caràcter continu de l'avaluació (art. 23.2). El professor registra les evidències per criteri en un instrument de registre sistemàtic (art. 23.8), a la zona del professorat del llibre digital, que calcula automàticament el nivell de cada criteri i de cada CE i el seguiment de les recuperacions (annex 12).", False)])

# recuperació
p = find_par(doc, "Tasca de recuperació final (CE4 i CE6).")
set_par(p, [("Tasca de recuperació de cada CE. ", True), ("Si en acabar la darrera SdA on s'avalua una CE l'alumne la té en NA, fa la tasca de recuperació d'aquella CE.", False)])
for tr in body.iter(W + 'tr'):
    tcs = tr.findall(W + 'tc')
    if len(tcs) == 3 and ptext(tcs[2]) == "Tasca de recuperació final":
        ce = ptext(tcs[0])[0]
        cell_set(tcs[2], [(f"Tasca de recuperació de la CE{ce}", False)])
p = find_par(doc, "CE que es tanquen a la SdA 6 (CE4 i CE6).")
set_par(p, [("Tasques de recuperació per CE. ", True), ("Hi ha sis tasques de recuperació, una per a cada competència específica, amb el mateix format: un repte amb temes a triar, parts guiades que recullen tots els criteris de la CE, un calendari amb una tutoria a mitja tasca, una defensa oral de 3 minuts i una rúbrica de quatre nivells per criteri. CE1: explicar un fenomen amb un model i resoldre un problema real (infografia o vídeo per a 1r). CE2: una petita recerca a casa, de la pregunta a l'informe, i la contribució d'una científica. CE3: fitxa de dades i de seguretat de productes de casa (pictogrames, unitats, formulació i gràfica). CE4: pòdcast que defensa un punt de vista amb fonts fiables. CE5: microprojecte per canviar un hàbit de casa i mesurar-ne l'efecte. CE6: línia del temps d'una idea científica i proposta sostenible sense biaixos de gènere. El nivell obtingut substitueix l'anterior si és més alt. També les pot fer l'alumnat que vulgui millorar el seu nivell. Són al llibre de l'alumnat i al llibre digital, i l'annex 17 en mostra una.", False)])

# ------------------------------------------------------------------ 10. Capítol 8: diversitat
p = find_par(doc, "D'acord amb el Decret 150/2017 i l'article 19 del Decret 175/2022")
set_par(p, [("D'acord amb el Decret 150/2017 i l'article 19 del Decret 175/2022, a l'aula de Física i química s'apliquen dos tipus de mesures: les universals, per a tot el grup i comunes a totes les SdA, i les addicionals, per a l'alumnat amb NESE que les necessita, que es concreten a la plantilla de cada SdA. Les mesures intensives no les aplica el professor de la matèria i no formen part d'aquesta programació. El grup inclou alumnat amb dislèxia, nouvingut, amb TDAH, amb TEA, d'altes capacitats i amb retard en l'aprenentatge, i per a cada perfil hi ha un exemple de fitxa adaptada (annex 14); l'annex 15 mostra sencera la fitxa per a l'alumnat amb retard en l'aprenentatge. Els materials adaptats tenen el mateix títol que la fitxa ordinària perquè cap alumne se senti assenyalat, mantenen els mateixos criteris i s'avaluen amb els mateixos nivells d'assoliment.", False)])
tbl = table_after_par(find_par(doc, "Taula 65. Mesures addicionals"))
for tr in tbl.findall(W + 'tr'):
    tcs = tr.findall(W + 'tc')
    if ptext(tcs[1]) == "Alumnat nouvingut":
        cell_set(tcs[3], [("Glossari trilingüe amb columna per a la llengua familiar, traducció del vocabulari clau a la llengua d'origen, diccionari (també digital), company o companya de suport al costat, banc de paraules, frases model i respostes amb dibuix; coordinació amb l'aula d'acollida", False)])
    if ptext(tcs[1]) == "Dislèxia":
        cell_set(tcs[3], [("Lletra d'alta llegibilitat de 13 punts, interlineat 1,7, fons crema, escala de prefixos dibuixada, exemples resolts, menys ítems; lectura en veu alta (també al llibre digital), 25 % més de temps i resposta oral d'una part de l'activitat de demostració", False)])
row = None
for tr in tbl.findall(W + 'tr'):
    if ptext(tr.findall(W + 'tc')[1]) == "Alumnat nouvingut":
        row = tr
new = add_row(tbl, ["2", "Retard en l'aprenentatge", "Fitxa 1 · El model de partícules (continguts bàsics)", "Continguts reduïts als essencials amb el mateix criteri (1.2), banc de paraules, frases per completar, respostes de selecció, dibuixos model i company de suport; objectiu: arribar a l'AS i passar a la fitxa ordinària"], like=list(tbl.findall(W + 'tr')).index(row))
new2 = add_row(tbl, ["3", "Altes capacitats", "Dossier d'ampliació de la SdA 3", "Reptes de més profunditat (no d'avançament de temari) per a quan acaben la feina: càlcul, problemes de Fermi, dades reals i disseny; rol d'expert o de mentor al grup"], like=list(tbl.findall(W + 'tr')).index(new))
p = find_par(doc, "Altres mesures addicionals que s'apliquen quan cal")
set_par(p, [("Altres mesures addicionals que s'apliquen quan cal: versions guiades de les fitxes clau amb el primer exercici resolt, ubicació a l'aula, temps addicional a les activitats de demostració, enunciats llegits en veu alta i possibilitat de respondre una part oralment.", False)])

# ------------------------------------------------------------------ 11. Annexos
p = find_par(doc, "Els annexos (10 fulls a doble cara) es presenten")
tbl = table_after_par(p)
AN = [("1–6", "Fitxa resum de cada SdA: repte, temporització, competències i criteris, objectius d'aprenentatge, producte i atenció a la diversitat; cada sessió amb el tipus d'activitats i què s'hi fa; evidències d'assoliment amb la sessió i els criteris"),
      ("7", "Full de ruta de l'alumne (SdA 5), en blanc: una targeta per sessió que l'alumne emplena en acabar-la (instrument organitzatiu)"),
      ("8", "Sondeig d'idees prèvies de la sessió 0 (avaluació inicial), primera pàgina"),
      ("9", "Full de la sessió de tancament del curs"),
      ("10", "Rúbriques del producte final i de l'explicació de la SdA 2"),
      ("11", "Calendari del curs: dies de classe de cada SdA, desdoblaments i grup sencer (instrument organitzatiu)"),
      ("12", "El llibre digital com a recurs didàctic: captures del llibre de l'alumnat, de les fitxes digitals, del laboratori virtual de forces de tracció i del registre d'avaluació"),
      ("13", "Tipus d'activitats: un exemple de cada fase del cicle d'aprenentatge (SdA 2) i mètode 1-2-4"),
      ("14", "Atenció a la diversitat: un exemple de fitxa adaptada per a cada perfil (dislèxia, nouvingut, TDAH, TEA, altes capacitats i continguts bàsics)"),
      ("15", "Exemple de fitxa adaptada sencera: retard en l'aprenentatge (fitxa 1 de la SdA 2 amb continguts bàsics i bastida)"),
      ("16", "Autoavaluació i coavaluació: m'avaluo, t'avaluo, ens avaluem i us avaluem"),
      ("17", "Tasca de recuperació de la CE1: enunciat i rúbrica")]
trs = tbl.findall(W + 'tr')
for tr in trs[2:]:
    tbl.remove(tr)
for a, b in AN[1:]:
    add_row(tbl, [a, b])
cell_set(tbl.findall(W + 'tr')[1].findall(W + 'tc')[1], [(AN[0][1], False)])

# referències a annexos dins del text
sub_all(doc, r"als annexos 8 i 9", "als annexos 8 i 9")
sub_all(doc, r"Avaluació formativa i formadora, amb rúbriques", "Avaluació formativa i formadora, amb rúbriques")

# espais buits després de les taules: 6 punts
els = list(body.iterchildren())
for i, el in enumerate(els):
    if el.tag == W + 'p' and i > 0 and els[i - 1].tag == W + 'tbl' and not ptext(el).strip() and el.find('.//' + W + 'sectPr') is None:
        ppr = el.find(W + 'pPr')
        if ppr is None:
            ppr = el.makeelement(W + 'pPr', {}); el.insert(0, ppr)
        sp = ppr.find(W + 'spacing')
        if sp is None:
            sp = ppr.makeelement(W + 'spacing', {}); ppr.append(sp)
        sp.set(W + 'line', '120'); sp.set(W + 'lineRule', 'exact'); sp.set(W + 'before', '0'); sp.set(W + 'after', '0')
sub_all(doc, r"Les proves i els fulls de laboratori es fan a classe", "Les activitats de demostració i els fulls de laboratori es fan a classe")

# ------------------------------------------------------------------ 13. Sense mesures intensives: només universals i addicionals
for tbl in list(body.iter(W + 'tbl')):
    for tr in list(tbl.findall(W + 'tr')):
        tcs = tr.findall(W + 'tc')
        if tcs and ptext(tcs[0]).strip() == "Intensives":
            tbl.remove(tr)
        elif tcs and ptext(tcs[0]).startswith("Alumne amb pla de suport individualitzat"):
            cell_set(tcs[0], [("Alumne amb necessitats educatives especials que necessita suport manipulatiu i visual", False)])
            cell_set(tcs[2], [("Mesura addicional: fitxa amb suport manipulatiu, mateixos criteris i rol definit als grups (SdA 3)", False)])
        elif tcs and ptext(tcs[0]).strip() == "Addicionals" and "taula periòdica acolorida" in ptext(tcs[1]):
            sub_in_par(tcs[1].findall(W + 'p')[-1], r"temps addicional a l'activitat de demostració\.", "temps addicional a l'activitat de demostració; fitxa «Dins de l'àtom i la taula periòdica» amb suport manipulatiu (models de Bohr per comptar electrons, taula periòdica simplificada i relació element–part del mòbil) i rol de registre a la campanya per a l'alumnat amb NESE que ho necessita.")
sub_all(doc, r"universalitat del currículum \(DUA: pla individualitzat amb versions simplificades de l'àtom i la taula periòdica\)", "universalitat del currículum (DUA: versions amb suport manipulatiu de l'àtom i la taula periòdica)")
sub_all(doc, r"seguiment de l'alumnat amb mesures addicionals i intensives", "seguiment de l'alumnat amb mesures addicionals")
# 8.3 fora; 8.4 passa a 8.3 (també a l'índex)
h = find_par(doc, "8.3 Mesures intensives", style="Heading2")
nxt = h.getnext()
while nxt is not None and not ptext(nxt).startswith("8.4 Altes capacitats"):
    rm = nxt; nxt = nxt.getnext(); rm.getparent().remove(rm)
h.getparent().remove(h)
toc = find_par(doc, "8.3 Mesures intensives")
toc.getparent().remove(toc)
sub_all(doc, r"^8\.4 Altes capacitats", "8.3 Altes capacitats")

# ------------------------------------------------------------------ 14. Revisió de coherència (octubre)
REV = [
 (r"una tasca de recuperació per a les competències que es tanquen a final de curs", "una tasca de recuperació per a cada competència específica"),
 (r"^Laboratori a les hores desdoblades, amb dotze pràctiques", "Laboratori a les hores desdoblades, amb onze pràctiques d'alumnat (la difusió de la SdA 5 és una demostració del docent en grup sencer)"),
 (r"i entenent la recerca com una tasca$", "i entenent la recerca com una tasca col·lectiva i interdisciplinària en constant evolució, influïda pel context polític i els recursos econòmics."),
 (r"A 3r es treballen tots els sabers del bloc, amb una mica més de profunditat", "A 3r es treballen 34 dels 35 sabers, amb una mica més de profunditat"),
 (r"i de la SdA 5 a l'abril \(MRUA\)", "i de la SdA 5 a l'abril (sessió 2, MRU)"),
 (r"La SdA 6 ha d'acabar la primera setmana de juny\. Si es perden sessions pel calendari de final de curs:", "Segons el calendari, la SdA 6 acaba el 16 de juny i la sessió de tancament és el 17. Si es perden sessions:"),
 (r"L'alumnat amb una CE en NA la rep en acabar la darrera SdA on s'avalua aquella CE \(CE2 i CE3 a la SdA 4; CE1 i CE5 a la SdA 5; CE4 i CE6 a la SdA 6\)\. El termini és de deu dies, amb una tutoria de 10 minuts a mitja tasca, i la defensa oral es fa abans de la sessió d'avaluació final\. Si la SdA 6 acaba després del 7 de juny, les tasques de la CE4 i la CE6 es redueixen als apartats essencials i la defensa es fa a la sessió de tancament\.",
  "L'alumnat amb una CE en NA la rep en acabar la darrera SdA on s'avalua aquella CE: la CE3 en acabar la SdA 4, la CE2 i la CE5 en acabar la SdA 5, i la CE1, la CE4 i la CE6 en acabar la SdA 6. Les tasques de la CE4 i de la CE6 es lliuren a la sessió de tancament, després d'avaluar-les a la SdA 6, i no a l'inici d'aquesta SdA. El termini és de deu dies, amb una tutoria de 10 minuts a mitja tasca, i la defensa oral es fa abans de la sessió d'avaluació final; compta el nivell més alt."),
 (r"^Simulacions: PhET \(estats de la matèria, propietats dels gasos, construeix un àtom, dispersió de Rutherford, circuits\) i un simulador propi de la bateria de liti\.",
  "Simulacions: PhET (densitat, sucre i sal, propietats dels gasos, estats de la matèria, dispersió de Rutherford, construeix un àtom, ajust d'equacions, difusió i circuits), una taula periòdica interactiva i dos simuladors propis (model cineticomolecular dels gasos i bateria de liti)."),
 (r"\(sessions 1–3 abans de Nadal; 4–10 al gener\)", "(sessions 1–3 abans de Nadal; 4–10 al gener i a principis de febrer)"),
 (r"activitat de demostració \(activitats 4\)", "activitat de demostració (activitat 4)"),
 (r"activitat de demostració \(activitats 2\)", "activitat de demostració (activitat 2)"),
 (r"^Fitxa d'evolució dels models, activitat de demostració$", "Fitxa 2 (evolució dels models), activitat de demostració"),
 (r"^Fitxa d'evolució dels models \(evidència d'assoliment\)$", "Fitxa 2, part A: evolució dels models (evidència d'assoliment)"),
 (r"^Fitxa d'evolució dels models atòmics$", "Fitxa 2 · Evolució dels models atòmics (part A)"),
 (r"\(sessions 1–2 abans de Setmana Santa; 3–13 a l'abril i al maig\)", "(sessió 1 abans de Setmana Santa; 2–13 a l'abril i al maig)"),
 (r"Aula ordinària i laboratori \(sessions 6 i 10\)\.", "Aula ordinària; problemes en mig grup (sessió 6); demostració de difusió en grup sencer (sessió 7); laboratori de Hooke en mig grup (sessió 10)."),
 (r"Aigua calenta preparada pel professor \(sessió 6\)", "Aigua calenta preparada pel professor (sessió 7)"),
 (r"^Pregunta: «Dos cotxes van a 50 km/h\. Han de fer el mateix moviment\?»\.", "Reactivació després de Setmana Santa (repte i hipòtesis de la sessió 1) i pregunta: «Dos cotxes van a 50 km/h. Han de fer el mateix moviment?»."),
 (r"^Reactivació després de Setmana Santa i correcció de la fitxa 1\.", "Correcció de la fitxa 1 i resolució de dubtes."),
 (r"Diana de final de curs i lliurament de la tasca de recuperació de les CE4 i CE6 a qui la necessiti\.", "Diana de final de curs. Lliurament de les tasques de recuperació de la CE4 i de la CE6 a qui les té en NA, després d'haver-les avaluat a la SdA 6."),
 (r"^Encàrrec de la direcció i presentació del repte i de les rúbriques; primeres idees\.", "Encàrrec de la direcció i presentació del repte i de les rúbriques; primeres idees."),
 (r"Si en acabar la darrera SdA on s'avalua una CE l'alumne la té en NA, fa la tasca de recuperació d'aquella CE\.", "Si en acabar la darrera SdA on s'avalua una CE l'alumne la té en NA, fa la tasca de recuperació d'aquella CE. Les de la CE4 i la CE6 es lliuren a la sessió de tancament, després d'avaluar-les a la SdA 6, i no a l'inici d'aquesta SdA."),
 (r"La versió de l'alumnat explica què cal fer per arribar a cada nivell, sense codis curriculars; la versió del professor indica, a més, el criteri que avalua cada aspecte\.", "La rúbrica explica què cal fer per arribar a cada nivell i indica, sota cada aspecte, el criteri d'avaluació que recull, perquè l'alumnat sàpiga què se li avalua."),
 (r"25 % més de temps", "temps addicional"),
 (r"\(DOGC núm\. 9688, 17\.6\.2026\)", "(BOPB, 10.6.2026; DOGC núm. 9688, 17.6.2026)"),
]
for a, b_ in REV:
    n = sub_all(doc, a, b_)
    if n == 0:
        print("  REVISIÓ sense coincidències:", a[:70])
# Taula 29: lectura de la SdA 5 a la sessió 8; taula 54: fitxa 6 a la sessió 8; objectius O2–O4 de la SdA 3 amb el criteri 6.1
for tbl in body.iter(W + 'tbl'):
    for tr in tbl.findall(W + 'tr'):
        tcs = tr.findall(W + 'tc')
        t0 = ptext(tcs[0]).strip() if tcs else ""
        if t0 == "5" and len(tcs) == 3 and "febre i el moviment" in ptext(tcs[1]):
            cell_set(tcs[2], [("Sessió 8, activitat 8.2", False)])
        if t0.startswith("La febre i la migració (fitxa 6)") and len(tcs) == 5:
            cell_set(tcs[3], [("8", False)])
        if t0 in ("O2", "O3", "O4") and len(tcs) == 4 and ptext(tcs[2]).strip() == "5.1" and any(w in ptext(tcs[1]) for w in ("bateria de liti", "taula periòdica", "assaig a la flama")):
            cell_set(tcs[2], [("6.1", False)])
        if t0 == "2.3" and len(tcs) == 6 and "Construeix un àtom" in ptext(tcs[3]):
            cell_set(tcs[5], [("Fitxa 2, part B (formativa)", False)])

# ------------------------------------------------------------------ 12. Paper i llibre digital; hiperenllaços
import prog_links
p = find_par(doc, "Llibre digital de l'aula:")
set_par(p, [("Llibre web i llibre digital: ", True), ("el llibre web (llibrefiq3r.cat) té totes les sessions, els fulls de l'alumnat, les simulacions i els reptes d'ampliació, i una zona del professorat amb activitats de demostració, solucionaris, rúbriques, materials adaptats i un registre d'avaluació per criteris; el llibre digital (llibrefiq3r.cat/digital) té les mateixes fitxes per respondre-les en línia. La majoria de classes es fan en paper, sense ordinador: l'alumnat treballa amb els fulls impresos i el seu dossier. El professor fa servir el llibre digital quan li convé rebre automàticament les respostes de l'alumnat (per exemple, el sondeig inicial o una fitxa que vol revisar abans de la sessió següent), i de tant en tant l'alumnat treu l'ordinador per fer les simulacions. Al capítol 6, cada sessió i cada full enllacen amb la seva pàgina del llibre.", False)])
link_phrase(doc, p, "llibrefiq3r.cat/digital", prog_links.B + "digital/")
link_phrase(doc, p, "llibrefiq3r.cat", prog_links.B)
print("enllaços:", prog_links.apply(doc))
_c, _m = prog_links.link_tables(doc)
print("enllaços a les taules:", _c)
for x in _m: print("   sense enllaç:", x)
# índex: títols nous
sub_all(doc, r"^7\.3 Instruments qualificadors i pesos", "7.3 Evidències d'assoliment de cada SdA")
sub_all(doc, r"^7\.4 Procediment de qualificació", "7.4 Com s'obté el nivell d'assoliment")
doc.save(OUT)
print("desat", OUT)
for k, v in cnt.items():
    if v == 0:
        print("  sense coincidències:", k[:60])
