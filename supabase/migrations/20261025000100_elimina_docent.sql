-- =====================================================================================
-- APLICADA el 24/10/2026 (migració elimina_docent): «docent» esborrat; les seves 4 respostes de prova s'han esborrat en cascada (còpia a backups/2026-10-24).
-- Queden només: maciapallares (administrador), claudiatallero i paularomero.
--
-- Estat al 24/10/2026 (consulta de només lectura):
--   profiles.username = 'docent', role = 'teacher', id c0de930a-4049-4066-92ad-0fbdcf8f92da
--   no és docent de cap curs i no té alumnat; no té cap clau a kv (data/users/<id>/…).
--
-- Opció recomanada: des de la zona docent amb l'usuari administrador (Edge Function «docents»,
--   acció delete), que ja comprova que no tingui alumnat. No cal SQL.
-- Opció SQL (service_role, editor SQL de Supabase): el bloc següent ho torna a comprovar i, si tot és
--   correcte, esborra l'usuari d'auth (el perfil s'esborra en cascada).
-- =====================================================================================
do $$
declare v uuid;
begin
  select id into v from public.profiles where username = 'docent' and role = 'teacher';
  if v is null then raise notice 'no hi ha cap usuari «docent»'; return; end if;
  if exists (select 1 from public.courses where teacher_id = v) then
    raise exception '«docent» té cursos: cal reassignar-los abans';
  end if;
  if exists (select 1 from public.kv where path like 'data/users/' || v::text || '/%') then
    raise exception '«docent» té dades a kv: fes-ne còpia abans';
  end if;
  delete from auth.users where id = v;   -- profiles.id té on delete cascade
  raise notice 'esborrat «docent» (%)', v;
end $$;

-- Després: comprova que només queden aquests comptes de professorat
-- select username, role from public.profiles where role in ('teacher','admin') order by 1;
--   claudiatallero teacher · maciapallares admin · paularomero teacher
