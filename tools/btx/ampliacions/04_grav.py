"""Tema 4. Camp gravitatori: definició de camp, treball de la força gravitatòria, potencial, balanços amb satèl·lits."""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _svg import Svg, INK, GREY, RED, BLUE, GREEN

F = "camp-gravitatori"


def fig_45():
    s = Svg(700, 392)
    cx, cy = 90, 350
    rA, rB = 320, 150
    s.circle(cx, cy, 34, INK, "#e9ecf1", 1.5)
    s.text(cx, cy + 5, "M", 15, "middle", INK, True)
    P = lambda r, a: (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
    for r in (rA, rB):
        s.poly([P(r, a) for a in range(0, 91, 2)], GREY, 1.1, dash="5 5")
    sub = lambda t: f"<tspan dy='4' font-size='10'>{t}</tspan>"
    s.text(P(rA, 0)[0] + 4, cy - 6, "r" + sub("A"), 12, "start", GREY, True)
    s.text(P(rB, 0)[0] + 4, cy - 6, "r" + sub("B"), 12, "start", GREY, True)
    A, B, Ap = P(rA, 12), P(rB, 72), P(rA, 72)
    # camí 1: corba de Bézier per dins
    C = (300, 230)
    pts = [((1 - t) ** 2 * A[0] + 2 * (1 - t) * t * C[0] + t * t * B[0], (1 - t) ** 2 * A[1] + 2 * (1 - t) * t * C[1] + t * t * B[1]) for t in [i / 40 for i in range(41)]]
    s.poly(pts, BLUE, 2.2)
    s.head(pts[20][0], pts[20][1], math.atan2(pts[21][1] - pts[19][1], pts[21][0] - pts[19][0]), BLUE, 11)
    s.text(pts[20][0] - 4, pts[20][1] + 26, "camí 1", 13, "middle", BLUE, bold=True)
    # camí 2: arc + radial
    arc = [P(rA, 12 + 60 * i / 40) for i in range(41)]
    s.poly(arc, RED, 2.2)
    s.head(arc[20][0], arc[20][1], math.atan2(arc[21][1] - arc[19][1], arc[21][0] - arc[19][0]), RED, 11)
    s.arrow(Ap[0], Ap[1], B[0], B[1], RED, 2.2, 11)
    q = P(rA + 16, 40)
    s.text(q[0], q[1], "camí 2", 13, "start", RED, bold=True)
    q = P(rA + 16, 40)
    s.text(q[0], q[1] + 17, "arc: W = 0", 12, "start", RED)
    m = P((rA + rB) / 2, 72)
    s.text(m[0] - 8, m[1], "tram radial", 12, "end", RED)
    for Q, lab in [(A, "A"), (B, "B")]:
        s.circle(Q[0], Q[1], 4.5, INK, INK)
    s.text(A[0] + 10, A[1] + 16, "A", 15, "start", INK, True)
    s.text(B[0] - 10, B[1] + 18, "B", 15, "end", INK, True)
    for a in (22, 55):
        p1, p2 = P(rA + 60, a), P(rA + 20, a)
        s.arrow(p1[0], p1[1], p2[0], p2[1], GREEN, 1.9, 9)
    q = P(rA + 62, 22)
    s.text(q[0] + 4, q[1] - 6, "g", 14, "start", GREEN, True, True)
    s.text(470, 36, "El treball d’A a B és el", 13, "start", INK)
    s.text(470, 54, "mateix pels dos camins:", 13, "start", INK)
    s.text(470, 72, "només depèn de r" + sub("A") + "<tspan dy='-4'> i r</tspan>" + sub("B"), 13, "start", INK)
    s.line(470, 98, 500, 98, GREY, 1.1, "5 5")
    s.text(508, 102, "equipotencials", 12, "start", GREY)
    return s.svg()


FIGS = {
    "fig-4.5": (fig_45(), "La força gravitatòria és conservativa. Per anar d’A a B, el camí 2 segueix primer un arc centrat en M "
                "(perpendicular a la força: no hi ha treball) i després un tram radial. Qualsevol camí, com el camí 1, es pot "
                "aproximar per una escala de trams d’arc i trams radials; només els radials fan treball i la seva suma només "
                "depèn de r<sub>A</sub> i r<sub>B</sub>. Les circumferències discontínues són superfícies equipotencials; "
                "el camp g (verd) hi és perpendicular i apunta cap als potencials més baixos."),
}

BLOCKS = [
    dict(file=F, id="grav-camp-def", where=("end", "grav-s2"), html=r"""
<div class="box def"><div class="lead">Què és un camp?</div><dl>
<dt>Camp</dt><dd>Una regió de l’espai on cada punt té assignat el valor d’una magnitud física. Si la magnitud és un nombre (temperatura, pressió, potencial), el camp és <i>escalar</i>; si és un vector (velocitat del vent, $\vec g$, $\vec E$, $\vec B$), el camp és <i>vectorial</i>.</dd>
<dt>Camp de forces</dt><dd>Un camp vectorial que fa una força sobre els cossos que tenen la propietat adequada: massa (camp gravitatori) o càrrega (camp elèctric). La massa $M$ que crea el camp és la <i>font</i>; la massa $m$ que el detecta és la <i>massa de prova</i>, prou petita perquè no modifiqui el camp que volem mesurar. Així el camp és una propietat de l’espai que envolta $M$, tant si hi ha $m$ com si no.</dd>
<dt>Línies de camp</dt><dd>Línies tangents en cada punt al vector camp. Es dibuixen més juntes on el camp és més intens i no es poden tallar mai (en cada punt el camp té una sola direcció). Les línies del camp gravitatori acaben sempre en masses: la gravetat només atreu.</dd>
</dl></div>
<div class="box ex"><div class="lead">Exemple resolt: on s’anul·la el camp entre la Terra i la Lluna?</div>
<p>La distància Terra-Lluna és $D=3{,}84\cdot10^{8}$ m i $M_T=81\,M_L$. En un punt entre els dos astres a una distància $x$ del centre de la Terra, els dos camps tenen sentits contraris; el camp total és nul si tenen el mateix mòdul:</p>
$$G\frac{M_T}{x^2}=G\frac{M_L}{(D-x)^2}\;\Rightarrow\;\frac{x}{D-x}=\sqrt{\frac{M_T}{M_L}}=9\;\Rightarrow\;x=\frac{9}{10}D=3{,}46\cdot10^{8}\ \text{m}$$
<p>(Hem pres l’arrel positiva perquè el punt és entre els dos astres.) El punt és molt més a prop de la Lluna, que té menys massa.</p></div>
<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: el camp a l’interior d’un planeta</div>
<p>A l’interior d’una esfera homogènia, a una distància $r<R$ del centre, només contribueix al camp la massa de l’esfera interior de radi $r$, $M(r)=M\,r^3/R^3$; l’atracció de la capa exterior s’anul·la. Aleshores $g(r)=G\,M(r)/r^2=g_0\,r/R$: el camp creix linealment des de zero al centre fins a $g_0$ a la superfície, i a partir d’aquí disminueix com $1/r^2$.</p></div>
"""),
    dict(file=F, id="grav-treball", where=("start", "grav-s3"), html=r"""
<h4 class="amp">Treball de la força gravitatòria: per què és conservativa</h4>
<p>Recordem les definicions de l’apartat 1.5: el treball d’una força és $W=\int_A^B\vec F\cdot d\vec r$ (la suma de $\vec F\cdot\Delta\vec r$ en trams petits); una força és <b>conservativa</b> si aquest treball només depèn dels punts inicial i final; i, en aquest cas, es pot definir una <b>energia potencial</b>, una <b>funció d’estat</b> tal que $W_{A\to B}=-\Delta E_p$.</p>
<div class="box dem"><div class="lead">Demostració: la força gravitatòria és conservativa</div>
<p><span class="pp">Punt de partida</span> la definició de treball com a suma dels treballs de trams petits, $W=\sum\vec F\cdot\Delta\vec r$, i el fet que la força gravitatòria és <i>central</i>: sempre té la direcció de la recta que uneix $m$ amb el centre de $M$, i el seu mòdul només depèn de la distància $r$.</p>
<p>Situació: una massa $m$ va d’un punt $A$ (a distància $r_A$ de $M$) a un punt $B$ (a distància $r_B$) per un camí qualsevol (figura 4.5).</p>
<p>Pas 1. Aproximem el camí per una escala de trams molt petits de dos tipus: arcs de circumferència centrats en $M$ i trams radials.</p>
<p>Pas 2. En un arc el desplaçament és perpendicular a la força ($\alpha=90°$, $\cos\alpha=0$): el treball és zero.</p>
<p>Pas 3. En un tram radial la força i el desplaçament tenen la mateixa direcció; el treball només depèn de les distàncies inicial i final del tram. Sumant tots els trams radials passem de $r_A$ a $r_B$, sigui quin sigui el camí.</p>
<div class="box res"><div class="lead">Resultat</div>
<p>El treball de la força gravitatòria només depèn de $r_A$ i $r_B$: la força és conservativa. El càlcul (vegeu el requadre «Per ampliar») dona</p>
$$W_{A\to B}=GMm\left(\frac{1}{r_B}-\frac{1}{r_A}\right)=-\left[\left(-\frac{GMm}{r_B}\right)-\left(-\frac{GMm}{r_A}\right)\right]=-\Delta E_p$$</div>
<p>Comprovació del signe: si $m$ s’acosta a $M$ ($r_B<r_A$), $1/r_B>1/r_A$ i $W>0$, com ha de ser: la força atractiva té el mateix sentit que el moviment. En un camí tancat ($B=A$) el treball és zero.</p></div>
[[fig-4.5]]
<div class="box def"><div class="lead">Treball del camp i treball d’un agent extern</div>
<p>Si $m$ es mou <i>espontàniament</i> (només sota l’acció del camp), el camp fa un treball positiu, l’energia potencial disminueix i l’energia cinètica augmenta: $W_{\text{camp}}=-\Delta E_p=\Delta E_c$.</p>
<p>Per allunyar $m$ de $M$ cal un agent extern (un motor, una persona) que faci una força oposada al camp. Si ho fa a velocitat constant ($\Delta E_c=0$), el teorema de l’energia cinètica diu que $W_{\text{ext}}+W_{\text{camp}}=0$, és a dir:</p>
$$W_{\text{ext}}=-W_{\text{camp}}=\Delta E_p$$
<p>L’energia potencial en un punt és, doncs, el treball que hauria de fer un agent extern per portar $m$ des de l’origen d’energia potencial (l’infinit) fins a aquell punt sense accelerar-la. Com que la gravetat atreu, aquest treball és negatiu: per això $E_p<0$.</p></div>
<div class="box rec"><div class="lead">Recorda</div>
<p>Només té sentit parlar del treball <i>fet per una força</i> durant un desplaçament. L’energia potencial no és «de la massa $m$», sinó del <i>sistema</i> format per $M$ i $m$, i és una funció d’estat: només depèn de la distància $r$ entre les dues masses.</p></div>
"""),
    dict(file=F, id="grav-potencial", where=("before", "<p>Prop de la superfície"), html=r"""
<div class="box def"><div class="lead">Potencial, diferència de potencial i superfícies equipotencials</div><dl>
<dt>Potencial gravitatori</dt><dd>En un punt, l’energia potencial per unitat de massa que tindria una massa de prova situada en aquell punt: $V=E_p/m$. És una propietat del punt (no depèn de $m$), una magnitud escalar i una funció d’estat. Unitat: $\mathrm{J\cdot kg^{-1}}$.</dd>
<dt>Treball i diferència de potencial</dt><dd>$W_{A\to B}=-m\,(V_B-V_A)$. Una massa abandonada es mou espontàniament cap als punts de potencial <i>més baix</i> (més negatiu), és a dir, cap a la massa que crea el camp.</dd>
<dt>Superfície equipotencial</dt><dd>Conjunt de punts amb el mateix potencial. Per a una massa puntual o esfèrica són esferes concèntriques. Moure una massa per sobre d’una equipotencial no requereix treball ($\Delta V=0$); per això les línies de camp són sempre perpendiculars a les superfícies equipotencials.</dd>
<dt>Relació entre camp i potencial</dt><dd>El camp apunta cap als potencials decreixents, i el seu mòdul és la rapidesa amb què canvia el potencial en aquesta direcció: $g_r=-\dfrac{dV}{dr}$. Comprovació: amb $V=-GM/r$, $\dfrac{dV}{dr}=\dfrac{GM}{r^2}$ i $g_r=-\dfrac{GM}{r^2}$ (el signe menys indica que $\vec g$ apunta cap a $M$).</dd>
</dl></div>
"""),
    dict(file=F, id="grav-mgh", where=("after", "<p>Prop de la superfície"), html=r"""
<div class="box dem"><div class="lead">Demostració: d’on surt $\Delta E_p\approx mgh$</div>
<p><span class="pp">Punt de partida</span> l’expressió general $E_p=-GMm/r$, que val a qualsevol distància del centre del planeta.</p>
<p>Situació: un cos de massa $m$ puja des de la superfície ($r=R$) fins a una altura $h$ ($r=R+h$).</p>
<p>Pas 1. Variació exacta d’energia potencial:</p>
$$\Delta E_p=-\frac{GMm}{R+h}+\frac{GMm}{R}=GMm\,\frac{(R+h)-R}{R\,(R+h)}=\frac{GMm\,h}{R\,(R+h)}$$
<p>Pas 2. Si $h\ll R$, $R+h\approx R$, i amb $GM=g_0R^2$:</p>
$$\Delta E_p\approx\frac{GMm\,h}{R^2}=m\,g_0\,h$$
<p>L’expressió $mgh$ és, doncs, una aproximació per a altures petites (suposa $g$ constant). Per a $h=1000$ km l’error ja és d’un 16 %: a la PAU, lluny de la superfície, cal fer servir sempre $-GMm/r$.</p></div>
"""),
    dict(file=F, id="grav-balancos", where=("end", "grav-s5"), html=r"""
<h4 class="amp">Balanços d’energia amb satèl·lits</h4>
<p>En una òrbita circular de radi $r$ l’energia cinètica, la potencial i la mecànica estan lligades:</p>
$$E_c=\frac{GMm}{2r},\qquad E_p=-\frac{GMm}{r}=-2E_c,\qquad E_m=E_c+E_p=-\frac{GMm}{2r}=-E_c$$
<p>Totes tres són funcions d’estat: per a un satèl·lit donat, només depenen del radi de l’òrbita. Per això el treball que cal per passar d’un estat a un altre només depèn de l’estat inicial i del final. Si les úniques forces són la gravetat (conservativa) i la dels motors, l’apartat 1.5 dona $W_{\text{motors}}=W_{\text{nc}}=\Delta E_m$.</p>
<ul><li><b>Posar en òrbita</b> un satèl·lit llançat des de la superfície (negligint la rotació terrestre i el fregament de l’aire): $W=E_{m,\text{òrbita}}-E_{m,\text{superfície}}=-\dfrac{GMm}{2r}+\dfrac{GMm}{R}$.</li>
<li><b>Canviar d’òrbita</b> de $r_1$ a $r_2>r_1$: $W=\Delta E_m=\dfrac{GMm}{2}\left(\dfrac{1}{r_1}-\dfrac{1}{r_2}\right)>0$. Paradoxa aparent: hem donat energia al satèl·lit i, en canvi, a l’òrbita alta va més a poc a poc; l’energia cinètica disminueix, però la potencial augmenta el doble.</li>
<li><b>Escapar des d’una òrbita</b>: cal portar $E_m$ fins a zero, $W=\dfrac{GMm}{2r}$; la velocitat d’escapament des de l’òrbita és $\sqrt{2GM/r}=\sqrt2\,v_{\text{orb}}$.</li></ul>
<div class="box ex"><div class="lead">Exemple resolt: energia per posar un satèl·lit en òrbita</div>
<p>Un satèl·lit de $500$ kg s’ha de col·locar en una òrbita circular a $600$ km d’altura ($M_T=5{,}97\cdot10^{24}$ kg, $R_T=6{,}37\cdot10^{6}$ m). Radi de l’òrbita: $r=R_T+h=6{,}97\cdot10^{6}$ m, i $GM_Tm=1{,}99\cdot10^{17}\ \mathrm{J\cdot m}$.</p>
$$E_{m,\text{òrbita}}=-\frac{GM_Tm}{2r}=-1{,}43\cdot10^{10}\ \text{J},\qquad E_{m,\text{superfície}}=-\frac{GM_Tm}{R_T}=-3{,}13\cdot10^{10}\ \text{J}$$
$$W=\Delta E_m=-1{,}43\cdot10^{10}-(-3{,}13\cdot10^{10})=1{,}70\cdot10^{10}\ \text{J}$$
<p>Velocitat orbital: $v=\sqrt{GM_T/r}=7{,}56\cdot10^{3}\ \mathrm{m\cdot s^{-1}}$.</p></div>
<div class="box rec"><div class="lead">Recorda: per què els astronautes «floten»?</div>
<p>A l’Estació Espacial Internacional (a uns 400 km d’altura) el camp gravitatori val $g=g_0\,R^2/(R+h)^2\approx8{,}7\ \mathrm{m\cdot s^{-2}}$, gairebé el mateix que a terra. No floten perquè no hi hagi gravetat, sinó perquè l’estació i els astronautes cauen junts, amb la mateixa acceleració (la gravetat fa de força centrípeta): és una caiguda lliure contínua (imponderabilitat).</p></div>
"""),
    dict(file=F, id="grav-central", where=("before", '<div class="box dem"><div class="lead">Demostració: relació entre les velocitats al periheli'), html=r"""
<div class="box def"><div class="lead">Força central, moment d’una força i conservació del moment angular</div><dl>
<dt>Força central</dt><dd>Força dirigida en tot moment cap a un punt fix (el centre) o des d’ell. La força gravitatòria que fa el Sol sobre un planeta és central.</dd>
<dt>Moment d’una força respecte d’un punt O</dt><dd>$\vec M_O=\vec r\times\vec F$, on $\vec r$ va d’O al punt d’aplicació; mòdul $M_O=rF\sin\alpha$. Mesura la capacitat de la força de fer girar el cos al voltant de O.</dd>
<dt>Teorema del moment angular</dt><dd>La variació del moment angular per unitat de temps és igual al moment de la força resultant: $\dfrac{d\vec L}{dt}=\vec M_O$. Si la força és central, $\vec r$ i $\vec F$ són paral·lels, $\sin\alpha=0$ i $\vec M_O=\vec 0$: el moment angular es conserva.</dd>
</dl>
<p>Atenció: es conserva el moment angular, no la velocitat. En una òrbita el·líptica la velocitat canvia (en mòdul i direcció), però el producte $r\,v\sin\alpha$ es manté constant.</p></div>
"""),
]
