/* Perilaku UX belajar yang dijanjikan teksnya: lencana yang jujur, penjelasan
 * kapan materi selesai, hasil Periksa untuk galat kompilasi, arah saat program
 * pendukung hilang, pernyataan gratis, teks dialog Reset, dan pemuat yang
 * diumumkan. Semuanya cacat atau janji yang tidak terlihat oleh tsc dan tes
 * sumber; hanya melihat HALAMANNYA yang membuktikannya.
 *
 *   BELAJAR_URL_BARU=http://127.0.0.1:7911/ BELAJAR_URL_KEMBALI=http://127.0.0.1:7912/ \
 *   PLAYWRIGHT_MJS=... node uji/manual/belajar-ux.mjs
 *
 * Dua server berprofil TERPISAH: BARU (xp = 0, tanpa progres) dan KEMBALI
 * (xp > 0, streak putus, ada kuis jatuh tempo). Skrip ini MENULIS ke profil
 * uji, bukan hanya membaca: membuka materi atau latihan mencatat "sebagian",
 * XP kecil, dan streak, dan kode yang diketik di editor masuk ke workspace
 * profil uji. Karena itu kedua profil WAJIB disemai ulang sebelum tiap jalan;
 * profil yang sudah pernah dipakai membuat blok A memerah dengan alasan yang
 * tidak ada hubungannya dengan lencana (streak sudah 1, bukan 0). Menolak
 * port 7777. Keadaan yang tidak bisa dibuat nyata (program pendukung hilang,
 * pemuat lambat) DISIMULASIKAN lewat intersepsi respons dan ditandai "SIM".
 */
const BARU = process.env.BELAJAR_URL_BARU ?? "";
const KEMBALI = process.env.BELAJAR_URL_KEMBALI ?? "";
for (const [nama, u] of [["BELAJAR_URL_BARU", BARU], ["BELAJAR_URL_KEMBALI", KEMBALI]]) {
  let x = null; try { x = new URL(u); } catch { /* kosong */ }
  if (!x || x.hostname !== "127.0.0.1" || x.port === "7777" || x.port === "") {
    console.error(`MENOLAK: ${nama} harus http://127.0.0.1:<port uji>/, bukan 7777.`);
    process.exit(2);
  }
}
const pw = await import(process.env.PLAYWRIGHT_MJS ?? "playwright");
const chromium = pw.chromium ?? pw.default.chromium;
const browser = await chromium.launch({
  executablePath: process.env.CHROME ?? "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox"] });
let gagal = 0;
const periksa = (nama, ok, rinci = "") => {
  if (!ok) gagal += 1;
  console.log(`${ok ? "lulus " : "GAGAL "} ${nama}${rinci ? "  (" + String(rinci).slice(0, 160) + ")" : ""}`);
};
async function buka(base, hash, { simulasi = null, lebar = 1440, tinggi = 900 } = {}) {
  const ctx = await browser.newContext({ viewport: { width: lebar, height: tinggi } });
  await ctx.addInitScript(() => { try { localStorage.setItem("belajar.gerak", JSON.stringify("mati")); } catch { /* abaikan */ } });
  const page = await ctx.newPage();
  const galat = [];
  page.on("pageerror", (e) => galat.push(String(e).slice(0, 160)));
  page.on("console", (m) => { if (m.type() === "error") galat.push(m.text().slice(0, 160)); });
  if (simulasi) await simulasi(page);
  await page.goto(base + hash);
  await page.waitForTimeout(1500);
  return { page, ctx, galat };
}
const teks = (page, sel) => page.locator(sel).first().innerText();
const judulLencana = (page) => page.evaluate(() => [...document.querySelectorAll("a.tanda")].map((a) => a.getAttribute("title")));

// A. lencana: tiga keadaan, tanpa kata "terputus"
{
  const { page, ctx } = await buka(BARU, "#/");
  const j = await judulLencana(page);
  periksa("A lencana (xp 0): tanpa kata 'terputus'", j.every((t) => !/terputus/i.test(t)), j.join(" | "));
  periksa("A lencana (xp 0): menjelaskan hitungan streak", /Belum ada hari berurutan/.test(j[0]), j[0]);
  periksa("A lencana XP: menyebut gelar dari total XP dan target bisa diubah", /dari total XP/.test(j[1]) && /Pengaturan/.test(j[1]), j[1]);
  await ctx.close();
  const k = await buka(KEMBALI, "#/");
  const jk = await judulLencana(k.page);
  periksa("A lencana (streak putus, ada rekor): menyebut rekor dan langkah kecil",
    /Belum ada hari berurutan sekarang · rekor \d+ hari/.test(jk[0]) && !/terputus/i.test(jk[0]), jk[0]);
  await k.ctx.close();
}

// B. materi: kapan selesai, tanpa kata "tuntas", tombol berikutnya jujur
{
  const { page, ctx } = await buka(BARU, "#/materi/python/1");
  const sisi = await page.locator(".baris-sisi", { hasText: "Selesai tercatat" }).count();
  periksa("B materi: kalimat aturan selesai tampil", sisi === 1);
  const pil = await page.evaluate(() => [...document.querySelectorAll(".materi-meta .pil")].map((e) => e.textContent.trim()));
  periksa("B materi: pil status tanpa kata 'tuntas'", pil.some((t) => /selesai dibaca/.test(t)) && pil.every((t) => !/tuntas/.test(t)), pil.join(" | "));
  const tombol = await page.locator(".materi-kaki button.tbl-utama").first().getAttribute("title");
  periksa("B materi: tombol berikutnya menyebut bahwa ia menandai selesai", /Menandai materi ini selesai/.test(tombol ?? ""), tombol);
  await ctx.close();
}

// C. latihan: galat sintaks vs belum sesuai
{
  const { page, ctx } = await buka(BARU, "#/latihan/python/0");
  const periksaKode = async (kode) => {
    await page.locator("textarea").first().fill(kode);
    await page.locator("button", { hasText: "Periksa jawaban" }).first().click();
    await page.waitForTimeout(3500);
    return page.locator(".kerja-hasil").first().innerText();
  };
  const galat = await periksaKode('print("halo');
  periksa("C galat sintaks: tidak menyuruh 'lihat bedanya' ke diff yang tidak ada", !/Lihat bedanya di bawah/.test(galat) && !/Baris hijau bertanda/.test(galat), galat.split("\n")[0]);
  periksa("C galat sintaks: menyebut programnya berhenti dengan error dan langkah berikutnya", /berhenti dengan error/.test(galat) && /Perbaiki errornya dulu/.test(galat));
  periksa("C galat sintaks: 'Artinya' tetap ada", /Artinya/.test(galat));
  const beda = await periksaKode('print("halo")');
  periksa("C belum sesuai (ada diff): judul dan legenda diff tetap tampil", /Lihat bedanya di bawah/.test(beda) && /Baris hijau bertanda/.test(beda));
  await ctx.close();
}

// D. SIM: program pendukung hilang
{
  const simulasi = async (page) => {
    await page.route("**/api/latihan?**", async (r) => { const re = await r.fetch(); const j = await re.json();
      j.dinilai = false; j.bisa_jalan = false; j.alasan = "Toolchain belum terpasang: gcc"; await r.fulfill({ response: re, json: j }); });
    await page.route("**/api/bahasa?**", async (r) => { const re = await r.fetch(); const j = await re.json();
      if (j.key === "c") { j.siap = false; j.hilang = ["gcc"]; j.pasang = "sudo dnf install gcc"; } await r.fulfill({ response: re, json: j }); });
  };
  const { page, ctx } = await buka(BARU, "#/latihan/c/0", { simulasi });
  const kartu = await page.locator(".keadaan").first().innerText();
  periksa("D SIM latihan: kartu memberi arah dan menyebut gratis", /belum terpasang/.test(kartu) && /gratis/.test(kartu) && /halaman C/.test(kartu), kartu.replace(/\n/g, " "));
  const datar = kartu.replace(/\s+/g, " ");
  periksa("D SIM latihan: alasan dari mesin berakhir titik, tanpa jargon 'Toolchain', dan tanpa mengulang 'belum terpasang'",
    /Program pendukung belum terpasang: gcc\. Jadi kodenya belum bisa dijalankan/.test(datar) && !/Toolchain/.test(datar)
      && (datar.match(/belum terpasang/g) ?? []).length === 1, datar);
  const tautan = await page.locator('.keadaan a[href="#/bahasa/c"]').count();
  periksa("D SIM latihan: ada tautan ke halaman bahasa", tautan === 1);
  const pil = await page.locator('a.pil[href="#/bahasa/c"]', { hasText: "Belum bisa dijalankan" }).count();
  periksa("D SIM latihan: tombol Jalankan yang hilang diganti penanda beralasan", pil === 1);
  await ctx.close();
  const b = await buka(BARU, "#/bahasa/c", { simulasi });
  const k2 = await b.page.locator(".keadaan").first();
  const kelas = await k2.getAttribute("class");
  periksa("D SIM bahasa: bukan gaya galat untuk keadaan yang normal", /keadaan-kosong/.test(kelas) && !/keadaan-salah/.test(kelas), kelas);
  const t2 = await k2.innerText();
  periksa("D SIM bahasa: 'Semuanya gratis' dan tombol Jalankan disebut", /Semuanya gratis/.test(t2) && /tombol Jalankan/.test(t2), t2.replace(/\n/g, " "));
  await b.ctx.close();
}

// E. Statistik: pernyataan gratis tanpa kata toolchain
{
  const { page, ctx } = await buka(KEMBALI, "#/statistik");
  const isi = await page.locator("main, #layar").first().innerText();
  periksa("E Statistik: 'opsional dan gratis' dan tanpa kata 'toolchain'", /opsional dan gratis/.test(isi) && !/toolchain/i.test(isi));
  await ctx.close();
}

// F. dialog Reset: dampak persis
{
  const { page, ctx } = await buka(BARU, "#/atur");
  await page.locator("button", { hasText: "Reset satu bahasa" }).click();
  await page.waitForSelector(".jendela");
  const d1 = await page.locator(".jendela").first().innerText();
  periksa("F reset satu bahasa: menyebut XP, level, streak, badge tetap ada", /XP, level, streak, dan badge-mu tetap ada/.test(d1), d1.replace(/\n/g, " "));
  periksa("F reset satu bahasa: menyebut salinan dan cara memulihkan", /Pulihkan dari salinan/.test(d1) && !/tidak bisa dibatalkan/i.test(d1));
  await page.keyboard.press("Escape"); await page.waitForTimeout(300);
  await page.locator("button", { hasText: "Reset SEMUA progres" }).click();
  await page.waitForSelector(".jendela");
  const d2 = await page.locator(".jendela").first().innerText();
  periksa("F reset semua: menyebut salinan, pemulihan, dan catatan tidak terhapus", /Pulihkan dari salinan/.test(d2) && /Catatan pribadimu tidak ikut terhapus/.test(d2), d2.replace(/\n/g, " "));
  await ctx.close();
}

// G. pemuat diumumkan (SIM: respons dilambatkan supaya pemuatnya sempat terlihat)
{
  const simulasi = async (page) => {
    await page.route("**/api/materi?**", async (r) => { await new Promise((s) => setTimeout(s, 2500)); await r.continue(); });
  };
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await simulasi(page);
  await page.goto(BARU + "#/materi/python/1");
  await page.waitForSelector(".pusaran", { timeout: 8000 });
  const r = await page.evaluate(() => [...document.querySelectorAll(".pusaran")].map((e) => ({
    sendiri: e.getAttribute("role") === "status",
    dekorasi: e.getAttribute("aria-hidden") === "true" && e.parentElement?.getAttribute("role") === "status" })));
  periksa("G SIM pemuat: tiap pusaran diumumkan (role status) atau dekorasi di dalam role status", r.length > 0 && r.every((x) => x.sendiri || x.dekorasi), JSON.stringify(r));
  await ctx.close();
}

// H. aksesibilitas papan ketik dan pembaca layar: judul tab, fokus saat
// berpindah layar, Lompat ke isi, petunjuk editor, umpan balik kuis, label
// isian, dan Esc di menu Lainnya. Diukur lewat DOM; tidak menggantikan uji
// dengan pembaca layar sungguhan.
{
  const { page, ctx } = await buka(BARU, "#/atur");
  const h1 = (await page.locator("h1").first().innerText()).replace(/\s+/g, " ").trim();
  const judul = await page.title();
  periksa("H judul tab mengikuti h1 layar", judul === `${h1} · belajar-codingV2`, `${judul} | ${h1}`);
  await page.keyboard.press("Tab");
  const pertama = await page.evaluate(() => ({ kelas: document.activeElement?.className ?? "", teks: document.activeElement?.textContent ?? "" }));
  periksa("H Lompat ke isi: butir fokus pertama dokumen", /lompat/.test(pertama.kelas) && /Lompat ke isi/.test(pertama.teks), JSON.stringify(pertama));
  await page.keyboard.press("Enter");
  const sesudah = await page.evaluate(() => document.activeElement?.id ?? "");
  periksa("H Lompat ke isi: fokus mendarat di #layar", sesudah === "layar", sesudah);
  const tanpaNama = await page.evaluate(() => [...document.querySelectorAll("#layar input")].filter((i) =>
    i.type !== "hidden" && !(i.labels && i.labels.length) && !i.getAttribute("aria-label") && !i.getAttribute("aria-labelledby")).map((i) => i.id || i.name || i.type));
  periksa("H Pengaturan: tiap isian punya nama (label atau aria-label)", tanpaNama.length === 0, tanpaNama.join(","));
  await page.evaluate(() => { location.hash = "#/statistik"; });
  await page.waitForTimeout(1500);
  const pindah = await page.evaluate(() => ({ tag: document.activeElement?.tagName, judul: document.title, h1: document.querySelector("#layar h1")?.textContent?.trim() }));
  periksa("H berpindah layar: fokus ke h1 baru dan judul tab ikut", pindah.tag === "H1" && pindah.judul.startsWith(pindah.h1 ?? "\u0000"), JSON.stringify(pindah));
  await page.locator(".rel-pemicu").click();
  const buka1 = await page.locator(".rel-pemicu").getAttribute("aria-expanded");
  await page.keyboard.press("Escape");
  await page.waitForTimeout(300);
  const esc = await page.evaluate(() => ({ kelas: document.activeElement?.className ?? "", buka: document.querySelector(".rel-pemicu")?.getAttribute("aria-expanded") }));
  periksa("H menu Lainnya: Esc menutup dan fokus kembali ke pemicunya", buka1 === "true" && esc.buka === "false" && /rel-pemicu/.test(esc.kelas), JSON.stringify(esc));
  await ctx.close();
}
{
  const { page, ctx } = await buka(BARU, "#/latihan/python/0");
  const ref = await page.evaluate(() => {
    const t = document.querySelector("textarea");
    const id = t?.getAttribute("aria-describedby");
    return { id, teks: id ? document.getElementById(id)?.textContent ?? "" : "" };
  });
  periksa("H editor: petunjuk keluar-dengan-papan-ketik dibacakan lewat aria-describedby", !!ref.id && /Esc/.test(ref.teks), JSON.stringify(ref));
  await ctx.close();
}
{
  const { page, ctx } = await buka(BARU, "#/kuis/python/0");
  await page.locator("button", { hasText: "Mulai kuis" }).first().click();
  await page.waitForSelector(".opsi button", { timeout: 8000 });
  await page.locator(".opsi button").first().click();
  await page.waitForSelector(".penjelasan", { timeout: 8000 });
  await page.waitForTimeout(400);
  const kuis = await page.evaluate(() => {
    const p = document.querySelector(".penjelasan");
    return {
      dalamStatus: !!p?.closest('[role="status"]'),
      terlihat: (p?.querySelector("b")?.textContent ?? "").trim(),
      umum: (document.querySelector(".pengumum")?.textContent ?? "").trim(),
    };
  });
  periksa("H kuis: hasil diumumkan SEKALI lewat pengumum global, bukan region kedua yang memuat tombol",
    !kuis.dalamStatus && /^(Benar\.|Belum tepat\. Jawaban yang benar: [A-D]\.)/.test(kuis.umum)
      && /^(Benar\.|Belum tepat\.)/.test(kuis.terlihat), JSON.stringify(kuis));
  await ctx.close();
}

// I. pintu masuk dan pindah antar-layar bertipe sama. Blok H hanya memuat
// `#/atur` (satu ruas) lalu pindah ke komponen lain; di situ pengaman "render
// pertama" tampak benar, padahal di lima dari tujuh pintu masuk fokus mendarat
// di <h1>, dan pindah materi 1 ke 2 meninggalkan judul tab dari materi 1.
{
  for (const hash of ["#/", "#/materi/python/1", "#/bahasa/python", "#/kuis/python/0", "#/latihan/python/0"]) {
    const { page, ctx } = await buka(BARU, hash);
    await page.waitForTimeout(1200);
    const aktif = await page.evaluate(() => document.activeElement === document.body);
    await page.keyboard.press("Tab");
    const tab = await page.evaluate(() => String(document.activeElement?.className ?? ""));
    periksa(`I muat langsung ${hash}: fokus di BODY dan Tab pertama ke "Lompat ke isi"`, aktif && /lompat/.test(tab), `body=${aktif} tab=${tab.slice(0, 30)}`);
    await ctx.close();
  }
  const m = await buka(BARU, "#/materi/python/1");
  await m.page.waitForTimeout(1000);
  await m.page.locator(".materi-kaki button.tbl-utama").first().click();
  await m.page.waitForTimeout(3000);
  const mm = await m.page.evaluate(() => ({ hash: location.hash, tag: document.activeElement?.tagName, judul: document.title, h1: document.querySelector("#layar h1")?.textContent?.trim() }));
  periksa("I materi 1 ke 2 (komponen sama, data baru): judul tab dan fokus mengikuti h1 baru",
    mm.hash.endsWith("/2") && mm.tag === "H1" && mm.judul === `${mm.h1} · belajar-codingV2`, JSON.stringify(mm));
  await m.ctx.close();
  const b = await buka(BARU, "#/bahasa/python");
  await b.page.waitForTimeout(1000);
  await b.page.evaluate(() => { location.hash = "#/bahasa/java"; });
  await b.page.waitForTimeout(2500);
  const bb = await b.page.evaluate(() => ({ tag: document.activeElement?.tagName, judul: document.title, h1: document.querySelector("#layar h1")?.textContent?.trim() }));
  periksa("I bahasa Python ke Java (komponen sama): judul tab dan fokus mengikuti h1 baru",
    bb.tag === "H1" && bb.judul === `${bb.h1} · belajar-codingV2` && /Java/.test(bb.h1 ?? ""), JSON.stringify(bb));
  await b.ctx.close();
  const k = await buka(BARU, "#/kuis/python/0");
  await k.page.waitForTimeout(1000);
  const h1Awal = await k.page.evaluate(() => document.querySelector("#layar h1")?.textContent?.trim());
  await k.page.evaluate(() => { location.hash = "#/kuis/python/1"; });
  await k.page.waitForTimeout(2500);
  const kk = await k.page.evaluate(() => ({ tag: document.activeElement?.tagName, judul: document.title, h1: document.querySelector("#layar h1")?.textContent?.trim() }));
  periksa("I kuis 1 ke kuis 2 (komponen sama): judul tab dan fokus mengikuti h1 baru",
    kk.tag === "H1" && kk.h1 !== h1Awal && kk.judul === `${kk.h1} · belajar-codingV2`, JSON.stringify(kk));
  await k.ctx.close();
}

// J. layar tanpa <h1> (SIM: materi dijawab 409) dan chip program pendukung.
// Kartu "Materi tidak terbuka" berdiri sendiri; judul tab dan fokus harus
// mengikuti judul kartunya, bukan tertinggal di judul layar sebelumnya.
{
  const simulasi = async (page) => {
    await page.route("**/api/materi?**", (r) => r.fulfill({ status: 409, contentType: "application/json", body: JSON.stringify({ galat: "Bab ini belum terbuka." }) }));
  };
  const { page, ctx } = await buka(BARU, "#/", { simulasi });
  await page.evaluate(() => { location.hash = "#/materi/python/1"; });
  await page.waitForTimeout(2500);
  const r = await page.evaluate(() => ({
    judul: document.title, h1: document.querySelectorAll("#layar h1").length,
    dalamKartu: Boolean(document.activeElement?.closest(".keadaan-isi")),
    teks: document.activeElement?.textContent?.trim(),
  }));
  periksa("J SIM materi gagal (tanpa h1): judul tab dan fokus mengikuti judul kartu",
    r.h1 === 0 && r.dalamKartu && r.judul === `${r.teks} · belajar-codingV2`, JSON.stringify(r));
  await ctx.close();
}
for (const tema of ["gelap", "terang", "kontras", "malam"]) {
  const simulasi = async (page) => {
    await page.addInitScript((t) => { try { localStorage.setItem("belajar.tema", JSON.stringify(t)); } catch { /* abaikan */ } }, tema);
    await page.route("**/api/bahasa?**", async (r) => { const re = await r.fetch(); const j = await re.json();
      if (j.key === "c") { j.siap = false; j.hilang = ["gcc"]; j.pasang = "sudo dnf install gcc"; } await r.fulfill({ response: re, json: j }); });
  };
  const { page, ctx } = await buka(BARU, "#/bahasa/c", { simulasi });
  const u = await page.evaluate(() => {
    const el = document.querySelector(".fakta-kurang");
    if (!el) return null;
    const sonde = document.createElement("i");
    sonde.style.color = "var(--tenang)"; document.body.appendChild(sonde);
    const tenang = getComputedStyle(sonde).color; sonde.remove();
    // `color-mix` dilaporkan sebagai `color(srgb 0.9 0.9 0.8 / a)`, komponen 0 sampai 1.
    const angka = (s) => { const n = s.match(/-?\d*\.?\d+(?:e-?\d+)?/g).map(Number); return s.startsWith("color(") ? [...n.slice(0, 3).map((v) => v * 255), ...n.slice(3)] : n; };
    const lum = ([r, g, b]) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
    let n = el, latar = null;
    while (n && !latar) { const m = angka(getComputedStyle(n).backgroundColor); if (m.length === 3 || m[3] === 1) latar = m.slice(0, 3); n = n.parentElement; }
    const teks = angka(getComputedStyle(el).color).slice(0, 3);
    const [a, b] = [lum(teks), lum(latar ?? [0, 0, 0])].sort((x, y) => y - x);
    return { warna: getComputedStyle(el).color, tenang, kontras: (a + 0.05) / (b + 0.05), isi: el.textContent.trim() };
  });
  periksa(`J chip program pendukung (${tema}): warna kabar, bukan galat, kontras >= 4,5`,
    Boolean(u) && u.warna === u.tenang && u.kontras >= 4.5 && /butuh gcc/.test(u.isi), JSON.stringify(u));
  await ctx.close();
}

// K. struktur materi, materi terkunci yang tidak buntu, kesiapan kuis, dan
// kontras teks yang dulu diredupkan dengan `opacity`.
// Kontras dihitung dari warna KOMPUTASI dengan `opacity` semua leluhur dan alfa
// latar ikut diperhitungkan: itu persis yang membuat teks `opacity: .32` jatuh
// ke 2:1 sementara token warnanya sendiri lolos.
const kontrasDi = (page, sel, prop = "color") => page.evaluate(([sel, prop]) => {
  const el = document.querySelector(sel);
  if (!el) return null;
  // `color-mix` dilaporkan sebagai `color(srgb 0.9 0.9 0.8 / a)`, komponen 0 sampai 1.
  const angka = (s) => { const n = s.match(/-?\d*\.?\d+(?:e-?\d+)?/g).map(Number); return s.startsWith("color(") ? [...n.slice(0, 3).map((v) => v * 255), ...n.slice(3)] : n; };
  const campur = (atas, bawah, a) => atas.slice(0, 3).map((c, i) => c * a + bawah[i] * (1 - a));
  const lum = ([r, g, b]) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const lapis = [];
  for (let x = el; x; x = x.parentElement) {
    const m = angka(getComputedStyle(x).backgroundColor);
    const alfa = m.length === 4 ? m[3] : 1;
    if (alfa === 0) continue;
    lapis.push([m.slice(0, 3), alfa]);
    if (alfa === 1) break;
  }
  let dasar = [0, 0, 0];
  if (lapis.length && lapis[lapis.length - 1][1] === 1) dasar = lapis.pop()[0];
  while (lapis.length) { const [w, a] = lapis.pop(); dasar = campur(w, dasar, a); }
  let op = 1;
  for (let x = el; x && x !== document.documentElement; x = x.parentElement) op *= Number(getComputedStyle(x).opacity);
  const teks = angka(getComputedStyle(el)[prop]);
  const efektif = campur(teks, dasar, (teks.length === 4 ? teks[3] : 1) * op);
  const [a, b] = [lum(efektif), lum(dasar)].sort((x, y) => y - x);
  return { kontras: (a + 0.05) / (b + 0.05), opasitas: op };
}, [sel, prop]);
{
  const m = await buka(BARU, "#/materi/python/1");
  const s = await m.page.evaluate(() => ({
    h: [...document.querySelectorAll("#layar h1, #layar h2, #layar h3, #layar h4")].map((e) => Number(e.tagName[1])),
    h2: document.querySelectorAll("#layar article.prosa h2").length,
    h3: document.querySelectorAll("#layar article.prosa h3").length,
  }));
  periksa("K materi: judul bagian h2 (bukan h3) dan tingkat heading tidak melompat",
    s.h2 >= 1 && s.h3 === 0 && s.h.every((n, i) => i === 0 || n <= s.h[i - 1] + 1), JSON.stringify(s));
  await m.ctx.close();
}
{
  const { page, ctx } = await buka(BARU, "#/materi/python/20");
  const k = await page.evaluate(() => {
    const b = document.querySelector(".keadaan-isi > b");
    return {
      role: b?.getAttribute("role"), level: b?.getAttribute("aria-level"), judul: document.title,
      judulKartu: b?.textContent?.trim(),
      a: [...document.querySelectorAll(".keadaan-isi a")].map((x) => ({ teks: x.textContent.trim(), href: x.getAttribute("href") })),
    };
  });
  periksa("K materi terkunci: judul kartu jadi heading tingkat 1 dan judul tab",
    k.role === "heading" && k.level === "1" && k.judul === `${k.judulKartu} · belajar-codingV2`, JSON.stringify(k));
  periksa("K materi terkunci: tautan langsung ke materi yang boleh dibuka, daftar materi sebagai cadangan",
    k.a.length === 2 && /^Baca /.test(k.a[0].teks) && /^#\/materi\/python\/\d+$/.test(k.a[0].href)
      && /Lihat daftar materi/.test(k.a[1].teks), JSON.stringify(k.a));
  await page.locator(".keadaan-isi a").first().click();
  await page.waitForTimeout(2500);
  const buka2 = await page.evaluate(() => ({ h1: document.querySelectorAll("#layar h1").length, kunci: document.querySelectorAll(".keadaan-kunci").length }));
  periksa("K materi terkunci: tautan 'Baca ...' membuka materi sungguhan, bukan penolakan lain", buka2.h1 === 1 && buka2.kunci === 0, JSON.stringify(buka2));
  await ctx.close();
}
{
  const dasar = await buka(BARU, "#/");
  const q = await dasar.page.evaluate(async () => {
    const r = await fetch("/api/bahasa?key=python", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR } });
    const j = await r.json();
    const i = j.kuis.findIndex((x) => !x.pernah && x.siap === false && x.sisa_materi > 0);
    return i < 0 ? null : { i, sisa: j.kuis[i].sisa_materi };
  });
  await dasar.ctx.close();
  periksa("K ada kuis yang materinya belum dibaca di profil uji", Boolean(q), JSON.stringify(q));
  if (q) {
    const k = await buka(BARU, `#/kuis/python/${q.i}`);
    const kepala = await k.page.locator(".kepala-besar").first().innerText();
    periksa("K pengantar kuis: menyebut materi yang diuji belum dibaca, sama dengan daftar bahasa",
      kepala.includes(`${q.sisa} materi yang diuji kuis ini belum kamu baca`), kepala.replace(/\n/g, " "));
    await k.ctx.close();
  }
}
for (const tema of ["gelap", "terang", "kontras", "malam"]) {
  const simulasi = async (page) => {
    await page.addInitScript((t) => { try { localStorage.setItem("belajar.tema", JSON.stringify(t)); } catch { /* abaikan */ } }, tema);
  };
  const b = await buka(BARU, "#/bahasa/python", { simulasi });
  const nomor = await kontrasDi(b.page, ".peta-bab .peta-terkunci");
  periksa(`K peta bab terkunci (${tema}): kontras >= 4,5 tanpa opacity`, Boolean(nomor) && nomor.kontras >= 4.5 && nomor.opasitas === 1, JSON.stringify(nomor));
  await b.ctx.close();
  const c = await buka(BARU, "#/karier", { simulasi });
  await c.page.locator(".kr-chip").nth(1).click();
  await c.page.waitForTimeout(600);
  const label = await kontrasDi(c.page, ".kr-simpul.redup .kr-label", "fill");
  const rumpun = await kontrasDi(c.page, ".kr-rumpun.redup", "fill");
  periksa(`K Karier saringan (${tema}): label simpul dan rumpun yang diredupkan tetap >= 4,5`,
    Boolean(label) && Boolean(rumpun) && label.kontras >= 4.5 && rumpun.kontras >= 4.5 && label.opasitas === 1,
    JSON.stringify({ label, rumpun }));
  await c.ctx.close();
  const s = await buka(BARU, "#/cari?q=variabel", { simulasi });
  const tanda = await kontrasDi(s.page, "mark");
  periksa(`K Cari mark (${tema}): kontras >= 4,5`, Boolean(tanda) && tanda.kontras >= 4.5, JSON.stringify(tanda));
  await s.ctx.close();
}

await browser.close();
console.log(gagal ? `GAGAL: ${gagal} pemeriksaan` : "SEMUA pemeriksaan lulus");
process.exit(gagal ? 1 : 0);
