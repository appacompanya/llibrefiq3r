"""Tema 6. Camp magnètic: producte vectorial, la força magnètica no fa treball, hèlix, selector, espectròmetre, ciclotró, força sobre corrents."""
F = "camp-magnetic"

BLOCKS = [
    dict(file=F, id="mag-vectorial", where=("end", "mag-s2"), html=r"""
<div class="box def"><div class="lead">Producte vectorial</div>
<p>El producte vectorial de dos vectors $\vec a$ i $\vec b$ és un <i>vector</i> $\vec c=\vec a\times\vec b$ amb:</p>
<ul><li><b>Mòdul:</b> $c=a\,b\sin\alpha$, on $\alpha$ és l’angle entre els dos vectors (és l’àrea del paral·lelogram que formen). És zero si són paral·lels i màxim si són perpendiculars.</li>
<li><b>Direcció:</b> perpendicular al pla que formen $\vec a$ i $\vec b$.</li>
<li><b>Sentit:</b> el que dona la regla de la mà dreta (o el d’avançament d’un llevataps que gira de $\vec a$ cap a $\vec b$ per l’angle més petit).</li></ul>
<p>No és commutatiu: $\vec b\times\vec a=-\vec a\times\vec b$. Amb els vectors unitaris dels eixos: $\vec i\times\vec j=\vec k$, $\vec j\times\vec k=\vec i$, $\vec k\times\vec i=\vec j$ (i canviant l’ordre, el signe), i $\vec i\times\vec i=\vec 0$. En components:</p>
$$\vec a\times\vec b=(a_yb_z-a_zb_y)\,\vec i+(a_zb_x-a_xb_z)\,\vec j+(a_xb_y-a_yb_x)\,\vec k$$
<p>Exemple: $\vec v=v\,\vec i$ i $\vec B=-B\,\vec k$ (cap endins del paper si $\vec k$ surt del paper): $\vec v\times\vec B=-vB\,(\vec i\times\vec k)=-vB\,(-\vec j)=vB\,\vec j$. Per a $q>0$ la força apunta cap a $+y$, com a la figura 6.5(a).</p></div>
<div class="box def"><div class="lead">Definició operativa del camp magnètic</div>
<p>La força de Lorentz permet definir $\vec B$ a partir del que mesurem: en un punt hi ha un camp magnètic d’1 T si una càrrega d’1 C que hi passa a $1\ \mathrm{m\cdot s^{-1}}$ perpendicularment al camp rep una força d’1 N: $1\ \mathrm{T}=1\ \mathrm{N\cdot s\cdot C^{-1}\cdot m^{-1}}=1\ \mathrm{N\cdot A^{-1}\cdot m^{-1}}$. És una unitat gran: el camp magnètic terrestre és d’uns $5\cdot10^{-5}$ T; un imant de nevera, unes centèsimes de tesla; una ressonància magnètica, 1,5–3 T.</p>
<p>Si en una regió hi ha alhora un camp elèctric i un de magnètic, la força total sobre la càrrega és $\vec F=q\,(\vec E+\vec v\times\vec B)$.</p></div>
<div class="box dem"><div class="lead">Demostració: la força magnètica no fa treball</div>
<p><span class="pp">Punt de partida</span> la definició de treball, $W=\vec F\cdot\Delta\vec r$, en un interval de temps petit $\Delta t$, i el teorema de l’energia cinètica, $W=\Delta E_c$.</p>
<p>Pas 1. En un interval petit el desplaçament té la direcció de la velocitat: $\Delta\vec r=\vec v\,\Delta t$.</p>
<p>Pas 2. La força de Lorentz és perpendicular a $\vec v$ (és un producte vectorial on hi ha $\vec v$): $\vec F\cdot\vec v=0$. Per tant $W=\vec F\cdot\vec v\,\Delta t=0$ en cada interval, i també en tota la trajectòria.</p>
<div class="box res"><div class="lead">Resultat</div>
$$W_{\text{magnètica}}=0\;\Rightarrow\;\Delta E_c=0\;\Rightarrow\;|\vec v|=\text{constant}$$</div>
<p>Un camp magnètic pot canviar la <i>direcció</i> de la velocitat, però no el seu mòdul ni l’energia cinètica. Per accelerar partícules (augmentar-ne l’energia) cal un camp elèctric.</p></div>
"""),
    dict(file=F, id="mag-aplicacions", where=("end", "mag-s3"), html=r"""
<h4 class="amp">Trajectòria en hèlix</h4>
<p>Si $\vec v$ forma un angle $\alpha$ amb $\vec B$, descomponem la velocitat en una component paral·lela al camp, $v_\parallel=v\cos\alpha$, i una de perpendicular, $v_\perp=v\sin\alpha$. La força només depèn de $v_\perp$ ($F=|q|v_\perp B$): en el pla perpendicular a $\vec B$ la partícula fa un MCU de radi $r=\dfrac{mv_\perp}{|q|B}$ i període $T=\dfrac{2\pi m}{|q|B}$, mentre que en la direcció del camp avança amb MRU. La combinació és una hèlix de pas $p=v_\parallel T$. Així queden atrapades les partícules del vent solar en el camp magnètic terrestre i es produeixen les aurores.</p>
<div class="box dem"><div class="lead">Demostració: selector de velocitats</div>
<p><span class="pp">Punt de partida</span> la primera llei de Newton: una partícula passa sense desviar-se si la força resultant és nul·la, $\vec F=q(\vec E+\vec v\times\vec B)=\vec 0$.</p>
<p>Situació: camps $\vec E$ i $\vec B$ uniformes, perpendiculars entre si i perpendiculars a la velocitat de les partícules, orientats de manera que la força elèctrica i la magnètica tenen sentits contraris.</p>
<p>Pas 1. Igualem els mòduls de les dues forces: $|q|E=|q|vB$.</p>
<p>Pas 2. La càrrega se simplifica: el resultat val per a qualsevol càrrega i massa.</p>
<div class="box res"><div class="lead">Resultat</div>
$$v=\frac{E}{B}$$</div>
<p>Les partícules més ràpides es desvien en el sentit de la força magnètica (que creix amb $v$) i les més lentes, en el de la força elèctrica.</p></div>
<div class="box dem"><div class="lead">Demostració: espectròmetre de masses</div>
<p><span class="pp">Punt de partida</span> la conservació de l’energia en el tram d’acceleració, $|q|\,\Delta V=\tfrac12mv^2$ (els ions parteixen del repòs), i el radi de la trajectòria circular, $r=\dfrac{mv}{|q|B}$.</p>
<p>Pas 1. Velocitat de sortida de l’acceleració: $v=\sqrt{\dfrac{2|q|\Delta V}{m}}$.</p>
<p>Pas 2. La substituïm al radi i simplifiquem:</p>
$$r=\frac{m}{|q|B}\sqrt{\frac{2|q|\Delta V}{m}}=\frac{1}{B}\sqrt{\frac{2m\,\Delta V}{|q|}}$$
<div class="box res"><div class="lead">Resultat</div>
$$r=\frac{1}{B}\sqrt{\frac{2m\,\Delta V}{|q|}}\qquad(r\propto\sqrt m)$$</div>
<p>Exemple: ions $^{35}\mathrm{Cl}^-$ i $^{37}\mathrm{Cl}^-$ accelerats amb $\Delta V=1000$ V en un camp $B=0{,}50$ T ($1\ \mathrm u=1{,}66\cdot10^{-27}$ kg): $r_{35}=5{,}39$ cm i $r_{37}=5{,}54$ cm. Després de mitja volta arriben a la placa separats $2(r_{37}-r_{35})\approx3{,}0$ mm: el detector separa els dos isòtops.</p></div>
<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: energia màxima d’un ciclotró</div>
<p>El període de gir no depèn de la velocitat, i per això una tensió alterna de freqüència fixa $f=\dfrac{|q|B}{2\pi m}$ accelera la partícula cada mitja volta. Quan el radi arriba al del ciclotró, $R$, la velocitat és $v=|q|BR/m$ i l’energia cinètica màxima és $E_c=\dfrac{q^2B^2R^2}{2m}$. Per a protons amb $B=1$ T i $R=0{,}5$ m: $f\approx15$ MHz i $E_c\approx12$ MeV.</p></div>
"""),
    dict(file=F, id="mag-ILB", where=("before", '<figure id="fig-6.3"'), html=r"""
<div class="box dem"><div class="lead">Demostració: força sobre un conductor a partir de la força de Lorentz</div>
<p><span class="pp">Punt de partida</span> la força de Lorentz sobre cada càrrega que circula pel conductor, $F=|q|vB\sin\alpha$, i la definició d’intensitat de corrent, $I=\dfrac{\Delta Q}{\Delta t}$.</p>
<p>Situació: un tram rectilini de conductor de longitud $L$, dins un camp uniforme $\vec B$ que forma un angle $\alpha$ amb el conductor. Pel conductor circula un corrent $I$: les càrregues lliures hi avancen amb una velocitat mitjana $v$.</p>
<p>Pas 1. La càrrega total $\Delta Q$ que hi ha en el tram recorre la longitud $L$ en un temps $\Delta t=L/v$; per tant $I=\dfrac{\Delta Q}{\Delta t}=\dfrac{\Delta Q\,v}{L}$, és a dir, $\Delta Q\,v=I\,L$.</p>
<p>Pas 2. Sumem les forces de Lorentz de totes les càrregues del tram (tenen la mateixa direcció): $F=\Delta Q\,vB\sin\alpha$.</p>
<div class="box res"><div class="lead">Resultat</div>
$$F=I\,L\,B\sin\alpha,\qquad \vec F=I\,\vec L\times\vec B$$</div>
<p>La força sobre el conductor és la suma de les forces magnètiques sobre les càrregues que s’hi mouen; per això té la mateixa regla de sentit, amb $\vec L$ en el sentit del corrent.</p></div>
"""),
    dict(file=F, id="mag-ampere", where=("end", "mag-s4"), html=r"""
<div class="box rec"><div class="lead">Recorda: l’ampere i els motors</div>
<p>Amb $I_1=I_2=1$ A i $d=1$ m, la força entre els fils és $F/L=\dfrac{\mu_0}{2\pi}=2\cdot10^{-7}\ \mathrm{N\cdot m^{-1}}$. Fins al 2019 aquesta era la definició de l’ampere; avui l’ampere es defineix fixant el valor exacte de la càrrega elemental $e$, però el resultat numèric és pràcticament el mateix.</p>
<p>Sobre una espira amb corrent dins un camp magnètic, les forces sobre els costats oposats tenen sentits contraris i formen un parell que la fa girar: és el principi del motor elèctric. El funcionament invers (fer girar una espira dins d’un camp per obtenir corrent) és el generador del tema 7.</p></div>
"""),
]
