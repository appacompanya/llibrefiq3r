create table if not exists public.kv (
  path text primary key,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);
alter table public.kv enable row level security;
create policy p_kv_sel on public.kv for select to authenticated using (public.is_teacher());
create policy p_kv_ins on public.kv for insert to authenticated with check (public.is_teacher());
create policy p_kv_upd on public.kv for update to authenticated using (public.is_teacher());
create policy p_kv_del on public.kv for delete to authenticated using (public.is_teacher());
grant select, insert, update, delete on public.kv to authenticated;
revoke all on public.kv from anon;

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
  values ('professorat', 'professorat', false, 20971520, array['application/pdf'])
  on conflict (id) do nothing;
create policy p_prof_sel on storage.objects for select to authenticated using (bucket_id = 'professorat' and public.is_teacher());
create policy p_prof_ins on storage.objects for insert to authenticated with check (bucket_id = 'professorat' and public.is_teacher());
create policy p_prof_upd on storage.objects for update to authenticated using (bucket_id = 'professorat' and public.is_teacher());
create policy p_prof_del on storage.objects for delete to authenticated using (bucket_id = 'professorat' and public.is_teacher());