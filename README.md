# Física i química · 3r d'ESO

Llibre digital dinàmic de Física i química de 3r d'ESO creat per Macià Esteve Pallarès Pallarès.

Web estàtica: `index.html` + `docs/` (fulls en PDF) + `img/` + `lib/` (visor de PDF).
Conté només el material de l'alumnat.

## Versió digital (`/digital/`)

Llibre amb accés per codi d'alumne, fitxes interactives (editor matemàtic, factors de conversió amb unitats, càlcul automàtic activable), fotos adjuntes i zona del professorat (`/digital/profe.html`) amb correcció assistida.
Dades a Supabase (projecte `llibre-fq3`): esquema a `supabase/schema.sql`, funcions a `supabase/functions/`.
Mode demostració sense servidor: `/digital/?demo` (codis DEMO-0001…0003) i `/digital/profe.html?demo`.

## Zona docent (`/docent/`, també `/2n/docent/` i `/4t/docent/`)

Un sol accés per al professorat dels tres llibres, amb usuari i contrasenya.

- **Administrador** (`maciapallares`): dona d'alta docents, els canvia la contrasenya i veu tots els cursos.
- **Docent**: crea els seus cursos de 2n, 3r o 4t d'ESO i hi dona d'alta l'alumnat. Cada alumne rep un codi d'accés. Un docent només veu l'alumnat dels seus cursos (regles RLS a la base de dades).
- Els cursos de 3r obren la zona del professorat del llibre digital (`/digital/profe.html`), amb un selector de curs. Els llibres digitals de 2n i 4t encara no existeixen.

## Correcció de les fitxes digitals

Quan l'alumne lliura una fitxa, la funció `autocorregeix` la corregeix sencera i l'alumne en veu el resultat de seguida:

1. Respostes buides i apartats que la fitxa comprova sola (càlculs, taules, V/F) es corregeixen sense IA.
2. Les respostes raonades, les errònies i els dibuixos en foto (en baixa resolució) els corregeix OpenAI `gpt-5.4-nano` amb el solucionari de la SdA. Si falla, prova `gpt-5.4-mini`.
3. Totes les fitxes corregides van a la pestanya **Per revisar**: el docent hi pot mirar què ha posat cada alumne i comprovar la IA, una a una («Bé, següent» o «Retorna amb canvis»). Les preguntes on la IA dubta surten marcades. Les fitxes en paper les valora el docent.
4. També valora l'ortografia en català (etiqueta «ortografia») i dona un indici de text copiat d'una IA: l'estil de la resposta segons la IA i els caràcters que l'alumne hi ha enganxat. Només ho veu el docent: al costat de la qualificació surt «IA» i la qualificació que tindria si aquelles preguntes comptessin com a NA.

La despesa aproximada del mes es desa a `kv` (`usage/AAAA-MM`) i es veu a «Ajustos». La clau d'OpenAI és al Vault de Supabase (`openai_api_key`).

## Llibres digitals de 2n i 4t (`/2n/digital/`, `/4t/digital/`)

Fan servir el mateix codi que el de 3r (`digital/js`, `digital/css`), amb les fitxes de cada nivell amb prefix
(`2n:`, `4t:`). Les fitxes digitals es generen a partir dels PDF de `2n/docs` i `4t/docs`, de manera que
**el llibre normal i el digital sempre van acoblats**:

- `tools/digital-pdf/build.py 2n|4t` reconstrueix el llibre digital d'un nivell a partir dels PDF.
- L'acció de GitHub `.github/workflows/llibre-digital.yml` ho fa sola cada vegada que canvia un PDF de
  `2n/docs` o `4t/docs` (o el llibre web) a `main`, i en desa el resultat.
- Si es canvien preguntes d'una fitxa que l'alumnat ja ha respost, les respostes es guarden per número de
  camp: cal evitar canviar l'ordre de les preguntes a mig curs.

## Activitats afegides i correccions dels fulls de 2n i 4t (`tools/fulls-extra/`)

- `continguts/c2n.py` i `c4t.py`: preguntes afegides a la fitxa de cada sessió (pensades perquè la fitxa es
  pugui fer en una hora). No són fulls a part: continuen el mateix full (i la numeració) just després de
  l'última pregunta, a l'espai lliure de l'última pàgina i, si cal, en pàgines noves.
- `continguts/d2n.py` i `d4t.py`: el dossier d'ampliació de cada SdA, amb la mateixa estructura que els de 3r
  (reptes amb etiqueta —Càlcul, Dades, Raonament, Experiment, Història, Investiga, Fermi—, apartats, taules i
  quadrícules per fer gràfiques) i recursos al final. Substitueix el contingut del full d'ampliació original i
  en conserva la capçalera.
- `continguts/fixes.py`: correccions de text fetes directament als PDF.
- `npm install` i després `python3 build.py 2n|4t` (o amb un nom de fitxer per fer-ne només un). Les
  pàgines originals que es modifiquen es guarden dins del PDF, així que les activitats afegides se
  substitueixen cada vegada (no s'acumulen) i els peus de pàgina es tornen a numerar; les correccions s'apliquen una sola vegada.
- Si substitueixes un PDF per una versió nova feta de zero, torna a executar `build.py` per afegir-hi les
  activitats.
- Després de fer push, l'acció de GitHub actualitza les fitxes digitals.
