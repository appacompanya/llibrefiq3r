"""Tema 8. Física quàntica: definicions de l'efecte fotoelèctric, intensitat i nombre de fotons, ona-corpuscle, espectres."""
F = "quantica"

BLOCKS = [
    dict(file=F, id="quant-defs", where=("after", '<div class="box ex"><div class="lead">Exemple resolt: Potassi</div>'), html=r"""
<div class="box def"><div class="lead">Definicions de l’efecte fotoelèctric</div><dl>
<dt>Treball d’extracció $W_0$</dt><dd>Energia mínima necessària per arrencar un electró de la superfície d’un metall. És una propietat del metall (uns quants eV: 2,3 eV el potassi, 4,3 eV el zinc).</dd>
<dt>Freqüència llindar $f_0$</dt><dd>Freqüència mínima de la llum que produeix efecte fotoelèctric en un metall: $f_0=W_0/h$. La longitud d’ona llindar, $\lambda_0=hc/W_0$, és la <i>màxima</i>.</dd>
<dt>Intensitat de la llum (model de fotons)</dt><dd>Energia que arriba per unitat de temps i de superfície, $I=\dfrac{N\,hf}{S\,t}$, on $N$ és el nombre de fotons. Amb la freqüència fixada, més intensitat vol dir <i>més fotons</i>, no fotons més energètics: s’arrenquen més electrons (més corrent), però cadascun amb la mateixa energia cinètica màxima.</dd>
<dt>Corrent de saturació</dt><dd>Quan la tensió entre ànode i càtode és prou gran perquè tots els electrons arrencats arribin a l’ànode, el corrent deixa d’augmentar. És proporcional a la intensitat de la llum.</dd>
</dl></div>
<table class="amp-tab"><thead><tr><th>Fet experimental</th><th>Predicció de la teoria ondulatòria clàssica</th><th>Explicació d’Einstein (fotons)</th></tr></thead><tbody>
<tr><td>Hi ha una freqüència llindar</td><td>Amb prou intensitat (o esperant prou temps) sempre s’haurien d’arrencar electrons</td><td>Un fotó amb $hf<W_0$ no pot arrencar cap electró, i els fotons no «sumen» la seva energia</td></tr>
<tr><td>$E_{c,\text{màx}}$ depèn de $f$, no de la intensitat</td><td>Més intensitat, més energia per electró</td><td>$E_{c,\text{màx}}=hf-W_0$: només depèn de l’energia de cada fotó</td></tr>
<tr><td>L’emissió és instantània</td><td>Amb llum feble, l’electró hauria d’acumular energia durant un temps</td><td>Cada electró absorbeix un fotó sencer, de cop</td></tr>
</tbody></table>
<div class="box ex"><div class="lead">Exemple resolt: quants fotons emet un làser?</div>
<p>Un punter làser de $1{,}0$ mW emet llum de $650$ nm. Energia de cada fotó: $E=hc/\lambda=6{,}63\cdot10^{-34}\cdot3{,}00\cdot10^{8}/650\cdot10^{-9}=3{,}06\cdot10^{-19}$ J. Nombre de fotons per segon: $N/t=P/E=1{,}0\cdot10^{-3}/3{,}06\cdot10^{-19}=3{,}3\cdot10^{15}$ fotons/s. Són tants que la llum ens sembla contínua.</p></div>
"""),
    dict(file=F, id="quant-dualitat", where=("after", "<p>Per a objectes macroscòpics"), html=r"""
<div class="box def"><div class="lead">Dualitat ona-corpuscle</div>
<p>La llum i les partícules materials mostren comportament ondulatori (interferència, difracció) o corpuscular (intercanvi d’energia i de quantitat de moviment en paquets) segons l’experiment, però mai els dos alhora en el mateix experiment. Totes dues descripcions són necessàries i complementàries.</p>
<ul><li>Un fotó, sense massa, té quantitat de moviment $p=\dfrac{E}{c}=\dfrac{h}{\lambda}$.</li>
<li>Una partícula de quantitat de moviment $p$ té una longitud d’ona $\lambda=h/p$. Per a una pilota de $0{,}10$ kg a $10\ \mathrm{m\cdot s^{-1}}$: $\lambda=\dfrac{6{,}63\cdot10^{-34}}{0{,}10\cdot10}=6{,}6\cdot10^{-34}$ m, uns $10^{18}$ vegades més petita que un nucli atòmic ($\sim10^{-15}$ m): cap obertura no la pot difractar.</li></ul></div>
"""),
    dict(file=F, id="quant-bohr", where=("end", "quant-s4"), html=r"""
<div class="box ex"><div class="lead">Exemple resolt: la ratlla vermella de l’hidrogen</div>
<p>En el salt de $n=3$ a $n=2$: $hf=E_3-E_2=-\dfrac{13{,}6}{9}+\dfrac{13{,}6}{4}=1{,}89$ eV $=3{,}03\cdot10^{-19}$ J. Longitud d’ona del fotó emès: $\lambda=\dfrac{hc}{E}=\dfrac{6{,}63\cdot10^{-34}\cdot3{,}00\cdot10^{8}}{3{,}03\cdot10^{-19}}=6{,}56\cdot10^{-7}$ m $=656$ nm (vermell, primera ratlla de la sèrie de Balmer).</p>
<p>Un àtom en l’estat fonamental ($n=1$) <i>absorbeix</i> només els fotons que tenen exactament l’energia d’un salt cap amunt; per això l’espectre d’absorció té ratlles fosques a les mateixes freqüències que l’espectre d’emissió. Per ionitzar l’àtom (portar l’electró de $n=1$ a $n\to\infty$) calen $13{,}6$ eV.</p></div>
"""),
]
