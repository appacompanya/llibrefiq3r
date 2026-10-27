"""Tema 3. Fenòmens ondulatoris: principi de Huygens i llei de Snell, coherència, ones estacionàries vs viatgeres."""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _svg import Svg, INK, GREY, RED, BLUE, GREEN

F = "fenomens-ondulatoris"


def fig_38():
    s = Svg(700, 400)
    y0 = 215
    s.items.append(f'<rect x="20" y="{y0}" width="660" height="175" fill="#e8f0fb"/>')
    s.line(20, y0, 680, y0, INK, 1.6)
    s.text(660, y0 - 10, "medi 1 (v₁)", 12, "end", GREY)
    s.text(660, y0 + 22, "medi 2 (v₂ &lt; v₁)", 12, "end", GREY)
    t1, AD = math.radians(40), 300
    v1t = AD * math.sin(t1)
    sin2 = v1t * (2 / 3) / AD
    t2 = math.asin(sin2)
    v2t = AD * sin2
    A = (180, y0)
    D = (A[0] + AD, y0)
    ux, uy = math.sin(t1), math.cos(t1)
    C = (D[0] - v1t * ux, y0 - v1t * uy)
    E = (A[0] + v2t * math.sin(t2), y0 + v2t * math.cos(t2))
    # raigs incidents
    for P, L in ((A, 110), (C, 50)):
        s.arrow(P[0] - L * ux, P[1] - L * uy, P[0] - 6 * ux, P[1] - 6 * uy, RED, 1.6, 9)
    s.line(C[0], C[1], D[0], D[1], RED, 1.6, "5 4")
    # front incident
    s.line(A[0], A[1], C[0], C[1], BLUE, 2.4)
    s.text((A[0] + C[0]) / 2 - 10, (A[1] + C[1]) / 2 - 8, "front incident", 12, "end", BLUE)
    # ondeta d'A
    ang = [math.radians(a) for a in range(0, 181, 3)]
    s.poly([(A[0] + v2t * math.cos(a), y0 + v2t * math.sin(a)) for a in ang], GREEN, 1.2, dash="4 4")
    # front refractat
    s.line(D[0], D[1], E[0], E[1], BLUE, 2.4)
    s.text((D[0] + E[0]) / 2 + 12, (D[1] + E[1]) / 2 + 22, "front refractat", 12, "start", BLUE)
    s.line(A[0], A[1], E[0], E[1], RED, 1.6, "5 4")
    vx, vy = math.sin(t2), math.cos(t2)
    s.arrow(E[0], E[1], E[0] + 60 * vx, E[1] + 60 * vy, RED, 1.6, 9)
    s.arrow(D[0], D[1], D[0] + 90 * vx, D[1] + 90 * vy, RED, 1.6, 9)
    # normals
    for P in (A, D):
        s.line(P[0], P[1] - 110, P[0], P[1] + 110, GREY, 1, "3 4")
    for P, lab, dx, dy in [(A, "A", -14, 18), (C, "C", 16, 4), (D, "D", 10, -8), (E, "E", -14, 14)]:
        s.circle(P[0], P[1], 3.5, INK, INK)
        s.text(P[0] + dx, P[1] + dy, lab, 14, "middle", INK, True)
    s.text((C[0] + D[0]) / 2 + 30, (C[1] + D[1]) / 2, "v₁·t", 13, "start", RED, True)
    s.text((A[0] + E[0]) / 2 - 12, (A[1] + E[1]) / 2 + 6, "v₂·t", 13, "end", RED, True)
    s.text(A[0] + 46, y0 - 10, "θ₁", 13, "middle", INK, True)
    s.text(D[0] - 48, y0 + 18, "θ₂", 13, "middle", INK, True)
    return s.svg()


FIGS = {
    "fig-3.8": (fig_38(), "Deducció de la llei de Snell amb el principi de Huygens (θ₁ = 40°, v₂ = ⅔·v₁). Mentre el front incident AC "
                "avança v₁·t fins que l’extrem C arriba a D, l’ondeta secundària emesa per A s’expandeix v₂·t dins el medi 2 "
                "(arc verd). El nou front DE és tangent a aquesta ondeta. Els triangles rectangles ACD i AED comparteixen la "
                "hipotenusa AD; l’angle del front amb la superfície és igual a l’angle del raig amb la normal."),
}

BLOCKS = [
    dict(file=F, id="fen-huygens", where=("before", "<p>Reflexió total:"), html=r"""
<div class="box def"><div class="lead">Principi de Huygens</div>
<p>Cada punt d’un front d’ona es comporta com un focus d’ones secundàries (ondetes) que es propaguen en totes direccions amb la velocitat de l’ona en aquell medi. El nou front d’ona, un temps $t$ després, és la superfície tangent (l’envolupant) a totes aquestes ondetes. Amb aquest principi geomètric s’expliquen la reflexió, la refracció i la difracció.</p></div>
<div class="box dem"><div class="lead">Demostració: llei de Snell a partir del principi de Huygens</div>
<p><span class="pp">Punt de partida</span> el principi de Huygens i el fet que, en cada medi, l’ona avança amb la seva velocitat ($v_1$ al medi 1, $v_2$ al medi 2).</p>
<p>Situació: un front d’ona pla AC arriba obliquament a la superfície de separació (figura 3.8). L’extrem A ja hi ha arribat; a l’extrem C li falta recórrer la distància CD.</p>
<p>Pas 1. En el temps $t$ que C triga a arribar a D, recorre $CD=v_1t$. Durant aquest temps, l’ondeta que surt d’A dins el medi 2 té un radi $AE=v_2t$, i el nou front d’ona és DE, tangent a l’ondeta.</p>
<p>Pas 2. Al triangle rectangle ACD (recte a C), l’angle a A és $\theta_1$ (el front forma amb la superfície el mateix angle que el raig amb la normal): $\sin\theta_1=\dfrac{CD}{AD}=\dfrac{v_1t}{AD}$.</p>
<p>Pas 3. Al triangle rectangle AED (recte a E), l’angle a D és $\theta_2$: $\sin\theta_2=\dfrac{AE}{AD}=\dfrac{v_2t}{AD}$.</p>
<p>Pas 4. Dividim les dues expressions; $t$ i $AD$ se simplifiquen:</p>
<div class="box res"><div class="lead">Resultat</div>
$$\frac{\sin\theta_1}{\sin\theta_2}=\frac{v_1}{v_2}=\frac{n_2}{n_1}\quad\Longleftrightarrow\quad n_1\sin\theta_1=n_2\sin\theta_2$$</div>
<p>(Hem fet servir $n=c/v$.) Si $v_2<v_1$, $\theta_2<\theta_1$: el raig s’acosta a la normal. Amb el mateix raonament, si l’ondeta es propaga en el mateix medi (reflexió), $AE=CD$ i els dos angles són iguals: llei de la reflexió.</p></div>
[[fig-3.8]]
"""),
    dict(file=F, id="fen-coherencia", where=("before", "<p>Si les dues ones tenen la mateixa amplitud"), html=r"""
<div class="box def"><div class="lead">Fonts coherents i diferència de camins</div><dl>
<dt>Fonts coherents</dt><dd>Fonts que emeten ones de la mateixa freqüència amb una diferència de fase constant en el temps. Només amb fonts coherents el patró d’interferència és estable (no canvia d’un instant a l’altre). Dues bombetes no són coherents; dos altaveus connectats al mateix generador sí que ho són.</dd>
<dt>Per què compta la diferència de camins</dt><dd>Si les fonts són en fase, l’ona que ha recorregut $r_1$ arriba a P amb fase $\omega t-kr_1$ i la que ha recorregut $r_2$, amb fase $\omega t-kr_2$. El desfasament a P és $\Delta\varphi=k\,|r_1-r_2|=\dfrac{2\pi}{\lambda}|r_1-r_2|$: interferència constructiva si $\Delta\varphi=2\pi n$ (és a dir, $|r_1-r_2|=n\lambda$) i destructiva si $\Delta\varphi=(2n+1)\pi$ (és a dir, $|r_1-r_2|=(2n+1)\lambda/2$).</dd>
</dl></div>
"""),
    dict(file=F, id="fen-estac", where=("before", "<p>Corda fixa pels dos extrems"), html=r"""
<table class="amp-tab"><thead><tr><th></th><th>Ona viatgera (harmònica)</th><th>Ona estacionària</th></tr></thead><tbody>
<tr><td>Propagació</td><td>Avança amb velocitat $v$</td><td>No avança: el perfil oscil·la sense desplaçar-se</td></tr>
<tr><td>Energia</td><td>La transporta en el sentit de propagació</td><td>No hi ha transport net: l’energia queda confinada entre nodes</td></tr>
<tr><td>Amplitud de cada punt</td><td>La mateixa, $A$, per a tots els punts</td><td>Depèn de la posició: $2A\,|\sin kx|$ (0 als nodes, $2A$ als ventres)</td></tr>
<tr><td>Fase de cada punt</td><td>Varia contínuament amb $x$ ($kx$)</td><td>Tots els punts entre dos nodes consecutius vibren en fase; a banda i banda d’un node, en oposició de fase</td></tr>
<tr><td>Freqüències possibles</td><td>Qualsevol</td><td>Només les compatibles amb les condicions als extrems (modes normals)</td></tr>
</tbody></table>
"""),
]

BLOCKS += [
    dict(file=F, id="fen-interf-dem", where=("replace", '<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: deducció de l’amplitud resultant</div>'), html=r"""
<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: deducció de l’amplitud resultant</div>
<p>Hipòtesis: dues fonts en fase emeten ones de la mateixa amplitud $A$ i la mateixa freqüència. Al punt P, a distàncies $r_1$ i $r_2$ de les fonts, arriben les ones</p>
$$y_1=A\sin(\omega t-kr_1),\qquad y_2=A\sin(\omega t-kr_2)$$
<div class="box rec"><div class="lead">Recorda</div>
<p>Suma de sinus (1r de Batxillerat): $\sin a+\sin b=2\sin\dfrac{a+b}{2}\cos\dfrac{a-b}{2}$.</p></div>
<p>Pas 1. Pel principi de superposició, la pertorbació a P és la suma: $y=y_1+y_2=A\left[\sin(\omega t-kr_1)+\sin(\omega t-kr_2)\right]$.</p>
<p>Pas 2. Apliquem la suma de sinus amb $a=\omega t-kr_1$ i $b=\omega t-kr_2$:</p>
$$\frac{a+b}{2}=\omega t-k\,\frac{r_1+r_2}{2},\qquad \frac{a-b}{2}=\frac{k\,(r_2-r_1)}{2}$$
$$y=\underbrace{2A\cos\frac{k\,(r_2-r_1)}{2}}_{\text{no depèn de }t}\;\sin\!\left(\omega t-k\,\frac{r_1+r_2}{2}\right)$$
<p>Pas 3. Interpretació. Per a un punt P concret, $r_1$ i $r_2$ són fixos: el primer factor és un nombre constant, i el segon és un sinus que oscil·la entre $-1$ i $1$. Per tant P fa un MHS de pulsació $\omega$, i la seva amplitud és el valor absolut d’aquest nombre (una amplitud sempre és positiva).</p>
<div class="box res"><div class="lead">Resultat</div>
$$A_R=\left|\,2A\cos\frac{\pi\,(r_2-r_1)}{\lambda}\,\right|\qquad\left(\text{amb }k=\frac{2\pi}{\lambda}\right)$$</div>
<p>Pas 4. Màxims i mínims.</p>
<ul><li><b>Màxim</b> ($A_R=2A$) quan $\left|\cos\dfrac{\pi(r_2-r_1)}{\lambda}\right|=1$, és a dir, quan l’argument és un múltiple de $\pi$: $\dfrac{\pi|r_1-r_2|}{\lambda}=n\pi\;\Rightarrow\;|r_1-r_2|=n\lambda$.</li>
<li><b>Mínim</b> ($A_R=0$) quan el cosinus val zero, és a dir, quan l’argument és un múltiple senar de $\pi/2$: $\dfrac{\pi|r_1-r_2|}{\lambda}=(2n+1)\dfrac{\pi}{2}\;\Rightarrow\;|r_1-r_2|=(2n+1)\dfrac{\lambda}{2}$.</li></ul>
<p>Són les condicions d’interferència constructiva i destructiva del text ($n\in\mathbb N$).</p></div>
"""),
    dict(file=F, id="fen-estac-dem", where=("replace", '<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: expressió de l’ona estacionària</div>'), html=r"""
<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: expressió de l’ona estacionària</div>
<p>Hipòtesis: una ona $y_1=A\sin(\omega t-kx)$ avança cap a les $x$ positives i es reflecteix en un extrem fix situat a $x=0$. En reflectir-se s’inverteix (canvia de signe) i torna cap a les $x$ negatives amb la mateixa amplitud:</p>
$$y_1=A\sin(\omega t-kx),\qquad y_2=-A\sin(\omega t+kx)$$
<div class="box rec"><div class="lead">Recorda</div>
<p>Diferència de sinus: $\sin a-\sin b=2\cos\dfrac{a+b}{2}\sin\dfrac{a-b}{2}$. A més, $\sin(-\alpha)=-\sin\alpha$.</p></div>
<p>Pas 1. Pel principi de superposició, cada punt de la corda té un desplaçament $y=y_1+y_2=A\left[\sin(\omega t-kx)-\sin(\omega t+kx)\right]$.</p>
<p>Pas 2. Apliquem la diferència de sinus amb $a=\omega t-kx$ i $b=\omega t+kx$:</p>
$$\frac{a+b}{2}=\frac{2\omega t}{2}=\omega t,\qquad \frac{a-b}{2}=\frac{-2kx}{2}=-kx$$
$$y=2A\cos(\omega t)\,\sin(-kx)=-2A\sin(kx)\cos(\omega t)$$
<p>Pas 3. Interpretació. Fixem-nos en un punt concret de la corda (una $x$ fixa). El factor $-2A\sin(kx)$ és aleshores un nombre constant, i $\cos(\omega t)$ oscil·la entre $-1$ i $1$. Per tant, cada punt fa un MHS de pulsació $\omega$ amb una amplitud igual al valor absolut d’aquell nombre (una amplitud sempre és positiva):</p>
<div class="box res"><div class="lead">Resultat</div>
$$y(x,t)=-2A\sin(kx)\cos(\omega t)\qquad\Rightarrow\qquad A(x)=\left|\,2A\sin(kx)\,\right|$$</div>
<p>A diferència d’una ona viatgera, la posició i el temps apareixen en factors separats (no hi ha cap combinació $\omega t\pm kx$): la forma de l’ona no avança, només canvia d’amplitud de punt a punt.</p>
<p>Pas 4. Nodes i ventres (amb $k=2\pi/\lambda$, de manera que $x=\dfrac{kx}{k}=\dfrac{\lambda}{2\pi}\,kx$):</p>
<ul><li><b>Nodes</b> (no vibren, $A(x)=0$): $\sin(kx)=0\;\Rightarrow\;kx=n\pi\;\Rightarrow\;x=n\dfrac{\lambda}{2}$.</li>
<li><b>Ventres</b> (amplitud màxima, $A(x)=2A$): $|\sin(kx)|=1\;\Rightarrow\;kx=(2n+1)\dfrac{\pi}{2}\;\Rightarrow\;x=(2n+1)\dfrac{\lambda}{4}$.</li></ul>
<p>Amb $n\in\mathbb N$. L’extrem fix ($x=0$) és un node, com havia de ser.</p></div>
"""),
]
