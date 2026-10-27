"""Tema 1. Moviment harmònic simple: definicions, condicions inicials, molla vertical i conceptes d'energia."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _svg import Svg, INK, GREY, RED, BLUE, GREEN

F = "mhs"


def fig_15():
    s = Svg(700, 330)
    ox, oy, sx, sy = 120, 165, 80, 22  # x en unitats arbitràries (-1..5), F = -k x amb k=1 -> eix F
    s.line(40, oy, 670, oy, GREY, 1)
    s.arrow(40, oy, 672, oy, GREY, 1, 8)
    s.arrow(ox, 315, ox, 22, GREY, 1, 8)
    s.text(675, oy - 8, "x", 14, "end", INK, True)
    s.text(ox + 8, 30, "F", 14, "start", INK, True)
    X = lambda x: ox + x * sx
    Y = lambda Fv: oy - Fv * sy
    xa, xb = 2.0, 5.0
    s.polygon([(X(xa), oy), (X(xa), Y(-xa)), (X(xb), Y(-xb)), (X(xb), oy)], RED, op=0.18)
    s.line(X(-0.6), Y(0.6), X(6.1), Y(-6.1), INK, 2.4)
    s.text(X(5.4), Y(-5.4) + 26, "F = −k·x", 13, "start", INK)
    for x, lab in [(xa, "x<tspan dy='4' font-size='10'>A</tspan>"), (xb, "x<tspan dy='4' font-size='10'>B</tspan>")]:
        s.line(X(x), oy - 5, X(x), oy + 5, INK, 1.4)
        s.line(X(x), oy, X(x), Y(-x), INK, 1, "4 4")
        s.text(X(x), oy - 12, lab, 13, "middle", INK, True)
        s.line(ox - 5, Y(-x), X(x), Y(-x), GREY, 1, "3 4")
    s.text(ox - 8, Y(-xa) + 4, "−k·x<tspan dy='4' font-size='10'>A</tspan>", 12, "end", INK)
    s.text(ox - 8, Y(-xb) + 4, "−k·x<tspan dy='4' font-size='10'>B</tspan>", 12, "end", INK)
    s.text(X(3.5), Y(-1.9), "àrea = W", 13, "middle", RED, bold=True)
    s.text(X(3.5), Y(-1.9) + 17, "(negativa: sota l’eix)", 11, "middle", RED)
    sub = lambda t: f"<tspan dy='4' font-size='9'>{t}</tspan><tspan dy='-4'>"
    s.text(30, 322, f"W(A→B) = −(k·x{sub('A')} + k·x</tspan>{sub('B')})/2 · (x</tspan>{sub('B')} − x</tspan>{sub('A')}) = −(½·k·x</tspan>{sub('B')}² − ½·k·x</tspan>{sub('A')}²)</tspan>", 12, "start", GREY)
    return s.svg()


FIGS = {
    "fig-1.5": (fig_15(), "Treball de la força elàstica quan l’extrem de la molla passa de x<sub>A</sub> a x<sub>B</sub>. "
                "La força és F = −k·x (recta de pendent −k); el treball és l’àrea (amb signe) entre la gràfica i l’eix x, "
                "un trapezi. Com que només depèn de x<sub>A</sub> i x<sub>B</sub>, la força elàstica és conservativa i "
                "E<sub>p</sub> = ½·k·x²."),
}

BLOCKS = [
    dict(file=F, id="mhs-def", where=("before", '<figure id="fig-1.1"'), html=r"""
<div class="box def"><div class="lead">Definicions</div><dl>
<dt>Moviment periòdic</dt><dd>Moviment que es repeteix idènticament (posició, velocitat i acceleració) cada cert interval de temps $T$, el període: $x(t+T)=x(t)$ per a qualsevol instant $t$. Exemples: un moviment circular uniforme, la rotació de la Terra.</dd>
<dt>Moviment oscil·latori o vibratori</dt><dd>Moviment d’anada i tornada a banda i banda d’una posició d’equilibri, sobre la mateixa trajectòria. Pot ser periòdic o no: si hi ha fregament, l’amplitud va disminuint (oscil·lació esmorteïda).</dd>
<dt>Posició d’equilibri</dt><dd>Posició en què la força resultant sobre el cos és nul·la. L’equilibri és <i>estable</i> si, quan separem una mica el cos, apareix una força que el torna cap a aquesta posició: una <i>força recuperadora</i>.</dd>
<dt>Moviment harmònic simple (MHS)</dt><dd>Moviment oscil·latori en una dimensió en què l’acceleració és proporcional a l’elongació i de sentit contrari, $a=-\omega^2x$, amb $\omega$ constant. Dinàmicament és el mateix que dir que la força resultant és recuperadora i <i>lineal</i>: $F=-kx$, amb $k=m\omega^2$. Tot MHS és periòdic, però no tot moviment periòdic és un MHS (el moviment circular uniforme és periòdic i no és oscil·latori).</dd>
</dl></div>
<p>Per què és tan important el MHS? Prop d’una posició d’equilibri estable, qualsevol força recuperadora es pot aproximar per una força proporcional al desplaçament (com quan aproximem una corba per la seva recta tangent). Per això les oscil·lacions <i>petites</i> de molts sistemes (una molla, un pèndol, els àtoms d’un sòlid, l’aire en un tub sonor) són, amb molt bona aproximació, harmòniques simples.</p>
"""),
    dict(file=F, id="mhs-ci", where=("after", '<div class="box ex"><div class="lead">Exemple resolt: Fase inicial</div>'), html=r"""
<h4 class="amp">Amplitud i fase inicial a partir de les condicions inicials</h4>
<p>Si coneixem la posició $x_0$ i la velocitat $v_0$ a $t=0$ i la pulsació $\omega$, podem trobar $A$ i $\varphi_0$ sense ambigüitat:</p>
<div class="box dem"><div class="lead">Demostració: $A$ i $\varphi_0$ a partir de $x_0$ i $v_0$</div>
<p><span class="pp">Punt de partida</span> les equacions de la posició i de la velocitat del MHS avaluades a $t=0$.</p>
<p>Pas 1. A $t=0$: $\;x_0=A\sin\varphi_0\;$ i $\;v_0=A\omega\cos\varphi_0$, és a dir, $\dfrac{v_0}{\omega}=A\cos\varphi_0$.</p>
<p>Pas 2. Elevem al quadrat i sumem; amb $\sin^2\varphi_0+\cos^2\varphi_0=1$ desapareix l’angle:</p>
$$x_0^2+\left(\frac{v_0}{\omega}\right)^2=A^2\left(\sin^2\varphi_0+\cos^2\varphi_0\right)=A^2$$
<p>Pas 3. Dividim les dues equacions del pas 1 i desapareix l’amplitud: $\tan\varphi_0=\dfrac{\omega x_0}{v_0}$.</p>
<div class="box res"><div class="lead">Resultat</div>
$$A=\sqrt{x_0^2+\frac{v_0^2}{\omega^2}},\qquad \sin\varphi_0=\frac{x_0}{A},\qquad \cos\varphi_0=\frac{v_0}{A\omega}$$
</div>
<p>La tangent sola no n’hi ha prou (dos angles tenen la mateixa tangent): el quadrant de $\varphi_0$ el fixen els signes de $\sin\varphi_0$ (el de $x_0$) i de $\cos\varphi_0$ (el de $v_0$).</p></div>
<table class="amp-tab"><thead><tr><th>Situació a $t=0$ (amb $x=A\sin(\omega t+\varphi_0)$)</th><th>$x_0$</th><th>$v_0$</th><th>$\varphi_0$</th></tr></thead><tbody>
<tr><td>Passa per l’equilibri cap a $x$ positives</td><td>$0$</td><td>$+A\omega$</td><td>$0$</td></tr>
<tr><td>És a l’extrem positiu (es deixa anar des del repòs)</td><td>$+A$</td><td>$0$</td><td>$\pi/2$</td></tr>
<tr><td>Passa per l’equilibri cap a $x$ negatives</td><td>$0$</td><td>$-A\omega$</td><td>$\pi$</td></tr>
<tr><td>És a l’extrem negatiu</td><td>$-A$</td><td>$0$</td><td>$3\pi/2$ (o $-\pi/2$)</td></tr>
</tbody></table>
<div class="box def"><div class="lead">Diferència de fase</div>
<p>Dos MHS de la mateixa pulsació, $x_1=A_1\sin(\omega t+\varphi_1)$ i $x_2=A_2\sin(\omega t+\varphi_2)$, tenen una diferència de fase $\Delta\varphi=\varphi_2-\varphi_1$ constant. Si $\Delta\varphi=0$ (o $2\pi n$) estan <i>en fase</i>: arriben alhora als extrems. Si $\Delta\varphi=\pi$ (o $(2n+1)\pi$) estan <i>en oposició de fase</i>: quan un és a $+A$, l’altre és a $-A$. Si $\Delta\varphi=\pi/2$ estan <i>en quadratura</i>.</p>
<p>En el mateix MHS: la velocitat, $v=A\omega\cos(\omega t+\varphi_0)=A\omega\sin(\omega t+\varphi_0+\tfrac{\pi}{2})$, va avançada $\pi/2$ respecte de la posició, i l’acceleració, $a=-\omega^2x$, és en oposició de fase amb la posició.</p></div>
"""),
    dict(file=F, id="mhs-vert", where=("end", "mhs-s4"), html=r"""
<h4 class="amp">Molla vertical: el pes només desplaça l’equilibri</h4>
<div class="box dem"><div class="lead">Demostració: una massa penjada d’una molla vertical també fa un MHS</div>
<p><span class="pp">Punt de partida</span> la segona llei de Newton amb les dues forces que actuen sobre la massa: el pes $mg$ (cap avall) i la força de la molla, $k\cdot(\text{allargament})$ (cap amunt quan la molla està estirada).</p>
<p>Situació: una molla de constant $k$ i longitud natural $l_0$ penja verticalment; hi pengem una massa $m$. Prenem l’eix $y$ vertical i <i>positiu cap avall</i>.</p>
<p>Pas 1. Nova posició d’equilibri. En equilibri la força resultant és nul·la i la molla s’ha allargat $\Delta l$:</p>
$$k\,\Delta l=mg\quad\Rightarrow\quad \Delta l=\frac{mg}{k}$$
<p>Pas 2. Separem la massa una distància $y$ d’aquesta posició d’equilibri. Ara l’allargament és $\Delta l+y$ i la força resultant (positiva cap avall) és</p>
$$F=mg-k(\Delta l+y)=\underbrace{(mg-k\Delta l)}_{=\,0}-ky=-ky$$
<p>Pas 3. La força resultant és recuperadora i lineal respecte de la nova posició d’equilibri: és un MHS amb la mateixa constant $k$.</p>
<div class="box res"><div class="lead">Resultat</div>
$$\omega=\sqrt{\frac{k}{m}}=\sqrt{\frac{g}{\Delta l}},\qquad T=2\pi\sqrt{\frac{m}{k}}=2\pi\sqrt{\frac{\Delta l}{g}}$$
</div>
<p>El pes no canvia ni la pulsació ni el període: només desplaça el centre de l’oscil·lació. L’elongació s’ha de mesurar des de la posició d’equilibri <i>amb la massa penjada</i>, no des de la longitud natural de la molla.</p></div>
<div class="box ex"><div class="lead">Exemple resolt: constant d’una molla a partir de l’allargament</div>
<p>En penjar-hi $0{,}200$ kg, una molla s’allarga $4{,}90$ cm. Aleshores $k=\dfrac{mg}{\Delta l}=\dfrac{0{,}200\cdot 9{,}80}{0{,}0490}=40{,}0\ \mathrm{N\cdot m^{-1}}$ i, si la fem oscil·lar, $T=2\pi\sqrt{\dfrac{\Delta l}{g}}=2\pi\sqrt{\dfrac{0{,}0490}{9{,}80}}=0{,}444$ s.</p></div>
"""),
    dict(file=F, id="mhs-energia-concepts", where=("start", "mhs-s5"), html=r"""
<h4 class="amp">Conceptes previs: treball, forces conservatives i energia potencial</h4>
<p>Per estudiar l’energia d’un oscil·lador (i, més endavant, la dels camps gravitatori i elèctric) necessitem uns quants conceptes de mecànica definits amb precisió. Es fan servir a tot el llibre.</p>
<div class="box def"><div class="lead">Treball d’una força</div><dl>
<dt>Força constant i desplaçament rectilini</dt><dd>El treball $W$ que fa una força constant $\vec F$ sobre un cos que es desplaça $\Delta\vec r$ és el producte escalar
$$W=\vec F\cdot\Delta\vec r=F\,\Delta r\cos\alpha$$
on $\alpha$ és l’angle entre la força i el desplaçament. És una magnitud escalar; s’expressa en joules ($1\ \mathrm{J}=1\ \mathrm{N\cdot m}$). Només treballa la component de la força en la direcció del desplaçament, $F\cos\alpha$.</dd>
<dt>Signe del treball</dt><dd>Si $\alpha<90°$, $W>0$: la força afavoreix el moviment i hi aporta energia (força motriu). Si $\alpha=90°$, $W=0$: les forces perpendiculars al desplaçament no fan treball (la normal en un pla horitzontal, la força centrípeta en un moviment circular, la força magnètica). Si $\alpha>90°$, $W<0$: la força s’oposa al moviment i en treu energia (fregament).</dd>
<dt>Força variable o trajectòria corba</dt><dd>Dividim el camí en desplaçaments $\Delta\vec r_i$ tan petits que, en cadascun, la força sigui pràcticament constant, i sumem: $W_{A\to B}=\sum_i\vec F_i\cdot\Delta\vec r_i$. En el límit de trossos infinitament petits la suma és una integral, $W_{A\to B}=\int_A^B\vec F\cdot d\vec r$. En una dimensió, el treball és l’<i>àrea</i> (amb signe) compresa entre la gràfica $F(x)$ i l’eix $x$.</dd>
<dt>Treball total</dt><dd>Si actuen diverses forces, el treball total és la suma dels treballs de cadascuna, que és igual al treball de la força resultant.</dd>
</dl></div>
<div class="box res"><div class="lead">Teorema de l’energia cinètica</div>
$$W_{\text{total}}=\Delta E_c=\tfrac12mv_B^2-\tfrac12mv_A^2$$
<p>El treball de totes les forces que actuen sobre un cos és igual a la variació de la seva energia cinètica. Justificació per a una força resultant constant en una recta: $F\,\Delta x=ma\,\Delta x$ i, pel MRUA, $v_B^2-v_A^2=2a\,\Delta x$; per tant $F\,\Delta x=\tfrac12mv_B^2-\tfrac12mv_A^2$. El teorema val en general (forces variables, camins corbs).</p></div>
<div class="box def"><div class="lead">Forces conservatives i no conservatives</div>
<p>Una força és <b>conservativa</b> si el treball que fa sobre un cos que va d’un punt $A$ a un punt $B$ depèn només de $A$ i de $B$, i no del camí seguit. De manera equivalent: el treball que fa en <i>qualsevol camí tancat</i> és zero, $\oint\vec F\cdot d\vec r=0$. (Si anem de $A$ a $B$ pel camí 1 i tornem pel camí 2, $W=W_1-W_2=0$ perquè $W_1=W_2$.)</p>
<ul><li><b>Conservatives:</b> la força gravitatòria (i el pes), la força elàstica d’una molla ideal, la força elèctrica entre càrregues en repòs.</li>
<li><b>No conservatives:</b> el fregament i la resistència de l’aire (el seu treball és negatiu en qualsevol camí i, com més llarg és el camí, més energia dissipen: $W_{fr}=-\mu N\,L$), les forces que fan motors, músculs o cordes.</li>
<li>La <b>força magnètica</b> sobre una càrrega és sempre perpendicular a la velocitat i no fa mai treball.</li></ul></div>
<div class="box def"><div class="lead">Funció d’estat</div>
<p>Una magnitud és una <b>funció d’estat</b> si el seu valor depèn només de l’estat del sistema (posició, velocitat, temperatura…) i no de com s’hi ha arribat. Per això la seva variació entre dos estats, $\Delta X=X_B-X_A$, només depèn de l’estat inicial i del final.</p>
<ul><li>Són funcions d’estat: la posició, l’energia cinètica, l’energia potencial, l’energia mecànica, el potencial gravitatori i l’elèctric, l’energia interna.</li>
<li><b>No</b> ho són el treball i la calor: són energia <i>que es transfereix</i> durant un procés i depenen del procés. Un cos <i>té</i> energia, però no <i>té</i> treball. Tampoc no ho és la distància recorreguda.</li></ul>
<p>Analogia: l’altitud d’un cim és una funció d’estat (la diferència d’altitud entre el refugi i el cim no depèn del camí), però els quilòmetres que caminem per pujar-hi depenen del camí triat.</p></div>
<div class="box def"><div class="lead">Energia potencial</div>
<p>Només per a una força conservativa podem definir una funció d’estat, l’<b>energia potencial</b> $E_p$, tal que el treball de la força entre dos punts és igual a <i>menys</i> la variació d’energia potencial:</p>
$$W_{\text{cons},\,A\to B}=-\Delta E_p=E_p(A)-E_p(B)$$
<p>Si el treball depengués del camí, no podríem assignar un valor únic a $E_p(B)$: per això cal que la força sigui conservativa. Només les <i>diferències</i> d’energia potencial tenen sentit físic; l’origen (el punt on $E_p=0$) es tria per comoditat: la posició d’equilibri per a una molla, el terra per al pes a prop de la superfície, l’infinit per a la gravitació i per a la força elèctrica. Quan la força conservativa fa un treball positiu, l’energia potencial disminueix.</p></div>
<div class="box res"><div class="lead">Energia mecànica i forces no conservatives</div>
<p>Separem el treball total en el de les forces conservatives i el de les no conservatives, $W_{\text{total}}=W_{\text{cons}}+W_{\text{nc}}=\Delta E_c$, i substituïm $W_{\text{cons}}=-\Delta E_p$:</p>
$$W_{\text{nc}}=\Delta E_c+\Delta E_p=\Delta E_m,\qquad E_m=E_c+E_p$$
<p>Si només fan treball forces conservatives ($W_{\text{nc}}=0$), l’energia mecànica es conserva: $E_{m,A}=E_{m,B}$. Si hi ha fregament, $W_{\text{nc}}<0$ i l’energia mecànica disminueix: aquesta energia no desapareix, es transforma en energia interna (escalfament) del cos i de l’entorn.</p></div>
<h4 class="amp">Energia potencial elàstica</h4>
<div class="box dem"><div class="lead">Demostració: la força elàstica és conservativa i $E_p=\tfrac12kx^2$</div>
<p><span class="pp">Punt de partida</span> la llei de Hooke, $F=-kx$, i la definició de treball d’una força variable en una dimensió: l’àrea amb signe sota la gràfica $F(x)$.</p>
<p>Situació: l’extrem d’una molla ideal (o el bloc que hi va lligat) passa de l’elongació $x_A$ a l’elongació $x_B$ (figura 1.5).</p>
<p>Pas 1. La gràfica $F(x)=-kx$ és una recta. Entre $x_A$ i $x_B$ l’àrea és un trapezi d’altura $x_B-x_A$ i bases $-kx_A$ i $-kx_B$:</p>
$$W_{A\to B}=\frac{(-kx_A)+(-kx_B)}{2}\,(x_B-x_A)=-\frac{k}{2}\,(x_B+x_A)(x_B-x_A)$$
<p>Pas 2. Amb $(x_B+x_A)(x_B-x_A)=x_B^2-x_A^2$:</p>
$$W_{A\to B}=-\left(\tfrac12kx_B^2-\tfrac12kx_A^2\right)$$
<p>Pas 3. El treball només depèn de les posicions inicial i final: la força elàstica és conservativa. Comparant amb $W=-\Delta E_p$ i prenent $E_p=0$ a la posició d’equilibri ($x=0$):</p>
<div class="box res"><div class="lead">Resultat</div>
$$E_p=\tfrac12kx^2$$</div>
<p>L’energia potencial elàstica és sempre positiva o nul·la, tant si la molla està estirada ($x>0$) com comprimida ($x<0$).</p></div>
[[fig-1.5]]
"""),
    dict(file=F, id="mhs-energia-ex", where=("end", "mhs-s5"), html=r"""
<div class="box ex"><div class="lead">Exemple resolt: velocitat a partir de l’energia</div>
<p>Un bloc de $0{,}50$ kg oscil·la lligat a una molla de $k=200\ \mathrm{N\cdot m^{-1}}$ amb $A=0{,}10$ m. L’energia mecànica és $E_m=\tfrac12kA^2=\tfrac12\cdot200\cdot0{,}10^2=1{,}0$ J. A $x=0{,}060$ m: $E_p=\tfrac12\cdot200\cdot0{,}060^2=0{,}36$ J, per tant $E_c=1{,}0-0{,}36=0{,}64$ J i $v=\sqrt{2E_c/m}=\sqrt{2\cdot0{,}64/0{,}50}=1{,}6\ \mathrm{m\cdot s^{-1}}$. Comprovació: $v=\omega\sqrt{A^2-x^2}=20\sqrt{0{,}10^2-0{,}060^2}=1{,}6\ \mathrm{m\cdot s^{-1}}$.</p></div>
<p>Si hi ha fregament, la força de fregament fa un treball negatiu i l’energia mecànica disminueix a cada oscil·lació: l’amplitud es va reduint (oscil·lació esmorteïda) fins que el cos s’atura. El MHS ideal és el límit sense fregament.</p>
"""),
]
