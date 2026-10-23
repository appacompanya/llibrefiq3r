"""Construeix el llibre digital de 2n (/2n/digital/) a partir del llibre web de 2n (/2n/index.html).
Fa el mateix que build_digital.py de 3r, però amb el codi compartit de /digital/js/ i /digital/css/:
  - 2n/digital/index.html  llibre de l'alumnat amb accés per codi i fitxes interactives
  - 2n/digital/profe.html  zona del professorat de 2n (fitxes, «Per revisar», seguiment, alumnat)
  - 2n/digital/js/docs.js i js/sdas.js  dades de 2n per a la zona del professorat
  - 2n/index.html          marca quines fitxes tenen versió digital
Les fitxes (2n/digital/js/fitxes-auto.js) les fan pdf2html.py i build_fitxes.py.
Ús: python3 build_digital.py"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "2n", "index.html")
OUTDIR = os.path.join(ROOT, "2n", "digital")
s = open(SRC, encoding="utf-8").read()

def rep(old, new, count=1):
    global s
    assert old in s, ("missing", old[:90])
    s = s.replace(old, new, count)

# fitxes digitals que hi ha
fx = open(os.path.join(OUTDIR, "js", "fitxes-auto.js"), encoding="utf-8").read()
FITXES = json.loads(fx[fx.index(", {") + 2:fx.rindex("}") + 1])
keys = sorted(FITXES)

# 1) el llibre web marca les fitxes amb versió digital (botó «Obre la fitxa digital» del visor)
web = s.replace("const DIGITAL = new Set([]);", "const DIGITAL = new Set(" + json.dumps(keys) + ");")
web = re.sub(r"const DIGITAL = new Set\(\[[^\]]*\]\);", "const DIGITAL = new Set(" + json.dumps(keys) + ");", web)
open(SRC, "w", encoding="utf-8").write(web)
s = web

# 2) rutes relatives des de /2n/digital/
s = s.replace('u:"docs/', 'u:"../docs/')
s = s.replace('"docs/" +', '"../docs/" +').replace('url: "docs/" +', 'url: "../docs/" +')
s = re.sub(r'src="img/', 'src="../img/', s)
s = s.replace('`img/sda${s.n}-s${i+1}.webp`', '`../img/sda${s.n}-s${i+1}.webp`')
s = s.replace('"../lib/pdf.worker.min.js"', '"../../lib/pdf.worker.min.js"')
s = s.replace('"../sim-', '"../../sim-').replace("u:\"../sim-", "u:\"../../sim-")
s = re.sub(r'"(img/(?:portada|coberta)[^"]+)"', r'"../\1"', s)
rep("<title>Física i química 2n ESO</title>", "<title>Física i química 2n ESO · Llibre digital</title>")
rep('<meta name="description" content="', '<meta name="robots" content="noindex">\n<meta name="description" content="') if '<meta name="description" content="' in s else None

# 3) llibreries de la versió digital (codi compartit amb 3r)
head_add = """<link rel="stylesheet" href="../../digital/css/fitxa.css">
<script>window.FQ_LEVEL = "2n"; window.FQ_WSPREFIX = "2n:";</script>
<script src="../../digital/js/config.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/mathlive@0.105.3/mathlive.min.js"></script>
<script src="../../digital/js/units.js"></script>
<script src="js/fitxes-auto.js"></script>
<script src="../../digital/js/store.js"></script>
<script src="../../digital/js/fitxa.js"></script>
"""
rep("</head>", head_add + "</head>")

# 4) vista de fitxa interactiva i rutes
rep('  <section class="viewer" id="vDoc" hidden', '  <section class="wsview" id="vWs" hidden></section>\n  <section class="viewer" id="vDoc" hidden')
rep('const VIEW = {home: "vHome", sda: "vSda", doc: "vDoc"};', 'const VIEW = {home: "vHome", sda: "vSda", doc: "vDoc", ws: "vWs"};')
rep("""function dlBtn(k, ghost){ const d = D[k]; if (!d) return ""; return `<a class="btn${ghost||d.t?' ghost':''}" href="#doc-${k}">${ICON_DOC}${esc(d.l)}</a>`; }""",
    """function dlBtn(k, ghost){ const d = D[k]; if (!d) return ""; const dg = window.FITXES && window.FITXES[k]; return `<a class="btn${ghost||d.t?' ghost':''}" href="#${dg ? "fitxa" : "doc"}-${k}">${ICON_DOC}${esc(d.l)}${dg ? '<span class="dig">digital</span>' : ""}</a>`; }""")
rep("function route(nav){\n  const h = location.hash.slice(1);", "function route(nav){\n  const h = location.hash.slice(1);\n  if (window.FQRoute && window.FQRoute(h)) { closeDoc(); return; }")
rep("\nroute();\n", "\nwindow.SDAS = SDAS; window.D = D;\nwindow.FQShowView = (n) => setView(n, location.hash.slice(1));\nroute();\n")
rep("</body>", '<script src="../../digital/js/alumne.js"></script>\n</body>')
# l'enllaç del visor a la fitxa digital, dins del mateix llibre
s = s.replace('g.href = "https://llibrefiq3r.cat/2n/digital/#fitxa-" + k;', 'g.href = "#fitxa-" + k;')

os.makedirs(os.path.join(OUTDIR, "js"), exist_ok=True)
open(os.path.join(OUTDIR, "index.html"), "w", encoding="utf-8").write(s)

# 5) dades per a la zona del professorat
D = json.loads(re.search(r"^const D = (\{.*?\});$", web, re.M).group(1))
docs = {k: {"l": v["l"], "sda": int(re.match(r"sda(\d)", v["f"]).group(1))} for k, v in D.items() if re.match(r"sda\d", v["f"]) and not v.get("t")}
open(os.path.join(OUTDIR, "js", "docs.js"), "w", encoding="utf-8").write("window.DOCS = " + json.dumps(docs, ensure_ascii=False) + ";\n")
m = re.search(r"^const SDAS = (\[.*?\]);$", web, re.M | re.S)
sdas = json.loads(m.group(1)) if m and m.group(1).strip().startswith("[{\"") else None
if sdas is None:
    raise SystemExit("No he pogut llegir SDAS de 2n/index.html")
open(os.path.join(OUTDIR, "js", "sdas.js"), "w", encoding="utf-8").write("window.SDAS = " + json.dumps([{"n": x["n"], "title": x["title"], "c": x.get("c")} for x in sdas], ensure_ascii=False) + ";\n")

# 6) zona del professorat de 2n: el tauler del llibre digital (profe.js) en una pàgina pròpia
css_vars = re.search(r":root\{[^}]*\}", web).group(0)
profe = f"""<!doctype html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Zona del professorat · FQ 2n ESO</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&display=swap">
<link rel="stylesheet" href="../../digital/css/fitxa.css">
<link rel="stylesheet" href="../../digital/css/profe.css">
<style>
{css_vars}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#15171b; --surface:#1d2026; --fg:#eceef1; --muted:#a3aab4; --line:#2f333b; --chip:#272b32; --ok:#5fd394; --warn:#f0b45c; --ink:#0f1620; --ink-fg:#eceef1; color-scheme:dark}}}}
*{{box-sizing:border-box}}
[hidden]{{display:none!important}}
body{{background:var(--bg);color:var(--fg);font-family:var(--font-body);font-size:15px;line-height:1.5;margin:0}}
.wrap{{max-width:1080px;margin:0 auto;padding:20px max(16px,env(safe-area-inset-right,0px)) 64px max(16px,env(safe-area-inset-left,0px));display:grid;gap:18px}}
h1,h2{{font-family:var(--font-display);font-weight:800;margin:0}}
.btn{{font:inherit;font-size:.86rem;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:6px 12px;border:1.5px solid var(--acc,var(--s1));background:var(--acc,var(--s1));color:#fff;text-decoration:none;white-space:nowrap}}
.btn.ghost{{background:transparent;color:var(--fg);border-color:var(--line)}}
.login{{max-width:420px;margin:8vh auto 0}}
.spin{{width:28px;height:28px;border:3px solid var(--line);border-top-color:var(--acc,var(--s1));border-radius:50%;animation:sp 1s linear infinite;margin:30px auto}}@keyframes sp{{to{{transform:rotate(360deg)}}}}
</style>
<script>window.FQ_LEVEL = "2n"; window.FQ_WSPREFIX = "2n:"; window.FQ_DOCENT_URL = "../../docent/";</script>
<script src="../../digital/js/config.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/mathlive@0.105.3/mathlive.min.js"></script>
<script src="../../digital/js/units.js"></script>
<script src="js/fitxes-auto.js"></script>
<script src="js/docs.js"></script>
<script src="js/sdas.js"></script>
<script src="../../digital/js/store.js"></script>
<script src="../../digital/js/fitxa.js"></script>
</head>
<body>
<div class="wrap" id="app"></div>
<div class="toast" id="toast" hidden role="status"></div>
<script src="../../digital/js/profe.js"></script>
</body>
</html>
"""
open(os.path.join(OUTDIR, "profe.html"), "w", encoding="utf-8").write(profe)
print("2n/digital:", len(keys), "fitxes digitals")
