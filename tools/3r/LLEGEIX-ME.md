# Kit del llibre de Física i química (base: llibre de 3r d'ESO)

Codi font amb què es van generar el llibre de 3r (llibrefiq3r.cat), el llibre digital, la zona del professorat, la programació i els annexos.
Serveix de plantilla per fer un llibre nou: es canvien els continguts i es manté l'estructura.

## Carpetes

- **`generadors/`**
  - **Plantilla del llibre web:** `template.html`, que conté les dades `D` (fulls), `L` (enllaços), `SDAS` (sessions de cada SdA), `EVAL` (evidències i rúbriques del registre) i el registre del professorat.
  - **Fulls en PDF, un fitxer per SdA:** `gen_detectius.py` (SdA 1), `gen_sda1.py` (SdA 2, malgrat el nom), `gen_mobil.py` (SdA 3), `gen_hidrogen.py` (SdA 4), `gen_cel.py` (SdA 5) i `gen_energia.py` (SdA 6).
    - Cada fitxer té una llista `DOCS` de parells (nom del PDF, funció que retorna l'HTML).
    - Es renderitza amb Playwright i Chromium.
    - Ajudes comunes a `gen_sda1.py`: `head`, `q`, `lines`, `rub`, `table`, `teacher_note`, `page`.
  - **Altres generadors:**
    - `gen_curs.py`: sessió 0, sessió de tancament, enquesta, formulari i glossari.
    - `gen_multinivell.py`, amb `mn_ampl.py`, `mn_adapt.py` i `mn_recup.py`: ampliació, materials adaptats i tasques de recuperació per CE.
    - `ruta.py`: full de ruta.
    - `figs.py`: pictogrames GHS i figures.
    - `unitfrac.py`: unitats en forma de fracció.
  - **Animacions i simuladors propis (sense so, en català):**
    - `gen_anims.py` genera les animacions pas a pas (`sim-ajust`, `sim-enllac`, `sim-colisions`, `sim-pila`, `sim-mrua`) a partir de `anims/_shell.html` i un fitxer `anims/<nom>.js` per animació (llista `steps`, cada pas amb text i funció de dibuix).
    - També genera els laboratoris interactius de MRU i MRUA (`anims/_lab_moviment.html`): l'alumne tria els valors i veu la pista, les gràfiques i la taula alhora.
    - `sim-gasos.html` i `sim-bateria.html` són simuladors fets a mà.
  - **Llibre imprès (DIN A4, color, wire-o):** `gen_llibre.py` munta tots els fulls amb portada, pàgines pròpies, QR dels recursos digitals i píndoles d'informació (`llibre_pindoles.py`).
  - **Construcció del web (retirada):** `build_web.py`, `build_site.py`, `build_digital.py`, `build_profe_digital.py` i `export_links.js` s'aturen i no reescriuen la web. La font és `contingut/3r/*.yaml` i el pipeline és `build_dades.py --aplica-html` (més avall). `build_fitxes_auto.py` continua al kit, però escriu a una ruta antiga, no al `digital/js/fitxes-auto.js` publicat.
  - **Programació (Word):**
    - `build_prog_final.py` transforma el Word base amb l'ajuda de `prog_edit.py`;
    - `prog_links.py` posa els hiperenllaços;
    - `fix_toc.py` actualitza els números de pàgina de l'índex.
  - **Annexos:**
    - `gen_annexos.py`: fitxes resum de les SdA i muntatge final;
    - `annex_samples.py`: fulls de mostra en Arial, a 9 punts com a mínim;
    - `gen_annex_extra.py`: llibre digital, tipus d'activitats, diversitat i coavaluació;
    - `gen_calendari.py`: calendari horitzontal, amb programació dinàmica de les sessions.
- **Recursos dins del llibre:** a `template.html`, cada enllaç de `L` pot portar `v` (vídeo directe), `img` (imatge), `an:1` (animació o simulador propi) o `fr:1` (web que es pot incrustar). Les simulacions PhET s'incrusten soles. S'obren en una finestra dins del llibre (`<dialog id="vidDlg">`). Les webs que no es poden incrustar s'obren en una pestanya nova.
- **`llibre-digital/`:** el llibre digital (`js/store.js` és la capa de dades, amb Supabase o mode demostració). `js/config.js` porta la URL i la clau pública del projecte de 3r: **cal canviar-les** pel projecte nou.
- **`supabase/`:** `schema.sql` (taules i regles RLS) i les funcions (correcció automàtica i gestió d'alumnes). Les claus van a l'entorn o al Vault, mai al codi.
- **`dades/`:**
  - `full.md`: text de la programació de 3r, que fa servir `gen_annexos.py`;
  - `sdas.json`: repte i metadades de cada SdA.
- **`model-programacio/`:** la programació de 3r en Word, en el format legal (model de format i d'estructura), els annexos en PDF i una mostra de 12 pàgines del llibre imprès.
- **`cdn/`:** paquets locals de mathlive i de supabase-js, per provar sense xarxa.

## Ordre de construcció (3r)

La web publicada no surt de `template.html`. `build_web.py`, `build_site.py`, `build_digital.py`,
`build_profe_digital.py` i `export_links.js` s'aturen: reescriurien el llibre amb la còpia vella.

1. Edita `contingut/3r/*.yaml`.
2. `python3 tools/3r/build_dades.py --aplica-html --estricte` (des de l'arrel del repositori).
3. `python3 tools/3r/artefactes.py --check` i, si els PDF nous són els bons, `--registra`.

`digital/js/dades-generades.js` és la foto intermèdia. El navegador no el carrega: `--aplica-html` enganxa els blocs a les pàgines. Vegeu `docs/ARQUITECTURA.md`.

Els PDF, la programació i els annexos segueixen els generadors d'aquesta carpeta (`build_prog_final.py`, `gen_annexos.py`, `gen_calendari.py`, `gen_anims.py`, `gen_llibre.py`). `node export_links.js` està retirat.

## Coses a tenir en compte (lliçons apreses)

- **Rutes absolutes:** alguns scripts porten rutes absolutes de l'entorn antic (`/home/claude/...` i una carpeta temporal `scratchpad`). Cal adaptar-les.
- **Compressió d'imatges dels PDF** (`rewrite_images` de pymupdf): pot trencar les trames CSS. Fes servir colors plans i comprova cada pàgina després de comprimir.
- **BeautifulSoup** passa `viewBox` a minúscules: tracta les dues formes.
- **Artefactes:** no serveixen fitxers `.xlsx`. Enllaça'ls amb una URL absoluta del web.
- **Proves locals:** les CDN poden estar bloquejades. Serveix mathlive en local i bloqueja supabase perquè funcioni el mode demostració.
- **Enllaços a les capçaleres fosques del Word:** en blanc i subratllats.
- **Format legal:** cos de la programació ≤ 70 pàgines, annexos ≤ 20, Arial 11 i taules a 9 punts.

## Al repositori (24/10/2026)

- `tools/3r/generadors/`: els scripts públics del kit (versió del 20/10). Els simuladors `sim-*.html` no s'hi copien perquè ja són a l'arrel del web (idèntics).
- `tools/3r/privat/`: generadors amb proves, solucionaris i adaptacions. **No es pugen** (repositori públic); vegeu `privat/LLEGEIX-ME.md`.
- `tools/3r/dades/`: `full.md` (text de la programació) i `sdas.json`.
- Les rutes absolutes antigues (`/home/claude`, `scratchpad`) encara hi són a `gen_annexos.py`, `annex_fitxes.py`, `annex_samples.py` i `gen_llibre.py`.
- La font única de les dades és ara `contingut/3r/` (vegeu `docs/ARQUITECTURA.md`): `build_dades.py` en genera `digital/js/dades-generades.js` i `artefactes.py` diu què cal regenerar.
- Diferències del kit (20/10) amb el web publicat (font de veritat): `digital/profe.html` (1 línia: `isStaff`), `js/profe.js` (~190 línies), `js/store.js` (~210), `js/fitxa.js`, `js/alumne.js`, `css/profe.css`, `css/fitxa.css`: són els canvis del 22-23/10 (cursos i docents, cua «Per revisar», ortografia i indici d'IA). `template.html` és anterior a aquests canvis.

## Imatges: una sola còpia (25/10/2026)

- Cada imatge és **un sol fitxer a `img/`** (arrel del web). El seu identificador és el camí dins de `img/` (p. ex. `sda2-s3.png`, `ghs/ghs03.png`).
- El web (`index.html`, `digital/`, `profe.html`, `digital/js/fitxes-auto.js`) l'enllaça com a `img/<id>` o `../img/<id>`. S'han eliminat les còpies de `digital/fimg/` (70) i `tools/3r/generadors/img/` (10).
- Els generadors de PDF la demanen a `tools/3r/lib/imatges.py` (`IM.uri(id)`, `IM.DIR`) i, en renderitzar cada PDF, desen quines imatges conté a `contingut/3r/generat/imatges-us.json`.
- `artefactes.py` guarda el hash de les imatges de cada PDF; si una canvia, `--check` diu `CAL REGENERAR … (imatge img/<id> canviada)` per a cada PDF afectat.
- **Per substituir una imatge:** sobreescriu `img/<id>` amb el mateix nom → `python3 tools/3r/artefactes.py --check` → regenera els PDF que surten → `--registra-imatges` (o `--registra` quan tot estigui al dia). El web la mostra nova sense fer res més.
- `supabase/functions/imatges4` és dels llibres de 2n i 4t (imatges generades, versionades per nom a `privat.imatges4`): no afecta 3r.

## Adaptacions per perfil (NESE)

- El docent assigna el perfil de cada alumne a la zona del professorat («Alumnat i codis» → botó d'adaptació). Es desa a `profiles.adaptacions` (l'alumne només el llegeix). Perfils: `dislexia`, `nouvingut`, `basics`, `discalculia`, `tdah`, `tea`.
- L'alumne tria «Fitxes: Digital / Paper» a la barra superior del llibre (`preferencies.mode_fitxes`). En paper, els botons obren el PDF original o, si té adaptació, la vista imprimible adaptada (`#paper-<fitxa>`).
- `digital/js/adaptacions.js` aplica les adaptacions automàtiques a totes les fitxes. `contingut/3r/adaptacions.yaml` conté el glossari per SdA i, per fitxa i perfil, `no_cal` o el contingut d'una versió adaptada (`abans`, i per pregunta `exemple`, `passos`, `pistes`, `frases`, `paraules`, `model`). Després d'editar-lo: `python3 -B tools/3r/build_adaptacions.py`.
- Criteris: document «Adaptacions del llibre digital: criteris per perfil».
