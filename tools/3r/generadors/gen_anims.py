#!/usr/bin/env python3
"""Genera les animacions pas a pas (sim-*.html) a partir de anims/_shell.html i anims/<nom>.js."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "anims")
SW = lambda c, t: f'<span><i class="sw" style="background:{c}"></i>{t}</span>'
SWS = lambda c, sg, t: f'<span><i class="sw" style="background:{c};width:16px;height:16px;color:#fff;font:800 12px/14px system-ui;text-align:center;font-style:normal">{sg}</i>{t}</span>'

ANIMS = {
    "ajust": dict(
        title="Ajust d'equacions químiques",
        eyebrow="Física i química · 3r ESO · SdA 4 · Un cotxe que només allibera aigua?",
        h1="Com s'ajusta una equació química",
        lead="Animació pas a pas amb models de boles: comptem els àtoms de cada element i ajustem l'equació canviant només els coeficients.",
        legend=SW("#ffffff", "hidrogen (H)") + SW("#ee5a4e", "oxigen (O)") + SW("#5b616b", "carboni (C)")),
    "enllac": dict(
        title="L'enllaç químic",
        eyebrow="Física i química · 3r ESO · SdA 3 · Què hi ha dins del meu mòbil?",
        h1="Enllaç iònic, covalent i metàl·lic",
        lead="Animació pas a pas: què fan els electrons de la capa externa quan els àtoms s'uneixen.",
        legend=SW("#2f6db5", "electró de la capa externa") + SW("#9aa3ad", "electró de capes internes") + "<span>Model de capes simplificat (no està a escala).</span>"),
    "colisions": dict(
        title="Teoria de col·lisions",
        eyebrow="Física i química · 3r ESO · SdA 4 · Un cotxe que només allibera aigua?",
        h1="La teoria de col·lisions i la velocitat de reacció",
        lead="Animació pas a pas: per què la temperatura, la concentració i la superfície de contacte canvien la velocitat d'una reacció.",
        legend=SW("#2f6db5", "partícula de reactiu A") + SW("#e08a2c", "partícula de reactiu B") + SW("#2e9d5b", "producte") + "<span>Estrella groga: xoc A–B eficaç. Cercle gris: xoc A–B que rebota.</span>"),
    "pila": dict(
        title="La pila de combustible",
        eyebrow="Física i química · 3r ESO · SdA 4 · Un cotxe que només allibera aigua?",
        h1="Com funciona una pila de combustible d'hidrogen",
        lead="Animació pas a pas: com el bus d'hidrogen obté electricitat a partir de l'hidrogen i l'oxigen de l'aire.",
        legend=SW("#ffffff", "hidrogen") + SW("#ee5a4e", "oxigen") + SWS("#b44fd6", "+", "ió H⁺") + SWS("#2f6db5", "−", "electró e⁻")),
    "mrua": dict(
        title="MRU i MRUA amb gràfiques",
        eyebrow="Física i química · 3r ESO · SdA 5 · Cèl·lules immunitàries a la caça dels patògens",
        h1="El moviment i la seva gràfica velocitat–temps",
        lead="Animació pas a pas: el patinet es mou i, alhora, es dibuixen les gràfiques velocitat–temps i posició–temps.",
        legend=SW("var(--acc)", "moviment actual") + SW("#9aa3ad", "moviment anterior, per comparar") + "<span>Els punts marquen la posició cada segon.</span>"),
}

def build(name):
    sh = open(os.path.join(A, "_shell.html"), encoding="utf-8").read()
    js = open(os.path.join(A, name + ".js"), encoding="utf-8").read()
    m = ANIMS[name]
    out = (sh.replace("__TITLE__", m["title"]).replace("__EYEBROW__", m["eyebrow"]).replace("__H1__", m["h1"])
             .replace("__LEAD__", m["lead"]).replace("__LEGEND__", m["legend"]).replace("__SIM__", js))
    p = os.path.join(HERE, f"sim-{name}.html")
    open(p, "w", encoding="utf-8").write(out)
    return p

if __name__ == "__main__":
    import sys
    names = sys.argv[1:] or [n for n in ANIMS if os.path.exists(os.path.join(A, n + ".js"))]
    for n in names:
        if n in ANIMS: print(build(n))

LABS = {
    "lab-mru": dict(mode="mru", title="Laboratori del MRU",
        h1="Laboratori: el moviment uniforme (MRU)",
        lead="Tria la posició inicial i la velocitat del patinet, prem «Inicia» i observa com canvien la posició i el temps, alhora, a la pista, a les gràfiques i a la taula.",
        qs=["Posa x₀ = 0 i v = 2 m/s. On és el patinet als 10 s? I si dupliques la velocitat?",
            "Desa el moviment i canvia només x₀. Què canvia a la gràfica posició–temps? I a la de velocitat–temps?",
            "Posa una velocitat negativa. Cap a on va el patinet? Com és el pendent de la gràfica posició–temps?",
            "A la taula, quants metres avança el patinet cada segon? Relaciona-ho amb la velocitat."]),
    "lab-mrua": dict(mode="mrua", title="Laboratori del MRUA",
        h1="Laboratori: el moviment accelerat (MRUA)",
        lead="Tria la posició inicial, la velocitat inicial i l'acceleració del patinet, prem «Inicia» i observa com canvien la posició i la velocitat al llarg del temps.",
        qs=["Amb x₀ = 0 i v₀ = 0, compara a = 1 m/s² i a = 2 m/s² (desa el primer). Quina distància fa cada un en 4 s? És el doble?",
            "A la taula, quant augmenta la velocitat cada segon? I la distància que recorre cada segon, és sempre la mateixa?",
            "Posa v₀ = 8 m/s i a = −2 m/s². Quan s'atura el patinet? A quina posició? Comprova-ho amb les equacions.",
            "Què representa el pendent de la gràfica velocitat–temps? I per què la gràfica posició–temps és una corba?"]),
}

def build_lab(name):
    sh = open(os.path.join(A, "_lab_moviment.html"), encoding="utf-8").read()
    m = LABS[name]
    out = (sh.replace("__TITLE__", m["title"]).replace("__H1__", m["h1"]).replace("__LEAD__", m["lead"])
             .replace("__MODE__", m["mode"]).replace("__QS__", "".join(f"<li>{q}</li>" for q in m["qs"])))
    p = os.path.join(HERE, f"sim-{name}.html")
    open(p, "w", encoding="utf-8").write(out)
    return p

if __name__ == "__main__":
    import sys
    for n in (sys.argv[1:] or list(LABS)):
        if n in LABS: print(build_lab(n))
