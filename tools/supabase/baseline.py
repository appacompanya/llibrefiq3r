"""Reconstrueix la migració de línia base (estat real de la base de dades) a partir d'una còpia de seguretat
de metadades feta amb consultes de només lectura (pg_policies, pg_get_functiondef, information_schema…).

Ús: python3 tools/supabase/baseline.py /ruta/a/backups/2026-10-24 > supabase/migrations/20261024000000_estat_actual.sql
No conté dades ni secrets: només l'estructura."""
import json, sys, os

B = sys.argv[1]
J = lambda n: json.load(open(os.path.join(B, f"meta.{n}.json"))) or []
cols, cons, idx, pols, funcs, trg, rls, bks = (J(n) for n in
    ["columns", "constraints", "indexes", "policies", "functions", "triggers", "rls", "buckets"])

out = []
w = out.append
w("""-- =====================================================================================
-- LÍNIA BASE · JA APLICADA. NO EXECUTAR SOBRE PRODUCCIÓ.
-- Estat real del projecte llibre-fq3 el 24/10/2026, reconstruït amb consultes de només lectura.
-- Recull també els canvis fets a mà que no constaven a l'historial de migracions
-- (cursos_i_docents del 22/10, cua de revisió, regles de kv…).
-- És idempotent (if not exists / create or replace / drop policy if exists) per poder muntar
-- un entorn de proves des de zero. Generat per tools/supabase/baseline.py.
-- =====================================================================================

create schema if not exists privat;
create extension if not exists pg_net with schema extensions;
create extension if not exists pgcrypto with schema extensions;
""")

order = ["profiles", "courses", "settings", "responses", "submissions", "feedback", "kv"]
tables = {}
for c in cols:
    tables.setdefault((c["schema"], c["table"]), []).append(c)
keys = sorted(tables, key=lambda k: (k[0] != "public", order.index(k[1]) if k[1] in order else 99, k[1]))

def coltype(c):
    u = c["udt"]
    return {"int8": "bigint", "int4": "integer", "bool": "boolean", "timestamptz": "timestamptz",
            "text": "text", "uuid": "uuid", "jsonb": "jsonb"}.get(u, u)

for s, t in keys:
    cs = sorted(tables[(s, t)], key=lambda c: c["pos"])
    w(f"-- ---------- {s}.{t} ----------")
    lines = []
    for c in cs:
        d = c["default"]
        ty = coltype(c)
        if d and d.startswith("nextval("):
            ty = "bigserial"; d = None
        l = f"  {c['col']} {ty}"
        if c["nullable"] == "NO": l += " not null"
        if d: l += f" default {d}"
        lines.append(l)
    w(f"create table if not exists {s}.{t} (\n" + ",\n".join(lines) + "\n);")
    # profiles referencia courses i viceversa: les claus foranes van al final
    for k in cons:
        if (k["schema"], k["table"]) == (s, t) and not k["def"].startswith("FOREIGN KEY"):
            w(f"do $$ begin alter table {s}.{t} add constraint {k['name']} {k['def']}; exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;")
    w("")
w("-- ---------- Claus foranes ----------")
for k in cons:
    if k["def"].startswith("FOREIGN KEY"):
        w(f"do $$ begin alter table {k['schema']}.{k['table']} add constraint {k['name']} {k['def']}; exception when duplicate_object or duplicate_table then null; end $$;")
w("\n-- ---------- Índexs ----------")
for i in idx:
    if "_pkey" in i["def"] or "_key ON" in i["def"]: continue
    w(i["def"].replace("CREATE INDEX", "create index if not exists").replace("CREATE UNIQUE INDEX", "create unique index if not exists") + ";")

w("\n-- ---------- Funcions ----------")
FORDER = ["is_admin", "is_teacher", "teaches", "teaches_txt", "my_course", "kv_can_read", "kv_can_write",
          "guard_submission", "genera_imatge", "gen_ses", "genera_imatge4", "gen4", "gen2", "models_req"]
for f in sorted(funcs, key=lambda f: (f["schema"] != "public", FORDER.index(f["name"]) if f["name"] in FORDER else 99, f["name"])):
    d = f["def"].rstrip()
    w(d + ";\n")
w("-- Permisos d'execució tal com són ara (només authenticated i service_role a public.*; privat.* només postgres)")
for f in funcs:
    sig = f"{f['schema']}.{f['name']}({f['args']})"
    acl = f["acl"] or ""
    w(f"revoke all on function {sig} from public, anon;")
    if "authenticated=X" in acl: w(f"grant execute on function {sig} to authenticated;")
    if "service_role=X" in acl: w(f"grant execute on function {sig} to service_role;")

w("\n-- ---------- Disparadors ----------")
for t in trg:
    if t["schema"] != "public": continue
    name = t["def"].split()[2]
    w(f"drop trigger if exists {name} on {t['schema']}.{t['table']};")
    w(t["def"] + ";")

w("\n-- ---------- RLS ----------")
for r in rls:
    w(f"alter table {r['schema']}.{r['table']} {'enable' if r['rls'] else 'disable'} row level security;")

w("\n-- ---------- Polítiques ----------")
for p in sorted(pols, key=lambda p: (p["schemaname"], p["tablename"], p["policyname"])):
    tgt = f"{p['schemaname']}.{p['tablename']}"
    roles = p["roles"] if isinstance(p["roles"], list) else str(p["roles"]).strip("{}").split(",")
    s = f"drop policy if exists {p['policyname']} on {tgt};\ncreate policy {p['policyname']} on {tgt} as {p['permissive'].lower()} for {p['cmd'].lower()} to {', '.join(roles)}"
    if p["qual"]: s += f"\n  using ({p['qual']})"
    if p["with_check"]: s += f"\n  with check ({p['with_check']})"
    w(s + ";")

w("\n-- ---------- Storage ----------")
for b in bks:
    mt = "array[" + ",".join(f"'{m}'" for m in (b["allowed_mime_types"] or [])) + "]" if b["allowed_mime_types"] else "null"
    w(f"insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types) values ('{b['id']}', '{b['name']}', {str(b['public']).lower()}, {b['file_size_limit']}, {mt}) on conflict (id) do nothing;")
w("\n-- Secrets: viuen al Vault de Supabase (openai_api_key, imatges4_token) o a l'entorn de les Edge Functions")
w("-- (ANTHROPIC_API_KEY, SUPABASE_SERVICE_ROLE_KEY). Aquí no n'hi ha cap.")
print("\n".join(out))
