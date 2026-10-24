"""Píndoles d'informació del llibre imprès: una pàgina per idea clau, abans de la fitxa on es fa servir.
Cada píndola: (sda, clau_del_full_davant_del_qual_va, títol, html). Els exemples fan servir dades diferents de les fitxes."""

P = []


def add(n, before, title, html):
    P.append({"n": n, "before": before, "title": title, "html": html})


def idea(t):
    return f'<div class="pi-idea">{t}</div>'


def ex(t, body):
    return f'<div class="pi-ex"><div class="pi-lab">Exemple resolt · {t}</div>{body}</div>'


def compte(t):
    return f'<div class="pi-warn"><b>Compte!</b> {t}</div>'


def resum(items):
    return '<div class="pi-sum"><div class="pi-lab">En resum</div><ul>' + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>"


# ------------------------------------------------------------------ SdA 1
add(1, "d1f1", "Magnituds, unitats i notació científica", (
    idea("Una <b>magnitud</b> és una propietat que es pot mesurar (massa, longitud, temps, temperatura…). Una mesura sempre té <b>un número i una unitat</b>: «5» no vol dir res; «5 g» sí.")
    + "<h3>Les unitats del Sistema Internacional (SI)</h3>"
    + "<table><tr><th>Magnitud</th><th>Unitat SI</th><th>Símbol</th><th>Altres unitats habituals</th></tr>"
      "<tr><td>Longitud</td><td>metre</td><td>m</td><td>km, cm, mm, µm</td></tr>"
      "<tr><td>Massa</td><td>quilogram</td><td>kg</td><td>g, mg, t</td></tr>"
      "<tr><td>Temps</td><td>segon</td><td>s</td><td>min, h</td></tr>"
      "<tr><td>Temperatura</td><td>kelvin</td><td>K</td><td>°C</td></tr>"
      "<tr><td>Volum (derivada)</td><td>metre cúbic</td><td>m³</td><td>L, mL, cm³ (1 mL = 1 cm³)</td></tr></table>"
    + "<h3>Els prefixos són potències de 10</h3>"
    + "<table><tr><th>giga (G)</th><th>mega (M)</th><th>quilo (k)</th><th>—</th><th>centi (c)</th><th>mil·li (m)</th><th>micro (µ)</th><th>nano (n)</th></tr>"
      "<tr><td>10⁹</td><td>10⁶</td><td>10³</td><td>1</td><td>10⁻²</td><td>10⁻³</td><td>10⁻⁶</td><td>10⁻⁹</td></tr></table>"
    + "<h3>Notació científica</h3><p>Un número en notació científica s'escriu com <b>a × 10ⁿ</b>, amb 1 ≤ a &lt; 10. Serveix per escriure números molt grans o molt petits sense omplir la pàgina de zeros.</p>"
    + ex("passar a notació científica", "<p>Distància de la Terra a la Lluna: 384 000 000 m → movem la coma 8 llocs a l'esquerra → <b>3,84 × 10⁸ m</b>.<br>Diàmetre d'un cabell: 0,00007 m → movem la coma 5 llocs a la dreta → <b>7 × 10⁻⁵ m</b>.</p>")
    + compte("si la coma es mou cap a l'esquerra, l'exponent és positiu (número gran); si es mou cap a la dreta, és negatiu (número petit).")
    + resum(["Sempre número + unitat.", "Prefix = potència de 10 (k = 10³, m = 10⁻³, µ = 10⁻⁶).", "Notació científica: a × 10ⁿ, amb 1 ≤ a &lt; 10."])))

add(1, "d1f2", "Factors de conversió, pas a pas", (
    idea("Un <b>factor de conversió</b> és una fracció que <b>val 1</b> perquè el numerador i el denominador són la mateixa quantitat escrita amb unitats diferents. Multiplicar per 1 no canvia la mesura: només en canvia la unitat.")
    + "<p>Per exemple, com que 1 km = 1000 m, aquestes dues fraccions valen 1:</p>"
    + "<p class='formula'>\\( \\dfrac{1000\\ \\text{m}}{1\\ \\text{km}} \\) &nbsp;&nbsp;i&nbsp;&nbsp; \\( \\dfrac{1\\ \\text{km}}{1000\\ \\text{m}} \\)</p>"
    + "<h3>El mètode en tres passos</h3><ol><li>Escriu la dada amb la seva unitat.</li><li>Multiplica per un factor que tingui <b>a baix</b> la unitat que vols eliminar i <b>a dalt</b> la que vols obtenir.</li><li>Simplifica les unitats (es cancel·len com en una fracció) i fes el càlcul.</li></ol>"
    + ex("una velocitat de km/h a m/s", "<p class='formula'>\\( 90\\ \\dfrac{\\text{km}}{\\text{h}} \\cdot \\dfrac{1000\\ \\text{m}}{1\\ \\text{km}} \\cdot \\dfrac{1\\ \\text{h}}{3600\\ \\text{s}} = 25\\ \\dfrac{\\text{m}}{\\text{s}} \\)</p><p>Els km es cancel·len amb els km, i les h amb les h. Queden m/s.</p>")
    + ex("una densitat de g/cm³ a kg/m³", "<p class='formula'>\\( 0{,}92\\ \\dfrac{\\text{g}}{\\text{cm}^3} \\cdot \\dfrac{1\\ \\text{kg}}{1000\\ \\text{g}} \\cdot \\dfrac{10^6\\ \\text{cm}^3}{1\\ \\text{m}^3} = 920\\ \\dfrac{\\text{kg}}{\\text{m}^3} \\)</p><p>Recorda que 1 m³ = (100 cm)³ = 10⁶ cm³.</p>")
    + compte("si la unitat que vols eliminar no queda a l'altra banda de la fracció, no es cancel·la. Gira el factor.")
    + resum(["Un factor de conversió val 1.", "La unitat que vull treure, a baix; la que vull obtenir, a dalt.", "Es poden encadenar tants factors com calgui."])))

add(1, "d1dens", "La densitat: una propietat característica", (
    idea("La <b>densitat</b> és la massa que hi ha en cada unitat de volum. És una <b>propietat característica</b>: no depèn de quanta substància tinguem, i per això serveix per identificar substàncies.")
    + "<p class='formula'>\\( \\rho = \\dfrac{m}{V} \\)</p><p>Unitats habituals: g/mL = g/cm³ = kg/L. En el SI: kg/m³ (1 g/cm³ = 1000 kg/m³).</p>"
    + "<table><tr><th>Substància (20 °C)</th><th>Densitat (g/cm³)</th></tr><tr><td>Aigua</td><td>1,00</td></tr><tr><td>Etanol</td><td>0,79</td></tr><tr><td>Oli d'oliva</td><td>≈ 0,91</td></tr><tr><td>Alumini</td><td>2,70</td></tr><tr><td>Ferro</td><td>7,87</td></tr></table>"
    + ex("identificar un líquid", "<p>Un líquid de 50,0 mL té una massa de 39,6 g. \\( \\rho = 39{,}6\\ \\text{g} / 50{,}0\\ \\text{mL} = 0{,}792\\ \\text{g/mL} \\): probablement és etanol.</p>")
    + "<h3>Quina qualitat té la mesura?</h3><p><b>Error absolut</b> = |valor mesurat − valor de referència|. <b>Error relatiu</b> = error absolut / valor de referència × 100. A l'exemple: |0,792 − 0,79| = 0,002 g/mL i 0,002 / 0,79 × 100 ≈ 0,3 %: una mesura molt bona.</p>"
    + compte("la massa i el volum no són propietats característiques: dues mostres d'aigua poden tenir masses diferents, però totes dues tenen la mateixa densitat.")
    + resum(["ρ = m / V.", "Els objectes menys densos que un líquid hi suren.", "L'error relatiu diu si una mesura és bona."])))

add(1, "d1sep", "Substàncies pures, mescles i com separar-les", (
    idea("Una <b>substància pura</b> té una composició fixa i propietats característiques fixes (l'aigua destil·lada, la sal, el ferro). Una <b>mescla</b> té diverses substàncies que conserven les seves propietats, i per això es poden separar per mètodes físics.")
    + "<ul><li><b>Mescla heterogènia:</b> es veuen les parts (sorra i aigua, oli i aigua).</li><li><b>Mescla homogènia o dissolució:</b> no es distingeixen les parts (aigua salada, aire).</li></ul>"
    + "<h3>Cada tècnica aprofita una propietat</h3>"
    + "<table><tr><th>Tècnica</th><th>Propietat que aprofita</th><th>Exemple</th></tr>"
      "<tr><td>Separació magnètica</td><td>Només alguns metalls són atrets per un imant</td><td>Llimadures de ferro i sorra</td></tr>"
      "<tr><td>Flotació</td><td>Densitat (menys densa que l'aigua, sura)</td><td>Serradures i sorra</td></tr>"
      "<tr><td>Filtració</td><td>Mida de les partícules (un sòlid no dissolt no passa pel filtre)</td><td>Sorra i aigua</td></tr>"
      "<tr><td>Decantació</td><td>Líquids no miscibles amb densitats diferents</td><td>Oli i aigua</td></tr>"
      "<tr><td>Evaporació i cristal·lització</td><td>Temperatura d'ebullició (el dissolvent s'evapora, el sòlid queda)</td><td>Sal i aigua</td></tr>"
      "<tr><td>Cromatografia</td><td>Cada component avança a una velocitat diferent pel paper</td><td>Tintes d'un retolador</td></tr></table>"
    + ex("dissenyar una separació", "<p>Mescla: sal, sorra i aigua. 1) <b>Filtrem</b>: la sorra queda al filtre. 2) <b>Evaporem</b> el líquid filtrat: la sal queda a la càpsula.</p>")
    + compte("dissoldre no és fondre. Quan la sal es dissol, no desapareix: les seves partícules es barregen amb les de l'aigua.")
    + resum(["Pures: composició fixa. Mescles: es poden separar per mètodes físics.", "Cada tècnica de separació es basa en una propietat.", "L'ordre dels passos importa."])))

# ------------------------------------------------------------------ SdA 2
add(2, "f1", "El model cineticomolecular", (
    idea("Per explicar com es comporten sòlids, líquids i gasos imaginem que la matèria està feta de <b>partícules molt petites</b> que es mouen. És un <b>model</b>: no les veiem, però explica el que observem.")
    + "<h3>Els postulats del model</h3><ol><li>La matèria està formada per partícules i entre elles hi ha <b>buit</b>.</li><li>Les partícules estan en <b>moviment continu</b>.</li><li>Com més alta és la temperatura, <b>més ràpid</b> es mouen (més energia cinètica).</li><li>Entre les partícules hi ha <b>forces d'atracció</b>, més fortes com més a prop són.</li></ol>"
    + "<table><tr><th></th><th>Sòlid</th><th>Líquid</th><th>Gas</th></tr><tr><td>Partícules</td><td>Molt juntes i ordenades; vibren</td><td>Juntes però desordenades; llisquen</td><td>Molt separades; es mouen en totes direccions</td></tr><tr><td>Forma i volum</td><td>Forma i volum fixos</td><td>Volum fix, forma del recipient</td><td>Ocupen tot el recipient</td></tr><tr><td>Compressible?</td><td>No</td><td>Gairebé no</td><td>Sí</td></tr></table>"
    + "<h3>Què és la pressió d'un gas?</h3><p>Les partícules del gas <b>xoquen contra les parets</b> del recipient. La pressió és l'efecte de tots aquests xocs. Si escalfem el gas, les partícules van més de pressa i xoquen més sovint i més fort: la pressió augmenta.</p>"
    + compte("les partícules no s'escalfen, no es dilaten ni es fonen. El que canvia és com es mouen i com de separades estan.")
    + resum(["Partícules + buit + moviment continu.", "Més temperatura → més velocitat.", "Pressió = xocs de les partícules contra les parets."])))

add(2, "f2", "Les lleis dels gasos i l'escala Kelvin", (
    idea("Quan un gas està tancat, la seva <b>pressió (p)</b>, el seu <b>volum (V)</b> i la seva <b>temperatura (T)</b> estan relacionats. Si en mantenim una de constant, les altres dues canvien de manera previsible.")
    + "<h3>L'escala Kelvin</h3><p class='formula'>T (K) = t (°C) + 273</p><p>A 0 K (−273 °C), el zero absolut, les partícules tindrien el mínim moviment possible. A les lleis dels gasos <b>sempre</b> s'utilitza la temperatura en kelvin.</p>"
    + "<table><tr><th>Llei</th><th>Què es manté constant</th><th>Relació</th><th>Expressió</th></tr>"
      "<tr><td>Boyle-Mariotte</td><td>Temperatura</td><td>Si V augmenta, p disminueix (inversa)</td><td>p₁·V₁ = p₂·V₂</td></tr>"
      "<tr><td>Charles</td><td>Pressió</td><td>Si T augmenta, V augmenta (directa)</td><td>V₁/T₁ = V₂/T₂</td></tr>"
      "<tr><td>Gay-Lussac</td><td>Volum</td><td>Si T augmenta, p augmenta (directa)</td><td>p₁/T₁ = p₂/T₂</td></tr></table>"
    + ex("una pilota al sol (Gay-Lussac)", "<p>Una pilota tancada té una pressió d'1,5 atm a 17 °C. Quina pressió tindrà a 47 °C si el volum no canvia?</p><p>T₁ = 17 + 273 = 290 K; T₂ = 47 + 273 = 320 K. &nbsp; p₂ = p₁ · T₂ / T₁ = 1,5 · 320 / 290 ≈ <b>1,66 atm</b>.</p>")
    + compte("si poses la temperatura en °C, el resultat surt malament (fins i tot pots dividir per zero!).")
    + resum(["T(K) = t(°C) + 273.", "Boyle: p·V constant. Charles: V/T constant. Gay-Lussac: p/T constant.", "Explica-ho sempre també amb les partícules."])))

add(2, "labc", "Els canvis d'estat i la corba d'escalfament", (
    idea("Quan escalfem una substància pura, la temperatura puja fins que arriba a un canvi d'estat. Mentre dura el canvi d'estat, <b>la temperatura es manté constant</b>: l'energia que rep serveix per separar les partícules, no per fer-les anar més ràpid.")
    + "<table><tr><th>Canvi</th><th>D'on a on</th><th>Energia</th></tr><tr><td>Fusió / solidificació</td><td>sòlid ↔ líquid</td><td>absorbeix / desprèn</td></tr><tr><td>Vaporització / condensació</td><td>líquid ↔ gas</td><td>absorbeix / desprèn</td></tr><tr><td>Sublimació / sublimació inversa</td><td>sòlid ↔ gas</td><td>absorbeix / desprèn</td></tr></table>"
    + "<p><b>Evaporació</b>: només a la superfície i a qualsevol temperatura. <b>Ebullició</b>: a tot el líquid i a una temperatura concreta (la temperatura d'ebullició), que depèn de la pressió.</p>"
    + "<h3>Com es llegeix una corba d'escalfament</h3><p>Els <b>trams inclinats</b> són una sola fase que s'escalfa. Els <b>trams horitzontals</b> són canvis d'estat: la seva temperatura és la de fusió o la d'ebullició, que són propietats característiques.</p>"
    + ex("l'aigua a la muntanya", "<p>A 3000 m d'altitud la pressió de l'aire és menor i l'aigua bull a uns 90 °C. Per això la pasta triga més a coure's: l'aigua no pot passar de 90 °C mentre bull.</p>")
    + compte("durant l'ebullició no s'ha de seguir escalfant «perquè pugi la temperatura»: no pujarà fins que tota l'aigua s'hagi evaporat.")
    + resum(["Trams plans = canvis d'estat.", "La temperatura d'ebullició depèn de la pressió.", "Evaporació ≠ ebullició."])))

# ------------------------------------------------------------------ SdA 3
add(3, "d3f2", "Els models atòmics: de Dalton a Bohr", (
    idea("Ningú no ha vist un àtom a ull nu. Els científics han proposat <b>models</b> i els han canviat cada vegada que un experiment no hi encaixava. La ciència avança així.")
    + "<table><tr><th>Model</th><th>Com és l'àtom</th><th>Per què va canviar</th></tr>"
      "<tr><td><b>Dalton</b> (1808)</td><td>Esfera massissa i indivisible; cada element té àtoms iguals</td><td>Es van descobrir els electrons (Thomson, 1897)</td></tr>"
      "<tr><td><b>Thomson</b> (1904)</td><td>Esfera amb càrrega positiva amb electrons incrustats</td><td>L'experiment de Rutherford: algunes partícules alfa reboten</td></tr>"
      "<tr><td><b>Rutherford</b> (1911)</td><td>Nucli petit i positiu on hi ha gairebé tota la massa; electrons al voltant; gairebé tot és buit</td><td>No explicava per què els electrons no cauen al nucli ni els espectres</td></tr>"
      "<tr><td><b>Bohr</b> (1913)</td><td>Electrons en òrbites (capes) amb energies fixes</td><td>Explica els espectres; avui es fa servir un model encara més complex</td></tr></table>"
    + "<h3>L'experiment de Rutherford</h3><p>Va llançar partícules alfa (positives) contra una làmina d'or molt prima. Gairebé totes la travessaven sense desviar-se (l'àtom és gairebé buit), però unes poques rebotaven: havien xocat amb un <b>nucli</b> petit, dens i positiu.</p>"
    + ex("l'escala de l'àtom", "<p>El nucli és unes 100 000 vegades més petit que l'àtom. Si el nucli fos una bala de 2 mm, l'àtom faria uns 200 m de diàmetre: gairebé tot buit.</p>")
    + compte("un model no és «fals» perquè n'hi hagi un de millor: explica bé uns fenòmens i no uns altres.")
    + resum(["Els models canvien amb les proves experimentals.", "Rutherford: nucli petit i positiu.", "Bohr: electrons en capes."])))

add(3, "d3f3", "Protons, neutrons, electrons, isòtops i ions", (
    idea("Un àtom té un <b>nucli</b> amb <b>protons (+)</b> i <b>neutrons (sense càrrega)</b>, i <b>electrons (−)</b> al voltant. Un àtom neutre té tants electrons com protons.")
    + "<table><tr><th>Símbol</th><th>Significat</th></tr><tr><td><b>Z</b> (nombre atòmic)</td><td>Nombre de protons. Identifica l'element.</td></tr><tr><td><b>A</b> (nombre màssic)</td><td>Protons + neutrons.</td></tr><tr><td>Neutrons</td><td>A − Z</td></tr></table>"
    + "<p><b>Isòtops:</b> àtoms del mateix element (mateix Z) amb diferent nombre de neutrons (diferent A). Per exemple, el carboni-12 i el carboni-14.</p>"
    + "<p><b>Ions:</b> àtoms que han guanyat o perdut electrons. Si en perden, queden positius (<b>cations</b>, per exemple Na⁺). Si en guanyen, queden negatius (<b>anions</b>, per exemple Cl⁻). Els protons no canvien mai.</p>"
    + ex("el magnesi", "<p>²⁴Mg (Z = 12): 12 protons, 24 − 12 = 12 neutrons, 12 electrons. L'ió Mg²⁺ ha perdut 2 electrons: 12 protons, 12 neutrons i <b>10 electrons</b>.</p>")
    + "<h3>Capes d'electrons (model de Bohr)</h3><p>La 1a capa admet fins a 2 electrons i la 2a i la 3a, fins a 8 als elements dels tres primers períodes. Exemple: Na (Z = 11) → 2, 8, 1.</p>"
    + compte("un ió positiu té <b>menys</b> electrons, no més protons.")
    + resum(["Z = protons; A = protons + neutrons.", "Isòtops: mateix Z, diferent A.", "Ions: es guanyen o es perden electrons."])))

add(3, "d3f4", "La taula periòdica", (
    idea("La taula periòdica ordena els elements per <b>nombre atòmic (Z)</b> creixent. Els elements d'una mateixa <b>columna (grup)</b> tenen el mateix nombre d'electrons a l'última capa i, per això, propietats químiques semblants.")
    + "<ul><li><b>Períodes</b> (files): el número del període indica quantes capes d'electrons té l'àtom.</li><li><b>Grups</b> (columnes): 18 grups. Alguns tenen nom propi: metalls alcalins (grup 1), alcalinoterris (2), halògens (17) i gasos nobles (18).</li><li><b>Metalls</b> (a l'esquerra i al centre): brillants, bons conductors, tendeixen a perdre electrons. <b>No-metalls</b> (a la dreta): mals conductors, tendeixen a guanyar electrons.</li></ul>"
    + "<h3>Mendeléiev, el 1869</h3><p>Va ordenar els 63 elements coneguts i va deixar <b>forats</b> per a elements que encara no s'havien descobert, i en va predir les propietats. Quan es van descobrir el gal·li i el germani, les prediccions van encaixar.</p>"
    + ex("predir propietats", "<p>El potassi (K) és al grup 1, com el liti i el sodi: és un metall tou que reacciona amb l'aigua de manera violenta i forma l'ió K⁺.</p>")
    + compte("els elements del mateix <b>període</b> no s'assemblen entre ells; els del mateix <b>grup</b>, sí.")
    + resum(["Ordre per Z.", "Mateix grup → propietats semblants.", "Metalls a l'esquerra, no-metalls a la dreta, gasos nobles a la columna 18."])))

add(3, "d3f5", "L'enllaç químic", (
    idea("Els àtoms s'uneixen perquè així queden més estables, sovint amb 8 electrons a l'última capa, com els gasos nobles. Segons quins àtoms s'uneixen, l'enllaç és d'un tipus o d'un altre.")
    + "<table><tr><th>Enllaç</th><th>Entre…</th><th>Què passa amb els electrons</th><th>Propietats</th><th>Exemple del mòbil</th></tr>"
      "<tr><td><b>Iònic</b></td><td>metall + no-metall</td><td>El metall en cedeix i el no-metall en capta: es formen ions que s'atrauen</td><td>Sòlids durs; condueixen fosos o dissolts</td><td>LiF, sals de l'electròlit</td></tr>"
      "<tr><td><b>Covalent</b></td><td>no-metall + no-metall</td><td>Es comparteixen parells d'electrons</td><td>Molècules; sovint gasos o líquids; no condueixen</td><td>Plàstics de la carcassa</td></tr>"
      "<tr><td><b>Metàl·lic</b></td><td>metall + metall</td><td>Els electrons es mouen lliurement entre els ions</td><td>Condueixen el corrent i la calor; es deformen sense trencar-se</td><td>Coure dels cables</td></tr></table>"
    + ex("el fluorur de liti, LiF", "<p>Li (2, 1) perd 1 electró → Li⁺. F (2, 7) en guanya 1 → F⁻. Els ions de càrrega oposada s'atrauen i formen un cristall.</p>")
    + compte("al cristall de sal no hi ha «molècules de NaCl»: hi ha milions d'ions Na⁺ i Cl⁻ ordenats.")
    + resum(["Iònic: transferència d'electrons.", "Covalent: compartició.", "Metàl·lic: electrons lliures → bons conductors."])))

# ------------------------------------------------------------------ SdA 4
add(4, "d4lab1", "La reacció química i la conservació de la massa", (
    idea("En una <b>reacció química</b> unes substàncies (<b>reactius</b>) es transformen en unes altres de diferents (<b>productes</b>). Els àtoms no es creen ni es destrueixen: es <b>reorganitzen</b>.")
    + "<h3>Com sabem que hi ha hagut una reacció?</h3><ul><li>Canvi de color, aparició d'un gas (bombolles), formació d'un sòlid (precipitat).</li><li>Es desprèn o s'absorbeix energia: la temperatura puja (<b>exotèrmica</b>) o baixa (<b>endotèrmica</b>).</li></ul>"
    + "<h3>Llei de Lavoisier</h3><p class='formula'>massa dels reactius = massa dels productes</p><p>En un <b>sistema tancat</b>, la massa total no canvia. En un <b>sistema obert</b> pot semblar que canvia perquè un gas surt (o entra) del recipient.</p>"
    + ex("quanta massa ha marxat?", "<p>Posem 2,0 g d'una pastilla efervescent en un got amb aigua: el total pesa 152,0 g. Quan s'acaben les bombolles, pesa 151,4 g. Han sortit 0,6 g de diòxid de carboni, que és un producte gasós.</p>")
    + compte("la massa no «desapareix». Si la balança marca menys, busca el gas que ha sortit.")
    + resum(["Reactius → productes.", "Els àtoms es conserven: la massa també.", "Sistema obert ≠ sistema tancat."])))

add(4, "d4f1", "Formulació i nomenclatura de compostos binaris", (
    idea("Una <b>fórmula</b> diu quins elements té un compost i en quina proporció. La IUPAC fixa les regles perquè tothom l'escrigui i l'anomeni igual.")
    + "<h3>Compostos iònics: metall + no-metall</h3><ol><li>Escriu els ions: per exemple Al³⁺ i O²⁻.</li><li>Busca la combinació amb <b>càrrega total zero</b>: 2 · (+3) + 3 · (−2) = 0.</li><li>Fórmula: <b>Al₂O₃</b>. Nom: òxid d'alumini.</li></ol>"
    + "<p>Si el metall pot tenir més d'una càrrega, s'indica amb números romans (<b>notació de Stock</b>): FeCl₃ és el clorur de ferro(III).</p>"
    + "<h3>Compostos de dos no-metalls: prefixos</h3><p>mono (1), di (2), tri (3), tetra (4), penta (5)… CO₂ és el <b>diòxid de carboni</b>; CO, el <b>monòxid de carboni</b>; N₂O₄, el <b>tetraòxid de dinitrogen</b>.</p>"
    + "<p>Noms acceptats: H₂O (aigua), NH₃ (amoníac), CH₄ (metà).</p>"
    + ex("el nom a partir de la fórmula", "<p>CaCl₂: calci (Ca²⁺) i clor (Cl⁻) → <b>clorur de calci</b>. Comprovació: +2 + 2 · (−1) = 0.</p>")
    + compte("no confonguis la càrrega de l'ió amb el subíndex: a Fe₂O₃ cada ferro és Fe³⁺, i per això es diu òxid de ferro(III).")
    + resum(["Iònics: càrrega total zero.", "Stock: càrrega del metall en números romans si en pot tenir més d'una.", "No-metalls: prefixos."])))

add(4, "d4f2", "Equacions químiques: ajust i càlculs de massa", (
    idea("Una <b>equació química</b> representa una reacció. Ha d'estar <b>ajustada</b>: hi ha d'haver el mateix nombre d'àtoms de cada element a cada costat.")
    + "<h3>Com s'ajusta</h3><ol><li>Escriu les fórmules correctes de reactius i productes.</li><li>Compta els àtoms de cada element a cada costat.</li><li>Canvia només els <b>coeficients</b> (els números de davant), mai els subíndexs.</li></ol>"
    + ex("la combustió de l'hidrogen", "<p>H₂ + O₂ → H₂O no està ajustada (2 O a l'esquerra, 1 a la dreta).<br><b>2 H₂ + O₂ → 2 H₂O</b>: 4 H i 2 O a cada costat.</p>")
    + "<h3>Llei de Proust: proporcions definides</h3><p>Els elements es combinen sempre en la mateixa proporció de massa. Amb les masses atòmiques (H = 1 u, O = 16 u): 2 H₂ (4 u) + O₂ (32 u) → 2 H₂O (36 u). Per tant, <b>4 g d'hidrogen reaccionen amb 32 g d'oxigen i formen 36 g d'aigua</b>: proporció 1 : 8 : 9.</p>"
    + ex("càlcul de massa", "<p>Quanta aigua es forma amb 10 g d'hidrogen? 10 g · (36 g / 4 g) = <b>90 g d'aigua</b>.</p>")
    + compte("si canvies un subíndex, canvies la substància: H₂O₂ no és aigua, és aigua oxigenada.")
    + resum(["Només es canvien els coeficients.", "Massa dels reactius = massa dels productes.", "Les proporcions de massa surten de l'equació ajustada."])))

add(4, "d4f3", "De què depèn la velocitat d'una reacció?", (
    idea("Perquè dues partícules reaccionin han de <b>xocar</b> amb prou energia i ben orientades (<b>teoria de col·lisions</b>). Tot el que faci augmentar els xocs eficaços fa la reacció més ràpida.")
    + "<table><tr><th>Factor</th><th>Què passa</th><th>Per què (partícules)</th></tr>"
      "<tr><td>Temperatura ↑</td><td>Més ràpida</td><td>Les partícules es mouen més de pressa: més xocs i amb més energia</td></tr>"
      "<tr><td>Concentració ↑</td><td>Més ràpida</td><td>Hi ha més partícules en el mateix volum: més xocs</td></tr>"
      "<tr><td>Superfície de contacte ↑</td><td>Més ràpida</td><td>Un sòlid trossejat té més partícules exposades</td></tr>"
      "<tr><td>Catalitzador</td><td>Més ràpida</td><td>Facilita la reacció i no es gasta</td></tr></table>"
    + ex("a la cuina", "<p>Guardem els aliments a la nevera perquè, a menys temperatura, les reaccions que els fan malbé van més lentes. Les patates tallades a daus es couen abans que senceres perquè tenen més superfície.</p>")
    + compte("un catalitzador no canvia els productes ni la quantitat que se n'obté: només fa que s'arribi abans al final.")
    + resum(["Més xocs eficaços → reacció més ràpida.", "Factors: temperatura, concentració, superfície, catalitzadors."])))

# ------------------------------------------------------------------ SdA 5
add(5, "d5f1", "Posició, desplaçament i velocitat: el MRU", (
    idea("Per descriure un moviment triem un <b>sistema de referència</b> (un origen i un sentit positiu). La <b>posició (x)</b> diu on és el mòbil; el <b>desplaçament (Δx = x − x₀)</b>, quant ha canviat la posició.")
    + "<p class='formula'>\\( v = \\dfrac{\\Delta x}{\\Delta t} \\)</p><p>Si la velocitat és constant i la trajectòria és recta, el moviment és <b>rectilini uniforme (MRU)</b>:</p><p class='formula'>x = x₀ + v · t</p>"
    + "<h3>La gràfica posició–temps</h3><p>En un MRU és una <b>recta</b>. El <b>pendent</b> de la recta és la velocitat: com més inclinada, més ràpid. Una recta horitzontal vol dir que el mòbil està aturat.</p>"
    + ex("un autobús", "<p>Un autobús surt d'una parada situada a x₀ = 200 m i va a 10 m/s. On és al cap de 30 s?<br>x = 200 + 10 · 30 = <b>500 m</b>.</p>")
    + compte("abans d'operar, posa totes les dades en les mateixes unitats (m i s). Per passar de km/h a m/s, divideix per 3,6.")
    + resum(["v = Δx / Δt.", "MRU: x = x₀ + v·t.", "Pendent de la gràfica x–t = velocitat."])))

add(5, "d5f2", "El MRUA i la distància d'aturada", (
    idea("L'<b>acceleració</b> diu quant canvia la velocitat cada segon: \\( a = \\Delta v / \\Delta t \\) (m/s²). Si és constant i la trajectòria és recta, tenim un <b>MRUA</b>. Si el mòbil frena, a és negativa.")
    + "<p class='formula'>v = v₀ + a·t &nbsp;&nbsp;&nbsp; x = x₀ + v₀·t + ½·a·t²</p>"
    + "<p>A la gràfica <b>velocitat–temps</b>, el pendent és l'acceleració i l'<b>àrea</b> sota la recta és la distància recorreguda.</p>"
    + "<h3>Distància d'aturada = distància de reacció + distància de frenada</h3><ul><li><b>Reacció:</b> mentre el conductor reacciona (≈ 1 s), el cotxe continua a la mateixa velocitat (MRU).</li><li><b>Frenada:</b> el cotxe desaccelera fins que s'atura (MRUA).</li></ul>"
    + ex("un cotxe a 72 km/h", "<p>72 km/h = 20 m/s. Reacció d'1 s: 20 m. Frenada amb a = −4 m/s²: t = 20 / 4 = 5 s; distància = 20 · 5 − ½ · 4 · 5² = 50 m. <b>Distància d'aturada: 70 m.</b></p>")
    + compte("si la velocitat es duplica, la distància de frenada es multiplica per 4. Per això uns pocs km/h de menys a prop de les escoles salven vides.")
    + resum(["a = Δv / Δt.", "Gràfica v–t: pendent = a; àrea = distància.", "Aturada = reacció + frenada."])))

add(5, "d5f5", "Difusió i gradient de concentració", (
    idea("La <b>difusió</b> és el moviment net de partícules des d'on n'hi ha més (més concentració) cap a on n'hi ha menys. Passa sola, gràcies al moviment aleatori de les partícules (model cineticomolecular).")
    + "<p>Un <b>gradient de concentració</b> és la diferència de concentració entre dos punts. Com més gran és el gradient, més ràpida és la difusió en aquell punt.</p>"
    + "<h3>Factors que l'afecten</h3><ul><li><b>Temperatura:</b> partícules més ràpides → difusió més ràpida.</li><li><b>Distància:</b> difondre's una distància el doble de llarga triga unes quatre vegades més.</li><li><b>Mida de les partícules i medi:</b> en un gas és molt més ràpida que en un líquid.</li></ul>"
    + "<h3>Per què és important per a les cèl·lules immunitàries?</h3><p>Els bacteris alliberen substàncies que es difonen al seu voltant i formen un gradient. Els neutròfils tenen <b>receptors</b> que detecten on n'hi ha més i es mouen cap allà: és la <b>quimiotaxi</b>.</p>"
    + ex("l'olor", "<p>Si algú obre una ampolla de colònia en un racó de l'aula, al cap d'una estona l'olor arriba a l'altra punta: les partícules s'han difós des d'on n'hi havia moltes cap on no n'hi havia.</p>")
    + compte("la difusió no necessita que res «empenyi» les partícules: n'hi ha prou amb el seu moviment desordenat.")
    + resum(["De més concentració a menys.", "Més temperatura → més ràpida.", "El gradient guia les cèl·lules (quimiotaxi)."])))

add(5, "d5f6", "Les forces i les lleis de Newton", (
    idea("Una <b>força</b> és una interacció entre dos cossos que pot canviar-ne el moviment o deformar-los. És una magnitud <b>vectorial</b> (té mòdul, direcció i sentit) i es mesura en <b>newtons (N)</b>.")
    + "<table><tr><th>Llei</th><th>Què diu</th><th>Exemple</th></tr>"
      "<tr><td><b>1a</b> (inèrcia)</td><td>Si la força total és zero, un cos continua en repòs o en MRU</td><td>En frenar de cop, el cos continua endavant: per això cal el cinturó</td></tr>"
      "<tr><td><b>2a</b> (dinàmica)</td><td>F = m · a: com més força, més acceleració; com més massa, menys</td><td>Costa més accelerar un carro ple que un de buit</td></tr>"
      "<tr><td><b>3a</b> (acció i reacció)</td><td>Si A fa una força sobre B, B en fa una d'igual i de sentit contrari sobre A</td><td>En empènyer la paret amb el patinet, tu vas enrere</td></tr></table>"
    + ex("2a llei", "<p>Un patinet i la seva conductora sumen 60 kg. Quina força neta cal per accelerar-los a 1,5 m/s²? F = 60 · 1,5 = <b>90 N</b>.</p>")
    + "<p><b>Pes</b>: la força amb què la Terra atreu un cos, P = m · g, amb g = 9,8 N/kg. Una massa d'1 kg pesa 9,8 N.</p>"
    + compte("massa (kg) i pes (N) no són el mateix: a la Lluna la teva massa és la mateixa, però pesaries unes sis vegades menys.")
    + resum(["Força: vector, en N.", "F = m·a.", "Acció i reacció actuen sobre cossos diferents."])))

add(5, "d5hooke", "La llei de Hooke", (
    idea("Un cos <b>elàstic</b> es deforma quan hi fem força i recupera la forma quan la deixem de fer. En una molla, l'allargament és <b>proporcional</b> a la força (mentre no la deformem massa).")
    + "<p class='formula'>F = k · Δx</p><p>F és la força (N), Δx l'allargament (m) i <b>k la constant elàstica</b> (N/m). Una molla amb una k gran és <b>rígida</b>; amb una k petita, és tova.</p>"
    + "<h3>Com es troba k</h3><p>Pengem masses diferents, mesurem l'allargament i fem la gràfica F–Δx. Surt una recta que passa per l'origen: el seu <b>pendent és k</b>.</p>"
    + ex("una molla", "<p>Una massa de 200 g (pes = 0,2 · 9,8 = 1,96 N) allarga una molla 4,0 cm = 0,040 m. k = 1,96 / 0,040 = <b>49 N/m</b>.</p>")
    + "<h3>I les cèl·lules?</h3><p>Els investigadors posen les cèl·lules sobre un gel tou que es comporta com un conjunt de molles. Si saben la k del gel i mesuren quant es mouen unes boletes fluorescents, poden calcular la força que fa la cèl·lula: <b>microscòpia de forces de tracció</b>.</p>"
    + compte("Δx és l'allargament (longitud final − longitud inicial), no la longitud de la molla.")
    + resum(["F = k·Δx.", "k = pendent de la gràfica F–Δx.", "Més k → material més rígid."])))

# ------------------------------------------------------------------ SdA 6
add(6, "d6f1", "Energia, potència i consum", (
    idea("L'<b>energia</b> és la capacitat de produir canvis. No es crea ni es destrueix: es <b>transforma</b> (principi de conservació). La <b>potència</b> diu quanta energia es transforma cada segon.")
    + "<p class='formula'>E = P · t</p><p>En el SI, l'energia es mesura en <b>joules (J)</b> i la potència en <b>watts (W)</b>: 1 W = 1 J/s. A la factura de la llum es fa servir el <b>quilowatt hora</b>: 1 kWh = 1000 W · 3600 s = 3,6 × 10⁶ J.</p>"
    + ex("quant costa?", "<p>Una estufa de 1500 W funciona 2 h al dia durant 30 dies. E = 1,5 kW · 60 h = 90 kWh. A 0,20 €/kWh: 90 · 0,20 = <b>18 €</b>.</p>")
    + "<h3>Rendiment</h3><p>Cap aparell transforma tota l'energia en la que volem: una part es «perd», normalment com a calor. El <b>rendiment</b> és el percentatge d'energia útil:</p><p class='formula'>rendiment = energia útil / energia consumida × 100</p><p>Un <b>diagrama de Sankey</b> ho dibuixa amb fletxes de gruix proporcional a l'energia.</p>"
    + compte("per calcular el cost, la potència en kW i el temps en hores. Si fas servir W i segons, et sortiran joules.")
    + resum(["E = P·t.", "1 kWh = 3,6 × 10⁶ J.", "Rendiment = útil / consumida × 100."])))

add(6, "d6lab", "Circuits en sèrie i en paral·lel", (
    idea("Un <b>circuit elèctric</b> és un camí tancat per on circula el corrent: generador (pila o endoll), conductors, receptors (bombetes, motors…) i interruptor.")
    + "<table><tr><th></th><th>Sèrie</th><th>Paral·lel</th></tr>"
      "<tr><td>Com es connecten</td><td>Un darrere l'altre, en un sol camí</td><td>Cada receptor en una branca diferent</td></tr>"
      "<tr><td>Si un s'espatlla</td><td>S'apaguen tots</td><td>Els altres continuen funcionant</td></tr>"
      "<tr><td>Tensió a cada receptor</td><td>Es reparteix</td><td>Tots reben la tensió del generador</td></tr>"
      "<tr><td>Exemple</td><td>Algunes tires de llums de Nadal antigues</td><td>Tots els endolls i llums de casa (230 V)</td></tr></table>"
    + "<p>Per això la instal·lació d'una casa o d'una escola és en <b>paral·lel</b>: cada aparell rep 230 V i el pots engegar o apagar sense afectar els altres.</p>"
    + "<h3>Magnituds elèctriques</h3><p><b>Intensitat</b> (I, en ampers): quantitat de càrrega que passa cada segon. <b>Tensió</b> (V, en volts): «empenta» que dona el generador. <b>Potència</b>: P = V · I.</p>"
    + ex("el carregador del portàtil", "<p>La sortida del carregador indica 20 V i 3,25 A. P = 20 · 3,25 = <b>65 W</b>.</p>")
    + compte("un aparell en espera (amb el llum vermell) també consumeix. Desendollar-lo és la manera més segura d'estalviar.")
    + resum(["Sèrie: un sol camí. Paral·lel: diverses branques.", "Casa i escola: en paral·lel a 230 V.", "P = V·I."])))

add(6, "d6f2", "D'on ve l'electricitat?", (
    idea("Gairebé tota l'electricitat es genera fent girar una <b>turbina</b> connectada a un <b>alternador</b>: en girar, uns imants i unes bobines produeixen corrent (inducció electromagnètica, descoberta per Faraday el 1831). La diferència entre centrals és <b>què fa girar la turbina</b>.")
    + "<table><tr><th>Font</th><th>Què fa girar la turbina</th><th>Renovable?</th></tr>"
      "<tr><td>Nuclear</td><td>Vapor escalfat per la fissió de l'urani</td><td>No</td></tr>"
      "<tr><td>Cicle combinat</td><td>Gasos de la combustió del gas natural i vapor</td><td>No</td></tr>"
      "<tr><td>Hidràulica</td><td>L'aigua d'un embassament</td><td>Sí</td></tr>"
      "<tr><td>Eòlica</td><td>El vent</td><td>Sí</td></tr>"
      "<tr><td>Fotovoltaica</td><td>No hi ha turbina: la llum genera corrent directament en el silici</td><td>Sí</td></tr></table>"
    + "<h3>El mix elèctric de Catalunya (2024)</h3><p>Segons Red Eléctrica, la generació a Catalunya el 2024 va ser: nuclear 59,1 %, cicle combinat 13 %, hidràulica 9,6 %, cogeneració 8,4 %, eòlica 7,6 % i altres 2,3 %. Les renovables van ser el 19,1 % del total.</p>"
    + compte("«renovable» no vol dir «sense cap impacte»: també cal fabricar els panells i els aerogeneradors. Però no s'esgoten i no emeten CO₂ mentre generen.")
    + resum(["Turbina + alternador → electricitat.", "Renovables: no s'esgoten.", "A Catalunya, la nuclear encara genera més de la meitat de l'electricitat."])))

CSS = """
.pi-top{display:flex;align-items:center;gap:3mm;border-bottom:2.2pt solid var(--acc);padding-bottom:2mm;margin-bottom:4mm}
.pi-top .tag{background:var(--acc);color:#fff;font-weight:700;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;border-radius:1.6mm;padding:.8mm 2.4mm}
.pi-top .s{font-size:9pt;font-weight:700;color:var(--acc);letter-spacing:.06em;text-transform:uppercase}
.pi-top h1{font-size:19pt;margin:0;flex-basis:100%}
.pi-top{flex-wrap:wrap}
.pi-idea{background:var(--tint);border-left:3pt solid var(--acc);border-radius:0 2.5mm 2.5mm 0;padding:3mm 4mm;margin:0 0 4mm;font-size:11.5pt}
.pi-ex{border:1.1pt solid var(--acc);border-radius:2.5mm;padding:2.5mm 3.5mm;margin:3mm 0;break-inside:avoid}
.pi-lab{font-size:9pt;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--acc);margin-bottom:1mm}
.pi-warn{background:#FFF4E5;border-radius:2.5mm;padding:2.5mm 3.5mm;margin:3mm 0;font-size:10.5pt}
.pi-warn b{color:#B4570F}
.pi-sum{background:var(--soft);border-radius:2.5mm;padding:2.5mm 3.5mm;margin-top:3mm}
.pi-sum ul{margin:0}
table{font-size:9.8pt}
"""


def html(p):
    """HTML d'una píndola (cal haver fet use(n) abans)."""
    import gen_sda1 as G
    top = (f'<div class="pi-top"><span class="tag">Píndola</span><span class="s">SdA {p["n"]} · {G.SDA["title"]}</span>'
           f'<h1>{p["title"]}</h1></div>')
    return G.page(top + p["html"], CSS)
