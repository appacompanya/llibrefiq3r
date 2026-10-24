-- HISTÒRICA · NO APLICADA (o desfeta): a la base de dades real no hi ha les taules autocorr i solucions
-- ni la funció public.openai_key(); la correcció automàtica fa servir kv (solucions*) i el Vault.
-- Recuperada de la conversa «Procés selectiu docents 2026» (15/10/2026). Es conserva només com a referència.

create table if not exists public.autocorr (
  student_id   uuid not null references public.profiles(id) on delete cascade,
  worksheet_id text not null,
  item_id      text not null,
  level        text check (level in ('NA','AS','AN','AE')),
  note         text,
  created_at   timestamptz not null default now(),
  primary key (student_id, worksheet_id, item_id)
);
alter table public.autocorr enable row level security;
drop policy if exists p_auto_sel on public.autocorr;
create policy p_auto_sel on public.autocorr for select using (student_id = auth.uid() or public.is_teacher());
grant select on public.autocorr to authenticated;
revoke all on public.autocorr from anon;

create table if not exists public.solucions (
  worksheet_id text primary key,
  text         text not null
);
alter table public.solucions enable row level security;
drop policy if exists p_sol_sel on public.solucions;
create policy p_sol_sel on public.solucions for select using (public.is_teacher());
grant select on public.solucions to authenticated;
revoke all on public.solucions from anon;

create or replace function public.openai_key() returns text
language sql stable security definer set search_path = public, vault as $$
  select decrypted_secret from vault.decrypted_secrets where name = 'openai_api_key' limit 1;
$$;
revoke all on function public.openai_key() from public, anon, authenticated;
grant execute on function public.openai_key() to service_role;