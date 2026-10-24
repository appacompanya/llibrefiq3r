"""Actualitza els números de pàgina de l'índex estàtic a partir del PDF renderitzat."""
import sys, re, pymupdf
from docx import Document
from prog_edit import W, ptext
docx_path, pdf_path = sys.argv[1], sys.argv[2]
d = pymupdf.open(pdf_path)
pages = []
for i in range(len(d)):
    t = d[i].get_text()
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    num = lines[-1] if lines and re.fullmatch(r"\d+", lines[-1]) else None
    pages.append((num, set(lines)))
doc = Document(docx_path)
n = 0; miss = []
for p in doc.element.body.iter(W + 'p'):
    t = ptext(p)
    m = re.match(r"^(.*\S)\t(\d+)$", t)
    if not m:
        continue
    title = m.group(1).strip()
    found = None
    for k, (num, lines) in enumerate(pages):
        if k < 3:
            continue
        if (title in lines or re.sub(r"SdA \d · ", "", title) in lines) and num:
            found = num; break
    if not found:
        miss.append(title); continue
    ts = [x for x in p.iter(W + 't')]
    for x in reversed(ts):
        if re.fullmatch(r"\d+", (x.text or "").strip()):
            x.text = (x.text or "").replace((x.text or "").strip(), found); n += 1; break
doc.save(docx_path)
print("actualitzats", n, "· no trobats:", miss)
