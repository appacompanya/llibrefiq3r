/* Zona del professorat a la web: substitueix les capacitats de claude.ai (db, user, downloads)
   per Supabase i el navegador, i serveix els PDF del professorat des d'un espai privat. */
(function (G) {
  "use strict";
  const S = G.FQStore;
  const sb = S.client; // null en mode demostració

  /* --- base de dades clau-valor (només professorat) amb la mateixa forma que la de claude.ai --- */
  const memKV = {};
  async function kvGet(path) {
    if (!sb) return memKV[path] ?? null;
    const { data } = await sb.from("kv").select("data").eq("path", path).maybeSingle(); return data ? data.data : null;
  }
  async function kvSet(path, data) {
    if (!sb) { memKV[path] = data; try { localStorage.setItem("fq3-kv", JSON.stringify(memKV)); } catch {} return; }
    const { error } = await sb.from("kv").upsert({ path, data, updated_at: new Date().toISOString() }); if (error) throw error;
  }
  async function kvDel(path) { if (!sb) { delete memKV[path]; return; } await sb.from("kv").delete().eq("path", path); }
  async function kvChildren(prefix) {
    if (!sb) return Object.keys(memKV).filter((k) => k.startsWith(prefix + "/") && !k.slice(prefix.length + 1).includes("/")).map((k) => ({ path: k, data: memKV[k] }));
    const { data } = await sb.from("kv").select("path, data").like("path", prefix + "/%"); return (data || []).filter((r) => !r.path.slice(prefix.length + 1).includes("/"));
  }
  try { Object.assign(memKV, JSON.parse(localStorage.getItem("fq3-kv")) || {}); } catch {}
  const doc = (path) => ({
    get: async () => { const d = await kvGet(path); return { exists: d != null, data: () => d }; },
    set: (obj) => kvSet(path, obj),
    delete: () => kvDel(path),
    collection: (name) => coll(path + "/" + name),
  });
  const coll = (path) => ({
    get: async () => ({ docs: (await kvChildren(path)).map((r) => ({ id: r.path.split("/").pop(), data: () => r.data })) }),
    doc: (id) => doc(path + "/" + id),
  });
  const dbNS = { doc };
  const downloads = { save: async ({ filename, data }) => {
    const blob = data instanceof Blob ? data : new Blob([data], { type: "text/plain;charset=utf-8" });
    const u = URL.createObjectURL(blob); const a = document.createElement("a"); a.href = u; a.download = filename; document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(u), 5000);
  } };
  G.claude = { use: async (name) => {
    if (name === "db") return dbNS;
    if (name === "user") { const me = S.me(); return me ? { id: async () => me.id } : null; }
    if (name === "downloads") return downloads;
    return null;
  } };

  /* --- adreça de cada PDF: alumnat -> ../docs; professorat -> espai privat (enllaç temporal) --- */
  const signed = {};
  G.fqDocUrl = async function (f) {
    const teacher = G.D && Object.values(G.D).some((d) => d.f === f && d.t);
    if (!teacher) return "../docs/" + f;
    if (!sb) return "../docs/" + f;
    if (signed[f] && signed[f].exp > Date.now()) return signed[f].url;
    const { data, error } = await sb.storage.from("professorat").createSignedUrl(f, 3600);
    if (error || !data) throw { code: "fetch" };
    signed[f] = { url: data.signedUrl, exp: Date.now() + 50 * 60 * 1000 }; return data.signedUrl;
  };
  G.fqTeacherFiles = () => G.D ? Object.values(G.D).filter((d) => d.t).map((d) => d.f) : [];
  G.fqListUploaded = async () => { if (!sb) return []; const { data } = await sb.storage.from("professorat").list("", { limit: 1000 }); return (data || []).map((x) => x.name); };
  G.fqUpload = async (file) => { const { error } = await sb.storage.from("professorat").upload(file.name, file, { upsert: true, contentType: "application/pdf" }); if (error) throw error; };
})(window);
