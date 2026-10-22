-- Versió aplicada al projecte Supabase «llibre-fq3» (migració llibre_fq3_schema, 14/10/2026).
-- Ampliada amb cursos, docents i cua de revisió: vegeu migrations/20261022_cursos_i_docents.sql.
-- Llibre digital de FQ 3r ESO · base de dades (Supabase / Postgres)
-- Executa-ho una sola vegada al SQL Editor del projecte (o amb el connector).

-- ---------- Perfils ----------
create table if not exists public.profiles (
  id          uuid primary key references auth.users(id) on delete cascade,
  role        text not null default 'student' check (role in ('student','teacher')),
  display_name text not null default '',
  grup        text not null default '',
  code        text,                       -- codi d'accés (només el veu el professorat)
  created_at  timestamptz not null default now()
);

create or replace function public.is_teacher() returns boolean
language sql stable security definer set search_path = public as $$
  select exists(select 1 from public.profiles where id = auth.uid() and role = 'teacher');
$$;

-- ---------- Ajustos (p. ex. càlcul automàtic) ----------
create table if not exists public.settings (
  key   text primary key,
  value jsonb not null,
  updated_at timestamptz not null default now()
);
insert into public.settings(key, value) values ('auto_calc', 'true'::jsonb)
  on conflict (key) do nothing;

-- ---------- Respostes (una fila per apartat) ----------
create table if not exists public.responses (
  student_id   uuid not null references public.profiles(id) on delete cascade,
  worksheet_id text not null,
  item_id      text not null,
  answer       jsonb not null default '{}'::jsonb,
  updated_at   timestamptz not null default now(),
  primary key (student_id, worksheet_id, item_id)
);

-- ---------- Lliuraments (una fila per fitxa) ----------
create table if not exists public.submissions (
  student_id   uuid not null references public.profiles(id) on delete cascade,
  worksheet_id text not null,
  status       text not null default 'draft' check (status in ('draft','submitted','returned')),
  submitted_at timestamptz,
  returned_at  timestamptz,
  photos       jsonb not null default '[]'::jsonb,   -- fotos del full en paper (camins al bucket)
  primary key (student_id, worksheet_id)
);

-- ---------- Retroacció (proposta i nota final) ----------
create table if not exists public.feedback (
  student_id     uuid not null references public.profiles(id) on delete cascade,
  worksheet_id   text not null,
  item_id        text not null,          -- '_global' per al comentari general
  proposal_level text,                   -- proposta automàtica: NA/AS/AN/AE
  proposal_note  text,
  level          text check (level in ('NA','AS','AN','AE')),
  comment        text,
  released       boolean not null default false,
  updated_at     timestamptz not null default now(),
  primary key (student_id, worksheet_id, item_id)
);

-- ---------- Seguretat (RLS) ----------
alter table public.profiles    enable row level security;
alter table public.settings    enable row level security;
alter table public.responses   enable row level security;
alter table public.submissions enable row level security;
alter table public.feedback    enable row level security;

-- perfils: cadascú el seu; el professorat, tots
drop policy if exists p_profiles_sel on public.profiles;
create policy p_profiles_sel on public.profiles for select using (id = auth.uid() or public.is_teacher());
drop policy if exists p_profiles_upd on public.profiles;
create policy p_profiles_upd on public.profiles for update using (public.is_teacher());
-- els alumnes no poden veure el seu propi camp "code" a través de la vista de professorat; el codi ja el coneixen.

-- ajustos: tothom autenticat llegeix; només el professorat escriu
drop policy if exists p_settings_sel on public.settings;
create policy p_settings_sel on public.settings for select using (auth.role() = 'authenticated');
drop policy if exists p_settings_all on public.settings;
create policy p_settings_all on public.settings for all using (public.is_teacher()) with check (public.is_teacher());

-- respostes: l'alumne les seves (i no pot editar una fitxa ja lliurada); el professorat, totes (lectura)
drop policy if exists p_resp_sel on public.responses;
create policy p_resp_sel on public.responses for select using (student_id = auth.uid() or public.is_teacher());
drop policy if exists p_resp_ins on public.responses;
create policy p_resp_ins on public.responses for insert with check (
  student_id = auth.uid() and not exists (
    select 1 from public.submissions s where s.student_id = auth.uid() and s.worksheet_id = responses.worksheet_id and s.status = 'submitted'));
drop policy if exists p_resp_upd on public.responses;
create policy p_resp_upd on public.responses for update using (
  student_id = auth.uid() and not exists (
    select 1 from public.submissions s where s.student_id = auth.uid() and s.worksheet_id = responses.worksheet_id and s.status = 'submitted'));

-- lliuraments
drop policy if exists p_sub_sel on public.submissions;
create policy p_sub_sel on public.submissions for select using (student_id = auth.uid() or public.is_teacher());
drop policy if exists p_sub_ins on public.submissions;
create policy p_sub_ins on public.submissions for insert with check (student_id = auth.uid() and status in ('draft','submitted'));
drop policy if exists p_sub_upd_student on public.submissions;
create policy p_sub_upd_student on public.submissions for update
  using (student_id = auth.uid() and status <> 'submitted')
  with check (student_id = auth.uid() and status in ('draft','submitted'));
drop policy if exists p_sub_upd_teacher on public.submissions;
create policy p_sub_upd_teacher on public.submissions for update using (public.is_teacher());

-- retroacció: l'alumne només la retornada; el professorat, tot
drop policy if exists p_fb_sel on public.feedback;
create policy p_fb_sel on public.feedback for select using ((student_id = auth.uid() and released) or public.is_teacher());
drop policy if exists p_fb_all on public.feedback;
create policy p_fb_all on public.feedback for all using (public.is_teacher()) with check (public.is_teacher());

-- ---------- Fotos (Storage) ----------
insert into storage.buckets (id, name, public) values ('fotos', 'fotos', false)
  on conflict (id) do nothing;

drop policy if exists p_fotos_ins on storage.objects;
create policy p_fotos_ins on storage.objects for insert to authenticated
  with check (bucket_id = 'fotos' and (storage.foldername(name))[1] = auth.uid()::text);
drop policy if exists p_fotos_sel on storage.objects;
create policy p_fotos_sel on storage.objects for select to authenticated
  using (bucket_id = 'fotos' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_teacher()));
drop policy if exists p_fotos_del on storage.objects;
create policy p_fotos_del on storage.objects for delete to authenticated
  using (bucket_id = 'fotos' and (storage.foldername(name))[1] = auth.uid()::text);

-- ---------- Permisos de l'API ----------
grant usage on schema public to authenticated;
grant select, insert, update, delete on public.profiles, public.settings, public.responses, public.submissions, public.feedback to authenticated;
revoke all on public.profiles, public.settings, public.responses, public.submissions, public.feedback from anon;
grant execute on function public.is_teacher() to authenticated;

-- ---------- Professorat ----------
-- Després de crear el teu usuari (Authentication → Users → Add user, amb el teu correu),
-- executa això canviant el correu:
-- insert into public.profiles(id, role, display_name)
--   select id, 'teacher', 'Macià Esteve' from auth.users where email = 'EL_TEU_CORREU'
--   on conflict (id) do update set role = 'teacher';
