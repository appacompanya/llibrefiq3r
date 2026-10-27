"""Tema 2. Moviment ondulatori: front d'ona, doble periodicitat, vibració dels punts, exemple d'equació, energia i amplitud."""
F = "ones"

BLOCKS = [
    dict(file=F, id="ones-front", where=("end", "ones-s2"), html=r"""
<div class="box def"><div class="lead">Front d’ona, raig i ona harmònica</div><dl>
<dt>Front d’ona</dt><dd>Superfície formada pels punts del medi que, en un instant donat, vibren en fase (tenen la mateixa fase). En una ona que surt d’un focus puntual en un medi homogeni, els fronts d’ona són esferes (ona esfèrica); molt lluny del focus, un tros petit de front és pràcticament pla (ona plana).</dd>
<dt>Raig</dt><dd>Línia perpendicular als fronts d’ona que indica la direcció de propagació.</dd>
<dt>Ona harmònica</dt><dd>Ona en què el focus fa un MHS. Cada punt del medi repeteix el MHS del focus amb un retard, de manera que tots els punts vibren amb la mateixa freqüència i (si no hi ha pèrdues) la mateixa amplitud.</dd>
</dl></div>
"""),
    dict(file=F, id="ones-doble", where=("after", '<div class="box ex"><div class="lead">Exemple resolt: Lectura d’una equació</div>'), html=r"""
<h4 class="amp">La doble periodicitat de l’ona</h4>
<p>La funció $y(x,t)=A\sin(\omega t-kx+\varphi_0)$ és periòdica en el temps <i>i</i> en l’espai:</p>
<ul><li><b>En el temps</b> (fixem un punt $x$): $y(x,t+T)=A\sin(\omega t+\omega T-kx+\varphi_0)=y(x,t)$ perquè $\omega T=2\pi$. Cada punt fa un MHS de període $T$.</li>
<li><b>En l’espai</b> (fixem un instant $t$, com en una fotografia): $y(x+\lambda,t)=A\sin(\omega t-kx-k\lambda+\varphi_0)=y(x,t)$ perquè $k\lambda=2\pi$. El perfil de l’ona es repeteix cada longitud d’ona.</li></ul>
<p>Cada punt del medi vibra amb un MHS: la seva velocitat i la seva acceleració de vibració són</p>
$$v_y=\frac{\partial y}{\partial t}=A\omega\cos(\omega t-kx+\varphi_0),\qquad a_y=\frac{\partial v_y}{\partial t}=-A\omega^2\sin(\omega t-kx+\varphi_0)=-\omega^2y$$
<p>(la derivada es fa respecte del temps mantenint $x$ fixa). Valors màxims: $v_{y,\text{màx}}=A\omega$ i $a_{y,\text{màx}}=A\omega^2$. La velocitat de propagació $v=\lambda f$ és constant i només depèn del medi; la velocitat de vibració $v_y$ canvia contínuament i depèn de l’amplitud i de la freqüència.</p>
<div class="box ex"><div class="lead">Exemple resolt: escriure l’equació d’una ona a partir de les dades</div>
<p>Una ona transversal d’amplitud $5{,}0$ cm i freqüència $10$ Hz es propaga cap a les $x$ <i>negatives</i> a $20\ \mathrm{m\cdot s^{-1}}$. A $t=0$, el punt $x=0$ és a la màxima elongació positiva.</p>
<p>Pas 1. Paràmetres: $\omega=2\pi f=20\pi\ \mathrm{rad\cdot s^{-1}}$, $\lambda=v/f=2{,}0$ m, $k=2\pi/\lambda=\pi\ \mathrm{rad\cdot m^{-1}}$.</p>
<p>Pas 2. Sentit de propagació cap a $-x$: el terme $kx$ va amb signe $+$: $y=A\sin(\omega t+kx+\varphi_0)$.</p>
<p>Pas 3. Fase inicial: a $x=0$, $t=0$, $y=A$, per tant $\sin\varphi_0=1$ i $\varphi_0=\pi/2$.</p>
$$y(x,t)=0{,}050\sin\!\left(20\pi t+\pi x+\frac{\pi}{2}\right)\ (\text{SI})$$
<p>Dos punts separats $0{,}50$ m tenen un desfasament $\Delta\varphi=k\,\Delta x=\pi/2$ rad (en quadratura). Velocitat màxima de vibració: $A\omega=0{,}050\cdot20\pi=3{,}1\ \mathrm{m\cdot s^{-1}}$.</p></div>
"""),
    dict(file=F, id="ones-energia", where=("before", "<p>Nivell d’intensitat sonora"), html=r"""
<div class="box dem"><div class="lead">Demostració: energia d’una ona i amplitud d’una ona esfèrica</div>
<p><span class="pp">Punt de partida</span> cada partícula del medi fa un MHS, de manera que la seva energia mecànica és $E=\tfrac12m\omega^2A^2$ (apartat 1.5), i la intensitat és la potència per unitat de superfície, $I=P/S$.</p>
<p>Pas 1. L’energia que transporta l’ona és la de les partícules que fa vibrar: és proporcional al quadrat de l’amplitud i al quadrat de la freqüència, $E\propto A^2f^2$. Per tant, per a una freqüència donada, $I\propto A^2$.</p>
<p>Pas 2. Per a una font puntual sense absorció, $I=\dfrac{P}{4\pi r^2}\propto\dfrac{1}{r^2}$.</p>
<p>Pas 3. Igualem les dues proporcionalitats: $A^2\propto 1/r^2$.</p>
<div class="box res"><div class="lead">Resultat</div>
$$I\propto A^2,\qquad A\propto\frac1r,\qquad \frac{A_2}{A_1}=\frac{r_1}{r_2}$$</div>
<p>En una ona esfèrica la intensitat és inversament proporcional a $r^2$, i l’amplitud, inversament proporcional a $r$: l’energia es reparteix en una superfície cada cop més gran. A més, els medis reals absorbeixen part de l’energia (absorció), i la intensitat disminueix encara més ràpid.</p></div>
"""),
]
