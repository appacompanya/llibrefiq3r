"""Fitxa resum d'una pàgina de cada SdA per als annexos (format de les bases: text 11 pt, taules 9 pt)."""
import sys, re
import gen_sda1 as G
from mn_common import use

sys.path.insert(0, "/tmp/claude-0/-home-claude/ab93dd98-bb64-5312-88e5-d8a23c91bc1c/scratchpad/prog2")
import sda_a, sda_b
import gen_annexos as GA

PROVA = "Activitat de demostració d'assoliment individual i esmena amb bolígraf verd."
DESC = {
    "Informe del grup i protocol": "Assignació justificada dels dotze pots i protocol d'identificació.",
    "Laboratori i seguretat": "Fulls de laboratori (s4–s6) i compliment de les normes de seguretat del decàleg (s1).",
    "Lectura sobre Ellen Swallow Richards": "Lectura en anglès amb preguntes de comprensió.",
    "Vídeo per a 1r d'ESO": "Fenomen quotidià explicat amb el model de partícules.",
    "Explicació final del repte": "Per què explota el desodorant, amb el model i les lleis dels gasos.",
    "Campanya i punt de recollida": "Campanya del grup per recollir mòbils i bateries a l'institut.",
    "Dossier sobre incendis i matèries primeres crítiques": "Anàlisi de fonts: incendis de bateries i matèries primeres crítiques.",
    "Fitxa d'evolució dels models atòmics": "De Dalton a Bohr: què explica cada model i per què canvia.",
    "Fulls de laboratori (sessions 2 i 6)": "Conservació de la massa i electròlisi: dades, càlculs i conclusió.",
    "Dossier i resposta del grup": "Resposta argumentada del grup sobre l'hidrogen verd.",
    "Full de forces cel·lulars": "Anàlisi de dues làmines de microscòpia de forces de tracció.",
    "Gràfiques del patinet (fitxa 3)": "Gràfiques posició–temps i velocitat–temps d'un patinet.",
    "La febre i la migració (fitxa 6)": "Efecte de la temperatura en el moviment dels neutròfils.",
    "Pla d'estalvi": "Mesures d'estalvi per a l'institut amb el càlcul en kWh i euros.",
    "Cerca d'informació (fitxa 2, part C)": "D'on ve l'electricitat, amb l'avaluació de la fiabilitat de les fonts.",
    "Debat": "Defensa de les mesures del pla amb arguments basats en dades.",
}

TYPE = {"Inicial": ("#B7791F", "#FDF0D5"), "Desenvolupament": ("#1F5FA8", "#DCEAF8"), "Estructuració": ("#6B4FB0", "#EAE3F7"),
        "Aplicació": ("#2E7D4F", "#DDF1E4"), "Avaluació": ("#B23A3A", "#F8E0E0")}
SHORT = {k: k for k in TYPE}

CSS = """
@page{size:A4;margin:10mm 12mm 10mm}
body{line-height:1.2}
.head{margin-bottom:1.5mm;padding-bottom:1mm}h1{font-size:16pt;margin:0}
table{margin:0 0 2mm;width:100%}th,td{padding:.4mm 1.2mm;vertical-align:top;line-height:1.15}
td.k{font-weight:700;width:24%;background:var(--tint);color:var(--acc)}
.c{display:inline-block;font-weight:700;border-radius:1mm;padding:0 1mm;margin:0 .6mm .3mm 0;white-space:nowrap}
.leg{margin:0 0 1.5mm}
"""


def chip(t):
    c, bg = TYPE[t]
    return f'<span class="c" style="color:{c};background:{bg}">{SHORT[t]}</span>'


def fitxa(n):
    S = getattr(sda_a if n <= 3 else sda_b, f"SDA{n}")
    use(n)
    when = S["when"].split(" · ")[0]
    rows = [("Repte", f"<b>{S['question']}</b>"),
            ("Temporització", f"{when} · {len(S['sessions'])} sessions de 55 min"),
            ("Competències i criteris", S["ce"]),
            ("Objectius d'aprenentatge", "<ol style='margin:0;padding-left:4mm'>" + "".join(f"<li>{o[0]}</li>" for o in S["objectives"]) + "</ol>"),
            ("Producte final", S["product"]),
            ("Atenció a la diversitat", next(m[1] for m in S["measures"] if m[0] == "Addicionals"))]
    t1 = "<table>" + "".join(f'<tr><td class="k">{k}</td><td>{v}</td></tr>' for k, v in rows) + "</table>"
    acts_md = [r[3] for r in GA.tables(GA.section(n))[0][1:]]
    seq = ""
    for i, (title, group, acts) in enumerate(S["sessions"], 1):
        types = []
        for a in acts:
            if a[1] and a[1] not in types:
                types.append(a[1])
        seq += (f"<tr><td><b>{i} · {title}</b></td><td>{group.split(' · ')[0]}</td>"
                f"<td>{''.join(chip(t) for t in types)} {GA.md_inline(acts_md[i-1])}</td></tr>")
    t2 = ('<table><tr><th style="width:22%">Sessió</th><th style="width:6%">Grup</th><th>Tipus d\'activitats i què farem</th></tr>'
          + seq + "</table>")
    rows3 = ""
    for r in S["instruments"]:
        paper = r[5] if len(r) > 5 else ""
        if paper in ("—", ""):
            rows3 += f'<tr><td colspan="2"><b>Avaluació formativa</b> (no entra al càlcul oficial): {r[0][0].lower() + r[0][1:]}.</td><td>{r[3]}</td><td>—</td></tr>'
        else:
            d = PROVA if r[0].startswith("Demostració") else DESC[r[0]]
            rows3 += f"<tr><td><b>{r[0]}</b></td><td>{d}</td><td>{r[3]}</td><td>{r[4]}</td></tr>"
    t3 = ('<table><tr><th style="width:22%">Instrument</th><th>Què és</th><th style="width:8%">Sessió</th><th style="width:16%">Criteris</th></tr>'
          + rows3 + "</table>")
    body = (f'<div class="head"><div><div class="kick">Fitxa resum · Situació d\'aprenentatge {n}</div><h1>{S["title"]}</h1></div></div>'
            f"{t1}{t2}{t3}")
    return G.page(body, CSS), True


def f1(): return fitxa(1)
def f2(): return fitxa(2)
def f3(): return fitxa(3)
def f4(): return fitxa(4)
def f5(): return fitxa(5)
def f6(): return fitxa(6)
