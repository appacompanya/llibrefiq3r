"""Problemes de tir, MCU, Newton, forces, energia i problemes mixtos."""
from banc import P, R, dec, vfmt, calc
from peces import EQ, fmt, solucio, valor

def eq(*trossos):
    return EQ("".join(trossos))


def _cap(tema, prefix):
    n = 0
    out = []

    def add(titol, niv, enun, res, sol, esq, esq_sol=None):
        nonlocal n
        n += 1
        out.append(P(tema, f"{prefix}.{n}", titol, niv, enun, res, sol, esq, esq_sol))

    return out, add


def tir():
    out, add = _cap("tir", "2")
    dades = [
        ("La pilota des del penya-segat", "senzill", "Des d’un penya-segat de 19,6 m es llança una pilota en horitzontal a 10 m/s.", 19.6, 10),
        ("El paquet de l’avió", "senzill", "Un avió deixa anar un paquet en horitzontal a 40 m/s des de 45 m d’altura. Es negligeix l’aire.", 45, 40),
        ("La font de la plaça", "mitjà", "Un rajolí surt en horitzontal a 3 m/s des de 1,25 m d’altura.", 1.25, 3),
        ("El salt de l’esquí de fira", "mitjà", "Un esquiador surt en horitzontal a 12 m/s d’un trampolí de 5 m.", 5, 12),
        ("La galleda del camió", "senzill", "De la caixa d’un camió, a 1,8 m del terra, cau una galleda amb velocitat horitzontal de 6 m/s.", 1.8, 6),
        ("El dron que deixa un paquet", "mitjà", "Un dron deixa un paquet amb velocitat horitzontal de 8 m/s des de 20 m.", 20, 8),
        ("La xinxeta de la taula", "senzill", "Una xinxeta llisca i surt per la vora d’una taula de 0,8 m d’altura a 2 m/s en horitzontal.", 0.8, 2),
        ("El porter", "mitjà", "Un porter treu de puny en horitzontal a 15 m/s des de 2,2 m d’altura.", 2.2, 15),
        ("L’aigua de la mànega", "senzill", "Una mànega llança aigua en horitzontal a 7 m/s des de 1,5 m.", 1.5, 7),
        ("El llibre de la finestra", "mitjà", "Un llibre surt en horitzontal a 4 m/s per una finestra situada a 7,2 m del pati.", 7.2, 4),
    ]
    for titol, niv, frase, h, v0 in dades:
        rt, rR = R("tir_h_t", {"h": h}, "t", "s"), R("tir_h_R", {"h": h, "v0": v0}, "R", "m")
        rvy, rv = R("tir_h_vy", {"h": h}, "vy", "m/s"), R("tir_h_v", {"h": h, "v0": v0}, "v", "m/s")
        add(titol, niv, f"<p>{frase} Quant triga a arribar a terra, quin abast fa i amb quin mòdul de velocitat arriba? Pren g = 9,8 m/s².</p>",
            [rt, rR, rvy, rv],
            solucio("El tir és horitzontal: la velocitat vertical inicial és zero i la horitzontal no canvia. El temps és el d’una caiguda des d’aquesta altura.",
                    eq(r"t = \sqrt{2h/g}") + eq(r"R = v_0 t") + eq(r"v = \sqrt{v_0^2 + v_y^2}"),
                    eq("t = ", vfmt(rt)) + eq("R = ", vfmt(rR)) + eq("v_y = ", vfmt(rvy)) + eq("v = ", vfmt(rv)),
                    f"Triga {valor(rt['valor'], rt['decimals'], 's')}, l’abast és {valor(rR['valor'], rR['decimals'], 'm')} i arriba a {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("tir_h", {"h": f"h = {fmt(h, dec(h))} m", "v": f"v₀ = {fmt(v0, dec(v0))} m/s"},
             "Tir horitzontal: la component horitzontal es manté i la vertical creix."))

    dades = [
        ("El llançador de pes", "senzill", "Es llança un projectil des del terra a 20 m/s amb un angle de 30°.", 20, 30),
        ("El xut a 45°", "senzill", "Una pilota surt del terra a 14 m/s i a 45°.", 14, 45),
        ("La font obliqua", "mitjà", "Un rajolí de font surt a 8 m/s i a 60°.", 8, 60),
        ("El servei curt", "mitjà", "Una pilota de tennis surt del terra a 25 m/s i a 20°.", 25, 20),
        ("L’obús de fira", "mitjà", "Un obús de fira surt a 30 m/s i a 50°.", 30, 50),
        ("La pedra a 37°", "senzill", "Es llança una pedra des del terra a 15 m/s i a 37°.", 15, 37),
        ("El globus d’aigua", "mitjà", "Un globus d’aigua surt a 10 m/s i a 55°.", 10, 55),
        ("El llançament a 53°", "mitjà", "Un atleta llança un objecte a 18 m/s i a 53° des del terra.", 18, 53),
        ("La cistella llunyana", "complet", "Una pilota surt del terra a 12 m/s i a 40°.", 12, 40),
        ("El coet de fira", "complet", "Un coet de fira surt a 22 m/s i a 65°.", 22, 65),
        ("Dos angles, el petit", "mitjà", "Es dispara un projectil a 16 m/s i a 25° des del terra.", 16, 25),
        ("El llançament suau", "senzill", "Una pilota surt a 9 m/s i a 35°.", 9, 35),
    ]
    for titol, niv, frase, v0, th in dades:
        rt, rH, rR = R("tir_t", {"v0": v0, "theta": th}, "t", "s"), R("tir_H", {"v0": v0, "theta": th}, "H", "m"), R("tir_R", {"v0": v0, "theta": th}, "R", "m")
        add(titol, niv, f"<p>{frase} Calcula el temps de vol, l’alçada màxima i l’abast. Es negligeix l’aire i g = 9,8 m/s². L’angle es mesura des de l’horitzontal.</p>",
            [rt, rH, rR],
            solucio("El projectil surt i torna al mateix nivell. La component horitzontal de la velocitat és constant i la vertical s’anul·la a dalt de tot.",
                    eq(r"t = 2 v_0 \sin\theta / g") + eq(r"H = (v_0 \sin\theta)^2 / (2g)") + eq(r"R = v_0^2 \sin 2\theta / g"),
                    eq("t = ", vfmt(rt)) + eq("H = ", vfmt(rH)) + eq("R = ", vfmt(rR)),
                    f"El temps de vol és {valor(rt['valor'], rt['decimals'], 's')}, l’alçada màxima és {valor(rH['valor'], rH['decimals'], 'm')} i l’abast és {valor(rR['valor'], rR['decimals'], 'm')}."),
            ("tir_p", {"theta": th, "h": "H", "r": "R"}, f"Trajectòria amb angle de sortida de {th}°."))

    # punt concret i velocitat inicial a partir de l'abast
    for titol, v0, th, t in [
        ("On és als 0,5 s", 20, 30, 0.5),
        ("On és als 1 s", 14, 45, 1),
        ("On és als 0,8 s", 18, 40, 0.8),
        ("On és als 0,4 s", 25, 50, 0.4),
    ]:
        rx, ry = R("tir_x", {"v0": v0, "theta": th, "t": t}, "x", "m"), R("tir_y", {"v0": v0, "theta": th, "t": t}, "y", "m")
        rv = R("tir_vmod", {"v0": v0, "theta": th, "t": t}, "v", "m/s")
        add(titol, "complet",
            f"<p>Un projectil surt de l’origen a {fmt(v0, dec(v0))} m/s i a {th}°. On és i quin mòdul de velocitat porta al cap de {fmt(t, dec(t))} s? g = 9,8 m/s².</p>",
            [rx, ry, rv],
            solucio("Separem el moviment. La posició horitzontal només depèn de la component horitzontal; la vertical, de la component vertical i de g.",
                    eq(r"x = (v_0 \cos\theta) t") + eq(r"y = (v_0 \sin\theta) t - \frac{1}{2} g t^2"),
                    eq("x = ", vfmt(rx)) + eq("y = ", vfmt(ry)) + eq("v = ", vfmt(rv)),
                    f"És al punt ({valor(rx['valor'], rx['decimals'], 'm')}, {valor(ry['valor'], ry['decimals'], 'm')}) i el mòdul de la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("tir_p", {"theta": th, "h": "y", "r": "x"}, "Es demana la posició en un instant concret de la trajectòria."))

    for titol, Rabs, th in [
        ("Quina velocitat cal per fer 20 m", 20, 45),
        ("Arribar a 30 m a 30°", 30, 30),
        ("Un abast de 15 m a 60°", 15, 60),
        ("Cistella a 12 m i 40°", 12, 40),
    ]:
        rv = R("tir_v0_R", {"R": Rabs, "theta": th}, "v", "m/s")
        add(titol, "complet",
            f"<p>Es vol un abast de {fmt(Rabs, dec(Rabs))} m sobre el terra amb un angle de {th}°. Quina velocitat inicial cal? g = 9,8 m/s².</p>",
            [rv],
            solucio("L’abast sobre el pla de sortida determina la velocitat si l’angle és conegut.",
                    eq(r"v_0 = \sqrt{R g / \sin 2\theta}"),
                    eq("v_0 = ", vfmt(rv)),
                    f"Cal llançar a {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("tir_p", {"theta": th, "h": "H", "r": f"R = {fmt(Rabs, dec(Rabs))} m"}, "L’abast és una dada i es busca la velocitat de sortida."))
    return out


def mcu():
    out, add = _cap("mcu", "3")
    for titol, T in [
        ("La roda del molí", 2), ("El disc del laboratori", 0.5), ("La sínia", 4),
        ("El ventilador lent", 0.2), ("La plataforma", 8), ("El plat de gir", 1.25),
    ]:
        rw, rf = R("omega_T", {"T": T}, "w", "rad/s"), R("freq_T", {"T": T}, "f", "Hz")
        add(titol, "senzill", f"<p>Un mòbil fa una volta cada {fmt(T, dec(T))} s amb rapidesa constant. Calcula la freqüència i la velocitat angular.</p>",
            [rw, rf],
            solucio("El període és el temps d’una volta. La freqüència n’és l’invers i la velocitat angular compta l’angle de 2π radiants de cada volta.",
                    eq(r"f = 1/T") + eq(r"\omega = 2\pi / T"),
                    eq("f = ", vfmt(rf)) + eq("\\omega = ", vfmt(rw)),
                    f"La freqüència és {valor(rf['valor'], rf['decimals'], 'Hz')} i la velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')}."),
            ("mcu", {"r": "r"}, "Una volta completa correspon a un angle de 2π radiants."))
    for titol, f, r in [("El torn", 2, 0.4), ("La politja", 0.5, 0.2), ("El disc compacte", 5, 0.06), ("La centrifugadora", 20, 0.12)]:
        rw, rv = R("omega_f", {"f": f}, "w", "rad/s"), R("v_wr", {"omega": calc("omega_f", {"f": f}), "r": r}, "v", "m/s")
        add(titol, "mitjà", f"<p>Una peça gira a {fmt(f, dec(f))} Hz. Un punt situat a {fmt(r, dec(r))} m de l’eix, quina velocitat lineal porta?</p>",
            [rw, rv],
            solucio("Primer es passa de la freqüència a la velocitat angular i després es multiplica pel radi.",
                    eq(r"\omega = 2\pi f") + eq(r"v = \omega r"),
                    eq("\\omega = ", vfmt(rw)) + eq("v = ", vfmt(rv)),
                    f"La velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')} i la velocitat lineal és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("v_omega", {}, "La velocitat lineal és tangent i val ωr."))
    for titol, v, r in [
        ("El cotxe a la rotonda", 12, 30), ("La bicicleta al velòdrom", 8, 20),
        ("El satèl·lit de fira", 6, 8), ("La pedra de la fona", 15, 0.8),
        ("El tren al revolt", 20, 200), ("El patinador", 4, 5),
    ]:
        rw, ra = R("omega_vr", {"v": v, "r": r}, "w", "rad/s"), R("ac_v", {"v": v, "r": r}, "a", "m/s²")
        add(titol, "mitjà", f"<p>Un mòbil va a {fmt(v, dec(v))} m/s per una circumferència de radi {fmt(r, dec(r))} m, amb rapidesa constant. Calcula la velocitat angular i l’acceleració centrípeta.</p>",
            [rw, ra],
            solucio("La rapidesa és constant, però el vector velocitat gira. L’acceleració centrípeta apunta al centre.",
                    eq(r"\omega = v/r") + eq(r"a_c = v^2/r"),
                    eq("\\omega = ", vfmt(rw)) + eq("a_c = ", vfmt(ra)),
                    f"La velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')} i l’acceleració centrípeta és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
            ("mcu_vec", {}, "Velocitat tangent i acceleració centrípeta cap al centre."))
    for titol, w, r in [("El molinet", 10, 0.3), ("L’eix del motor", 40, 0.05), ("La grua que gira", 0.4, 25), ("El carrusel", 1.2, 6)]:
        rv, ra = R("v_wr", {"omega": w, "r": r}, "v", "m/s"), R("ac_w", {"omega": w, "r": r}, "a", "m/s²")
        add(titol, "senzill", f"<p>Un punt gira amb velocitat angular constant de {fmt(w, dec(w))} rad/s a {fmt(r, dec(r))} m de l’eix. Quina velocitat i quina acceleració centrípeta té?</p>",
            [rv, ra],
            solucio("Amb la velocitat angular i el radi es troben la velocitat lineal i l’acceleració centrípeta.",
                    eq(r"v = \omega r") + eq(r"a_c = \omega^2 r"),
                    eq("v = ", vfmt(rv)) + eq("a_c = ", vfmt(ra)),
                    f"La velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')} i l’acceleració centrípeta és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
            ("v_omega", {}, "Relació entre la velocitat angular i la velocitat lineal."))
    for titol, r, th, t in [("L’arc de la porta", 2, 1.2, 0.4), ("El braç del robot", 0.5, 2, 0.5), ("La agulla", 0.08, 3, 0.2), ("La cinquena part de volta", 4, 1.256637, 2)]:
        rw, rs = R("omega_theta", {"theta": th, "t": t}, "w", "rad/s"), R("arc", {"r": r, "theta": th}, "s", "m")
        add(titol, "mitjà", f"<p>Un punt d’una circumferència de radi {fmt(r, dec(r))} m recorre un angle de {fmt(th, 2)} rad en {fmt(t, dec(t))} s, a ritme constant. Calcula la velocitat angular i la longitud de l’arc.</p>",
            [rw, rs],
            solucio("L’angle ja és en radiants. La velocitat angular és l’angle partit pel temps i l’arc és el radi multiplicat per l’angle.",
                    eq(r"\omega = \theta / t") + eq(r"s = r \theta"),
                    eq("\\omega = ", vfmt(rw)) + eq("s = ", vfmt(rs)),
                    f"La velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')} i l’arc fa {valor(rs['valor'], rs['decimals'], 'm')}."),
            ("mcu", {"r": f"r = {fmt(r, dec(r))} m"}, "L’arc recorregut és rθ, amb l’angle en radiants."))
    for titol, v, r in [("La formiga al disc", 0.5, 0.1), ("El punt del pneumàtic", 18, 0.3), ("L’hèlix", 30, 0.4), ("El tiovivo", 3, 4)]:
        ra = R("ac_v", {"v": v, "r": r}, "a", "m/s²")
        rT = R("T_vr", {"v": v, "r": r}, "T", "s")
        add(titol, "mitjà", f"<p>Un punt es mou a {fmt(v, dec(v))} m/s per una circumferència de radi {fmt(r, dec(r))} m. Calcula l’acceleració centrípeta i el període.</p>",
            [ra, rT],
            solucio("L’acceleració centrípeta depèn de la rapidesa i del radi. El període és el temps d’una volta, la longitud de la circumferència dividida per la rapidesa.",
                    eq(r"a_c = v^2 / r") + eq(r"T = 2\pi r / v"),
                    eq("a_c = ", vfmt(ra)) + eq("T = ", vfmt(rT)),
                    f"L’acceleració centrípeta és {valor(ra['valor'], ra['decimals'], 'm/s²')} i el període és {valor(rT['valor'], rT['decimals'], 's')}."),
            ("mcu_vec", {}, "La rapidesa és constant i l’acceleració apunta al centre."))
    return out


def newton():
    out, add = _cap("newton", "4")
    for titol, m, a in [
        ("Empènyer el carretó", 20, 0.5), ("El disc d’hoquei", 0.2, 4), ("El cotxe", 1200, 1.5),
        ("La caixa", 8, 0.8), ("El llibre", 1.2, 3), ("La pilota de bòling", 5, 2),
        ("El vagó", 8000, 0.2), ("El paquet", 3, 1.4),
    ]:
        r = R("f_ma", {"m": m, "a": a}, "F", "N")
        add(titol, "senzill", f"<p>Una força resultant de direcció constant dona a un cos de {fmt(m, dec(m))} kg una acceleració de {fmt(a, dec(a))} m/s². Quant val la resultant?</p>",
            [r],
            solucio("La segona llei diu que la força resultant és la massa multiplicada per l’acceleració. Resultant i acceleració tenen el mateix sentit.",
                    eq(r"F = m a"),
                    eq("F = ", vfmt(r)),
                    f"La força resultant és {valor(r['valor'], r['decimals'], 'N')}."),
            ("fma", {}, "Amb la mateixa força, la massa petita accelera més. Aquí la massa i l’acceleració són dades."))
    for titol, F, m in [
        ("Estirar el trineu", 40, 10), ("El io-io", 0.6, 0.05), ("La barca", 200, 80),
        ("El calaix", 15, 6), ("L’elefant de joguina", 2, 0.4), ("El contenidor", 500, 250),
    ]:
        r = R("a_fm", {"F": F, "m": m}, "a", "m/s²")
        add(titol, "senzill", f"<p>Una força resultant de {fmt(F, dec(F))} N actua sobre un cos de {fmt(m, dec(m))} kg. Quina acceleració li dona?</p>",
            [r],
            solucio("Aïllem l’acceleració de la segona llei. No hi ha cap altra força: la dada ja és la resultant.",
                    eq(r"a = F/m"),
                    eq("a = ", vfmt(r)),
                    f"L’acceleració és {valor(r['valor'], r['decimals'], 'm/s²')}."),
            ("dcl", {"fregament": False, "força": True, "F": "F"}, "La força F és, en aquest enunciat, la resultant."))
    for titol, m in [("L’alumne", 60), ("La motxilla", 4), ("El professor", 75), ("La poma", 0.2), ("El cotxe petit", 900), ("El llibre de física", 0.8)]:
        r = R("pes", {"m": m}, "P", "N")
        add(titol, "senzill", f"<p>Quan pesa, en newtons, un cos de {fmt(m, dec(m))} kg a prop de la Terra? Pren g = 9,8 m/s². La massa no canvia si el cos està quiet o en moviment.</p>",
            [r],
            solucio("El pes és la força d’atracció de la Terra. No s’ha de confondre amb la massa: el pes es mesura en newtons.",
                    eq(r"P = m g"),
                    eq("P = ", vfmt(r)),
                    f"Pesa {valor(r['valor'], r['decimals'], 'N')}."),
            ("dcl", {"fregament": False, "força": False}, "El pes és vertical i cap avall. La normal, si el cos és damunt un pla, el compensa quan no hi ha acceleració vertical."))
    for titol, F, a in [("Quina massa", 30, 2), ("El bloc desconegut", 12, 0.5), ("La sonda", 4, 0.2), ("El carret", 7, 1.4)]:
        r = R("m_fa", {"F": F, "a": a}, "m", "kg")
        add(titol, "mitjà", f"<p>Una força resultant de {fmt(F, dec(F))} N produeix una acceleració de {fmt(a, dec(a))} m/s². Quina massa té el cos?</p>",
            [r],
            solucio("De la segona llei s’aïlla la massa. La força de l’enunciat és la resultant.",
                    eq(r"m = F/a"),
                    eq("m = ", vfmt(r)),
                    f"La massa és {valor(r['valor'], r['decimals'], 'kg')}."),
            ("fma", {}, "La massa relaciona la força resultant amb l’acceleració."))
    # parells: el mòdul és el pes o la normal
    for titol, m in [("El llibre sobre la taula", 1.5), ("La caixa al terra", 12), ("L’ampolla", 0.5), ("El banc del parc", 30)]:
        r = R("pes", {"m": m}, "F", "N")
        add(titol, "mitjà",
            f"<p>Un cos de {fmt(m, dec(m))} kg està en repòs damunt una taula horitzontal. Quant val la normal? I quin mòdul té la força amb què el cos empeny la taula, que és la parella de la normal?</p>",
            [r],
            solucio("En vertical la resultant és zero, de manera que la normal iguala el pes. Per la tercera llei, la força del cos sobre la taula té el mateix mòdul que la normal i actua sobre la taula, no sobre el cos.",
                    eq(r"N = m g"),
                    eq("N = ", vfmt(r)),
                    f"La normal i la força sobre la taula valen, cadascuna, {valor(r['valor'], r['decimals'], 'N')}."),
            ("parells", {}, "El pes i la normal actuen tots dos sobre el cos. El parell de la normal actua sobre la taula."))
    return out


def forces():
    out, add = _cap("forces", "5")
    for titol, F, m in [("El trineu al gel llis", 24, 8), ("La caixa al terra polit", 10, 4), ("El disc a la taula d’aire", 0.3, 0.15), ("El vagó sense fregament", 400, 200)]:
        r = R("a_hor", {"F": F, "m": m}, "a", "m/s²")
        rn = R("pes", {"m": m}, "N", "N")
        add(titol, "senzill", f"<p>Una força horitzontal de {fmt(F, dec(F))} N estira un cos de {fmt(m, dec(m))} kg damunt un pla horitzontal llis. Quina acceleració té i quant val la normal?</p>",
            [r, rn],
            solucio("El pla és llis: no hi ha fregament. En vertical el pes i la normal es compensen. En horitzontal la resultant és la força aplicada.",
                    eq(r"N = m g") + eq(r"a = F/m"),
                    eq("N = ", vfmt(rn)) + eq("a = ", vfmt(r)),
                    f"La normal és {valor(rn['valor'], rn['decimals'], 'N')} i l’acceleració és {valor(r['valor'], r['decimals'], 'm/s²')}."),
            ("dcl", {"fregament": False, "força": True, "F": "F"}, "Pla horitzontal llis. La normal equilibra el pes."))
    for titol, F, m, mu in [
        ("La caixa que rellisca", 40, 10, 0.2), ("El sofà", 80, 20, 0.3), ("El bloc del laboratori", 12, 2, 0.25),
        ("El trineu amb sorra", 50, 8, 0.4), ("La nevera", 100, 40, 0.15), ("El calaix pesant", 30, 5, 0.35),
        ("El palet", 200, 50, 0.2), ("La maleta", 25, 6, 0.1),
    ]:
        r = R("a_hor_f", {"F": F, "m": m, "mu": mu}, "a", "m/s²")
        rf = R("freg_c", {"mu": mu, "N": calc("pes", {"m": m})}, "f", "N")
        add(titol, "mitjà", f"<p>Una força horitzontal de {fmt(F, dec(F))} N arrossega un cos de {fmt(m, dec(m))} kg per un pla horitzontal. El coeficient de fregament cinètic és {fmt(mu, dec(mu))} i el cos ja llisca. Quina acceleració té?</p>",
            [rf, r],
            solucio("El cos llisca, de manera que el fregament és el cinètic i val μN. En un pla horitzontal la normal iguala el pes. La resultant horitzontal és F menys el fregament, en el sentit de F.",
                    eq(r"f = \mu m g") + eq(r"a = (F - f)/m"),
                    eq("f = ", vfmt(rf)) + eq("a = ", vfmt(r)),
                    f"El fregament és {valor(rf['valor'], rf['decimals'], 'N')} i l’acceleració és {valor(r['valor'], r['decimals'], 'm/s²')}."),
            ("dcl", {"fregament": True, "força": True, "F": "F"}, "Fregament cinètic, oposat al moviment, i força aplicada."))
    for titol, m, alpha, freg, mu in [
        ("El pla de 30° llis", 2, 30, False, 0),
        ("El pla de 45° llis", 5, 45, False, 0),
        ("El pla de 20° llis", 3, 20, False, 0),
        ("El pla de 53° llis", 4, 53, False, 0),
        ("Baixa amb fregament, 30°", 2, 30, True, 0.2),
        ("Baixa amb fregament, 37°", 6, 37, True, 0.1),
        ("Baixa amb fregament, 45°", 3, 45, True, 0.25),
        ("Baixa amb fregament, 25°", 8, 25, True, 0.15),
    ]:
        if not freg:
            ra, rn = R("a_inclin_0", {"alpha": alpha}, "a", "m/s²"), R("N_inclin", {"m": m, "alpha": alpha}, "N", "N")
            add(titol, "mitjà", f"<p>Un bloc de {fmt(m, dec(m))} kg baixa per un pla inclinat llis de {alpha}°. Quina acceleració té i quant val la normal?</p>",
                [ra, rn],
                solucio("No hi ha fregament. Amb l’eix x pendent avall, la component del pes al llarg del pla és mg sin α i la normal equilibra mg cos α.",
                        eq(r"a = g \sin\alpha") + eq(r"N = m g \cos\alpha"),
                        eq("a = ", vfmt(ra)) + eq("N = ", vfmt(rn)),
                        f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la normal és {valor(rn['valor'], rn['decimals'], 'N')}."),
                ("inclinat", {"alpha": alpha, "fregament": False}, "Pla inclinat llis. El pes es descompon al llarg del pla i en la direcció de la normal."),
                ("dcl_inclinat", {"alpha": alpha, "fregament": False}, "Diagrama de cos lliure amb els eixos del pla."))
        else:
            ra, rn = R("a_inclin_f", {"alpha": alpha, "mu": mu}, "a", "m/s²"), R("N_inclin", {"m": m, "alpha": alpha}, "N", "N")
            rf = R("freg_c", {"mu": mu, "N": rn["valor"]}, "f", "N")
            add(titol, "complet", f"<p>Un bloc de {fmt(m, dec(m))} kg baixa lliscant per un pla de {alpha}°. El coeficient de fregament cinètic és {fmt(mu, dec(mu))}. Quina acceleració té?</p>",
                [rn, rf, ra],
                solucio("El bloc baixa, de manera que el fregament cinètic apunta pendent amunt. La normal és mg cos α i el fregament és μN.",
                        eq(r"a = g(\sin\alpha - \mu\cos\alpha)"),
                        eq("N = ", vfmt(rn)) + eq("f = ", vfmt(rf)) + eq("a = ", vfmt(ra)),
                        f"La normal és {valor(rn['valor'], rn['decimals'], 'N')}, el fregament és {valor(rf['valor'], rf['decimals'], 'N')} i l’acceleració pendent avall és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
                ("inclinat", {"alpha": alpha, "fregament": True}, "El fregament és paral·lel al pla i s’oposa a la baixada."),
                ("dcl_inclinat", {"alpha": alpha, "fregament": True}, "Diagrama de cos lliure del bloc que baixa."))
    for titol, m1, m2 in [("Atwood 2 i 3 kg", 2, 3), ("Atwood 1 i 3 kg", 1, 3), ("Atwood 4 i 6 kg", 4, 6), ("Atwood 1,5 i 2,5 kg", 1.5, 2.5)]:
        ra, rT = R("atwood_a", {"m1": m1, "m2": m2}, "a", "m/s²"), R("atwood_T", {"m1": m1, "m2": m2}, "T", "N")
        add(titol, "complet", f"<p>Dos blocs de {fmt(m1, dec(m1))} kg i {fmt(m2, dec(m2))} kg pengen d’una corda que passa per una politja ideal. Quina acceleració té el sistema i quant val la tensió? El bloc gros baixa.</p>",
            [ra, rT],
            solucio("La politja és ideal: la tensió és la mateixa als dos costats i la corda no té massa. Per al sistema, la resultant és el pes gros menys el pes petit.",
                    eq(r"a = (m_2 - m_1)g / (m_1 + m_2)") + eq(r"T = 2 m_1 m_2 g / (m_1 + m_2)"),
                    eq("a = ", vfmt(ra)) + eq("T = ", vfmt(rT)),
                    f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la tensió és {valor(rT['valor'], rT['decimals'], 'N')}."),
            ("atwood", {"m1": f"{fmt(m1, dec(m1))} kg", "m2": f"{fmt(m2, dec(m2))} kg"}, "El bloc de més massa baixa."))
    for titol, M, m, mu in [("Taula llisa", 4, 1, 0), ("Taula llisa, un altre cas", 6, 2, 0), ("Taula amb fregament", 4, 2, 0.2), ("Taula amb fregament petit", 5, 2, 0.1)]:
        ra = R("penjant_a", {"M": M, "m": m, "mu": mu}, "a", "m/s²")
        rT = R("penjant_T", {"M": M, "m": m, "mu": mu}, "T", "N")
        frase = "la taula és llisa" if mu == 0 else f"el coeficient de fregament cinètic amb la taula és {fmt(mu, dec(mu))} i el bloc de la taula llisca"
        add(titol, "complet", f"<p>Un bloc de {fmt(M, dec(M))} kg és damunt una taula i va lligat, amb una corda i una politja a la vora, a un bloc de {fmt(m, dec(m))} kg que penja. En aquest cas {frase}. Calcula l’acceleració i la tensió.</p>",
            [ra, rT],
            solucio("El pes que accelera el sistema és el del bloc que penja. Si hi ha fregament, es resta a la resultant. La tensió s’obté del diagrama del bloc que penja.",
                    eq(r"a = (m g - \mu M g)/(M + m)"),
                    eq("a = ", vfmt(ra)) + eq("T = ", vfmt(rT)),
                    f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la tensió és {valor(rT['valor'], rT['decimals'], 'N')}."),
            ("taula", {"M": f"{fmt(M, dec(M))} kg", "m": f"{fmt(m, dec(m))} kg"}, "Un bloc damunt la taula i un altre que penja."))
    for titol, k, x in [("La molla del laboratori", 200, 0.05), ("La molla de la porta", 80, 0.12)]:
        r = R("molla_F", {"k": k, "x": x}, "F", "N")
        add(titol, "senzill", f"<p>Una molla de constant {fmt(k, dec(k))} N/m s’allarga {fmt(x, dec(x))} m. Quina força fa?</p>",
            [r],
            solucio("La força elàstica és proporcional a la deformació i s’oposa a l’allargament: la molla estira cap endins.",
                    eq(r"F = k x"),
                    eq("F = ", vfmt(r)),
                    f"La força és {valor(r['valor'], r['decimals'], 'N')}."),
            ("molla", {}, "La deformació x es mesura des de la longitud natural."))
    for titol, m, v, r in [("La corda que gira", 0.4, 3, 0.8), ("El cotxe al revolt pla", 1000, 12, 40)]:
        if "corda" in titol:
            rf = R("ac_necessaria", {"m": m, "v": v, "r": r}, "T", "N")
            add(titol, "mitjà", f"<p>Una massa de {fmt(m, dec(m))} kg gira, lligada a una corda de {fmt(r, dec(r))} m, a {fmt(v, dec(v))} m/s en un pla horitzontal llis. Quant val la tensió?</p>",
                [rf],
                solucio("En el pla horitzontal l’única força cap al centre és la tensió. Aquesta força és la resultant centrípeta.",
                        eq(r"T = m v^2 / r"),
                        eq("T = ", vfmt(rf)),
                        f"La tensió és {valor(rf['valor'], rf['decimals'], 'N')}."),
                ("corda", {"r": f"r = {fmt(r, dec(r))} m"}, "La tensió apunta cap al centre i la velocitat és tangent."))
        else:
            rv = R("vmax_revolt", {"mu": 0.4, "r": r}, "v", "m/s")
            add("El revolt pla", "complet", f"<p>Un cotxe pren un revolt pla de radi {fmt(r, dec(r))} m. El coeficient de fregament estàtic entre les rodes i l’asfalt és 0,4. Quina és la velocitat màxima per no derrapar?</p>",
                [rv],
                solucio("Al límit, el fregament estàtic màxim fa de força centrípeta i la normal iguala el pes.",
                        eq(r"\mu m g = m v^2 / r"),
                        eq("v = ", vfmt(rv)),
                        f"La velocitat màxima és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
                ("revolt", {}, "Vist des de dalt: el fregament apunta cap al centre de la corba."))
    rp = R("theta_peralt", {"v": 20, "r": 50}, "theta", "°")
    add("El peralt", "complet", "<p>Un revolt de 50 m de radi està peraltat i s’hi pot passar a 20 m/s sense fer servir el fregament. Quin angle de peralt cal? g = 9,8 m/s².</p>",
        [rp],
        solucio("Sense fregament, la component horitzontal de la normal és la força centrípeta. L’angle compleix tan θ = v²/(r g).",
                eq(r"\theta = \arctan(v^2 /(r g))"),
                eq("\\theta = ", vfmt(rp)),
                f"L’angle de peralt és {valor(rp['valor'], rp['decimals'], '°')}."),
        ("peralt", {"theta": max(15, int(round(rp["valor"])))}, "La normal és perpendicular a la calçada peraltada."))
    rn = R("N_loop_dalt", {"m": 800, "v": 12, "r": 8}, "N", "N")
    add("El lòpping", "complet", "<p>Un cotxe de 800 kg passa pel capdamunt d’un lòpping de 8 m de radi a 12 m/s. Quant val la normal en aquest punt?</p>",
        [rn],
        solucio("Al capdamunt, el pes i la normal apunten tots dos cap al centre. La seva suma és la força centrípeta.",
                eq(r"N + m g = m v^2 / r"),
                eq("N = ", vfmt(rn)),
                f"La normal és {valor(rn['valor'], rn['decimals'], 'N')}."),
        ("loop", {}, "Al capdamunt el pes i la normal apunten cap al centre."))
    return out


def energia():
    out, add = _cap("energia", "6")
    for titol, m, h in [
        ("La pedra que cau", 0.2, 19.6), ("El llibre que rellisca del prestatge", 1, 1.25),
        ("El salt", 60, 2), ("La poma", 0.15, 4.9), ("El paquet", 3, 10), ("La clau", 0.05, 5),
    ]:
        rv, re = R("v_caiguda_e", {"h": h}, "v", "m/s"), R("ep", {"m": m, "h": h}, "E", "J")
        add(titol, "senzill", f"<p>Un cos de {fmt(m, dec(m))} kg cau des del repòs un desnivell de {fmt(h, dec(h))} m. Quina velocitat porta en arribar a baix i quina energia potencial ha perdut? Només actua el pes. g = 9,8 m/s². Pren energia potencial zero a baix.</p>",
            [rv, re],
            solucio("Només treballa el pes, de manera que l’energia mecànica es conserva. A dalt tot és potencial i a baix tot és cinètic, si el zero d’altura és a baix.",
                    eq(r"m g h = \frac{1}{2} m v^2"),
                    eq("E_p = ", vfmt(re)) + eq("v = ", vfmt(rv)),
                    f"Perd {valor(re['valor'], re['decimals'], 'J')} d’energia potencial i arriba a {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("barres", {"etapes": [("dalt", 0, 100), ("baix", 100, 0)]}, "L’energia potencial inicial es converteix en cinètica."))
    for titol, m, v in [
        ("Llançar la pilota", 0.4, 8), ("El coet petit", 0.2, 14), ("La fletxa", 0.05, 20),
        ("La pedra", 0.3, 9.8), ("El paquet cap amunt", 2, 6), ("La bola", 1, 4),
    ]:
        rh = R("h_llanc_e", {"v": v}, "h", "m")
        re = R("ec", {"m": m, "v": v}, "E", "J")
        add(titol, "senzill", f"<p>Es llança un cos de {fmt(m, dec(m))} kg verticalment cap amunt a {fmt(v, dec(v))} m/s. Quina alçada màxima assoleix? Només actua el pes.</p>",
            [rh, re],
            solucio("A dalt la velocitat és zero. L’energia cinètica inicial es converteix tota en potencial. El nivell zero és el punt de llançament.",
                    eq(r"\frac{1}{2} m v^2 = m g h"),
                    eq("E_c = ", vfmt(re)) + eq("h = ", vfmt(rh)),
                    f"L’energia cinètica inicial és {valor(re['valor'], re['decimals'], 'J')} i l’alçada màxima és {valor(rh['valor'], rh['decimals'], 'm')}."),
            ("llancament", {}, "Al punt més alt la velocitat és zero i l’energia és tota potencial."))
    for titol, m, h1, v1, h2 in [
        ("La muntanya russa", 400, 12, 0, 3), ("L’esquiador al pendent llis", 70, 8, 2, 2),
        ("El carretó", 20, 5, 3, 1), ("La boleta a la rampa", 0.1, 1.5, 0, 0.4),
        ("El vagó", 1200, 15, 4, 6), ("La pista de gel vertical", 50, 6, 1, 6),
    ]:
        rv = R("v_entre_altures", {"h1": h1, "v1": v1, "h2": h2}, "v", "m/s")
        add(titol, "mitjà", f"<p>Un cos de {fmt(m, dec(m))} kg passa per un punt A, a {fmt(h1, dec(h1))} m d’altura, a {fmt(v1, dec(v1))} m/s, i després per un punt B, a {fmt(h2, dec(h2))} m. El recorregut és llis i només actua el pes. Quina velocitat porta a B?</p>",
            [rv],
            solucio("Es conserva l’energia mecànica. El nivell zero pot ser qualsevol, perquè només importen les altures que diu l’enunciat. La massa es cancel·la.",
                    eq(r"\frac{1}{2} v_1^2 + g h_1 = \frac{1}{2} v_2^2 + g h_2"),
                    eq("v_2 = ", vfmt(rv)),
                    f"A B porta {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("muntanya", {"hA": f"{fmt(h1, dec(h1))} m", "hB": f"{fmt(h1, dec(h1))} m", "hC": f"{fmt(h2, dec(h2))} m"},
             "Les altures dels punts fixen l’energia potencial."))
    for titol, m, L, th in [
        ("El pèndol de 2 m", 0.5, 2, 60), ("El pèndol curt", 0.2, 0.8, 30),
        ("El pèndol del laboratori", 1, 1.5, 45), ("El gronxador", 30, 3, 20),
        ("El pèndol a 90°", 0.4, 1, 90), ("El pèndol petit", 0.1, 0.5, 40),
    ]:
        rh, rv = R("h_pendol", {"L": L, "theta": th}, "h", "m"), R("v_pendol", {"L": L, "theta": th}, "v", "m/s")
        add(titol, "mitjà", f"<p>Un pèndol de longitud {fmt(L, dec(L))} m i massa {fmt(m, dec(m))} kg es deixa anar des d’un angle de {th}° respecte de la vertical. Quina velocitat porta en passar pel punt més baix?</p>",
            [rh, rv],
            solucio("L’altura respecte del punt més baix és L(1 − cos θ). Es conserva l’energia mecànica: a dalt la velocitat és zero i a baix l’altura és zero.",
                    eq(r"h = L(1 - \cos\theta)") + eq(r"v = \sqrt{2 g h}"),
                    eq("h = ", vfmt(rh)) + eq("v = ", vfmt(rv)),
                    f"L’altura inicial és {valor(rh['valor'], rh['decimals'], 'm')} i la velocitat a baix és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("pendol", {"theta": th}, "L’altura es mesura des del punt més baix."))
    for titol, m, k, A in [
        ("La molla de 200 N/m", 0.5, 200, 0.1), ("La molla tova", 0.2, 50, 0.08),
        ("El bloc i la molla", 1, 98, 0.2), ("L’oscil·lador", 0.4, 160, 0.05),
        ("Compressió gran", 2, 800, 0.1), ("La molla del calaix", 0.3, 120, 0.04),
        ("Alliberar des de 15 cm", 0.25, 100, 0.15), ("El carro amb molla", 4, 400, 0.2),
    ]:
        rv = R("v_molla", {"k": k, "m": m, "A": A}, "v", "m/s")
        re = R("epe", {"k": k, "x": A}, "E", "J")
        add(titol, "mitjà", f"<p>Una molla de constant {fmt(k, dec(k))} N/m està comprimida {fmt(A, dec(A))} m i es deixa anar, unida a un bloc de {fmt(m, dec(m))} kg, damunt un pla horitzontal llis. Quina velocitat porta el bloc en passar per la posició d’equilibri de la molla?</p>",
            [re, rv],
            solucio("Al pla horitzontal el pes i la normal no treballen. L’energia de la molla a la compressió inicial es converteix en energia cinètica a l’equilibri, on la deformació és zero.",
                    eq(r"\frac{1}{2} k A^2 = \frac{1}{2} m v^2"),
                    eq("E = ", vfmt(re)) + eq("v = ", vfmt(rv)),
                    f"L’energia inicial de la molla és {valor(re['valor'], re['decimals'], 'J')} i la velocitat a l’equilibri és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("molla", {"comprimida": True}, "La molla comprimida té energia potencial elàstica."))
    return out


def mixtos():
    out, add = _cap("mixtos", "7")
    for titol, m, d, alpha in [
        ("El pla i dos mètodes", 3, 4, 30),
        ("Rampa de 20°", 5, 6, 20),
        ("Rampa de 45°", 2, 2, 45),
        ("Rampa de 37°", 4, 5, 37),
    ]:
        ra = R("a_inclin_0", {"alpha": alpha}, "a", "m/s²")
        rv = R("v_inclin_e", {"d": d, "alpha": alpha}, "v", "m/s")
        add(titol, "complet", f"<p>Un bloc de {fmt(m, dec(m))} kg parteix del repòs i recorre {fmt(d, dec(d))} m per un pla inclinat llis de {alpha}°. Calcula l’acceleració amb les lleis de Newton i la velocitat al final del tram conservant l’energia.</p>",
            [ra, rv],
            solucio("El pla és llis. Newton dona l’acceleració, g sin α, independent de la massa. L’energia només depèn del desnivell d sin α, i ha de donar la mateixa velocitat que la cinemàtica amb aquesta acceleració.",
                    eq(r"a = g \sin\alpha") + eq(r"v = \sqrt{2 g d \sin\alpha}"),
                    eq("a = ", vfmt(ra)) + eq("v = ", vfmt(rv)),
                    f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la velocitat al final és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("inclinat", {"alpha": alpha, "fregament": False}, "Pla inclinat llis. Es pot resoldre per forces i per energia."),
            ("dcl_inclinat", {"alpha": alpha, "fregament": False}, "Diagrama per escriure la segona llei al llarg del pla."))
    for titol, v0, th, h in [
        ("Velocitat a 2 m d’altura", 20, 50, 2),
        ("Velocitat a 1 m", 15, 60, 1),
        ("Velocitat a 3 m", 25, 40, 3),
        ("Velocitat a 0,5 m", 12, 45, 0.5),
    ]:
        rv = R("v_entre_altures", {"h1": 0, "v1": v0, "h2": h}, "v", "m/s")
        add(titol, "complet", f"<p>Un projectil surt del terra a {fmt(v0, dec(v0))} m/s. Quan és a {fmt(h, dec(h))} m d’altura, quin mòdul de velocitat porta? No facis servir el temps: conserva l’energia. Es negligeix l’aire.</p>",
            [rv],
            solucio("Sense resistència de l’aire l’energia mecànica es conserva. A una altura h la cinètica ha disminuït en el que ha guanyat la potencial. El mòdul no depèn de l’angle: l’angle reparteix la velocitat entre components, però el mòdul el fixa l’energia.",
                    eq(r"\frac{1}{2} m v_0^2 = \frac{1}{2} m v^2 + m g h"),
                    eq("v = ", vfmt(rv)),
                    f"El mòdul de la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("tir_p", {"theta": th, "h": f"h = {fmt(h, dec(h))} m", "r": "x"}, "A una altura intermèdia encara hi ha velocitat, horitzontal i vertical."))
    for titol, m, L, th in [("Tensió a baix del pèndol", 0.5, 2, 60), ("Tensió del gronxador", 40, 2.5, 30), ("Tensió del pèndol curt", 0.3, 1, 45)]:
        rv = R("v_pendol", {"L": L, "theta": th}, "v", "m/s")
        rT = R("T_cord_baix", {"m": m, "v": rv["valor"], "r": L}, "T", "N")
        add(titol, "complet", f"<p>Un pèndol de massa {fmt(m, dec(m))} kg i longitud {fmt(L, dec(L))} m es deixa anar des de {th}°. Quina tensió fa la corda en passar pel punt més baix?</p>",
            [rv, rT],
            solucio("Primer es troba la velocitat al punt baix conservant l’energia. Després, al punt baix, la tensió és cap amunt i el pes cap avall: la resultant cap al centre, que és cap amunt, val T − mg.",
                    eq(r"v = \sqrt{2 g L (1 - \cos\theta)}") + eq(r"T - m g = m v^2 / L"),
                    eq("v = ", vfmt(rv)) + eq("T = ", vfmt(rT)),
                    f"La velocitat a baix és {valor(rv['valor'], rv['decimals'], 'm/s')} i la tensió és {valor(rT['valor'], rT['decimals'], 'N')}."),
            ("pendol", {"theta": th}, "Es deixa anar des de l’angle indicat i es demana la corda al punt més baix."))
    for titol, r in [("El lòpping mínim", 5), ("El loop de 2 m", 2), ("El loop de 8 m", 8)]:
        rH, rv = R("H_loop", {"r": r}, "H", "m"), R("vmin_loop", {"r": r}, "v", "m/s")
        add(titol, "complet", f"<p>Un carretó entra en un lòpping de radi {fmt(r, dec(r))} m. Des de quina altura mínima, mesurada des del terra, s’ha de deixar caure, partint del repòs i per una pista llisa, perquè passi pel capdamunt sense caure? Quina velocitat porta llavors al capdamunt?</p>",
            [rH, rv],
            solucio("Al capdamunt, la velocitat mínima és la que fa nul·la la normal: el pes sol fa de força centrípeta, v² = g r. L’altura del capdamunt és 2r. Conservant l’energia des del repòs, mgH = ½m v² + mg(2r), i en surt H = 2,5 r.",
                    eq(r"v = \sqrt{g r}") + eq(r"H = 2{,}5\, r"),
                    eq("v = ", vfmt(rv)) + eq("H = ", vfmt(rH)),
                    f"Al capdamunt porta {valor(rv['valor'], rv['decimals'], 'm/s')} i cal deixar-lo anar des de {valor(rH['valor'], rH['decimals'], 'm')}."),
            ("loop", {}, "Per passar pel capdamunt cal altura suficient des del terra."))
    for titol, m, k, A in [("La molla llança el bloc rampa amunt", 0.5, 200, 0.2), ("Una altra molla i una rampa", 1, 100, 0.3)]:
        rv = R("v_molla", {"k": k, "m": m, "A": A}, "v", "m/s")
        rh = R("h_llanc_e", {"v": rv["valor"]}, "h", "m")
        add(titol, "complet", f"<p>Una molla de constant {fmt(k, dec(k))} N/m, comprimida {fmt(A, dec(A))} m, llança un bloc de {fmt(m, dec(m))} kg per un pla horitzontal llis. El bloc entra després en una rampa llisa. Quina altura màxima puja, mesurada des del pla?</p>",
            [rv, rh],
            solucio("Fins a l’equilibri de la molla, l’energia elàstica es converteix en cinètica. Aquesta cinètica, a la rampa llisa, es converteix en potencial fins que el bloc s’atura. És el mateix que igualar directament l’energia de la molla amb mgh.",
                    eq(r"\frac{1}{2} k A^2 = m g h"),
                    eq("v = ", vfmt(rv)) + eq("h = ", vfmt(rh)),
                    f"En sortir de la molla porta {valor(rv['valor'], rv['decimals'], 'm/s')} i puja {valor(rh['valor'], rh['decimals'], 'm')}."),
            ("molla", {"comprimida": True}, "La compressió inicial de la molla fixa l’energia disponible."))
    for titol, m1, m2, h in [("Atwood i energia", 2, 3, 1), ("Atwood, un metre i mig", 1, 2, 1.5)]:
        ra = R("atwood_a", {"m1": m1, "m2": m2}, "a", "m/s²")
        rv = R("atwood_v", {"m1": m1, "m2": m2, "h": h}, "v", "m/s")
        add(titol, "complet", f"<p>En una màquina d’Atwood les masses són {fmt(m1, dec(m1))} kg i {fmt(m2, dec(m2))} kg, i parteixen del repòs. Calcula l’acceleració amb Newton i la velocitat quan la massa grossa ha baixat {fmt(h, dec(h))} m, conservant l’energia.</p>",
            [ra, rv],
            solucio("Newton dona l’acceleració del sistema. L’energia també es conserva, perquè la politja és ideal i la corda no dissipa: la pèrdua d’energia potencial és (m₂ − m₁) g h i es converteix en cinètica de les dues masses, que porten la mateixa rapidesa.",
                    eq(r"a = (m_2 - m_1) g / (m_1 + m_2)") + eq(r"v = \sqrt{2 (m_2 - m_1) g h / (m_1 + m_2)}"),
                    eq("a = ", vfmt(ra)) + eq("v = ", vfmt(rv)),
                    f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("atwood", {"m1": f"{fmt(m1, dec(m1))} kg", "m2": f"{fmt(m2, dec(m2))} kg"}, "Les dues masses porten la mateixa rapidesa en cada instant."))
    return out
