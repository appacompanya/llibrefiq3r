"""Zona del professorat web (../llibrefiq3r/digital/profe.html): llibre del professorat + accés amb usuari
+ PDF del professorat des d'un espai privat + avaluació a Supabase + tauler del llibre digital."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(HERE, "profe.html"), encoding="utf-8").read()
OUT = os.path.join(HERE, "..", "llibrefiq3r", "digital", "profe.html")
def rep(old, new, count=1):
    global s
    assert old in s, ("missing", old[:100]); s = s.replace(old, new, count)

# rutes
s = re.sub(r'src="img/', 'src="../img/', s)
s = s.replace('`img/sda${s.n}-s${i+1}.png`', '`../img/sda${s.n}-s${i+1}.png`')
s = s.replace('"lib/pdf.worker.min.js"', '"../lib/pdf.worker.min.js"')
s = s.replace('u:"sim-', 'u:"../sim-')
s = re.sub(r'"(img/(?:portada|coberta)[^"]+)"', r'"../\1"', s)
# PDF: alumnat a ../docs, professorat a l'espai privat
rep('const r = await fetch("docs/" + f);', 'const r = await fetch(await window.fqDocUrl(f));')
rep('pdfjsLib.getDocument({url: "docs/" + d.f, isEvalSupported: false}).promise', 'window.fqDocUrl(d.f).then((u) => pdfjsLib.getDocument({url: u, isEvalSupported: false}).promise)')
rep('const r = await fetch("docs/" + file);', 'const r = await fetch(await window.fqDocUrl(file));')
assert '"docs/"' not in s, "queden rutes docs/"
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '').replace('<meta charset="utf-8">\n', '')
title = re.search(r"<title>(.*?)</title>", s).group(1); s = s.replace(f"<title>{title}</title>\n", "")
head = f"""<!doctype html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Zona del professorat · FQ 3r ESO</title>
<link rel="stylesheet" href="css/fitxa.css">
<link rel="stylesheet" href="css/profe.css">
<script src="js/config.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/mathlive@0.105.3/mathlive.min.js"></script>
<script src="js/units.js"></script>
<script src="js/fitxes-auto.js"></script>
<script src="js/fitxes.js"></script>
<script src="js/docs.js"></script>
<script src="js/store.js"></script>
<script src="js/fitxa.js"></script>
<script src="js/profe-shim.js"></script>
<script>window.FQ_EMBED = true;</script>
"""
s = head + s
rep('<div class="wrap">', '</head>\n<body>\n<div class="tlogin" id="tlogin"><form id="tlf"><div class="eyebrow">Física i química · 3r d\'ESO</div><h1>Zona del professorat</h1><label>Usuari<input id="tlu" autocomplete="username" required></label><label>Contrasenya<input id="tlp" type="password" autocomplete="current-password" required></label><p class="err" id="tle"></p><button class="btn" type="submit">Entra</button></form></div>\n<div class="wrap">')
# vista del tauler digital
rep('  <section class="viewer" id="vDoc" hidden', '  <section class="view" id="vDig" hidden></section>\n  <section class="viewer" id="vDoc" hidden')
rep('const VIEW = {home: "vHome", sda: "vSda", doc: "vDoc"};', 'const VIEW = {home: "vHome", sda: "vSda", doc: "vDoc", dig: "vDig"};')
rep("function route(nav){\n  const h = location.hash.slice(1);", "function route(nav){\n  const h = location.hash.slice(1);\n  if (h === \"digital\") { closeDoc(); document.documentElement.style.setProperty(\"--acc\", \"var(--s6)\"); setView(\"dig\", h); if (window.FQ_READY && window.FQDigital && !route.dig) { route.dig = true; window.FQDigital.mount(document.getElementById(\"vDig\")); } return; }")
# accés directe des de la portada
rep('<div class="qlinks">${SDAS.map', '<div class="qlinks"><a class="btn" href="#digital" style="--acc:var(--s6)">Llibre digital: alumnat, codis i lliuraments</a>${SDAS.map')
# inici: primer l'accés, després el llibre
rep('\nroute();\nif (MODE==="profe") initStore();\n', '''
window.D = D; window.SDAS = SDAS;
async function fqStart(){
  document.getElementById("tlogin").hidden = true;
  window.FQ_READY = true; route(); initStore();
}
(async () => {
  let me = null; try { me = await window.FQStore.init(); } catch(e) {}
  if (me && me.role === "teacher") return fqStart();
  document.getElementById("tlf").addEventListener("submit", async (e) => {
    e.preventDefault(); const b = e.target.querySelector("button"); b.disabled = true; document.getElementById("tle").textContent = "";
    try { await window.FQStore.signInTeacher(document.getElementById("tlu").value, document.getElementById("tlp").value); await fqStart(); }
    catch(err) { document.getElementById("tle").textContent = "Usuari o contrasenya incorrectes."; }
    finally { b.disabled = false; }
  });
})();
''')
rep("</script>\n", "</script>\n<script src=\"js/profe.js\"></script>\n", 1) if False else None
s = s.rstrip() + '\n<script src="js/profe.js"></script>\n</body>\n</html>\n'
open(OUT, "w", encoding="utf-8").write(s)
print("profe.html", len(s)//1024, "KB")
