"""Problemes de cinemàtica, de nivell de 1r de batxillerat.

Cada enunciat és una situació concreta, coherent amb el títol. Les solucions
substitueixen les dades amb unitats.
"""
from peces import EQ, fmt, igual, solucio, valor, calc


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


def nsq(x, unitat="m/s"):
    """(valor amb unitat) al quadrat. El parèntesi va dins la base del superíndex."""
    return "{(" + ntex(x, unitat) + ")}^2"


def ntex(x, unitat, sup=""):
    d = dec(x)
    if not unitat:
        t = fmt(x, d)
    else:
        t = rf"{fmt(x, d)}\,\mathrm{{{unitat}}}"
    if sup:
        t += "^{" + sup + "}"
    return t


def tots():
    from banc_resta import tir, mcu, newton, forces, energia, mixtos
    return cinematica() + tir() + mcu() + newton() + forces() + energia() + mixtos()


def cinematica():
    out = []
    n = 0

    def add(titol, niv, enun, res, sol, esq, esq_sol=None):
        nonlocal n
        n += 1
        out.append(P("cinematica", f"1.{n}", titol, niv, enun, res, sol, esq, esq_sol))

    # --- MRU: posició ---
    r = R("mru_x", {"x0": 0, "v": 12, "t": 25}, "x", "m")
    rd = R("mru_x", {"x0": 0, "v": 12, "t": 25}, "d", "m")
    add("El tramvia del carrer Aragó", "senzill",
        "<p>El tramvia de la línia T2 surt de l’estació del Clot i recorre el carrer Aragó, recte, a 12 m/s constants.</p>"
        "<p>a) Quina posició té respecte de l’estació al cap de 25 s?</p>"
        "<p>b) Quin desplaçament ha fet en aquest temps?</p>",
        [r, rd],
        solucio(
            "El tramvia va per un tram recte a velocitat constant: l’acceleració és zero i l’equació del MRU dona la posició. L’origen és l’estació del Clot i el sentit positiu és el de la marxa. Com que surt de l’origen, el desplaçament coincideix amb la posició.",
            EQ(r"x = x_0 + v t"),
            igual("x", ntex(0, "m") + " + " + ntex(12, "m/s") + r" \cdot " + ntex(25, "s"), r["valor"], r["decimals"], "m"),
            f"Al cap de 25 s el tramvia és a {valor(r['valor'], r['decimals'], 'm')} de l’estació, i el desplaçament és també {valor(rd['valor'], rd['decimals'], 'm')}."),
        ("eix", {"punts": [(0.08, "Clot", "#5c6570"), (0.72, "25 s", "#1f5fbf")], "cota": (0.08, 0.72, "12 m/s"), "qui": "Tramvia T2 · carrer Aragó"},
         "El tramvia surt del Clot a 12 m/s."))

    r = R("mru_x", {"x0": 0, "v": 6.5, "t": 40}, "x", "m")
    rt = R("mru_t", {"x0": 0, "x": 260, "v": 6.5}, "t", "s")
    add("La ciclista del carril bici", "senzill",
        "<p>La Laia pedala pel carril bici de la Diagonal a 6,5 m/s constants. Quan passa per davant de l’institut comencem a comptar el temps.</p>"
        "<p>a) On és al cap de 40 s?</p>"
        "<p>b) Quant triga a fer 260 m des de l’institut?</p>",
        [r, rt],
        solucio(
            "La velocitat de la Laia no canvia, així que fem servir el MRU. L’origen és l’institut.",
            EQ(r"x = v t") + EQ(r"t = x / v"),
            igual("x", ntex(6.5, "m/s") + r" \cdot " + ntex(40, "s"), r["valor"], r["decimals"], "m")
            + igual("t", ntex(260, "m") + " / " + ntex(6.5, "m/s"), rt["valor"], rt["decimals"], "s"),
            f"Al cap de 40 s és a {valor(r['valor'], r['decimals'], 'm')} de l’institut, i triga {valor(rt['valor'], rt['decimals'], 's')} a fer 260 m."),
        ("eix", {"punts": [(0.08, "institut", "#5c6570"), (0.7, "Laia", "#1f5fbf")], "cota": (0.08, 0.7, "6,5 m/s"), "qui": "Ciclista al carril bici"},
         "La Laia passa per l’institut a 6,5 m/s."))

    r = R("mru_t", {"x0": 15, "x": 105, "v": 5}, "t", "s")
    add("El patinet fins a la fleca", "senzill",
        "<p>L’Oriol va amb el patinet elèctric a 5 m/s constants. Quan és a 15 m de casa, encara li falten arribar fins a la fleca, que és a 105 m de casa, pel mateix carrer recte.</p>"
        "<p>Quant triga a anar d’aquest punt a la fleca?</p>",
        [r],
        solucio(
            "El patinet porta velocitat constant. El temps és el desplaçament fins a la fleca dividit per aquesta velocitat.",
            EQ(r"t = (x - x_0) / v"),
            igual("t", "(" + ntex(105, "m") + " - " + ntex(15, "m") + ") / " + ntex(5, "m/s"), r["valor"], r["decimals"], "s"),
            f"L’Oriol triga {valor(r['valor'], r['decimals'], 's')} a arribar a la fleca."),
        ("eix", {"punts": [(0.15, "15 m", "#5c6570"), (0.75, "fleca", "#c26a00")], "cota": (0.15, 0.75, "5 m/s"), "qui": "Patinet de l’Oriol"},
         "Del punt a 15 m de casa fins a la fleca, a 5 m/s."))

    r = R("mru_x", {"x0": 100, "v": 22, "t": 30}, "x", "m")
    add("L’autocar de l’excursió", "senzill",
        "<p>L’autocar de l’institut entra a l’autovia pel quilòmetre que marquem com a x = 100 m i manté 22 m/s en un tram recte.</p>"
        "<p>Quina coordenada té al cap de 30 s?</p>",
        [r],
        solucio(
            "En aquest tram l’autocar no accelera. L’equació del MRU suma a la posició inicial el producte de la velocitat pel temps.",
            EQ(r"x = x_0 + v t"),
            igual("x", ntex(100, "m") + " + " + ntex(22, "m/s") + r" \cdot " + ntex(30, "s"), r["valor"], r["decimals"], "m"),
            f"Al cap de 30 s l’autocar és a {valor(r['valor'], r['decimals'], 'm')}."),
        ("eix", {"punts": [(0.12, "100 m", "#5c6570"), (0.72, "30 s", "#1f5fbf")], "cota": (0.12, 0.72, "22 m/s"), "qui": "Autocar de l’excursió"},
         "L’autocar entra al tram a x = 100 m."))

    r = R("mru_x", {"x0": -20, "v": 8, "t": 15}, "x", "m")
    add("El dron de la filmació", "mitjà",
        "<p>Un dron filma un carrer recte. A l’instant inicial és 20 m abans de l’origen de la plaça (x = −20 m) i vola cap a la plaça a 8 m/s constants.</p>"
        "<p>a) Quina posició té al cap de 15 s?</p>"
        "<p>b) El signe de la posició inicial, què indica?</p>",
        [r],
        solucio(
            "El dron va a velocitat constant cap al sentit positiu. El MRU admet una posició inicial negativa: vol dir que encara no ha arribat a l’origen.",
            EQ(r"x = x_0 + v t"),
            igual("x", ntex(-20, "m") + " + " + ntex(8, "m/s") + r" \cdot " + ntex(15, "s"), r["valor"], r["decimals"], "m"),
            f"Al cap de 15 s el dron és a {valor(r['valor'], r['decimals'], 'm')}. El signe negatiu de la posició inicial indica que era abans de la plaça, en el sentit oposat al del moviment."),
        ("eix", {"punts": [(0.2, "dron", "#c26a00"), (0.55, "plaça", "#5c6570")], "cota": (0.2, 0.55, "8 m/s"), "qui": "Dron · x₀ = −20 m"},
         "El dron és abans de l’origen i vola cap a la plaça."))

    r = R("mru_v", {"x0": 0, "x": 720, "t": 60}, "v", "m/s")
    add("El metro entre Glòries i Clot", "senzill",
        "<p>Entre les estacions de Glòries i Clot hi ha 720 m de túnel recte. El metro els fa en 60 s a velocitat constant.</p>"
        "<p>Quina velocitat porta?</p>",
        [r],
        solucio(
            "Si la velocitat és constant, és el desplaçament dividit pel temps. Aquí el desplaçament és la distància entre estacions perquè no hi ha marxa enrere.",
            EQ(r"v = \Delta x / \Delta t"),
            igual("v", ntex(720, "m") + " / " + ntex(60, "s"), r["valor"], r["decimals"], "m/s"),
            f"El metro porta {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("eix", {"punts": [(0.12, "Glòries", "#5c6570"), (0.78, "Clot", "#1f5fbf")], "cota": (0.12, 0.78, "720 m"), "qui": "Metro Glòries–Clot"},
         "720 m entre les dues estacions, fets en 60 s."))

    r = R("mru_v", {"x0": 0, "x": 150, "t": 120}, "v", "m/s")
    add("La caminada fins a l’institut", "senzill",
        "<p>La Núria camina 150 m en línia recta des de la parada de l’autobús fins a l’institut, i hi triga 120 s a un ritme constant.</p>"
        "<p>Quina velocitat mitjana porta? En aquest cas, coincideix amb la velocitat, perquè no varia.</p>",
        [r],
        solucio(
            "El ritme és constant, de manera que la velocitat mitjana i la velocitat instantània són la mateixa i valen el desplaçament partit pel temps.",
            EQ(r"v = \Delta x / \Delta t"),
            igual("v", ntex(150, "m") + " / " + ntex(120, "s"), r["valor"], r["decimals"], "m/s"),
            f"La Núria camina a {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("eix", {"punts": [(0.12, "parada", "#5c6570"), (0.75, "institut", "#1f5fbf")], "cota": (0.12, 0.75, "150 m"), "qui": "Caminada de la Núria"},
         "De la parada a l’institut, 150 m en 120 s."))

    r = R("mru_v", {"x0": 20, "x": 260, "t": 40}, "v", "m/s")
    add("El missatger entre dos portals", "mitjà",
        "<p>Un missatger en bicicleta passa pel portal número 20 (x = 20 m) i, 40 s més tard, pel portal número que marquem com a x = 260 m. En aquest tros el carrer és recte i no frena.</p>"
        "<p>Quina velocitat porta?</p>",
        [r],
        solucio(
            "Entre els dos portals la velocitat és constant. No partim de l’origen: el desplaçament és la diferència de posicions.",
            EQ(r"v = (x - x_0) / t"),
            igual("v", "(" + ntex(260, "m") + " - " + ntex(20, "m") + ") / " + ntex(40, "s"), r["valor"], r["decimals"], "m/s"),
            f"El missatger porta {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("eix", {"punts": [(0.18, "portal 20", "#5c6570"), (0.78, "260 m", "#1f5fbf")], "cota": (0.18, 0.78, "40 s"), "qui": "Missatger"},
         "Dels 20 m als 260 m en 40 s."))

    r = R("mru_t", {"x0": 200, "x": 1600, "v": 28}, "t", "s")
    add("El tren regional", "senzill",
        "<p>Un tren regional va a 28 m/s constants. Passa per una balisa situada a x = 200 m i la següent balisa és a x = 1600 m, a la mateixa via recta.</p>"
        "<p>Quant triga a anar de l’una a l’altra?</p>",
        [r],
        solucio(
            "La velocitat no canvia, així que el temps és el desplaçament entre balises dividit per 28 m/s.",
            EQ(r"t = (x - x_0) / v"),
            igual("t", "(" + ntex(1600, "m") + " - " + ntex(200, "m") + ") / " + ntex(28, "m/s"), r["valor"], r["decimals"], "s"),
            f"El tren triga {valor(r['valor'], r['decimals'], 's')}."),
        ("eix", {"punts": [(0.12, "balisa 1", "#5c6570"), (0.8, "balisa 2", "#1f5fbf")], "cota": (0.12, 0.8, "28 m/s"), "qui": "Tren regional"},
         "Entre les dues balises, a 28 m/s."))

    r = R("mru_t", {"x0": 0, "x": 210, "v": 7}, "t", "s")
    add("El ciclista fins al semàfor", "senzill",
        "<p>En Pol va en bicicleta a 7 m/s constants per un carrer recte. El semàfor és a 210 m d’on és ara.</p>"
        "<p>Quant triga a arribar-hi?</p>",
        [r],
        solucio(
            "Velocitat constant i carrer recte: el temps surt de l’equació del MRU aïllant t.",
            EQ(r"t = x / v"),
            igual("t", ntex(210, "m") + " / " + ntex(7, "m/s"), r["valor"], r["decimals"], "s"),
            f"En Pol triga {valor(r['valor'], r['decimals'], 's')} a arribar al semàfor."),
        ("eix", {"punts": [(0.12, "Pol", "#1f5fbf"), (0.78, "semàfor", "#c26a00")], "cota": (0.12, 0.78, "7 m/s"), "qui": "Bicicleta d’en Pol"},
         "210 m fins al semàfor, a 7 m/s."))

    r = R("mru_t", {"x0": 10, "x": 80, "v": 3.5}, "t", "s")
    add("La barca al canal", "mitjà",
        "<p>Una barca baixa un canal recte a 3,5 m/s. Passa per la marca dels 10 m i ha d’arribar a la marca dels 80 m.</p>"
        "<p>Quant de temps hi està?</p>",
        [r],
        solucio(
            "La velocitat de la barca és constant. El temps és la diferència de marques dividida per la velocitat.",
            EQ(r"t = (x - x_0) / v"),
            igual("t", "(" + ntex(80, "m") + " - " + ntex(10, "m") + ") / " + ntex(3.5, "m/s"), r["valor"], r["decimals"], "s"),
            f"La barca hi està {valor(r['valor'], r['decimals'], 's')}."),
        ("eix", {"punts": [(0.15, "10 m", "#5c6570"), (0.72, "80 m", "#1f5fbf")], "cota": (0.15, 0.72, "3,5 m/s"), "qui": "Barca al canal"},
         "De la marca 10 m a la marca 80 m."))

    # encontres
    rt = R("encontre_t", {"x10": 0, "v1": 10, "x20": 120, "v2": 4}, "t", "s")
    rx = R("encontre_x", {"x10": 0, "v1": 10, "x20": 120, "v2": 4}, "x", "m")
    add("La bicicleta atrapa el patinet", "mitjà",
        "<p>Un patinet és a 120 m de l’origen i va a 4 m/s. La Marta surt de l’origen amb la bicicleta a 10 m/s, en el mateix sentit i pel mateix carril recte. Tots dos mantenen la velocitat.</p>"
        "<p>a) Al cap de quant temps la Marta atrapa el patinet?</p>"
        "<p>b) En quin punt?</p>",
        [rt, rx],
        solucio(
            "Els dos fan un MRU. S’atrapen quan les posicions coincideixen: la bicicleta, que surt de zero, ha de recuperar els 120 m d’avantatge a una velocitat relativa de 10 − 4 m/s.",
            EQ(r"x_0 + v t = 120\,\mathrm{m} + 4\,\mathrm{m/s} \cdot t"),
            igual("t", ntex(120, "m") + " / (" + ntex(10, "m/s") + " - " + ntex(4, "m/s") + ")", rt["valor"], rt["decimals"], "s")
            + igual("x", ntex(10, "m/s") + r" \cdot " + ntex(rt["valor"], "s"), rx["valor"], rx["decimals"], "m"),
            f"La Marta atrapa el patinet al cap de {valor(rt['valor'], rt['decimals'], 's')}, a {valor(rx['valor'], rx['decimals'], 'm')} de l’origen."),
        ("eix", {"punts": [(0.1, "Marta", "#1f5fbf"), (0.55, "patinet", "#c26a00")], "cota": (0.1, 0.55, "120 m"), "qui": "Bicicleta 10 m/s · patinet 4 m/s"},
         "La Marta surt al darrere i va més de pressa."))

    rt = R("encontre_t", {"x10": 0, "v1": 30, "x20": 300, "v2": 18}, "t", "s")
    rx = R("encontre_x", {"x10": 0, "v1": 30, "x20": 300, "v2": 18}, "x", "m")
    add("El cotxe avança el camió", "mitjà",
        "<p>A l’autovia, un camió és a x = 300 m i va a 18 m/s. Un cotxe és a x = 0 i va a 30 m/s, pel mateix carril i en el mateix sentit.</p>"
        "<p>a) Quan l’avança?</p><p>b) On?</p>",
        [rt, rx],
        solucio(
            "Tots dos van a velocitat constant. L’avanç es produeix quan el cotxe, més ràpid, arriba a la posició del camió.",
            EQ(r"30\,\mathrm{m/s} \cdot t = 300\,\mathrm{m} + 18\,\mathrm{m/s} \cdot t"),
            igual("t", ntex(300, "m") + " / (" + ntex(30, "m/s") + " - " + ntex(18, "m/s") + ")", rt["valor"], rt["decimals"], "s")
            + igual("x", ntex(30, "m/s") + r" \cdot " + ntex(rt["valor"], "s"), rx["valor"], rx["decimals"], "m"),
            f"El cotxe avança el camió al cap de {valor(rt['valor'], rt['decimals'], 's')}, a {valor(rx['valor'], rx['decimals'], 'm')}."),
        ("eix", {"punts": [(0.1, "cotxe", "#1f5fbf"), (0.5, "camió", "#c26a00")], "cota": (0.1, 0.5, "300 m"), "qui": "Cotxe 30 m/s · camió 18 m/s"},
         "El cotxe surt 300 m al darrere del camió."))

    rt = R("encontre_t", {"x10": 0, "v1": 20, "x20": 900, "v2": -10}, "t", "s")
    rx = R("encontre_x", {"x10": 0, "v1": 20, "x20": 900, "v2": -10}, "x", "m")
    add("Dos trens que s’acosten", "mitjà",
        "<p>Dos trens s’acosten per una via recta. Un surt de x = 0 a 20 m/s cap a la dreta. L’altre surt de x = 900 m a 10 m/s cap a l’esquerra.</p>"
        "<p>a) Quan es creuen?</p><p>b) En quin punt de la via?</p>",
        [rt, rx],
        solucio(
            "Cada tren fa un MRU. La velocitat del segon és negativa perquè va cap a l’esquerra. Es creuen quan les dues posicions són iguals. La velocitat a què es tanquen la distància és 20 + 10 m/s.",
            EQ(r"20\,\mathrm{m/s} \cdot t = 900\,\mathrm{m} - 10\,\mathrm{m/s} \cdot t"),
            igual("t", ntex(900, "m") + " / (" + ntex(20, "m/s") + " + " + ntex(10, "m/s") + ")", rt["valor"], rt["decimals"], "s")
            + igual("x", ntex(20, "m/s") + r" \cdot " + ntex(rt["valor"], "s"), rx["valor"], rx["decimals"], "m"),
            f"Es creuen al cap de {valor(rt['valor'], rt['decimals'], 's')}, a {valor(rx['valor'], rx['decimals'], 'm')}."),
        ("eix", {"punts": [(0.1, "tren A", "#1f5fbf"), (0.85, "tren B", "#c26a00")], "cota": (0.1, 0.85, "900 m"), "qui": "Dos trens en sentits oposats"},
         "Un tren a 20 m/s i l’altre a 10 m/s, l’un cap a l’altre."))

    rt = R("encontre_t", {"x10": 50, "v1": 25, "x20": 400, "v2": 15}, "t", "s")
    rx = R("encontre_x", {"x10": 50, "v1": 25, "x20": 400, "v2": 15}, "x", "m")
    add("La moto i l’autocar", "mitjà",
        "<p>Una moto és a x = 50 m i va a 25 m/s. Un autocar és a x = 400 m i va a 15 m/s. Tots dos van cap a la dreta per una recta.</p>"
        "<p>a) Quan la moto arriba a l’altura de l’autocar?</p><p>b) On?</p>",
        [rt, rx],
        solucio(
            "Són dos MRU en el mateix sentit. La moto va més de pressa i parteix de més enrere. Igualem les posicions.",
            EQ(r"50\,\mathrm{m} + 25\,\mathrm{m/s} \cdot t = 400\,\mathrm{m} + 15\,\mathrm{m/s} \cdot t"),
            igual("t", "(" + ntex(400, "m") + " - " + ntex(50, "m") + ") / (" + ntex(25, "m/s") + " - " + ntex(15, "m/s") + ")", rt["valor"], rt["decimals"], "s")
            + igual("x", ntex(50, "m") + " + " + ntex(25, "m/s") + r" \cdot " + ntex(rt["valor"], "s"), rx["valor"], rx["decimals"], "m"),
            f"La moto arriba a l’altura de l’autocar al cap de {valor(rt['valor'], rt['decimals'], 's')}, a {valor(rx['valor'], rx['decimals'], 'm')}."),
        ("eix", {"punts": [(0.15, "moto", "#1f5fbf"), (0.62, "autocar", "#c26a00")], "cota": (0.15, 0.62, "350 m"), "qui": "Moto 25 m/s · autocar 15 m/s"},
         "La moto és a 50 m i l’autocar a 400 m."))

    # MRUA
    def mrua(titol, niv, enun, x0, v0, a, t, qui, peu, perque, resultat):
        rv = R("mrua_v", {"v0": v0, "a": a, "t": t}, "v", "m/s")
        rx = R("mrua_x", {"x0": x0, "v0": v0, "a": a, "t": t}, "x", "m")
        add(titol, niv, enun, [rv, rx],
            solucio(perque, EQ(r"v = v_0 + a t") + EQ(r"x = x_0 + v_0 t + \frac{1}{2} a t^2"),
                    igual("v", ntex(v0, "m/s") + " + (" + ntex(a, "m/s", "2") + r") \cdot " + ntex(t, "s"), rv["valor"], rv["decimals"], "m/s")
                    + igual("x", ntex(x0, "m") + " + " + ntex(v0, "m/s") + r" \cdot " + ntex(t, "s") + r" + \frac{1}{2} \cdot " + ntex(a, "m/s", "2") + r" \cdot " + ntex(t, "s") + "^2", rx["valor"], rx["decimals"], "m"),
                    resultat(rv, rx)),
            ("grafica", {"trams": [[(0, v0), (t, rv["valor"])]], "xlabel": "t (s)", "ylabel": "v (m/s)",
                         "xmin": 0, "xmax": max(t * 1.25, 1), "ymin": min(0, v0, rv["valor"]) - 1,
                         "ymax": max(v0, rv["valor"], 1) + 2, "qui": qui}, peu))

    mrua("El cotxe que surt del semàfor", "senzill",
         "<p>Un cotxe arrenca del semàfor (repòs) amb una acceleració constant de 2 m/s².</p><p>a) Quina velocitat porta al cap de 5 s?</p><p>b) Quina distància ha fet?</p>",
         0, 0, 2, 5, "Cotxe · a = 2 m/s²", "La velocitat del cotxe creix de manera uniforme des del repòs.",
         "Surt del repòs amb acceleració constant: és un MRUA. La velocitat creix proporcionalment al temps i la posició segueix el terme amb t al quadrat.",
         lambda rv, rx: f"Al cap de 5 s el cotxe porta {valor(rv['valor'], rv['decimals'], 'm/s')} i ha avançat {valor(rx['valor'], rx['decimals'], 'm')}.")

    mrua("La moto a la sortida del poble", "senzill",
         "<p>Una moto passa pel rètol de sortida del poble a 8 m/s i accelera a 1,5 m/s² durant 4 s, en línia recta.</p><p>a) Quina velocitat hi porta al final?</p><p>b) A quina distància del rètol és?</p>",
         0, 8, 1.5, 4, "Moto · v₀ = 8 m/s · a = 1,5 m/s²", "La moto ja porta velocitat i l’acceleració la fa créixer.",
         "Ja té velocitat inicial i l’acceleració és constant, així que calen les dues equacions del MRUA, no les del MRU.",
         lambda rv, rx: f"Al cap de 4 s la moto porta {valor(rv['valor'], rv['decimals'], 'm/s')} i és a {valor(rx['valor'], rx['decimals'], 'm')} del rètol.")

    mrua("El tren que entra a l’estació", "mitjà",
         "<p>Un tren arriba a l’estació a 20 m/s i frena amb acceleració constant de −0,8 m/s². Estudiem els 10 s primers de la frenada. L’origen és el punt on comença a frenar.</p><p>a) Quina velocitat porta als 10 s?</p><p>b) Quina distància ha recorregut frenant?</p>",
         0, 20, -0.8, 10, "Tren · frena a 0,8 m/s²", "La velocitat baixa amb pendent constant.",
         "Frenar amb acceleració constant és un MRUA. El signe negatiu de l’acceleració, amb l’eix en el sentit de la marxa, vol dir que la velocitat disminueix.",
         lambda rv, rx: f"Als 10 s el tren encara porta {valor(rv['valor'], rv['decimals'], 'm/s')} i ha recorregut {valor(rx['valor'], rx['decimals'], 'm')} frenant.")

    mrua("L’ascensor", "mitjà",
         "<p>Un ascensor passa pel tercer pis, que prenem com a y = 6 m, a 2 m/s cap amunt, i a partir d’aquest instant accelera a 0,5 m/s² durant 4 s.</p><p>a) Quina velocitat porta al final?</p><p>b) A quina altura és?</p>",
         6, 2, 0.5, 4, "Ascensor · y₀ = 6 m", "La velocitat cap amunt creix.",
         "L’ascensor ja puja i a més accelera cap amunt. L’origen d’altures no és zero: la posició inicial és 6 m i s’hi suma el que puja durant els 4 s.",
         lambda rv, rx: f"Al cap de 4 s l’ascensor puja a {valor(rv['valor'], rv['decimals'], 'm/s')} i és a {valor(rx['valor'], rx['decimals'], 'm')}.")

    mrua("El camió a la incorporació", "senzill",
         "<p>Un camió entra a l’autovia a 12 m/s i accelera a 0,4 m/s² durant 15 s en el carril d’incorporació, que és recte.</p><p>a) Quina velocitat hi assoleix?</p><p>b) Quina longitud d’incorporació ha fet servir?</p>",
         0, 12, 0.4, 15, "Camió · incorporació", "Acceleració petita i constant durant 15 s.",
         "L’acceleració és constant des del moment d’entrar. La velocitat final és la inicial més a·t, i la longitud és la posició del MRUA.",
         lambda rv, rx: f"El camió arriba a {valor(rv['valor'], rv['decimals'], 'm/s')} i fa servir {valor(rx['valor'], rx['decimals'], 'm')} d’incorporació.")

    mrua("El patinet que frena al pas", "senzill",
         "<p>L’Aina va en patinet a 6 m/s i, en veure un pas de vianants, frena a −1,2 m/s² durant 3 s.</p><p>a) Quina velocitat hi porta al final?</p><p>b) Quants metres ha avançat mentre frenava?</p>",
         0, 6, -1.2, 3, "Patinet de l’Aina · frena", "La velocitat baixa des de 6 m/s.",
         "La frenada és un MRUA amb acceleració negativa. Encara va cap endavant, perquè la velocitat no arriba a canviar de signe en aquests 3 s.",
         lambda rv, rx: f"Al cap de 3 s l’Aina porta {valor(rv['valor'], rv['decimals'], 'm/s')} i ha avançat {valor(rx['valor'], rx['decimals'], 'm')}.")

    r = R("mrua_vf", {"v0": 18, "a": -3, "dx": 30, "signe": 1}, "v", "m/s")
    add("Frenar abans del pas de vianants", "mitjà",
        "<p>Un cotxe va a 18 m/s i frena a −3 m/s², constant, en acostar-se a un pas de vianants. Volem la velocitat que porta després de recórrer 30 m de frenada. No ens donen el temps.</p>",
        [r],
        solucio(
            "No coneixem el temps, però sí la velocitat inicial, l’acceleració i el desplaçament. L’equació que no conté el temps és la que convé. El cotxe encara va cap endavant, així que la velocitat és positiva.",
            EQ(r"v^2 = v_0^2 + 2 a \Delta x"),
            igual("v", r"\sqrt{" + nsq(18) + " + 2 \cdot (" + ntex(-3, "m/s", "2") + r") \cdot " + ntex(30, "m") + "}", r["valor"], r["decimals"], "m/s"),
            f"Després de 30 m el cotxe porta {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("grafica", {"trams": [[(0, 18), (30, r["valor"])]], "xlabel": "x (m)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 36, "ymin": 0, "ymax": 22, "qui": "Cotxe · 30 m de frenada"},
         "La velocitat baixa al llarg dels 30 m."))

    r = R("mrua_vf", {"v0": 0, "a": 4, "dx": 50, "signe": 1}, "v", "m/s")
    add("La pista d’acceleració", "mitjà",
        "<p>En una pista recta, un cotxe surt del repòs i manté 4 m/s². Quina velocitat porta en passar pels 50 m?</p>",
        [r],
        solucio(
            "Surt del repòs i l’acceleració és constant. Com que demanen la velocitat a una distància, i no a un temps, fem servir v² = 2 a Δx.",
            EQ(r"v^2 = 2 a \Delta x"),
            igual("v", r"\sqrt{2 \cdot " + ntex(4, "m/s", "2") + r" \cdot " + ntex(50, "m") + "}", r["valor"], r["decimals"], "m/s"),
            f"Als 50 m el cotxe porta {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("grafica", {"trams": [[(0, 0), (50, r["valor"])]], "xlabel": "x (m)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 60, "ymin": 0, "ymax": r["valor"] + 4, "qui": "Pista · a = 4 m/s²"},
         "El cotxe surt del repòs i als 50 m ja porta velocitat."))

    r = R("mrua_a_x", {"v0": 16, "v": 4, "dx": 40}, "a", "m/s²")
    add("L’autobús que s’acosta a la parada", "mitjà",
        "<p>Un autobús passa de 16 m/s a 4 m/s en 40 m, amb acceleració constant, en acostar-se a la parada.</p>"
        "<p>Quant val l’acceleració?</p>",
        [r],
        solucio(
            "Coneixem les dues velocitats i la distància, no el temps. Aïllem l’acceleració de v² = v₀² + 2 a Δx.",
            EQ(r"a = (v^2 - v_0^2) / (2 \Delta x)"),
            igual("a", "(" + nsq(4) + " - " + nsq(16) + ") / (2 \cdot " + ntex(40, "m") + ")", r["valor"], r["decimals"], "m/s", "2"),
            f"L’autobús frena amb una acceleració de {valor(r['valor'], r['decimals'], 'm/s²')}. El signe negatiu vol dir que la velocitat disminueix."),
        ("grafica", {"trams": [[(0, 16), (40, 4)]], "xlabel": "x (m)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 48, "ymin": 0, "ymax": 20, "qui": "Autobús cap a la parada"},
         "De 16 m/s a 4 m/s en 40 m."))

    ra = R("mrua_a_t", {"v0": 2, "v": 14, "t": 6}, "a", "m/s²")
    rx = R("mrua_x", {"x0": 0, "v0": 2, "a": 2, "t": 6}, "x", "m")
    add("Gràfica d’un patinet que accelera", "mitjà",
        "<p>La gràfica velocitat-temps d’un patinet és una recta: a t = 0 porta 2 m/s i a t = 6 s porta 14 m/s.</p>"
        "<p>a) Quina acceleració llegeixes del pendent?</p>"
        "<p>b) Quin desplaçament fas amb l’àrea sota la recta?</p>",
        [ra, rx],
        solucio(
            "En una gràfica velocitat-temps el pendent és l’acceleració i l’àrea sota la gràfica és el desplaçament. Aquí l’àrea és un trapezi de bases 2 m/s i 14 m/s i altura 6 s.",
            EQ(r"a = \Delta v / \Delta t") + EQ(r"\Delta x = (v_0 + v) t / 2"),
            igual("a", "(" + ntex(14, "m/s") + " - " + ntex(2, "m/s") + ") / " + ntex(6, "s"), ra["valor"], ra["decimals"], "m/s", "2")
            + igual("\\Delta x", "(" + ntex(2, "m/s") + " + " + ntex(14, "m/s") + r") \cdot " + ntex(6, "s") + " / 2", rx["valor"], rx["decimals"], "m"),
            f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i el desplaçament és {valor(rx['valor'], rx['decimals'], 'm')}."),
        ("grafica", {"trams": [[(0, 2), (6, 14)]], "xlabel": "t (s)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 8, "ymin": 0, "ymax": 16, "qui": "Patinet · gràfica v–t"},
         "Recta de 2 m/s a 14 m/s en 6 s. El pendent és l’acceleració i l’àrea, el desplaçament."))

    rv = R("mrua_v", {"v0": 10, "a": -2, "t": 3}, "v", "m/s")
    rx1 = R("mrua_x", {"x0": 0, "v0": 10, "a": -2, "t": 3}, "x1", "m")
    rx = R("mru_x", {"x0": rx1["valor"], "v": rv["valor"], "t": 8}, "x", "m")
    add("El cotxe que frena i després manté", "mitjà",
        "<p>Un cotxe va a 10 m/s i frena a −2 m/s² durant 3 s. Després manté constant la velocitat que porta, durant 8 s més.</p>"
        "<p>a) Quina velocitat porta al final de la frenada?</p>"
        "<p>b) Quina posició té, respecte de l’inici, al final dels 8 s següents?</p>",
        [rv, rx1, rx],
        solucio(
            "Hi ha dos trams i no es poden ajuntar en un sol MRUA, perquè l’acceleració canvia. Al primer tram l’acceleració és −2 m/s². Al segon és zero, i la velocitat inicial d’aquest tram és la velocitat final del primer.",
            EQ(r"v = v_0 + a t") + EQ(r"x = x_1 + v t_2"),
            igual("v", ntex(10, "m/s") + " + (" + ntex(-2, "m/s", "2") + r") \cdot " + ntex(3, "s"), rv["valor"], rv["decimals"], "m/s")
            + igual("x_1", ntex(10, "m/s") + r" \cdot " + ntex(3, "s") + r" + \frac{1}{2} \cdot (" + ntex(-2, "m/s", "2") + r") \cdot " + ntex(3, "s") + "^2", rx1["valor"], rx1["decimals"], "m")
            + igual("x", ntex(rx1["valor"], "m") + " + " + ntex(rv["valor"], "m/s") + r" \cdot " + ntex(8, "s"), rx["valor"], rx["decimals"], "m"),
            f"En acabar de frenar porta {valor(rv['valor'], rv['decimals'], 'm/s')} i és a {valor(rx1['valor'], rx1['decimals'], 'm')}. Al final de tot és a {valor(rx['valor'], rx['decimals'], 'm')}."),
        ("grafica", {"trams": [[(0, 10), (3, rv["valor"]), (11, rv["valor"])]], "xlabel": "t (s)", "ylabel": "v (m/s)",
                     "xmin": 0, "xmax": 12, "ymin": 0, "ymax": 12, "qui": "Cotxe · frena 3 s i després manté"},
         "Primer la velocitat baixa i després és una recta horitzontal."))

    def caig(titol, niv, enun, h, qui, perque, frase):
        rt = R("caiguda_t", {"h": h}, "t", "s")
        rv = R("caiguda_v", {"h": h}, "v", "m/s")
        add(titol, niv, enun, [rt, rv],
            solucio(perque, EQ(r"h = \frac{1}{2} g t^2") + EQ(r"v = \sqrt{2 g h}"),
                    igual("t", r"\sqrt{2 \cdot " + ntex(h, "m") + " / " + ntex(9.8, "m/s", "2") + "}", rt["valor"], rt["decimals"], "s")
                    + igual("v", r"\sqrt{2 \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(h, "m") + "}", rv["valor"], rv["decimals"], "m/s"),
                    frase(rt, rv)),
            ("caiguda", {"h": f"h = {fmt(h, dec(h))} m", "qui": qui}, f"Caiguda des de {fmt(h, dec(h))} m, des del repòs."))

    caig("La pedra del penya-segat", "senzill",
         "<p>Des d’un penya-segat de 19,6 m es deixa caure una pedra, sense velocitat inicial. Es negligeix l’aire i es pren g = 9,8 m/s².</p><p>a) Quant triga a arribar a l’aigua?</p><p>b) Amb quina velocitat hi arriba?</p>",
         19.6, "Pedra · penya-segat 19,6 m",
         "És una caiguda lliure des del repòs: l’acceleració és g cap avall i la velocitat inicial és zero. El temps surt de l’altura i la velocitat, del mateix desnivell.",
         lambda rt, rv: f"La pedra triga {valor(rt['valor'], rt['decimals'], 's')} i arriba a l’aigua a {valor(rv['valor'], rv['decimals'], 'm/s')}.")

    caig("El test de la finestra", "senzill",
         "<p>Un test rellisca de l’ampit d’una finestra situada a 4,9 m del terra i cau des del repòs. g = 9,8 m/s².</p><p>a) Quant triga a arribar a terra?</p><p>b) A quina velocitat ho fa?</p>",
         4.9, "Test · finestra a 4,9 m",
         "El test parteix del repòs i només l’accelera la gravetat. Per això el temps depèn de l’altura i no de la massa del test.",
         lambda rt, rv: f"El test triga {valor(rt['valor'], rt['decimals'], 's')} i arriba a {valor(rv['valor'], rv['decimals'], 'm/s')}.")

    caig("El salt des del pont", "senzill",
         "<p>Una persona salta des d’un pont de 10 m sobre el riu. Es pot prendre la caiguda com a lliure i des del repòs. g = 9,8 m/s².</p><p>a) Quant dura la caiguda?</p><p>b) A quina velocitat arriba a l’aigua?</p>",
         10, "Salt · pont de 10 m",
         "Si es negligeix l’aire, el salt és una caiguda lliure. L’altura fixa el temps i la velocitat d’arribada.",
         lambda rt, rv: f"La caiguda dura {valor(rt['valor'], rt['decimals'], 's')} i arriba a l’aigua a {valor(rv['valor'], rv['decimals'], 'm/s')}.")

    caig("La pilota del terrat", "senzill",
         "<p>Una pilota cau des del terrat d’un edifici de 45 m, partint del repòs. g = 9,8 m/s².</p><p>a) Quant triga?</p><p>b) Amb quina velocitat arriba al carrer?</p>",
         45, "Pilota · terrat de 45 m",
         "Caiguda lliure des del repòs: v₀ = 0 i a = g cap avall. No cal la massa de la pilota.",
         lambda rt, rv: f"La pilota triga {valor(rt['valor'], rt['decimals'], 's')} i arriba a {valor(rv['valor'], rv['decimals'], 'm/s')}.")

    caig("El paquet de la grua", "senzill",
         "<p>Un paquet es desprèn d’una grua i cau 5 m fins a terra, des del repòs. g = 9,8 m/s².</p><p>a) Quant triga?</p><p>b) A quina velocitat topa a terra?</p>",
         5, "Paquet · grua, 5 m",
         "El paquet surt del repòs. El temps i la velocitat es troben només amb l’altura i g.",
         lambda rt, rv: f"El paquet triga {valor(rt['valor'], rt['decimals'], 's')} i topa a {valor(rv['valor'], rv['decimals'], 'm/s')}.")

    def llanc(titol, niv, enun, v0, qui):
        rh = R("llanc_h", {"v0": v0}, "h", "m")
        rt = R("llanc_t_dalt", {"v0": v0}, "t", "s")
        rT = R("llanc_t_total", {"v0": v0}, "T", "s")
        add(titol, niv, enun, [rh, rt, rT],
            solucio(
                "Amb l’eix cap amunt l’acceleració és −g durant tot el vol, també al punt més alt. Allà la velocitat és zero, i per això l’alçada surt de v₀² = 2 g h. La baixada fins al mateix punt dura el mateix que la pujada.",
                EQ(r"h = v_0^2 / (2 g)") + EQ(r"t = v_0 / g"),
                igual("h", nsq(v0) + " / (2 \cdot " + ntex(9.8, "m/s", "2") + ")", rh["valor"], rh["decimals"], "m")
                + igual("t", ntex(v0, "m/s") + " / " + ntex(9.8, "m/s", "2"), rt["valor"], rt["decimals"], "s")
                + igual("T", "2 \cdot " + ntex(rt["valor"], "s"), rT["valor"], rT["decimals"], "s"),
                f"Puja {valor(rh['valor'], rh['decimals'], 'm')}, triga {valor(rt['valor'], rt['decimals'], 's')} a arribar-hi i {valor(rT['valor'], rT['decimals'], 's')} a tornar al punt de partida."),
            ("llancament", {"qui": qui}, "Llançament cap amunt. Al punt més alt la velocitat és zero i l’acceleració no."))

    llanc("La pilota de la classe de gimnàs", "senzill",
          "<p>A gimnàs es llança una pilota verticalment cap amunt a 14 m/s des del terra. g = 9,8 m/s² i l’eix apunta cap amunt.</p><p>a) Quina alçada màxima assoleix?</p><p>b) Quant triga a arribar-hi?</p><p>c) Quant triga a tornar a la mà, si es queda a la mateixa altura?</p>",
          14, "Pilota · v₀ = 14 m/s")
    llanc("El coet d’aigua", "senzill",
          "<p>Un coet d’aigua puja en vertical amb una velocitat inicial de 19,6 m/s. Després d’aquest impuls ja no fa força: només cau sota la gravetat. g = 9,8 m/s².</p><p>a) Quina alçada màxima assoleix?</p><p>b) Quant triga a arribar-hi?</p><p>c) Quant triga a tornar a terra?</p>",
          19.6, "Coet d’aigua · v₀ = 19,6 m/s")
    llanc("La fletxa vertical", "mitjà",
          "<p>Es dispara una fletxa verticalment cap amunt a 28 m/s. Es negligeix l’aire. g = 9,8 m/s².</p><p>a) Quina alçada màxima assoleix?</p><p>b) Quant triga a arribar-hi?</p><p>c) Quant triga a tornar a l’altura de sortida?</p>",
          28, "Fletxa · v₀ = 28 m/s")
    llanc("La clau llançada cap amunt", "senzill",
          "<p>Es llança una clau verticalment cap amunt a 9,8 m/s. g = 9,8 m/s².</p><p>a) Quina alçada màxima assoleix?</p><p>b) Quant triga a arribar-hi?</p><p>c) Quant triga a tornar al punt de partida?</p>",
          9.8, "Clau · v₀ = 9,8 m/s")

    ry = R("vertical_y", {"y0": 0, "v0": 20, "t": 1}, "y", "m")
    rv = R("vertical_v", {"v0": 20, "t": 1}, "v", "m/s")
    add("La pedra al cap d’un segon", "mitjà",
        "<p>Es llança una pedra verticalment cap amunt a 20 m/s des del terra. Eix cap amunt i g = 9,8 m/s².</p>"
        "<p>a) A quina altura és al cap d’1 s?</p><p>b) Quina velocitat hi porta, i encara puja o ja baixa?</p>",
        [ry, rv],
        solucio(
            "És un MRUA vertical amb acceleració −g des del primer instant. Al cap d’1 s encara no ha arribat dalt de tot, i el signe de la velocitat diu si puja o baixa.",
            EQ(r"y = v_0 t - \frac{1}{2} g t^2") + EQ(r"v = v_0 - g t"),
            igual("y", ntex(20, "m/s") + r" \cdot " + ntex(1, "s") + r" - \frac{1}{2} \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(1, "s") + "^2", ry["valor"], ry["decimals"], "m")
            + igual("v", ntex(20, "m/s") + " - " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(1, "s"), rv["valor"], rv["decimals"], "m/s"),
            f"Al cap d’1 s la pedra és a {valor(ry['valor'], ry['decimals'], 'm')} i porta {valor(rv['valor'], rv['decimals'], 'm/s')}. El signe positiu vol dir que encara puja."),
        ("llancament", {"qui": "Pedra · v₀ = 20 m/s · t = 1 s"}, "Es demana la situació al cap d’un segon, abans del punt més alt."))

    r = R("mru_v", {"x0": 0, "x": 400, "t": 50}, "v", "m/s")
    add("L’autobús urbà", "senzill",
        "<p>L’autobús urbà fa 400 m de carrer recte en 50 s, a velocitat constant, entre dues parades.</p><p>Quina velocitat porta?</p>",
        [r],
        solucio("Entre parades la velocitat és constant, així que és el desplaçament dividit pel temps.",
                EQ(r"v = \Delta x / \Delta t"),
                igual("v", ntex(400, "m") + " / " + ntex(50, "s"), r["valor"], r["decimals"], "m/s"),
                f"L’autobús porta {valor(r['valor'], r['decimals'], 'm/s')}."),
        ("eix", {"punts": [(0.12, "parada 1", "#5c6570"), (0.78, "parada 2", "#1f5fbf")], "cota": (0.12, 0.78, "400 m"), "qui": "Autobús urbà"},
         "400 m entre dues parades, en 50 s."))

    r = R("mru_x", {"x0": 0, "v": 4, "t": 12}, "x", "m")
    add("El corredor dels 100 m", "senzill",
        "<p>En un tram d’entrenament, un corredor manté 4 m/s constants.</p><p>Quina distància fa en 12 s?</p>",
        [r],
        solucio("En aquest tram la velocitat no canvia. La distància, que aquí coincideix amb el desplaçament, és v t.",
                EQ(r"x = v t"),
                igual("x", ntex(4, "m/s") + r" \cdot " + ntex(12, "s"), r["valor"], r["decimals"], "m"),
                f"En 12 s el corredor fa {valor(r['valor'], r['decimals'], 'm')}."),
        ("eix", {"punts": [(0.12, "sortida", "#5c6570"), (0.7, "12 s", "#1f5fbf")], "cota": (0.12, 0.7, "4 m/s"), "qui": "Corredor · 4 m/s"},
         "Tram a velocitat constant."))

    rv = R("mrua_v", {"v0": 0, "a": 1, "t": 6}, "v", "m/s")
    rx = R("mrua_x", {"x0": 0, "v0": 0, "a": 1, "t": 6}, "x", "m")
    add("La cursa de l’ascensor de l’obra", "senzill",
        "<p>L’elevador d’una obra surt del terra del repòs i puja amb una acceleració constant d’1 m/s² durant 6 s.</p><p>a) Quina velocitat porta?</p><p>b) A quina altura és?</p>",
        [rv, rx],
        solucio("Surt del repòs amb acceleració constant cap amunt: és un MRUA. La velocitat és a t i l’altura és ½ a t².",
                EQ(r"v = a t") + EQ(r"y = \frac{1}{2} a t^2"),
                igual("v", ntex(1, "m/s", "2") + r" \cdot " + ntex(6, "s"), rv["valor"], rv["decimals"], "m/s")
                + igual("y", r"\frac{1}{2} \cdot " + ntex(1, "m/s", "2") + r" \cdot " + ntex(6, "s") + "^2", rx["valor"], rx["decimals"], "m"),
                f"Al cap de 6 s l’elevador porta {valor(rv['valor'], rv['decimals'], 'm/s')} i és a {valor(rx['valor'], rx['decimals'], 'm')}."),
        ("llancament", {"qui": "Elevador de l’obra · a = 1 m/s² · 6 s"}, "Puja des del repòs amb acceleració constant."))
    return out
