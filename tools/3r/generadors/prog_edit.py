"""Eines per editar la programació (docx) conservant el format de cada run."""
import re, copy
from docx import Document
from docx.oxml.ns import qn

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def ptext(p_el):
    return "".join(t.text or "" for t in p_el.iter(W + 't'))


def runs_t(p_el):
    """Llista de nodes w:t en ordre (dins de runs, també hiperenllaços)."""
    return [t for t in p_el.iter(W + 't')]


def sub_in_par(p_el, pattern, repl, flags=0):
    """Substitueix el patró al paràgraf encara que travessi diversos runs; el text nou va al run on comença la coincidència."""
    ts = runs_t(p_el)
    if not ts:
        return 0
    full = "".join(t.text or "" for t in ts)
    rx = re.compile(pattern, flags)
    ms = list(rx.finditer(full))
    if not ms:
        return 0
    # de darrere cap endavant per no desplaçar posicions
    for m in reversed(ms):
        new = m.expand(repl) if isinstance(repl, str) else repl(m)
        a, b = m.start(), m.end()
        pos = 0
        first = True
        for t in ts:
            s = t.text or ""
            ta, tb = pos, pos + len(s)
            pos = tb
            if tb <= a or ta >= b:
                continue
            la, lb = max(a, ta) - ta, min(b, tb) - ta
            if first:
                t.text = s[:la] + new + s[lb:]
                first = False
            else:
                t.text = s[:la] + s[lb:]
            t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        ts = runs_t(p_el)
    return len(ms)


def sub_all(doc, pattern, repl, flags=0):
    n = 0
    for p in doc.element.body.iter(W + 'p'):
        n += sub_in_par(p, pattern, repl, flags)
    return n


def find_par(doc, startswith, nth=0, style=None):
    k = 0
    for p in doc.element.body.iter(W + 'p'):
        if ptext(p).startswith(startswith):
            if style:
                st = p.find(W + 'pPr/' + W + 'pStyle')
                if st is None or st.get(W + 'val') != style:
                    continue
            if k == nth:
                return p
            k += 1
    raise KeyError(startswith)


def set_par(p_el, parts):
    """Reescriu el paràgraf: parts = [(text, bold), ...]; copia el format del primer run normal i del primer run en negreta."""
    runs = p_el.findall(W + 'r')
    base = None; boldr = None
    for r in runs:
        rpr = r.find(W + 'rPr')
        bb = rpr.find(W + 'b') if rpr is not None else None
        isb = bb is not None and bb.get(W + 'val') not in ('0', 'false')
        if isb and boldr is None:
            boldr = r
        if not isb and base is None:
            base = r
    base = base if base is not None else (runs[0] if runs else None)
    for r in list(p_el):
        if r.tag in (W + 'r', W + 'hyperlink'):
            p_el.remove(r)
    for txt, b in parts:
        src = (boldr if (b and boldr is not None) else base)
        if src is not None:
            r = copy.deepcopy(src)
            for x in list(r):
                if x.tag != W + 'rPr':
                    r.remove(x)
        else:
            r = p_el.makeelement(W + 'r', {})
        rpr = r.find(W + 'rPr')
        if b:
            if rpr is None:
                rpr = r.makeelement(W + 'rPr', {}); r.insert(0, rpr)
            for x in rpr.findall(W + 'b') + rpr.findall(W + 'bCs'):
                rpr.remove(x)
            rpr.insert(0, rpr.makeelement(W + 'b', {}))
        if not b and rpr is not None:
            for x in rpr.findall(W + 'b') + rpr.findall(W + 'bCs'):
                rpr.remove(x)
        t = r.makeelement(W + 't', {}); t.text = txt
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        r.append(t)
        p_el.append(r)
    return p_el


def clone_after(p_el, parts, ref=None):
    """Crea un paràgraf nou després de p_el, amb el format de ref (o de p_el)."""
    src = ref if ref is not None else p_el
    new = copy.deepcopy(src)
    set_par(new, parts)
    p_el.addnext(new)
    return new


def remove_col(tbl, col_idx):
    grid = tbl.find(W + 'tblGrid')
    if grid is not None:
        cols = grid.findall(W + 'gridCol')
        if col_idx < len(cols):
            grid.remove(cols[col_idx])
    for tr in tbl.iter(W + 'tr'):
        tcs = tr.findall(W + 'tc')
        if len(tcs) > col_idx:
            tr.remove(tcs[col_idx])


def table_after_par(p_el):
    el = p_el.getnext()
    while el is not None and el.tag != W + 'tbl':
        el = el.getnext()
    return el


def cell_set(tc, parts):
    ps = tc.findall(W + 'p')
    set_par(ps[0], parts)
    for p in ps[1:]:
        tc.remove(p)


def add_row(tbl, values, like=-1):
    trs = tbl.findall(W + 'tr')
    new = copy.deepcopy(trs[like])
    for tc, v in zip(new.findall(W + 'tc'), values):
        cell_set(tc, v if isinstance(v, list) else [(v, False)])
    trs[like].addnext(new) if like != -1 else tbl.append(new)
    return new


# ---------------------------------------------------------------- hiperenllaços
from docx.opc.constants import RELATIONSHIP_TYPE as RT
RNS = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def _style_link_run(r):
    rpr = r.find(W + 'rPr')
    if rpr is None:
        rpr = r.makeelement(W + 'rPr', {}); r.insert(0, rpr)
    for tag in ('color', 'u'):
        for x in rpr.findall(W + tag):
            rpr.remove(x)
    c = rpr.makeelement(W + 'color', {W + 'val': '1F5FA8'}); rpr.append(c)
    u = rpr.makeelement(W + 'u', {W + 'val': 'single'}); rpr.append(u)


def wrap_run_link(doc, r, url):
    rid = doc.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = r.makeelement(W + 'hyperlink', {RNS + 'id': rid, W + 'history': '1'})
    r.addprevious(h); h.append(r)
    _style_link_run(r)
    return h


def link_phrase(doc, p_el, phrase, url):
    """Converteix en enllaç la primera aparició de phrase dins d'un sol run del paràgraf. Retorna True si ho fa."""
    import copy as _c
    for r in p_el.iter(W + 'r'):
        if r.getparent().tag == W + 'hyperlink':
            continue
        t = r.find(W + 't')
        if t is None or not t.text or phrase not in t.text:
            continue
        txt = t.text; i = txt.index(phrase)
        before, mid, after = txt[:i], txt[i:i + len(phrase)], txt[i + len(phrase):]
        rm = _c.deepcopy(r); rm.find(W + 't').text = mid
        rm.find(W + 't').set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        r.addnext(rm)
        if after:
            ra = _c.deepcopy(r); ra.find(W + 't').text = after
            ra.find(W + 't').set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            rm.addnext(ra)
        if before:
            t.text = before; t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        else:
            r.getparent().remove(r)
        wrap_run_link(doc, rm, url)
        return True
    return False
