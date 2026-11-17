"""Verificació independent de totes les solucions.

Les fórmules d'aquest fitxer no importen el motor que escriu el llibre.
Primer es comproven contra resultats calculats a mà (oracles). Després es
comparen, problema per problema, amb els valors publicats.
"""
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fmt import fmt  # només l'arrodoniment, no la física

G = 9.8


def fis(tipus, p):
    g = float(p.get("g", G))
    if tipus == "mru_x":
        return p["x0"] + p["t"] * p["v"]
    if tipus == "mru_v":
        return (p["x"] - p["x0"]) / p["t"]
    if tipus == "mru_t":
        return (p["x"] - p["x0"]) / p["v"]
    if tipus == "encontre_t":
        return (p["x10"] - p["x20"]) / (p["v2"] - p["v1"])
    if tipus == "encontre_x":
        t = fis("encontre_t", p)
        return p["x10"] + p["v1"] * t
    if tipus == "mrua_v":
        return p["v0"] + p["t"] * p["a"]
    if tipus == "mrua_x":
        return p["x0"] + p["t"] * (p["v0"] + p["a"] * p["t"] / 2)
    if tipus == "mrua_t":
        return (p["v"] - p["v0"]) / p["a"]
    if tipus == "mrua_a_t":
        return (p["v"] - p["v0"]) / p["t"]
    if tipus == "mrua_vf":
        disc = p["v0"] ** 2 + 2 * p["a"] * p["dx"]
        if disc < -1e-9:
            raise ValueError("discriminant")
        return p.get("signe", 1) * math.sqrt(max(0.0, disc))
    if tipus == "mrua_a_x":
        return (p["v"] ** 2 - p["v0"] ** 2) / (2 * p["dx"])
    if tipus == "caiguda_t":
        return math.sqrt(2 * p["h"] / g)
    if tipus == "caiguda_v":
        return math.sqrt(2 * g * p["h"])
    if tipus == "llanc_h":
        return (p["v0"] ** 2) / (2 * g)
    if tipus == "llanc_t_dalt":
        return p["v0"] / g
    if tipus == "llanc_t_total":
        return 2 * p["v0"] / g
    if tipus == "vertical_y":
        return p["y0"] + p["t"] * p["v0"] - g * p["t"] ** 2 / 2
    if tipus == "vertical_v":
        return p["v0"] - g * p["t"]
    if tipus == "vertical_t":
        disc = p["v0"] ** 2 - 2 * g * (p["y"] - p["y0"])
        rad = math.sqrt(disc)
        menor = (p["v0"] - rad) / g
        major = (p["v0"] + rad) / g
        return menor if p.get("branca") == "primera" else major
    if tipus == "tir_h_t":
        return math.sqrt(2 * p["h"] / g)
    if tipus == "tir_h_R":
        return p["v0"] * math.sqrt(2 * p["h"] / g)
    if tipus == "tir_h_vy":
        return math.sqrt(2 * g * p["h"])
    if tipus == "tir_h_v":
        return math.hypot(p["v0"], math.sqrt(2 * g * p["h"]))
    if tipus == "tir_h_v0":
        return p["R"] / math.sqrt(2 * p["h"] / g)
    if tipus == "tir_t":
        return 2 * p["v0"] * math.sin(math.radians(p["theta"])) / g
    if tipus == "tir_H":
        vy = p["v0"] * math.sin(math.radians(p["theta"]))
        return vy ** 2 / (2 * g)
    if tipus == "tir_R":
        return p["v0"] ** 2 * math.sin(math.radians(2 * p["theta"])) / g
    if tipus == "tir_vx":
        return p["v0"] * math.cos(math.radians(p["theta"]))
    if tipus == "tir_vy0":
        return p["v0"] * math.sin(math.radians(p["theta"]))
    if tipus == "tir_x":
        return p["v0"] * math.cos(math.radians(p["theta"])) * p["t"]
    if tipus == "tir_y":
        vy = p["v0"] * math.sin(math.radians(p["theta"]))
        return vy * p["t"] - g * p["t"] ** 2 / 2
    if tipus == "tir_vy":
        return p["v0"] * math.sin(math.radians(p["theta"])) - g * p["t"]
    if tipus == "tir_vmod":
        vx = p["v0"] * math.cos(math.radians(p["theta"]))
        vy = p["v0"] * math.sin(math.radians(p["theta"])) - g * p["t"]
        return math.hypot(vx, vy)
    if tipus == "tir_v0_R":
        return math.sqrt(p["R"] * g / math.sin(math.radians(2 * p["theta"])))
    if tipus == "omega_T":
        return 2 * math.pi / p["T"]
    if tipus == "omega_f":
        return 2 * math.pi * p["f"]
    if tipus == "freq_T":
        return 1 / p["T"]
    if tipus == "T_f":
        return 1 / p["f"]
    if tipus == "omega_theta":
        return p["theta"] / p["t"]
    if tipus == "v_wr":
        return p["omega"] * p["r"]
    if tipus == "omega_vr":
        return p["v"] / p["r"]
    if tipus == "ac_v":
        return p["v"] ** 2 / p["r"]
    if tipus == "ac_w":
        return p["omega"] ** 2 * p["r"]
    if tipus == "T_vr":
        return 2 * math.pi * p["r"] / p["v"]
    if tipus == "arc":
        return p["r"] * p["theta"]
    if tipus == "f_ma":
        return p["m"] * p["a"]
    if tipus == "a_fm":
        return p["F"] / p["m"]
    if tipus == "m_fa":
        return p["F"] / p["a"]
    if tipus == "pes":
        return p["m"] * g
    if tipus == "normal_pla":
        return p["m"] * g
    if tipus == "freg_c":
        return p["mu"] * p["N"]
    if tipus == "a_hor_f":
        return p["F"] / p["m"] - p["mu"] * g
    if tipus == "a_hor":
        return p["F"] / p["m"]
    if tipus == "a_inclin_0":
        return g * math.sin(math.radians(p["alpha"]))
    if tipus == "N_inclin":
        return p["m"] * g * math.cos(math.radians(p["alpha"]))
    if tipus == "a_inclin_f":
        s = math.sin(math.radians(p["alpha"]))
        c = math.cos(math.radians(p["alpha"]))
        return g * s - p["mu"] * g * c
    if tipus == "a_inclin_puja":
        s = math.sin(math.radians(p["alpha"]))
        c = math.cos(math.radians(p["alpha"]))
        return (p["F"] - p["m"] * g * s - p["mu"] * p["m"] * g * c) / p["m"]
    if tipus == "atwood_a":
        return g * (p["m2"] - p["m1"]) / (p["m1"] + p["m2"])
    if tipus == "atwood_T":
        return (2 * p["m1"] * p["m2"] / (p["m1"] + p["m2"])) * g
    if tipus == "atwood_v":
        return math.sqrt(2 * g * (p["m2"] - p["m1"]) * p["h"] / (p["m1"] + p["m2"]))
    if tipus == "penjant_a":
        mu = p.get("mu", 0)
        return g * (p["m"] - mu * p["M"]) / (p["M"] + p["m"])
    if tipus == "penjant_T":
        mu = p.get("mu", 0)
        a = g * (p["m"] - mu * p["M"]) / (p["M"] + p["m"])
        return p["m"] * (g - a)
    if tipus == "molla_F":
        return p["k"] * p["x"]
    if tipus == "ac_necessaria":
        return p["m"] * p["v"] ** 2 / p["r"]
    if tipus == "vmax_revolt":
        return math.sqrt(p["mu"] * g * p["r"])
    if tipus == "theta_peralt":
        return math.degrees(math.atan2(p["v"] ** 2, p["r"] * g))
    if tipus == "v_peralt":
        return math.sqrt(p["r"] * g * math.tan(math.radians(p["theta"])))
    if tipus == "N_loop_dalt":
        return p["m"] * (p["v"] ** 2 / p["r"] - g)
    if tipus == "N_loop_baix":
        return p["m"] * (p["v"] ** 2 / p["r"] + g)
    if tipus == "T_cord_baix":
        return p["m"] * (p["v"] ** 2 / p["r"] + g)
    if tipus == "T_cord_angle":
        return p["m"] * p["v"] ** 2 / p["r"] + p["m"] * g * math.cos(math.radians(p["theta"]))
    if tipus == "vmin_loop":
        return math.sqrt(g * p["r"])
    if tipus == "ec":
        return p["m"] * p["v"] * p["v"] / 2
    if tipus == "ep":
        return p["m"] * g * p["h"]
    if tipus == "epe":
        return p["k"] * p["x"] * p["x"] / 2
    if tipus == "v_caiguda_e":
        return math.sqrt(2 * g * p["h"])
    if tipus == "h_llanc_e":
        return p["v"] ** 2 / (2 * g)
    if tipus == "v_entre_altures":
        return math.sqrt(p["v1"] ** 2 + 2 * g * (p["h1"] - p["h2"]))
    if tipus == "v_inclin_e":
        return math.sqrt(2 * g * p["d"] * math.sin(math.radians(p["alpha"])))
    if tipus == "h_pendol":
        return p["L"] * (1 - math.cos(math.radians(p["theta"])))
    if tipus == "v_pendol":
        h = p["L"] * (1 - math.cos(math.radians(p["theta"])))
        return math.sqrt(2 * g * h)
    if tipus == "v_molla":
        return p["A"] * math.sqrt(p["k"] / p["m"])
    if tipus == "v_molla_x":
        return math.sqrt(p["k"] / p["m"] * (p["A"] ** 2 - p["x"] ** 2))
    if tipus == "x_molla_vertical":
        return 2 * p["m"] * g / p["k"]
    if tipus == "H_loop":
        return 5 * p["r"] / 2
    if tipus == "v_loop_des_de_H":
        return math.sqrt(2 * g * (p["H"] - p["h"]))
    raise KeyError(tipus)


# Resultats fets a mà, amb g = 9,8. Si una fórmula del verificador és falsa, cau aquí.
ORACLES = [
    ("mru_x", {"x0": 10, "v": 3, "t": 4}, 22),
    ("mru_v", {"x0": 0, "x": 100, "t": 8}, 12.5),
    ("mrua_x", {"x0": 0, "v0": 0, "a": 2, "t": 5}, 25),
    ("mrua_v", {"v0": 4, "a": -2, "t": 3}, -2),
    ("mrua_vf", {"v0": 0, "a": 2, "dx": 8, "signe": 1}, math.sqrt(32)),
    ("caiguda_t", {"h": 4.9}, 1),
    ("caiguda_v", {"h": 4.9}, 9.8),
    ("llanc_h", {"v0": 19.6}, 19.6),
    ("llanc_t_dalt", {"v0": 19.6}, 2),
    ("llanc_t_total", {"v0": 19.6}, 4),
    ("tir_h_t", {"h": 4.9}, 1),
    ("tir_h_R", {"h": 4.9, "v0": 10}, 10),
    ("tir_h_v", {"h": 4.9, "v0": 10}, math.sqrt(100 + 96.04)),
    ("tir_R", {"v0": 14, "theta": 45}, 20),
    ("tir_H", {"v0": 14, "theta": 90}, 10),
    ("omega_T", {"T": 0.5}, 4 * math.pi),
    ("v_wr", {"omega": 5, "r": 0.4}, 2),
    ("ac_v", {"v": 4, "r": 2}, 8),
    ("pes", {"m": 2}, 19.6),
    ("a_hor_f", {"F": 20, "m": 4, "mu": 0.25}, 2.55),
    ("a_inclin_0", {"alpha": 30}, 4.9),
    ("atwood_a", {"m1": 2, "m2": 3}, 1.96),
    ("atwood_T", {"m1": 2, "m2": 3}, 23.52),
    ("atwood_v", {"m1": 2, "m2": 3, "h": 5}, math.sqrt(19.6)),
    ("vmin_loop", {"r": 2.5}, math.sqrt(24.5)),
    ("H_loop", {"r": 2}, 5),
    ("v_caiguda_e", {"h": 10}, math.sqrt(196)),
    ("h_llanc_e", {"v": 9.8}, 4.9),
    ("h_pendol", {"L": 2, "theta": 60}, 1),
    ("v_molla", {"k": 200, "m": 0.5, "A": 0.1}, 2),
    ("x_molla_vertical", {"m": 1, "k": 98}, 0.2),
    ("ec", {"m": 2, "v": 3}, 9),
    ("ep", {"m": 2, "h": 5}, 98),
    ("v_entre_altures", {"h1": 8, "v1": 0, "h2": 3}, math.sqrt(98)),
]


def comprova_oracles():
    errors = []
    for tipus, params, esperat in ORACLES:
        obt = fis(tipus, params)
        if abs(obt - esperat) > 1e-6:
            errors.append(f"oracle {tipus}: {obt} ≠ {esperat}")
    return errors


def text_net(html):
    t = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", t)


def comprova_problemes(problemes):
    """problemes: llista de dicts amb id, tema, enun, solucio, resultats=[{tipus, params, nom, decimals, unitat}]."""
    errors = []
    from motor import calcular

    for pr in problemes:
        net = text_net(pr["enunciat"] + " " + pr["solucio"])
        if pr["tema"] in ("energia", "mixtos") and re.search(r"fregament", net, re.I):
            errors.append(f"{pr['id']}: l'energia no pot portar fregament")
        if pr["tema"] == "energia" and re.search(r"no conservativ", net, re.I):
            errors.append(f"{pr['id']}: no s'ha d'usar el treball de les forces no conservatives")
        if "Plantejament" not in pr["solucio"] or "Resultat" not in pr["solucio"]:
            errors.append(f"{pr['id']}: la solució no té plantejament i resultat")
        enun = text_net(pr["enunciat"]).lower()
        if re.search(r"\bun cos\b", enun):
            errors.append(f"{pr['id']}: l'enunciat parla d'«un cos» i no de la situació del títol")
        claus = [m for m in re.findall(r"[0-9A-Za-zÀ-ÿ]+", pr["titol"]) if len(m) >= 4]
        if claus and not any(m.lower() in enun for m in claus):
            errors.append(f"{pr['id']}: el títol «{pr['titol']}» no lliga amb l'enunciat")
        if "·" not in net and "/" not in net:
            errors.append(f"{pr['id']}: el càlcul no mostra la substitució")
        for r in pr["resultats"]:
            a = calcular(r["tipus"], r["params"])
            b = fis(r["tipus"], r["params"])
            if abs(a - b) > 1e-6:
                errors.append(f"{pr['id']} {r['nom']}: motor {a} ≠ verificador {b}")
            shown = fmt(b, r["decimals"])
            unit = r["unitat"]
            # el nombre publicat, amb la unitat a tocar (permet un espai fi)
            if shown not in net:
                errors.append(f"{pr['id']} {r['nom']}: no surt {shown} al text")
            if unit and unit not in net:
                errors.append(f"{pr['id']} {r['nom']}: falta la unitat {unit}")
            # g de l'enunciat, si n'hi ha
            if "g" in r["params"] and abs(r["params"]["g"] - 9.8) > 1e-9:
                errors.append(f"{pr['id']}: g diferent de 9,8 sense motiu")
    return errors


def main():
    from banc import tots

    err = comprova_oracles()
    err += comprova_problemes(tots())
    # recompte
    from collections import Counter
    c = Counter(p["tema"] for p in tots())
    print("Problemes:", dict(c), "total", sum(c.values()))
    if err:
        print(f"{len(err)} errors")
        for e in err[:40]:
            print(" -", e)
        sys.exit(1)
    print("Verificació correcta.")


if __name__ == "__main__":
    main()
