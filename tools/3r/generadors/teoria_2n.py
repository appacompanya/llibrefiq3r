"""Contingut dels dossiers de teoria de 2n d'ESO. El fa servir gen_teoria_curs.py (CURS=2n)."""
import gen_teoria as GT
from gen_teoria import H, S, P, UL, OL, TIP, EX, F, T, TOC, KW
import figs
import teoria_figs as TF, teoria_figs2 as T2, teoria_figs3 as T3

def A(n): return GT.COL[n][1]
def DEF(t, h): return f'<div class="fbox" style="background:#fff"><b>{t}.</b> {h}</div>'
def FIG(svg, cap, w="150mm"): return figs.fig(svg, cap, w)

# ======================================================================== SdA 1
def sda1():
    a = A(1)
    b = H(1, "Com es mesura el món? El laboratori, les magnituds i les unitats, els canvis d'unitats i els nombres molt grans i molt petits.")
    b += TOC("La seguretat al laboratori", "El material de laboratori", "Magnituds i unitats", "El Sistema Internacional i els prefixos", "Els instruments de mesura",
             "Mesurar bé: repeticions i mitjana", "Canvis d'unitats amb factors de conversió", "Unitats de superfície i de volum", "La notació científica", "Com resoldre un problema")
    b += S(1, "La seguretat al laboratori")
    b += P("El laboratori és un lloc de treball segur si tothom en segueix les normes. La majoria d'accidents passen per presses, per distraccions o per no llegir les etiquetes. Abans de començar una pràctica cal saber <b>què farem</b>, <b>amb quins productes</b> i <b>quins perills</b> tenen.")
    b += UL("Porta <b>bata</b> i <b>ulleres de seguretat</b> quan ho indiqui el professor, i els cabells recollits.",
            "<b>No mengis ni beguis</b> al laboratori i no tastis mai cap producte. Per olorar, apropa el vapor amb la mà, sense posar-hi el nas a sobre.",
            "<b>Llegeix l'etiqueta</b> abans de fer servir un producte i torna'l a tapar després.",
            "Treballa amb <b>ordre</b>: la taula neta, els productes lluny de la vora i el material que no fas servir, guardat.",
            "Si hi ha un accident (un tall, una cremada, un producte que esquitxa), <b>avisa el professor de seguida</b>. Si un producte toca la pell o els ulls, renta amb molta aigua.",
            "Llença els residus on t'indiquin: no tot va a l'aigüera.")
    b += P("Les etiquetes dels productes perillosos porten <b>pictogrames de perill</b>: un rombe amb el marc vermell i un dibuix negre. També hi ha una <b>paraula d'advertència</b>: <b>Perill</b> (per als perills greus) o <b>Atenció</b> (per als menys greus), i unes frases que expliquen el perill i com evitar-lo. Molts productes de casa (lleixiu, desembussadors, esprais) també en porten.")
    b += figs.picto_table(cols=3, size="11mm")
    b += S(2, "El material de laboratori")
    b += P("Cada estri té una funció. Per <b>mesurar volums</b> amb exactitud fem servir la proveta, la pipeta o la bureta; el vas de precipitats i l'erlenmeyer tenen marques, però només són orientatives. Per <b>mesurar masses</b> fem servir la balança.")
    b += FIG(T3.material_lab(a), "Material bàsic del laboratori i per a què serveix.", "165mm")
    b += P("Per llegir el volum d'un líquid en una proveta ens fixem en el <b>menisc</b>, la corba que fa la superfície del líquid. Llegim la part de baix del menisc, amb els ulls a la mateixa altura; si mirem des de dalt o des de baix, cometem un <b>error de paral·laxi</b>.")
    b += FIG(TF.proveta_menisc(), "Com es llegeix una proveta: els ulls a l'altura de la part de baix del menisc.", "120mm")
    b += P("Per mesurar el volum d'un sòlid irregular, com una pedra, fem servir el <b>mètode del desplaçament</b>: posem aigua en una proveta, n'anotem el volum, hi submergim la pedra i tornem a llegir. El volum de la pedra és la diferència entre les dues lectures.")
    b += FIG(TF.desplacament(), "El volum de la pedra és el que puja l'aigua.", "120mm")
    b += S(3, "Magnituds i unitats")
    b += P("Una <b>magnitud</b> és una propietat que es pot <b>mesurar</b>: la longitud, la massa, el temps, la temperatura, el volum… <b>Mesurar</b> és comparar una magnitud amb una quantitat de referència de la mateixa magnitud, que anomenem <b>unitat</b>. El resultat d'una mesura sempre té un <b>nombre</b> i una <b>unitat</b>: dir que l'aula fa «8» no vol dir res; dir que fa 8 m, sí.",
           "La bellesa, la simpatia o la por <b>no</b> són magnituds, perquè no hi ha cap unitat amb què comparar-les ni cap instrument que les mesuri.")
    b += S(4, "El Sistema Internacional i els prefixos")
    b += P("Fa segles, cada país (i fins i tot cada poble) tenia les seves unitats: pams, canes, lliures, quarteres… Això feia molt difícil comerciar i compartir resultats. Per entendre'ns, avui la ciència fa servir el <b>Sistema Internacional d'unitats (SI)</b>. Algunes magnituds són <b>fonamentals</b> (es defineixen per si mateixes) i les altres són <b>derivades</b> (es calculen a partir de les fonamentals).")
    b += T(["Magnitud", "Tipus", "Unitat del SI", "Altres unitats habituals", "Instrument"],
           [["Longitud", "fonamental", "metre (m)", "km, cm, mm", "regle, cinta mètrica"], ["Massa", "fonamental", "quilogram (kg)", "g, mg, t", "balança"],
            ["Temps", "fonamental", "segon (s)", "min, h, dia", "cronòmetre"], ["Temperatura", "fonamental", "kelvin (K)", "grau Celsius (°C)", "termòmetre"],
            ["Superfície", "derivada", "metre quadrat (m²)", "cm², km², ha", "es calcula"], ["Volum", "derivada", "metre cúbic (m³)", "L, mL, cm³", "proveta, pipeta"],
            ["Velocitat", "derivada", "metre per segon (m/s)", "km/h", "es calcula"]], w=["16%", "14%", "22%", "24%", "24%"])
    b += P("Per no haver d'escriure nombres enormes o diminuts, afegim <b>prefixos</b> davant de la unitat. Cada prefix és una potència de 10:")
    b += T(["Prefix", "Símbol", "Equival a", "Exemple"],
           [["kilo", "k", "1 000", "1 km = 1 000 m"], ["hecto", "h", "100", "1 hm = 100 m"], ["deca", "da", "10", "1 dam = 10 m"], ["(unitat)", "", "1", "1 m"],
            ["deci", "d", "0,1", "1 dm = 0,1 m"], ["centi", "c", "0,01", "1 cm = 0,01 m"], ["mil·li", "m", "0,001", "1 mm = 0,001 m"]])
    b += FIG(T3.escala_longitud(a), "L'escala de les unitats de longitud: cada salt val 10.", "155mm")
    b += S(5, "Els instruments de mesura")
    b += P("Tot instrument té dues característiques importants:")
    b += UL("La <b>sensibilitat</b> (o resolució): la quantitat més petita que pot mesurar. En un regle mil·limetrat és 1 mm; en una proveta amb ratlles cada 2 mL, és 2 mL; en una balança que mostra 12,40 g, és 0,01 g.",
            "L'<b>abast</b>: el valor més gran que pot mesurar. Una proveta de 100 mL no serveix per mesurar 250 mL d'una sola vegada.")
    b += P("Triem l'instrument segons el que vulguem mesurar: per mesurar el pati, una cinta mètrica; per mesurar el gruix d'un full, millor un peu de rei o mesurar 100 fulls junts i dividir.")
    b += S(6, "Mesurar bé: repeticions i mitjana")
    b += P("Cap mesura no és perfecta: sempre hi ha petites diferències per l'instrument, per la persona que mesura o per com es fa. Per això els científics <b>repeteixen</b> les mesures (com a mínim tres vegades) i en calculen la <b>mitjana</b>. Si una mesura és molt diferent de les altres, segurament hi ha hagut un error i la descartem.")
    b += F('mitjana = <span class="fr"><span>suma de totes les mesures</span><span>nombre de mesures</span></span>')
    b += EX("Exemple", "Mesurem la llargada de l'aula tres vegades: 8,12 m, 8,08 m i 8,10 m. La mitjana és (8,12 + 8,08 + 8,10) / 3 = 24,30 / 3 = 8,10 m. El resultat no pot tenir més decimals que les mesures.")
    b += TIP("Mesurar el que és molt petit", "Si una gota és massa petita per mesurar-la, en comptem moltes: si 20 gotes fan 1 mL, cada gota fa 1 / 20 = 0,05 mL. El mateix truc serveix per al gruix d'un full o la massa d'un gra d'arròs.")
    b += S(7, "Canvis d'unitats amb factors de conversió")
    b += P("Sovint cal canviar d'unitat: passar els minuts a hores, els grams a quilograms, els km/h a m/s… Ho fem amb un <b>factor de conversió</b>: una fracció que val 1 perquè a dalt i a baix hi ha la mateixa quantitat escrita amb unitats diferents. Per exemple, (1 000 m / 1 km) val 1, perquè 1 000 m i 1 km són el mateix.")
    b += OL("Escriu la dada amb la seva unitat.", "Escriu al costat una fracció amb l'equivalència entre la unitat que tens i la que vols.", "Posa la unitat que vols <b>treure a baix</b> i la que vols <b>obtenir a dalt</b>.", "Simplifica la unitat que es repeteix a dalt i a baix i fes l'operació.")
    b += EX("Exemple 1", "Passa 2,5 km a m: \\( 2{,}5\\ \\mathrm{km} \\cdot \\dfrac{1000\\ \\mathrm{m}}{1\\ \\mathrm{km}} = 2500\\ \\mathrm{m} \\).")
    b += EX("Exemple 2", "Passa 450 g a kg: \\( 450\\ \\mathrm{g} \\cdot \\dfrac{1\\ \\mathrm{kg}}{1000\\ \\mathrm{g}} = 0{,}45\\ \\mathrm{kg} \\).")
    b += EX("Exemple 3 (factors encadenats)", "Quants segons té un dia? \\( 1\\ \\mathrm{dia} \\cdot \\dfrac{24\\ \\mathrm{h}}{1\\ \\mathrm{dia}} \\cdot \\dfrac{60\\ \\mathrm{min}}{1\\ \\mathrm{h}} \\cdot \\dfrac{60\\ \\mathrm{s}}{1\\ \\mathrm{min}} = 86400\\ \\mathrm{s} \\).")
    b += EX("Exemple 4 (unitats compostes)", "Passa 90 km/h a m/s. Cal un factor per als km i un altre per a les hores: \\( 90\\ \\dfrac{\\mathrm{km}}{\\mathrm{h}} \\cdot \\dfrac{1000\\ \\mathrm{m}}{1\\ \\mathrm{km}} \\cdot \\dfrac{1\\ \\mathrm{h}}{3600\\ \\mathrm{s}} = 25\\ \\dfrac{\\mathrm{m}}{\\mathrm{s}} \\).")
    b += TIP("Comprova el resultat", "Si passes a una unitat més petita, el nombre ha de sortir més gran (2,5 km → 2 500 m), i si passes a una unitat més gran, més petit (450 g → 0,45 kg). Si no és així, has posat el factor al revés.")
    b += S(8, "Unitats de superfície i de volum")
    b += P("La <b>superfície</b> té dues dimensions (llargada i amplada). Un quadrat d'1 m de costat té 100 cm · 100 cm = 10 000 cm². Per això, a les unitats de superfície, cada salt de l'escala val <b>100</b>: 1 m² = 100 dm² = 10 000 cm².",
           "El <b>volum</b> té tres dimensions (llargada, amplada i altura). Un cub d'1 m de costat té 10 · 10 · 10 = 1 000 dm³. A les unitats de volum, cada salt val <b>1 000</b>: 1 m³ = 1 000 dm³ = 1 000 000 cm³.")
    b += F("Superfície d'un rectangle: S = llargada · amplada", "Volum d'un prisma (una caixa, una aula, una piscina): V = llargada · amplada · altura")
    b += P("Els líquids es mesuren sovint en <b>litres</b>. La relació entre el litre i les unitats de volum és molt important:")
    b += FIG(T3.litre_dm3(a), "En un cub d'1 dm de costat hi cap exactament 1 litre.", "150mm")
    b += EX("Exemple", "Una piscina fa 25 m de llarg, 10 m d'ample i 2 m de fondària. V = 25 · 10 · 2 = 500 m³. En litres: \\( 500\\ \\mathrm{m^3} \\cdot \\dfrac{1000\\ \\mathrm{L}}{1\\ \\mathrm{m^3}} = 500000\\ \\mathrm{L} \\).")
    b += S(9, "La notació científica")
    b += P("Alguns nombres són tan grans o tan petits que costa escriure'ls i llegir-los: la distància a la Lluna, el nombre de gotes d'aigua d'una piscina, la mida d'un bacteri… Per escriure'ls fem servir la <b>notació científica</b>: un nombre entre 1 i 10 multiplicat per una potència de 10.")
    b += F("a · 10ⁿ    amb 1 ≤ a < 10", note="n positiu: nombre gran (movem la coma cap a l'esquerra) · n negatiu: nombre petit (movem la coma cap a la dreta)")
    b += T(["Nombre", "Notació científica", "Què és"],
           [["384 000 000 m", "3,84 · 10⁸ m", "distància de la Terra a la Lluna"], ["7 900 000 000", "7,9 · 10⁹", "persones al món (aprox.)"],
            ["0,000 002 m", "2 · 10⁻⁶ m", "mida d'un bacteri"], ["0,05 mL", "5 · 10⁻² mL", "volum d'una gota d'aigua"]])
    b += P("Per <b>passar a notació científica</b> comptem quantes posicions movem la coma fins que queda una sola xifra (diferent de zero) davant de la coma: aquest és l'exponent. Per <b>multiplicar</b> dos nombres en notació científica, multipliquem els nombres i <b>sumem</b> els exponents; per <b>dividir</b>, dividim els nombres i <b>restem</b> els exponents.")
    b += EX("Exemple", "Quantes gotes hi ha en 1 m³ d'aigua si cada gota fa 0,05 mL? 1 m³ = 10⁶ mL. Gotes = 10⁶ / (5 · 10⁻²) = 0,2 · 10⁸ = 2 · 10⁷ gotes: vint milions de gotes.")
    b += S(10, "Com resoldre un problema")
    b += P("A física i química resolem els problemes sempre amb el mateix ordre. Així no ens perdem i és fàcil trobar els errors:")
    b += OL("<b>Dades:</b> escriu les dades amb les unitats i el que et demanen.", "<b>Unitats:</b> passa-les totes a les mateixes unitats (sovint, les del SI).", "<b>Fórmula:</b> escriu la fórmula que relaciona les dades.",
            "<b>Càlcul:</b> substitueix i calcula.", "<b>Resultat:</b> escriu el resultat amb la unitat i pensa si té sentit (una aula no pot fer 3 000 m de llarg).")
    b += TIP("La ciència la fan persones", "El sistema mètric decimal va néixer a França el 1791. Per definir el metre, Pierre Méchain i Jean-Baptiste Delambre van mesurar el meridià de Dunkerque a Barcelona; Méchain va fer algunes de les mesures des del castell de Montjuïc.")
    b += KW(("Magnitud", "propietat que es pot mesurar"), ("Unitat", "quantitat de referència amb què comparem en mesurar"), ("SI", "Sistema Internacional d'unitats"),
            ("Sensibilitat", "quantitat més petita que pot mesurar un instrument"), ("Menisc", "corba de la superfície d'un líquid en un tub"), ("Mitjana", "suma de les mesures dividida pel nombre de mesures"),
            ("Factor de conversió", "fracció que val 1 per canviar d'unitat"), ("Litre", "volum d'1 dm³"), ("Notació científica", "a · 10ⁿ, amb a entre 1 i 10"), ("Pictograma de perill", "rombe vermell que avisa d'un perill"))
    return b

# ======================================================================== SdA 2
def sda2():
    a = A(2)
    b = H(2, "Per què uns líquids suren damunt dels altres? La massa, el volum i la densitat, la flotació i les persones que hi ha darrere de la ciència.")
    b += TOC("Què és la matèria", "La massa i com es mesura", "El volum i com es mesura", "Propietats generals i característiques", "La densitat",
             "Calcular masses i volums", "Sura o s'enfonsa?", "La densitat mitjana: vaixells i icebergs", "El densímetre", "Arquimedes, Hipàtia i la ciència")
    b += S(1, "Què és la matèria")
    b += P("La <b>matèria</b> és tot allò que té massa i ocupa un lloc a l'espai, és a dir, té volum. L'aigua, l'aire, una pedra o el nostre cos són matèria. La llum, el so o les idees no ho són.",
           "Cada tipus de matèria és un <b>material</b> o una <b>substància</b>: l'aigua, l'oli, el ferro, el suro… Per saber quina substància és una mostra, n'estudiem les propietats.")
    b += S(2, "La massa i com es mesura")
    b += P("La <b>massa</b> és la quantitat de matèria que té un cos. La seva unitat al SI és el <b>quilogram (kg)</b>, però al laboratori sovint fem servir el gram (g): 1 kg = 1 000 g. Es mesura amb una <b>balança</b>.",
           "La massa no és el mateix que el pes: la massa d'un astronauta és la mateixa a la Terra que a la Lluna, però a la Lluna pesa menys perquè la Lluna l'atreu menys.")
    b += TIP("La tara", "Per mesurar la massa d'un líquid, primer pesem el recipient buit (la <b>tara</b>), després el pesem amb el líquid, i restem: massa del líquid = massa del recipient ple − massa del recipient buit. Moltes balances tenen un botó de tara que posa la pantalla a zero amb el recipient a sobre.")
    b += S(3, "El volum i com es mesura")
    b += P("El <b>volum</b> és l'espai que ocupa un cos. La unitat del SI és el metre cúbic (m³), però per als líquids fem servir el litre (L) i el mil·lilitre (mL). Recorda: <b>1 L = 1 dm³</b> i <b>1 mL = 1 cm³</b>.")
    b += UL("<b>Líquids:</b> amb una proveta, una pipeta o una bureta (llegint la part de baix del menisc).",
            "<b>Sòlids regulars</b> (cubs, prismes, cilindres): mesurem les dimensions i calculem el volum. Un prisma: V = llargada · amplada · altura.",
            "<b>Sòlids irregulars:</b> pel mètode del desplaçament d'aigua en una proveta. El volum del sòlid és el volum final menys el volum inicial.")
    b += S(4, "Propietats generals i propietats característiques")
    b += P("Les <b>propietats generals</b> les té qualsevol tros de matèria i <b>no serveixen per identificar-la</b>: la massa, el volum, la temperatura. Un quilo de ferro i un quilo de palla tenen la mateixa massa, però no són la mateixa substància.",
           "Les <b>propietats característiques</b> tenen un valor propi per a cada substància i <b>sí que serveixen per identificar-la</b>: la densitat, la temperatura de fusió i d'ebullició, el color, la solubilitat, la conductivitat… No depenen de la quantitat de substància que tinguem.")
    b += S(5, "La densitat")
    b += P("Si al laboratori mesurem la massa de 20, 40, 60 i 80 mL d'un líquid, veiem que en doblar el volum es dobla la massa: massa i volum són <b>directament proporcionals</b>. Si dividim la massa entre el volum, sempre obtenim el mateix nombre per a un mateix líquid, però un nombre diferent per a cada líquid. Aquest nombre és la <b>densitat</b>.")
    b += FIG(T3.grafica_massa_volum(a), "Massa i volum de dos líquids: cada líquid fa una recta, i el pendent és la densitat.", "155mm")
    b += DEF("Densitat", "és la massa que té cada unitat de volum d'una substància. Ens diu com d'«atapeïda» està la matèria. És una propietat característica.")
    b += F("d = m / V", note="m: massa (g o kg) · V: volum (cm³, mL, m³…) · d: densitat (g/cm³ = g/mL, o kg/m³ al SI) · 1 g/cm³ = 1 000 kg/m³")
    b += P("Per exemple, la densitat de l'aigua és 1 g/cm³: cada centímetre cúbic d'aigua té una massa d'1 g. La del ferro és 7,87 g/cm³: un centímetre cúbic de ferro té una massa de gairebé 8 g.")
    b += T(["Substància", "d (g/cm³)", "Substància", "d (g/cm³)"],
           [["Aire", "0,0012", "Aigua de mar", "1,03"], ["Suro", "0,24", "Glicerina", "1,26"], ["Alcohol (etanol)", "0,79", "Alumini", "2,70"],
            ["Oli d'oliva", "0,92", "Ferro", "7,87"], ["Gel", "0,92", "Plom", "11,3"], ["Aigua", "1,00", "Or", "19,3"]])
    b += TIP("La densitat i la temperatura", "Quan un material s'escalfa, es dilata: la massa és la mateixa, però el volum augmenta una mica, i per tant la densitat disminueix. Per això les taules indiquen sempre la temperatura (normalment 20 °C).")
    b += S(6, "Calcular masses i volums amb la densitat")
    b += P("De la fórmula de la densitat podem aïllar la massa o el volum:")
    b += F("m = d · V", "V = m / d")
    b += EX("Exemple 1 · Identificar una substància", "Un anell té una massa de 9,65 g i un volum de 0,5 cm³. d = 9,65 / 0,5 = 19,3 g/cm³. Mirant la taula, pot ser d'or.")
    b += EX("Exemple 2 · Calcular una massa", "Quina massa té una garrafa de 5 L d'oli d'oliva? Passem el volum: 5 L = 5 000 mL. m = d · V = 0,92 · 5 000 = 4 600 g = 4,6 kg (sense comptar el plàstic).")
    b += EX("Exemple 3 · Calcular un volum", "Quin volum ocupen 500 g de gel? V = m / d = 500 / 0,92 ≈ 543 cm³. La mateixa massa d'aigua líquida ocuparia 500 cm³: en congelar-se, l'aigua augmenta de volum. Per això una ampolla plena d'aigua es trenca al congelador.")
    b += EX("Exemple 4 · L'aire de l'aula", "Una aula fa 8 m · 6 m · 3 m = 144 m³. L'aire té una densitat d'1,2 kg/m³: m = 1,2 · 144 ≈ 173 kg d'aire. L'aire no pesa gaire, però en tenim molt!")
    b += S(7, "Sura o s'enfonsa?")
    b += P("Un objecte <b>sura</b> en un líquid si la seva densitat és <b>més petita</b> que la del líquid, i s'<b>enfonsa</b> si és <b>més gran</b>. Si les densitats són iguals, l'objecte queda «aturat» a mitja altura, sense pujar ni baixar.",
           "Quan un objecte sura, una part queda submergida i una part fora. Com més s'acosta la seva densitat a la del líquid, més part queda submergida: el suro (0,24 g/cm³) gairebé no s'enfonsa, mentre que el gel (0,92 g/cm³) queda submergit en un 92 % aproximadament.")
    b += FIG(T3.sura_enfonsa(a), "Objectes de densitats diferents en aigua.", "160mm")
    b += P("El mateix passa amb els <b>líquids que no es barregen</b>: es col·loquen en capes, amb el més dens a baix i el menys dens a dalt. Així es pot fer una torre de colors dins d'un got: mel, glicerina, aigua amb colorant, oli i alcohol.")
    b += FIG(TF.columna_densitat(), "Torre de líquids: de més dens (a baix) a menys dens (a dalt).", "130mm")
    b += P("Si dissolem sal o sucre a l'aigua, la densitat augmenta. Per això és més fàcil surar al mar que a la piscina, i encara més al mar Mort, que té tanta sal que la seva densitat és d'uns 1,24 g/cm³. Amb aigua amb diferents quantitats de sucre i colorants, podem fer capes de colors.")
    b += S(8, "La densitat mitjana: vaixells i icebergs")
    b += P("Com pot surar un vaixell d'acer, si l'acer és gairebé 8 vegades més dens que l'aigua? Perquè el que compta és la <b>densitat mitjana</b> de tot l'objecte: la massa total dividida pel volum total, comptant-hi l'aire de dins. Un vaixell és buit per dins i té un volum molt gran; la seva densitat mitjana és més petita que la de l'aigua i sura. Si fa un forat i entra aigua, la densitat mitjana augmenta i s'enfonsa.",
           "Passa el mateix amb una barca de plastilina: una bola de plastilina s'enfonsa, però si la modelem en forma de barca, amb parets i aire a dins, sura.",
           "Els <b>icebergs</b> suren perquè el gel és menys dens que l'aigua de mar, però com que les densitats són semblants (0,92 i 1,03), gairebé el 90 % de l'iceberg queda sota l'aigua. D'aquí ve l'expressió «només és la punta de l'iceberg».")
    b += S(9, "El densímetre")
    b += P("El <b>densímetre</b> és un tub de vidre tancat, amb un llast a baix i una escala a dalt. Es posa dins del líquid i sura: com més dens és el líquid, menys s'enfonsa el densímetre. La densitat es llegeix a l'escala, al nivell de la superfície del líquid. Serveix per controlar la qualitat de la llet, del vi, de l'oli o de l'àcid de les bateries.")
    b += FIG(T3.densimetre(a), "El densímetre s'enfonsa menys com més dens és el líquid. Un ou sura en aigua amb molta sal.", "160mm")
    b += S(10, "Arquimedes, Hipàtia i la ciència")
    b += P("Segons la llegenda, el rei Hieró de Siracusa (segle III aC) va demanar a <b>Arquimedes</b> si la seva corona era d'or pur o si l'orfebre l'havia barrejat amb plata. Arquimedes no la podia fondre ni tallar. Mentre es banyava, va veure que l'aigua pujava quan ell entrava a la banyera i va pensar que podia mesurar el volum de la corona submergint-la. Coneixent la massa i el volum, en podia calcular la densitat i comparar-la amb la de l'or. La història de sortir corrent pel carrer cridant «Eureka!» és, probablement, una llegenda; el mètode, en canvi, funciona.")
    b += EX("Exemple", "Una corona de 1 000 g desplaça 60 cm³ d'aigua. d = 1 000 / 60 ≈ 16,7 g/cm³. L'or pur té 19,3 g/cm³: la corona no és d'or pur, està barrejada amb un metall menys dens (com la plata, 10,5 g/cm³).")
    b += P("<b>Hipàtia d'Alexandria</b> (segle IV–V) va ser matemàtica, astrònoma i filòsofa, i dirigia una escola a Alexandria. En una carta, el seu deixeble Sinesi li demana com construir un <b>hidroscopi</b>, un instrument que s'ha identificat amb el densímetre. Durant segles, moltes dones científiques han estat oblidades o se n'ha atribuït la feina a homes: és un <b>biaix de gènere</b> que avui intentem corregir fent conèixer la seva feina.")
    b += TIP("La ciència és col·lectiva", "Els descobriments rarament els fa una sola persona: es basen en el que han fet altres, es comproven i es discuteixen. Separar els fets de les llegendes forma part de pensar com un científic.")
    b += KW(("Matèria", "tot el que té massa i volum"), ("Massa", "quantitat de matèria; en kg"), ("Volum", "espai que ocupa un cos; en m³ o L"), ("Tara", "massa del recipient buit"),
            ("Propietat característica", "permet identificar una substància"), ("Densitat", "massa per unitat de volum: d = m / V"), ("Directament proporcional", "si una es dobla, l'altra també"),
            ("Densitat mitjana", "<span class="fr"><span>massa total</span><span>volum total</span></span> d'un objecte"), ("Densímetre", "instrument que mesura la densitat d'un líquid"), ("Biaix de gènere", "oblidar o infravalorar la feina de les dones"))
    return b

# ======================================================================== SdA 3
def sda3():
    a = A(3)
    b = H(3, "Per què la pilota bota menys quan fa fred? Els estats de la matèria, el model de partícules, els canvis d'estat i les lleis dels gasos.")
    b += TOC("Els tres estats de la matèria", "El model de partícules", "Els canvis d'estat", "Evaporació i ebullició", "La corba d'escalfament",
             "La temperatura i l'escala Kelvin", "La pressió dels gasos", "La llei de Boyle-Mariotte", "Les lleis de Charles i de Gay-Lussac", "Com resoldre problemes de gasos")
    b += S(1, "Els tres estats de la matèria")
    b += P("A la natura trobem la matèria en tres estats principals: <b>sòlid</b>, <b>líquid</b> i <b>gas</b>. L'aigua els té tots tres: gel, aigua líquida i vapor d'aigua.")
    b += T(["", "Sòlid", "Líquid", "Gas"],
           [["Forma", "pròpia, fixa", "la del recipient", "la del recipient"], ["Volum", "fix", "fix", "variable: ocupa tot el recipient"],
            ["Es pot comprimir?", "no", "gairebé no", "sí, molt"], ["Flueix?", "no", "sí", "sí"], ["Exemples", "gel, ferro, sal", "aigua, oli, alcohol", "aire, vapor, butà"]])
    b += S(2, "El model de partícules")
    b += P("Per explicar per què els estats es comporten així, la ciència fa servir el <b>model de partícules</b> (o teoria cineticomolecular). Un <b>model</b> és una representació simplificada que ens ajuda a entendre i a predir el que passa. Diu:")
    b += OL("La matèria està formada per <b>partícules</b> molt petites, que no podem veure.", "Entre les partícules <b>no hi ha res</b>: hi ha buit.", "Les partícules estan en <b>moviment</b> constant. Com més alta és la temperatura, més de pressa es mouen.",
            "Entre les partícules hi ha <b>forces d'atracció</b>, més fortes com més a prop estan.")
    b += FIG(T2.estats_particules(a), "Els tres estats segons el model de partícules.", "150mm")
    b += UL("<b>Sòlid:</b> partícules molt juntes i ordenades, que només vibren al seu lloc. Per això té forma i volum fixos.",
            "<b>Líquid:</b> partícules juntes però desordenades, que llisquen les unes sobre les altres. Té volum fix, però agafa la forma del recipient.",
            "<b>Gas:</b> partícules molt separades, amb molt de buit entre elles, que es mouen molt de pressa i en totes direccions. Per això ocupa tot el recipient i es pot comprimir: les partícules s'apropen.")
    b += P("El model també explica la <b>difusió</b>: una gota de colorant es reparteix sola per l'aigua perquè les partícules es mouen i es barregen. En aigua calenta es reparteix més de pressa, perquè les partícules es mouen més ràpid.")
    b += S(3, "Els canvis d'estat")
    b += P("Si escalfem o refredem una substància, pot canviar d'estat. En els canvis d'estat la substància <b>continua sent la mateixa</b> (el gel, l'aigua i el vapor són aigua): són <b>canvis físics</b>.")
    b += FIG(T3.canvis_estat(a), "Els noms dels canvis d'estat.", "150mm")
    b += P("Quan escalfem, les partícules es mouen més i se separen; quan refredem, es mouen menys i s'apropen. Cada substància pura canvia d'estat a una temperatura fixa: la <b>temperatura de fusió</b> (de sòlid a líquid) i la <b>temperatura d'ebullició</b> (de líquid a gas). Són propietats característiques.")
    b += T(["Substància", "T de fusió (°C)", "T d'ebullició (°C)", "Estat a 20 °C"],
           [["Aigua", "0", "100", "líquid"], ["Alcohol (etanol)", "−114", "78", "líquid"], ["Oxigen", "−218", "−183", "gas"], ["Ferro", "1 538", "2 862", "sòlid"], ["Sal (clorur de sodi)", "801", "1 465", "sòlid"]])
    b += TIP("Com saber l'estat d'una substància", "Si la temperatura és més baixa que la de fusió, és sòlida; si està entre la de fusió i la d'ebullició, és líquida; si és més alta que la d'ebullició, és gas.")
    b += S(4, "Evaporació i ebullició")
    b += P("Hi ha dues maneres de passar de líquid a gas (vaporització):")
    b += UL("<b>Evaporació:</b> passa a <b>qualsevol temperatura</b> i només a la <b>superfície</b> del líquid. Les partícules més ràpides de la superfície s'escapen. Per això s'asseca la roba estesa o un toll. És més ràpida si fa calor, si fa vent o si el líquid està escampat.",
            "<b>Ebullició:</b> passa a una <b>temperatura fixa</b> (la d'ebullició) i a <b>tot el líquid</b>: es formen bombolles de vapor a dins que pugen i esclaten.")
    b += FIG(T2.evaporacio_ebullicio(a), "Evaporació (a la superfície) i ebullició (a tot el líquid).", "140mm")
    b += S(5, "La corba d'escalfament")
    b += P("Si escalfem gel i n'anotem la temperatura cada minut, obtenim una gràfica temperatura–temps anomenada <b>corba d'escalfament</b>. Té trams inclinats, on la temperatura puja, i <b>trams horitzontals</b>, on la temperatura no canvia encara que continuem escalfant: són els canvis d'estat.")
    b += FIG(T2.corba_escalfament(a), "Corba d'escalfament de l'aigua.", "140mm")
    b += P("Als trams horitzontals l'energia que donem no fa moure més de pressa les partícules, sinó que serveix per <b>separar-les</b> (trencar les atraccions entre elles). Quan tot el gel s'ha fos, la temperatura torna a pujar. La <b>corba de refredament</b> és igual però al revés, i té els trams horitzontals a les mateixes temperatures.",
           "Una <b>substància pura</b> té trams horitzontals ben definits. Una <b>mescla</b> (aigua amb sal, per exemple) no en té: canvia d'estat en un interval de temperatures. Així podem distingir una substància pura d'una mescla.")
    b += S(6, "La temperatura i l'escala Kelvin")
    b += P("La <b>temperatura</b> mesura com de ràpid es mouen, de mitjana, les partícules d'un cos. Fem servir dues escales:")
    b += UL("<b>Celsius (°C):</b> 0 °C és la temperatura de fusió del gel i 100 °C, la d'ebullició de l'aigua.",
            "<b>Kelvin (K):</b> és l'escala del SI. Comença al <b>zero absolut</b> (0 K = −273 °C), la temperatura més baixa possible, quan les partícules pràcticament no es mouen. No té temperatures negatives.")
    b += FIG(T3.escales_temperatura(a), "Les escales Celsius i Kelvin.", "150mm")
    b += F("T (K) = t (°C) + 273", note="Un augment d'1 °C és el mateix que un augment d'1 K.")
    b += EX("Exemples", "25 °C = 25 + 273 = 298 K · 0 °C = 273 K · 350 K = 350 − 273 = 77 °C.")
    b += S(7, "La pressió dels gasos")
    b += P("Les partícules d'un gas es mouen molt de pressa i xoquen contínuament contra les parets del recipient. Cada xoc fa una petita força; la suma de tots els xocs sobre cada unitat de superfície és la <b>pressió</b> del gas. La pressió augmenta si hi ha <b>més xocs</b> o si els xocs són <b>més forts</b>.")
    b += FIG(T3.pressio_pilota(a), "L'aire d'una pilota freda i d'una a temperatura ambient.", "145mm")
    b += P("Això explica el repte: a la nit, al pati, l'aire de la pilota es refreda. Les partícules es mouen més a poc a poc, xoquen menys i amb menys força contra la paret, i la pressió de dins baixa. La pilota queda més tova i bota menys.",
           "L'aire que ens envolta també fa pressió: és la <b>pressió atmosfèrica</b>. Les unitats de pressió més habituals són:")
    b += T(["Unitat", "Símbol", "Equivalència"], [["pascal (unitat del SI)", "Pa", "—"], ["atmosfera", "atm", "1 atm = 101 325 Pa"], ["mil·límetre de mercuri", "mmHg", "1 atm = 760 mmHg"], ["hectopascal (mapes del temps)", "hPa", "1 atm = 1 013 hPa"]])
    b += EX("Exemple", "Passa 1,5 atm a mmHg: \\( 1{,}5\\ \\mathrm{atm} \\cdot \\dfrac{760\\ \\mathrm{mmHg}}{1\\ \\mathrm{atm}} = 1140\\ \\mathrm{mmHg} \\).")
    b += S(8, "La llei de Boyle-Mariotte")
    b += P("Si tapem una xeringa amb aire i empenyem l'èmbol, el volum disminueix i notem que l'aire «empeny» cada vegada més: la pressió augmenta. Robert Boyle (1662) i Edme Mariotte (1676) van descobrir que, si la temperatura no canvia, la pressió i el volum d'un gas són <b>inversament proporcionals</b>: si el volum es redueix a la meitat, la pressió es dobla.")
    b += F("P₁ · V₁ = P₂ · V₂    (a temperatura constant)")
    b += FIG(T2.boyle_embol(a), "En reduir el volum, les partícules xoquen més sovint amb les parets: la pressió augmenta.", "130mm")
    b += P("Amb el model de partícules: si el volum és més petit, les partícules tenen menys espai i xoquen més sovint contra les parets.")
    b += EX("Exemple", "Una bombolla d'un submarinista té un volum de 2 cm³ a 3 atm. Quin volum tindrà a la superfície (1 atm)? V₂ = P₁ · V₁ / P₂ = 3 · 2 / 1 = 6 cm³. Per això els submarinistes no han d'aguantar mai la respiració quan pugen: l'aire dels pulmons s'expandiria.")
    b += S(9, "Les lleis de Charles i de Gay-Lussac")
    b += P("La temperatura també influeix en els gasos. A les lleis de gasos la temperatura s'ha d'expressar <b>sempre en kelvin</b>.")
    b += UL("<b>Llei de Charles</b> (a pressió constant): el volum és directament proporcional a la temperatura. Si un globus s'escalfa, s'infla; si el posem en aigua amb gel, es desinfla. V₁ / T₁ = V₂ / T₂.",
            "<b>Llei de Gay-Lussac</b> (a volum constant): la pressió és directament proporcional a la temperatura. Una olla tancada o un pneumàtic augmenten de pressió en escalfar-se; una pilota freda té menys pressió. P₁ / T₁ = P₂ / T₂.")
    b += FIG(T2.lleis_gasos(a), "Gràfiques de les tres lleis dels gasos.", "155mm")
    b += EX("Exemple · Charles", "Un globus té 3,0 L a 27 °C. Quin volum tindrà a 87 °C? T₁ = 300 K, T₂ = 360 K. V₂ = V₁ · T₂ / T₁ = 3,0 · 360 / 300 = 3,6 L.")
    b += EX("Exemple · Gay-Lussac (el repte)", "Una pilota té una pressió d'1,60 atm a 25 °C (298 K). A la nit baixa a 5 °C (278 K): P₂ = P₁ · T₂ / T₁ = 1,60 · 278 / 298 ≈ 1,49 atm. Ha perdut pressió i bota menys.")
    b += TIP("Compte amb els kelvin", "Si fem el càlcul en °C, el resultat és absurd: passar de 10 °C a 20 °C no dobla la pressió! En kelvin, de 283 K a 293 K, només augmenta un 3,5 %.")
    b += S(10, "Com resoldre problemes de gasos (mètode 1-2-4)")
    b += OL("<b>Identifica</b> què es manté constant: la temperatura (Boyle), la pressió (Charles) o el volum (Gay-Lussac).", "<b>Escriu</b> les dades de l'estat 1 i de l'estat 2, i la incògnita.",
            "<b>Passa</b> les temperatures a kelvin i comprova que les pressions i els volums estan en les mateixes unitats als dos estats.", "<b>Aïlla</b> la incògnita, calcula i comprova si el resultat té sentit (si escalfem, el volum o la pressió han d'augmentar).")
    b += TIP("La ciència la fan persones", "Joseph-Louis Gay-Lussac (1778–1850) va pujar el 1804 en un globus d'hidrogen fins a 7 000 m per recollir mostres d'aire i mesurar-ne la temperatura i la pressió: va comprovar que la composició de l'aire és la mateixa a dalt que a baix.")
    b += KW(("Model de partícules", "la matèria és feta de partícules en moviment amb buit entre elles"), ("Fusió", "pas de sòlid a líquid"), ("Vaporització", "pas de líquid a gas (evaporació o ebullició)"),
            ("Condensació", "pas de gas a líquid"), ("Sublimació", "pas directe de sòlid a gas"), ("Temperatura d'ebullició", "temperatura fixa a què bull una substància pura"),
            ("Zero absolut", "0 K = −273 °C"), ("Pressió", "efecte dels xocs de les partícules sobre les parets"), ("Inversament proporcional", "si una es dobla, l'altra es fa la meitat"), ("Llei de Gay-Lussac", "a volum constant, P / T és constant"))
    return b

# ======================================================================== SdA 4
def sda4():
    a = A(4)
    b = H(4, "Podem fer potable l'aigua d'un riu? Les substàncies pures i les mescles, les dissolucions, la concentració, la solubilitat i les tècniques de separació.")
    b += TOC("Substàncies pures i mescles", "Elements i compostos", "Mescles homogènies i heterogènies", "Les dissolucions", "La concentració", "Preparar i diluir dissolucions",
             "La solubilitat", "Tècniques de separació", "L'aigua potable: de l'embassament a l'aixeta", "Cuidem l'aigua")
    b += S(1, "Substàncies pures i mescles")
    b += P("Una <b>substància pura</b> està formada per un sol tipus de partícules. Té una composició fixa i unes propietats característiques constants: l'aigua destil·lada sempre bull a 100 °C (a nivell del mar) i té una densitat d'1 g/cm³.",
           "Una <b>mescla</b> està formada per dues o més substàncies que no han reaccionat entre elles. La seva composició pot variar (més o menys sal a l'aigua) i les seves propietats depenen de la composició. La majoria dels materials que ens envolten són mescles: l'aire, l'aigua de l'aixeta, la llet, el granit…")
    b += FIG(TF.particules_materia(), "Model de partícules: element, compost i mescles.", "150mm")
    b += TIP("L'aigua de l'aixeta no és pura", "L'aigua que bevem és una mescla: porta sals minerals dissoltes (calci, magnesi, sodi…) i una mica de clor que la desinfecta. «Aigua pura» en el llenguatge de la publicitat vol dir «neta» o «sense contaminants», no «substància pura».")
    b += S(2, "Elements i compostos")
    b += UL("Un <b>element</b> és una substància pura formada per un sol tipus d'àtom: el ferro (Fe), l'oxigen (O₂), l'or (Au). No es pot descompondre en substàncies més simples.",
            "Un <b>compost</b> és una substància pura formada per diversos tipus d'àtoms units en una proporció fixa: l'aigua (H₂O), el clorur de sodi o sal de cuina (NaCl), el diòxid de carboni (CO₂). Es pot descompondre en elements amb una reacció química.")
    b += S(3, "Mescles homogènies i heterogènies")
    b += UL("<b>Mescla heterogènia:</b> se'n distingeixen els components a simple vista o amb una lupa (aigua amb sorra, amanida, granit, aigua amb oli). No té la mateixa composició a tot arreu.",
            "<b>Mescla homogènia o dissolució:</b> no se'n distingeixen els components, ni amb un microscopi (aigua amb sal, aire, vinagre, bronze). Té la mateixa composició a tot arreu.")
    b += P("Hi ha mescles que semblen homogènies però no ho són: la llet o la maionesa, vistes al microscopi, tenen gotetes de greix escampades. S'anomenen <b>col·loides</b>.")
    b += S(4, "Les dissolucions")
    b += P("Una <b>dissolució</b> és una mescla homogènia. Té dos tipus de components:")
    b += UL("El <b>dissolvent</b>: el component que hi ha en més quantitat (sovint, l'aigua, que per això s'anomena «dissolvent universal»).", "El <b>solut</b>: el component o components que hi ha en menys quantitat (la sal, el sucre, el CO₂ d'un refresc).")
    b += FIG(T3.dissolucio(a), "En dissoldre's, les partícules de solut es reparteixen entre les del dissolvent.", "150mm")
    b += P("Quan dissolem sal en aigua, la sal no «desapareix»: les seves partícules es reparteixen entre les de l'aigua. Si pesem l'aigua i la sal per separat i després la dissolució, la massa és la mateixa: <b>massa de la dissolució = massa del solut + massa del dissolvent</b>. En canvi, els volums no sempre se sumen exactament.",
           "Les dissolucions poden ser sòlides (aliatges com el bronze o l'acer), líquides (aigua amb sal, vi) o gasoses (aire).")
    b += S(5, "La concentració")
    b += P("La <b>concentració</b> indica quanta quantitat de solut hi ha en una quantitat de dissolució. Una dissolució és <b>diluïda</b> si té poc solut i <b>concentrada</b> si en té molt. Per comparar-les cal un nombre. Aquest curs la mesurarem en massa de solut per cada litre de dissolució:")
    b += F('c = <span class="fr"><span>massa de solut</span><span>volum de dissolució</span></span>', note="Unitats: g/L o, per a quantitats molt petites, mg/L (1 g = 1 000 mg)")
    b += P("Per exemple, l'aigua de mar té una concentració de sals d'uns 35 g/L: en cada litre d'aigua de mar hi ha 35 g de sals dissoltes. Les etiquetes de les ampolles d'aigua indiquen la concentració de cada ió en mg/L.")
    b += EX("Exemple 1 · Calcular una concentració", "Dissolem 10 g de sucre en aigua fins a fer 250 mL de dissolució. Passem el volum a litres: 250 mL = 0,25 L. c = 10 / 0,25 = 40 g/L.")
    b += EX("Exemple 2 · Calcular la massa de solut", "Quanta sal hi ha en 2 L d'aigua de mar (35 g/L)? massa = c · V = 35 · 2 = 70 g.")
    b += EX("Exemple 3 · Canviar d'unitats", "Una aigua té 12 mg/L de sodi. Quants grams de sodi hi ha en una garrafa de 5 L? massa = 12 · 5 = 60 mg = 0,060 g.")
    b += EX("Exemple 4 · Els nitrats", "La llei permet com a màxim 50 mg/L de nitrats a l'aigua de boca. Una mostra de pou té 0,08 g de nitrats en 1 L: 0,08 g = 80 mg, i per tant 80 mg/L. No és potable.")
    b += S(6, "Preparar i diluir dissolucions")
    b += P("Per preparar 250 mL d'una dissolució de sal de 20 g/L: calculem la massa de sal (20 · 0,25 = 5 g), la pesem amb la balança, la dissolem en una mica d'aigua en un vas de precipitats i ho passem a un <b>matràs aforat</b> de 250 mL. Hi afegim aigua fins a la marca (enrasar) i agitem.",
           "<b>Diluir</b> és afegir més dissolvent. La massa de solut no canvia, però es reparteix en més volum i la concentració baixa. Diluir no fa desaparèixer el solut: un contaminant diluït en un riu hi continua sent.")
    b += EX("Exemple", "Tenim 100 mL d'una dissolució de 20 g/L (porta 2 g de sal) i hi afegim aigua fins a 400 mL. Els 2 g de sal ara són en 0,4 L: c = 2 / 0,4 = 5 g/L. Hem multiplicat el volum per 4 i la concentració s'ha dividit per 4.")
    b += S(7, "La solubilitat")
    b += P("Si afegim sal a un got d'aigua i remenem, arriba un moment que la sal ja no es dissol i queda al fons. La dissolució està <b>saturada</b>: ja no admet més solut a aquella temperatura.")
    b += DEF("Solubilitat", "és la quantitat màxima de solut que es pot dissoldre en una quantitat de dissolvent a una temperatura determinada. Normalment s'expressa en grams de solut per cada 100 g d'aigua. És una propietat característica.")
    b += P("La solubilitat depèn de la <b>temperatura</b>. Ho representem amb les <b>corbes de solubilitat</b>:")
    b += FIG(T3.corba_solubilitat(a), "Corbes de solubilitat del nitrat de potassi i de la sal.", "150mm")
    b += UL("Per a la majoria dels <b>sòlids</b>, la solubilitat <b>augmenta</b> amb la temperatura: el sucre es dissol millor en llet calenta. Si refredem una dissolució saturada, el que sobra cristal·litza.",
            "Per als <b>gasos</b>, la solubilitat <b>disminueix</b> amb la temperatura: un refresc calent perd el gas de seguida. Per això, quan l'aigua d'un riu s'escalfa (per l'estiu o per un abocament calent), hi ha menys oxigen dissolt i els peixos ho passen malament.")
    b += S(8, "Tècniques de separació")
    b += P("Els components d'una mescla es poden separar per <b>mètodes físics</b>, aprofitant que tenen propietats diferents. Triem la tècnica segons el tipus de mescla:")
    b += T(["Tècnica", "Quan la fem servir", "En què es basa", "Exemple"],
           [["Separació magnètica", "un sòlid és magnètic", "l'imant atrau el ferro", "ferro i sorra"], ["Tamisatge", "sòlids de mides diferents", "mida dels grans", "grava i sorra"],
            ["Decantació", "sòlid que es diposita al fons, o líquids que no es barregen", "densitat", "fang i aigua; oli i aigua (embut de decantació)"],
            ["Filtració", "sòlid no dissolt en un líquid", "el paper de filtre deixa passar el líquid i reté el sòlid", "sorra i aigua salada"],
            ["Evaporació i cristal·lització", "sòlid dissolt en un líquid (recuperem el sòlid)", "el líquid s'evapora i el sòlid no", "sal de l'aigua de mar (salines)"],
            ["Destil·lació", "líquid amb sòlids dissolts o dos líquids (recuperem el líquid)", "temperatura d'ebullició", "aigua destil·lada; alcohol del vi"]], w=["18%", "28%", "28%", "26%"])
    b += FIG(TF.separacio(), "Algunes tècniques de separació.", "150mm")
    b += P("A la <b>destil·lació</b> escalfem la mescla fins que el líquid bull. El vapor passa per un <b>refrigerant</b> (un tub envoltat d'aigua freda), es condensa i el recollim en un altre recipient. Les sals queden al matràs.")
    b += FIG(T3.destillacio(a), "Muntatge de destil·lació.", "155mm")
    b += EX("Exemple · Separar sorra, sal i ferro", "1. Passem un imant (embolicat amb un plàstic) i separem el ferro. 2. Afegim aigua i remenem: la sal es dissol i la sorra no. 3. Filtrem: la sorra queda al paper. 4. Evaporem el líquid filtrat: queda la sal.")
    b += S(9, "L'aigua potable: de l'embassament a l'aixeta")
    b += P("L'<b>aigua potable</b> és la que es pot beure sense risc per a la salut. No és aigua pura: ha de tenir poques sals, cap microorganisme perillós i cap contaminant per sobre dels valors que marca la llei. L'aigua de l'aixeta és una de les més controlades: se n'analitzen mostres cada dia.",
           "A l'àrea de Barcelona, l'aigua arriba dels rius Ter i Llobregat i, cada vegada més, de plantes dessalinitzadores i de la regeneració d'aigua. A la <b>potabilitzadora</b> (ETAP) passa per diverses etapes:")
    b += FIG(T3.potabilitzadora(a), "Etapes principals d'una planta potabilitzadora.", "165mm")
    b += P("Després d'usar-la, l'aigua bruta va per les clavegueres fins a la <b>depuradora</b> (EDAR), que en treu els sòlids, els greixos i la matèria orgànica (amb bacteris que se la mengen) abans de tornar-la al riu o al mar. Gràcies a les depuradores, el riu Besòs, que als anys 80 era un dels més contaminats d'Europa, s'ha recuperat i hi tornen a viure peixos i ocells.")
    b += TIP("La depuradora casolana", "Un filtre de grava, sorra i carbó actiu aclareix molt l'aigua: reté les partícules i el carbó adsorbeix colors i olors. Però <b>no la fa potable</b>: no elimina les sals dissoltes ni els microorganismes. Per això no hem de beure mai aigua filtrada a casa.")
    b += S(10, "Cuidem l'aigua")
    b += P("L'aigua dolça és un recurs escàs, i a Catalunya hem viscut sequeres greus. Cuidar-la vol dir <b>gastar-ne menys</b> (dutxes curtes, reparar les aixetes que gotegen) i <b>no contaminar-la</b>. Per l'aigüera i el vàter només hi ha d'anar aigua, sabó i paper higiènic:")
    b += UL("L'<b>oli</b> de cuinar embussa les canonades i dificulta la depuració: es guarda en una ampolla i es porta a la deixalleria.", "Les <b>tovalloletes</b>, els bastonets i les compreses no es desfan: van a la brossa.",
            "Els <b>medicaments</b> es porten a la farmàcia (punt SIGRE).", "Les <b>pintures i dissolvents</b> es porten a la deixalleria.")
    b += TIP("La ciència la fan persones", "Ellen Swallow Richards (1842–1911), química nord-americana, va analitzar més de 40 000 mostres d'aigua de Massachusetts. Gràcies a la seva feina es van crear els primers estàndards de qualitat de l'aigua i la primera planta moderna de depuració d'aigües residuals.")
    b += KW(("Substància pura", "un sol tipus de partícules, composició fixa"), ("Mescla", "dues o més substàncies sense reaccionar"), ("Dissolució", "mescla homogènia"), ("Solut", "component minoritari d'una dissolució"),
            ("Dissolvent", "component majoritari d'una dissolució"), ("Concentració", "massa de solut per volum de dissolució (g/L)"), ("Diluir", "afegir dissolvent; la concentració baixa"),
            ("Saturada", "dissolució que no admet més solut"), ("Solubilitat", "màxim de solut que es dissol a una temperatura"), ("Destil·lació", "separació per diferència de temperatura d'ebullició"))
    return b

# ======================================================================== SdA 5
def sda5():
    a = A(5)
    b = H(5, "Per què puja la massa i es daura la coca? Els canvis físics i químics, les reaccions, la conservació de la massa, la velocitat de les reaccions i la química de la cuina.")
    b += TOC("Canvis físics i canvis químics", "Les evidències d'un canvi químic", "Què passa en una reacció química", "Escriure una reacció", "La conservació de la massa",
             "La velocitat de les reaccions", "La fermentació: el llevat", "La química de la cuina", "La combustió i la seguretat", "Química, salut i casa")
    b += S(1, "Canvis físics i canvis químics")
    b += P("La matèria canvia contínuament: el gel es fon, el paper crema, el pa es torra, el ferro es rovella… Podem classificar els canvis en dos grups:")
    b += UL("<b>Canvi físic:</b> la substància <b>continua sent la mateixa</b>, encara que canviï de forma, de mida o d'estat. Exemples: fondre xocolata, dissoldre sucre, trencar un got, bullir aigua, picar gel. Molts són reversibles.",
            "<b>Canvi químic</b> o <b>reacció química</b>: es formen <b>substàncies noves</b>, amb propietats diferents de les inicials. Exemples: cremar fusta, torrar pa, coure un ou, rovellar-se un clau, fer-se malbé la fruita. Normalment no es poden desfer.")
    b += EX("Exemple", "Si fonem sucre, continua sent sucre (canvi físic): en refredar-se torna a ser sòlid i dolç. Si l'escalfem més, es torna marró, fa una olor nova i perd el gust dolç: s'ha format caramel, una substància nova (canvi químic).")
    b += S(2, "Les evidències d'un canvi químic")
    b += P("No podem veure les partícules, però hi ha pistes que ens indiquen que hi ha hagut un canvi químic:")
    b += FIG(T3.evidencies(a), "Evidències que indiquen que hi ha hagut un canvi químic.", "165mm")
    b += P("Compte: una sola evidència no sempre és suficient. Quan bullim aigua surten bombolles i és un canvi físic; quan es fon gel, absorbeix calor i també és físic. Cal pensar si s'ha format una substància nova. Com més evidències trobem, més segurs podem estar.")
    b += S(3, "Què passa en una reacció química")
    b += P("Les substàncies estan formades per <b>àtoms</b> units entre ells formant <b>molècules</b> (o cristalls). En una reacció química, els enllaços entre els àtoms es trenquen i els àtoms <b>es reorganitzen</b> d'una altra manera, formant substàncies noves. Els àtoms no es creen ni es destrueixen: són els mateixos abans i després.")
    b += UL("Els <b>reactius</b> són les substàncies que tenim al principi.", "Els <b>productes</b> són les substàncies que es formen.")
    b += FIG(T3.reaccio_model(a), "Model de la combustió del metà: els àtoms es reorganitzen.", "150mm")
    b += S(4, "Escriure una reacció")
    b += P("Les reaccions s'escriuen amb una <b>equació</b>: els reactius a l'esquerra, una fletxa (que es llegeix «es transforma en» o «dona») i els productes a la dreta. Aquest curs les escriurem amb paraules:")
    b += F("reactius → productes")
    b += EX("Exemples", "carbó + oxigen → diòxid de carboni · bicarbonat de sodi + vinagre → acetat de sodi + aigua + diòxid de carboni · ferro + oxigen + aigua → rovell (òxid de ferro).")
    b += S(5, "La conservació de la massa")
    b += P("A finals del segle XVIII, <b>Antoine Lavoisier</b> i <b>Marie-Anne Paulze Lavoisier</b> van fer moltes reaccions en recipients tancats i van pesar-ho tot amb balances molt precises. Van descobrir que la massa total no canvia:")
    b += DEF("Llei de conservació de la massa (Lavoisier)", "en una reacció química, la massa total dels reactius és igual a la massa total dels productes. «Res no es crea ni es destrueix, tot es transforma.»")
    b += P("Això té sentit amb el model d'àtoms: si els àtoms només es reorganitzen, n'hi ha el mateix nombre i la massa total és la mateixa. Si en un experiment sembla que la massa canvia, és que algun gas ha entrat o ha sortit del recipient.")
    b += FIG(T3.lavoisier_globus(a), "Bicarbonat i vinagre en un recipient obert i en un de tancat.", "150mm")
    b += EX("Exemple 1", "Cremem 12 g de carbó amb 32 g d'oxigen. Quant diòxid de carboni es forma? 12 + 32 = 44 g.")
    b += EX("Exemple 2 · El clau rovellat", "Un clau de 10,0 g es rovella i passa a pesar 10,8 g. No s'ha creat massa: el ferro s'ha combinat amb 0,8 g d'oxigen (i aigua) de l'aire.")
    b += EX("Exemple 3 · La foguera", "Si cremem 5 kg de fusta queden 0,1 kg de cendres. On són els 4,9 kg (i l'oxigen que ha reaccionat)? A l'aire, en forma de diòxid de carboni i vapor d'aigua.")
    b += S(6, "La velocitat de les reaccions")
    b += P("Algunes reaccions són molt ràpides (una explosió, un llumí que s'encén) i d'altres molt lentes (el rovell, la fruita que madura). Perquè dues partícules reaccionin han de <b>xocar</b>, i el xoc ha de tenir prou energia i la bona orientació. Tot el que faci augmentar els xocs eficaços fa anar la reacció més de pressa:")
    b += T(["Factor", "Què passa", "Exemple"],
           [["Temperatura", "més temperatura: les partícules es mouen més de pressa, xoquen més i amb més energia", "la nevera alenteix que els aliments es facin malbé"],
            ["Mida dels trossos (superfície)", "trossos petits: més superfície en contacte, més xocs", "la farina en pols crema molt més de pressa que un tros de pa"],
            ["Concentració", "més concentració: més partícules, més xocs", "el vinagre concentrat reacciona més de pressa amb el bicarbonat"],
            ["Catalitzadors", "substàncies que acceleren la reacció sense gastar-se", "els enzims del llevat, de la saliva i del cos"]], w=["22%", "44%", "34%"])
    b += FIG(T2.factors_velocitat(a), "Factors que modifiquen la velocitat d'una reacció.", "150mm")
    b += S(7, "La fermentació: el llevat")
    b += P("El <b>llevat</b> està format per fongs microscòpics vius. Quan el barregem amb farina i aigua, els seus enzims transformen els sucres en <b>diòxid de carboni</b> i alcohol: és la <b>fermentació</b>. El CO₂ queda atrapat a la massa i fa bombolles: per això la massa puja. Al forn, l'alcohol s'evapora i les bombolles s'expandeixen.",
           "La temperatura és clau: a 10 °C el llevat treballa molt a poc a poc; cap als 35 °C fa la fermentació més ràpida; i a 60–70 °C els fongs moren i la massa ja no puja. Per això la massa es deixa reposar en un lloc tebi.")
    b += F("sucre → diòxid de carboni + alcohol (etanol)", note="La fan els enzims del llevat (catalitzadors)")
    b += TIP("I el llevat químic?", "El «llevat químic» o impulsor no és viu: és bicarbonat de sodi barrejat amb un àcid en pols. Quan es mulla i s'escalfa, reaccionen i fan CO₂ de pressa. S'usa en pastissos i magdalenes.")
    b += S(8, "La química de la cuina")
    b += P("Cuinar és fer química. Dues reaccions donen color, gust i aroma a molts aliments:")
    b += UL("<b>Reacció de Maillard:</b> entre els sucres i les proteïnes, a partir d'uns 140 °C. Fa la crosta daurada del pa, de la coca, de la carn a la planxa i de les galetes. Dona centenars de substàncies noves amb gust i olor.",
            "<b>Caramel·lització:</b> els sucres sols, escalfats per sobre d'uns 160 °C, es tornen marrons i fan gust de caramel.")
    b += P("Si escalfem massa, l'aliment es crema i es formen substàncies amargues i negres (carbó) i algunes de perjudicials per a la salut, com l'acrilamida. Per això és millor <b>daurar</b> que <b>cremar</b>.",
           "Altres canvis químics de la cuina: l'ou que es cou (les proteïnes canvien de forma i ja no tornen enrere), la llet que es fa iogurt (fermentació per bacteris) o la poma tallada que s'enfosqueix (oxidació, que es frena amb suc de llimona).")
    b += S(9, "La combustió i la seguretat")
    b += P("Una <b>combustió</b> és una reacció química en què una substància (el <b>combustible</b>) reacciona amb l'<b>oxigen</b> i desprèn molta energia en forma de calor i llum. Perquè comenci cal una mica d'energia inicial (la flama d'un llumí, una espurna).")
    b += F("combustible + oxigen → diòxid de carboni + aigua + energia")
    b += FIG(T3.triangle_foc(a), "El triangle del foc i com s'apaga un foc.", "155mm")
    b += P("El <b>monòxid de carboni</b> (CO) es forma quan una combustió té poc oxigen (estufes, escalfadors o brasers en llocs mal ventilats). És un gas tòxic, sense color ni olor, que impedeix que la sang transporti l'oxigen. Per això cal ventilar sempre i revisar els aparells de gas.")
    b += TIP("Una revetlla segura", "Encén els petards i les fonts lluny de la cara i de la roba, amb un adult a prop i en un espai obert; no te'ls posis mai a la butxaca; no tornis a encendre un petard que no ha esclatat; i, si una paella d'oli s'encén, tapa-la i apaga el foc: <b>mai hi tiris aigua</b>.")
    b += S(10, "Química, salut i casa")
    b += P("Els aliments es fan malbé per reaccions químiques i per microorganismes. Per <b>conservar-los</b> alentim aquestes reaccions: amb fred (nevera, congelador), traient-los l'aigua (assecat, salat), escalfant-los per matar els microorganismes (pasteurització, conserves) o traient-los l'aire (envasat al buit).",
           "Els <b>productes de neteja</b> també són química. <b>No s'han de barrejar mai</b>: el lleixiu barrejat amb amoníac o amb productes àcids (salfumant, alguns desincrustants) desprèn gasos tòxics (cloramines o clor). Cal llegir sempre l'etiqueta, fer-los servir amb ventilació i guardar-los en el seu envàs original, fora de l'abast dels infants.")
    b += TIP("La ciència la fan persones", "Marie-Anne Paulze Lavoisier (1758–1836) treballava al laboratori amb Antoine Lavoisier: anotava els experiments, en dibuixava els aparells i va traduir de l'anglès obres científiques clau. Durant molt de temps la seva feina va quedar a l'ombra.")
    b += KW(("Canvi físic", "la substància continua sent la mateixa"), ("Canvi químic", "es formen substàncies noves"), ("Reactius", "substàncies inicials d'una reacció"), ("Productes", "substàncies que es formen"),
            ("Llei de Lavoisier", "la massa total es conserva en una reacció"), ("Catalitzador", "accelera una reacció sense gastar-se"), ("Fermentació", "el llevat transforma sucres en CO₂ i alcohol"),
            ("Reacció de Maillard", "sucres + proteïnes: daurat i aroma"), ("Combustió", "reacció amb oxigen que desprèn calor i llum"), ("Monòxid de carboni", "gas tòxic de les combustions amb poc oxigen"))
    return b

# ======================================================================== SdA 6
def sda6():
    a = A(6)
    b = H(6, "Quina carmanyola manté més calenta la sopa? L'energia, la calor i la temperatura, com es transmet la calor, l'aïllament i les fonts d'energia.")
    b += TOC("Què és l'energia", "Formes d'energia i transformacions", "Conservació i degradació de l'energia", "Unitats d'energia", "Calor i temperatura",
             "L'equilibri tèrmic", "Calcular la calor", "Com es transmet la calor", "Conductors i aïllants: la carmanyola i la casa", "Les fonts d'energia i l'estalvi")
    b += S(1, "Què és l'energia")
    b += P("L'<b>energia</b> és la capacitat que tenen els cossos de produir canvis: moure's, escalfar-se, il·luminar, canviar d'estat, fer reaccions químiques… Necessitem energia per a tot: per viure (la treiem dels aliments), per moure el cotxe, per escalfar la sopa o per carregar el mòbil.",
           "La unitat d'energia del SI és el <b>joule (J)</b>, en honor de James Prescott Joule.")
    b += S(2, "Formes d'energia i transformacions")
    b += T(["Forma d'energia", "La tenen…", "Exemple"],
           [["Cinètica", "els cossos en moviment", "una bicicleta, el vent, l'aigua d'un riu"], ["Potencial gravitatòria", "els cossos situats a una altura", "l'aigua d'un embassament, una pedra en un penya-segat"],
            ["Elàstica", "els cossos deformats", "una molla comprimida, un arc tibat"], ["Tèrmica (interna)", "tots els cossos, pel moviment de les seves partícules", "la sopa calenta"],
            ["Química", "les substàncies, als seus enllaços", "els aliments, la gasolina, les piles"], ["Elèctrica", "el corrent elèctric", "la que arriba als endolls"],
            ["Lluminosa (radiant)", "la llum i altres radiacions", "el Sol, una bombeta"], ["Nuclear", "els nuclis dels àtoms", "l'urani de les centrals nuclears"]], w=["24%", "38%", "38%"])
    b += P("L'energia es pot <b>transformar</b> d'una forma a una altra. Una cadena de transformacions ens explica d'on ve l'energia que fem servir:")
    b += EX("Exemples", "Un fogó de gas: química → tèrmica. Una pila en una llanterna: química → elèctrica → lluminosa (i tèrmica). Una central hidroelèctrica: potencial → cinètica → elèctrica. Nosaltres pedalant: química (aliments) → cinètica.")
    b += FIG(T2.energia_mecanica(a), "Transformació d'energia potencial en cinètica.", "140mm")
    b += S(3, "Conservació i degradació de l'energia")
    b += DEF("Principi de conservació de l'energia", "l'energia no es crea ni es destrueix: només es transforma d'una forma a una altra o passa d'un cos a un altre. L'energia total sempre és la mateixa.")
    b += P("Aleshores, per què diem que «gastem» energia? Perquè en cada transformació una part de l'energia acaba com a <b>calor</b> que s'escampa per l'entorn i ja no podem aprofitar: l'energia es <b>degrada</b>. Una bombeta antiga converteix en llum només un 5 % de l'energia elèctrica; la resta escalfa l'habitació. Un LED n'aprofita molt més: és més <b>eficient</b>.")
    b += S(4, "Unitats d'energia")
    b += P("A més del joule, hi ha altres unitats habituals. Les canviem amb factors de conversió:")
    b += T(["Unitat", "On la trobem", "Equivalència"],
           [["joule (J) i quilojoule (kJ)", "unitat del SI; etiquetes dels aliments", "1 kJ = 1 000 J"], ["caloria (cal) i quilocaloria (kcal)", "etiquetes dels aliments", "1 cal = 4,18 J · 1 kcal = 4 180 J"],
            ["quilowatt hora (kWh)", "factures de la llum", "1 kWh = 3 600 000 J = 3,6 · 10⁶ J"]])
    b += EX("Exemple", "Una galeta té 80 kcal. Quants kJ són? \\( 80\\ \\mathrm{kcal} \\cdot \\dfrac{4{,}18\\ \\mathrm{kJ}}{1\\ \\mathrm{kcal}} \\approx 334\\ \\mathrm{kJ} \\).")
    b += S(5, "Calor i temperatura")
    b += P("A la vida diària confonem calor i temperatura, però a la ciència són coses diferents:")
    b += UL("La <b>temperatura</b> indica com de ràpid es mouen, de mitjana, les partícules d'un cos. És una propietat del cos i es mesura amb un termòmetre (°C o K). Una tassa i una olla de sopa poden estar a la mateixa temperatura.",
            "La <b>calor</b> és <b>energia que passa</b> d'un cos a un altre perquè estan a temperatures diferents. Va sempre del cos <b>calent</b> al cos <b>fred</b>. Es mesura en joules. Un cos no «té» calor: té energia tèrmica, i en guanya o en perd en forma de calor.")
    b += P("Per això, quan toquem una barana de metall a l'hivern no és que «ens doni fred»: és que nosaltres li donem calor a ella, i molt de pressa.")
    b += S(6, "L'equilibri tèrmic")
    b += P("Quan posem en contacte dos cossos a temperatures diferents, el calent perd energia i es refreda, i el fred en guanya i s'escalfa. La calor passa fins que tots dos arriben a la <b>mateixa temperatura</b>: diem que han arribat a l'<b>equilibri tèrmic</b>. És el que passa a la sopa de la carmanyola: perd calor cap a l'aire de l'aula fins que arriba a la temperatura ambient.")
    b += FIG(T3.equilibri_termic(a), "En contacte, els dos cossos arriben a la mateixa temperatura.", "150mm")
    b += P("Si barregem la mateixa quantitat d'aigua a 70 °C i a 20 °C, la temperatura final és la mitjana: 45 °C. Si hi ha més aigua freda que calenta, la temperatura final queda més a prop de la de l'aigua freda.")
    b += S(7, "Calcular la calor")
    b += P("La calor que necessita un cos per escalfar-se depèn de tres coses: de la seva <b>massa</b> (escalfar una olla gran costa més que escalfar una tassa), de quant volem que pugi la <b>temperatura</b> i del <b>material</b>. Cada material té una <b>calor específica</b> (c): l'energia que cal per escalfar 1 kg d'aquell material 1 °C.")
    b += F("Q = m · c · ΔT", note="Q: calor (J) · m: massa (kg) · c: calor específica (J/(kg·°C)) · ΔT = T final − T inicial (°C)")
    b += T(["Material", "c (J/(kg·°C))", "Material", "c (J/(kg·°C))"], [["Aigua", "4 180", "Alumini", "900"], ["Oli d'oliva", "1 970", "Ferro", "450"], ["Aire", "1 000", "Coure", "385"]])
    b += EX("Exemple 1 · La sopa", "Quanta calor cal per escalfar 0,5 kg de sopa (com si fos aigua) de 20 °C a 80 °C? Q = 0,5 · 4 180 · (80 − 20) = 125 400 J ≈ 125 kJ.")
    b += EX("Exemple 2 · Oli i aigua", "Amb la mateixa calor, 1 kg d'oli s'escalfa més del doble que 1 kg d'aigua, perquè té una calor específica més petita. Per això l'oli de la paella s'escalfa tan de pressa.")
    b += EX("Exemple 3 · Calor perduda", "Si la sopa de la carmanyola (0,4 kg) passa de 75 °C a 45 °C, ΔT = −30 °C i Q = 0,4 · 4 180 · (−30) ≈ −50 000 J. El signe negatiu indica que la sopa <b>perd</b> 50 kJ de calor.")
    b += TIP("El mar suavitza el clima", "L'aigua té una calor específica molt alta: costa molt escalfar-la i també refredar-la. A l'estiu el mar absorbeix calor sense escalfar-se gaire, i a l'hivern la desprèn a poc a poc. Per això a la costa (Barcelona) les temperatures són més suaus que a l'interior (Lleida).")
    b += S(8, "Com es transmet la calor")
    b += P("La calor pot passar d'un lloc a un altre de tres maneres:")
    b += FIG(T3.transmissio_calor(a), "Conducció, convecció i radiació.", "160mm")
    b += UL("<b>Conducció:</b> la calor passa de partícula a partícula, per contacte, sense que la matèria es desplaci. És la manera principal en els sòlids. Exemple: el mànec d'una cullera de metall que s'escalfa dins la sopa.",
            "<b>Convecció:</b> en els líquids i els gasos, la part calenta es dilata, es fa menys densa i puja, i la part freda, més densa, baixa. Es formen corrents que reparteixen la calor. Exemples: l'aigua d'una olla, l'aire d'una habitació amb un radiador, els vents.",
            "<b>Radiació:</b> tots els cossos emeten radiació (ones), més com més calents són. Pot viatjar pel buit: així ens arriba la calor del Sol. Les superfícies fosques absorbeixen més radiació i les clares i brillants la reflecteixen.")
    b += S(9, "Conductors i aïllants: la carmanyola i la casa")
    b += P("Els <b>conductors tèrmics</b> deixen passar bé la calor: els metalls (coure, alumini, acer). Els <b>aïllants tèrmics</b> la deixen passar molt malament: la fusta, el plàstic, el suro, la llana, el poliestirè (porexpan) i, sobretot, l'<b>aire quiet</b>. Molts aïllants funcionen perquè tenen aire atrapat en petites bombolles o entre fibres, que no es pot moure i no fa convecció.")
    b += P("Per mantenir calenta la sopa cal frenar les tres maneres de transmetre la calor: un material aïllant o una capa d'aire per frenar la conducció, una tapa ben tancada per evitar la convecció, i una superfície brillant per reflectir la radiació. Així funciona un termo:")
    b += FIG(T3.termo(a), "Com està fet un termo.", "135mm")
    b += P("A una <b>casa</b> passa el mateix. Una casa sense aïllar perd molta calor a l'hivern (i n'entra molta a l'estiu):")
    b += FIG(T3.casa_perdues(a), "Per on perd la calor una casa sense aïllar.", "140mm")
    b += P("Aïllar la teulada i les parets, posar finestres de doble vidre i tapar les escletxes pot reduir a la meitat l'energia de la calefacció. Això estalvia diners i emissions de CO₂.")
    b += S(10, "Les fonts d'energia i l'estalvi")
    b += P("Les <b>fonts d'energia</b> són els recursos naturals d'on obtenim l'energia. Poden ser:")
    b += T(["", "Renovables", "No renovables"],
           [["Què són", "es regeneren de manera natural i no s'esgoten", "n'hi ha una quantitat limitada; es formen molt lentament o no es formen"],
            ["Exemples", "solar, eòlica, hidràulica, biomassa, geotèrmica, marina", "petroli, carbó, gas natural (combustibles fòssils), urani (nuclear)"],
            ["Avantatges", "gairebé no emeten CO₂; són locals", "produeixen energia en qualsevol moment"],
            ["Inconvenients", "depenen del sol o del vent; cal emmagatzemar l'energia; ocupen territori", "s'esgoten; emeten CO₂ i contaminants (fòssils) o generen residus radioactius (nuclear)"]], w=["16%", "42%", "42%"])
    b += FIG(T2.fonts_energia(a), "Fonts d'energia renovables i no renovables.", "155mm")
    b += P("Cremar combustibles fòssils emet <b>diòxid de carboni</b>, que augmenta l'efecte d'hivernacle i el canvi climàtic. La <b>transició energètica</b> vol dir passar a fonts renovables i, sobretot, gastar menys energia. Tothom hi pot participar:")
    b += UL("<b>Hàbits:</b> apagar llums i aparells, no deixar-los en espera, posar la calefacció a 19–20 °C i l'aire condicionat a 26 °C, tancar les portes.", "<b>Eficiència:</b> bombetes LED, electrodomèstics de classe A, aïllar edificis.",
            "<b>Renovables:</b> plaques solars als terrats (de casa o de l'institut), comunitats energètiques entre veïns.")
    b += TIP("La ciència la fan persones", "Mária Telkes (1900–1995), la «reina del Sol», va dissenyar el 1948 la primera casa escalfada amb energia solar, la Dover Sun House, i també forns solars i dessalinitzadores solars per a llocs sense electricitat.")
    b += KW(("Energia", "capacitat de produir canvis; en joules (J)"), ("Conservació de l'energia", "no es crea ni es destrueix, es transforma"), ("Degradació", "l'energia acaba com a calor que no podem aprofitar"),
            ("Temperatura", "mesura de l'agitació de les partícules"), ("Calor", "energia que passa d'un cos calent a un de fred"), ("Equilibri tèrmic", "els cossos arriben a la mateixa temperatura"),
            ("Calor específica", "energia per escalfar 1 kg d'un material 1 °C"), ("Conducció", "transmissió de la calor per contacte"), ("Aïllant tèrmic", "material que deixa passar malament la calor"), ("Renovable", "font d'energia que no s'esgota"))
    return b

FUNCS = {1: sda1, 2: sda2, 3: sda3, 4: sda4, 5: sda5, 6: sda6}
