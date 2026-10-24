// Descarrega les imatges dels llibres (4t i 2n) generades amb privat.genera_imatge4.
// Protegida amb un token (vault: imatges4_token) al paràmetre ?t=.
// ?noms=a,b,c filtra per nom; ?pref=2n- filtra per prefix. Retorna un zip amb <nom>.jpg (l'última versió de cada nom).
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
  const t = url.searchParams.get("t") || "";
  const [{ ok }] = await sql`select exists(select 1 from vault.decrypted_secrets where name = 'imatges4_token' and decrypted_secret = ${t}) as ok`;
  if (!ok) return new Response("forbidden", { status: 403 });
  const noms = (url.searchParams.get("noms") || "").split(",").map((s) => s.trim()).filter(Boolean);
  const pref = (url.searchParams.get("pref") || "").replace(/[%_\\]/g, "");
  const rows = noms.length
    ? await sql`select distinct on (i.nom) i.nom, r.status_code, r.content from privat.imatges4 i join net._http_response r on r.id = i.request_id where i.nom = any(${noms}) order by i.nom, i.id desc`
    : pref
    ? await sql`select distinct on (i.nom) i.nom, r.status_code, r.content from privat.imatges4 i join net._http_response r on r.id = i.request_id where i.nom like ${pref + "%"} order by i.nom, i.id desc`
    : await sql`select distinct on (i.nom) i.nom, r.status_code, r.content from privat.imatges4 i join net._http_response r on r.id = i.request_id order by i.nom, i.id desc`;
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
  const zip = zipSync(files, { level: 0 });
  const stamp = new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
  return new Response(zip, {
    headers: {
      "Content-Type": "application/zip",
      "Content-Disposition": `attachment; filename="imatges-${pref || "llibre"}${stamp}.zip"`,
    },
  });
});
