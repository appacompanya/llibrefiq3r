"""Problemes de tir, MCU, Newton, forces, energia i mixtos. Nivell de 1r."""
from banc import P, R, dec, ntex, nsq
from peces import EQ, igual, solucio, valor


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

    def hor(titol, niv, enun, h, v0, qui, perque, cloenda, demana):
        tots = {
            "t": R("tir_h_t", {"h": h}, "t", "s"),
            "R": R("tir_h_R", {"h": h, "v0": v0}, "R", "m"),
            "vy": R("tir_h_vy", {"h": h}, "vy", "m/s"),
            "v": R("tir_h_v", {"h": h, "v0": v0}, "v", "m/s"),
        }
        res = [tots[k] for k in demana]
        blocs = ""
        if "t" in demana:
            blocs += igual("t", r"\sqrt{2 \cdot " + ntex(h, "m") + " / " + ntex(9.8, "m/s", "2") + "}", tots["t"]["valor"], tots["t"]["decimals"], "s")
        if "R" in demana:
            blocs += igual("R", ntex(v0, "m/s") + r" \cdot " + ntex(tots["t"]["valor"], "s"), tots["R"]["valor"], tots["R"]["decimals"], "m")
        if "vy" in demana:
            blocs += igual("v_y", ntex(9.8, "m/s", "2") + r" \cdot " + ntex(tots["t"]["valor"], "s"), tots["vy"]["valor"], tots["vy"]["decimals"], "m/s")
        if "v" in demana:
            blocs += igual("v", r"\sqrt{" + nsq(v0) + " + " + nsq(tots["vy"]["valor"]) + "}", tots["v"]["valor"], tots["v"]["decimals"], "m/s")
        add(titol, niv, enun, res,
            solucio(perque, EQ(r"t = \sqrt{2h/g}") + EQ(r"R = v_0 t"), blocs, cloenda(tots)),
            ("tir_h", {"h": f"h = {ntex(h, 'm').split(chr(92))[0]} m".replace("mathrm{m}", "").replace(",", ","), "v": f"v₀ = {fmt_simple(v0)} m/s", "qui": qui},
             f"{qui}. L’altura i la velocitat horitzontal són les de l’enunciat."))

    # The h label above is messy. I'll set labels simply below by not using that hack.
    # Redefine hor cleanly.
    return _tir_real(out, add)


def fmt_simple(x):
    from peces import fmt
    return fmt(x, dec(x))


def _tir_real(out, add):
    from peces import fmt

    def H(titol, niv, enun, h, v0, qui, perque, cloenda, demana):
        t = R("tir_h_t", {"h": h}, "t", "s")
        RR = R("tir_h_R", {"h": h, "v0": v0}, "R", "m")
        vy = R("tir_h_vy", {"h": h}, "vy", "m/s")
        v = R("tir_h_v", {"h": h, "v0": v0}, "v", "m/s")
        bag = {"t": t, "R": RR, "vy": vy, "v": v}
        blocs = ""
        if "t" in demana:
            blocs += igual("t", r"\sqrt{2 \cdot " + ntex(h, "m") + " / " + ntex(9.8, "m/s", "2") + "}", t["valor"], t["decimals"], "s")
        if "R" in demana:
            blocs += igual("R", ntex(v0, "m/s") + r" \cdot " + ntex(t["valor"], "s"), RR["valor"], RR["decimals"], "m")
        if "vy" in demana:
            blocs += igual("v_y", ntex(9.8, "m/s", "2") + r" \cdot " + ntex(t["valor"], "s"), vy["valor"], vy["decimals"], "m/s")
        if "v" in demana:
            blocs += igual("v", r"\sqrt{" + nsq(v0) + " + " + nsq(vy["valor"]) + "}", v["valor"], v["decimals"], "m/s")
        add(titol, niv, enun, [bag[k] for k in demana],
            solucio(perque, EQ(r"t = \sqrt{2h/g},\quad R = v_0 t"), blocs, cloenda(bag)),
            ("tir_h", {"h": f"{fmt(h, dec(h))} m", "v": f"{fmt(v0, dec(v0))} m/s", "qui": qui},
             "Tir horitzontal: la velocitat inicial no té component vertical."))

    H("La pilota des del penya-segat", "senzill",
      "<p>Des del penya-segat de la cala, a 19,6 m sobre l’aigua, es llança una pilota en horitzontal a 10 m/s. Es negligeix l’aire i g = 9,8 m/s².</p><p>a) Quant triga a caure a l’aigua?</p><p>b) A quina distància horitzontal de la base del penya-segat cau?</p>",
      19.6, 10, "Pilota · penya-segat 19,6 m · 10 m/s",
      "El llançament és horitzontal: la velocitat vertical inicial és zero i la horitzontal no canvia, perquè en horitzontal no hi ha acceleració. El temps és el d’una caiguda des de 19,6 m.",
      lambda b: f"La pilota triga {valor(b['t']['valor'], b['t']['decimals'], 's')} i cau a {valor(b['R']['valor'], b['R']['decimals'], 'm')} de la base.",
      ("t", "R"))

    H("El paquet de l’avió d’emergència", "senzill",
      "<p>Un avió deixa anar un paquet d’emergència en horitzontal a 40 m/s quan vola a 45 m d’altura, a velocitat constant. Es negligeix l’aire. g = 9,8 m/s².</p><p>a) Quant triga el paquet a arribar a terra?</p><p>b) Quin abast horitzontal fa?</p>",
      45, 40, "Paquet · avió a 45 m · 40 m/s",
      "En el moment de deixar-lo anar, el paquet ja porta la velocitat horitzontal de l’avió i velocitat vertical zero. El temps de caiguda només depèn de l’altura.",
      lambda b: f"El paquet triga {valor(b['t']['valor'], b['t']['decimals'], 's')} i avança {valor(b['R']['valor'], b['R']['decimals'], 'm')} en horitzontal.",
      ("t", "R"))

    H("El rajolí de la font", "senzill",
      "<p>El rajolí d’una font de la plaça surt en horitzontal a 3 m/s des d’un broc situat a 1,25 m del bassal. g = 9,8 m/s².</p><p>a) Quant triga l’aigua a arribar al bassal?</p><p>b) A quina distància del peu de la font cau?</p>",
      1.25, 3, "Font · broc a 1,25 m · 3 m/s",
      "El rajolí surt en horitzontal. Cada gota fa un tir horitzontal: cau amb g i avança a 3 m/s.",
      lambda b: f"L’aigua triga {valor(b['t']['valor'], b['t']['decimals'], 's')} i cau a {valor(b['R']['valor'], b['R']['decimals'], 'm')} del peu de la font.",
      ("t", "R"))

    H("L’esquiador del trampolí", "mitjà",
      "<p>Un esquiador surt en horitzontal a 12 m/s d’un trampolí situat a 5 m per sobre del pendent d’arribada, que en aquest tram considerem horitzontal. g = 9,8 m/s².</p><p>a) Quant està a l’aire?</p><p>b) Quin abast fa?</p><p>c) Amb quina velocitat vertical arriba?</p>",
      5, 12, "Esquiador · trampolí 5 m · 12 m/s",
      "Surt en horitzontal, així que v_y inicial és zero. La velocitat vertical en arribar és g t, cap avall, i no depèn dels 12 m/s.",
      lambda b: f"Està a l’aire {valor(b['t']['valor'], b['t']['decimals'], 's')}, fa un abast de {valor(b['R']['valor'], b['R']['decimals'], 'm')} i arriba amb una velocitat vertical de {valor(b['vy']['valor'], b['vy']['decimals'], 'm/s')}.",
      ("t", "R", "vy"))

    H("La galleda del camió", "senzill",
      "<p>De la caixa d’un camió, a 1,8 m del terra, una galleda surt en horitzontal a 6 m/s perquè el camió frena de cop. g = 9,8 m/s².</p><p>a) Quant triga a arribar a terra?</p><p>b) A quants metres del camió, en horitzontal, cau?</p>",
      1.8, 6, "Galleda · caixa a 1,8 m · 6 m/s",
      "En sortir de la caixa la galleda conserva la velocitat horitzontal i comença a caure. El temps no depèn dels 6 m/s.",
      lambda b: f"La galleda triga {valor(b['t']['valor'], b['t']['decimals'], 's')} i cau a {valor(b['R']['valor'], b['R']['decimals'], 'm')} en horitzontal.",
      ("t", "R"))

    H("El dron que deixa el paquet", "mitjà",
      "<p>Un dron deixa un paquet quan vola en horitzontal a 8 m/s i a 20 m del terra. g = 9,8 m/s².</p><p>a) Quant triga el paquet a arribar a terra?</p><p>b) Quin abast fa?</p><p>c) Quin mòdul de velocitat porta en arribar?</p>",
      20, 8, "Dron · 20 m · 8 m/s",
      "El paquet surt amb la velocitat horitzontal del dron. En arribar, aquesta component encara val 8 m/s i la vertical és la d’una caiguda de 20 m. El mòdul es troba amb Pitàgores.",
      lambda b: f"El paquet triga {valor(b['t']['valor'], b['t']['decimals'], 's')}, avança {valor(b['R']['valor'], b['R']['decimals'], 'm')} i arriba a {valor(b['v']['valor'], b['v']['decimals'], 'm/s')}.",
      ("t", "R", "v"))

    H("La xinxeta de la taula", "senzill",
      "<p>Una xinxeta llisca i surt per la vora d’una taula de 0,8 m d’altura a 2 m/s en horitzontal. g = 9,8 m/s².</p><p>a) Quant triga a arribar a terra?</p><p>b) A quina distància de la pota de la taula cau?</p>",
      0.8, 2, "Xinxeta · taula 0,8 m · 2 m/s",
      "És un tir horitzontal des de l’altura de la taula. El temps és el de la caiguda i l’abast és v₀ t.",
      lambda b: f"La xinxeta triga {valor(b['t']['valor'], b['t']['decimals'], 's')} i cau a {valor(b['R']['valor'], b['R']['decimals'], 'm')} de la pota.",
      ("t", "R"))

    H("El porter treu de puny", "mitjà",
      "<p>Un porter treu de puny en horitzontal a 15 m/s. La mà és a 2,2 m del terra. g = 9,8 m/s².</p><p>a) Quant triga la pilota a tocar terra?</p><p>b) Quin abast fa?</p><p>c) Quina velocitat vertical porta en tocar terra?</p>",
      2.2, 15, "Porter · mà a 2,2 m · 15 m/s",
      "La pilota surt en horitzontal des de l’altura de la mà. La velocitat vertical en arribar és g t i no depèn dels 15 m/s.",
      lambda b: f"La pilota triga {valor(b['t']['valor'], b['t']['decimals'], 's')}, fa {valor(b['R']['valor'], b['R']['decimals'], 'm')} d’abast i arriba amb {valor(b['vy']['valor'], b['vy']['decimals'], 'm/s')} cap avall.",
      ("t", "R", "vy"))

    H("La mànega del jardí", "senzill",
      "<p>Una mànega llança aigua en horitzontal a 7 m/s des d’una alçada d’1,5 m. g = 9,8 m/s².</p><p>a) Quant triga l’aigua a arribar a terra?</p><p>b) Fins a quina distància rega, en horitzontal?</p>",
      1.5, 7, "Mànega · 1,5 m · 7 m/s",
      "Cada gota fa un tir horitzontal. La distància de reg és l’abast R = v₀ t.",
      lambda b: f"L’aigua triga {valor(b['t']['valor'], b['t']['decimals'], 's')} i rega fins a {valor(b['R']['valor'], b['R']['decimals'], 'm')}.",
      ("t", "R"))

    H("El llibre de la finestra", "senzill",
      "<p>Un llibre surt en horitzontal a 4 m/s per una finestra situada a 7,2 m del pati. g = 9,8 m/s².</p><p>a) Quant triga a arribar al pati?</p><p>b) A quina distància de la paret cau?</p>",
      7.2, 4, "Llibre · finestra a 7,2 m · 4 m/s",
      "El llibre surt en horitzontal. El temps només depèn dels 7,2 m i l’abast, dels 4 m/s i d’aquest temps.",
      lambda b: f"El llibre triga {valor(b['t']['valor'], b['t']['decimals'], 's')} i cau a {valor(b['R']['valor'], b['R']['decimals'], 'm')} de la paret.",
      ("t", "R"))

    # velocitat necessària (problema invers)
    rv = R("tir_h_v0", {"h": 4.9, "R": 10}, "v", "m/s")
    rt = R("tir_h_t", {"h": 4.9}, "t", "s")
    add("Quina velocitat ha de portar el patinet", "mitjà",
        "<p>Un patinet surt en horitzontal per l’extrem d’una rampa situada a 4,9 m del terra. Es vol que caigui en un coixí situat a 10 m en horitzontal. g = 9,8 m/s².</p><p>a) Quant triga la caiguda?</p><p>b) A quina velocitat horitzontal ha de sortir?</p>",
        [rt, rv],
        solucio(
            "L’altura fixa el temps, perquè surt en horitzontal. L’abast que volem és v₀ t, així que la velocitat és l’abast dividit per aquest temps.",
            EQ(r"t = \sqrt{2h/g}") + EQ(r"v_0 = R / t"),
            igual("t", r"\sqrt{2 \cdot " + ntex(4.9, "m") + " / " + ntex(9.8, "m/s", "2") + "}", rt["valor"], rt["decimals"], "s")
            + igual("v_0", ntex(10, "m") + " / " + ntex(rt["valor"], "s"), rv["valor"], rv["decimals"], "m/s"),
            f"La caiguda dura {valor(rt['valor'], rt['decimals'], 's')} i el patinet ha de sortir a {valor(rv['valor'], rv['decimals'], 'm/s')}."),
        ("tir_h", {"h": "4,9 m", "v": "v₀ ?", "qui": "Patinet · rampa 4,9 m · coixí a 10 m"},
         "Es busca la velocitat horitzontal per caure al coixí."))

    def obl(titol, niv, enun, v0, th, qui, perque, cloenda, demana):
        bag = {
            "t": R("tir_t", {"v0": v0, "theta": th}, "t", "s"),
            "H": R("tir_H", {"v0": v0, "theta": th}, "H", "m"),
            "R": R("tir_R", {"v0": v0, "theta": th}, "R", "m"),
            "vx": R("tir_vx", {"v0": v0, "theta": th}, "vx", "m/s"),
        }
        blocs = ""
        if "vx" in demana:
            blocs += igual("v_x", ntex(v0, "m/s") + r" \cdot \cos " + f"{th}" + r"^\circ", bag["vx"]["valor"], bag["vx"]["decimals"], "m/s")
        if "t" in demana:
            blocs += igual("t", "2 \cdot " + ntex(v0, "m/s") + r" \cdot \sin " + f"{th}" + r"^\circ / " + ntex(9.8, "m/s", "2"), bag["t"]["valor"], bag["t"]["decimals"], "s")
        if "H" in demana:
            blocs += igual("H", "(" + ntex(v0, "m/s") + r" \cdot \sin " + f"{th}" + r"^\circ)^2 / (2 \cdot " + ntex(9.8, "m/s", "2") + ")", bag["H"]["valor"], bag["H"]["decimals"], "m")
        if "R" in demana:
            blocs += igual("R", nsq(v0) + " \cdot \\sin " + f"{2 * th}" + r"^\circ / " + ntex(9.8, "m/s", "2"), bag["R"]["valor"], bag["R"]["decimals"], "m")
        add(titol, niv, enun, [bag[k] for k in demana],
            solucio(perque, EQ(r"t = 2 v_0 \sin\theta / g") + EQ(r"H = (v_0 \sin\theta)^2 /(2g)") + EQ(r"R = v_0^2 \sin 2\theta / g"),
                    blocs, cloenda(bag)),
            ("tir_p", {"theta": th, "h": "H", "r": "R", "qui": qui},
             f"Tir des del terra a {th}° i {fmt(v0, dec(v0))} m/s."))

    obl("El xut de falta", "senzill",
        "<p>En l’entrenament d’una falta, el xut surt del terra a 14 m/s i a 45°. Es negligeix l’aire. g = 9,8 m/s².</p><p>a) Quant dura el vol fins a tornar a terra?</p><p>b) Quin abast fa?</p>",
        14, 45, "Xut · 14 m/s · 45°",
        "Surt i torna a la mateixa altura. A 45° el sinus de 2θ val 1, i l’abast és v₀²/g. El temps surt de la component vertical, que s’anul·la a dalt i es fa igual i oposada en tornar a terra.",
        lambda b: f"El xut dura {valor(b['t']['valor'], b['t']['decimals'], 's')} i l’abast és {valor(b['R']['valor'], b['R']['decimals'], 'm')}.",
        ("t", "R"))

    obl("La font a 30°", "senzill",
        "<p>Un rajolí de font surt del terra a 8 m/s i a 30°. g = 9,8 m/s².</p><p>a) Quina alçada màxima assoleix?</p><p>b) Quin abast fa sobre el terra?</p>",
        8, 30, "Font · 8 m/s · 30°",
        "El rajolí surt i torna al nivell del broc, que és a terra. A 30°, sin 30° = 1/2, i això simplifica l’alçada i el temps. L’abast fa servir sin 60°.",
        lambda b: f"L’aigua puja {valor(b['H']['valor'], b['H']['decimals'], 'm')} i cau a {valor(b['R']['valor'], b['R']['decimals'], 'm')} del broc.",
        ("H", "R"))

    obl("El llançador de pes", "mitjà",
        "<p>Un llançador de pes, en un entrenament, fa sortir el pes del terra a 10 m/s i a 30°. g = 9,8 m/s².</p><p>a) Quina és la component horitzontal de la velocitat?</p><p>b) Quina alçada màxima assoleix?</p><p>c) Quin abast fa?</p>",
        10, 30, "Pes · 10 m/s · 30°",
        "La component horitzontal no canvia i val v₀ cos 30°. L’alçada màxima només depèn de la component vertical. L’abast, de les dues.",
        lambda b: f"La component horitzontal és {valor(b['vx']['valor'], b['vx']['decimals'], 'm/s')}, l’alçada màxima és {valor(b['H']['valor'], b['H']['decimals'], 'm')} i l’abast és {valor(b['R']['valor'], b['R']['decimals'], 'm')}.",
        ("vx", "H", "R"))

    obl("El servei de tennis suau", "senzill",
        "<p>En un exercici, una pilota de tennis surt del terra a 12 m/s i a 60°. g = 9,8 m/s².</p><p>a) Quant dura el vol?</p><p>b) Quina alçada màxima assoleix?</p>",
        12, 60, "Tennis · 12 m/s · 60°",
        "Angle gran: puja molt i el temps de vol és llarg perquè sin 60° és gran. Surt i torna al mateix nivell.",
        lambda b: f"El vol dura {valor(b['t']['valor'], b['t']['decimals'], 's')} i l’alçada màxima és {valor(b['H']['valor'], b['H']['decimals'], 'm')}.",
        ("t", "H"))

    obl("La pedra a la platja", "senzill",
        "<p>Es llança una pedra des de la sorra a 20 m/s i a 30°. g = 9,8 m/s².</p><p>a) Quant dura fins a tornar a la sorra?</p><p>b) Quin abast fa?</p>",
        20, 30, "Pedra · platja · 20 m/s · 30°",
        "La sorra és horitzontal i el punt d’arribada és a la mateixa altura. Per això valen les fórmules del temps de vol i de l’abast.",
        lambda b: f"La pedra està {valor(b['t']['valor'], b['t']['decimals'], 's')} a l’aire i cau a {valor(b['R']['valor'], b['R']['decimals'], 'm')}.",
        ("t", "R"))

    obl("El globus d’aigua", "mitjà",
        "<p>En una festa es llança un globus d’aigua des del terra a 10 m/s i a 60°. g = 9,8 m/s².</p><p>a) Quina alçada màxima assoleix?</p><p>b) Al punt més alt, quina velocitat horitzontal li queda?</p>",
        10, 60, "Globus · 10 m/s · 60°",
        "Al punt més alt la velocitat vertical és zero, però la horitzontal no s’ha anul·lat: continua sent v₀ cos 60°. L’alçada surt només de la component vertical.",
        lambda b: f"El globus puja {valor(b['H']['valor'], b['H']['decimals'], 'm')} i al capdamunt encara porta {valor(b['vx']['valor'], b['vx']['decimals'], 'm/s')} en horitzontal.",
        ("H", "vx"))

    obl("El bàsquet d’entrenament", "mitjà",
        "<p>En un entrenament de bàsquet, la pilota surt de les mans arran de la pista, a 8 m/s i a 60°. g = 9,8 m/s².</p><p>a) Quina alçada màxima assoleix?</p><p>b) Si la cistella és a 3 m, aquesta alçada és suficient per passar-hi per sobre?</p>",
        8, 60, "Bàsquet · 8 m/s · 60°",
        "L’alçada màxima és (v₀ sin 60°)²/(2g). Després es compara amb els 3 m de la cistella. No cal el temps.",
        lambda b: f"La pilota puja {valor(b['H']['valor'], b['H']['decimals'], 'm')}. " + ("Això supera els 3 m de la cistella." if b["H"]["valor"] > 3 else "Això no arriba als 3 m de la cistella, així que aquest llançament no hi passaria per sobre."),
        ("H",))

    obl("El coet de fira", "senzill",
        "<p>Un coet de fira surt del terra a 15 m/s i a 45°, i després només actua el pes. g = 9,8 m/s².</p><p>a) Quin abast fa?</p><p>b) Quina alçada màxima assoleix?</p>",
        15, 45, "Coet de fira · 15 m/s · 45°",
        "A 45° l’abast és el màxim possible per a aquesta velocitat i val v₀²/g. L’alçada fa servir sin 45°.",
        lambda b: f"El coet fa un abast de {valor(b['R']['valor'], b['R']['decimals'], 'm')} i puja {valor(b['H']['valor'], b['H']['decimals'], 'm')}.",
        ("R", "H"))

    rv0 = R("tir_v0_R", {"R": 20, "theta": 45}, "v", "m/s")
    add("A quina velocitat cal xutar", "mitjà",
        "<p>Es vol que una pilota, xutada des del terra a 45°, faci un abast de 20 m. g = 9,8 m/s².</p><p>Quina velocitat inicial cal?</p>",
        [rv0],
        solucio(
            "A 45°, sin 90° = 1 i l’abast és v₀²/g. Aïllar la velocitat és un problema invers: no ens la donen, la busquem.",
            EQ(r"v_0 = \sqrt{R g}"),
            igual("v_0", r"\sqrt{" + ntex(20, "m") + r" \cdot " + ntex(9.8, "m/s", "2") + "}", rv0["valor"], rv0["decimals"], "m/s"),
            f"Cal xutar a {valor(rv0['valor'], rv0['decimals'], 'm/s')}."),
        ("tir_p", {"theta": 45, "h": "H", "r": "20 m", "qui": "Xut a 45° · abast 20 m"},
         "L’abast és una dada i l’angle és 45°."))

    # posició en un instant
    for titol, v0, th, t, qui, historia in [
        ("On és la pilota als 0,5 s", 20, 30, 0.5, "Pilota · 20 m/s · 30° · t = 0,5 s",
         "<p>Una pilota surt de l’origen a 20 m/s i a 30°. g = 9,8 m/s².</p><p>a) Quines coordenades (x, y) té al cap de 0,5 s?</p><p>b) Quin mòdul de velocitat porta en aquest instant?</p>"),
        ("El globus al cap d’1 s", 10, 60, 1, "Globus · 10 m/s · 60° · t = 1 s",
         "<p>Un globus d’aigua surt de l’origen a 10 m/s i a 60°. g = 9,8 m/s².</p><p>a) On és al cap d’1 s?</p><p>b) Quin mòdul de velocitat hi porta?</p>"),
    ]:
        rx = R("tir_x", {"v0": v0, "theta": th, "t": t}, "x", "m")
        ry = R("tir_y", {"v0": v0, "theta": th, "t": t}, "y", "m")
        rv = R("tir_vmod", {"v0": v0, "theta": th, "t": t}, "v", "m/s")
        vx = R("tir_vx", {"v0": v0, "theta": th}, "vx", "m/s")
        vy0 = R("tir_vy0", {"v0": v0, "theta": th}, "vy", "m/s")
        add(titol, "mitjà", historia, [rx, ry, rv],
            solucio(
                "El temps lliga els dos moviments. La x només avança amb la component horitzontal. La y és la d’un llançament vertical amb velocitat inicial v₀ sin θ. El mòdul junta vx, que no canvia, i vy en aquest instant.",
                EQ(r"x = (v_0 \cos\theta) t") + EQ(r"y = (v_0 \sin\theta) t - \frac12 g t^2"),
                igual("v_x", ntex(v0, "m/s") + rf" \cdot \cos {th}^\circ", vx["valor"], vx["decimals"], "m/s")
                + igual("x", ntex(vx["valor"], "m/s") + r" \cdot " + ntex(t, "s"), rx["valor"], rx["decimals"], "m")
                + igual("y", ntex(vy0["valor"], "m/s") + r" \cdot " + ntex(t, "s") + r" - \frac{1}{2} \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(t, "s") + "^2", ry["valor"], ry["decimals"], "m")
                + igual("v", r"\sqrt{" + nsq(vx["valor"]) + " + " + nsq(calc_vy(v0, th, t)) + "}", rv["valor"], rv["decimals"], "m/s"),
                f"És al punt x = {valor(rx['valor'], rx['decimals'], 'm')}, y = {valor(ry['valor'], ry['decimals'], 'm')}, i el mòdul de la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("tir_p", {"theta": th, "h": "y", "r": "x", "qui": qui},
             "Es demana un instant concret, no tot el vol."))

    # tres tirs més, preguntes diferents
    obl("La mànega a 45°", "senzill",
        "<p>Una mànega, arran de terra, llança aigua a 7 m/s i a 45°. g = 9,8 m/s².</p><p>a) Quin abast fa el raig sobre el terra?</p><p>b) Quina alçada màxima assoleix?</p>",
        7, 45, "Mànega a terra · 7 m/s · 45°",
        "El broc és a terra i l’aigua hi torna. A 45° l’abast és v₀²/g.",
        lambda b: f"El raig arriba a {valor(b['R']['valor'], b['R']['decimals'], 'm')} i puja {valor(b['H']['valor'], b['H']['decimals'], 'm')}.",
        ("R", "H"))

    obl("El llançament suau a 30°", "senzill",
        "<p>Es fa un llançament suau d’una pilota de platja des de la sorra, a 6 m/s i a 30°. g = 9,8 m/s².</p><p>a) Quant dura el vol?</p><p>b) Quina alçada màxima assoleix?</p>",
        6, 30, "Pilota de platja · 6 m/s · 30°",
        "Velocitat petita i angle de 30°: sin 30° = 1/2, així que la component vertical és la meitat de 6 m/s. El temps de vol és dues vegades el temps de pujada.",
        lambda b: f"El vol dura {valor(b['t']['valor'], b['t']['decimals'], 's')} i l’alçada màxima és {valor(b['H']['valor'], b['H']['decimals'], 'm')}.",
        ("t", "H"))

    obl("La fletxa a 45°", "mitjà",
        "<p>Una fletxa surt del terra a 18 m/s i a 45°. g = 9,8 m/s².</p><p>a) Quin abast fa?</p><p>b) Al punt més alt, quina velocitat li queda?</p>",
        18, 45, "Fletxa · 18 m/s · 45°",
        "A 45° les dues components inicials són iguals. Al punt més alt només queda la horitzontal, v₀ cos 45°.",
        lambda b: f"L’abast és {valor(b['R']['valor'], b['R']['decimals'], 'm')} i al capdamunt la fletxa encara porta {valor(b['vx']['valor'], b['vx']['decimals'], 'm/s')}.",
        ("R", "vx"))
    return out


def calc_vy(v0, th, t):
    from motor import calcular
    return calcular("tir_vy", {"v0": v0, "theta": th, "t": t})


def mcu():
    out, add = _cap("mcu", "3")

    def peri(titol, enun, T, qui):
        rw, rf = R("omega_T", {"T": T}, "w", "rad/s"), R("freq_T", {"T": T}, "f", "Hz")
        add(titol, "senzill", enun, [rf, rw],
            solucio(
                "El període és el temps d’una volta. La freqüència és l’invers, i la velocitat angular compta els 2π radiants de cada volta. No s’han de confondre Hz i rad/s.",
                EQ(r"f = 1/T") + EQ(r"\omega = 2\pi / T"),
                igual("f", "1 / " + ntex(T, "s"), rf["valor"], rf["decimals"], "Hz")
                + igual("\\omega", r"2 \cdot \pi \cdot " + ntex(rf["valor"], "Hz"), rw["valor"], rw["decimals"], "rad/s"),
                f"Fa {valor(rf['valor'], rf['decimals'], 'Hz')} i la velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')}."),
            ("mcu", {"r": "r", "qui": qui}, f"Una volta cada {fmt_s(T)} s."))

    peri("La nòria", "<p>La nòria del parc fa una volta cada 20 s, a ritme constant.</p><p>a) Quina freqüència té?</p><p>b) Quina velocitat angular?</p>", 20, "Nòria · T = 20 s")
    peri("El plat del microones", "<p>El plat del microones fa una volta cada 5 s.</p><p>a) Quina freqüència té?</p><p>b) Quina velocitat angular?</p>", 5, "Plat del microones · T = 5 s")
    peri("El carrusel", "<p>El carrusel de la fira fa una volta cada 8 s.</p><p>a) Quina freqüència té?</p><p>b) Quina velocitat angular?</p>", 8, "Carrusel · T = 8 s")
    peri("La rentadora al centrifugat", "<p>El bombo d’una rentadora, en un centrifugat lent de laboratori, fa una volta cada 0,5 s.</p><p>a) Quina freqüència té?</p><p>b) Quina velocitat angular?</p>", 0.5, "Rentadora · T = 0,5 s")
    peri("L’agulla del rellotge de cuina", "<p>El segoner d’un rellotge de cuina fa una volta cada 60 s.</p><p>a) Quina freqüència té?</p><p>b) Quina velocitat angular?</p>", 60, "Segoner · T = 60 s")
    peri("La sínia del poble", "<p>La sínia del poble fa una volta cada 12 s.</p><p>a) Quina freqüència té?</p><p>b) Quina velocitat angular?</p>", 12, "Sínia · T = 12 s")

    def punt(titol, enun, f, r, qui):
        rw = R("omega_f", {"f": f}, "w", "rad/s")
        rv = R("v_wr", {"omega": rw["valor"], "r": r}, "v", "m/s")
        add(titol, "mitjà", enun, [rw, rv],
            solucio(
                "La freqüència es passa a velocitat angular multiplicant per 2π. La velocitat lineal d’un punt és ω r: com més lluny de l’eix, més de pressa va.",
                EQ(r"\omega = 2\pi f") + EQ(r"v = \omega r"),
                igual("\\omega", r"2 \cdot \pi \cdot " + ntex(f, "Hz"), rw["valor"], rw["decimals"], "rad/s")
                + igual("v", ntex(rw["valor"], "rad/s") + r" \cdot " + ntex(r, "m"), rv["valor"], rv["decimals"], "m/s"),
                f"La velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')} i el punt va a {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("v_omega", {"qui": qui}, "v = ω r al punt indicat."))

    punt("La cadira exterior de la nòria", "<p>Una nòria gira a 0,05 Hz. Una cadira és a 8 m de l’eix.</p><p>a) Quina velocitat angular té la nòria?</p><p>b) A quina velocitat es mou la cadira?</p>", 0.05, 8, "Cadira de la nòria · r = 8 m · 0,05 Hz")
    punt("El torn del pou", "<p>Un torn gira a 2 Hz. La corda s’enrotlla en un cilindre de 0,15 m de radi.</p><p>a) Quina velocitat angular té el cilindre?</p><p>b) A quina velocitat puja la galleda, si no rellisca?</p>", 2, 0.15, "Torn del pou · r = 0,15 m · 2 Hz")
    punt("El disc de vinil", "<p>Un disc gira a 0,55 Hz. El solc exterior és a 0,14 m del centre.</p><p>a) Quina velocitat angular té?</p><p>b) A quina velocitat passa l’agulla per aquest solc?</p>", 0.55, 0.14, "Disc · r = 0,14 m")
    punt("L’hèlix del ventilador", "<p>Un ventilador gira a 8 Hz. La punta de l’hèlix és a 0,20 m de l’eix.</p><p>a) Quina velocitat angular té?</p><p>b) A quina velocitat es mou la punta?</p>", 8, 0.20, "Ventilador · punta a 0,20 m · 8 Hz")

    def corba(titol, enun, v, r, qui):
        rw = R("omega_vr", {"v": v, "r": r}, "w", "rad/s")
        ra = R("ac_v", {"v": v, "r": r}, "a", "m/s²")
        add(titol, "mitjà", enun, [rw, ra],
            solucio(
                "La rapidesa és constant, però la direcció canvia: hi ha acceleració centrípeta, cap al centre, de valor v²/r. La velocitat angular és v/r.",
                EQ(r"\omega = v/r") + EQ(r"a_c = v^2/r"),
                igual("\\omega", ntex(v, "m/s") + " / " + ntex(r, "m"), rw["valor"], rw["decimals"], "rad/s")
                + igual("a_c", nsq(v) + " / " + ntex(r, "m"), ra["valor"], ra["decimals"], "m/s", "2"),
                f"La velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')} i l’acceleració centrípeta és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
            ("mcu_vec", {"qui": qui}, "Velocitat tangent i acceleració cap al centre."))

    corba("El cotxe a la rotonda", "<p>Un cotxe pren una rotonda de 30 m de radi a 12 m/s constants.</p><p>a) Quina velocitat angular porta?</p><p>b) Quina acceleració centrípeta?</p>", 12, 30, "Cotxe · rotonda r = 30 m · 12 m/s")
    corba("La bicicleta al velòdrom", "<p>Una bicicleta va a 8 m/s per un velòdrom de 20 m de radi, a rapidesa constant.</p><p>a) Quina velocitat angular té?</p><p>b) Quina acceleració centrípeta?</p>", 8, 20, "Bicicleta · velòdrom r = 20 m · 8 m/s")
    corba("El cotxe de xoc", "<p>Un cotxe de xoc descriu una circumferència de 8 m de radi a 6 m/s constants.</p><p>a) Quina velocitat angular té?</p><p>b) Quina acceleració centrípeta?</p>", 6, 8, "Cotxe de xoc · r = 8 m · 6 m/s")
    corba("La pedra de la fona", "<p>Una fona fa girar una pedra a 10 m/s en una circumferència de 0,8 m de radi.</p><p>a) Quina velocitat angular té?</p><p>b) Quina acceleració centrípeta?</p>", 10, 0.8, "Fona · r = 0,8 m · 10 m/s")
    corba("El tren al revolt", "<p>Un tren pren un revolt de 400 m de radi a 20 m/s constants.</p><p>a) Quina velocitat angular té?</p><p>b) Quina acceleració centrípeta?</p>", 20, 400, "Tren · revolt r = 400 m · 20 m/s")
    corba("El patinador", "<p>Un patinador fa un cercle de 5 m de radi a 4 m/s constants.</p><p>a) Quina velocitat angular té?</p><p>b) Quina acceleració centrípeta?</p>", 4, 5, "Patinador · r = 5 m · 4 m/s")

    def omega_donada(titol, enun, w, r, qui):
        rv = R("v_wr", {"omega": w, "r": r}, "v", "m/s")
        ra = R("ac_w", {"omega": w, "r": r}, "a", "m/s²")
        add(titol, "senzill", enun, [rv, ra],
            solucio(
                "Ens donen la velocitat angular en rad/s. La velocitat lineal és ω r i l’acceleració centrípeta és ω² r.",
                EQ(r"v = \omega r") + EQ(r"a_c = \omega^2 r"),
                igual("v", ntex(w, "rad/s") + r" \cdot " + ntex(r, "m"), rv["valor"], rv["decimals"], "m/s")
                + igual("a_c", ntex(w, "rad/s") + "^2 \cdot " + ntex(r, "m"), ra["valor"], ra["decimals"], "m/s", "2"),
                f"La velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')} i l’acceleració centrípeta és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
            ("v_omega", {"qui": qui}, "Dades: ω i r."))

    omega_donada("El molinet de vent", "<p>Un molinet gira a 4 rad/s. Una bola de l’extrem és a 0,3 m de l’eix.</p><p>a) A quina velocitat es mou la bola?</p><p>b) Quina acceleració centrípeta té?</p>", 4, 0.3, "Molinet · 4 rad/s · r = 0,3 m")
    omega_donada("La grua que gira", "<p>El braç d’una grua gira a 0,2 rad/s. La càrrega penja a 25 m de l’eix de gir.</p><p>a) A quina velocitat es desplaça la càrrega?</p><p>b) Quina acceleració centrípeta té?</p>", 0.2, 25, "Grua · 0,2 rad/s · r = 25 m")
    omega_donada("El cavallet del carrusel", "<p>El carrusel gira a 0,8 rad/s. Un cavallet és a 4 m del centre.</p><p>a) A quina velocitat va el cavallet?</p><p>b) Quina acceleració centrípeta té?</p>", 0.8, 4, "Cavallet · 0,8 rad/s · r = 4 m")
    omega_donada("La bola del pèndol cònic de fira", "<p>Una bola lligada a un fil gira en horitzontal a 6 rad/s. El radi del cercle és 0,5 m.</p><p>a) A quina velocitat va la bola?</p><p>b) Quina acceleració centrípeta té?</p>", 6, 0.5, "Bola · 6 rad/s · r = 0,5 m")

    def arc(titol, enun, r, th, t, qui):
        rw = R("omega_theta", {"theta": th, "t": t}, "w", "rad/s")
        rs = R("arc", {"r": r, "theta": th}, "s", "m")
        add(titol, "mitjà", enun, [rw, rs],
            solucio(
                "L’angle ja és en radiants. La velocitat angular és l’angle partit pel temps, i la longitud de l’arc és r θ. Si l’angle fos en graus, primer s’hauria de passar a radiants.",
                EQ(r"\omega = \theta / t") + EQ(r"s = r \theta"),
                igual("\\omega", ntex(th, "rad") + " / " + ntex(t, "s"), rw["valor"], rw["decimals"], "rad/s")
                + igual("s", ntex(r, "m") + r" \cdot " + ntex(th, "rad"), rs["valor"], rs["decimals"], "m"),
                f"La velocitat angular és {valor(rw['valor'], rw['decimals'], 'rad/s')} i l’arc fa {valor(rs['valor'], rs['decimals'], 'm')}."),
            ("mcu", {"r": f"r = {fmt_s(r)} m", "qui": qui}, "L’arc és rθ, amb θ en radiants."))

    arc("El braç del robot", "<p>El braç d’un robot, de 0,5 m, gira un angle d’1 rad en 0,5 s, a ritme constant.</p><p>a) Quina velocitat angular té?</p><p>b) Quina longitud d’arc recorre la punta?</p>", 0.5, 1, 0.5, "Braç del robot · 1 rad")
    arc("La porta del garatge", "<p>Una porta corredissa circular, de radi 2 m, gira 0,5 rad en 2 s.</p><p>a) Quina velocitat angular té?</p><p>b) Quina longitud recorre l’extrem?</p>", 2, 0.5, 2, "Porta · radi 2 m · 0,5 rad")
    arc("L’eixugaparabrises", "<p>La punta d’un eixugaparabrises és a 0,4 m de l’eix i escombra 1 rad en 0,4 s.</p><p>a) Quina velocitat angular té?</p><p>b) Quina longitud de vidre escombra?</p>", 0.4, 1, 0.4, "Eixugaparabrises · 1 rad")
    arc("El focus de l’escenari", "<p>Un focus gira 1,5 rad en 3 s. El feix il·lumina un teló situat, en aquest moviment, sobre un arc de 4 m de radi.</p><p>a) Quina velocitat angular té el focus?</p><p>b) Quina longitud de teló escombra el feix?</p>", 4, 1.5, 3, "Focus · 1,5 rad · r = 4 m")

    for titol, enun, v, r, qui in [
        ("La formiga al disc", "<p>Una formiga camina a 0,05 m/s per la vora d’un disc de 0,1 m de radi, a rapidesa constant.</p><p>a) Quina acceleració centrípeta té?</p><p>b) Quant triga a fer una volta?</p>", 0.05, 0.1, "Formiga · r = 0,1 m"),
        ("El punt del pneumàtic", "<p>Un punt de la banda de rodament d’un pneumàtic de 0,3 m de radi es mou a 9 m/s respecte del centre, en un tram on la roda gira a ritme constant.</p><p>a) Quina acceleració centrípeta té?</p><p>b) Quant triga la roda a fer una volta?</p>", 9, 0.3, "Pneumàtic · r = 0,3 m · 9 m/s"),
    ]:
        ra = R("ac_v", {"v": v, "r": r}, "a", "m/s²")
        rT = R("T_vr", {"v": v, "r": r}, "T", "s")
        add(titol, "mitjà", enun, [ra, rT],
            solucio(
                "L’acceleració centrípeta és v²/r. El període és el temps d’una volta: la longitud 2πr dividida per la rapidesa.",
                EQ(r"a_c = v^2/r") + EQ(r"T = 2\pi r / v"),
                igual("a_c", nsq(v) + " / " + ntex(r, "m"), ra["valor"], ra["decimals"], "m/s", "2")
                + igual("T", r"2 \cdot \pi \cdot " + ntex(r, "m") + " / " + ntex(v, "m/s"), rT["valor"], rT["decimals"], "s"),
                f"L’acceleració centrípeta és {valor(ra['valor'], ra['decimals'], 'm/s²')} i una volta dura {valor(rT['valor'], rT['decimals'], 's')}."),
            ("mcu_vec", {"qui": qui}, "Rapidesa constant i acceleració cap al centre."))
    return out


def fmt_s(x):
    from peces import fmt
    return fmt(x, dec(x))


def newton():
    out, add = _cap("newton", "4")

    casos = [
        ("Empènyer el carretó", "Un carretó de 20 kg, amb les rodes que no frenen, rep una força resultant de direcció constant que li dona una acceleració de 0,5 m/s².", 20, 0.5, "Carretó · 20 kg · a = 0,5 m/s²"),
        ("El disc d’hoquei", "Un disc d’hoquei de 0,2 kg rep una força resultant que li dona una acceleració de 4 m/s² sobre el gel.", 0.2, 4, "Disc d’hoquei · 0,2 kg"),
        ("El cotxe que accelera", "Un cotxe de 1200 kg accelera a 1,5 m/s² en una recta. La força que es demana és la resultant, no la del motor sola.", 1200, 1.5, "Cotxe · 1200 kg · a = 1,5 m/s²"),
        ("La caixa del passadís", "S’empeny una caixa de 8 kg pel passadís i adquireix una acceleració de 0,8 m/s². La força que es demana és la resultant.", 8, 0.8, "Caixa · 8 kg"),
        ("El llibre sobre la taula d’aire", "Un llibre de 1,2 kg, damunt una taula d’aire, adquireix una acceleració de 3 m/s² sota una força resultant horitzontal.", 1.2, 3, "Llibre · 1,2 kg"),
        ("La pilota de bòling", "Una pilota de bòling de 5 kg rep una força resultant de 10 N? No: l’enunciat dona l’acceleració, 2 m/s², i es demana la resultant.", 5, 2, "Bòling · 5 kg · a = 2 m/s²"),
    ]
    # Fix the bowling enunciat to be clean
    casos[5] = ("La pilota de bòling", "Una pilota de bòling de 5 kg adquireix una acceleració de 2 m/s² en el sentit de la força resultant.", 5, 2, "Bòling · 5 kg · a = 2 m/s²")
    for titol, frase, m, a, qui in casos:
        r = R("f_ma", {"m": m, "a": a}, "F", "N")
        add(titol, "senzill", f"<p>{frase}</p><p>Quant val la força resultant?</p>", [r],
            solucio(
                "La segona llei diu que la força resultant és la massa multiplicada per l’acceleració. Resultant i acceleració tenen el mateix sentit. No s’hi han de sumar el pes ni la normal si ja es compensen i la dada és l’acceleració horitzontal.",
                EQ(r"F = m a"),
                igual("F", ntex(m, "kg") + r" \cdot " + ntex(a, "m/s", "2"), r["valor"], r["decimals"], "N"),
                f"La força resultant és {valor(r['valor'], r['decimals'], 'N')}."),
            ("fma", {"qui": qui}, "La mateixa relació F = m a, amb les dades d’aquest cas."))

    for titol, frase, F, m, qui in [
        ("Estirar el trineu al gel", "S’estira un trineu de 10 kg sobre gel polit amb una força resultant de 40 N.", 40, 10, "Trineu · 10 kg · F = 40 N"),
        ("La barca al canal", "Una barca de 80 kg rep una força resultant de 200 N en el sentit de la marxa.", 200, 80, "Barca · 80 kg · F = 200 N"),
        ("El calaix buit", "S’estira un calaix de 6 kg amb una força resultant de 15 N.", 15, 6, "Calaix · 6 kg · F = 15 N"),
        ("El contenidor", "Un contenidor de 250 kg rep una força resultant de 500 N.", 500, 250, "Contenidor · 250 kg · F = 500 N"),
        ("La maleta a la cinta", "Una maleta de 8 kg és a una cinta que li comunica una força resultant de 4 N en el sentit del moviment.", 4, 8, "Maleta · 8 kg · F = 4 N"),
        ("El monopatí", "Un monopatí, amb el genet, té una massa de 50 kg i rep una força resultant de 25 N.", 25, 50, "Monopatí · 50 kg · F = 25 N"),
    ]:
        r = R("a_fm", {"F": F, "m": m}, "a", "m/s²")
        add(titol, "senzill", f"<p>{frase} Quina acceleració adquireix?</p>", [r],
            solucio(
                "La força de l’enunciat ja és la resultant. L’acceleració és aquesta força dividida per la massa, en el mateix sentit.",
                EQ(r"a = F/m"),
                igual("a", ntex(F, "N") + " / " + ntex(m, "kg"), r["valor"], r["decimals"], "m/s", "2"),
                f"L’acceleració és {valor(r['valor'], r['decimals'], 'm/s²')}."),
            ("dcl", {"fregament": False, "força": True, "F": "F", "qui": qui}, "La fletxa F és la resultant d’aquest enunciat."))

    for titol, frase, m, qui in [
        ("El pes de l’alumne", "Un alumne té una massa de 60 kg.", 60, "Alumne · 60 kg"),
        ("El pes de la motxilla", "Una motxilla té una massa de 4 kg.", 4, "Motxilla · 4 kg"),
        ("El pes de la poma", "Una poma té una massa de 0,2 kg.", 0.2, "Poma · 0,2 kg"),
        ("El pes del cotxe petit", "Un cotxe petit té una massa de 900 kg.", 900, "Cotxe · 900 kg"),
        ("El pes del llibre de física", "El llibre de física té una massa de 0,8 kg.", 0.8, "Llibre · 0,8 kg"),
        ("El pes de la maleta", "Una maleta de mà té una massa de 8 kg.", 8, "Maleta · 8 kg"),
    ]:
        r = R("pes", {"m": m}, "P", "N")
        add(titol, "senzill", f"<p>{frase} Quant pesa, en newtons, a prop de la Terra? Pren g = 9,8 m/s². La massa seria la mateixa a la Lluna; el pes, no.</p>", [r],
            solucio(
                "El pes és la força d’atracció de la Terra, P = m g. No és la massa: es mesura en newtons.",
                EQ(r"P = m g"),
                igual("P", ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2"), r["valor"], r["decimals"], "N"),
                f"Pesa {valor(r['valor'], r['decimals'], 'N')}."),
            ("dcl", {"fregament": False, "força": False, "qui": qui}, "El pes és vertical i cap avall."))

    for titol, frase, F, a, qui in [
        ("Quina massa té el bloc", "Una força resultant de 30 N dona a un bloc una acceleració de 2 m/s².", 30, 2, "Bloc · F = 30 N · a = 2 m/s²"),
        ("La massa del carret", "Una força resultant de 7 N dona al carret una acceleració d’1,4 m/s².", 7, 1.4, "Carret · F = 7 N"),
        ("La massa de la sonda de joguina", "Una força resultant de 4 N dona a una sonda de joguina una acceleració de 0,2 m/s².", 4, 0.2, "Sonda · F = 4 N"),
        ("La massa del trineu", "Una força resultant de 12 N dona al trineu una acceleració de 0,5 m/s².", 12, 0.5, "Trineu · F = 12 N · a = 0,5 m/s²"),
    ]:
        r = R("m_fa", {"F": F, "a": a}, "m", "kg")
        add(titol, "senzill", f"<p>{frase} Quina massa té?</p>", [r],
            solucio(
                "És la segona llei a l’inrevés: la massa és la força resultant dividida per l’acceleració.",
                EQ(r"m = F/a"),
                igual("m", ntex(F, "N") + " / " + ntex(a, "m/s", "2"), r["valor"], r["decimals"], "kg"),
                f"La massa és {valor(r['valor'], r['decimals'], 'kg')}."),
            ("fma", {"qui": qui}, "Es busca la massa, no la força."))

    for titol, frase, m, qui in [
        ("El llibre quiet damunt la taula", "Un llibre de 1,5 kg està en repòs damunt la taula de l’aula.", 1.5, "Llibre · 1,5 kg · taula"),
        ("La caixa quieta a terra", "Una caixa de 12 kg està quieta a terra.", 12, "Caixa · 12 kg · terra"),
        ("L’ampolla quieta", "Una ampolla de 0,5 kg està quieta damunt el marbre.", 0.5, "Ampolla · 0,5 kg"),
        ("El banc del parc", "Un banc del parc, de 30 kg, està quiet a terra.", 30, "Banc · 30 kg"),
    ]:
        r = R("pes", {"m": m}, "N", "N")
        add(titol, "mitjà",
            f"<p>{frase}</p><p>a) Quant val la normal?</p><p>b) Quin mòdul té la força amb què l’objecte empeny la superfície? Recorda que aquesta força i la normal són un parell, i actuen sobre cossos diferents.</p>",
            [r],
            solucio(
                "Està en repòs, així que la resultant vertical és zero i la normal iguala el pes. Per la tercera llei, l’objecte empeny la superfície amb una força del mateix mòdul, però aquesta força no actua sobre l’objecte: actua sobre la taula o el terra.",
                EQ(r"N = m g"),
                igual("N", ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2"), r["valor"], r["decimals"], "N"),
                f"La normal i l’empenta sobre la superfície valen, cadascuna, {valor(r['valor'], r['decimals'], 'N')}."),
            ("parells", {"qui": qui}, "El pes i la normal actuen sobre l’objecte. El parell de la normal actua sobre la superfície."))

    r = R("pes", {"m": 3}, "P", "N")
    add("El pes del gat", "senzill",
        "<p>Un gat té una massa de 3 kg. Quant pesa, en newtons, a prop de la Terra? g = 9,8 m/s².</p>",
        [r],
        solucio("El pes és la força amb què la Terra atrau el gat. No s’ha de confondre amb la massa.",
                EQ(r"P = m g"),
                igual("P", ntex(3, "kg") + r" \cdot " + ntex(9.8, "m/s", "2"), r["valor"], r["decimals"], "N"),
                f"El gat pesa {valor(r['valor'], r['decimals'], 'N')}."),
        ("dcl", {"fregament": False, "força": False, "qui": "Gat · 3 kg"}, "El pes és vertical i cap avall."))

    r = R("a_fm", {"F": 6, "m": 12}, "a", "m/s²")
    add("El carro de la compra", "senzill",
        "<p>El carro de la compra, amb la bossa, té una massa de 12 kg i rep una força resultant de 6 N en el sentit de la marxa.</p><p>Quina acceleració adquireix?</p>",
        [r],
        solucio("La força de l’enunciat ja és la resultant. L’acceleració és F/m.",
                EQ(r"a = F/m"),
                igual("a", ntex(6, "N") + " / " + ntex(12, "kg"), r["valor"], r["decimals"], "m/s", "2"),
                f"El carro adquireix una acceleració de {valor(r['valor'], r['decimals'], 'm/s²')}."),
        ("dcl", {"fregament": False, "força": True, "F": "F", "qui": "Carro de la compra · 12 kg · F = 6 N"}, "La fletxa és la força resultant."))
    return out


def forces():
    out, add = _cap("forces", "5")

    def llis(titol, enun, F, m, qui):
        ra = R("a_hor", {"F": F, "m": m}, "a", "m/s²")
        rn = R("pes", {"m": m}, "N", "N")
        add(titol, "senzill", enun, [rn, ra],
            solucio(
                "El pla és horitzontal i llis: no hi ha fregament. En vertical el pes i la normal es compensen, perquè no hi ha acceleració vertical. En horitzontal la resultant és la força aplicada.",
                EQ(r"N = m g") + EQ(r"a = F/m"),
                igual("N", ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2"), rn["valor"], rn["decimals"], "N")
                + igual("a", ntex(F, "N") + " / " + ntex(m, "kg"), ra["valor"], ra["decimals"], "m/s", "2"),
                f"La normal és {valor(rn['valor'], rn['decimals'], 'N')} i l’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
            ("dcl", {"fregament": False, "força": True, "F": f"{fmt_s(F)} N", "massa": f"{fmt_s(m)} kg"},
             "Pla horitzontal llis: el pes i la normal es compensen."))

    llis("El trineu al gel llis", "<p>S’estira un trineu de 8 kg amb una força horitzontal de 24 N sobre gel que es pot considerar llis.</p><p>a) Quant val la normal?</p><p>b) Quina acceleració té el trineu?</p>", 24, 8, "Trineu · 8 kg · F = 24 N · gel llis")
    llis("La caixa al terra encerat", "<p>S’empeny una caixa de 4 kg amb una força horitzontal de 10 N per un terra encerat que considerem llis.</p><p>a) Quant val la normal?</p><p>b) Quina acceleració té?</p>", 10, 4, "Caixa · 4 kg · F = 10 N")
    llis("El disc a la taula d’aire", "<p>Un disc de 0,15 kg és damunt una taula d’aire i se l’empeny amb una força horitzontal de 0,3 N.</p><p>a) Quant val la normal?</p><p>b) Quina acceleració té?</p>", 0.3, 0.15, "Disc · 0,15 kg · F = 0,3 N")
    llis("El vagó a la via recta", "<p>S’estira un vagó de 200 kg amb una força horitzontal de 400 N per una via recta sense fregament apreciable.</p><p>a) Quant val la normal?</p><p>b) Quina acceleració té?</p>", 400, 200, "Vagó · 200 kg · F = 400 N")

    def freg(titol, enun, F, m, mu, qui):
        rf = R("freg_c", {"mu": mu, "N": m * 9.8}, "f", "N")
        ra = R("a_hor_f", {"F": F, "m": m, "mu": mu}, "a", "m/s²")
        add(titol, "mitjà", enun, [rf, ra],
            solucio(
                "El cos ja llisca, així que el fregament és el cinètic i val μ N. En un pla horitzontal la normal iguala el pes. La resultant horitzontal és la força aplicada menys el fregament, en el sentit de la força.",
                EQ(r"f = \mu m g") + EQ(r"a = (F - f)/m"),
                igual("f", ntex(mu, "") + r" \cdot " + ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2"), rf["valor"], rf["decimals"], "N")
                + igual("a", "(" + ntex(F, "N") + " - " + ntex(rf["valor"], "N") + ") / " + ntex(m, "kg"), ra["valor"], ra["decimals"], "m/s", "2"),
                f"El fregament és {valor(rf['valor'], rf['decimals'], 'N')} i l’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
            ("dcl", {"fregament": True, "força": True, "F": f"{fmt_s(F)} N", "massa": f"{fmt_s(m)} kg", "mu": f"μ = {str(mu).replace('.', ',')}"},
             "El fregament cinètic s’oposa al lliscament."))

    freg("La maleta que rellisca", "<p>S’estira una maleta de 6 kg amb una força horitzontal de 20 N. El coeficient de fregament cinètic amb el terra és 0,1 i la maleta ja llisca. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 20, 6, 0.1, "Maleta · 6 kg · F = 20 N · μ = 0,1")
    freg("El sofà pel passadís", "<p>S’empeny un sofà de 20 kg amb una força horitzontal de 80 N. El coeficient de fregament cinètic és 0,3 i el sofà ja llisca. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 80, 20, 0.3, "Sofà · 20 kg · F = 80 N · μ = 0,3")
    freg("El bloc del laboratori", "<p>Al laboratori, un bloc de 2 kg llisca per la taula. Se l’estira amb 12 N horitzontals i μ_c = 0,25. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 12, 2, 0.25, "Bloc de laboratori · 2 kg · μ = 0,25")
    freg("El trineu amb sorra", "<p>Un trineu de 8 kg, carregat de sorra, llisca per l’asfalt. Se l’estira amb 50 N i μ_c = 0,4. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 50, 8, 0.4, "Trineu amb sorra · 8 kg · μ = 0,4")
    freg("La nevera", "<p>Es fa lliscar una nevera de 40 kg amb una força horitzontal de 100 N. μ_c = 0,15. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 100, 40, 0.15, "Nevera · 40 kg · F = 100 N · μ = 0,15")
    freg("El calaix pesant", "<p>Un calaix de 5 kg ja llisca. Se l’estira amb 30 N i μ_c = 0,2. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 30, 5, 0.2, "Calaix · 5 kg · F = 30 N · μ = 0,2")
    freg("El palet del magatzem", "<p>Un palet de 50 kg llisca pel magatzem. Se l’empeny amb 200 N i μ_c = 0,2. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 200, 50, 0.2, "Palet · 50 kg · F = 200 N · μ = 0,2")
    freg("La maleta al terra de l’aeroport", "<p>Una maleta de 10 kg llisca pel terra de l’aeroport. Se l’estira amb 25 N i μ_c = 0,1. g = 9,8 m/s².</p><p>a) Quant val el fregament?</p><p>b) Quina acceleració té?</p>", 25, 10, 0.1, "Maleta d’aeroport · 10 kg · μ = 0,1")

    def inc0(titol, enun, m, alpha, qui):
        ra = R("a_inclin_0", {"alpha": alpha}, "a", "m/s²")
        rn = R("N_inclin", {"m": m, "alpha": alpha}, "N", "N")
        add(titol, "mitjà", enun, [ra, rn],
            solucio(
                "El pla és llis. Convé un eix al llarg del pla, pendent avall, i un de perpendicular. La component del pes al llarg del pla és m g sin α i és la resultant. La normal equilibra m g cos α.",
                EQ(r"a = g \sin\alpha") + EQ(r"N = m g \cos\alpha"),
                igual("a", ntex(9.8, "m/s", "2") + rf" \cdot \sin {alpha}^\circ", ra["valor"], ra["decimals"], "m/s", "2")
                + igual("N", ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2") + rf" \cdot \cos {alpha}^\circ", rn["valor"], rn["decimals"], "N"),
                f"L’acceleració pendent avall és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la normal és {valor(rn['valor'], rn['decimals'], 'N')}."),
            ("inclinat", {"alpha": alpha, "fregament": False, "massa": f"{fmt_s(m)} kg"},
             f"Baixada per un pla llis de {alpha}°. El pes és vertical i la normal, perpendicular al pla."),
            ("dcl_inclinat", {"alpha": alpha, "fregament": False, "massa": f"{fmt_s(m)} kg"},
             "El pes es descompon en P sin α, al llarg del pla, i P cos α, perpendicular al pla."))

    inc0("El trineu al pla de 30°", "<p>Un trineu de 2 kg baixa per un pla nevat, llis, de 30°. g = 9,8 m/s².</p><p>a) Quina acceleració té?</p><p>b) Quant val la normal?</p>", 2, 30, "Trineu · 2 kg · pla llis 30°")
    inc0("La caixa al pla de 45°", "<p>Una caixa de 5 kg baixa per un pla llis de 45°. g = 9,8 m/s².</p><p>a) Quina acceleració té?</p><p>b) Quant val la normal?</p>", 5, 45, "Caixa · 5 kg · pla llis 45°")
    inc0("El monopatí al pla de 20°", "<p>Un monopatí de 3 kg baixa per una rampa llisa de 20°. g = 9,8 m/s².</p><p>a) Quina acceleració té?</p><p>b) Quant val la normal?</p>", 3, 20, "Monopatí · 3 kg · rampa llisa 20°")
    inc0("El bloc al pla de 60°", "<p>Un bloc de 4 kg baixa per un pla llis de 60°. g = 9,8 m/s².</p><p>a) Quina acceleració té?</p><p>b) Quant val la normal?</p>", 4, 60, "Bloc · 4 kg · pla llis 60°")

    def incf(titol, enun, m, alpha, mu, qui):
        rn = R("N_inclin", {"m": m, "alpha": alpha}, "N", "N")
        rf = R("freg_c", {"mu": mu, "N": rn["valor"]}, "f", "N")
        ra = R("a_inclin_f", {"alpha": alpha, "mu": mu}, "a", "m/s²")
        add(titol, "mitjà", enun, [rn, rf, ra],
            solucio(
                "El bloc baixa, així que el fregament cinètic apunta pendent amunt. La normal és m g cos α i el fregament és μ N. La resultant pendent avall és el pes al llarg del pla menys el fregament.",
                EQ(r"a = g(\sin\alpha - \mu \cos\alpha)"),
                igual("N", ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2") + rf" \cdot \cos {alpha}^\circ", rn["valor"], rn["decimals"], "N")
                + igual("f", ntex(mu, "") + r" \cdot " + ntex(rn["valor"], "N"), rf["valor"], rf["decimals"], "N")
                + igual("a", ntex(9.8, "m/s", "2") + rf" \cdot (\sin {alpha}^\circ - " + ntex(mu, "") + rf" \cdot \cos {alpha}^\circ)", ra["valor"], ra["decimals"], "m/s", "2"),
                f"La normal és {valor(rn['valor'], rn['decimals'], 'N')}, el fregament és {valor(rf['valor'], rf['decimals'], 'N')} i l’acceleració pendent avall és {valor(ra['valor'], ra['decimals'], 'm/s²')}."),
            ("inclinat", {"alpha": alpha, "fregament": True, "massa": f"{fmt_s(m)} kg"},
             f"Baixada per un pla de {alpha}° amb fregament cinètic."),
            ("dcl_inclinat", {"alpha": alpha, "fregament": True, "massa": f"{fmt_s(m)} kg"},
             "El pes es descompon en P sin α i P cos α. El fregament apunta pendent amunt."))

    incf("La caixa que baixa a 30°", "<p>Una caixa de 2 kg baixa lliscant per un pla de 30°. μ_c = 0,2. g = 9,8 m/s².</p><p>a) Quant valen la normal i el fregament?</p><p>b) Quina acceleració té?</p>", 2, 30, 0.2, "Caixa · 2 kg · 30° · μ = 0,2")
    incf("El trineu que baixa a 20°", "<p>Un trineu de 6 kg baixa lliscant per un pla de 20°. μ_c = 0,1. g = 9,8 m/s².</p><p>a) Quant valen la normal i el fregament?</p><p>b) Quina acceleració té?</p>", 6, 20, 0.1, "Trineu · 6 kg · 20° · μ = 0,1")
    incf("El bloc que baixa a 45°", "<p>Un bloc de 3 kg baixa lliscant per un pla de 45°. μ_c = 0,25. g = 9,8 m/s².</p><p>a) Quant valen la normal i el fregament?</p><p>b) Quina acceleració té?</p>", 3, 45, 0.25, "Bloc · 3 kg · 45° · μ = 0,25")
    incf("La maleta a la rampa", "<p>Una maleta de 8 kg baixa lliscant per una rampa de 30°. μ_c = 0,2. g = 9,8 m/s².</p><p>a) Quant valen la normal i el fregament?</p><p>b) Quina acceleració té?</p>", 8, 30, 0.2, "Maleta · 8 kg · rampa 30° · μ = 0,2")

    def at(titol, enun, m1, m2):
        ra = R("atwood_a", {"m1": m1, "m2": m2}, "a", "m/s²")
        rT = R("atwood_T", {"m1": m1, "m2": m2}, "T", "N")
        add(titol, "mitjà", enun, [ra, rT],
            solucio(
                "La politja és ideal: no té massa ni fregament a l’eix, i la tensió és la mateixa als dos costats. La massa grossa baixa. La resultant del sistema és (m₂ − m₁) g i la massa que s’accelera és la suma.",
                EQ(r"a = (m_2 - m_1) g / (m_1 + m_2)"),
                igual("a", "(" + ntex(m2, "kg") + " - " + ntex(m1, "kg") + r") \cdot " + ntex(9.8, "m/s", "2") + " / (" + ntex(m1, "kg") + " + " + ntex(m2, "kg") + ")", ra["valor"], ra["decimals"], "m/s", "2")
                + igual("T", "2 \cdot " + ntex(m1, "kg") + r" \cdot " + ntex(m2, "kg") + r" \cdot " + ntex(9.8, "m/s", "2") + " / (" + ntex(m1, "kg") + " + " + ntex(m2, "kg") + ")", rT["valor"], rT["decimals"], "N"),
                f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la tensió és {valor(rT['valor'], rT['decimals'], 'N')}."),
            ("atwood", {"m1": f"{fmt_s(m1)} kg", "m2": f"{fmt_s(m2)} kg", "qui": f"Politja · {fmt_s(m1)} kg i {fmt_s(m2)} kg"},
             "La massa més gran baixa."))

    at("La politja del laboratori", "<p>Al laboratori, dues masses de 2 kg i 3 kg pengen d’una corda que passa per una politja ideal. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió?</p>", 2, 3)
    at("La politja de la grua de maqueta", "<p>En una maqueta, pengen 1 kg i 3 kg d’una politja ideal. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió?</p>", 1, 3)
    at("Dos cubells al pou", "<p>Dos cubells de 4 kg i 6 kg pengen d’una politja ideal al pou del pati. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió de la corda?</p>", 4, 6)
    at("Les masses de 2 kg i 4 kg", "<p>Dues masses de 2 kg i 4 kg pengen d’una politja ideal. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió?</p>", 2, 4)

    def pen(titol, enun, M, m, mu, qui):
        ra = R("penjant_a", {"M": M, "m": m, "mu": mu}, "a", "m/s²")
        rT = R("penjant_T", {"M": M, "m": m, "mu": mu}, "T", "N")
        add(titol, "mitjà", enun, [ra, rT],
            solucio(
                "El pes que accelera el sistema és el del bloc que penja. Si la taula és llisa, no es resta fregament. La tensió s’obté del bloc que penja: el seu pes menys T val m a.",
                EQ(r"a = (m g - \mu M g)/(M + m)"),
                igual("a", "(" + ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2") + " - " + ntex(mu, "") + r" \cdot " + ntex(M, "kg") + r" \cdot " + ntex(9.8, "m/s", "2") + ") / (" + ntex(M, "kg") + " + " + ntex(m, "kg") + ")", ra["valor"], ra["decimals"], "m/s", "2")
                + igual("T", ntex(m, "kg") + r" \cdot (" + ntex(9.8, "m/s", "2") + " - " + ntex(ra["valor"], "m/s", "2") + ")", rT["valor"], rT["decimals"], "N"),
                f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la tensió és {valor(rT['valor'], rT['decimals'], 'N')}."),
            ("taula", {"M": f"{fmt_s(M)} kg", "m": f"{fmt_s(m)} kg", "qui": qui}, "Bloc damunt la taula i bloc que penja."))

    pen("El bloc i el peset a la taula llisa", "<p>Un bloc de 4 kg és damunt una taula llisa i va lligat, amb una politja a la vora, a un peset d’1 kg que penja. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió?</p>", 4, 1, 0, "Taula llisa · 4 kg i 1 kg")
    pen("La caixa i la massa que penja", "<p>Una caixa de 6 kg és damunt una taula llisa i va lligada a una massa de 2 kg que penja. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió?</p>", 6, 2, 0, "Taula llisa · 6 kg i 2 kg")
    pen("La taula amb fregament", "<p>Un bloc de 4 kg és damunt una taula amb μ_c = 0,2 i va lligat a un bloc de 2 kg que penja. El de la taula ja llisca. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió?</p>", 4, 2, 0.2, "Taula · μ = 0,2 · 4 kg i 2 kg")
    pen("El calaix i el pes penjat", "<p>Un calaix de 5 kg llisca per una taula amb μ_c = 0,1, estirat per una massa de 2 kg que penja. g = 9,8 m/s².</p><p>a) Quina acceleració té el sistema?</p><p>b) Quant val la tensió?</p>", 5, 2, 0.1, "Calaix · μ = 0,1 · 5 kg i 2 kg")

    for titol, enun, k, x, qui in [
        ("La molla del laboratori", "<p>Una molla de laboratori, de constant 200 N/m, s’allarga 0,05 m.</p><p>Quina força fa?</p>", 200, 0.05, "Molla de laboratori · k = 200 N/m · x = 0,05 m"),
        ("La molla de la porta", "<p>La molla d’una porta, de constant 80 N/m, s’allarga 0,12 m en obrir-la.</p><p>Quina força fa la molla?</p>", 80, 0.12, "Molla de la porta · k = 80 N/m · x = 0,12 m"),
    ]:
        r = R("molla_F", {"k": k, "x": x}, "F", "N")
        add(titol, "senzill", enun, [r],
            solucio(
                "La força elàstica és proporcional a la deformació respecte de la longitud natural, i s’oposa a l’allargament.",
                EQ(r"F = k x"),
                igual("F", ntex(k, "N/m") + r" \cdot " + ntex(x, "m"), r["valor"], r["decimals"], "N"),
                f"La molla fa {valor(r['valor'], r['decimals'], 'N')}."),
            ("molla", {"x": f"{fmt_s(x)} m"}, "La cota és la deformació, no la longitud total de la molla."))

    rf = R("ac_necessaria", {"m": 0.4, "v": 3, "r": 0.8}, "T", "N")
    add("La corda que fa girar la pilota", "mitjà",
        "<p>Una pilota de 0,4 kg gira, lligada a una corda de 0,8 m, a 3 m/s en un pla horitzontal llis.</p><p>Quant val la tensió de la corda?</p>",
        [rf],
        solucio(
            "En el pla horitzontal l’única força cap al centre és la tensió. Aquesta força és la resultant centrípeta, m v²/r. No s’hi afegeix una «força centrípeta» de més.",
            EQ(r"T = m v^2 / r"),
            igual("T", ntex(0.4, "kg") + r" \cdot " + nsq(3) + " / " + ntex(0.8, "m"), rf["valor"], rf["decimals"], "N"),
            f"La tensió és {valor(rf['valor'], rf['decimals'], 'N')}."),
        ("corda", {"r": "0,8 m", "qui": "Pilota · 0,4 kg · 3 m/s · r = 0,8 m"}, "La tensió apunta al centre."))

    rv = R("vmax_revolt", {"mu": 0.4, "r": 40}, "v", "m/s")
    add("El cotxe al revolt pla", "mitjà",
        "<p>Un cotxe pren un revolt pla de 40 m de radi. El coeficient de fregament estàtic entre les rodes i l’asfalt és 0,4. g = 9,8 m/s².</p><p>Quina és la velocitat màxima per no derrapar?</p>",
        [rv],
        solucio(
            "En un revolt pla, el fregament de les rodes apunta cap al centre i fa de força centrípeta. Al límit, μ N = μ m g = m v²/r. La massa es cancel·la.",
            EQ(r"v = \sqrt{\mu r g}"),
            igual("v", r"\sqrt{" + ntex(0.4, "") + r" \cdot " + ntex(40, "m") + r" \cdot " + ntex(9.8, "m/s", "2") + "}", rv["valor"], rv["decimals"], "m/s"),
            f"La velocitat màxima és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
        ("revolt", {"qui": "Cotxe · revolt pla r = 40 m · μ = 0,4"}, "Vist des de dalt: el fregament apunta al centre."))

    rp = R("v_peralt", {"r": 20, "theta": 45}, "v", "m/s")
    add("El revolt peraltat", "mitjà",
        "<p>Un revolt de 20 m de radi està peraltat 45° i s’hi vol passar sense fer servir el fregament. g = 9,8 m/s² i tan 45° = 1.</p><p>Quina velocitat hi correspon?</p>",
        [rp],
        solucio(
            "Sense fregament, la component horitzontal de la normal és la força centrípeta i la vertical equilibra el pes. Dividint les dues equacions queda tan θ = v²/(r g). A 45° la tangent val 1, així que v² = r g.",
            EQ(r"v = \sqrt{r g \tan\theta}"),
            igual("v", r"\sqrt{" + ntex(20, "m") + r" \cdot " + ntex(9.8, "m/s", "2") + r" \cdot 1}", rp["valor"], rp["decimals"], "m/s"),
            f"La velocitat és {valor(rp['valor'], rp['decimals'], 'm/s')}."),
        ("peralt", {"theta": 45, "qui": "Peralt · r = 20 m · 45°"}, "La normal és perpendicular a la calçada."))

    rn = R("N_loop_dalt", {"m": 500, "v": 10, "r": 8}, "N", "N")
    add("El cotxe dalt del lòpping", "mitjà",
        "<p>Un cotxe de 500 kg passa pel capdamunt d’un lòpping de 8 m de radi a 10 m/s. g = 9,8 m/s².</p><p>Quant val la normal en aquest punt?</p>",
        [rn],
        solucio(
            "Al capdamunt, el pes i la normal apunten tots dos cap al centre. La seva suma és la força centrípeta: N + m g = m v²/r.",
            EQ(r"N = m v^2 / r - m g"),
            igual("N", ntex(500, "kg") + r" \cdot " + nsq(10) + " / " + ntex(8, "m") + " - " + ntex(500, "kg") + r" \cdot " + ntex(9.8, "m/s", "2"), rn["valor"], rn["decimals"], "N"),
            f"La normal al capdamunt és {valor(rn['valor'], rn['decimals'], 'N')}."),
        ("loop", {"qui": "Cotxe · 500 kg · dalt del lòpping · r = 8 m · 10 m/s"}, "Al capdamunt el pes i la normal apunten al centre."))
    return out


def energia():
    out, add = _cap("energia", "6")

    def cau(titol, enun, m, h, qui):
        rv = R("v_caiguda_e", {"h": h}, "v", "m/s")
        re = R("ep", {"m": m, "h": h}, "E", "J")
        add(titol, "senzill", enun, [re, rv],
            solucio(
                "Només treballa el pes, així que l’energia mecànica es conserva. Amb el zero d’altura a baix, a dalt tot és potencial i a baix tot és cinètic. La massa es cancel·la en la velocitat, però no en l’energia.",
                EQ(r"m g h = \frac{1}{2} m v^2"),
                igual("E_p", ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(h, "m"), re["valor"], re["decimals"], "J")
                + igual("v", r"\sqrt{2 \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(h, "m") + "}", rv["valor"], rv["decimals"], "m/s"),
                f"L’energia potencial inicial és {valor(re['valor'], re['decimals'], 'J')} i la velocitat en arribar a baix és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("barres", {"etapes": [("dalt", 0, 100), ("baix", 100, 0)], "qui": qui}, "L’energia potencial es converteix en cinètica."))

    cau("La pedra que cau al pou", "<p>Una pedra de 0,2 kg cau des del repòs un desnivell de 19,6 m fins a l’aigua del pou. Només actua el pes. g = 9,8 m/s². Pren l’energia potencial zero a baix.</p><p>a) Quina energia potencial té a dalt?</p><p>b) A quina velocitat arriba a l’aigua?</p>", 0.2, 19.6, "Pedra · pou · 19,6 m")
    cau("El llibre que rellisca del prestatge", "<p>Un llibre d’1 kg rellisca del prestatge i cau 1,25 m fins a terra, des del repòs. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia potencial perd?</p><p>b) A quina velocitat arriba a terra?</p>", 1, 1.25, "Llibre · prestatge · 1,25 m")
    cau("El salt a la piscina", "<p>Una persona de 60 kg es deixa caure des del trampolí de la piscina, a 2 m de l’aigua, des del repòs. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia potencial té respecte de l’aigua?</p><p>b) A quina velocitat arriba a l’aigua?</p>", 60, 2, "Piscina · trampolí a 2 m · 60 kg")
    cau("La poma de l’arbre", "<p>Una poma de 0,15 kg cau 4,9 m des de la branca, des del repòs. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia potencial perd?</p><p>b) A quina velocitat arriba a terra?</p>", 0.15, 4.9, "Poma · 4,9 m")
    cau("El paquet de la bastida", "<p>Un paquet de 3 kg cau 10 m des d’una bastida, des del repòs. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia potencial inicial té, amb el zero a terra?</p><p>b) A quina velocitat arriba?</p>", 3, 10, "Paquet · bastida · 10 m")
    cau("La clau que cau de la butxaca", "<p>Una clau de 0,05 kg cau 5 m des de la butxaca, des del repòs. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia potencial perd?</p><p>b) A quina velocitat arriba a terra?</p>", 0.05, 5, "Clau · 5 m")

    def amunt(titol, enun, m, v, qui):
        rh = R("h_llanc_e", {"v": v}, "h", "m")
        re = R("ec", {"m": m, "v": v}, "E", "J")
        add(titol, "senzill", enun, [re, rh],
            solucio(
                "A dalt la velocitat és zero. L’energia cinètica inicial es converteix tota en potencial. El nivell zero és el punt de llançament, i només actua el pes.",
                EQ(r"\frac{1}{2} m v^2 = m g h"),
                igual("E_c", r"\frac{1}{2} \cdot " + ntex(m, "kg") + r" \cdot " + nsq(v), re["valor"], re["decimals"], "J")
                + igual("h", nsq(v) + " / (2 \cdot " + ntex(9.8, "m/s", "2") + ")", rh["valor"], rh["decimals"], "m"),
                f"L’energia cinètica inicial és {valor(re['valor'], re['decimals'], 'J')} i l’alçada màxima és {valor(rh['valor'], rh['decimals'], 'm')}."),
            ("llancament", {"qui": qui}, "Al punt més alt la velocitat és zero."))

    amunt("La pilota de bàsquet cap amunt", "<p>Es llança una pilota de bàsquet de 0,6 kg verticalment cap amunt a 8 m/s. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia cinètica té en sortir?</p><p>b) Quina alçada màxima assoleix?</p>", 0.6, 8, "Bàsquet · 0,6 kg · 8 m/s")
    amunt("El coet petit", "<p>Un coet petit de 0,2 kg puja a 14 m/s en el moment en què s’apaga el motor. A partir d’aquí només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia cinètica té en apagar-se?</p><p>b) Quina alçada puja encara?</p>", 0.2, 14, "Coet petit · 14 m/s")
    amunt("La fletxa cap amunt", "<p>Una fletxa de 0,05 kg surt verticalment a 20 m/s. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia cinètica té en sortir?</p><p>b) Quina alçada màxima assoleix?</p>", 0.05, 20, "Fletxa · 20 m/s")
    amunt("La pedra llançada al camp", "<p>Es llança una pedra de 0,3 kg verticalment cap amunt a 9,8 m/s. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia cinètica té?</p><p>b) Quina alçada màxima assoleix?</p>", 0.3, 9.8, "Pedra · 9,8 m/s")
    amunt("El paquet llançat a dalt", "<p>Es llança un paquet de 2 kg verticalment cap amunt a 6 m/s. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia cinètica té?</p><p>b) Quina alçada màxima assoleix?</p>", 2, 6, "Paquet · 6 m/s")
    amunt("La bola de la classe", "<p>Es llança una bola d’1 kg verticalment cap amunt a 4 m/s. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina energia cinètica té?</p><p>b) Quina alçada màxima assoleix?</p>", 1, 4, "Bola · 4 m/s")

    def entre(titol, enun, m, h1, v1, h2, qui):
        rv = R("v_entre_altures", {"h1": h1, "v1": v1, "h2": h2}, "v", "m/s")
        add(titol, "mitjà", enun, [rv],
            solucio(
                "La pista és llisa i només actua el pes, així que l’energia mecànica es conserva. La massa es cancel·la: només importen les altures i la velocitat al punt de partida.",
                EQ(r"\frac{1}{2} v_1^2 + g h_1 = \frac{1}{2} v_2^2 + g h_2"),
                igual("v_2", r"\sqrt{" + nsq(v1) + " + 2 \cdot " + ntex(9.8, "m/s", "2") + r" \cdot (" + ntex(h1, "m") + " - " + ntex(h2, "m") + ")}", rv["valor"], rv["decimals"], "m/s"),
                f"Al segon punt porta {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("muntanya", {"hA": f"{fmt_s(h1)} m", "hB": f"{fmt_s(h1)} m", "hC": f"{fmt_s(h2)} m", "qui": qui},
             "Les altures dels punts són les de l’enunciat."))

    entre("La muntanya russa", "<p>Un vagó de 400 kg de la muntanya russa passa pel punt A, a 12 m, pràcticament parat, i després pel punt B, a 3 m. La via és llisa i només actua el pes. g = 9,8 m/s².</p><p>Quina velocitat porta a B?</p>", 400, 12, 0, 3, "Muntanya russa · A a 12 m · B a 3 m")
    entre("L’esquiador a la pista llisa", "<p>Un esquiador de 70 kg passa per un punt a 8 m d’altura a 2 m/s i després per un punt a 2 m. La pista és llisa i només actua el pes. g = 9,8 m/s².</p><p>Quina velocitat porta al segon punt?</p>", 70, 8, 2, 2, "Esquiador · 8 m i després 2 m")
    entre("El carretó de la rampa", "<p>Un carretó de 20 kg passa per dalt d’una rampa llisa, a 5 m, a 3 m/s, i baixa fins a 1 m d’altura. Només actua el pes. g = 9,8 m/s².</p><p>Quina velocitat hi porta?</p>", 20, 5, 3, 1, "Carretó · de 5 m a 1 m")
    entre("La boleta al tub", "<p>Una boleta de 0,1 kg entra en un tub llis a 1,5 m d’altura, parada, i surt a 0,4 m. Només actua el pes. g = 9,8 m/s².</p><p>Quina velocitat porta a la sortida?</p>", 0.1, 1.5, 0, 0.4, "Boleta · de 1,5 m a 0,4 m")
    entre("El vagó de la mina", "<p>Un vagó de 1200 kg passa per un punt a 15 m a 4 m/s i després per un punt a 6 m, per una via llisa. Només actua el pes. g = 9,8 m/s².</p><p>Quina velocitat porta al segon punt?</p>", 1200, 15, 4, 6, "Vagó de la mina · 15 m i 6 m")
    entre("El trineu a la baixada llisa", "<p>Un trineu de 50 kg passa per un punt a 6 m d’altura a 1 m/s i després per un punt a 1,5 m, per una baixada llisa. Només actua el pes. g = 9,8 m/s².</p><p>Quina velocitat porta al punt més baix?</p>", 50, 6, 1, 1.5, "Trineu · de 6 m a 1,5 m")

    # The last one is a bad enunciat if h1=h2. I'll replace it after by not using that call... I already added it. Let me fix by not calling with equal heights. I'll overwrite by changing the call - I already wrote h2=6. Let me fix the function call - I'll edit after if needed. Let me change it now... the write is done as I'm composing. I'll fix the last entre to have different heights. I'll do a search replace after the file is written if I leave it. Let me change the line before finishing the function... I'm still in the write contents. I'll set h2 to 1.5 and rewrite the sentence properly. I already have the bad sentence in the string. I'll fix with StrReplace after.

    def pend(titol, enun, m, L, th, qui):
        rh = R("h_pendol", {"L": L, "theta": th}, "h", "m")
        rv = R("v_pendol", {"L": L, "theta": th}, "v", "m/s")
        add(titol, "mitjà", enun, [rh, rv],
            solucio(
                "L’altura respecte del punt més baix és L(1 − cos θ). Es conserva l’energia: a dalt la velocitat és zero i a baix l’altura és zero. La massa es cancel·la.",
                EQ(r"h = L(1 - \cos\theta)") + EQ(r"v = \sqrt{2 g h}"),
                igual("h", ntex(L, "m") + rf" \cdot (1 - \cos {th}^\circ)", rh["valor"], rh["decimals"], "m")
                + igual("v", r"\sqrt{2 \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(rh["valor"], "m") + "}", rv["valor"], rv["decimals"], "m/s"),
                f"L’altura inicial és {valor(rh['valor'], rh['decimals'], 'm')} i la velocitat al punt baix és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("pendol", {"theta": th, "qui": qui}, f"Es deixa anar des de {th}°."))

    pend("El pèndol del laboratori", "<p>Un pèndol de laboratori, de 0,5 kg i 2 m, es deixa anar des de 60° respecte de la vertical. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina altura té respecte del punt baix?</p><p>b) Quina velocitat hi porta en passar per baix?</p>", 0.5, 2, 60, "Pèndol de laboratori · L = 2 m · 60°")
    pend("El pèndol curt", "<p>Un pèndol de 0,2 kg i 0,8 m es deixa anar des de 30°. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina altura cau fins al punt baix?</p><p>b) Quina velocitat hi porta?</p>", 0.2, 0.8, 30, "Pèndol curt · L = 0,8 m · 30°")
    pend("El gronxador", "<p>Un gronxador de 3 m, amb una criatura de 30 kg, es deixa anar des de 20° respecte de la vertical. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina altura baixa fins al punt més baix?</p><p>b) Quina velocitat hi porta?</p>", 30, 3, 20, "Gronxador · L = 3 m · 20°")
    pend("El pèndol deixat anar en horitzontal", "<p>Un pèndol d’1 m i 0,4 kg es deixa anar des de l’horitzontal, és a dir, des de 90°. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina altura cau?</p><p>b) Quina velocitat porta al punt baix?</p>", 0.4, 1, 90, "Pèndol · 90° · L = 1 m")
    pend("El pèndol de la porta", "<p>Una bola de 0,1 kg lligada a un fil de 0,5 m es deixa anar des de 40°. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina altura té respecte del punt baix?</p><p>b) Quina velocitat hi porta?</p>", 0.1, 0.5, 40, "Fil de 0,5 m · 40°")
    pend("El pèndol de 1,5 m", "<p>Un pèndol d’1 kg i 1,5 m es deixa anar des de 45°. Només actua el pes. g = 9,8 m/s².</p><p>a) Quina altura cau?</p><p>b) Quina velocitat porta al punt baix?</p>", 1, 1.5, 45, "Pèndol · L = 1,5 m · 45°")

    def moll(titol, enun, m, k, A, qui):
        rv = R("v_molla", {"k": k, "m": m, "A": A}, "v", "m/s")
        re = R("epe", {"k": k, "x": A}, "E", "J")
        add(titol, "mitjà", enun, [re, rv],
            solucio(
                "El pla és horitzontal i llis: el pes i la normal no treballen. L’energia de la molla a la compressió inicial es converteix en cinètica quan la deformació és zero.",
                EQ(r"\frac{1}{2} k A^2 = \frac{1}{2} m v^2"),
                igual("E", r"\frac{1}{2} \cdot " + ntex(k, "N/m") + r" \cdot " + ntex(A, "m") + "^2", re["valor"], re["decimals"], "J")
                + igual("v", ntex(A, "m") + r" \cdot \sqrt{" + ntex(k, "N/m") + " / " + ntex(m, "kg") + "}", rv["valor"], rv["decimals"], "m/s"),
                f"L’energia inicial de la molla és {valor(re['valor'], re['decimals'], 'J')} i la velocitat a l’equilibri és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("molla", {"comprimida": True, "x": f"{fmt_s(A)} m"}, "La cota és la compressió inicial de la molla."))

    moll("La molla de 200 N/m", "<p>Una molla de 200 N/m està comprimida 0,1 m i es deixa anar, unida a un bloc de 0,5 kg, damunt una taula llisa.</p><p>a) Quina energia té la molla al principi?</p><p>b) Quina velocitat porta el bloc en passar per l’equilibri?</p>", 0.5, 200, 0.1, "Bloc 0,5 kg · k = 200 N/m · 0,1 m")
    moll("La molla tova", "<p>Una molla de 50 N/m, comprimida 0,08 m, llança un bloc de 0,2 kg per una taula llisa.</p><p>a) Quina energia té al principi?</p><p>b) Quina velocitat porta a l’equilibri?</p>", 0.2, 50, 0.08, "Bloc 0,2 kg · k = 50 N/m")
    moll("El bloc i la molla de 98 N/m", "<p>Una molla de 98 N/m, comprimida 0,2 m, impulsa un bloc d’1 kg per un pla horitzontal llis.</p><p>a) Quina energia emmagatzema?</p><p>b) Quina velocitat dona al bloc a l’equilibri?</p>", 1, 98, 0.2, "Bloc 1 kg · k = 98 N/m · 0,2 m")
    moll("L’oscil·lador de la pràctica", "<p>A la pràctica, una molla de 160 N/m comprimida 0,05 m va unida a una massa de 0,4 kg sobre un carril llis.</p><p>a) Quina energia té la molla?</p><p>b) Quina velocitat màxima assoleix la massa?</p>", 0.4, 160, 0.05, "Pràctica · 0,4 kg · k = 160 N/m")
    moll("La compressió del carro", "<p>Un carro de 2 kg és empès per una molla de 800 N/m comprimida 0,1 m, en un carril llis.</p><p>a) Quina energia té la molla?</p><p>b) Quina velocitat porta el carro a l’equilibri?</p>", 2, 800, 0.1, "Carro · 2 kg · k = 800 N/m")
    moll("La molla del calaix", "<p>La molla d’un calaix, de 120 N/m, es comprimeix 0,04 m i es deixa anar amb una massa de 0,3 kg que llisca lliurement sobre la guia.</p><p>a) Quina energia té?</p><p>b) Quina velocitat porta la massa a l’equilibri?</p>", 0.3, 120, 0.04, "Calaix · 0,3 kg · k = 120 N/m")
    moll("El llançament des de 15 cm", "<p>Es fa un llançament comprimint 0,15 m (15 cm) una molla de 100 N/m, i es deixa anar un bloc de 0,25 kg per un pla llis.</p><p>a) Quina energia té la molla?</p><p>b) Quina velocitat porta el bloc a l’equilibri?</p>", 0.25, 100, 0.15, "Llançament · compressió 15 cm · 0,25 kg")
    moll("El carro gran", "<p>Un carro de 4 kg és impulsat per una molla de 400 N/m comprimida 0,2 m, en un carril llis.</p><p>a) Quina energia té la molla?</p><p>b) Quina velocitat porta el carro a l’equilibri?</p>", 4, 400, 0.2, "Carro 4 kg · k = 400 N/m · 0,2 m")
    return out


def mixtos():
    out, add = _cap("mixtos", "7")

    def rampa(titol, enun, m, d, alpha, qui):
        ra = R("a_inclin_0", {"alpha": alpha}, "a", "m/s²")
        rv = R("v_inclin_e", {"d": d, "alpha": alpha}, "v", "m/s")
        add(titol, "mitjà", enun, [ra, rv],
            solucio(
                "El pla és llis. Amb Newton, la resultant al llarg del pla és m g sin α i l’acceleració és g sin α. Amb l’energia, només importa el desnivell d sin α, i la velocitat al final, partint del repòs, és l’arrel de 2 g h. Els dos camins han de coincidir.",
                EQ(r"a = g \sin\alpha") + EQ(r"v = \sqrt{2 g d \sin\alpha}"),
                igual("a", ntex(9.8, "m/s", "2") + rf" \cdot \sin {alpha}^\circ", ra["valor"], ra["decimals"], "m/s", "2")
                + igual("v", r"\sqrt{2 \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(d, "m") + rf" \cdot \sin {alpha}^\circ" + "}", rv["valor"], rv["decimals"], "m/s"),
                f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i la velocitat al final del tram és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("inclinat", {"alpha": alpha, "fregament": False, "massa": f"{fmt_s(m)} kg", "longitud": f"{fmt_s(d)} m"},
             f"Recorregut de {fmt_s(d)} m per un pla llis de {alpha}°."),
            ("dcl_inclinat", {"alpha": alpha, "fregament": False, "massa": f"{fmt_s(m)} kg"},
             "El pes es descompon en P sin α, al llarg del pla, i P cos α, perpendicular al pla."))

    rampa("El trineu als dos mètodes", "<p>Un trineu de 3 kg parteix del repòs i recorre 4 m per un pla nevat llis de 30°. g = 9,8 m/s².</p><p>a) Quina acceleració té, amb Newton?</p><p>b) Quina velocitat porta al final, amb l’energia?</p>", 3, 4, 30, "Trineu · 4 m · pla llis 30°")
    rampa("El monopatí a la rampa", "<p>Un monopatí de 5 kg parteix del repòs i recorre 6 m per una rampa llisa de 20°. g = 9,8 m/s².</p><p>a) Quina acceleració té?</p><p>b) Quina velocitat porta al final?</p>", 5, 6, 20, "Monopatí · 6 m · rampa llisa 20°")
    rampa("La caixa a la rampa de 45°", "<p>Una caixa de 2 kg parteix del repòs i recorre 2 m per una rampa llisa de 45°. g = 9,8 m/s².</p><p>a) Quina acceleració té?</p><p>b) Quina velocitat porta al final?</p>", 2, 2, 45, "Caixa · 2 m · rampa llisa 45°")
    rampa("El carretó a la baixada", "<p>Un carretó de 4 kg parteix del repòs i recorre 5 m per un pla llis de 30°. g = 9,8 m/s².</p><p>a) Quina acceleració té?</p><p>b) Quina velocitat porta al final?</p>", 4, 5, 30, "Carretó · 5 m · pla llis 30°")

    def velh(titol, enun, v0, th, h, qui):
        rv = R("v_entre_altures", {"h1": 0, "v1": v0, "h2": h}, "v", "m/s")
        add(titol, "mitjà", enun, [rv],
            solucio(
                "Sense resistència de l’aire l’energia mecànica es conserva. A una altura h la cinètica ha disminuït en el que ha guanyat la potencial. El mòdul no depèn de l’angle.",
                EQ(r"\frac{1}{2} v_0^2 = \frac{1}{2} v^2 + g h"),
                igual("v", r"\sqrt{" + nsq(v0) + " - 2 \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(h, "m") + "}", rv["valor"], rv["decimals"], "m/s"),
                f"A aquesta altura el mòdul de la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("tir_p", {"theta": th, "h": f"{fmt_s(h)} m", "r": "x", "qui": qui}, "Es demana el mòdul a una altura concreta."))

    velh("La pilota a 2 m d’altura", "<p>Una pilota surt del terra a 20 m/s. Quan és a 2 m d’altura, quin mòdul de velocitat porta? No facis servir el temps. Es negligeix l’aire. g = 9,8 m/s².</p>", 20, 50, 2, "Pilota · v₀ = 20 m/s · altura 2 m")
    velh("La pedra a 1 m", "<p>Una pedra surt del terra a 15 m/s. A 1 m d’altura, quin mòdul de velocitat porta? Conserva l’energia. g = 9,8 m/s².</p>", 15, 60, 1, "Pedra · 15 m/s · altura 1 m")
    velh("El globus a 0,5 m", "<p>Un globus surt del terra a 12 m/s. A 0,5 m d’altura, quin mòdul de velocitat porta? g = 9,8 m/s².</p>", 12, 45, 0.5, "Globus · 12 m/s · altura 0,5 m")

    def ten(titol, enun, m, L, th, qui):
        rv = R("v_pendol", {"L": L, "theta": th}, "v", "m/s")
        rT = R("T_cord_baix", {"m": m, "v": rv["valor"], "r": L}, "T", "N")
        add(titol, "mitjà", enun, [rv, rT],
            solucio(
                "Primer es troba la velocitat al punt baix conservant l’energia. Al punt baix la tensió és cap amunt i el pes cap avall, i el centre de la circumferència és a dalt: la resultant cap al centre és T − m g.",
                EQ(r"v = \sqrt{2 g L (1-\cos\theta)}") + EQ(r"T - m g = m v^2 / L"),
                igual("v", r"\sqrt{2 \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(L, "m") + rf" \cdot (1-\cos {th}^\circ)" + "}", rv["valor"], rv["decimals"], "m/s")
                + igual("T", ntex(m, "kg") + r" \cdot " + nsq(rv["valor"]) + " / " + ntex(L, "m") + " + " + ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2"), rT["valor"], rT["decimals"], "N"),
                f"Al punt baix la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')} i la tensió és {valor(rT['valor'], rT['decimals'], 'N')}."),
            ("pendol", {"theta": th, "qui": qui}, "Es demana la corda al punt més baix."))

    ten("La tensió del pèndol de laboratori", "<p>Un pèndol de 0,5 kg i 2 m es deixa anar des de 60°. g = 9,8 m/s².</p><p>Quina tensió fa el fil en passar pel punt més baix?</p>", 0.5, 2, 60, "Pèndol · 0,5 kg · L = 2 m · 60°")
    ten("La tensió del gronxador", "<p>Un gronxador de 2,5 m amb una criatura de 40 kg es deixa anar des de 30°. g = 9,8 m/s².</p><p>Quina tensió fan les cordes, en conjunt, al punt més baix?</p>", 40, 2.5, 30, "Gronxador · 40 kg · L = 2,5 m · 30°")
    ten("La tensió del pèndol curt", "<p>Un pèndol de 0,3 kg i 1 m es deixa anar des de 45°. g = 9,8 m/s².</p><p>Quina tensió fa el fil al punt baix?</p>", 0.3, 1, 45, "Pèndol curt · 0,3 kg · 45°")

    def loopmin(titol, enun, r, qui):
        rH = R("H_loop", {"r": r}, "H", "m")
        rv = R("vmin_loop", {"r": r}, "v", "m/s")
        add(titol, "mitjà", enun, [rH, rv],
            solucio(
                "Al capdamunt, la velocitat mínima és la que fa nul·la la normal: el pes sol fa de força centrípeta, v² = g r. L’altura del capdamunt respecte del terra és 2r. Conservant l’energia des del repòs, m g H = ½ m v² + m g (2r), i en surt H = 2,5 r.",
                EQ(r"v = \sqrt{g r}") + EQ(r"H = 2{,}5\, r"),
                igual("v", r"\sqrt{" + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(r, "m") + "}", rv["valor"], rv["decimals"], "m/s")
                + igual("H", "2,5 \cdot " + ntex(r, "m"), rH["valor"], rH["decimals"], "m"),
                f"Al capdamunt porta {valor(rv['valor'], rv['decimals'], 'm/s')} i cal deixar-lo anar des de {valor(rH['valor'], rH['decimals'], 'm')}."),
            ("loop", {"qui": qui}, "Per passar pel capdamunt cal prou altura."))

    loopmin("El lòpping de la pista", "<p>Un carretó entra en un lòpping de 4 m de radi per una pista llisa. Es deixa caure des del repòs. g = 9,8 m/s².</p><p>a) Quina velocitat mínima ha de portar al capdamunt?</p><p>b) Des de quina altura, mesurada des del terra, s’ha de deixar anar?</p>", 4, "Carretó · lòpping r = 4 m")
    loopmin("El loop de la maqueta", "<p>Una boleta fa un loop de 2 m de radi en una pista llisa. g = 9,8 m/s².</p><p>a) Quina velocitat mínima cal al capdamunt?</p><p>b) Des de quina altura s’ha de deixar anar, des del repòs?</p>", 2, "Boleta · loop r = 2 m")

    def molla_rampa(titol, enun, m, k, A, qui):
        rv = R("v_molla", {"k": k, "m": m, "A": A}, "v", "m/s")
        rh = R("h_llanc_e", {"v": rv["valor"]}, "h", "m")
        add(titol, "mitjà", enun, [rv, rh],
            solucio(
                "La molla, al pla llis, converteix l’energia elàstica en cinètica. Aquesta cinètica, a la rampa llisa, es converteix en potencial fins que el bloc s’atura. És el mateix que igualar l’energia de la molla amb m g h.",
                EQ(r"\frac{1}{2} k A^2 = m g h"),
                igual("v", ntex(A, "m") + r" \cdot \sqrt{" + ntex(k, "N/m") + " / " + ntex(m, "kg") + "}", rv["valor"], rv["decimals"], "m/s")
                + igual("h", r"\frac{1}{2} \cdot " + ntex(k, "N/m") + r" \cdot " + ntex(A, "m") + "^2 / (" + ntex(m, "kg") + r" \cdot " + ntex(9.8, "m/s", "2") + ")", rh["valor"], rh["decimals"], "m"),
                f"En sortir de la molla porta {valor(rv['valor'], rv['decimals'], 'm/s')} i puja {valor(rh['valor'], rh['decimals'], 'm')}."),
            ("molla", {"comprimida": True, "x": f"{fmt_s(A)} m"}, "La compressió inicial fixa l’energia de la molla."))

    molla_rampa("La molla que llança el bloc rampa amunt", "<p>Una molla de 200 N/m, comprimida 0,2 m, llança un bloc de 0,5 kg per un pla horitzontal llis. Després el bloc entra en una rampa llisa. g = 9,8 m/s².</p><p>a) Quina velocitat porta en deixar la molla, a l’equilibri?</p><p>b) Quina altura màxima puja, des del pla?</p>", 0.5, 200, 0.2, "Bloc 0,5 kg · k = 200 N/m · 0,2 m")
    molla_rampa("El carro impulsat cap a la rampa", "<p>Una molla de 100 N/m, comprimida 0,3 m, impulsa un carro d’1 kg per un carril llis que després puja. g = 9,8 m/s².</p><p>a) Quina velocitat porta a l’equilibri de la molla?</p><p>b) Quina altura màxima assoleix?</p>", 1, 100, 0.3, "Carro 1 kg · k = 100 N/m · 0,3 m")

    def atwood_e(titol, enun, m1, m2, h):
        ra = R("atwood_a", {"m1": m1, "m2": m2}, "a", "m/s²")
        rv = R("atwood_v", {"m1": m1, "m2": m2, "h": h}, "v", "m/s")
        add(titol, "mitjà", enun, [ra, rv],
            solucio(
                "Newton dona l’acceleració: la resultant és (m₂ − m₁) g. L’energia també es conserva, perquè la politja és ideal: la pèrdua d’energia potencial (m₂ − m₁) g h es converteix en cinètica de les dues masses, que porten la mateixa rapidesa.",
                EQ(r"a = (m_2-m_1)g/(m_1+m_2)") + EQ(r"v = \sqrt{2(m_2-m_1) g h / (m_1+m_2)}"),
                igual("a", "(" + ntex(m2, "kg") + " - " + ntex(m1, "kg") + r") \cdot " + ntex(9.8, "m/s", "2") + " / (" + ntex(m1, "kg") + " + " + ntex(m2, "kg") + ")", ra["valor"], ra["decimals"], "m/s", "2")
                + igual("v", r"\sqrt{2 \cdot (" + ntex(m2, "kg") + " - " + ntex(m1, "kg") + r") \cdot " + ntex(9.8, "m/s", "2") + r" \cdot " + ntex(h, "m") + " / (" + ntex(m1, "kg") + " + " + ntex(m2, "kg") + ")}", rv["valor"], rv["decimals"], "m/s"),
                f"L’acceleració és {valor(ra['valor'], ra['decimals'], 'm/s²')} i, quan la massa grossa ha baixat {fmt_s(h)} m, la velocitat és {valor(rv['valor'], rv['decimals'], 'm/s')}."),
            ("atwood", {"m1": f"{fmt_s(m1)} kg", "m2": f"{fmt_s(m2)} kg", "qui": f"Politja · baixa {fmt_s(h)} m"},
             "Les dues masses porten la mateixa rapidesa."))

    atwood_e("La politja, per forces i per energia", "<p>Dues masses d’1 kg i de 2 kg pengen d’una politja ideal i parteixen del repòs. g = 9,8 m/s².</p><p>a) Quina acceleració tenen?</p><p>b) Quina velocitat porten quan la de 2 kg ha baixat 1 m?</p>", 1, 2, 1)
    atwood_e("Els cubells del pou", "<p>Dos cubells de 2 kg i 3 kg pengen d’una politja ideal i parteixen del repòs. g = 9,8 m/s².</p><p>a) Quina acceleració tenen?</p><p>b) Quina velocitat porten quan el de 3 kg ha baixat 1,5 m?</p>", 2, 3, 1.5)
    return out
