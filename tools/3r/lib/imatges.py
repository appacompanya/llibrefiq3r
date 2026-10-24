"""Imatges de 3r: una sola còpia de cada imatge, a la carpeta img/ de l'arrel del web.

L'identificador d'una imatge és el seu camí dins de img/ (p. ex. «sda2-s3.png», «ghs/ghs03.png»).
- El web (index.html, digital/, profe) l'enllaça com a img/<id> o ../img/<id>.
- Els generadors de PDF la demanen amb imatges.uri(id) o imatges.DIR: mai no en fan còpies.
- tools/3r/artefactes.py registra el hash de cada imatge que fa servir cada PDF: si canvies una imatge,
  --check diu CAL REGENERAR per a tots els PDF i annexos que la contenen.
Per substituir una imatge: sobreescriu img/<id> amb el mateix nom i executa artefactes.py --check."""
import hashlib, os, re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DIR = os.path.join(ROOT, "img")
EXT = (".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif")


def path(id_):
    p = os.path.join(DIR, id_)
    if not os.path.exists(p):
        raise FileNotFoundError(f"La imatge «{id_}» no és a img/")
    return p


def uri(id_):
    return "file://" + path(id_)


def totes():
    out = []
    for d, _, fs in os.walk(DIR):
        for f in fs:
            if f.lower().endswith(EXT):
                out.append(os.path.relpath(os.path.join(d, f), DIR).replace(os.sep, "/"))
    return sorted(out)


def hash_(id_):
    return hashlib.sha256(open(path(id_), "rb").read()).hexdigest()[:16]


_LIT = re.compile(r"[\w{}:.\-/]*\.(?:png|jpe?g|webp|svg|gif)", re.I)


def usades_per(text, ids=None):
    """Imatges (ids) que un codi font o un HTML pot fer servir: noms literals i plantilles f-string («sda2-s{n}.png»)."""
    ids = ids or totes()
    out = set()
    for lit in set(_LIT.findall(text)):
        pat = re.escape(lit.split("/")[-1])
        pat = re.sub(r"\\\{[^}]*\\\}", ".+?", pat)
        rx = re.compile("^" + pat + "$")
        out |= {i for i in ids if rx.match(i.split("/")[-1])}
    # ghs: GHS(c) → ghs/ghsNN.png
    if "GHS(" in text or "ghs{" in text:
        out |= {i for i in ids if i.startswith("ghs/")}
    return sorted(out)


US = os.path.join(ROOT, "contingut", "3r", "generat", "imatges-us.json")


def ids_en_html(html):
    pre = "file://" + DIR + "/"
    ids = set(totes())
    return sorted({u for u in re.findall(re.escape(pre) + r"([^\"')\s]+)", html) if u in ids})


def registra_us(pdf, html):
    """El criden els generadors en renderitzar cada PDF: desa quines imatges conté (font exacta per a artefactes.py)."""
    import json
    d = json.load(open(US)) if os.path.exists(US) else {}
    d[os.path.basename(pdf)] = ids_en_html(html)
    json.dump(d, open(US, "w"), ensure_ascii=False, indent=1, sort_keys=True)
