-- PAU d'anglès digital (2n de Batxillerat): cursos d'anglès, puntuacions numèriques i registre d'integritat.
-- Additiu: no toca dades existents.

-- 1. Cursos d'anglès a la zona docent
alter table public.courses drop constraint if exists courses_level_check;
alter table public.courses add constraint courses_level_check check (level = any (array['2n','3r','4t','ang']));

-- 2. Puntuacions numèriques (la PAU puntua sobre 10: listening 3, reading 3, writing 4)
alter table public.feedback add column if not exists points numeric;           -- nota del docent (la que veu l'alumne)
alter table public.feedback add column if not exists proposal_points numeric;  -- proposta automàtica / IA (només docent)

-- 3. Registre d'integritat de l'examen: sortides de pestanya, intents d'enganxar, etc.
--    L'alumne només hi pot AFEGIR files seves; no les pot llegir, canviar ni esborrar. El docent les llegeix.
create table if not exists public.exam_events (
  id bigserial primary key,
  student_id uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  worksheet_id text not null,
  kind text not null check (kind in ('start','hidden','visible','blur','focus','paste','drop','copy','cut','contextmenu','bigInsert','audioPlay','audioEnd','submit')),
  at timestamptz not null default now(),
  data jsonb not null default '{}'::jsonb
);
create index if not exists exam_events_ws_idx on public.exam_events (student_id, worksheet_id, at);
alter table public.exam_events enable row level security;
drop policy if exists p_ev_ins on public.exam_events;
create policy p_ev_ins on public.exam_events for insert to authenticated
  with check (student_id = (select auth.uid()) and worksheet_id like 'ang:%' and octet_length(data::text) < 2000);
drop policy if exists p_ev_sel on public.exam_events;
create policy p_ev_sel on public.exam_events for select to authenticated
  using (public.teaches(student_id));
revoke all on public.exam_events from anon;
grant select, insert on public.exam_events to authenticated;
grant usage, select on sequence public.exam_events_id_seq to authenticated;
