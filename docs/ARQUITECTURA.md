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

`tools/3r/artefactes.py --check` compara els PDF i les fitxes amb `contingut/3r/artefactes.json`. `--registra` desa l'estat actual. El graf de conseqüències és `tools/3r/impacte.py` (secció següent): diu què cal fer i només executa el pas segur.

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

## Interconnexió de 3r

El currículum, les SdA, les sessions, els documents, les evidències i els artefactes formen un graf. `tools/3r/impacte.py` el recorre: donada una peça, llista què queda afectat i quina acció toca. `artefactes.py --check` només compara empremtes; no diu la cadena ni executa res.

```bash
python3 tools/3r/impacte.py consulta REF
python3 tools/3r/impacte.py actua REF
python3 tools/3r/impacte.py comprova
python3 tools/3r/artefactes.py --impacte REF
python3 tools/3r/artefactes.py --actua REF
```

`REF` és un criteri (`2.3`), una CE (`CE2`), una SdA (`sda5`), una sessió (`sessio:5:7` o `sda5 sessio 7`), un uid (`d5f5`, `s5.difu`), un YAML, `full.md`, `mapa_ce`, un PDF de `docs/` o del bucket, o una imatge (`img/sda1-s1.png`).

`actua` només executa un pas, i només si el canvi arriba al web, al mapa o als uid:

```bash
python3 tools/3r/build_dades.py --aplica-html --estricte
```

No regenera PDF i no fa `artefactes.py --registra`: un full no regenerat ha de continuar sortint com a deriva. Els generadors de SdA no són al git (kit de referència del 18/10/2026, anterior al mapa de CE, a la SdA 6 de 8 sessions i als GS/MG). Els que sí són al repo i importen `gen_sda1.py` (`gen_curs.py`, `gen_annexos.py`, `mn_recup.py`, `gen_multinivell.py`) tampoc s'executen. `gen_calendari.py` llegeix `annex_groups.json` (G/M/L), no el booleà `mitja` del YAML. `build_fitxes_auto.py` està aturat.

| Si canvia | Queda afectat | Acció |
| --- | --- | --- |
| Criteri, ítem, evidència, document, sessió, enllaç | Web, `mapa_ce.json`, `uids.json` | `build_dades.py` (segur) |
| Criteri o evidència | PDF de l'instrument i de la rúbrica de la SdA, taules 10-11, `full.md`, annexos | PENDENT MANUAL |
| Sessió (text o GS/MG) | Web. El PDF dels fulls d'aquella sessió no | Segur només el web. `full.md`, `sdas.json`, `annex_groups.json`, annexos i calendari: PENDENT MANUAL |
| Imatge `img/` | Els PDF que la porten | El web la mostra sola. Els PDF: PENDENT MANUAL |
| `full.md` | Annexos i coherència de les taules | PENDENT MANUAL. El web no llegeix aquest fitxer |

`mitja: false` és grup sencer (GS) i `mitja: true` és mig grup (MG). A `annex_groups.json`, L és un laboratori en mig grup: el booleà no el distingeix de M, i per això no es recalcula sol.

### Exemple

Sessió 7 de la SdA 5, difusió, grup sencer:

```text
Si toco sessio:5:7 (GS) → web (SDAS, amb el grup GS/MG) → python3 tools/3r/build_dades.py --aplica-html --estricte
Els PDF d'aquests documents no es regeneren: el text del full no surt del YAML de la sessió: d5f5
Còpies i annexos → PENDENT MANUAL (calendari, professorat/programacio-annexos.pdf, docs/programacio-annexos.pdf, full.md, sdas.json, annex_groups.json)
```

Criteri 2.3 (l'avaluen ítems de les SdA 1, 2 i 5):

```text
Si toco 2.3 → s1.prova.p3 → s1.prova → d1prova → professorat/sda1-13-prova.pdf → PENDENT MANUAL
Pas segur: python3 tools/3r/build_dades.py --aplica-html --estricte
```

Aquest PDF el faria `gen_detectius.py`, que no és al git. La mateixa consulta també marca, entre d'altres, `docs/sda5-07-fitxa-5-difusio-i-gradient.pdf` (`gen_cel.py`, privat; l'ítem és `s5.difu.x2`, la demostració de difusió en grup sencer) i la rúbrica `docs/sda5-14-rubriques.pdf`: no és un instrument de l'evidència, però imprimeix els criteris de la SdA. `python3 tools/3r/impacte.py comprova` tanca aquestes cadenes.

