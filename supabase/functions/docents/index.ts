// Edge Function «docents»: l'administrador crea i gestiona els comptes del professorat.
// Crida: POST { username, name, password }            -> { id, username }
//        POST { action: "password", id, password }    -> { ok: true }
//        POST { action: "delete", id }                -> { ok: true }   (només si no té alumnat)
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const EMAIL_DOMAIN = "professorat.llibrefq3.app";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json" } });
const USER_RE = /^[a-z0-9][a-z0-9._-]{2,29}$/;
const okPassword = (p: unknown) => typeof p === "string" && p.length >= 8 && p.length <= 72;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const url = Deno.env.get("SUPABASE_URL")!;
  const anon = Deno.env.get("SUPABASE_ANON_KEY")!;
  const service = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

  const caller = createClient(url, anon, { global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } } });
  const { data: me } = await caller.auth.getUser();
  if (!me?.user) return json({ error: "no_auth" }, 401);
  const admin = createClient(url, service);
  const { data: prof } = await admin.from("profiles").select("role").eq("id", me.user.id).single();
  if (prof?.role !== "admin") return json({ error: "forbidden" }, 403);

  const body = await req.json().catch(() => ({}));
  const target = async (id: string) => {
    const { data } = await admin.from("profiles").select("id, role").eq("id", id).maybeSingle();
    return data && (data.role === "teacher" || data.role === "admin") ? data : null;
  };

  if (body.action === "password") {
    if (!okPassword(body.password)) return json({ error: "weak_password" }, 400);
    if (!(await target(String(body.id)))) return json({ error: "not_found" }, 404);
    const { error } = await admin.auth.admin.updateUserById(String(body.id), { password: body.password });
    if (error) return json({ error: error.message }, 400);
    return json({ ok: true });
  }
  if (body.action === "delete") {
    const id = String(body.id);
    if (id === me.user.id) return json({ error: "self" }, 400);
    const t = await target(id);
    if (!t) return json({ error: "not_found" }, 404);
    if (t.role === "admin") return json({ error: "forbidden" }, 403);
    const { data: cs } = await admin.from("courses").select("id").eq("teacher_id", id);
    const ids = (cs ?? []).map((c: any) => c.id);
    if (ids.length) {
      const { count } = await admin.from("profiles").select("id", { count: "exact", head: true }).in("course_id", ids);
      if (count) return json({ error: "has_students" }, 400);
    }
    const { error } = await admin.auth.admin.deleteUser(id);
    if (error) return json({ error: error.message }, 400);
    return json({ ok: true });
  }

  const username = String(body.username ?? "").trim().toLowerCase();
  const name = String(body.name ?? "").trim().slice(0, 80);
  if (!USER_RE.test(username)) return json({ error: "bad_username" }, 400);
  if (!name) return json({ error: "bad_name" }, 400);
  if (!okPassword(body.password)) return json({ error: "weak_password" }, 400);
  const { data: dup } = await admin.from("profiles").select("id").eq("username", username).maybeSingle();
  if (dup) return json({ error: "username_taken" }, 409);
  const { data, error } = await admin.auth.admin.createUser({ email: `${username}@${EMAIL_DOMAIN}`, password: body.password, email_confirm: true });
  if (error || !data.user) return json({ error: error?.message ?? "create_failed" }, 400);
  const { error: e2 } = await admin.from("profiles").insert({ id: data.user.id, role: "teacher", display_name: name, username });
  if (e2) { await admin.auth.admin.deleteUser(data.user.id); return json({ error: e2.message }, 400); }
  return json({ id: data.user.id, username });
});
