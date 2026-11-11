"""Segmenta els exàmens i les pautes de la PAU d'anglès en sèries i blocs (listening, reading, writing)."""
import re
import pymupdf as fitz

PART = [  # (regex, bloc)
    (re.compile(r"listening\s+comprehension", re.I), "listening"),
    (re.compile(r"reading\s+comprehension", re.I), "reading"),
    (re.compile(r"^\s*(part\s*\d\s*:\s*|[IVX]+\.\s*)?(writing|redacci[oó])\b", re.I | re.M), "writing"),
]
COVER = re.compile(r"Comprensi[oó] oral|Comprensi[oó] escrita", re.I)


def page_texts(path):
    d = fitz.open(path)
    return d, [p.get_text() for p in d]


def head_part(t, key=False):
    """Bloc que comença en aquesta pàgina (mirant les primeres línies amb text de capçalera)."""
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    for l in lines[:14]:
        if key:
            m = re.match(r"^(?:Part\s*\d\s*:\s*|[IVX]+\s*[.:]\s*)?(Listening|Reading|Writing)\b", l, re.I)
        else:
            m = re.match(r"^Part\s*\d\s*:\s*(Listening|Reading|Writing)\b", l, re.I)
        if m:
            return m.group(1).lower()
    return None


def is_cover(t):
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    if not head_part(t) and re.search(r"Espai per etiquetes|Ubicaci[oó] del tribunal|Etiqueta de l.(alumne|estudiant)", t) and re.search(r"S[èe]rie\s*\d", t):
        return True
    return sum(1 for l in lines if re.fullmatch(r"Comprensi[oó] (oral|escrita)|Redacci[oó]|Expressi[oó] escrita", l)) >= 2 and not head_part(t)


def blank(t):
    t = re.sub(r"(Nota de .*|Etiqueta.*|\d+|L’Institut d’Estudis Catalans.*|Writing score|Reading comprehension score)", "", t)
    return len(re.sub(r"\W", "", t)) < 40


def exam_series(path):
    """[{'pages': {bloc: [i,...]}}, ...] per a cada sèrie de l'examen (índexs 0-based)."""
    d, T = page_texts(path)
    series, cur, bloc, pending = [], None, None, []
    for i, t in enumerate(T):
        hp = head_part(t)
        if is_cover(t):
            m = re.search(r"S[èe]rie\s*(\d+)", t)
            cur = {"pages": {}, "cover": i, "serie": int(m.group(1)) if m else None}; series.append(cur); bloc = None; pending = []
            continue
        if cur is None:
            cur = {"pages": {}, "cover": None, "serie": None}; series.append(cur)
        if hp:
            if hp in cur["pages"] and hp != bloc:  # sèrie nova sense portada
                cur = {"pages": {}, "cover": None, "serie": None}; series.append(cur)
            bloc = hp
            cur["pages"].setdefault(bloc, []).extend(pending); pending = []
        if blank(t):
            continue
        if bloc is None:
            pending.append(i)  # text de lectura abans de la capçalera de la part
        else:
            cur["pages"].setdefault(bloc, []).append(i)
    for s in series:
        s["listening_title"] = listening_title(T, s["pages"].get("listening", []))
    return d, T, [s for s in series if s["pages"]]


HEAD = [
    ("listening", re.compile(r"^(?:Part\s*\d\s*:\s*|[IVX]+\s*[.:]\s*)?(?:Listening\s+comprehension|Comprensi[oó]\s+(?:oral|aud\w*|d.un\s+text\s+oral)|Prova\s+auditiva)\b", re.I)),
    ("reading", re.compile(r"^(?:Part\s*\d\s*:\s*|[IVX]+\s*[.:]\s*)?(?:Reading\s+comprehension|Comprensi[oó]\s+(?:escrita|lectora)|Prova\s+escrita)\b", re.I)),
    ("writing", re.compile(r"^(?:Part\s*\d\s*:\s*|[IVX]+\s*[.:]\s*)?(?:Writing|Redacci[oó]|Expressi[oó]\s+escrita)\s*(?:\(.*\))?\s*$", re.I)),
]
SERIE = re.compile(r"^S[ÈE]RIE\s*(\d+)", re.I)


def key_series(path):
    """Pautes: llista de sèries, cada una amb les pàgines de cada bloc. Una pàgina on canvia de bloc va als dos blocs."""
    d, T = page_texts(path)
    series, cur, bloc = [], None, None

    def new(n=None):
        s = {"pages": {}, "serie": n}; series.append(s); return s
    for i, t in enumerate(T):
        if blank(t):
            continue
        events = []
        for l in (x.strip() for x in t.splitlines()):
            m = SERIE.match(l)
            if m:
                events.append(("serie", int(m.group(1))))
                continue
            for b, rx in HEAD:
                if rx.match(l):
                    events.append(("bloc", b)); break
        if cur is not None and bloc:
            cur["pages"].setdefault(bloc, []).append(i)
        for kind, v in events:
            if kind == "serie":
                if cur is None or cur["pages"] or cur["serie"] is not None:
                    if cur is not None and bloc and cur["pages"].get(bloc, [None])[-1] == i and not any(e[0] == "bloc" for e in events[:events.index((kind, v))]):
                        cur["pages"][bloc].pop()
                        if not cur["pages"][bloc]: del cur["pages"][bloc]
                    cur = new(v); bloc = None
                else:
                    cur["serie"] = v
            else:
                if cur is None or (v == "listening" and v in cur["pages"] and bloc != v) or (v in cur["pages"] and v != bloc and cur["pages"].get(v, [None])[-1] != i and v != "listening" and bloc == "listening" and "reading" in cur["pages"] and "listening" in cur["pages"] and list(cur["pages"]).index("listening") > 0 and False):
                    cur = new(); 
                if v != bloc or cur["pages"].get(v, [None])[-1] != i:
                    if cur["pages"].get(v, [None])[-1] != i:
                        cur["pages"].setdefault(v, []).append(i)
                bloc = v
    for s in series:
        s["pages"] = {b: sorted(set(v)) for b, v in s["pages"].items() if v}
        s["listening_title"] = listening_title(T, s["pages"].get("listening", []), key=True)
    return d, T, [s for s in series if s["pages"]]


def listening_title(T, pages, key=False):
    if not pages:
        return None
    rx = HEAD[0][1] if key else re.compile(r"^Part\s*\d\s*:\s*Listening", re.I)
    lines = [l.strip() for p in pages[:2] for l in T[p].splitlines() if l.strip()]
    for j, l in enumerate(lines):
        if rx.match(l):
            for k in lines[j + 1:j + 4]:
                k2 = re.sub(r"\(.*?\)", "", k).strip()
                if len(k2) > 3 and not re.match(r"(In the|In this|Now|Read|\[|Choose|Anglès|Pàgina)", k2, re.I):
                    return k2
    return None
