"""Tema 9. Relativitat: definicions bàsiques, simultaneïtat, límit clàssic de l'energia cinètica."""
F = "relativitat"

BLOCKS = [
    dict(file=F, id="rel-defs", where=("end", "rel-s1"), html=r"""
<div class="box def"><div class="lead">Definicions</div><dl>
<dt>Esdeveniment</dt><dd>Un fet que passa en un punt de l’espai i en un instant: queda determinat per tres coordenades d’espai i una de temps $(x,y,z,t)$.</dd>
<dt>Sistema de referència inercial</dt><dd>Sistema de referència en què un cos sobre el qual no actua cap força es manté en repòs o en MRU (s’hi compleix la primera llei de Newton). Qualsevol sistema que es mou amb velocitat constant respecte d’un d’inercial també ho és. Un sistema accelerat (un cotxe que frena, una plataforma que gira) no és inercial.</dd>
<dt>Temps propi $\Delta t_0$</dt><dd>Interval de temps entre dos esdeveniments mesurat per un observador per a qui tots dos passen al mateix lloc (el rellotge que els mesura és en repòs respecte d’ells). És el temps més curt que pot mesurar qualsevol observador inercial.</dd>
<dt>Longitud pròpia $L_0$</dt><dd>Longitud d’un objecte mesurada per un observador en repòs respecte d’ell. És la més gran: qualsevol observador respecte del qual l’objecte es mou hi mesura $L=L_0/\gamma<L_0$ en la direcció del moviment.</dd>
</dl></div>
<div class="box rec"><div class="lead">Recorda: la simultaneïtat és relativa</div>
<p>Si la velocitat de la llum és la mateixa per a tots els observadors, dos esdeveniments simultanis per a un observador poden no ser-ho per a un altre que es mou respecte del primer. Exemple: una bombeta encesa al centre d’un vagó il·lumina alhora les dues portes per a un passatger; per a un observador de l’andana, la porta del darrere avança cap a la llum i s’il·lumina abans que la del davant. No hi ha un temps absolut compartit per tots els observadors.</p></div>
"""),
    dict(file=F, id="rel-ec", where=("end", "rel-s4"), html=r"""
<div class="box dem"><div class="lead">Demostració: a velocitats petites, $E_c=(m-m_0)c^2$ es redueix a $\tfrac12m_0v^2$</div>
<p><span class="pp">Punt de partida</span> l’energia cinètica relativista, $E_c=(m-m_0)c^2=(\gamma-1)\,m_0c^2$, i l’aproximació $(1-x)^{-1/2}\approx1+\tfrac12x$, vàlida per a $x\ll1$.</p>
<p>Pas 1. Amb $x=v^2/c^2\ll1$: $\gamma=\left(1-\dfrac{v^2}{c^2}\right)^{-1/2}\approx1+\dfrac{v^2}{2c^2}$.</p>
<p>Pas 2. Substituïm: $E_c\approx\dfrac{v^2}{2c^2}\,m_0c^2$.</p>
<div class="box res"><div class="lead">Resultat</div>
$$E_c\approx\tfrac12m_0v^2\qquad(v\ll c)$$</div>
<p>La mecànica de Newton és el límit de la relativitat per a velocitats petites. Per a $v=0{,}8c$ ja no val: per a un electró ($m_0c^2=0{,}511$ MeV), l’energia cinètica correcta és $(\gamma-1)\,m_0c^2=0{,}667\cdot0{,}511=0{,}341$ MeV, mentre que $\tfrac12m_0v^2=0{,}32\cdot0{,}511=0{,}164$ MeV, menys de la meitat.</p></div>
<div class="box noav"><div class="lead">Per ampliar – no avaluable a la PAU: quantitat de moviment i energia</div>
<p>La quantitat de moviment relativista és $p=\gamma m_0v$, i l’energia total, la quantitat de moviment i la massa en repòs es relacionen per $E^2=(pc)^2+(m_0c^2)^2$. Per a un fotó ($m_0=0$) dona $E=pc$, la relació que fa servir De Broglie al tema 8.</p></div>
"""),
]
