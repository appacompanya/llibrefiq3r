/* Capa de dades: Supabase (si config.js té URL i clau pública) o mode demostració (dades al navegador). */
(function (G) {
  "use strict";
  const CFG = G.FQ_CONFIG || {};
  const EMAIL_DOMAIN = "alumnes.llibrefq3.app";
  const normCode = (c) => String(c || "").toUpperCase().replace(/[^A-Z0-9]/g, "").replace(/^(.{4})(.{4})$/, "$1-$2");

  /* ---------------- Mode demostració ---------------- */
  function demoStore() {
    const KEY = "fq3-demo-db-v1";
    const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || null; } catch { return null; } };
    let db = load();
    if (!db) {
      db = { settings: { auto_calc: true }, students: [], responses: {}, submissions: {}, feedback: {}, photos: {} };
      ["Alumne/a 01 (exemple)", "Alumne/a 02 (exemple)", "Alumne/a 03 (exemple)"].forEach((n, i) =>
        db.students.push({ id: "demo" + (i + 1), display_name: n, grup: "3r A", code: "DEMO-000" + (i + 1), role: "student" }));
    }
    const save = () => { try { localStorage.setItem(KEY, JSON.stringify(db)); } catch {} };
    let me = null; try { me = JSON.parse(sessionStorage.getItem("fq3-demo-me")); } catch {}
    const setMe = (p) => { me = p; try { p ? sessionStorage.setItem("fq3-demo-me", JSON.stringify(p)) : sessionStorage.removeItem("fq3-demo-me"); } catch {} };
    const k = (...a) => a.join("|");
    return {
      mode: "demo",
      async init() { return me; },
      async signInStudent(code) { const s = db.students.find((x) => x.code === normCode(code)); if (!s) throw new Error("bad_code"); setMe(s); return s; },
      async signInTeacher() { const t = { id: "teacher", role: "teacher", display_name: "Professor (demostració)" }; setMe(t); return t; },
      async signOut() { setMe(null); },
      me: () => me,
      async getSettings() { return { ...db.settings }; },
      async setSetting(key, value) { db.settings[key] = value; save(); },
      async loadResponses(ws, sid = me.id) { const o = {}; for (const [kk, v] of Object.entries(db.responses)) { const [s, w, it] = kk.split("|"); if (s === sid && w === ws) o[it] = v; } return o; },
      async saveResponse(ws, item, answer) { db.responses[k(me.id, ws, item)] = answer; save(); },
      async getSubmission(ws, sid = me.id) { return db.submissions[k(sid, ws)] || { status: "draft", photos: [] }; },
      async submit(ws) { const s = db.submissions[k(me.id, ws)] || { photos: [] }; s.status = "submitted"; s.submitted_at = new Date().toISOString(); db.submissions[k(me.id, ws)] = s; save(); },
      async addPhoto(ws, item, file) {
        const data = await new Promise((res) => { const r = new FileReader(); r.onload = () => res(r.result); r.readAsDataURL(file); });
        const path = `${me.id}/${ws}/${item || "full"}/${Date.now()}`; db.photos[path] = data;
        const s = db.submissions[k(me.id, ws)] || { status: "draft", photos: [] }; s.photos = [...(s.photos || []), { path, item }]; db.submissions[k(me.id, ws)] = s; save(); return path;
      },
      async removePhoto(ws, path) { delete db.photos[path]; const s = db.submissions[k(me.id, ws)]; if (s) s.photos = s.photos.filter((p) => p.path !== path); save(); },
      async photoUrl(path) { return db.photos[path] || ""; },
      async myFeedback(ws) { return Object.entries(db.feedback).filter(([kk, v]) => kk.startsWith(k(me.id, ws) + "|") && v.released).map(([kk, v]) => ({ item_id: kk.split("|")[2], ...v })); },
      // professorat
      async listStudents() { return db.students.map((s) => ({ ...s })); },
      async createStudents(names, grup) {
        const A = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; const out = [];
        for (const n of names) { let c = ""; for (let i = 0; i < 8; i++) c += A[Math.floor(Math.random() * A.length)]; c = c.slice(0, 4) + "-" + c.slice(4);
          const s = { id: "s" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6), display_name: n, grup, code: c, role: "student" }; db.students.push(s); out.push(s); }
        save(); return out;
      },
      async resetCode(id) { const s = db.students.find((x) => x.id === id); const A = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; let c = ""; for (let i = 0; i < 8; i++) c += A[Math.floor(Math.random() * A.length)]; s.code = c.slice(0, 4) + "-" + c.slice(4); save(); return s.code; },
      async deleteStudent(id) { db.students = db.students.filter((x) => x.id !== id); save(); },
      async listSubmissions() { return Object.entries(db.submissions).map(([kk, v]) => ({ student_id: kk.split("|")[0], worksheet_id: kk.split("|")[1], ...v })); },
      async listResponseKeys() { const s = new Set(); Object.keys(db.responses).forEach((kk) => { const [a, b] = kk.split("|"); s.add(a + "|" + b); }); return [...s].map((x) => ({ student_id: x.split("|")[0], worksheet_id: x.split("|")[1] })); },
      async feedbackFor(sid, ws) { return Object.entries(db.feedback).filter(([kk]) => kk.startsWith(k(sid, ws) + "|")).map(([kk, v]) => ({ item_id: kk.split("|")[2], ...v })); },
      async saveFeedback(sid, ws, rows) { rows.forEach((r) => { db.feedback[k(sid, ws, r.item_id)] = { ...(db.feedback[k(sid, ws, r.item_id)] || {}), ...r }; }); save(); },
      async release(sid, ws) { Object.entries(db.feedback).forEach(([kk, v]) => { if (kk.startsWith(k(sid, ws) + "|")) v.released = true; }); const s = db.submissions[k(sid, ws)] || { photos: [] }; s.status = "returned"; s.returned_at = new Date().toISOString(); db.submissions[k(sid, ws)] = s; save(); },
      async reopen(sid, ws) { const s = db.submissions[k(sid, ws)]; if (s) { s.status = "draft"; save(); } },
      async proposeAI() { throw new Error("demo_no_ai"); },
      resetDemo() { try { localStorage.removeItem(KEY); sessionStorage.removeItem("fq3-demo-me"); } catch {} location.reload(); },
    };
  }

  /* ---------------- Supabase ---------------- */
  function supaStore() {
    const sb = G.supabase.createClient(CFG.SUPABASE_URL, CFG.SUPABASE_ANON_KEY, { auth: { persistSession: true, storageKey: "fq3-auth" } });
    let me = null;
    const must = ({ data, error }) => { if (error) throw error; return data; };
    async function loadProfile() {
      const { data: u } = await sb.auth.getUser(); if (!u?.user) { me = null; return null; }
      const { data } = await sb.from("profiles").select("id, role, display_name, grup").eq("id", u.user.id).maybeSingle();
      me = data || null; return me;
    }
    async function fn(name, body) {
      const { data, error } = await sb.functions.invoke(name, { body });
      if (error) { let msg = error.message; try { msg = (await error.context.json()).error || msg; } catch {} throw new Error(msg); }
      return data;
    }
    return {
      mode: "supabase", client: sb,
      async init() { return loadProfile(); },
      async signInStudent(code) {
        const c = normCode(code);
        const { error } = await sb.auth.signInWithPassword({ email: `${c.toLowerCase()}@${EMAIL_DOMAIN}`, password: c });
        if (error) throw new Error("bad_code");
        const p = await loadProfile(); if (!p) throw new Error("no_profile"); return p;
      },
      async signInTeacher(email, password) {
        const { error } = await sb.auth.signInWithPassword({ email, password }); if (error) throw new Error("bad_login");
        const p = await loadProfile(); if (p?.role !== "teacher") { await sb.auth.signOut(); throw new Error("not_teacher"); } return p;
      },
      async signOut() { await sb.auth.signOut(); me = null; },
      me: () => me,
      async getSettings() { const rows = must(await sb.from("settings").select("key, value")); return Object.fromEntries(rows.map((r) => [r.key, r.value])); },
      async setSetting(key, value) { must(await sb.from("settings").upsert({ key, value, updated_at: new Date().toISOString() })); },
      async loadResponses(ws, sid = me.id) { const rows = must(await sb.from("responses").select("item_id, answer").eq("student_id", sid).eq("worksheet_id", ws)); return Object.fromEntries(rows.map((r) => [r.item_id, r.answer])); },
      async saveResponse(ws, item, answer) { must(await sb.from("responses").upsert({ student_id: me.id, worksheet_id: ws, item_id: item, answer, updated_at: new Date().toISOString() })); },
      async getSubmission(ws, sid = me.id) { const r = must(await sb.from("submissions").select("*").eq("student_id", sid).eq("worksheet_id", ws).maybeSingle()); return r || { status: "draft", photos: [] }; },
      async submit(ws) { must(await sb.from("submissions").upsert({ student_id: me.id, worksheet_id: ws, status: "submitted", submitted_at: new Date().toISOString() })); },
      async addPhoto(ws, item, file) {
        const ext = (file.type.split("/")[1] || "jpg").replace("jpeg", "jpg");
        const path = `${me.id}/${ws}/${item || "full"}/${Date.now()}.${ext}`;
        must(await sb.storage.from("fotos").upload(path, file, { contentType: file.type, upsert: false }));
        const cur = await this.getSubmission(ws);
        must(await sb.from("submissions").upsert({ student_id: me.id, worksheet_id: ws, status: cur.status === "submitted" ? "submitted" : "draft", photos: [...(cur.photos || []), { path, item }] }));
        return path;
      },
      async removePhoto(ws, path) {
        await sb.storage.from("fotos").remove([path]);
        const cur = await this.getSubmission(ws);
        must(await sb.from("submissions").upsert({ student_id: me.id, worksheet_id: ws, status: cur.status, photos: (cur.photos || []).filter((p) => p.path !== path) }));
      },
      async photoUrl(path) { const { data } = await sb.storage.from("fotos").createSignedUrl(path, 3600); return data?.signedUrl || ""; },
      async myFeedback(ws) { return must(await sb.from("feedback").select("item_id, level, comment").eq("student_id", me.id).eq("worksheet_id", ws).eq("released", true)); },
      // professorat
      async listStudents() { return must(await sb.from("profiles").select("id, display_name, grup, code, role").eq("role", "student").order("grup").order("display_name")); },
      async createStudents(names, grup) { return (await fn("alumnes", { names, grup })).students.map((s) => ({ id: s.id, display_name: s.name, grup, code: s.code })); },
      async resetCode(id) { return (await fn("alumnes", { action: "reset", id })).code; },
      async deleteStudent(id) { await fn("alumnes", { action: "delete", id }); },
      async listSubmissions() { return must(await sb.from("submissions").select("*")); },
      async listResponseKeys() { return must(await sb.from("responses").select("student_id, worksheet_id")); },
      async feedbackFor(sid, ws) { return must(await sb.from("feedback").select("*").eq("student_id", sid).eq("worksheet_id", ws)); },
      async saveFeedback(sid, ws, rows) { must(await sb.from("feedback").upsert(rows.map((r) => ({ student_id: sid, worksheet_id: ws, ...r, updated_at: new Date().toISOString() })))); },
      async release(sid, ws) {
        must(await sb.from("feedback").update({ released: true }).eq("student_id", sid).eq("worksheet_id", ws));
        must(await sb.from("submissions").upsert({ student_id: sid, worksheet_id: ws, status: "returned", returned_at: new Date().toISOString() }));
      },
      async reopen(sid, ws) { must(await sb.from("submissions").update({ status: "draft" }).eq("student_id", sid).eq("worksheet_id", ws)); },
      async proposeAI(sid, ws, items) { return fn("corregeix", { student_id: sid, worksheet_id: ws, items }); },
    };
  }

  G.FQStore = (CFG.SUPABASE_URL && CFG.SUPABASE_ANON_KEY && G.supabase) ? supaStore() : demoStore();
  G.FQStore.normCode = normCode;
})(window);
