-- =====================================================================================
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

-- ---------- public.profiles ----------
create table if not exists public.profiles (
  id uuid not null,
  role text not null default 'student'::text,
  display_name text not null default ''::text,
  grup text not null default ''::text,
  code text,
  created_at timestamptz not null default now(),
  username text,
  course_id uuid
);
do $$ begin alter table public.profiles add constraint profiles_pkey PRIMARY KEY (id); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;
do $$ begin alter table public.profiles add constraint profiles_role_check CHECK ((role = ANY (ARRAY['student'::text, 'teacher'::text, 'admin'::text]))); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;
do $$ begin alter table public.profiles add constraint profiles_username_key UNIQUE (username); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- public.courses ----------
create table if not exists public.courses (
  id uuid not null default gen_random_uuid(),
  teacher_id uuid not null,
  name text not null,
  settings jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  level text not null default '3r'::text
);
do $$ begin alter table public.courses add constraint courses_name_check CHECK (((char_length(name) >= 1) AND (char_length(name) <= 60))); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;
do $$ begin alter table public.courses add constraint courses_pkey PRIMARY KEY (id); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;
do $$ begin alter table public.courses add constraint courses_level_check CHECK ((level = ANY (ARRAY['2n'::text, '3r'::text, '4t'::text]))); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- public.settings ----------
create table if not exists public.settings (
  key text not null,
  value jsonb not null,
  updated_at timestamptz not null default now()
);
do $$ begin alter table public.settings add constraint settings_pkey PRIMARY KEY (key); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- public.responses ----------
create table if not exists public.responses (
  student_id uuid not null,
  worksheet_id text not null,
  item_id text not null,
  answer jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);
do $$ begin alter table public.responses add constraint responses_pkey PRIMARY KEY (student_id, worksheet_id, item_id); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- public.submissions ----------
create table if not exists public.submissions (
  student_id uuid not null,
  worksheet_id text not null,
  status text not null default 'draft'::text,
  submitted_at timestamptz,
  returned_at timestamptz,
  photos jsonb not null default '[]'::jsonb,
  review text,
  review_items jsonb not null default '[]'::jsonb
);
do $$ begin alter table public.submissions add constraint submissions_status_check CHECK ((status = ANY (ARRAY['draft'::text, 'submitted'::text, 'returned'::text]))); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;
do $$ begin alter table public.submissions add constraint submissions_pkey PRIMARY KEY (student_id, worksheet_id); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;
do $$ begin alter table public.submissions add constraint submissions_review_check CHECK ((review = ANY (ARRAY['pending'::text, 'auto'::text, 'done'::text]))); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- public.feedback ----------
create table if not exists public.feedback (
  student_id uuid not null,
  worksheet_id text not null,
  item_id text not null,
  proposal_level text,
  proposal_note text,
  level text,
  comment text,
  released boolean not null default false,
  updated_at timestamptz not null default now()
);
do $$ begin alter table public.feedback add constraint feedback_level_check CHECK ((level = ANY (ARRAY['NA'::text, 'AS'::text, 'AN'::text, 'AE'::text]))); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;
do $$ begin alter table public.feedback add constraint feedback_pkey PRIMARY KEY (student_id, worksheet_id, item_id); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- public.kv ----------
create table if not exists public.kv (
  path text not null,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);
do $$ begin alter table public.kv add constraint kv_pkey PRIMARY KEY (path); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- privat.imatges ----------
create table if not exists privat.imatges (
  id bigserial not null,
  prompt text not null,
  mida text,
  request_id bigint,
  created_at timestamptz default now()
);
do $$ begin alter table privat.imatges add constraint imatges_pkey PRIMARY KEY (id); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- privat.imatges4 ----------
create table if not exists privat.imatges4 (
  id bigserial not null,
  nom text not null,
  prompt text not null,
  model text not null,
  mida text not null,
  qualitat text not null,
  request_id bigint,
  created_at timestamptz default now()
);
do $$ begin alter table privat.imatges4 add constraint imatges4_pkey PRIMARY KEY (id); exception when duplicate_object or duplicate_table or invalid_table_definition then null; end $$;

-- ---------- Claus foranes ----------
do $$ begin alter table public.profiles add constraint profiles_id_fkey FOREIGN KEY (id) REFERENCES auth.users(id) ON DELETE CASCADE; exception when duplicate_object or duplicate_table then null; end $$;
do $$ begin alter table public.responses add constraint responses_student_id_fkey FOREIGN KEY (student_id) REFERENCES profiles(id) ON DELETE CASCADE; exception when duplicate_object or duplicate_table then null; end $$;
do $$ begin alter table public.submissions add constraint submissions_student_id_fkey FOREIGN KEY (student_id) REFERENCES profiles(id) ON DELETE CASCADE; exception when duplicate_object or duplicate_table then null; end $$;
do $$ begin alter table public.feedback add constraint feedback_student_id_fkey FOREIGN KEY (student_id) REFERENCES profiles(id) ON DELETE CASCADE; exception when duplicate_object or duplicate_table then null; end $$;
do $$ begin alter table public.courses add constraint courses_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES profiles(id) ON DELETE CASCADE; exception when duplicate_object or duplicate_table then null; end $$;
do $$ begin alter table public.profiles add constraint profiles_course_id_fkey FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE SET NULL; exception when duplicate_object or duplicate_table then null; end $$;

-- ---------- Índexs ----------
create index if not exists profiles_course_idx ON public.profiles USING btree (course_id);
create index if not exists courses_teacher_idx ON public.courses USING btree (teacher_id);

-- ---------- Funcions ----------
CREATE OR REPLACE FUNCTION public.is_admin()
 RETURNS boolean
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select exists(select 1 from public.profiles where id = auth.uid() and role = 'admin');
$function$;

CREATE OR REPLACE FUNCTION public.is_teacher()
 RETURNS boolean
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select exists(select 1 from public.profiles where id = auth.uid() and role in ('teacher','admin'));
$function$;

CREATE OR REPLACE FUNCTION public.teaches(sid uuid)
 RETURNS boolean
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select public.is_admin() or exists(
    select 1 from public.profiles p join public.courses c on c.id = p.course_id
    where p.id = sid and c.teacher_id = auth.uid());
$function$;

CREATE OR REPLACE FUNCTION public.teaches_txt(sid text)
 RETURNS boolean
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select exists(select 1 from public.profiles p where p.id::text = sid and public.teaches(p.id));
$function$;

CREATE OR REPLACE FUNCTION public.my_course()
 RETURNS uuid
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select course_id from public.profiles where id = auth.uid();
$function$;

CREATE OR REPLACE FUNCTION public.kv_can_read(p text)
 RETURNS boolean
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select public.is_teacher() and case
    when p like 'errors/%' or p like 'informe/%' then public.teaches_txt(split_part(p, '/', 2))
    when p like 'data/users/%' then split_part(p, '/', 3) = auth.uid()::text or public.is_admin()
    else true end;
$function$;

CREATE OR REPLACE FUNCTION public.kv_can_write(p text)
 RETURNS boolean
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select public.is_teacher() and case
    when p like 'errors/%' or p like 'informe/%' then public.teaches_txt(split_part(p, '/', 2))
    when p like 'data/users/%' then split_part(p, '/', 3) = auth.uid()::text
    else public.is_admin() end;
$function$;

CREATE OR REPLACE FUNCTION public.guard_submission()
 RETURNS trigger
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
begin
  if auth.uid() = new.student_id and not public.is_teacher() then
    if tg_op = 'INSERT' then new.review := null; new.review_items := '[]'::jsonb;
    else new.review := old.review; new.review_items := old.review_items; end if;
  end if;
  return new;
end $function$;

CREATE OR REPLACE FUNCTION privat.genera_imatge(p_prompt text, p_size text DEFAULT '1536x1024'::text, p_quality text DEFAULT 'medium'::text)
 RETURNS bigint
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'privat', 'extensions', 'public'
AS $function$
declare rid bigint; k text;
begin
  select decrypted_secret into k from vault.decrypted_secrets where name = 'openai_api_key';
  rid := net.http_post(
    url := 'https://api.openai.com/v1/images/generations',
    body := jsonb_build_object('model','gpt-image-1','prompt',p_prompt,'size',p_size,'quality',p_quality,'output_format','jpeg','output_compression',85,'n',1),
    headers := jsonb_build_object('Content-Type','application/json','Authorization','Bearer ' || k),
    timeout_milliseconds := 180000);
  insert into privat.imatges(prompt, mida, request_id) values (p_prompt, p_size, rid);
  return rid;
end $function$;

CREATE OR REPLACE FUNCTION privat.gen_ses(p text)
 RETURNS bigint
 LANGUAGE sql
AS $function$ select privat.genera_imatge('Flat cartoon educational illustration for a secondary-school science book, thick black outlines, soft flat colours, pure white background, wide composition, characters are diverse teenagers aged 14-15 with casual clothes and uncovered hair (no headscarves, no hijabs, no religious clothing), absolutely no text, no letters, no numbers, no labels. ' || p, '1536x1024', 'medium') $function$;

CREATE OR REPLACE FUNCTION privat.genera_imatge4(p_nom text, p_prompt text, p_model text DEFAULT 'gpt-image-1-mini'::text, p_size text DEFAULT '1536x1024'::text, p_quality text DEFAULT 'medium'::text)
 RETURNS bigint
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'privat', 'public'
AS $function$
declare rid bigint; k text;
begin
  select decrypted_secret into k from vault.decrypted_secrets where name = 'openai_api_key';
  rid := net.http_post(
    url := 'https://api.openai.com/v1/images/generations',
    body := jsonb_build_object('model', p_model, 'prompt', p_prompt, 'size', p_size, 'quality', p_quality,
                               'output_format', 'jpeg', 'output_compression', 85, 'n', 1),
    headers := jsonb_build_object('Content-Type', 'application/json', 'Authorization', 'Bearer ' || k),
    timeout_milliseconds := 180000);
  insert into privat.imatges4(nom, prompt, model, mida, qualitat, request_id) values (p_nom, p_prompt, p_model, p_size, p_quality, rid);
  return rid;
end $function$;

CREATE OR REPLACE FUNCTION privat.gen4(p_nom text, p_sda integer, p_escena text, p_model text DEFAULT 'gpt-image-1-mini'::text, p_size text DEFAULT '1536x1024'::text)
 RETURNS bigint
 LANGUAGE sql
 SECURITY DEFINER
 SET search_path TO 'privat', 'public'
AS $function$
  select privat.genera_imatge4(p_nom,
    'Flat cartoon illustration for a secondary-school science textbook, bold black outlines, simple flat colours, no text, no letters, no numbers, no labels, no logos. Solid uniform '
    || (array['vivid violet (#7A4CC2)','ocean blue (#1F8FB8)','leaf green (#4E8A2E)','warm ochre (#B8742A)','raspberry red (#D14B66)','deep navy blue (#1D5C8C)'])[p_sda]
    || ' background filling the whole image. ' || p_escena
    || ' All young people are teenagers aged 15-16 with natural, realistic skin tones and uncovered hair (no headscarves, no hijabs). Nobody holds a mobile phone. Simple, clean composition with few objects; everything drawn realistically and correctly.',
    p_model, p_size, 'medium');
$function$;

CREATE OR REPLACE FUNCTION privat.gen2(p_nom text, p_sda integer, p_escena text, p_model text DEFAULT 'gpt-image-1-mini'::text, p_size text DEFAULT '1536x1024'::text)
 RETURNS bigint
 LANGUAGE sql
 SECURITY DEFINER
 SET search_path TO 'privat', 'public'
AS $function$
  select privat.genera_imatge4(p_nom,
    'Flat cartoon illustration for a secondary-school science textbook, bold black outlines, simple flat colours, no text, no letters, no numbers, no labels, no logos. Solid uniform '
    || (array['teal green (#12857A)','magenta pink (#B83A7A)','warm orange (#D9731A)','cobalt blue (#2F6FB5)','golden ochre (#B7791F)','tomato red (#C63D3D)'])[p_sda]
    || ' background filling the whole image. ' || p_escena
    || ' All young people are teenagers aged 13-14 with natural, realistic skin tones and uncovered hair (no headscarves, no hijabs). Nobody holds a mobile phone. Simple, clean composition with few objects; everything drawn realistically and correctly.',
    p_model, p_size, 'medium');
$function$;

CREATE OR REPLACE FUNCTION privat.models_req()
 RETURNS bigint
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'privat', 'extensions', 'public'
AS $function$
declare k text; begin select decrypted_secret into k from vault.decrypted_secrets where name='openai_api_key';
return net.http_get(url:='https://api.openai.com/v1/models', headers:=jsonb_build_object('Authorization','Bearer '||k)); end $function$;

-- Permisos d'execució tal com són ara (només authenticated i service_role a public.*; privat.* només postgres)
revoke all on function public.kv_can_write(p text) from public, anon;
grant execute on function public.kv_can_write(p text) to authenticated;
grant execute on function public.kv_can_write(p text) to service_role;
revoke all on function privat.models_req() from public, anon;
revoke all on function privat.genera_imatge(p_prompt text, p_size text, p_quality text) from public, anon;
revoke all on function privat.gen_ses(p text) from public, anon;
revoke all on function privat.genera_imatge4(p_nom text, p_prompt text, p_model text, p_size text, p_quality text) from public, anon;
revoke all on function privat.gen4(p_nom text, p_sda integer, p_escena text, p_model text, p_size text) from public, anon;
revoke all on function privat.gen2(p_nom text, p_sda integer, p_escena text, p_model text, p_size text) from public, anon;
revoke all on function public.is_teacher() from public, anon;
grant execute on function public.is_teacher() to authenticated;
grant execute on function public.is_teacher() to service_role;
revoke all on function public.is_admin() from public, anon;
grant execute on function public.is_admin() to authenticated;
grant execute on function public.is_admin() to service_role;
revoke all on function public.teaches(sid uuid) from public, anon;
grant execute on function public.teaches(sid uuid) to authenticated;
grant execute on function public.teaches(sid uuid) to service_role;
revoke all on function public.teaches_txt(sid text) from public, anon;
grant execute on function public.teaches_txt(sid text) to authenticated;
grant execute on function public.teaches_txt(sid text) to service_role;
revoke all on function public.my_course() from public, anon;
grant execute on function public.my_course() to authenticated;
grant execute on function public.my_course() to service_role;
revoke all on function public.kv_can_read(p text) from public, anon;
grant execute on function public.kv_can_read(p text) to authenticated;
grant execute on function public.kv_can_read(p text) to service_role;
revoke all on function public.guard_submission() from public, anon;
grant execute on function public.guard_submission() to service_role;

-- ---------- Disparadors ----------
drop trigger if exists submissions_guard on public.submissions;
CREATE TRIGGER submissions_guard BEFORE INSERT OR UPDATE ON public.submissions FOR EACH ROW EXECUTE FUNCTION guard_submission();

-- ---------- RLS ----------
alter table public.kv enable row level security;
alter table public.settings enable row level security;
alter table public.responses enable row level security;
alter table public.feedback enable row level security;
alter table privat.imatges disable row level security;
alter table privat.imatges4 disable row level security;
alter table public.profiles enable row level security;
alter table public.submissions enable row level security;
alter table public.courses enable row level security;

-- ---------- Polítiques ----------
drop policy if exists p_courses_del on public.courses;
create policy p_courses_del on public.courses as permissive for delete to public
  using (((teacher_id = ( SELECT auth.uid() AS uid)) OR is_admin()));
drop policy if exists p_courses_ins on public.courses;
create policy p_courses_ins on public.courses as permissive for insert to public
  with check ((is_teacher() AND (teacher_id = ( SELECT auth.uid() AS uid))));
drop policy if exists p_courses_sel on public.courses;
create policy p_courses_sel on public.courses as permissive for select to public
  using (((teacher_id = ( SELECT auth.uid() AS uid)) OR is_admin() OR (id = my_course())));
drop policy if exists p_courses_upd on public.courses;
create policy p_courses_upd on public.courses as permissive for update to public
  using (((teacher_id = ( SELECT auth.uid() AS uid)) OR is_admin()))
  with check (((teacher_id = ( SELECT auth.uid() AS uid)) OR is_admin()));
drop policy if exists p_fb_del on public.feedback;
create policy p_fb_del on public.feedback as permissive for delete to public
  using (teaches(student_id));
drop policy if exists p_fb_ins on public.feedback;
create policy p_fb_ins on public.feedback as permissive for insert to public
  with check (teaches(student_id));
drop policy if exists p_fb_sel on public.feedback;
create policy p_fb_sel on public.feedback as permissive for select to public
  using ((((student_id = ( SELECT auth.uid() AS uid)) AND released) OR teaches(student_id)));
drop policy if exists p_fb_upd on public.feedback;
create policy p_fb_upd on public.feedback as permissive for update to public
  using (teaches(student_id));
drop policy if exists p_kv_del on public.kv;
create policy p_kv_del on public.kv as permissive for delete to authenticated
  using (kv_can_write(path));
drop policy if exists p_kv_ins on public.kv;
create policy p_kv_ins on public.kv as permissive for insert to authenticated
  with check (kv_can_write(path));
drop policy if exists p_kv_sel on public.kv;
create policy p_kv_sel on public.kv as permissive for select to authenticated
  using (kv_can_read(path));
drop policy if exists p_kv_upd on public.kv;
create policy p_kv_upd on public.kv as permissive for update to authenticated
  using (kv_can_write(path))
  with check (kv_can_write(path));
drop policy if exists p_profiles_sel on public.profiles;
create policy p_profiles_sel on public.profiles as permissive for select to public
  using (((id = ( SELECT auth.uid() AS uid)) OR teaches(id) OR is_admin()));
drop policy if exists p_profiles_upd on public.profiles;
create policy p_profiles_upd on public.profiles as permissive for update to public
  using ((is_admin() OR teaches(id)))
  with check ((is_admin() OR ((role = 'student'::text) AND teaches(id) AND ((course_id IS NULL) OR (EXISTS ( SELECT 1
   FROM courses c
  WHERE ((c.id = profiles.course_id) AND (c.teacher_id = ( SELECT auth.uid() AS uid)))))))));
drop policy if exists p_resp_ins on public.responses;
create policy p_resp_ins on public.responses as permissive for insert to public
  with check (((student_id = ( SELECT auth.uid() AS uid)) AND (NOT (EXISTS ( SELECT 1
   FROM submissions s
  WHERE ((s.student_id = ( SELECT auth.uid() AS uid)) AND (s.worksheet_id = responses.worksheet_id) AND (s.status = 'submitted'::text)))))));
drop policy if exists p_resp_sel on public.responses;
create policy p_resp_sel on public.responses as permissive for select to public
  using (((student_id = ( SELECT auth.uid() AS uid)) OR teaches(student_id)));
drop policy if exists p_resp_upd on public.responses;
create policy p_resp_upd on public.responses as permissive for update to public
  using (((student_id = ( SELECT auth.uid() AS uid)) AND (NOT (EXISTS ( SELECT 1
   FROM submissions s
  WHERE ((s.student_id = ( SELECT auth.uid() AS uid)) AND (s.worksheet_id = responses.worksheet_id) AND (s.status = 'submitted'::text)))))));
drop policy if exists p_settings_ins on public.settings;
create policy p_settings_ins on public.settings as permissive for insert to authenticated
  with check (is_admin());
drop policy if exists p_settings_sel on public.settings;
create policy p_settings_sel on public.settings as permissive for select to authenticated
  using (true);
drop policy if exists p_settings_upd on public.settings;
create policy p_settings_upd on public.settings as permissive for update to authenticated
  using (is_admin());
drop policy if exists p_sub_ins on public.submissions;
create policy p_sub_ins on public.submissions as permissive for insert to public
  with check ((((student_id = ( SELECT auth.uid() AS uid)) AND (status = ANY (ARRAY['draft'::text, 'submitted'::text]))) OR teaches(student_id)));
drop policy if exists p_sub_sel on public.submissions;
create policy p_sub_sel on public.submissions as permissive for select to public
  using (((student_id = ( SELECT auth.uid() AS uid)) OR teaches(student_id)));
drop policy if exists p_sub_upd on public.submissions;
create policy p_sub_upd on public.submissions as permissive for update to public
  using ((((student_id = ( SELECT auth.uid() AS uid)) AND (status <> 'submitted'::text)) OR teaches(student_id)))
  with check ((((student_id = ( SELECT auth.uid() AS uid)) AND (status = ANY (ARRAY['draft'::text, 'submitted'::text]))) OR teaches(student_id)));
drop policy if exists p_fotos_del on storage.objects;
create policy p_fotos_del on storage.objects as permissive for delete to authenticated
  using (((bucket_id = 'fotos'::text) AND ((storage.foldername(name))[1] = (( SELECT auth.uid() AS uid))::text)));
drop policy if exists p_fotos_ins on storage.objects;
create policy p_fotos_ins on storage.objects as permissive for insert to authenticated
  with check (((bucket_id = 'fotos'::text) AND ((storage.foldername(name))[1] = (( SELECT auth.uid() AS uid))::text)));
drop policy if exists p_fotos_sel on storage.objects;
create policy p_fotos_sel on storage.objects as permissive for select to authenticated
  using (((bucket_id = 'fotos'::text) AND (((storage.foldername(name))[1] = (( SELECT auth.uid() AS uid))::text) OR teaches_txt((storage.foldername(name))[1]))));
drop policy if exists p_prof_del on storage.objects;
create policy p_prof_del on storage.objects as permissive for delete to authenticated
  using (((bucket_id = 'professorat'::text) AND is_admin()));
drop policy if exists p_prof_ins on storage.objects;
create policy p_prof_ins on storage.objects as permissive for insert to authenticated
  with check (((bucket_id = 'professorat'::text) AND is_admin()));
drop policy if exists p_prof_sel on storage.objects;
create policy p_prof_sel on storage.objects as permissive for select to authenticated
  using (((bucket_id = 'professorat'::text) AND is_teacher()));
drop policy if exists p_prof_upd on storage.objects;
create policy p_prof_upd on storage.objects as permissive for update to authenticated
  using (((bucket_id = 'professorat'::text) AND is_admin()));

-- ---------- Storage ----------
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types) values ('fotos', 'fotos', false, 8388608, array['image/jpeg','image/png','image/webp','image/heic','image/heif']) on conflict (id) do nothing;
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types) values ('professorat', 'professorat', false, 20971520, array['application/pdf']) on conflict (id) do nothing;

-- Secrets: viuen al Vault de Supabase (openai_api_key, imatges4_token) o a l'entorn de les Edge Functions
-- (ANTHROPIC_API_KEY, SUPABASE_SERVICE_ROLE_KEY). Aquí no n'hi ha cap.
