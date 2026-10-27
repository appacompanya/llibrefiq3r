"""Tema 11. Òptica: elements d'una lent, augment lateral, casos de la lent convergent i objecte al focus."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _svg import Svg, INK, GREY, RED, BLUE, GREEN

F = "optica"


def fig_117():
    s = Svg(700, 400)
    ay, lx, fp = 160, 350, 150
    s.line(30, ay, 680, ay, GREY, 1)
    # lent convergent
    s.line(lx, 20, lx, 370, INK, 2)
    s.head(lx, 20, -1.5708, INK, 11)
    s.head(lx, 370, 1.5708, INK, 11)
    for x, lab in [(lx - fp, "F"), (lx + fp, "F′")]:
        s.circle(x, ay, 3.5, INK, INK)
        s.text(x + (-10 if lab == "F" else 4), ay + (20 if lab == "F" else -10), lab, 13, "middle" if lab == "F" else "start", INK, True)
    s.text(lx + 7, ay + 18, "O", 12, "start", INK)
    # objecte al focus objecte
    top = (lx - fp, ay - 70)
    s.arrow(lx - fp, ay, top[0], top[1], INK, 2.6, 11)
    s.text(top[0] - 8, top[1] - 6, "objecte a F", 12, "end", INK)
    k = 70 / fp
    xe = 650
    # raig 1: paral·lel a l'eix -> passa per F'
    s.mid_arrow(top[0], top[1], lx, top[1], RED, 1.8, 0.5)
    s.mid_arrow(lx, top[1], xe, top[1] + (xe - lx) * k, RED, 1.8, 0.55)
    # raig 2: pel centre òptic, no es desvia
    s.mid_arrow(top[0], top[1], lx, ay, BLUE, 1.8, 0.5)
    s.mid_arrow(lx, ay, xe, ay + (xe - lx) * k, BLUE, 1.8, 0.55)
    # raig 3: arbitrari, toca la lent a y=200 i surt paral·lel als altres
    y3 = 205
    s.mid_arrow(top[0], top[1], lx, y3, GREEN, 1.8, 0.5)
    s.mid_arrow(lx, y3, xe, y3 + (xe - lx) * k, GREEN, 1.8, 0.55)
    # prolongacions cap enrere (tampoc es tallen)
    for y0 in (top[1], ay, y3):
        s.line(lx, y0, lx - 120, y0 - 120 * k, GREY, 1.1, "5 5")
    s.text(470, 40, "Raigs emergents paral·lels:", 13, "start", INK, bold=True)
    s.text(470, 58, "no es tallen (ni ells ni les", 12, "start", INK)
    s.text(470, 74, "prolongacions) → la imatge", 12, "start", INK)
    s.text(470, 90, "es forma a l’infinit", 12, "start", INK)
    s.text(30, 392, "f′ = 3, s = −3  →  1/s′ = 1/f′ + 1/s = 1/3 − 1/3 = 0  →  s′ → ∞", 12, "start", GREY)
    return s.svg()


FIGS = {
    "fig-11.7": (fig_117(), "Objecte situat al focus objecte F d’una lent convergent. El raig paral·lel a l’eix (vermell) es refracta "
                 "passant per F′; el raig que passa pel centre òptic (blau) no es desvia; qualsevol altre raig (verd) surt paral·lel "
                 "a aquests dos. Tots els raigs que surten d’un mateix punt de l’objecte emergeixen paral·lels: no es tallen enlloc, "
                 "ni tampoc les seves prolongacions (discontínues). No hi ha imatge a distància finita: es diu que la imatge es "
                 "forma a l’infinit."),
}

BLOCKS = [
    dict(file=F, id="opt-elements", where=("start", "opt-s4"), html=r"""
<div class="box def"><div class="lead">Elements d’una lent prima i tipus d’imatge</div><dl>
<dt>Eix òptic i centre òptic O</dt><dd>L’eix òptic és la recta perpendicular a la lent que passa pel seu centre; el centre òptic O és el punt de la lent on un raig passa sense desviar-se (en aquest punt la lent es comporta com una làmina de cares paral·leles molt prima).</dd>
<dt>Focus imatge F′</dt><dd>Punt de l’eix on convergeixen (o d’on semblen sortir, en una lent divergent) els raigs que arriben paral·lels a l’eix. La seva distància a O és la distància focal imatge $f'$: positiva per a una lent convergent i negativa per a una divergent.</dd>
<dt>Focus objecte F</dt><dd>Punt de l’eix tal que els raigs que hi passen (o que s’hi dirigeixen) surten de la lent paral·lels a l’eix. Si hi ha el mateix medi a banda i banda de la lent, F i F′ són simètrics respecte d’O: $f=-f'$.</dd>
<dt>Imatge real</dt><dd>La formen els raigs <i>mateixos</i> en tallar-se després de la lent ($s'>0$). Es pot recollir en una pantalla (projector, càmera, retina).</dd>
<dt>Imatge virtual</dt><dd>La formen les <i>prolongacions</i> dels raigs, que semblen sortir d’un punt d’on realment no surten ($s'<0$ per a una lent). No es pot recollir en una pantalla, però l’ull la veu (lupa, mirall pla).</dd>
<dt>Dreta o invertida; més gran o més petita</dt><dd>Ho diu l’augment lateral $m=y'/y$: si $m>0$ la imatge és dreta i si $m<0$, invertida; si $|m|>1$ és més gran que l’objecte i si $|m|<1$, més petita.</dd>
</dl></div>
"""),
    dict(file=F, id="opt-augment", where=("before", '<figure id="fig-11.1"'), html=r"""
<div class="box dem"><div class="lead">Demostració: augment lateral $m=s'/s$</div>
<p><span class="pp">Punt de partida</span> el raig que passa pel centre òptic O no es desvia, i la semblança de triangles.</p>
<p>Situació: objecte d’altura $y$ a la posició $s$ i imatge d’altura $y'$ a la posició $s'$ (figura 11.1). El raig que va de l’extrem de l’objecte a l’extrem de la imatge passa per O en línia recta.</p>
<p>Pas 1. Aquest raig forma dos triangles rectangles amb l’eix: un de catets $|s|$ i $|y|$ (costat de l’objecte) i un altre de catets $|s'|$ i $|y'|$ (costat de la imatge). Els angles en O són iguals (oposats pel vèrtex): els triangles són semblants.</p>
$$\frac{|y'|}{|y|}=\frac{|s'|}{|s|}$$
<p>Pas 2. Signes (DIN): en una imatge real, $s<0$ i $s'>0$, i la imatge és invertida ($y'$ i $y$ de signes contraris). Per tant el quocient amb signe $y'/y$ és negatiu, igual que $s'/s$. El mateix raonament val per a les imatges virtuals (dretes, amb $s'$ i $s$ del mateix signe).</p>
<div class="box res"><div class="lead">Resultat</div>
$$m=\frac{y'}{y}=\frac{s'}{s}$$</div></div>
"""),
    dict(file=F, id="opt-casos", where=("before", '<div class="box ex"><div class="lead">Exemple resolt: Lent d’un projector</div>'), html=r"""
<h4 class="amp">Lent convergent: la imatge segons la posició de l’objecte</h4>
<p>Amb $f'>0$ i l’objecte a l’esquerra ($s<0$), l’equació de les lents dona $\dfrac{1}{s'}=\dfrac{1}{f'}+\dfrac1s$. Movent l’objecte des de molt lluny fins a la lent:</p>
<table class="amp-tab"><thead><tr><th>Posició de l’objecte</th><th>Posició de la imatge</th><th>Característiques</th><th>Ús</th></tr></thead><tbody>
<tr><td>Molt lluny ($s\to-\infty$)</td><td>Al focus imatge, $s'=f'$</td><td>Real, invertida, molt petita</td><td>Telescopi, ull mirant lluny</td></tr>
<tr><td>Més enllà de $2F$ ($|s|>2f'$)</td><td>Entre $F'$ i $2F'$</td><td>Real, invertida, més petita ($|m|<1$)</td><td>Càmera de fotos, ull</td></tr>
<tr><td>A $2F$ ($|s|=2f'$)</td><td>A $2F'$, $s'=2f'$</td><td>Real, invertida, igual ($m=-1$)</td><td>Fotocopiadora a escala 1:1</td></tr>
<tr><td>Entre $2F$ i $F$ ($f'<|s|<2f'$)</td><td>Més enllà de $2F'$</td><td>Real, invertida, més gran ($|m|>1$)</td><td>Projector</td></tr>
<tr><td><b>Al focus objecte $F$</b> ($|s|=f'$)</td><td><b>A l’infinit</b>: no es forma</td><td>Els raigs surten paral·lels</td><td>Focus, far, col·limador</td></tr>
<tr><td>Entre $F$ i la lent ($|s|<f'$)</td><td>Davant la lent, $s'<0$</td><td>Virtual, dreta, més gran ($m>1$)</td><td>Lupa</td></tr>
</tbody></table>
<p>A mesura que l’objecte s’acosta a $F$ des de fora, la imatge real s’allunya i es fa cada cop més gran; quan l’objecte passa entre el focus i la lent, la imatge esdevé virtual: apareix molt lluny, al mateix costat que l’objecte, i s’acosta a la lent a mesura que l’objecte s’hi acosta. Una lent divergent, en canvi, dona sempre una imatge virtual, dreta i més petita (figura 11.3).</p>
<div class="box ex"><div class="lead">Exemple resolt: què passa si l’objecte és al focus d’una lent convergent?</div>
<p>Una lent convergent té $f'=3{,}0$ cm i posem l’objecte a $s=-3{,}0$ cm, just al focus objecte. L’equació de les lents dona</p>
$$\frac{1}{s'}=\frac{1}{f'}+\frac{1}{s}=\frac{1}{3{,}0}+\frac{1}{-3{,}0}=0\quad\Rightarrow\quad s'\to\infty$$
<p>No hi ha cap valor finit de $s'$ que compleixi l’equació: la imatge «es forma a l’infinit». L’augment $m=s'/s$ tampoc no té un valor finit.</p>
<p><b>Diagrama de raigs</b> (figura 11.7). Des de l’extrem superior de l’objecte: (1) el raig paral·lel a l’eix es refracta passant per $F'$; (2) el raig que passa pel centre òptic no es desvia. Com que l’extrem de l’objecte és sobre el pla focal, aquests dos raigs —i qualsevol altre que surti del mateix punt— emergeixen <i>paral·lels entre si</i>. Rectes paral·leles no es tallen: no hi ha imatge real. Les prolongacions cap enrere també són paral·leles: tampoc no hi ha imatge virtual.</p>
<p><b>Interpretació física.</b> De cada punt de l’objecte en surt, després de la lent, un feix de raigs paral·lels (un feix col·limat). Així funcionen els fars i els focus (la bombeta es col·loca al focus d’una lent o d’un mirall). Un ull relaxat, enfocat a l’infinit, sí que forma a la retina una imatge nítida d’aquest feix: per això la manera més còmoda de fer servir una lupa és posar l’objecte al focus.</p></div>
[[fig-11.7]]
"""),
]
