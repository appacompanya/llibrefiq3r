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

**Pendent:** desar-les xifrades com les de 2n i 4t (`tools/material/build.py --fonts`, amb el secret `FQ_MATERIAL_B`
que només pot copiar un administrador). No s'ha fet en aquesta fase perquè cal el secret.
Els scripts públics de `tools/3r/generadors/` (p. ex. `gen_curs.py`, `gen_multinivell.py`) importen ajudes de `gen_sda1.py`:
sense aquesta carpeta no s'executen.
