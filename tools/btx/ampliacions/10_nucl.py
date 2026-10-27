"""Tema 10. Física nuclear: definicions, corba d'energia d'enllaç per nucleó, significat de la constant de desintegració, activitat."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _svg import Svg, INK, GREY, RED, BLUE, GREEN, ORANGE

F = "particules"

# energia d'enllaç per nucleó (MeV), valors de taules (AME)
DATA = [(2, 1.112, "²H"), (3, 2.573, ""), (4, 7.074, "⁴He"), (6, 5.332, ""), (7, 5.606, ""), (9, 6.463, ""), (11, 6.928, ""),
        (12, 7.680, ""), (14, 7.476, ""), (16, 7.976, "¹⁶O"), (20, 8.032, ""), (24, 8.261, ""), (28, 8.448, ""), (32, 8.493, ""),
        (40, 8.551, ""), (56, 8.790, "⁵⁶Fe"), (62, 8.795, ""), (84, 8.717, ""), (120, 8.505, ""), (138, 8.393, ""),
        (142, 8.346, ""), (208, 7.868, "²⁰⁸Pb"), (235, 7.591, "²³⁵U"), (238, 7.570, "")]


def fig_102():
    s = Svg(700, 380)
    x0, y0, w, h = 70, 320, 590, 280
    X = lambda A: x0 + A / 240 * w
    Y = lambda b: y0 - b / 9.5 * h
    s.arrow(x0, y0, x0 + w + 15, y0, GREY, 1.2, 8)
    s.arrow(x0, y0, x0, y0 - h - 15, GREY, 1.2, 8)
    for A in range(0, 241, 40):
        s.line(X(A), y0, X(A), y0 + 5, GREY, 1)
        s.text(X(A), y0 + 19, str(A), 11, "middle", GREY)
    for b in range(0, 10, 2):
        s.line(x0 - 5, Y(b), x0, Y(b), GREY, 1)
        s.text(x0 - 9, Y(b) + 4, str(b), 11, "end", GREY)
        if b:
            s.line(x0, Y(b), x0 + w, Y(b), "#e6e9ee", 1)
    s.text(x0 + w, y0 + 36, "nombre màssic A", 12, "end", INK)
    s.text(x0 - 50, y0 - h - 22, "E<tspan dy='4' font-size='9'>enllaç</tspan><tspan dy='-4'> / A (MeV)</tspan>", 12, "start", INK)
    pts = [(X(A), Y(b)) for A, b, _ in DATA]
    s.poly(pts, BLUE, 1.6)
    for (A, b, lab), (x, y) in zip(DATA, pts):
        s.circle(x, y, 3, BLUE, BLUE)
        if lab:
            dy = {"²H": 18, "⁴He": 4}.get(lab, -10)
            dx = {"²H": 8, "⁴He": -10}.get(lab, 0)
            s.text(x + dx, y + dy, lab, 12, "end" if dx < 0 else ("start" if dx else "middle"), INK, bold=True)
    s.arrow(X(10), Y(4.6), X(48), Y(4.6), RED, 2, 10)
    s.text(X(12), Y(4.6) - 8, "fusió", 13, "start", RED, bold=True)
    s.arrow(X(232), Y(5.6), X(125), Y(5.6), ORANGE, 2, 10)
    s.text(X(228), Y(5.6) - 8, "fissió", 13, "end", ORANGE, bold=True)
    s.text(X(150), Y(3.4), "Les dues reaccions acosten els nuclis", 12, "middle", INK)
    s.text(X(150), Y(3.4) + 16, "al màxim (més estables): s’allibera energia", 12, "middle", INK)
    return s.svg()


FIGS = {
    "fig-10.2": (fig_102(), "Energia d’enllaç per nucleó en funció del nombre màssic (valors experimentals d’alguns núclids). La corba "
                 "puja ràpidament als nuclis lleugers, té el màxim (uns 8,8 MeV) prop del ferro-56 i del níquel-62 i baixa lentament "
                 "als pesants. Fusionar nuclis lleugers o fissionar nuclis pesants dona productes amb més energia d’enllaç per "
                 "nucleó, és a dir, més estables i amb menys massa: la diferència de massa s’allibera com a energia."),
}

BLOCKS = [
    dict(file=F, id="nucl-defs", where=("before", '<div class="box ex"><div class="lead">Exemple resolt: Heli-4</div>'), html=r"""
<div class="box def"><div class="lead">Definicions</div><dl>
<dt>Núclid</dt><dd>Cada tipus de nucli, caracteritzat pel nombre de protons $Z$ i el nombre de neutrons $N$ (o pel nombre màssic $A=Z+N$).</dd>
<dt>Isòtops</dt><dd>Núclids amb el mateix $Z$ (mateix element, mateixes propietats químiques) i diferent $N$: $^{12}_{\ 6}\mathrm C$ i $^{14}_{\ 6}\mathrm C$.</dd>
<dt>Unitat de massa atòmica</dt><dd>$1\ \mathrm u$ és la dotzena part de la massa d’un àtom de $^{12}\mathrm C$: $1\ \mathrm u=1{,}6605\cdot10^{-27}$ kg, i la seva energia en repòs és $931{,}5$ MeV.</dd>
<dt>Energia d’enllaç</dt><dd>Energia que cal aportar a un nucli per separar-ne tots els nucleons fins a distàncies on ja no interaccionin. És la mateixa energia que s’allibera quan el nucli es forma a partir dels nucleons separats; per això el nucli té menys massa que els seus components: $E_{\text{enllaç}}=\Delta m\,c^2$.</dd>
<dt>Estabilitat</dt><dd>Un nucli és més estable com més gran és la seva energia d’enllaç <i>per nucleó</i> (figura 10.2): cada nucleó hi està més fortament lligat.</dd>
</dl></div>
"""),
    dict(file=F, id="nucl-corba", where=("end", "nucl-s1"), html=r"""
[[fig-10.2]]
<div class="box ex"><div class="lead">Exemple resolt: d’on surten els 200 MeV de la fissió?</div>
<p>L’urani-235 té una energia d’enllaç per nucleó d’uns $7{,}6$ MeV; els nuclis mitjans que en resulten (bari, criptó…) en tenen uns $8{,}5$ MeV. Cadascun dels 235 nucleons queda lligat uns $0{,}9$ MeV més fortament, de manera que s’alliberen aproximadament $235\cdot0{,}9\approx2\cdot10^{2}$ MeV per fissió. És l’ordre de magnitud correcte: la corba de la figura 10.2 permet estimar l’energia de qualsevol fissió o fusió.</p></div>
"""),
    dict(file=F, id="nucl-lambda", where=("before", "<p>Vida mitjana"), html=r"""
<div class="box def"><div class="lead">Què vol dir la constant de desintegració?</div>
<p>Si tenim $N$ nuclis, en un interval de temps petit $\Delta t$ se’n desintegra, de mitjana, una fracció $\lambda\,\Delta t$: $\Delta N\approx-\lambda N\,\Delta t$. El nombre de desintegracions per unitat de temps és proporcional al nombre de nuclis que queden. Una magnitud que disminueix a un ritme proporcional al seu valor decreix exponencialment: això és la llei $N=N_0e^{-\lambda t}$. Per la mateixa raó l’activitat, $A=\lambda N$, segueix la mateixa llei.</p>
<p>El període de semidesintegració i la vida mitjana són propietats de cada núclid: no depenen de la quantitat de mostra, de la temperatura ni de l’estat químic.</p></div>
<div class="box ex"><div class="lead">Exemple resolt: activitat d’una mostra de iode-131</div>
<p>Una mostra conté $1{,}0\ \mu$g de $^{131}\mathrm I$ ($T_{1/2}=8{,}02$ dies, massa molar $131\ \mathrm{g\cdot mol^{-1}}$).</p>
<p>Nombre de nuclis: $N_0=\dfrac{1{,}0\cdot10^{-6}}{131}\cdot6{,}022\cdot10^{23}=4{,}6\cdot10^{15}$. Constant de desintegració: $\lambda=\dfrac{\ln2}{T_{1/2}}=\dfrac{0{,}693}{8{,}02\cdot86\,400\ \text{s}}=1{,}00\cdot10^{-6}\ \mathrm{s^{-1}}$.</p>
<p>Activitat inicial: $A_0=\lambda N_0=4{,}6\cdot10^{9}$ Bq. Al cap de 30 dies: $A=A_0e^{-\lambda t}=4{,}6\cdot10^{9}\cdot e^{-0{,}0864\cdot30}=3{,}4\cdot10^{8}$ Bq (amb $\lambda=0{,}0864\ \text{dies}^{-1}$: el temps i $\lambda$ han d’anar en les mateixes unitats).</p></div>
"""),
]
