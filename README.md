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

La despesa aproximada del mes es desa a `kv` (`usage/AAAA-MM`) i es veu a «Ajustos». La clau d'OpenAI és al Vault de Supabase (`openai_api_key`).
