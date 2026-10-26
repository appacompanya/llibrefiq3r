"""Contingut dels dossiers de teoria de 4t d'ESO. El fa servir gen_teoria_curs.py (CURS=4t)."""
import gen_teoria as GT
from gen_teoria import H, S, P, UL, OL, TIP, EX, F, T, TOC, KW, taula_familia
import figs
import teoria_figs as TF, teoria_figs2 as T2, teoria_figs3 as T3, teoria_figs4 as T4

def A(n): return GT.COL[n][1]
def DEF(t, h): return f'<div class="fbox" style="background:#fff"><b>{t}.</b> {h}</div>'
def FIG(svg, cap, w="150mm"): return figs.fig(svg, cap, w)
def fr(a, b): return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'

# ======================================================================== SdA 1
def sda1():
    a = A(1)
    b = H(1, "D'on surt el color d'un castell de focs? L'àtom i els seus models, els electrons i la llum, la configuració electrònica, la taula periòdica, l'enllaç i la formulació.")
    b += TOC("Els models atòmics", "Les partícules de l'àtom: Z i A", "Ions i isòtops. La massa atòmica", "La llum i els espectres", "El model de Bohr: salts d'electrons i colors",
             "La configuració electrònica", "La taula periòdica i els electrons", "L'enllaç químic i les propietats", "Formulació inorgànica: compostos binaris", "Formulació: hidròxids, oxoàcids i oxosals", "La química dels focs i el medi")
    b += S(1, "Els models atòmics")
    b += P("Ningú no ha vist mai un àtom tal com el dibuixem. Els científics construeixen <b>models</b>: representacions que expliquen els resultats dels experiments. Quan un experiment nou no encaixa amb el model, cal canviar-lo. La història de l'àtom és un bon exemple de com avança la ciència.")
    b += FIG(T4.models_atomics(a), "Evolució dels models atòmics.", "165mm")
    b += T(["Model", "Com és l'àtom", "Què va obligar a canviar-lo"],
           [["Dalton (1808)", "Esferes massisses i indivisibles; cada element té àtoms d'una massa pròpia.", "El descobriment de l'electró (Thomson, 1897, amb els raigs catòdics): l'àtom té parts."],
            ["Thomson (1904)", "Esfera de càrrega positiva amb els electrons incrustats, com les panses d'un pastís.", "L'experiment de la làmina d'or de Rutherford (1909–1911): algunes partícules alfa reboten."],
            ["Rutherford (1911)", "Nucli molt petit, dens i positiu; els electrons giren al voltant; la major part de l'àtom és buida.", "No explica per què els electrons no cauen al nucli ni els espectres de línies."],
            ["Bohr (1913)", "Els electrons giren en òrbites de radi i energia fixos (nivells); no emeten energia mentre hi són.", "No funciona bé per als àtoms amb molts electrons."],
            ["Actual (mecanoquàntic)", "Els electrons ocupen <b>orbitals</b>: zones on és probable trobar-los, agrupats en nivells i subnivells.", "—"]], w=["18%", "46%", "36%"])
    b += FIG(T2.rutherford(a), "L'experiment de Rutherford: la majoria de partícules travessen l'or, però algunes reboten en el nucli.", "140mm")
    b += S(2, "Les partícules de l'àtom: Z i A")
    b += T(["Partícula", "Lloc", "Càrrega", "Massa relativa"], [["Protó (p⁺)", "nucli", "+1", "1"], ["Neutró (n)", "nucli", "0", "1"], ["Electró (e⁻)", "escorça", "−1", "1/1 836 (gairebé zero)"]])
    b += UL("El <b>nombre atòmic (Z)</b> és el nombre de protons. Identifica l'element: tots els àtoms de carboni tenen Z = 6. En un àtom neutre, també és el nombre d'electrons.",
            "El <b>nombre màssic (A)</b> és el nombre de protons més neutrons: A = Z + N. Gairebé tota la massa de l'àtom és al nucli.")
    b += P("Ho escrivim així: \\( {}^{A}_{Z}\\mathrm{X} \\). Per exemple, \\( {}^{23}_{11}\\mathrm{Na} \\) té 11 protons, 11 electrons i 23 − 11 = 12 neutrons.")
    b += S(3, "Ions i isòtops. La massa atòmica")
    b += UL("Un <b>ió</b> és un àtom que ha guanyat o perdut electrons. Si en perd, queda amb càrrega positiva (<b>catió</b>: Na⁺, Ca²⁺); si en guanya, amb càrrega negativa (<b>anió</b>: Cl⁻, O²⁻). El nucli no canvia.",
            "Els <b>isòtops</b> són àtoms del mateix element (mateix Z) amb diferent nombre de neutrons (diferent A). Tenen les mateixes propietats químiques.")
    b += FIG(T4.isotops(a), "Els tres isòtops de l'hidrogen.", "155mm")
    b += P("La <b>massa atòmica</b> que surt a la taula periòdica és la mitjana ponderada de les masses dels isòtops naturals de l'element, segons la seva abundància. S'expressa en unitats de massa atòmica (u).")
    b += EX("Exemple · El coure", "El coure natural té un 69,2 % de ⁶³Cu (62,93 u) i un 30,8 % de ⁶⁵Cu (64,93 u). Massa atòmica = 0,692 · 62,93 + 0,308 · 64,93 ≈ 63,55 u. Per això a la taula no surt un nombre enter.")
    b += S(4, "La llum i els espectres")
    b += P("La llum és una ona electromagnètica. Cada color correspon a una <b>longitud d'ona</b> (des d'uns 400 nm, el violeta, fins a uns 700 nm, el vermell) i a una <b>energia</b>: la llum violeta en porta més que la vermella. Si fem passar la llum per un prisma o per un CD (que fa d'<b>espectroscopi</b>), se separa en els seus colors i en veiem l'<b>espectre</b>.")
    b += UL("Un sòlid incandescent (el filament d'una bombeta, el Sol) fa un <b>espectre continu</b>, amb tots els colors.",
            "Un gas escalfat o excitat amb electricitat fa un <b>espectre de línies</b>: només uns quants colors, propis de cada element. És com la seva empremta dactilar.")
    b += FIG(T4.espectres(a), "Espectre continu i espectres d'emissió de l'hidrogen i del sodi.", "160mm")
    b += S(5, "El model de Bohr: salts d'electrons i colors")
    b += P("Bohr va explicar els espectres de línies. Els electrons només poden ocupar uns <b>nivells d'energia</b> determinats (n = 1, 2, 3…). Quan reben energia (d'una flama o d'un corrent elèctric), salten a un nivell superior; són inestables i tornen a baixar, i aleshores emeten l'energia sobrant en forma de llum. Com que els nivells són fixos, els salts també ho són, i per això cada element emet uns colors concrets.")
    b += FIG(T4.salts_electrons(a), "Absorció i emissió d'energia en els salts d'electrons.", "155mm")
    b += F("E<sub>llum</sub> = E<sub>nivell superior</sub> − E<sub>nivell inferior</sub>", note="Salt gran → llum de més energia (blava, violeta) · salt petit → llum de menys energia (vermella)")
    b += P("Això explica el repte: a cada carcassa dels focs hi ha sals de metalls diferents. En cremar, la calor excita els electrons dels metalls, que emeten el seu color. L'<b>assaig a la flama</b> fa el mateix al laboratori:")
    b += T(["Metall", "Color a la flama", "Sal habitual als focs"], [["Liti", "vermell carmí", "carbonat de liti"], ["Sodi", "groc ataronjat", "(contaminant: tapa altres colors)"], ["Potassi", "lila", "nitrat de potassi (oxidant)"],
            ["Calci", "taronja", "clorur de calci"], ["Estronci", "vermell intens", "nitrat d'estronci, Sr(NO₃)₂"], ["Bari", "verd", "nitrat de bari"], ["Coure", "verd blavós / blau", "clorur de coure(I), CuCl"]])
    b += TIP("La ciència la fan persones", "Cecilia Payne-Gaposchkin (1900–1979) va analitzar els espectres dels estels i el 1925 va concloure que estan fets sobretot d'hidrogen i heli. Al principi no la van creure; anys després es va confirmar que tenia raó.")
    b += S(6, "La configuració electrònica")
    b += P("Al model actual, cada nivell (n = 1, 2, 3…) es divideix en <b>subnivells</b>: s, p, d i f, que poden tenir com a màxim 2, 6, 10 i 14 electrons. La <b>configuració electrònica</b> indica com es reparteixen els electrons d'un àtom. Els electrons ocupen primer els subnivells de menys energia, seguint l'ordre del <b>diagrama de Moeller</b>:")
    b += FIG(T4.moeller(a), "Diagrama de Moeller: ordre d'ompliment dels subnivells.", "145mm")
    b += EX("Exemples", "O (Z = 8): 1s² 2s² 2p⁴ · Cl (Z = 17): 1s² 2s² 2p⁶ 3s² 3p⁵ · Ca (Z = 20): 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² · Fe (Z = 26): 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶.")
    b += P("Els <b>electrons de valència</b> són els del nivell més extern (el de n més gran). Són els que participen en les reaccions i els enllaços. Els <b>gasos nobles</b> tenen el nivell extern complet (s² p⁶, vuit electrons, excepte l'heli, amb dos) i són molt estables: gairebé no reaccionen.",
           "Els altres àtoms tendeixen a guanyar, perdre o compartir electrons per quedar amb la configuració del gas noble més proper (<b>regla de l'octet</b>). El sodi (3s¹) perd un electró i queda Na⁺ (1s² 2s² 2p⁶, com el neó); el clor (3s² 3p⁵) en guanya un i queda Cl⁻ (com l'argó).")
    b += S(7, "La taula periòdica i els electrons")
    b += P("Mendeléiev va ordenar els elements el 1869 per massa i per propietats, i va deixar forats per a elements encara desconeguts. Avui els ordenem per nombre atòmic, i la configuració electrònica explica per què funciona:")
    b += UL("El <b>període</b> (fila) és el nivell més alt ocupat per electrons: el sodi (…3s¹) és del període 3.",
            "Els elements d'un mateix <b>grup</b> (columna) tenen la mateixa configuració de valència i, per tant, propietats semblants: tots els alcalins acaben en s¹ i perden fàcilment un electró.",
            "El <b>bloc</b> depèn del subnivell on entra l'últim electró: s, p, d o f.")
    b += FIG(T4.blocs_taula(a), "Els blocs s, p, d i f de la taula periòdica.", "165mm")
    b += taula_familia()
    b += P("A l'esquerra i al centre hi ha els <b>metalls</b>, que tendeixen a perdre electrons i formar cations; a la dreta, els <b>no metalls</b>, que tendeixen a guanyar-ne i formar anions (excepte els gasos nobles). La <b>valència</b> d'un element és el nombre d'electrons que tendeix a guanyar, perdre o compartir: grup 1 → +1, grup 2 → +2, grup 13 → +3, grup 16 → −2, grup 17 → −1.")
    b += S(8, "L'enllaç químic i les propietats")
    b += P("Els àtoms s'uneixen per quedar més estables. El tipus d'enllaç depèn de quins àtoms s'uneixen i explica les propietats de la substància:")
    b += FIG(T2.enllacos(a), "Els tres tipus d'enllaç.", "155mm")
    b += T(["", "Iònic", "Covalent", "Metàl·lic"],
           [["Entre", "metall + no metall", "no metall + no metall", "metall + metall"], ["Com", "el metall cedeix electrons al no metall; els ions s'atrauen", "els àtoms comparteixen parells d'electrons", "els àtoms deixen electrons lliures que es mouen per tot el metall"],
            ["Formen", "xarxes cristal·lines (NaCl, KNO₃)", "molècules (H₂O, CO₂) o xarxes covalents (diamant, SiO₂)", "xarxes metàl·liques (Fe, Cu, Al)"],
            ["Propietats", "sòlids durs i fràgils; T de fusió alta; condueixen fosos o dissolts; molts es dissolen en aigua", "moleculars: T de fusió baixa, no condueixen; xarxes covalents: molt dures", "condueixen el corrent i la calor; dúctils i mal·leables; brillants"]], w=["13%", "29%", "29%", "29%"])
    b += EX("Exemple · Una carcassa de focs", "El nitrat de potassi (iònic) és un sòlid que es dissol a l'aigua i, fos, condueix; el carboni i el sofre de la pólvora formen substàncies covalents que no condueixen; el magnesi i l'alumini (metàl·lics) fan espurnes blanques i brillants.")
    b += S(9, "Formulació inorgànica: compostos binaris")
    b += P("La <b>IUPAC</b> (Unió Internacional de Química Pura i Aplicada) fixa les normes per escriure (formular) i anomenar els compostos. A la fórmula, l'element menys electronegatiu (més a l'esquerra de la taula) s'escriu primer. El <b>nombre d'oxidació</b> és la càrrega que tindria un àtom si tots els seus enllaços fossin iònics; la suma dels nombres d'oxidació d'un compost neutre és zero.")
    b += T(["Element", "Nombres d'oxidació habituals"], [["H", "+1 (−1 amb metalls)"], ["O", "−2"], ["Grup 1 (Li, Na, K)", "+1"], ["Grup 2 (Mg, Ca, Sr, Ba)", "+2"], ["Al", "+3"],
            ["Fe", "+2, +3"], ["Cu", "+1, +2"], ["F, Cl, Br, I (amb metalls)", "−1"], ["S (amb metalls)", "−2"], ["N (amb metalls)", "−3"]], w=["45%", "55%"])
    b += P("Hi ha dues nomenclatures habituals: amb <b>prefixos</b> (mono-, di-, tri-, tetra-, penta-…) i amb el <b>nombre d'oxidació</b> en xifres romanes entre parèntesis, si l'element en té més d'un.")
    b += T(["Tipus", "Fórmula", "Amb prefixos", "Amb nombre d'oxidació"],
           [["Òxid", "Fe₂O₃", "triòxid de diferro", "òxid de ferro(III)"], ["Òxid", "CO₂", "diòxid de carboni", "—"], ["Òxid", "CaO", "òxid de calci", "òxid de calci"],
            ["Hidrur metàl·lic", "NaH", "hidrur de sodi", "hidrur de sodi"], ["Hidrurs especials", "NH₃ · CH₄ · H₂O", "amoníac · metà · aigua (noms acceptats)", ""],
            ["Hidràcid (dissolt)", "HCl", "clorur d'hidrogen", "àcid clorhídric"], ["Sal binària", "CuCl", "clorur de coure", "clorur de coure(I)"], ["Sal binària", "SrCl₂", "diclorur d'estronci", "clorur d'estronci"]], w=["20%", "18%", "30%", "32%"])
    b += TIP("Com escriure la fórmula", "Escriu els símbols, posa els nombres d'oxidació, i creua'ls com a subíndexs (simplificant si es pot): Al³⁺ i O²⁻ → Al₂O₃; Ca²⁺ i Cl⁻ → CaCl₂; Ca²⁺ i O²⁻ → Ca₂O₂ → CaO.")
    b += S(10, "Formulació: hidròxids, oxoàcids i oxosals")
    b += UL("<b>Hidròxids:</b> metall + grup hidròxid (OH⁻). NaOH, hidròxid de sodi; Ca(OH)₂, hidròxid de calci; Fe(OH)₃, hidròxid de ferro(III).",
            "<b>Oxoàcids:</b> hidrogen + no metall + oxigen. Cal conèixer-ne alguns: HNO₃ (àcid nítric), H₂CO₃ (àcid carbònic), H₂SO₄ (àcid sulfúric), HClO₄ (àcid perclòric).",
            "<b>Oxosals:</b> substitueixen l'hidrogen de l'oxoàcid per un metall. L'anió canvia de terminació: <b>-ic → -at</b> (i -ós → -it).")
    b += T(["Oxoàcid", "Anió", "Exemple d'oxosal"], [["HNO₃, àcid nítric", "NO₃⁻, nitrat", "KNO₃, nitrat de potassi · Sr(NO₃)₂, nitrat d'estronci"], ["H₂CO₃, àcid carbònic", "CO₃²⁻, carbonat", "CaCO₃, carbonat de calci · Li₂CO₃, carbonat de liti"],
            ["H₂SO₄, àcid sulfúric", "SO₄²⁻, sulfat", "CuSO₄, sulfat de coure(II) · CaSO₄, sulfat de calci"], ["HClO₄, àcid perclòric", "ClO₄⁻, perclorat", "KClO₄, perclorat de potassi"]], w=["28%", "22%", "50%"])
    b += EX("Exemple · La recepta d'una estrella vermella", "Nitrat d'estronci, Sr(NO₃)₂ (dona el color vermell i és oxidant), perclorat de potassi, KClO₄ (oxidant), un combustible (carbó o magnesi) i un aglutinant. La <b>pólvora</b> clàssica és una mescla de nitrat de potassi, carbó i sofre.")
    b += S(11, "La química dels focs i el medi")
    b += P("Els focs artificials són química aplicada, però tenen una cara fosca. En esclatar deixen a l'aire partícules fines amb metalls (estronci, bari, coure, potassi) i fum. La investigadora <b>Teresa Moreno</b> (IDAEA-CSIC) ha mesurat a Barcelona i en altres ciutats com augmenten aquests metalls a l'aire durant les revetlles i els castells de focs. A més, el <b>perclorat</b> que queda pot arribar a l'aigua i alterar la tiroide.",
           "Per fer focs més nets es treballa en oxidants sense perclorat, colors sense bari, menys fum i espectacles de drons o làser. Argumentar sobre aquests temes vol dir fer servir <b>dades</b> i fonts fiables, no només opinions.")
    b += KW(("Model atòmic", "representació de l'àtom que explica els experiments"), ("Nombre atòmic (Z)", "nombre de protons"), ("Nombre màssic (A)", "protons + neutrons"), ("Ió", "àtom amb càrrega per haver guanyat o perdut electrons"),
            ("Isòtops", "mateix Z, diferent nombre de neutrons"), ("Espectre de línies", "colors propis que emet un element"), ("Configuració electrònica", "repartiment dels electrons en nivells i subnivells"),
            ("Electrons de valència", "electrons del nivell més extern"), ("Enllaç iònic", "transferència d'electrons entre metall i no metall"), ("Oxosal", "sal d'un oxoàcid: nitrats, carbonats, sulfats…"))
    return b

# ======================================================================== SdA 2
def sda2():
    a = A(2)
    b = H(2, "Val la pena comprar aigua embotellada? Les dissolucions, la concentració, el mol i la molaritat, la conductivitat, la duresa i les fonts fiables.")
    b += TOC("Mescles, dissolucions i col·loides", "Què diu l'etiqueta d'una aigua", "La concentració: g/L, %, ppm", "Preparar i diluir dissolucions", "La quantitat de substància: el mol",
             "La massa molar", "La molaritat", "La conductivitat i la recta de calibratge", "La duresa de l'aigua", "L'aigua de l'aixeta: qualitat, preu i residus")
    b += S(1, "Mescles, dissolucions i col·loides")
    b += P("Classifiquem les mescles segons la mida de les partícules disperses:")
    b += T(["", "Dissolució", "Col·loide", "Suspensió"],
           [["Mida de les partícules", "&lt; 1 nm (ions, molècules)", "1 nm – 1 µm", "&gt; 1 µm"], ["Aspecte", "transparent, homogènia", "sembla homogènia; tèrbola o opaca", "tèrbola, heterogènia"],
            ["Sedimenta?", "no", "no", "sí, amb el temps"], ["Es filtra?", "no", "no (amb paper normal)", "sí"], ["Efecte Tyndall", "no", "sí", "sí"], ["Exemples", "aigua mineral, aire, vinagre", "llet, maionesa, boira, gelatina", "aigua amb sorra, suc de taronja"]], w=["22%", "26%", "26%", "26%"])
    b += P("L'<b>efecte Tyndall</b> és la dispersió de la llum per les partícules d'un col·loide: si hi fem passar un làser, veiem el feix. En una dissolució, no. Així els distingim.")
    b += FIG(T4.tyndall(a), "Efecte Tyndall: el feix es veu en un col·loide però no en una dissolució.", "140mm")
    b += S(2, "Què diu l'etiqueta d'una aigua")
    b += P("L'aigua mineral és una dissolució: porta ions dissolts, que l'etiqueta indica en <b>mg/L</b>. Els principals són els cations calci (Ca²⁺), magnesi (Mg²⁺), sodi (Na⁺) i potassi (K⁺), i els anions bicarbonat (HCO₃⁻), sulfat (SO₄²⁻), clorur (Cl⁻) i nitrat (NO₃⁻).",
           "El <b>residu sec</b> és la massa de sals que queda en evaporar 1 L d'aigua a 180 °C. Segons el residu sec, l'aigua és de mineralització <b>molt feble</b> (&lt; 50 mg/L), <b>feble</b> (50–500 mg/L), <b>mitjana</b> (500–1 500 mg/L) o <b>forta</b> (&gt; 1 500 mg/L). Si evaporem l'aigua, els ions es combinen i formen sals: carbonat de calci (CaCO₃), sulfat de magnesi (MgSO₄), clorur de sodi (NaCl)…")
    b += S(3, "La concentració: g/L, % i ppm")
    b += P("La <b>concentració</b> indica la quantitat de solut que hi ha en una quantitat de dissolució. Segons el cas, la donem de maneres diferents:")
    b += T(["Forma", "Fórmula", "On la trobem"],
           [["Massa per volum (g/L, mg/L)", f"c = {fr('massa de solut', 'volum de dissolució')}", "etiquetes d'aigua, anàlisis"],
            ["Percentatge en massa", f"% massa = {fr('massa de solut', 'massa de dissolució')} · 100", "sèrum fisiològic (0,9 %), aliments"],
            ["Percentatge en volum", f"% volum = {fr('volum de solut', 'volum de dissolució')} · 100", "begudes alcohòliques, alcohol de farmàcia"],
            ["Parts per milió (ppm)", f"ppm = {fr('massa de solut', 'massa de dissolució')} · 10⁶", "contaminants; en aigua, 1 ppm ≈ 1 mg/L"]], w=["26%", "44%", "30%"])
    b += EX("Exemple 1", "El sèrum fisiològic té un 0,9 % en massa de NaCl: en 100 g de sèrum hi ha 0,9 g de sal. Per fer-ne 500 g cal 0,9 · 500 / 100 = 4,5 g de NaCl.")
    b += EX("Exemple 2", "Una cervesa de 330 mL té un 5 % en volum d'alcohol: 5 · 330 / 100 = 16,5 mL d'etanol.")
    b += EX("Exemple 3", "Una aigua té 25 mg/L de nitrats. El límit legal és 50 mg/L (Reial decret 3/2023): compleix, amb un marge del 50 %.")
    b += S(4, "Preparar i diluir dissolucions")
    b += P("Per preparar una dissolució d'una concentració exacta fem servir la balança i un <b>matràs aforat</b>, que només té una marca i mesura un volum molt precís.")
    b += FIG(T4.preparar_dissolucio(a), "Passos per preparar una dissolució.", "155mm")
    b += P("<b>Diluir</b> és afegir dissolvent. La quantitat de solut no canvia; només es reparteix en més volum. Per això:")
    b += F("c₁ · V₁ = c₂ · V₂", note="c₁ i V₁: dissolució concentrada · c₂ i V₂: dissolució diluïda (mateixes unitats als dos costats)")
    b += FIG(T4.dilucio(a), "En diluir, el solut és el mateix però en més volum.", "150mm")
    b += EX("Exemple", "Quin volum de sèrum de 9 g/L cal per preparar 250 mL de 3 g/L? V₁ = c₂ · V₂ / c₁ = 3 · 250 / 9 ≈ 83 mL; hi afegim aigua fins a 250 mL.")
    b += S(5, "La quantitat de substància: el mol")
    b += P("Els àtoms i les molècules són tan petits que no els podem comptar un per un. Igual que comptem els ous per dotzenes, els químics compten les partícules per <b>mols</b>.")
    b += DEF("Mol", "és la quantitat de substància que conté 6,022 · 10²³ partícules (àtoms, molècules o ions). Aquest nombre és el <b>nombre d'Avogadro</b>, N<sub>A</sub>. El mol és la unitat de quantitat de substància del SI.")
    b += F(f"N = n · N<sub>A</sub>", f"n = {fr('N', 'N<sub>A</sub>')}", note="N: nombre de partícules · n: nombre de mols · N<sub>A</sub> = 6,022 · 10²³ partícules/mol")
    b += S(6, "La massa molar")
    b += P("La <b>massa molar</b> (M) és la massa d'un mol d'una substància, en g/mol. Numèricament és igual a la massa atòmica o molecular (en u). Per calcular la massa molecular sumem les masses atòmiques de tots els àtoms de la fórmula.")
    b += EX("Exemples", "H₂O: 2 · 1 + 16 = 18 g/mol · NaCl: 23 + 35,5 = 58,5 g/mol · CaCO₃: 40 + 12 + 3 · 16 = 100 g/mol · CO₂: 12 + 2 · 16 = 44 g/mol.")
    b += FIG(T4.mol_mostres(a), "Un mol de diferents substàncies: el mateix nombre de partícules, masses diferents.", "155mm")
    b += F(f"n = {fr('m', 'M')}", note="n: mols · m: massa (g) · M: massa molar (g/mol)")
    b += EX("Exemple 1 · Un got d'aigua", "Quantes molècules hi ha en un got de 250 g d'aigua? n = 250 / 18 ≈ 13,9 mol. N = 13,9 · 6,022 · 10²³ ≈ 8,4 · 10²⁴ molècules.")
    b += EX("Exemple 2 · El calci", "Una aigua té 80 mg/L de Ca²⁺ (M = 40 g/mol). En 1 L: n = 0,080 / 40 = 0,002 mol = 2 · 10⁻³ mol; N = 2 · 10⁻³ · 6,022 · 10²³ ≈ 1,2 · 10²¹ ions de calci.")
    b += S(7, "La molaritat")
    b += P("En química, la manera més útil d'expressar la concentració és en <b>mols de solut per litre de dissolució</b>: la <b>molaritat</b>. Ens diu quantes partícules de solut hi ha, cosa important per a les reaccions.")
    b += F(f"c = {fr('n (mol de solut)', 'V (L de dissolució)')}", note="Unitat: mol/L (també s'escriu M) · c₁ · V₁ = c₂ · V₂ també serveix en mol/L")
    b += EX("Exemple 1", "Dissolem 5,85 g de NaCl fins a 250 mL. n = 5,85 / 58,5 = 0,100 mol; c = 0,100 / 0,250 = 0,400 mol/L.")
    b += EX("Exemple 2", "Quina massa de glucosa (C₆H₁₂O₆, M = 180 g/mol) cal per fer 500 mL de dissolució 0,2 mol/L? n = c · V = 0,2 · 0,5 = 0,1 mol; m = n · M = 0,1 · 180 = 18 g.")
    b += EX("Exemple 3 · Una anàlisi de sang", "La glucosa en sang en dejú és normal entre 70 i 100 mg/dL. 90 mg/dL = 0,90 g/L; en mol/L: 0,90 / 180 = 0,005 mol/L = 5 mmol/L, la unitat que fan servir molts laboratoris europeus.")
    b += S(8, "La conductivitat i la recta de calibratge")
    b += P("L'aigua pura gairebé no condueix el corrent elèctric. Els ions dissolts sí que el condueixen: com més ions, més <b>conductivitat</b> (es mesura en µS/cm amb un conductímetre). Per això la conductivitat ens dona una idea ràpida de la mineralització d'una aigua.",
           "Per saber la concentració d'una mostra fem una <b>recta de calibratge</b>: preparem dissolucions <b>patró</b> de concentració coneguda, en mesurem la conductivitat i dibuixem la gràfica. Després mesurem la mostra i hi llegim la concentració. És un mètode que fan servir molts laboratoris d'anàlisi.")
    b += FIG(T4.recta_calibratge(a), "Recta de calibratge de conductivitat amb dissolucions de NaCl.", "150mm")
    b += S(9, "La duresa de l'aigua")
    b += P("La <b>duresa</b> d'una aigua és la quantitat d'ions calci (Ca²⁺) i magnesi (Mg²⁺) que porta. S'expressa en <b>graus francesos</b> (°F): 1 °F equival a 10 mg/L de carbonat de calci. Una aigua és tova per sota d'uns 15 °F i dura per sobre de 30 °F. L'aigua de Barcelona és força dura (uns 30–45 °F, segons el barri i l'origen de l'aigua).",
           "L'aigua dura no és perjudicial per a la salut, però fa <b>calç</b> (incrustacions de CaCO₃ a les aixetes, rentadores i escalfadors) i fa menys escuma amb el sabó, perquè el calci i el magnesi formen sals insolubles amb el sabó. Al laboratori comparem la duresa comptant les gotes de sabó que calen per fer escuma persistent.")
    b += S(10, "L'aigua de l'aixeta: qualitat, preu i residus")
    b += P("L'aigua de l'aixeta a Catalunya ha de complir els valors del <b>Reial decret 3/2023</b>, que fixa uns 50 paràmetres (microbiològics, químics i indicadors) i obliga a fer-ne controls freqüents. A Barcelona es poden consultar els resultats per barri al web d'Aigües de Barcelona.",
           "Per decidir amb criteri cal mirar <b>dades</b>: el preu de l'aigua de l'aixeta és d'uns 2 € per metre cúbic (0,002 € el litre), mentre que l'embotellada costa entre 0,20 i 0,60 € el litre, unes 100–300 vegades més. A més, una família que beu aigua embotellada pot llençar centenars d'ampolles de plàstic a l'any. Si el gust de clor molesta, es pot deixar l'aigua en una gerra a la nevera unes hores o fer servir un filtre.")
    b += TIP("Les fonts fiables", "Per avaluar una font, pregunta't qui ho diu (institució, empresa, expert?), quan ho diu (és actual?), per què (vol vendre alguna cosa?) i amb quines proves (dona dades i referències?). Una anàlisi oficial és més fiable que un anunci o un vídeo sense fonts.")
    b += KW(("Dissolució", "mescla homogènia amb partícules &lt; 1 nm"), ("Col·loide", "mescla amb partícules d'1 nm a 1 µm; fa efecte Tyndall"), ("Residu sec", "sals que queden en evaporar 1 L d'aigua"), ("ppm", "parts per milió; en aigua, ≈ mg/L"),
            ("Mol", "6,022 · 10²³ partícules"), ("Massa molar", "massa d'un mol, en g/mol"), ("Molaritat", "mols de solut per litre de dissolució"), ("Diluir", "afegir dissolvent: c₁ · V₁ = c₂ · V₂"),
            ("Recta de calibratge", "gràfica amb patrons per trobar una concentració"), ("Duresa", "contingut de Ca²⁺ i Mg²⁺; en °F"))
    return b

# ======================================================================== SdA 3
def sda3():
    a = A(3)
    b = H(3, "Quant CO₂ emet cada manera d'arribar a l'institut? Les equacions en mols, la química del carboni, les combustions, l'estequiometria i l'energia de les reaccions.")
    b += TOC("Les reaccions químiques i la llei de Lavoisier", "Ajustar equacions", "Llegir una equació: molècules, mols i grams", "La química del carboni", "Formulació dels hidrocarburs i els alcohols",
             "Les combustions", "Estequiometria: càlculs amb equacions", "El reactiu limitant", "De la gasolina al CO₂", "L'energia de les reaccions", "La mobilitat, l'aire i la salut")
    b += S(1, "Les reaccions químiques i la llei de Lavoisier")
    b += P("En una <b>reacció química</b> unes substàncies (els <b>reactius</b>) es transformen en unes altres (els <b>productes</b>). Els enllaços dels reactius es trenquen i els àtoms es reorganitzen formant enllaços nous. Els àtoms no es creen ni es destrueixen; per això es compleix la <b>llei de conservació de la massa</b> (Lavoisier, 1789): la massa total dels reactius és igual a la massa total dels productes.")
    b += FIG(T3.reaccio_model(a), "Model de la combustió del metà: els àtoms es reorganitzen.", "150mm")
    b += S(2, "Ajustar equacions")
    b += P("Una equació química està <b>ajustada</b> quan hi ha el mateix nombre d'àtoms de cada element a cada costat. Per ajustar-la posem <b>coeficients</b> davant de les fórmules; no podem canviar mai els subíndexs, perquè canviaríem la substància.")
    b += OL("Escriu les fórmules correctes dels reactius i els productes.", "Ajusta primer els elements que surten en una sola substància a cada costat (sovint C i després H).", "Deixa l'oxigen i els elements sols per al final.", "Comprova àtom per àtom.")
    b += EX("Exemple", "Combustió del propà: C₃H₈ + O₂ → CO₂ + H₂O. Carboni: 3 CO₂. Hidrogen: 8 H → 4 H₂O. Oxigen a la dreta: 3 · 2 + 4 = 10 → 5 O₂. Resultat: C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O.")
    b += S(3, "Llegir una equació: molècules, mols i grams")
    b += P("Els coeficients d'una equació ajustada indiquen la proporció en què reaccionen les partícules i, per tant, també els <b>mols</b>. Amb les masses molars ho podem passar a <b>grams</b> i comprovar la llei de Lavoisier.")
    b += T(["", "CH₄", "+ 2 O₂", "→ CO₂", "+ 2 H₂O"],
           [["Molècules", "1", "2", "1", "2"], ["Mols", "1 mol", "2 mol", "1 mol", "2 mol"], ["Grams", "16 g", "2 · 32 = 64 g", "44 g", "2 · 18 = 36 g"], ["Total", "80 g de reactius", "", "80 g de productes", ""]])
    b += S(4, "La química del carboni")
    b += P("El carboni té 4 electrons de valència i forma <b>4 enllaços covalents</b>. Es pot unir amb altres carbonis formant cadenes llargues, ramificades o tancades, amb enllaços simples, dobles o triples. Per això hi ha milions de compostos de carboni: la <b>química orgànica</b> estudia els combustibles, els plàstics, els medicaments i les molècules dels éssers vius.",
           "Els <b>hidrocarburs</b> són compostos de carboni i hidrogen. Són la base dels combustibles: el gas natural (metà), el butà i el propà de les bombones, la gasolina i el gasoil (mescles d'hidrocarburs de 5 a 20 carbonis, aproximadament).")
    b += FIG(T4.hidrocarburs(a), "Fórmules desenvolupades d'alguns hidrocarburs i de l'etanol.", "170mm")
    b += S(5, "Formulació dels hidrocarburs i els alcohols")
    b += P("El nom indica el <b>nombre de carbonis</b> (prefix) i el <b>tipus d'enllaç</b> o grup (terminació):")
    b += T(["Carbonis", "Prefix", "Alcà (-à): simple", "Alquè (-è): doble", "Alquí (-í): triple", "Alcohol (-ol): –OH"],
           [["1", "met-", "metà CH₄", "—", "—", "metanol CH₃OH"], ["2", "et-", "età CH₃–CH₃", "etè CH₂=CH₂", "etí CH≡CH", "etanol CH₃–CH₂OH"], ["3", "prop-", "propà CH₃–CH₂–CH₃", "propè CH₂=CH–CH₃", "propí CH≡C–CH₃", "propan-1-ol"],
            ["4", "but-", "butà C₄H₁₀", "but-1-è", "but-1-í", "butan-1-ol"], ["5", "pent-", "pentà C₅H₁₂", "", "", ""], ["8", "oct-", "octà C₈H₁₈ (gasolina)", "", "", ""]], w=["10%", "10%", "22%", "20%", "18%", "20%"])
    b += P("Els alcans tenen de fórmula general C<sub>n</sub>H<sub>2n+2</sub>. Quan cal, un nombre indica la posició del doble enllaç, del triple o del grup –OH (but-1-è, propan-2-ol), comptant des de l'extrem més proper. L'<b>etanol</b> és l'alcohol de les begudes i també un biocombustible que es barreja amb la gasolina.")
    b += S(6, "Les combustions")
    b += P("Una <b>combustió</b> és una reacció d'un combustible amb l'oxigen que desprèn molta energia. Si hi ha prou oxigen, la combustió és <b>completa</b> i els productes d'un hidrocarbur o d'un alcohol són CO₂ i H₂O. Si falta oxigen, és <b>incompleta</b>: es formen monòxid de carboni (CO, molt tòxic) i sutge (carboni, C), que fa la flama groga i fumosa.")
    b += F("hidrocarbur + O₂ → CO₂ + H₂O + energia")
    b += EX("Exemples ajustats", "Metà: CH₄ + 2 O₂ → CO₂ + 2 H₂O · Butà: 2 C₄H₁₀ + 13 O₂ → 8 CO₂ + 10 H₂O · Octà: 2 C₈H₁₈ + 25 O₂ → 16 CO₂ + 18 H₂O · Etanol: C₂H₅OH + 3 O₂ → 2 CO₂ + 3 H₂O.")
    b += P("Al motor dels cotxes, la temperatura és tan alta que el nitrogen i l'oxigen de l'aire també reaccionen i formen <b>òxids de nitrogen</b> (NO i NO₂, els NOₓ), que contaminen l'aire de les ciutats: N₂ + O₂ → 2 NO; 2 NO + O₂ → 2 NO₂.")
    b += TIP("Com sabem que una espelma fa CO₂ i aigua", "Si posem un got fred a sobre de la flama, s'entela: és aigua. Si recollim els gasos i els fem bombollejar en <b>aigua de calç</b> (hidròxid de calci), aquesta es torna tèrbola: el CO₂ forma carbonat de calci, insoluble. Ca(OH)₂ + CO₂ → CaCO₃ + H₂O.")
    b += S(7, "Estequiometria: càlculs amb equacions")
    b += P("L'<b>estequiometria</b> calcula les quantitats de reactius i productes d'una reacció. Ho fem sempre amb els mateixos passos:")
    b += FIG(T4.estequiometria(a), "Els passos d'un càlcul estequiomètric.", "165mm")
    b += EX("Exemple · La bombona de butà", "Quant CO₂ fa una bombona de 12,5 kg de butà (C₄H₁₀, M = 58 g/mol)? 0) 2 C₄H₁₀ + 13 O₂ → 8 CO₂ + 10 H₂O. 1) n = 12 500 / 58 ≈ 215,5 mol de butà. 2) Per cada 2 mol de butà se'n formen 8 de CO₂: n(CO₂) = 215,5 · 8 / 2 = 862 mol. 3) m = 862 · 44 ≈ 37 900 g ≈ 38 kg de CO₂: tres vegades la massa del butà! L'oxigen ve de l'aire.")
    b += EX("Exemple · La calç", "Quanta calç viva (CaO, M = 56) s'obté escalfant 1 000 kg de pedra calcària (CaCO₃, M = 100)? CaCO₃ → CaO + CO₂. n = 1 000 000 / 100 = 10 000 mol → 10 000 mol de CaO → 560 kg de CaO (i s'alliberen 440 kg de CO₂).")
    b += S(8, "El reactiu limitant")
    b += P("Sovint un dels reactius s'acaba abans que l'altre. El que s'acaba primer és el <b>reactiu limitant</b>: determina quant producte es forma. L'altre és el <b>reactiu en excés</b>, i en sobra una part. Com quan fem entrepans: si tenim 10 llesques de pa i 3 talls de pernil, només en farem 3, i el pernil és el limitant.")
    b += EX("Exemple · Bicarbonat i vinagre", "NaHCO₃ + CH₃COOH → CH₃COONa + H₂O + CO₂. Si posem sempre el mateix vinagre i cada vegada més bicarbonat, el CO₂ augmenta fins que l'àcid s'acaba. A partir d'aleshores, afegir més bicarbonat no fa més gas: el vinagre s'ha convertit en el reactiu limitant.")
    b += S(9, "De la gasolina al CO₂")
    b += P("Com pot ser que un litre de gasolina, que té una massa d'uns 0,75 kg, faci més de 2 kg de CO₂? Perquè cada àtom de carboni de la gasolina s'endú dos àtoms d'oxigen de l'aire. Fem el càlcul suposant que la gasolina és octà:")
    b += EX("Càlcul", "m = d · V = 0,75 kg/L · 1 L = 750 g d'octà (M = 114 g/mol): n = 750 / 114 ≈ 6,58 mol. 2 C₈H₁₈ + 25 O₂ → 16 CO₂ + 18 H₂O: n(CO₂) = 6,58 · 16 / 2 = 52,6 mol; m = 52,6 · 44 ≈ 2 300 g ≈ 2,3 kg de CO₂ per litre. El factor oficial del Ministeri (MITECO) és d'uns 2,2–2,3 kg de CO₂ per litre de gasolina: el càlcul encaixa.")
    b += P("Per comparar mitjans de transport fem servir el <b>CO₂ per passatger i per quilòmetre</b>: un cotxe amb una sola persona emet unes quantes vegades més que un autobús ple o el metro, i la bicicleta o anar a peu no emeten gens durant el trajecte.")
    b += S(10, "L'energia de les reaccions")
    b += P("Trencar enllaços consumeix energia i formar-ne en desprèn. Si en formar els productes es desprèn més energia de la que ha calgut per trencar els reactius, la reacció és <b>exotèrmica</b> (desprèn calor: les combustions). Si n'absorbeix, és <b>endotèrmica</b> (necessita calor: descompondre la pedra calcària, la fotosíntesi).",
           "Moltes reaccions exotèrmiques no comencen soles: cal una espurna o una flama per arrencar-les. És l'<b>energia d'activació</b>, l'energia mínima perquè els xocs entre partícules siguin eficaços.")
    b += FIG(T2.diagrames_energia(a), "Diagrames d'energia d'una reacció exotèrmica i d'una endotèrmica.", "150mm")
    b += T(["Combustible", "Energia (kJ/g)", "CO₂ (g per kJ)"], [["Hidrogen", "142", "0"], ["Metà (gas natural)", "55", "0,050"], ["Gasolina (octà)", "47", "0,066"], ["Etanol", "30", "0,064"], ["Carbó", "≈ 30", "≈ 0,11"]], w=["40%", "30%", "30%"])
    b += P("Al laboratori podem mesurar l'energia d'un combustible escalfant aigua amb ell: la calor que guanya l'aigua és Q = m · c · ΔT (c de l'aigua = 4,18 J/(g·°C)).")
    b += FIG(T4.calorimetre(a), "Mesura de la calor de combustió de l'etanol.", "135mm")
    b += EX("Exemple", "Cremem 1,0 g d'etanol i escalfem 200 g d'aigua de 20 °C a 44 °C. Q = 200 · 4,18 · 24 ≈ 20 000 J = 20 kJ. El valor teòric és 30 kJ/g: el rendiment és 20 / 30 · 100 ≈ 67 %. La resta s'ha perdut escalfant l'aire i la llauna.")
    b += S(11, "La mobilitat, l'aire i la salut")
    b += P("Els cotxes i les motos, a més de CO₂ (que escalfa el planeta), emeten <b>NO₂</b> i <b>partícules fines</b> (PM₂,₅ i PM₁₀), que entren als pulmons i a la sang. L'Agència de Salut Pública de Barcelona (ASPB) estima que la contaminació de l'aire causa cada any a la ciutat centenars de morts prematures (al voltant d'un miler, segons els anys i els contaminants considerats). Els infants són especialment vulnerables: per això moltes ciutats pacifiquen els entorns escolars.",
           "Una campanya de mobilitat eficaç fa servir dades: quant CO₂ estalvia cada canvi de trajecte, quins beneficis té per a la salut i quines alternatives reals hi ha per a cada persona.")
    b += KW(("Reactiu i producte", "substàncies inicials i finals d'una reacció"), ("Equació ajustada", "mateix nombre d'àtoms de cada element als dos costats"), ("Hidrocarbur", "compost de carboni i hidrogen"),
            ("Alcà, alquè, alquí", "enllaços simples, un doble, un triple"), ("Alcohol", "compost orgànic amb el grup –OH"), ("Combustió completa", "fa CO₂ i H₂O"), ("Estequiometria", "càlcul de quantitats a partir de l'equació"),
            ("Reactiu limitant", "el que s'acaba primer i limita el producte"), ("Exotèrmica", "reacció que desprèn energia"), ("Energia d'activació", "energia mínima per començar una reacció"))
    return b

# ======================================================================== SdA 4
def sda4():
    a = A(4)
    b = H(4, "Per què es desfan les pedres i es rovellen les baranes? Els àcids i les bases, la neutralització, la pluja àcida, la velocitat de reacció, l'oxidació-reducció i la protecció del patrimoni.")
    b += TOC("Àcids i bases", "L'escala de pH i els indicadors", "La neutralització", "Àcids i carbonats", "La pluja àcida i la pedra", "La velocitat de les reaccions",
             "Col·lisions, energia d'activació i catalitzadors", "Oxidació i reducció", "La corrosió del ferro", "Les piles", "Com protegim el patrimoni")
    b += S(1, "Àcids i bases")
    b += T(["", "Àcids", "Bases (àlcalis)"],
           [["Propietats", "gust agre; ataquen metalls i el marbre; canvien el color dels indicadors", "gust amarg i tacte sabonós; dissolen greixos; canvien el color dels indicadors"],
            ["En aigua alliberen", "ions H⁺ (H₃O⁺)", "ions OH⁻"], ["Exemples a casa", "vinagre (àcid acètic), llimona (àcid cítric), salfumant (àcid clorhídric)", "lleixiu, amoníac, bicarbonat, sosa càustica dels desembussadors"],
            ["Exemples de laboratori", "HCl, HNO₃, H₂SO₄", "NaOH, KOH, Ca(OH)₂"]], w=["20%", "40%", "40%"])
    b += P("Segons la teoria d'<b>Arrhenius</b>, un àcid és una substància que en aigua allibera ions H⁺ (HCl → H⁺ + Cl⁻) i una base, una que allibera ions OH⁻ (NaOH → Na⁺ + OH⁻).")
    b += TIP("Seguretat", "Els àcids i les bases forts són <b>corrosius</b>: cremen la pell i els ulls. Fes servir ulleres i guants, i, per diluir un àcid concentrat, aboca sempre l'àcid sobre l'aigua, mai l'aigua sobre l'àcid. No barregis mai lleixiu amb àcids ni amb amoníac.")
    b += S(2, "L'escala de pH i els indicadors")
    b += P("El <b>pH</b> mesura l'acidesa d'una dissolució en una escala de 0 a 14. Un pH menor que 7 és àcid; igual a 7, neutre; i major que 7, bàsic. És una escala logarítmica: una dissolució de pH 3 és 10 vegades més àcida que una de pH 4, i 100 vegades més que una de pH 5.")
    b += FIG(T4.escala_ph(a), "L'escala de pH amb alguns productes habituals.", "165mm")
    b += P("Els <b>indicadors</b> són substàncies que canvien de color segons el pH: el paper indicador universal, la fenolftaleïna (incolora en àcid, rosa en bàsic) o el tornassol. La <b>col llombarda</b> conté antocianines que fan d'indicador natural: vermell en medi molt àcid, lila en neutre, verd i groc en medi bàsic. Per mesurar el pH amb precisió fem servir un <b>pH-metre</b>.")
    b += S(3, "La neutralització")
    b += P("Quan barregem un àcid i una base en la proporció adequada, s'anul·len: es forma una <b>sal</b> i <b>aigua</b>, i el pH s'acosta a 7. És la <b>neutralització</b>.")
    b += F("àcid + base → sal + aigua", note="L'essencial: H⁺ + OH⁻ → H₂O")
    b += FIG(T4.neutralitzacio(a), "Neutralització de l'àcid clorhídric amb hidròxid de sodi.", "140mm")
    b += EX("Exemples", "HCl + NaOH → NaCl + H₂O · H₂SO₄ + 2 KOH → K₂SO₄ + 2 H₂O · 2 HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + 2 H₂O.")
    b += P("Ho fem servir sovint: els <b>antiàcids</b> (hidròxid de magnesi o d'alumini, bicarbonat) neutralitzen l'excés d'àcid de l'estómac; la pagesia afegeix calç als sòls massa àcids; i a les depuradores es neutralitzen les aigües industrials abans d'abocar-les.")
    b += S(4, "Àcids i carbonats")
    b += P("Els àcids reaccionen amb els <b>carbonats</b> i desprenen <b>diòxid de carboni</b>, que fa bombolles (efervescència). Aquesta reacció és la base de la prova per reconèixer roques calcàries: si hi tirem una gota d'àcid i fa bombolles, és pedra calcària.")
    b += F("carbonat + àcid → sal + aigua + diòxid de carboni", "CaCO₃ + 2 HCl → CaCl₂ + H₂O + CO₂")
    b += S(5, "La pluja àcida i la pedra")
    b += P("La pluja normal ja és lleugerament àcida (pH ≈ 5,6) perquè porta CO₂ dissolt. Parlem de <b>pluja àcida</b> quan el pH és més baix. La causen el <b>diòxid de sofre</b> (SO₂), que surt de cremar carbó i gasoil amb sofre, i els <b>òxids de nitrogen</b> (NOₓ) dels motors i les calefaccions. A l'atmosfera reaccionen amb l'oxigen i l'aigua i formen àcid sulfúric i àcid nítric.")
    b += F("2 SO₂ + O₂ → 2 SO₃", "SO₃ + H₂O → H₂SO₄")
    b += FIG(T4.pluja_acida(a), "Formació de la pluja àcida i atac a la pedra calcària.", "160mm")
    b += P("Molts monuments són de <b>pedra calcària</b> o de <b>marbre</b> (carbonat de calci). L'àcid sulfúric la transforma en <b>guix</b> (sulfat de calci), que és més tou, més soluble i ocupa més volum: la pedra s'esquerda i es desfà. A les zones protegides de la pluja, el guix atrapa el sutge dels motors i es formen les <b>crostes negres</b> de moltes façanes.")
    b += F("CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂")
    b += P("A Barcelona, el SO₂ ha baixat molt les últimes dècades (menys carbó i combustibles amb menys sofre i menys indústria a la ciutat), però el <b>NO₂</b> del trànsit continua sent elevat en molts carrers i és el contaminant que més preocupa.")
    b += S(6, "La velocitat de les reaccions")
    b += P("La <b>velocitat de reacció</b> indica quanta quantitat de reactiu desapareix (o de producte es forma) per unitat de temps. La podem mesurar, per exemple, pel volum de CO₂ que surt cada minut o per la massa que perd un recipient obert. Els factors que l'afecten són:")
    b += T(["Factor", "Efecte", "Exemple amb la pedra"],
           [["Concentració", "més concentració → més xocs → més ràpida", "l'àcid concentrat ataca el marbre més de pressa"], ["Temperatura", "més temperatura → partícules més ràpides, xocs més freqüents i amb més energia → més ràpida", "la reacció és més ràpida en aigua calenta"],
            ["Superfície de contacte", "trossos més petits → més superfície → més xocs → més ràpida", "la pols de marbre reacciona molt més de pressa que un tros sencer"], ["Catalitzador", "accelera la reacció sense consumir-se", "els enzims; els catalitzadors dels cotxes"]], w=["20%", "45%", "35%"])
    b += FIG(T2.factors_velocitat(a), "Factors que modifiquen la velocitat d'una reacció.", "150mm")
    b += TIP("Dissenyar un experiment just", "Per estudiar un factor, el canviem només a ell (<b>variable independent</b>), mesurem el resultat (<b>variable dependent</b>: el CO₂ o la massa perduda) i mantenim igual tota la resta (<b>variables controlades</b>: la massa de marbre, el volum d'àcid…). I repetim cada mesura.")
    b += S(7, "Col·lisions, energia d'activació i catalitzadors")
    b += P("La <b>teoria de les col·lisions</b> explica per què passen les reaccions i per què ho fan més ràpid o més lent. Perquè dues partícules reaccionin, han de xocar, i el xoc ha de ser <b>eficaç</b>, és a dir, ha de complir dues condicions:")
    b += OL("Les partícules han de tenir <b>prou energia cinètica</b>: com a mínim l'<b>energia d'activació</b>, necessària per trencar els enllaços.", "Han de xocar amb l'<b>orientació adequada</b>, de manera que els àtoms que han d'enllaçar quedin a prop.")
    b += FIG(T2.col_lisions(a), "Xoc eficaç i xocs no eficaços.", "160mm")
    b += P("Un <b>catalitzador</b> proporciona un camí alternatiu amb una <b>energia d'activació més petita</b>: més xocs són eficaços i la reacció va més de pressa. No es gasta i no canvia el resultat de la reacció. Els enzims són catalitzadors biològics.")
    b += FIG(T2.diagrames_energia(a), "Diagrames d'energia: l'energia d'activació és la «muntanya» que cal superar.", "150mm")
    b += S(8, "Oxidació i reducció")
    b += P("Moltes reaccions consisteixen en un <b>intercanvi d'electrons</b> entre substàncies: són les reaccions d'<b>oxidació-reducció</b> o <b>redox</b>.")
    b += UL("<b>Oxidació:</b> una substància <b>perd</b> electrons. Fe → Fe²⁺ + 2 e⁻.", "<b>Reducció:</b> una substància <b>guanya</b> electrons. Cu²⁺ + 2 e⁻ → Cu.",
            "Sempre van juntes: els electrons que perd una substància els guanya una altra.")
    b += EX("Exemple", "Un clau de ferro dins de sulfat de coure(II): Fe + CuSO₄ → FeSO₄ + Cu. El ferro s'oxida (es dissol com a Fe²⁺) i el coure es redueix (es diposita, vermellós, sobre el clau). Passa perquè el ferro és més reactiu que el coure.")
    b += P("La <b>sèrie de reactivitat</b> ordena els metalls segons la facilitat amb què s'oxiden: K, Na, Ca, Mg, Al, Zn, Fe, Pb, Cu, Ag, Au (de més a menys reactiu). Un metall pot desplaçar d'una dissolució els ions dels metalls que té a la seva dreta. L'or i la plata, poc reactius, es troben purs a la natura i no es rovellen.")
    b += S(9, "La corrosió del ferro")
    b += P("La <b>corrosió</b> és l'oxidació d'un metall pel seu entorn. El ferro es rovella quan hi ha alhora <b>aigua</b> i <b>oxigen</b>: el ferro s'oxida i es forma un òxid de ferro(III) hidratat, el rovell, porós i que se n'escata, de manera que la corrosió continua cap a dins. La sal (al costat del mar o a les carreteres a l'hivern) i els àcids l'acceleren.")
    b += F("4 Fe + 3 O₂ + 2n H₂O → 2 Fe₂O₃ · n H₂O (rovell)")
    b += FIG(T4.sis_claus(a), "L'experiment dels sis claus: què cal perquè el ferro es rovelli?", "160mm")
    b += S(10, "Les piles")
    b += P("En una reacció redox, els electrons passen d'una substància a l'altra. Si separem l'oxidació i la reducció en dos recipients i els connectem amb un fil, els electrons circulen pel fil: hem fet una <b>pila</b>, que transforma energia química en elèctrica.",
           "A la <b>pila de Daniell</b>, una làmina de zinc en sulfat de zinc (l'<b>ànode</b>, on hi ha l'oxidació) i una de coure en sulfat de coure (el <b>càtode</b>, on hi ha la reducció) es connecten amb un fil i un <b>pont salí</b>, que tanca el circuit. Dona una tensió d'uns 1,1 V. Amb dues monedes de metalls diferents clavades en una llimona també es fa una pila.")
    b += FIG(T4.pila_daniell(a), "La pila de Daniell.", "130mm")
    b += P("La corrosió és com una petita pila: on hi ha dos metalls en contacte i aigua, el més reactiu s'oxida. Per això un cargol d'acer en una planxa de coure es rovella molt de pressa.")
    b += S(11, "Com protegim el patrimoni")
    b += UL("<b>Barreres:</b> pintar, envernissar, greixar o plastificar el ferro perquè no hi arribin l'aigua i l'oxigen. A la pedra, consolidants i hidrofugants que no la segellen del tot (ha de poder transpirar).",
            "<b>Galvanitzar:</b> recobrir l'acer de zinc. El zinc, més reactiu, s'oxida abans que el ferro i el protegeix encara que la capa es ratlli.",
            "<b>Ànodes de sacrifici:</b> blocs de zinc o magnesi units als vaixells, a les canonades o als dipòsits, que es corroeixen en lloc del ferro i es van canviant.",
            "<b>Materials resistents:</b> acer inoxidable (amb crom, que fa una capa d'òxid protectora), alumini, bronze.",
            "<b>Menys contaminació:</b> reduir el trànsit i les emissions de SO₂ i NOₓ alenteix la degradació de les façanes. Netejar les crostes negres amb tècniques suaus (làser, apòsits) sense malmetre la pedra.")
    b += TIP("La ciència la fan persones", "Agnes Pockels (1862–1935) no va poder anar a la universitat per ser dona. Des de la cuina de casa, amb un recipient i una balança que ella mateixa va construir, va estudiar la tensió superficial de l'aigua amb sabó i oli. El 1891 va publicar els seus resultats a la revista <i>Nature</i> gràcies a una carta a Lord Rayleigh.")
    b += KW(("Àcid", "allibera H⁺ en aigua; pH &lt; 7"), ("Base", "allibera OH⁻ en aigua; pH &gt; 7"), ("pH", "escala d'acidesa de 0 a 14"), ("Neutralització", "àcid + base → sal + aigua"),
            ("Pluja àcida", "pluja amb àcids sulfúric i nítric; pH &lt; 5,6"), ("Xoc eficaç", "amb prou energia i bona orientació"), ("Energia d'activació", "energia mínima perquè una reacció comenci"),
            ("Oxidació", "pèrdua d'electrons"), ("Reducció", "guany d'electrons"), ("Ànode de sacrifici", "metall més reactiu que es corroeix per protegir el ferro"))
    return b

# ======================================================================== SdA 5
def sda5():
    a = A(5)
    b = H(5, "Com es tanca una ferida? La posició, el desplaçament i la velocitat com a vectors, el MRU i el MRUA, la caiguda lliure, les forces, les lleis de Newton, el fregament i l'equilibri.")
    b += TOC("Posició, desplaçament i vectors", "La velocitat", "El moviment rectilini uniforme (MRU)", "L'acceleració i el MRUA", "Seguretat viària: temps de reacció i distància d'aturada",
             "La caiguda lliure", "Les forces com a vectors", "Les lleis de Newton", "El fregament i la velocitat límit", "Forces elàstiques: la llei de Hooke", "Equilibri i tensió: qui estira i qui empeny?")
    b += S(1, "Posició, desplaçament i vectors")
    b += P("Per descriure un moviment cal un <b>sistema de referència</b>: un origen i uns eixos. La <b>posició</b> d'un mòbil és on és respecte de l'origen. La <b>trajectòria</b> és el camí que segueix, i la seva longitud és la <b>distància recorreguda</b>. El <b>desplaçament</b> és el canvi de posició: va en línia recta de la posició inicial a la final.")
    b += FIG(T2.trajectoria_desplacament(a), "Trajectòria i desplaçament.", "120mm")
    b += P("Algunes magnituds queden ben definides amb un nombre i una unitat: són <b>escalars</b> (la massa, la temperatura, la distància). D'altres també necessiten una direcció i un sentit: són <b>vectorials</b> (el desplaçament, la velocitat, l'acceleració, la força). Un vector es dibuixa amb una fletxa: la longitud és el <b>mòdul</b>, la recta on és la <b>direcció</b> i la punta el <b>sentit</b>.",
           "En el pla, un vector es pot escriure amb les seves <b>components</b>: quant avança en x i quant en y. El mòdul es calcula amb el teorema de Pitàgores.")
    b += F("v = (vₓ, v<sub>y</sub>)", "|v| = √(vₓ² + v<sub>y</sub>²)")
    b += FIG(T4.vector_components(a), "Desplaçament per l'Eixample: components i mòdul.", "150mm")
    b += EX("Exemple · Una cèl·lula", "Una cèl·lula del front de la ferida passa de la posició (10, 5) µm a la (34, 12) µm. Δr = (24, 7) µm i |Δr| = √(24² + 7²) = 25 µm.")
    b += S(2, "La velocitat")
    b += P("La <b>velocitat mitjana</b> és el desplaçament dividit pel temps que s'ha trigat. La <b>rapidesa mitjana</b> fa servir la distància recorreguda. La <b>velocitat instantània</b> és la que té el mòbil en un instant (la que marca el velocímetre).")
    b += F(f"v<sub>m</sub> = {fr('Δx', 'Δt')} = {fr('x − x₀', 't − t₀')}", note="Unitat del SI: m/s · 1 m/s = 3,6 km/h")
    b += P("El <b>criteri de signes</b>: triem un sentit positiu (per exemple, cap a la dreta o cap amunt). Una velocitat negativa vol dir que el mòbil es mou en sentit contrari.")
    b += S(3, "El moviment rectilini uniforme (MRU)")
    b += P("Un mòbil té un <b>MRU</b> si es mou en línia recta amb velocitat constant: recorre distàncies iguals en temps iguals. A la gràfica x–t és una recta (el pendent és la velocitat) i a la gràfica v–t, una recta horitzontal.")
    b += F("x = x₀ + v · t")
    b += FIG(T2.grafiques_moviment(a), "Gràfiques del MRU i del MRUA.", "165mm")
    b += EX("Exemple · El front de la ferida", "En les fotos d'una ferida en una capa de cèl·lules, la vora es mou de x = 0 µm a x = 60 µm en 3 h. v = 60 / 3 = 20 µm/h. Si la ferida fa 400 µm d'ample i les dues vores avancen l'una cap a l'altra a 20 µm/h, es tancarà en 400 / (2 · 20) = 10 h.")
    b += EX("Exemple · Una trobada", "Dos cotxes surten alhora de dos pobles separats 90 km, l'un cap a l'altre, a 50 km/h i a 40 km/h. x₁ = 50 t; x₂ = 90 − 40 t. Es troben quan x₁ = x₂: 50 t = 90 − 40 t → t = 1 h, a 50 km del primer poble.")
    b += S(4, "L'acceleració i el MRUA")
    b += P("L'<b>acceleració</b> indica com canvia la velocitat amb el temps. Si un mòbil frena, l'acceleració té el sentit contrari a la velocitat (amb el nostre criteri, sovint negativa).")
    b += F(f"a = {fr('Δv', 'Δt')} = {fr('v − v₀', 't')}", note="Unitat del SI: m/s²")
    b += P("En el <b>moviment rectilini uniformement accelerat (MRUA)</b> l'acceleració és constant. Les equacions són:")
    b += F("v = v₀ + a · t", "x = x₀ + v₀ · t + ½ · a · t²", "v² = v₀² + 2 · a · Δx  (equació sense temps)")
    b += P("A la gràfica v–t, el MRUA és una recta: el pendent és l'acceleració i l'<b>àrea sota la recta</b> és el desplaçament.")
    b += EX("Exemple · Una frenada", "Un cotxe va a 72 km/h (20 m/s) i frena amb a = −7 m/s². Temps de frenada: 0 = 20 − 7 t → t ≈ 2,9 s. Distància de frenada (sense temps): 0 = 20² + 2 · (−7) · Δx → Δx = 400 / 14 ≈ 28,6 m.")
    b += S(5, "Seguretat viària: temps de reacció i distància d'aturada")
    b += P("Des que veiem un perill fins que trepitgem el fre passa un temps, el <b>temps de reacció</b> (uns 0,7–1 s, i molt més si mirem el mòbil o hem begut alcohol). Durant aquest temps el cotxe continua a la mateixa velocitat (MRU). Després frena (MRUA). La <b>distància d'aturada</b> és la suma de les dues:")
    b += F(f"d<sub>aturada</sub> = v · t<sub>reacció</sub> + {fr('v²', '2 · |a|')}")
    b += FIG(T4.distancia_aturada(a), "Distància d'aturada a 50 km/h i a 30 km/h.", "165mm")
    b += P("La distància de frenada augmenta amb el <b>quadrat</b> de la velocitat: si dupliquem la velocitat, es multiplica per quatre. Per això limitar la velocitat a 30 km/h als carrers de la ciutat salva vides: a 30 km/h un cotxe s'atura en uns 13 m; a 50 km/h, en uns 28 m. I en un atropellament a 30 km/h la majoria de vianants sobreviuen; a 50 km/h, el risc de mort es multiplica.")
    b += TIP("Mesurar el temps de reacció", "Una persona deixa caure un regle i l'altra l'atura amb els dits. Si el regle ha caigut una distància d, el temps de reacció és t = √(2d / g). Si el regle cau 20 cm: t = √(2 · 0,20 / 9,8) ≈ 0,20 s. Amb distraccions, el temps augmenta.")
    b += S(6, "La caiguda lliure")
    b += P("Si deixem caure un objecte i el fregament amb l'aire és negligible, cau amb una acceleració constant, la <b>gravetat</b>: g = 9,8 m/s², cap avall. Tots els cossos cauen igual de de pressa, independentment de la massa (Galileu). És un MRUA. Amb el criteri de signes positiu cap amunt, a = −g.")
    b += FIG(T4.caiguda_lliure(a), "Caiguda lliure: posicions cada segon i gràfica v–t.", "155mm")
    b += EX("Exemple · Llançament vertical", "Llancem una pilota cap amunt a 15 m/s. A l'altura màxima, v = 0: 0 = 15 − 9,8 t → t ≈ 1,53 s. Altura màxima: 0 = 15² − 2 · 9,8 · h → h = 225 / 19,6 ≈ 11,5 m.")
    b += P("Per què les cèl·lules no cauen com pedres? Perquè en un líquid el fregament és molt important comparat amb el pes d'una cosa tan petita. Les cèl·lules sedimenten molt a poc a poc, a una velocitat constant. La <b>velocitat de sedimentació globular (VSG)</b> d'una anàlisi de sang mesura com de pressa baixen els glòbuls vermells en un tub; si va més ràpid del normal, pot indicar una inflamació.")
    b += S(7, "Les forces com a vectors")
    b += P("Una <b>força</b> és una interacció entre dos cossos que pot canviar-ne l'estat de moviment o deformar-los. Es mesura en <b>newtons (N)</b> amb un dinamòmetre. Com que és un vector, per sumar forces cal tenir en compte la direcció i el sentit: el resultat és la <b>força resultant</b> (ΣF).")
    b += FIG(T2.forces_resultant(a), "Suma de forces en la mateixa direcció i perpendiculars.", "155mm")
    b += P("Per resoldre un problema de forces dibuixem el <b>diagrama de forces</b> (o de cos lliure): el cos com un punt i totes les forces que actuen sobre ell. Les més habituals són:")
    b += UL("<b>Pes (P):</b> la força amb què la Terra atreu el cos. P = m · g, vertical i cap avall.", "<b>Normal (N):</b> la força que fa la superfície on es recolza el cos, perpendicular a la superfície.",
            "<b>Fregament (f):</b> s'oposa al moviment (o a l'intent de moviment), paral·lela a la superfície.", "<b>Tensió (T):</b> la que fa una corda, un cable o un teixit tibant.", "<b>Força motriu (F):</b> la del motor, els músculs, etc.")
    b += FIG(T4.diagrama_cotxe(a), "Diagrama de forces d'un cotxe que accelera.", "145mm")
    b += P("En un <b>pla inclinat</b> descomponem el pes en una component paral·lela al pla, que tendeix a fer-lo baixar, i una de perpendicular, que s'equilibra amb la normal:")
    b += FIG(T4.pla_inclinat(a), "Descomposició del pes en un pla inclinat.", "150mm")
    b += F("Pₓ = m · g · sin α", "P<sub>y</sub> = m · g · cos α")
    b += S(8, "Les lleis de Newton")
    b += UL("<b>1a llei (inèrcia):</b> si la força resultant sobre un cos és zero, el cos continua en repòs o en MRU. Per això ens anem cap endavant quan l'autobús frena: el nostre cos tendeix a continuar movent-se.",
            "<b>2a llei (fonamental de la dinàmica):</b> la força resultant és igual a la massa per l'acceleració, i l'acceleració té la direcció i el sentit de la força resultant: <b>ΣF = m · a</b>.",
            "<b>3a llei (acció i reacció):</b> si un cos fa una força sobre un altre, l'altre en fa una d'igual i de sentit contrari sobre el primer. Les dues forces actuen sobre cossos diferents i, per tant, no s'anul·len.")
    b += FIG(T2.accio_reaccio(a), "Acció i reacció.", "140mm")
    b += EX("Exemple · D'on surt −7 m/s²", "En frenar, la força que atura el cotxe és el fregament de les rodes amb l'asfalt: f = μ · N = μ · m · g. Per la 2a llei, a = f / m = μ · g. Amb asfalt sec, μ ≈ 0,7: a = 0,7 · 9,8 ≈ 6,9 m/s², és a dir, unes −7 m/s². Amb asfalt mullat, μ ≈ 0,4 i a ≈ −3,9 m/s²: la distància de frenada gairebé es duplica.")
    b += EX("Exemple · La moto", "Una moto de 200 kg (amb el pilot) accelera a 2 m/s² i el fregament total és de 300 N. ΣF = m · a → F − 300 = 200 · 2 → F = 700 N.")
    b += S(9, "El fregament i la velocitat límit")
    b += P("El <b>fregament</b> és la força que apareix entre dues superfícies en contacte i que s'oposa al lliscament. Depèn dels materials (coeficient de fregament, μ) i de com d'estretes estan les superfícies (la normal):")
    b += F("f = μ · N", note="μ no té unitats · sabatilla de goma en terra sec: μ ≈ 0,8–1 · gel: μ ≈ 0,05")
    b += P("Per mesurar μ: posem la sabatilla en un pla inclinat i anem augmentant l'angle fins que comença a lliscar. En aquest angle límit, Pₓ = f: m · g · sin α = μ · m · g · cos α → <b>μ = tan α</b>.",
           "En un fluid (aire, aigua, glicerina) el fregament augmenta amb la velocitat. Un objecte que cau accelera fins que el fregament i l'empenta igualen el pes; aleshores la força resultant és zero i baixa a velocitat constant, la <b>velocitat límit</b>. És el que passa amb els paracaigudistes, les gotes de pluja i les cèl·lules.")
    b += FIG(T4.velocitat_limit(a), "Una bola que cau en glicerina arriba a una velocitat límit.", "145mm")
    b += S(10, "Forces elàstiques: la llei de Hooke")
    b += P("Quan estirem una molla o un material elàstic, l'allargament és directament proporcional a la força (mentre no superem el límit d'elasticitat):")
    b += F("F = k · Δx", note="k: constant elàstica (N/m) · Δx: allargament (m)")
    b += FIG(T2.hooke(a), "Llei de Hooke: la força i l'allargament són proporcionals.", "140mm")
    b += P("Els biòlegs fan servir aquesta llei per mesurar forces molt petites. Posen cèl·lules sobre un <b>gel tou</b> amb boletes fluorescents; quan les cèl·lules estiren, el gel es deforma i les boletes es desplacen. Coneixent la rigidesa del gel, calculen les <b>forces de tracció</b> de les cèl·lules (de l'ordre dels nanonewtons). Per la 3a llei, la cèl·lula estira el gel i el gel estira la cèl·lula amb la mateixa força.")
    b += S(11, "Equilibri i tensió: qui estira i qui empeny?")
    b += P("Un cos està en <b>equilibri</b> quan la força resultant és zero (ΣF = 0): està en repòs o es mou a velocitat constant. Les cèl·lules del front d'una ferida avancen tan a poc a poc i són tan petites que la seva inèrcia és pràcticament nul·la: en cada instant les forces sobre elles estan pràcticament equilibrades.",
           "Els experiments mostren que les cèl·lules de la <b>vora</b> de la ferida s'agafen al substrat i <b>estiren</b> cap endavant; les cèl·lules de darrere són <b>arrossegades</b> per les seves veïnes, a les quals estan unides. La capa de cèl·lules queda en <b>tensió</b>, com una corda en el joc d'estirar la corda. Com en una cordada, la tensió és més gran a prop de la vora que tira.")
    b += EX("Exemple · El semàfor penjat", "Un semàfor de 20 kg penja d'un cable vertical. En equilibri, T = P = 20 · 9,8 = 196 N. Si penja de dos cables que fan 30° amb l'horitzontal, cada cable ha de fer 2 · T · sin 30° = 196 N → T = 196 N: els cables inclinats han d'aguantar més tensió que si fossin verticals (98 N cadascun).")
    b += KW(("Desplaçament", "canvi de posició, en línia recta"), ("Vector", "magnitud amb mòdul, direcció i sentit"), ("Velocitat", "desplaçament per unitat de temps (m/s)"), ("Acceleració", "canvi de velocitat per unitat de temps (m/s²)"),
            ("MRUA", "moviment rectilini amb acceleració constant"), ("Distància d'aturada", "distància de reacció + distància de frenada"), ("Força resultant", "suma vectorial de totes les forces"),
            ("2a llei de Newton", "ΣF = m · a"), ("Velocitat límit", "velocitat constant quan les forces s'equilibren"), ("Llei de Hooke", "F = k · Δx"))
    return b

# ======================================================================== SdA 6
def sda6():
    a = A(6)
    b = H(6, "Com baixava i pujava l'Ictineo? La pressió, la pressió hidrostàtica, el principi de Pascal, la pressió atmosfèrica, l'empenta i la flotació.")
    b += TOC("Què és la pressió", "Unitats de pressió", "La pressió dins dels líquids", "Vasos comunicants i manòmetres", "El principi de Pascal", "La pressió atmosfèrica",
             "L'empenta i el principi d'Arquimedes", "Surar o enfonsar-se", "Com funciona un submarí", "Monturiol i la ciència col·lectiva")
    b += S(1, "Què és la pressió")
    b += P("Per què ens enfonsem a la neu amb botes i no amb raquetes? Per què un ganivet esmolat talla millor? La mateixa força pot tenir efectes molt diferents segons la <b>superfície</b> on es reparteix. La <b>pressió</b> és la força perpendicular que actua sobre cada unitat de superfície.")
    b += F(f"p = {fr('F', 'S')}", note="F: força perpendicular (N) · S: superfície (m²) · p: pressió en pascals (Pa); 1 Pa = 1 N/m²")
    b += FIG(T4.pressio_superficie(a), "La mateixa força sobre superfícies diferents.", "150mm")
    b += EX("Exemple", "Una persona de 60 kg (P = 588 N) dreta amb dues sabates de 150 cm² cadascuna: S = 300 cm² = 0,03 m²; p = 588 / 0,03 ≈ 19 600 Pa. Amb un taló d'agulla d'1 cm² que aguanta la meitat del pes: p = 294 / 0,0001 = 2 940 000 Pa, 150 vegades més. Per això els talons fan malbé els terres de fusta.")
    b += P("Per <b>augmentar</b> la pressió reduïm la superfície (ganivets, agulles, xinxetes, claus); per <b>reduir-la</b>, l'augmentem (raquetes de neu, erugues de les excavadores, fonaments dels edificis).")
    b += S(2, "Unitats de pressió")
    b += T(["Unitat", "Equivalència", "On la trobem"], [["pascal (Pa)", "unitat del SI · 1 hPa = 100 Pa", "ciència; mapes del temps (hPa)"], ["atmosfera (atm)", "1 atm = 101 325 Pa", "pressió atmosfèrica, submarinisme"],
            ["bar i mil·libar", "1 bar = 100 000 Pa ≈ 1 atm · 1 mbar = 1 hPa", "pneumàtics, bombones"], ["mil·límetre de mercuri (mmHg)", "1 atm = 760 mmHg", "pressió arterial, baròmetres"]], w=["28%", "40%", "32%"])
    b += EX("Exemple", "Un pneumàtic a 2,2 bar: \\( 2{,}2\\ \\mathrm{bar} \\cdot \\dfrac{100000\\ \\mathrm{Pa}}{1\\ \\mathrm{bar}} = 220000\\ \\mathrm{Pa} \\approx 2{,}2\\ \\mathrm{atm} \\).")
    b += S(3, "La pressió dins dels líquids")
    b += P("Un líquid pesa, i aquest pes fa pressió sobre el fons i les parets del recipient i sobre qualsevol objecte submergit. És la <b>pressió hidrostàtica</b>. Augmenta amb la <b>profunditat</b> i amb la <b>densitat</b> del líquid, però no depèn de la forma del recipient ni de la quantitat total de líquid. A una mateixa profunditat, la pressió és igual en totes direccions.")
    b += F("p = ρ · g · h", note="ρ: densitat del líquid (kg/m³) · g = 9,8 m/s² · h: profunditat (m) · p en Pa")
    b += FIG(T4.pressio_hidrostatica(a), "La pressió hidrostàtica augmenta amb la profunditat.", "145mm")
    b += P("La pressió total sobre un submarinista és la pressió atmosfèrica que hi ha sobre l'aigua més la pressió hidrostàtica:")
    b += F("p<sub>total</sub> = p<sub>atm</sub> + ρ · g · h")
    b += EX("Exemple · L'Ictineo a 30 m", "Aigua de mar: ρ = 1 030 kg/m³. p<sub>hidrostàtica</sub> = 1 030 · 9,8 · 30 ≈ 302 800 Pa ≈ 3 atm. Total: 1 + 3 = 4 atm. Sobre una finestreta de 0,03 m², F = p<sub>hidrostàtica</sub> · S ≈ 302 800 · 0,03 ≈ 9 100 N (el pes de gairebé una tona!). Per això el casc de l'Ictineo era de fusta d'olivera i de roure reforçada i les finestretes, de vidre gruixut.")
    b += TIP("Per què les preses són més gruixudes a baix", "La pressió de l'aigua de l'embassament és molt més gran al fons que a la superfície. Per això la paret de les preses és molt més gruixuda a la base, i els dipòsits d'aigua es fan alts: com més altura, més pressió a les aixetes.")
    b += S(4, "Vasos comunicants i manòmetres")
    b += P("Si diversos recipients estan connectats per baix, el líquid arriba a la <b>mateixa altura</b> a tots, sigui quina sigui la seva forma: són <b>vasos comunicants</b>. Així funcionen els dipòsits d'aigua dels pobles, el nivell dels paletes i les fonts.",
           "Un <b>manòmetre de tub en U</b> mesura diferències de pressió: la diferència d'altura del líquid a les dues branques és proporcional a la diferència de pressió.")
    b += FIG(T4.manometre(a), "Manòmetre de tub en U per estudiar la pressió dins d'un líquid.", "140mm")
    b += S(5, "El principi de Pascal")
    b += P("Si premem un líquid tancat en un punt, l'augment de pressió es transmet <b>igual a tots els punts</b> del líquid i a les parets del recipient. És el <b>principi de Pascal</b> (Blaise Pascal, segle XVII). Els líquids gairebé no es poden comprimir, i per això transmeten la força.")
    b += P("La <b>premsa hidràulica</b> fa servir aquest principi per multiplicar forces: dos èmbols de superfícies diferents connectats per un líquid. La pressió és la mateixa als dos, i per tant:")
    b += F(f"{fr('F₁', 'S₁')} = {fr('F₂', 'S₂')}", note="Si l'èmbol gran té 50 vegades més superfície, la força s'hi multiplica per 50 (però s'ha de desplaçar 50 vegades menys)")
    b += FIG(T4.premsa_hidraulica(a), "Premsa hidràulica.", "150mm")
    b += EX("Exemple · El gat del taller", "Èmbol petit de 4 cm² i gran de 400 cm². Per aixecar un cotxe de 1 200 kg (P = 11 760 N): F₁ = F₂ · S₁ / S₂ = 11 760 · 4 / 400 ≈ 118 N, el pes d'uns 12 kg.")
    b += P("També funcionen així els <b>frens</b> dels cotxes (el pedal empeny un líquid que transmet la pressió a les quatre rodes), les excavadores, els ascensors hidràulics i les cadires dels dentistes.")
    b += S(6, "La pressió atmosfèrica")
    b += P("Vivim al fons d'un oceà d'aire d'uns quants quilòmetres de gruix. El pes d'aquest aire fa una pressió sobre tot el que hi ha a la superfície de la Terra: la <b>pressió atmosfèrica</b>. Al nivell del mar val de mitjana 1 atm = 101 325 Pa (unes 10 tones sobre cada metre quadrat!). No ho notem perquè la pressió dins del nostre cos és igual i empeny cap enfora.")
    b += FIG(T4.torricelli(a), "L'experiment de Torricelli.", "145mm")
    b += P("<b>Evangelista Torricelli</b> (1643) va omplir de mercuri un tub d'1 m, el va tapar, el va girar i el va posar dins d'una cubeta de mercuri. El mercuri va baixar fins a deixar una columna de <b>760 mm</b>: a dalt va quedar el buit, i la pressió de l'aire sobre la cubeta aguantava la columna. Havia inventat el <b>baròmetre</b>.")
    b += UL("La pressió atmosfèrica <b>disminueix amb l'altitud</b>, perquè hi ha menys aire a sobre: al Tibidabo (512 m) és unes 0,94 atm; al cim de l'Everest, només un terç d'atmosfera.",
            "Una llauna amb una mica d'aigua bullint, si la tapem i la refredem, s'aixafa: el vapor de dins condensa, la pressió interior baixa molt i la pressió atmosfèrica l'esclafa.",
            "Quan xuclem amb una palleta, reduïm la pressió dins la boca i la pressió atmosfèrica empeny el líquid cap amunt.",
            "Els <b>bussejadors</b> respiren aire a la mateixa pressió que l'aigua que els envolta; per això, en pujar, han d'expulsar aire i fer-ho a poc a poc (llei de Boyle).")
    b += S(7, "L'empenta i el principi d'Arquimedes")
    b += P("Quan submergim un objecte en un líquid, el líquid empeny totes les seves cares. Com que la pressió augmenta amb la profunditat, la força cap amunt a la cara de baix és més gran que la força cap avall a la cara de dalt. El resultat és una força vertical cap amunt: l'<b>empenta</b> (E).")
    b += FIG(T4.empenta(a), "D'on surt l'empenta.", "150mm")
    b += DEF("Principi d'Arquimedes", "tot cos submergit totalment o parcialment en un fluid rep una empenta vertical i cap amunt igual al pes del fluid que desallotja.")
    b += F("E = ρ<sub>líquid</sub> · V<sub>submergit</sub> · g", note="ρ<sub>líquid</sub>: densitat del líquid (kg/m³) · V<sub>submergit</sub>: volum de la part submergida (m³) · E en N")
    b += P("Si pengem un objecte d'un dinamòmetre i el submergim, marca menys: és el <b>pes aparent</b>.")
    b += F("P<sub>aparent</sub> = P − E")
    b += EX("Exemple · Mesurar una densitat", "Un tros de metall pesa 2,70 N a l'aire i 1,70 N dins l'aigua. E = 2,70 − 1,70 = 1,00 N. V = E / (ρ<sub>aigua</sub> · g) = 1,00 / (1 000 · 9,8) ≈ 1,02 · 10⁻⁴ m³. m = P / g = 2,70 / 9,8 ≈ 0,276 kg. ρ = m / V ≈ 2 700 kg/m³: és alumini.")
    b += S(8, "Surar o enfonsar-se")
    b += P("Sobre un cos submergit actuen dues forces verticals: el pes (cap avall) i l'empenta (cap amunt). Comparant-les, o comparant la <b>densitat mitjana</b> del cos amb la del líquid, sabem què passarà:")
    b += FIG(T4.flotacio(a), "S'enfonsa, en equilibri o sura.", "155mm")
    b += UL("Si P &gt; E (ρ<sub>cos</sub> &gt; ρ<sub>líquid</sub>), el cos <b>s'enfonsa</b>.", "Si P = E totalment submergit (ρ<sub>cos</sub> = ρ<sub>líquid</sub>), queda en <b>equilibri</b> a qualsevol profunditat.",
            "Si P &lt; E quan està submergit (ρ<sub>cos</sub> &lt; ρ<sub>líquid</sub>), puja i <b>sura</b>: queda amb una part fora de manera que l'empenta de la part submergida iguali el pes.")
    b += EX("Exemple · Un vaixell", "Un vaixell de 5 000 tones sura quan desallotja 5 000 tones d'aigua. En aigua de mar (més densa) en desallotja menys volum que en aigua dolça: per això un vaixell s'enfonsa una mica més quan entra en un riu.")
    b += P("El <b>ludió</b> (o diablet de Descartes) és un petit flotador amb aire dins d'una ampolla plena d'aigua. Si premem l'ampolla, la pressió comprimeix l'aire del ludió, hi entra aigua, la seva densitat mitjana augmenta i baixa; si deixem de prémer, torna a pujar.")
    b += S(9, "Com funciona un submarí")
    b += P("Un submarí controla la seva <b>densitat mitjana</b> amb els <b>tancs de llast</b>. Per baixar, omple els tancs d'aigua: la massa augmenta sense que canviï el volum, la densitat mitjana supera la de l'aigua i s'enfonsa. Per aturar-se a una profunditat, ajusta l'aigua fins que el pes iguala l'empenta. Per pujar, expulsa l'aigua amb aire comprimit o amb bombes, es fa més lleuger i sura.")
    b += FIG(T4.submari(a), "Els tancs de llast d'un submarí.", "160mm")
    b += S(10, "Monturiol i la ciència col·lectiva")
    b += P("<b>Narcís Monturiol</b> (Figueres, 1819 – Sant Martí de Provençals, 1885) va pensar el submarí veient la duresa de la feina dels pescadors de corall de Cadaqués. El 1859 va provar l'<b>Ictineo I</b> al port de Barcelona i el 1864 va avarar l'<b>Ictineo II</b>, de 17 m de llarg, amb tancs de llast, un casc doble i un sistema per renovar l'aire.",
           "El gran problema dels submarins era el motor: un motor de vapor normal necessita aire per cremar el combustible. Monturiol va idear un <b>motor químic anaeròbic</b>: una reacció de clorat de potassi, zinc i diòxid de manganès (catalitzador) desprenia calor per moure una màquina de vapor i, alhora, <b>oxigen</b> que la tripulació podia respirar (2 KClO₃ → 2 KCl + 3 O₂). Va ser un dels primers motors del món que funcionaven sense aire.",
           "L'Ictineo no el va fer una persona sola: hi van treballar enginyers, fusters, mecànics i químics, i es va finançar amb aportacions populars. Malgrat l'èxit de les proves, el projecte va fallir per manca de diners i l'Ictineo II es va vendre com a ferralla el 1868. La ciència és una obra <b>col·lectiva</b> i depèn també del suport de la societat. Avui una rèplica de l'Ictineo II es pot veure al port de Barcelona.")
    b += TIP("Ciència i societat avui", "Els robots submarins es fan servir per estudiar les praderies de posidònia, controlar la contaminació, cartografiar el fons marí o inspeccionar ports i cables. Com a ciutadania, podem decidir quins usos volem prioritzar per al nostre litoral.")
    b += KW(("Pressió", "força perpendicular per unitat de superfície; en Pa"), ("Pressió hidrostàtica", "p = ρ · g · h"), ("Vasos comunicants", "el líquid arriba a la mateixa altura"), ("Principi de Pascal", "la pressió es transmet igual a tot el líquid"),
            ("Premsa hidràulica", "multiplica forces: F₁ / S₁ = F₂ / S₂"), ("Pressió atmosfèrica", "pressió del pes de l'aire; 1 atm = 760 mmHg"), ("Empenta", "força cap amunt que fa un fluid sobre un cos submergit"),
            ("Principi d'Arquimedes", "E = pes del fluid desallotjat"), ("Pes aparent", "P − E"), ("Tancs de llast", "dipòsits que canvien la densitat mitjana d'un submarí"))
    return b

FUNCS = {1: sda1, 2: sda2, 3: sda3, 4: sda4, 5: sda5, 6: sda6}
