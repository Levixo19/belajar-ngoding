/* Pembaca materi "lembar baca": prosa lebih sempit dari pelat kode, H1 tidak lagi 66 px, header
 * tidak mengulang bab dan posisi, dan tautan Ruang Coba membuka kode yang benar.
 *
 * Latar (hasil debat 17 agen, 2026-10-29): baris prosa dulu 99 karakter karena `72ch` mengukur angka
 * nol (791 px), dan `.kepala-besar h1` (66 px) mengalahkan `.kepala-materi h1` (41 px) hanya oleh urutan
 * CSS. Pemilik membaca di tema TERANG, jadi tema itu diukur lebih dulu.
 *
 *   BELAJAR_URL=http://127.0.0.1:7795/ node uji/manual/lembar-baca.mjs
 *
 * Hanya GET, terhadap server berprofil SEMENTARA dengan `buka_semua_bab` (lihat `lib.mjs`); menolak 7777.
 */

import { URL_DASAR, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Lembar baca");
const dekat = (a, b, t = 1) => Math.abs(a - b) <= t;

for (const [lebar, tinggi, tema] of [[1440, 900, "terang"], [1920, 1080, "terang"], [1440, 900, "gelap"], [1440, 900, "kontras"]]) {
  const s = await mulai({ lebar, tinggi, tema, gerak: "mati", hash: "#/materi/html/1", tunggu: ".materi-tata" });
  await s.page.waitForTimeout(700);
  const r = await s.page.evaluate(() => {
    const k = (q) => { const e = document.querySelector(q); if (!e) return null; const b = e.getBoundingClientRect(); return { kiri: b.left, w: b.width, atas: b.top }; };
    const par = document.querySelector(".prosa > section > .par");
    return {
      h1: parseFloat(getComputedStyle(document.querySelector(".kepala-materi h1")).fontSize),
      par: k(".prosa > section > .par"), kode: k(".blok-kode"), h1kotak: k(".kepala-materi h1"),
      label: !!document.querySelector(".kepala-materi .mata"), pil: document.querySelectorAll(".kepala-materi .pil").length,
      meluber: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      meta: document.querySelector(".kepala-meta")?.textContent ?? null,
    };
  });
  const pelat = await s.page.evaluate(() => {
    const kode = document.querySelector(".blok-kode .kode");
    if (!kode) return null;
    const baca = (c) => { const m = c.match(/[\d.]+/g)?.map(Number) ?? []; if (c.startsWith("color(")) return { r: m[1] * 255, g: m[2] * 255, b: m[3] * 255, a: m[4] ?? 1 }; return { r: m[0], g: m[1], b: m[2], a: m[3] ?? 1 }; };
    const lum = (c) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
    let e = kode, latar = null;
    while (e) { const c = baca(getComputedStyle(e).backgroundColor); if (c.a > 0.95) { latar = c; break; } e = e.parentElement; }
    const teks = baca(getComputedStyle(kode).color);
    const kontras = latar ? (Math.max(lum(latar), lum(teks)) + 0.05) / (Math.min(lum(latar), lum(teks)) + 0.05) : null;
    return { lumLatar: latar ? lum(latar) : null, kontras };
  });
  const n = `${lebar}px ${tema}`;
  P.cek(`${n}: H1 materi tidak lebih besar dari 45 px (dulu 66 dan 74)`, r.h1 <= 45.5, r.h1);
  P.cek(`${n}: prosa 560 sampai 620 px (sekitar 75 karakter), bukan selebar pelat`, !!r.par && r.par.w >= 560 && r.par.w <= 620, r.par);
  P.cek(`${n}: blok kode tetap selebar pelat penuh, sedikitnya 150 px lebih lebar dari prosa`, !!r.kode && !!r.par && r.kode.w >= r.par.w + 150, { kode: r.kode, par: r.par });
  P.cek(`${n}: H1, prosa, dan kode berbagi tepi kiri yang sama`, !!r.par && !!r.kode && dekat(r.h1kotak.kiri, r.par.kiri) && dekat(r.kode.kiri, r.par.kiri), { h1: r.h1kotak.kiri, par: r.par?.kiri, kode: r.kode?.kiri });
  P.cek(`${n}: label bab hilang dan hanya satu pil (tingkat) di kepala`, !r.label && r.pil === 1, { label: r.label, pil: r.pil });
  P.cek(`${n}: halaman tidak meluber ke samping`, r.meluber <= 0, r.meluber);
  P.cek(`${n}: baris meta "sekitar N menit" ada di kepala`, /^sekitar \d+ menit/.test(r.meta ?? ""), r.meta);
  P.cek(`${n}: pelat kode gelap (luminans latar di bawah 0,1), juga di tema terang`, !!pelat && pelat.lumLatar < 0.1, pelat);
  P.cek(`${n}: teks kode terbaca di pelat (kontras 4,5:1 atau lebih)`, !!pelat && pelat.kontras >= 4.5, pelat);
  if (lebar === 1440 && tema === "terang") {
    P.cek(`${n}: paragraf pertama dimulai di atas y=470 (dulu sekitar 513 sampai 531)`, r.par.atas < 470, r.par.atas);
  }
  await s.tutup();
}

/* Ruang Coba: kode yang dibuka tautan blok HARUS kode blok itu. Bagian yang berisi prosa dan kode
 * dipecah jadi dua blok, jadi indeks blok bergeser dari indeks data (dulu 807 dari 2.757 blok salah). */
const s = await mulai({ lebar: 1440, tinggi: 900, tema: "terang", gerak: "mati", hash: "#/materi/css/23", tunggu: ".materi-tata" });
await s.page.waitForTimeout(700);
const rc = await s.page.evaluate(async () => {
  const token = window.TOKEN_BELAJAR ?? "";
  const norm = (t) => (t || "").replace(/\s+/g, " ").trim();
  const hasil = [];
  for (const a of document.querySelectorAll("a")) {
    const q = new URLSearchParams((a.getAttribute("href") || "").split("?")[1] || "");
    if (a.textContent.trim() !== "Ruang Coba" || !q.has("bagian")) continue;
    const tampil = norm(a.closest(".blok-kode")?.querySelector(".kode")?.textContent);
    const j = await (await fetch(`/api/materi/contoh?key=css&indeks=23&bagian=${q.get("bagian")}`, { headers: { "X-Belajar-Token": token } })).json().catch(() => ({}));
    hasil.push({ bagian: q.get("bagian"), cocok: !!j.kode && norm(j.kode) === tampil });
  }
  return hasil;
});
P.cek("CSS materi 24 (bagian campur): ada tautan Ruang Coba pada blok kode", rc.length >= 2, rc);
P.cek("CSS materi 24: SETIAP tautan Ruang Coba membuka kode yang sama dengan yang tampil di blok", rc.length > 0 && rc.every((x) => x.cocok), rc);
await s.tutup();

/* "Cara memecahkannya" terlipat: tombol asli, isi disembunyikan sampai dibuka, dan satu klik membukanya. */
{
  const t = await mulai({ lebar: 1440, tinggi: 900, tema: "terang", gerak: "mati", hash: "#/materi/html/1", tunggu: ".materi-tata" });
  await t.page.waitForTimeout(700);
  const sebelum = await t.page.evaluate(() => {
    const tb = document.querySelector(".pecahkan-tombol"), isi = document.querySelector(".pecahkan-isi");
    return tb && isi ? { expanded: tb.getAttribute("aria-expanded"), hidden: isi.hidden, tampak: isi.offsetParent !== null, kontrol: tb.getAttribute("aria-controls") === isi.id, teks: tb.textContent } : null;
  });
  P.cek("pecahkan: tombol ada, tertutup, dan isinya tak terlihat", !!sebelum && sebelum.expanded === "false" && sebelum.hidden && !sebelum.tampak && sebelum.kontrol, sebelum);
  await t.page.click(".pecahkan-tombol");
  await t.page.waitForTimeout(150);
  const sesudah = await t.page.evaluate(() => {
    const tb = document.querySelector(".pecahkan-tombol"), isi = document.querySelector(".pecahkan-isi");
    return { expanded: tb.getAttribute("aria-expanded"), tampak: isi.offsetParent !== null, tinggi: isi.getBoundingClientRect().height };
  });
  P.cek("pecahkan: klik membuka isinya", sesudah.expanded === "true" && sesudah.tampak && sesudah.tinggi > 20, sesudah);
  const cetak = await t.page.evaluate(() => { const isi = document.querySelector(".pecahkan-isi"); isi.hidden = true; const d = getComputedStyle(isi).display; return d; });
  P.cek("pecahkan: atribut hidden memang menyembunyikan (dasar aturan cetak)", cetak === "none", cetak);
  await t.page.emulateMedia({ media: "print" });
  const dicetak = await t.page.evaluate(() => getComputedStyle(document.querySelector(".pecahkan-isi")).display);
  await t.page.emulateMedia({ media: "screen" });
  P.cek("pecahkan: saat dicetak isinya dipaksa terlihat walau tertutup", dicetak === "block", dicetak);
  await t.tutup();
}

/* Rel kiri: butir materi hanya untuk bab aktif; bab lain dibuka satu klik dan bisa ditutup lagi. */
{
  const t = await mulai({ lebar: 1440, tinggi: 900, tema: "terang", gerak: "mati", hash: "#/materi/html/1", tunggu: ".materi-tata" });
  await t.page.waitForTimeout(700);
  const hitung = () => t.page.evaluate(() => {
    const tombol = [...document.querySelectorAll(".materi-rel-bab-tombol")];
    const butir = [...document.querySelectorAll(".materi-rel li")];
    return { bab: tombol.length, expanded: tombol.map((b) => b.getAttribute("aria-expanded")), tampak: butir.filter((li) => li.offsetParent !== null).length, total: butir.length };
  });
  const a = await hitung();
  P.cek("rel: ada beberapa bab dengan tombol, tepat satu terbuka", a.bab >= 3 && a.expanded.filter((x) => x === "true").length === 1, a);
  P.cek("rel: butir bab yang tertutup tidak tampak (jauh lebih sedikit dari total)", a.tampak < a.total / 2 && a.tampak >= 2, a);
  const tutup = await t.page.evaluate(() => [...document.querySelectorAll(".materi-rel-bab-tombol")].findIndex((b) => b.getAttribute("aria-expanded") === "false"));
  await t.page.locator(".materi-rel-bab-tombol").nth(tutup).click();
  await t.page.waitForTimeout(150);
  const b = await hitung();
  P.cek("rel: klik bab tertutup menambah butir yang tampak", b.tampak > a.tampak && b.expanded[tutup] === "true", { a, b });
  await t.page.locator(".materi-rel-bab-tombol").nth(tutup).click();
  await t.page.waitForTimeout(150);
  const c = await hitung();
  P.cek("rel: klik lagi menutupnya kembali", c.tampak === a.tampak && c.expanded[tutup] === "false", { a, c });
  await t.page.locator(".materi-rel-bab-tombol").nth(tutup).focus();
  await t.page.keyboard.press("Enter");
  await t.page.waitForTimeout(150);
  const d = await hitung();
  P.cek("rel: Enter pada tombol bab juga membuka (papan ketik)", d.tampak > a.tampak, { a, d });
  await t.tutup();
}

/* Callout bersimbol: Jebakan bersegitiga, Aturan bersiku. Dicari di beberapa materi karena tidak semua punya. */
{
  const t = await mulai({ lebar: 1440, tinggi: 900, tema: "terang", gerak: "mati", hash: "#/materi/html/1", tunggu: ".materi-tata" });
  let ketemu = { jebakan: null, aturan: null };
  for (let n = 1; n <= 12 && (!ketemu.jebakan || !ketemu.aturan); n++) {
    await t.page.evaluate((x) => { location.hash = `#/materi/html/${x}`; }, n);
    await t.page.waitForSelector(".materi-tata", { timeout: 8000 }).catch(() => {});
    await t.page.waitForTimeout(500);
    const r = await t.page.evaluate(() => {
      const ukur = (q) => { const e = document.querySelector(q); if (!e) return null; const b = getComputedStyle(e, "::before"); return { isi: b.content, lebar: b.width, kiri: parseFloat(getComputedStyle(e).paddingLeft) / parseFloat(getComputedStyle(document.documentElement).fontSize) }; };
      return { jebakan: ukur(".prosa .peran-jebakan"), aturan: ukur(".prosa .peran-aturan") };
    });
    ketemu = { jebakan: ketemu.jebakan ?? r.jebakan, aturan: ketemu.aturan ?? r.aturan };
  }
  P.cek("callout Jebakan: simbol ::before tergambar dan teks digeser memberi tempat", !!ketemu.jebakan && ketemu.jebakan.isi !== "none" && parseFloat(ketemu.jebakan.lebar) > 8 && ketemu.jebakan.kiri >= 2.5, ketemu.jebakan);
  P.cek("callout Aturan: simbol ::before tergambar dan teks digeser memberi tempat", !!ketemu.aturan && ketemu.aturan.isi !== "none" && parseFloat(ketemu.aturan.lebar) > 8 && ketemu.aturan.kiri >= 2.5, ketemu.aturan);
  await t.tutup();
}

P.selesai();
