-- Cursos i docents (migració cursos_i_docents, 22/10/2026).
-- Abans: un sol professor veia tot l'alumnat.
-- Ara:   l'administrador crea docents; cada docent crea els seus cursos i l'alumnat de cada curs.
--        Un docent només veu l'alumnat dels seus cursos; l'administrador ho veu tot.

-- ---------- Rols i usuari ----------
alter table public.profiles drop constraint if exists profiles_role_check;
alter table public.profiles add constraint profiles_role_check check (role in ('student','teacher','admin'));
alter table public.profiles add column if not exists username text unique;

-- ---------- Cursos ----------
create table if not exists public.courses (
  id         uuid primary key default gen_random_uuid(),
  teacher_id uuid not null references public.profiles(id) on delete cascade,
  name       text not null check (char_length(name) between 1 and 60),
  settings   jsonb not null default '{}'::jsonb,   -- auto_calc, pes_fitxes… (de cada curs)
  created_at timestamptz not null default now()
);
alter table public.courses add column if not exists level text not null default '3r' check (level in ('2n','3r','4t'));
create index if not exists courses_teacher_idx on public.courses(teacher_id);
alter table public.profiles add column if not exists course_id uuid references public.courses(id) on delete set null;
create index if not exists profiles_course_idx on public.profiles(course_id);

-- ---------- Cua de revisió ----------
-- null o 'pending': el professor l'ha de revisar · 'auto': corregida del tot automàticament · 'done': revisada i retornada
alter table public.submissions add column if not exists review text check (review in ('pending','auto','done'));
alter table public.submissions add column if not exists review_items jsonb not null default '[]'::jsonb;

-- ---------- Funcions de permisos ----------
create or replace function public.is_teacher() returns boolean
language sql stable security definer set search_path = public as $$
  select exists(select 1 from public.profiles where id = auth.uid() and role in ('teacher','admin'));
$$;
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists(select 1 from public.profiles where id = auth.uid() and role = 'admin');
$$;
-- el docent que crida té aquest alumne en algun dels seus cursos (o és administrador)
create or replace function public.teaches(sid uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select public.is_admin() or exists(
    select 1 from public.profiles p join public.courses c on c.id = p.course_id
    where p.id = sid and c.teacher_id = auth.uid());
$$;
create or replace function public.teaches_txt(sid text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists(select 1 from public.profiles p where p.id::text = sid and public.teaches(p.id));
$$;
create or replace function public.my_course() returns uuid
language sql stable security definer set search_path = public as $$
  select course_id from public.profiles where id = auth.uid();
$$;
-- camins de public.kv: errors/<alumne>/… i informe/<alumne> (del docent de l'alumne), data/users/<docent>/… (de cada docent)
create or replace function public.kv_can_read(p text) returns boolean
language sql stable security definer set search_path = public as $$
  select public.is_teacher() and case
    when p like 'errors/%' or p like 'informe/%' then public.teaches_txt(split_part(p, '/', 2))
    when p like 'data/users/%' then split_part(p, '/', 3) = auth.uid()::text or public.is_admin()
    else true end;
$$;
create or replace function public.kv_can_write(p text) returns boolean
language sql stable security definer set search_path = public as $$
  select public.is_teacher() and case
    when p like 'errors/%' or p like 'informe/%' then public.teaches_txt(split_part(p, '/', 2))
    when p like 'data/users/%' then split_part(p, '/', 3) = auth.uid()::text
    else public.is_admin() end;
$$;

-- l'alumne no pot canviar l'estat de revisió del seu lliurament
create or replace function public.guard_submission() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() = new.student_id and not public.is_teacher() then
    if tg_op = 'INSERT' then new.review := null; new.review_items := '[]'::jsonb;
    else new.review := old.review; new.review_items := old.review_items; end if;
  end if;
  return new;
end $$;
drop trigger if exists submissions_guard on public.submissions;
create trigger submissions_guard before insert or update on public.submissions
  for each row execute function public.guard_submission();

-- ---------- Regles (RLS) ----------
alter table public.courses enable row level security;

drop policy if exists p_courses_sel on public.courses;
create policy p_courses_sel on public.courses for select using (teacher_id = (select auth.uid()) or public.is_admin() or id = public.my_course());
drop policy if exists p_courses_ins on public.courses;
create policy p_courses_ins on public.courses for insert with check (public.is_teacher() and teacher_id = (select auth.uid()));
drop policy if exists p_courses_upd on public.courses;
create policy p_courses_upd on public.courses for update using (teacher_id = (select auth.uid()) or public.is_admin())
  with check (teacher_id = (select auth.uid()) or public.is_admin());
drop policy if exists p_courses_del on public.courses;
create policy p_courses_del on public.courses for delete using (teacher_id = (select auth.uid()) or public.is_admin());

drop policy if exists p_profiles_sel on public.profiles;
create policy p_profiles_sel on public.profiles for select using (id = (select auth.uid()) or public.teaches(id) or public.is_admin());
drop policy if exists p_profiles_upd on public.profiles;
create policy p_profiles_upd on public.profiles for update using (public.is_admin() or public.teaches(id))
  with check (public.is_admin() or (role = 'student' and public.teaches(id)
    and (course_id is null or exists(select 1 from public.courses c where c.id = course_id and c.teacher_id = (select auth.uid()))))));

-- ajustos globals: només l'administrador hi escriu
drop policy if exists p_settings_ins on public.settings;
create policy p_settings_ins on public.settings for insert with check (public.is_admin());
drop policy if exists p_settings_upd on public.settings;
create policy p_settings_upd on public.settings for update using (public.is_admin());

drop policy if exists p_resp_sel on public.responses;
create policy p_resp_sel on public.responses for select using (student_id = (select auth.uid()) or public.teaches(student_id));

drop policy if exists p_sub_sel on public.submissions;
create policy p_sub_sel on public.submissions for select using (student_id = (select auth.uid()) or public.teaches(student_id));
drop policy if exists p_sub_ins on public.submissions;
create policy p_sub_ins on public.submissions for insert with check (
  (student_id = (select auth.uid()) and status in ('draft','submitted')) or public.teaches(student_id));
drop policy if exists p_sub_upd on public.submissions;
create policy p_sub_upd on public.submissions for update
  using ((student_id = (select auth.uid()) and status <> 'submitted') or public.teaches(student_id))
  with check ((student_id = (select auth.uid()) and status in ('draft','submitted')) or public.teaches(student_id));

drop policy if exists p_fb_sel on public.feedback;
create policy p_fb_sel on public.feedback for select using ((student_id = (select auth.uid()) and released) or public.teaches(student_id));
drop policy if exists p_fb_ins on public.feedback;
create policy p_fb_ins on public.feedback for insert with check (public.teaches(student_id));
drop policy if exists p_fb_upd on public.feedback;
create policy p_fb_upd on public.feedback for update using (public.teaches(student_id));
drop policy if exists p_fb_del on public.feedback;
create policy p_fb_del on public.feedback for delete using (public.teaches(student_id));

drop policy if exists p_kv_sel on public.kv;
create policy p_kv_sel on public.kv for select using (public.kv_can_read(path));
drop policy if exists p_kv_ins on public.kv;
create policy p_kv_ins on public.kv for insert with check (public.kv_can_write(path));
drop policy if exists p_kv_upd on public.kv;
create policy p_kv_upd on public.kv for update using (public.kv_can_write(path)) with check (public.kv_can_write(path));
drop policy if exists p_kv_del on public.kv;
create policy p_kv_del on public.kv for delete using (public.kv_can_write(path));

-- fotos: l'alumne les seves; el docent, les del seu alumnat
drop policy if exists p_fotos_sel on storage.objects;
create policy p_fotos_sel on storage.objects for select to authenticated
  using (bucket_id = 'fotos' and ((storage.foldername(name))[1] = (select auth.uid())::text or public.teaches_txt((storage.foldername(name))[1])));
-- PDF del professorat: tots els docents els llegeixen; només l'administrador els puja o els esborra
drop policy if exists p_prof_ins on storage.objects;
create policy p_prof_ins on storage.objects for insert to authenticated with check (bucket_id = 'professorat' and public.is_admin());
drop policy if exists p_prof_upd on storage.objects;
create policy p_prof_upd on storage.objects for update to authenticated using (bucket_id = 'professorat' and public.is_admin());
drop policy if exists p_prof_del on storage.objects;
create policy p_prof_del on storage.objects for delete to authenticated using (bucket_id = 'professorat' and public.is_admin());

grant select, insert, update, delete on public.courses to authenticated;
revoke all on public.courses from anon;
grant execute on function public.is_admin(), public.teaches(uuid), public.teaches_txt(text), public.my_course(),
  public.kv_can_read(text), public.kv_can_write(text) to authenticated;
revoke execute on function public.is_admin(), public.teaches(uuid), public.teaches_txt(text), public.my_course(),
  public.kv_can_read(text), public.kv_can_write(text), public.guard_submission() from public, anon;
revoke execute on function public.guard_submission() from authenticated;

-- ---------- Dades (aplicat a mà el 22/10/2026) ----------
-- 1. Compte d'administrador «maciapallares» (maciapallares@professorat.llibrefq3.app), rol 'admin'.
--    La contrasenya no és al repositori.
-- 2. Curs «3r B» (nivell 3r) de maciapallares, amb els ajustos globals auto_calc i pes_fitxes.
--    Tot l'alumnat existent hi passa (course_id, grup = '3r B'). No s'esborra cap resposta, lliurament ni retroacció.
-- 3. El registre d'avaluació (kv data/users/<docent>/…) passa del compte «docent» al de maciapallares.
--    El compte «docent» es manté, sense cursos ni alumnat.
-- 4. Lliuraments ja enviats: review = 'auto' si tenien correcció automàtica; si no, 'pending' (cua «Per corregir»).
