"""Xifra els .py de tools/3r/privat/ amb el mateix esquema que 2n i 4t.

No toca fonts-privades.bin ni els PDF de 2n/4t. El secret no es llegeix d'un fitxer
del repositori: ha d'arribar per l'entorn FQ_MATERIAL_B (taula kv, camí clau-material).

  FQ_MATERIAL_B='…' python3 tools/3r/xifra_fonts_privat.py

Escriu tools/3r/privat/fonts-3r.bin, que el .gitignore d'aquesta carpeta no puja.
"""
import hashlib, io, json, os, sys, tarfile
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
PRIV = os.path.join(HERE, "privat")
OUT = os.path.join(PRIV, "fonts-3r.bin")
PUB = os.path.join(ROOT, "tools", "material", "clau-publica.json")
P = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B"
        "0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE4"
        "5B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F174"
        "6C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA05"
        "1015728E5A8AACAA68FFFFFFFFFFFFFFFF", 16)


def main():
    b = os.environ.get("FQ_MATERIAL_B")
    if not b:
        sys.exit("Cal FQ_MATERIAL_B a l'entorn (el secret b de la taula kv, camí clau-material). No el desis al repositori.")
    fonts = sorted(f for f in os.listdir(PRIV) if f.endswith(".py"))
    if not fonts:
        sys.exit("A tools/3r/privat/ no hi ha cap .py per xifrar. Copia-hi els generadors en local; no els pugis en clar.")
    A = int(json.load(open(PUB, encoding="utf-8"))["A"])
    k = hashlib.sha256(pow(A, int(b), P).to_bytes(256, "big")).digest()
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        for f in fonts:
            t.add(os.path.join(PRIV, f), arcname=f)
    iv = os.urandom(12)
    blob = iv + AESGCM(k).encrypt(iv, buf.getvalue(), None)
    open(OUT, "wb").write(blob)
    print(f"Xifrats {len(fonts)} fitxers a {OUT} (no es puja a git).")


if __name__ == "__main__":
    main()
