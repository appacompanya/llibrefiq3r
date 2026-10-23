"""Material del professorat de 2n i 4t (activitats de demostració d'assoliment i solucionaris), xifrat.

El repositori és públic, però aquest material només el pot veure el professorat. Per això:
- Les fonts (els textos de les activitats i dels solucionaris) no són aquí en clar: són a fonts-privades.bin, xifrades.
- Els PDF es publiquen xifrats (AES-256-GCM) a <nivell>/material/*.bin.
- La clau no és enlloc en clar: surt d'un intercanvi Diffie-Hellman (grup MODP de 2048 bits de l'RFC 3526). El secret b
  és a la base de dades (taula kv, camí «clau-material»), que només pot llegir el professorat; la part pública (A i B)
  és a clau-publica.json. Clau = SHA-256(A^b mod p). La zona del professorat llegeix b, calcula la clau, desxifra el
  PDF al navegador i l'obre.

Ús (cal el secret b a la variable FQ_MATERIAL_B; un administrador el pot copiar de la taula kv):
  python3 build.py               desxifra les fonts, genera els PDF i els torna a xifrar
  python3 build.py --fonts DIR   fa servir les fonts d'una carpeta en clar i les desa xifrades a fonts-privades.bin
  python3 build.py --extreu DIR  desxifra les fonts a DIR (per editar-les)
Després cal pujar el JSON «solucions-<nivell>.json» que s'escriu a la carpeta temporal a la taula kv («solucions-2n», «solucions-4t»),
que fa servir la correcció automàtica."""
import os, re, sys, io, json, base64, hashlib, tarfile, tempfile, importlib, subprocess, html
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
FX = os.path.join(ROOT, "tools", "fulls-extra")
sys.path.insert(0, FX)
import estil

BUNDLE = os.path.join(HERE, "fonts-privades.bin")


P = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B"
        "0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE4"
        "5B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F174"
        "6C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA05"
        "1015728E5A8AACAA68FFFFFFFFFFFFFFFF", 16)


def key():
    if os.environ.get("FQ_MATERIAL_KEY"):            # clau ja derivada (base64)
        return base64.b64decode(os.environ["FQ_MATERIAL_KEY"])
    b = os.environ.get("FQ_MATERIAL_B")
    if not b: raise SystemExit("Cal el secret b a FQ_MATERIAL_B (taula kv, camí «clau-material»).")
    A = int(json.load(open(os.path.join(HERE, "clau-publica.json")))["A"])
    return hashlib.sha256(pow(A, int(b), P).to_bytes(256, "big")).digest()


def enc(data, k):
    iv = os.urandom(12)
    return iv + AESGCM(k).encrypt(iv, data, None)


def dec(blob, k):
    return AESGCM(k).decrypt(blob[:12], blob[12:], None)


def pack(src, k):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        for f in sorted(os.listdir(src)):
            if f.endswith(".py"): t.add(os.path.join(src, f), arcname=f)
    open(BUNDLE, "wb").write(enc(buf.getvalue(), k))


def unpack(dst, k):
    os.makedirs(dst, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(dec(open(BUNDLE, "rb").read(), k)), mode="r:gz") as t:
        t.extractall(dst, filter="data")


def sol_html(items):
    """Solucionari amb criteris: resposta de cada activitat i com es valora."""
    out = []
    for n, ans, crit, levels in items:
        lv = "".join(f"<li>{html.escape(x.strip())}</li>" for x in re.split(r"(?=\b(?:AE|AN|AS|NA):)", levels) if x.strip())
        out.append(f'<div class="q" style="break-inside:avoid"><span class="n">{n}</span><div><p>{html.escape(ans)}</p>'
                   f'<div class="sol"><p><b>Criteri {html.escape(crit)}.</b> Com es valora:</p><ul>{lv}</ul></div></div></div>')
    note = ('<p class="intro">Cada activitat indica el criteri d\'avaluació. Per a cada criteri, el nivell (NA, AS, AN, AE) es decideix amb '
            'el conjunt de les activitats que el mostren, seguint la rúbrica de la SdA. No hi ha percentatges ni notes numèriques.</p>')
    return note + "".join(out)


def amp_html(text):
    out = []
    for line in text.strip().split("\n"):
        m = re.match(r"(\d+)\. ([^:]+?) \(([^)]+)\): (.*)", line)
        if not m: raise SystemExit("Línia de solucionari no reconeguda: " + line[:60])
        n, t, tag, body = m.groups()
        body = html.escape(body)
        body = re.sub(r"(?<=[ .])([a-h])\) ", r"<br><b>\1)</b> ", body)
        out.append(f'<div class="q" style="break-inside:avoid"><span class="n">{n}</span><div><p><span class="tag">{html.escape(tag)}</span> '
                   f'<b>{html.escape(t)}.</b></p><p>{body}</p></div></div>')
    return ('<p class="intro">Respostes dels reptes del dossier d\'ampliació. Als reptes oberts («Investiga», «Experiment»…) es dona una '
            'resposta model: s\'accepta qualsevol resposta ben raonada i, si cal, amb la font citada.</p>' + "".join(out))


def main():
    args = sys.argv[1:]
    k = key()
    if args[:1] == ["--extreu"]:
        unpack(args[1], k); print("Fonts desxifrades a", args[1]); return
    if args[:1] == ["--fonts"]:
        src = args[1]; pack(src, k)
    else:
        src = tempfile.mkdtemp(prefix="material-"); unpack(src, k)
    sys.path.insert(0, src)
    tmp = tempfile.mkdtemp(prefix="material-pdf-")
    jobs, docs = [], {}
    for lv in ("2n", "4t"):
        A = importlib.import_module(f"a{lv}")
        S = importlib.import_module(f"sol{lv}")
        docs[lv] = []
        for n in range(1, 7):
            items = [
                (f"{lv}-sda{n}-activitat.pdf", "Activitat de demostració d'assoliment",
                 estil.header(lv, n, A.TITLE) + A.ACT[n]),
                (f"{lv}-sda{n}-solucionari-activitat.pdf", "Solucionari amb criteris de l'activitat de demostració",
                 estil.header(lv, n, "Solucionari de l'activitat de demostració", "Professorat") + sol_html(A.SOL[n])),
                (f"{lv}-sda{n}-solucionari-ampliacio.pdf", "Solucionari dels reptes d'ampliació",
                 estil.header(lv, n, "Solucionari dels reptes d'ampliació", "Professorat") + amp_html(S.AMP[n])),
            ]
            for f, label, body in items:
                hp = os.path.join(tmp, f.replace(".pdf", ".html"))
                open(hp, "w", encoding="utf-8").write(estil.page(lv, n, body))
                jobs.append({"html": hp, "pdf": hp.replace(".html", ".pdf"), "footer": estil.footer_num(lv, n)})
                docs[lv].append({"f": f.replace(".pdf", ".bin"), "l": label, "sda": n, "nom": f})
        json.dump({str(n): {"amp": S.AMP[n].strip()} for n in range(1, 7)}, open(os.path.join(tmp, f"solucions-{lv}.json"), "w"), ensure_ascii=False)
    jp = os.path.join(tmp, "feines.json"); json.dump(jobs, open(jp, "w"))
    subprocess.run(["node", os.path.join(FX, "render.js"), jp], check=True)
    for lv in docs:
        out = os.path.join(ROOT, lv, "material"); os.makedirs(out, exist_ok=True)
        for d in docs[lv]:
            pdf = open(os.path.join(tmp, d["nom"]), "rb").read()
            open(os.path.join(out, d["f"]), "wb").write(enc(pdf, k))
        js = "/* Generat per tools/material/build.py. Material del professorat xifrat: la zona del professorat el desxifra. */\n"
        js += "window.FQ_MATERIAL = " + json.dumps(docs[lv], ensure_ascii=False) + ";\n"
        js += "window.FQ_MATERIAL_A = " + json.dumps(json.load(open(os.path.join(HERE, "clau-publica.json")))["A"]) + ";\n"
        open(os.path.join(ROOT, lv, "digital", "js", "material.js"), "w", encoding="utf-8").write(js)
        print(lv, len(docs[lv]), "documents xifrats")
    print("PDF en clar (per revisar) i JSON de solucions a:", tmp)


if __name__ == "__main__":
    main()
