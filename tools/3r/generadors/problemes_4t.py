"""Dossiers de problemes de 4t d'ESO (exercicis del tipus de les fitxes de cada SdA)."""
from gen_problemes import Q, nf
from gen_teoria import T

# ======================================================================== SdA 1
def sda1():
    S = []
    S.append(("Models atòmics", [
        (1, Q(1, "Ordena i descriu", "els models atòmics de Thomson, Bohr, Dalton, Rutherford i el model actual."), "Dalton (esfera massissa) → Thomson (esfera positiva amb electrons) → Rutherford (nucli i escorça) → Bohr (nivells d'energia) → actual (orbitals)"),
        (2, Q(2, "Experiment i model.", "Relaciona cada experiment amb el model que va fer caure: a) raigs catòdics (descobriment de l'electró); b) làmina d'or; c) espectres de línies."), "a) Dalton · b) Thomson · c) Rutherford"),
        (2, Q(2, "La làmina d'or.", "Per què la majoria de partícules alfa travessen la làmina d'or i unes poques reboten? Quina conclusió en treu Rutherford sobre la mida del nucli?"), "L'àtom és gairebé buit; només reboten les que xoquen de cara amb el nucli, molt petit, dens i positiu."),
        (1, Q(1, "Les partícules.", "Completa: el protó té càrrega ___ i és al ___; el neutró té càrrega ___ i és al ___; l'electró té càrrega ___ i és a l'___. Quina partícula té una massa gairebé negligible?"), "+1, nucli · 0, nucli · −1, escorça · l'electró"),
    ]))
    S.append(("Z, A, ions i isòtops", [
        (1, Q(1, "Completa la taula.", "", table=T(["Espècie", "Z", "A", "p⁺", "n", "e⁻"], [["²³Na", "11", "", "", "", ""], ["³⁵Cl⁻", "17", "", "", "", ""], ["⁴⁰Ca²⁺", "20", "", "", "", ""], ["⁵⁶Fe³⁺", "26", "", "", "", ""], ["", "", "", "8", "8", "10"]])),
         "²³Na: 11, 12, 11 · ³⁵Cl⁻: 17, 18, 18 · ⁴⁰Ca²⁺: 20, 20, 18 · ⁵⁶Fe³⁺: 26, 30, 23 · ¹⁶O²⁻ (Z = 8, A = 16)"),
        (2, Q(2, "Massa atòmica.", "El bor natural té un 19,9 % de ¹⁰B (10,01 u) i un 80,1 % d'¹¹B (11,01 u). Calcula'n la massa atòmica."), f"{nf(0.199*10.01+0.801*11.01, 2)} u"),
        (3, Q(3, "L'abundància.", "El liti té dos isòtops: ⁶Li (6,02 u) i ⁷Li (7,02 u). Si la massa atòmica és 6,94 u, quin percentatge hi ha de cada isòtop?"), f"⁶Li: {nf((7.02-6.94)/1*100, 0)} % · ⁷Li: {nf((6.94-6.02)/1*100, 0)} %"),
        (2, Q(2, "Vertader o fals?", "Justifica:", "Dos isòtops tenen el mateix nombre màssic.", "Un anió té més electrons que protons.", "El ³⁷Cl i el ³⁵Cl tenen propietats químiques molt diferents.", "Per formar Mg²⁺, el magnesi perd 2 protons."), "a) F: mateix Z · b) V · c) F · d) F: perd 2 electrons"),
    ]))
    S.append(("La llum, els espectres i el model de Bohr", [
        (1, Q(1, "Continu o de línies?", "Quin espectre fa: a) el filament d'una bombeta · b) un llum de sodi del carrer · c) el Sol · d) un tub amb hidrogen excitat?"), "a) continu · b) de línies · c) continu (amb línies d'absorció) · d) de línies"),
        (2, Q(2, "Salts d'electrons.", "Explica amb el model de Bohr per què una sal de coure dona color verd blavós a la flama. Per què cada element té el seu espectre?"), "Els electrons absorbeixen energia, salten a nivells superiors i en tornar emeten llum de l'energia del salt. Els nivells de cada element són diferents."),
        (2, Q(2, "Més o menys energia?", "Un salt d'electrons emet llum vermella i un altre, llum blava. Quin salt és més gran? Per què?"), "El de la llum blava: la llum blava porta més energia que la vermella."),
        (2, Q(2, "L'estrella misteriosa.", "En l'assaig a la flama, una sal sense etiqueta fa una flama vermella intensa. Quins metalls podria contenir? Com ho confirmaries?"), "Estronci o liti. Comparant-ho amb sals conegudes o amb un espectroscopi (línies característiques)."),
    ]))
    S.append(("Configuració electrònica i taula periòdica", [
        (1, Q(1, "Configuracions.", "Escriu la configuració electrònica de: N (7), Na (11), S (16), Ar (18), K (19), Ca (20), Fe (26), Br (35)."),
         "N 1s² 2s² 2p³ · Na …3s¹ · S …3s² 3p⁴ · Ar …3s² 3p⁶ · K …3p⁶ 4s¹ · Ca …4s² · Fe …4s² 3d⁶ · Br …4s² 3d¹⁰ 4p⁵"),
        (2, Q(2, "Electrons de valència.", "Quants electrons de valència tenen O, Mg, Cl, Al i Ne? Quin ió formarà cadascun?"), "O 6 → O²⁻ · Mg 2 → Mg²⁺ · Cl 7 → Cl⁻ · Al 3 → Al³⁺ · Ne 8 → cap"),
        (2, Q(2, "On és?", "Situa a la taula (període, grup i bloc): a) 1s² 2s² 2p⁵ · b) …3s² · c) …4s² 3d⁵ · d) …4s² 4p⁶. Quin element és?"), "a) 2, 17, p: F · b) 3, 2, s: Mg · c) 4, 7, d: Mn · d) 4, 18, p: Kr"),
        (2, Q(2, "Configuració dels ions.", "Escriu la configuració de Na⁺, Cl⁻, Mg²⁺ i O²⁻. A quin gas noble s'assembla cadascuna?"), "Na⁺ i Mg²⁺: 1s² 2s² 2p⁶ (Ne) · Cl⁻: …3s² 3p⁶ (Ar) · O²⁻: 1s² 2s² 2p⁶ (Ne)"),
        (3, Q(3, "Per què funciona la taula?", "Explica per què el liti, el sodi i el potassi tenen propietats semblants, i per què el clor i l'argó, que són al mateix període, en tenen de molt diferents."), "Li, Na, K: la mateixa configuració de valència (s¹). Cl (s² p⁵) tendeix a guanyar un electró; Ar (s² p⁶) té la capa completa i no reacciona."),
    ]))
    S.append(("Enllaç químic", [
        (1, Q(1, "Quin enllaç?", "KCl, H₂O, Cu, CO₂, MgO, Fe, NH₃, CaCl₂, diamant, Al."), "Iònic: KCl, MgO, CaCl₂ · covalent: H₂O, CO₂, NH₃, diamant (xarxa) · metàl·lic: Cu, Fe, Al"),
        (2, Q(2, "Prediu les propietats.", "Prediu si és sòlid, líquid o gas a 25 °C, si es dissol en aigua i si condueix: a) nitrat de potassi · b) diòxid de carboni · c) magnesi."), "a) sòlid, soluble, condueix fos o dissolt · b) gas, poc soluble, no condueix · c) sòlid, no soluble, condueix"),
        (3, Q(3, "Explica-ho.", "Per què el clorur de sodi no condueix en estat sòlid però sí fos o dissolt en aigua?"), "En el sòlid els ions estan fixos a la xarxa; fos o dissolt, els ions es poden moure i transporten la càrrega."),
        (2, Q(2, "Dibuixa l'enllaç.", "Representa amb els electrons de valència com es formen el fluorur de liti (LiF) i la molècula de clor (Cl₂)."), "LiF: el Li cedeix el seu electró al F (Li⁺ F⁻) · Cl₂: comparteixen un parell d'electrons"),
    ]))
    S.append(("Formulació inorgànica", [
        (1, Q(1, "Binaris.", "Formula: òxid de calci · diòxid de carboni · òxid de ferro(III) · clorur de sodi · hidrur de liti · clorur d'estronci · sulfur de zinc · triòxid de sofre · àcid clorhídric · amoníac."), "CaO · CO₂ · Fe₂O₃ · NaCl · LiH · SrCl₂ · ZnS · SO₃ · HCl (aq) · NH₃"),
        (1, Q(1, "Anomena.", "Al₂O₃ · CuCl · CuCl₂ · K₂O · FeS · N₂O₅ · BaCl₂ · CH₄ · MgH₂ · PCl₃."), "òxid d'alumini · clorur de coure(I) · clorur de coure(II) · òxid de potassi · sulfur de ferro(II) · pentaòxid de dinitrogen · clorur de bari · metà · hidrur de magnesi · triclorur de fòsfor"),
        (2, Q(2, "Hidròxids i oxoàcids.", "Formula o anomena: NaOH · hidròxid de calci · Fe(OH)₃ · àcid nítric · H₂SO₄ · àcid carbònic · HClO₄ · hidròxid de potassi."), "hidròxid de sodi · Ca(OH)₂ · hidròxid de ferro(III) · HNO₃ · àcid sulfúric · H₂CO₃ · àcid perclòric · KOH"),
        (2, Q(2, "Oxosals.", "Formula o anomena: KNO₃ · carbonat de calci · Sr(NO₃)₂ · sulfat de coure(II) · KClO₄ · carbonat de liti · Na₂SO₄ · nitrat de bari."), "nitrat de potassi · CaCO₃ · nitrat d'estronci · CuSO₄ · perclorat de potassi · Li₂CO₃ · sulfat de sodi · Ba(NO₃)₂"),
        (3, Q(3, "La recepta del color.", "Per fer una estrella verda es fa servir nitrat de bari i, per fer-ne una de blava, clorur de coure(I). Escriu-ne les fórmules i explica d'on surt el color."), "Ba(NO₃)₂ i CuCl. El color el donen els electrons dels metalls (Ba, Cu) excitats per la calor."),
    ]))
    return {"sub": "Models atòmics, Z, A, ions i isòtops, espectres i model de Bohr, configuració electrònica, taula periòdica, enllaç i formulació.", "seccions": S}

# ======================================================================== SdA 2
def sda2():
    S = []
    S.append(("Mescles, dissolucions i col·loides", [
        (1, Q(1, "Classifica", "com a dissolució, col·loide o suspensió: aigua mineral, llet, aigua amb sorra, maionesa, aire, boira, suc de taronja natural, vinagre."), "Dissolucions: aigua mineral, aire, vinagre · col·loides: llet, maionesa, boira · suspensions: aigua amb sorra, suc de taronja"),
        (2, Q(2, "L'efecte Tyndall.", "Com distingiries amb un làser un got d'aigua amb sal d'un got d'aigua amb unes gotes de llet? Explica per què passa."), "Al col·loide (llet) el feix es veu: les partícules dispersen la llum. A la dissolució, no."),
        (2, Q(2, "L'etiqueta.", "Una aigua té un residu sec de 320 mg/L. Quina mineralització té? Si evaporem 5 L, quina massa de sals queda?"), "Feble (50–500 mg/L) · 1,6 g"),
    ]))
    S.append(("Concentració: g/L, %, ppm", [
        (1, Q(1, "En g/L.", "a) 8 g de sal en 400 mL · b) 0,5 g en 250 mL · c) 120 mg en 2 L (en mg/L)."), "a) 20 g/L · b) 2 g/L · c) 60 mg/L"),
        (1, Q(1, "En % en massa.", "Dissolem 9 g de sal en 991 g d'aigua. Quin és el % en massa? Quin producte és?"), "0,9 %: sèrum fisiològic"),
        (2, Q(2, "En % en volum.", "Quants mL d'etanol hi ha en una ampolla de 750 mL de vi de 13 % vol? I en 200 mL d'alcohol de farmàcia del 96 %?"), f"{nf(0.13*750, 1)} mL · 192 mL"),
        (2, Q(2, "Ppm.", "Una mostra d'aigua d'1 kg conté 0,05 g de nitrats. Quina concentració té en ppm? Compleix el límit de 50 mg/L?"), "50 ppm: just al límit"),
        (2, Q(2, "L'etiqueta de l'ampolla.", "Una aigua conté 45 mg/L de calci i 18 mg/L de magnesi. a) Quina massa de calci prens si beus 1,5 L al dia? b) Quina massa de magnesi hi ha en una garrafa de 8 L?"), "a) 67,5 mg · b) 144 mg"),
    ]))
    S.append(("Preparar i diluir dissolucions", [
        (1, Q(1, "Prepara.", "Quina massa de NaCl cal per fer 250 mL de dissolució de 9 g/L? Descriu el procediment i el material."), "2,25 g; balança, vas de precipitats, matràs aforat de 250 mL, enrasar"),
        (2, Q(2, "Dilueix.", "Quin volum d'una dissolució de 20 g/L cal per preparar 500 mL de 4 g/L?"), "100 mL"),
        (2, Q(2, "Tres dilucions.", "Tenim una dissolució de 10 g/L. En diluïm 10 mL fins a 100 mL. D'aquesta, en diluïm 10 mL fins a 100 mL, i ho repetim una tercera vegada. Quina concentració té cada dilució?"), "1 g/L · 0,1 g/L · 0,01 g/L"),
    ]))
    S.append(("El mol i la massa molar", [
        (1, Q(1, "Masses molars.", "Calcula: H₂O, NaCl, CaCO₃, CO₂, C₆H₁₂O₆, MgSO₄, Ca(OH)₂, NaHCO₃."), "18 · 58,5 · 100 · 44 · 180 · 120 · 74 · 84 g/mol"),
        (1, Q(1, "Mols i grams.", "a) Quants mols són 36 g d'aigua? b) Quina massa tenen 0,5 mol de NaCl? c) Quants mols hi ha en 10 g de CaCO₃?"), "a) 2 mol · b) 29,25 g · c) 0,1 mol"),
        (2, Q(2, "Partícules.", "Quantes molècules hi ha en 9 g d'aigua? I quants àtoms d'hidrogen?"), "3,01 · 10²³ molècules · 6,02 · 10²³ àtoms d'H"),
        (2, Q(2, "El calci de l'aigua.", "Una aigua té 80 mg/L de Ca²⁺ (40 g/mol). Quants mols i quants ions de calci hi ha en un got de 250 mL?"), f"5 · 10⁻⁴ mol · {nf(5e-4*6.022e23, 2, True)} ions"),
        (3, Q(3, "Una gota d'aigua.", "Una gota d'aigua té un volum de 0,05 mL (1 g/mL). Quantes molècules d'aigua conté? Compara-ho amb les persones del planeta (8 · 10⁹)."), f"{nf(0.05/18*6.022e23, 2, True)} molècules: unes {nf(0.05/18*6.022e23/8e9, 1, True)} vegades més"),
    ]))
    S.append(("La molaritat", [
        (1, Q(1, "Calcula la molaritat.", "a) 0,2 mol de NaCl en 500 mL · b) 11,7 g de NaCl en 250 mL · c) 18 g de glucosa en 1 L."), "a) 0,4 mol/L · b) 0,8 mol/L · c) 0,1 mol/L"),
        (2, Q(2, "Quina massa?", "Quina massa de NaOH (40 g/mol) cal per preparar 250 mL d'una dissolució 0,5 mol/L?"), "5 g"),
        (2, Q(2, "Dilució en mol/L.", "Quin volum d'HCl 2 mol/L cal per preparar 500 mL d'HCl 0,1 mol/L?"), "25 mL"),
        (3, Q(3, "L'anàlisi de sang.", "La glucosa d'una persona és de 95 mg/dL. Expressa-ho en g/L i en mmol/L (glucosa: 180 g/mol)."), f"0,95 g/L · {nf(0.95/180*1000, 2)} mmol/L"),
    ]))
    S.append(("Conductivitat, duresa i aigua de l'aixeta", [
        (2, Q(2, "La recta de calibratge.", "Amb aquests patrons, una mostra té una conductivitat de 1 400 µS/cm. Quina concentració de NaCl té?", table=T(["c (g/L)", "0,2", "0,4", "0,6", "0,8"], [["κ (µS/cm)", "400", "800", "1 200", "1 600"]])), "0,7 g/L"),
        (2, Q(2, "Per què condueix?", "Per què l'aigua destil·lada gairebé no condueix i l'aigua mineral sí? Com canviaria la conductivitat d'una aigua de mineralització forta?"), "La mineral té ions dissolts; com més ions, més conductivitat: seria més alta."),
        (2, Q(2, "La duresa.", "Una aigua té 350 mg/L de CaCO₃. Quina duresa té en graus francesos (1 °F = 10 mg/L de CaCO₃)? És tova o dura? Quins problemes pot causar?"), "35 °F: dura · calç a aixetes i electrodomèstics, menys escuma amb el sabó"),
        (3, Q(3, "Aixeta o ampolla?", "Una família beu 4 L d'aigua al dia. Calcula el cost anual amb aigua de l'aixeta (2 €/m³) i amb aigua embotellada (0,30 €/L). Quantes ampolles d'1,5 L llençaria a l'any?"), f"Aixeta: {nf(4*365/1000*2, 2)} € · ampolla: {nf(4*365*0.30, 0)} € · {nf(4*365/1.5, 0)} ampolles"),
        (2, Q(2, "Fonts fiables.", "Ordena de més a menys fiable i justifica-ho: un vídeo d'un influencer que ven filtres, l'anàlisi de l'aigua del web d'Aigües de Barcelona, un article d'un diari que cita l'Agència de Salut Pública."), "Anàlisi oficial (dades i controls) → article que cita una institució → vídeo amb interès comercial i sense fonts."),
    ]))
    return {"sub": "Dissolucions i col·loides, concentració, preparar i diluir, el mol, la molaritat, la conductivitat i la duresa.",
            "dades": "Masses atòmiques (g/mol): H = 1 · C = 12 · O = 16 · Na = 23 · Mg = 24 · S = 32 · Cl = 35,5 · Ca = 40 · N<sub>A</sub> = 6,022 · 10²³", "seccions": S}

# ======================================================================== SdA 3
def sda3():
    S = []
    S.append(("Ajustar i llegir equacions", [
        (1, Q(1, "Ajusta.", "a) CH₄ + O₂ → CO₂ + H₂O · b) N₂ + H₂ → NH₃ · c) Fe + O₂ → Fe₂O₃ · d) C₂H₅OH + O₂ → CO₂ + H₂O · e) C₄H₁₀ + O₂ → CO₂ + H₂O · f) Al + HCl → AlCl₃ + H₂."),
         "a) 1, 2, 1, 2 · b) 1, 3, 2 · c) 4, 3, 2 · d) 1, 3, 2, 3 · e) 2, 13, 8, 10 · f) 2, 6, 2, 3"),
        (2, Q(2, "Molècules, mols i grams.", "Llegeix l'equació 2 H₂ + O₂ → 2 H₂O en molècules, en mols i en grams, i comprova la llei de Lavoisier."), "2 molècules + 1 → 2 · 2 mol + 1 mol → 2 mol · 4 g + 32 g → 36 g"),
        (2, Q(2, "Comprova Lavoisier.", "Calcula la massa de cada terme de C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O (per mol) i comprova que es conserva."), "44 + 160 = 204 g → 132 + 72 = 204 g"),
        (2, Q(2, "Mols de producte.", "Quants mols d'aigua es formen quan cremen 3 mol de propà? Quants mols d'oxigen calen?"), "12 mol d'aigua · 15 mol d'O₂"),
        (1, Q(1, "Quina està ajustada?", "a) 2 CO + O₂ → 2 CO₂ · b) H₂ + Cl₂ → HCl · c) CaCO₃ → CaO + CO₂ · d) Na + H₂O → NaOH + H₂."), "a) sí · b) no (2 HCl) · c) sí · d) no (2 Na + 2 H₂O → 2 NaOH + H₂)"),
    ]))
    S.append(("La química del carboni", [
        (1, Q(1, "Anomena.", "CH₄ · CH₃–CH₃ · CH₃–CH₂–CH₃ · CH₂=CH₂ · CH≡CH · CH₃OH · CH₃–CH₂OH · C₄H₁₀."), "metà · età · propà · etè · etí · metanol · etanol · butà"),
        (1, Q(1, "Formula.", "pentà · propè · propí · octà · propan-1-ol · but-1-è."), "CH₃–CH₂–CH₂–CH₂–CH₃ · CH₂=CH–CH₃ · CH≡C–CH₃ · C₈H₁₈ · CH₃–CH₂–CH₂OH · CH₂=CH–CH₂–CH₃"),
        (2, Q(2, "Alcà, alquè, alquí o alcohol?", "Classifica: C₃H₈, C₂H₄, C₃H₄, C₂H₅OH, C₅H₁₂, C₄H₈. Quina fórmula general tenen els alcans?"), "Alcans: C₃H₈, C₅H₁₂ · alquens: C₂H₄, C₄H₈ · alquí: C₃H₄ · alcohol: C₂H₅OH · CₙH₂ₙ₊₂"),
        (2, Q(2, "Per què tants compostos?", "Explica per què el carboni forma milions de compostos diferents."), "Fa 4 enllaços covalents i s'uneix amb altres carbonis formant cadenes llargues, ramificades o tancades, amb enllaços simples, dobles o triples."),
    ]))
    S.append(("Les combustions", [
        (1, Q(1, "Escriu i ajusta", "la combustió completa del metà, el propà i l'etanol."), "CH₄ + 2 O₂ → CO₂ + 2 H₂O · C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O · C₂H₅OH + 3 O₂ → 2 CO₂ + 3 H₂O"),
        (2, Q(2, "Completa o incompleta?", "Quines diferències hi ha entre una combustió completa i una d'incompleta? Per què és perillosa la incompleta? Com reconeixes una flama de combustió incompleta?"), "Completa: CO₂ + H₂O amb prou oxigen · incompleta: CO (tòxic) i sutge. Flama groga i fumosa."),
        (2, Q(2, "Demostra-ho.", "Com demostraries que en cremar una espelma es formen aigua i diòxid de carboni?"), "Got fred a sobre (s'entela: aigua) · gasos en aigua de calç (es torna tèrbola: CO₂)."),
        (2, Q(2, "Els NOₓ.", "Per què els cotxes emeten òxids de nitrogen si la gasolina no porta nitrogen? Escriu les reaccions."), "A la temperatura del motor reaccionen el N₂ i l'O₂ de l'aire: N₂ + O₂ → 2 NO; 2 NO + O₂ → 2 NO₂"),
    ]))
    S.append(("Estequiometria", [
        (2, Q(2, "Metà i CO₂.", "Quina massa de CO₂ es forma en cremar 32 g de metà? I quanta aigua?"), "88 g de CO₂ · 72 g d'aigua"),
        (2, Q(2, "La bombona de butà.", "Quina massa d'oxigen cal per cremar 1 kg de butà (2 C₄H₁₀ + 13 O₂ → 8 CO₂ + 10 H₂O)? Quin CO₂ es forma?"), f"{nf(1000/58*6.5*32/1000, 2)} kg d'O₂ · {nf(1000/58*4*44/1000, 2)} kg de CO₂"),
        (2, Q(2, "La calç.", "Quina massa de CaCO₃ cal descompondre per obtenir 112 kg de CaO (CaCO₃ → CaO + CO₂)?"), "200 kg"),
        (2, Q(2, "L'airbag.", "L'airbag s'infla amb nitrogen: 2 NaN₃ → 2 Na + 3 N₂. Quina massa de N₂ es forma amb 65 g de NaN₃ (65 g/mol)?"), "42 g"),
        (3, Q(3, "Reactiu limitant.", "Fem reaccionar 12 g de magnesi amb 0,4 mol d'HCl: Mg + 2 HCl → MgCl₂ + H₂. Quin és el reactiu limitant? Quina massa d'hidrogen es desprèn?"), "Mg = 0,5 mol (necessitaria 1 mol d'HCl): limitant l'HCl · 0,2 mol de H₂ = 0,4 g"),
        (3, Q(3, "Gasolina i CO₂.", "Considerant la gasolina com a octà (d = 0,75 kg/L), calcula el CO₂ que fa un cotxe que gasta 6 L cada 100 km. Quants grams de CO₂ per km?"), f"{nf(6*0.75*1000/114*8*44/1000, 1)} kg per 100 km · {nf(6*0.75*1000/114*8*44/100, 0)} g/km"),
    ]))
    S.append(("L'energia de les reaccions", [
        (1, Q(1, "Exo o endo?", "a) combustió del butà · b) descomposició de la pedra calcària · c) fotosíntesi · d) respiració · e) dissoldre nitrat d'amoni (es refreda)."), "Exotèrmiques: a, d · endotèrmiques: b, c, e"),
        (2, Q(2, "Diagrama d'energia.", "Dibuixa el diagrama d'energia de la combustió del metà. Marca l'energia d'activació i l'energia alliberada. Per què cal una espurna per encendre el gas?"), "Productes més avall que els reactius. Cal superar l'energia d'activació."),
        (2, Q(2, "La calorimetria.", "Cremem 1,5 g d'etanol i escalfem 250 g d'aigua de 18 °C a 45 °C. a) Quanta calor guanya l'aigua? b) Quanta per gram d'etanol? c) Si el valor teòric és 30 kJ/g, quin és el rendiment?"), f"a) {nf(250*4.18*27/1000, 1)} kJ · b) {nf(250*4.18*27/1000/1.5, 1)} kJ/g · c) {nf(250*4.18*27/1000/1.5/30*100, 0)} %"),
        (3, Q(3, "Compara combustibles.", "El metà allibera 55 kJ/g i l'octà 47 kJ/g. Per obtenir 1 000 kJ, quin CO₂ fa cada un? Quin contamina menys per energia?"), f"Metà: {nf(1000/55*44/16, 0)} g · octà: {nf(1000/47*16*44/(2*114), 0)} g: el metà"),
    ]))
    S.append(("Mobilitat, aire i salut", [
        (2, Q(2, "CO₂ per persona.", "Un cotxe emet 150 g de CO₂/km i un autobús, 800 g/km. Quant CO₂ emet cada persona en un trajecte de 5 km si al cotxe hi va 1 persona i a l'autobús 40?"), "Cotxe: 750 g · autobús: 100 g per persona"),
        (2, Q(2, "Contaminants.", "Quina diferència hi ha entre l'efecte del CO₂ i el del NO₂ o les partícules fines? Per què es pacifiquen els entorns escolars?"), "CO₂: escalfament global · NO₂ i partícules: danyen la salut de les persones que les respiren. Els infants són més vulnerables."),
    ]))
    return {"sub": "Ajust i lectura d'equacions, química del carboni, combustions, estequiometria i reactiu limitant, energia de les reaccions.",
            "dades": "Masses atòmiques (g/mol): H = 1 · C = 12 · N = 14 · O = 16 · Na = 23 · Mg = 24 · Cl = 35,5 · Ca = 40 · c(aigua) = 4,18 J/(g·°C)", "seccions": S}

# ======================================================================== SdA 4
def sda4():
    S = []
    S.append(("Àcids, bases i pH", [
        (1, Q(1, "Àcid, bàsic o neutre?", "a) suc de llimona (pH 2) · b) lleixiu (pH 12) · c) aigua pura · d) vinagre (pH 3) · e) bicarbonat (pH 8,5) · f) pluja àcida (pH 4,5)."), "Àcids: a, d, f · bàsics: b, e · neutre: c"),
        (1, Q(1, "Propietats.", "Escriu dues propietats dels àcids i dues de les bases, i dos exemples de cada a casa."), "Àcids: gust agre, ataquen metalls i marbre (vinagre, llimona) · bases: tacte sabonós, dissolen greixos (lleixiu, amoníac)"),
        (2, Q(2, "Quantes vegades?", "Una dissolució té pH 3 i una altra pH 5. Quina és més àcida i quantes vegades?"), "La de pH 3, 100 vegades més"),
        (2, Q(2, "L'indicador de col.", "El suc de col llombarda és vermell en medi àcid, lila en neutre i verd en bàsic. De quin color es posarà amb vinagre, amb aigua i amb lleixiu diluït?"), "vermell · lila · verd (o groc)"),
        (2, Q(2, "Arrhenius.", "Escriu la dissociació en aigua de l'HCl, l'HNO₃, el NaOH i el KOH. Quins són àcids i quins bases?"), "HCl → H⁺ + Cl⁻ · HNO₃ → H⁺ + NO₃⁻ (àcids) · NaOH → Na⁺ + OH⁻ · KOH → K⁺ + OH⁻ (bases)"),
    ]))
    S.append(("Neutralització i carbonats", [
        (1, Q(1, "Completa i ajusta.", "a) HCl + NaOH → · b) H₂SO₄ + KOH → · c) HNO₃ + Ca(OH)₂ → · d) HCl + Mg(OH)₂ →"), "a) NaCl + H₂O · b) H₂SO₄ + 2 KOH → K₂SO₄ + 2 H₂O · c) 2 HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + 2 H₂O · d) 2 HCl + Mg(OH)₂ → MgCl₂ + 2 H₂O"),
        (2, Q(2, "Àcid i carbonat.", "Escriu i ajusta la reacció del carbonat de calci amb l'àcid clorhídric. Quina evidència es veu? Com la faries servir per reconèixer una roca calcària?"), "CaCO₃ + 2 HCl → CaCl₂ + H₂O + CO₂ · efervescència · una gota d'àcid fa bombolles"),
        (2, Q(2, "Usos.", "Explica per què: a) els antiàcids alleugen l'acidesa d'estómac; b) s'afegeix calç als sòls massa àcids."), "a) són bases que neutralitzen l'excés d'àcid · b) la calç (bàsica) neutralitza l'acidesa del sòl"),
        (3, Q(3, "Quant de reactiu?", "Quina massa de NaOH (40 g/mol) neutralitza 100 mL d'HCl 0,5 mol/L?"), "0,05 mol → 2 g"),
    ]))
    S.append(("La pluja àcida i la pedra", [
        (1, Q(1, "D'on ve?", "Quins gasos causen la pluja àcida i d'on surten? Quins àcids formen?"), "SO₂ (combustibles amb sofre) i NOₓ (motors i calefaccions) · àcid sulfúric i nítric"),
        (2, Q(2, "Les reaccions.", "Ajusta: SO₂ + O₂ → SO₃ · SO₃ + H₂O → H₂SO₄ · CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂. Per què el guix fa malbé la pedra?"), "2 SO₂ + O₂ → 2 SO₃ · les altres ja estan ajustades. El guix és més tou i soluble i ocupa més volum: la pedra s'esquerda."),
        (3, Q(3, "La pedra que es desfà.", "Quina massa de guix (CaSO₄, 136 g/mol) es forma quan reaccionen 50 g de marbre (CaCO₃) amb prou àcid sulfúric?"), "0,5 mol → 68 g"),
        (2, Q(2, "Barcelona.", "Les emissions de SO₂ a Barcelona han baixat molt, però el NO₂ continua alt en molts carrers. A què creus que es deu? Quines mesures proposaries?"), "Menys carbó i combustibles amb sofre; el NO₂ ve sobretot del trànsit. Menys cotxes, transport públic, zones de baixes emissions."),
    ]))
    S.append(("Velocitat de reacció i col·lisions", [
        (1, Q(1, "Quin factor?", "a) La pols de marbre reacciona més de pressa que un tros · b) l'àcid concentrat ataca més de pressa · c) a l'estiu les façanes es degraden més de pressa · d) el catalitzador del cotxe."), "a) superfície · b) concentració · c) temperatura · d) catalitzador"),
        (2, Q(2, "Xocs eficaços.", "Quines dues condicions ha de complir un xoc per ser eficaç? Explica per què augmentar la temperatura accelera una reacció."), "Prou energia (≥ Eₐ) i orientació adequada. A més T, les partícules van més ràpid: més xocs i més xocs amb energia suficient."),
        (2, Q(2, "Els catalitzadors.", "Dibuixa el diagrama d'energia d'una reacció amb catalitzador i sense. Què canvia i què no?"), "Canvia (baixa) l'energia d'activació; no canvien els reactius, els productes ni l'energia de reacció."),
        (2, Q(2, "Llegeix les dades.", "En la reacció del marbre amb àcid, el volum de CO₂ recollit és: 0 s → 0 mL; 30 s → 40 mL; 60 s → 65 mL; 90 s → 80 mL; 120 s → 85 mL. a) Calcula la velocitat mitjana en els primers 30 s i entre 90 i 120 s. b) Per què va disminuint?"), "a) 1,33 mL/s i 0,17 mL/s · b) es van gastant els reactius (baixa la concentració)"),
        (3, Q(3, "Dissenya l'experiment.", "Dissenya un experiment per estudiar com afecta la concentració de l'àcid a la velocitat d'atac del marbre: variables, material, mesures i com presentaries els resultats."), "Independent: concentració · dependent: CO₂ o massa perduda en un temps · controlades: massa i mida del marbre, volum, temperatura. Taula i gràfica."),
    ]))
    S.append(("Oxidació-reducció, corrosió i piles", [
        (1, Q(1, "Oxidació o reducció?", "a) Fe → Fe²⁺ + 2 e⁻ · b) Cu²⁺ + 2 e⁻ → Cu · c) Zn → Zn²⁺ + 2 e⁻ · d) Ag⁺ + e⁻ → Ag."), "a) oxidació · b) reducció · c) oxidació · d) reducció"),
        (2, Q(2, "Hi haurà reacció?", "Amb la sèrie de reactivitat (K, Na, Ca, Mg, Al, Zn, Fe, Pb, Cu, Ag, Au), prediu si hi ha reacció: a) un clau de ferro en sulfat de coure · b) una làmina de coure en sulfat de zinc · c) zinc en nitrat de plata."), "a) sí (el Fe desplaça el Cu) · b) no · c) sí"),
        (2, Q(2, "Els sis claus.", "Prediu en quins tubs es rovellarà el clau: a) aire sec · b) aigua bullida amb oli a sobre · c) aigua i aire · d) aigua salada · e) clau pintat · f) clau embolicat amb zinc. Què cal perquè el ferro es rovelli?"), "Es rovellen c i d (més ràpid en d). Cal aigua i oxigen."),
        (2, Q(2, "La pila de Daniell.", "En una pila zinc–coure, quin metall és l'ànode i quin el càtode? Cap on van els electrons? Escriu les semireaccions. Per a què serveix el pont salí?"), "Ànode: Zn (Zn → Zn²⁺ + 2 e⁻) · càtode: Cu (Cu²⁺ + 2 e⁻ → Cu) · electrons del Zn al Cu · el pont salí tanca el circuit"),
        (3, Q(3, "Protegir el ferro.", "Explica com protegeix el ferro cada mètode: pintura, galvanitzat, ànode de sacrifici de magnesi, acer inoxidable."), "Pintura: barrera · galvanitzat: capa de zinc que s'oxida abans · ànode: el Mg (més reactiu) es corroeix en lloc del ferro · inoxidable: el crom fa una capa protectora"),
        (2, Q(2, "Ciència i societat.", "Agnes Pockels va fer recerca des de la cuina de casa. Per què? Posa un exemple d'un biaix de gènere en la ciència."), "No la van deixar estudiar a la universitat per ser dona. Exemples: autories oblidades, menys reconeixement (resposta oberta)."),
        (2, Q(2, "Oxidant i reductor.", "En la reacció Zn + CuSO₄ → ZnSO₄ + Cu, quin metall s'oxida i quin es redueix? Escriu les dues semireaccions."), "Zn s'oxida (Zn → Zn²⁺ + 2 e⁻) · Cu²⁺ es redueix (Cu²⁺ + 2 e⁻ → Cu)"),
    ]))
    return {"sub": "Àcids i bases, pH, neutralització, pluja àcida, velocitat de reacció i col·lisions, redox, corrosió i piles.",
            "dades": "Masses atòmiques (g/mol): H = 1 · C = 12 · O = 16 · Na = 23 · S = 32 · Cl = 35,5 · Ca = 40", "seccions": S}

# ======================================================================== SdA 5
def sda5():
    S = []
    S.append(("Vectors, posició i desplaçament", [
        (1, Q(1, "Mòdul.", "Calcula el mòdul dels vectors (3, 4), (6, 8), (−5, 12) i (1, 1)."), "5 · 10 · 13 · √2 ≈ 1,41"),
        (2, Q(2, "Desplaçament i distància.", "Camines 400 m cap a l'est i 300 m cap al nord. Quina distància recorres? Quin és el desplaçament (components i mòdul)?"), "700 m · (400, 300) m, 500 m"),
        (2, Q(2, "Suma de vectors.", "Suma els desplaçaments (2, 3) m, (4, −1) m i (−1, 2) m. Quin és el mòdul del resultat?"), f"(5, 4) m · {nf(41**0.5, 2)} m"),
        (2, Q(2, "La cèl·lula.", "Una cèl·lula passa de (12, 4) µm a (36, 14) µm en 2 h. Calcula el vector desplaçament, el seu mòdul i la velocitat mitjana."), "(24, 10) µm · 26 µm · 13 µm/h"),
    ]))
    S.append(("MRU i MRUA", [
        (1, Q(1, "Canvi d'unitats.", "Passa a m/s: 54 km/h · 90 km/h · 30 km/h. I 20 µm/h a µm/min."), f"15 · 25 · {nf(30/3.6, 2)} m/s · {nf(20/60, 2)} µm/min"),
        (2, Q(2, "El front de la ferida.", "Les vores d'una ferida de 500 µm avancen l'una cap a l'altra a 25 µm/h cadascuna. Quan es tancarà?"), "10 h"),
        (2, Q(2, "Trobada.", "Un cotxe surt de A a 90 km/h i, alhora, una moto surt de B, a 60 km de A, cap a A a 60 km/h. Quan i on es troben?"), "t = 0,4 h = 24 min, a 36 km de A"),
        (2, Q(2, "Persecució.", "Un cotxe passa per davant d'un radar a 108 km/h. 10 s després surt un cotxe de policia del radar a 144 km/h constants. Quan l'atrapa?"), "Als 30 s de sortir la policia (1 200 m del radar)"),
        (1, Q(1, "Accelera.", "Un cotxe passa de 0 a 100 km/h en 10 s. Calcula l'acceleració i la distància recorreguda."), f"{nf(100/3.6/10, 2)} m/s² · {nf(0.5*100/3.6*10, 0)} m"),
        (2, Q(2, "Equació sense temps.", "Una moto va a 72 km/h i frena amb a = −5 m/s². Quina distància recorre fins que s'atura?"), "40 m"),
        (2, Q(2, "Gràfiques.", "Un mòbil té aquesta velocitat: de 0 a 4 s passa de 0 a 12 m/s; de 4 a 10 s es manté a 12 m/s; de 10 a 14 s frena fins a aturar-se. a) Dibuixa la gràfica v–t. b) Calcula l'acceleració de cada tram. c) Calcula la distància total."), "b) 3 · 0 · −3 m/s² · c) 24 + 72 + 24 = 120 m"),
        (3, Q(3, "La distància d'aturada.", "Calcula la distància d'aturada a 50 km/h i a 30 km/h amb un temps de reacció d'1 s i a = −7 m/s². Repeteix-ho amb el terra mullat (a = −4 m/s²) a 50 km/h."), f"{nf(50/3.6+(50/3.6)**2/14, 1)} m · {nf(30/3.6+(30/3.6)**2/14, 1)} m · mullat: {nf(50/3.6+(50/3.6)**2/8, 1)} m"),
    ]))
    S.append(("Caiguda lliure", [
        (1, Q(1, "Des del balcó.", "Deixem caure una pedra des de 20 m. Quant triga a arribar a terra i amb quina velocitat? (g = 9,8 m/s²)"), f"{nf((2*20/9.8)**0.5, 2)} s · {nf((2*9.8*20)**0.5, 1)} m/s"),
        (2, Q(2, "Llançament vertical.", "Llancem una pilota cap amunt a 12 m/s. a) Quant triga a arribar a dalt? b) Quina altura màxima assoleix? c) Quant triga a tornar a la mà?"), f"a) {nf(12/9.8, 2)} s · b) {nf(144/19.6, 2)} m · c) {nf(24/9.8, 2)} s"),
        (2, Q(2, "El temps de reacció.", "El regle cau 15 cm abans que l'aturis. Quin és el teu temps de reacció? Si conduïssis a 50 km/h, quants metres faries abans de frenar?"), f"{nf((0.3/9.8)**0.5, 2)} s · {nf(50/3.6*(0.3/9.8)**0.5, 1)} m"),
    ]))
    S.append(("Forces i lleis de Newton", [
        (1, Q(1, "Resultant.", "Calcula la resultant: a) 40 N i 25 N en el mateix sentit · b) en sentits contraris · c) 6 N i 8 N perpendiculars."), "a) 65 N · b) 15 N · c) 10 N"),
        (2, Q(2, "Diagrama de forces.", "Dibuixa el diagrama de forces d'un llibre sobre una taula, d'un cotxe que accelera i d'una làmpada penjada del sostre."), "Llibre: P i N · cotxe: P, N, F motor i fregament · làmpada: P i T"),
        (2, Q(2, "Segona llei.", "Un cotxe de 1 200 kg accelera a 2 m/s² amb un fregament total de 600 N. Quina força fa el motor?"), "3 000 N"),
        (2, Q(2, "La frenada.", "Amb μ = 0,7 (asfalt sec), quina acceleració de frenada té un cotxe? I amb μ = 0,4 (mullat)? (a = μ · g)"), "−6,9 m/s² · −3,9 m/s²"),
        (2, Q(2, "Pla inclinat.", "Una caixa de 10 kg és en un pla inclinat de 30°. Calcula les components del pes paral·lela i perpendicular al pla, i la normal. (sin 30° = 0,5; cos 30° = 0,87)"), "Pₓ = 49 N · P_y = N ≈ 85 N"),
        (3, Q(3, "L'angle límit.", "Una sabatilla comença a lliscar en un pla inclinat a 35° (tan 35° = 0,70). Quin és el coeficient de fregament? Amb el terra mullat llisca a 20° (tan 20° = 0,36): què ha passat?"), "μ = 0,70 · μ baixa a 0,36: rellisca molt més"),
        (2, Q(2, "Acció i reacció.", "Una cèl·lula estira el gel amb una força de 5 nN cap enrere. Quina força fa el gel sobre la cèl·lula? Per què no s'anul·len?"), "5 nN cap endavant · actuen sobre cossos diferents"),
    ]))
    S.append(("Fregament, Hooke i equilibri", [
        (2, Q(2, "Velocitat límit.", "Explica per què una bola que cau en glicerina arriba a una velocitat constant. Dibuixa les forces quan ja té la velocitat límit."), "El fregament augmenta amb la velocitat fins que P = E + F: resultant zero i velocitat constant."),
        (1, Q(1, "Hooke.", "Una molla de k = 200 N/m s'allarga 5 cm. Quina força hi actua? Quant s'allargarà amb 30 N?"), "10 N · 15 cm"),
        (3, Q(3, "La força d'una cèl·lula.", "Un gel es comporta com una molla de k = 0,002 N/m. Una cèl·lula el deforma 2 µm. Quina força fa la cèl·lula, en nN?"), "4 · 10⁻⁹ N = 4 nN"),
        (2, Q(2, "El semàfor.", "Un semàfor de 15 kg penja d'un sol cable. Quina tensió suporta el cable? I si penja de dos cables verticals?"), "147 N · 73,5 N cada un"),
    ]))
    return {"sub": "Vectors, MRU i MRUA, distància d'aturada, caiguda lliure, forces i lleis de Newton, fregament, Hooke i equilibri.", "seccions": S}

# ======================================================================== SdA 6
def sda6():
    S = []
    S.append(("La pressió", [
        (1, Q(1, "Calcula la pressió.", "a) Una força de 500 N sobre 0,25 m² · b) una persona de 600 N sobre dues sabates de 200 cm² cadascuna · c) la mateixa persona sobre unes raquetes de 0,25 m² en total."), "a) 2 000 Pa · b) 15 000 Pa · c) 2 400 Pa"),
        (1, Q(1, "Augmentar o reduir?", "Explica per què: a) un ganivet esmolat talla millor · b) les excavadores tenen erugues · c) les xinxetes tenen punta · d) els camions pesants tenen moltes rodes."), "a, c) menys superfície: més pressió · b, d) més superfície: menys pressió"),
        (2, Q(2, "Unitats.", "Passa: a) 2,5 atm a Pa · b) 1 520 mmHg a atm · c) 3 bar a Pa · d) 950 hPa a atm."), f"a) {nf(2.5*101325, 0)} Pa · b) 2 atm · c) 300 000 Pa · d) {nf(95000/101325, 3)} atm"),
        (2, Q(2, "El taló.", "Una persona de 60 kg recolza tot el pes sobre un taló d'1 cm². Quina pressió fa? Compara-ho amb un elefant de 4 000 kg sobre quatre potes de 0,1 m² cadascuna."), f"{nf(60*9.8/1e-4, 0)} Pa · elefant: {nf(4000*9.8/0.4, 0)} Pa: el taló fa més pressió"),
        (2, Q(2, "La pressió a la superfície.", "Calcula la força total que fa l'atmosfera sobre la superfície d'una taula d'1,2 m × 0,8 m. Per què no s'enfonsa?"), f"{nf(101325*0.96, 0)} N · la pressió de l'aire també empeny des de sota"),
    ]))
    S.append(("Pressió hidrostàtica", [
        (1, Q(1, "A la piscina.", "Quina pressió hidrostàtica hi ha al fons d'una piscina de 2 m (ρ = 1 000 kg/m³)? I la pressió total?"), f"{nf(1000*9.8*2, 0)} Pa · {nf(101325+19600, 0)} Pa"),
        (2, Q(2, "El submarinista.", "A quina profunditat de l'aigua de mar (1 030 kg/m³) la pressió hidrostàtica és d'1 atm? I la pressió total de 3 atm?"), f"{nf(101325/(1030*9.8), 1)} m · {nf(2*101325/(1030*9.8), 1)} m"),
        (2, Q(2, "La finestreta.", "L'Ictineo baixa a 30 m (aigua de mar). Quina força fa l'aigua sobre una finestreta de 20 cm de diàmetre (només la pressió hidrostàtica)?"), f"{nf(1030*9.8*30, 0)} Pa · {nf(1030*9.8*30*3.1416*0.1**2, 0)} N"),
        (2, Q(2, "Vertader o fals?", "Justifica:", "La pressió al fons depèn de la forma del recipient.", "A la mateixa profunditat, la pressió és igual en totes direccions.", "En aigua salada, a la mateixa profunditat, la pressió és més gran.", "La pressió depèn de la quantitat total d'aigua."), "a) F · b) V · c) V · d) F (només de la profunditat i la densitat)"),
        (3, Q(3, "El manòmetre.", "En un manòmetre de tub en U amb aigua, la diferència d'altura és de 12 cm. Quina diferència de pressió marca? Si posem la càpsula més avall, què passa amb la diferència d'altura?"), f"{nf(1000*9.8*0.12, 0)} Pa · augmenta"),
    ]))
    S.append(("Pascal i la pressió atmosfèrica", [
        (1, Q(1, "La premsa.", "Una premsa hidràulica té èmbols de 10 cm² i 500 cm². Quina força cal fer al petit per aixecar un pes de 10 000 N?"), "200 N"),
        (2, Q(2, "El gat del taller.", "Fem una força de 150 N sobre un èmbol de 3 cm². Quina massa podem aixecar amb un èmbol de 300 cm²?"), f"15 000 N → {nf(15000/9.8, 0)} kg"),
        (2, Q(2, "Els frens.", "Explica com funciona el sistema de frens d'un cotxe amb el principi de Pascal."), "El pedal empeny un líquid; la pressió es transmet igual fins a les quatre rodes i hi fa una força gran sobre les pastilles."),
        (2, Q(2, "Torricelli.", "Per què el mercuri es queda a 760 mm i no baixa del tot? Què passaria a dalt d'una muntanya? Per què Torricelli no ho va fer amb aigua?"), "L'aire empeny el mercuri de la cubeta. A dalt d'una muntanya la columna seria més baixa. Amb aigua caldria un tub de més de 10 m."),
        (2, Q(2, "La llauna aixafada.", "Bullim una mica d'aigua en una llauna, la tapem i la refredem: s'aixafa. Explica-ho."), "El vapor condensa i la pressió de dins baixa molt; la pressió atmosfèrica l'aixafa."),
    ]))
    S.append(("L'empenta i el principi d'Arquimedes", [
        (1, Q(1, "L'empenta.", "Quina empenta rep un cos de 2 L totalment submergit en aigua? I en aigua de mar (1 030 kg/m³)?"), f"{nf(1000*0.002*9.8, 1)} N · {nf(1030*0.002*9.8, 1)} N"),
        (2, Q(2, "Pes aparent.", "Una pedra pesa 12 N a l'aire i 8 N dins l'aigua. a) Quina empenta rep? b) Quin volum té? c) Quina densitat té?"), f"a) 4 N · b) {nf(4/9800*1e6, 0)} cm³ · c) 3 000 kg/m³"),
        (2, Q(2, "D'on surt l'empenta?", "Explica, amb la pressió hidrostàtica, per què un cos submergit rep una força cap amunt."), "La pressió és més gran a la cara de baix (més profunda) que a la de dalt; la diferència de forces és cap amunt."),
        (3, Q(3, "Corona d'or?", "Una corona pesa 9,8 N a l'aire i 9,25 N dins l'aigua. Calcula'n la densitat. És d'or (19 300 kg/m³)?"), f"E = 0,55 N; ρ = (P / E) · ρ(aigua) ≈ 17 800 kg/m³: no és d'or pur"),
    ]))
    S.append(("Flotació i submarins", [
        (1, Q(1, "Sura o s'enfonsa?", "Compara les densitats: fusta (600 kg/m³), gel (920 kg/m³), alumini (2 700 kg/m³), oli (920 kg/m³) en aigua. Què fa cada un?"), "Suren: fusta, gel, oli · s'enfonsa: alumini"),
        (2, Q(2, "Quina part submergida?", "Un tros de fusta de 600 kg/m³ sura a l'aigua. Quin percentatge del seu volum queda submergit? I un iceberg (920 kg/m³) a l'aigua de mar (1 030 kg/m³)?"), f"60 % · {nf(920/1030*100, 0)} %"),
        (2, Q(2, "El ludió.", "Explica per què el ludió baixa quan premem l'ampolla i puja quan la deixem anar."), "En prémer, l'aire del ludió es comprimeix, hi entra aigua i la densitat mitjana augmenta; en deixar anar, l'aire s'expandeix i surt aigua."),
        (2, Q(2, "Els tancs de llast.", "Un submarí de 2 000 m³ té una massa de 1 950 t. a) Quina és la seva densitat mitjana? Sura a l'aigua de mar? b) Quanta aigua ha d'entrar als tancs perquè quedi en equilibri submergit?"), f"a) 975 kg/m³: sura · b) {nf(2000*1.03-1950, 0)} t d'aigua"),
        (3, Q(3, "El submarí d'ampolla.", "Dissenya un submarí d'ampolla que baixi, s'aturi i torni a pujar. Explica com controlaries la densitat mitjana i quines forces hi actuen a cada moment."), "Resposta oberta: llast fix + recipient on entra aigua o aire (xeringa i tub); baixa si P &gt; E, equilibri si P = E, puja si P &lt; E."),
        (2, Q(2, "El motor de Monturiol.", "Per què l'Ictineo II necessitava un motor que funcionés sense aire? Quin gas desprenia la reacció del clorat de potassi i per a què servia?"), "Sota l'aigua no hi ha aire per cremar combustible. Desprenia oxigen, que també podia respirar la tripulació."),
    ]))
    return {"sub": "La pressió, la pressió hidrostàtica, el principi de Pascal, la pressió atmosfèrica, l'empenta i la flotació.",
            "dades": "g = 9,8 m/s² · ρ(aigua) = 1 000 kg/m³ · ρ(aigua de mar) = 1 030 kg/m³ · 1 atm = 101 325 Pa = 760 mmHg", "seccions": S}

FUNCS = {1: sda1, 2: sda2, 3: sda3, 4: sda4, 5: sda5, 6: sda6}
