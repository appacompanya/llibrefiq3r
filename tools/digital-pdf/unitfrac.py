"""Mostra les unitats compostes (g/L, m/s, kg/m³…) com a fracció apilada.
- Text HTML: <span class="uf"><span>g</span><span>L</span></span>
- Fórmules LaTeX: \\mathrm{g/L} -> \\dfrac{\\mathrm{g}}{\\mathrm{L}}
No toca <script>, <style>, <svg>, atributs, URL ni camps de formulari."""
import re

_U = r'(?:[kKhdcmµμnMG]?(?:g|L|l|m|s|h|min|mol|J|W|N|Pa|atm|bar|K|A|V|Ω|Wh|cal|M)|°C|€)(?:[²³⁻¹]+)?'
_PROD = _U + r'(?:·' + _U + r')*'
TEXT_RE = re.compile(r'(?<![\w/·.])(' + _PROD + r')/(\(' + _PROD + r'\)|' + _PROD + r')(?![\w/²³]|<sup)')

_MU = r'[A-Za-zµμ°Ω]+(?:\^\{?-?\d\}?)?'
_MPROD = _MU + r'(?:\s*\\cdot\s*' + _MU + r')*'
MATH_RE = re.compile(r'\\mathrm\{\s*(' + _MPROD + r')\s*/\s*(\(\s*' + _MPROD + r'\s*\)|' + _MPROD + r')\s*\}')

CSS = (".uf{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;"
       "font-size:.9em;line-height:1.05;margin:0 .12em;text-indent:0}"
       ".uf>span{display:block;padding:0 .14em;white-space:nowrap}"
       ".uf>span:first-child{border-bottom:.08em solid currentColor}")


def _frac_text(m):
    a, b = m.group(1), m.group(2)
    if b.startswith('(') and b.endswith(')'):
        b = b[1:-1]
    return f'<span class="uf"><span>{a}</span><span>{b}</span></span>'


def _frac_math(m):
    a, b = m.group(1).strip(), m.group(2).strip()
    if b.startswith('(') and b.endswith(')'):
        b = b[1:-1].strip()
    return r'\dfrac{\mathrm{' + a + r'}}{\mathrm{' + b + r'}}'


def frac_math(tex):
    return MATH_RE.sub(_frac_math, tex)


_MATH_SPLIT = re.compile(r'(\\\(.*?\\\)|\\\[.*?\\\])', re.S)


def _frac_plain(txt):
    out = []
    for part in _MATH_SPLIT.split(txt):
        if part.startswith('\\(') or part.startswith('\\['):
            out.append(frac_math(part))
            continue
        # no tocar URL: es protegeixen les paraules amb :// o www.
        words = re.split(r'(\s+)', part)
        for i, w in enumerate(words):
            if '://' in w or 'www.' in w or '.org/' in w or '.cat/' in w or '.es/' in w:
                continue
            words[i] = TEXT_RE.sub(_frac_text, w) if '/' in w else w
        out.append(''.join(words))
    return ''.join(out)


_SKIP = ('script', 'style', 'svg', 'textarea', 'math-field', 'title')


def frac_units(html):
    toks = re.split(r'(<[^>]+>)', html)
    skip = []
    out = []
    buf = []

    def flush():
        if buf:
            out.append(_frac_plain(''.join(buf)) if not skip else ''.join(buf))
            buf.clear()

    for t in toks:
        if t.startswith('<'):
            m = re.match(r'<\s*(/)?\s*([a-zA-Z][\w-]*)', t)
            if m:
                name = m.group(2).lower()
                if name in _SKIP:
                    flush()
                    if m.group(1):
                        if skip and skip[-1] == name:
                            skip.pop()
                    elif not t.rstrip().endswith('/>'):
                        skip.append(name)
                    out.append(t)
                    continue
            # les etiquetes en línia (b, i, sub, sup) no trenquen el text matemàtic
            if re.match(r'</?(b|i|em|strong|sub|sup)\b', t):
                buf.append(t)
            else:
                flush()
                out.append(t)
        else:
            buf.append(t)
    flush()
    return ''.join(out)


if __name__ == '__main__':
    tests = ['Densitat (g/mL) i 54 km/h, 9 g/L, 0,15 €/kWh, kJ/(kg·K), m/s², V/F, 1/V, https://x.cat/m/s',
             r'\(1{,}2\ \mathrm{g/mL}\) i \(c = 4{,}18\ \mathrm{kJ/(kg\cdot K)}\) i \(\mathrm{kg/m^3}\)',
             '<svg><text>m/s</text></svg> <b>v</b> (m/s)']
    for t in tests:
        print(frac_units(t))
