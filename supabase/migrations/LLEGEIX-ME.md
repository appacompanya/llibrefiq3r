# Migracions de la base de dades (projecte llibre-fq3)

| Fitxer | Estat |
| --- | --- |
| `20261014201302_llibre_fq3_schema.sql` … `20261020173544_gen2_imatges_2n.sql` | Aplicades (consten a l'historial de Supabase). Recuperades de les converses. |
| `20261022_cursos_i_docents.sql` | Aplicada **a mà** (no consta a l'historial). |
| `20261024000000_estat_actual.sql` | **Línia base, ja aplicada.** Estat real del 24/10/2026 reconstruït amb consultes de només lectura (`tools/supabase/baseline.py`). És la referència de veritat de l'estructura. No s'ha d'executar sobre producció. |
| `historic/20261015_autocorreccio.sql` | No present a la base de dades real. Només com a referència. |
| `pending/` | **Preparades, NO aplicades.** Cal revisar-les i aprovar-les abans d'aplicar-les. |

Cap fitxer conté claus: els secrets són al Vault (`openai_api_key`, `imatges4_token`) o a l'entorn de les Edge Functions.
