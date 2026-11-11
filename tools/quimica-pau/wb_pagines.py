#!/usr/bin/env python3
"""Cerca a la Wayback Machine les pàgines antigues de «models d'examen» de Química i n'extreu els enllaços als PDF.

Escriu una URL per línia (PDF via web.archive.org id_) a stdout."""
import json, re, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (llibrefiq3r; recull PAU)"}


def get(u, t=90):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            err = e; time.sleep(4 * (k + 1))
    print("ERR", u, err, file=sys.stderr); return ""


pages = set()
for host in ("universitats.gencat.cat", "universitatsirecerca.gencat.cat"):
    q = (f"https://web.archive.org/cdx/search/cdx?url={host}/ca/*&output=json&fl=timestamp,original"
         "&filter=statuscode:200&filter=mimetype:text/html&filter=original:.*[Qq]u[ií%].*m.*&limit=20000")
    try:
        rows = json.loads(get(q, 300) or "[]")
    except Exception:
        rows = []
    print(host, len(rows), file=sys.stderr)
    for ts, orig in rows[1:]:
        if re.search(r"quimica|qu%C3%ADmica", orig, re.I) and re.search(r"model|examen|pau|prova", orig, re.I):
            pages.add((ts, orig))
print(len(pages), "pàgines", file=sys.stderr)
# per cada URL de pàgina, agafa un snapshot per any
best = {}
for ts, orig in pages:
    key = (re.sub(r"[?#].*", "", orig.split("://")[-1]).rstrip("/"), ts[:4])
    best.setdefault(key, (ts, orig))
pdfs = set()
for (k, yr), (ts, orig) in sorted(best.items()):
    html = get(f"https://web.archive.org/web/{ts}/{orig}")
    for h in re.findall(r'href="([^"]+\.pdf)"', html, re.I):
        h = re.sub(r"^https?://web\.archive\.org/web/\d+(id_|im_)?/", "", h)
        if h.startswith("/web/"):
            h = re.sub(r"^/web/\d+(id_|im_)?/", "", h)
        u = urllib.parse.urljoin(orig, h)
        if re.search(r"quim", u, re.I):
            pdfs.add(u)
    time.sleep(1)
for u in sorted(pdfs):
    print(u)
print(len(pdfs), "PDF", file=sys.stderr)
