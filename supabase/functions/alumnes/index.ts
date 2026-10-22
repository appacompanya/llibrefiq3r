// Edge Function «alumnes»: el docent crea comptes d'alumne amb un codi d'accés dins d'un dels seus cursos.
// Crida: POST { names: ["Nom Cognom", ...], course_id }  -> { students: [{id, name, code}] }
//        POST { action: "reset", id: "<uuid>" }          -> { code }
//        POST { action: "delete", id: "<uuid>" }         -> { ok: true }
// Un docent només pot tocar l'alumnat dels seus cursos; l'administrador, el de tots.
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const EMAIL_DOMAIN = "alumnes.llibrefq3.app";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json" } });

// codi tipus "K7QM-4TXR" (sense lletres confusibles)
function newCode() {
  const A = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  const r = crypto.getRandomValues(new Uint8Array(8));
  const s = Array.from(r, (n) => A[n % A.length]).join("");
  return s.slice(0, 4) + "-" + s.slice(4);
}
const emailFor = (code: string) => `${code.toLowerCase()}@${EMAIL_DOMAIN}`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const url = Deno.env.get("SUPABASE_URL")!;
  const anon = Deno.env.get("SUPABASE_ANON_KEY")!;
  const service = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

  // 1) qui fa la crida? ha de ser professorat
  const caller = createClient(url, anon, { global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } } });
  const { data: me } = await caller.auth.getUser();
  if (!me?.user) return json({ error: "no_auth" }, 401);
  const admin = createClient(url, service);
  const { data: prof } = await admin.from("profiles").select("role").eq("id", me.user.id).single();
  if (prof?.role !== "teacher" && prof?.role !== "admin") return json({ error: "forbidden" }, 403);
  const isAdmin = prof.role === "admin";

  // el curs és del docent que crida?
  const ownCourse = async (cid: string) => {
    const { data } = await admin.from("courses").select("id, name, teacher_id").eq("id", cid).maybeSingle();
    return data && (isAdmin || data.teacher_id === me.user.id) ? data : null;
  };
  // l'alumne és d'un curs del docent que crida?
  const ownStudent = async (sid: string) => {
    const { data } = await admin.from("profiles").select("id, role, course_id").eq("id", sid).maybeSingle();
    if (!data || data.role !== "student") return false;
    if (isAdmin) return true;
    return !!(data.course_id && (await ownCourse(data.course_id)));
  };

  const body = await req.json().catch(() => ({}));

  if (body.action === "reset" && body.id) {
    if (!(await ownStudent(String(body.id)))) return json({ error: "forbidden" }, 403);
    const code = newCode();
    const { error } = await admin.auth.admin.updateUserById(body.id, { email: emailFor(code), password: code, email_confirm: true });
    if (error) return json({ error: error.message }, 400);
    await admin.from("profiles").update({ code }).eq("id", body.id);
    return json({ code });
  }
  if (body.action === "delete" && body.id) {
    if (!(await ownStudent(String(body.id)))) return json({ error: "forbidden" }, 403);
    const { error } = await admin.auth.admin.deleteUser(body.id);
    if (error) return json({ error: error.message }, 400);
    return json({ ok: true });
  }

  // compatibilitat amb la zona del professorat antiga (sense cursos): si el docent només té un curs, és aquest
  if (!body.course_id) {
    const { data: cs } = await admin.from("courses").select("id").eq("teacher_id", me.user.id);
    if (cs && cs.length === 1) body.course_id = cs[0].id;
  }
  const course = await ownCourse(String(body.course_id ?? ""));
  if (!course) return json({ error: "bad_course" }, 400);
  const names: string[] = (body.names ?? []).map((n: string) => String(n).trim()).filter(Boolean).slice(0, 60);
  const out: { id: string; name: string; code: string }[] = [];
  for (const name of names) {
    const code = newCode();
    const { data, error } = await admin.auth.admin.createUser({ email: emailFor(code), password: code, email_confirm: true });
    if (error || !data.user) return json({ error: error?.message ?? "create_failed", created: out }, 400);
    await admin.from("profiles").insert({ id: data.user.id, role: "student", display_name: name.slice(0, 80), grup: course.name.slice(0, 20), code, course_id: course.id });
    out.push({ id: data.user.id, name, code });
  }
  return json({ students: out });
});
