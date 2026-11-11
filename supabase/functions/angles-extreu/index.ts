// Edge Function «angles-extreu»: passa un examen de la PAU d'anglès (text dels PDF oficials) a dades estructurades
// per a la versió digital: preguntes i opcions del listening, text i preguntes del reading, temes del writing,
// i la clau / respostes model de les pautes oficials.
// - Només s'executa amb el token del Vault «imatges4_token» (cap alumne ni visitant la pot cridar).
// - Llegeix el text de tools/angles-pau/text/<id>.json (repositori públic; els PDF ja són públics).
// - Desa el resultat a public.kv «angles/extret/<id>» (només professorat) i no torna a cridar la IA si ja hi és.
import { createClient } from "npm:@supabase/supabase-js@2.45.4";
import postgres from "npm:postgres@3.4.4";

const RAW = "https://raw.githubusercontent.com/appacompanya/llibrefiq3r/main/tools/angles-pau/text/";
const MODELS = ["gpt-5.4-mini", "gpt-5.4-nano"];
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { "Content-Type": "application/json" } });

async function secret(name: string): Promise<string | null> {
  const sql = postgres(Deno.env.get("SUPABASE_DB_URL")!, { max: 1, prepare: false });
  try { const r = await sql`select decrypted_secret from vault.decrypted_secrets where name = ${name} limit 1`; return r[0]?.decrypted_secret ?? null; }
  finally { await sql.end({ timeout: 2 }); }
}

const SYSTEM = `You convert one Catalan university-entrance (PAU) English exam into JSON for a digital version.
You receive raw text extracted from the official PDFs: for each part (listening, reading, writing) the exam text ("examen") and the official marking guide ("pauta", may be empty).
Copy wording EXACTLY as in the exam (fix only PDF artefacts: broken hyphenation, stray line numbers, page headers/footers, the label "Listening · PAU …" at the top, score boxes like "Correcta Incorrecta No contestada", "Nota de …").
Return ONLY this JSON object:
{
 "listening": {
   "title": string,
   "intro": string,                     // the instructions before the questions, as shown to students (e.g. "In this radio programme you are going to hear some new words…")
   "glossary": [{"term": string, "meaning": string}],   // the new-words list (Catalan/Spanish meanings) if present
   "instructions": string,              // e.g. "Choose the best answer according to the recording. Only ONE answer is correct." plus the scoring line
   "questions": [{"n": int, "q": string, "options": [string, string, string, string], "answer": int|null}]  // answer = 0-based index of the correct option according to the pauta; null if the pauta does not say
 },
 "reading": {
   "title": string,
   "text": [string],                    // the article, one string per paragraph, verbatim, without line numbers
   "source": string,                    // credit line under the text, if any
   "glossary": [{"term": string, "meaning": string}],
   "instructions": string,
   "questions": [{"n": int, "type": "mc"|"open", "q": string, "options": [string] , "answer": int|null, "model": string, "points": number}]
       // "mc": multiple choice with options and answer index (from the pauta). "open": written answer; "model" = accepted answer(s) from the pauta (join alternatives with " / "), options = [].
       // Include every sub-question; points = value stated in the exam for that question (e.g. 0.5).
 },
 "writing": {
   "instructions": string,              // general instructions (word count, choose ONE option…)
   "words": [int, int],                 // min and max words, e.g. [125, 150]
   "options": [{"n": int, "prompt": string}],   // each writing task verbatim, including its context
   "criteria": string                   // writing marking criteria from the pauta, if present; else ""
 },
 "warnings": [string]                   // anything you could not read reliably (e.g. "pauta missing for listening")
}
Never invent content. If the pauta gives the correct answer as text, find the option that matches it. If an answer is not determinable, use null and add a warning.`;

async function chat(user: string): Promise<{ data: any; model: string }> {
  const key = await secret("openai_api_key");
  let last = "";
  for (const model of MODELS) {
    const r = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST", headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ model, messages: [{ role: "system", content: SYSTEM }, { role: "user", content: user }], response_format: { type: "json_object" }, reasoning_effort: "low", max_completion_tokens: 16000 }),
    });
    if (r.ok) { const o = await r.json(); return { data: JSON.parse(o.choices?.[0]?.message?.content || "{}"), model }; }
    last = (await r.text()).slice(0, 300);
  }
  throw new Error("model_error: " + last);
}

function check(d: any): string[] {
  const w: string[] = [];
  const L = d?.listening?.questions || [];
  if (L.length !== 8) w.push(`listening: ${L.length} preguntes`);
  L.forEach((q: any) => { if (!Array.isArray(q.options) || q.options.length !== 4) w.push(`listening ${q.n}: ${q.options?.length} opcions`); if (q.answer == null) w.push(`listening ${q.n}: sense clau`); });
  const R = d?.reading?.questions || [];
  if (R.length < 4) w.push(`reading: ${R.length} preguntes`);
  R.forEach((q: any) => { if (q.type === "mc" && q.answer == null) w.push(`reading ${q.n}: sense clau`); });
  if (!(d?.reading?.text || []).length) w.push("reading: sense text");
  if (!(d?.writing?.options || []).length) w.push("writing: sense temes");
  return w;
}

Deno.serve(async (req: Request) => {
  if (req.method !== "POST") return json({ error: "POST" }, 405);
  const { id, token, force } = await req.json().catch(() => ({}));
  if (!token || token !== (await secret("imatges4_token"))) return json({ error: "forbidden" }, 403);
  if (!/^\d{4}-[a-z]+(-tei)?-s\d+$/.test(String(id))) return json({ error: "bad_id" }, 400);
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const path = `angles/extret/${id}`;
  if (!force) {
    const { data } = await admin.from("kv").select("data").eq("path", path).maybeSingle();
    if (data?.data?.listening) return json({ id, cached: true, warnings: data.data._check || [] });
  }
  const src = await fetch(RAW + id + ".json");
  if (!src.ok) return json({ error: "no_text", status: src.status }, 404);
  const t = await src.json();
  const user = ["listening", "reading", "writing"].map((b) => `=== ${b.toUpperCase()} · EXAMEN ===\n${t[b]?.examen || ""}\n=== ${b.toUpperCase()} · PAUTA ===\n${t[b]?.pauta || "(cap)"}`).join("\n\n");
  try {
    const { data, model } = await chat(`Exam: PAU ${t.any} ${t.conv}${t.serie ? " · Sèrie " + t.serie : ""} (${t.model}).\n\n${user}`);
    data._check = check(data); data._model = model; data._id = id; data._at = new Date().toISOString();
    await admin.from("kv").upsert({ path, data, updated_at: new Date().toISOString() });
    return json({ id, model, warnings: data._check });
  } catch (e) {
    await admin.from("kv").upsert({ path: path + "/error", data: { error: String(e).slice(0, 500), at: new Date().toISOString() } });
    return json({ id, error: String(e).slice(0, 300) }, 500);
  }
});
