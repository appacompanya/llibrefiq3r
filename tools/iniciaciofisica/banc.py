"""Problemes del llibre. Cada solució es calcula aquí i la torna a comprovar verifica.py."""
from peces import M, EQ, fmt, calc, solucio, valor


def dec(x):
    if abs(x - round(x)) < 1e-6:
        return 0
    if abs(x - float(fmt(x, 1).replace(",", "."))) < 1e-6:
        return 1
    return 2


def R(tipus, params, nom, unitat, d=None):
    val = calc(tipus, params)
    if d is None:
        d = dec(val)
    return {"tipus": tipus, "params": params, "nom": nom, "decimals": d, "unitat": unitat, "valor": val}


def P(tema, num, titol, nivell, enun, resultats, sol, esq, esq_sol=None):
    return {
        "tema": tema, "num": num, "id": f"{num}", "titol": titol, "nivell": nivell,
        "enunciat": enun, "solucio": sol, "resultats": resultats,
        "esq": esq, "esq_sol": esq_sol,
    }


def vfmt(r):
    return fmt(r["valor"], r["decimals"])


def esq_eix(a, b, ca, cb, cota):
    return ("eix", {"punts": [(0.12, a, "#5c6570"), (0.78, b, "#1f5fbf")], "cota": (0.12, 0.78, cota)},
            "Esquema del recorregut sobre la trajectòria recta.")


def tots():
    from banc_resta import tir, mcu, newton, forces, energia, mixtos
    p = []
    p += cinematica()
    p += tir()
    p += mcu()
    p += newton()
    p += forces()
    p += energia()
    p += mixtos()
    return p


def cinematica():
    out = []
    n = 0

    def add(titol, niv, enun, res, sol, esq, esq_sol=None):
        nonlocal n
        n += 1
        out.append(P("cinematica", f"1.{n}", titol, niv, enun, res, sol, esq, esq_sol))

    files = [
        ("El tramvia del carrer Aragó", "senzill", "El tramvia de la línia T2 passa pel punt x = 40 m i manté una velocitat constant de 12 m/s.", 40, 12, 25),
        ("La ciclista del carril bici", "senzill", "Una ciclista passa per x = 0 amb velocitat constant de 6,5 m/s en un tram recte del carril bici.", 0, 6.5, 40),
        ("El patinet", "senzill", "Un patinet elèctric circula a 5 m/s constants i, quan comencem a comptar, ja és a 15 m de l’origen.", 15, 5, 18),
        ("L’autocar de l’excursió", "senzill", "Un autocar de l’institut manté 22 m/s en un tram recte d’autovia i passa per x = 100 m.", 100, 22, 30),
        ("El dron en línia recta", "mitjà", "Un dron vola en línia recta a 8 m/s constants. A l’instant inicial és a x = −20 m.", -20, 8, 15),
    ]
    for titol, niv, frase, x0, v, t in files:
        r = R("mru_x", {"x0": x0, "v": v, "t": t}, "x", "m")
        add(titol, niv,
            f"<p>{frase} Quant val la posició al cap de {fmt(t, dec(t))} s?</p>",
            [r],
            solucio(
                "La velocitat no canvia, de manera que el moviment és un MRU. Triem l’eix en el sentit de la marxa.",
                EQ(r"x = x_0 + v t"),
                f"<p>Substituïm les dades de l’enunciat, sense canviar d’unitats:</p>" + EQ(f"x = {fmt(x0, dec(x0))} + {fmt(v, dec(v))} \\cdot {fmt(t, dec(t))} = {vfmt(r)}"),
                f"Al cap de {fmt(t, dec(t))} s el mòbil és a {valor(r['valor'], r['decimals'], 'm')}."),
            esq_eix("x₀", "x", "", "", f"{fmt(v, dec(v))} m/s"))

    files = [
        ("El metro entre dues estacions", "senzill", "Entre dues estacions hi ha 720 m en línia recta. El metro els fa a velocitat constant en 60 s.", 0, 720, 60),
        ("La caminada", "senzill", "Una persona camina 150 m en línia recta en 120 s, a ritme constant.", 0, 150, 120),
        ("El missatger", "mitjà", "Un missatger surt de x = 20 m i arriba a x = 260 m en 40 s, amb velocitat constant.", 20, 260, 40),
    ]
    for titol, niv, frase, x0, x, t in files:
        r = R("mru_v", {"x0": x0, "x": x, "t": t}, "v", "m/s")
        add(titol, niv, f"<p>{frase} Quina velocitat porta?</p>", [r],
            solucio("En un MRU la velocitat és el desplaçament dividit pel temps.",
                    EQ(r"v = \frac{x - x_0}{t}"),
                    EQ(f"v = \\frac{{{fmt(x, dec(x))} - {fmt(x0, dec(x0))}}}{{{fmt(t, dec(t))}}} = {vfmt(r)}"),
                    f"La velocitat és {valor(r['valor'], r['decimals'], 'm/s')}."),
            esq_eix("sortida", "arribada", "", "", f"{fmt(x - x0, dec(x - x0))} m"))

    files = [
        ("Quan arriba el tren", "mitjà", "Un tren regional va a 28 m/s constants. Volem saber quant triga a passar de x = 200 m a x = 1600 m.", 200, 1600, 28),
        ("El temps del ciclista", "senzill", "Una ciclista va a 7 m/s constants. Quant triga a recórrer 210 m a partir de l’origen?", 0, 210, 7),
        ("La barca al canal", "mitjà", "Una barca baixa un canal recte a 3,5 m/s. Quant triga a anar de la marca 10 m a la marca 80 m?", 10, 80, 3.5),
    ]
    for titol, niv, frase, x0, x, v in files:
        r = R("mru_t", {"x0": x0, "x": x, "v": v}, "t", "s")
        add(titol, niv, f"<p>{frase}</p>", [r],
            solucio("Aïllem el temps de l’equació del MRU. La velocitat és constant i no nul·la.",
                    EQ(r"t = \frac{x - x_0}{v}"),
                    EQ(f"t = \\frac{{{fmt(x, dec(x))} - {fmt(x0, dec(x0))}}}{{{fmt(v, dec(v))}}} = {vfmt(r)}"),
                    f"Triga {valor(r['valor'], r['decimals'], 's')}."),
            esq_eix("x₀", "x", "", "", f"{fmt(v, dec(v))} m/s"))

    files = [
        ("La bicicleta atrapa el patinet", "mitjà", "Un patinet és a x = 120 m i va a 4 m/s. Una bicicleta surt de l’origen a 10 m/s, en el mateix sentit.", 0, 10, 120, 4),
        ("El cotxe i el camió", "complet", "Un camió és a x = 300 m i va a 18 m/s. Un cotxe surt de x = 0 a 30 m/s, pel mateix carril i en el mateix sentit.", 0, 30, 300, 18),
        ("Dos trens que s’acosten", "complet", "Un tren surt de x = 0 a 20 m/s cap a la dreta. Un altre surt de x = 900 m a 10 m/s cap a l’esquerra.", 0, 20, 900, -10),
        ("L’autocar i la moto", "mitjà", "Una moto és a x = 50 m i va a 25 m/s. Un autocar és a x = 400 m i va a 15 m/s, tots dos cap a la dreta.", 50, 25, 400, 15),
    ]
    for titol, niv, frase, x10, v1, x20, v2 in files:
        rt = R("encontre_t", {"x10": x10, "v1": v1, "x20": x20, "v2": v2}, "t", "s")
        rx = R("encontre_x", {"x10": x10, "v1": v1, "x20": x20, "v2": v2}, "x", "m")
        add(titol, niv, f"<p>{frase} En quin instant i en quin punt es troben, si mantenen la velocitat?</p>",
            [rt, rx],
            solucio("Els dos mòbils fan un MRU. Es troben quan les dues posicions coincideixen.",
                    EQ(r"x_1 + v_1 t = x_2 + v_2 t"),
                    f"<p>Aïllem el temps i, amb aquest temps, la posició del primer mòbil.</p>"
                    + EQ(f"t = {vfmt(rt)}") + EQ(f"x = {vfmt(rx)}"),
                    f"Es troben al cap de {valor(rt['valor'], rt['decimals'], 's')}, a {valor(rx['valor'], rx['decimals'], 'm')}."),
            ("eix", {"punts": [(0.15, "1", "#1f5fbf"), (0.7, "2", "#c26a00")], "cota": (0.15, 0.7, "es troben")},
             "Posició inicial de cada mòbil. Les fletxes del moviment van en el sentit de cada velocitat."))

    files = [
        ("El cotxe que arrenca", "senzill", "Un cotxe arrenca del repòs amb una acceleració constant de 2 m/s².", 0, 0, 2, 5),
        ("La moto", "senzill", "Una moto passa a 8 m/s i accelera a 1,5 m/s² durant 4 s.", 0, 8, 1.5, 4),
        ("El tren que frena", "mitjà", "Un tren va a 20 m/s i frena amb acceleració constant de −0,8 m/s² durant 10 s. L’origen és el punt on comença a frenar.", 0, 20, -0.8, 10),
        ("L’ascensor", "mitjà", "Un ascensor passa per y = 6 m a 2 m/s cap amunt i accelera a 0,5 m/s² durant 4 s.", 6, 2, 0.5, 4),
        ("El camió a la incorporació", "mitjà", "Un camió entra a l’autovia a 12 m/s i accelera a 0,4 m/s² durant 15 s.", 0, 12, 0.4, 15),
        ("La frenada del patinet", "senzill", "Un patinet va a 6 m/s i frena a −1,2 m/s² durant 3 s.", 0, 6, -1.2, 3),
    ]
    for titol, niv, frase, x0, v0, a, t in files:
        rv = R("mrua_v", {"v0": v0, "a": a, "t": t}, "v", "m/s")
        rx = R("mrua_x", {"x0": x0, "v0": v0, "a": a, "t": t}, "x", "m")
        add(titol, niv, f"<p>{frase} Quina velocitat porta i on és al cap de {fmt(t, dec(t))} s?</p>",
            [rv, rx],
            solucio("L’acceleració és constant: és un MRUA. Escrivim la velocitat i la posició amb el mateix eix.",
                    EQ(r"v = v_0 + a t") + EQ(r"x = x_0 + v_0 t + \frac{1}{2} a t^2"),
                    EQ(f"v = {fmt(v0, dec(v0))} + ({fmt(a, dec(a))}) \\cdot {fmt(t, dec(t))} = {vfmt(rv)}")
                    + EQ(f"x = {vfmt(rx)}"),
                    f"La velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')} i la posició és {valor(rx['valor'], rx['decimals'], 'm')}."),
            ("grafica", {"trams": [[(0, v0), (t, rv["valor"])]], "xlabel": "t (s)", "ylabel": "v (m/s)",
                         "xmin": 0, "xmax": t * 1.3, "ymin": min(0, v0, rv["valor"]) - 1, "ymax": max(v0, rv["valor"]) + 2},
             "Gràfica velocitat-temps del tram. El pendent és l’acceleració."))

    files = [
        ("Frenar abans del pas", "mitjà", "Un cotxe va a 18 m/s i frena a −3 m/s². Volem la velocitat després de recórrer 30 m, i el signe negatiu de l’acceleració ja indica el sentit de frenada.", 18, -3, 30),
        ("La pista d’acceleració", "mitjà", "Un cotxe de carreres surt del repòs i manté 4 m/s² al llarg de 50 m.", 0, 4, 50),
        ("Quant frena", "complet", "Un autobús passa de 16 m/s a 4 m/s en 40 m, amb acceleració constant.", 16, 4, 40),
    ]
    # third is a from velocities
    r = R("mrua_vf", {"v0": 18, "a": -3, "dx": 30, "signe": 1}, "v", "m/s")
    add("Frenar abans del pas", "mitjà",
        "<p>Un cotxe va a 18 m/s i frena amb acceleració constant de −3 m/s². Quina velocitat porta després de recórrer 30 m?</p>",
        [r],
        solucio("No ens donen el temps. Fem servir la relació que el elimina. El cotxe encara va cap endavant, de manera que la velocitat és positiva.",
                EQ(r"v^2 = v_0^2 + 2 a \Delta x"),
                EQ(f"v = {vfmt(r)}"),
                f"Després de 30 m porta {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("grafica", {"trams": [[(0, 18), (30, r["valor"])]], "xlabel": "x (m)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 36, "ymin": 0, "ymax": 22},
         "La velocitat disminueix al llarg dels 30 m de frenada."))
    r = R("mrua_vf", {"v0": 0, "a": 4, "dx": 50, "signe": 1}, "v", "m/s")
    add("La pista d’acceleració", "mitjà",
        "<p>Un cotxe surt del repòs amb acceleració constant de 4 m/s². Quina velocitat porta després de 50 m?</p>",
        [r],
        solucio("Surt del repòs i l’acceleració és constant. No cal el temps.",
                EQ(r"v^2 = 2 a \Delta x"),
                EQ(f"v = {vfmt(r)}"),
                f"Als 50 m porta {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("grafica", {"trams": [[(0, 0), (50, r["valor"])]], "xlabel": "x (m)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 60, "ymin": 0, "ymax": r["valor"] * 1.2},
         "La velocitat creix al llarg de la pista."))
    r = R("mrua_a_x", {"v0": 16, "v": 4, "dx": 40}, "a", "m/s²")
    add("L’autobús que frena", "complet",
        "<p>Un autobús passa de 16 m/s a 4 m/s en 40 m, amb acceleració constant. Quant val l’acceleració?</p>",
        [r],
        solucio("Coneixem les dues velocitats i el desplaçament. Aïllem l’acceleració.",
                EQ(r"a = \frac{v^2 - v_0^2}{2 \Delta x}"),
                EQ(f"a = {vfmt(r)}"),
                f"L’acceleració és {valor(r['valor'], r['decimals'], 'm/s²')}. El signe negatiu indica que frena."),
        ("grafica", {"trams": [[(0, 16), (40, 4)]], "xlabel": "x (m)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 48, "ymin": 0, "ymax": 20},
         "La velocitat baixa de 16 m/s a 4 m/s en 40 m."))

    # gràfiques: pendent i àrea
    r = R("mrua_a_t", {"v0": 2, "v": 14, "t": 6}, "a", "m/s²")
    rx = R("mrua_x", {"x0": 0, "v0": 2, "a": r["valor"], "t": 6}, "x", "m")
    # careful: a from (14-2)/6 = 2 exactly, x = 2*6 + 0.5*2*36 = 12+36 = 48
    add("Llegir el pendent i l’àrea", "mitjà",
        "<p>La gràfica velocitat-temps d’un tram és una recta que passa de 2 m/s a 14 m/s entre t = 0 i t = 6 s. Quina acceleració té el moviment i quin desplaçament fa en aquests 6 s?</p>",
        [r, rx],
        solucio("A la gràfica velocitat-temps el pendent és l’acceleració i l’àrea sota la recta és el desplaçament. L’àrea és un trapezi.",
                EQ(r"a = \frac{\Delta v}{\Delta t}") + EQ(r"\Delta x = \frac{v_0 + v}{2} \Delta t"),
                EQ(f"a = {vfmt(r)}") + EQ(f"\\Delta x = {vfmt(rx)}"),
                f"L’acceleració és {valor(r['valor'], r['decimals'], 'm/s²')} i el desplaçament és {valor(rx['valor'], rx['decimals'], 'm')}."),
        ("grafica", {"trams": [[(0, 2), (6, 14)]], "xlabel": "t (s)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 8, "ymin": 0, "ymax": 16},
         "Recta velocitat-temps. El pendent és l’acceleració i l’àrea és el desplaçament."))

    r = R("mrua_v", {"v0": 10, "a": -2, "t": 3}, "v", "m/s")
    rx1 = R("mrua_x", {"x0": 0, "v0": 10, "a": -2, "t": 3}, "x1", "m")
    rx2 = R("mru_x", {"x0": rx1["valor"], "v": r["valor"], "t": 8}, "x", "m")
    add("Dos trams", "complet",
        "<p>Un cotxe va a 10 m/s i accelera a −2 m/s² durant 3 s. Després manté constant la velocitat que porta durant 8 s més. Quin desplaçament total fa?</p>",
        [r, rx1, rx2],
        solucio("Hi ha dos trams. Al primer l’acceleració és constant; al segon la velocitat ja no canvia. La posició final del primer tram és l’origen del segon.",
                EQ(r"v = v_0 + a t") + EQ(r"x = x_1 + v t_2"),
                f"<p>Al final del primer tram la velocitat és {vfmt(r)} m/s i la posició és {vfmt(rx1)} m. Els 8 s següents, a velocitat constant, porten el cotxe fins a la posició total.</p>"
                + EQ(f"x = {vfmt(rx2)}"),
                f"El desplaçament total, mesurat des de l’origen, acaba a {valor(rx2['valor'], rx2['decimals'], 'm')}."),
        ("grafica", {"trams": [[(0, 10), (3, 4), (11, 4)]], "xlabel": "t (s)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 12, "ymin": 0, "ymax": 12},
         "Dos trams: primer la velocitat baixa i després es manté."))

    # caigudes
    for titol, niv, frase, h in [
        ("La pedra del penya-segat", "senzill", "Es deixa caure una pedra des de 19,6 m, sense velocitat inicial i sense tenir en compte l’aire.", 19.6),
        ("El test de la finestra", "senzill", "Un test cau des d’una finestra situada a 4,9 m del terra. Surt del repòs.", 4.9),
        ("El salt d’un pont", "mitjà", "Una persona salta des d’un pont de 10 m. Es pot prendre la caiguda com a lliure des del repòs.", 10),
        ("La pilota del terrat", "mitjà", "Una pilota cau des d’un terrat de 45 m, partint del repòs.", 45),
        ("El paquet i la grua", "senzill", "Un paquet es desprèn d’una grua i cau 5 m fins a terra, des del repòs.", 5),
    ]:
        rt = R("caiguda_t", {"h": h}, "t", "s")
        rv = R("caiguda_v", {"h": h}, "v", "m/s")
        add(titol, niv, f"<p>{frase} Quant triga a arribar a terra i amb quina velocitat ho fa? Pren g = 9,8 m/s².</p>",
            [rt, rv],
            solucio("És una caiguda lliure des del repòs. El temps surt de l’altura i la velocitat, del mateix desnivell. El sentit de la velocitat és cap avall.",
                    EQ(r"t = \sqrt{\frac{2h}{g}}") + EQ(r"v = \sqrt{2 g h}"),
                    EQ(f"t = {vfmt(rt)}") + EQ(f"v = {vfmt(rv)}"),
                    f"Triga {valor(rt['valor'], rt['decimals'], 's')} i arriba a {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("caiguda", {"h": f"h = {fmt(h, dec(h))} m"}, "Caiguda des del repòs. La velocitat creix cap avall."))

    for titol, niv, frase, v0 in [
        ("La pilota cap amunt", "senzill", "Es llança una pilota verticalment cap amunt a 14 m/s des del terra.", 14),
        ("El coet d’aigua", "mitjà", "Un coet d’aigua puja amb velocitat inicial de 19,6 m/s, en vertical.", 19.6),
        ("La fletxa", "mitjà", "Es dispara una fletxa verticalment cap amunt a 28 m/s.", 28),
        ("El llançament a 9,8 m/s", "senzill", "Es llança una clau cap amunt a 9,8 m/s.", 9.8),
    ]:
        rh = R("llanc_h", {"v0": v0}, "h", "m")
        rt = R("llanc_t_dalt", {"v0": v0}, "t", "s")
        rT = R("llanc_t_total", {"v0": v0}, "T", "s")
        add(titol, niv, f"<p>{frase} Quina alçada màxima assoleix, quant triga a arribar-hi i quant triga a tornar al punt de partida? Pren g = 9,8 m/s² i l’eix cap amunt.</p>",
            [rh, rt, rT],
            solucio("Amb l’eix cap amunt l’acceleració és −g. Al punt més alt la velocitat és zero. La baixada fins al mateix punt dura el mateix que la pujada.",
                    EQ(r"h = \frac{v_0^2}{2g}") + EQ(r"t = \frac{v_0}{g}"),
                    EQ(f"h = {vfmt(rh)}") + EQ(f"t = {vfmt(rt)}") + EQ(f"T = {vfmt(rT)}"),
                    f"Puja {valor(rh['valor'], rh['decimals'], 'm')}, triga {valor(rt['valor'], rt['decimals'], 's')} a arribar-hi i {valor(rT['valor'], rT['decimals'], 's')} a tornar."),
            ("llancament", {}, "Llançament vertical. Al punt més alt la velocitat és nul·la i l’acceleració no."))

    # una de vertical a un instant
    rv = R("vertical_v", {"v0": 20, "t": 1}, "v", "m/s")
    ry = R("vertical_y", {"y0": 0, "v0": 20, "t": 1}, "y", "m")
    add("On és al cap d’un segon", "mitjà",
        "<p>Es llança una pedra cap amunt a 20 m/s des del terra. On és i quina velocitat porta al cap d’1 s? Eix cap amunt i g = 9,8 m/s².</p>",
        [ry, rv],
        solucio("És un MRUA vertical amb acceleració −g. Substituïm t = 1 s a les dues equacions.",
                EQ(r"y = v_0 t - \frac{1}{2} g t^2") + EQ(r"v = v_0 - g t"),
                EQ(f"y = {vfmt(ry)}") + EQ(f"v = {vfmt(rv)}"),
                f"Al cap d’1 s és a {valor(ry['valor'], ry['decimals'], 'm')} i la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')}. El signe positiu vol dir que encara puja."),
        ("llancament", {}, "La pedra encara puja al cap d’un segon."))
    return out
