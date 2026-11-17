"""Càlculs tancats que omplen les solucions. El verificador en té una còpia independent."""
import math

G = 9.8


def _need(p, *keys):
    for k in keys:
        if k not in p:
            raise KeyError(k)
    return [p[k] for k in keys]


def calcular(tipus, p):
    g = p.get("g", G)
    if tipus == "mru_x":
        x0, v, t = _need(p, "x0", "v", "t")
        return x0 + v * t
    if tipus == "mru_v":
        x0, x, t = _need(p, "x0", "x", "t")
        return (x - x0) / t
    if tipus == "mru_t":
        x0, x, v = _need(p, "x0", "x", "v")
        return (x - x0) / v
    if tipus == "encontre_t":
        x10, v1, x20, v2 = _need(p, "x10", "v1", "x20", "v2")
        return (x20 - x10) / (v1 - v2)
    if tipus == "encontre_x":
        t = calcular("encontre_t", p)
        return p["x10"] + p["v1"] * t
    if tipus == "mrua_v":
        v0, a, t = _need(p, "v0", "a", "t")
        return v0 + a * t
    if tipus == "mrua_x":
        x0, v0, a, t = _need(p, "x0", "v0", "a", "t")
        return x0 + v0 * t + 0.5 * a * t * t
    if tipus == "mrua_t":
        v0, v, a = _need(p, "v0", "v", "a")
        return (v - v0) / a
    if tipus == "mrua_a_t":
        v0, v, t = _need(p, "v0", "v", "t")
        return (v - v0) / t
    if tipus == "mrua_vf":
        v0, a, dx = _need(p, "v0", "a", "dx")
        disc = v0 * v0 + 2 * a * dx
        if disc < 0:
            raise ValueError("discriminant negatiu")
        sgn = p.get("signe", 1)
        return sgn * math.sqrt(disc)
    if tipus == "mrua_a_x":
        v0, v, dx = _need(p, "v0", "v", "dx")
        return (v * v - v0 * v0) / (2 * dx)
    if tipus == "caiguda_t":
        (h,) = _need(p, "h")
        return math.sqrt(2 * h / g)
    if tipus == "caiguda_v":
        (h,) = _need(p, "h")
        return math.sqrt(2 * g * h)
    if tipus == "llanc_h":
        (v0,) = _need(p, "v0")
        return v0 * v0 / (2 * g)
    if tipus == "llanc_t_dalt":
        (v0,) = _need(p, "v0")
        return v0 / g
    if tipus == "llanc_t_total":
        (v0,) = _need(p, "v0")
        return 2 * v0 / g
    if tipus == "vertical_y":
        y0, v0, t = _need(p, "y0", "v0", "t")
        return y0 + v0 * t - 0.5 * g * t * t
    if tipus == "vertical_v":
        v0, t = _need(p, "v0", "t")
        return v0 - g * t
    if tipus == "vertical_t":
        # temps en què passa per l'altura y. branca: "primera" o "segona"
        y0, v0, y = _need(p, "y0", "v0", "y")
        disc = v0 * v0 - 2 * g * (y - y0)
        if disc < 0:
            raise ValueError("no hi arriba")
        s = math.sqrt(disc)
        t1, t2 = (v0 - s) / g, (v0 + s) / g
        return t1 if p.get("branca") == "primera" else t2
    if tipus == "tir_h_t":
        (h,) = _need(p, "h")
        return math.sqrt(2 * h / g)
    if tipus == "tir_h_R":
        h, v0 = _need(p, "h", "v0")
        return v0 * math.sqrt(2 * h / g)
    if tipus == "tir_h_vy":
        h = _need(p, "h")[0]
        return math.sqrt(2 * g * h)
    if tipus == "tir_h_v":
        h, v0 = _need(p, "h", "v0")
        vy = math.sqrt(2 * g * h)
        return math.sqrt(v0 * v0 + vy * vy)
    if tipus == "tir_t":
        v0, th = _need(p, "v0", "theta")
        return 2 * v0 * math.sin(math.radians(th)) / g
    if tipus == "tir_H":
        v0, th = _need(p, "v0", "theta")
        vy = v0 * math.sin(math.radians(th))
        return vy * vy / (2 * g)
    if tipus == "tir_R":
        v0, th = _need(p, "v0", "theta")
        return v0 * v0 * math.sin(math.radians(2 * th)) / g
    if tipus == "tir_vx":
        v0, th = _need(p, "v0", "theta")
        return v0 * math.cos(math.radians(th))
    if tipus == "tir_vy0":
        v0, th = _need(p, "v0", "theta")
        return v0 * math.sin(math.radians(th))
    if tipus == "tir_x":
        v0, th, t = _need(p, "v0", "theta", "t")
        return v0 * math.cos(math.radians(th)) * t
    if tipus == "tir_y":
        v0, th, t = _need(p, "v0", "theta", "t")
        vy = v0 * math.sin(math.radians(th))
        return vy * t - 0.5 * g * t * t
    if tipus == "tir_vy":
        v0, th, t = _need(p, "v0", "theta", "t")
        return v0 * math.sin(math.radians(th)) - g * t
    if tipus == "tir_vmod":
        v0, th, t = _need(p, "v0", "theta", "t")
        vx = v0 * math.cos(math.radians(th))
        vy = v0 * math.sin(math.radians(th)) - g * t
        return math.sqrt(vx * vx + vy * vy)
    if tipus == "tir_v0_R":
        # v0 a partir de l'abast i l'angle, sortida des del terra
        R, th = _need(p, "R", "theta")
        s = math.sin(math.radians(2 * th))
        return math.sqrt(R * g / s)
    if tipus == "omega_T":
        (T,) = _need(p, "T")
        return 2 * math.pi / T
    if tipus == "omega_f":
        (f,) = _need(p, "f")
        return 2 * math.pi * f
    if tipus == "freq_T":
        (T,) = _need(p, "T")
        return 1 / T
    if tipus == "T_f":
        (f,) = _need(p, "f")
        return 1 / f
    if tipus == "omega_theta":
        th, t = _need(p, "theta", "t")  # theta en radiants
        return th / t
    if tipus == "v_wr":
        w, r = _need(p, "omega", "r")
        return w * r
    if tipus == "omega_vr":
        v, r = _need(p, "v", "r")
        return v / r
    if tipus == "ac_v":
        v, r = _need(p, "v", "r")
        return v * v / r
    if tipus == "ac_w":
        w, r = _need(p, "omega", "r")
        return w * w * r
    if tipus == "T_vr":
        v, r = _need(p, "v", "r")
        return 2 * math.pi * r / v
    if tipus == "arc":
        r, th = _need(p, "r", "theta")  # radiants
        return r * th
    if tipus == "f_ma":
        m, a = _need(p, "m", "a")
        return m * a
    if tipus == "a_fm":
        F, m = _need(p, "F", "m")
        return F / m
    if tipus == "m_fa":
        F, a = _need(p, "F", "a")
        return F / a
    if tipus == "pes":
        (m,) = _need(p, "m")
        return m * g
    if tipus == "normal_pla":
        (m,) = _need(p, "m")
        return m * g
    if tipus == "freg_c":
        mu, N = _need(p, "mu", "N")
        return mu * N
    if tipus == "a_hor_f":
        # força horitzontal F, fregament cinètic, N = mg
        F, m, mu = _need(p, "F", "m", "mu")
        return (F - mu * m * g) / m
    if tipus == "a_hor":
        F, m = _need(p, "F", "m")
        return F / m
    if tipus == "a_inclin_0":
        (alpha,) = _need(p, "alpha")
        return g * math.sin(math.radians(alpha))
    if tipus == "N_inclin":
        m, alpha = _need(p, "m", "alpha")
        return m * g * math.cos(math.radians(alpha))
    if tipus == "a_inclin_f":
        # baixa el pla, fregament cinètic
        alpha, mu = _need(p, "alpha", "mu")
        return g * (math.sin(math.radians(alpha)) - mu * math.cos(math.radians(alpha)))
    if tipus == "a_inclin_puja":
        # força F paral·lela al pla, cap amunt, amb fregament cinètic (el cos puja)
        F, m, alpha, mu = _need(p, "F", "m", "alpha", "mu")
        return (F - m * g * math.sin(math.radians(alpha)) - mu * m * g * math.cos(math.radians(alpha))) / m
    if tipus == "atwood_a":
        m1, m2 = _need(p, "m1", "m2")  # m2 baixa
        return (m2 - m1) * g / (m1 + m2)
    if tipus == "atwood_T":
        m1, m2 = _need(p, "m1", "m2")
        return 2 * m1 * m2 * g / (m1 + m2)
    if tipus == "atwood_v":
        m1, m2, h = _need(p, "m1", "m2", "h")
        return math.sqrt(2 * (m2 - m1) * g * h / (m1 + m2))
    if tipus == "penjant_a":
        # M damunt la taula, m penjat. mu opcional (0 si no hi és)
        M, m = _need(p, "M", "m")
        mu = p.get("mu", 0)
        return (m * g - mu * M * g) / (M + m)
    if tipus == "penjant_T":
        M, m = _need(p, "M", "m")
        mu = p.get("mu", 0)
        a = (m * g - mu * M * g) / (M + m)
        return m * g - m * a
    if tipus == "molla_F":
        k, x = _need(p, "k", "x")
        return k * x
    if tipus == "ac_necessaria":
        m, v, r = _need(p, "m", "v", "r")
        return m * v * v / r
    if tipus == "vmax_revolt":
        mu, r = _need(p, "mu", "r")
        return math.sqrt(mu * r * g)
    if tipus == "theta_peralt":
        v, r = _need(p, "v", "r")
        return math.degrees(math.atan(v * v / (r * g)))
    if tipus == "v_peralt":
        r, th = _need(p, "r", "theta")
        return math.sqrt(r * g * math.tan(math.radians(th)))
    if tipus == "N_loop_dalt":
        m, v, r = _need(p, "m", "v", "r")
        return m * v * v / r - m * g
    if tipus == "N_loop_baix":
        m, v, r = _need(p, "m", "v", "r")
        return m * v * v / r + m * g
    if tipus == "T_cord_baix":
        m, v, r = _need(p, "m", "v", "r")
        return m * v * v / r + m * g
    if tipus == "T_cord_angle":
        m, v, r, th = _need(p, "m", "v", "r", "theta")
        return m * v * v / r + m * g * math.cos(math.radians(th))
    if tipus == "vmin_loop":
        (r,) = _need(p, "r")
        return math.sqrt(g * r)
    if tipus == "ec":
        m, v = _need(p, "m", "v")
        return 0.5 * m * v * v
    if tipus == "ep":
        m, h = _need(p, "m", "h")
        return m * g * h
    if tipus == "epe":
        k, x = _need(p, "k", "x")
        return 0.5 * k * x * x
    if tipus == "v_caiguda_e":
        (h,) = _need(p, "h")
        return math.sqrt(2 * g * h)
    if tipus == "h_llanc_e":
        (v,) = _need(p, "v")
        return v * v / (2 * g)
    if tipus == "v_entre_altures":
        h1, v1, h2 = _need(p, "h1", "v1", "h2")
        disc = v1 * v1 + 2 * g * (h1 - h2)
        if disc < 0:
            raise ValueError("no hi arriba")
        return math.sqrt(disc)
    if tipus == "v_inclin_e":
        d, alpha = _need(p, "d", "alpha")
        return math.sqrt(2 * g * d * math.sin(math.radians(alpha)))
    if tipus == "h_pendol":
        L, th = _need(p, "L", "theta")
        return L * (1 - math.cos(math.radians(th)))
    if tipus == "v_pendol":
        L, th = _need(p, "L", "theta")
        h = L * (1 - math.cos(math.radians(th)))
        return math.sqrt(2 * g * h)
    if tipus == "v_molla":
        k, m, A = _need(p, "k", "m", "A")
        return A * math.sqrt(k / m)
    if tipus == "v_molla_x":
        k, m, A, x = _need(p, "k", "m", "A", "x")
        disc = k * (A * A - x * x) / m
        return math.sqrt(disc)
    if tipus == "x_molla_vertical":
        # es deixa anar en contacte, sense velocitat: mgx = 1/2 k x^2, x = 2mg/k
        m, k = _need(p, "m", "k")
        return 2 * m * g / k
    if tipus == "H_loop":
        (r,) = _need(p, "r")
        return 2.5 * r
    if tipus == "v_loop_des_de_H":
        H, r, h = _need(p, "H", "r", "h")
        # Ep=0 al terra. Al punt d'altura h: mgH = 1/2 mv^2 + mgh
        disc = 2 * g * (H - h)
        if disc < 0:
            raise ValueError("no hi arriba")
        return math.sqrt(disc)
    if tipus == "potencia":
        # només definició P = ΔE / Δt, usada si cal en teoria; no als problemes d'energia amb fregament
        E, t = _need(p, "E", "t")
        return E / t
    raise KeyError("tipus desconegut: " + tipus)
