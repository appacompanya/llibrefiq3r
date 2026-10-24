"""Lectura de la font única (contingut/3r) per als generadors de PDF.

Els generadors no escriuen mai a mà els criteris d'una rúbrica o d'una activitat de demostració
d'assoliment: els demanen aquí, perquè si canvia el YAML el PDF canviï igual.

  etiq(1, "inf", "i1")    → "Hipòtesis (2.1)"            (fila d'una rúbrica)
  pts(3, "prova", "p2")   → "<span class='pts'> (criteri 1.1)</span>"
  crit(4, "prova", "p2")  → ["2.2", "1.2"]

La carpeta de contingut es busca a $FQ3_CONTINGUT, o pujant des d'aquest fitxer i des del directori actual.
"""
import os, functools
import yaml


def _arrel():
    if os.environ.get("FQ3_CONTINGUT"):
        return os.environ["FQ3_CONTINGUT"]
    for base in (os.path.dirname(os.path.abspath(__file__)), os.getcwd()):
        d = base
        while d != os.path.dirname(d):
            c = os.path.join(d, "contingut", "3r")
            if os.path.exists(os.path.join(c, "curriculum.yaml")):
                return c
            d = os.path.dirname(d)
    raise SystemExit("fq3dades: no trobo contingut/3r (defineix FQ3_CONTINGUT)")


@functools.lru_cache(None)
def sda(n):
    return yaml.safe_load(open(os.path.join(_arrel(), "sda", f"sda{n}.yaml"), encoding="utf-8"))


USATS = set()


def item(n, evid, it):
    for e in sda(n)["evidencies"]:
        if e["id"] == evid:
            for i in e["items"]:
                if i["id"] == it:
                    USATS.add(i["uid"])
                    return i
    raise KeyError(f"s{n}.{evid}.{it} no és a contingut/3r/sda/sda{n}.yaml")


def crit(n, evid, it):
    return list(item(n, evid, it)["criteris"])


def llista(cs):
    return cs[0] if len(cs) == 1 else ", ".join(cs[:-1]) + " i " + cs[-1]


def etiq(n, evid, it, titol=None):
    i = item(n, evid, it)
    return f"{titol or i['titol']} ({llista(i['criteris'])})"


def pts(n, evid, it):
    cs = crit(n, evid, it)
    return f"<span class='pts'> ({'criteri' if len(cs) == 1 else 'criteris'} {llista(cs)})</span>"


def no_usats(n, evids):
    """Ítems qualificadors del YAML que el generador no ha fet servir (per avisar)."""
    return [i["uid"] for e in sda(n)["evidencies"] if e["id"] in evids for i in e["items"] if i["uid"] not in USATS]
