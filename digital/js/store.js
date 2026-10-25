/* Capa de dades: Supabase (si config.js té URL i clau pública) o mode demostració (dades al navegador).
   Rols: alumne (student), docent (teacher) i administrador (admin, també és docent).
   Cada docent té cursos (2n, 3r o 4t d'ESO) i cada alumne és d'un curs. */
(function (G) {
  "use strict";
  const CFG = G.FQ_CONFIG || {};
  const EMAIL_DOMAIN = "alumnes.llibrefq3.app";
  const normCode = (c) => String(c || "").toUpperCase().replace(/[^A-Z0-9]/g, "").replace(/^(.{4})(.{4})$/, "$1-$2");
  const isStaff = (p) => !!p && (p.role === "teacher" || p.role === "admin");
  const LEVELS = ["2n", "3r", "4t"];
  /* perfils d'adaptació (NESE) que pot assignar el docent */
  const ADAPT = ["dislexia", "nouvingut", "basics", "discalculia", "tdah", "tea"];
  /* ajudes que l'alumne pot desactivar (continguts bàsics no: el decideix el docent) */
  const AJUDES = ["lletra", "veu", "glossari", "passos", "pantalla", "guia"];
  /* curs triat a la zona del professorat (es recorda en aquest navegador) */
  const CUR_KEY = "fq-curs";
  const getCur = () => { try { return localStorage.getItem(CUR_KEY) || null; } catch { return null; } };
  const setCur = (id) => { try { id ? localStorage.setItem(CUR_KEY, id) : localStorage.removeItem(CUR_KEY); } catch {} };
  const month = () => new Date().toISOString().slice(0, 7);

  /* ---------------- Mode demostració ---------------- */
  function demoStore() {
    const KEY = "fq3-demo-db-v5";
    /* Comptes fixos de la demostració. S'han de poder fer servir sempre: si el navegador ja té dades,
       o si un docent ha reiniciat o esborrat el codi, es tornen a posar a cada càrrega. */
    const SEED_COURSES = [
      { id: "c-demo", name: "3r A (exemple)", level: "3r", teacher_id: "teacher", settings: { auto_calc: true } },
      { id: "c-demo2", name: "2n A (exemple)", level: "2n", teacher_id: "teacher", settings: { auto_calc: true } },
      { id: "c-demo4", name: "4t A (exemple)", level: "4t", teacher_id: "teacher", settings: { auto_calc: true } },
    ];
    const SEED_STUDENTS = [
      { id: "demo1", display_name: "Alumne/a 01 (exemple)", grup: "3r A (exemple)", code: "DEMO-0001", role: "student", course_id: "c-demo" },
      { id: "demo2", display_name: "Alumne/a 02 (exemple)", grup: "3r A (exemple)", code: "DEMO-0002", role: "student", course_id: "c-demo" },
      { id: "demo3", display_name: "Alumne/a 03 (exemple)", grup: "3r A (exemple)", code: "DEMO-0003", role: "student", course_id: "c-demo" },
      { id: "demo2n1", display_name: "Alumne/a 2n 01 (exemple)", grup: "2n A (exemple)", code: "DEMO-2001", role: "student", course_id: "c-demo2" },
      { id: "demo2n2", display_name: "Alumne/a 2n 02 (exemple)", grup: "2n A (exemple)", code: "DEMO-2002", role: "student", course_id: "c-demo2" },
      { id: "demo4t1", display_name: "Alumne/a 4t 01 (exemple)", grup: "4t A (exemple)", code: "DEMO-4001", role: "student", course_id: "c-demo4" },
      { id: "demo4t2", display_name: "Alumne/a 4t 02 (exemple)", grup: "4t A (exemple)", code: "DEMO-4002", role: "student", course_id: "c-demo4" },
    ];
    const seedIds = new Set(SEED_STUDENTS.map((s) => s.id));
    const seedCodes = new Set(SEED_STUDENTS.map((s) => s.code));
    const isSeedStudent = (s) => !!s && (seedIds.has(s.id) || seedCodes.has(s.code));
    const newCode = () => { const A = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; let c = ""; for (let i = 0; i < 8; i++) c += A[Math.floor(Math.random() * A.length)]; return c.slice(0, 4) + "-" + c.slice(4); };
    const asObj = (v) => (v && typeof v === "object" && !Array.isArray(v) ? v : {});
    function ensureDemoSeeds(db) {
      db.settings = asObj(db.settings);
      if (db.settings.auto_calc == null) db.settings.auto_calc = true;
      db.teachers = Array.isArray(db.teachers) ? db.teachers : [];
      db.courses = Array.isArray(db.courses) ? db.courses : [];
      db.students = Array.isArray(db.students) ? db.students : [];
      db.responses = asObj(db.responses);
      db.submissions = asObj(db.submissions);
      db.feedback = asObj(db.feedback);
      db.photos = asObj(db.photos);
      if (!db.teachers.some((t) => t.id === "teacher"))
        db.teachers.unshift({ id: "teacher", role: "admin", display_name: "Professor (demostració)", username: "docent" });
      for (const c of SEED_COURSES) {
        let cur = db.courses.find((x) => x.id === c.id);
        if (!cur) { cur = { ...c, settings: { ...c.settings } }; db.courses.push(cur); }
        cur.level = c.level;
        if (!cur.teacher_id) cur.teacher_id = c.teacher_id;
        if (!cur.name) cur.name = c.name;
        if (!cur.settings || typeof cur.settings !== "object") cur.settings = { auto_calc: true };
      }
      for (const s of db.students) {
        if (seedIds.has(s.id) || !seedCodes.has(s.code)) continue;
        let c = newCode();
        while (seedCodes.has(c) || db.students.some((x) => x !== s && x.code === c)) c = newCode();
        s.code = c;
      }
      for (const s of SEED_STUDENTS) {
        const course = db.courses.find((c) => c.id === s.course_id);
        let cur = db.students.find((x) => x.id === s.id);
        if (!cur) { cur = { ...s }; db.students.push(cur); }
        cur.code = s.code;
        cur.role = "student";
        cur.course_id = s.course_id;
        if (!cur.display_name) cur.display_name = s.display_name;
        cur.grup = (course && course.name) || cur.grup || s.grup;
      }
    }
    const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || null; } catch { return null; } };
    let db = load();
    if (!db || typeof db !== "object" || Array.isArray(db)) db = {};
    ensureDemoSeeds(db);
    const save = () => { try { localStorage.setItem(KEY, JSON.stringify(db)); } catch {} };
    save();
    let me = null; try { me = JSON.parse(sessionStorage.getItem("fq3-demo-me")); } catch {}
    const setMe = (p) => { me = p; try { p ? sessionStorage.setItem("fq3-demo-me", JSON.stringify(p)) : sessionStorage.removeItem("fq3-demo-me"); } catch {} };
    const k = (...a) => a.join("|");
    const rid = (p) => p + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
    const course = (id) => db.courses.find((c) => c.id === id);
    const mine = () => db.courses.filter((c) => me && (me.role === "admin" || c.teacher_id === me.id));
    const sub = (sid, ws) => db.submissions[k(sid, ws)];
    return {
      mode: "demo", client: null,
      async init() { ensureDemoSeeds(db); save(); return me; },
      async signInStudent(code) { ensureDemoSeeds(db); save(); const s = db.students.find((x) => x.code === normCode(code)); if (!s) throw new Error("bad_code"); setMe(s); return s; },
      async signInTeacher(user, pw) {
        const t = db.teachers.find((x) => x.username === String(user).trim().toLowerCase());
        if (!t || pw !== (t.password || "docent")) throw new Error("bad_login");
        setMe(t); return t;
      },
      async signOut() { setMe(null); },
      me: () => me,
      // cursos
      curCourse: () => { const c = getCur(); return mine().some((x) => x.id === c) ? c : null; },
      setCourse: setCur,
      async listCourses() { return mine().map((c) => ({ ...c, teacher_name: (db.teachers.find((t) => t.id === c.teacher_id) || {}).display_name || "" })); },
      async createCourse(name, level) { const c = { id: rid("c"), name: String(name).slice(0, 60), level, teacher_id: me.id, settings: { auto_calc: true } }; db.courses.push(c); save(); return c; },
      async renameCourse(id, name) { const c = course(id); if (c) { c.name = String(name).slice(0, 60); db.students.filter((s) => s.course_id === id).forEach((s) => (s.grup = c.name)); save(); } },
      async deleteCourse(id) { if (db.students.some((s) => s.course_id === id)) throw new Error("has_students"); db.courses = db.courses.filter((c) => c.id !== id); save(); },
      async myLevel() { return me && me.course_id ? ((course(me.course_id) || {}).level || null) : null; },
      async getSettings() {
        const cid = me && me.role === "student" ? me.course_id : this.curCourse();
        return { ...db.settings, ...((course(cid) || {}).settings || {}) };
      },
      async setSetting(key, value) { const c = course(this.curCourse()); if (c) { c.settings = { ...c.settings, [key]: value }; save(); } else { db.settings[key] = value; save(); } },
      async loadResponses(ws, sid = me.id) { const o = {}; for (const [kk, v] of Object.entries(db.responses)) { const [s, w, it] = kk.split("|"); if (s === sid && w === ws) o[it] = v; } return o; },
      async saveResponse(ws, item, answer) { db.responses[k(me.id, ws, item)] = answer; save(); },
      async getSubmission(ws, sid = me.id) { return sub(sid, ws) || { status: "draft", photos: [] }; },
      async submit(ws) { const s = sub(me.id, ws) || { photos: [] }; s.status = "submitted"; s.submitted_at = new Date().toISOString(); s.review = null; s.review_items = []; db.submissions[k(me.id, ws)] = s; save(); },
      async addPhoto(ws, item, file) {
        const data = await new Promise((res) => { const r = new FileReader(); r.onload = () => res(r.result); r.readAsDataURL(file); });
        const path = `${me.id}/${ws}/${item || "full"}/${Date.now()}`; db.photos[path] = data;
        const s = sub(me.id, ws) || { status: "draft", photos: [] }; s.photos = [...(s.photos || []), { path, item }]; db.submissions[k(me.id, ws)] = s; save(); return path;
      },
      async removePhoto(ws, path) { delete db.photos[path]; const s = sub(me.id, ws); if (s) s.photos = s.photos.filter((p) => p.path !== path); save(); },
      async photoUrl(path) { return db.photos[path] || ""; },
      async myFeedback(ws) { return Object.entries(db.feedback).filter(([kk, v]) => kk.startsWith(k(me.id, ws) + "|") && v.released).map(([kk, v]) => ({ item_id: kk.split("|")[2], ...v })); },
      // professorat
      async listStudents(cid = this.curCourse()) { const ids = new Set(mine().map((c) => c.id)); return db.students.filter((s) => cid ? s.course_id === cid : ids.has(s.course_id)).map((s) => ({ ...s })); },
      async createStudents(names, cid = this.curCourse()) {
        const c = course(cid); if (!c) throw new Error("bad_course"); const out = [];
        for (const n of names) { const s = { id: rid("s"), display_name: n, grup: c.name, code: newCode(), role: "student", course_id: c.id }; db.students.push(s); out.push(s); }
        save(); return out;
      },
      async resetCode(id) {
        ensureDemoSeeds(db);
        const s = db.students.find((x) => x.id === id);
        if (!s) throw new Error("bad_student");
        if (isSeedStudent(s)) { save(); throw new Error("Els comptes de demostració conserven el codi DEMO."); }
        s.code = newCode(); ensureDemoSeeds(db); save(); return s.code;
      },
      async setAdaptacions(id, list, idioma) { const s = db.students.find((x) => x.id === id); if (!s) throw new Error("bad_student"); s.adaptacions = (list || []).filter((x) => ADAPT.includes(x)); s.adapt_idioma = s.adaptacions.includes("nouvingut") ? (idioma || null) : null; save(); },
      async myAdaptacions() { const s = me && db.students.find((x) => x.id === me.id); return (s && s.adaptacions) || []; },
      async myAdapt() { const s = me && db.students.find((x) => x.id === me.id); return { perfils: (s && s.adaptacions) || [], idioma: (s && s.adapt_idioma) || null }; },
      async getPrefs() { const s = me && db.students.find((x) => x.id === me.id); return { mode: (s && s.mode_fitxes) || "digital", ajudes_off: (s && s.ajudes_off) || [] }; },
      async setPrefs(p) { const s = me && db.students.find((x) => x.id === me.id); if (!s) return; if (p.mode) s.mode_fitxes = p.mode === "paper" ? "paper" : "digital"; if (p.ajudes_off) s.ajudes_off = p.ajudes_off.filter((x) => AJUDES.includes(x)); save(); },
      async getMode() { const s = me && db.students.find((x) => x.id === me.id); return (s && s.mode_fitxes) || "digital"; },
      async setMode(m) { const s = me && db.students.find((x) => x.id === me.id); if (s) { s.mode_fitxes = m === "paper" ? "paper" : "digital"; save(); } },
      async deleteStudent(id) {
        const s = db.students.find((x) => x.id === id);
        if (isSeedStudent(s)) throw new Error("Els comptes de demostració no es poden esborrar.");
        db.students = db.students.filter((x) => x.id !== id);
        ensureDemoSeeds(db); save();
      },
      async listSubmissions() { return Object.entries(db.submissions).map(([kk, v]) => ({ student_id: kk.split("|")[0], worksheet_id: kk.split("|")[1], ...v })); },
      async listResponseKeys() { const s = new Set(); Object.keys(db.responses).forEach((kk) => { const [a, b] = kk.split("|"); s.add(a + "|" + b); }); return [...s].map((x) => ({ student_id: x.split("|")[0], worksheet_id: x.split("|")[1] })); },
      async feedbackFor(sid, ws) { return Object.entries(db.feedback).filter(([kk]) => kk.startsWith(k(sid, ws) + "|")).map(([kk, v]) => ({ item_id: kk.split("|")[2], ...v })); },
      async saveFeedback(sid, ws, rows) { rows.forEach((r) => { db.feedback[k(sid, ws, r.item_id)] = { ...(db.feedback[k(sid, ws, r.item_id)] || {}), ...r }; }); save(); },
      async release(sid, ws) { Object.entries(db.feedback).forEach(([kk, v]) => { if (kk.startsWith(k(sid, ws) + "|")) v.released = true; }); const s = sub(sid, ws) || { photos: [] }; s.status = "returned"; s.returned_at = new Date().toISOString(); s.review = "done"; db.submissions[k(sid, ws)] = s; save(); },
      async reopen(sid, ws) { const s = sub(sid, ws); if (s) { s.status = "draft"; s.review = null; s.review_items = []; } Object.keys(db.feedback).forEach((kk) => { if (kk.startsWith(k(sid, ws) + "|auto:")) delete db.feedback[kk]; }); save(); },
      async markReviewed(sid, ws) { const s = sub(sid, ws); if (s) { s.review = "done"; save(); } },
      // correcció automàtica (demostració: només amb la comprovació automàtica de la fitxa, sense IA)
      async autoCorrect(ws, title, sda, items, sid = me.id) {
        const lvOf = (sc) => sc == null ? null : sc >= 0.95 ? "AE" : sc >= 0.75 ? "AN" : sc >= 0.5 ? "AS" : "NA";
        const now = new Date().toISOString(); const rows = []; const review = [];
        const errs = (x) => { const e = []; if (!x.answer || x.answer === "(sense resposta)") e.push("incompleta"); else if (x.score != null && x.score < 0.95) { if (/unitat/i.test(String(x.auto))) e.push("unitats"); else e.push(/V |F |tf/.test(x.answer) ? "conceptual" : "càlcul"); } return e; };
        items.forEach((x) => { const blank = x.answer === "(sense resposta)"; const lv = blank ? "NA" : lvOf(x.score); if (!blank && x.score == null) review.push(x.id);
          const note = blank ? "No has respost aquesta pregunta." : x.score == null ? "Aquesta resposta la corregirà el professor (en mode demostració no hi ha IA)." : x.score >= 0.95 ? "Correcte. Bona feina!" : `La comprovació automàtica indica errors (${x.auto}). Revisa el càlcul i les unitats.`;
          rows.push({ item_id: "auto:" + x.id, level: lv, comment: note, released: true, updated_at: now });
          const cur = db.feedback[k(sid, ws, x.id)] || { released: false }; db.feedback[k(sid, ws, x.id)] = { ...cur, proposal_level: lv, proposal_note: note }; });
        const sc = items.map((x) => x.score).filter((v) => v != null); const avg = sc.length ? sc.reduce((a, b) => a + b, 0) / sc.length : null;
        rows.push({ item_id: "auto:_global", level: lvOf(avg), comment: review.length ? `Hi ha ${review.length === 1 ? "una pregunta" : review.length + " preguntes"} que corregirà el professor.` : avg == null ? "Aquesta fitxa la corregirà el professor." : `Has encertat aproximadament el ${Math.round(avg * 100)} % dels apartats que es poden comprovar automàticament.`, released: true, updated_at: now });
        rows.forEach((r) => { db.feedback[k(sid, ws, r.item_id)] = r; });
        const s = sub(sid, ws); if (s && s.status === "submitted") { s.review = "pending"; s.review_items = review; }
        db.kv = db.kv || {}; db.kv[`errors/${sid}/${ws}`] = { sda, at: now, items: items.map((x) => ({ id: x.id, level: lvOf(x.score), errors: errs(x) })), global: rows[rows.length - 1].comment };
        save(); return rows;
      },
      async deleteAuto(sid, ws) { Object.keys(db.feedback).forEach((kk) => { if (kk.startsWith(k(sid, ws) + "|auto:")) delete db.feedback[kk]; }); save(); },
      async allFeedback() { return Object.entries(db.feedback).map(([kk, v]) => { const [a, b, c] = kk.split("|"); return { student_id: a, worksheet_id: b, item_id: c, level: v.level || null, proposal_level: v.proposal_level || null, released: !!v.released }; }); },
      async errorsAll() { return Object.entries(db.kv || {}).filter(([p]) => p.startsWith("errors/")).map(([p, d]) => ({ student_id: p.split("/")[1], worksheet_id: p.split("/")[2], ...d })); },
      async getInforme(sid) { return (db.kv || {})["informe/" + sid] || null; },
      async makeInforme(sid, data) {
        const sd = data.sdas || []; const lv = sd.filter((x) => x.mitjana != null);
        const top = Object.entries(data.errors || {}).sort((a, b) => b[1] - a[1]).slice(0, 3).map(([e, n]) => `${e} (${n})`);
        const tr = lv.length > 1 ? (lv[lv.length - 1].mitjana > lv[0].mitjana + 0.2 ? "millora" : lv[lv.length - 1].mitjana < lv[0].mitjana - 0.2 ? "empitjora" : "es manté estable") : null;
        const rec = { resum: `Informe de demostració, calculat sense IA a partir de ${data.lliurades || 0} fitxes lliurades.`, fortaleses: lv.filter((x) => x.mitjana >= 3).map((x) => `SdA ${x.sda}: nivell mitjà alt`), errors: top.length ? ["Errors més freqüents: " + top.join(", ")] : ["Encara no hi ha prou dades."], progres: tr ? `D'una SdA a la següent, el nivell ${tr}.` : "Cal més d'una SdA per comparar el progrés.", propostes: ["Amb la connexió al servidor, aquest informe l'escriu la IA."], at: new Date().toISOString() };
        db.kv = db.kv || {}; db.kv["informe/" + sid] = rec; save(); return rec;
      },
      async usage() { return { month: month(), calls: 0, usd: 0 }; },
      // docents (només administrador)
      async listTeachers() { return db.teachers.map((t) => ({ ...t, courses: db.courses.filter((c) => c.teacher_id === t.id).map((c) => ({ ...c, n: db.students.filter((s) => s.course_id === c.id).length })) })); },
      async createTeacher({ username, name, password }) {
        const u = String(username).trim().toLowerCase(); if (!/^[a-z0-9][a-z0-9._-]{2,29}$/.test(u)) throw new Error("bad_username"); if (String(password).length < 8) throw new Error("weak_password");
        if (db.teachers.some((t) => t.username === u)) throw new Error("username_taken");
        const t = { id: rid("t"), role: "teacher", display_name: name, username: u, password }; db.teachers.push(t); save(); return t;
      },
      async setTeacherPassword(id, password) { if (String(password).length < 8) throw new Error("weak_password"); const t = db.teachers.find((x) => x.id === id); if (t) { t.password = password; save(); } },
      async deleteTeacher(id) { const ids = db.courses.filter((c) => c.teacher_id === id).map((c) => c.id); if (db.students.some((s) => ids.includes(s.course_id))) throw new Error("has_students"); db.teachers = db.teachers.filter((t) => t.id !== id); db.courses = db.courses.filter((c) => c.teacher_id !== id); save(); },
      resetDemo() { try { localStorage.removeItem(KEY); sessionStorage.removeItem("fq3-demo-me"); } catch {} location.reload(); },
    };
  }

  /* ---------------- Supabase ---------------- */
  function supaStore() {
    const sb = G.supabase.createClient(CFG.SUPABASE_URL, CFG.SUPABASE_ANON_KEY, { auth: { persistSession: true, storageKey: "fq3-auth" } });
    let me = null, courses = null;
    const must = ({ data, error }) => { if (error) throw error; return data; };
    async function loadProfile() {
      const { data: u } = await sb.auth.getUser(); if (!u?.user) { me = null; return null; }
      const { data } = await sb.from("profiles").select("id, role, display_name, grup, username, course_id, adaptacions, adapt_idioma").eq("id", u.user.id).maybeSingle();
      me = data || null; courses = null; return me;
    }
    async function fn(name, body) {
      const { data, error } = await sb.functions.invoke(name, { body });
      if (error) { let msg = error.message; try { msg = (await error.context.json()).error || msg; } catch {} throw new Error(msg); }
      return data;
    }
    async function myCourses() {
      if (courses) return courses;
      let q = sb.from("courses").select("id, name, level, teacher_id, settings, created_at").order("level").order("name");
      if (me && me.role !== "admin") q = q.eq("teacher_id", me.id);
      courses = must(await q); return courses;
    }
    return {
      mode: "supabase", client: sb,
      async init() { const p = await loadProfile(); if (isStaff(p)) await myCourses(); return p; },
      async signInStudent(code) {
        const c = normCode(code);
        const { error } = await sb.auth.signInWithPassword({ email: `${c.toLowerCase()}@${EMAIL_DOMAIN}`, password: c });
        if (error) throw new Error("bad_code");
        const p = await loadProfile(); if (!p) throw new Error("no_profile"); return p;
      },
      async signInTeacher(user, password) {
        const u = String(user || "").trim().toLowerCase();
        const email = u.includes("@") ? u : `${u}@professorat.llibrefq3.app`;
        const { error } = await sb.auth.signInWithPassword({ email, password }); if (error) throw new Error("bad_login");
        const p = await loadProfile(); if (!isStaff(p)) { await sb.auth.signOut(); throw new Error("not_teacher"); }
        await myCourses(); return p;
      },
      async signOut() { await sb.auth.signOut(); me = null; courses = null; },
      me: () => me,
      // cursos
      curCourse() { const c = getCur(); return (courses || []).some((x) => x.id === c) ? c : null; },
      setCourse: setCur,
      async listCourses() {
        const cs = await myCourses();
        if (me.role !== "admin") return cs.map((c) => ({ ...c, teacher_name: me.display_name }));
        const ids = [...new Set(cs.map((c) => c.teacher_id))];
        const ts = ids.length ? must(await sb.from("profiles").select("id, display_name").in("id", ids)) : [];
        return cs.map((c) => ({ ...c, teacher_name: (ts.find((t) => t.id === c.teacher_id) || {}).display_name || "" }));
      },
      async createCourse(name, level) {
        if (!LEVELS.includes(level)) throw new Error("bad_level");
        const c = must(await sb.from("courses").insert({ name: String(name).trim().slice(0, 60), level, teacher_id: me.id, settings: { auto_calc: true } }).select().single());
        courses = null; return c;
      },
      async renameCourse(id, name) {
        const n = String(name).trim().slice(0, 60);
        must(await sb.from("courses").update({ name: n }).eq("id", id));
        must(await sb.from("profiles").update({ grup: n.slice(0, 20) }).eq("course_id", id));
        courses = null;
      },
      async deleteCourse(id) {
        const { count } = await sb.from("profiles").select("id", { count: "exact", head: true }).eq("course_id", id);
        if (count) throw new Error("has_students");
        must(await sb.from("courses").delete().eq("id", id)); courses = null;
      },
      async myLevel() { if (!me || !me.course_id) return null; const r = must(await sb.from("courses").select("level").eq("id", me.course_id).maybeSingle()); return r ? r.level : null; },
      async getSettings() {
        const glob = Object.fromEntries(must(await sb.from("settings").select("key, value")).map((r) => [r.key, r.value]));
        let cs = {};
        if (me && me.role === "student" && me.course_id) { const r = must(await sb.from("courses").select("settings").eq("id", me.course_id).maybeSingle()); cs = (r && r.settings) || {}; }
        else if (isStaff(me)) { const c = (await myCourses()).find((x) => x.id === this.curCourse()); cs = (c && c.settings) || {}; }
        return { ...glob, ...cs };
      },
      async setSetting(key, value) {
        const id = this.curCourse(); if (!id) throw new Error("no_course");
        const r = must(await sb.from("courses").select("settings").eq("id", id).single());
        const settings = { ...(r.settings || {}), [key]: value };
        must(await sb.from("courses").update({ settings }).eq("id", id));
        const c = (courses || []).find((x) => x.id === id); if (c) c.settings = settings;
      },
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
      // professorat (les regles de la base de dades ja limiten a l'alumnat dels cursos del docent)
      async listStudents(cid = this.curCourse()) {
        let q = sb.from("profiles").select("id, display_name, grup, code, role, course_id, adaptacions, adapt_idioma").eq("role", "student");
        if (cid) q = q.eq("course_id", cid); else { const ids = (await myCourses()).map((c) => c.id); if (!ids.length) return []; q = q.in("course_id", ids); }
        return must(await q.order("display_name"));
      },
      async createStudents(names, cid = this.curCourse()) { return (await fn("alumnes", { names, course_id: cid })).students.map((s) => ({ id: s.id, display_name: s.name, code: s.code, course_id: cid })); },
      async resetCode(id) { return (await fn("alumnes", { action: "reset", id })).code; },
      async deleteStudent(id) { await fn("alumnes", { action: "delete", id }); },
      async setAdaptacions(id, list, idioma) { const a = (list || []).filter((x) => ADAPT.includes(x)); must(await sb.from("profiles").update({ adaptacions: a, adapt_idioma: a.includes("nouvingut") ? (idioma || null) : null }).eq("id", id)); },
      async myAdapt() { if (!me) return { perfils: [], idioma: null }; const r = must(await sb.from("profiles").select("adaptacions, adapt_idioma").eq("id", me.id).maybeSingle()); return { perfils: (r && r.adaptacions) || [], idioma: (r && r.adapt_idioma) || null }; },
      async getPrefs() { if (!me) return { mode: "digital", ajudes_off: [] }; const r = must(await sb.from("preferencies").select("mode_fitxes, ajudes_off").eq("student_id", me.id).maybeSingle()); return { mode: (r && r.mode_fitxes) || "digital", ajudes_off: (r && r.ajudes_off) || [] }; },
      async setPrefs(p) { const cur = await this.getPrefs(); const row = { student_id: me.id, mode_fitxes: (p.mode || cur.mode) === "paper" ? "paper" : "digital", ajudes_off: (p.ajudes_off || cur.ajudes_off).filter((x) => AJUDES.includes(x)), updated_at: new Date().toISOString() }; must(await sb.from("preferencies").upsert(row)); },
      async myAdaptacions() { if (!me) return []; const r = must(await sb.from("profiles").select("adaptacions").eq("id", me.id).maybeSingle()); return (r && r.adaptacions) || []; },
      async getMode() { if (!me) return "digital"; const r = must(await sb.from("preferencies").select("mode_fitxes").eq("student_id", me.id).maybeSingle()); return (r && r.mode_fitxes) || "digital"; },
      async setMode(m) { must(await sb.from("preferencies").upsert({ student_id: me.id, mode_fitxes: m === "paper" ? "paper" : "digital", updated_at: new Date().toISOString() })); },
      async listSubmissions() { return must(await sb.from("submissions").select("*")); },
      async listResponseKeys() { return must(await sb.from("responses").select("student_id, worksheet_id")); },
      async feedbackFor(sid, ws) { return must(await sb.from("feedback").select("*").eq("student_id", sid).eq("worksheet_id", ws)); },
      async saveFeedback(sid, ws, rows) { must(await sb.from("feedback").upsert(rows.map((r) => ({ student_id: sid, worksheet_id: ws, ...r, updated_at: new Date().toISOString() })))); },
      async release(sid, ws) {
        must(await sb.from("feedback").update({ released: true }).eq("student_id", sid).eq("worksheet_id", ws));
        must(await sb.from("submissions").upsert({ student_id: sid, worksheet_id: ws, status: "returned", returned_at: new Date().toISOString(), review: "done" }));
      },
      async reopen(sid, ws) { must(await sb.from("submissions").update({ status: "draft", review: null, review_items: [] }).eq("student_id", sid).eq("worksheet_id", ws)); try { await sb.from("feedback").delete().eq("student_id", sid).eq("worksheet_id", ws).like("item_id", "auto:%"); } catch {} },
      async markReviewed(sid, ws) { must(await sb.from("submissions").update({ review: "done" }).eq("student_id", sid).eq("worksheet_id", ws)); },
      async proposeAI(sid, ws, items) { return fn("corregeix", { student_id: sid, worksheet_id: ws, items }); },
      async autoCorrect(ws, title, sda, items, sid) { return (await fn("autocorregeix", { worksheet_id: ws, title, sda, items, ...(sid ? { student_id: sid } : {}) })).rows || null; },
      async deleteAuto(sid, ws) { must(await sb.from("feedback").delete().eq("student_id", sid).eq("worksheet_id", ws).like("item_id", "auto:%")); },
      async allFeedback() { return must(await sb.from("feedback").select("student_id, worksheet_id, item_id, level, proposal_level, released")); },
      async errorsAll() { const rows = must(await sb.from("kv").select("path, data").like("path", "errors/%")); return rows.map((r) => ({ student_id: r.path.split("/")[1], worksheet_id: r.path.split("/")[2], ...r.data })); },
      async getInforme(sid) { const r = must(await sb.from("kv").select("data").eq("path", "informe/" + sid).maybeSingle()); return r ? r.data : null; },
      async makeInforme(sid, data) { return (await fn("autocorregeix", { action: "informe", student_id: sid, data })).informe; },
      async usage() { const m = month(); const r = must(await sb.from("kv").select("data").eq("path", "usage/" + m).maybeSingle()); return { month: m, calls: 0, usd: 0, ...((r && r.data) || {}) }; },
      // docents (només administrador)
      async listTeachers() {
        const ts = must(await sb.from("profiles").select("id, role, display_name, username, created_at").in("role", ["teacher", "admin"]).order("display_name"));
        const cs = must(await sb.from("courses").select("id, name, level, teacher_id"));
        const st = must(await sb.from("profiles").select("course_id").eq("role", "student"));
        return ts.map((t) => ({ ...t, courses: cs.filter((c) => c.teacher_id === t.id).map((c) => ({ ...c, n: st.filter((s) => s.course_id === c.id).length })) }));
      },
      async createTeacher({ username, name, password }) { return fn("docents", { username, name, password }); },
      async setTeacherPassword(id, password) { return fn("docents", { action: "password", id, password }); },
      async deleteTeacher(id) { return fn("docents", { action: "delete", id }); },
    };
  }

  /* Cada llibre desa les fitxes amb un prefix propi (2n → «2n:d1f1»), perquè no es barregin amb les de 3r
     (sense prefix). Les pàgines de 2n posen window.FQ_WSPREFIX = "2n:" abans de carregar aquest fitxer. */
  function prefixed(st, P) {
    const W = (ws) => P + ws;
    const mine = (id) => P ? String(id).startsWith(P) : !String(id).includes(":");
    const un = (rows) => (rows || []).filter((r) => mine(r.worksheet_id)).map((r) => ({ ...r, worksheet_id: String(r.worksheet_id).slice(P.length) }));
    const o = Object.create(st);
    ["loadResponses", "saveResponse", "getSubmission", "submit", "addPhoto", "removePhoto", "myFeedback", "autoCorrect"].forEach((m) => {
      o[m] = (ws, ...a) => st[m].call(o, W(ws), ...a);
    });
    ["feedbackFor", "saveFeedback", "release", "reopen", "markReviewed", "deleteAuto", "proposeAI"].forEach((m) => {
      o[m] = (sid, ws, ...a) => st[m].call(o, sid, W(ws), ...a);
    });
    ["listSubmissions", "listResponseKeys", "allFeedback", "errorsAll"].forEach((m) => {
      o[m] = async (...a) => un(await st[m].call(o, ...a));
    });
    // getSubmission i addPhoto es criden entre ells amb l'identificador ja prefixat
    o.getSubmission = (ws, ...a) => st.getSubmission.call(st, String(ws).startsWith(P) && P ? ws : W(ws), ...a);
    return o;
  }
  const base = (CFG.SUPABASE_URL && CFG.SUPABASE_ANON_KEY && G.supabase) ? supaStore() : demoStore();
  G.FQStore = prefixed(base, G.FQ_WSPREFIX || "");
  G.FQStore.normCode = normCode;
  G.FQStore.isStaff = isStaff;
  G.FQStore.LEVELS = LEVELS;
  G.FQStore.ADAPT = ADAPT;
  G.FQStore.AJUDES = AJUDES;
})(window);
