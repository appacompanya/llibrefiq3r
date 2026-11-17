"""Teoria del llibre, en català i amb un esquema a cada bloc important."""
from peces import figura, M, EQ, calc, fmt, valor

G = "9,8"


def _cap(slug, n, titol, classe, grup, resum, seccions):
    return dict(slug=slug, n=n, titol=titol, classe=classe, grup=grup, resum=resum, seccions=seccions)


def _sec(i, num, titol, html):
    return dict(id=i, num=num, titol=titol, html=html)


def cinematica():
    t = calc("caiguda_t", {"h": 19.6})
    v = calc("caiguda_v", {"h": 19.6})
    hmax = calc("llanc_h", {"v0": 14})
    ttop = calc("llanc_t_dalt", {"v0": 14})
    return _cap("cinematica", "1", "Cinemàtica", "b-cin", "Moviment",
        "Posició, velocitat i acceleració. MRU, MRUA, gràfiques i moviment vertical.",
        [
        _sec("s1", "1.1", "Posició, trajectòria i desplaçament", f"""
<p>La cinemàtica descriu el moviment sense preguntar encara quina força el provoca. Per fer-ho cal dir on és el mòbil, com canvia aquesta posició amb el temps i com canvia la velocitat. En aquest capítol el moviment és rectilini: la trajectòria, que és la línia que recorre el mòbil, és un tros de recta, i n’hi ha prou amb una sola coordenada.</p>
<p>La <b>posició</b> {M(r"x")} és la coordenada del mòbil respecte d’un origen que triem nosaltres i d’un sentit que també triem. No és una propietat del mòbil: si canviem l’origen, el nombre canvia. El que no depèn de l’origen de la mateixa manera és el canvi de posició.</p>
{figura("eix", "La posició es llegeix sobre l’eix. El desplaçament és la diferència entre la posició final i la inicial, i porta signe.",
        punts=[(0.08, "origen", "#5c6570"), (0.32, "x₁", "#1f5fbf"), (0.78, "x₂", "#c26a00")],
        cota=(0.32, 0.78, "Δx"))}
<p>El <b>desplaçament</b> entre dos instants és la posició final menys la inicial, {M(r"\Delta x = x_2 - x_1")}. El signe diu el sentit: positiu si el mòbil acaba més endavant segons l’eix que hem triat, negatiu si acaba més enrere. La <b>distància recorreguda</b> és una altra cosa: és la longitud del camí, sempre positiva, i se suma encara que el mòbil faci mitja volta. Si un ascensor puja 8 m i en baixa 3, el desplaçament és 5 m cap amunt i la distància recorreguda és 11 m.</p>
<div class="box corr"><p class="lead">Error freqüent</p><p>Confondre desplaçament i distància recorreguda. El desplaçament porta signe i només mira el punt de sortida i el d’arribada. La distància recorreguda no es cancel·la quan hi ha una anada i una tornada.</p></div>
"""),
        _sec("s2", "1.2", "Velocitat", f"""
<p>La <b>velocitat mitjana</b> entre dos instants és el desplaçament dividit pel temps transcorregut:</p>
{EQ(r"v_m = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}")}
<p>La unitat del Sistema Internacional és el metre per segon, m/s. La velocitat mitjana també porta signe, el mateix del desplaçament. No s’ha de confondre amb la rapidesa mitjana, que és la distància recorreguda dividida pel temps i que sempre és positiva. Un cotxe que se’n va i torna al punt de partida té velocitat mitjana nul·la i rapidesa mitjana diferent de zero.</p>
<p>La <b>velocitat instantània</b> és el valor de la velocitat mitjana quan l’interval de temps es fa molt petit. En els moviments d’aquest capítol no caldrà calcular límits: o bé la velocitat és constant, o bé canvia de manera uniforme i la dona una equació. Quan es diu «la velocitat» sense adjectiu, en un problema de batxillerat se sol voler la instantània.</p>
<div class="box rec"><p class="lead">Recorda</p><p>Una velocitat negativa no vol dir que el mòbil «vagi a poc a poc». Vol dir que es mou en el sentit negatiu de l’eix. El mòdul de la velocitat és el valor absolut, i és el que marca un velocímetre.</p></div>
"""),
        _sec("s3", "1.3", "Acceleració", f"""
<p>L’<b>acceleració mitjana</b> mesura com canvia la velocitat amb el temps:</p>
{EQ(r"a_m = \frac{\Delta v}{\Delta t} = \frac{v_2 - v_1}{t_2 - t_1}")}
<p>La unitat és el metre per segon al quadrat, m/s². L’acceleració porta signe. Si l’eix apunta cap endavant, una acceleració positiva vol dir que la velocitat creix en aquest sentit: o bé el mòbil va cada cop més de pressa cap endavant, o bé frena mentre va cap enrere. Una acceleració negativa vol dir el contrari. Frenar, per tant, no és «tenir acceleració negativa» de manera automàtica: depèn de cap on apunti l’eix i de cap on vagi la velocitat.</p>
<p>En aquest curs tractarem sobretot l’acceleració constant. Quan l’acceleració és constant, l’acceleració mitjana i la instantània coincideixen, i el moviment es diu <b>rectilini uniformement accelerat</b>.</p>
"""),
        _sec("s4", "1.4", "Moviment rectilini uniforme", f"""
<p>En el moviment rectilini uniforme, el MRU, la velocitat és constant i l’acceleració és zero. La posició creix (o decreix) al mateix ritme tota l’estona. L’equació de la posició és</p>
{EQ(r"x = x_0 + v t")}
<p>on {M(r"x_0")} és la posició a l’instant que triem com a {M(r"t = 0")}, i {M(r"v")} és la velocitat constant. Si es coneixen tres d’aquestes magnituds, la quarta en surt aïllant. El temps, per exemple, és {M(r"t = (x - x_0)/v")}, sempre que la velocitat no sigui zero.</p>
{figura("grafica", "En un MRU la gràfica posició-temps és una recta. El pendent d’aquesta recta és la velocitat.",
        trams=[[(0, 4), (8, 36)]], xlabel="t (s)", ylabel="x (m)", xmin=0, xmax=10, ymin=0, ymax=40)}
<p>A la gràfica {M(r"x")}–{M(r"t")} el pendent és {M(r"\Delta x / \Delta t")}, és a dir, la velocitat. Una recta més dreta vol dir una velocitat més gran. Una recta horitzontal vol dir que el mòbil està aturat. Una recta que baixa vol dir velocitat negativa.</p>
<div class="box ex"><p class="lead">Exemple resolt</p>
<p><span class="pp">Plantejament</span> Un tren passa per l’origen amb velocitat constant de 24 m/s. Volem la posició al cap de 45 s.</p>
<p><span class="pp">Equació</span> Com que la velocitat no canvia, fem servir {M(r"x = x_0 + v t")}, amb {M(r"x_0 = 0")}.</p>
<p><span class="pp">Càlcul</span> {M(r"x = 24 \cdot 45 = 1080")} m.</p>
<p><span class="pp">Resultat</span> Al cap de 45 s el tren és a <b>1080 m</b> de l’origen, en el sentit positiu.</p></div>
"""),
        _sec("s5", "1.5", "Moviment rectilini uniformement accelerat", f"""
<p>En el MRUA l’acceleració és constant i diferent de zero. La velocitat canvia de manera uniforme i la posició no segueix una recta respecte del temps. Les dues equacions que cal saber usar, amb l’origen de temps a {M(r"t = 0")}, són</p>
{EQ(r"v = v_0 + a t")}
{EQ(r"x = x_0 + v_0 t + \frac{1}{2} a t^2")}
<p>{M(r"v_0")} és la velocitat a l’instant inicial. Si no ens donen el temps però sí el desplaçament, és útil l’equació que el temps no conté:</p>
{EQ(r"v^2 = v_0^2 + 2 a \Delta x")}
<p>amb {M(r"\Delta x = x - x_0")}. Aquesta relació surt d’eliminar el temps entre les dues anteriors. El signe de {M(r"v")} s’ha de triar amb el sentit del moviment: l’arrel quadrada dona un mòdul, i el signe el posem nosaltres.</p>
{figura("grafica", "En un MRUA la velocitat és una recta respecte del temps. El pendent és l’acceleració.",
        trams=[[(0, 2), (6, 14)]], xlabel="t (s)", ylabel="v (m/s)", xmin=0, xmax=8, ymin=0, ymax=16)}
<p>A la gràfica {M(r"v")}–{M(r"t")} el pendent és l’acceleració. L’àrea entre la gràfica i l’eix del temps, comptada positiva per sobre i negativa per sota, és el desplaçament. A la gràfica {M(r"a")}–{M(r"t")} d’un MRUA es veu una recta horitzontal, perquè l’acceleració no canvia.</p>
{figura("grafica", "Acceleració constant: la gràfica acceleració-temps és horitzontal.",
        trams=[[(0, 2), (7, 2)]], xlabel="t (s)", ylabel="a (m/s²)", xmin=0, xmax=8, ymin=-1, ymax=4)}
<div class="box ex"><p class="lead">Exemple resolt</p>
<p><span class="pp">Plantejament</span> Un cotxe parteix del repòs amb acceleració constant de 1,5 m/s². Volem la velocitat i la posició al cap de 6 s. L’origen és el punt de partida.</p>
<p><span class="pp">Càlcul</span> {M(r"v = 0 + 1,5 \cdot 6 = 9")} m/s. La posició és {M(r"x = 0 + 0 \cdot 6 + \frac{1}{2} \cdot 1,5 \cdot 6^2 = 27")} m.</p>
<p><span class="pp">Resultat</span> Al cap de 6 s va a <b>9 m/s</b> i ha recorregut <b>27 m</b>.</p></div>
"""),
        _sec("s6", "1.6", "Com es llegeix una gràfica", f"""
<p>Abans de calcular res, cal mirar què hi ha a cada eix i en quines unitats. Una recta a la gràfica {M(r"x")}–{M(r"t")} no vol dir el mateix que una recta a la gràfica {M(r"v")}–{M(r"t")}.</p>
<ul>
<li>A {M(r"x")}–{M(r"t")}, el pendent és la velocitat. Una corba que s’empina cada cop més és un MRUA amb acceleració del mateix sentit que la velocitat.</li>
<li>A {M(r"v")}–{M(r"t")}, el pendent és l’acceleració i l’àrea és el desplaçament. Si la recta travessa l’eix, el mòbil s’atura un instant i canvia de sentit.</li>
<li>A {M(r"a")}–{M(r"t")}, l’àrea entre la gràfica i l’eix és el canvi de velocitat, {M(r"\Delta v")}.</li>
</ul>
<p>Quan el moviment té dos trams, se’n fa un de cada vegada. La posició i la velocitat del final del primer tram són la posició i la velocitat inicials del segon. No es pot aplicar una sola equació de MRUA a tot el recorregut si l’acceleració canvia de tram.</p>
"""),
        _sec("s7", "1.7", "Caiguda lliure i llançament vertical", f"""
<p>A prop de la Terra, i si es pot negligir la resistència de l’aire, tots els cossos cauen amb la mateixa acceleració, {M(r"g = 9,8\,\mathrm{m/s}^2")}, cap avall. El moviment és un MRUA vertical. En aquest llibre, si no es diu una altra cosa, l’eix vertical apunta <b>cap amunt</b> i l’origen és a terra o al punt que indiqui l’enunciat. Amb aquest conveni l’acceleració és negativa:</p>
{EQ(r"a = -g = -9,8\,\mathrm{m/s}^2")}
{EQ(r"v = v_0 - g t")}
{EQ(r"y = y_0 + v_0 t - \frac{1}{2} g t^2")}
<p>En una <b>caiguda lliure</b> es deixa anar el cos, de manera que {M(r"v_0 = 0")}. Si l’altura de partida és {M(r"h")} i l’origen és a dalt, amb el sentit positiu cap avall és més còmode escriure {M(r"h = \frac{1}{2} g t^2")} i {M(r"v = g t")}. El mòdul de la velocitat d’arribada també es pot escriure {M(r"v = \sqrt{2 g h}")}, que no depèn de quin sentit hàgim anomenat positiu.</p>
{figura("caiguda", "Caiguda des del repòs. La velocitat, cap avall, és més gran com més temps ha passat. L’acceleració val g en tots els punts.", h="h")}
<p>En un <b>llançament vertical cap amunt</b> la velocitat inicial és positiva. El cos puja, s’atura un instant i torna a baixar. A dalt de tot la velocitat és zero, però l’acceleració continua sent {M(r"-g")}: no és un punt d’equilibri. L’alçada màxima, mesurada des del punt de llançament, és {M(r"h = v_0^2 / (2g)")}. El temps fins al punt més alt és {M(r"v_0 / g")}, i el temps fins a tornar a la mateixa altura és el doble, perquè la pujada i la baixada són simètriques si es pot negligir l’aire.</p>
{figura("llancament", "Llançament cap amunt. Al punt més alt la velocitat és nul·la i l’acceleració continua sent −g si l’eix apunta cap amunt.")}
<div class="box ex"><p class="lead">Exemple resolt</p>
<p><span class="pp">Plantejament</span> Es deixa caure una pedra des de 19,6 m. Volem el temps de caiguda i la velocitat d’arribada. Prenem {M(r"g = 9,8")} m/s² i el sentit positiu cap avall, amb origen al punt de partida, de manera que {M(r"v_0 = 0")}.</p>
<p><span class="pp">Càlcul</span> De {M(r"h = \frac{1}{2} g t^2")} surt {M(rf"t = \sqrt{{2 \cdot 19,6 / 9,8}} = {fmt(t, 2)}")} s. La velocitat és {M(rf"v = \sqrt{{2 g h}} = {fmt(v, 2)}")} m/s, cap avall.</p>
<p><span class="pp">Resultat</span> Triga <b>{fmt(t, 2)} s</b> i arriba a <b>{fmt(v, 2)} m/s</b>.</p></div>
<div class="box ex"><p class="lead">Exemple resolt</p>
<p><span class="pp">Plantejament</span> Es llança una pilota cap amunt a 14 m/s des del terra. Eix cap amunt.</p>
<p><span class="pp">Càlcul</span> L’alçada màxima és {M(rf"h = 14^2 / (2 \cdot 9,8) = {fmt(hmax, 2)}")} m. El temps fins a dalt és {M(rf"t = 14 / 9,8 = {fmt(ttop, 2)}")} s.</p>
<p><span class="pp">Resultat</span> Puja <b>{fmt(hmax, 2)} m</b> i triga <b>{fmt(ttop, 2)} s</b> a arribar-hi. Torna a terra al cap del doble, {fmt(2*ttop, 2)} s, amb velocitat de 14 m/s cap avall.</p></div>
"""),
        _sec("fm", "F", "Formulari del tema", f"""
<table><thead><tr><th>Relació</th><th>Quan es fa servir</th></tr></thead><tbody>
<tr><td>{M(r"v_m = \Delta x / \Delta t")}</td><td>Velocitat mitjana en qualsevol moviment rectilini.</td></tr>
<tr><td>{M(r"x = x_0 + v t")}</td><td>MRU, velocitat constant.</td></tr>
<tr><td>{M(r"v = v_0 + a t")}</td><td>MRUA, per trobar la velocitat.</td></tr>
<tr><td>{M(r"x = x_0 + v_0 t + \frac{1}{2} a t^2")}</td><td>MRUA, per trobar la posició.</td></tr>
<tr><td>{M(r"v^2 = v_0^2 + 2 a \Delta x")}</td><td>MRUA quan no intervé el temps.</td></tr>
<tr><td>{M(r"a = -g")} amb l’eix cap amunt</td><td>Caiguda i llançament vertical, sense aire.</td></tr>
</tbody></table>
<p>En tot el llibre, si l’enunciat no diu una altra cosa, {M(r"g = 9,8\,\mathrm{m/s}^2")}.</p>
"""),
        _sec("err", "E", "Errors freqüents", """
<ul>
<li>Aplicar les equacions del MRU quan la velocitat canvia, o les del MRUA a un tram on l’acceleració no és la de l’enunciat.</li>
<li>Oblidar el signe. Una velocitat cap avall és negativa si l’eix apunta cap amunt.</li>
<li>Creure que al punt més alt d’un llançament l’acceleració és zero. La velocitat és zero; l’acceleració val g.</li>
<li>Llegir el pendent d’una gràfica sense mirar quines magnituds hi ha als eixos.</li>
<li>Sumar temps i distàncies de dos trams com si fossin un sol MRUA.</li>
</ul>
"""),
        ])


def tir():
    return _cap("tir", "2", "Tir parabòlic", "b-tir", "Moviment",
        "Tir horitzontal i tir oblic: abast, alçada màxima, temps de vol i trajectòria.",
        [
        _sec("s1", "2.1", "Dos moviments alhora", f"""
<p>Un projectil llançat en l’aire, si es negligeix el fregament amb l’aire, té acceleració constant: zero en horitzontal i {M(r"-g")} en vertical, amb l’eix vertical cap amunt. El moviment es descompon en dos moviments independents que comparteixen el temps.</p>
<p>La component horitzontal de la velocitat no canvia, perquè en aquesta direcció no hi ha acceleració. La component vertical es comporta exactament com un llançament vertical. La trajectòria que en resulta és una paràbola.</p>
{EQ(r"v_x = v_0 \cos\theta")}
{EQ(r"v_y = v_0 \sin\theta - g t")}
{EQ(r"x = x_0 + (v_0 \cos\theta)\, t")}
{EQ(r"y = y_0 + (v_0 \sin\theta)\, t - \frac{1}{2} g t^2")}
<p>L’angle {M(r"\theta")} es mesura des de l’horitzontal. Si el tir és horitzontal, {M(r"\theta = 0")}, i per tant {M(r"v_y")} inicial és zero.</p>
"""),
        _sec("s2", "2.2", "Tir horitzontal", f"""
<p>Es llança un cos en horitzontal des d’una altura {M(r"h")}, amb velocitat {M(r"v_0")}. Cau mentre avança. El temps que triga a arribar a terra és el d’una caiguda lliure des d’aquesta altura, perquè la velocitat vertical inicial és zero:</p>
{EQ(r"t = \sqrt{\frac{2h}{g}}")}
<p>L’<b>abast</b>, que és la distància horitzontal recorreguda fins a terra, és {M(r"R = v_0 t")}. En el moment d’arribar, la velocitat horitzontal encara és {M(r"v_0")} i la vertical val {M(r"\sqrt{2gh}")}, cap avall. El mòdul de la velocitat és {M(r"v = \sqrt{v_0^2 + v_y^2}")}.</p>
{figura("tir_h", "Tir horitzontal. La component horitzontal de la velocitat es manté; la vertical creix com en una caiguda.", h="h", v="v₀")}
<div class="box corr"><p class="lead">Error freqüent</p><p>Creure que com més de pressa es llança en horitzontal, més triga a caure. El temps de caiguda només depèn de l’altura. La velocitat horitzontal canvia l’abast, no el temps.</p></div>
"""),
        _sec("s3", "2.3", "Tir oblic", f"""
<p>Si el cos surt des del terra amb velocitat {M(r"v_0")} i angle {M(r"\theta")}, torna a terra quan {M(r"y = 0")}. El temps de vol, l’alçada màxima i l’abast són</p>
{EQ(r"t_{\mathrm{vol}} = \frac{2 v_0 \sin\theta}{g}")}
{EQ(r"H = \frac{v_0^2 \sin^2\theta}{2g}")}
{EQ(r"R = \frac{v_0^2 \sin 2\theta}{g}")}
<p>L’alçada màxima s’assoleix a la meitat del temps de vol, quan la velocitat vertical s’anul·la. En aquest punt la velocitat no és zero: en queda la component horitzontal, {M(r"v_0 \cos\theta")}.</p>
{figura("tir_p", "Tir oblic des del terra. Al punt més alt la velocitat és horitzontal. H és l’alçada màxima i R l’abast.", theta=40, h="H", r="R")}
<p>L’abast és màxim, per a una velocitat inicial donada, quan {M(r"\sin 2\theta = 1")}, és a dir, a 45°. Dos angles complementaris, com 30° i 60°, donen el mateix abast i alçades diferents: l’angle gran puja més i està menys estona «avançant de pressa» en horitzontal.</p>
"""),
        _sec("s4", "2.4", "L’equació de la trajectòria", f"""
<p>Si s’elimina el temps entre {M(r"x")} i {M(r"y")}, s’obté l’altura de cada posició horitzontal, sense haver de passar pel temps. Per a un tir que surt de l’origen,</p>
{EQ(r"y = x \tan\theta - \frac{g x^2}{2 v_0^2 \cos^2\theta}")}
<p>Aquesta equació serveix per saber si el projectil passa per sobre d’un obstacle situat a una distància {M(r"x")}, o per trobar on és quan ha avançat una distància donada. És una paràbola. No substitueix les equacions del temps quan el que es demana és un instant o una velocitat en un instant concret: llavors és més net tornar a {M(r"x(t)")} i {M(r"y(t)")}.</p>
{figura("tir_p", "La trajectòria és una paràbola. L’angle de sortida és el de la tangent a l’origen.", theta=55, h="H", r="R")}
<div class="box rec"><p class="lead">Recorda</p><p>El temps és el lligam entre el moviment horitzontal i el vertical. Si un apartat demana «quan», gairebé sempre es troba primer el temps amb l’equació vertical, o amb l’horitzontal si la posició {M(r"x")} és la dada, i després se substitueix a l’altra component.</p></div>
"""),
        _sec("fm", "F", "Formulari del tema", f"""
<table><thead><tr><th>Relació</th><th>Quan es fa servir</th></tr></thead><tbody>
<tr><td>{M(r"v_x = v_0 \cos\theta")}</td><td>Component horitzontal, constant.</td></tr>
<tr><td>{M(r"v_y = v_0 \sin\theta - g t")}</td><td>Component vertical, eix cap amunt.</td></tr>
<tr><td>{M(r"t = \sqrt{2h/g}")}</td><td>Temps d’un tir horitzontal des d’altura h.</td></tr>
<tr><td>{M(r"R = v_0^2 \sin 2\theta / g")}</td><td>Abast sobre el pla de sortida.</td></tr>
<tr><td>{M(r"H = (v_0 \sin\theta)^2 / (2g)")}</td><td>Alçada màxima sobre el punt de sortida.</td></tr>
</tbody></table>
"""),
        _sec("err", "E", "Errors freqüents", f"""
<ul>
<li>Fer servir l’abast {M(r"R = v_0^2 \sin 2\theta / g")} quan el punt d’arribada no és a la mateixa altura que el de sortida. Aquesta fórmula és només per al pla horitzontal de sortida.</li>
<li>Oblidar que al punt més alt queda velocitat horitzontal.</li>
<li>Posar l’angle respecte de la vertical. En aquest llibre l’angle del tir es mesura des de l’horitzontal.</li>
<li>Sumar les components de la velocitat en comptes de combinar-les amb el teorema de Pitàgores.</li>
</ul>
"""),
        ])


def mcu():
    return _cap("mcu", "3", "Moviment circular uniforme", "b-mcu", "Moviment",
        "Angle, velocitat angular, període, freqüència, v = ωr i acceleració centrípeta.",
        [
        _sec("s1", "3.1", "Angle, període i freqüència", f"""
<p>Un mòbil descriu una circumferència amb rapidesa constant. L’angle girat es mesura en radiants. Un radian és l’angle que abasta un arc de longitud igual al radi; una volta sencera són {M(r"2\pi")} radiants.</p>
<p>La <b>velocitat angular</b> és el ritme amb què creix l’angle:</p>
{EQ(r"\omega = \frac{\Delta\theta}{\Delta t}")}
<p>Si el moviment és uniforme, {M(r"\omega")} és constant. El <b>període</b> {M(r"T")} és el temps d’una volta, i la <b>freqüència</b> {M(r"f")} és el nombre de voltes per segon. Es relacionen així:</p>
{EQ(r"f = \frac{1}{T} \qquad \omega = \frac{2\pi}{T} = 2\pi f")}
<p>La unitat de {M(r"\omega")} és el radian per segon, rad/s. La de la freqüència és el hertz, Hz, que és una volta per segon. Una freqüència de 50 Hz vol dir 50 voltes cada segon, no 50 rad/s.</p>
{figura("mcu", "L’angle θ es mesura en radiants. La velocitat angular diu com de pressa creix aquest angle.")}
"""),
        _sec("s2", "3.2", "Velocitat lineal i velocitat angular", f"""
<p>La velocitat del mòbil és tangent a la circumferència. El seu mòdul, la rapidesa lineal, i la velocitat angular es lliguen pel radi:</p>
{EQ(r"v = \omega r")}
<p>A igualtat de {M(r"\omega")}, el punt de més radi va més de pressa. L’arc recorregut és {M(r"s = r \theta")}, amb {M(r"\theta")} en radiants; per això {M(r"v = s/t = r \omega")}.</p>
{figura("v_omega", "La velocitat és tangent. El seu mòdul és ω multiplicat pel radi.")}
<div class="box corr"><p class="lead">Error freqüent</p><p>Posar l’angle en graus dins de {M(r"s = r \theta")} o de {M(r"\omega = \theta / t")}. Aquestes fórmules volen radiants. Per passar de graus a radiants es multiplica per {M(r"\pi / 180")}.</p></div>
"""),
        _sec("s3", "3.3", "Acceleració centrípeta", f"""
<p>Encara que el mòdul de la velocitat sigui constant, la velocitat com a vector canvia, perquè canvia de direcció. Hi ha, per tant, acceleració. En un MCU aquesta acceleració apunta cap al centre de la circumferència i es diu <b>acceleració centrípeta</b>:</p>
{EQ(r"a_c = \frac{v^2}{r} = \omega^2 r")}
<p>No hi ha acceleració tangencial: el mòbil no va ni més de pressa ni més a poc a poc. Tota l’acceleració serveix per girar el vector velocitat. Com més ràpid i com més tancada és la corba, més gran és {M(r"a_c")}.</p>
{figura("mcu_vec", "En qualsevol punt del MCU la velocitat és tangent i l’acceleració centrípeta apunta al centre.")}
<p>Més endavant, quan es parli de forces, aquesta acceleració demanarà una força resultant cap al centre, {M(r"F_c = m a_c")}. Ara n’hi ha prou de saber calcular {M(r"a_c")} i de no confondre-la amb una acceleració que faci canviar el mòdul de {M(r"v")}.</p>
"""),
        _sec("fm", "F", "Formulari del tema", f"""
<table><thead><tr><th>Relació</th><th>Unitat</th></tr></thead><tbody>
<tr><td>{M(r"\omega = 2\pi / T = 2\pi f")}</td><td>rad/s</td></tr>
<tr><td>{M(r"f = 1/T")}</td><td>Hz</td></tr>
<tr><td>{M(r"v = \omega r")}</td><td>m/s</td></tr>
<tr><td>{M(r"a_c = v^2 / r = \omega^2 r")}</td><td>m/s²</td></tr>
<tr><td>{M(r"s = r \theta")}</td><td>m, amb θ en rad</td></tr>
</tbody></table>
"""),
        _sec("err", "E", "Errors freqüents", """
<ul>
<li>Confondre freqüència i velocitat angular. Passar de l’una a l’altra exigeix el factor 2π.</li>
<li>Dir que en un MCU l’acceleració és zero perquè «la velocitat és constant». El mòdul és constant; el vector no.</li>
<li>Posar l’acceleració centrípeta tangent a la trajectòria. És radial, cap al centre.</li>
<li>Fer servir graus on la fórmula vol radiants.</li>
</ul>
"""),
        ])


def newton():
    return _cap("newton", "4", "Lleis de Newton", "b-new", "Dinàmica",
        "Inèrcia, llei fonamental i parells acció-reacció. Massa i pes.",
        [
        _sec("s1", "4.1", "La primera llei", f"""
<p>Si la força resultant sobre un cos és zero, la velocitat del cos no canvia: o està quiet, o es mou en línia recta amb velocitat constant. Aquest enunciat és la <b>primera llei de Newton</b>, o llei de la inèrcia. No cal una força per mantenir un MRU. Cal una força resultant diferent de zero per canviar la velocitat, és a dir, per accelerar, frenar o girar.</p>
<p>La inèrcia és la resistència a aquest canvi. Es mesura amb la massa. Un camió i una pilota que vagin a la mateixa velocitat no són igual de «difícils d’aturar»: el camió té més massa i, per tant, més inèrcia.</p>
<div class="box rec"><p class="lead">Recorda</p><p>Un cos en repòs i un cos en MRU tenen, tots dos, força resultant nul·la. L’equilibri no és només «estar quiet».</p></div>
"""),
        _sec("s2", "4.2", "La segona llei", f"""
<p>La força resultant sobre un cos i l’acceleració que adquireix són proporcionals. La constant de proporcionalitat és la massa:</p>
{EQ(r"\vec F_{\mathrm{res}} = m \vec a")}
<p>En mòdul, si la resultant té mòdul {M(r"F")}, {M(r"F = m a")}. La força es mesura en newtons. Un newton és la força que dona a una massa d’un quilogram una acceleració d’un metre per segon al quadrat: {M(r"1\,\mathrm{N} = 1\,\mathrm{kg \cdot m/s^2}")}.</p>
<p>La resultant és la suma vectorial de totes les forces, no «la força més gran». Si dues forces iguals i oposades actuen sobre el mateix cos, la resultant és zero i el cos no accelera. L’acceleració té sempre la direcció i el sentit de la resultant, no els de cadascuna de les forces per separat.</p>
{figura("fma", "La mateixa força resultant dona més acceleració al cos de menys massa.")}
"""),
        _sec("s3", "4.3", "La tercera llei", f"""
<p>Les forces apareixen per parelles. Si un cos A fa una força sobre un cos B, el cos B fa sobre A una força del mateix mòdul, la mateixa direcció i sentit contrari. Les dues forces són simultànies, de la mateixa natura, i <b>actuen sobre cossos diferents</b>. Per això no es cancel·len entre elles: cada una entra al diagrama d’un cos diferent.</p>
{figura("parells", "El pes i la normal que actuen sobre el llibre no formen un parell acció-reacció, perquè totes dues actuen sobre el llibre. El parell de la normal és la força amb què el llibre empeny la taula.")}
<p>El pes d’un llibre i la normal de la taula sobre el llibre poden sumar zero i deixar el llibre en equilibri, però no són un parell de la tercera llei: totes dues actuen sobre el llibre. El parell del pes és l’atracció que el llibre fa sobre la Terra. El parell de la normal és l’empenta del llibre contra la taula.</p>
"""),
        _sec("s4", "4.4", "Massa i pes", f"""
<p>La <b>massa</b> {M(r"m")} mesura la inèrcia i també la quantitat de matèria. No depèn del lloc. Es mesura en quilograms.</p>
<p>El <b>pes</b> és la força amb què la Terra atrau el cos. A prop de la superfície val</p>
{EQ(r"P = m g")}
<p>amb {M(r"g = 9,8")} m/s². El pes es mesura en newtons, no en quilograms. Un cos de 2 kg pesa {M(r"2 \cdot 9,8 = 19,6")} N. A la Lluna la massa seria la mateixa i el pes, no, perquè {M(r"g")} hi és més petit.</p>
<div class="box corr"><p class="lead">Error freqüent</p><p>Escriure el pes en quilograms, o posar la massa en newtons dins de {M(r"F = m a")}. Abans de substituir, cada dada ha d’estar en la unitat que la fórmula espera.</p></div>
"""),
        _sec("fm", "F", "Formulari del tema", f"""
<table><thead><tr><th>Relació</th><th>Comentari</th></tr></thead><tbody>
<tr><td>{M(r"F_{\mathrm{res}} = m a")}</td><td>Segona llei, en mòdul.</td></tr>
<tr><td>{M(r"P = m g")}</td><td>Pes a prop de la Terra, g = 9,8 m/s².</td></tr>
<tr><td>Parell acció-reacció</td><td>Mateix mòdul, sentits oposats, cossos diferents.</td></tr>
</tbody></table>
"""),
        _sec("err", "E", "Errors freqüents", """
<ul>
<li>Creure que el moviment demana una força resultant en el sentit de la velocitat. Això només és cert si hi ha acceleració en aquest sentit.</li>
<li>Sumar com a nombres dues forces que no tenen la mateixa direcció.</li>
<li>Cancel·lar les dues forces d’un parell acció-reacció dins del diagrama d’un sol cos.</li>
<li>Confondre massa i pes.</li>
</ul>
"""),
        ])


def forces():
    return _cap("forces", "5", "Forces i balanços", "b-for", "Dinàmica",
        "Pes, normal, fregament, tensió i força elàstica. Plans, politges i força centrípeta.",
        [
        _sec("s1", "5.1", "Les forces que farem servir", f"""
<p>Un balanç de forces comença per una llista completa de les forces que actuen sobre el cos que estudiem, i només d’aquestes. Les que apareixen en aquest capítol són aquestes.</p>
<p>El <b>pes</b> {M(r"P = mg")} és vertical i cap avall. Actua sempre, tant si el cos toca una superfície com si no.</p>
<p>La <b>normal</b> {M(r"N")} és la força de contacte perpendicular a la superfície. No és una reacció automàtica del pes: en un pla inclinat no val {M(r"mg")}, i si un fil estira el cos cap amunt pot ser més petita que el pes. La normal empeny el cos i no l’estira.</p>
<p>El <b>fregament</b> és paral·lel a la superfície i s’oposa al lliscament. El fregament estàtic, quan el cos encara no llisca, val el que calgui per impedir el moviment, fins a un màxim {M(r"f_{s,\max} = \mu_s N")}. El fregament cinètic, quan ja llisca, val {M(r"f_c = \mu_c N")} i s’oposa a la velocitat. {M(r"\mu_s")} i {M(r"\mu_c")} són els coeficients, sense unitat, i en general {M(r"\mu_s > \mu_c")}.</p>
<p>La <b>tensió</b> d’una corda estira el cos cap a la corda. En una corda ideal, de massa negligible i que no s’allarga, la tensió és la mateixa als dos extrems i la corda només aguanta tracció, no compressió.</p>
<p>La <b>força elàstica</b> d’una molla és {M(r"F = k x")}, on {M(r"x")} és la deformació respecte de la longitud natural i {M(r"k")} és la constant de la molla, en N/m. La força s’oposa a la deformació: la molla estirada estira cap endins, i la comprimida empeny cap enfora.</p>
"""),
        _sec("s2", "5.2", "El diagrama de cos lliure", f"""
<p>El diagrama de cos lliure és el dibuix del cos sol, separat de la resta, amb totes les forces que els altres cossos li fan. No s’hi dibuixa la velocitat, ni l’acceleració com si fos una força, ni les forces que el cos fa sobre els altres. Cada força surt del cos, amb fletxa, nom i, si es pot, un valor.</p>
{figura("dcl", "Diagrama en un pla horitzontal: pes, normal, força aplicada i fregament. El pes i la normal es compensen.", fregament=True)}
<p>Després del dibuix es trien eixos. En un pla horitzontal, un eix horitzontal i un de vertical. En un pla inclinat, convé un eix al llarg del pla i un de perpendicular, perquè l’acceleració, si n’hi ha, va al llarg del pla i la normal queda en un sol eix. Es projecten les forces i s’escriu {M(r"\sum F_x = m a_x")} i {M(r"\sum F_y = m a_y")}. Si el cos no accelera en un eix, la suma en aquell eix és zero.</p>
"""),
        _sec("s3", "5.3", "Pla horitzontal", f"""
<p>En un pla horitzontal el pes i la normal són verticals. Si no hi ha cap altra força vertical, {M(r"N = P = mg")}. En horitzontal, la resultant és la força aplicada menys el fregament, si n’hi ha i si el cos es mou en el sentit de la força:</p>
{EQ(r"F - f = m a \qquad f = \mu_c N = \mu_c m g")}
<p>Si la superfície és llisa, {M(r"f = 0")} i {M(r"a = F/m")}. Si el cos està en repòs i la força aplicada no supera {M(r"\mu_s N")}, no es posa en marxa i l’acceleració és zero: el fregament estàtic iguala la força aplicada.</p>
"""),
        _sec("s4", "5.4", "El pla inclinat", f"""
<p>En un pla d’angle {M(r"\alpha")}, el pes es descompon. Amb l’eix {M(r"x")} pendent avall i l’eix {M(r"y")} perpendicular al pla, cap enfora:</p>
{EQ(r"P_x = m g \sin\alpha \qquad P_y = m g \cos\alpha")}
<p>La normal equilibra la component perpendicular, {M(r"N = m g \cos\alpha")}, si res més empeny el cos contra el pla. Sense fregament, la resultant és {M(r"m g \sin\alpha")} i l’acceleració pendent avall és {M(r"a = g \sin\alpha")}, independent de la massa.</p>
{figura("inclinat", "Pla inclinat amb pes, normal i fregament. L’angle del pla és el que forma amb l’horitzontal.", alpha=30, fregament=True)}
{figura("dcl_inclinat", "Diagrama de cos lliure amb els eixos del pla i les components del pes.", alpha=30, fregament=True)}
<p>Si hi ha fregament cinètic i el cos baixa, el fregament apunta pendent amunt i val {M(r"\mu_c N = \mu_c m g \cos\alpha")}. L’acceleració pendent avall és</p>
{EQ(r"a = g (\sin\alpha - \mu_c \cos\alpha)")}
<p>Si aquesta expressió surt negativa, el fregament cinètic no es pot aplicar tal qual: el cos no baixaria tot sol i cal estudiar el fregament estàtic.</p>
"""),
        _sec("s5", "5.5", "Cossos enllaçats i politja", f"""
<p>Quan dos cossos van lligats per una corda ideal, es poden estudiar junts o per separat. Junts, la tensió és una força interna i no entra a la resultant del sistema, sempre que la corda no canviï de direcció. Per separat, la tensió sí que entra, i és la mateixa als dos extrems.</p>
{figura("dos_blocs", "Dos blocs lligats en un pla horitzontal. Per al sistema sencer la tensió es cancel·la; per a cada bloc, no.", m1="m₁", m2="m₂")}
<p>En una politja ideal, sense massa i sense fregament a l’eix, la tensió també és la mateixa als dos costats. A la màquina d’Atwood, amb {M(r"m_2 > m_1")}, l’acceleració del sistema i la tensió són</p>
{EQ(r"a = \frac{(m_2 - m_1) g}{m_1 + m_2} \qquad T = \frac{2 m_1 m_2 g}{m_1 + m_2}")}
{figura("atwood", "Politja ideal. Si m₂ és més gran, m₂ baixa i m₁ puja, amb la mateixa acceleració en mòdul.", m1="m₁", m2="m₂")}
<p>Si un bloc és damunt una taula llisa i l’altre penja, l’únic pes que accelera el sistema és el del bloc que penja. Amb masses {M(r"M")} a la taula i {M(r"m")} penjant,</p>
{EQ(r"a = \frac{m g}{M + m} \qquad T = M a = \frac{M m g}{M + m}")}
{figura("taula", "El pes del bloc que penja arrossega el de la taula. Si la taula és llisa, no hi ha fregament a la resultant.", M="M", m="m")}
"""),
        _sec("s6", "5.6", "Força elàstica i força centrípeta", f"""
<p>Una molla de constant {M(r"k")} deformada una longitud {M(r"x")} fa {M(r"F = kx")}. En un problema de forces, aquesta expressió es posa al diagrama com qualsevol altra força, amb el sentit que correspon: contra la deformació.</p>
{figura("molla", "La força de la molla és proporcional a la deformació i s’hi oposa.")}
<p>Quan un cos descriu una circumferència, la segona llei en la direcció radial diu que la resultant cap al centre val {M(r"m v^2 / r")}. Aquesta resultant és la <b>força centrípeta</b>. No és una força nova que calgui afegir al diagrama: és el nom de la suma de les que ja hi són, projectades cap al centre.</p>
{figura("revolt", "En un revolt pla, el fregament de les rodes apunta cap al centre i fa de força centrípeta.")}
<p>En un revolt pla, aquesta força la fa el fregament. El màxim, just abans de derrapar, és {M(r"\mu N = \mu m g")}, i la velocitat màxima és {M(r"v = \sqrt{\mu r g}")}. En un revolt peraltat un angle {M(r"\theta")}, sense fregament, la component horitzontal de la normal fa aquest paper, i {M(r"\tan\theta = v^2 /(r g)")}.</p>
{figura("peralt", "Secció d’un peralt. La normal és perpendicular a la calçada, no vertical.", theta=28)}
{figura("corda", "La tensió de la corda és la força centrípeta si el pla del gir és horitzontal i llis.", r="r")}
<p>En un lòpping vertical, al capdamunt el pes i la normal apunten tots dos cap al centre: {M(r"N + mg = m v^2 / r")}. La velocitat mínima per no caure és la que fa {M(r"N = 0")}, és a dir {M(r"v = \sqrt{g r}")}. A baix, la normal és cap amunt, més gran que el pes: {M(r"N - mg = m v^2 / r")}.</p>
{figura("loop", "Lòpping. Al capdamunt el pes ajuda a fer la força centrípeta; a baix, la normal ha de vèncer el pes i encara aportar la força centrípeta.")}
"""),
        _sec("fm", "F", "Formulari del tema", f"""
<table><thead><tr><th>Situació</th><th>Relació</th></tr></thead><tbody>
<tr><td>Pes</td><td>{M(r"P = mg")}</td></tr>
<tr><td>Fregament cinètic</td><td>{M(r"f_c = \mu_c N")}</td></tr>
<tr><td>Fregament estàtic màxim</td><td>{M(r"f_{s,\max} = \mu_s N")}</td></tr>
<tr><td>Pla inclinat llis</td><td>{M(r"a = g\sin\alpha")}, {M(r"N = mg\cos\alpha")}</td></tr>
<tr><td>Atwood</td><td>{M(r"a = (m_2-m_1)g/(m_1+m_2)")}</td></tr>
<tr><td>Molla</td><td>{M(r"F = kx")}</td></tr>
<tr><td>Força centrípeta</td><td>{M(r"F_c = m v^2 / r")}</td></tr>
<tr><td>Peralt sense fregament</td><td>{M(r"\tan\theta = v^2/(r g)")}</td></tr>
</tbody></table>
"""),
        _sec("err", "E", "Errors freqüents", f"""
<ul>
<li>Posar la normal igual al pes en un pla inclinat. Al pla inclinat {M(r"N = mg\cos\alpha")}.</li>
<li>Dibuixar el fregament en el sentit del moviment. El cinètic s’oposa a la velocitat; l’estàtic s’oposa a la tendència a lliscar.</li>
<li>Afegir «la força centrípeta» com una fletxa de més, a banda de la tensió o del fregament que ja la fan.</li>
<li>Creure que la tensió d’una politja simple és el pes del cos que penja. Només ho és si aquest cos no accelera.</li>
</ul>
"""),
        ])


def energia():
    return _cap("energia", "6", "Energia", "b-ene", "Energia",
        "Treball, energia cinètica i potencial. Conservació de l’energia mecànica, sense fregament.",
        [
        _sec("s1", "6.1", "Treball i energia cinètica", f"""
<p>El <b>treball</b> d’una força constant que forma un angle {M(r"\varphi")} amb el desplaçament és</p>
{EQ(r"W = F \Delta x \cos\varphi")}
<p>Es mesura en joules. Un joule és el treball d’una força d’un newton al llarg d’un metre en la seva mateixa direcció. Si la força és perpendicular al desplaçament, el treball és zero: la normal d’un pla horitzontal no treballa mentre el cos llisca sobre el pla, i el pes no treballa en un desplaçament horitzontal.</p>
{figura("treball", "Només la component de la força al llarg del desplaçament fa treball.")}
<p>L’<b>energia cinètica</b> és l’energia associada a la velocitat:</p>
{EQ(r"E_c = \frac{1}{2} m v^2")}
<p>És sempre positiva i es mesura també en joules. En aquest capítol la farem servir dins del balanç de l’energia mecànica.</p>
"""),
        _sec("s2", "6.2", "Energia potencial", f"""
<p>L’<b>energia potencial gravitatòria</b>, a prop de la Terra, es pot escriure</p>
{EQ(r"E_p = m g h")}
<p>L’altura {M(r"h")} es mesura des d’un nivell que triem nosaltres. El valor de {M(r"E_p")} depèn d’aquesta tria; les diferències, no. Per això en un problema cal dir quin és el nivell zero i no canviar-lo a mig càlcul. Quan un cos puja, l’energia potencial gravitatòria augmenta; quan baixa, disminueix.</p>
<p>L’<b>energia potencial elàstica</b> d’una molla és</p>
{EQ(r"E_p = \frac{1}{2} k x^2")}
<p>on {M(r"x")} és la deformació respecte de la longitud natural. Val el mateix si la molla s’estira que si es comprimeix la mateixa longitud, perquè {M(r"x")} hi és al quadrat. Al punt d’equilibri de la molla, si {M(r"x = 0")}, aquesta energia és zero.</p>
{figura("molla", "En una molla horitzontal, la deformació x és la que entra a l’energia potencial elàstica.", comprimida=False)}
"""),
        _sec("s3", "6.3", "Conservació de l’energia mecànica", f"""
<p>L’<b>energia mecànica</b> és la suma de la cinètica i de les potencials que intervenen:</p>
{EQ(r"E_m = E_c + E_p")}
<p>Quan les úniques forces que treballen són el pes i la força de les molles, l’energia mecànica es conserva. El que perd una forma d’energia ho guanya l’altra, i</p>
{EQ(r"E_{c1} + E_{p1} = E_{c2} + E_{p2}")}
<p>En aquest capítol tots els problemes són d’aquest tipus. No hi ha fregament, ni cap altra força que en tregui energia mecànica. Si un enunciat d’un altre tema porta fregament, l’energia mecànica no es conserva i aquell problema no es resol amb aquest balanç.</p>
{figura("barres", "En una caiguda sense fregament l’energia mecànica es manté: la potencial es converteix en cinètica.",
        etapes=[("dalt", 0, 100), ("a mig camí", 50, 50), ("terra", 100, 0)])}
<p>Una caiguda des del repòs il·lustra el balanç. Si a dalt {M(r"E_c = 0")} i {M(r"E_p = mgh")}, i a baix {M(r"E_p = 0")}, llavors {M(r"\frac{1}{2} m v^2 = m g h")}, de manera que {M(r"v = \sqrt{2gh}")}. La massa se’n va: cau igual de de pressa un cos pesant que un de lleuger, si es pot negligir l’aire. El mateix resultat que la cinemàtica, per un camí que no necessita el temps.</p>
<p>En un llançament cap amunt, l’energia cinètica inicial es converteix en potencial. A dalt, {M(r"v = 0")} i {M(r"h = v_0^2 / (2g)")}. Entre dues altures qualssevol,</p>
{EQ(r"\frac{1}{2} m v_1^2 + m g h_1 = \frac{1}{2} m v_2^2 + m g h_2")}
{figura("muntanya", "Muntanya russa sense fregament. L’altura de cada punt fixa l’energia potencial; la velocitat es troba conservant l’energia mecànica.", hA="0", hB="h_B", hC="h_C")}
<p>En un pla inclinat llis passa el mateix: només importa el desnivell, no la longitud del pla. Si el pla baixa una altura {M(r"h = d \sin\alpha")}, la velocitat al final, partint del repòs, és {M(r"\sqrt{2gh}")}, com si hagués caigut en vertical aquesta altura.</p>
"""),
        _sec("s4", "6.4", "Pèndol, molla i tir", f"""
<p>En un pèndol simple de longitud {M(r"L")}, si es mesura l’altura des del punt més baix, el cos deixat anar des d’un angle {M(r"\theta")} respecte de la vertical té una altura {M(r"h = L(1 - \cos\theta)")}. Al punt baix tota l’energia és cinètica:</p>
{EQ(r"m g L (1 - \cos\theta) = \frac{1}{2} m v^2")}
{figura("pendol", "L’altura del pèndol es mesura des del punt més baix. Sense fregament, l’energia mecànica es conserva.", theta=50)}
<p>En una molla horitzontal, sense fregament, l’energia passa de potencial elàstica a cinètica. Si s’allibera des de l’amplitud {M(r"A")}, on la velocitat és zero,</p>
{EQ(r"\frac{1}{2} k A^2 = \frac{1}{2} m v^2 + \frac{1}{2} k x^2")}
<p>La velocitat màxima és a {M(r"x = 0")} i val {M(r"v = A \sqrt{k/m}")}.</p>
{figura("barres", "Molla sense fregament. A l’amplitud tota l’energia és potencial; a l’equilibri, tota és cinètica.",
        etapes=[("amplitud", 0, 100), ("a mig camí", 50, 50), ("equilibri", 100, 0)])}
<p>En un tir parabòlic sense resistència de l’aire l’energia mecànica també es conserva. Al punt més alt no val zero l’energia cinètica, perquè la velocitat horitzontal no s’ha anul·lat. Si es pren energia potencial zero al nivell de sortida i el tir surt i torna a aquest nivell, la velocitat d’arribada té el mateix mòdul que la de sortida.</p>
{figura("barres", "Tir sense resistència de l’aire. Al punt més alt queda energia cinètica, la de la velocitat horitzontal.",
        etapes=[("sortida", 70, 0), ("dalt", 30, 40), ("arribada", 70, 0)])}
<p>La <b>potència</b> és el ritme amb què es transfereix energia, {M(r"P = \Delta E / \Delta t")}, i es mesura en watts. En aquest capítol no la farem servir per resoldre els exercicis: tots es resolen amb la conservació de l’energia mecànica.</p>
<div class="box clau"><p class="lead">El balanç d’aquest capítol</p><p>Es tria un nivell zero per a l’altura. S’escriu {M(r"E_c + E_p")} al punt inicial i al punt final, amb la gravitatòria, l’elàstica o totes dues. Es conserven. No s’hi afegeix cap terme de fregament ni de treball de cap altra força.</p></div>
"""),
        _sec("fm", "F", "Formulari del tema", f"""
<table><thead><tr><th>Relació</th><th>Comentari</th></tr></thead><tbody>
<tr><td>{M(r"W = F \Delta x \cos\varphi")}</td><td>Treball d’una força constant.</td></tr>
<tr><td>{M(r"E_c = \frac{1}{2} m v^2")}</td><td>Energia cinètica.</td></tr>
<tr><td>{M(r"E_p = m g h")}</td><td>Potencial gravitatòria.</td></tr>
<tr><td>{M(r"E_p = \frac{1}{2} k x^2")}</td><td>Potencial elàstica.</td></tr>
<tr><td>{M(r"E_{m1} = E_{m2}")}</td><td>Sense fregament, només pes i molles.</td></tr>
<tr><td>{M(r"v = \sqrt{2 g h}")}</td><td>Caiguda des del repòs, desnivell h.</td></tr>
</tbody></table>
"""),
        _sec("err", "E", "Errors freqüents", """
<ul>
<li>Canviar el nivell zero de l’altura entre el punt inicial i el final.</li>
<li>Posar energia cinètica zero al capdamunt d’un tir parabòlic. Hi queda la velocitat horitzontal.</li>
<li>Fer servir la conservació quan l’enunciat diu que hi ha fregament. En aquest capítol no n’hi ha; si en un altre problema n’hi ha, aquest balanç no es pot aplicar tal qual.</li>
<li>Oblidar l’energia elàstica quan la molla està deformada, o comptar-la dues vegades.</li>
<li>Confondre la deformació de la molla amb la longitud total de la molla.</li>
</ul>
"""),
        ])


TEMES = [cinematica(), tir(), mcu(), newton(), forces(), energia()]
