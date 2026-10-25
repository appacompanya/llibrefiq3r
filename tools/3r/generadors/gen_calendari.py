"""Calendari anual (1 pàgina): dies de classe de cada SdA pintats del color de la SdA.
Dilluns i dimecres: mig grup (el professor repeteix la sessió amb cada meitat) -> to clar.
Dijous: grup sencer -> color ple. Cada sessió de l'alumnat ocupa un dijous o la parella dilluns+dimecres."""
import datetime as dt, json, os, calendar
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
COL = {0: "#5d646d", 1: "#2E959C", 2: "#F27C29", 3: "#685AD2", 4: "#40915F", 5: "#CE4555", 6: "#2989E4"}
NAME = {0: "Sessió 0 i tancament", 1: "SdA 1 · Detectius de la matèria", 2: "SdA 2 · El desodorant kamikaze", 3: "SdA 3 · Què hi ha dins del meu mòbil?",
        4: "SdA 4 · Un cotxe que només allibera aigua?", 5: "SdA 5 · Cèl·lules a la caça dels patògens", 6: "SdA 6 · L'energia del nostre institut"}
START, END = dt.date(2026, 9, 8), dt.date(2027, 6, 21)
FEST = {dt.date(2026, 9, 11): "Diada", dt.date(2026, 9, 24): "La Mercè", dt.date(2026, 10, 12): "Festa nacional", dt.date(2026, 10, 30): "Lliure disposició",
        dt.date(2026, 12, 7): "Lliure disposició", dt.date(2026, 12, 8): "Immaculada", dt.date(2027, 2, 8): "Lliure disposició",
        dt.date(2027, 5, 14): "Lliure disposició", dt.date(2027, 5, 17): "Segona Pasqua"}
VAC = [(dt.date(2026, 12, 22), dt.date(2027, 1, 7), "Nadal"), (dt.date(2027, 3, 20), dt.date(2027, 3, 29), "Setmana Santa")]
G = json.load(open(os.path.join(HERE, "annex_groups.json"), encoding="utf-8"))  # {"1": "GMGM...", ...} G grup sencer, M mig grup, L laboratori (només en mig grup)

def lective(d):
    return START <= d <= END and d.weekday() < 5 and d not in FEST and not any(a <= d <= b for a, b, _ in VAC)

def schedule():
    """Programació dinàmica: col·loca les sessions en ordre minimitzant els intercanvis (G en hora desdoblada o M sense laboratori en dijous)."""
    seq = [(0, 0, "G")] + [(n, i + 1, t) for n in range(1, 7) for i, t in enumerate(G[str(n)])] + [(0, 99, "G")]
    slots = []
    d = START - dt.timedelta(days=START.weekday())
    while d <= END:
        mon, wed, thu = d, d + dt.timedelta(2), d + dt.timedelta(3)
        if lective(mon) and lective(wed): slots.append(("MG", mon, wed))
        if lective(thu): slots.append(("GS", thu))
        d += dt.timedelta(7)
    INF = 10 ** 9
    N, K = len(slots), len(seq)
    best = [[INF] * (K + 1) for _ in range(N + 1)]; best[N][K] = 0
    choice = [[None] * (K + 1) for _ in range(N + 1)]
    def cost(sl, t):
        if sl[0] == "MG": return 0 if t in "ML" else 1
        return 0 if t == "G" else (1 if t == "M" else INF)
    for i in range(N - 1, -1, -1):
        for k in range(K, -1, -1):
            v, ch = best[i + 1][k] + (0 if k == K else 0.001), "skip"   # esperar costa molt poc (preferim acabar abans)
            if k < K:
                c = cost(slots[i], seq[k][2])
                if c < INF and best[i + 1][k + 1] + c < v: v, ch = best[i + 1][k + 1] + c, "put"
            best[i][k], choice[i][k] = v, ch
    out, i, k = {}, 0, 0
    while i < N and k < K:
        if choice[i][k] == "put":
            sl = slots[i]; n, sn, t = seq[k]
            if sl[0] == "MG":
                if t in "ML": out[sl[1]] = out[sl[2]] = (n, sn, t, "M")
                else: out[sl[1]] = (n, sn, t, "X")
            else:
                out[sl[1]] = (n, sn, t, "G")
            k += 1
        i += 1
    return out, k == K

def tint(h, f):
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02x%02x%02x" % tuple(round(c + (255 - c) * f) for c in (r, g, b))

def html():
    S, ok = schedule()
    assert ok, "no hi caben totes les sessions"
    months = [(2026, m) for m in range(9, 13)] + [(2027, m) for m in range(1, 7)]
    MN = ["", "Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"]
    cards = ""
    # sessions de marge: franges setmanals (mig grup dl+dc o grup sencer dj) que no ocupa cap sessió
    MARGE = set()
    d0 = START - dt.timedelta(days=START.weekday())
    while d0 <= END:
        mon, wed, thu = d0, d0 + dt.timedelta(2), d0 + dt.timedelta(3)
        if lective(mon) and lective(wed) and mon not in S and wed not in S: MARGE |= {mon, wed}
        if lective(thu) and thu not in S: MARGE.add(thu)
        d0 += dt.timedelta(7)
    for y, m in months:
        cells = "".join(f"<div class='dh'>{x}</div>" for x in "DlDmDcDjDvDsDg".replace("Dl", "Dl ").split()) if False else "".join(f"<div class='dh'>{x}</div>" for x in ["dl", "dt", "dc", "dj", "dv", "ds", "dg"])
        first = dt.date(y, m, 1)
        cells += "<div></div>" * first.weekday()
        for day in range(1, calendar.monthrange(y, m)[1] + 1):
            d = dt.date(y, m, day)
            st, tip, lab = "", "", ""
            if d in S:
                n, s, _, kind = S[d]
                c = COL[n]
                bg = c if kind in "GX" else tint(c, .62)
                fg = "#fff" if kind in "GX" else c
                st = f"background:{bg};color:{fg};font-weight:700"
                lab = f"<i>{'0' if s == 0 else ('T' if s == 99 else s)}{'↔' if kind == 'X' else ''}</i>"
            elif d in MARGE:
                st = "background:#FFE27A;color:#7a5a00;font-weight:700"
                lab = "<i>M</i>"
            elif d in FEST:
                st = "background:#eceef1;color:#9aa0a6"
            elif any(a <= d <= b for a, b, _ in VAC):
                st = "background:#eceef1;color:#9aa0a6"
            elif d.weekday() >= 5 or not (START <= d <= END):
                st = "color:#b8bcc2"
            cells += f"<div class='d' style='{st}'>{day}{lab}</div>"
        cards += f"<div class='mo'><h3>{MN[m]} {y}</h3><div class='gr'>{cells}</div></div>"
    leg = "".join(f"<span><b style='background:{COL[n]}'></b><b style='background:{tint(COL[n], .62)}'></b>{NAME[n]}</span>" for n in range(1, 7))
    leg += f"<span><b style='background:{COL[0]}'></b>Sessió 0 i tancament (T)</span><span><b style='background:#FFE27A'></b>M: sessió de marge (imprevistos, sortides, recuperacions)</span><span><b style='background:#eceef1'></b>Vacances, festius i dies de lliure disposició</span>"
    used = len({v[:2] for v in S.values()})
    teach = sum(1 for v in S.values())
    return f"""<!doctype html><html lang="ca"><head><meta charset="utf-8"><style>
@page{{size:A4 landscape;margin:7mm 9mm}}body{{font-family:Arial,'Liberation Sans',Helvetica,sans-serif;margin:0;color:#1f2328}}.kick{{font-size:9pt;font-weight:700;color:#1F4E79;letter-spacing:.02em}}
h1{{font-size:14pt;margin:0}}.sub{{font-size:9pt;line-height:1.25;color:#5d646d;margin:.8mm 0 2mm}}
.wrap{{display:grid;grid-template-columns:repeat(5,1fr);gap:2mm 4mm}}.mo h3{{font-size:10pt;margin:0 0 .6mm}}
.gr{{display:grid;grid-template-columns:repeat(7,1fr);gap:.6mm}}.dh{{font-size:9pt;color:#5d646d;text-align:center}}
.d{{font-size:9pt;text-align:center;border-radius:1mm;height:9.4mm;line-height:4.9mm;position:relative}}.d i{{display:block;font-style:normal;font-size:9pt;line-height:3.9mm;opacity:.95}}
.leg{{display:flex;flex-wrap:wrap;gap:1.2mm 5mm;font-size:9pt;margin-top:2mm}}.leg span{{display:inline-flex;align-items:center;gap:1mm}}.leg b{{display:inline-block;width:4mm;height:3.4mm;border-radius:.8mm}}
.note{{font-size:9pt;line-height:1.25;color:#5d646d;margin-top:1.2mm}}
</style></head><body><div class="kick">ANNEX 11 · INSTRUMENT ORGANITZATIU</div><h1>Calendari del curs 2026-2027 · Física i química 3r d'ESO</h1>
<p class="sub">To clar: sessió de mig grup (dilluns i dimecres). Color ple: grup sencer (dijous). El número és la sessió de la SdA; ↔: sessió de grup sencer en dilluns.</p>
<div class="wrap">{cards}</div><div class="leg">{leg}</div>

</body></html>"""

if __name__ == "__main__":
    h = html()
    p = os.path.join(HERE, "annex", "calendari.html"); open(p, "w", encoding="utf-8").write(h)
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page(viewport={"width": 1400, "height": 990})
        pg.goto("file://" + p); pg.wait_for_timeout(400)
        pg.pdf(path=os.path.join(HERE, "annex", "calendari.pdf"), format="A4", landscape=True, print_background=True)
        pg.screenshot(path=os.path.join(HERE, "annex", "calendari.png"), full_page=True)
        br.close()
    print("ok")
