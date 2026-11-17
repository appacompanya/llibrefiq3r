"""Peces compartides: fórmules, figures i el motlle d'una solució."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fmt import fmt
from mathhtml import M, EQ
from esquemes import dibuixa
from motor import calcular


def figura(nom, peu, **kw):
    svg = dibuixa(nom, **kw)
    return f'<figure>{svg}<figcaption><b>FIGURA</b> {peu}</figcaption></figure>'


def solucio(plantejament, equacio, calcul, resultat):
    """equacio i calcul poden contenir blocs (fórmules centrades), per això no van dins d’un sol paràgraf."""
    return (
        f'<p><span class="pp">Plantejament</span> {plantejament}</p>'
        f'<p><span class="pp">Equació</span></p>{equacio}'
        f'<p><span class="pp">Càlcul</span></p>{calcul}'
        f'<p><span class="pp">Resultat</span> {resultat}</p>'
    )


def valor(x, d, unitat):
    return f"<b>{fmt(x, d)} {unitat}</b>"


def igual(lhs, mig, resultat, d, unitat, sup=""):
    """Línia de càlcul amb la substitució i les unitats: lhs = dades = resultat."""
    uni = rf"\,\mathrm{{{unitat}}}"
    if sup:
        uni += "^{" + sup + "}"
    return EQ(f"{lhs} = {mig} = {fmt(resultat, d)}{uni}")


def gtex():
    return r"9,8\,\mathrm{m/s}^2"


def calc(tipus, params):
    return calcular(tipus, params)
