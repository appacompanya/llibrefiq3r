create table if not exists public.profiles (
  id          uuid primary key references auth.users(id) on delete cascade,
  role        text not null default 'student' check (role in ('student','teacher')),
  display_name text not null default '',
  grup        text not null default '',
  code        text,
  created_at  timestamptz not null default now()
);

create or replace function public.is_teacher() returns boolean
language sql stable security definer set search_path = public as $$
  select exists(select 1 from public.profiles where id = auth.uid() and role = 'teacher');
$$;

create table if not exists public.settings (
  key   text primary key,
  value jsonb not null,
  updated_at timestamptz not null default now()
);
insert into public.settings(key, value) values ('auto_calc', 'true'::jsonb) on conflict (key) do nothing;

create table if not exists public.responses (
  student_id   uuid not null references public.profiles(id) on delete cascade,
  worksheet_id text not null,
  item_id      text not null,
  answer       jsonb not null default '{}'::jsonb,
  updated_at   timestamptz not null default now(),
  primary key (student_id, worksheet_id, item_id)
);

create table if not exists public.submissions (
  student_id   uuid not null references public.profiles(id) on delete cascade,
  worksheet_id text not null,
  status       text not null default 'draft' check (status in ('draft','submitted','returned')),
  submitted_at timestamptz,
  returned_at  timestamptz,
  photos       jsonb not null default '[]'::jsonb,
  primary key (student_id, worksheet_id)
);

create table if not exists public.feedback (
  student_id     uuid not null references public.profiles(id) on delete cascade,
  worksheet_id   text not null,
  item_id        text not null,
  proposal_level text,
  proposal_note  text,
  level          text check (level in ('NA','AS','AN','AE')),
  comment        text,
  released       boolean not null default false,
  updated_at     timestamptz not null default now(),
  primary key (student_id, worksheet_id, item_id)
);

alter table public.profiles    enable row level security;
alter table public.settings    enable row level security;
alter table public.responses   enable row level security;
alter table public.submissions enable row level security;
alter table public.feedback    enable row level security;

create policy p_profiles_sel on public.profiles for select using (id = (select auth.uid()) or public.is_teacher());
create policy p_profiles_upd on public.profiles for update using (public.is_teacher());

create policy p_settings_sel on public.settings for select to authenticated using (true);
create policy p_settings_ins on public.settings for insert to authenticated with check (public.is_teacher());
create policy p_settings_upd on public.settings for update to authenticated using (public.is_teacher());

create policy p_resp_sel on public.responses for select using (student_id = (select auth.uid()) or public.is_teacher());
create policy p_resp_ins on public.responses for insert with check (
  student_id = (select auth.uid()) and not exists (
    select 1 from public.submissions s where s.student_id = (select auth.uid()) and s.worksheet_id = responses.worksheet_id and s.status = 'submitted'));
create policy p_resp_upd on public.responses for update using (
  student_id = (select auth.uid()) and not exists (
    select 1 from public.submissions s where s.student_id = (select auth.uid()) and s.worksheet_id = responses.worksheet_id and s.status = 'submitted'));

create policy p_sub_sel on public.submissions for select using (student_id = (select auth.uid()) or public.is_teacher());
create policy p_sub_ins on public.submissions for insert with check ((student_id = (select auth.uid()) and status in ('draft','submitted')) or public.is_teacher());
create policy p_sub_upd on public.submissions for update
  using ((student_id = (select auth.uid()) and status <> 'submitted') or public.is_teacher())
  with check ((student_id = (select auth.uid()) and status in ('draft','submitted')) or public.is_teacher());

create policy p_fb_sel on public.feedback for select using ((student_id = (select auth.uid()) and released) or public.is_teacher());
create policy p_fb_ins on public.feedback for insert with check (public.is_teacher());
create policy p_fb_upd on public.feedback for update using (public.is_teacher());
create policy p_fb_del on public.feedback for delete using (public.is_teacher());

grant usage on schema public to authenticated;
grant select, insert, update, delete on public.profiles, public.settings, public.responses, public.submissions, public.feedback to authenticated;
revoke all on public.profiles, public.settings, public.responses, public.submissions, public.feedback from anon;
revoke execute on function public.is_teacher() from anon, public;
grant execute on function public.is_teacher() to authenticated;

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
  values ('fotos', 'fotos', false, 8388608, array['image/jpeg','image/png','image/webp','image/heic','image/heif'])
  on conflict (id) do nothing;

create policy p_fotos_ins on storage.objects for insert to authenticated
  with check (bucket_id = 'fotos' and (storage.foldername(name))[1] = (select auth.uid())::text);
create policy p_fotos_sel on storage.objects for select to authenticated
  using (bucket_id = 'fotos' and ((storage.foldername(name))[1] = (select auth.uid())::text or public.is_teacher()));
create policy p_fotos_del on storage.objects for delete to authenticated
  using (bucket_id = 'fotos' and (storage.foldername(name))[1] = (select auth.uid())::text);