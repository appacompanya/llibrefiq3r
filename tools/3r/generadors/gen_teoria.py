"""Dossiers de teoria de 3r d'ESO: un PDF per SdA amb tota la teoria de la situació d'aprenentatge.
   Ús: python3 -B gen_teoria.py [1 2 …]  → docs/sdaN-00-dossier-de-teoria.pdf
   Fa servir el disseny dels fulls (gen_sda1) i algunes figures dels generadors de cada SdA."""
import os, sys
import gen_sda1 as G
import figs
import gen_mobil as M, gen_hidrogen as Hd, gen_energia as En
from playwright.sync_api import sync_playwright

COL = {1: ("Detectius de la matèria", "#2F8F95", "#E3F1F2"), 2: ("El desodorant kamikaze", "#E0782F", "#FCE9DA"),
       3: ("Què hi ha dins del meu mòbil?", "#6C5CC9", "#ECE9FA"), 4: ("Un cotxe que només allibera aigua?", "#3F9A5A", "#E2F2E6"),
       5: ("Cèl·lules a la caça dels patògens", "#D14B66", "#FBE3E8"), 6: ("L'energia del nostre institut", "#2F6DB5", "#E1EBF7")}

EXTRA = """
.dh{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.2pt solid var(--acc);padding-bottom:2.5mm;margin-bottom:4mm}
.dh .tag{font-size:9.5pt;font-weight:700;color:#fff;background:var(--acc);border-radius:1.6mm;padding:.8mm 2.6mm}
.toc{font-size:10pt;columns:2;column-gap:8mm;margin:0 0 4mm;padding-left:5mm}
.ex{border-left:3pt solid var(--acc);background:#fff;padding:1.5mm 0 1.5mm 3.5mm;margin:2mm 0 3mm;font-size:10pt;break-inside:avoid}
.ex b.t{color:var(--acc)}
.fbox{border:1.2pt solid var(--acc);border-radius:2.5mm;padding:2mm 3.5mm;margin:2mm 0 3mm;background:var(--tint);break-inside:avoid}
.fbox .formula{margin:1mm 0}
.kw{columns:2;column-gap:8mm;font-size:9.8pt}.kw p{break-inside:avoid;margin:0 0 1.5mm}
h2{margin-top:6mm}
"""

def H(n, sub):
    t = COL[n][0]
    return (f'<div class="dh"><div><div class="kick">Física i química · 3r ESO · SdA {n} · {t}</div><h1>Dossier de teoria</h1>'
            f'<p class="intro" style="margin:1mm 0 0">{sub}</p></div><span class="tag">Teoria</span></div>')
def S(k, t): return f'<h2><span class="k">{k}</span> {t}</h2>'
def P(*t): return "".join(f"<p>{x}</p>" for x in t)
def UL(*t): return "<ul>" + "".join(f"<li>{x}</li>" for x in t) + "</ul>"
def OL(*t): return "<ol>" + "".join(f"<li>{x}</li>" for x in t) + "</ol>"
def TIP(t, h): return f'<div class="tip"><b>{t}.</b> {h}</div>'
def EX(t, h): return f'<div class="ex"><b class="t">{t}.</b> {h}</div>'
def F(*f, note=""): return '<div class="fbox">' + "".join(f'<div class="formula">{x}</div>' for x in f) + (f'<div class="small" style="text-align:center">{note}</div>' if note else "") + "</div>"
def T(head, rows, w=None):
    cg = "".join(f'<col style="width:{x}">' for x in w) if w else ""
    return f'<table><colgroup>{cg}</colgroup><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
def TOC(*t): return '<ol class="toc">' + "".join(f"<li>{x}</li>" for x in t) + "</ol>"
def KW(*pairs): return S("✓", "Paraules clau") + '<div class="kw">' + "".join(f"<p><b>{a}:</b> {b}</p>" for a, b in pairs) + "</div>"

# ======================================================================== SdA 1
def sda1():
    b = H(1, "Com podem identificar una substància? Magnituds, mesura, densitat, mescles i canvis químics.")
    b += TOC("Magnituds i unitats", "Factors de conversió", "Notació científica", "La mesura i l'error", "La densitat",
             "Substàncies pures i mescles", "Tècniques de separació", "Conductivitat i dissociació iònica", "Canvis físics i químics", "Seguretat al laboratori")
    b += S(1, "Magnituds i unitats")
    b += P("Una <b>magnitud</b> és una propietat que es pot mesurar i expressar amb un <b>nombre</b> i una <b>unitat</b>: la massa, la longitud, la temperatura… La bellesa o la por no són magnituds, perquè no es poden mesurar.",
           "Per entendre'ns arreu del món fem servir el <b>Sistema Internacional d'unitats (SI)</b>. Les magnituds <b>fonamentals</b> es defineixen per si mateixes; les <b>derivades</b> s'obtenen combinant les fonamentals.")
    b += T(["Magnitud fonamental", "Unitat del SI", "Magnitud derivada", "Unitat del SI"],
           [["Longitud", "metre (m)", "Superfície", "metre quadrat (m²)"], ["Massa", "quilogram (kg)", "Volum", "metre cúbic (m³)"],
            ["Temps", "segon (s)", "Velocitat", "metre per segon (m/s)"], ["Temperatura", "kelvin (K)", "Densitat", "quilogram per metre cúbic (kg/m³)"]])
    b += P("Els <b>prefixos</b> indiquen múltiples i submúltiples de la unitat:")
    b += T(["Prefix", "Símbol", "Equivalència", "Potència de 10"],
           [["kilo", "k", "1 000", "10³"], ["hecto", "h", "100", "10²"], ["deca", "da", "10", "10¹"], ["deci", "d", "0,1", "10⁻¹"],
            ["centi", "c", "0,01", "10⁻²"], ["mil·li", "m", "0,001", "10⁻³"], ["micro", "µ", "0,000 001", "10⁻⁶"], ["nano", "n", "0,000 000 001", "10⁻⁹"]])
    b += TIP("Volum", "1 L = 1 dm³ i <b>1 mL = 1 cm³</b>. 1 m³ = 1 000 L.")
    b += S(2, "Factors de conversió")
    b += P("Un <b>factor de conversió</b> és una fracció que val 1, perquè a dalt i a baix hi ha la mateixa quantitat escrita amb unitats diferents. En multiplicar-hi, la quantitat no canvia, però sí la unitat. La unitat que volem treure ha de quedar una vegada a dalt i una a baix, per simplificar-se.")
    b += EX("Exemple", "Passa 72 km/h a m/s: \\( 72\\ \\frac{\\mathrm{km}}{\\mathrm{h}} \\cdot \\frac{1000\\ \\mathrm{m}}{1\\ \\mathrm{km}} \\cdot \\frac{1\\ \\mathrm{h}}{3600\\ \\mathrm{s}} = 20\\ \\frac{\\mathrm{m}}{\\mathrm{s}} \\). Quan hi ha més d'una unitat, encadenem factors, un per a cada unitat.")
    b += EX("Exemple", "Passa 1,2 g/mL a kg/m³: \\( 1{,}2\\ \\frac{\\mathrm{g}}{\\mathrm{mL}} \\cdot \\frac{1\\ \\mathrm{kg}}{1000\\ \\mathrm{g}} \\cdot \\frac{10^{6}\\ \\mathrm{mL}}{1\\ \\mathrm{m^3}} = 1200\\ \\frac{\\mathrm{kg}}{\\mathrm{m^3}} \\).")
    b += S(3, "Notació científica")
    b += P("Per escriure nombres molt grans o molt petits fem servir la <b>notació científica</b>: \\( a \\cdot 10^{n} \\), amb \\( 1 \\le a < 10 \\). Si el nombre és més gran que 1, l'exponent és positiu; si és més petit que 1, és negatiu.")
    b += EX("Exemples", "300 000 000 m/s = 3 · 10⁸ m/s (velocitat de la llum) · 0,000 07 m = 7 · 10⁻⁵ m (gruix d'un cabell).")
    b += P("Per <b>multiplicar</b>, multipliquem els nombres i <b>sumem</b> els exponents; per <b>dividir</b>, dividim els nombres i <b>restem</b> els exponents: (3 · 10⁴) · (2 · 10⁻⁶) = 6 · 10⁻².")
    b += S(4, "La mesura i l'error")
    b += P("Tota mesura té un error. La <b>sensibilitat</b> d'un instrument és la quantitat més petita que pot apreciar (en una proveta, la distància entre dues ratlles). En un líquid, llegim el volum a la part de baix del menisc, amb els ulls a la seva altura.",
           "Per saber com d'exacta és una mesura, la comparem amb un <b>valor de referència</b>:")
    b += F("E<sub>a</sub> = | valor mesurat − valor de referència |", "E<sub>r</sub> (%) = E<sub>a</sub> / valor de referència · 100", note="L'error absolut té les unitats de la mesura; l'error relatiu, en percentatge, permet comparar mesures diferents.")
    b += EX("Exemple", "Mesurem 0,82 g/mL per a l'etanol i la referència és 0,79 g/mL: E<sub>a</sub> = 0,03 g/mL; E<sub>r</sub> = 0,03 / 0,79 · 100 ≈ 3,8 %. Un error relatiu gran pot indicar un error de mesura o que la substància no és pura (l'etanol 96 % porta aigua).")
    b += S(5, "La densitat")
    b += P("La <b>densitat</b> és la massa que té cada unitat de volum d'una substància. És una <b>propietat característica</b>: no depèn de la quantitat de substància i serveix per identificar-la. En canvi, la massa i el volum són propietats generals.")
    b += F("ρ = m / V", note="ρ en g/cm³ (= g/mL) o en kg/m³ · 1 g/cm³ = 1 000 kg/m³")
    b += T(["Substància (20 °C)", "ρ (g/cm³)", "Substància (20 °C)", "ρ (g/cm³)"],
           [["Aigua", "1,00", "Oli d'oliva", "0,92"], ["Etanol", "0,79", "Glicerina", "1,26"], ["Aigua de mar", "1,03", "Ferro", "7,87"]])
    b += EX("Exemple", "Un pot ple té una massa de 160 g i buit, 60 g. El líquid té 100 g i ocupa 125 mL: ρ = 100 / 125 = 0,80 g/mL. Pot ser etanol.")
    b += P("Un líquid menys dens <b>sura</b> damunt d'un de més dens si no es barregen (l'oli sura a l'aigua). La densitat depèn de la temperatura i de la puresa; per això cap prova sola no és suficient: cal combinar <b>proves convergents</b>.")
    b += S(6, "Substàncies pures i mescles")
    b += UL("<b>Substància pura:</b> té una composició fixa i unes propietats característiques pròpies. Pot ser un <b>element</b> (un sol tipus d'àtom: ferro, oxigen) o un <b>compost</b> (diversos elements units en una proporció fixa: aigua, clorur de sodi).",
            "<b>Mescla homogènia o dissolució:</b> no se'n distingeixen els components, ni amb microscopi (aigua amb sal, aire).",
            "<b>Mescla heterogènia:</b> se'n distingeixen els components (aigua i sorra, oli i aigua).")
    b += S(7, "Tècniques de separació")
    b += P("Cada tècnica aprofita una propietat diferent dels components:")
    b += T(["Tècnica", "Propietat en què es basa", "Exemple"],
           [["Separació magnètica", "El ferro és atret per l'imant", "Llimadures de ferro i sorra"], ["Decantació", "Densitat de dos líquids que no es barregen", "Oli i aigua (embut de decantació)"],
            ["Filtració", "Mida de les partícules: el sòlid no travessa el paper", "Sorra i aigua salada"], ["Evaporació i cristal·lització", "L'aigua s'evapora i la sal no", "Obtenir la sal de l'aigua salada"],
            ["Flotació", "Densitat del sòlid menor que la de l'aigua", "Serradures i sorra"], ["Cromatografia", "Cada pigment avança diferent amb la fase mòbil", "Tintes d'un retolador"]], w=["26%", "42%", "32%"])
    b += P("La <b>miscibilitat</b> és la capacitat de dos líquids de barrejar-se: l'etanol és miscible amb l'aigua i l'oli no. A la <b>cromatografia</b>, l'aigua puja pel paper per capil·laritat i arrossega els pigments; una tinta que dona diverses taques és una mescla.")
    b += S(8, "Conductivitat i dissociació iònica")
    b += P("L'aigua pura gairebé no condueix el corrent elèctric. Quan el clorur de sodi es dissol, es <b>dissocia</b> en ions que es poden moure i transporten la càrrega: NaCl → Na⁺ + Cl⁻. Per això l'aigua salada encén el LED del muntatge i l'aigua amb sucre, no: el sucre es dissol, però no forma ions.")
    b += S(9, "Canvis físics i canvis químics")
    b += UL("<b>Canvi físic:</b> la substància continua sent la mateixa (fondre, dissoldre, trencar).",
            "<b>Canvi químic:</b> es formen substàncies noves. Evidències: canvi de color, gas, precipitat, calor o llum.")
    b += EX("Exemple", "Un clau de ferro en sulfat de coure (blau): el clau es recobreix d'una capa vermellosa de coure i la dissolució perd color. Fe + CuSO₄ → FeSO₄ + Cu. És un canvi químic.")
    b += S(10, "Seguretat al laboratori")
    b += P("Les etiquetes porten <b>pictogrames de perill</b> (rombes vermells) i una paraula d'avís: <b>Perill</b> (el més greu) o <b>Atenció</b>. Normes bàsiques: ulleres i bata, cabells recollits, no menjar ni beure, no olorar directament, llegir l'etiqueta abans de fer servir un producte, avisar el professor de qualsevol accident i llençar els residus on s'indiqui.")
    b += figs.picto_table(cols=3, size="11mm")
    b += TIP("La ciència la fan persones", "Ellen Swallow Richards (1842–1911), primera dona que va estudiar al MIT, va analitzar milers de mostres d'aigua de Massachusetts i va fer el primer mapa del clorur: va comparar cada mostra amb un valor de referència, com fem nosaltres amb els pots.")
    b += KW(("Magnitud", "propietat que es pot mesurar"), ("Unitat", "quantitat que es fa servir com a referència per mesurar"), ("Factor de conversió", "fracció que val 1 per canviar d'unitat"),
            ("Sensibilitat", "quantitat més petita que aprecia un instrument"), ("Error relatiu", "error absolut dividit pel valor de referència, en %"), ("Densitat", "massa per unitat de volum"),
            ("Propietat característica", "propietat que permet identificar una substància"), ("Dissolució", "mescla homogènia"), ("Ió", "àtom o grup d'àtoms amb càrrega elèctrica"), ("Canvi químic", "canvi en què es formen substàncies noves"))
    return b

# ======================================================================== SdA 2
def sda2():
    b = H(2, "Per què explota un desodorant dins d'un cotxe a l'agost? El model de partícules, els estats de la matèria i les lleis dels gasos.")
    b += TOC("El model cineticomolecular", "Els estats d'agregació", "La temperatura i l'escala Kelvin", "La pressió", "Les lleis dels gasos", "Els canvis d'estat", "La corba d'escalfament", "El repte i la seguretat")
    b += S(1, "El model cineticomolecular")
    b += P("Un <b>model</b> és una representació simplificada que ens ajuda a explicar el que observem. El <b>model cineticomolecular</b> (o model de partícules) diu que:")
    b += OL("La matèria està formada per <b>partícules</b> molt petites.", "Entre les partícules <b>no hi ha res</b>: hi ha buit (no hi ha aire).",
            "Les partícules estan en <b>moviment constant</b>.", "Com més alta és la temperatura, <b>més de pressa</b> es mouen.", "Les partícules <b>no canvien de mida</b> ni de forma quan s'escalfen: canvia com es mouen i la distància entre elles.")
    b += EX("Per exemple", "Sentim el perfum a l'altra punta de l'aula perquè les seves partícules es mouen i s'escampen entre les de l'aire (<b>difusió</b>). L'aire d'una xeringa tapada es pot comprimir perquè entre les partícules hi ha molt d'espai buit; l'aigua, gairebé gens.")
    b += S(2, "Els estats d'agregació")
    b += T(["", "Sòlid", "Líquid", "Gas"],
           [["Partícules", "Molt juntes i ordenades", "Juntes però desordenades", "Molt separades"], ["Moviment", "Vibren al seu lloc", "Llisquen les unes sobre les altres", "Es mouen lliurement i molt de pressa"],
            ["Forma", "Pròpia", "La del recipient", "La del recipient"], ["Volum", "Propi", "Propi", "Ocupa tot el recipient"], ["Es pot comprimir?", "No", "Gairebé no", "Sí"]], w=["20%", "26%", "27%", "27%"])
    b += S(3, "La temperatura i l'escala Kelvin")
    b += P("La <b>temperatura</b> ens diu com de ràpid es mouen les partícules: com més alta, més ràpides. A les lleis dels gasos la temperatura s'ha de fer servir sempre en <b>kelvin</b>. El <b>zero absolut</b> (0 K = −273 °C) és la temperatura més baixa possible: les partícules es mourien el mínim possible.")
    b += F("T (K) = T (°C) + 273", note="Exemple: 27 °C = 300 K · 373 K = 100 °C. Una variació d'1 °C és igual a una variació d'1 K.")
    b += S(4, "La pressió")
    b += P("Les partícules d'un gas xoquen contínuament contra les parets del recipient. La <b>pressió</b> és el resultat d'aquests xocs: com més xocs i més forts, més pressió. Es mesura en atmosferes (atm), en pascals (Pa) o en mil·límetres de mercuri (mmHg).")
    b += F("1 atm = 760 mmHg = 101 325 Pa")
    b += S(5, "Les lleis dels gasos")
    b += P("Quan una de les tres magnituds (pressió, volum o temperatura) es manté constant, les altres dues es relacionen d'una manera senzilla:")
    b += T(["Llei", "Es manté constant", "Què passa", "Fórmula"],
           [["Boyle-Mariotte", "Temperatura", "Si el volum es fa més petit, la pressió es fa més gran", "P₁ · V₁ = P₂ · V₂"],
            ["Charles", "Pressió", "Si la temperatura puja, el volum es fa més gran", "V₁ / T₁ = V₂ / T₂"],
            ["Gay-Lussac", "Volum", "Si la temperatura puja, la pressió es fa més gran", "P₁ / T₁ = P₂ / T₂"]], w=["18%", "17%", "40%", "25%"])
    b += EX("Exemple (Boyle)", "Una xeringa tapada té 40 mL d'aire a 1 atm i l'empenyem fins a 10 mL: P₂ = 1 · 40 / 10 = 4 atm.")
    b += EX("Exemple (Charles)", "Un globus de 2,0 L a 27 °C (300 K) es posa al congelador a −18 °C (255 K): V₂ = 2,0 · 255 / 300 = 1,7 L.")
    b += EX("Exemple (Gay-Lussac)", "Un desodorant a 3,0 atm i 20 °C (293 K) arriba a 65 °C (338 K) dins d'un cotxe: P₂ = 3,0 · 338 / 293 ≈ 3,5 atm.")
    b += TIP("Com es resol un problema de gasos", "1) Escriu les dades amb unitats. 2) Mira quina magnitud es manté constant i tria la llei. 3) Passa les temperatures a kelvin. 4) Aïlla la incògnita i calcula. 5) Escriu el resultat amb la unitat i comprova si té sentit.")
    b += S(6, "Els canvis d'estat")
    b += P("Quan escalfem o refredem una substància pot canviar d'estat. La substància és la mateixa: només canvia com estan i com es mouen les partícules. És un <b>canvi físic</b>.")
    b += G.canvis_svg()
    b += T(["Núm.", "Canvi", "De … a …", "Energia"],
           [["1", "Fusió", "sòlid → líquid", "absorbeix"], ["2", "Solidificació", "líquid → sòlid", "desprèn"], ["3", "Vaporització", "líquid → gas", "absorbeix"],
            ["4", "Condensació", "gas → líquid", "desprèn"], ["5", "Sublimació", "sòlid → gas", "absorbeix"], ["6", "Sublimació inversa", "gas → sòlid", "desprèn"]])
    b += P("La vaporització pot ser de dues maneres. L'<b>evaporació</b> passa només a la superfície del líquid i a qualsevol temperatura (la roba s'asseca a 20 °C). L'<b>ebullició</b> passa a tot el líquid, amb bombolles, a una temperatura fixa: la <b>temperatura d'ebullició</b>, que depèn de la pressió. A dalt de l'Everest l'aigua bull a uns 70 °C; a l'olla a pressió, a més de 100 °C; en una xeringa on reduïm la pressió, a 50 °C.")
    b += S(7, "La corba d'escalfament")
    b += P("Si escalfem gel i anotem la temperatura cada minut, la gràfica temperatura–temps té <b>trams que pugen</b> (la temperatura augmenta) i <b>trams plans</b> (canvi d'estat). Mentre dura el canvi d'estat la temperatura no puja, encara que continuem escalfant: l'energia serveix per <b>separar les partícules</b>, no per fer-les anar més de pressa.")
    b += P("Les temperatures de fusió i d'ebullició són propietats característiques. L'aigua pura es fon a 0 °C i bull a 100 °C a 1 atm; al laboratori pot sortir una mica diferent pel termòmetre, la pressió o les sals de l'aigua de l'aixeta.")
    b += S(8, "El repte i la seguretat")
    b += P("Dins del cotxe a l'agost la temperatura puja. Les partícules del gas de la llauna es mouen més de pressa, xoquen més sovint i amb més força contra les parets i la <b>pressió augmenta</b> (llei de Gay-Lussac, a volum constant). A més, el propel·lent líquid de dins es vaporitza i la pressió puja encara més. Si la llauna no la resisteix, <b>rebenta</b>.")
    b += TIP("Seguretat", "Les etiquetes dels aerosols diuen: «Recipient a pressió: pot rebentar si s'escalfa. No l'exposeu a temperatures superiors a 50 °C.» Porten el pictograma d'inflamable i el de gas a pressió.")
    b += KW(("Model cineticomolecular", "la matèria són partícules en moviment amb buit entre elles"), ("Difusió", "les partícules d'una substància s'escampen entre les d'una altra"),
            ("Temperatura", "mesura de com de ràpid es mouen les partícules"), ("Zero absolut", "0 K = −273 °C"), ("Pressió", "efecte dels xocs de les partícules contra les parets"),
            ("Boyle-Mariotte", "P · V = constant, a T constant"), ("Charles", "V / T = constant, a P constant"), ("Gay-Lussac", "P / T = constant, a V constant"),
            ("Evaporació", "vaporització només a la superfície"), ("Ebullició", "vaporització a tot el líquid, a una temperatura fixa"))
    return b

# ======================================================================== SdA 3
def sda3():
    b = H(3, "Què hi ha dins del meu mòbil? L'àtom, els ions, la taula periòdica, l'enllaç químic i la bateria de liti.")
    b += TOC("Elements químics", "Els models atòmics", "Les partícules de l'àtom", "Isòtops", "Els ions", "El model de Bohr i l'assaig a la flama", "La taula periòdica", "L'enllaç químic", "La bateria de liti", "Mòbils, recursos i reciclatge")
    b += S(1, "Elements químics")
    b += P("Un <b>element químic</b> és una substància formada per un sol tipus d'àtom. Se'n coneixen 118 i cadascun té un <b>símbol</b> (Li, Co, Cu, Au…). Un mòbil en conté uns 31: coure als circuits, silici als xips, liti i cobalt a la bateria, or als contactes, neodimi a l'altaveu…")
    b += S(2, "Els models atòmics")
    b += T(["Model", "Any", "Com és l'àtom", "Per què canvia"],
           [["Dalton", "1808", "Esfera massissa i indivisible", "Explicava les proporcions de les reaccions"],
            ["Thomson", "1897", "Esfera positiva amb electrons incrustats («pastís de panses»)", "Es descobreix l'electró"],
            ["Rutherford", "1911", "Nucli molt petit i positiu; els electrons giren al voltant; la major part és buit", "Les partícules α travessen una làmina d'or i unes poques reboten"],
            ["Bohr", "1913", "Els electrons es mouen en capes (òrbites) d'energia definida", "Explica els colors de la llum que emeten els elements"]], w=["15%", "9%", "41%", "35%"])
    b += P("Els models canvien quan apareixen proves noves que l'anterior no pot explicar: la ciència és una construcció col·lectiva i en revisió.")
    b += S(3, "Les partícules de l'àtom")
    b += T(["Partícula", "Càrrega", "Massa", "On és"], [["Protó", "+1", "1 u", "Nucli"], ["Neutró", "0", "1 u", "Nucli"], ["Electró", "−1", "gairebé 0", "Escorça (capes)"]])
    b += F("Z = nombre de protons (nombre atòmic)", "A = protons + neutrons (nombre màssic) · neutrons = A − Z", note="En un àtom neutre, electrons = protons.")
    b += EX("Exemple", "<sup>7</sup><sub>3</sub>Li: Z = 3 → 3 protons i 3 electrons; neutrons = 7 − 3 = 4.")
    b += S(4, "Isòtops")
    b += P("Els <b>isòtops</b> són àtoms del mateix element (mateix Z) amb diferent nombre de neutrons (diferent A). Per exemple, <sup>6</sup>Li i <sup>7</sup>Li, o <sup>12</sup>C i <sup>14</sup>C. Tenen les mateixes propietats químiques, perquè tenen els mateixos electrons.")
    b += S(5, "Els ions")
    b += P("Un <b>ió</b> és un àtom que ha guanyat o perdut electrons i, per tant, té càrrega. El nombre de protons no canvia mai.")
    b += UL("<b>Catió</b> (+): ha perdut electrons. Li → Li⁺ + e⁻. Els metalls tendeixen a formar cations.",
            "<b>Anió</b> (−): ha guanyat electrons. F + e⁻ → F⁻. Els no metalls tendeixen a formar anions.")
    b += EX("Exemple", "Co²⁺ (Z = 27): 27 protons i 27 − 2 = 25 electrons. O²⁻ (Z = 8): 8 protons i 8 + 2 = 10 electrons.")
    b += S(6, "El model de Bohr i l'assaig a la flama")
    b += P("Al model de Bohr, els electrons s'ordenen en capes: fins a 2 a la primera, fins a 8 a la segona i comencem a omplir la tercera amb 8. Liti (Z = 3): 2, 1 · Oxigen (Z = 8): 2, 6 · Sodi (Z = 11): 2, 8, 1. Els electrons de l'<b>última capa</b> decideixen com es comporta l'element.",
           "Quan escalfem una sal a la flama, alguns electrons absorbeixen energia i salten a una capa més allunyada. En tornar a la seva capa, emeten aquesta energia en forma de <b>llum d'uns colors concrets</b>. Cada element té el seu: el liti dona vermell intens; el sodi, groc; el coure, verd. L'<b>espectroscopi</b> separa la llum en línies i és més fiable que el color a ull nu (el liti i l'estronci fan tots dos vermell). El color identifica l'element, no el compost. Així, Bunsen i Kirchhoff van descobrir el cesi i el rubidi (1860–1861).")
    b += S(7, "La taula periòdica")
    b += P("El 1869, Dmitri <b>Mendeléiev</b> va ordenar els elements i va deixar forats per a elements encara no descoberts, de què va predir les propietats. Avui la taula s'ordena per <b>nombre atòmic Z</b>. Les files són els <b>períodes</b> (1–7) i les columnes, els <b>grups</b> (1–18). Els elements d'un mateix grup tenen el mateix nombre d'electrons a l'última capa i propietats semblants.")
    b += M.taula_svg(width_mm=165)
    b += UL("<b>Metalls</b> (a l'esquerra i al centre): brillants, bons conductors, tendeixen a formar cations.",
            "<b>No metalls</b> (a la dreta): mals conductors, tendeixen a formar anions. <b>Semimetalls</b>: B, Si, Ge, As, Sb, Te.",
            "<b>Gasos nobles</b> (grup 18): última capa plena, gairebé no reaccionen.",
            "Ió que tendeix a formar cada grup: grup 1 → +1 · grup 2 → +2 · grup 13 → +3 · grup 16 → −2 · grup 17 → −1.")
    b += P("El grup 1 (liti, sodi, potassi) són els <b>metalls alcalins</b>: tenen 1 electró a l'última capa, el perden fàcilment i reaccionen amb l'aigua, cada vegada amb més força com més avall són del grup.")
    b += S(8, "L'enllaç químic")
    b += P("Els àtoms s'uneixen per tenir una configuració més estable, semblant a la d'un gas noble (última capa plena).")
    b += T(["Enllaç", "Entre…", "Què fan els electrons", "Propietats i exemple"],
           [["Iònic", "metall + no metall", "Un àtom en cedeix i l'altre en capta: es formen ions que s'atrauen", "Sòlids durs, condueixen fosos o dissolts. LiF, NaCl, LiCoO₂"],
            ["Covalent", "no metall + no metall", "Es comparteixen", "Molècules (H₂O, CO₂) o xarxes molt dures (SiO₂, diamant). No condueixen (excepte el grafit)"],
            ["Metàl·lic", "metall + metall", "Formen un núvol d'electrons lliures", "Condueixen el corrent i la calor, es deformen. Cu, Au"]], w=["13%", "19%", "33%", "35%"])
    b += EX("Exemple", "LiF: el liti (2, 1) cedeix 1 electró al fluor (2, 7). Es formen Li⁺ i F⁻; una càrrega + i una −, i el compost és neutre. Els cables són de coure (metàl·lic, electrons lliures) i el separador de la bateria és de plàstic (covalent, aïllant). El grafit condueix perquè cada carboni té un electró lliure que es mou entre les capes.")
    b += S(9, "La bateria de liti")
    b += P("La bateria té dos elèctrodes: l'<b>ànode</b> de grafit i el <b>càtode</b> d'òxid de liti i cobalt (LiCoO₂), separats per un <b>electròlit</b> i un separador. Quan fem servir el mòbil, el liti de l'ànode perd un electró: Li → Li⁺ + e⁻. Els ions Li⁺ viatgen per l'electròlit fins al càtode i els electrons van pel circuit del mòbil i el fan funcionar. Quan la carreguem, el carregador fa tornar el liti a l'ànode.",
           "Si la bateria es perfora o s'aixafa (per exemple, al camió de les escombraries), l'ànode i el càtode es toquen: hi ha un <b>curtcircuit</b>, s'escalfa, l'electròlit (inflamable) es crema i és molt difícil d'apagar.")
    b += S(10, "Mòbils, recursos i reciclatge")
    b += P("Molts materials del mòbil són <b>matèries primeres crítiques</b>: són importants per a la tecnologia i se n'obtenen en pocs països, de vegades amb problemes ambientals i socials (com el cobalt i el coltan de la República Democràtica del Congo). Per això cal, per ordre, <b>reutilitzar</b> (fer durar el mòbil), <b>reciclar</b> i <b>recuperar</b> els elements. Els mòbils vells es porten a un punt de recollida, mai al contenidor de rebuig.")
    b += KW(("Element", "substància amb un sol tipus d'àtom"), ("Nombre atòmic (Z)", "nombre de protons"), ("Nombre màssic (A)", "protons + neutrons"), ("Isòtops", "mateix Z, diferent A"),
            ("Catió / anió", "ió positiu / ió negatiu"), ("Període / grup", "fila / columna de la taula periòdica"), ("Electrons de valència", "electrons de l'última capa"),
            ("Enllaç iònic", "entre ions de càrrega oposada"), ("Enllaç covalent", "electrons compartits"), ("Electròlit", "medi per on viatgen els ions a la bateria"))
    return b

# ======================================================================== SdA 4
def sda4():
    b = H(4, "Un cotxe que només allibera aigua? La reacció química, la formulació, les equacions i els càlculs de massa.")
    b += TOC("Canvis químics i reaccions", "La conservació de la massa", "Formulació i nomenclatura", "L'equació química ajustada", "Càlculs de massa", "L'energia de les reaccions", "La velocitat de les reaccions", "Els combustibles i l'hidrogen")
    b += S(1, "Canvis químics i reaccions")
    b += P("En una <b>reacció química</b>, unes substàncies, els <b>reactius</b>, es transformen en unes altres de noves, els <b>productes</b>. Els enllaços dels reactius es trenquen i els àtoms es <b>reorganitzen</b>. Evidències: es forma un gas, canvia el color, apareix un sòlid, s'allibera o s'absorbeix calor, hi ha llum.")
    b += EX("Combustió de l'espelma", "La parafina reacciona amb l'oxigen de l'aire i es formen aigua (el got fred s'entela) i diòxid de carboni (l'aigua de calç es torna blanca). Si l'espelma fos d'hidrogen, només es formaria aigua.")
    b += S(2, "La conservació de la massa")
    b += P("<b>Llei de Lavoisier (1789):</b> en una reacció química, la massa total dels reactius és igual a la massa total dels productes. Els àtoms no es creen ni es destrueixen: només es reorganitzen.",
           "En un <b>sistema obert</b> sembla que la massa canvia perquè hi entren o en surten gasos (al vas amb vinagre i bicarbonat, el CO₂ s'escapa). En un <b>sistema tancat</b> la massa es manté constant.",
           "<b>Llei de Proust:</b> els elements es combinen sempre en la mateixa proporció en massa. 4 g d'hidrogen reaccionen amb 32 g d'oxigen i formen 36 g d'aigua; amb 8 g d'hidrogen, el doble de tot.")
    b += S(3, "Formulació i nomenclatura (IUPAC)")
    b += UL("<b>Substàncies simples:</b> un sol element. Metalls i gasos nobles amb el símbol (Fe, Mg, He). Alguns no metalls formen molècules de dos àtoms: H₂, O₂, N₂, Cl₂, F₂.",
            "<b>Ions:</b> cations amb «ió» + nom (Na⁺ ió sodi, Fe³⁺ ió ferro(III)); anions acabats en <b>-ur</b> (Cl⁻ clorur, S²⁻ sulfur, F⁻ fluorur) i O²⁻ òxid.",
            "<b>Compostos iònics binaris</b> (metall + no metall): les càrregues s'han de compensar. Nom: anió + «de» + catió. MgCl₂ clorur de magnesi · Al₂O₃ òxid d'alumini · Fe₂O₃ òxid de ferro(III).",
            "<b>Compostos de dos no metalls:</b> prefixos mono-, di-, tri-, tetra-, penta-. CO monòxid de carboni · CO₂ diòxid de carboni · SO₃ triòxid de sofre · N₂O monòxid de dinitrogen.",
            "Noms acceptats: H₂O aigua · NH₃ amoníac · CH₄ metà.")
    b += EX("Com es formula", "Ió alumini Al³⁺ i ió òxid O²⁻: 2 Al donen +6 i 3 O donen −6 → Al₂O₃.")
    b += S(4, "L'equació química ajustada")
    b += P("Una <b>equació química</b> representa una reacció: reactius a l'esquerra, fletxa, productes a la dreta. Està <b>ajustada</b> quan hi ha el mateix nombre d'àtoms de cada element a cada costat. Per ajustar-la, posem <b>coeficients</b> davant de les fórmules; mai no canviem els subíndexs.")
    b += Hd.particules_svg()
    b += EX("Exemple", "CH₄ + O₂ → CO₂ + H₂O. Carboni: 1 i 1. Hidrogen: 4 a l'esquerra → 2 H₂O. Oxigen: 4 a la dreta → 2 O₂. Ajustada: CH₄ + 2 O₂ → CO₂ + 2 H₂O.")
    b += S(5, "Càlculs de massa")
    b += P("Amb les <b>masses atòmiques</b> (H = 1 u, C = 12 u, O = 16 u, Mg = 24 u, Cl = 35,5 u…) calculem la massa de cada terme de l'equació i en traiem la proporció. Després fem servir un factor de conversió, com a la SdA 1.")
    b += F("2 H₂ + O₂ → 2 H₂O", "4 g + 32 g → 36 g")
    b += EX("Exemple", "Quina massa d'aigua es forma amb 8 g d'hidrogen? \\( 8\\ \\mathrm{g\\ H_2} \\cdot \\frac{36\\ \\mathrm{g\\ H_2O}}{4\\ \\mathrm{g\\ H_2}} = 72\\ \\mathrm{g\\ H_2O} \\). Un autobús que consumeix 20 kg d'hidrogen al dia allibera 180 kg d'aigua.")
    b += P("Si les quantitats dels reactius no estan en la proporció exacta, un s'acaba primer (el <b>reactiu limitant</b>) i de l'altre en sobra.")
    b += S(6, "L'energia de les reaccions")
    b += UL("<b>Exotèrmica:</b> allibera energia a l'entorn (la temperatura puja). Combustions, el magnesi amb àcid clorhídric, l'hidrogen amb l'oxigen.",
            "<b>Endotèrmica:</b> absorbeix energia de l'entorn (la temperatura baixa o cal subministrar energia). El vinagre amb bicarbonat, l'electròlisi de l'aigua, la fotosíntesi.")
    b += P("A l'<b>electròlisi</b>, el corrent elèctric descompon l'aigua: 2 H₂O → 2 H₂ + O₂. Es forma el doble de volum d'hidrogen (al càtode, −) que d'oxigen (a l'ànode, +).")
    b += Hd.electrolisi_svg()
    b += S(7, "La velocitat de les reaccions")
    b += P("Segons la <b>teoria de les col·lisions</b>, perquè dues partícules reaccionin han de xocar amb prou energia. Tot el que augmenta els xocs eficaços fa la reacció més ràpida:")
    b += T(["Factor", "Efecte", "Exemple"],
           [["Temperatura", "Més temperatura → partícules més ràpides → més xocs i més forts", "El menjar dura més a la nevera"],
            ["Concentració", "Més partícules en el mateix volum → més xocs", "L'àcid més concentrat fa més bombolles"],
            ["Superfície de contacte", "Trossos més petits → més superfície exposada", "Les estelles cremen abans que un tronc"]], w=["22%", "45%", "33%"])
    b += S(8, "Els combustibles i l'hidrogen")
    b += P("Els <b>hidrocarburs</b> (metà, propà, butà, gasolina) contenen carboni i hidrogen; en cremar-los es formen CO₂ i H₂O. L'<b>hidrogen</b> no conté carboni: en una pila de combustible reacciona amb l'oxigen i només forma aigua. Però que el vehicle no emeti CO₂ no vol dir que no contamini gens: depèn de com s'obté l'hidrogen.")
    b += T(["Hidrogen", "D'on surt", "Emissions"], [["Gris", "Gas natural", "Emet CO₂ en produir-lo (uns 10–12 kg de CO₂ per kg d'H₂)"], ["Blau", "Gas natural, capturant part del CO₂", "Menys emissions"], ["Verd", "Electròlisi amb electricitat renovable", "Gairebé sense emissions"]], w=["14%", "40%", "46%"])
    b += P("A més, amb la mateixa electricitat renovable un vehicle de bateria fa unes 2–3 vegades més quilòmetres que un d'hidrogen. L'hidrogen té més sentit en vehicles grans que fan molts quilòmetres, com els autobusos.")
    b += KW(("Reactius / productes", "substàncies inicials / substàncies noves"), ("Llei de Lavoisier", "la massa es conserva en una reacció"), ("Llei de Proust", "proporció fixa en massa"),
            ("Coeficient", "nombre davant d'una fórmula per ajustar l'equació"), ("Reactiu limitant", "el que s'acaba primer"), ("Exotèrmica / endotèrmica", "allibera / absorbeix energia"),
            ("Teoria de les col·lisions", "les partícules han de xocar per reaccionar"), ("Electròlisi", "descomposició amb corrent elèctric"), ("Hidrocarbur", "compost de carboni i hidrogen"), ("Hidrogen verd", "obtingut amb electricitat renovable"))
    return b

# ======================================================================== SdA 5
def sda5():
    b = H(5, "Com persegueix un neutròfil un bacteri sense veure'l? El moviment, el gradient de concentració i les forces.")
    b += TOC("Posició, trajectòria i desplaçament", "La velocitat", "El moviment rectilini uniforme (MRU)", "L'acceleració i el MRUA", "Les gràfiques del moviment", "Com es resol un problema", "Escales i mida de les cèl·lules", "Difusió i gradient de concentració", "Les forces", "La llei de Hooke", "Les lleis de Newton", "Les forces de les cèl·lules")
    b += S(1, "Posició, trajectòria i desplaçament")
    b += P("Per descriure un moviment cal un <b>sistema de referència</b>. La <b>posició</b> (x) diu on és el mòbil respecte d'aquest punt. La <b>trajectòria</b> és el camí que segueix; la <b>distància recorreguda</b> és la longitud d'aquest camí. El <b>desplaçament</b> és el canvi de posició, Δx = x − x₀: la fletxa recta que va de l'inici al final.")
    b += S(2, "La velocitat")
    b += F("v = Δx / Δt", note="Al SI, en m/s. De km/h a m/s, es divideix entre 3,6; de m/s a km/h, es multiplica per 3,6.")
    b += P("La <b>rapidesa mitjana</b> és la distància recorreguda dividida pel temps. El mòdul de la <b>velocitat mitjana</b> és el desplaçament dividit pel temps. Si la trajectòria no és recta (com la d'un neutròfil), la rapidesa mitjana és més gran que la velocitat mitjana.")
    b += S(3, "El moviment rectilini uniforme (MRU)")
    b += P("La trajectòria és recta i la velocitat és constant: el mòbil recorre la mateixa distància cada segon.")
    b += F("x = x₀ + v · t")
    b += EX("Exemple", "Un autobús passa per x = 50 m a 36 km/h (10 m/s): x = 50 + 10 · t. Als 8 s és a 130 m; arriba a x = 250 m a t = 20 s.")
    b += S(4, "L'acceleració i el MRUA")
    b += P("L'<b>acceleració</b> indica quant canvia la velocitat cada segon. Si el mòbil frena, és negativa. Al <b>MRUA</b> la trajectòria és recta i l'acceleració és constant.")
    b += F("a = Δv / Δt  (m/s²)", "v = v₀ + a · t", "x = x₀ + v₀ · t + ½ · a · t²")
    b += EX("Exemple", "Una moto surt del repòs amb a = 2,5 m/s² durant 8 s: v = 0 + 2,5 · 8 = 20 m/s (72 km/h); x = ½ · 2,5 · 8² = 80 m.")
    b += EX("Frenada", "Un cotxe a 50 km/h (13,9 m/s) frena amb a = −5 m/s²: triga t = 13,9 / 5 ≈ 2,8 s i recorre ≈ 19 m. A 30 km/h, només ≈ 7 m. Si el conductor triga 1 s a reaccionar, hi hem de sumar la distància que fa en aquest segon.")
    b += S(5, "Les gràfiques del moviment")
    b += T(["", "Gràfica x–t", "Gràfica v–t"],
           [["Repòs", "Recta horitzontal", "Recta sobre l'eix (v = 0)"], ["MRU", "Recta inclinada; el <b>pendent</b> és la velocitat", "Recta horitzontal"],
            ["MRUA", "Corba (paràbola)", "Recta inclinada; el <b>pendent</b> és l'acceleració"]])
    b += P("A la gràfica v–t, l'<b>àrea</b> sota la línia és la distància recorreguda. El pendent es calcula amb dos punts: pendent = (canvi de l'eix vertical) / (canvi de l'eix horitzontal).")
    b += S(6, "Com es resol un problema de moviment")
    b += OL("Dibuixa la situació i tria el sistema de referència.", "Escriu les dades amb unitats del SI.", "Identifica el tipus de moviment (MRU o MRUA).", "Escriu les equacions i substitueix.", "Calcula i comprova que el resultat té sentit, amb la unitat.")
    b += TIP("Dos mòbils", "Per saber quan i on es troben, escriu l'equació de posició de cadascun amb el mateix origen i iguala-les.")
    b += S(7, "Escales i mida de les cèl·lules")
    b += P("Les cèl·lules es mesuren en <b>micròmetres</b>: 1 µm = 0,001 mm = 10⁻⁶ m. Un glòbul vermell fa 7,5 µm. En una imatge de microscopi, la <b>barra d'escala</b> ens diu quants µm representa cada mm; també podem fer servir un objecte conegut com a referència.")
    b += F("augments = mida a la imatge / mida real", note="Les dues mides en la mateixa unitat.")
    b += S(8, "Difusió i gradient de concentració")
    b += P("La <b>difusió</b> és el moviment net de partícules des d'on n'hi ha més cap a on n'hi ha menys, a causa del moviment de les partícules. És més ràpida amb més temperatura. La <b>concentració</b> indica quantes partícules hi ha en un volum.",
           "Un <b>gradient de concentració</b> és la variació de la concentració per unitat de distància. Els bacteris alliberen molècules que es difonen: n'hi ha més a prop del bacteri. El neutròfil té <b>receptors</b> a la membrana; la banda que en detecta més s'orienta cap al bacteri i la cèl·lula avança cap allà. Aquest moviment guiat per un gradient químic es diu <b>quimiotaxi</b>.")
    b += F("gradient = Δconcentració / Δdistància", note="Exemple: de 100 nM a 20 nM en 40 µm → (20 − 100) / 40 = −2 nM/µm.")
    b += S(9, "Les forces")
    b += P("Una <b>força</b> és tota acció capaç de canviar l'estat de moviment d'un cos o de deformar-lo. Es mesura en <b>newtons</b> (N) amb un dinamòmetre. És una magnitud <b>vectorial</b>: té mòdul (valor), direcció i sentit, i es representa amb una fletxa. Diverses forces es poden substituir per la seva <b>força resultant</b>: per sumar-les gràficament, posem les fletxes una a continuació de l'altra.",
           "El <b>pes</b> és la força amb què la Terra atrau un cos: P = m · g, amb g = 9,8 N/kg. Una massa de 50 g pesa 0,050 · 9,8 = 0,49 N.")
    b += S(10, "La llei de Hooke")
    b += P("En un cos elàstic, com una molla, l'allargament és proporcional a la força aplicada, mentre no superem el <b>límit d'elasticitat</b> (si l'estirem massa, ja no torna a la forma inicial).")
    b += F("F = k · Δx", note="k: constant elàstica (N/m), el pendent de la gràfica F–Δx · Δx: allargament (m)")
    b += EX("Exemple", "Una molla s'allarga 0,025 m amb un pes de 0,49 N: k = 0,49 / 0,025 ≈ 20 N/m. Si s'allarga 0,05 m, la força és 20 · 0,05 = 1 N.")
    b += S(11, "Les lleis de Newton")
    b += T(["Llei", "Què diu", "Exemple"],
           [["1a · Inèrcia", "Si la força resultant és zero, el cos manté el repòs o el MRU", "Si el patinet frena de cop, el cos continua endavant"],
            ["2a · Força i acceleració", "F = m · a (1 N = 1 kg · m/s²)", "Un patinet més carregat costa més d'accelerar"],
            ["3a · Acció i reacció", "Si A fa una força sobre B, B en fa una d'igual i de sentit contrari sobre A", "Empenyem el terra enrere i el terra ens empeny endavant"]], w=["22%", "43%", "35%"])
    b += EX("Exemple", "Un patinet amb el conductor (80 kg) frena amb a = −3 m/s²: F = 80 · (−3) = −240 N.")
    b += S(12, "Les forces de les cèl·lules")
    b += P("Per dins, la cèl·lula té un <b>citoesquelet</b>. Els filaments d'<b>actina</b> empenyen la membrana endavant i estiren el substrat cap enrere a través de les <b>adhesions focals</b>; els <b>microtúbuls</b> fan de vies de transport. Per la 3a llei de Newton, el substrat estira la cèl·lula cap endavant i la cèl·lula avança.",
           "Les forces de les cèl·lules són de l'ordre dels <b>nanonewtons</b> (1 nN = 10⁻⁹ N). Es mesuren posant la cèl·lula sobre un gel tou amb boletes: el gel es comporta com un conjunt de molles i, pel desplaçament de les boletes i la llei de Hooke, en calculem la força. A l'escala de la cèl·lula, el fregament de l'aigua és molt gran: quan deixa de fer força, s'atura gairebé a l'instant.")
    b += TIP("Salut", "Mesurar les forces i la velocitat de les cèl·lules ajuda a entendre la immunitat, la cicatrització de les ferides i la metàstasi. Amb febre, els neutròfils es mouen més de pressa: la febre és una conseqüència de la resposta del cos a la infecció, no la causa de la malaltia.")
    b += KW(("Desplaçament", "canvi de posició (fletxa de l'inici al final)"), ("Velocitat", "Δx / Δt"), ("Acceleració", "Δv / Δt"), ("MRU / MRUA", "velocitat constant / acceleració constant"),
            ("Pendent", "a la x–t, velocitat; a la v–t, acceleració"), ("Gradient", "variació de la concentració amb la distància"), ("Quimiotaxi", "moviment guiat per un gradient químic"),
            ("Força", "acció que canvia el moviment o deforma; en N"), ("Constant elàstica", "k = F / Δx"), ("Inèrcia", "tendència a mantenir l'estat de moviment"))
    return b

# ======================================================================== SdA 6
def sda6():
    b = H(6, "Quanta energia gasta la nostra aula i com podem estalviar-ne? L'energia, la potència, l'electricitat i les fonts d'energia.")
    b += TOC("L'energia i les seves formes", "Transformació i conservació", "El rendiment", "Potència i consum", "Calcular el consum i el cost", "El corrent elèctric", "Circuits en sèrie i en paral·lel", "Seguretat elèctrica", "Com es genera l'electricitat", "Les fonts d'energia", "La informació fiable")
    b += S(1, "L'energia i les seves formes")
    b += P("L'<b>energia</b> és la capacitat d'un sistema per produir canvis. Es mesura en <b>joules</b> (J). Es manifesta de formes diferents: <b>cinètica</b> (moviment), <b>potencial</b> (posició, com l'aigua d'un embassament), <b>tèrmica</b>, <b>química</b> (aliments, combustibles, piles), <b>elèctrica</b>, <b>lluminosa</b>, <b>sonora</b> i <b>nuclear</b>.")
    b += S(2, "Transformació i conservació")
    b += P("L'energia passa d'una forma a una altra, però <b>no es crea ni es destrueix</b>: la quantitat total es conserva. En cada transformació, una part es converteix en energia tèrmica que no podem aprofitar (diem que es «degrada»).")
    b += EX("Exemples", "Ventilador: elèctrica → cinètica (+ tèrmica). Placa fotovoltaica: lluminosa → elèctrica. Altaveu: elèctrica → sonora. Pila que encén un llum: química → elèctrica → lluminosa.")
    b += S(3, "El rendiment")
    b += P("El <b>rendiment</b> indica quina part de l'energia consumida es converteix en energia útil. Es representa amb un <b>diagrama de Sankey</b>: l'amplada de cada fletxa és proporcional a l'energia.")
    b += F("rendiment (%) = energia útil / energia consumida · 100")
    b += En.sankey_svg()
    b += EX("Exemple", "Una bombeta d'incandescència de 60 W fa 3 J de llum cada segon: rendiment = 3 / 60 · 100 = 5 %. Una LED de 8 W fa la mateixa llum: 3 / 8 · 100 ≈ 38 %. La resta es converteix en calor.")
    b += S(4, "Potència i consum")
    b += P("La <b>potència</b> és l'energia que un aparell transforma cada segon. Es mesura en <b>watts</b> (W); la trobem a l'etiqueta. A les factures, l'energia es mesura en <b>quilowatts hora</b> (kWh): l'energia que transforma un aparell d'1 000 W en 1 hora.")
    b += F("P = E / t  ·  E = P · t", "1 kWh = 3,6 · 10⁶ J", note="E en J si P en W i t en s · E en kWh si P en kW i t en h")
    b += S(5, "Calcular el consum i el cost")
    b += OL("Escriu la potència en kW (W / 1 000).", "Multiplica per les hores que funciona: kWh.", "Multiplica pels dies, si cal.", "Cost = kWh · preu (per exemple, 0,15 € per kWh).")
    b += EX("Exemple", "Una bombeta encesa 5 h cada dia durant un any: 60 W → 0,060 · 5 · 365 = 109,5 kWh → 16,43 €. LED de 8 W → 0,008 · 5 · 365 = 14,6 kWh → 2,19 €. S'estalvien 14,24 € l'any amb una sola bombeta.")
    b += P("El <b>mode d'espera</b> (el llum vermell encès) també consumeix: un televisor d'1 W en espera 20 h al dia gasta 7,3 kWh l'any. Multiplicat per tres milions de llars, són 21,9 GWh (1 GWh = 10⁶ kWh). El <b>wattímetre</b> mesura el consum real d'un aparell, que pot ser diferent del de l'etiqueta.")
    b += S(6, "El corrent elèctric")
    b += P("El <b>corrent elèctric</b> és el moviment ordenat de càrregues (electrons) per un circuit. Un circuit té un <b>generador</b> (pila, endoll), conductors, receptors (bombetes, motors) i un interruptor. La <b>tensió</b> o voltatge (V, en volts) és l'impuls que dona el generador; la <b>intensitat</b> (I, en ampers) és la quantitat de càrrega que passa cada segon. A casa, la tensió és de 230 V.")
    b += F("P = V · I")
    b += S(7, "Circuits en sèrie i en paral·lel")
    b += En.circuits_svg()
    b += T(["", "En sèrie", "En paral·lel"],
           [["Connexió", "Un darrere l'altre, pel mateix camí", "Cadascun en una branca diferent"], ["Si una bombeta es fon", "S'apaguen totes", "Les altres continuen enceses"],
            ["Brillantor de dues bombetes", "Fan menys llum", "Cadascuna fa la llum normal"], ["Tensió de cada aparell", "Es reparteix entre tots", "Cadascun rep tota la tensió (230 V a casa)"]], w=["28%", "36%", "36%"])
    b += P("La instal·lació d'una casa o de l'institut és <b>en paral·lel</b>: podem apagar un llum sense que s'apaguin els altres, i cada aparell funciona a 230 V.")
    b += S(8, "Seguretat elèctrica")
    b += UL("Endolla i desendolla agafant l'endoll, mai el cable, i amb les mans seques. No facis servir aparells amb el cable malmès.",
            "Molts aparells de molta potència en un sol endoll amb un lladre fan passar molta intensitat: els cables s'escalfen i hi pot haver un incendi.",
            "El <b>magnetotèrmic</b> talla el corrent si passa massa intensitat (sobrecàrrega o curtcircuit). El <b>diferencial</b> el talla si hi ha una fuita de corrent, per exemple a través d'una persona.")
    b += S(9, "Com es genera l'electricitat")
    b += P("La majoria de centrals fan girar una <b>turbina</b> connectada a un <b>alternador</b>. A l'alternador, un imant gira dins d'una bobina i hi genera corrent elèctric (<b>inducció electromagnètica</b>, descoberta per Michael Faraday el 1831). El que canvia d'una central a una altra és què fa girar la turbina.")
    b += En.alternador_svg()
    b += EX("Cadenes de transformacions", "Hidràulica: potencial de l'aigua → cinètica → la turbina gira → l'alternador genera electricitat. Cicle combinat: química del gas → tèrmica → cinètica → elèctrica. Fotovoltaica: lluminosa → elèctrica, sense turbina.")
    b += S(10, "Les fonts d'energia")
    b += T(["Renovables", "No renovables"], [["Es regeneren de manera natural: hidràulica, eòlica, solar (fotovoltaica i tèrmica), biomassa, geotèrmica.", "Se n'esgoten les reserves: nuclear (urani), gas natural, petroli, carbó."],
            ["Avantatges: no s'esgoten i gairebé no emeten CO₂. Inconvenients: depenen del temps (sol, vent), ocupen territori, cal emmagatzemar l'energia.", "Avantatges: produeixen quan cal. Inconvenients: s'esgoten, emeten CO₂ (combustibles fòssils) o generen residus radioactius (nuclear)."]])
    b += P("A Catalunya, l'any 2024 les renovables van generar el 19,1 % de l'electricitat (dades de Red Eléctrica). Catalunya consumeix més electricitat de la que genera. La millor energia és la que no es gasta: un pla d'estalvi combina <b>hàbits sostenibles</b> (apagar llums i aparells), <b>eficiència</b> (LED, aparells eficients) i <b>generació renovable</b> (plaques solars), amb la participació de tota la comunitat.")
    b += TIP("La ciència la fan persones", "Mária Telkes (1900–1995) va dissenyar la Dover Sun House (1948), una casa escalfada amb el Sol: una sal es fonia de dia, absorbint energia, i en solidificar-se de nit la desprenia.")
    b += S(11, "La informació fiable")
    b += P("Per decidir cal informació fiable. Davant d'una font, pregunta't: <b>qui</b> ho diu (és expert, és una institució?), <b>quan</b> ho diu (és actual?), <b>per què</b> ho diu (vol vendre alguna cosa?) i <b>amb quines proves</b> (dona dades i referències?). Cita sempre les fonts: Autor o institució (any). <i>Títol</i>. Adreça web.")
    b += KW(("Energia", "capacitat de produir canvis; en J"), ("Conservació de l'energia", "no es crea ni es destrueix, es transforma"), ("Rendiment", "energia útil / energia consumida"),
            ("Potència", "energia per unitat de temps; en W"), ("kWh", "unitat d'energia de les factures; 3,6 · 10⁶ J"), ("Tensió", "impuls del generador; en V"), ("Intensitat", "càrrega que passa cada segon; en A"),
            ("En paral·lel", "cada aparell en una branca"), ("Alternador", "transforma energia cinètica en elèctrica"), ("Renovable", "font que es regenera de manera natural"))
    return b

FUNCS = {1: sda1, 2: sda2, 3: sda3, 4: sda4, 5: sda5, 6: sda6}

def build(ns, out_dir):
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for n in ns:
            t, c, tint = COL[n]
            G.SDA.update({"n": n, "title": t, "color": c, "tint": tint})
            body = FUNCS[n]()
            html = G.page(body, EXTRA)
            path = os.path.join(out_dir, f"sda{n}-teoria.html"); open(path, "w", encoding="utf-8").write(html)
            pg.goto("file://" + path)
            pg.wait_for_function('document.body.dataset.math==="ok"', timeout=15000); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pdf = os.path.join(out_dir, f"sda{n}-00-dossier-de-teoria.pdf")
            pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True, display_header_footer=True,
                   header_template="<div></div>", footer_template=G.FOOT.format(n=n, t=t))
            os.remove(path); print("ok", pdf)
        br.close()

if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or [1, 2, 3, 4, 5, 6]
    build(ns, os.environ.get("OUT", G.OUT))
