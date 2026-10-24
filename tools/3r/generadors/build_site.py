"""Genera la web estàtica del llibre de l'alumnat (sense dependre de Claude) a ../site-fq3.

- Només inclou el material de l'alumnat: cap fitxer marcat com a t:1 (prova, solucionaris, adaptacions...).
- Descàrregues amb enllaços normals del navegador.
- Llest per publicar a GitHub Pages.
"""
import os, re, shutil, json

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(SRC), "site-fq3")

page = open(os.path.join(SRC, "index.html"), encoding="utf-8").read()   # versió alumne ja construïda per build_web.py
assert 'const MODE = "alumne"' in page

# 1) descàrregues amb el navegador en lloc de la capacitat de claude.ai
old = re.search(r'function getDownloads\(\)\{[^\n]*\}', page).group(0)
new = ('function getDownloads(){ return Promise.resolve({save: async ({filename, data}) => {'
       ' const blob = data instanceof Blob ? data : new Blob([data], {type: "text/plain;charset=utf-8"});'
       ' const u = URL.createObjectURL(blob); const a = document.createElement("a");'
       ' a.href = u; a.download = filename; document.body.appendChild(a); a.click(); a.remove();'
       ' setTimeout(() => URL.revokeObjectURL(u), 5000); }}); }')
page = page.replace(old, new)
page = page.replace("Per descarregar el full, obre aquesta pàgina des de claude.ai.", "No s'ha pogut descarregar el full.")
page = page.replace("Per descarregar els fulls, obre aquesta pàgina des de claude.ai.", "No s'han pogut descarregar els fulls.")
page = page.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
page = page.replace('<meta charset="utf-8">\n', '')

# 1b) treure de la pàgina pública les dades del professorat (noms de fitxers privats, enllaços i notes)
page = re.sub(r'\n\s*\w+:\s*\{f:"[^"]+",[^}]*t:1\},?', '', page)
page = re.sub(r'teacher:\[\n.*?\n\s*\]\}', 'teacher:[]}', page, flags=re.S)
page = re.sub(r'const LINKS = \{.*?\n\};', 'const LINKS = {};', page, flags=re.S)
page = re.sub(r', dt:\[[^\]]*\]', '', page)

# 2) esquelet HTML complet
title = re.search(r"<title>(.*?)</title>", page).group(1)
page = page.replace(f"<title>{title}</title>\n", "")
fav = ("data:image/svg+xml," + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect x='4' y='4' width='56' height='56' rx='8' fill='white' stroke='%231f2328' stroke-width='5'/%3E%3Ctext x='32' y='43' font-family='Arial' font-weight='700' font-size='28' text-anchor='middle' fill='%231f2328'%3EFq%3C/text%3E%3C/svg%3E")
head = f"""<!doctype html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="Llibre digital dinàmic de Física i química de 3r d'ESO: sis reptes, sessió a sessió, amb fitxes, simulacions i lectures.">
<link rel="icon" href="{fav}">
"""
page = head + page.replace("<style>", "<style>\nhtml{-webkit-text-size-adjust:100%}", 1)
page = page.replace("<div class=\"wrap\">", "</head>\n<body>\n<div class=\"wrap\">", 1)
page = page.rstrip() + "\n</body>\n</html>\n"

# 3) fitxers
if os.path.exists(OUT):
    for name in os.listdir(OUT):
        if name in (".git",): continue
        p = os.path.join(OUT, name)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)

D = dict(re.findall(r'(\w+):\s*\{f:"([^"]+)"', page))
teacher = set(re.findall(r'\{f:"([^"]+)"[^}]*t:1\}', page))
student_files = sorted(set(D.values()) - teacher)

def copy_student_pdf(src, dst):
    """Copia el PDF sense les pàgines de notes per al professorat."""
    import subprocess
    from pypdf import PdfReader, PdfWriter
    r = PdfReader(src); keep = []
    for i in range(len(r.pages)):
        t = subprocess.run(["pdftotext", "-f", str(i + 1), "-l", str(i + 1), src, "-"], capture_output=True, text=True).stdout
        if re.search(r"per al professorat", t, re.I) and re.search(r"no s.imprimeix", t): continue
        keep.append(i)
    if len(keep) == len(r.pages): shutil.copy2(src, dst); return
    w = PdfWriter()
    for i in keep: w.add_page(r.pages[i])
    with open(dst, "wb") as fh: w.write(fh)
    print("  sense notes del professorat:", os.path.basename(src), len(r.pages), "->", len(keep))

os.makedirs(os.path.join(OUT, "docs"))
missing = []
for f in student_files:
    src = os.path.join(SRC, "docs", f)
    if os.path.exists(src): copy_student_pdf(src, os.path.join(OUT, "docs", f))
    else: missing.append(f)
shutil.copytree(os.path.join(SRC, "img"), os.path.join(OUT, "img"), ignore=shutil.ignore_patterns("portada-profe.*"))
shutil.copytree(os.path.join(SRC, "lib"), os.path.join(OUT, "lib"))
import glob
for _f in glob.glob(os.path.join(SRC, "sim-*.html")): shutil.copy2(_f, OUT)
shutil.copy2(os.path.join(SRC, "docs", "sda6-00-plantilla-inventari-energetic.xlsx"), os.path.join(OUT, "docs"))
open(os.path.join(OUT, ".nojekyll"), "w").close()
open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(
"""# Física i química · 3r d'ESO

Llibre digital dinàmic de Física i química de 3r d'ESO creat per Macià Esteve Pallarès Pallarès.

Web estàtica: `index.html` + `docs/` (fulls en PDF) + `img/` + `lib/` (visor de PDF).
Conté només el material de l'alumnat.
""")
print("pàgina:", len(page)//1024, "KB · fulls alumnat:", len(student_files), "· exclosos (professorat):", len(teacher), "· falten:", missing)
