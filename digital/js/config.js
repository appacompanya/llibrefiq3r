/* Configuració pública del projecte Supabase «llibre-fq3».
   La clau "anon" és pública per disseny: la seguretat la fan les regles RLS de la base de dades.
   Si es deixa buit, el llibre funciona en MODE DEMOSTRACIÓ (dades només al navegador). */
window.FQ_CONFIG = {
  SUPABASE_URL: "https://pwqyqwiwarffzdkblglt.supabase.co",
  SUPABASE_ANON_KEY: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB3cXlxd2l3YXJmZnpka2JsZ2x0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE5OTk5MjEsImV4cCI6MjEwNzU3NTkyMX0.TOGACayLHFHTW4NfnsSGPwjIyMZGYAinTdx8nQfj2VM",
};
/* ?demo a l'adreça força el mode demostració */
if (/[?&]demo\b/.test(location.search)) { window.FQ_CONFIG = {}; }
