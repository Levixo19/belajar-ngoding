/* Ukuran lensa dan saringan layar Langit di peramban: tombol utama panel pada
 * tinggi pakai laptop, saringan konsep dan profesi (nomor, cincin fokus, nama
 * tidak boleh pudar; hasilnya harus ada di nama aksesibel), opsi terkunci,
 * ukuran huruf aplikasi, dan pembeda baru lawan terkunci.
 *
 * "Tinggi pakai" BUKAN tinggi layar: layar 1080 memberi viewport 904 (hilang
 * 176 px untuk bilah peramban dan tugas), jadi layar 768 memberi sekitar 592
 * dan 720 sekitar 544. Dasar ukurnya 544, 592, dan 650.
 *
 *     BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/ukur-lensa.mjs
 */
import { aktif, lum, mulai, pemeriksa, rasio } from "./lib.mjs";

const P = pemeriksa("ukur lensa dan saringan");
const rgb = (c) => (c.match(/[\d.]+/g) || []).slice(0, 3).map(Number);
const campur = (fg, bg, a) => fg.map((v, i) => Math.round(v * a + bg[i] * (1 - a)));

/* ---- tombol utama panel tampak penuh pada tinggi pakai laptop */
for (const h of [904, 768, 650, 592, 544]) {
  const s = await mulai({ lebar: 1366, tinggi: h, hash: "#/langit/html/0", tunggu: ".lt-lensa" });
  const r = await s.page.evaluate(() => {
    const a = document.querySelector(".lt-panel a.tbl-utama")?.getBoundingClientRect();
    const p = document.querySelector(".lt-panel-isi").getBoundingClientRect();
    const rel = document.getElementById("rel")?.getBoundingClientRect().bottom ?? 0;
    return a ? { atas: Math.round(a.top), bawah: Math.round(a.bottom), batas: Math.round(Math.min(p.bottom, innerHeight)), rel: Math.round(rel) } : null;
  });
  P.cek(`tinggi ${h}: "Mulai membaca" tampak penuh (di dalam panel dan layar)`, !!r && r.bawah <= r.batas && r.atas >= r.rel, r);
  await s.tutup();
}

/* ---- kontrol di panel dan kepala lensa: sasaran >= 24 px (WCAG 2.5.8) */
{
  const s = await mulai({ lebar: 1366, tinggi: 768, hash: "#/langit/python/5", tunggu: ".lt-lensa g[role=option]" });
  await s.page.waitForTimeout(500);
  const kecil = await s.page.evaluate(() => [...document.querySelectorAll(".lt-panel a, .lt-panel button, .lt-lensa-kepala a, .lt-lensa-kepala button")]
    .map((e) => { const r = e.getBoundingClientRect(); return { n: (e.textContent || e.getAttribute("aria-label") || "").trim().slice(0, 20), w: Math.round(r.width), h: Math.round(r.height) }; })
    .filter((x) => x.w > 0 && (x.h < 24 || x.w < 24)));
  P.cek("semua tautan dan tombol panel dan kepala lensa >= 24 x 24 px", kecil.length === 0, kecil);
  await s.tutup();
}

/* ---- saringan konsep: tidak ada peredupan, cincin fokus dan nomor utuh */
for (const tema of ["terang", "gelap", "malam", "kontras"]) {
  const s = await mulai({ tema, hash: "#/langit", tunggu: ".lt-ikhtisar" });
  await s.page.getByRole("button", { name: "Percabangan" }).click(); await s.page.waitForTimeout(200);
  const label0 = await s.page.$$eval("a.lt-nama", (a) => a.map((x) => x.getAttribute("aria-label")));
  const dgn = await s.page.evaluate(() => ({
    cincin: document.querySelectorAll(".lt-ik-cocok").length,
    redup: document.querySelectorAll(".lt-redup, .lt-gl-redup").length,
  }));
  P.cek(`${tema} peta + konsep: cincin ada, kelas redup tidak ada`, dgn.cincin > 0 && dgn.redup === 0, dgn);
  await s.page.evaluate(() => { location.hash = "#/langit/html"; });
  await s.page.waitForSelector(".lt-lensa g[role=option]"); await s.page.waitForTimeout(400);
  // Fokus papan ketik (:focus-visible): lensa yang dibuka sesudah klik mouse memberi
  // fokus lewat program, yang BUKAN focus-visible; satu panah menegakkannya.
  for (let i = 0; i < 30 && !(await aktif(s.page)).includes("option"); i++) await s.page.keyboard.press("Tab");
  await s.page.keyboard.press("ArrowRight"); await s.page.waitForTimeout(80);
  const o = await s.page.evaluate(() => {
    const eff = (el) => { let v = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement ?? e.parentNode) v *= Number(getComputedStyle(e).opacity); return v; };
    const g = document.activeElement;
    const nomor = [...document.querySelectorAll(".lt-ln-nomor")];
    // Latar nomor = kanvas (di tema terang ia pelat gelap), bukan wadah lensa.
    return {
      fokusOpsi: g?.getAttribute?.("role") === "option",
      opNomorMin: Math.min(...nomor.map(eff)), opFokus: eff(g?.querySelector(".lt-fokus")),
      fill: getComputedStyle(nomor[0]).fill, bg: getComputedStyle(document.querySelector(".lt-lensa-kanvas")).backgroundColor,
      terkunciAria: [...document.querySelectorAll("g[role=option]")].filter((x) => x.getAttribute("aria-disabled") === "true").length,
      sebutTerkunci: [...document.querySelectorAll("g[role=option]")].filter((x) => /masih terkunci/.test(x.getAttribute("aria-label"))).length,
    };
  });
  P.cek(`${tema} lensa + konsep: nomor dan cincin fokus tidak diredupkan`, o.fokusOpsi && o.opNomorMin === 1 && o.opFokus === 1, o);
  const k = rasio(rgb(o.fill), rgb(o.bg));
  P.cek(`${tema} nomor bintang >= 4,5:1`, k >= 4.5, k.toFixed(2));
  if (tema === "terang") P.cek("opsi terkunci TIDAK aria-disabled (tetap bisa dipilih), namanya menyebut 'masih terkunci'", o.terkunciAria === 0 && o.sebutTerkunci > 0, { aria: o.terkunciAria, nama: o.sebutTerkunci });
  await s.tutup();
}

/* ---- hasil saringan harus ada di NAMA AKSESIBEL (konsep dan profesi) */
{
  const s = await mulai({ hash: "#/langit", tunggu: ".lt-ikhtisar" });
  const ambilNama = () => s.page.$$eval("a.lt-nama", (a) => a.map((x) => x.getAttribute("aria-label")));
  const polos = await ambilNama();
  await s.page.getByRole("button", { name: "Percabangan" }).click(); await s.page.waitForTimeout(200);
  const k = await ambilNama();
  const berubah = k.filter((x, i) => x !== polos[i]).length;
  const cincinPerRasi = await s.page.$$eval(".lt-ik-svg .lt-ik-cocok", (c) => new Set(c.map((x) => x.parentElement)).size);
  P.cek("konsep: nama tautan berubah tepat pada rasi yang bercincin", berubah === cincinPerRasi && berubah >= 10, { berubah, cincinPerRasi });
  P.cek("konsep: nama tautan memuat teks yang terlihat (\"Python 0/44\")", polos.every((n) => /^\S.* \d+\/\d+: /.test(n)), polos[0]);
  await s.page.getByRole("button", { name: "Percabangan" }).click();
  // Pilihan buatan sendiri, bukan <select>: buka daftarnya lalu klik opsinya.
  await s.page.locator(".langit-pilih").click();
  await s.page.locator(".pil-daftar li", { hasText: "Frontend Developer" }).first().click(); await s.page.waitForTimeout(250);
  const p = await ambilNama();
  const bekal = await s.page.$$eval("a.lt-nama[data-bekal]", (a) => a.map((x) => x.dataset.key));
  const bekalNama = p.filter((n) => /, bagian bekal Frontend Developer\./.test(n)).length;
  const opNama = await s.page.$$eval("a.lt-nama", (a) => Math.min(...a.map((x) => Number(getComputedStyle(x).opacity))));
  P.cek("profesi: nama berubah tepat pada rasi bekal, tidak ada nama yang diredupkan", bekal.length >= 2 && bekalNama === bekal.length && opNama === 1, { bekal, bekalNama, opNama });
  const garis = await s.page.$$eval("a.lt-nama[data-bekal] .lt-nama-teks", (a) => a.map((x) => getComputedStyle(x).textDecorationLine));
  P.cek("profesi: penanda bekal juga bentuk (garis bawah), bukan hanya nama aksesibel", garis.length > 0 && garis.every((g) => g.includes("underline")), garis);
  await s.tutup();
}

/* ---- ukuran huruf aplikasi ("sangat besar" = 20 px): teks peta dan lensa ikut membesar */
{
  const s = await mulai({ lebar: 1905, tinggi: 904, ukuranTeks: "sangat besar", hash: "#/langit", tunggu: ".lt-ikhtisar" });
  const f = await s.page.evaluate(() => {
    const px = (q) => { const e = document.querySelector(q); return e ? +parseFloat(getComputedStyle(e).fontSize).toFixed(2) : null; };
    return { html: px("html"), nama: px(".lt-nama-teks"), hitungan: px(".lt-nama-prog b"), judulKeluarga: px(".lt-keluarga h2"), ketKeluarga: px(".lt-keluarga p"), mulai: px(".lt-mulai") };
  });
  P.cek("peta @20 px: tidak ada teks di bawah 15 px", Object.values(f).every((v) => v === null || v >= 15), f);
  const nab = await s.page.evaluate(() => {
    const kotak = [...document.querySelectorAll(".lt-nama, .lt-keluarga")].map((e) => e.getBoundingClientRect());
    let tabrak = 0;
    for (let i = 0; i < kotak.length; i++) for (let j = i + 1; j < kotak.length; j++) {
      const a = kotak[i], b = kotak[j];
      if (a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top) tabrak += 1;
    }
    return tabrak;
  });
  P.cek("peta @20 px: nol nama atau judul keluarga saling menimpa", nab === 0, nab);
  await s.page.evaluate(() => { location.hash = "#/langit/html/0"; });
  await s.page.waitForSelector(".lt-lensa g[role=option]"); await s.page.waitForTimeout(500);
  const l = await s.page.evaluate(() => {
    const px = (q) => { const e = document.querySelector(q); return e ? +parseFloat(getComputedStyle(e).fontSize).toFixed(2) : null; };
    return { nomor: px(".lt-ln-nomor"), pilBab: px(".lt-ln-bab text"), berikut: px(".lt-ln-berikut text"), pil: px(".lt-panel .pil"), judul: px(".lt-panel-kepala h3") };
  });
  P.cek("lensa @20 px: nomor, lencana, dan pil panel >= 15 px", l.nomor >= 15 && l.pilBab >= 15 && l.berikut >= 15 && l.pil >= 15, l);
  await s.tutup();
  // Di bawah 1.156 x 1,25 = 1.445 px akar, hurufnya terlalu besar untuk peta: Daftar.
  const d = await mulai({ lebar: 1500, tinggi: 800, ukuranTeks: "sangat besar", hash: "#/langit", tunggu: ".lt-ikhtisar, .lt-daftar" });
  const mode = await d.page.evaluate(() => ({ akar: document.querySelector(".lt-halaman").clientWidth, daftar: !!document.querySelector(".lt-daftar") }));
  P.cek("@20 px, akar di bawah 1.445: Daftar (bukan peta yang bertabrakan)", mode.akar < 1445 === mode.daftar, mode);
  await d.tutup();
}

/* ---- baru lawan terkunci terbedakan oleh terang-gelap (tidak hanya bentuk) */
{
  const s = await mulai({ hash: "#/langit", tunggu: ".lt-ikhtisar" });
  for (const tema of ["terang", "gelap", "malam", "kontras"]) {
    await s.page.evaluate((t) => { document.documentElement.dataset.tema = t; }, tema); await s.page.waitForTimeout(120);
    const w = await s.page.evaluate(() => {
      const baca = (v) => { const e = document.createElement("div"); e.style.color = `var(${v})`; document.body.appendChild(e); const c = getComputedStyle(e).color; e.remove(); return c; };
      const rgbOf = (c) => { const m = c.match(/color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)\)/); return m ? [m[1], m[2], m[3]].map((x) => Math.round(x * 255)) : c.match(/[\d.]+/g).slice(0, 3).map(Number); };
      return { baru: rgbOf(baca("--lg-baru")), kunci: rgbOf(baca("--lg-kunci")) };
    });
    const r = rasio(w.baru, w.kunci);
    P.cek(`${tema}: baru lawan terkunci selisih luminans >= 1,8`, r >= 1.8, r.toFixed(2));
  }
  await s.tutup();
}

/* ---- tautan lewati tidak menggeser halaman saat fokus */
{
  const s = await mulai({ hash: "#/langit", tunggu: ".lt-ikhtisar" });
  const y0 = await s.page.evaluate(() => document.querySelector(".lt-halaman h1").getBoundingClientRect().top);
  for (let i = 0; i < 20; i++) { await s.page.keyboard.press("Tab"); if ((await aktif(s.page)).includes("Lewati")) break; }
  const a = await s.page.evaluate(() => { const e = document.activeElement.getBoundingClientRect(); return { lebar: Math.round(e.width), h1: document.querySelector(".lt-halaman h1").getBoundingClientRect().top }; });
  P.cek("tautan lewati: halaman tidak bergeser dan tombolnya tidak selebar kolom", Math.abs(a.h1 - y0) < 0.5 && a.lebar < 400, { y0, ...a });
  await s.tutup();
}

P.selesai();
