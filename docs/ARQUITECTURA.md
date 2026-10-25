# Arquitectura del repositori

El repositori publica quatre llibres. No és només el de 3r.

| Curs | On és | Com es construeix |
| --- | --- | --- |
| 3r ESO | arrel (`index.html`, `digital/`, `docs/`, `contingut/3r/`) | YAML → `tools/3r/build_dades.py` |
| 2n ESO | `2n/` | PDF de `2n/docs` → `tools/digital-pdf/build.py` |
| 4t ESO | `4t/` | PDF de `4t/docs` → `tools/digital-pdf/build.py` |
| Batxillerat | `btx/` | material propi; aquest document no el descriu |

2n i 4t comparteixen el codi de `digital/js` i `digital/css`. El seu material de professorat va xifrat (AES-256-GCM, clau derivada per Diffie-Hellman). Aquest model no es canvia des d'aquí. Vegeu `tools/material/build.py`.

## 3r: font única

Les sessions, els fulls, les evidències i els criteris viuen a `contingut/3r/*.yaml`.

```bash
python3 tools/3r/build_dades.py --aplica-html --estricte
```

El script escriu `digital/js/dades-generades.js` i, amb `--aplica-html`, copia els blocs `D`, `L`, `SDAS`, `EVAL` i `CRIT_NAMES` dins de `index.html`, `digital/index.html` i `digital/profe.html`.

`dades-generades.js` **no el carrega el navegador**. És la foto intermèdia que el mateix script enganxa a les pàgines. Si es genera sense `--aplica-html`, el fitxer JS queda nou i les pàgines, velles.

`--estricte` acaba amb error si la validació troba avisos (criteris, pesos, CE).

`tools/3r/artefactes.py --check` compara els PDF i les fitxes amb `contingut/3r/artefactes.json`. `--registra` desa l'estat actual.

## Camí antic, retirat

`tools/3r/generadors/template.html` és una còpia anterior del llibre. Aquests scripts s'aturen amb un missatge i no escriuen res, perquè reescriurien la web amb aquella còpia:

- `build_web.py`
- `build_site.py`
- `build_digital.py` (el de 3r; el de 2n i 4t és `tools/digital-pdf/build_digital.py`)
- `build_profe_digital.py`
- `export_links.js`

## PDF del professorat de 3r

Els fulls marcats `professorat: true` es busquen al bucket privat `professorat` de Supabase. Si el bucket no té el fitxer i n'hi ha una còpia a `docs/`, la zona del professorat obre aquesta còpia. És el cas de `docs/sda2-18-adaptada-continguts-basics-fitxa-1.pdf` (fitxa 1 de la SdA 2, continguts bàsics).

Els generadors amb proves i solucionaris no són al git. La carpeta `tools/3r/privat/` només porta la instrucció. No hi ha secrets al repositori.
