# Fonts privades de 3r (no es publiquen)

El repositori és públic. Aquests generadors contenen el text de les activitats de demostració d'assoliment,
dels solucionaris, de les adaptacions (PI, dislèxia, TDAH, TEA, discalcúlia, nouvingut) i de l'ampliació amb solucions,
que només ha de veure el professorat. Per això aquesta carpeta està exclosa de git (`.gitignore`).

| Fitxer | Què genera |
| --- | --- |
| `gen_detectius.py` | SdA 1 (fulls, prova, solucionaris) |
| `gen_sda1.py` | SdA 2 (malgrat el nom) i les ajudes comunes `head`, `q`, `lines`, `rub`, `table`, `teacher_note`, `page` |
| `gen_mobil.py` | SdA 3 |
| `gen_hidrogen.py` | SdA 4 |
| `gen_cel.py` | SdA 5 |
| `gen_energia.py` | SdA 6 |
| `mn_ampl.py` | Reptes d'ampliació i solucionari |
| `mn_adapt.py` | Materials adaptats (mesures addicionals i intensives) |

Origen: `kit-llibre-fq-4t.zip` (versió del 20/10/2026). Es poden obtenir de la còpia del kit fora del repositori.

## Xifrar les fonts (mateix esquema que 2n i 4t, sense tocar aquell material)

No facis `tools/material/build.py --fonts` amb aquesta carpeta. Aquella ordre **substitueix**
`tools/material/fonts-privades.bin`, que és el paquet de 2n i 4t, i després només sap construir els PDF d'aquests dos cursos.

El model de xifrat de 2n i 4t no canvia: AES-256-GCM i clau `SHA-256(A^b mod p)`, amb `A` a
`tools/material/clau-publica.json` i `b` a la taula `kv` (camí `clau-material`).

Per deixar els generadors de 3r xifrats al mateix esquema, en local i sense pujar secrets:

1. Un administrador copia el valor `b` de `kv` / `clau-material` i l'exporta a la sessió:
   `export FQ_MATERIAL_B='…'`. No el desis en cap fitxer del repositori ni el posis a la línia d'ordres d'un script que es pugi.
2. Copia els `.py` de la taula (el kit del 20/10/2026) dins `tools/3r/privat/`. El `.gitignore` d'aquesta carpeta no els puja.
3. Executa `python3 tools/3r/xifra_fonts_privat.py`. Escriu `tools/3r/privat/fonts-3r.bin` (també ignorat per git).
4. Esborra els `.py` en clar de la màquina si no els has d'editar. Per tornar-los a tenir cal el mateix `FQ_MATERIAL_B`; el script només xifra, no desxifra.

Els PDF de professorat de 3r que ja existeixen segueixen al bucket `professorat` de Supabase. Aquest pas només protegeix les fonts dels generadors.

Els scripts públics de `tools/3r/generadors/` (p. ex. `gen_curs.py`, `gen_multinivell.py`) importen ajudes de `gen_sda1.py`:
sense aquesta carpeta no s'executen.
