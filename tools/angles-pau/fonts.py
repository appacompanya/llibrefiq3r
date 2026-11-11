#!/usr/bin/env python3
"""Baixa les fonts de la PAU d'anglès (enunciats, correccions i àudios) a una carpeta.

S'executa a GitHub Actions (el contenidor de treball no hi té accés).
Fonts:
  1. Carpetes de la coordinació de la PAU d'anglès (Dropbox, enllaçades des de sites.google.com/xtec.cat/pau-angles).
  2. Pàgina oficial d'Anglès del Canal Universitats (PDF i àudios de les convocatòries recents).
Ús: python3 tools/angles-pau/fonts.py /tmp/fonts
"""
import io, re, sys, time, urllib.parse, urllib.request, zipfile
from pathlib import Path

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "fonts")
OUT.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
DROPBOX = {
    "examens": "https://www.dropbox.com/sh/rx6xgodnwkku6fq/AACzWjRVKmYdBwof46sUlau9a?dl=1",
    "audios": "https://www.dropbox.com/sh/9bmfy3i0pppbslu/AADygPVjSubqGh9IfTdrwEiCa?dl=1",
    "solucions": "https://www.dropbox.com/sh/ra5roai078cwf07/AAAYnlHdH5BwRY-PoaQM50TOa?dl=1",
    "nou-model": "https://www.dropbox.com/scl/fo/wyc3tigch338vqtsjl5yy/AIgdBDy16ioQK5tF9rZ974w?rlkey=uavsirrx1a8h1rrdhstiuven8&dl=1",
}
GENCAT = [
    "https://universitats.gencat.cat/ca/pau/models-examen-anys-anteriors/angles/",
    "https://universitats.gencat.cat/ca/pau/materies-pau/angles/",
]
log = open(OUT / "registre.txt", "w")


def get(url, timeout=600):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get("Content-Type", ""), r.geturl()


# 1. Dropbox: cada carpeta compartida es baixa sencera com a ZIP
for name, url in DROPBOX.items():
    dest = OUT / "dropbox" / name
    dest.mkdir(parents=True, exist_ok=True)
    for attempt in range(3):
        try:
            body, ct, final = get(url, timeout=1800)
            zf = zipfile.ZipFile(io.BytesIO(body))
            n = 0
            for info in zf.infolist():
                if info.is_dir():
                    continue
                p = dest / info.filename
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(zf.read(info))
                n += 1
            log.write(f"OK\tdropbox/{name}\t{n} fitxers\t{len(body)} bytes\n")
            break
        except Exception as e:
            log.write(f"ERR\tdropbox/{name}\tintent {attempt+1}\t{e}\n")
            time.sleep(10)

# 2. Canal Universitats: PDF i àudios enllaçats des de la pàgina d'Anglès
dest = OUT / "gencat"
dest.mkdir(exist_ok=True)
seen = set()
for page in GENCAT:
    try:
        html = get(page, 60)[0].decode("utf-8", "replace")
    except Exception as e:
        log.write(f"ERR\t{page}\t{e}\n"); continue
    log.write(f"OK\t{page}\n")
    for href in re.findall(r'href="([^"]+)"', html):
        u = urllib.parse.urljoin(page, href.replace("&amp;", "&"))
        if not re.search(r"\.(pdf|mp3|m4a|wav|ogg)(\?|$)", u, re.I) or u in seen:
            continue
        seen.add(u)
        fn = re.sub(r"^https?://[^/]+/(web/\.content/)?", "", u).split("?")[0].replace("/", "__")
        try:
            body = get(u, 300)[0]
            (dest / fn).write_bytes(body)
            log.write(f"OK\t{fn}\t{len(body)}\t{u}\n")
        except Exception as e:
            log.write(f"ERR\t{u}\t{e}\n")
log.close()
