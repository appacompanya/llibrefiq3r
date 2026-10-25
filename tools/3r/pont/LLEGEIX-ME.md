# Pont del bucket «professorat» (Supabase llibre-fq3)

Els PDF del professorat (activitats de demostració, solucionaris, adaptats, annexos) viuen al bucket
privat `professorat`. Claude els puja i baixa sense demanar res al professor amb la funció
`supabase/functions/professorat-pont`, que només s'activa des de SQL (`net.http_post`) amb el token
del vault `professorat_pont_token`. El token no surt mai de la base de dades.

## Baixar fitxers del bucket
```sql
select net.http_post(url := 'https://pwqyqwiwarffzdkblglt.supabase.co/functions/v1/professorat-pont',
  body := jsonb_build_object('t', (select decrypted_secret from vault.decrypted_secrets where name = 'professorat_pont_token'),
                             'accio', 'baixa', 'fitxers', jsonb_build_array('sda3-13-prova.pdf')),
  headers := '{"Content-Type":"application/json"}'::jsonb, timeout_milliseconds := 150000);
-- uns segons després (net._http_response guarda el registre):
select b64 from privat.pujades where cami = 'sda3-13-prova.pdf' and direccio = 'baixada' order by id desc limit 1;
-- en acabar: delete from privat.pujades where direccio = 'baixada';
```

## Pujar fitxers
- **Públics (també a `docs/`)**: `accio: 'copia_web'` copia `https://llibrefiq3r.cat/docs/<fitxer>` (cal que el
  canvi ja sigui a `main` i publicat).
- **Privats**: xifra'ls amb `xifra.py` (clau del vault `professorat_pont_clau`), puja els `.enc` a la carpeta
  `xifrat/` de la branca de pas `tmp-pont-xifrat` i crida `accio: 'copia_xifrat', 'branca': 'tmp-pont-xifrat'`.
  Després buida la branca (commit que esborra `xifrat/`).
- **Petits**: insereix `(cami, direccio='puja', b64)` a `privat.pujades` i crida `accio: 'puja'`.

Després de pujar: refresca `contingut/3r/generat/bucket-professorat.json` des de `storage.objects` i fes
`python3 -B tools/3r/artefactes.py --registra-nomes professorat/<fitxer>`.

## Retocs mínims de PDF publicats
`retoca_digit.py IN OUT "context|posició|nou"` canvia un sol caràcter (p. ex. un número de sessió o de criteri)
sense regenerar el PDF, amb la mateixa font (Atkinson Hyperlegible). Serveix quan el generador privat està
desfasat respecte del PDF publicat.
