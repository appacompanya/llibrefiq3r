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
  - **Construcció del web:** `build_web.py` (plantilla → `index.html` i `profe.html`), `build_site.py` (web estàtica) i `export_links.js` (`links.json`).
  - **Llibre digital:** `build_digital.py`, `build_fitxes_auto.py` (converteix els fulls HTML en fitxes en línia amb camps) i `build_profe_digital.py`.
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

1. `python3 build_web.py`
2. `python3 build_site.py`
3. Copiar el web al repositori.
4. `python3 build_digital.py`
5. `python3 build_fitxes_auto.py`
6. `python3 build_profe_digital.py`
7. Programació: `python3 build_prog_final.py`, convertir a PDF amb `soffice --headless --convert-to pdf` i passar `fix_toc.py` dues vegades.
8. `python3 gen_calendari.py`, `python3 gen_annex_extra.py` i `python3 gen_annexos.py`.
9. Animacions: `python3 gen_anims.py`. Llibre imprès: `node export_links.js` i `python3 gen_llibre.py`.

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
