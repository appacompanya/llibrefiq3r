create table if not exists privat.imatges4 (
  id bigserial primary key,
  nom text not null,
  prompt text not null,
  model text not null,
  mida text not null,
  qualitat text not null,
  request_id bigint,
  created_at timestamptz default now()
);
revoke all on privat.imatges4 from anon, authenticated;

create or replace function privat.genera_imatge4(p_nom text, p_prompt text, p_model text default 'gpt-image-1-mini', p_size text default '1536x1024', p_quality text default 'medium')
returns bigint language plpgsql security definer set search_path = privat, public as $$
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
end $$;
revoke all on function privat.genera_imatge4(text, text, text, text, text) from public, anon, authenticated;

do $$ begin
  if not exists (select 1 from vault.secrets where name = 'imatges4_token') then
    perform vault.create_secret(replace(gen_random_uuid()::text, '-', ''), 'imatges4_token', 'Token per descarregar les imatges de 4t');
  end if;
end $$;