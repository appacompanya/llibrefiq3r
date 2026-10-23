"""Controls automàtics de les fitxes de 2n o 4t reconstruïdes (per trobar-hi errors de conversió)."""
import os, re, sys, json, glob
import fitz
from bs4 import BeautifulSoup
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from nivell import LEVEL, ROOT, TMP
tpl = open(os.path.join(ROOT, LEVEL, "index.html"), encoding="utf-8").read()
D = json.loads(re.search(r"^const D = (\{.*?\});$", tpl, re.M).group(1))
for f in sorted(glob.glob(os.path.join(TMP, "*.html"))):
    k = os.path.basename(f)[:-5]
    soup = BeautifulSoup(open(f).read(), "html.parser")
    probs = []
    # preguntes: les del PDF (números blancs dins d'insígnies) i les reconstruïdes
    d = fitz.open(os.path.join(ROOT, LEVEL, "docs", D[k]["f"]))
    nq_pdf = sum(1 for p in d for b in p.get_text("dict")["blocks"] if b["type"] == 0 for l in b["lines"] for s in l["spans"] if s["color"] == 0xffffff and s["text"].strip().isdigit())
    nq = len(soup.select(".q > .n")) + len(soup.select(".list .c .b"))
    if nq != nq_pdf: probs.append(f"preguntes {nq}/{nq_pdf}")
    # paràgrafs molt curts fora de taules (fraccions o etiquetes trencades)
    short = [p.get_text(" ", strip=True) for p in soup.find_all("p") if not p.find_parent("table") and 0 < len(p.get_text(strip=True)) <= 6 and not p.find("span", class_="blank")]
    if short: probs.append("curts: " + " | ".join(short[:6]))
    # text de lletres espaiades (etiquetes girades)
    sp = [p.get_text() for p in soup.find_all("p") if re.search(r"(\b\w ){4,}", p.get_text())]
    if sp: probs.append("espaiat: " + " | ".join(x[:30] for x in sp[:3]))
    if probs: print(k, "·", " · ".join(probs))
