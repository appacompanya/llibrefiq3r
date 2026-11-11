// Descarrega les il·lustracions de la PAU d'anglès generades amb privat.genera_imatge4.
// Només serveix les files amb nom «ang-…» (imatges que es publiquen al web), en un zip amb <nom>.jpg.
// ?noms=a,b filtra per nom. Sense secrets: no dona accés a res més.
import postgres from "npm:postgres@3.4.4";
import { zipSync } from "npm:fflate@0.8.2";

const sql = postgres(Deno.env.get("SUPABASE_DB_URL")!, { prepare: false, max: 1 });

function b64ToBytes(b64: string): Uint8Array {
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

Deno.serve(async (req: Request) => {
  const url = new URL(req.url);
  const noms = (url.searchParams.get("noms") || "").split(",").map((s) => s.trim()).filter((s) => /^ang-[a-z0-9-]+$/.test(s));
  const rows = noms.length
    ? await sql`select distinct on (i.nom) i.nom, r.status_code, r.content from privat.imatges4 i join net._http_response r on r.id = i.request_id where i.nom = any(${noms}) and r.status_code is not null order by i.nom, i.id desc`
    : await sql`select distinct on (i.nom) i.nom, r.status_code, r.content from privat.imatges4 i join net._http_response r on r.id = i.request_id where i.nom like 'ang-%' and r.status_code is not null order by i.nom, i.id desc`;
  const files: Record<string, Uint8Array> = {};
  const log: string[] = [];
  for (const r of rows) {
    try {
      const j = JSON.parse(r.content);
      if (r.status_code === 200 && j.data && j.data[0] && j.data[0].b64_json) {
        files[`${r.nom}.jpg`] = b64ToBytes(j.data[0].b64_json);
        log.push(`${r.nom}\tok`);
      } else {
        log.push(`${r.nom}\terror ${r.status_code} ${JSON.stringify(j.error || j).slice(0, 300)}`);
      }
    } catch (e) {
      log.push(`${r.nom}\terror ${String(e).slice(0, 200)}`);
    }
  }
  files["registre.txt"] = new TextEncoder().encode(log.join("\n") + "\n");
  return new Response(zipSync(files, { level: 0 }), { headers: { "Content-Type": "application/zip" } });
});
