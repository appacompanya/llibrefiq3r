// Pont del bucket privat «professorat» (llibre-fq3). Permet que Claude hi pugi i en baixi PDF
// sense demanar res al professor. Només s'activa des de SQL (net.http_post) amb el token del vault
// «professorat_pont_token», que no surt mai de la base de dades.
//
// Cos JSON (POST):
//   {"t": TOKEN, "accio": "puja"}                      puja les files de privat.pujades (direccio='puja', fet=false)
//   {"t": TOKEN, "accio": "baixa", "fitxers": [..]}    desa cada fitxer del bucket a privat.pujades (direccio='baixada', b64)
//   {"t": TOKEN, "accio": "copia_web", "fitxers": [..]} copia https://llibrefiq3r.cat/docs/<fitxer> al bucket
//   {"t": TOKEN, "accio": "copia_xifrat", "branca": B, "fitxers": [..]}
//        baixa <fitxer>.enc de la branca B del repositori (IV de 12 bytes + AES-256-GCM amb la clau
//        del vault «professorat_pont_clau»), el desxifra i el puja al bucket. Així els PDF del
//        professorat no són mai públics en clar.
import postgres from "npm:postgres@3.4.4";
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const sql = postgres(Deno.env.get("SUPABASE_DB_URL")!, { prepare: false, max: 1 });
const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const BUCKET = "professorat";
const NOM = /^[a-z0-9][a-z0-9._-]{0,120}\.pdf$/;

const b64ToBytes = (b64: string) => Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
function bytesToB64(u: Uint8Array) {
  let s = "";
  for (let i = 0; i < u.length; i += 0x8000) s += String.fromCharCode(...u.subarray(i, i + 0x8000));
  return btoa(s);
}

Deno.serve(async (req: Request) => {
  if (req.method !== "POST") return new Response("method", { status: 405 });
  const body = await req.json().catch(() => ({}));
  const [{ ok }] = await sql`select exists(select 1 from vault.decrypted_secrets where name = 'professorat_pont_token' and decrypted_secret = ${String(body.t || "")}) as ok`;
  if (!ok) return new Response("forbidden", { status: 403 });
  const log: string[] = [];
  const fitxers: string[] = (body.fitxers || []).filter((f: string) => NOM.test(f));

  if (body.accio === "puja") {
    const rows = await sql`select id, cami, b64 from privat.pujades where direccio = 'puja' and not fet order by id`;
    for (const r of rows) {
      if (!NOM.test(r.cami)) { await sql`update privat.pujades set fet = true, resultat = 'nom no vàlid' where id = ${r.id}`; continue; }
      const { error } = await sb.storage.from(BUCKET).upload(r.cami, b64ToBytes(r.b64), { upsert: true, contentType: "application/pdf" });
      const res = error ? "error " + error.message : "ok";
      await sql`update privat.pujades set fet = true, resultat = ${res}, b64 = case when ${!error} then null else b64 end where id = ${r.id}`;
      log.push(`${r.cami}\t${res}`);
    }
  } else if (body.accio === "baixa") {
    for (const f of fitxers) {
      const { data, error } = await sb.storage.from(BUCKET).download(f);
      if (error || !data) { log.push(`${f}\terror ${error?.message}`); continue; }
      const b64 = bytesToB64(new Uint8Array(await data.arrayBuffer()));
      await sql`insert into privat.pujades (cami, direccio, b64, fet, resultat) values (${f}, 'baixada', ${b64}, true, 'ok')`;
      log.push(`${f}\tok`);
    }
  } else if (body.accio === "copia_web") {
    for (const f of fitxers) {
      const r = await fetch(`https://llibrefiq3r.cat/docs/${f}`);
      if (!r.ok) { log.push(`${f}\terror web ${r.status}`); continue; }
      const { error } = await sb.storage.from(BUCKET).upload(f, new Uint8Array(await r.arrayBuffer()), { upsert: true, contentType: "application/pdf" });
      log.push(`${f}\t${error ? "error " + error.message : "ok"}`);
    }
  } else if (body.accio === "copia_xifrat") {
    const branca = String(body.branca || "");
    if (!/^[a-z0-9._/-]{1,80}$/.test(branca)) return new Response("branca", { status: 400 });
    const [{ k }] = await sql`select decrypted_secret as k from vault.decrypted_secrets where name = 'professorat_pont_clau'`;
    const key = await crypto.subtle.importKey("raw", Uint8Array.from(k.match(/../g).map((h: string) => parseInt(h, 16))), "AES-GCM", false, ["decrypt"]);
    for (const f of fitxers) {
      const r = await fetch(`https://raw.githubusercontent.com/appacompanya/llibrefiq3r/${branca}/xifrat/${f}.enc`);
      if (!r.ok) { log.push(`${f}\terror web ${r.status}`); continue; }
      const buf = new Uint8Array(await r.arrayBuffer());
      let pdf: Uint8Array;
      try { pdf = new Uint8Array(await crypto.subtle.decrypt({ name: "AES-GCM", iv: buf.slice(0, 12) }, key, buf.slice(12))); }
      catch { log.push(`${f}\terror desxifrant`); continue; }
      const { error } = await sb.storage.from(BUCKET).upload(f, pdf, { upsert: true, contentType: "application/pdf" });
      log.push(`${f}\t${error ? "error " + error.message : "ok " + pdf.length}`);
    }
  } else return new Response("accio", { status: 400 });

  return new Response(log.join("\n") + "\n", { headers: { "Content-Type": "text/plain; charset=utf-8" } });
});
