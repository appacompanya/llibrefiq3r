"""Fórmules clau destacades dins del text i files noves als formularis de final de tema."""

CHAP = {"mhs": "mhs", "ones": "ones", "fenomens-ondulatoris": "fen", "camp-gravitatori": "grav", "camp-electric": "elec",
        "camp-magnetic": "mag", "induccio": "ind", "quantica": "quant", "relativitat": "rel", "particules": "nucl", "optica": "opt"}


def clau(title, *formulas, note=""):
    f = "".join(f"$${x}$$" for x in formulas)
    n = f"<p>{note}</p>" if note else ""
    return f'<div class="box clau"><div class="lead">{title}</div>{f}{n}</div>'


def rows(*rs):
    return "".join(f"<tr><td>{a}</td><td>${b}$</td><td>{c}</td></tr>" for a, b, c in rs)


BLOCKS = [
    # ---------- fórmules clau dins del text ----------
    dict(file="fenomens-ondulatoris", id="clau-snell", where=("after", "<ul><li>Llei de la reflexió"), html=clau(
        "Fórmules clau: reflexió i refracció", r"\theta_1'=\theta_1\qquad\qquad n_1\sin\theta_1=n_2\sin\theta_2\qquad\qquad \frac{\sin\theta_1}{\sin\theta_2}=\frac{v_1}{v_2}=\frac{\lambda_1}{\lambda_2}",
        note="Angles mesurats respecte de la normal. La freqüència no canvia en passar d’un medi a un altre.")),
    dict(file="fenomens-ondulatoris", id="clau-interf", where=("replace", "<ul><li>Interferència constructiva"), html=clau(
        "Fórmules clau: condicions d’interferència (fonts en fase)",
        r"\text{Constructiva (màxim, les ones arriben en fase):}\qquad |r_1-r_2|=n\,\lambda",
        r"\text{Destructiva (mínim, arriben en oposició de fase):}\qquad |r_1-r_2|=(2n+1)\,\frac{\lambda}{2}",
        note="Amb $n=0,1,2,\\dots$ La diferència de camins $|r_1-r_2|$ és la diferència entre les distàncies del punt a cada font. Sense valor absolut: $r_1-r_2=n\\lambda$ amb $n\\in\\mathbb Z$ (també valors negatius).")),
    dict(file="fenomens-ondulatoris", id="clau-nodes", where=("after", "<ul><li>Nodes:"), html=clau(
        "Fórmules clau: nodes i ventres (x des d’un extrem fix)",
        r"\text{Nodes:}\quad x=n\,\frac{\lambda}{2}\qquad\qquad \text{Ventres:}\quad x=(2n+1)\,\frac{\lambda}{4}",
        note="Distància entre dos nodes (o dos ventres) consecutius: $\\lambda/2$; entre un node i el ventre següent: $\\lambda/4$.")),
    dict(file="fenomens-ondulatoris", id="clau-modes", where=("after", '<figure id="fig-3.6"'), html=r"""
<div class="box clau"><div class="lead">Fórmules clau: harmònics de cordes i tubs</div>
<p><b>Corda fixa–fixa i tub obert–obert</b> ($n=1,2,3,\dots$):</p>
$$L=n\,\frac{\lambda_n}{2}\qquad\qquad \lambda_n=\frac{2L}{n}\qquad\qquad f_n=n\,\frac{v}{2L}$$
<p><b>Tub tancat–obert</b> (només $n$ senar: $1,3,5,\dots$):</p>
$$L=n\,\frac{\lambda_n}{4}\qquad\qquad \lambda_n=\frac{4L}{n}\qquad\qquad f_n=n\,\frac{v}{4L}$$
<p>El mode $n=1$ és el fonamental, i $f_n=n\,f_1$.</p></div>
"""),
    dict(file="induccio", id="clau-flux", where=("after", "<p>El flux magnètic a través"), html=clau(
        "Fórmula clau: flux magnètic", r"\Phi=\vec B\cdot\vec S=B\,S\cos\theta\qquad(\text{bobina de }N\text{ espires: }N\,B\,S\cos\theta)",
        note="$\\theta$ és l’angle entre $\\vec B$ i la <i>normal</i> a la superfície. Unitat: weber, $1\\ \\mathrm{Wb}=1\\ \\mathrm{T\\cdot m^2}$.")),
    dict(file="camp-electric", id="clau-pot", where=("after", "<p>El potencial elèctric és"), html=clau(
        "Fórmules clau: energia potencial i potencial (amb el signe de les càrregues)",
        r"E_p=k\,\frac{Q\,q}{r}\qquad\qquad V=k\,\frac{Q}{r}\qquad\qquad W_{A\to B}=-\Delta E_p=-q\,(V_B-V_A)")),

    # ---------- files noves als formularis de final de tema ----------
    dict(file="mhs", id="fm-mhs", where=("fm", "mhs"), html=rows(
        ("Amplitud i fase inicial a partir de $x_0$ i $v_0$", r"A=\sqrt{x_0^2+v_0^2/\omega^2},\ \ \sin\varphi_0=x_0/A", "m; rad"),
        ("Molla vertical (allargament a l’equilibri)", r"\Delta l=\dfrac{mg}{k},\ \ T=2\pi\sqrt{\Delta l/g}", "m; s"),
        ("Treball d’una força constant", r"W=F\,\Delta r\cos\alpha", "J"),
        ("Teorema de l’energia cinètica", r"W_{\text{total}}=\Delta E_c", "J"),
        ("Força conservativa i energia potencial", r"W_{\text{cons}}=-\Delta E_p", "J"),
        ("Forces no conservatives", r"W_{\text{nc}}=\Delta E_m", "J"),
    )),
    dict(file="ones", id="fm-ones", where=("fm", "ones"), html=rows(
        ("Desfasament entre dos punts", r"\Delta\varphi=k\,\Delta x=2\pi\,\dfrac{\Delta x}{\lambda}", "rad"),
        ("Acceleració de vibració", r"a_y=-\omega^2y,\ \ a_{y,\text{màx}}=A\omega^2", "m·s<sup>−2</sup>"),
        ("Intensitat i amplitud", r"I\propto A^2,\ \ A\propto 1/r", "—"),
    )),
    dict(file="fenomens-ondulatoris", id="fm-fen", where=("fm", "fen"), html=rows(
        ("Huygens i Snell (amb velocitats)", r"\dfrac{\sin\theta_1}{\sin\theta_2}=\dfrac{v_1}{v_2}=\dfrac{\lambda_1}{\lambda_2}", "—"),
        ("Amplitud resultant (interferència)", r"A_R=\left|2A\cos\dfrac{\pi(r_2-r_1)}{\lambda}\right|", "m"),
        ("Ona estacionària (extrem fix a $x=0$)", r"y=-2A\sin(kx)\cos(\omega t)", "m"),
    )),
    dict(file="camp-gravitatori", id="fm-grav", where=("fm", "grav"), html=rows(
        ("Treball del camp entre $r_A$ i $r_B$", r"W_{A\to B}=GMm\left(\dfrac{1}{r_B}-\dfrac{1}{r_A}\right)", "J"),
        ("Treball d’un agent extern (sense variar $E_c$)", r"W_{\text{ext}}=\Delta E_p", "J"),
        ("Camp i potencial", r"g_r=-\dfrac{dV}{dr}", "N·kg<sup>−1</sup>"),
        ("Aproximació prop de la superfície ($h\\ll R$)", r"\Delta E_p\approx m\,g_0\,h", "J"),
        ("Energies en òrbita circular", r"E_c=\dfrac{GMm}{2r},\ E_p=-2E_c,\ E_m=-E_c", "J"),
        ("Canvi d’òrbita (treball dels motors)", r"W=\Delta E_m=\dfrac{GMm}{2}\left(\dfrac{1}{r_1}-\dfrac{1}{r_2}\right)", "J"),
    )),
    dict(file="camp-electric", id="fm-elec", where=("fm", "elec"), html=rows(
        ("Constant de Coulomb", r"k=\dfrac{1}{4\pi\varepsilon_0},\ \ \varepsilon_0=8{,}85\cdot10^{-12}", "C<sup>2</sup>·N<sup>−1</sup>·m<sup>−2</sup>"),
        ("Camp uniforme i diferència de potencial", r"E=\dfrac{|\Delta V|}{d},\ \ E_x=-\dfrac{dV}{dx}", "V·m<sup>−1</sup>"),
        ("Treball d’un agent extern", r"W_{\text{ext}}=\Delta E_p=q\,\Delta V", "J"),
        ("Energia d’un sistema de càrregues", r"E_p=k\sum_{\text{parelles}}\dfrac{q_iq_j}{r_{ij}}", "J"),
        ("Electronvolt", r"1\ \mathrm{eV}=1{,}602\cdot10^{-19}\ \mathrm J", "J"),
    )),
    dict(file="camp-magnetic", id="fm-mag", where=("fm", "mag"), html=rows(
        ("Força sobre una càrrega amb $\\vec E$ i $\\vec B$", r"\vec F=q\,(\vec E+\vec v\times\vec B)", "N"),
        ("Hèlix (velocitat obliqua)", r"r=\dfrac{mv_\perp}{|q|B},\ \ p=v_\parallel T", "m"),
        ("Espectròmetre de masses", r"r=\dfrac{1}{B}\sqrt{\dfrac{2m\,\Delta V}{|q|}}", "m"),
        ("Freqüència del ciclotró", r"f=\dfrac{|q|B}{2\pi m}", "Hz"),
    )),
    dict(file="induccio", id="fm-ind", where=("fm", "ind"), html=rows(
        ("Corrent induït", r"I=\dfrac{\varepsilon}{R}", "A"),
        ("Potència en la barra (fre magnètic)", r"P=F\,v=\dfrac{B^2l^2v^2}{R}=\varepsilon\,I", "W"),
        ("Transformador ideal (corrents)", r"\dfrac{I_1}{I_2}=\dfrac{N_2}{N_1},\ \ V_1I_1=V_2I_2", "—"),
        ("Pèrdues en una línia", r"P_{\text{pèrdues}}=I^2R=\left(\dfrac{P}{V}\right)^2R", "W"),
    )),
    dict(file="quantica", id="fm-quant", where=("fm", "quant"), html=rows(
        ("Quantitat de moviment d’un fotó", r"p=\dfrac{h}{\lambda}=\dfrac{E}{c}", "kg·m·s<sup>−1</sup>"),
        ("Nombre de fotons per segon", r"\dfrac{N}{t}=\dfrac{P}{hf}", "s<sup>−1</sup>"),
        ("Longitud d’ona llindar", r"\lambda_0=\dfrac{hc}{W_0}", "m"),
    )),
    dict(file="relativitat", id="fm-rel", where=("fm", "rel"), html=rows(
        ("Contracció de la longitud (qualitativa)", r"L=\dfrac{L_0}{\gamma}", "m"),
        ("Límit clàssic ($v\\ll c$)", r"E_c\approx\tfrac12m_0v^2", "J"),
    )),
    dict(file="particules", id="fm-nucl", where=("fm", "nucl"), html=rows(
        ("Nombre de nuclis d’una mostra", r"N=\dfrac{m}{M}\,N_A", "—"),
        ("Desintegració en funció de $T_{1/2}$", r"N=N_0\left(\tfrac12\right)^{t/T_{1/2}}", "—"),
        ("Energia d’enllaç per nucleó", r"E_{\text{enllaç}}/A", "MeV"),
    )),
    dict(file="optica", id="fm-opt", where=("fm", "opt"), html=rows(
        ("Focus objecte i focus imatge", r"f=-f'", "m"),
        ("Objecte al focus objecte", r"s=f\ \Rightarrow\ \dfrac{1}{s'}=0,\ s'\to\infty", "—"),
        ("Lupa ($|s|<f'$)", r"s'<0,\ m>1\ (\text{virtual, dreta, més gran})", "—"),
    )),
]

RENAMES = [("Fórmules clau (resum)", "Formulari del tema")]
