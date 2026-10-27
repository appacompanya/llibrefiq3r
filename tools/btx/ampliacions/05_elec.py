"""Tema 5. Camp elèctric: càrrega, permitivitat, treball i potencial, camp uniforme, analogia amb la gravitació."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _svg import Svg, INK, GREY, RED, BLUE, GREEN

F = "camp-electric"


def fig_54():
    s = Svg(700, 330)
    x1, x2, y1, y2 = 150, 530, 40, 270
    s.items.append(f'<rect x="{x1-14}" y="{y1}" width="14" height="{y2-y1}" fill="#f3d6d4" stroke="{RED}" stroke-width="1.5"/>')
    s.items.append(f'<rect x="{x2}" y="{y1}" width="14" height="{y2-y1}" fill="#d6e2f5" stroke="{BLUE}" stroke-width="1.5"/>')
    for y in range(y1 + 18, y2, 34):
        s.text(x1 - 7, y + 5, "+", 14, "middle", RED, bold=True)
        s.text(x2 + 7, y + 5, "−", 14, "middle", BLUE, bold=True)
    for y in (80, 155, 230):
        s.arrow(x1 + 20, y, x2 - 20, y, INK, 1.8, 11)
    s.text((x1 + x1 + (x2 - x1) / 4) / 2, 70, "E", 15, "middle", INK, True, True)
    vals = ["100 V", "75 V", "50 V", "25 V", "0 V"]
    for i, v in enumerate(vals):
        x = x1 + (x2 - x1) * i / 4
        if 0 < i < 4:
            s.line(x, y1 + 6, x, y2 - 6, GREEN, 1.4, "6 5")
        s.text(x, y1 - 10, v, 12, "middle", GREEN, bold=True)
    s.arrow(x1, 300, x2, 300, GREY, 1.2, 8)
    s.arrow(x2, 300, x1, 300, GREY, 1.2, 8)
    s.text((x1 + x2) / 2, 318, "d", 14, "middle", INK, True)
    s.text(600, 120, "E = ΔV / d", 14, "start", INK, bold=True)
    s.text(600, 142, "V disminueix", 12, "start", GREY)
    s.text(600, 158, "en el sentit", 12, "start", GREY)
    s.text(600, 174, "del camp", 12, "start", GREY)
    s.text(40, 160, "placa +", 12, "middle", RED)
    s.text(40, 176, "V = 100 V", 12, "middle", RED)
    return s.svg()


FIGS = {
    "fig-5.4": (fig_54(), "Camp uniforme entre dues plaques paral·leles separades una distància d i amb una diferència de "
                "potencial ΔV = 100 V. Les línies de camp són paral·leles i equidistants i van de la placa positiva a la "
                "negativa; les superfícies equipotencials (verd) són plans paral·lels a les plaques, igualment espaiats: el "
                "potencial disminueix linealment en el sentit del camp, i E = ΔV/d."),
}

BLOCKS = [
    dict(file=F, id="elec-carrega", where=("before", '<div class="box dem"><div class="lead">Demostració: camp creat per una càrrega puntual'), html=r"""
<div class="box def"><div class="lead">La càrrega elèctrica i la constant de Coulomb</div><dl>
<dt>Càrrega elèctrica</dt><dd>Propietat de la matèria responsable de les interaccions elèctriques. N’hi ha de dos signes: les del mateix signe es repel·leixen i les de signe contrari s’atreuen. Unitat SI: el coulomb (C).</dd>
<dt>Quantització</dt><dd>Tota càrrega és un múltiple enter de la càrrega elemental, $q=n\,e$, amb $e=1{,}602\cdot10^{-19}$ C (la del protó; la de l’electró és $-e$).</dd>
<dt>Conservació</dt><dd>En un sistema aïllat la càrrega total es manté constant: la càrrega no es crea ni es destrueix, només es transfereix (per fregament, per contacte…).</dd>
<dt>Permitivitat</dt><dd>La constant de Coulomb s’escriu $k=\dfrac{1}{4\pi\varepsilon_0}$, on $\varepsilon_0=8{,}85\cdot10^{-12}\ \mathrm{C^2\cdot N^{-1}\cdot m^{-2}}$ és la permitivitat del buit. En un medi material (aigua, oli…) la força es divideix per la permitivitat relativa $\varepsilon_r\geq1$: $F=\dfrac{1}{4\pi\varepsilon_0\varepsilon_r}\dfrac{|Q||q|}{r^2}$. Si l’enunciat no diu res, el medi és el buit (o l’aire, gairebé igual).</dd>
<dt>Càrrega de prova</dt><dd>Càrrega <i>positiva</i> i prou petita perquè no modifiqui el camp que volem mesurar. Per conveni, el sentit del camp és el de la força sobre una càrrega positiva.</dd>
</dl></div>
"""),
    dict(file=F, id="elec-treball", where=("before", "<p>En un camp uniforme (entre plaques"), html=r"""
<h4 class="amp">Per què la força elèctrica és conservativa</h4>
<p>La força de Coulomb entre càrregues en repòs és central (dirigida segons la recta que uneix les càrregues) i el seu mòdul només depèn de la distància, com la gravitatòria. L’argument de l’apartat 4.3 (figura 4.5) val igual: en els trams d’arc la força és perpendicular al desplaçament i no fa treball, i en els trams radials el treball només depèn de les distàncies inicial i final. Per tant, $W_{A\to B}$ no depèn del camí, l’energia potencial $E_p=k\,Qq/r$ és una funció d’estat i el potencial també ho és.</p>
<div class="box def"><div class="lead">Interpretació de l’energia potencial i del potencial</div><dl>
<dt>Energia potencial d’un sistema de càrregues</dt><dd>És el treball que ha de fer un agent extern per portar les càrregues des de l’infinit (on $E_p=0$) fins a la seva posició, sense donar-los energia cinètica. Si les càrregues es repel·leixen ($Qq>0$) cal fer treball per acostar-les: $E_p>0$. Si s’atreuen, el camp ja «ajuda»: $E_p<0$.</dd>
<dt>Potencial en un punt</dt><dd>$V=E_p/q$: l’energia potencial per unitat de càrrega positiva situada en aquell punt. Només depèn de les càrregues que creen el camp i de la posició.</dd>
<dt>Diferència de potencial (tensió)</dt><dd>$\Delta V=V_B-V_A=-W_{A\to B}/q$. Un volt és la diferència de potencial entre dos punts quan el camp fa un treball de $-1$ J per portar $+1$ C de l’un a l’altre: $1\ \mathrm{V}=1\ \mathrm{J\cdot C^{-1}}$.</dd>
<dt>Electronvolt</dt><dd>Energia que guanya un electró (o qualsevol partícula de càrrega $e$) en ser accelerat per una diferència de potencial d’1 V: $1\ \mathrm{eV}=1{,}602\cdot10^{-19}$ J. És la unitat habitual en física atòmica i nuclear.</dd>
</dl></div>
<table class="amp-tab"><thead><tr><th>Càrrega que es mou lliurement (només sota la força elèctrica)</th><th>Cap a on va</th><th>$W_{\text{camp}}$</th><th>$\Delta E_p$</th><th>$\Delta E_c$</th></tr></thead><tbody>
<tr><td>Positiva ($q>0$)</td><td>Potencials decreixents ($\Delta V<0$), en el sentit del camp</td><td>$>0$</td><td>$<0$</td><td>$>0$</td></tr>
<tr><td>Negativa ($q<0$)</td><td>Potencials creixents ($\Delta V>0$), en sentit contrari al camp</td><td>$>0$</td><td>$<0$</td><td>$>0$</td></tr>
</tbody></table>
<p>En tots dos casos, si la càrrega es mou espontàniament la seva energia potencial disminueix. Per moure-la en sentit contrari cal un agent extern que faci un treball $W_{\text{ext}}=\Delta E_p=q\,\Delta V$ (a velocitat constant).</p>
<div class="box ex"><div class="lead">Exemple resolt: qui fa el treball?</div>
<p>Una càrrega $q=-2{,}0$ nC passa d’un punt A amb $V_A=300$ V a un punt B amb $V_B=-100$ V. Treball del camp: $W_{A\to B}=-q\,(V_B-V_A)=-(-2{,}0\cdot10^{-9})\cdot(-100-300)=-8{,}0\cdot10^{-7}$ J. És negatiu: una càrrega negativa no va espontàniament cap a potencials més baixos. Un agent extern ha de fer un treball de $+8{,}0\cdot10^{-7}$ J (si la càrrega no guanya energia cinètica), i l’energia potencial augmenta en aquesta quantitat.</p></div>
<div class="box ex"><div class="lead">Exemple resolt: energia electrostàtica d’un sistema de tres càrregues</div>
<p>$q_1=+2\ \mu$C a $(0,0)$, $q_2=-2\ \mu$C a $(3,0)$ m i $q_3=+1\ \mu$C a $(0,4)$ m. Es sumen les energies de cada parella, amb el signe de les càrregues (distàncies 3 m, 4 m i 5 m):</p>
$$E_p=k\left(\frac{q_1q_2}{r_{12}}+\frac{q_1q_3}{r_{13}}+\frac{q_2q_3}{r_{23}}\right)=9\cdot10^{9}\left(\frac{-4\cdot10^{-12}}{3}+\frac{2\cdot10^{-12}}{4}+\frac{-2\cdot10^{-12}}{5}\right)=-1{,}11\cdot10^{-2}\ \text{J}$$
<p>És negativa: per separar les tres càrregues fins a l’infinit caldria aportar $1{,}11\cdot10^{-2}$ J.</p></div>
"""),
    dict(file=F, id="elec-uniforme", where=("after", "<p>En un camp uniforme (entre plaques"), html=r"""
<div class="box dem"><div class="lead">Demostració: relació entre el camp i la diferència de potencial en un camp uniforme</div>
<p><span class="pp">Punt de partida</span> dues expressions del treball que fa el camp sobre una càrrega de prova $q>0$ que va d’una placa a l’altra: la definició de treball d’una força constant, $W=F\,d\cos0°$, i la relació amb el potencial, $W=-q\,\Delta V$.</p>
<p>Situació: dues plaques paral·leles separades una distància $d$, amb una diferència de potencial; entre elles el camp $\vec E$ és uniforme i perpendicular a les plaques (figura 5.4). La càrrega va de la placa positiva (A) a la negativa (B), en el sentit del camp.</p>
<p>Pas 1. La força $qE$ és constant i té el sentit del desplaçament: $W_{A\to B}=qE\,d$.</p>
<p>Pas 2. Igualem amb $W_{A\to B}=-q\,(V_B-V_A)$ i simplifiquem $q$:</p>
$$qE\,d=-q\,(V_B-V_A)\quad\Rightarrow\quad E=\frac{V_A-V_B}{d}$$
<div class="box res"><div class="lead">Resultat</div>
$$E=\frac{|\Delta V|}{d}\qquad(\text{el camp apunta cap als potencials decreixents})$$</div>
<p>Per això el camp elèctric també es pot expressar en $\mathrm{V\cdot m^{-1}}$ ($1\ \mathrm{V\cdot m^{-1}}=1\ \mathrm{N\cdot C^{-1}}$). En general, la component del camp en una direcció és menys la rapidesa amb què canvia el potencial en aquesta direcció: $E_x=-\dfrac{dV}{dx}$.</p></div>
[[fig-5.4]]
"""),
    dict(file=F, id="elec-analogia", where=("end", "elec-s3"), html=r"""
<h4 class="amp">Camp gravitatori i camp elèctric: analogies i diferències</h4>
<table class="amp-tab"><thead><tr><th></th><th>Camp gravitatori</th><th>Camp elèctric</th></tr></thead><tbody>
<tr><td>Font del camp</td><td>Massa (sempre positiva)</td><td>Càrrega (positiva o negativa)</td></tr>
<tr><td>Llei de força</td><td>$F=G\,\dfrac{Mm}{r^2}$, sempre atractiva</td><td>$F=k\,\dfrac{|Q||q|}{r^2}$, atractiva o repulsiva</td></tr>
<tr><td>Constant</td><td>$G=6{,}67\cdot10^{-11}$, universal (no depèn del medi)</td><td>$k=9{,}0\cdot10^{9}$ al buit; depèn del medi ($\varepsilon_r$)</td></tr>
<tr><td>Intensitat</td><td>$g=G\,M/r^2$ (cap a la massa)</td><td>$E=k\,|Q|/r^2$ (cap enfora si $Q>0$)</td></tr>
<tr><td>Energia potencial</td><td>$E_p=-G\,Mm/r$, sempre negativa</td><td>$E_p=k\,Qq/r$, de qualsevol signe</td></tr>
<tr><td>Potencial</td><td>$V=-G\,M/r$</td><td>$V=k\,Q/r$</td></tr>
<tr><td>Comú</td><td colspan="2">Forces centrals i conservatives, proporcionals a $1/r^2$; principi de superposició (vectorial per als camps, escalar per als potencials); $W=-\Delta E_p$; línies de camp perpendiculars a les equipotencials.</td></tr>
<tr><td>Intensitat relativa</td><td colspan="2">Entre dos protons, la força elèctrica és uns $10^{36}$ vegades la gravitatòria. A escala atòmica la gravetat és negligible; a escala astronòmica domina perquè la matèria és neutra en conjunt.</td></tr>
</tbody></table>
<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: conductors en equilibri</div>
<p>En un conductor en equilibri electrostàtic les càrregues lliures no es mouen: el camp a l’interior és zero, tot el conductor té el mateix potencial i la càrrega neta es distribueix per la superfície. Per això l’interior d’una caixa metàl·lica queda protegit dels camps exteriors (gàbia de Faraday), i per això un cotxe és un bon refugi durant una tempesta elèctrica.</p></div>
"""),
    dict(file=F, id="elec-deflexio", where=("after", '<div class="box ex"><div class="lead">Exemple resolt: Electró accelerat</div>'), html=r"""
<div class="box ex"><div class="lead">Exemple resolt: desviació d’un electró entre dues plaques</div>
<p>Un electró entra amb $v_0=2{,}0\cdot10^{7}\ \mathrm{m\cdot s^{-1}}$, perpendicularment al camp, entre dues plaques de $L=5{,}0$ cm on $E=2{,}0\cdot10^{3}\ \mathrm{N\cdot C^{-1}}$ ($m_e=9{,}11\cdot10^{-31}$ kg).</p>
<p>Força i acceleració (perpendiculars a $\vec v_0$, en sentit contrari al camp perquè la càrrega és negativa): $a=\dfrac{eE}{m_e}=\dfrac{1{,}602\cdot10^{-19}\cdot2{,}0\cdot10^{3}}{9{,}11\cdot10^{-31}}=3{,}52\cdot10^{14}\ \mathrm{m\cdot s^{-2}}$.</p>
<p>Temps entre les plaques (MRU en la direcció de $\vec v_0$): $t=L/v_0=2{,}5\cdot10^{-9}$ s. Desviació (MRUA): $y=\tfrac12at^2=1{,}1\cdot10^{-3}$ m. Velocitat transversal a la sortida: $v_y=at=8{,}8\cdot10^{5}\ \mathrm{m\cdot s^{-1}}$; angle de desviació: $\tan\theta=v_y/v_0$, $\theta=2{,}5°$.</p>
<p>Per què no tenim en compte el pes? $m_eg=8{,}9\cdot10^{-30}$ N, mentre que $eE=3{,}2\cdot10^{-16}$ N: el pes és unes $10^{13}$ vegades més petit.</p></div>
"""),
]
