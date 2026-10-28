/* Harness pengukuran MANUAL layar Langit (butuh peramban, jadi tidak ikut suite).
 *
 *   BELAJAR_URL=http://127.0.0.1:7788/  node uji/manual/alur-nyata.mjs
 *
 * ATURAN YANG MENGIKAT: jalankan dengan server berprofil TERPISAH, bukan profil
 * pelajar (lihat "Yang berlaku untuk tes berlaku juga untuk MENCOBA APLIKASINYA"
 * di AGENTS.md). Semua permintaan selain GET DIGAGALKAN di sini, jadi menekan
 * "Mulai membaca" tidak menulis progres apa pun walaupun profilnya salah.
 *
 * Playwright dan Chrome tidak jadi dependensi repo: jalur modulnya lewat
 * PLAYWRIGHT_MJS (bawaan: paket `playwright` yang bisa di-resolve dari sini),
 * Chrome lewat CHROME (bawaan /usr/bin/google-chrome).
 */

export const URL_DASAR = process.env.BELAJAR_URL ?? "http://127.0.0.1:7788/";

async function muatPlaywright() {
  const jalur = process.env.PLAYWRIGHT_MJS;
  const pw = jalur ? await import(jalur) : await import("playwright");
  return pw.chromium ?? pw.default.chromium;
}

/** Mulai satu sesi. `profil`: "nyata" (apa adanya dari server), "campur" (satu
 *  per tiga selesai, satu sebagian, tiga baru, sisanya terkunci: semua status
 *  muncul), atau "semua" (semua selesai); dua yang terakhir lewat intersepsi
 *  respons `/api/langit` di SISI KLIEN, server tidak menulis apa pun. */
export async function mulai(o = {}) {
  const { lebar = 1366, tinggi = 768, tema = "terang", gerak = "mati", hash = "#/langit", profil = "nyata",
    dpr = 1, reduce = false, forced = false, throttle = 1, bilahKlasik = false,
    tunggu = null, ukuranTeks = null, argsChrome = [] } = o;
  // Alamat lensa (#/langit/<kurikulum>[/n]): ikhtisar ada tetapi tersembunyi, jadi yang ditunggu lensanya.
  const sasaranTunggu = tunggu ?? (/^#\/langit\/[^/]+/.test(hash) ? ".lt-lensa g[role=option]" : ".lt-ikhtisar, .lt-daftar");
  const chromium = await muatPlaywright();
  const browser = await chromium.launch({
    executablePath: process.env.CHROME ?? "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox", ...argsChrome],
    ...(bilahKlasik ? { ignoreDefaultArgs: ["--hide-scrollbars"] } : {}),
  });
  const ctx = await browser.newContext({
    viewport: { width: lebar, height: tinggi }, deviceScaleFactor: dpr,
    reducedMotion: reduce ? "reduce" : "no-preference", forcedColors: forced ? "active" : "none",
  });
  const tulisDitolak = [];
  await ctx.route("**/*", async (r) => {
    const q = r.request();
    if (q.method() !== "GET") { tulisDitolak.push(q.method() + " " + q.url()); return r.abort(); }
    if (profil !== "nyata" && /\/api\/langit(\?|$)/.test(q.url())) {
      const resp = await r.fetch(); const j = await resp.json();
      for (const rasi of j.bahasa) {
        const n = rasi.materi.length, s = Math.floor(n / 3);
        rasi.materi.forEach((m, i) => {
          if (profil === "semua") { m.status = "selesai"; m.terkunci = false; return; }
          if (i < s) { m.status = "selesai"; m.terkunci = false; }
          else if (i === s) { m.status = "sebagian"; m.terkunci = false; }
          else if (i <= s + 3) { m.status = "baru"; m.terkunci = false; }
          else { m.status = "baru"; m.terkunci = true; }
        });
      }
      return r.fulfill({ response: resp, body: JSON.stringify(j), contentType: "application/json" });
    }
    return r.continue();
  });
  await ctx.addInitScript(([t, g, u]) => {
    try {
      localStorage.setItem("belajar.tema", JSON.stringify(t));
      localStorage.setItem("belajar.gerak", JSON.stringify(g));
      if (u) localStorage.setItem("belajar.ukuran", JSON.stringify(u));
    } catch { /* tanpa localStorage: tetap jalan */ }
  }, [tema, gerak, ukuranTeks]);
  const page = await ctx.newPage();
  page.setDefaultTimeout(5000);
  const konsol = [];
  page.on("console", (m) => { if (["error", "warning"].includes(m.type())) konsol.push(m.type() + ": " + m.text()); });
  page.on("pageerror", (e) => konsol.push("pageerror: " + e.message));
  await page.goto(URL_DASAR + hash, { waitUntil: "load" });
  await page.waitForSelector(sasaranTunggu, { timeout: 30000 });
  await page.evaluate(([t, g]) => { document.documentElement.dataset.tema = t; document.documentElement.dataset.gerak = g; }, [tema, gerak]);
  await page.waitForTimeout(700);
  if (throttle > 1) {
    const cdp = await ctx.newCDPSession(page);
    await cdp.send("Emulation.setCPUThrottlingRate", { rate: throttle });
  }
  return { browser, ctx, page, konsol, tulisDitolak, tutup: () => browser.close() };
}

/** Penampung hasil: satu baris per pemeriksaan, kode keluar 1 bila ada yang gagal. */
export function pemeriksa(judul) {
  let gagal = 0, jumlah = 0;
  console.log(`== ${judul}`);
  return {
    cek(nama, kondisi, rincian = "") {
      jumlah += 1;
      if (!kondisi) gagal += 1;
      console.log(`  ${kondisi ? "ok    " : "GAGAL "} ${nama}${rincian !== "" ? "  " + (typeof rincian === "string" ? rincian : JSON.stringify(rincian)) : ""}`);
    },
    selesai() {
      console.log(gagal ? `GAGAL: ${gagal} dari ${jumlah} pemeriksaan` : `LULUS: ${jumlah} pemeriksaan`);
      // Keluar eksplisit: bagian yang gagal di tengah jalan bisa meninggalkan
      // peramban terbuka, dan itu menahan proses Node hidup selamanya.
      process.exit(gagal ? 1 : 0);
    },
  };
}

/** Elemen yang sedang berfokus, diringkas. */
export const aktif = (p) => p.evaluate(() => {
  const a = document.activeElement;
  if (!a) return "null";
  return a.tagName + (a.getAttribute("role") ? `[${a.getAttribute("role")}]` : "") + " :: " +
    (a.getAttribute("aria-label") || a.textContent || "").trim().slice(0, 50);
});
export const fokusBody = (p) => p.evaluate(() => document.activeElement === document.body || document.activeElement === null);

// Kontras WCAG 2.x
export function lum([r, g, b]) {
  const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
}
export function rasio(a, b) {
  const la = lum(a), lb = lum(b);
  return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
}
