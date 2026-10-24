"""Annexos nous de la programació: llibre digital, calendari, tipus d'activitats, atenció a la diversitat i auto/coavaluació.
Format de les bases: Arial 11 al text, taules a 9 punts. Sortida: annex/annex-extra.pdf (i una pàgina PNG per annex)."""
import os
from playwright.sync_api import sync_playwright
H = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(H, "annex")
f = lambda p: "file://" + os.path.join(A, p)

CSS = """@page{size:A4;margin:14mm 16mm 13mm}*{box-sizing:border-box}
body{font-family:Arial,"Liberation Sans",Helvetica,sans-serif;font-size:11pt;line-height:1.5;color:#1f2328;margin:0}
h1{font-size:14pt;line-height:1.25;margin:0 0 1mm}.an{font-size:9pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#5d646d}
p{margin:1.2mm 0}.pb{break-after:page}a{color:#1F5FA8}
table{width:100%;border-collapse:collapse;font-size:9pt;line-height:1.25;margin:2mm 0}th,td{border:.6pt solid #c9ccd1;padding:1.2mm 1.8mm;vertical-align:top;text-align:left}th{background:#eef0f2}
table.fig td{border:none;padding:1mm 1.5mm 2mm}table.fig img{width:100%;height:46mm;object-fit:cover;object-position:top;border:.6pt solid #c9ccd1;border-radius:1.5mm;display:block;margin-bottom:1mm}
.th{width:24mm;border:.6pt solid #c9ccd1}.small{font-size:11pt;color:#5d646d}td .small{font-size:9pt}
"""

def head(n, title, sub=""):
    return f'<div class="an">Annex {n}</div><h1>{title}</h1>' + (f'<p class="small">{sub}</p>' if sub else "")

def llibre(n):
    B = "https://llibrefiq3r.cat/"
    shots = [
        ("02-sda5.png", "Pàgina d'una SdA: repte, competències i, sessió a sessió, què farem, la il·lustració i els fulls i recursos.", B + "#sda5"),
        ("05-fitxa-factors.png", "<b>Fitxa digital de factors de conversió (SdA 1).</b> L'alumne escriu cada factor com una fracció i el llibre simplifica les unitats i calcula el resultat. Funciona com a <b>bastida</b>: fa visible que un factor de conversió és una fracció que val 1 i que les unitats es cancel·len, fins que l'alumne ho fa sol en paper.", B + "digital/#fitxa-d1f2"),
        ("06-tfm-cel.png", "Laboratori virtual de forces de tracció (SdA 5): alinear les làmines, mesurar el desplaçament de cada boleta i calcular F = k·Δx.", B + "digital/#fitxa-d5tfm"),
        ("10-registre-c.png", "Zona del professorat: registre per criteris (NA, AS, AN, AE), nivell de cada competència i seguiment de les recuperacions.", B + "digital/profe.html"),
    ]
    cells = [f'<td style="width:50%"><a href="{u}"><img src="{f("shots/" + s)}"></a>{c} <a href="{u}">Obre-ho</a></td>' for s, c, u in shots]
    t = "".join(f"<tr>{cells[i]}{cells[i+1]}</tr>" for i in (0, 2))
    por = (f'<table class="fig"><tr><td style="width:56%"><a href="{B}"><img src="{f("shots/01-portada-full.png")}" style="height:auto;object-fit:contain"></a></td>'
           f'<td style="vertical-align:middle"><b>Portada del llibre de l\'alumnat</b> (<a href="{B}">llibrefiq3r.cat</a>): els sis reptes del curs, cadascun amb la il·lustració i el color de la seva SdA. Des de cada repte s\'obren les sessions i els fulls.<br><br>'
           f'Altres recursos: <a href="{B}sim-gasos.html">simulador del model cineticomolecular</a>, <a href="{B}sim-bateria.html">simulador de la bateria de liti</a> i <a href="{B}digital/">llibre digital</a> (fitxes en línia amb correcció automàtica).</td></tr></table>')
    return (head(n, "El llibre digital com a recurs didàctic", "La majoria de sessions es fan en paper; el llibre digital es fa servir quan convé rebre les respostes automàticament i per a les simulacions.")
            + por + f'<table class="fig">{t}</table>')

def calendari(n):
    return (head(n, "Calendari del curs i distribució de les SdA", "Cada SdA té el seu color. To clar: sessió desdoblada (dilluns i dimecres, el professor la fa amb cada meitat del grup). Color ple: sessió de grup sencer (dijous).")
            + f'<img src="{f("calendari.png")}" style="width:100%;border:.6pt solid #c9ccd1">')

TIPUS = [
    ("Inicial (exploració)", "sda2-02-full-del-repte.png", "Full del repte, part A (SdA 2, sessió 1)", "L'alumnat llegeix l'etiqueta del desodorant, dibuixa com s'imagina el gas de la llauna freda i calenta i escriu la seva explicació inicial. Fa aflorar les idees prèvies i planteja el repte."),
    ("Desenvolupament (introducció de nous coneixements)", "sda2-03-laboratori-globus.png", "Laboratori dels globus al fred i a la calor (sessió 2)", "Mesuren el perímetre de dos globus, calculen el volum i en comparen la variació. Les dades obren la necessitat d'un model que les expliqui."),
    ("Estructuració (síntesi)", "sda2-04-fitxa-1-model-cineticomolecular.png", "Fitxa 1 · El model cineticomolecular i mapa conceptual (sessions 3 i 7)", "Formalitzen els postulats del model, el fan servir per explicar el globus del congelador i organitzen els conceptes al mapa conceptual."),
    ("Aplicació (transferència)", "sda2-08-guio-del-video.png", "Guió del vídeo per a 1r d'ESO (sessions 7 i 8)", "Apliquen el model a un fenomen quotidià nou i l'expliquen a l'alumnat de 1r: producte final de la SdA."),
    ("Avaluació i regulació", "sda2-12-diana-autoavaluacio.png", "Diana d'autoavaluació i activitat de demostració d'assoliment (sessions 9 i 10)", "Demostren individualment l'assoliment dels criteris en situacions noves, esmenen amb bolígraf verd i valoren el seu progrés amb la diana."),
]

def tipus(n):
    K = ["repte", "lab", "f1", "video", "diana"]
    rows = "".join(f'<tr><td style="width:24%"><b>{t}</b></td><td style="width:27mm"><a href="https://llibrefiq3r.cat/#doc-{k}"><img class="th" src="{f("thumbs/" + im)}"></a></td><td><b><a href="https://llibrefiq3r.cat/#doc-{k}">{nom}</a></b><br>{d}</td></tr>' for (t, im, nom, d), k in zip(TIPUS, K))
    return (head(n, "Tipus d'activitats: un exemple de cada fase", "Exemples de la SdA 2 · El desodorant kamikaze. Totes les SdA segueixen el mateix cicle d'aprenentatge.")
            + f'<table><tr><th>Fase</th><th>Full</th><th>Activitat i finalitat</th></tr>{rows}</table>'
            + '<p class="small">Metodologia 1-2-4 a les fitxes: primer cada alumne la fa individualment (1), després la contrasta i la corregeix amb el company o companya (2) i finalment el grup de quatre posa en comú els dubtes i les respostes (4) abans de la correcció amb el solucionari.</p>')

NESE = [
    ("Dislèxia", "sda1-20-adaptada-dislexia-fitxa-1.png", "Fitxa 1 de la SdA 1 (unitats i notació científica)",
     "Lletra gran i sense serifes, interlineat ampli i fons crema; exemples resolts; menys ítems per pàgina; enunciats curts; lectura en veu alta al llibre digital; temps addicional i possibilitat de respondre oralment una part de l'activitat de demostració."),
    ("Alumnat nouvingut", "sda2-17-adaptada-nouvingut-glossari-visual.png", "Glossari visual i fitxa 1 de la SdA 2",
     "Glossari visual amb columna per a la llengua familiar; traducció del vocabulari clau i diccionari (també digital); company o companya de suport al costat; frases model i banc de paraules; coordinació amb l'aula d'acollida."),
    ("TDAH", "sda5-22-adaptada-tdah-problemes-de-moviment.png", "Problemes de moviment de la SdA 5",
     "Un problema per targeta amb temps orientatiu; llista de comprovació per passos; barra de progrés i pausa activa pactada; ubicació a prop del professor; lliurament per parts."),
    ("TEA", "sda6-16-adaptada-tea-guio-del-debat.png", "Guió anticipat del debat de la SdA 6",
     "Anticipació de l'horari i del rol; normes explícites; frases model per intervenir; targeta de pausa; avís previ de qualsevol canvi; treball en grup amb rols clars."),
    ("Altes capacitats", "sda3-18-ampliacio.png", "Dossier d'ampliació de la SdA 3",
     "Reptes d'ampliació en profunditat (no avançament de temari) per a quan acaben la feina: càlculs, problemes de Fermi, dades reals i disseny; també rol d'expert o de mentor en el grup."),
    ("Retard en l'aprenentatge (continguts bàsics)", "sda2-18-adaptada-continguts-basics-fitxa-1.png", "Fitxa 1 de la SdA 2 amb continguts bàsics",
     "Continguts reduïts als essencials amb el mateix criteri; banc de paraules, frases per completar, respostes de selecció i dibuixos model; company de suport; objectiu d'arribar a AS i passar a la fitxa ordinària. La primera pàgina es reprodueix sencera a l'annex 15."),
]

def nese(n):
    K = ["d1adap", "d2adap", "d5adap", "d6adap", "d3amp", "d2bas"]
    cards = "".join(f'<tr><td style="width:23mm;padding:1mm"><a href="https://llibrefiq3r.cat/digital/profe.html#doc-{k}"><img class="th" style="width:20mm" src="{f("thumbs/" + im)}"></a></td><td><b>{t}</b> · <a href="https://llibrefiq3r.cat/digital/profe.html#doc-{k}">{doc}</a><br>{m}</td></tr>' for (t, im, doc, m), k in zip(NESE, K))
    return (head(n, "Atenció a la diversitat: un exemple d'adaptació per perfil", "El grup-classe inclou alumnat amb dislèxia, nouvingut, amb TDAH, amb TEA, d'altes capacitats i amb retard en l'aprenentatge. Cada perfil té un exemple de fitxa adaptada al llibre del professorat.")
            + f'<table><tr><th>Full</th><th>Perfil, exemple i mesures</th></tr>{cards}</table>'
            + '<p class="small" style="margin-top:1mm">Totes les adaptacions mantenen els sabers i els criteris d\'avaluació de la fitxa ordinària i s\'avaluen amb els mateixos nivells d\'assoliment. A més, els grups de treball són heterogenis i el llibre digital ofereix lectura en veu alta, ampliació del text i correcció immediata per a tothom (mesures universals, DUA).</p>')

def coav(n):
    rows = [
        ("M'avaluo", "Autoavaluació", "Cada alumne valora la seva feina amb la rúbrica: diana de cada SdA, esmena amb bolígraf verd i autoavaluació del vídeo.", "«He entès el fenomen i el sé explicar amb el model de partícules»: AE · AN · AS · NA"),
        ("T'avaluo", "Coavaluació entre iguals", "Un company o companya valora la feina de l'altre amb respecte, amb un punt fort i una proposta de millora (assignació circular).", "«Ha complert el seu rol»: AE · AN · AS · NA + punt fort i proposta"),
        ("Ens avaluem", "Avaluació del grup", "El grup valora el seu procés: organització, participació equilibrada i qualitat del producte.", "«Tothom ha participat de manera equilibrada»: AE · AN · AS · NA"),
        ("Us avaluem", "Avaluació d'un altre grup", "Cada grup avalua el vídeo d'un altre grup amb la mateixa rúbrica que fa servir el professor.", "«Explicació científica (criteri 1.2)»: AE · AN · AS · NA"),
    ]
    t = "".join(f"<tr><td><b>{a}</b><br><span class='small'>{b}</span></td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)
    return (head(n, "Autoavaluació i coavaluació: un exemple de cada tipus", "Exemple de la sessió 10 de la SdA 2 (full «Avaluem els vídeos»). Les quatre valoracions són formatives i complementen la del professor.")
            + f'<table><tr><th style="width:22%">Tipus</th><th>Com es fa</th><th style="width:34%">Exemple d\'ítem</th></tr>{t}</table>'
            + f'<table class="fig"><tr><td style="width:50%"><a href="https://llibrefiq3r.cat/#doc-d2coav"><img src="{f("thumbs/sda2-19-avaluem-els-videos.png")}" style="height:62mm"></a>Full «Avaluem els vídeos» (pàgina 1).</td>'
            + f'<td><a href="https://llibrefiq3r.cat/#doc-diana"><img src="{f("thumbs/sda2-12-diana-autoavaluacio.png")}" style="height:62mm"></a>Diana d\'autoavaluació de la SdA 2.</td></tr></table>'
            + '<p class="small">Mètode 1-2-4: individualment (1), per parelles (2) i en grup de quatre (4). Les dades de les coavaluacions no es converteixen en nota: serveixen perquè l\'alumnat s\'apropiï dels criteris i aprengui a donar i rebre retorn.</p>')

PARTS = [("llibre", llibre), ("tipus", tipus), ("diversitat", nese), ("coavaluacio", coav)]

def build(start=12):
    NUMS = [12, 13, 14, 16]
    body = '<div class="pb"></div>'.join(fn(NUMS[i]) for i, (_, fn) in enumerate(PARTS))
    html = f'<!doctype html><html lang="ca"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
    p = os.path.join(A, "annex-extra.html"); open(p, "w", encoding="utf-8").write(html)
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page()
        pg.goto("file://" + p); pg.wait_for_timeout(800)
        pg.pdf(path=os.path.join(A, "annex-extra.pdf"), format="A4", print_background=True)
        br.close()
    print("ok")

if __name__ == "__main__":
    import sys
    build(int(sys.argv[1]) if len(sys.argv) > 1 else 12)
