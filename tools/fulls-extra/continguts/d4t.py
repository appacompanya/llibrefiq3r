"""Dossiers d'ampliació de 4t ESO (un per SdA), amb la mateixa estructura que els de 3r: reptes amb etiqueta,
apartats i, al final, recursos. Substitueixen el contingut del full d'ampliació original (se'n conserva la
capçalera) i n'aprofiten els reptes. Les dades que no surten als fulls del curs són constants o dades de
referència (NOAA, IUPAC, OMS…) o s'indiquen com a suposició."""
from estil import rep, tip, table, graf, resources, h2, DOSSIER_INTRO

PHET = "https://phet.colorado.edu/ca/"
VIQUI = "https://ca.wikipedia.org"
REC = '<p class="intro">Recursos per continuar aprenent. Entra a l\'adreça i cerca el títol entre cometes.</p>'
BOX = lambda h: f'<div class="box" style="min-height:{h}mm"></div>'


def dossier(reptes, recursos):
    return DOSSIER_INTRO + "".join(reptes) + resources(recursos, h2("R", "Recursos per anar més enllà") + REC)


DOSSIER = {}

# ================================================================== SdA 1 · Els colors de la Mercè
DOSSIER["sda1-21-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "L'energia de la llum.", "La llum està feta de fotons, i l'energia de cada fotó depèn de la seva longitud d'ona λ.", [
        "Calcula l'energia d'un fotó vermell (656 nm) i d'un de violeta (410 nm), en J i en eV.",
        "Quin té més energia? Quantes vegades més?",
        "Els focs fan llum perquè els electrons salten entre nivells. Quina diferència d'energia (en eV) correspon a la llum vermella?"], 6,
        tip("\\(E = \\dfrac{h\\,c}{\\lambda}\\), amb \\(h = 6{,}626 \\cdot 10^{-34}\\ \\text{J}\\cdot\\text{s}\\) i \\(c = 3{,}0 \\cdot 10^{8}\\ \\text{m/s}\\). "
            "1 eV = 1,602 · 10⁻¹⁹ J. 1 nm = 10⁻⁹ m.")),
    rep(2, "Càlcul", "Bohr va encertar.", "Bohr va calcular que els nivells d'energia de l'àtom d'hidrogen valen \\(E_n = -\\dfrac{13{,}6}{n^2}\\ \\text{eV}\\).", [
        "Calcula l'energia dels nivells n = 2 i n = 3.",
        "Quina energia té el fotó que s'emet en el salt de n = 3 a n = 2? Passa-la a joules.",
        "Calcula la longitud d'ona d'aquest fotó i compara-la amb la línia vermella de l'hidrogen (656 nm, fitxa 3). Què en conclous?"], 7),
    rep(3, "Raonament", "Ultraviolat i pell.", "Per trencar enllaços de l'ADN de la pell cal una energia mínima d'uns 4 eV per fotó.", [
        "Calcula la longitud d'ona màxima que pot tenir un fotó amb 4 eV.",
        "A quina zona de l'espectre correspon? Per què la llum visible no crema la pell?",
        "Per què una crema solar s'ha de posar encara que el dia estigui ennuvolat?"], 5),
    rep(4, "Càlcul", "Tres isòtops del magnesi.", "El magnesi natural és una mescla de tres isòtops:", [
        "Quants protons i neutrons té cada isòtop?",
        "Calcula la massa atòmica mitjana i compara-la amb la de la taula periòdica (24,31 u).",
        "Per què els tres isòtops fan el mateix color a la flama?"], 5,
        table(["Isòtop", "²⁴Mg", "²⁵Mg", "²⁶Mg"], [["Massa (u)", "23,985", "24,986", "25,983"], ["Abundància (%)", "78,99", "10,00", "11,01"]])),
    rep(5, "Càlcul", "El rellotge del carboni-14.", "El ¹⁴C és radioactiu: cada 5.730 anys (el seu període de semidesintegració) en queda la meitat. "
        "Mentre un ésser és viu, en té una proporció constant; quan mor, el ¹⁴C va disminuint.", [
        "Quina fracció de ¹⁴C queda en un tros de fusta de fa 11.460 anys? I de fa 17.190 anys?",
        "Un os conserva 1/16 del ¹⁴C inicial. Quants anys té?",
        "Per què no es pot datar amb ¹⁴C un os de dinosaure de fa 66 milions d'anys?"], 6),
    rep(6, "Història", "Un element descobert al Sol.", "El 1868, durant un eclipsi, Pierre Janssen i Norman Lockyer van observar a l'espectre del Sol "
        "una línia groga de 587,6 nm que no corresponia a cap element conegut. Lockyer el va anomenar heli, del grec hèlios (sol). "
        "No es va trobar a la Terra fins al 1895.", [
        "Com és possible descobrir un element a 150 milions de quilòmetres? Fes servir la paraula «espectre».",
        "Per què aquesta línia no podia ser la del sodi (589 nm), que també és groga?",
        "Relaciona aquest descobriment amb el de Cecilia Payne (fitxa 3)."], 6),
    rep(7, "Investiga", "Les excepcions del crom i del coure.", "El crom (Z = 24) i el coure (Z = 29) no segueixen exactament el diagrama de Moeller: "
        "les seves configuracions acaben en 3d⁵ 4s¹ i 3d¹⁰ 4s¹.", [
        "Escriu la configuració que esperaries per a cadascun segons el diagrama de Moeller i la configuració real.",
        "Busca per què passa (subnivells semiplens i plens). Cita la font.",
        "Quants electrons desaparellats té el crom en cada cas?"], 6),
    rep(8, "Càlcul", "Quin oxidant dona més oxigen?", "Als focs, l'oxidant aporta l'oxigen perquè el combustible cremi. Els més usats són el perclorat "
        "de potassi i el nitrat de potassi. Masses atòmiques: K 39,1 · Cl 35,5 · N 14,0 · O 16,0.", [
        "Escriu les fórmules i calcula'n les masses molars.",
        "Calcula el percentatge en massa d'oxigen de cadascun.",
        "Per què es busquen oxidants sense perclorat (fitxa 9)?"], 6),
], [
    ("Construeix un àtom", "Simulació PhET: afegeix protons, neutrons i electrons i mira com canvien l'element, la càrrega i la massa", PHET + " · «Construeix un àtom» (Build an Atom)"),
    ("Isòtops i massa atòmica", "Simulació PhET: barreja isòtops i calcula la massa atòmica mitjana", PHET + " · «Isòtops i massa atòmica» (Isotopes and Atomic Mass)"),
    ("Models de l'àtom d'hidrogen", "Simulació PhET: compara els models de Thomson, Rutherford i Bohr amb els espectres", PHET + " · «Models of the Hydrogen Atom»"),
    ("Cecilia Payne-Gaposchkin", "Viquipèdia en català: la vida de l'astrònoma que va descobrir de què estan fets els estels", VIQUI + " · «Cecilia Payne-Gaposchkin»"),
    ("Heli", "Viquipèdia en català: el descobriment a l'espectre del Sol i les propietats de l'element", VIQUI + " · «Heli»"),
    ("Taula periòdica de la IUPAC", "Unió Internacional de Química Pura i Aplicada: la taula oficial amb les masses atòmiques actuals", "https://iupac.org · «Periodic Table of Elements»"),
])

# ================================================================== SdA 2 · Aixeta o ampolla?
DOSSIER["sda2-21-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "Del % a la molaritat.", "L'àcid clorhídric comercial (salfumant concentrat) és del 37 % en massa i té una densitat d'1,19 g/mL. M(HCl) = 36,5 g/mol.", [
        "Agafa 1 L de dissolució. Quina massa té?",
        "Quants grams i quants mols d'HCl hi ha en aquest litre? Quina és la molaritat?",
        "Quants mL d'aquest àcid calen per preparar 500 mL d'HCl 0,10 mol/L?"], 7),
    rep(2, "Càlcul", "Dilucions en sèrie.", "Partim d'una dissolució 1,0 mol/L i fem dilucions successives 1:10 (1 mL de dissolució + 9 mL d'aigua).", [
        "Quina concentració té el tub 5?",
        "Quantes molècules de solut hi ha en 1 mL del tub 5? (N<sub>A</sub> = 6,022 · 10²³)",
        "Si en féssim 30, quantes molècules hi hauria en 1 mL? Què vol dir aquest resultat?"], 6),
    rep(3, "Càlcul", "Aigua saturada de sal.", "A 20 °C, 1 L d'aigua dissol uns 360 g de NaCl (M = 58,4 g/mol), i la dissolució saturada té una densitat d'1,20 g/mL.", [
        "Quina massa i quin volum té la dissolució saturada?",
        "Quina és la seva molaritat? I la concentració en g/L?",
        "Per què no podem preparar un sèrum de 400 g/L?"], 6),
    rep(4, "Dades", "Aigua tova, aigua dura.", "La duresa de l'aigua es calcula amb el calci i el magnesi i s'expressa en mg de CaCO₃ per litre: "
        "duresa = 2,5 · [Ca] + 4,1 · [Mg], amb [Ca] i [Mg] en mg/L. Una classificació habitual és: tova (menys de 60), moderadament dura "
        "(60–120), dura (120–180) i molt dura (més de 180).", [
        "Calcula la duresa i classifica les dues aigües.",
        "Per què es forma calç a dins del bullidor? (Pista: en escalfar-se, l'hidrogencarbonat es descompon i es forma carbonat de calci.)",
        "L'aigua dura és dolenta per a la salut? Busca-ho en una font fiable i cita-la."], 6,
        table(["Aigua", "Calci (mg/L)", "Magnesi (mg/L)", "Duresa (mg CaCO₃/L)", "Tipus"], [["A (aixeta, exemple)", "85", "20", "", ""], ["B (embotellada feble)", "10", "2", "", ""]], empty_cols=(3, 4))),
    rep(5, "Càlcul", "Sals amb aigua.", "El sulfat de coure(II) es ven com a cristalls blaus de CuSO₄·5H₂O (M = 249,7 g/mol), que porten aigua dins del cristall.", [
        "Quina massa n'has de pesar per preparar 250 mL d'una dissolució 0,10 mol/L de sulfat de coure(II)?",
        "Quina massa hauries pesat si haguessis fet el càlcul amb el CuSO₄ sense aigua (M = 159,6 g/mol)?",
        "Si haguessis pesat aquesta segona massa de cristalls blaus, quina concentració real tindria la dissolució?"], 6),
    rep(6, "Raonament", "El sèrum i els glòbuls vermells.", "Una dissolució és isotònica amb la sang si té la mateixa concentració de partícules dissoltes. "
        "El sèrum fisiològic (9 g/L de NaCl) ho és. L'aigua passa a través de la membrana de les cèl·lules cap a on hi ha més concentració (osmosi).", [
        "Què li passa a un glòbul vermell en aigua destil·lada? I en aigua amb 30 g/L de sal?",
        "Dibuixa un glòbul vermell en les tres dissolucions i indica cap on va l'aigua.",
        "Per què no es pot posar aigua destil·lada directament a la vena?"], 5, after=BOX(28)),
    rep(7, "Experiment", "L'efecte Tyndall a casa.", "Amb la llanterna del mòbil, uns gots transparents, aigua i llet pots veure l'efecte Tyndall.", [
        "Dissenya un experiment per trobar la quantitat mínima de llet (en gotes per got) amb què es veu el feix de llum.",
        "Quina variable canvies, quina observes i quines mantens iguals?",
        "Per què el cel és blau i les postes de sol són vermelles? Busca-ho i relaciona-ho amb aquest experiment."], 6),
], [
    ("Molaritat", "Simulació PhET: canvia la quantitat de solut i el volum i mira com canvia la concentració", PHET + " · «Molaritat» (Molarity)"),
    ("Concentració", "Simulació PhET: dissolucions, saturació i mesura de la concentració", PHET + " · «Concentració» (Concentration)"),
    ("Reial decret 3/2023 (qualitat de l'aigua de consum)", "Butlletí Oficial de l'Estat: els valors paramètrics de cada substància", "https://www.boe.es · «Real Decreto 3/2023»"),
    ("Qualitat de l'aigua per adreça", "Aigües de Barcelona: l'anàlisi de l'aigua del teu barri", "https://www.aiguesdebarcelona.cat"),
    ("Osmosi", "Viquipèdia en català: el pas de l'aigua a través de membranes i les dissolucions isotòniques", VIQUI + " · «Osmosi»"),
    ("Efecte Tyndall", "Viquipèdia en català: per què veiem els raigs de llum en un col·loide", VIQUI + " · «Efecte Tyndall»"),
])

# ================================================================== SdA 3 · Quant CO₂ costa venir a l'institut?
DOSSIER["sda3-22-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "El volum del CO₂.", "A 25 °C i 1 atm, un mol de qualsevol gas ocupa uns 24,5 L.", [
        "Amb el resultat de la fitxa 5 (massa de CO₂ que fa 1 L de gasolina), calcula quants mols de CO₂ són.",
        "Quins litres i quins m³ de CO₂ fa 1 L de gasolina?",
        "Un cotxe gasta 6 L cada 100 km. Quants km ha de fer per omplir de CO₂ el volum de la teva aula (8 m × 6 m × 3 m)?"], 6),
    rep(2, "Càlcul", "I el gasoil?", "Fem servir el dodecà (C₁₂H₂₆) com a model de gasoil, amb una densitat de 0,84 kg/L.", [
        "Escriu i ajusta l'equació de la combustió completa del dodecà.",
        "Calcula quants kg de CO₂ fa 1 L de gasoil.",
        "Compara-ho amb el factor del MITECO (2,488 kg/L). Per què emet més CO₂ un litre de gasoil que un de gasolina?"], 7),
    rep(3, "Càlcul", "Qui s'acaba primer?", "Fem reaccionar 10 g d'hidrogen amb 64 g d'oxigen per formar aigua: 2 H₂ + O₂ → 2 H₂O.", [
        "Quants mols hi ha de cada reactiu? Quin és el reactiu limitant?",
        "Quanta aigua es forma?",
        "Quants grams sobren de l'altre reactiu? Comprova que la massa es conserva."], 6),
    rep(4, "Càlcul", "El rendiment.", "En una fàbrica s'obtenen 15 t d'amoníac a partir de 15 t d'hidrogen: N₂ + 3 H₂ → 2 NH₃.", [
        "Quantes tones d'amoníac s'obtindrien si tot l'hidrogen reaccionés?",
        "Quin és el rendiment de la reacció (massa real ÷ massa teòrica · 100)?",
        "Per què les reaccions industrials no tenen un rendiment del 100 %?"], 6),
    rep(5, "Dades", "La corba de Keeling.", "Des del 1958 es mesura el CO₂ de l'aire a l'observatori de Mauna Loa (Hawaii). Mitjanes anuals (NOAA, arrodonides):", [
        "Representa les dades.",
        "Calcula quantes ppm ha augmentat cada any, de mitjana, en cada interval. Què observes?",
        "Abans de la revolució industrial hi havia unes 280 ppm. En quin percentatge ha augmentat fins al 2024?",
        "Si el ritme dels últims anys es mantingués, quantes ppm hi hauria el 2030?"], 5,
        table(["Any", "1960", "1980", "2000", "2020", "2024"], [["CO₂ (ppm)", "317", "339", "370", "414", "425"]]) +
        graf((1960, 2030, 10), (300, 450, 25), "any", "CO₂ (ppm)")),
    rep(6, "Càlcul", "L'hidrogen com a combustible.", "En cremar 1 mol d'hidrogen es desprenen uns 286 kJ, i en cremar 1 mol de metà, uns 890 kJ.", [
        "Quants kJ per gram desprèn cada combustible? Quin és millor per gram?",
        "Quant CO₂ fa la combustió de l'hidrogen?",
        "Gairebé tot l'hidrogen que es fabrica avui surt del gas natural. Què vol dir l'«hidrogen verd»? Quins inconvenients té l'hidrogen (emmagatzematge, seguretat…)?"], 6),
    rep(7, "Raonament", "El cotxe elèctric i els biocombustibles.", "Un cotxe elèctric gasta 15 kWh cada 100 km. Suposem que produir 1 kWh d'electricitat "
        "emet 0,15 kg de CO₂ (depèn de com s'ha generat).", [
        "Quants kg de CO₂ per km emet? Compara-ho amb un cotxe de gasolina de 6 L/100 km (2,237 kg CO₂/L).",
        "Quines emissions no compta aquest càlcul (fabricació, bateria…)?",
        "L'etanol es pot fabricar a partir de plantes que han absorbit CO₂. Per què es diu que és «neutre en carboni»? És del tot cert? Busca-ho i cita la font."], 7),
], [
    ("Ajusta equacions químiques", "Simulació PhET: ajusta reaccions i comprova que es conserven els àtoms", PHET + " · «Balancing Chemical Equations»"),
    ("Reactius, productes i sobrants", "Simulació PhET: el reactiu limitant amb sandvitxos i molècules", PHET + " · «Reactants, Products and Leftovers»"),
    ("Factors d'emissió", "Ministeri per a la Transició Ecològica: com es calcula la petjada de carboni", "https://www.miteco.gob.es · «Huella de carbono»"),
    ("Diòxid de carboni a l'atmosfera", "Laboratori de Monitoratge Global de la NOAA: la corba del CO₂ mesurat a Mauna Loa", "https://gml.noaa.gov · «Trends in CO₂»"),
    ("Corba de Keeling", "Viquipèdia en català: la història de les mesures de Charles David Keeling", VIQUI + " · «Corba de Keeling»"),
    ("Qualitat de l'aire a Barcelona", "Agència de Salut Pública de Barcelona: informes anuals i dades de les estacions", "https://www.aspb.cat"),
])

# ================================================================== SdA 4 · El patrimoni que es desfà
DOSSIER["sda4-20-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "El pH amb logaritmes.", "", [
        "Calcula el pH d'una dissolució d'HCl 0,010 mol/L.",
        "Calcula el pH d'una dissolució de NaOH 0,0010 mol/L.",
        "La pluja natural té [H⁺] = 2,5 · 10⁻⁶ mol/L. Quin pH té? Per què ja és una mica àcida? (Pista: el CO₂ de l'aire.)"], 6,
        tip("\\(\\text{pH} = -\\log\\,[\\text{H}^+]\\), amb [H⁺] en mol/L. A 25 °C, \\([\\text{H}^+] \\cdot [\\text{OH}^-] = 10^{-14}\\).")),
    rep(2, "Raonament", "Diluir no és neutralitzar.", "Diluïm 1 mL d'HCl 1 mol/L fins a 1 L, i després aquest litre fins a 1.000 L.", [
        "Quin pH té cada dissolució?",
        "Si continuéssim diluint, el pH podria arribar a 8? Per què?",
        "Per neutralitzar un vessament d'àcid al laboratori, és millor afegir-hi molta aigua o bicarbonat? Per què?"], 6),
    rep(3, "Càlcul", "Barregem àcid i base.", "Barregem 50 mL d'HCl 0,10 mol/L i 40 mL de NaOH 0,10 mol/L.", [
        "Quants mols d'H⁺ i d'OH⁻ hi ha? Quants n'hi sobren i de quin tipus?",
        "Quina concentració tenen en el volum total (90 mL)?",
        "Quin és el pH de la mescla? Quants mL més de NaOH caldrien per arribar a pH 7?"], 6),
    rep(4, "Càlcul", "Piles amb metalls diferents.", "El voltatge d'una pila en condicions estàndard és \\(E = E^\\circ_{\\text{càtode}} - E^\\circ_{\\text{ànode}}\\). "
        "El metall que s'oxida (ànode) és el de potencial més baix.", [
        "Calcula el voltatge de les piles Zn/Cu, Fe/Cu i Mg/Cu. Quin metall s'oxida en cada una?",
        "Quina pila faries amb aquests metalls per obtenir el voltatge més gran?",
        "Per què en una pila Zn/Cu la làmina de zinc perd massa i la de coure en guanya?"], 6,
        table(["Parell", "Mg²⁺/Mg", "Zn²⁺/Zn", "Fe²⁺/Fe", "Cu²⁺/Cu", "Ag⁺/Ag"], [["E° (V)", "−2,37", "−0,76", "−0,44", "+0,34", "+0,80"]])),
    rep(5, "Dades", "La regla dels 10 °C.", "Hem mesurat quant triga a desfer-se un tros de marbre en àcid clorhídric diluït a diferents temperatures:", [
        "Representa el temps en funció de la temperatura.",
        "Es compleix que la velocitat es duplica, aproximadament, cada vegada que la temperatura puja 10 °C? Justifica-ho amb les dades.",
        "Explica-ho amb la teoria de col·lisions i l'energia d'activació. Per què a l'estiu la pedra es degrada una mica més de pressa?"], 4,
        table(["Temperatura (°C)", "20", "30", "40", "50"], [["Temps (min)", "40", "21", "10", "5,5"]]) +
        graf((10, 60, 10), (0, 45, 5), "T (°C)", "t (min)")),
    rep(6, "Càlcul", "Quant marbre es menja la pluja?", "Suposem que sobre 1 m² d'una façana de marbre cauen 600 L de pluja a l'any (com a Barcelona) "
        "i que la pluja té un pH de 4,6. Reacció: CaCO₃ + 2 H⁺ → Ca²⁺ + CO₂ + H₂O.", [
        "Quina concentració d'H⁺ té la pluja? Quants mols d'H⁺ cauen en un any sobre 1 m²?",
        "Quants grams de CaCO₃ pot dissoldre aquesta pluja en un any? I en un segle?",
        "Per què el càlcul real és més complicat (vent, pluja que no toca la pedra, SO₂ sec…)?"], 6),
    rep(7, "Raonament", "La pàtina verda.", "L'Estàtua de la Llibertat de Nova York és de coure. Al principi era de color coure, però en uns trenta anys "
        "es va cobrir d'una pàtina verda de sals de coure, que la protegeix.", [
        "Escriu la semireacció d'oxidació del coure a Cu²⁺. És una oxidació o una reducció?",
        "Per què la pàtina del coure protegeix el metall i el rovell del ferro no?",
        "S'hauria de netejar la pàtina dels monuments de bronze de Barcelona? Argumenta-ho."], 6),
    rep(8, "Investiga", "La reacció rellotge.", "En la reacció rellotge de iode, la dissolució es torna blava de cop al cap d'un temps que depèn de les concentracions i de la temperatura.", [
        "Busca com funciona i cita la font.",
        "Dissenya un experiment per estudiar com afecta la concentració al temps de reacció. Quines variables controles?",
        "Quina mesura faries servir com a «velocitat» de la reacció?"], 6),
], [
    ("Escala de pH", "Simulació PhET: mesura el pH de productes de casa i mira què passa quan els dilueixes", PHET + " · «Escala de pH» (pH Scale)"),
    ("Pluja àcida", "Viquipèdia en català: com es forma i com afecta els monuments i els boscos", VIQUI + " · «Pluja àcida»"),
    ("Pila de Daniell", "Viquipèdia en català: la pila de zinc i coure i el pont salí", VIQUI + " · «Pila Daniell»"),
    ("Velocitat de reacció", "Simulació PhET: temperatura, concentració i energia d'activació amb partícules que xoquen", PHET + " · «Reactions & Rates»"),
    ("Agnes Pockels", "Viquipèdia en català: la científica que va estudiar les superfícies a la pica de la cuina", VIQUI + " · «Agnes Pockels»"),
    ("Qualitat de l'aire a Barcelona", "Agència de Salut Pública de Barcelona: diòxid de sofre i de nitrogen a les estacions", "https://www.aspb.cat"),
])

# ================================================================== SdA 5 · Com es tanca una ferida?
DOSSIER["sda5-22-ampliacio.pdf"] = dossier([
    rep(1, "Càlcul", "La rotonda: moviment circular uniforme.", "Un cotxe de 1.200 kg gira en una rotonda de 40 m de radi a 36 km/h.", [
        "Quant triga a fer una volta?",
        "Calcula l'acceleració centrípeta i la força centrípeta.",
        "Quin coeficient de fregament mínim cal perquè no derrapi?",
        "Si plou (μ = 0,4), pot girar a 36 km/h? I a 60 km/h? Dibuixa el diagrama de forces del cotxe vist des de dalt."], 8,
        tip("En un MCU la rapidesa és constant, però la velocitat canvia de direcció: hi ha una <b>acceleració centrípeta</b> cap al centre, "
            "\\(a_c = \\dfrac{v^2}{r}\\), i cal una <b>força centrípeta</b> \\(F_c = m\\,\\dfrac{v^2}{r}\\). Quan un cotxe gira, aquesta força la fa "
            "el fregament dels pneumàtics amb l'asfalt. El període és \\(T = \\dfrac{2\\pi r}{v}\\).")),
    rep(2, "Càlcul", "La gravitació.", "Newton va descobrir que la força que fa caure una poma és la mateixa que manté la Lluna en òrbita.", [
        "Calcula g a la superfície de la Terra.",
        "L'Estació Espacial Internacional vola a uns 400 km d'altura. Calcula-hi g. Si és gairebé igual que aquí, per què els astronautes suren? (Pista: caiguda lliure.)",
        "Quina força gravitatòria fan dues cèl·lules veïnes de 10⁻¹² kg separades 20 µm? Compara-la amb els nanonewtons de les forces de tracció (fitxa 7)."], 7,
        tip("\\(F = G\\,\\dfrac{m_1 m_2}{r^2}\\), amb \\(G = 6{,}674 \\cdot 10^{-11}\\ \\text{N}\\cdot\\text{m}^2/\\text{kg}^2\\). A la superfície, \\(g = G\\,\\dfrac{M_T}{R_T^2}\\). "
            "\\(M_T = 5{,}97 \\cdot 10^{24}\\) kg; \\(R_T = 6{,}37 \\cdot 10^{6}\\) m.")),
    rep(3, "Càlcul", "Un satèl·lit geostacionari.", "Un satèl·lit geostacionari gira a 42.200 km del centre de la Terra i fa una volta cada 24 h: sempre és sobre el mateix punt.", [
        "Calcula'n la velocitat en km/s.",
        "Calcula'n l'acceleració centrípeta.",
        "Calcula g a aquesta distància amb la llei de la gravitació i compara-la amb l'acceleració centrípeta. Què en conclous?"], 6),
    rep(4, "Càlcul", "La llei de Stokes i la VSG.", "Suposa que un glòbul vermell és una esfera de 4 µm de radi, 75 kg/m³ més densa que el plasma, i que la viscositat del plasma és 1,2 · 10⁻³ Pa·s.", [
        "Calcula'n la velocitat límit en m/s i en mm/h.",
        "Compara-la amb la VSG de la fitxa 4.",
        "Quan hi ha inflamació, els glòbuls vermells s'apilen en grups. Per què això fa pujar la VSG? (Pista: com depèn v de r?)"], 6,
        tip("Una esfera petita de radi r que cau dins d'un líquid de viscositat η arriba a una velocitat límit "
            "\\(v = \\dfrac{2\\,r^2\\,\\Delta\\rho\\,g}{9\\,\\eta}\\), on Δρ és la diferència de densitat entre l'esfera i el líquid.")),
    rep(5, "Càlcul", "La sabatilla que llisca.", "Inclinem la taula del laboratori 3 fins a 40° i la sabatilla llisca. Durant el lliscament, el coeficient de fregament és μ = 0,5.", [
        "Dibuixa'n el diagrama de forces.",
        "Demostra que a = g · (sin α − μ · cos α) i calcula-la.",
        "Quant triga a recórrer els 60 cm de la taula si surt del repòs?"], 7),
    rep(6, "Càlcul", "De la taula a terra: un tir horitzontal.", "Una pilota rodola per una taula d'1,25 m d'alçada a 2,0 m/s i cau. "
        "El moviment horitzontal és un MRU i el vertical, una caiguda lliure: són independents.", [
        "Quant de temps triga a arribar a terra?",
        "A quina distància de la taula toca a terra?",
        "Si la pilota anés al doble de velocitat, trigaria més o menys a caure? I on cauria?"], 6),
], [
    ("Suma de vectors", "Simulació PhET: suma vectors amb components i fletxes", PHET + " · «Vector Addition»"),
    ("Moviment de projectils", "Simulació PhET: llançaments amb angle, resistència de l'aire i trajectòries", PHET + " · «Projectile Motion»"),
    ("Gravetat i òrbites", "Simulació PhET: el Sol, la Terra, la Lluna i els satèl·lits", PHET + " · «Gravity And Orbits»"),
    ("Forces i moviment: conceptes bàsics", "Simulació PhET: força resultant, fregament i acceleració", PHET + " · «Forces and Motion: Basics»"),
    ("Llei de Hooke", "Simulació PhET: molles en sèrie i en paral·lel, i la constant k", PHET + " · «Hooke's Law»"),
    ("Institut de Bioenginyeria de Catalunya", "On treballa el grup de Xavier Trepat: notícies i divulgació sobre les forces de les cèl·lules", "https://ibecbarcelona.eu"),
])

# ================================================================== SdA 6 · L'Ictineo de Monturiol
DOSSIER["sda6-19-ampliacio.pdf"] = dossier([
    rep(1, "Dades", "L'ordinador de busseig.", "Un ordinador de busseig ha registrat la pressió total en baixar al mar:", [
        "Representa la pressió en funció de la fondària.",
        "Calcula el pendent de la recta en Pa/m. Quin significat té?",
        "Amb el pendent i p = ρ · g · h, calcula la densitat de l'aigua. És aigua dolça o de mar?",
        "Quina pressió esperes a 40 m?"], 4,
        table(["Fondària (m)", "0", "5", "10", "15", "20", "25"], [["Pressió (bar)", "1,01", "1,52", "2,02", "2,52", "3,02", "3,53"]]) +
        graf((0, 30, 5), (0, 4, 0.5), "fondària (m)", "p (bar)")),
    rep(2, "Càlcul", "La bombolla que creix.", "Un bussejador deixa anar una bombolla de 2,0 cm³ a 20 m de fondària al mar (1.025 kg/m³). La temperatura no canvia.", [
        "Calcula la pressió total a 20 m.",
        "Quin volum tindrà la bombolla a la superfície? (Llei de Boyle: p₁V₁ = p₂V₂.)",
        "Per què els bussejadors no han de pujar mai aguantant la respiració?"], 6),
    rep(3, "Càlcul", "L'aire del llast.", "Per buidar el tanc de llast d'un submarí, s'hi bomba aire a pressió que empeny l'aigua cap a fora.", [
        "A quina pressió mínima s'ha de bombar l'aire a 30 m de fondària al mar?",
        "Si el tanc fa 2 m³, quin volum ocuparia aquest aire a la superfície?",
        "Per què l'Ictineo II necessitava molta energia per emergir des de fondàries grans?"], 6),
    rep(4, "Càlcul", "El globus aerostàtic.", "Un globus d'aire calent té un volum de 2.500 m³. L'aire de fora té una densitat d'1,2 kg/m³ i el de dins, de 0,95 kg/m³.", [
        "Quina empenta rep el globus? (g = 9,8 m/s²)",
        "Quin pes té l'aire calent de dins?",
        "Quina massa màxima (globus, cistella i persones) pot aixecar? Per què els globus volen més bé als matins freds?"], 6),
    rep(5, "Càlcul", "Surar al mar Mort.", "L'aigua del mar Mort té una densitat d'uns 1.240 kg/m³, i el cos humà, d'uns 1.010 kg/m³.", [
        "Quin percentatge del cos queda submergit al mar Mort?",
        "I al Mediterrani (1.025 kg/m³)?",
        "Quina densitat mitjana ha de tenir un submarí perquè suri al Mediterrani amb un 10 % del volum fora de l'aigua?"], 6),
    rep(6, "Càlcul", "El batiscaf Trieste.", "El 1960, el batiscaf Trieste va baixar fins a uns 10.900 m de fondària a la fossa de les Mariannes, amb Jacques Piccard i Don Walsh.", [
        "Quina pressió hidrostàtica hi havia? Quantes atmosferes són?",
        "Quina força feia l'aigua sobre una finestreta de 10 cm de radi? A quantes tones equival?",
        "El Trieste flotava gràcies a un dipòsit ple de gasolina, menys densa que l'aigua i gairebé incompressible. Per què no podia fer servir aire?"], 6),
    rep(7, "Càlcul", "Torricelli amb oli.", "Torricelli va mesurar la pressió atmosfèrica amb una columna de mercuri de 760 mm.", [
        "Quina altura tindria la columna d'un baròmetre fet amb oli (920 kg/m³) per equilibrar 1 atm (101.325 Pa)?",
        "I amb aigua? Per què no es fan baròmetres d'aigua?",
        "Per què la columna de Torricelli no depèn del gruix del tub?"], 5),
], [
    ("Sota pressió", "Simulació PhET: pressió en líquids diferents, a la Terra i en altres planetes", PHET + " · «Sota pressió» (Under Pressure)"),
    ("Flotabilitat", "Simulació PhET: empenta, densitat i flotació amb blocs de materials diferents", PHET + " · «Flotabilitat» (Buoyancy)"),
    ("Narcís Monturiol", "Viquipèdia en català: la vida de l'inventor i la història dels Ictineos", VIQUI + " · «Narcís Monturiol i Estarriol»"),
    ("Fossa de les Mariannes", "Viquipèdia en català: el punt més profund dels oceans i les immersions que hi han arribat", VIQUI + " · «Fossa de les Mariannes»"),
    ("Museu Marítim de Barcelona", "Història de la navegació, la construcció naval i el port de Barcelona", "https://www.mmb.cat"),
    ("Principi de Pascal", "Viquipèdia en català: la premsa hidràulica, els frens i altres aplicacions", VIQUI + " · «Principi de Pascal»"),
])
