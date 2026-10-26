"""Contingut dels dossiers de teoria de 3r d'ESO (versió ampliada). El fa servir gen_teoria.py."""
from gen_teoria import H, S, P, UL, OL, TIP, EX, F, T, TOC, KW, taula_familia, electrolisi_teoria
import gen_sda1 as G, figs, gen_hidrogen as Hd, gen_energia as En
import teoria_figs as TF, teoria_figs2 as T2

PB = '<div class="pb"></div>'
def DEF(t, h): return f'<div class="fbox" style="background:#fff"><b>{t}.</b> {h}</div>'

# ======================================================================== SdA 1
def sda1():
    b = H(1, "Com podem identificar una substància? La mesura, la densitat, les mescles i els canvis químics.")
    b += TOC("Magnituds i unitats del SI", "Canvis d'unitats: factors de conversió", "Notació científica i xifres significatives", "La mesura: instruments, errors i incertesa",
             "La densitat", "Substàncies pures i mescles", "Dissolucions i concentració", "Tècniques de separació", "Conductivitat elèctrica i ions", "Canvis físics i canvis químics", "Seguretat al laboratori", "Com treballa la ciència")
    b += S(1, "Magnituds i unitats del SI")
    b += P("Una <b>magnitud</b> és qualsevol propietat d'un cos, d'una substància o d'un fenomen que es pot <b>mesurar</b>, és a dir, expressar amb un nombre i una unitat (la massa, la longitud, la temperatura…). <b>Mesurar</b> és comparar una magnitud amb una quantitat de la mateixa magnitud que prenem com a referència, la <b>unitat</b>. La bellesa o la por no són magnituds: no es poden comparar amb una unitat.",
           "Des del 1960 la comunitat científica fa servir el <b>Sistema Internacional d'unitats (SI)</b>. Té set magnituds <b>fonamentals</b>, que es defineixen per si mateixes; totes les altres són <b>derivades</b>, perquè s'obtenen combinant les fonamentals amb una fórmula.")
    b += T(["Magnitud fonamental", "Unitat (símbol)", "Magnitud derivada", "Com s'obté", "Unitat del SI"],
           [["Longitud", "metre (m)", "Superfície", "llargada · amplada", "m²"], ["Massa", "quilogram (kg)", "Volum", "llargada · amplada · altura", "m³"],
            ["Temps", "segon (s)", "Velocitat", "distància / temps", "m/s"], ["Temperatura", "kelvin (K)", "Densitat", "massa / volum", "kg/m³"],
            ["Intensitat de corrent", "ampere (A)", "Força", "massa · acceleració", "newton (N)"], ["Quantitat de substància", "mol (mol)", "Energia", "força · distància", "joule (J)"],
            ["Intensitat lluminosa", "candela (cd)", "Concentració", "massa de solut / volum", "kg/m³ (g/L)"]], w=["20%", "17%", "17%", "28%", "18%"])
    b += P("Els <b>prefixos</b> indiquen múltiples i submúltiples de la unitat. Tots són potències de 10:")
    b += T(["Prefix", "Símbol", "Valor", "Prefix", "Símbol", "Valor"],
           [["giga", "G", "10⁹", "deci", "d", "10⁻¹"], ["mega", "M", "10⁶", "centi", "c", "10⁻²"], ["kilo", "k", "10³", "mil·li", "m", "10⁻³"],
            ["hecto", "h", "10²", "micro", "µ", "10⁻⁶"], ["deca", "da", "10¹", "nano", "n", "10⁻⁹"]])
    b += TIP("Unitats de superfície i de volum", "Com que la superfície té dues dimensions, 1 m² = (100 cm)² = 10 000 cm². El volum en té tres: 1 m³ = (100 cm)³ = 1 000 000 cm³. Equivalències útils: <b>1 L = 1 dm³</b>, <b>1 mL = 1 cm³</b> i 1 m³ = 1 000 L.")
    b += S(2, "Canvis d'unitats: factors de conversió")
    b += P("Un <b>factor de conversió</b> és una fracció que val 1, perquè a dalt i a baix hi ha la mateixa quantitat escrita amb unitats diferents (per exemple, 1 km i 1 000 m). En multiplicar una quantitat per un factor de conversió no la canviem, només en canviem la unitat. La unitat que volem treure ha de quedar una vegada al numerador i una al denominador, perquè es simplifiqui.")
    b += OL("Escriu la quantitat amb la seva unitat.", "Busca l'equivalència entre la unitat que tens i la que vols.", "Escriu el factor amb la unitat que vols a <b>dalt</b> i la que vols treure a <b>baix</b>.", "Simplifica les unitats i calcula.", "Si hi ha unitats compostes (km/h, g/mL), encadena un factor per a cada unitat.")
    b += EX("Exemple", "Passa 72 km/h a m/s: \\( 72\\ \\dfrac{\\mathrm{km}}{\\mathrm{h}} \\cdot \\dfrac{1000\\ \\mathrm{m}}{1\\ \\mathrm{km}} \\cdot \\dfrac{1\\ \\mathrm{h}}{3600\\ \\mathrm{s}} = 20\\ \\dfrac{\\mathrm{m}}{\\mathrm{s}} \\).")
    b += EX("Exemple", "Passa 1,2 g/mL a kg/m³: \\( 1{,}2\\ \\dfrac{\\mathrm{g}}{\\mathrm{mL}} \\cdot \\dfrac{1\\ \\mathrm{kg}}{1000\\ \\mathrm{g}} \\cdot \\dfrac{10^{6}\\ \\mathrm{mL}}{1\\ \\mathrm{m^3}} = 1200\\ \\dfrac{\\mathrm{kg}}{\\mathrm{m^3}} \\).")
    b += S(3, "Notació científica i xifres significatives")
    b += P("Per escriure nombres molt grans o molt petits fem servir la <b>notació científica</b>: \\( a \\cdot 10^{n} \\), amb \\( 1 \\le a < 10 \\) i <i>n</i> un nombre enter. Si el nombre és més gran que 1, l'exponent és positiu (hem mogut la coma cap a l'esquerra); si és més petit que 1, és negatiu (l'hem moguda cap a la dreta).")
    b += EX("Exemples", "300 000 000 m/s = 3 · 10⁸ m/s (velocitat de la llum) · 0,000 07 m = 7 · 10⁻⁵ m (gruix d'un cabell) · 6 371 000 m = 6,371 · 10⁶ m (radi de la Terra).")
    b += P("Per <b>multiplicar</b>, multipliquem els nombres i <b>sumem</b> els exponents; per <b>dividir</b>, dividim els nombres i <b>restem</b> els exponents. Si el resultat no té la forma correcta, l'ajustem: (5 · 10³) · (4 · 10²) = 20 · 10⁵ = 2 · 10⁶.",
           "Les <b>xifres significatives</b> són les que coneixem amb seguretat més la primera de dubtosa. Una massa de 12,40 g té quatre xifres significatives: el zero final indica que la balança aprecia centèsimes. En un càlcul, el resultat no pot tenir més xifres significatives que la dada que en té menys: si dividim 100 g entre 125 mL, escrivim 0,800 g/mL, no 0,8000000 g/mL. Els zeros de l'esquerra no són significatius (0,0052 en té dues).")
    b += S(4, "La mesura: instruments, errors i incertesa")
    b += P("Cada instrument té una <b>sensibilitat</b> (o resolució): la variació més petita que pot detectar. En una proveta graduada de mil·lilitre en mil·lilitre és 1 mL; en una balança de centèsimes, 0,01 g. També té un <b>abast</b>, el valor màxim que pot mesurar. Per mesurar el volum d'un líquid ens hem de fixar en la part de baix del <b>menisc</b>, amb els ulls a la mateixa altura per evitar l'error de paral·laxi.",
           "Cap mesura no és exacta. Hi ha dos tipus d'errors:")
    b += UL("<b>Errors sistemàtics:</b> sempre en el mateix sentit, per un instrument mal calibrat o un mètode incorrecte (una balança que no marca zero, llegir sempre el menisc des de dalt). No es corregeixen repetint la mesura, sinó revisant el mètode.",
            "<b>Errors aleatoris:</b> a l'atzar, de vegades per sobre i de vegades per sota (petites variacions en la lectura, en el temps de reacció). Es redueixen <b>repetint la mesura</b> diverses vegades i fent la <b>mitjana</b>.")
    b += figs.fig(TF.proveta_menisc(), "Com es llegeix una proveta: els ulls a l'altura de la part de baix del menisc.", "125mm")
    b += P("Una mesura és <b>exacta</b> si s'acosta al valor real, i és <b>precisa</b> si en repetir-la surten valors molt semblants. Per saber com d'exacta és, la comparem amb un <b>valor de referència</b> (el d'una taula de dades fiable):")
    b += figs.fig(TF.dianes(), "Exactitud i precisió: quatre sèries de mesures comparades amb el valor real (el centre).", "160mm")
    b += F("E<sub>a</sub> = | valor mesurat − valor de referència |", "E<sub>r</sub> (%) = E<sub>a</sub> / valor de referència · 100",
           note="L'error absolut té les unitats de la mesura. L'error relatiu, en percentatge, permet comparar la qualitat de mesures diferents.")
    b += EX("Exemple", "Mesurem 0,82 g/mL per a l'etanol i la referència és 0,79 g/mL: E<sub>a</sub> = 0,03 g/mL; E<sub>r</sub> = 0,03 / 0,79 · 100 ≈ 3,8 %. Un error relatiu gran no vol dir sempre que ens hem equivocat de substància: l'etanol de farmàcia (96 %) porta aigua i té una densitat més alta que el pur.")
    b += S(5, "La densitat")
    b += P("Les propietats de la matèria poden ser <b>generals</b> (les té qualsevol material i no serveixen per identificar-lo: massa, volum, temperatura) o <b>característiques</b> (tenen un valor propi per a cada substància pura: densitat, temperatura de fusió i d'ebullició, solubilitat, conductivitat…). Les propietats característiques ens permeten identificar substàncies.",
           "La <b>densitat</b> és la massa de cada unitat de volum d'una substància. No depèn de la quantitat: un clau de ferro i una biga de ferro tenen la mateixa densitat. Sí que depèn de la <b>temperatura</b>, perquè en escalfar un material el volum augmenta una mica i la densitat disminueix.")
    b += F("ρ = m / V", note="ρ en g/cm³ (= g/mL) o en kg/m³ · 1 g/cm³ = 1 000 kg/m³")
    b += P("Per mesurar-la: la massa amb una balança i el volum amb una proveta. Si el sòlid és irregular, el submergim en una proveta amb aigua: el seu volum és el que puja l'aigua (<b>mètode del desplaçament</b>). Si és un líquid en un pot, la massa del líquid és la massa del pot ple menys la del pot buit (la <b>tara</b>).")
    b += figs.fig(TF.desplacament(), "Mètode del desplaçament: el volum de la pedra és el que puja l'aigua.", "125mm")
    b += T(["Substància (20 °C)", "ρ (g/cm³)", "Substància (20 °C)", "ρ (g/cm³)"],
           [["Aire", "0,0012", "Aigua de mar", "1,03"], ["Etanol", "0,79", "Glicerina", "1,26"], ["Oli d'oliva", "0,92", "Alumini", "2,70"], ["Gel", "0,92", "Ferro", "7,87"], ["Aigua", "1,00", "Or", "19,3"]])
    b += EX("Exemple", "Un pot ple té una massa de 160 g i buit, 60 g. El líquid té 100 g i ocupa 125 mL: ρ = 100 / 125 = 0,800 g/mL. Pot ser etanol, però cal confirmar-ho amb una altra prova.")
    b += figs.fig(TF.columna_densitat(), "Columna de densitats: els líquids menys densos suren damunt dels més densos.", "135mm")
    b += P("Un cos <b>sura</b> en un líquid si la seva densitat és més petita que la del líquid, i s'enfonsa si és més gran. Dos líquids que no es barregen es col·loquen en capes, amb el més dens a sota. Com que dues substàncies poden tenir densitats molt semblants, cap prova sola no és suficient: cal combinar <b>proves convergents</b> (densitat, conductivitat, miscibilitat, reaccions…).")
    b += S(6, "Substàncies pures i mescles")
    b += P("Una <b>substància pura</b> té una composició fixa i unes propietats característiques constants: es fon i bull a una temperatura fixa. Pot ser:")
    b += UL("un <b>element</b>, format per un sol tipus d'àtom, que no es pot descompondre en substàncies més simples (ferro, oxigen, carboni);",
            "un <b>compost</b>, format per dos elements o més units en una proporció fixa, que sí que es pot descompondre per mètodes químics (aigua, H₂O; clorur de sodi, NaCl). Les propietats d'un compost són diferents de les dels elements que el formen: el sodi és un metall que reacciona violentament amb l'aigua i el clor és un gas tòxic, però el clorur de sodi és la sal de cuina.")
    b += P("Una <b>mescla</b> està formada per dues substàncies o més que conserven les seves propietats i es poden separar per mètodes físics. La seva composició és variable i no té una temperatura d'ebullició fixa (l'aigua salada bull a una temperatura que va pujant).")
    b += UL("<b>Mescla homogènia o dissolució:</b> no se'n distingeixen els components, ni amb microscopi. Té la mateixa composició a tot arreu (aigua amb sal, aire, bronze).",
            "<b>Mescla heterogènia:</b> se'n distingeixen els components a simple vista o amb una lupa (aigua i sorra, granit, oli i aigua).",
            "<b>Col·loide:</b> sembla homogeni, però al microscopi se'n veuen les parts (llet, maionesa, boira). Dispersa la llum d'un feix làser.")
    b += figs.fig(TF.particules_materia(), "Com es veuen amb el model de partícules les substàncies pures i les mescles.", "160mm")
    b += S(7, "Dissolucions i concentració")
    b += P("En una dissolució, el component que hi ha en més quantitat és el <b>dissolvent</b> (sovint l'aigua) i el que hi ha en menys quantitat, el <b>solut</b>. La <b>concentració</b> indica quant solut hi ha en una quantitat de dissolució:")
    b += F("c (g/L) = massa de solut (g) / volum de dissolució (L)", "% en massa = massa de solut / massa de dissolució · 100")
    b += P("La <b>solubilitat</b> és la quantitat màxima de solut que es pot dissoldre en una quantitat de dissolvent a una temperatura donada (per exemple, 36 g de sal en 100 g d'aigua a 20 °C). Quan s'hi ha dissolt el màxim, la dissolució està <b>saturada</b>. La solubilitat de la majoria de sòlids augmenta amb la temperatura; la dels gasos disminueix.")
    b += S(8, "Tècniques de separació")
    b += P("Cada tècnica aprofita una propietat diferent dels components de la mescla. Per separar una mescla de diversos components, cal pensar l'<b>ordre</b> dels passos.")
    b += T(["Tècnica", "Propietat en què es basa", "Exemple"],
           [["Separació magnètica", "Magnetisme: el ferro és atret per l'imant", "Llimadures de ferro i sorra"], ["Decantació", "Densitat de dos líquids que no es barregen (o d'un sòlid que es diposita)", "Oli i aigua (embut de decantació)"],
            ["Filtració", "Mida de les partícules: el sòlid no travessa els porus del paper", "Sorra i aigua salada"], ["Flotació", "Densitat menor que la de l'aigua", "Serradures i sorra"],
            ["Evaporació i cristal·lització", "L'aigua s'evapora i el solut no; en anar-se evaporant, el solut forma cristalls", "Sal de l'aigua de mar (salines)"],
            ["Destil·lació", "Temperatures d'ebullició diferents: el vapor es condensa i es recull", "Aigua i alcohol; aigua pura de l'aigua de mar"],
            ["Cromatografia", "Afinitat diferent de cada component per la fase mòbil i pel paper", "Pigments d'una tinta"]], w=["24%", "46%", "30%"])
    b += EX("Exemple", "Mescla de sorra, llimadures de ferro, serradures i aigua salada: 1) imant (ferro); 2) les serradures suren i es recullen; 3) filtració (la sorra queda al paper); 4) evaporació de l'aigua (queda la sal).")
    b += figs.fig(TF.separacio(), "Quatre tècniques de separació i la propietat en què es basa cadascuna.", "170mm")
    b += figs.cromatografia()
    b += S(9, "Conductivitat elèctrica i ions")
    b += P("Per conduir el corrent elèctric calen partícules amb càrrega que es puguin moure. Els metalls condueixen perquè tenen electrons lliures. L'aigua pura gairebé no condueix. Quan una substància com el clorur de sodi es dissol, es <b>dissocia</b> en <b>ions</b> (partícules amb càrrega): NaCl → Na⁺ + Cl⁻. Els ions es mouen per la dissolució i transporten la càrrega: la dissolució és conductora i en diem un <b>electròlit</b>. El sucre es dissol, però no forma ions, i per això l'aigua amb sucre no condueix.")
    b += figs.fig(TF.dissociacio(), "En dissoldre's, el clorur de sodi es dissocia en ions que es poden moure.", "140mm")
    b += figs.circuit_conductivitat()
    b += S(10, "Canvis físics i canvis químics")
    b += UL("<b>Canvi físic:</b> la substància continua sent la mateixa; només canvia l'estat, la forma o la mida (fondre gel, dissoldre sucre, trencar un vidre). Normalment és reversible.",
            "<b>Canvi químic</b> o <b>reacció química:</b> unes substàncies (els <b>reactius</b>) es transformen en unes altres de noves (els <b>productes</b>), amb propietats diferents. Evidències: canvi de color, formació d'un gas (bombolles), formació d'un sòlid (precipitat), alliberament o absorció d'energia (calor, llum), canvi d'olor.")
    b += EX("Exemple", "Un clau de ferro en una dissolució blava de sulfat de coure: el clau es recobreix d'una capa vermellosa de coure i el color blau es va perdent. Fe + CuSO₄ → FeSO₄ + Cu. S'han format substàncies noves: és un canvi químic.")
    b += figs.fig(TF.clau_coure(), "Un canvi químic: el ferro reacciona amb el sulfat de coure i es forma coure.", "135mm")
    b += S(11, "Seguretat al laboratori")
    b += P("Les etiquetes dels productes perillosos porten <b>pictogrames</b> (rombes amb la vora vermella, segons el reglament CLP de la Unió Europea), una <b>paraula d'avís</b> (<b>Perill</b> per als perills greus i <b>Atenció</b> per als menys greus) i frases d'indicacions de perill i de consells de prudència.")
    b += figs.picto_table(cols=3, size="11mm")
    b += UL("Porta bata i ulleres de seguretat, i guants quan ho indiqui el professor. Cabells recollits.", "No mengis ni beguis. No toquis, no olorris directament ni tastis cap producte.",
            "Llegeix l'etiqueta abans de fer servir un producte i torna'l a tapar.", "Escalfa els tubs d'assaig inclinats i sense apuntar ningú.", "Llença els residus als recipients indicats i avisa el professor de qualsevol accident.")
    b += S(12, "Com treballa la ciència")
    b += P("Per resoldre un problema, la ciència fa servir un mètode: ens fem una <b>pregunta</b>, proposem una <b>hipòtesi</b> (una resposta provisional que es pugui comprovar), dissenyem un <b>experiment</b> en què canviem una sola variable (la <b>independent</b>), mesurem el que en resulta (la <b>dependent</b>) i mantenim iguals les altres (les <b>controlades</b>). Amb les dades, traiem <b>conclusions</b> i les comuniquem citant les fonts.")
    b += TIP("La ciència la fan persones", "Ellen Swallow Richards (1842–1911), primera dona que va estudiar al MIT, va analitzar milers de mostres d'aigua de Massachusetts i va fer el primer «mapa del clorur normal»: va comparar cada mostra amb un valor de referència, com fem nosaltres amb els pots. La seva feina va portar a les primeres normes de qualitat de l'aigua dels Estats Units.")
    b += KW(("Magnitud", "propietat que es pot mesurar"), ("Sensibilitat", "variació més petita que detecta un instrument"), ("Error sistemàtic i aleatori", "sempre en el mateix sentit i a l'atzar"),
            ("Exactitud i precisió", "proximitat al valor real i coincidència entre mesures repetides"), ("Densitat", "massa per unitat de volum"), ("Propietat característica", "permet identificar una substància"),
            ("Element i compost", "un sol tipus d'àtom; diversos elements en proporció fixa"), ("Dissolució", "mescla homogènia de solut i dissolvent"), ("Solubilitat", "màxim de solut que es dissol"), ("Electròlit", "substància que en dissoldre's forma ions i condueix"))
    return b

# ======================================================================== SdA 2
def sda2():
    b = H(2, "Per què explota un desodorant dins d'un cotxe a l'agost? El model cineticomolecular, els estats de la matèria i les lleis dels gasos.")
    b += TOC("Què és un model científic", "El model cineticomolecular", "Temperatura i energia de les partícules", "Els estats d'agregació", "La pressió", "Les lleis dels gasos", "La llei combinada i el zero absolut", "Els canvis d'estat", "Les corbes d'escalfament i de refredament", "El repte i la seguretat")
    b += S(1, "Què és un model científic")
    b += P("Un <b>model</b> és una representació simplificada de la realitat que ens permet explicar fenòmens i fer prediccions. Un bon model explica el que observem i encerta les prediccions; si un experiment el contradiu, el model s'ha de modificar o canviar. No podem veure les partícules de la matèria, però el model de partícules explica perquè els gasos es comprimeixen, els olors s'escampen o els globus s'inflen en escalfar-los.")
    b += S(2, "El model cineticomolecular")
    b += OL("La matèria està formada per <b>partícules</b> molt petites (àtoms o molècules), totes iguals en una substància pura.",
            "Entre les partícules <b>no hi ha res</b>: hi ha buit. (No hi ha aire entre les partícules d'un gas: l'aire també està fet de partícules.)",
            "Les partícules estan en <b>moviment constant</b>: vibren, giren o es desplacen.",
            "Entre les partícules hi ha <b>forces d'atracció</b>, més intenses com més a prop són.",
            "Les partícules <b>xoquen</b> entre elles i amb les parets del recipient sense perdre energia en conjunt.",
            "Com més alta és la temperatura, més <b>energia cinètica</b> tenen les partícules i més de pressa es mouen.")
    b += EX("Ho explica", "<b>Difusió:</b> sentim el perfum a l'altra punta de l'aula perquè les seves partícules es mouen i s'escampen entre les de l'aire; amb aigua calenta, el colorant s'escampa més de pressa. <b>Compressió:</b> l'aire d'una xeringa tapada es pot comprimir perquè entre les partícules hi ha molt d'espai buit; l'aigua, gairebé gens. <b>Dilatació:</b> en escalfar un cos, les partícules es mouen més i se separen una mica: el cos ocupa més volum, però les partícules <b>no</b> es fan més grans.")
    b += S(3, "Temperatura i energia de les partícules")
    b += P("La <b>temperatura</b> és una mesura de l'<b>energia cinètica mitjana</b> de les partícules: com més alta, més de pressa es mouen de mitjana. No totes les partícules es mouen igual de ràpid: la temperatura n'és la mitjana. Si refredem una substància, les partícules es mouen cada vegada menys. El <b>zero absolut</b> (0 K = −273,15 °C, que arrodonim a −273 °C) és la temperatura més baixa possible: les partícules tindrien el mínim moviment possible. Per això, a les lleis dels gasos la temperatura s'expressa sempre en <b>kelvin</b>, una escala que comença al zero absolut i no té valors negatius.")
    b += F("T (K) = T (°C) + 273", note="27 °C = 300 K · 373 K = 100 °C · una variació d'1 °C és igual a una variació d'1 K")
    b += S(4, "Els estats d'agregació")
    b += P("L'estat d'una substància depèn de la competència entre les <b>forces d'atracció</b> (que mantenen les partícules juntes) i el <b>moviment</b> de les partícules (que les separa).")
    b += T(["", "Sòlid", "Líquid", "Gas"],
           [["Forces d'atracció", "Molt intenses", "Intenses", "Gairebé nul·les"], ["Partícules", "Molt juntes i ordenades (xarxa)", "Juntes però desordenades", "Molt separades i desordenades"],
            ["Moviment", "Vibren al seu lloc", "Llisquen les unes sobre les altres", "Es desplacen lliurement i molt de pressa"],
            ["Forma", "Pròpia", "La del recipient", "La del recipient"], ["Volum", "Propi", "Propi", "Ocupa tot el recipient"],
            ["Compressibilitat", "No es comprimeix", "Gairebé no es comprimeix", "Es comprimeix fàcilment"], ["Fluïdesa", "No flueix", "Flueix", "Flueix"]], w=["20%", "26%", "27%", "27%"])
    b += figs.fig(T2.estats_particules(), "Model de partícules dels tres estats d'agregació.", "150mm")
    b += P("La sorra «raja» com un líquid, però és un sòlid: cada gra és un sòlid amb forma i volum propis.")
    b += S(5, "La pressió")
    b += P("La <b>pressió</b> és la força que es fa per unitat de superfície: P = F / S. Es mesura en <b>pascals</b> (1 Pa = 1 N/m²). En un gas, la pressió és l'efecte dels <b>xocs de les partícules</b> contra les parets del recipient: com més xocs per segon i com més forts, més pressió. La pressió del gas augmenta si hi ha més partícules, si el volum és més petit (xoquen més sovint) o si la temperatura és més alta (xoquen més sovint i amb més força).",
           "L'aire que ens envolta també fa pressió: la <b>pressió atmosfèrica</b>, que al nivell del mar val aproximadament 1 atm i disminueix amb l'altura. Es mesura amb el <b>baròmetre</b>; la pressió d'un gas tancat (una roda, una bombona) es mesura amb el <b>manòmetre</b>.")
    b += F("1 atm = 760 mmHg = 101 325 Pa ≈ 1 013 hPa ≈ 1 bar")
    b += figs.fig(T2.boyle_embol(), "Si el volum es redueix a la meitat, les partícules xoquen el doble de vegades amb les parets: la pressió es duplica.", "120mm")
    b += S(6, "Les lleis dels gasos")
    b += P("L'estat d'un gas es descriu amb tres magnituds: <b>pressió</b>, <b>volum</b> i <b>temperatura</b>. Si en mantenim una de constant, les altres dues es relacionen d'una manera senzilla. Les tres lleis es van descobrir experimentalment i el model cineticomolecular les explica.")
    b += T(["Llei", "Constant", "Relació", "Fórmula", "Explicació amb el model", "Gràfica"],
           [["Boyle-Mariotte (1662)", "T", "Inversament proporcionals: si V es fa la meitat, P es fa el doble", "P₁ · V₁ = P₂ · V₂", "Amb menys volum, les partícules xoquen més sovint contra les parets", "P–V: hipèrbola"],
            ["Charles (1787)", "P", "Directament proporcionals: si T (K) es duplica, V es duplica", "V₁ / T₁ = V₂ / T₂", "Les partícules es mouen més de pressa i empenyen les parets fins que el volum augmenta", "V–T: recta que passa per 0 K"],
            ["Gay-Lussac (1802)", "V", "Directament proporcionals: si T (K) es duplica, P es duplica", "P₁ / T₁ = P₂ / T₂", "Les partícules xoquen més sovint i més fort contra les parets", "P–T: recta que passa per 0 K"]], w=["14%", "8%", "22%", "15%", "26%", "15%"])
    b += figs.fig(T2.lleis_gasos(), "Gràfiques de les tres lleis dels gasos.", "160mm")
    b += EX("Exemple (Boyle)", "Una xeringa tapada té 40 mL d'aire a 1 atm i l'empenyem fins a 10 mL: P₂ = 1 · 40 / 10 = 4 atm.")
    b += EX("Exemple (Charles)", "Un globus de 2,0 L a 27 °C (300 K) es posa al congelador a −18 °C (255 K): V₂ = 2,0 · 255 / 300 = 1,7 L.")
    b += EX("Exemple (Gay-Lussac)", "Un desodorant a 3,0 atm i 20 °C (293 K) arriba a 65 °C (338 K) dins d'un cotxe: P₂ = 3,0 · 338 / 293 ≈ 3,5 atm.")
    b += TIP("Com es resol un problema de gasos", "1) Escriu les dades amb unitats (estat 1 i estat 2). 2) Mira quina magnitud es manté constant i tria la llei. 3) Passa les temperatures a kelvin (les pressions i els volums poden anar en qualsevol unitat, però la mateixa als dos estats). 4) Aïlla la incògnita i calcula. 5) Escriu el resultat amb la unitat i comprova si té sentit: si el gas s'escalfa a volum constant, la pressió ha d'augmentar.")
    b += S(7, "La llei combinada i el zero absolut")
    b += P("Les tres lleis es poden reunir en una de sola, vàlida quan canvien les tres magnituds alhora (amb la mateixa quantitat de gas):")
    b += F("P₁ · V₁ / T₁ = P₂ · V₂ / T₂")
    b += P("Si representem el volum d'un gas a pressió constant en funció de la temperatura en °C i allarguem la recta cap avall, talla l'eix a −273 °C, sigui quin sigui el gas. Aquesta temperatura, en què el volum seria zero, és el zero absolut. Així va néixer l'escala Kelvin (William Thomson, lord Kelvin, 1848).")
    b += S(8, "Els canvis d'estat")
    b += P("Quan escalfem o refredem una substància pot canviar d'estat. La substància és la mateixa: només canvien l'ordre, la separació i el moviment de les partícules. És un <b>canvi físic</b> i reversible. Per passar a un estat més desordenat (de sòlid a líquid o de líquid a gas), les partícules han de vèncer les forces d'atracció: cal <b>absorbir energia</b>. En el procés invers, la substància <b>desprèn energia</b>.")
    b += G.canvis_svg()
    b += T(["Núm.", "Canvi", "De … a …", "Energia", "Exemple"],
           [["1", "Fusió", "sòlid → líquid", "absorbeix", "El gel es fon"], ["2", "Solidificació", "líquid → sòlid", "desprèn", "Fem glaçons"], ["3", "Vaporització", "líquid → gas", "absorbeix", "La roba s'asseca"],
            ["4", "Condensació", "gas → líquid", "desprèn", "El mirall s'entela"], ["5", "Sublimació", "sòlid → gas", "absorbeix", "La naftalina, la neu carbònica"], ["6", "Sublimació inversa", "gas → sòlid", "desprèn", "La gebrada"]])
    b += P("La vaporització pot ser de dues maneres:")
    b += UL("<b>Evaporació:</b> passa només a la <b>superfície</b> del líquid i a <b>qualsevol temperatura</b>. Les partícules de la superfície que es mouen més de pressa escapen. És més ràpida com més alta és la temperatura, com més superfície hi ha i si fa vent. Refreda el líquid que queda (per això la suor ens refreda).",
            "<b>Ebullició:</b> passa a <b>tot el líquid</b>, amb bombolles de vapor que es formen a dins, a una temperatura fixa: la <b>temperatura d'ebullició</b>. Aquesta temperatura depèn de la pressió exterior: a dalt de l'Everest l'aigua bull a uns 70 °C; a l'olla a pressió, a uns 120 °C; i en una xeringa on reduïm la pressió, l'aigua pot bullir a 50 °C.")
    b += figs.fig(T2.evaporacio_ebullicio(), "Evaporació i ebullició.", "145mm")
    b += S(9, "Les corbes d'escalfament i de refredament")
    b += P("Si escalfem gel a −20 °C i anotem la temperatura cada minut, obtenim una gràfica temperatura–temps amb <b>trams inclinats</b> (la temperatura puja i la substància és en un sol estat) i <b>trams horitzontals</b> (canvi d'estat: hi conviuen dos estats). Mentre dura el canvi d'estat la temperatura <b>no puja</b>, encara que continuem escalfant: l'energia serveix per vèncer les forces d'atracció i separar les partícules, no per fer-les anar més de pressa. La quantitat d'energia que cal per fondre o vaporitzar un quilogram d'una substància és la seva <b>calor latent</b>.",
           "La corba de <b>refredament</b> és la inversa: els trams horitzontals apareixen a les mateixes temperatures, perquè una substància pura es fon i se solidifica a la mateixa temperatura.",
           "Les temperatures de fusió i d'ebullició són propietats característiques: ens permeten identificar una substància i saber en quin estat és a una temperatura donada. Si la temperatura és més baixa que la de fusió, és sòlida; entre la de fusió i la d'ebullició, líquida; per sobre de la d'ebullició, gas. L'aigua pura es fon a 0 °C i bull a 100 °C a 1 atm. Una mescla, en canvi, no té trams horitzontals perfectes.")
    b += figs.fig(T2.corba_escalfament(), "Corba d'escalfament de l'aigua des de −20 °C.", "140mm")
    b += S(10, "El repte i la seguretat")
    b += P("Dins del cotxe a l'agost la temperatura pot arribar a 60–70 °C. Les partícules del gas de la llauna es mouen més de pressa, xoquen més sovint i amb més força contra les parets i la <b>pressió augmenta</b> (llei de Gay-Lussac, perquè el volum de la llauna és constant). A més, dins de la llauna hi ha propel·lent en estat líquid: amb la calor se'n vaporitza més i la pressió puja encara més. Si la llauna no resisteix aquesta pressió, <b>rebenta</b>; i com que el gas és inflamable, pot provocar un incendi.")
    b += TIP("Seguretat", "Les etiquetes dels aerosols diuen: «Recipient a pressió: pot rebentar si s'escalfa. Protegiu-lo de la llum del sol. No l'exposeu a temperatures superiors a 50 °C. No el perforeu ni el cremeu, ni tan sols quan ja s'hagi acabat.» Porten el pictograma de flama (inflamable) i el de bombona (gas a pressió).")
    b += KW(("Model", "representació simplificada que explica i prediu"), ("Model cineticomolecular", "partícules en moviment, amb buit i forces d'atracció entre elles"),
            ("Temperatura", "mesura de l'energia cinètica mitjana de les partícules"), ("Zero absolut", "0 K = −273 °C"), ("Pressió", "força per unitat de superfície; en un gas, efecte dels xocs"),
            ("Boyle-Mariotte", "P · V = constant (T constant)"), ("Charles", "V / T = constant (P constant)"), ("Gay-Lussac", "P / T = constant (V constant)"),
            ("Calor latent", "energia per canviar d'estat 1 kg de substància"), ("Temperatura d'ebullició", "temperatura fixa a què bull un líquid; depèn de la pressió"))
    return b

# ======================================================================== SdA 3
def sda3():
    b = H(3, "Què hi ha dins del meu mòbil? L'àtom, els ions, la taula periòdica, l'enllaç químic i la bateria de liti.")
    b += TOC("Elements químics", "Els models atòmics", "Les partícules de l'àtom: Z i A", "Isòtops i massa atòmica", "Els ions", "Els electrons en capes i l'assaig a la flama", "La taula periòdica", "Propietats periòdiques", "L'enllaç químic", "Fórmules i substàncies", "La bateria de liti", "Mòbils, recursos i reciclatge")
    b += S(1, "Elements químics")
    b += P("Un <b>element químic</b> és una substància formada per un sol tipus d'àtom, que no es pot descompondre en substàncies més simples. Se'n coneixen 118; uns 90 es troben a la natura i la resta s'han obtingut al laboratori. Cada element té un nom i un <b>símbol</b> d'una o dues lletres (la primera en majúscula), sovint a partir del nom llatí: Na (<i>natrium</i>, sodi), K (<i>kalium</i>, potassi), Au (<i>aurum</i>, or), Pb (<i>plumbum</i>, plom). Un mòbil en conté uns 31: coure als circuits, silici als xips, liti i cobalt a la bateria, or als contactes, neodimi a l'altaveu, indi a la pantalla…")
    b += S(2, "Els models atòmics")
    b += P("L'àtom és massa petit per veure'l (uns 10⁻¹⁰ m). El que en sabem ho hem deduït d'experiments, i el model ha anat canviant cada vegada que un experiment no es podia explicar amb el model anterior.")
    b += T(["Model", "Any", "Com és l'àtom", "Què explica i per què es va abandonar"],
           [["Dalton", "1808", "Esferes massisses i indivisibles; els àtoms d'un element són iguals entre ells i diferents dels d'un altre; els compostos es formen unint àtoms en proporcions de nombres enters", "Explicava les lleis de les reaccions (Lavoisier, Proust). No explicava l'electricitat: es va descobrir que l'àtom té parts"],
            ["Thomson", "1897", "Esfera de càrrega positiva amb electrons (negatius) incrustats, com un pastís de panses; en conjunt, neutre", "Explicava l'electrització i l'existència de l'electró. No explicava l'experiment de Rutherford"],
            ["Rutherford", "1911", "Un <b>nucli</b> molt petit, amb tota la càrrega positiva i gairebé tota la massa; els electrons giren al voltant; la major part de l'àtom és <b>buit</b>", "Explicava la dispersió de les partícules α. No explicava per què els elements emeten llum de colors concrets"],
            ["Bohr", "1913", "Els electrons es mouen en <b>capes</b> o òrbites amb una energia fixa; només poden saltar d'una capa a una altra absorbint o emetent energia", "Explica els espectres dels elements. Avui es fa servir un model encara més complet (orbitals)"]], w=["12%", "8%", "42%", "38%"])
    b += EX("L'experiment de Rutherford", "Va bombardejar una làmina d'or molt prima amb partícules alfa (positives). Gairebé totes la travessaven sense desviar-se (l'àtom és gairebé buit), unes poques es desviaven i algunes rebotaven (xocaven amb un nucli molt petit, positiu i dens). El nucli és unes 100 000 vegades més petit que l'àtom: si l'àtom fos un estadi de futbol, el nucli seria una formiga al centre del camp.")
    b += S(3, "Les partícules de l'àtom: Z i A")
    b += T(["Partícula", "Càrrega", "Massa (u)", "On és", "Descoberta"], [["Protó", "+1", "≈ 1", "Nucli", "Rutherford, 1919"], ["Neutró", "0", "≈ 1", "Nucli", "Chadwick, 1932"], ["Electró", "−1", "≈ 1/1836 (gairebé 0)", "Escorça (capes)", "Thomson, 1897"]])
    b += P("La unitat de massa atòmica (u) és aproximadament la massa d'un protó (1,66 · 10⁻²⁷ kg).")
    b += F("Z = nombre de protons (nombre atòmic)", "A = protons + neutrons (nombre màssic)", "neutrons = A − Z", note="El nombre atòmic identifica l'element: tots els àtoms de carboni tenen 6 protons. En un àtom neutre, electrons = protons. Notació: <sup>A</sup><sub>Z</sub>X")
    b += EX("Exemple", "<sup>7</sup><sub>3</sub>Li: Z = 3 → 3 protons i 3 electrons; neutrons = 7 − 3 = 4. <sup>56</sup><sub>26</sub>Fe: 26 protons, 26 electrons i 30 neutrons.")
    b += S(4, "Isòtops i massa atòmica")
    b += P("Els <b>isòtops</b> són àtoms del mateix element (mateix Z) amb diferent nombre de neutrons (diferent A): <sup>6</sup>Li i <sup>7</sup>Li; <sup>12</sup>C, <sup>13</sup>C i <sup>14</sup>C. Tenen les mateixes propietats químiques, perquè tenen el mateix nombre d'electrons, però masses diferents. Alguns són radioactius (el <sup>14</sup>C es fa servir per datar restes arqueològiques).",
           "La <b>massa atòmica</b> que surt a la taula periòdica és la mitjana de les masses dels isòtops de l'element, tenint en compte l'abundància de cadascun. Per això no és un nombre enter.")
    b += EX("Exemple", "El clor natural té un 75 % de <sup>35</sup>Cl i un 25 % de <sup>37</sup>Cl: massa atòmica = 0,75 · 35 + 0,25 · 37 = 35,5 u.")
    b += S(5, "Els ions")
    b += P("Un <b>ió</b> és un àtom (o un grup d'àtoms) que ha guanyat o perdut electrons i, per tant, té càrrega elèctrica. El nombre de protons no canvia mai: si canviés, seria un altre element.")
    b += UL("<b>Catió</b> (+): ha <b>perdut</b> electrons. Li → Li⁺ + e⁻ · Mg → Mg²⁺ + 2 e⁻. Els <b>metalls</b> tendeixen a formar cations.",
            "<b>Anió</b> (−): ha <b>guanyat</b> electrons. F + e⁻ → F⁻ · O + 2 e⁻ → O²⁻. Els <b>no metalls</b> tendeixen a formar anions.")
    b += figs.fig(T2.ions_formacio(), "Formació d'un catió (Na⁺) i d'un anió (Cl⁻) amb el model de capes.", "165mm")
    b += F("electrons d'un ió = Z − càrrega", note="Na⁺ (Z = 11): 10 electrons · O²⁻ (Z = 8): 8 + 2 = 10 electrons · Co²⁺ (Z = 27): 25 electrons")
    b += S(6, "Els electrons en capes i l'assaig a la flama")
    b += P("Al model de Bohr, els electrons s'ordenen en capes al voltant del nucli. A la primera capa hi caben 2 electrons; a la segona, 8; a 3r d'ESO omplim la tercera fins a 8 i comencem la quarta. Els electrons de l'<b>última capa</b> (electrons de valència) decideixen les propietats químiques de l'element.")
    b += T(["Element", "Z", "Capes", "Element", "Z", "Capes"],
           [["Hidrogen", "1", "1", "Neó", "10", "2, 8"], ["Heli", "2", "2", "Sodi", "11", "2, 8, 1"], ["Liti", "3", "2, 1", "Clor", "17", "2, 8, 7"], ["Carboni", "6", "2, 4", "Argó", "18", "2, 8, 8"],
            ["Oxigen", "8", "2, 6", "Potassi", "19", "2, 8, 8, 1"], ["Fluor", "9", "2, 7", "Calci", "20", "2, 8, 8, 2"]])
    b += figs.fig(T2.bohr_atoms(), "Electrons per capes (model de Bohr) del liti, l'oxigen, el sodi i el clor.", "160mm")
    b += P("Quan escalfem una sal a la flama, alguns electrons <b>absorbeixen energia</b> i salten a una capa més allunyada del nucli (estat excitat). En tornar a la seva capa, <b>emeten aquesta energia en forma de llum</b>. Com que les capes de cada element tenen unes energies concretes, cada element emet uns colors propis: el liti, vermell intens; el sodi, groc; el potassi, lila; el coure, verd blavós; l'estronci, vermell. L'<b>espectroscopi</b> separa la llum en línies de colors (l'<b>espectre d'emissió</b>), que és com l'empremta dactilar de l'element i és més fiable que el color a ull nu (el liti i l'estronci fan tots dos vermell). El color identifica l'<b>element</b>, no el compost. Bunsen i Kirchhoff van descobrir així el cesi i el rubidi (1860–1861), i l'heli es va descobrir primer a l'espectre del Sol.")
    b += PB + S(7, "La taula periòdica")
    b += P("El 1869, Dmitri <b>Mendeléiev</b> va ordenar els 63 elements coneguts per massa atòmica i va col·locar en una mateixa columna els que tenien propietats semblants. Va deixar forats per a elements encara no descoberts i en va predir les propietats; quan es van descobrir el gal·li, l'escandi i el germani, les prediccions es van complir. Avui la taula s'ordena per <b>nombre atòmic Z</b>.")
    b += taula_familia()
    b += UL("Les files són els <b>períodes</b> (1–7): el número del període indica quantes capes d'electrons té l'àtom.",
            "Les columnes són els <b>grups</b> (1–18): els elements d'un grup tenen el mateix nombre d'electrons a l'última capa i, per tant, propietats químiques semblants. Grups 1 i 2: tants electrons de valència com el número del grup; grups 13–18: el número del grup menys 10.",
            "Grups amb nom propi: <b>alcalins</b> (1), <b>alcalinoterris</b> (2), <b>metalls de transició</b> (3–12), <b>terris</b> (13), <b>carbonoides</b> (14), <b>nitrogenoides</b> (15), <b>amfígens</b> (16), <b>halògens</b> (17) i <b>gasos nobles</b> (18). Les dues files de sota són els <b>lantànids</b> (terres rares, com el neodimi dels imants de l'altaveu) i els <b>actínids</b>.")
    b += T(["", "Metalls", "No metalls", "Semimetalls"],
           [["On són", "Esquerra i centre (la gran majoria)", "Dreta (i l'hidrogen)", "Frontera en escala: B, Si, Ge, As, Sb, Te"],
            ["Propietats", "Brillantor metàl·lica, bons conductors de la calor i el corrent, dúctils i mal·leables, sòlids (excepte el mercuri)", "Sense brillantor, mals conductors, fràgils si són sòlids; molts són gasos", "Propietats intermèdies; el silici i el germani són semiconductors (xips)"],
            ["Ions", "Formen cations (perden electrons)", "Formen anions (guanyen electrons)", "—"]], w=["14%", "32%", "30%", "24%"])
    b += S(8, "Propietats periòdiques")
    b += P("Les propietats dels elements varien de manera regular (periòdica) al llarg de la taula:")
    b += UL("<b>València iònica:</b> per tenir l'última capa completa com un gas noble (<b>regla de l'octet</b>), els àtoms guanyen o perden electrons. Grup 1 → +1 · grup 2 → +2 · grup 13 → +3 · grup 15 → −3 · grup 16 → −2 · grup 17 → −1 · grup 18 → no en formen.",
            "<b>Mida dels àtoms:</b> augmenta en baixar en un grup (hi ha més capes) i disminueix d'esquerra a dreta en un període (el nucli té més protons i atrau més els electrons).",
            "<b>Caràcter metàl·lic i reactivitat:</b> els metalls alcalins perden fàcilment el seu únic electró de valència, i com més avall són al grup, més fàcilment el perden i més violentament reaccionen amb l'aigua (Li < Na < K). Els halògens guanyen fàcilment un electró, i el més reactiu és el fluor. Els gasos nobles gairebé no reaccionen.")
    b += S(9, "L'enllaç químic")
    b += P("Els àtoms s'uneixen perquè així són més estables: aconsegueixen una configuració semblant a la d'un gas noble guanyant, perdent o compartint electrons. Hi ha tres tipus d'enllaç:")
    b += T(["Enllaç", "Entre…", "Què fan els electrons", "Estructura", "Propietats", "Exemples"],
           [["Iònic", "metall + no metall", "El metall en cedeix i el no metall en capta; els ions de càrrega oposada s'atrauen", "Xarxa cristal·lina de cations i anions", "Sòlids durs i fràgils, temperatures de fusió altes; molts es dissolen en aigua; condueixen fosos o dissolts, no en estat sòlid", "NaCl, LiF, LiCoO₂"],
            ["Covalent", "no metall + no metall", "Es comparteixen parells d'electrons", "Molècules (H₂, O₂, H₂O, CO₂) o xarxes covalents (diamant, grafit, SiO₂)", "Molècules: sovint gasos o líquids, temperatures de fusió baixes. Xarxes: molt dures i temperatures de fusió molt altes. No condueixen (excepte el grafit)", "H₂O, CO₂, SiO₂, plàstics"],
            ["Metàl·lic", "metall + metall", "Els àtoms deixen anar els electrons de valència, que formen un «núvol» que es mou per tot el metall", "Xarxa de cations envoltats d'electrons lliures", "Condueixen el corrent i la calor, brillants, dúctils i mal·leables", "Cu, Au, Al, aliatges"]], w=["10%", "13%", "21%", "18%", "26%", "12%"])
    b += figs.fig(T2.enllacos(), "Els tres tipus d'enllaç químic.", "155mm")
    b += EX("Exemple d'enllaç iònic", "LiF: el liti (2, 1) cedeix el seu electró de valència al fluor (2, 7). Es formen Li⁺ (2) i F⁻ (2, 8), els dos amb la configuració d'un gas noble. Les càrregues + i − s'atrauen; el compost és neutre perquè hi ha el mateix nombre de cations que d'anions.")
    b += EX("Exemple d'enllaç covalent", "A la molècula d'aigua, l'oxigen (6 electrons de valència) comparteix un parell d'electrons amb cada hidrogen: així l'oxigen arriba a 8 i cada hidrogen a 2.")
    b += P("Al mòbil: els cables i les pistes són de <b>coure</b> (metàl·lic, condueix); el separador de la bateria és de <b>plàstic</b> (covalent, aïllant); el vidre de la pantalla és <b>SiO₂</b> (xarxa covalent, dur). El <b>grafit</b> és carboni amb enllaços covalents, però cada àtom té un electró lliure que es pot moure entre les capes: per això condueix i es fa servir a l'ànode de la bateria.")
    b += S(10, "Fórmules i substàncies")
    b += P("La <b>fórmula</b> d'una substància indica quins elements la formen i en quina proporció. En un compost iònic indica la proporció d'ions a la xarxa (MgCl₂: un Mg²⁺ per cada dos Cl⁻, perquè les càrregues es compensen). En una substància covalent molecular, indica els àtoms de cada molècula (H₂O: dos àtoms d'hidrogen i un d'oxigen).")
    b += S(11, "La bateria de liti")
    b += P("Una bateria transforma energia química en energia elèctrica. La de liti té dos elèctrodes: l'<b>ànode</b> de grafit, on hi ha el liti, i el <b>càtode</b> d'òxid de liti i cobalt (LiCoO₂), separats per un <b>electròlit</b> (un líquid amb ions) i un <b>separador</b> de plàstic.",
           "Quan fem servir el mòbil (descàrrega), cada àtom de liti de l'ànode perd un electró: Li → Li⁺ + e⁻. Els ions Li⁺ viatgen a través de l'electròlit fins al càtode; els electrons no poden passar per l'electròlit i fan el camí pel circuit del mòbil: aquest corrent d'electrons fa funcionar el mòbil. Quan la carreguem, el carregador aporta energia i fa tornar el liti a l'ànode.",
           "Si la bateria es perfora, s'aixafa (per exemple, dins del camió de les escombraries) o s'escalfa massa, el separador es pot trencar: l'ànode i el càtode es toquen, hi ha un <b>curtcircuit</b>, la bateria s'escalfa molt de pressa, l'electròlit (inflamable) es crema i el foc és molt difícil d'apagar.")
    b += figs.fig(T2.bateria_liti(), "La bateria de liti mentre fem servir el mòbil.", "145mm")
    b += S(12, "Mòbils, recursos i reciclatge")
    b += P("Molts materials del mòbil són <b>matèries primeres crítiques</b>: són imprescindibles per a la tecnologia i se n'obtenen en pocs països, de vegades amb greus problemes ambientals (contaminació, desforestació) i socials (treball infantil, conflictes armats), com el cobalt i el coltan de la República Democràtica del Congo. Per això cal, per ordre: <b>reduir</b> (no canviar de mòbil si no cal), <b>reutilitzar</b> (reparar-lo, donar-lo) i <b>reciclar</b> (portar-lo a un punt de recollida, on es recuperen els elements, per exemple dissolent els metalls i separant-ne els ions). Mai al contenidor de rebuig.")
    b += KW(("Element", "substància amb un sol tipus d'àtom"), ("Nucli", "part central de l'àtom, amb protons i neutrons"), ("Nombre atòmic (Z)", "nombre de protons; identifica l'element"), ("Nombre màssic (A)", "protons + neutrons"),
            ("Isòtops", "mateix Z, diferent A"), ("Catió i anió", "ió positiu i ió negatiu"), ("Electrons de valència", "electrons de l'última capa"), ("Espectre d'emissió", "línies de colors que emet un element excitat"),
            ("Regla de l'octet", "els àtoms tendeixen a tenir 8 electrons a l'última capa"), ("Enllaç iònic, covalent i metàl·lic", "transferència, compartició i núvol d'electrons"))
    return b

# ======================================================================== SdA 4
def sda4():
    b = H(4, "Un cotxe que només allibera aigua? La reacció química, la formulació, les equacions, els càlculs de massa i l'energia de les reaccions.")
    b += TOC("La reacció química", "La teoria de les col·lisions", "La conservació de la massa i les proporcions", "Massa atòmica i massa molecular", "Formulació i nomenclatura", "L'equació química i com s'ajusta", "Càlculs de massa", "L'energia de les reaccions", "La velocitat de les reaccions", "Reaccions importants", "Els combustibles i l'hidrogen")
    b += S(1, "La reacció química")
    b += P("En una <b>reacció química</b>, unes substàncies, els <b>reactius</b>, es transformen en unes altres de noves, els <b>productes</b>, amb propietats diferents. A escala de partícules, els <b>enllaços</b> entre els àtoms dels reactius es <b>trenquen</b> i els àtoms es <b>reorganitzen</b> i formen enllaços nous. Els àtoms no canvien: només canvien de company.",
           "Evidències que s'ha produït una reacció: es forma un gas (bombolles), canvia el color, apareix un sòlid (precipitat), canvia l'olor, s'allibera o s'absorbeix calor, s'emet llum o so.")
    b += EX("Combustió de l'espelma", "La parafina (un hidrocarbur, amb carboni i hidrogen) reacciona amb l'oxigen de l'aire i es formen aigua (el got fred s'entela) i diòxid de carboni (l'aigua de calç es torna blanca). Si l'espelma fos d'hidrogen, només es formaria aigua.")
    b += S(2, "La teoria de les col·lisions")
    b += P("Per explicar com i a quina velocitat passen les reaccions fem servir la <b>teoria de les col·lisions</b>. Perquè dues partícules reaccionin no n'hi ha prou que es trobin: han de complir tres condicions.")
    b += OL("Les partícules dels reactius han de <b>xocar</b>.",
            "El xoc ha de tenir prou <b>energia</b>: l'energia cinètica de les partícules ha de ser igual o més gran que l'<b>energia d'activació</b> (E<sub>a</sub>), l'energia mínima necessària per trencar els enllaços dels reactius.",
            "Les partícules han de xocar amb l'<b>orientació adequada</b>: les parts de les molècules que han de reaccionar s'han de trobar.")
    b += P("Un xoc que compleix les tres condicions és un <b>xoc eficaç</b> i hi forma els productes. La majoria de xocs no són eficaços: les partícules reboten i continuen sent reactius. L'energia d'activació és com un turó que cal superar: per això el paper no crema sol a temperatura ambient, però sí quan hi apropem un llumí, que aporta l'energia per començar la reacció; després, la calor que desprèn la mateixa combustió la manté.")
    b += figs.fig(T2.col_lisions(), "Teoria de les col·lisions: només els xocs amb prou energia i ben orientats formen productes.", "160mm")
    b += F("xoc eficaç = xoc + energia ≥ E<sub>a</sub> + orientació adequada")
    b += S(3, "La conservació de la massa i les proporcions")
    b += P("<b>Llei de Lavoisier o de conservació de la massa (1789):</b> en una reacció química en un sistema tancat, la massa total dels reactius és igual a la massa total dels productes. S'explica perquè els àtoms no es creen ni es destrueixen: només es reorganitzen.",
           "En un <b>sistema obert</b> sembla que la massa canvia perquè hi entren o en surten gasos: en el vas amb vinagre i bicarbonat, el CO₂ s'escapa i la massa baixa; quan es rovella un clau o crema magnesi, l'oxigen de l'aire s'hi incorpora i la massa del sòlid puja. En un <b>sistema tancat</b> la massa es manté constant.",
           "<b>Llei de Proust o de les proporcions definides (1799):</b> quan dos elements es combinen per formar un compost, ho fan sempre en la mateixa proporció en massa. 4 g d'hidrogen reaccionen amb 32 g d'oxigen i formen 36 g d'aigua (proporció 1 : 8); amb 8 g d'hidrogen calen 64 g d'oxigen i es formen 72 g d'aigua. Si hi posem 10 g d'hidrogen i 64 g d'oxigen, sobraran 2 g d'hidrogen.")
    b += figs.fig(T2.sistema_obert_tancat(), "La massa es conserva en un sistema tancat; en un d'obert, el gas s'escapa.", "140mm")
    b += S(4, "Massa atòmica i massa molecular")
    b += P("La <b>massa atòmica</b> d'un element és la massa dels seus àtoms en unitats de massa atòmica (u); la trobem a la taula periòdica. La <b>massa molecular</b> d'una substància és la suma de les masses atòmiques dels àtoms que indica la fórmula.")
    b += T(["Element", "H", "C", "N", "O", "Na", "Mg", "Al", "S", "Cl", "Ca", "Fe"], [["Massa (u)", "1", "12", "14", "16", "23", "24", "27", "32", "35,5", "40", "56"]])
    b += EX("Exemple", "H₂O: 2 · 1 + 16 = 18 u · CO₂: 12 + 2 · 16 = 44 u · CH₄: 12 + 4 · 1 = 16 u · MgCl₂: 24 + 2 · 35,5 = 95 u.")
    b += S(5, "Formulació i nomenclatura (IUPAC)")
    b += P("Per entendre'ns, les fórmules i els noms segueixen les normes de la <b>IUPAC</b> (Unió Internacional de Química Pura i Aplicada).")
    b += UL("<b>Substàncies simples:</b> formades per un sol element. Metalls i gasos nobles s'escriuen amb el símbol (Fe, Mg, He). Alguns no metalls formen molècules diatòmiques: H₂ (dihidrogen), O₂ (dioxigen), N₂ (dinitrogen), F₂, Cl₂, Br₂, I₂. L'ozó és O₃ (trioxigen).",
            "<b>Cations monoatòmics:</b> «ió» + nom del metall: Na⁺ ió sodi, Ca²⁺ ió calci, Al³⁺ ió alumini. Si el metall pot formar més d'un ió, la càrrega s'indica amb nombres romans: Fe²⁺ ió ferro(II), Fe³⁺ ió ferro(III), Cu⁺ ió coure(I), Cu²⁺ ió coure(II).",
            "<b>Anions monoatòmics:</b> arrel del nom + <b>-ur</b>: F⁻ fluorur, Cl⁻ clorur, Br⁻ bromur, I⁻ iodur, S²⁻ sulfur, N³⁻ nitrur, H⁻ hidrur; i O²⁻ òxid.")
    b += P("<b>Compostos iònics binaris</b> (metall + no metall): la suma de les càrregues ha de ser zero. S'escriu primer el catió i després l'anió; el nom és el de l'anió + «de» + el del catió.")
    b += EX("Com es formula", "Ió alumini Al³⁺ i ió òxid O²⁻: necessitem 2 Al (+6) i 3 O (−6) → <b>Al₂O₃</b>, òxid d'alumini. Truc: la càrrega d'un ió és el subíndex de l'altre (simplificant si es pot): Ca²⁺ i O²⁻ → Ca₂O₂ → <b>CaO</b>.")
    b += P("<b>Compostos de dos no metalls</b> (covalents): s'escriu primer l'element que és més a l'esquerra a la taula (o més avall en un grup), amb l'ordre B, Si, C, Sb, As, P, N, H, Te, Se, S, I, Br, Cl, O, F. El nom porta <b>prefixos</b> multiplicadors (mono-, di-, tri-, tetra-, penta-, hexa-, hepta-) que indiquen quants àtoms de cada element hi ha. El prefix mono- s'omet en el primer element.")
    b += T(["Fórmula", "Nom", "Fórmula", "Nom"],
           [["CO", "monòxid de carboni", "NO₂", "diòxid de nitrogen"], ["CO₂", "diòxid de carboni", "N₂O", "monòxid de dinitrogen"], ["SO₃", "triòxid de sofre", "CCl₄", "tetraclorur de carboni"],
            ["HCl", "clorur d'hidrogen", "H₂S", "sulfur d'hidrogen"], ["H₂O", "aigua (nom acceptat)", "NH₃", "amoníac (nom acceptat)"], ["CH₄", "metà (nom acceptat)", "P₂O₅", "pentaòxid de difòsfor"]])
    b += S(6, "L'equació química i com s'ajusta")
    b += P("Una <b>equació química</b> representa una reacció: les fórmules dels reactius a l'esquerra, una fletxa, i les dels productes a la dreta. Es pot indicar l'estat de cada substància: (s) sòlid, (l) líquid, (g) gas, (aq) dissolt en aigua. Una equació està <b>ajustada</b> quan hi ha el mateix nombre d'àtoms de cada element a cada costat, com exigeix la llei de Lavoisier. Per ajustar-la posem <b>coeficients</b> davant de les fórmules; <b>mai no canviem els subíndexs</b>, perquè canviaríem la substància.")
    b += Hd.particules_svg()
    b += OL("Escriu les fórmules correctes de reactius i productes.", "Compta els àtoms de cada element a cada costat.", "Ajusta primer els elements que surten en una sola substància a cada costat (sovint els metalls i el carboni), després l'hidrogen i al final l'oxigen.", "Torna a comptar. Si queda un coeficient fraccionari, multiplica-ho tot per 2.")
    b += EX("Exemple", "CH₄ + O₂ → CO₂ + H₂O. Carboni: 1 i 1. Hidrogen: 4 a l'esquerra → 2 H₂O. Oxigen: a la dreta n'hi ha 2 + 2 = 4 → 2 O₂. Ajustada: <b>CH₄ + 2 O₂ → CO₂ + 2 H₂O</b>.")
    b += EX("Exemple", "Mg + HCl → MgCl₂ + H₂. Clor: 1 i 2 → 2 HCl. Hidrogen: 2 i 2. Ajustada: <b>Mg + 2 HCl → MgCl₂ + H₂</b>.")
    b += S(7, "Càlculs de massa")
    b += P("Els coeficients d'una equació ajustada indiquen la proporció en què reaccionen les partícules. Si hi multipliquem les masses moleculars, obtenim la proporció en massa (en grams) entre reactius i productes. Amb aquesta proporció fem un factor de conversió.")
    b += F("2 H₂ + O₂ → 2 H₂O", "2 · 2 = 4 g + 32 g → 2 · 18 = 36 g")
    b += EX("Exemple", "Quina massa d'aigua es forma amb 8 g d'hidrogen? \\( 8\\ \\mathrm{g\\ H_2} \\cdot \\dfrac{36\\ \\mathrm{g\\ H_2O}}{4\\ \\mathrm{g\\ H_2}} = 72\\ \\mathrm{g\\ H_2O} \\). I d'oxigen calen \\( 8 \\cdot \\dfrac{32}{4} = 64 \\) g. Un autobús que consumeix 20 kg d'hidrogen al dia allibera 180 kg d'aigua i consumeix 160 kg d'oxigen.")
    b += EX("Reactiu limitant", "Fem reaccionar 10 g d'hidrogen amb 100 g d'oxigen. 10 g d'H₂ necessiten 10 · 32 / 4 = 80 g d'O₂: en tenim prou, i en sobraran 20 g. L'hidrogen s'acaba primer: és el <b>reactiu limitant</b>, i és el que decideix quanta aigua es forma (10 · 36 / 4 = 90 g). L'oxigen és el reactiu en excés.")
    b += S(8, "L'energia de les reaccions")
    b += P("En una reacció, trencar els enllaços dels reactius <b>absorbeix</b> energia i formar els enllaços dels productes en <b>desprèn</b>. El balanç decideix si la reacció és:")
    b += UL("<b>Exotèrmica:</b> allibera energia a l'entorn (normalment en forma de calor i, de vegades, de llum); l'entorn s'escalfa. Els productes tenen menys energia que els reactius. Combustions, la respiració cel·lular, el magnesi amb àcid clorhídric, l'hidrogen amb l'oxigen.",
            "<b>Endotèrmica:</b> absorbeix energia de l'entorn (l'entorn es refreda) o cal subministrar-n'hi contínuament. Els productes tenen més energia que els reactius. El vinagre amb el bicarbonat, l'electròlisi de l'aigua, la fotosíntesi, coure un ou.")
    b += figs.fig(T2.diagrames_energia(), "Diagrames d'energia d'una reacció exotèrmica i d'una d'endotèrmica.", "160mm")
    b += T(["Diagrama d'energia", "Exotèrmica", "Endotèrmica"],
           [["Energia dels productes", "Més baixa que la dels reactius", "Més alta que la dels reactius"], ["Energia d'activació", "Sí: cal superar el «turó» per començar", "Sí: cal superar el «turó» i, a més, aportar l'energia que falta"], ["Temperatura de l'entorn", "Puja", "Baixa (o cal escalfar)"]])
    b += P("A l'<b>electròlisi</b>, el corrent elèctric aporta l'energia per descompondre l'aigua: 2 H₂O → 2 H₂ + O₂. Es forma el <b>doble de volum d'hidrogen</b> (al càtode, −) que d'oxigen (a l'ànode, +), perquè per cada molècula d'oxigen se'n formen dues d'hidrogen i, en les mateixes condicions, volums iguals de gasos contenen el mateix nombre de molècules. En massa, en canvi, la proporció és 4 g d'H₂ per 32 g d'O₂.")
    b += figs.fig(T2.electrolisi_neta(), "Electròlisi de l'aigua: al càtode es forma el doble de volum d'hidrogen que d'oxigen a l'ànode.", "150mm")
    b += S(9, "La velocitat de les reaccions")
    b += P("La <b>velocitat de reacció</b> indica quanta quantitat de reactiu desapareix (o de producte es forma) per unitat de temps. Segons la teoria de les col·lisions, tot el que augmenta el nombre de <b>xocs eficaços</b> per segon fa la reacció més ràpida:")
    b += T(["Factor", "Per què augmenta la velocitat", "Exemple"],
           [["Temperatura", "Les partícules es mouen més de pressa: xoquen més sovint i, sobretot, una proporció molt més gran de xocs supera l'energia d'activació", "El menjar es fa malbé més de pressa a l'estiu; a la nevera dura més"],
            ["Concentració", "Hi ha més partícules de reactiu en el mateix volum: més xocs per segon", "L'àcid més concentrat fa més bombolles amb el magnesi"],
            ["Superfície de contacte", "Si el sòlid està més dividit, hi ha més partícules exposades que poden xocar", "Les estelles cremen abans que un tronc; una pastilla triturada es dissol abans"],
            ["Catalitzadors", "Substàncies que ofereixen un camí amb una energia d'activació més baixa; no es gasten en la reacció", "Els enzims de la digestió; el catalitzador del tub d'escapament dels cotxes"]], w=["20%", "48%", "32%"])
    b += figs.fig(T2.factors_velocitat(), "Factors que augmenten la velocitat de les reaccions.", "160mm")
    b += S(10, "Reaccions importants")
    b += UL("<b>Combustió:</b> reacció d'un combustible amb l'oxigen, molt exotèrmica. Si el combustible conté carboni i hidrogen i hi ha prou oxigen, es formen CO₂ i H₂O; si falta oxigen, es pot formar monòxid de carboni (CO), un gas tòxic i sense olor.",
            "<b>Oxidació dels metalls:</b> el ferro es rovella en contacte amb l'oxigen i l'aigua (formació d'òxids de ferro); és una reacció lenta.",
            "<b>Reaccions dels àcids amb els metalls:</b> es formen una sal i hidrogen (Mg + 2 HCl → MgCl₂ + H₂). L'hidrogen es reconeix perquè, en apropar-hi una flama, fa una petita explosió.",
            "<b>Descomposició:</b> un compost es descompon en substàncies més simples (electròlisi de l'aigua; descomposició de l'aigua oxigenada).")
    b += S(11, "Els combustibles i l'hidrogen")
    b += P("Els <b>hidrocarburs</b> (metà, propà, butà, gasolina, gasoil) són compostos de carboni i hidrogen que s'obtenen del petroli i del gas natural. En cremar-los alliberen energia, però també CO₂, un gas d'efecte hivernacle. L'<b>hidrogen</b> no conté carboni: en una pila de combustible reacciona amb l'oxigen (2 H₂ + O₂ → 2 H₂O) i genera electricitat i aigua. Però que el vehicle no emeti CO₂ pel tub d'escapament no vol dir que no contamini gens: depèn de com s'obté l'hidrogen i de quanta energia s'hi gasta.")
    b += T(["Hidrogen", "D'on surt", "Emissions"], [["Gris", "Gas natural (reformat amb vapor)", "Emet CO₂ en produir-lo (uns 10–12 kg de CO₂ per kg d'H₂)"], ["Blau", "Gas natural, capturant i emmagatzemant part del CO₂", "Menys emissions"], ["Verd", "Electròlisi de l'aigua amb electricitat renovable", "Gairebé sense emissions"]], w=["14%", "40%", "46%"])
    b += P("A més, cada transformació perd energia: amb la mateixa electricitat renovable, un vehicle de bateria fa unes 2–3 vegades més quilòmetres que un d'hidrogen. L'hidrogen té més sentit en vehicles grans que fan molts quilòmetres i no poden parar gaire a carregar (autobusos, camions, vaixells), i en indústries que no es poden electrificar.")
    b += KW(("Reactius i productes", "substàncies inicials i substàncies noves"), ("Xoc eficaç", "xoc amb prou energia i orientació adequada"), ("Energia d'activació", "energia mínima perquè comenci la reacció"),
            ("Llei de Lavoisier", "la massa es conserva en un sistema tancat"), ("Llei de Proust", "els elements es combinen en proporció fixa en massa"), ("Massa molecular", "suma de les masses atòmiques de la fórmula"),
            ("Coeficient", "nombre davant d'una fórmula per ajustar l'equació"), ("Reactiu limitant", "el que s'acaba primer"), ("Exotèrmica i endotèrmica", "allibera energia i absorbeix energia"), ("Catalitzador", "accelera la reacció sense gastar-se"))
    return b

# ======================================================================== SdA 5
def sda5():
    b = H(5, "Com persegueix un neutròfil un bacteri sense veure'l? El moviment, el gradient de concentració i les forces.")
    b += TOC("Sistema de referència, posició i trajectòria", "Magnituds escalars i vectorials", "La velocitat", "El moviment rectilini uniforme (MRU)", "L'acceleració i el MRUA", "Caiguda lliure i frenada", "Les gràfiques del moviment", "Com es resol un problema",
             "Escales: la mida de les cèl·lules", "Difusió, gradient i quimiotaxi", "Les forces", "La llei de Hooke", "Les lleis de Newton", "Les forces de les cèl·lules")
    b += S(1, "Sistema de referència, posició i trajectòria")
    b += P("Un cos es mou quan canvia de posició respecte d'un punt que considerem fix, el <b>sistema de referència</b>. El moviment és relatiu: un passatger assegut en un tren està en repòs respecte del tren, però es mou respecte de l'andana.")
    b += UL("<b>Posició</b> (x): lloc on és el mòbil respecte del sistema de referència. Pot ser positiva o negativa.",
            "<b>Trajectòria</b>: línia que dibuixa el mòbil en moure's. Pot ser rectilínia o curvilínia (circular, parabòlica…).",
            "<b>Distància recorreguda</b> (d): longitud de la trajectòria. Sempre és positiva.",
            "<b>Desplaçament</b> (Δx = x − x₀): canvi de posició, la fletxa recta que va de la posició inicial a la final. Si anem i tornem al punt de partida, hem recorregut distància però el desplaçament és zero.")
    b += figs.fig(T2.trajectoria_desplacament(), "Trajectòria i desplaçament.", "120mm")
    b += S(2, "Magnituds escalars i vectorials")
    b += P("Les magnituds <b>escalars</b> queden definides amb un nombre i una unitat (massa, temps, temperatura, distància). Les <b>vectorials</b> necessiten, a més, una <b>direcció</b> i un <b>sentit</b>, i es representen amb una fletxa (<b>vector</b>) la longitud de la qual és el <b>mòdul</b>: desplaçament, velocitat, acceleració, força.")
    b += S(3, "La velocitat")
    b += F("v = Δx / Δt", note="Al SI, en m/s. De km/h a m/s, es divideix entre 3,6; de m/s a km/h, es multiplica per 3,6.")
    b += P("La <b>rapidesa mitjana</b> és la distància recorreguda dividida pel temps total. El mòdul de la <b>velocitat mitjana</b> és el desplaçament dividit pel temps. Si la trajectòria no és recta (com la d'un neutròfil que va canviant de direcció), la rapidesa mitjana és més gran que la velocitat mitjana. La <b>velocitat instantània</b> és la que té el mòbil en un instant concret (la que marca el velocímetre).")
    b += S(4, "El moviment rectilini uniforme (MRU)")
    b += P("La trajectòria és recta i la velocitat és constant: el mòbil recorre distàncies iguals en temps iguals. L'acceleració és zero.")
    b += F("x = x₀ + v · t")
    b += EX("Exemple", "Un autobús passa per x = 50 m a 36 km/h (10 m/s): x = 50 + 10 · t. Als 8 s és a 130 m; arriba a x = 250 m quan 250 = 50 + 10 · t → t = 20 s.")
    b += EX("Dos mòbils", "Dos patinets surten alhora de dos punts separats 300 m i van l'un cap a l'altre a 5 m/s. Amb l'origen al primer: x₁ = 5 · t i x₂ = 300 − 5 · t (el signe − indica que va cap a l'origen). Es troben quan x₁ = x₂: 5t = 300 − 5t → t = 30 s, a x = 150 m.")
    b += S(5, "L'acceleració i el MRUA")
    b += P("L'<b>acceleració</b> indica quant canvia la velocitat cada segon. Si el mòbil va cada vegada més de pressa i l'acceleració té el mateix signe que la velocitat, accelera; si frena, l'acceleració té el signe contrari (negativa si es mou en sentit positiu). Al <b>moviment rectilini uniformement accelerat (MRUA)</b> la trajectòria és recta i l'acceleració és constant: la velocitat canvia el mateix cada segon.")
    b += F("a = Δv / Δt  (m/s²)", "v = v₀ + a · t", "x = x₀ + v₀ · t + ½ · a · t²")
    b += EX("Exemple", "Una moto surt del repòs amb a = 2,5 m/s² durant 8 s: v = 0 + 2,5 · 8 = 20 m/s (72 km/h); x = ½ · 2,5 · 8² = 80 m.")
    b += S(6, "Caiguda lliure i frenada")
    b += P("Sense fregament amb l'aire, tots els cossos cauen amb la mateixa acceleració, la de la gravetat: <b>g = 9,8 m/s²</b> (Galileu). Una pilota que cau és un MRUA.",
           "La <b>distància d'aturada</b> d'un vehicle és la suma de la <b>distància de reacció</b> (la que recorre a velocitat constant mentre el conductor reacciona, uns 0,75–1 s) i la <b>distància de frenada</b> (MRUA amb acceleració negativa). Com que la distància de frenada depèn del quadrat de la velocitat, si la velocitat es duplica, la distància de frenada es multiplica per quatre.")
    b += EX("Frenada", "Un cotxe a 50 km/h (13,9 m/s) frena amb a = −5 m/s²: triga t = 13,9 / 5 ≈ 2,8 s i recorre ≈ 19 m. A 30 km/h (8,3 m/s): 1,7 s i ≈ 7 m. Amb 1 s de reacció, la distància d'aturada és ≈ 33 m a 50 km/h i ≈ 15 m a 30 km/h: per això a prop de les escoles el límit és de 30 km/h.")
    b += S(7, "Les gràfiques del moviment")
    b += T(["", "Gràfica x–t", "Gràfica v–t", "Gràfica a–t"],
           [["Repòs", "Recta horitzontal", "Recta sobre l'eix (v = 0)", "a = 0"], ["MRU", "Recta inclinada; el <b>pendent</b> és la velocitat (com més inclinada, més ràpid)", "Recta horitzontal", "a = 0"],
            ["MRUA", "Corba (paràbola)", "Recta inclinada; el <b>pendent</b> és l'acceleració", "Recta horitzontal"]])
    b += figs.fig(T2.grafiques_moviment(), "Gràfiques x–t i v–t del MRU i del MRUA.", "165mm")
    b += P("El <b>pendent</b> d'una recta es calcula amb dos punts: pendent = (canvi de l'eix vertical) / (canvi de l'eix horitzontal). A la gràfica v–t, l'<b>àrea</b> sota la línia és el desplaçament (la distància, si no canvia el sentit): un rectangle (base · altura) per als trams de velocitat constant i un triangle (base · altura / 2) per als que acceleren des de zero.")
    b += EX("Exemple", "Un patinet passa de 0 a 4 m/s en 2 s, manté 4 m/s durant 6 s i frena fins a aturar-se en 4 s. Acceleracions: 2 m/s², 0 i −1 m/s². Distància = 2 · 4 / 2 + 6 · 4 + 4 · 4 / 2 = 4 + 24 + 8 = 36 m.")
    b += S(8, "Com es resol un problema de moviment")
    b += OL("Dibuixa la situació i tria el sistema de referència i el sentit positiu.", "Escriu les dades amb unitats del SI (passa els km/h a m/s, els minuts a s).", "Identifica el tipus de moviment de cada tram (MRU o MRUA).", "Escriu les equacions, substitueix i aïlla la incògnita.", "Calcula i comprova que el resultat té sentit, amb la unitat.")
    b += S(9, "Escales: la mida de les cèl·lules")
    b += P("Les cèl·lules es mesuren en <b>micròmetres</b>: 1 µm = 0,001 mm = 10⁻⁶ m. Un glòbul vermell fa 7,5 µm; un neutròfil, uns 12 µm; un bacteri, 1–2 µm. Per mesurar en una imatge de microscopi fem servir la <b>barra d'escala</b> (indica quants µm representa una longitud de la imatge) o un objecte de mida coneguda.")
    b += F("augments = mida a la imatge / mida real", note="Les dues mides en la mateixa unitat. Mida real = mida a la imatge / augments.")
    b += S(10, "Difusió, gradient i quimiotaxi")
    b += P("La <b>difusió</b> és el moviment net de partícules des d'on n'hi ha més (concentració alta) cap a on n'hi ha menys (concentració baixa), a causa del moviment desordenat de les partícules (model cineticomolecular). Continua fins que la concentració és igual a tot arreu. És més ràpida amb més temperatura i en distàncies curtes: per això funciona bé a l'escala de les cèl·lules però no per portar oxigen a tot el cos.",
           "Un <b>gradient de concentració</b> és la variació de la concentració per unitat de distància. Els bacteris alliberen molècules (pèptids) que es difonen al seu voltant: la concentració és més alta a prop del bacteri i va baixant en allunyar-se'n.")
    b += F("gradient = Δconcentració / Δdistància", note="Exemple: de 100 nM a 20 nM en 40 µm → (20 − 100) / 40 = −2 nM/µm (la concentració baixa 2 nM per cada µm)")
    b += P("El neutròfil té <b>receptors</b> a la membrana que detecten aquestes molècules. La banda de la cèl·lula que en detecta més (la que mira cap al bacteri) es <b>polaritza</b>: hi creix l'actina i la cèl·lula avança cap allà. Aquest moviment guiat per un gradient químic es diu <b>quimiotaxi</b>. Amb febre, les cèl·lules immunitàries es mouen més de pressa.")
    b += figs.fig(T2.quimiotaxi(), "Quimiotaxi: el neutròfil segueix el gradient de concentració fins als bacteris.", "165mm")
    b += S(11, "Les forces")
    b += P("Una <b>força</b> és tota acció capaç de canviar l'estat de moviment d'un cos (posar-lo en moviment, aturar-lo, canviar-ne la velocitat o la direcció) o de <b>deformar-lo</b>. És una magnitud vectorial i es mesura en <b>newtons</b> (N) amb un <b>dinamòmetre</b>. Les forces poden ser <b>de contacte</b> (empènyer, fregament, la força normal d'una taula) o <b>a distància</b> (gravitatòria, elèctrica, magnètica).",
           "El <b>pes</b> és la força amb què la Terra atrau un cos: P = m · g, amb g = 9,8 N/kg. La massa (kg) és la mateixa a tot arreu; el pes (N) depèn d'on som: a la Lluna, on g = 1,6 N/kg, pesaríem unes sis vegades menys. Una massa de 50 g pesa 0,050 · 9,8 = 0,49 N.",
           "Quan sobre un cos actuen diverses forces, les podem substituir per una de sola, la <b>força resultant</b>. Si tenen la mateixa direcció i sentit, se sumen; si tenen sentits contraris, es resten i la resultant té el sentit de la més gran; si són perpendiculars, el mòdul de la resultant es calcula amb el teorema de Pitàgores. Gràficament, posem les fletxes una a continuació de l'altra: la resultant va de l'origen de la primera a l'extrem de l'última.")
    b += figs.fig(T2.forces_resultant(), "Força resultant en tres casos.", "155mm")
    b += S(12, "La llei de Hooke")
    b += P("Els cossos <b>elàstics</b> (una molla, una goma) recuperen la forma quan deixem de fer força; els <b>plàstics</b> (la plastilina) no. En un cos elàstic, l'allargament és proporcional a la força aplicada, mentre no superem el <b>límit d'elasticitat</b>: si l'estirem massa, queda deformat o es trenca. Els dinamòmetres funcionen gràcies a aquesta llei.")
    b += F("F = k · Δx", note="k: constant elàstica (N/m), el pendent de la gràfica F–Δx · Δx: allargament (m) = longitud − longitud inicial")
    b += EX("Exemple", "Una molla s'allarga 0,025 m amb un pes de 0,49 N: k = 0,49 / 0,025 ≈ 20 N/m. Si s'allarga 0,05 m, la força és 20 · 0,05 = 1 N, i la massa penjada és 1 / 9,8 ≈ 0,10 kg.")
    b += figs.fig(T2.hooke(), "Llei de Hooke: l'allargament és proporcional a la força.", "160mm")
    b += S(13, "Les lleis de Newton")
    b += T(["Llei", "Què diu", "Exemple"],
           [["1a · Inèrcia", "Si la força resultant sobre un cos és zero, el cos manté el seu estat: si estava en repòs, continua en repòs; si es movia, continua amb MRU", "Si el patinet frena de cop, el cos del conductor continua endavant (per això porta casc i els cotxes, cinturó)"],
            ["2a · Força i acceleració", "La força resultant és igual a la massa per l'acceleració: F = m · a (1 N = 1 kg · m/s²). L'acceleració té la direcció i el sentit de la força resultant", "Amb la mateixa força, un patinet més carregat accelera menys"],
            ["3a · Acció i reacció", "Si un cos A fa una força sobre un cos B, B fa sobre A una força igual i de sentit contrari. Les dues forces actuen sobre cossos diferents i no s'anul·len", "Per avançar, empenyem el terra cap enrere i el terra ens empeny cap endavant; un coet expulsa gasos i els gasos l'empenyen"]], w=["18%", "47%", "35%"])
    b += EX("Exemple", "Un patinet amb el conductor (80 kg) passa de 0 a 6 m/s en 4 s: a = 6 / 4 = 1,5 m/s² i F = 80 · 1,5 = 120 N. Si frena amb a = −3 m/s², la força de frenada és 80 · (−3) = −240 N.")
    b += figs.fig(T2.accio_reaccio(), "Acció i reacció: per avançar, empenyem (o estirem) el terra cap enrere.", "165mm")
    b += S(14, "Les forces de les cèl·lules")
    b += P("Per dins, la cèl·lula té un <b>citoesquelet</b>, una xarxa de filaments de proteïnes. Els filaments d'<b>actina</b> creixen a la part del davant i empenyen la membrana endavant; a la vegada, a través de les <b>adhesions focals</b> (punts on la cèl·lula s'enganxa al substrat), estiren el substrat cap enrere. Per la 3a llei de Newton, el substrat estira la cèl·lula cap endavant, i la cèl·lula avança. Els <b>microtúbuls</b> fan de vies de transport dins de la cèl·lula.",
           "Les forces de les cèl·lules són de l'ordre dels <b>nanonewtons</b> (1 nN = 10⁻⁹ N). Es mesuren posant la cèl·lula sobre un gel tou amb boletes fluorescents: el gel es comporta com un conjunt de molles i, pel desplaçament de les boletes i la llei de Hooke, en calculem la força. A l'escala de la cèl·lula, el fregament de l'aigua és enorme comparat amb la massa de la cèl·lula: quan deixa de fer força, s'atura gairebé a l'instant (la inèrcia no hi té gaire paper).")
    b += TIP("Salut", "Mesurar les forces i la velocitat de les cèl·lules ajuda a entendre la resposta immunitària, la cicatrització de les ferides (les cèl·lules de la vora es mouen per tancar-la) i la metàstasi (les cèl·lules tumorals que es desplacen per l'organisme). La febre és una conseqüència de la resposta del cos a la infecció, no la causa de la malaltia.")
    b += KW(("Sistema de referència", "punt respecte del qual descrivim el moviment"), ("Desplaçament", "canvi de posició"), ("Velocitat i acceleració", "Δx / Δt i Δv / Δt"), ("MRU i MRUA", "velocitat constant i acceleració constant"),
            ("Pendent", "a la x–t, velocitat; a la v–t, acceleració"), ("Gradient", "variació de la concentració amb la distància"), ("Quimiotaxi", "moviment guiat per un gradient químic"),
            ("Força resultant", "força que substitueix totes les que actuen sobre un cos"), ("Constant elàstica", "k = F / Δx"), ("Inèrcia", "tendència a mantenir l'estat de moviment"))
    return b

# ======================================================================== SdA 6
def sda6():
    b = H(6, "Quanta energia gasta la nostra aula i com podem estalviar-ne? L'energia, el treball, la potència, l'electricitat i les fonts d'energia.")
    b += TOC("L'energia i les seves formes", "Energia mecànica: cinètica i potencial", "Treball i calor: com es transfereix l'energia", "Conservació i degradació de l'energia", "El rendiment", "La potència", "Consum i cost de l'energia elèctrica", "El circuit elèctric: càrrega, intensitat, tensió i resistència", "Circuits en sèrie i en paral·lel", "Efectes del corrent i seguretat elèctrica", "Com es genera l'electricitat", "Les fonts d'energia", "La informació fiable")
    b += S(1, "L'energia i les seves formes")
    b += P("L'<b>energia</b> és la capacitat d'un sistema per produir canvis (moure's, escalfar-se, deformar-se, fer llum…). Al SI es mesura en <b>joules</b> (J); també es fan servir la caloria (1 cal = 4,18 J), la quilocaloria dels aliments (1 kcal = 4 180 J) i el quilowatt hora de les factures (1 kWh = 3,6 · 10⁶ J).")
    b += T(["Forma", "Associada a…", "Exemples"],
           [["Cinètica", "el moviment", "Un cotxe en marxa, el vent"], ["Potencial gravitatòria", "la posició (altura)", "L'aigua d'un embassament"], ["Potencial elàstica", "la deformació", "Un arc tensat, una molla comprimida"],
            ["Tèrmica (interna)", "el moviment de les partícules", "Una sopa calenta"], ["Química", "els enllaços entre àtoms", "Aliments, combustibles, piles"], ["Elèctrica", "el moviment de càrregues", "El corrent d'un endoll"],
            ["Radiant (lluminosa)", "les ones electromagnètiques", "La llum del Sol"], ["Sonora", "les vibracions de l'aire", "La música d'un altaveu"], ["Nuclear", "el nucli dels àtoms", "Les centrals nuclears, el Sol"]])
    b += S(2, "Energia mecànica: cinètica i potencial")
    b += F("E<sub>c</sub> = ½ · m · v²", "E<sub>p</sub> = m · g · h", "E<sub>m</sub> = E<sub>c</sub> + E<sub>p</sub>", note="m en kg, v en m/s, h en m, g = 9,8 m/s² → energia en J")
    b += P("L'energia cinètica depèn del quadrat de la velocitat: si un cotxe va el doble de ràpid, té quatre vegades més energia (i necessita quatre vegades més distància per frenar). Si no hi ha fregament, l'energia mecànica es conserva: quan un cos cau, l'energia potencial es transforma en cinètica.")
    b += EX("Exemple", "Un cotxe de 1 000 kg a 20 m/s (72 km/h) té E<sub>c</sub> = ½ · 1 000 · 20² = 200 000 J. 1 m³ d'aigua (1 000 kg) a 100 m d'altura en un embassament té E<sub>p</sub> = 1 000 · 9,8 · 100 = 980 000 J.")
    b += figs.fig(T2.energia_mecanica(), "Conservació de l'energia mecànica en una muntanya russa sense fregament.", "145mm")
    b += S(3, "Treball i calor: com es transfereix l'energia")
    b += P("L'energia passa d'un sistema a un altre de dues maneres. Per <b>treball</b>, quan una força desplaça un cos: W = F · d (en J, si la força té la direcció del desplaçament). Per <b>calor</b>, quan dos cossos a temperatures diferents són en contacte: l'energia passa del més calent al més fred fins que arriben a la mateixa temperatura (equilibri tèrmic). La calor no és una forma d'energia que un cos «té», sinó energia en trànsit.")
    b += S(4, "Conservació i degradació de l'energia")
    b += P("<b>Principi de conservació de l'energia:</b> l'energia no es crea ni es destrueix, només es transforma d'una forma a una altra o es transfereix d'un sistema a un altre; la quantitat total es manté constant.",
           "Ara bé, en cada transformació una part de l'energia es converteix en <b>energia tèrmica</b> que s'escampa per l'entorn i ja no podem aprofitar: diem que l'energia es <b>degrada</b>. Per això cal estalviar energia, encara que «no es perdi».")
    b += EX("Transformacions", "Ventilador: elèctrica → cinètica (+ tèrmica). Placa fotovoltaica: radiant → elèctrica. Altaveu: elèctrica → sonora. Pila que encén un llum: química → elèctrica → lluminosa (+ tèrmica). El nostre cos: química (aliments) → cinètica i tèrmica.")
    b += S(5, "El rendiment")
    b += P("El <b>rendiment</b> indica quina part de l'energia consumida es converteix en energia útil (la que volem obtenir). Sempre és més petit que el 100 %. Es representa amb un <b>diagrama de Sankey</b>: l'amplada de cada fletxa és proporcional a l'energia.")
    b += F("rendiment (%) = energia útil / energia consumida · 100")
    b += En.sankey_svg()
    b += EX("Exemple", "Una bombeta d'incandescència de 60 W fa 3 J de llum cada segon: rendiment = 3 / 60 · 100 = 5 %; els altres 57 J són calor. Una LED de 8 W fa la mateixa llum: 3 / 8 · 100 ≈ 38 %. Altres rendiments aproximats: motor de gasolina 25–30 %, motor elèctric 85–90 %, placa fotovoltaica 20 %.")
    b += S(6, "La potència")
    b += P("La <b>potència</b> indica la rapidesa amb què un aparell transforma l'energia: l'energia per unitat de temps. Es mesura en <b>watts</b> (1 W = 1 J/s) i la trobem a l'etiqueta dels aparells. Dos aparells poden gastar la mateixa energia, però el de més potència la gasta més de pressa.")
    b += F("P = E / t  ·  E = P · t", "1 kWh = 1 000 W · 3 600 s = 3,6 · 10⁶ J", note="E en J si P en W i t en s · E en kWh si P en kW i t en h")
    b += S(7, "Consum i cost de l'energia elèctrica")
    b += OL("Passa la potència a kW (divideix els watts entre 1 000).", "Multiplica per les hores que funciona: obtens kWh.", "Multiplica pels dies, si cal.", "Cost = kWh · preu del kWh (per exemple, 0,15 €).")
    b += EX("Exemple", "Una bombeta encesa 5 h cada dia durant un any: 60 W → 0,060 · 5 · 365 = 109,5 kWh → 16,43 €. LED de 8 W → 0,008 · 5 · 365 = 14,6 kWh → 2,19 €. S'estalvien 14,24 € l'any amb una sola bombeta.")
    b += P("El <b>consum fantasma</b> o en mode d'espera (el llum vermell encès, els carregadors endollats) també suma: un televisor d'1 W en espera 20 h al dia gasta 7,3 kWh l'any; amb tres milions de llars, 21,9 GWh (1 GWh = 10⁶ kWh). El <b>wattímetre</b> mesura la potència i l'energia reals d'un aparell, que poden ser diferents de les de l'etiqueta (l'etiqueta indica el màxim). L'<b>etiqueta energètica</b> classifica els electrodomèstics de la A (més eficient) a la G.")
    b += S(8, "El circuit elèctric: càrrega, intensitat, tensió i resistència")
    b += P("La matèria té càrregues elèctriques: protons (+) i electrons (−). El <b>corrent elèctric</b> és el moviment ordenat de càrregues per un conductor; en els metalls, el dels electrons lliures. Un <b>circuit</b> és un camí tancat format per un <b>generador</b> (pila, bateria, endoll), conductors (cables), receptors (bombetes, motors, resistències) i elements de control (interruptors). Si el circuit és obert, no hi passa corrent.")
    b += T(["Magnitud", "Què és", "Unitat", "Es mesura amb"],
           [["Intensitat (I)", "Quantitat de càrrega que travessa el conductor cada segon", "ampere (A)", "Amperímetre (en sèrie)"], ["Tensió o voltatge (V)", "Energia que el generador dona a cada unitat de càrrega: l'«impuls» del corrent", "volt (V)", "Voltímetre (en paral·lel)"],
            ["Resistència (R)", "Oposició d'un material al pas del corrent", "ohm (Ω)", "Ohmímetre"]], w=["20%", "45%", "15%", "20%"])
    b += figs.fig(T2.circuit_mesura(), "Elements d'un circuit i com es connecten l'amperímetre i el voltímetre.", "135mm")
    b += F("Llei d'Ohm: V = I · R", "Potència elèctrica: P = V · I", "Energia elèctrica: E = P · t = V · I · t", note="A casa i a l'institut, la tensió és de 230 V.")
    b += EX("Exemple", "Un bullidor de 2 000 W connectat a 230 V: I = P / V = 2 000 / 230 ≈ 8,7 A. Si funciona 3 minuts (0,05 h) gasta 2 kW · 0,05 h = 0,1 kWh.")
    b += S(9, "Circuits en sèrie i en paral·lel")
    b += figs.fig(T2.circuits_serie_paralel(), "Dues bombetes en sèrie i en paral·lel.", "140mm")
    b += T(["", "En sèrie", "En paral·lel"],
           [["Connexió", "Un darrere l'altre, pel mateix camí", "Cadascun en una branca diferent"], ["Intensitat", "La mateixa per tots els receptors", "Es reparteix entre les branques"], ["Tensió", "Es reparteix entre els receptors", "Tots reben la mateixa tensió (230 V a casa)"],
            ["Si un receptor es fon o es desconnecta", "S'apaguen tots (el circuit s'obre)", "Els altres continuen funcionant"], ["Dues bombetes iguals", "Fan menys llum que una de sola", "Cadascuna fa la llum normal (però es gasta el doble d'energia)"]], w=["28%", "36%", "36%"])
    b += P("La instal·lació d'una casa o de l'institut és <b>en paral·lel</b>: cada aparell funciona a 230 V i en podem apagar un sense que s'apaguin els altres. Com més aparells endollem alhora, més intensitat passa pel cable principal.")
    b += S(10, "Efectes del corrent i seguretat elèctrica")
    b += P("El corrent elèctric produeix efectes que aprofitem: <b>tèrmic</b> (efecte Joule: els conductors s'escalfen; estufes, assecadors, torradores), <b>lluminós</b> (bombetes), <b>magnètic</b> (motors, timbres) i <b>químic</b> (electròlisi, càrrega de bateries). L'efecte Joule també és la causa que els cables sobrecarregats s'escalfin i puguin provocar un incendi.")
    b += UL("Endolla i desendolla agafant l'endoll, mai el cable, i amb les mans seques. No facis servir aparells amb el cable malmès ni posis res als forats de l'endoll.",
            "No connectis molts aparells de molta potència a un sol endoll amb un lladre: la intensitat total pot escalfar massa els cables.",
            "El <b>magnetotèrmic</b> (PIA) talla el corrent si passa massa intensitat (sobrecàrrega o curtcircuit). El <b>diferencial</b> el talla si hi ha una fuita de corrent cap a terra, per exemple a través d'una persona: ens protegeix de les electrocucions. La <b>presa de terra</b> desvia les fuites cap al terra.")
    b += S(11, "Com es genera l'electricitat")
    b += P("La majoria de centrals fan girar una <b>turbina</b> connectada a un <b>alternador</b>. A l'alternador, un imant gira dins d'una bobina de fil de coure (o la bobina gira dins de l'imant) i hi genera corrent elèctric: és la <b>inducció electromagnètica</b>, descoberta per Michael Faraday el 1831. El que canvia d'una central a una altra és què fa girar la turbina. Després, uns <b>transformadors</b> eleven la tensió per transportar l'electricitat amb menys pèrdues per les línies d'alta tensió, i la tornen a baixar abans d'arribar a casa.")
    b += En.alternador_svg()
    b += EX("Cadenes de transformacions", "Hidràulica: potencial de l'aigua → cinètica → la turbina gira → l'alternador genera electricitat. Tèrmica i cicle combinat: química del gas → tèrmica (vapor a pressió) → cinètica → elèctrica. Nuclear: nuclear → tèrmica → cinètica → elèctrica. Eòlica: cinètica del vent → elèctrica. Fotovoltaica: radiant → elèctrica directament, sense turbina.")
    b += S(12, "Les fonts d'energia")
    b += T(["Renovables", "No renovables"], [["Es regeneren de manera natural al ritme que les fem servir: hidràulica, eòlica, solar (fotovoltaica i tèrmica), biomassa, geotèrmica, mareomotriu.", "Se n'esgoten les reserves, perquè es van formar en milions d'anys: petroli, carbó i gas natural (combustibles fòssils) i urani (nuclear)."],
            ["Avantatges: no s'esgoten, gairebé no emeten CO₂ en funcionar i són autòctones. Inconvenients: depenen del temps (sol, vent, pluja), ocupen territori i tenen impacte en el paisatge i en la fauna, i cal emmagatzemar l'energia (bateries, embassaments).", "Avantatges: produeixen quan cal i de manera constant. Inconvenients: s'esgoten, els combustibles fòssils emeten CO₂ (canvi climàtic) i contaminants de l'aire, i la nuclear genera residus radioactius de llarga durada."]])
    b += figs.fig(T2.fonts_energia(), "Algunes fonts d'energia per generar electricitat.", "160mm")
    b += P("Molta de l'energia que fem servir ve, en el fons, del Sol: el vent (escalfament desigual de l'aire), el cicle de l'aigua (hidràulica), la biomassa (fotosíntesi) i fins i tot els combustibles fòssils (restes d'éssers vius de fa milions d'anys).",
           "A Catalunya, l'any 2024 les renovables van generar el 19,1 % de l'electricitat, segons Red Eléctrica, i la nuclear va ser la primera font. Catalunya consumeix més electricitat de la que genera i n'importa d'altres territoris.",
           "La millor energia és la que no es gasta. Un pla d'estalvi combina <b>hàbits sostenibles</b> (apagar llums i aparells, aprofitar la llum natural), <b>eficiència</b> (LED, electrodomèstics de classe A, bon aïllament) i <b>generació renovable</b> (plaques solars, comunitats energètiques), amb la participació de tota la comunitat.")
    b += TIP("La ciència la fan persones", "Mária Telkes (1900–1995) va dissenyar la Dover Sun House (1948), una de les primeres cases escalfades amb energia solar: una sal (el sulfat de sodi) es fonia de dia absorbint l'energia del Sol i, en solidificar-se de nit, la desprenia. La premsa l'anomenava «la reina del Sol», però el seu nom és poc conegut.")
    b += S(13, "La informació fiable")
    b += P("Per prendre decisions sobre l'energia cal informació fiable. Davant d'una font, pregunta't: <b>qui</b> ho diu (és un expert, una institució pública, una universitat?), <b>quan</b> ho diu (és actual?), <b>per què</b> ho diu (vol informar o vendre alguna cosa?) i <b>amb quines proves</b> (dona dades i referències que es puguin comprovar?). Contrasta la informació amb més d'una font i cita-les sempre: Autor o institució (any). <i>Títol</i>. Adreça web.")
    b += KW(("Energia", "capacitat de produir canvis; en J"), ("Energia cinètica i potencial", "½ m v² i m g h"), ("Conservació de l'energia", "no es crea ni es destrueix, es transforma"), ("Degradació", "part de l'energia es converteix en calor no aprofitable"),
            ("Rendiment", "energia útil / energia consumida"), ("Potència", "energia per unitat de temps; en W"), ("kWh", "unitat d'energia de les factures; 3,6 · 10⁶ J"),
            ("Llei d'Ohm", "V = I · R"), ("En paral·lel", "cada aparell en una branca, amb tota la tensió"), ("Inducció electromagnètica", "un imant que gira en una bobina genera corrent"))
    return b

FUNCS = {1: sda1, 2: sda2, 3: sda3, 4: sda4, 5: sda5, 6: sda6}
