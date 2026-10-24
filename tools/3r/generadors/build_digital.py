"""Construeix la versió digital (amb accés d'alumne i fitxes interactives) a ../llibrefiq3r/digital/index.html
a partir de la web estàtica (../site-fq3/index.html)."""
import os, re

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site-fq3", "index.html")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "llibrefiq3r", "digital", "index.html")
s = open(SRC, encoding="utf-8").read()

def rep(old, new, count=1):
    global s
    assert old in s, ("missing", old[:90])
    s = s.replace(old, new, count)

# rutes relatives des de /digital/
s = s.replace('u:"docs/', 'u:"../docs/')
s = s.replace('"docs/" +', '"../docs/" +').replace("url: \"docs/\" +", "url: \"../docs/\" +")
s = re.sub(r'src="img/', 'src="../img/', s)
s = s.replace('`img/sda${s.n}-s${i+1}.png`', '`../img/sda${s.n}-s${i+1}.png`')
s = s.replace('"lib/pdf.worker.min.js"', '"../lib/pdf.worker.min.js"')
s = s.replace('u:"sim-', 'u:"../sim-')
s = re.sub(r'"(img/(?:portada|coberta)[^"]+)"', r'"../\1"', s)
rep("<title>Física i química 3r ESO</title>", "<title>Física i química 3r ESO · Llibre digital</title>")

# llibreries i estils de la versió digital
head_add = """<link rel="stylesheet" href="css/fitxa.css">
<script src="js/config.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/mathlive@0.105.3/mathlive.min.js"></script>
<script src="js/units.js"></script>
<script src="js/fitxes-auto.js"></script>
<script src="js/fitxes.js"></script>
<script src="js/store.js"></script>
<script src="js/fitxa.js"></script>
<script src="js/tfm.js"></script>
"""
rep("</head>", head_add + "</head>")

# secció de la fitxa interactiva
rep('  <section class="viewer" id="vDoc" hidden', '  <section class="wsview" id="vWs" hidden></section>\n  <section class="viewer" id="vDoc" hidden')
rep('const VIEW = {home: "vHome", sda: "vSda", doc: "vDoc"};', 'const VIEW = {home: "vHome", sda: "vSda", doc: "vDoc", ws: "vWs"};')

# botons: les fitxes digitals s'obren com a fitxa interactiva
rep("""function dlBtn(k, ghost){ const d = D[k]; return `<a class="btn${ghost||d.t?' ghost':''}" href="#doc-${k}">${ICON_DOC}${esc(d.l)}</a>`; }""",
    """function dlBtn(k, ghost){ const d = D[k]; const dg = window.FITXES && window.FITXES[k]; return `<a class="btn${ghost||d.t?' ghost':''}" href="#${dg ? "fitxa" : "doc"}-${k}">${ICON_DOC}${esc(d.l)}${dg ? '<span class="dig">digital</span>' : ""}</a>`; }""")

# enganxa les rutes de la versió digital
rep("function route(nav){\n  const h = location.hash.slice(1);", "function route(nav){\n  const h = location.hash.slice(1);\n  if (window.FQRoute && window.FQRoute(h)) { closeDoc(); return; }")
rep("\nroute();\n", "\nwindow.SDAS = SDAS; window.D = D;\nwindow.FQShowView = (n) => setView(n, location.hash.slice(1));\nroute();\n")
rep("</body>", '<script src="js/alumne.js"></script>\n</body>')

# llista de fulls de l'alumnat per a la zona del professorat
import json
D = dict(re.findall(r'(\w+):\s*\{f:"(sda(\d)[^"]+)"', s) and [(k, f) for k, f, _ in re.findall(r'(\w+):\s*\{f:"(sda(\d)[^"]+)"', s)])
labels = dict(re.findall(r'(\w+):\s*\{f:"[^"]+", l:"([^"]+)"', s))
docs = {k: {"l": labels.get(k, k), "sda": int(re.match(r"sda(\d)", f).group(1))} for k, f in D.items()}
open(os.path.join(os.path.dirname(OUT), "js", "docs.js"), "w", encoding="utf-8").write("window.DOCS = " + json.dumps(docs, ensure_ascii=False) + ";\n")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(s)
print("digital/index.html", len(s) // 1024, "KB")
