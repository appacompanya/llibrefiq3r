"""Tasques de recuperació: una per a cada competència específica (CE1–CE6), totes amb el mateix format
(repte amb temes a triar, parts guiades, calendari, rúbrica per criteris i nota per al professorat)."""
import gen_sda1 as G
import figs
from mn_common import use, page, table, teacher_note, q, lines, BADGE_CSS

# color neutre del curs per a les tasques de recuperació
CURS = {"n": 0, "title": "Tasques de recuperació", "color": "#3B4A5C", "tint": "#E7EBF0"}
CE_TXT = {
    1: "Interpretar fenòmens de la naturalesa, predient i argumentant-ne el comportament a partir de models, lleis i teories propis de la física i la química.",
    2: "Dissenyar, desenvolupar i comunicar recerques, incloent-hi la formulació de preguntes i d'hipòtesis i la seva contrastació experimental.",
    3: "Generar, interpretar i validar dades i informació en diferents formats i fonts, fent servir el llenguatge científic i usant de manera responsable i segura el material de laboratori.",
    4: "Utilitzar de forma crítica i eficient plataformes tecnològiques i recursos variats per cercar informació, crear materials i comunicar-se sobre qüestions ecosocialment rellevants.",
    5: "Analitzar els efectes de determinades accions sobre el medi ambient i la salut, basant-se en la física i la química, per fer propostes d'acció i adoptar hàbits sostenibles i saludables.",
    6: "Interpretar i valorar la ciència com una construcció col·lectiva en continu canvi i evolució, que interacciona amb la societat per generar millores.",
}
LAST = {1: "la SdA 5", 2: "la SdA 4", 3: "la SdA 4", 4: "la SdA 6", 5: "la SdA 5", 6: "la SdA 6"}
WHERE = {1: "SdA 2 i SdA 5", 2: "SdA 1 i SdA 4", 3: "SdA 1 i SdA 4", 4: "SdA 2 i SdA 6", 5: "SdA 3 i SdA 5", 6: "SdA 3 i SdA 6"}


def head(ce, title, intro):
    G.SDA.update(CURS)
    who = '<div class="who"><span>Nom <i></i></span><span>Grup <i></i></span><span>Data <i></i></span></div>'
    h = (f'<div class="head"><div><div class="kick">Física i química · 3r ESO · Tasca de recuperació de la CE{ce}</div>'
         f'<h1>{title}<span class="badge">Recuperació CE{ce}</span></h1></div>{who}</div>')
    h += f'<p class="intro">{intro}</p>'
    h += (f'<div class="tip" style="padding:2mm 3mm"><b>Competència específica {ce}.</b> {CE_TXT[ce]} '
          f'La vas treballar a la {WHERE[ce]}. Si fas aquesta tasca millor que durant el curs, el nivell d\'assoliment nou substitueix l\'anterior.</div>')
    return h


def calendari(ce, rows=None):
    if rows is None and ce in (4, 6):
        sda = "la SdA 2" if ce == 4 else "la SdA 3"
        rows = [[f"A l'inici de la SdA 6, si tinc la CE{ce} en NA a {sda}", "Rebo la tasca, trio el tema i reviso la rúbrica."],
                ["Al cap de cinc dies", "Ensenyo l'esborrany de les parts A i B al professor (tutoria de 10 minuts)."],
                ["Al cap de deu dies", "Lliuro el producte (a l'aula virtual o en paper)."],
                ["Sessió de tancament", f"Defensa oral de 3 minuts. Compta el nivell més alt entre la tasca i la SdA 6."]]
    rows = rows or [[f"En acabar {LAST[ce]} (o quan t'ho indiqui el professor)", "Rebo la tasca, trio el tema i reviso la rúbrica."],
                    ["Al cap de cinc dies", "Ensenyo l'esborrany de les parts A i B al professor (tutoria de 10 minuts)."],
                    ["Al cap de deu dies", "Lliuro el producte (a l'aula virtual o en paper)."],
                    ["Abans de la sessió d'avaluació", "Defensa oral de 3 minuts amb el professor."]]
    return "<h2>Calendari i lliurament</h2>" + table(["Quan", "Què"], rows, widths=["34%", "66%"])


def done(b):
    return page(b, ".small{font-size:9.5pt;color:var(--muted);font-weight:400}td:empty{height:8mm}"), True


# ------------------------------------------------------------------ CE1
def recup_ce1():
    b = head(1, "Explica un fenomen amb la física i la química",
             "Prepara una infografia (un full A3 o una diapositiva) o un vídeo d'1 a 2 minuts per a l'alumnat de 1r d'ESO que expliqui un fenomen quotidià amb un model de la física i la química. Abans, resol les parts A, B i C del tema que triïs.")
    b += "<h2><span class='k'>0</span> Tria el fenomen</h2>"
    b += table(["Tema", "De què va", "Model que fas servir"], [
        ["<b>A · La roda de la bicicleta a l'estiu</b>", "Per què augmenta la pressió de la roda quan la bici es queda al sol?", "Model cineticomolecular i llei de Gay-Lussac (SdA 2)"],
        ["<b>B · El patinet que frena</b>", "Quina distància necessita un patinet per aturar-se?", "MRUA i gràfiques v–t (SdA 5)"],
        ["<b>C · Un altre fenomen</b>", "Proposa'n un al professor (per exemple, l'olla a pressió o la cèl·lula que persegueix un bacteri).", "El que correspongui"]], widths=["28%", "44%", "28%"])
    b += "<h2><span class='k'>A</span> Interpreta les dades</h2>"
    b += q(1, "<b>Tema A.</b> Hem mesurat la pressió de l'aire d'una roda tancada a diferents temperatures:" +
           table(["Temperatura (°C)", "10", "20", "30", "40"], [["Temperatura (K)", "", "", "", ""], ["Pressió (bar)", "2,40", "2,48", "2,57", "2,65"], ["p / T (bar/K)", "", "", "", ""]]) +
           "a) Completa la taula. b) Representa la pressió en funció de la temperatura en kelvin. c) Què tenen en comú els valors de p / T? Quina llei ho explica?")
    b += q(2, "<b>Tema B.</b> Un patinet frena en línia recta. Aquesta és la seva velocitat cada segon:" +
           table(["t (s)", "0", "1", "2", "3", "4"], [["v (m/s)", "6,0", "4,5", "3,0", "1,5", "0"]]) +
           "a) Representa la gràfica v–t. b) Quin tipus de moviment és? c) Calcula l'acceleració. d) Calcula la distància de frenada a partir de l'àrea sota la gràfica.")
    b += lines(4)
    b += "<h2><span class='k'>B</span> Explica-ho amb el model</h2>"
    b += q(3, "Explica el fenomen del teu tema amb el model. <b>Tema A:</b> dibuixa les partícules de l'aire de la roda a 10 °C i a 40 °C i explica per què augmenta la pressió. <b>Tema B:</b> explica què vol dir una acceleració negativa i per què la velocitat disminueix el mateix cada segon.")
    b += '<div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm"><div class="box" style="min-height:38mm">Abans</div><div class="box" style="min-height:38mm">Després</div></div>'
    b += q(4, "<b>Prediu.</b> Tema A: quina pressió tindrà la roda a 60 °C (l'asfalt a l'agost)? Tema B: quina distància de frenada tindria el patinet si anés a 3 m/s amb la mateixa acceleració? Justifica la predicció amb el model o la llei." + lines(4))
    b += '<div class="pb"></div>'
    b += "<h2><span class='k'>C</span> Un problema real i una solució</h2>"
    b += q(5, "<b>Tema A.</b> El fabricant de la roda recomana no passar de 2,8 bar. Algú l'infla a 2,40 bar un matí a 10 °C i la deixa al sol a 60 °C. És un problema? Proposa dues solucions. "
              "<b>Tema B.</b> El patinet va a 6 m/s i la persona triga 1 s a reaccionar abans de frenar (durant aquest segon continua a la mateixa velocitat). Calcula la distància total d'aturada i compara-la amb la d'un patinet a 4 m/s. Quina velocitat màxima proposaries davant d'una escola? Per què?" + lines(7))
    b += "<h2><span class='k'>D</span> El producte i la defensa</h2>"
    b += q(6, "Fes la infografia o el vídeo per a 1r d'ESO. Ha de tenir: el fenomen, el model (amb un dibuix), una dada o gràfica de la part A, la predicció i el consell final. Després, en una defensa de 3 minuts, respondràs dues preguntes del professor.")
    b += calendari(1)
    b += '<div class="pb"></div>'
    b += G.rub("Rúbrica de la tasca de recuperació de la CE1", [
        ("Interpretació de les dades (1.1)", "Completa la taula, fa la gràfica amb magnituds, unitats i escala adequada i n'extreu la regularitat amb raons científiques", "Taula i gràfica correctes; conclusió amb alguna imprecisió", "Taula o gràfica incompletes; conclusió poc justificada", "No interpreta les dades"),
        ("Explicació amb el model (1.2)", "Explica el fenomen amb el model o la llei adequats i el dibuix o l'esquema el representa sense errors", "Explicació correcta amb alguna imprecisió", "Explicació parcial o model mal aplicat", "No fa servir cap model"),
        ("Predicció (1.2)", "Fa la predicció amb el càlcul correcte i la justifica", "Predicció correcta amb poca justificació", "Predicció amb errors de càlcul", "No fa cap predicció"),
        ("Problema i solucions (1.3)", "Identifica els conceptes del problema, el resol amb unitats i proposa solucions viables i justificades", "Resol el problema i proposa una solució", "Resolució parcial o solució poc relacionada", "No resol el problema"),
    ])
    b += teacher_note([
        f"<b>Per a qui és:</b> l'alumnat amb NA a la CE1 en acabar {LAST[1]} (criteris 1.1, 1.2 i 1.3) o qui vulgui millorar el nivell. El nivell nou substitueix el de la CE1 a la SdA 2 i a la SdA 5 si és més alt.",
        "<b>Solucions.</b> Tema A: T = 283, 293, 303 i 313 K; p / T ≈ 0,00848 bar/K en tots els casos (constant): llei de Gay-Lussac, a volum constant la pressió és proporcional a la temperatura absoluta. A 60 °C (333 K): p ≈ 0,00848 · 333 ≈ <b>2,82 bar</b>, per sobre del màxim recomanat: cal desinflar una mica la roda a l'estiu o no deixar-la al sol. "
        "Tema B: MRUA; a = (0 − 6,0) / 4 = <b>−1,5 m/s²</b>; distància de frenada = ½ · 6,0 · 4 = <b>12 m</b>. A 3 m/s: t = 2 s i d = ½ · 3 · 2 = <b>3 m</b> (la meitat de velocitat, una quarta part de distància). "
        "Amb 1 s de reacció: 6 + 12 = <b>18 m</b>; a 4 m/s: 4 + 4² / (2 · 1,5) ≈ 4 + 5,3 = <b>9,3 m</b>.",
        "<b>Atenció a la diversitat:</b> es pot fer en parella amb un rol clar per a cadascú; l'alumnat amb dislèxia pot fer el producte en format vídeo; l'alumnat nouvingut, amb el glossari visual del curs.",
    ], title="Com funciona la recuperació · nota per al professorat, no s'imprimeix per a l'alumne")
    return done(b)


# ------------------------------------------------------------------ CE2
def recup_ce2():
    b = head(2, "Una petita recerca a casa",
             "Fes una recerca senzilla a casa, en parella (pot ser amb algú de la família), i presenta-la en un informe de dues pàgines o en un vídeo de 3 minuts. Fes servir només material de casa i aigua de l'aixeta (mai foc ni productes de neteja).")
    b += "<h2><span class='k'>0</span> Tria la recerca</h2>"
    b += table(["Recerca", "Material"], [
        ["<b>A · El glaçó.</b> De què depèn el temps que triga un glaçó a fondre's?", "Glaçons iguals, gots, aigua de l'aixeta, sal, cronòmetre del mòbil"],
        ["<b>B · La pastilla efervescent.</b> Es dissol més de pressa en aigua calenta?", "Pastilles efervescents iguals, gots, aigua freda i calenta de l'aixeta, termòmetre de cuina si en tens, cronòmetre"],
        ["<b>C · La goma elàstica.</b> Quant s'allarga segons el pes que hi pengem?", "Una goma, una bossa petita, monedes iguals o bosses d'aigua, regle"]], widths=["55%", "45%"])
    b += "<h2><span class='k'>A</span> La pregunta i la hipòtesi</h2>"
    b += q(1, "Escriu la pregunta d'investigació i una hipòtesi que es pugui comprovar. Justifica la hipòtesi amb el que has après a classe (per exemple, el model de partícules o la llei de Hooke)." + lines(4))
    b += "<h2><span class='k'>B</span> El disseny</h2>"
    b += q(2, "Completa la taula de variables i escriu els passos de manera que una altra persona pugui repetir l'experiment. Fes com a mínim tres repeticions de cada mesura." +
           table(["Variable", "Quina és"], [["Independent (la que canvio)", ""], ["Dependent (la que mesuro)", ""], ["Controlades (les que mantinc iguals)", ""]], widths=["38%", "62%"]) + lines(5))
    b += '<div class="pb"></div>'
    b += "<h2><span class='k'>C</span> Les dades i la interpretació</h2>"
    b += q(3, "Anota les mesures i calcula la mitjana. Després fes la gràfica adequada i interpreta-la: es confirma la hipòtesi? Quines fonts d'error hi ha hagut?" +
           table(["Valor de la variable independent", "Mesura 1", "Mesura 2", "Mesura 3", "Mitjana"], [["", "", "", "", ""] for _ in range(5)]) + lines(5))
    b += "<h2><span class='k'>D</span> Treballem en equip</h2>"
    b += q(4, "Explica com us heu repartit la feina (qui ha mesurat, qui ha anotat, qui ha fet la gràfica) i què ha aportat l'altra persona. Què faríeu diferent?" + lines(3))
    b += "<h2><span class='k'>E</span> La ciència la fan persones</h2>"
    b += q(5, "Tria una científica relacionada amb la teva recerca o amb una SdA del curs (per exemple, Ellen Swallow Richards, Marguerite Perey, Mária Telkes o Rosalind Franklin). Explica què va aportar, amb quines dificultats es va trobar pel fet de ser dona i per què creus que el seu nom és poc conegut. Cita la font." + lines(5))
    b += "<h2><span class='k'>F</span> El producte</h2>"
    b += q(6, "Presenta la recerca en un informe de dues pàgines o en un vídeo de 3 minuts amb aquest ordre: pregunta, hipòtesi, disseny, dades (taula i gràfica), conclusió i fonts d'error. Afegeix-hi fotos de l'experiment.")
    b += calendari(2)
    b += '<div class="pb"></div>'
    b += G.rub("Rúbrica de la tasca de recuperació de la CE2", [
        ("Pregunta i hipòtesi (2.1)", "Pregunta clara i hipòtesi comprovable justificada amb un model", "Pregunta i hipòtesi comprovables, poc justificades", "Hipòtesi vaga o difícil de comprovar", "Sense pregunta o hipòtesi"),
        ("Disseny (2.2)", "Identifica totes les variables, controla les altres i el procediment és reproduïble amb repeticions", "Variables correctes i procediment amb alguna mancança", "Variables mal identificades o procediment incomplet", "No dissenya el procediment"),
        ("Experimentació i interpretació (2.3)", "Mesures repetides, mitjanes i gràfica correctes; conclusió coherent i fonts d'error ben argumentades", "Dades i gràfica correctes; conclusió amb alguna imprecisió", "Dades incompletes o conclusió no relacionada amb les dades", "No hi ha dades"),
        ("Treball en equip (2.4)", "Rols clars i aportació valorada de l'altra persona; proposa millores", "Rols clars", "Repartiment poc clar", "No hi ha treball compartit"),
        ("Presentació dels resultats (2.5)", "Informe o vídeo ordenat, amb taula, gràfica i fotos; llenguatge científic adequat", "Presentació correcta amb algun element que falta", "Presentació desordenada o incompleta", "No es presenta"),
        ("La ciència la fan persones (2.6)", "Explica l'aportació de la científica, analitza els biaixos de gènere i cita la font", "Explica l'aportació i esmenta els biaixos", "Biografia sense reflexió", "No ho fa"),
    ])
    b += teacher_note([
        f"<b>Per a qui és:</b> l'alumnat amb NA a la CE2 en acabar {LAST[2]} (criteris 2.1 a 2.6) o qui vulgui millorar. El nivell nou substitueix el de la CE2 a la SdA 1 i a la SdA 4 si és més alt.",
        "<b>Resultats esperats.</b> A: el glaçó es fon més de pressa en aigua que a l'aire, i en aigua de l'aixeta que en aigua molt salada freda (cal controlar volum i temperatura de l'aigua). B: la pastilla es dissol més de pressa en aigua calenta (més energia cinètica de les partícules: més xocs eficaços). C: l'allargament és proporcional al pes fins al límit d'elasticitat (llei de Hooke); la gràfica F–Δx és una recta per l'origen.",
        "<b>Seguretat:</b> només aigua de l'aixeta (mai bullint), sense foc ni productes de neteja. Es pot fer a l'institut, a l'hora del pati, si a casa no és possible.",
        "<b>Atenció a la diversitat:</b> es pot donar la taula de variables mig completada a l'alumnat amb més dificultats; l'alumnat d'altes capacitats pot afegir una segona variable o calcular el pendent.",
    ], title="Com funciona la recuperació · nota per al professorat, no s'imprimeix per a l'alumne")
    return done(b)


# ------------------------------------------------------------------ CE3
def recup_ce3():
    b = head(3, "Dades, unitats i seguretat dels productes de casa",
             "Fes la fitxa de dades i de seguretat de dos productes que tinguis a casa (per exemple, alcohol de farmàcia, lleixiu, salfumant, un esprai o un detergent). No obris els envasos: només cal llegir-ne l'etiqueta. Després resol els càlculs i la part de formulació.")
    b += "<h2><span class='k'>A</span> Llegeix l'etiqueta i la seguretat</h2>"
    b += figs.picto_table()
    b += q(1, "Per a cada producte, copia els pictogrames, la paraula d'avís (Perill o Atenció) i dues frases de precaució. Explica què vol dir cada pictograma i on el guardaries a casa." +
           table(["Producte", "Pictogrames (codi i nom)", "Paraula d'avís", "Precaucions i on el guardo"], [["", "", "", ""], ["", "", "", ""]]))
    b += q(2, "<b>Al laboratori.</b> Escriu quatre normes del decàleg de seguretat de la classe relacionades amb aquests productes i explica per què protegeixen la salut, el medi ambient o les instal·lacions." + lines(4))
    b += '<div class="pb"></div>'
    b += "<h2><span class='k'>B</span> Unitats i càlculs</h2>"
    b += q(3, "Fes els càlculs amb factors de conversió i escriu el resultat amb unitats." +
           "<ol type='a'><li>Una ampolla de detergent conté 1,5 L i la densitat del detergent és 1,05 g/mL. Quina massa de detergent hi ha, en kg?</li>"
           "<li>Un lleixiu indica 40 g/L de clor actiu. Expressa-ho en mg/mL. Quina massa de clor actiu hi ha en una ampolla de 2 L?</li>"
           "<li>Un esprai conté 200 mL. Expressa el volum en L i en m³ (en notació científica).</li>"
           "<li>L'alcohol de farmàcia té una densitat de 0,81 g/cm³. Expressa-la en kg/m³.</li></ol>" + lines(6))
    b += "<h2><span class='k'>C</span> Formulació</h2>"
    b += q(4, "Escriu el nom o la fórmula d'aquestes substàncies, que trobem a casa o a l'entorn:" +
           table(["Fórmula o nom", "Nom o fórmula", "On la trobem"], [["NaCl", "", "sal de cuina"], ["HCl", "", "salfumant (dissolt en aigua)"], ["NH₃", "", "alguns netejadors"], ["diòxid de carboni", "", "begudes amb gas"], ["CH₄", "", "gas natural"], ["òxid de calci", "", "calç viva"], ["Fe₂O₃", "", "rovell"], ["diòxid de silici", "", "sorra i vidre"]], widths=["30%", "35%", "35%"]))
    b += "<h2><span class='k'>D</span> Genera i interpreta dades</h2>"
    b += q(5, "Un grup ha mesurat quant triga a dissoldre's una pastilla efervescent en aigua a diferents temperatures. També van anotar el color del got." +
           table(["Temperatura (°C)", "10", "20", "30", "40", "50"], [["Temps (s)", "90", "62", "44", "32", "24"], ["Color del got", "blau", "verd", "blau", "vermell", "verd"]]) +
           "a) Quina informació de la taula no és rellevant per a la pregunta? Per què? b) Representa el temps en funció de la temperatura. c) Descriu la relació i estima el temps a 35 °C. d) Explica el resultat amb la teoria de les col·lisions.")
    b += lines(5)
    b += "<h2><span class='k'>E</span> El producte</h2>"
    b += q(6, "Fes una fitxa resum (un full) dels dos productes per penjar a la classe: pictogrames i significat, precaucions, una dada amb unitats i la fórmula d'una substància que contenen o que hi està relacionada.")
    b += calendari(3)
    b += '<div class="pb"></div>'
    b += G.rub("Rúbrica de la tasca de recuperació de la CE3", [
        ("Dades en formats diversos (3.1)", "Descarta la dada irrellevant, fa la gràfica correcta, interpreta la relació i fa l'estimació", "Gràfica i interpretació correctes amb alguna imprecisió", "Gràfica incompleta o interpretació poc relacionada", "No interpreta les dades"),
        ("Unitats i eines matemàtiques (3.2)", "Tots els càlculs amb factors de conversió, unitats i notació científica correctes", "Algun error menor d'unitats o de càlcul", "Errors freqüents d'unitats", "No fa els càlculs"),
        ("Formulació IUPAC (3.2)", "Totes les fórmules i els noms correctes", "Un o dos errors", "Tres o quatre errors", "Més de quatre errors"),
        ("Seguretat i normes (3.3)", "Interpreta tots els pictogrames i relaciona les normes amb la salut, el medi ambient i les instal·lacions", "Interpreta els pictogrames i justifica les normes", "Interpretació parcial o normes sense justificar", "No interpreta les etiquetes"),
    ])
    b += teacher_note([
        f"<b>Per a qui és:</b> l'alumnat amb NA a la CE3 en acabar {LAST[3]} (criteris 3.1, 3.2 i 3.3) o qui vulgui millorar. El nivell nou substitueix el de la CE3 a la SdA 1 i a la SdA 4 si és més alt.",
        "<b>Solucions B.</b> a) 1500 mL · 1,05 g/mL = 1575 g = <b>1,575 kg</b>. b) 40 g/L = <b>40 mg/mL</b>; 40 g/L · 2 L = <b>80 g</b>. c) 200 mL = <b>0,200 L = 2 · 10⁻⁴ m³</b>. d) 0,81 g/cm³ = <b>810 kg/m³</b>.",
        "<b>Solucions C.</b> clorur de sodi; clorur d'hidrogen (àcid clorhídric en dissolució); amoníac; CO₂; metà; CaO; òxid de ferro(III); SiO₂.",
        "<b>Solucions D.</b> a) El color del got: no és una variable que afecti la velocitat de dissolució. c) Com més temperatura, menys temps (relació decreixent, no lineal); a 35 °C, uns 37–39 s. d) A més temperatura, les partícules es mouen més de pressa i xoquen més sovint i amb més energia: més xocs eficaços.",
        "<b>Seguretat:</b> recordeu que no cal obrir cap envàs; es poden fer servir fotografies d'etiquetes que doni el professor.",
    ], title="Com funciona la recuperació · nota per al professorat, no s'imprimeix per a l'alumne")
    return done(b)


# ------------------------------------------------------------------ CE4 (format original de la SdA 6)
TOPICS4 = [
    ("Les bateries de ió liti", "Del primer prototip als mòbils i els cotxes elèctrics. Connecta amb la SdA 3."),
    ("L'hidrogen verd", "Electròlisi, piles de combustible i autobusos d'hidrogen. Connecta amb la SdA 4."),
    ("L'energia solar fotovoltaica", "Les plaques dels terrats i l'autoconsum. Connecta amb la SdA 6."),
    ("El reciclatge dels mòbils", "Matèries primeres crítiques, residus i punts de recollida. Connecta amb la SdA 3."),
]


def recup_ce4():
    b = head(4, "Un pòdcast per defensar una idea",
             "Prepara un pòdcast o una presentació narrada de 3 a 4 minuts per a l'alumnat de 2n d'ESO que defensi el teu punt de vista sobre aquesta pregunta: <i>Aquesta tecnologia ens ajuda a ser una societat més sostenible?</i>")
    b += "<h2><span class='k'>0</span> El repte</h2>"
    b += "<p>Tria un d'aquests temes (o proposa'n un altre al professor):</p>"
    b += table(["Tema", "Per on començar"], [[f"<b>{t}</b>", d] for t, d in TOPICS4], widths=["32%", "68%"])
    b += "<h2><span class='k'>A</span> Cerca i avalua la informació</h2>"
    b += q(1, "Fes servir com a mínim <b>tres fonts</b> de tipus diferent (una institució pública o una universitat, un mitjà de comunicació i un article de divulgació). Omple la fitxa per a cada font i cita-la amb el format: Autor o institució (any). <i>Títol</i>. Adreça web." +
           table(["Font (títol i enllaç)", "Qui l'ha escrita? És experta?", "Data", "Per a què s'ha escrit? (informar, vendre, opinar)", "Coincideix amb altres fonts?"], [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]))
    b += "<h2><span class='k'>B</span> El meu punt de vista</h2>"
    b += q(2, "Escriu la teva opinió en una frase. Després dona'n <b>tres arguments</b> basats en dades de les fonts i un <b>contraargument</b> que algú et podria fer, amb la teva resposta." + lines(6))
    b += '<div class="pb"></div>'
    b += q(3, "<b>Escolta altres veus.</b> Pregunta l'opinió a dues persones diferents (de la família, del barri o de la classe). Què en pensen? Algun argument t'ha fet canviar o matisar la teva opinió? Com tindràs en compte persones o col·lectius que solen quedar fora d'aquests debats?" + lines(4))
    b += "<h2><span class='k'>C</span> El producte digital</h2>"
    b += q(4, "Grava el pòdcast o la presentació narrada (3–4 minuts). Ha d'incloure la pregunta, la teva opinió, els arguments amb dades, el contraargument, un llenguatge adequat per a 2n d'ESO i les fonts citades al final. Si fas servir imatges o música, que siguin pròpies o de llicència lliure (amb l'autoria).")
    b += "<h2><span class='k'>D</span> La defensa</h2>"
    b += q(5, "<b>Defensa oral (3 minuts).</b> Respondràs dues preguntes i una objecció del professor amb arguments basats en dades.")
    b += calendari(4)
    b += '<div class="pb"></div>'
    b += G.rub("Rúbrica de la tasca de recuperació de la CE4", [
        ("Informació fiable (4.3)", "Tres fonts o més de tipus diferent, avaluades amb criteris i contrastades", "Tres fonts avaluades amb alguna mancança", "Menys de tres fonts o avaluació superficial", "Fonts no fiables"),
        ("Cita de les fonts (4.3)", "Cita totes les fonts correctament i hi relaciona cada dada", "Cita les fonts amb algun element que falta", "Cita incompleta", "No cita les fonts"),
        ("Producte digital (4.1)", "Producte clar, creatiu i adaptat a 2n d'ESO; so i imatge cuidats; llicències respectades", "Producte clar i adaptat; algun problema tècnic menor", "Producte poc estructurat o massa tècnic", "No es pot seguir o no s'ha lliurat"),
        ("Punt de vista justificat (4.2)", "Opinió clara amb tres arguments basats en dades i resposta al contraargument", "Opinió amb arguments basats en dades", "Opinió poc argumentada", "No justifica l'opinió"),
        ("Respecte i inclusió (4.2)", "Incorpora altres veus i té en compte col·lectius diversos sense estereotips", "Incorpora altres veus", "Esmenta altres opinions sense tenir-les en compte", "No té en compte altres opinions"),
    ])
    b += teacher_note([
        f"<b>Per a qui és:</b> l'alumnat amb NA a la CE4 a la SdA 2 (criteri 4.1); es lliura a l'inici de la SdA 6 perquè es pugui defensar abans de l'avaluació final. També qui vulgui millorar. El nivell nou substitueix el de la CE4 a la SdA 2 i a la SdA 6 si és més alt.",
        "<b>Orientacions:</b> és la mateixa estructura de la tasca de comunicació del curs. A la tutoria de mitja tasca reviseu la fitxa de fonts i els arguments abans de gravar.",
        "<b>Atenció a la diversitat:</b> l'alumnat amb mesures addicionals pot fer la defensa per escrit o gravada; l'alumnat nouvingut pot fer el producte en parella i amb el glossari del curs.",
    ], title="Com funciona la recuperació · nota per al professorat, no s'imprimeix per a l'alumne")
    return done(b)


# ------------------------------------------------------------------ CE5
def recup_ce5():
    b = head(5, "Un hàbit més sostenible i saludable a casa",
             "Fes un microprojecte de dues setmanes a casa: analitza un hàbit, justifica amb la física i la química per què afecta el medi ambient o la salut, proposa un canvi, posa'l en pràctica amb la família i mesura'n el resultat.")
    b += "<h2><span class='k'>0</span> Tria l'hàbit</h2>"
    b += table(["Hàbit", "Què mesures", "Connexió"], [
        ["<b>A · Aparells en espera</b>", "Quants aparells queden endollats en espera i quantes hores", "SdA 6"],
        ["<b>B · Aigua embotellada o de l'aixeta</b>", "Quantes ampolles de plàstic es fan servir en una setmana", "SdA 1 i SdA 4"],
        ["<b>C · Mòbils, piles i residus electrònics</b>", "Quants aparells i piles vells hi ha a casa i on acaben", "SdA 3"]], widths=["36%", "44%", "20%"])
    b += "<h2><span class='k'>A</span> Diagnosi</h2>"
    b += q(1, "Recull les dades de casa durant una setmana en una taula (què, quant, quan). Quin és el punt de partida?" + table(["Dia", "Dada 1", "Dada 2", "Observacions"], [["", "", "", ""] for _ in range(7)]))
    b += "<h2><span class='k'>B</span> Per què importa</h2>"
    b += q(2, "Justifica amb la física i la química com afecta aquest hàbit l'aire, l'aigua o el sòl (per exemple: emissions en generar electricitat, plàstic que es degrada en microplàstics, metalls pesants i electròlits de les bateries)." + lines(5))
    b += q(3, "<b>Fes el càlcul.</b> <i>A:</i> si a casa hi ha 10 aparells en espera de 2 W durant 20 h al dia, quanta energia es perd en un any, en kWh, i quant costa a 0,15 €/kWh? <i>B:</i> si una família de quatre persones beu 2 L d'aigua per persona i dia en ampolles d'1,5 L de 30 g de plàstic, quanta massa de plàstic fa servir en un any? <i>C:</i> un mòbil té 0,034 g d'or; quina massa d'or hi ha en 25 mòbils vells guardats en calaixos d'una classe?" + lines(5))
    b += '<div class="pb"></div>'
    b += "<h2><span class='k'>C</span> La ciència hi pot ajudar</h2>"
    b += q(4, "Explica una manera en què els coneixements de física i química ajuden a millorar aquest problema i la salut de les persones (per exemple, el reciclatge recupera elements, els LED tenen més rendiment, l'aigua de l'aixeta es depura i es controla)." + lines(4))
    b += "<h2><span class='k'>D</span> El pla d'acció</h2>"
    b += q(5, "Planifica el canvi amb la família: objectiu mesurable, accions concretes, qui fa cada cosa i com ho mesurareu. Posa'l en pràctica una setmana i torna a recollir les dades." +
           table(["Objectiu mesurable", "Accions", "Qui hi participa", "Dada abans", "Dada després"], [["", "", "", "", ""]]) + lines(3))
    b += "<h2><span class='k'>E</span> Resultats i reflexió</h2>"
    b += q(6, "Compara les dades d'abans i de després. Heu assolit l'objectiu? Què ha costat més? Quin consell donaries a la resta de la classe? Presenta-ho en un full o en una diapositiva amb una gràfica de barres." + lines(4))
    b += calendari(5, [[f"En acabar {LAST[5]} (o quan t'ho indiqui el professor)", "Rebo la tasca, trio l'hàbit i reviso la rúbrica."], ["Setmana 1", "Diagnosi (part A) i parts B i C. Tutoria de 10 minuts."], ["Setmana 2", "Pla d'acció i dades de després (parts D i E)."], ["Abans de la sessió d'avaluació", "Lliurament i defensa oral de 3 minuts."]])
    b += '<div class="pb"></div>'
    b += G.rub("Rúbrica de la tasca de recuperació de la CE5", [
        ("Preservació de l'aire, l'aigua i el sòl (5.1)", "Justifica amb fonaments científics i dades com afecta l'hàbit l'aire, l'aigua o el sòl", "Justifica l'impacte amb algun argument científic", "Esmenta l'impacte sense justificar-lo", "No relaciona l'hàbit amb el medi"),
        ("Hàbits sostenibles (5.2)", "Analitza de manera crítica l'hàbit amb dades pròpies i el càlcul correcte", "Analitza l'hàbit amb dades i algun error menor", "Anàlisi poc concreta", "No analitza l'hàbit"),
        ("La física i la química ajuden (5.3)", "Explica amb precisió com la ciència contribueix a la sostenibilitat i a la salut", "Explica una contribució amb alguna imprecisió", "Contribució esmentada sense explicar", "No ho relaciona"),
        ("Projecte guiat (5.4)", "Objectiu mesurable, pla complet, dades d'abans i després i reflexió crítica compartida amb la família", "Pla complet i dades d'abans i després", "Pla incomplet o sense dades de després", "No hi ha pla"),
    ])
    b += teacher_note([
        f"<b>Per a qui és:</b> l'alumnat amb NA a la CE5 en acabar {LAST[5]} (criteris 5.1 a 5.4) o qui vulgui millorar. El nivell nou substitueix el de la CE5 a la SdA 3 i a la SdA 5 si és més alt.",
        "<b>Solucions del càlcul.</b> A: 10 · 2 W · 20 h · 365 = 146 000 Wh = <b>146 kWh</b>; 146 · 0,15 ≈ <b>21,9 €</b> l'any. B: 4 · 2 = 8 L/dia; 8 / 1,5 ≈ 5,3 ampolles/dia; · 365 ≈ 1950 ampolles; · 30 g ≈ <b>58 kg</b> de plàstic l'any. C: 25 · 0,034 = <b>0,85 g</b> d'or.",
        "<b>Atenció a la diversitat:</b> si a casa no és possible fer el projecte, es pot fer a l'aula o a l'institut (per exemple, els aparells en espera d'una aula).",
    ], title="Com funciona la recuperació · nota per al professorat, no s'imprimeix per a l'alumne")
    return done(b)


# ------------------------------------------------------------------ CE6
def recup_ce6():
    b = head(6, "La història d'una idea i el seu futur",
             "Fes una línia del temps (en paper o digital) que expliqui com ha canviat una idea o una tecnologia gràcies al treball de moltes persones, i acaba-la amb una proposta perquè aquesta ciència ajudi a resoldre una necessitat del teu entorn.")
    b += "<h2><span class='k'>0</span> Tria la idea</h2>"
    b += table(["Tema", "Per on començar"], [
        ["<b>A · El model atòmic</b>", "De Dalton a Bohr i al model actual (SdA 3)."],
        ["<b>B · La il·luminació</b>", "Del foc a la bombeta d'incandescència, el fluorescent i el LED (SdA 6)."],
        ["<b>C · Les bateries</b>", "De la pila de Volta a les bateries de ió liti i les d'estat sòlid (SdA 3)."],
        ["<b>D · El cotxe</b>", "Del vapor a la combustió, l'elèctric i l'hidrogen (SdA 4)."]], widths=["30%", "70%"])
    b += "<h2><span class='k'>A</span> La línia del temps</h2>"
    b += q(1, "Escriu com a mínim <b>cinc fites</b> en ordre: any, qui hi va treballar (homes i dones), què van descobrir o inventar i <b>per què</b> es va canviar la idea anterior (quina prova o quina necessitat ho va provocar). Cita les fonts." +
           table(["Any", "Persones", "Què va canviar", "Per què (prova o necessitat)"], [["", "", "", ""] for _ in range(5)], widths=["12%", "26%", "31%", "31%"]))
    b += "<h2><span class='k'>B</span> Ciència, tecnologia, societat i medi ambient</h2>"
    b += q(2, "Explica una repercussió d'aquesta idea en la tecnologia, una en la societat i una en el medi ambient. Explica també un cas en què la societat o la tecnologia van influir en la ciència (per exemple, un instrument nou o una necessitat econòmica)." + lines(6))
    b += '<div class="pb"></div>'
    b += "<h2><span class='k'>C</span> Una proposta per al nostre entorn</h2>"
    b += q(3, "Detecta una necessitat de l'institut o del barri relacionada amb el teu tema (energia, residus, transport, salut). Proposa una solució sostenible basada en aquesta ciència: què cal fer, qui hi participa (alumnat, famílies, Ajuntament…) i un avantatge i un límit de la proposta." + lines(6))
    b += q(4, "<b>Sense biaixos.</b> Revisa la proposta: es reparteixen les tasques sense estereotips de gènere? Hi ha cap col·lectiu que no hi hagis tingut en compte? Com ho milloraries?" + lines(3))
    b += "<h2><span class='k'>D</span> El producte i la defensa</h2>"
    b += q(5, "Presenta la línia del temps i la proposta en un cartell A3 o en una presentació digital, i defensa-la oralment en 3 minuts.")
    b += calendari(6)
    b += '<div class="pb"></div>'
    b += G.rub("Rúbrica de la tasca de recuperació de la CE6", [
        ("La ciència en construcció (6.1)", "Cinc fites ben ordenades amb les persones que hi van participar i el motiu de cada canvi, amb fonts", "Fites correctes amb algun motiu poc explicat", "Fites incompletes o sense explicar per què canvien", "No fa la línia del temps"),
        ("Repercussions mútues (6.1)", "Explica repercussions en tecnologia, societat i medi ambient i una influència de la societat en la ciència", "Explica les repercussions amb alguna imprecisió", "Repercussions esmentades sense explicar", "No en parla"),
        ("Solució sostenible (6.2)", "Proposa una solució viable basada en la ciència, amb participació ciutadana, un avantatge i un límit", "Proposta viable amb algun element que falta", "Proposta genèrica", "No hi ha proposta"),
        ("Sense biaixos de gènere (6.2)", "Revisa la proposta i el repartiment de tasques sense estereotips i inclou col·lectius diversos", "Revisa el repartiment de tasques", "Revisió superficial", "No ho revisa"),
    ])
    b += teacher_note([
        f"<b>Per a qui és:</b> l'alumnat amb NA a la CE6 a la SdA 3 (criteri 6.1); es lliura a l'inici de la SdA 6 perquè es pugui defensar abans de l'avaluació final. També qui vulgui millorar. El nivell nou substitueix el de la CE6 a la SdA 3 i a la SdA 6 si és més alt.",
        "<b>Fites orientatives.</b> A: Dalton 1808, Thomson 1897, Rutherford 1911 (amb Geiger i Marsden), Bohr 1913, Chadwick 1932; Marie Curie i Marguerite Perey (radioactivitat, franci). B: Edison i Swan (1879), fluorescents (anys 1930), LED blau de Nakamura, Akasaki i Amano (1990s, premi Nobel 2014). C: Volta (1800), Planté (1859), Goodenough, Whittingham i Yoshino (bateria de ió liti, Nobel 2019). D: motor de combustió (Benz, 1886), Bertha Benz (primer viatge llarg, 1888), cotxe elèctric modern, pila de combustible.",
        "<b>Atenció a la diversitat:</b> es pot donar una plantilla de línia del temps amb les dates ja posades.",
    ], title="Com funciona la recuperació · nota per al professorat, no s'imprimeix per a l'alumne")
    return done(b)


# compatibilitat amb el nom antic
recup = recup_ce4
