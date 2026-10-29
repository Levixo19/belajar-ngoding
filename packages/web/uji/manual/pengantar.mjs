/* Pemeriksaan layar Pengantar (`#/pengantar`) di peramban. Yang diukur adalah
 * perilaku, bukan sumbernya: hero memakan roda dan tombol hanya selama tertutup,
 * papan ketik punya jalan sendiri, tiga tingkat gerak selain "penuh" tidak
 * dibajak, isi tidak bisa difokuskan sebelum terbuka, angka di isi sama dengan
 * `/api/awal`, dan teks terang di atas gambar terukur kontrasnya.
 *
 *   BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/pengantar.mjs
 *
 * Jalankan terhadap server berprofil SEMENTARA (lihat `lib.mjs`). Skrip ini
 * hanya membaca; permintaan tulis dicegat `lib.mjs` dan dihitung sebagai gagal.
 */

import { URL_DASAR, lum, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Layar Pengantar");
const JUDUL = "Belajar coding, bintang demi bintang";

const keadaan = (page) => page.evaluate(() => {
  const h = document.querySelector(".hg");
  const pel = document.querySelector(".hg-pelat").getBoundingClientRect();
  const m = document.querySelector(".hg-media").getBoundingClientRect();
  return {
    p: parseFloat(getComputedStyle(h).getPropertyValue("--hg-p")),
    buka: h.dataset.terbuka, y: Math.round(scrollY),
    medW: m.width, medH: m.height, pelW: pel.width, pelH: pel.height,
    isi: !!document.querySelector(".hg-isi"),
    petunjuk: !!document.querySelector(".hg-petunjuk"),
    lewati: !!document.querySelector(".hg-lewati"),
  };
});
const buka = (opsi = {}) => mulai({
  lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/pengantar", tunggu: ".hg-pelat", ...opsi,
});
const dekat = (a, b, t) => Math.abs(a - b) <= t;
const tunggu = (page, ms) => page.waitForTimeout(ms);
// Hero menyusul targetnya per bingkai animasi, jadi "tunggu 1,1 detik" rapuh di mesin yang sedang sibuk (p baru 0,9986
// pada ambang 0,999). Yang ditunggu KONDISINYA: `--hg-p` tiba di sekitar nilai yang dituju. Kegagalannya dibiarkan
// jatuh ke pemeriksaan sesudahnya, yang melaporkannya dengan angka.
const tungguP = async (page, nilai, tol = 0.0005, ms = 6000) => {
  await page.waitForFunction(([n, t]) => Math.abs(parseFloat(getComputedStyle(document.querySelector(".hg")).getPropertyValue("--hg-p")) - n) <= t, [nilai, tol], { timeout: ms }).catch(() => {});
  await page.waitForTimeout(150);
};
// `HANYA=A,B` menjalankan bagian tertentu saja (dipakai baterai mutan supaya tiap mutan murah).
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
// Pusat mendatar teks kedua baris judul. Diukur dari teksnya (Range), bukan dari <span> blok yang selebar kolom.
const pusat = (page) => page.evaluate(() => {
  const c = (s) => { const r = document.createRange(); r.selectNodeContents(document.querySelector(s)); const b = r.getBoundingClientRect(); return b.x + b.width / 2; };
  return [c(".hg-kiri"), c(".hg-kanan")];
});

/* ------------------------------------------------ A keadaan awal (gerak penuh) */
if (jalan("A")) {
  const s = await buka(); const page = s.page;
  const k = await keadaan(page);
  P.cek("A tertutup di awal: p = 0, tanpa isi, dengan petunjuk dan tombol Lewati",
    k.p === 0 && k.buka === "false" && !k.isi && k.petunjuk && k.lewati, k);
  P.cek("A media kecil di awal (18rem = 288 px) dan lebih pendek dari pelatnya", dekat(k.medW, 288, 2) && k.medH < k.pelH, { medW: k.medW, medH: k.medH, pelH: k.pelH });
  const latar0 = await page.evaluate(() => getComputedStyle(document.querySelector(".hg-latar")).opacity);
  P.cek("A latar tampak penuh di awal (opacity 1)", latar0 === "1", latar0);
  const [ck0, cn0] = await pusat(page);
  P.cek("A kedua baris judul sejajar di tengah selama tertutup", dekat(ck0, cn0, 3), { kiri: ck0, kanan: cn0 });
  const fokus = await page.evaluate(() => [...document.querySelectorAll(".hg a, .hg button, .hg [tabindex]")].map((e) => e.textContent.trim().slice(0, 24)));
  P.cek("A selama tertutup hanya tombol Lewati yang bisa difokuskan di dalam hero", fokus.length === 1 && fokus[0] === "Lewati pengantar", fokus);
  P.cek("A judul h1 utuh dan jadi judul tab", (await page.locator("h1").first().innerText()).replace(/\s+/g, " ").trim() === JUDUL && (await page.title()).includes(JUDUL), await page.title());
  const gb = await page.evaluate(() => [...document.querySelectorAll(".hg-latar, .hg-media img")].map((i) => ({ ok: i.complete && i.naturalWidth > 0, alt: i.getAttribute("alt") })));
  P.cek("A kedua gambar termuat; latar dekoratif (alt kosong), media beralt", gb.length === 2 && gb.every((g) => g.ok) && gb[0].alt === "" && /Rasi Python/.test(gb[1].alt ?? ""), gb);
  const tipe = await page.evaluate(async () => (await fetch("/gambar/pengantar-peta.jpg")).headers.get("content-type"));
  P.cek("A gambar disajikan server sebagai image/jpeg", tipe === "image/jpeg", tipe);
  P.cek("A tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

/* ------------------------------------------------ B roda membuka, C lalu menggulir */
if (jalan("B")) {
  const s = await buka(); const page = s.page;
  await page.mouse.move(700, 450);
  const deret = [];
  for (let i = 0; i < 3; i++) { await page.mouse.wheel(0, 300); await tungguP(page, (300 / 1100) * (i + 1), 0.01); deret.push((await keadaan(page)).p); }
  const k3 = await keadaan(page);
  P.cek("B roda menggeser p naik terus tanpa menggulir halaman (900 px roda, hero belum terbuka)",
    deret[0] > 0.15 && deret[1] > deret[0] && deret[2] > deret[1] && deret[2] < 1 && k3.y === 0, { deret, y: k3.y });
  await page.mouse.wheel(0, 400); await tungguP(page, 1);
  const k = await keadaan(page);
  P.cek("B sesudah 1.300 px roda hero terbuka: p = 1, isi ada, petunjuk dan Lewati hilang",
    k.p === 1 && k.buka === "true" && k.isi && !k.petunjuk && !k.lewati, k);
  P.cek("B terbuka penuh: media memenuhi pelatnya", dekat(k.medW, k.pelW, 2) && dekat(k.medH, k.pelH, 2), { medW: k.medW, pelW: k.pelW, medH: k.medH, pelH: k.pelH });
  const latar = await page.evaluate(() => getComputedStyle(document.querySelector(".hg-latar")).opacity);
  P.cek("B latar memudar sepenuhnya saat terbuka (opacity 0)", latar === "0", latar);
  const [ck1, cn1] = await pusat(page);
  P.cek("B judul terbelah: baris pertama bergeser ke kiri, kedua ke kanan (selisih pusat > 300 px)", cn1 - ck1 > 300, { kiri: ck1, kanan: cn1 });
  await page.mouse.wheel(0, 500); await tunggu(page, 600);
  const g = await keadaan(page);
  P.cek("C sesudah terbuka, roda menggulir halaman seperti biasa", g.y >= 300 && g.buka === "true", { y: g.y });

  // D inersia: gulir naik yang baru berhenti tidak ikut menutup hero.
  await page.evaluate(() => window.scrollTo(0, 0));
  await tunggu(page, 60);
  await page.mouse.wheel(0, -200); await tunggu(page, 500);
  const i1 = await keadaan(page);
  P.cek("D gulir naik berinersia yang baru tiba di puncak TIDAK menutup hero", i1.buka === "true" && i1.p === 1 && i1.isi, i1);
  await tunggu(page, 500);
  await page.mouse.wheel(0, -300); await tunggu(page, 900);
  const i2 = await keadaan(page);
  P.cek("D sesudah diam di puncak, gulir naik menutup hero lagi (isi dilepas)", i2.p < 1 && i2.p > 0.5 && !i2.isi && i2.petunjuk, i2);
  P.cek("B-D tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

/* ------------------------------------------------ E papan ketik, F tidak mencuri tombol */
if (jalan("E")) {
  const s = await buka(); const page = s.page;
  await page.keyboard.press("Space"); await tunggu(page, 700);
  const a = await keadaan(page);
  P.cek("E satu Spasi memajukan p sekitar 0,34", dekat(a.p, 0.34, 0.03) && a.buka === "false", a);
  await page.keyboard.press("Space"); await page.keyboard.press("Space"); await tungguP(page, 1);
  const b = await keadaan(page);
  P.cek("E tiga Spasi membuka hero", b.p === 1 && b.isi, b);
  await tunggu(page, 450);
  await page.keyboard.press("Home"); await tungguP(page, 0);
  const c = await keadaan(page);
  P.cek("E Home di puncak yang diam menutup hero seluruhnya", c.p === 0 && !c.isi, c);
  await page.keyboard.press("End"); await tungguP(page, 1);
  P.cek("E End membuka hero seluruhnya", (await keadaan(page)).p === 1);
  await tunggu(page, 450);
  await page.keyboard.press("Shift+Space"); await tungguP(page, 0.66, 0.002);
  const d = await keadaan(page);
  P.cek("E Shift+Spasi di puncak yang diam memundurkan satu langkah", dekat(d.p, 0.66, 0.03) && !d.isi, d);
  await page.keyboard.press("Home"); await tungguP(page, 0);
  await page.evaluate(() => { const i = document.createElement("input"); i.id = "uji-isian"; document.body.appendChild(i); i.focus(); });
  await page.keyboard.press("Space"); await tunggu(page, 500);
  const e = await keadaan(page);
  P.cek("F Spasi di dalam kotak isian tidak dicuri hero (p tetap 0)", e.p === 0, e);
  await page.evaluate(() => { document.getElementById("uji-isian")?.remove(); document.body.focus(); });
  await s.tutup();
}

/* ------------------------------------------------ G tombol Lewati */
if (jalan("G")) {
  const s = await buka(); const page = s.page;
  await page.locator(".hg-lewati").click(); await tunggu(page, 1100);
  const k = await keadaan(page);
  const fokus = await page.evaluate(() => document.activeElement?.className ?? "");
  P.cek("G Lewati membuka hero seketika, memindahkan fokus ke isi, dan menggulirnya terlihat",
    k.p === 1 && k.isi && !k.lewati && String(fokus).includes("hg-isi") && k.y > 100, { ...k, fokus });
  await s.tutup();
}

/* ------------------------------------------------ H selain gerak penuh: tidak dibajak */
if (jalan("H")) for (const [nama, o] of [["halus", { gerak: "halus" }], ["mati", { gerak: "mati" }], ["prefers-reduced-motion", { reduce: true, gerak: "penuh" }]]) {
  const s = await buka(o); const page = s.page;
  await tunggu(page, 300);
  const k = await keadaan(page);
  P.cek(`H ${nama}: hero tampil SUDAH terbuka, tanpa petunjuk dan tanpa Lewati`, k.p === 1 && k.buka === "true" && k.isi && !k.petunjuk && !k.lewati, k);
  const dicegah = await page.evaluate(() => {
    const w = new WheelEvent("wheel", { deltaY: 300, cancelable: true, bubbles: true });
    window.dispatchEvent(w);
    const t = new KeyboardEvent("keydown", { key: " ", cancelable: true, bubbles: true });
    document.body.dispatchEvent(t);
    return [w.defaultPrevented, t.defaultPrevented];
  });
  P.cek(`H ${nama}: roda dan Spasi tidak dicegah (gulir tetap milik halaman)`, dicegah[0] === false && dicegah[1] === false, dicegah);
  // Naik di puncak yang sudah diam MENUTUP hero pada gerak penuh; di sini ia tidak boleh dibajak.
  await tunggu(page, 450);
  const naik = await page.evaluate(() => {
    const w = new WheelEvent("wheel", { deltaY: -120, cancelable: true, bubbles: true });
    window.dispatchEvent(w);
    return w.defaultPrevented;
  });
  await tunggu(page, 600);
  const sesudah = await keadaan(page);
  P.cek(`H ${nama}: gulir naik di puncak tidak menutup hero`, naik === false && sesudah.p === 1 && sesudah.isi, { naik, p: sesudah.p });
  await page.mouse.move(700, 450); await page.mouse.wheel(0, 500); await tunggu(page, 600);
  P.cek(`H ${nama}: roda sungguhan menggulir halaman`, (await keadaan(page)).y >= 300);
  await s.tutup();
}
if (jalan("H")) {
  // Pada gerak penuh yang masih tertutup, hero MEMAKAN keduanya (kebalikan H).
  const s = await buka(); const page = s.page;
  const dicegah = await page.evaluate(() => {
    const w = new WheelEvent("wheel", { deltaY: 100, cancelable: true, bubbles: true });
    window.dispatchEvent(w);
    const t = new KeyboardEvent("keydown", { key: "ArrowDown", cancelable: true, bubbles: true });
    document.body.dispatchEvent(t);
    return [w.defaultPrevented, t.defaultPrevented];
  });
  P.cek("H gerak penuh tertutup: roda dan panah bawah dimakan hero", dicegah[0] === true && dicegah[1] === true, dicegah);
  await s.tutup();
}

/* ------------------------------------------------ I kontras teks di atas gambar */
// Warna teks dibaca dari gaya SUNGGUHAN (bukan diketik di sini): mutan yang mengganti warna
// tombol Lewati dengan warna tema dulu lolos karena rasio dihitung terhadap konstanta.
const bacaWarna = (c) => {
  const n = c.match(/[\d.]+/g).slice(0, 3).map(Number);
  return c.startsWith("color(") ? n.map((v) => v * 255) : n; // `color(srgb ...)` berkomponen 0..1
};
async function bgTerangPersentil(page, kotak, persen) {
  const png = await page.screenshot({ clip: kotak, type: "png" });
  return page.evaluate(async ([b64, pr]) => {
    const im = new Image(); im.src = "data:image/png;base64," + b64; await im.decode();
    const c = document.createElement("canvas"); c.width = im.width; c.height = im.height;
    const x = c.getContext("2d", { willReadFrequently: true }); x.drawImage(im, 0, 0);
    const d = x.getImageData(0, 0, c.width, c.height).data;
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    const L = [];
    for (let i = 0; i < d.length; i += 4) L.push(0.2126 * f(d[i]) + 0.7152 * f(d[i + 1]) + 0.0722 * f(d[i + 2]));
    L.sort((a, b) => a - b);
    return L[Math.min(L.length - 1, Math.floor((L.length * pr) / 100))];
  }, [png.toString("base64"), persen]);
}
if (jalan("I")) for (const tema of ["gelap", "terang"]) {
  const s = await buka({ tema }); const page = s.page;
  const warna = await page.evaluate(() => {
    const w = (sel) => getComputedStyle(document.querySelector(sel)).color;
    return { judul: w(".hg-kiri"), petunjuk: w(".hg-petunjuk"), lewati: w(".hg-lewati") };
  });
  const TEKS = { judul: bacaWarna(warna.judul), petunjuk: bacaWarna(warna.petunjuk), lewati: bacaWarna(warna.lewati) };
  await page.addStyleTag({ content: ".hg-judul, .hg-petunjuk, .hg-lewati, .hg-lewati * { color: transparent !important; text-shadow: none !important; }" });
  const terburuk = { judul: 99, petunjuk: 99, lewati: 99 };
  for (const p of [0, 0.5, 1]) {
    await page.evaluate((v) => document.querySelector(".hg").style.setProperty("--hg-p", String(v)), p);
    await tunggu(page, 150);
    const kotak = await page.evaluate(() => {
      const teks = (el) => { const r = document.createRange(); r.selectNodeContents(el); const b = r.getBoundingClientRect(); return { x: b.x, y: b.y, width: b.width, height: b.height }; };
      return {
        kiri: teks(document.querySelector(".hg-kiri")), kanan: teks(document.querySelector(".hg-kanan")),
        // Tombol diukur di bawah HURUFNYA, bukan seluruh kotak: garis tepinya yang terang
        // (rgba terang) ikut terbaca sebagai "latar" dan menurunkan rasio tanpa menyentuh teks.
        petunjuk: teks(document.querySelector(".hg-petunjuk")), lewati: teks(document.querySelector(".hg-lewati")),
      };
    });
    for (const [jenis, kot] of [["judul", kotak.kiri], ["judul", kotak.kanan], ["petunjuk", kotak.petunjuk], ["lewati", kotak.lewati]]) {
      const L = await bgTerangPersentil(page, kot, 99);
      const r = (lum(TEKS[jenis]) + 0.05) / (L + 0.05);
      terburuk[jenis] = Math.min(terburuk[jenis], r);
    }
  }
  const hasil = Object.fromEntries(Object.entries(terburuk).map(([k, v]) => [k, Math.round(v * 100) / 100]));
  P.cek(`I ${tema}: teks terang di atas gambar >= 4,5:1 pada p = 0, 0,5, dan 1 (persentil ke-99 latar)`, Object.values(terburuk).every((v) => v >= 4.5), hasil);
  const pelat = await page.evaluate(() => getComputedStyle(document.querySelector(".hg-pelat")).backgroundColor);
  P.cek(`I ${tema}: pelat tetap gelap di tema ini`, pelat === "rgb(7, 11, 24)", pelat);
  await s.tutup();
}

/* ------------------------------------------------ J isi sama dengan API, K tautan dari layar mulai */
if (jalan("J")) {
  const s = await buka({ gerak: "mati" }); const page = s.page;
  const fakta = await page.evaluate(async () => {
    const aw = await (await fetch("/api/awal", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR } })).json();
    const t = aw.bahasa.reduce((a, b) => ({ m: a.m + b.materi, k: a.k + b.kuis, l: a.l + b.latihan }), { m: 0, k: 0, l: 0 });
    const f = (n) => n.toLocaleString("id-ID");
    return {
      harap: `${f(aw.bahasa.length)} kurikulum, ${f(t.m)} materi, ${f(t.k)} kuis, dan ${f(t.l)} latihan`,
      teks: document.querySelector(".pengantar .sambut-sub").textContent.replace(/\s+/g, " "),
      rusak: /undefined|NaN|\[object Object\]|\bnull\b/.test(document.querySelector(".hg-isi").textContent),
      tautan: [...document.querySelectorAll(".pengantar-pintu a, .pengantar-aksi a")].map((a) => a.getAttribute("href")),
    };
  });
  P.cek("J angka di isi dihitung dari /api/awal, bukan diketik", fakta.teks.includes(fakta.harap), { harap: fakta.harap, teks: fakta.teks.slice(0, 90) });
  P.cek("J isi tanpa undefined, NaN, [object Object], atau null", fakta.rusak === false);
  P.cek("J lima tautan: Langit, Karier, Ruang Coba, Pustaka, Dasbor", JSON.stringify(fakta.tautan) === JSON.stringify(["#/langit", "#/karier", "#/coba", "#/pustaka", "#/"]), fakta.tautan);
  const rata = await page.evaluate(() => {
    const p = document.querySelector(".pengantar .sambut-sub").getBoundingClientRect();
    const h = document.querySelector(".pengantar").getBoundingClientRect();
    return Math.abs((p.left + p.right) / 2 - (h.left + h.right) / 2);
  });
  P.cek("J paragraf pembuka berada di tengah kolomnya", rata < 2, rata);
  await s.tutup();
}
if (jalan("K")) {
  const s = await mulai({ lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/", tunggu: ".mulai" });
  const page = s.page;
  const tautan = page.locator('.mulai a[href="#/pengantar"]');
  P.cek("K layar mulai (profil tanpa XP) menautkan ke pengantar", (await tautan.count()) === 1, await tautan.allInnerTexts());
  await tautan.click(); await page.waitForSelector(".hg-pelat"); await tunggu(page, 300);
  P.cek("K klik tautan membuka #/pengantar", (await page.evaluate(() => location.hash)) === "#/pengantar");
  P.cek("K tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

P.selesai();
