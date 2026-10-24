"""Canvi de contingut del 24/10/2026: repartiment de CE aprovat (3 CE per SdA).

Només afegeix (no esborra res) i manté tots els uid. Puja la versio de les evidències i dels ítems
que canvien de criteri. Els ítems nous comencen a versio 1. Fonts dels criteris: Decret 175/2022.

  SdA 1 +CE5: lectura Ellen Swallow Richards, ítem nou e2 «Aigua i salut» (5.1).
  SdA 2 +CE2: el laboratori de la corba d'escalfament passa a qualificador (evidència nova s2.labc, 2.3).
  SdA 3 +CE1: activitats 2-4 de la demostració d'assoliment, de 6.1 a 1.1 / 1.2 / 1.2.
  SdA 4 +CE1: activitat 2 (la llana d'acer), 2.2 → 2.2 i 1.2.
  SdA 5 +CE2: laboratori de difusió (fitxa 5) qualificador (evidència nova s5.difu, 2.2 i 2.3).
  SdA 6 +CE1: activitat 2 (sèrie o paral·lel?), 4.2 → 1.2.
Pesos de cada evidència: els de la programació (full.md); a les SdA 2 i 5 es redistribueixen per
fer lloc a l'evidència nova.
Ús (una sola vegada): python3 tools/3r/canvis/20261024_repartiment_ce.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "lib"))
import yamlio

C = os.path.normpath(os.path.join(HERE, "..", "..", "..", "contingut", "3r", "sda"))
PES = {1: {"inf": 40, "prova": 30, "lab": 20, "ellen": 10},
       2: {"video": 35, "expl": 25, "prova": 25, "labc": 15},
       3: {"camp": 35, "prova": 30, "dos": 25, "fit": 10},
       4: {"lab": 40, "prova": 30, "dos": 30},
       5: {"prova": 30, "tfm": 30, "graf": 15, "febre": 10, "difu": 15},
       6: {"pla": 35, "prova": 30, "cerca": 20, "debat": 15}}
META = {1: ("CE2 i CE3", "CE2, CE3 i CE5"), 2: ("CE1 i CE4", "CE1, CE2 i CE4"), 3: ("CE5 i CE6", "CE1, CE5 i CE6"),
        4: ("CE2 i CE3", "CE1, CE2 i CE3"), 5: ("CE1 i CE5", "CE1, CE2 i CE5"), 6: ("CE4 i CE6", "CE1, CE4 i CE6")}


def ev(s, eid): return next(e for e in s["evidencies"] if e["id"] == eid)
def it(e, iid): return next(i for i in e["items"] if i["id"] == iid)
def retag(s, eid, iid, crit):
    e = ev(s, eid); i = it(e, iid)
    if i["criteris"] != crit:
        i["criteris"] = crit; i["versio"] += 1; e["_canvi"] = True


def main():
    for n in range(1, 7):
        p = os.path.join(C, f"sda{n}.yaml"); s, head = yamlio.load(p)
        if s.get("versio", 1) >= 2: print(f"SdA {n}: ja aplicat"); continue
        if n == 1:
            e = ev(s, "ellen")
            e["items"].append({"uid": "s1.ellen.e2", "id": "e2", "versio": 1, "titol": "Aigua i salut", "criteris": ["5.1"],
                "descriptors": {"AE": "Justifica amb arguments científics per què cal controlar la qualitat de l'aigua i relaciona els ions mesurats amb la salut de les persones i del medi",
                                "AN": "Justifica la importància de les normes de qualitat de l'aigua amb algun argument científic",
                                "AS": "Diu que l'aigua ha de ser de qualitat sense justificar-ho",
                                "NA": "No respon o la resposta no té relació amb la qualitat de l'aigua"}})
            e["_canvi"] = True
        if n == 2:
            s["evidencies"].append({"uid": "s2.labc", "id": "labc", "versio": 1, "titol": "Laboratori de la corba d'escalfament i informe de pràctica (sessió 6)",
                "instruments": ["labc", "inf"], "items": [
                {"uid": "s2.labc.k1", "id": "k1", "versio": 1, "titol": "Execució i registre de dades", "criteris": ["2.3"],
                 "descriptors": {"AE": "Mesura la temperatura cada 2 minuts amb el termòmetre ben col·locat, registra totes les dades amb unitats i fa la gràfica temperatura-temps amb escala i eixos correctes",
                                 "AN": "Registra les dades amb unitats i fa la gràfica amb algun error menor d'escala o d'eixos",
                                 "AS": "Registre incomplet o gràfica amb errors d'escala o sense unitats",
                                 "NA": "No registra les dades o no fa la gràfica"}},
                {"uid": "s2.labc.k2", "id": "k2", "versio": 1, "titol": "Interpretació dels resultats", "criteris": ["2.3"],
                 "descriptors": {"AE": "Identifica el tram on la temperatura es manté constant, l'explica amb el model de partícules i compara la predicció amb el resultat",
                                 "AN": "Identifica el tram constant i l'explica amb alguna imprecisió",
                                 "AS": "Descriu la gràfica sense interpretar-la",
                                 "NA": "No interpreta els resultats"}}]})
        if n == 3:
            retag(s, "prova", "p2", ["1.1"]); retag(s, "prova", "p3", ["1.2"]); retag(s, "prova", "p4", ["1.2"])
        if n == 4:
            retag(s, "prova", "p2", ["2.2", "1.2"])
        if n == 5:
            s["evidencies"].append({"uid": "s5.difu", "id": "difu", "versio": 1, "titol": "Laboratori de difusió (fitxa 5, sessió 7)",
                "instruments": ["d5f5"], "items": [
                {"uid": "s5.difu.x1", "id": "x1", "versio": 1, "titol": "Disseny de l'experiment", "criteris": ["2.2"],
                 "descriptors": {"AE": "Formula una pregunta i una hipòtesi contrastables, identifica la variable independent, la dependent i les controlades i escriu un procediment on només varia la temperatura",
                                 "AN": "Identifica les variables i escriu un procediment amb algun control que falta",
                                 "AS": "Procediment incomplet o variables confoses",
                                 "NA": "No dissenya l'experiment"}},
                {"uid": "s5.difu.x2", "id": "x2", "versio": 1, "titol": "Conclusions i límits", "criteris": ["2.3"],
                 "descriptors": {"AE": "Treu una conclusió coherent amb les dades, diu si es confirma la hipòtesi i proposa una millora tenint en compte els límits (la tinta també cau per gravetat)",
                                 "AN": "Treu una conclusió coherent i diu si es confirma la hipòtesi",
                                 "AS": "Conclusió poc relacionada amb les dades",
                                 "NA": "Sense conclusió"}}]})
        if n == 6:
            retag(s, "prova", "p2", ["1.2"])
        for e in s["evidencies"]:
            if e.pop("_canvi", False): e["versio"] += 1
            e["pes"] = PES[n][e["id"]]
        assert sum(PES[n].values()) == 100 and set(PES[n]) == {e["id"] for e in s["evidencies"]}
        a, b = META[n]; assert a in s["meta"], (n, s["meta"]); s["meta"] = s["meta"].replace(a, b)
        s["versio"] = 2
        yamlio.save(p, s, head); print(f"SdA {n}: fet")


if __name__ == "__main__":
    main()
