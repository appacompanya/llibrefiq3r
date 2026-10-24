-- =====================================================================================
-- PREPARADA · NO APLICADA. Cal revisió i aprovació explícita abans d'executar-la.
-- Fase 2 de l'arquitectura de dades del llibre de 3r (llibre-fq3).
--
-- Decisió de l'usuari (24/10/2026): VARIANT A.
--   · Cada docent, també l'administrador (maciapallares), veu NOMÉS l'alumnat dels seus cursos:
--     teaches() = el curs de l'alumne té teacher_id = auth.uid(). Sense excepció per a l'administrador
--     a les dades de l'alumnat (profiles d'alumnes, responses, submissions, feedback, avaluacions,
--     kv d'alumnes, fotos).
--   · is_admin() només serveix per gestionar: crear i esborrar docents i canviar rols.
--   · Qualsevol docent crea els seus cursos (teacher_id = auth.uid()) i hi dona d'alta l'alumnat.
--   · Nota: avui maciapallares és el docent dels 3 cursos (3r B, 2n B, 4t ESO) i dels 23 alumnes,
--     així que els continua veient perquè en són el docent, no perquè sigui administrador.
--
-- Què fa:
--   1. teaches()/teaches_txt() sense excepció per a l'administrador.
--   2. profiles: l'administrador només veu i modifica perfils de docents; els canvis de rol només
--      els pot fer l'administrador i mai sobre comptes d'alumne (disparador guard_profile).
--   3. courses: cada docent crea, modifica i esborra només els seus cursos; no es pot esborrar un curs
--      amb alumnat (abans quedava orfe). L'administrador continua veient la llista de cursos (nom i docent),
--      no l'alumnat.
--   4. Versions: item_version a responses i feedback, worksheet_version a submissions (per defecte 1,
--      que és la versió de tot el contingut actual) i taula responses_arxiu per conservar respostes
--      d'una versió anterior quan una pregunta canvia de fons.
--   5. feedback.graded_by i graded_at (qui ha posat la nota), omplerts per un disparador.
--   6. Taula avaluacions (registre d'avaluació per ítem d'evidència, amb uid i versió) amb RLS via teaches().
--   7. kv: usage/ només l'administrador; data/users/<uid> només el propietari (sense excepció d'administrador).
--   8. privat.gen_ses amb search_path fix; permisos d'execució revisats.
-- No esborra cap dada. Totes les files actuals queden amb versió 1.
-- =====================================================================================

begin;

-- ---------- 1. Funcions de permisos (variant A) ----------
create or replace function public.teaches(sid uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists(
    select 1 from public.profiles p join public.courses c on c.id = p.course_id
    where p.id = sid and p.role = 'student' and c.teacher_id = auth.uid());
$$;

create or replace function public.teaches_txt(sid text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists(select 1 from public.profiles p where p.id::text = sid and public.teaches(p.id));
$$;

-- el docent que crida és el propietari d'aquest curs
create or replace function public.owns_course(cid uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists(select 1 from public.courses c where c.id = cid and c.teacher_id = auth.uid());
$$;

-- ---------- 2. profiles ----------
drop policy if exists p_profiles_sel on public.profiles;
create policy p_profiles_sel on public.profiles for select using (
  id = (select auth.uid())
  or public.teaches(id)
  or (public.is_admin() and role in ('teacher', 'admin')));

drop policy if exists p_profiles_upd on public.profiles;
create policy p_profiles_upd on public.profiles for update
  using (public.teaches(id) or (public.is_admin() and role in ('teacher', 'admin')))
  with check (
    (role = 'student' and public.teaches(id) and (course_id is null or public.owns_course(course_id)))
    or (public.is_admin() and role in ('teacher', 'admin')));

-- Canvis de rol: només l'administrador, només entre docent i administrador, mai sobre un alumne.
-- Un docent no pot posar un alumne en un curs d'un altre docent.
create or replace function public.guard_profile() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is null then return new; end if;            -- service_role (Edge Functions): ja validen
  if new.role is distinct from old.role then
    if not public.is_admin() or old.role = 'student' or new.role = 'student' or old.id = auth.uid() then
      raise exception 'canvi de rol no permès';
    end if;
  end if;
  if new.course_id is distinct from old.course_id and new.course_id is not null and not public.owns_course(new.course_id) then
    raise exception 'el curs no és teu';
  end if;
  if new.id is distinct from old.id or (new.username is distinct from old.username and not public.is_admin()) then
    raise exception 'camp no modificable';
  end if;
  return new;
end $$;
drop trigger if exists profiles_guard on public.profiles;
create trigger profiles_guard before update on public.profiles for each row execute function public.guard_profile();

-- ---------- 3. courses ----------
drop policy if exists p_courses_sel on public.courses;
create policy p_courses_sel on public.courses for select using (
  teacher_id = (select auth.uid()) or id = public.my_course() or public.is_admin());
drop policy if exists p_courses_ins on public.courses;
create policy p_courses_ins on public.courses for insert with check (
  public.is_teacher() and teacher_id = (select auth.uid()));
drop policy if exists p_courses_upd on public.courses;
create policy p_courses_upd on public.courses for update
  using (teacher_id = (select auth.uid()))
  with check (teacher_id = (select auth.uid()));
drop policy if exists p_courses_del on public.courses;
create policy p_courses_del on public.courses for delete using (
  teacher_id = (select auth.uid())
  and not exists (select 1 from public.profiles p where p.course_id = courses.id));
-- el docent no ha d'escriure teacher_id: es força al de qui crida
alter table public.courses alter column teacher_id set default auth.uid();

-- ---------- 4. Versions ----------
alter table public.responses   add column if not exists item_version int not null default 1;
alter table public.feedback    add column if not exists item_version int not null default 1;
alter table public.submissions add column if not exists worksheet_version int not null default 1;

create table if not exists public.responses_arxiu (
  student_id   uuid not null references public.profiles(id) on delete cascade,
  worksheet_id text not null,
  item_id      text not null,
  item_version int  not null,
  answer       jsonb not null,
  updated_at   timestamptz not null,
  archived_at  timestamptz not null default now(),
  primary key (student_id, worksheet_id, item_id, item_version)
);
alter table public.responses_arxiu enable row level security;
drop policy if exists p_arxiu_sel on public.responses_arxiu;
create policy p_arxiu_sel on public.responses_arxiu for select using (
  student_id = (select auth.uid()) or public.teaches(student_id));
revoke all on public.responses_arxiu from anon;
grant select on public.responses_arxiu to authenticated;

-- Quan una pregunta canvia de fons (versio nova al YAML): arxiva les respostes antigues i deixa la fila
-- lliure per a la versió nova. Només des de service_role (script de publicació), mai des del navegador.
create or replace function public.arxiva_item(p_ws text, p_item text, p_nova int) returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  insert into public.responses_arxiu (student_id, worksheet_id, item_id, item_version, answer, updated_at)
    select student_id, worksheet_id, item_id, item_version, answer, updated_at
    from public.responses where worksheet_id = p_ws and item_id = p_item and item_version < p_nova
  on conflict do nothing;
  get diagnostics n = row_count;
  delete from public.responses where worksheet_id = p_ws and item_id = p_item and item_version < p_nova;
  -- el feedback es conserva tal com és, amb la seva item_version
  return n;
end $$;
revoke all on function public.arxiva_item(text, text, int) from public, anon, authenticated;
grant execute on function public.arxiva_item(text, text, int) to service_role;

-- ---------- 5. Qui posa la nota ----------
alter table public.feedback add column if not exists graded_by uuid references public.profiles(id) on delete set null;
alter table public.feedback add column if not exists graded_at timestamptz;
create or replace function public.set_graded_by() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is not null and public.is_teacher() and (
       tg_op = 'INSERT' and (new.level is not null or new.comment is not null)
    or tg_op = 'UPDATE' and (new.level is distinct from old.level or new.comment is distinct from old.comment)) then
    new.graded_by := auth.uid(); new.graded_at := now();
  end if;
  return new;
end $$;
drop trigger if exists feedback_graded_by on public.feedback;
create trigger feedback_graded_by before insert or update on public.feedback for each row execute function public.set_graded_by();

-- ---------- 6. Registre d'avaluació ----------
create table if not exists public.avaluacions (
  id            bigint generated always as identity primary key,
  student_id    uuid not null references public.profiles(id) on delete cascade,
  course_id     uuid references public.courses(id) on delete set null,
  evidencia_uid text not null,             -- p. ex. s1.prova (contingut/3r/sda/sda1.yaml)
  item_uid      text not null,             -- p. ex. s1.prova.p1
  versio        int  not null default 1,   -- versio de l'ítem al YAML
  level         text check (level in ('NA','AS','AN','AE')),
  comment       text,
  graded_by     uuid default auth.uid() references public.profiles(id) on delete set null,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  unique (student_id, item_uid, versio)
);
create index if not exists avaluacions_course_idx on public.avaluacions(course_id);
alter table public.avaluacions enable row level security;
drop policy if exists p_aval_sel on public.avaluacions;
create policy p_aval_sel on public.avaluacions for select using (public.teaches(student_id));
drop policy if exists p_aval_ins on public.avaluacions;
create policy p_aval_ins on public.avaluacions for insert with check (
  public.teaches(student_id) and graded_by = (select auth.uid())
  and course_id is not distinct from (select p.course_id from public.profiles p where p.id = student_id));
drop policy if exists p_aval_upd on public.avaluacions;
create policy p_aval_upd on public.avaluacions for update
  using (public.teaches(student_id))
  with check (public.teaches(student_id) and graded_by = (select auth.uid()));
drop policy if exists p_aval_del on public.avaluacions;
create policy p_aval_del on public.avaluacions for delete using (public.teaches(student_id));
create or replace function public.touch_avaluacio() returns trigger
language plpgsql set search_path = public as $$
begin new.updated_at := now(); if auth.uid() is not null then new.graded_by := auth.uid(); end if; return new; end $$;
drop trigger if exists avaluacions_touch on public.avaluacions;
create trigger avaluacions_touch before update on public.avaluacions for each row execute function public.touch_avaluacio();
revoke all on public.avaluacions from anon;
grant select, insert, update, delete on public.avaluacions to authenticated;

-- ---------- 7. kv ----------
create or replace function public.kv_can_read(p text) returns boolean
language sql stable security definer set search_path = public as $$
  select public.is_teacher() and case
    when p like 'errors/%' or p like 'informe/%' then public.teaches_txt(split_part(p, '/', 2))
    when p like 'data/users/%' then split_part(p, '/', 3) = auth.uid()::text
    when p like 'usage/%' then public.is_admin()
    else true end;   -- solucions*, clau-material*: material comú del professorat
$$;

-- ---------- 8. Higiene ----------
alter function privat.gen_ses(text) set search_path = privat, public;
revoke all on function public.guard_profile() from public, anon, authenticated;
revoke all on function public.set_graded_by() from public, anon, authenticated;
revoke all on function public.touch_avaluacio() from public, anon, authenticated;
revoke all on function public.owns_course(uuid) from public, anon;
grant execute on function public.owns_course(uuid) to authenticated, service_role;
revoke all on function public.teaches(uuid) from public, anon;
revoke all on function public.teaches_txt(text) from public, anon;
grant execute on function public.teaches(uuid), public.teaches_txt(text) to authenticated, service_role;

commit;

-- ---------- Comprovacions després d'aplicar (només lectura) ----------
-- select count(*) from public.responses where item_version <> 1;          -- 0
-- select count(*) from public.feedback  where item_version <> 1;          -- 0
-- Amb la sessió de claudiatallero o paularomero (sense cursos encara):
--   select count(*) from public.profiles where role = 'student';          -- 0
--   select count(*) from public.responses;                                -- 0
-- Amb la de maciapallares: 23 alumnes, 301 respostes (en són el docent).
