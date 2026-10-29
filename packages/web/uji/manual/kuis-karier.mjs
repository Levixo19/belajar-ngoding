/* Perilaku kuis kecocokan Peta Karier yang dijanjikan rancangannya: satu soal
 * sekali tampil, pilihan terpilih terlihat tanpa bergantung warna, syarat
 * minimum disebut dengan angkanya, tidak ada tombol yang buntu, dan hasilnya
 * menjelaskan jawaban MANA yang membawa ke tiap profesi. Semuanya janji yang
 * tidak terlihat oleh tsc dan tes sumber; hanya melihat HALAMANNYA yang
 * membuktikannya.
 *
 *   BELAJAR_URL=http://127.0.0.1:7972/ PLAYWRIGHT_MJS=... node uji/manual/kuis-karier.mjs
 *   OUT=/jalur/folder  (opsional: simpan tangkapan layar)
 *
 * Jalankan terhadap server berprofil TERPISAH. Skrip ini menolak port 7777 dan
 * MENULIS satu hal ke profil uji: "Jadikan tujuanku" mengisi `tujuan_karier` di
 * konfigurasi, lalu dibatalkan lagi sebelum selesai. Hasil kuis sendiri hanya
 * GET. Keadaan yang tidak bisa dibuat nyata (server gagal, server lama tanpa
 * medan `dari`) DISIMULASIKAN lewat intersepsi respons dan ditandai "SIM".
 */
import fs from "node:fs";
import path from "node:path";

const URL_DASAR = process.env.BELAJAR_URL ?? "";
let alamat = null; try { alamat = new URL(URL_DASAR); } catch { /* kosong */ }
if (!alamat || alamat.hostname !== "127.0.0.1" || alamat.port === "7777" || alamat.port === "") {
  console.error("MENOLAK: BELAJAR_URL harus http://127.0.0.1:<port uji>/, bukan 7777.");
  process.exit(2);
}
const OUT = process.env.OUT ?? "";
if (OUT) fs.mkdirSync(OUT, { recursive: true });
const pw = await import(process.env.PLAYWRIGHT_MJS ?? "playwright");
const chromium = pw.chromium ?? pw.default.chromium;
const browser = await chromium.launch({
  executablePath: process.env.CHROME ?? "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox"] });

let gagal = 0;
const periksa = (nama, ok, rinci = "") => {
  if (!ok) gagal += 1;
  console.log(`${ok ? "lulus " : "GAGAL "} ${nama}${rinci ? "  (" + String(rinci).slice(0, 170) + ")" : ""}`);
};

async function buka({ tema = "gelap", lebar = 1440, tinggi = 900, simulasi = null } = {}) {
  const ctx = await browser.newContext({ viewport: { width: lebar, height: tinggi } });
  await ctx.addInitScript((t) => {
    try { localStorage.setItem("belajar.gerak", JSON.stringify("mati")); localStorage.setItem("belajar.tema", JSON.stringify(t)); } catch { /* abaikan */ }
  }, tema);
  const page = await ctx.newPage();
  const galat = [];
  page.on("pageerror", (e) => galat.push(String(e).slice(0, 160)));
  page.on("console", (m) => { if (m.type() === "error") galat.push(m.text().slice(0, 160)); });
  if (simulasi) await simulasi(page);
  await page.goto(URL_DASAR + "#/karier");
  await page.waitForSelector("#kr-cocok .kr-soal", { timeout: 15000 });
  await page.waitForTimeout(500);
  await page.evaluate(() => { document.getElementById("kr-cocok").scrollIntoView({ block: "start" }); window.scrollBy(0, -100); });
  return { page, galat };
}
const foto = async (page, nama) => { if (OUT) await page.screenshot({ path: path.join(OUT, nama + ".png") }); };
const api = (page, jalur) => page.evaluate(async (j) => {
  const r = await fetch("/api/" + j, { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR } });
  return r.json();
}, jalur);
const ruang = (page) => page.locator("#kr-cocok");
const opsi = (page) => page.locator("#kr-cocok .kr-pilihan");
const tombol = (page, nama) => ruang(page).getByRole("button", { name: nama });
const fokusTag = (page) => page.evaluate(() => {
  const a = document.activeElement;
  return a ? `${a.tagName}${a.tagName === "LEGEND" ? ":" + a.textContent.slice(0, 40) : ""}` : "null";
});
const hitung = (page) => ruang(page).locator(".kc-hitung").textContent();
const sehat = (galat, nama) => periksa(`${nama}: tanpa galat konsol`, galat.length === 0, galat[0]);
const rapat = (s) => s.replace(/\s+/g, " ").trim();

/** Kontras teks terhadap latar KOMPUTASI: alfa latar dan opacity leluhur ikut
 *  dihitung (cara yang sama dengan belajar-ux.mjs blok K). */
const kontrasDi = (page, sel, prop = "color") => page.evaluate(([sel, prop]) => {
  const el = document.querySelector(sel);
  if (!el) return null;
  // `color-mix` dilaporkan peramban sebagai `color(srgb 0.93 0.90 0.86 / 0.1)`,
  // komponennya 0 sampai 1. Membacanya sebagai 0 sampai 255 membuat latar
  // krem terhitung hitam dan kontras 14:1 tampak 1,2:1.
  const angka = (s) => {
    const n = s.match(/-?\d*\.?\d+(?:e-?\d+)?/g).map(Number);
    return s.startsWith("color(") ? [...n.slice(0, 3).map((v) => v * 255), ...n.slice(3)] : n;
  };
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
  return +((a + 0.05) / (b + 0.05)).toFixed(2);
}, [sel, prop]);

/* ------------------------------------------------------------------- A awal */
{
  const { page, galat } = await buka();
  const n = await page.locator("#kr-cocok fieldset.kr-soal").count();
  periksa("A satu soal tampil, bukan enam", n === 1, `fieldset=${n}`);
  periksa("A hitungan 'Soal 1 dari 6' terlihat", (await hitung(page)) === "Soal 1 dari 6");
  periksa("A empat pilihan, tak ada yang terpilih dari awal",
    (await opsi(page).count()) === 4 && (await page.locator("#kr-cocok input[type=radio]:checked").count()) === 0);
  periksa("A daftar jawaban: enam baris, semuanya 'Belum dijawab'",
    (await page.locator("#kr-cocok .kc-baris").count()) === 6 &&
    (await page.locator("#kr-cocok .kc-baris[data-kosong]").count()) === 6);
  periksa("A syarat minimum disebut dengan angkanya",
    (await ruang(page).locator(".kc-sisa").textContent()) === "Jawab 3 soal lagi untuk melihat yang cocok.");
  periksa("A tombol maju di soal kosong = Lewati (tenang, bukan utama)",
    (await tombol(page, "Lewati soal ini").count()) === 1 && /tbl-hantu/.test(await tombol(page, "Lewati soal ini").getAttribute("class")));
  periksa("A tidak ada tombol atau isian yang mati di kuis",
    (await page.locator("#kr-cocok button:disabled, #kr-cocok input:disabled").count()) === 0);
  periksa("A kalimat pembuka menyebut jumlah soal dengan kata",
    /^Enam pertanyaan/.test(await ruang(page).locator(".kr-bagian-kepala p").textContent()));
  await foto(page, "A-awal");
  sehat(galat, "A");
  await page.context().close();
}

/* ---------------------------------------------------- B memilih dan papan ketik */
{
  const { page, galat } = await buka();
  const label2 = (await opsi(page).nth(1).locator(".kc-label").textContent()).trim();
  await opsi(page).nth(1).click();
  periksa("B klik memilih tepat satu opsi", (await page.locator("#kr-cocok input[type=radio]:checked").count()) === 1 &&
    await opsi(page).nth(1).locator("input").isChecked());
  const tampak = await page.evaluate(() => [...document.querySelectorAll("#kr-cocok .kr-pilihan")].map((l) => ({
    tanda: getComputedStyle(l.querySelector(".kc-tanda")).visibility,
    tebal: Number(getComputedStyle(l.querySelector(".kc-label")).fontWeight),
    nomor: getComputedStyle(l.querySelector(".kc-nomor")).backgroundColor,
  })));
  periksa("B pilihan terpilih bertanda centang, yang lain tidak",
    tampak[1].tanda === "visible" && [0, 2, 3].every((i) => tampak[i].tanda === "hidden"), JSON.stringify(tampak.map((x) => x.tanda)));
  periksa("B terpilih dibedakan TANPA warna: huruf lebih tebal dan centang", tampak[1].tebal >= 600 && tampak[0].tebal < 600);
  periksa("B nomor pilihan terpilih terisi, bukan hanya garis", tampak[1].nomor !== tampak[0].nomor);
  periksa("B daftar jawaban memuat kalimat pilihan itu persis",
    (await page.locator("#kr-cocok .kc-baris").first().locator(".kc-teks").textContent()) === label2);
  periksa("B tombol maju berubah jadi Lanjut dan menjadi tombol utama",
    (await tombol(page, "Lanjut").count()) === 1 && /tbl-utama/.test(await tombol(page, "Lanjut").getAttribute("class")));
  periksa("B sisa jawaban ikut berubah", (await ruang(page).locator(".kc-sisa").textContent()) === "Jawab 2 soal lagi untuk melihat yang cocok.");
  await foto(page, "B-satu-dipilih");

  // papan ketik: angka memilih dan memindahkan fokus, panah menggeser, Enter maju
  await opsi(page).nth(0).locator("input").focus();
  await page.keyboard.press("3");
  periksa("B tombol angka 3 memilih opsi ketiga dan fokus ikut",
    (await opsi(page).nth(2).locator("input").isChecked()) &&
    await page.evaluate(() => document.activeElement === document.querySelectorAll("#kr-cocok input[type=radio]")[2]));
  await page.keyboard.press("ArrowDown");
  periksa("B panah bawah memilih opsi keempat (perilaku radio asli)", await opsi(page).nth(3).locator("input").isChecked());
  await page.keyboard.press("Enter");
  await page.waitForTimeout(200);
  periksa("B Enter maju ke soal 2 dan fokus ke judul soalnya",
    /^LEGEND:/.test(await fokusTag(page)) && (await hitung(page)) === "Soal 2 dari 6", await fokusTag(page));
  await tombol(page, "Kembali").click();
  await page.waitForTimeout(200);
  periksa("B Kembali mempertahankan jawaban soal 1", (await opsi(page).nth(3).locator("input").isChecked()) && (await hitung(page)) === "Soal 1 dari 6");
  periksa("B Kembali tidak ada di soal pertama", (await tombol(page, "Kembali").count()) === 0);
  sehat(galat, "B");
  await page.context().close();
}

/* ----------------------------------------- C syarat minimum jujur dan tak buntu */
{
  const { page, galat } = await buka();
  await opsi(page).nth(0).click();
  await tombol(page, "Lanjut").click();
  await opsi(page).nth(1).click();
  periksa("C dua jawaban: kalimat menyebut tinggal satu", (await ruang(page).locator(".kc-sisa").textContent()) === "Jawab 1 soal lagi untuk melihat yang cocok.");
  periksa("C dua jawaban: tidak ada tombol hasil", (await tombol(page, "Lihat yang cocok").count()) === 0);
  await page.locator("#kr-cocok .kc-baris").nth(5).click();
  await page.waitForTimeout(150);
  periksa("C lompat lewat daftar ke soal 6", (await hitung(page)) === "Soal 6 dari 6" && /^LEGEND:/.test(await fokusTag(page)));
  periksa("C di soal terakhir yang kurang jawaban: tombol mengantar ke soal yang belum dijawab, bukan menolak",
    (await tombol(page, "Ke soal 3 yang belum dijawab").count()) === 1);
  periksa("C tombol itu tidak digandakan di daftar jawaban", (await ruang(page).getByRole("button", { name: /yang belum dijawab/ }).count()) === 1);
  await tombol(page, "Ke soal 3 yang belum dijawab").click();
  await page.waitForTimeout(150);
  periksa("C tombol itu benar-benar membuka soal 3", (await hitung(page)) === "Soal 3 dari 6");
  await opsi(page).nth(2).click();
  periksa("C tiga jawaban: kalimat berganti", (await ruang(page).locator(".kc-sisa").textContent()) === "Makin banyak soal terjawab, makin jelas arahnya.");
  periksa("C tiga jawaban: tombol hasil muncul di daftar", (await ruang(page).locator(".kc-rel").getByRole("button", { name: "Lihat yang cocok" }).count()) === 1);
  await foto(page, "C-tiga-jawaban");
  sehat(galat, "C");
  await page.context().close();
}

/* ------------------------------------------------------------------ D hasil */
{
  const { page, galat } = await buka();
  const profesi = Object.fromEntries((await api(page, "karier")).profesi.map((p) => [p.id, p.nama]));
  const dipilih = [0, 1, 2, null, 1, 0];       // soal 4 dilewati
  const kalimat = [];
  for (let i = 0; i < 6; i++) {
    const j = dipilih[i];
    if (j === null) { await tombol(page, "Lewati soal ini").click(); kalimat.push(null); continue; }
    kalimat.push((await opsi(page).nth(j).locator(".kc-label").textContent()).trim());
    await opsi(page).nth(j).click();
    if (i < 5) await tombol(page, "Lanjut").click();
  }
  periksa("D di soal terakhir tombol maju = Lihat yang cocok (utama)", /tbl-utama/.test(await tombol(page, "Lihat yang cocok").first().getAttribute("class")));
  await tombol(page, "Lihat yang cocok").first().click();
  await page.waitForSelector("#kr-cocok .kc-hasil");
  await page.waitForTimeout(250);
  const server = await api(page, "karier/kuis?pilihan=0,1,2,,1,0");
  const kartu = page.locator("#kr-cocok .kr-juara > li");
  periksa("D fokus pindah ke judul hasil", (await page.evaluate(() => document.activeElement?.className)) === "kc-hasil-judul");
  periksa("D judul hasil menyebut jumlah dengan kata", (await ruang(page).locator(".kc-hasil-judul").textContent()) === "Tiga arah yang paling dekat dengan jawabanmu");
  const nama = await Promise.all([0, 1, 2].map(async (i) => (await kartu.nth(i).locator(".judul").textContent()).trim()));
  periksa("D tiga kartu, nama dan urutannya sama persis dengan jawaban server",
    nama.length === 3 && nama.every((n, i) => n === profesi[server.hasil[i].id]), nama.join(" | "));
  const dariApi = server.hasil.map((h) => h.dari ?? []);
  periksa("D tiap kartu: jumlah baris alasan = jumlah butir `dari` dari server",
    (await Promise.all([0, 1, 2].map((i) => kartu.nth(i).locator(".kc-alasan li").count()))).every((c, i) => c === dariApi[i].length && c > 0),
    JSON.stringify(dariApi.map((d) => d.length)));
  let alasanBenar = true, rinci = "";
  for (let i = 0; i < 3; i++) {
    const baris = kartu.nth(i).locator(".kc-alasan li");
    for (let k = 0; k < dariApi[i].length; k++) {
      const teks = await baris.nth(k).textContent();
      const soal = dariApi[i][k].soal;
      if (!teks.includes(`Soal ${soal + 1}`) || !teks.includes(`“${kalimat[soal]}”`) || !/menunjuk ke /.test(teks)) { alasanBenar = false; rinci = teks; }
    }
  }
  periksa("D alasan memakai kalimat jawabanmu sendiri (dikutip persis) dan nomor soalnya", alasanBenar, rinci);
  periksa("D soal yang dilewati (4) tidak pernah disebut sebagai alasan", !(await ruang(page).locator(".kc-alasan").allTextContents()).some((t) => /Soal 4\b/.test(t)));
  periksa("D tiap kartu menjelaskan apa profesi itu (kalimat ringkas)", (await Promise.all([0, 1, 2].map((i) => kartu.nth(i).locator(".kc-ringkas").textContent()))).every((t) => t.length > 30));
  periksa("D ada catatan bahwa urutan bukan penilaian kemampuan", rapat(await ruang(page).locator(".kc-hasil > .kr-catatan").textContent()).includes("bukan penilaian kemampuanmu"));
  periksa("D tanpa teks undefined, NaN, [object Object], null", !/undefined|NaN|\[object Object\]|\bnull\b/.test(await ruang(page).textContent()));
  // `.kr-juara li` dulu berlaku untuk SEMUA li turunan: baris alasan di dalam kartu ikut menjadi
  // kotak bertepi, dan yang pertama bertepi kuning. Tidak satu pun pemeriksaan teks melihatnya.
  periksa("D baris alasan tidak mewarisi gaya kartu juara (tanpa garis tepi, bukan flex)",
    await page.evaluate(() => { const l = [...document.querySelectorAll("#kr-cocok .kc-alasan li")];
      return l.length > 0 && l.every((x) => { const c = getComputedStyle(x); return c.borderTopWidth === "0px" && c.display !== "flex"; }); }));
  await foto(page, "D-hasil");

  // Lihat profesi: memilih di peta DAN membawa orangnya ke panelnya
  await kartu.nth(1).getByRole("button", { name: "Lihat profesi" }).click();
  await page.waitForTimeout(400);
  const panel = await page.evaluate(() => { const el = document.getElementById("kr-panel"); const r = el.getBoundingClientRect(); return { atas: r.top, bawah: r.bottom, teks: el.textContent }; });
  periksa("D 'Lihat profesi' menggulir panelnya ke layar", panel.atas > 60 && panel.atas < 400 && panel.bawah > 100, JSON.stringify({ atas: panel.atas | 0, bawah: panel.bawah | 0 }));
  periksa("D panel memuat profesi yang dipilih", panel.teks.includes(nama[1].replace(/ \(.*\)$/, "")), nama[1]);

  // Jadikan tujuanku: keputusan orangnya; ditulis ke profil uji lalu dibatalkan
  await page.evaluate(() => document.getElementById("kr-cocok").scrollIntoView({ block: "start" }));
  const t0 = kartu.nth(0).locator(".kr-tujuan");
  await t0.click(); await page.waitForTimeout(400);
  periksa("D 'Jadikan tujuanku' berubah jadi 'Tujuanmu' (aria-pressed)", (await t0.getAttribute("aria-pressed")) === "true" && /Tujuanmu/.test(await t0.textContent()));
  await t0.click(); await page.waitForTimeout(400);
  periksa("D dibatalkan lagi (profil uji kembali bersih)", (await t0.getAttribute("aria-pressed")) === "false");

  // Ubah jawaban: kembali ke soal dengan jawaban utuh, hasil dan alasan mengikuti jawaban baru
  await page.evaluate(() => document.getElementById("kr-cocok").scrollIntoView({ block: "start" }));
  await ruang(page).getByRole("button", { name: "Ubah jawaban" }).click();
  await page.waitForTimeout(200);
  periksa("D Ubah jawaban membuka soal lagi dengan jawaban yang tersimpan",
    (await page.locator("#kr-cocok input[type=radio]:checked").count()) === 1 && (await ruang(page).locator(".kc-hitung").count()) === 1);
  await page.locator("#kr-cocok .kc-baris").nth(0).click();
  const labelBaru = (await opsi(page).nth(3).locator(".kc-label").textContent()).trim();
  await opsi(page).nth(3).click();
  await ruang(page).locator(".kc-rel").getByRole("button", { name: "Lihat yang cocok" }).click();
  await page.waitForSelector("#kr-cocok .kc-hasil"); await page.waitForTimeout(250);
  const server2 = await api(page, "karier/kuis?pilihan=3,1,2,,1,0");
  const nama2 = await Promise.all([0, 1, 2].map(async (i) => (await kartu.nth(i).locator(".judul").textContent()).trim()));
  const baris1 = (await ruang(page).locator(".kc-alasan li").allTextContents()).filter((t) => /^Soal 1\b/.test(t.trim()));
  periksa("D jawaban yang diubah: hasil sama dengan server untuk jawaban baru",
    nama2.every((n, i) => n === profesi[server2.hasil[i].id]), nama2.join(" | "));
  periksa("D jawaban yang diubah: alasan soal 1 memakai kalimat BARU, tidak ada sisa yang lama",
    baris1.length >= 1 && baris1.every((t) => t.includes(`“${labelBaru}”`) && !t.includes(kalimat[0])), `${baris1.length} baris soal 1`);
  sehat(galat, "D");
  await page.context().close();
}

/* -------------------------------------------------- E kontras di empat tema */
for (const tema of ["gelap", "malam", "terang", "kontras"]) {
  const { page } = await buka({ tema });
  await opsi(page).nth(1).click();
  await tombol(page, "Lanjut").click();
  const ukur = {
    teksPilihan: await kontrasDi(page, "#kr-cocok .kr-pilihan:nth-child(1) .kc-label"),
    bantu: await kontrasDi(page, "#kr-cocok .kc-bantu"),
    hitung: await kontrasDi(page, "#kr-cocok .kc-hitung"),
    kosong: await kontrasDi(page, "#kr-cocok .kc-baris[data-kosong] .kc-teks"),
    isi: await kontrasDi(page, "#kr-cocok .kc-baris:not([data-kosong]) .kc-teks"),
    sisa: await kontrasDi(page, "#kr-cocok .kc-sisa"),
  };
  await opsi(page).nth(2).click();
  ukur.terpilih = await kontrasDi(page, "#kr-cocok .kr-pilihan:nth-child(3) .kc-label");
  ukur.centang = await kontrasDi(page, "#kr-cocok .kr-pilihan:nth-child(3) .kc-tanda");
  ukur.nomorTerpilih = await kontrasDi(page, "#kr-cocok .kr-pilihan:nth-child(3) .kc-nomor");
  const rendah = Object.entries(ukur).filter(([k, v]) => v === null || v < (k === "centang" ? 3 : 4.5));
  periksa(`E ${tema}: semua teks kuis >= 4,5:1 (centang >= 3:1)`, rendah.length === 0, JSON.stringify(ukur));
  await foto(page, `E-${tema}`);
  await page.context().close();
}

/* -------------------------------------------- F tata letak pada tiga ukuran desktop */
for (const [lebar, tinggi] of [[1280, 800], [1440, 900], [1600, 1000]]) {
  const { page } = await buka({ lebar, tinggi });
  await opsi(page).nth(0).click(); await tombol(page, "Lanjut").click();
  await opsi(page).nth(1).click(); await tombol(page, "Lanjut").click();
  await opsi(page).nth(2).click();
  const m = await page.evaluate(() => {
    const u = document.querySelector(".kc-utama").getBoundingClientRect(), r = document.querySelector(".kc-rel").getBoundingClientRect();
    const s = document.getElementById("kr-cocok");
    return { lebarU: u.width, lebarR: r.width, berdampingan: r.left >= u.right - 0.5,
      tumpuk: !(u.right <= r.left + 0.5 || r.right <= u.left + 0.5 || u.bottom <= r.top || r.bottom <= u.top),
      luber: document.documentElement.scrollWidth > document.documentElement.clientWidth, sc: s.scrollWidth > s.clientWidth };
  });
  periksa(`F ${lebar}x${tinggi}: soal dan daftar jawaban berdampingan, tidak bertumpuk, tidak meluber`,
    m.berdampingan && !m.tumpuk && !m.luber && !m.sc && m.lebarU > 480 && m.lebarR > 240, JSON.stringify({ u: m.lebarU | 0, r: m.lebarR | 0, kanan: m.berdampingan }));
  await page.context().close();
}

/* ---------------------------------------------------- G SIM server gagal */
{
  const { page } = await buka({ simulasi: (p) => p.route("**/api/karier/kuis*", (r) =>
    r.fulfill({ status: 500, contentType: "application/json", body: JSON.stringify({ galat: "uji" }) })) });
  for (let i = 0; i < 3; i++) { await opsi(page).nth(0).click(); if (i < 2) await tombol(page, "Lanjut").click(); }
  await ruang(page).locator(".kc-rel").getByRole("button", { name: "Lihat yang cocok" }).click();
  await page.waitForTimeout(500);
  periksa("G SIM: server gagal tidak mengosongkan kuis, orangnya tetap di soal dan jawabannya utuh",
    (await ruang(page).locator(".kc-hitung").count()) === 1 && (await ruang(page).locator(".kc-hasil").count()) === 0 &&
    (await ruang(page).locator(".kc-baris:not([data-kosong])").count()) === 3);
  periksa("G SIM: kegagalan diberi tahu lewat toast", /Gagal memuat hasil kuis/.test(await page.locator("body").textContent()));
  await page.context().close();
}

/* ------------------------------------- H SIM server lama tanpa medan `dari` */
{
  const { page, galat } = await buka({ simulasi: (p) => p.route("**/api/karier/kuis*", async (r) => {
    const res = await r.fetch(); const j = await res.json();
    j.hasil.forEach((h) => { delete h.dari; });
    await r.fulfill({ response: res, json: j });
  }) });
  for (let i = 0; i < 3; i++) { await opsi(page).nth(1).click(); if (i < 2) await tombol(page, "Lanjut").click(); }
  await ruang(page).locator(".kc-rel").getByRole("button", { name: "Lihat yang cocok" }).click();
  await page.waitForSelector("#kr-cocok .kc-hasil"); await page.waitForTimeout(250);
  periksa("H SIM: tanpa `dari` hasil tetap terbaca (cadangan 'Cocok karena')",
    (await ruang(page).locator(".kr-juara .ket").count()) === 3 && /^Cocok karena: /.test(await ruang(page).locator(".kr-juara .ket").first().textContent()));
  sehat(galat, "H");
  await page.context().close();
}

/* ------------------------------------------------ I fokus tidak jatuh ke body */
{
  const { page } = await buka();
  const hasil = [];
  await opsi(page).nth(0).click(); await tombol(page, "Lanjut").click(); hasil.push(await fokusTag(page));
  await page.locator("#kr-cocok .kc-baris").nth(4).click(); hasil.push(await fokusTag(page));
  await tombol(page, "Kembali").click(); hasil.push(await fokusTag(page));
  periksa("I fokus mendarat di judul soal sesudah Lanjut, lompat, dan Kembali", hasil.every((t) => t.startsWith("LEGEND:")), hasil.join(" | "));
  await page.context().close();
}

await browser.close();
console.log(gagal === 0 ? "\nSEMUA PEMERIKSAAN LULUS" : `\n${gagal} PEMERIKSAAN GAGAL`);
process.exit(gagal === 0 ? 0 : 1);
