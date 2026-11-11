#!/usr/bin/env python3
"""Recorre les pàgines de models d'examen de la PAU (universitats.gencat.cat) i baixa els PDF de Química.

S'executa a GitHub Actions (el contenidor de treball no hi té accés). Desa els PDF a fonts/ i la llista a fonts/llista.tsv.
"""
import re, sys, time, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "fonts")
OUT.mkdir(parents=True, exist_ok=True)
HOST = "universitats.gencat.cat"
START = [
    "https://universitats.gencat.cat/ca/pau/models-examen-anys-anteriors/",
    "https://universitats.gencat.cat/ca/pau/examens-correccions/",
    "https://universitats.gencat.cat/ca/pau/index.html",
]
UA = {"User-Agent": "Mozilla/5.0 (llibrefiq3r; recull PAU Química per a ús educatiu)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.headers.get("Content-Type", "")


seen, pdfs, queue = set(), {}, [(u, 0) for u in START]
log = open(OUT / "pagines.txt", "w")
while queue and len(seen) < 400:
    url, d = queue.pop(0)
    if url in seen:
        continue
    seen.add(url)
    try:
        body, ct = get(url)
    except Exception as e:
        log.write(f"ERR\t{url}\t{e}\n"); continue
    if "html" not in ct:
        continue
    html = body.decode("utf-8", "replace")
    log.write(f"OK\t{d}\t{url}\n")
    for href in re.findall(r'href="([^"#]+)"', html):
        u = urllib.parse.urljoin(url, href.replace("&amp;", "&"))
        p = urllib.parse.urlparse(u)
        if p.netloc != HOST:
            continue
        if u.lower().endswith(".pdf"):
            name = Path(p.path).name.lower()
            if "quim" in name or "/quimica/" in p.path.lower():
                pdfs.setdefault(u, url)
        elif d < 3 and "/ca/pau/" in p.path and not any(x in p.path for x in ("/inscripcio", "/calendari", "/notes", "/reclam")):
            queue.append((u.split("?")[0], d + 1))
    time.sleep(0.3)
log.close()

with open(OUT / "llista.tsv", "w") as f:
    for u, src in sorted(pdfs.items()):
        name = urllib.parse.urlparse(u).path.split("/web/.content/")[-1].replace("/", "__")
        try:
            body, _ = get(u)
            (OUT / name).write_bytes(body)
            f.write(f"{name}\t{len(body)}\t{u}\t{src}\n")
        except Exception as e:
            f.write(f"ERR\t0\t{u}\t{e}\n")
        time.sleep(0.2)
print(len(seen), "pàgines,", len(pdfs), "PDF de química")
