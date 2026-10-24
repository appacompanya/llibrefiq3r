create schema if not exists privat;
revoke all on schema privat from public, anon, authenticated;
create table if not exists privat.imatges (
  id bigserial primary key, prompt text not null, mida text, request_id bigint, created_at timestamptz default now()
);
create or replace function privat.genera_imatge(p_prompt text, p_size text default '1536x1024', p_quality text default 'medium')
returns bigint language plpgsql security definer set search_path = privat, extensions, public as $$
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
end $$;
revoke all on function privat.genera_imatge(text,text,text) from public, anon, authenticated;