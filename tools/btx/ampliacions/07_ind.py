"""Tema 7. Inducció: FEM, signe del flux, Lenz i conservació de l'energia, balanç d'energia de la barra, transformador i transport."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _svg import Svg, INK, GREY, RED, BLUE, GREEN, ORANGE

F = "induccio"


def fig_73():
    s = Svg(700, 310)
    # imant
    s.items.append(f'<rect x="60" y="125" width="90" height="50" fill="#d6e2f5" stroke="{INK}" stroke-width="1.5"/>')
    s.items.append(f'<rect x="150" y="125" width="90" height="50" fill="#f3d6d4" stroke="{INK}" stroke-width="1.5"/>')
    s.text(105, 156, "S", 18, "middle", BLUE, bold=True)
    s.text(195, 156, "N", 18, "middle", RED, bold=True)
    s.arrow(110, 205, 210, 205, INK, 2, 10)
    s.text(160, 228, "l’imant s’acosta", 12, "middle", INK)
    # línies de camp de l'imant cap a la dreta
    for dy in (-30, 0, 30):
        s.arrow(250, 150 + dy * 0.6, 330, 150 + dy, GREY, 1.4, 8)
    s.text(300, 108, "B de l’imant", 12, "middle", GREY)
    # espira (el·lipse)
    s.items.append(f'<ellipse cx="420" cy="150" rx="26" ry="80" fill="none" stroke="{ORANGE}" stroke-width="3"/>')
    # corrent induït: fletxes sobre l'espira
    s.text(420, 58, "espira", 12, "middle", ORANGE, bold=True)
    # requadre: l'espira vista des de l'imant
    s.circle(640, 240, 26, ORANGE, "none", 3)
    s.head(640 - 26, 236, 1.5708, ORANGE, 12)
    s.head(640 + 26, 244, -1.5708, ORANGE, 12)
    s.circle(640, 240, 3.5, GREEN, GREEN)
    s.circle(640, 240, 8, GREEN, "none", 1.5)
    s.text(640, 284, "vista des de l’imant:", 11, "middle", ORANGE)
    s.text(640, 298, "corrent antihorari", 11, "middle", ORANGE, bold=True)
    # camp induït cap a l'esquerra (s'oposa)
    s.arrow(520, 150, 440, 150, GREEN, 2.4, 11)
    s.arrow(470, 150, 380, 150, GREEN, 2.4, 11)
    s.text(560, 145, "B induït", 13, "start", GREEN, bold=True)
    s.text(560, 163, "(s’oposa a l’augment", 12, "start", GREEN)
    s.text(560, 179, "del flux)", 12, "start", GREEN)
    s.text(420, 262, "la cara de l’espira que mira l’imant", 12, "middle", INK)
    s.text(420, 278, "fa de pol N: repel·leix l’imant", 12, "middle", INK)
    return s.svg()


FIGS = {
    "fig-7.3": (fig_73(), "Llei de Lenz. Quan el pol nord d’un imant s’acosta a una espira, el flux cap a la dreta que la travessa "
                "augmenta. El corrent induït crea un camp cap a l’esquerra (verd), que s’oposa a aquest augment: la cara de "
                "l’espira que mira l’imant es comporta com un pol nord i el repel·leix. Cal fer treball per acostar l’imant, i "
                "aquest treball és l’origen de l’energia elèctrica induïda. Requadre: vista des de l’imant, el corrent induït circula en sentit antihorari i el camp induït surt cap a l’observador (⊙)."),
}

BLOCKS = [
    dict(file=F, id="ind-fem", where=("end", "ind-s1"), html=r"""
<div class="box def"><div class="lead">Força electromotriu (FEM) i signe del flux</div><dl>
<dt>Força electromotriu</dt><dd>Energia que un generador (pila, dinamo, bobina en un flux variable) dona a cada unitat de càrrega que recorre el circuit: $\varepsilon=W/q$. Malgrat el nom, no és una força: es mesura en volts ($1\ \mathrm V=1\ \mathrm{J\cdot C^{-1}}$). En un circuit tancat de resistència $R$ fa circular un corrent $I=\varepsilon/R$.</dd>
<dt>Signe del flux</dt><dd>El vector superfície $\vec S$ (perpendicular a l’espira, de mòdul l’àrea) es pot triar cap a una banda o l’altra; un cop triat, el flux és positiu si $\vec B$ travessa l’espira en el mateix sentit que $\vec S$ i negatiu en cas contrari. El sentit positiu del corrent és el que dona la regla de la mà dreta amb el polze en el sentit de $\vec S$.</dd>
<dt>Interpretació</dt><dd>El flux és proporcional al nombre de línies de camp que travessen la superfície. Com que les línies de $\vec B$ són tancades, el flux a través d’una superfície tancada és sempre zero (no hi ha monopols magnètics).</dd>
</dl></div>
"""),
    dict(file=F, id="ind-lenz", where=("end", "ind-s2"), html=r"""
[[fig-7.3]]
<div class="box def"><div class="lead">Per què el signe menys? La llei de Lenz és la conservació de l’energia</div>
<p>Si el corrent induït reforcés la variació de flux, en acostar una mica l’imant l’espira l’atrauria, el flux augmentaria encara més, el corrent creixeria… i obtindríem energia elèctrica i cinètica del no-res. Com que el corrent induït s’oposa a la variació (figura 7.3), cal fer un treball per moure l’imant contra la força de repulsió, i aquest treball és exactament l’energia elèctrica que es dissipa al circuit. El signe menys de la llei de Faraday-Lenz expressa la conservació de l’energia.</p></div>
<div class="box ex"><div class="lead">Exemple resolt: bobina en un camp que augmenta</div>
<p>Una bobina de $N=200$ espires d’àrea $S=10\ \mathrm{cm^2}=1{,}0\cdot10^{-3}\ \mathrm{m^2}$ té el pla perpendicular a un camp que augmenta uniformement de $0{,}20$ T a $0{,}80$ T en $0{,}30$ s. La resistència de la bobina és $2{,}0\ \Omega$.</p>
$$|\varepsilon|=N\,\frac{\Delta\Phi}{\Delta t}=N\,S\,\frac{\Delta B}{\Delta t}=200\cdot1{,}0\cdot10^{-3}\cdot\frac{0{,}60}{0{,}30}=0{,}40\ \text{V},\qquad I=\frac{\varepsilon}{R}=0{,}20\ \text{A}$$
<p>Sentit (Lenz): el flux augmenta, de manera que el camp induït és de sentit contrari al camp extern dins la bobina; la regla de la mà dreta amb el polze en el sentit del camp induït dona el sentit del corrent.</p></div>
"""),
    dict(file=F, id="ind-barra", where=("end", "ind-s3"), html=r"""
<div class="box dem"><div class="lead">Demostració: la mateixa FEM a partir de la força de Lorentz</div>
<p><span class="pp">Punt de partida</span> la força de Lorentz sobre els electrons lliures de la barra, que es mouen amb ella a velocitat $\vec v$ dins el camp $\vec B$, i la definició de FEM com a treball per unitat de càrrega, $\varepsilon=W/q$.</p>
<p>Pas 1. Cada càrrega $q$ de la barra rep una força $|q|vB$ dirigida al llarg de la barra ($\vec v\perp\vec B$).</p>
<p>Pas 2. Aquesta força empeny les càrregues tota la longitud $l$ de la barra: fa un treball $W=|q|vB\,l$ sobre cada càrrega.</p>
<div class="box res"><div class="lead">Resultat</div>
$$\varepsilon=\frac{W}{|q|}=Blv$$</div>
<p>És el mateix resultat que dona la llei de Faraday: les dues descripcions (flux variable o força sobre càrregues en moviment) són equivalents.</p></div>
<div class="box dem"><div class="lead">Demostració: balanç d’energia de la barra (el fre magnètic)</div>
<p><span class="pp">Punt de partida</span> la llei d’Ohm, $I=\varepsilon/R$, la força sobre un conductor, $F=IlB$, i la potència d’una força, $P=Fv$.</p>
<p>Situació: la barra de la figura 7.1 llisca a velocitat constant $v$; el circuit té una resistència total $R$.</p>
<p>Pas 1. Corrent induït: $I=\dfrac{\varepsilon}{R}=\dfrac{Blv}{R}$.</p>
<p>Pas 2. Força magnètica sobre la barra (s’oposa al moviment, per Lenz): $F_m=IlB=\dfrac{B^2l^2v}{R}$. Per mantenir $v$ constant, un agent extern ha de fer una força igual i oposada.</p>
<p>Pas 3. Potència mecànica de l’agent: $P_{\text{mec}}=F_mv=\dfrac{B^2l^2v^2}{R}$. Potència elèctrica dissipada a la resistència: $P_{\text{el}}=I^2R=\dfrac{B^2l^2v^2}{R}$.</p>
<div class="box res"><div class="lead">Resultat</div>
$$P_{\text{mec}}=P_{\text{el}}=\frac{B^2l^2v^2}{R}=\varepsilon\,I$$</div>
<p>Tot el treball mecànic es converteix en energia elèctrica (i després en calor a la resistència). Exemple: $l=0{,}50$ m, $B=0{,}40$ T, $v=3{,}0\ \mathrm{m\cdot s^{-1}}$, $R=2{,}0\ \Omega$: $\varepsilon=0{,}60$ V, $I=0{,}30$ A, $F=0{,}060$ N i $P=0{,}18$ W.</p></div>
"""),
    dict(file=F, id="ind-transf", where=("end", "ind-s5"), html=r"""
<div class="box dem"><div class="lead">Demostració: relació de transformació d’un transformador ideal</div>
<p><span class="pp">Punt de partida</span> la llei de Faraday aplicada a cada bobina i la conservació de l’energia.</p>
<p>Situació: transformador ideal; el nucli de ferro condueix tot el flux, de manera que cada espira del primari ($N_1$ espires) i del secundari ($N_2$) és travessada pel mateix flux $\Phi(t)$; no hi ha pèrdues.</p>
<p>Pas 1. FEM en cada bobina: $\varepsilon_1=-N_1\dfrac{d\Phi}{dt}$ i $\varepsilon_2=-N_2\dfrac{d\Phi}{dt}$.</p>
<p>Pas 2. Dividim: el factor $d\Phi/dt$ és el mateix i se simplifica: $\dfrac{V_2}{V_1}=\dfrac{N_2}{N_1}$.</p>
<p>Pas 3. Sense pèrdues, la potència que entra pel primari surt pel secundari: $V_1I_1=V_2I_2$, és a dir, $\dfrac{I_1}{I_2}=\dfrac{V_2}{V_1}$.</p>
<div class="box res"><div class="lead">Resultat</div>
$$\frac{V_2}{V_1}=\frac{N_2}{N_1}=\frac{I_1}{I_2}$$</div>
<p>Un transformador elevador ($N_2>N_1$) augmenta la tensió i redueix el corrent en la mateixa proporció; no «crea» energia.</p></div>
<div class="box ex"><div class="lead">Exemple resolt: per què el transport elèctric es fa a alta tensió</div>
<p>Volem transportar una potència $P=1{,}0$ MW per una línia de resistència total $R=5{,}0\ \Omega$. El corrent és $I=P/V$ i la potència perduda per efecte Joule, $P_{\text{pèrdues}}=I^2R$.</p>
<ul><li>A $V=10$ kV: $I=100$ A i $P_{\text{pèrdues}}=100^2\cdot5{,}0=5{,}0\cdot10^{4}$ W (el 5 % de la potència).</li>
<li>A $V=400$ kV: $I=2{,}5$ A i $P_{\text{pèrdues}}=2{,}5^2\cdot5{,}0\approx31$ W.</li></ul>
<p>Les pèrdues són proporcionals a $1/V^2$: multiplicar la tensió per 40 les divideix per 1600. Per això s’eleva la tensió a la central amb transformadors i es redueix a prop del consum.</p></div>
"""),
]
