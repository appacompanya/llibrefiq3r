"""Fórmules del llibre en HTML, amb un subconjunt petit de notació matemàtica.

Entrada (exemples):
  x = x_0 + v_0 t + \\frac{1}{2} a t^2
  v^2 = v_0^2 + 2 a \\Delta x
  a_c = \\frac{v^2}{r}
"""
import html

GREEK = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "theta": "θ",
    "pi": "π", "omega": "ω", "mu": "μ", "phi": "φ", "varphi": "φ", "rho": "ρ",
    "Delta": "Δ", "Omega": "Ω", "Sigma": "Σ",
}
SYMS = {
    "cdot": "·", "times": "×", "approx": "≈", "leq": "≤", "geq": "≥",
    "pm": "±", "mp": "∓", "rightarrow": "→", "circ": "°", "degree": "°",
    "infty": "∞", "neq": "≠", "sum": "Σ",
}


def _raw_group(s, i):
    if i >= len(s) or s[i] != "{":
        raise ValueError("s'esperava { a: " + s)
    depth, j = 1, i + 1
    while j < len(s) and depth:
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
        if depth:
            j += 1
    return s[i + 1:j], j + 1


def _group(s, i):
    """Llegeix un grup {…} o un sol àtom. Retorna (html, i_nou)."""
    if i < len(s) and s[i] == "{":
        i += 1
        inner, i = _seq(s, i)
        if i >= len(s) or s[i] != "}":
            raise ValueError("falta } a: " + s)
        return inner, i + 1
    return _atom(s, i)


def _atom(s, i):
    if i >= len(s):
        raise ValueError("fórmula inacabada: " + s)
    if s[i] == "\\":
        j = i + 1
        if j < len(s) and not s[j].isalpha():
            cmd, j = s[j], j + 1
        else:
            while j < len(s) and s[j].isalpha():
                j += 1
            cmd = s[i + 1:j]
        if cmd == "frac":
            num, j = _group(s, j)
            den, j = _group(s, j)
            return f'<span class="frac"><span class="n">{num}</span><span class="d">{den}</span></span>', j
        if cmd == "sqrt":
            arg, j = _group(s, j)
            return f'<span class="sqrt">{arg}</span>', j
        if cmd in ("mathrm", "text"):
            raw, j = _raw_group(s, j)
            return f'<span class="rm">{html.escape(raw)}</span>', j
        if cmd == "vec":
            arg, j = _group(s, j)
            return f'<span class="vec">{arg}</span>', j
        if cmd in GREEK:
            return f"<i>{GREEK[cmd]}</i>", j
        if cmd in SYMS:
            return f'<span class="op">{SYMS[cmd]}</span>', j
        if cmd in ("sin", "cos", "tan", "log", "max", "min", "arctan"):
            return f'<span class="rm">{cmd}</span>', j
        if cmd in ("quad", "qquad", ",", " "):
            return '<span class="thin"> </span><span class="thin"> </span>', j
        raise ValueError("ordre desconeguda \\" + cmd)
    if s[i] == "{":
        return _group(s, i)
    if s[i].isdigit() or (s[i] == "," and i + 1 < len(s) and s[i + 1].isdigit()):
        j = i
        if s[j].isdigit():
            while j < len(s) and s[j].isdigit():
                j += 1
        if j < len(s) and s[j] == ",":
            k = j + 1
            if k < len(s) and s[k].isdigit():
                j = k
                while j < len(s) and s[j].isdigit():
                    j += 1
        return f'<span class="rm">{html.escape(s[i:j])}</span>', j
    if s[i].isalpha():
        return f"<i>{html.escape(s[i])}</i>", i + 1
    if s[i] == "(":
        inner, j = _seq(s, i + 1, stop=")")
        if j >= len(s) or s[j] != ")":
            raise ValueError("falta ) a: " + s)
        return f'<span class="op">(</span>{inner}<span class="op">)</span>', j + 1
    if s[i] in "+-=)[]<>":
        return f'<span class="op">{html.escape(s[i])}</span>', i + 1
    return html.escape(s[i]), i + 1


def _seq(s, i, stop="}"):
    parts = []
    while i < len(s):
        if s[i] in stop:
            break
        if s[i].isspace():
            i += 1
            parts.append('<span class="thin"> </span>')
            continue
        atom, i = _atom(s, i)
        while i < len(s) and s[i] in "_^":
            kind = s[i]
            i += 1
            arg, i = _group(s, i) if i < len(s) and s[i] == "{" else _atom(s, i)
            tag = "sub" if kind == "_" else "sup"
            atom = f"{atom}<{tag}>{arg}</{tag}>"
        parts.append(atom)
    return "".join(parts), i


def render(tex, display=False):
    body, i = _seq(tex.strip(), 0)
    if i != len(tex.strip()):
        raise ValueError("sobra text a: " + tex)
    cls = "math disp" if display else "math"
    return f'<span class="{cls}">{body}</span>'


def M(tex):
    return render(tex, False)


def EQ(tex):
    return f'<div class="eq">{render(tex, True)}</div>'
