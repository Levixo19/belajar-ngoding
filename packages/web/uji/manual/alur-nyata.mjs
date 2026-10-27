/* Alur nyata layar Langit di aplikasi PENUH (bundel React yang dilayani server).
 *
 * Yang dijaga di sini hanya bisa diukur di peramban dan lolos dari semua tes
 * lain: fokus papan ketik, Esc dari BODY, alamat rusak, gulir untuk fokus dan
 * panel, dan keadaan lintas navigasi. Tiap pemeriksaan menamai cacat yang
 * ditangkapnya.
 *
 *     BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/alur-nyata.mjs
 */
import { aktif, fokusBody, mulai, pemeriksa } from "./lib.mjs";

const P = pemeriksa("alur nyata Langit");
/** Satu bagian yang gagal (waktu habis karena fokus tidak pindah, dan seterusnya)
 *  dilaporkan sebagai pemeriksaan GAGAL, bukan menghentikan seluruh skrip:
 *  bagian sesudahnya tetap perlu dijalankan. */
const bagian = async (nama, fn) => {
  try { await fn(); } catch (e) { P.cek(`${nama}: bagian berhenti`, false, String(e.message).split("\n")[0]); }
};
const hash = (s) => s.page.evaluate(() => location.hash);
const opsi = (s) => s.page.$$("g[role=option]");
/** Esc berlapis: kartu judul, lalu pilihan, lalu lensa. Menekan Esc sampai
 *  `kondisi` terpenuhi (paling banyak 4 kali); mengembalikan berapa kali. */
const escSampai = async (s, kondisi, maks = 4) => {
  for (let n = 1; n <= maks; n++) {
    await s.page.keyboard.press("Escape"); await s.page.waitForTimeout(250);
    if (await kondisi()) return n;
  }
  return -1;
};
const klikBintang = async (s, i) => {
  const b = await (await opsi(s))[i].boundingBox();
  await s.page.mouse.click(b.x + b.width / 2, b.y + b.height / 2);
  await s.page.waitForTimeout(250);
};

/* ---- alamat dengan persen-sandi rusak tidak mengosongkan aplikasi */
for (const h of ["#/langit/%", "#/langit/%E0%A4%A", "#/langit/zzz", "#/langit/html/999"]) await bagian("alamat " + h, async () => {
  const s = await mulai({ hash: h, tunggu: "body" });
  await s.page.waitForTimeout(1200);
  const anak = await s.page.evaluate(() => document.querySelector("#akar")?.children.length ?? -1);
  P.cek(`alamat ${h}: aplikasi tetap tergambar`, anak > 0 && !s.konsol.some((k) => k.startsWith("pageerror")), { akarAnak: anak, galat: s.konsol.slice(0, 1) });
  await s.tutup();
});

/* ---- Esc dari BODY (muat langsung, klik ruang kosong, klik teks panel) */
await bagian("Esc dari BODY", async () => {
  const s = await mulai({ hash: "#/langit/python/3", tunggu: ".lt-lensa" });
  P.cek("muat alamat langsung tidak merebut fokus", await fokusBody(s.page));
  await s.page.keyboard.press("Escape"); await s.page.waitForTimeout(250);
  P.cek("Esc dari BODY melepas pilihan", (await hash(s)) === "#/langit/python", await hash(s));
  const k = await s.page.evaluate(() => { const r = document.querySelector(".lt-lensa-kanvas").getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; });
  await klikBintang(s, 5);
  await s.page.mouse.click(k.x + k.w - 30, k.y + k.h - 20); await s.page.waitForTimeout(250);
  P.cek("klik ruang kosong melepas pilihan", (await hash(s)) === "#/langit/python", await hash(s));
  await klikBintang(s, 5);
  await s.page.click(".lt-panel-ringkas, .lt-panel-kepala h3"); await s.page.waitForTimeout(150);
  P.cek("klik teks panel menjatuhkan fokus ke BODY (keadaan sah)", await fokusBody(s.page));
  await s.page.keyboard.press("Escape"); await s.page.waitForTimeout(250);
  P.cek("Esc dari BODY sesudah klik teks panel", (await hash(s)) === "#/langit/python", await hash(s));
  const nEsc = await escSampai(s, async () => (await hash(s)) === "#/langit");
  P.cek("Esc berlapis menutup lensa dalam paling banyak dua tekan lagi (kartu, lalu lensa)", nEsc >= 1 && nEsc <= 2, { nEsc, hash: await hash(s) });
  await s.tutup();
});

/* ---- tombol panel tidak membuang fokus ke BODY */
await bagian("tombol panel", async () => {
  const s = await mulai({ hash: "#/langit/python", tunggu: ".lt-lensa" });
  await klikBintang(s, 5);
  const panel = s.page.locator(".lt-panel");
  const sesudah = panel.getByRole("button", { name: /Sesudahnya/ });
  await sesudah.focus();
  await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(200);
  const h1 = await hash(s), a1 = await aktif(s.page);
  await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(200);
  const h2 = await hash(s), a2 = await aktif(s.page);
  P.cek("Sesudahnya dua kali berturut-turut: maju dua bintang, fokus tetap di tombol",
    h1 === "#/langit/python/6" && h2 === "#/langit/python/7" && a1.includes("Sesudahnya") && a2.includes("Sesudahnya"), { h1, a1, h2, a2 });
  const tutupX = panel.getByRole("button", { name: /Tutup detail/ });
  await tutupX.focus(); await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(200);
  P.cek("Tutup detail: fokus kembali ke bintangnya", /option/.test(await aktif(s.page)), await aktif(s.page));
  await s.page.locator(".lt-berikut").focus(); await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(250);
  P.cek("Berikutnya (panel rasi): fokus di bintang", /option/.test(await aktif(s.page)), await aktif(s.page));
  await escSampai(s, async () => (await s.page.locator(".lt-bab-baris").count()) > 0);
  await s.page.locator(".lt-bab-baris").nth(2).focus(); await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(250);
  P.cek("baris bab (panel rasi): fokus di bintang", /option/.test(await aktif(s.page)), await aktif(s.page));
  // bintang terakhir: Sesudahnya tidak hilang dari urutan fokus
  const n = (await opsi(s)).length;
  await s.page.keyboard.press("End"); await s.page.waitForTimeout(100);
  await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(250);
  await panel.getByRole("button", { name: /Sesudahnya/ }).focus(); await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(150);
  P.cek("Sesudahnya di bintang terakhir: tidak berbuat apa pun dan fokus tetap", (await hash(s)) === `#/langit/python/${n - 1}` && (await aktif(s.page)).includes("Sesudahnya"), { h: await hash(s), a: await aktif(s.page) });
  await s.tutup();
});

/* ---- pintasan peramban tidak dibajak daftar bintang */
await bagian("pintasan peramban", async () => {
  const s = await mulai({ hash: "#/langit/python", tunggu: ".lt-lensa" });
  await s.page.evaluate(() => { window.__log = []; document.addEventListener("keydown", (e) => window.__log.push([e.key, e.altKey, e.ctrlKey, e.metaKey, e.defaultPrevented])); });
  const o = await opsi(s);
  await o[1].evaluate((e) => e.focus());
  for (const [mod, tombol] of [["Alt", "ArrowRight"], ["Alt", "ArrowLeft"], ["Control", "Home"], ["Control", "End"], ["Meta", "ArrowRight"]]) {
    await s.page.keyboard.down(mod); await s.page.keyboard.press(tombol); await s.page.keyboard.up(mod);
    await s.page.waitForTimeout(60);
    const tetap = /option/.test(await aktif(s.page)) && (await aktif(s.page)).includes("2. ");
    P.cek(`${mod}+${tombol} tidak menggeser fokus bintang`, tetap, await aktif(s.page));
  }
  const dicegah = await s.page.evaluate(() => window.__log.filter((x) => (x[1] || x[2] || x[3]) && x[4]).length);
  P.cek("tidak ada preventDefault untuk tombol ber-Alt/Ctrl/Meta", dicegah === 0, { dicegah });
  await s.page.keyboard.press("ArrowRight");
  P.cek("panah biasa tetap menggeser fokus", (await aktif(s.page)).includes("3. "), await aktif(s.page));
  await s.tutup();
});

/* ---- fokus selalu tampak pada tinggi laptop nyata dan zum: viewport CSS = layar / zum - bilah peramban */
for (const [w, h, ket] of [[1366, 600, "1366x600"], [1093, 480, "1366 zum 125"], [952, 452, "1905 zum 200"], [683, 384, "1366 zum 200"]]) await bagian("zum " + ket, async () => {
  const s = await mulai({ lebar: w, tinggi: h, hash: "#/langit/html", tunggu: ".lt-lensa" });
  const relBawah = await s.page.evaluate(() => document.getElementById("rel")?.getBoundingClientRect().bottom ?? 0);
  await s.page.evaluate(() => document.querySelector("g[role=option]").focus({ preventScroll: true }));
  const n = (await opsi(s)).length;
  let luar = 0, diBawahPil = 0;
  for (let i = 0; i < n; i++) {
    await s.page.waitForTimeout(40);
    const r = await s.page.evaluate(() => { const e = document.activeElement.getBoundingClientRect(); return [e.top, e.bottom]; });
    if (r[0] < 0 || r[1] > h) luar += 1; else if (r[0] < relBawah - 0.5) diBawahPil += 1;
    await s.page.keyboard.press("ArrowRight");
  }
  P.cek(`${ket}: ${n} langkah panah, fokus tampak penuh dan tidak di bawah pil atas`, luar === 0 && diBawahPil === 0, { luar, diBawahPil });
  await s.tutup();
});

/* ---- PENUH=1: SELURUH rasi (1.062 langkah panah) pada tinggi pakai laptop 592 dan 544 */
if (process.env.PENUH) {
  for (const [w, h, ket] of [[1366, 592, "1366x592"], [1280, 544, "1280x544"]]) await bagian("penuh " + ket, async () => {
    const s = await mulai({ lebar: w, tinggi: h, hash: "#/langit", tunggu: ".lt-ikhtisar, .lt-daftar" });
    const kunci = await s.page.evaluate(async () => {
      const r = await fetch("/api/langit", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR } });
      return (await r.json()).bahasa.map((b) => b.key);
    });
    let langkah = 0, luar = 0, diBawahPil = 0;
    for (const k of kunci) {
      await s.page.evaluate((x) => { location.hash = "#/langit/" + x; }, k);
      await s.page.waitForSelector(".lt-lensa g[role=option]"); await s.page.waitForTimeout(150);
      const relBawah = await s.page.evaluate(() => document.getElementById("rel")?.getBoundingClientRect().bottom ?? 0);
      await s.page.evaluate(() => document.querySelector("g[role=option]").focus({ preventScroll: true }));
      const n = (await opsi(s)).length;
      for (let i = 0; i < n; i++) {
        await s.page.waitForTimeout(25);
        const r = await s.page.evaluate(() => { const e = document.activeElement.getBoundingClientRect(); return [e.top, e.bottom]; });
        langkah += 1;
        if (r[0] < 0 || r[1] > h) luar += 1; else if (r[0] < relBawah - 0.5) diBawahPil += 1;
        await s.page.keyboard.press("ArrowRight");
      }
    }
    P.cek(`${ket}: ${langkah} langkah panah di ${kunci.length} rasi: fokus tampak penuh dan tidak di bawah pil atas`, langkah >= 1062 && luar === 0 && diBawahPil === 0, { langkah, luar, diBawahPil });
    await s.tutup();
  });
}

/* ---- mode panel di bawah: judul panel tampak sesudah memilih, KECUALI bila
   jendela terlalu pendek untuk memuat judul dan bintang terpilih bersama
   (kanvas 380 px di atas panel, ruang tampak 370 px di 952x452 dan 314 px di
   683x384). Di sana bintang menang: gulir dibatasi `bintangAtas` di
   `deltaGulirPanel`, dan penanda terpilih tepat di bawah pil atas + 8 px.
   Dulu judul yang menang, dan bintang di bagian atas kanvas hilang dari
   pandangan tepat saat dipilih (keputusan butir 5 ronde perbaikan). */
for (const [w, h, ket] of [[952, 452, "952x452"], [683, 384, "683x384"], [1000, 600, "1000x600"]]) await bagian("panel bawah " + ket, async () => {
  const s = await mulai({ lebar: w, tinggi: h, hash: "#/langit/html", tunggu: ".lt-lensa" });
  await klikBintang(s, 2);
  await s.page.waitForTimeout(500);
  const r = await s.page.evaluate(() => {
    const e = document.querySelector(".lt-panel-kepala h3")?.getBoundingClientRect();
    const c = document.querySelector(".lt-ln-terpilih-isi")?.getBoundingClientRect();
    return { atas: e?.top, bawah: e?.bottom, tinggi: innerHeight, mode: document.querySelector(".lt-lensa-isi")?.dataset.mode,
      cincinAtas: c?.top, bawahPil: document.getElementById("rel")?.getBoundingClientRect().bottom ?? 0 };
  });
  const judulTampak = r.atas >= 0 && r.bawah <= r.tinggi;
  const bintangDijaga = Math.abs(r.cincinAtas - (r.bawahPil + 8)) < 1.5;
  P.cek(`${ket}: judul panel tampak penuh sesudah klik bintang, atau bintang dijaga di bawah pil atas bila keduanya tak muat`,
    r.mode === "bawah" && r.cincinAtas >= r.bawahPil && (judulTampak || bintangDijaga), { ...r, judulTampak, bintangDijaga });
  await s.tutup();
});

/* ---- Daftar (akar < 1156): tutup lensa mengembalikan fokus dan posisi */
await bagian("Daftar", async () => {
  const s = await mulai({ lebar: 952, tinggi: 700, hash: "#/langit", tunggu: ".lt-daftar" });
  const baris = s.page.locator('a.lt-daftar-baris[href="#/langit/sql"]');
  await baris.scrollIntoViewIfNeeded(); await s.page.waitForTimeout(150);
  await baris.focus(); await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(500);
  await escSampai(s, async () => (await hash(s)) === "#/langit");
  await s.page.waitForTimeout(300);
  const r = await s.page.evaluate(() => { const e = document.querySelector('a.lt-daftar-baris[href="#/langit/sql"]'); const b = e.getBoundingClientRect(); return { fokus: document.activeElement === e, tampak: b.top >= 0 && b.bottom <= innerHeight }; });
  P.cek("Daftar: sesudah menutup lensa fokus di barisnya dan barisnya tampak", r.fokus && r.tampak, r);
  // Tautan lewati: Enter memindahkan fokus ke daftar (dulu hanya ada di peta,
  // jadi Daftar menuntut sekitar 16 Tab melewati saringan).
  await s.page.evaluate(() => { location.hash = "#/langit"; }); await s.page.waitForTimeout(400);
  const lewati = s.page.locator(".lt-krom .lt-lewati");
  const adaLewat = (await lewati.count()) === 1;
  P.cek("Daftar: ada tepat satu tautan lewati", adaLewat);
  if (adaLewat) {
    await lewati.focus(); await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(150);
    const di = await s.page.evaluate(() => { const a = document.activeElement; return !!a && !!a.closest(".lt-daftar"); });
    P.cek("Daftar: tautan lewati memindahkan fokus ke daftar rasi", di);
  }
  P.cek("Daftar: penanda 'Mulai di sini', bila ada, bertautan sah (ada-tidaknya pada profil xp = 0 diperiksa ukur-peta.mjs)", await s.page.evaluate(() => {
    const a = document.querySelector(".lt-daftar .lt-mulai");
    return !a || /^#\/langit\/[a-z0-9]+\/\d+$/.test(a.getAttribute("href") || "");
  }));
  await s.tutup();
});

/* ---- /api/bahasa gagal: bintang terkunci menyebut kegagalannya, bukan diam */
await bagian("galat /api/bahasa", async () => {
  const PESAN = "Alasan terkunci dan keterangan bab tidak bisa dimuat";
  for (const gagal of [true, false]) {
    const s = await mulai({ lebar: 1366, tinggi: 768, hash: "#/langit", tunggu: ".lt-ikhtisar" });
    if (gagal) await s.page.route(/\/api\/bahasa\?/, (r) => r.fulfill({ status: 500, contentType: "application/json", body: '{"galat":"uji"}' }));
    await s.page.evaluate(() => { location.hash = "#/langit/python/10"; });
    await s.page.waitForSelector(".lt-panel-isi", { timeout: 15000 });
    await s.page.waitForTimeout(800);
    const teks = await s.page.evaluate(() => document.querySelector(".lt-panel-isi")?.innerText ?? "");
    P.cek(gagal ? "API bahasa 500: panel bintang terkunci menyebut kegagalan" : "API bahasa normal: pesan kegagalan tidak muncul dan alasan tampil",
      gagal ? teks.includes(PESAN) : !teks.includes(PESAN) && /Baca \d+ materi lagi/.test(teks));
    await s.tutup();
  }
});

/* ---- keadaan lintas navigasi: Kembali dari materi mendarat di lensa yang sama */
await bagian("keadaan lintas navigasi", async () => {
  const s = await mulai({ hash: "#/langit", tunggu: ".lt-ikhtisar" });
  await s.page.getByRole("button", { name: "Perulangan" }).click();
  await s.page.locator("a.lt-nama[data-key=html]").click(); await s.page.waitForTimeout(500);
  await klikBintang(s, 0);
  const st = await s.page.evaluate(() => ({ h: location.hash, lt: history.state?.lt }));
  P.cek("pilihan perkakas ditulis ke history.state", st.lt?.konsep === "Perulangan", st);
  await s.page.locator(".lt-panel a.tbl-utama").click(); await s.page.waitForTimeout(800);
  P.cek("tombol aksi membuka layar materi", /^#\/materi\/html\/0/.test(await hash(s)), await hash(s));
  P.cek("memilih bintang tidak menulis; membuka materi mencoba menulis (ditolak harness)", s.tulisDitolak.length <= 1, s.tulisDitolak);
  await s.page.goBack(); await s.page.waitForTimeout(900);
  const pulih = await s.page.evaluate(() => ({ h: location.hash, terpilih: document.querySelector('g[role=option][aria-selected=true]')?.getAttribute("aria-label")?.slice(0, 30), konsep: document.querySelector(".lt-lensa-alat button")?.textContent?.slice(0, 40) }));
  P.cek("Kembali: lensa, bintang, dan saringan pulih", pulih.h === "#/langit/html/0" && !!pulih.terpilih && /Perulangan/.test(pulih.konsep ?? ""), pulih);
  P.cek("Kembali: fokus di bintang", /option/.test(await aktif(s.page)), await aktif(s.page));
  // ERR_FAILED = POST yang sengaja digagalkan harness (tulisDitolak), bukan galat aplikasi
  const galat = s.konsol.filter((k) => !/ERR_FAILED/.test(k));
  P.cek("tanpa galat konsol", galat.length === 0, galat.slice(0, 2));
  await s.tutup();
});

/* ---- bintang terpilih tetap tampak di mode panel di bawah: gulir ke judul panel
   tidak boleh mendorong bintang di bagian atas kanvas ke bawah pil atas (dulu 4
   dari 12 klik di 320x568 sampai 952x600) */
for (const [w, h] of [[952, 600], [683, 384], [390, 600], [320, 568]]) await bagian(`bintang tampak ${w}x${h}`, async () => {
  for (const idx of [5, 12]) {
    const s = await mulai({ lebar: w, tinggi: h, hash: "#/langit/html", tunggu: ".lt-lensa" });
    const atas = (i) => s.page.evaluate((i) => { const g = document.querySelectorAll(".lt-lensa g[role=option]")[i]; const r = g.getBoundingClientRect(); return { x: r.left + r.width / 2, y: r.top + r.height / 2 }; }, i);
    let p = await atas(idx);
    if (p.y > h - 20 || p.y < 0) { await s.page.evaluate((y) => window.scrollTo(0, scrollY + y - 150), p.y); p = await atas(idx); }
    await s.page.mouse.click(p.x, p.y); await s.page.waitForTimeout(700);
    const r = await s.page.evaluate((i) => {
      const cincin = document.querySelector(".lt-ln-terpilih-isi")?.getBoundingClientRect();
      return { atas: cincin?.top, bawahPil: document.getElementById("rel")?.getBoundingClientRect().bottom ?? 0 };
    }, idx);
    P.cek(`${w}x${h} bintang ${idx + 1}: penanda terpilih di bawah pil atas sesudah gulir`, r.atas !== undefined && r.atas >= r.bawahPil, r);
    await s.tutup();
  }
});

/* ---- Esc dengan menu "Lainnya" terbuka menutup menu SAJA: pendengar dokumen
   milik lensa jalan lebih dulu daripada pendengar jendela milik menu */
await bagian("Esc dan menu Lainnya", async () => {
  const s = await mulai({ lebar: 1440, tinggi: 900, hash: "#/langit/html/2", tunggu: ".lt-lensa g[role=option]" });
  const st = () => s.page.evaluate(() => ({ terpilih: document.querySelectorAll('.lt-lensa [aria-selected="true"]').length, menu: document.querySelector(".rel-pemicu")?.getAttribute("aria-expanded"), hash: location.hash }));
  await s.page.click(".rel-pemicu"); await s.page.waitForTimeout(200);
  const a = await st();
  await s.page.keyboard.press("Escape"); await s.page.waitForTimeout(250);
  const b = await st();
  P.cek("Esc dengan menu Lainnya terbuka: menu tutup, pilihan bintang TETAP", a.menu === "true" && b.menu === "false" && b.terpilih === 1 && b.hash === "#/langit/html/2", { a, b });
  await s.page.keyboard.press("Escape"); await s.page.waitForTimeout(250);
  P.cek("Esc berikutnya (menu sudah tutup): baru melepas pilihan", (await hash(s)) === "#/langit/html", await hash(s));
  await s.tutup();
});

/* ---- Esc sesudah Enter: pilihan lalu lensa, dua tekan. Fokus kembali ke bintang
   yang baru dilepas dan dulu memunculkan kartunya lagi (Esc kedua cuma
   menyembunyikannya, ketiga baru menutup lensa) */
await bagian("Esc sesudah Enter", async () => {
  const s = await mulai({ hash: "#/langit/python", tunggu: ".lt-lensa g[role=option]" });
  await s.page.evaluate(() => document.querySelectorAll("g[role=option]")[3].focus({ preventScroll: true }));
  await s.page.keyboard.press("ArrowRight"); await s.page.keyboard.press("ArrowLeft");
  await s.page.keyboard.press("Enter"); await s.page.waitForTimeout(250);
  P.cek("Enter memilih bintang", (await hash(s)) === "#/langit/python/3", await hash(s));
  await s.page.keyboard.press("Escape"); await s.page.waitForTimeout(250);
  const kartu = await s.page.evaluate(() => !!document.querySelector(".lt-ln-tip"));
  P.cek("Esc pertama melepas pilihan dan kartu fokus tidak muncul lagi", (await hash(s)) === "#/langit/python" && !kartu, { hash: await hash(s), kartu });
  await s.page.keyboard.press("Escape"); await s.page.waitForTimeout(250);
  P.cek("Esc kedua menutup lensa (kaki lensa menjanjikan \"Esc kembali ke peta\")", (await hash(s)) === "#/langit", await hash(s));
  await s.tutup();
});

/* ---- kartu judul hover tidak memblokir bintang tetangga untuk mouse: gerakan
   paling alami (menyusuri rasi dari bintang ke tetangganya) dulu salah 21 sampai
   28 persen karena pusat tetangga ada di bawah kartu */
for (const [w, h] of [[1366, 768], [1905, 904]]) await bagian(`kartu hover ${w}x${h}`, async () => {
  const s = await mulai({ lebar: w, tinggi: h, hash: "#/langit/python", tunggu: ".lt-lensa g[role=option]" });
  const pusat = (i) => s.page.evaluate((i) => { const g = document.querySelectorAll(".lt-lensa [role=option]")[i]; const r = (g.querySelector(".lt-gl-isi, .lt-gl-tepi") ?? g).getBoundingClientRect(); return { x: r.left + r.width / 2, y: r.top + r.height / 2 }; }, i);
  const n = (await opsi(s)).length;
  const salah = [];
  let tertutup = 0;
  for (let i = 1; i < n; i++) {
    await s.page.mouse.move(w - 5, 120); await s.page.waitForTimeout(60);
    const a = await pusat(i - 1), b = await pusat(i);
    await s.page.mouse.move(a.x, a.y); await s.page.waitForTimeout(70);
    const kartu = await s.page.evaluate(() => { const t = document.querySelector(".lt-ln-tip"); if (!t) return null; const r = t.getBoundingClientRect(); return [r.left, r.top, r.right, r.bottom]; });
    if (kartu && b.x >= kartu[0] && b.x <= kartu[2] && b.y >= kartu[1] && b.y <= kartu[3]) tertutup += 1;
    for (let k = 1; k <= 24; k++) { await s.page.mouse.move(a.x + ((b.x - a.x) * k) / 24, a.y + ((b.y - a.y) * k) / 24); await s.page.waitForTimeout(8); }
    await s.page.waitForTimeout(60);
    await s.page.mouse.down(); await s.page.mouse.up(); await s.page.waitForTimeout(90);
    const t = await s.page.evaluate(() => { const e = document.querySelector("[role=option][aria-selected=true]"); return e ? [...document.querySelectorAll(".lt-lensa [role=option]")].indexOf(e) : -1; });
    if (t !== i) salah.push({ harap: i, dapat: t });
  }
  P.cek(`${w}x${h}: ${n - 1} perpindahan bintang ke tetangganya (${tertutup} dengan pusat tujuan di bawah kartu), semua memilih tetangga`, salah.length === 0 && tertutup >= 5, { salah: salah.length, tertutup, contoh: salah.slice(0, 4) });
  await s.tutup();
});

P.selesai();
