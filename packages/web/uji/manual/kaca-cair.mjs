/* Pemeriksaan kaca cair di bilah atas (`komponen/TetesKaca.tsx` + blok "kaca cair"
 * di gaya.css), diukur di peramban. Yang diukur perilaku dan piksel, bukan sumber:
 *
 *   A  struktur: atribut, kanvas tidak menangkap penunjuk dan tidak bisa difokuskan,
 *      tata letak tidak bergeser, tema kontras tetap bilah padat
 *   B  tetes MENGIKUTI butir aktif: letaknya diukur dari PIKSEL kanvas WebGL (semua
 *      yang lain disembunyikan), diadu dengan kotak butirnya, untuk keenam tujuan
 *      dan untuk rute yang tidak punya butir
 *   C  GPU hanya bekerja saat ada yang bergerak: nol gambar saat diam, kursor hanya
 *      di tingkat penuh, tingkat mati langsung berdiri
 *   D  kontras huruf bilah di atas kaca, dari piksel sungguhan, empat tema, tiga
 *      halaman, tiga posisi gulir
 *   E  navigasi tetap bekerja: klik, aria-current, panel "Lainnya"
 *   F  konteks WebGL dicabut: pindah ke tetes cadangan, dan ganti tema saat berjalan
 *   G  tanpa WebGL sama sekali: tetes CSS cadangan di tempat yang sama
 *
 *   BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/kaca-cair.mjs
 *   HANYA=B,C node uji/manual/kaca-cair.mjs     bagian tertentu saja
 *   FOTO=/jalur/direktori node ...              simpan tangkapan bilah
 *
 * Jalankan terhadap server berprofil SEMENTARA (lihat `lib.mjs`); permintaan
 * tulis dicegat dan dihitung gagal. Peringatan "GPU stall due to ReadPixels"
 * dari SwiftShader datang dari pengambilan tangkapan layar, bukan dari aplikasi,
 * jadi disaring dari pemeriksaan konsol.
 */

import { URL_DASAR, lum, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Kaca cair di bilah atas");
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
const RUTE = [
  ["dasbor", "#/dasbor", "Dasbor"], ["langit", "#/langit", "Langit"], ["pustaka", "#/pustaka", "Pustaka"],
  ["karier", "#/karier", "Karier"], ["coba", "#/coba", "Ruang Coba"], ["lainnya", "#/statistik", "Lainnya"],
];
const TANPA_BUTIR = "#/bahasa/python";
const TEMA = ["gelap", "malam", "terang"];

const buka = (opsi = {}) => mulai({
  lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/dasbor", tunggu: "#rel[data-kaca]", ...opsi,
});
const tunggu = (page, ms) => page.waitForTimeout(ms);
const bukanGerutan = (k) => !/GPU stall|GL Driver Message/.test(k);

/** Hitung panggilan gambar kanvas tetes. Dipasang SESUDAH halaman termuat. */
const pasangCacah = (page) => page.evaluate(() => {
  window.__gambar = 0;
  const asli = WebGLRenderingContext.prototype.drawArrays;
  WebGLRenderingContext.prototype.drawArrays = function (...a) {
    if (this.canvas.classList.contains("tk-kanvas")) window.__gambar += 1;
    return asli.apply(this, a);
  };
});
const cacah = (page) => page.evaluate(() => window.__gambar);
/** Tunggu sampai jumlah gambar berhenti bertambah selama `jeda` ms (tiga kali berturut-turut). */
async function tungguDiam(page, { jeda = 250, maks = 8000 } = {}) {
  let terakhir = await cacah(page);
  let sama = 0;
  const mulaiMs = Date.now();
  while (sama < 3 && Date.now() - mulaiMs < maks) {
    await tunggu(page, jeda);
    const kini = await cacah(page);
    sama = kini === terakhir ? sama + 1 : 0;
    terakhir = kini;
  }
  return sama >= 3;
}

const kotakButir = (page, nama) => page.evaluate((n) => {
  const el = document.querySelector(`#rel [data-rel="${n}"]`);
  if (!el) return null;
  const b = el.getBoundingClientRect();
  return { kiri: b.left, kanan: b.right, atas: b.top, bawah: b.bottom, lebar: b.width, tinggi: b.height };
}, nama);

/** Yang tersisa di piksel HANYA kanvas: latar hitam, isi halaman disembunyikan, bilah tanpa
 *  kaca, tanpa batas, tanpa huruf. Dipasang sekali per sesi. */
const sembunyikanSelainKanvas = (page) => page.addStyleTag({
  content: `
    html, body, #latar, #cangkang { background: #000 !important; }
    #panggung { visibility: hidden !important; }
    #rel { background: transparent !important; border-color: transparent !important; box-shadow: none !important;
           -webkit-backdrop-filter: none !important; backdrop-filter: none !important; }
    #rel *:not(.tk-kanvas):not(.tk-bias) { color: transparent !important; text-shadow: none !important; }
    #rel .merek-bara, #rel .rel-tombol, #rel #ukuran, #rel .merek { visibility: hidden !important; }
    #maju-baca { display: none !important; }
  `,
});

/** Rentang mendatar tetes di baris tengah bilah, dari piksel. `null` = tidak ada tetes. */
async function eksten(page) {
  const k = await page.evaluate(() => {
    const n = document.getElementById("rel").getBoundingClientRect();
    const u = document.getElementById("rel-utama").getBoundingClientRect();
    const p = document.querySelector(".rel-pemicu").getBoundingClientRect();
    return { x: Math.floor(u.left), y: Math.floor(n.top + 10), w: Math.ceil(p.right - Math.floor(u.left)), h: Math.floor(n.height - 20) };
  });
  const png = await page.screenshot({ clip: { x: k.x, y: k.y, width: k.w, height: k.h }, type: "png" });
  return page.evaluate(async ([b64, x0]) => {
    const im = new Image(); im.src = "data:image/png;base64," + b64; await im.decode();
    const c = document.createElement("canvas"); c.width = im.width; c.height = im.height;
    const x = c.getContext("2d", { willReadFrequently: true }); x.drawImage(im, 0, 0);
    const d = x.getImageData(0, 0, c.width, c.height).data;
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    let kiri = -1, kanan = -1;
    for (let i = 0; i < c.width; i++) {
      let maks = 0;
      for (let j = 0; j < c.height; j++) {
        const o = (j * c.width + i) * 4;
        maks = Math.max(maks, 0.2126 * f(d[o]) + 0.7152 * f(d[o + 1]) + 0.0722 * f(d[o + 2]));
      }
      if (maks > 0.05) { if (kiri < 0) kiri = i; kanan = i + 1; }
    }
    return kiri < 0 ? null : { kiri: x0 + kiri, kanan: x0 + kanan };
  }, [png.toString("base64"), k.x]);
}
const hampir = (a, b, t) => Math.abs(a - b) <= t;

const bacaWarna = (c) => {
  const n = c.match(/[\d.]+/g).slice(0, 3).map(Number);
  return c.startsWith("color(") ? n.map((v) => v * 255) : n; // `color(srgb ...)` berkomponen 0..1
};
async function rasioTerburuk(page, kotak, warnaTeks) {
  const png = await page.screenshot({ clip: kotak, type: "png" });
  const L = await page.evaluate(async ([b64]) => {
    const im = new Image(); im.src = "data:image/png;base64," + b64; await im.decode();
    const c = document.createElement("canvas"); c.width = im.width; c.height = im.height;
    const x = c.getContext("2d", { willReadFrequently: true }); x.drawImage(im, 0, 0);
    const d = x.getImageData(0, 0, c.width, c.height).data;
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    const a = [];
    for (let i = 0; i < d.length; i += 4) a.push(0.2126 * f(d[i]) + 0.7152 * f(d[i + 1]) + 0.0722 * f(d[i + 2]));
    a.sort((p, q) => p - q);
    const at = (pr) => a[Math.min(a.length - 1, Math.floor((a.length * pr) / 100))];
    return { gelap: at(1), terang: at(99) };
  }, [png.toString("base64")]);
  const lt = lum(warnaTeks);
  const r = (l) => (Math.max(lt, l) + 0.05) / (Math.min(lt, l) + 0.05);
  return Math.min(r(L.gelap), r(L.terang)); // pasangan terburuk: piksel latar terjauh ke arah warna teks
}

/* ------------------------------------------------ A struktur dan tata letak */
if (jalan("A")) {
  for (const tema of TEMA) {
    const s = await buka({ tema }); const page = s.page;
    await tunggu(page, 500);
    const a = await page.evaluate(() => {
      const nav = document.getElementById("rel");
      const k = document.querySelector("#rel .tk-kanvas");
      const c = document.querySelector("#rel .tk-cadangan");
      const svg = document.querySelector("#rel .tk-bias");
      const nb = nav.getBoundingClientRect();
      const kb = k.getBoundingClientRect();
      const cs = getComputedStyle(nav);
      const tabbable = [...nav.querySelectorAll("a[href], button, input, [tabindex]")].filter((e) => e.tabIndex >= 0);
      return {
        kaca: nav.dataset.kaca, tk: nav.dataset.tk, bias: nav.dataset.bias,
        jumlahKanvas: document.querySelectorAll(".tk-kanvas").length,
        kanvasAria: k.getAttribute("aria-hidden"), kanvasPE: getComputedStyle(k).pointerEvents, kanvasDisp: getComputedStyle(k).display,
        kanvasTab: k.tabIndex, cadanganAria: c.getAttribute("aria-hidden"), cadanganDisp: getComputedStyle(c).display,
        svgAria: svg.getAttribute("aria-hidden"), filter: !!document.getElementById("tk-bias"),
        kanvasSelisih: [Math.round((nb.left - kb.left) * 10) / 10, Math.round((nb.top - kb.top) * 10) / 10,
          Math.round((kb.width - nb.width) * 10) / 10, Math.round((kb.height - nb.height) * 10) / 10],
        buffer: [k.width, k.height], cssUkuran: [Math.round(kb.width), Math.round(kb.height)],
        radius: parseFloat(cs.borderTopLeftRadius), tinggi: nb.height,
        bf: cs.backdropFilter || cs.webkitBackdropFilter,
        tabbableDalamTetes: tabbable.filter((e) => e.closest(".tk-kanvas, .tk-cadangan, .tk-bias")).length,
        bg: cs.backgroundColor,
        kanvasZ: getComputedStyle(k).zIndex, kanvasPos: getComputedStyle(k).position,
        kiniBg: getComputedStyle(document.querySelector("#rel-utama a.kini")).backgroundColor,
      };
    });
    P.cek(`A ${tema}: penanda lama a.kini mati selagi tetes memegang penanda (tidak ada penanda ganda)`,
      a.kiniBg === "rgba(0, 0, 0, 0)" || a.kiniBg === "transparent", a.kiniBg);
    P.cek(`A ${tema}: kanvas di bawah huruf (absolute, z-index -1 di dalam konteks susun bilah)`, a.kanvasZ === "-1" && a.kanvasPos === "absolute", [a.kanvasZ, a.kanvasPos]);
    P.cek(`A ${tema}: atribut kaca cair, WebGL, pembiasan nyala`, a.kaca === "cair" && a.tk === "gl" && a.bias === "on", [a.kaca, a.tk, a.bias]);
    P.cek(`A ${tema}: tepat satu kanvas (StrictMode tidak menggandakannya)`, a.jumlahKanvas === 1, a.jumlahKanvas);
    P.cek(`A ${tema}: kanvas dan tetes cadangan aria-hidden, penunjuk menembus, tidak bisa difokuskan`,
      a.kanvasAria === "true" && a.cadanganAria === "true" && a.svgAria === "true" && a.kanvasPE === "none" && a.kanvasTab === -1 && a.tabbableDalamTetes === 0 && a.filter,
      [a.kanvasAria, a.kanvasPE, a.kanvasTab, a.tabbableDalamTetes, a.filter]);
    P.cek(`A ${tema}: kanvas tampil, tetes cadangan tersembunyi (WebGL jalan)`, a.kanvasDisp === "block" && a.cadanganDisp === "none", [a.kanvasDisp, a.cadanganDisp]);
    P.cek(`A ${tema}: kanvas 2 px lebih besar di tiap sisi dan sejajar bilah`,
      hampir(a.kanvasSelisih[0], 2, 0.6) && hampir(a.kanvasSelisih[1], 2, 0.6) && hampir(a.kanvasSelisih[2], 4, 0.6) && hampir(a.kanvasSelisih[3], 4, 0.6), a.kanvasSelisih);
    P.cek(`A ${tema}: buffer kanvas selebar ukuran CSS-nya (dpr 1: satu piksel per piksel)`, a.buffer[0] === a.cssUkuran[0] && a.buffer[1] === a.cssUkuran[1], [a.buffer, a.cssUkuran]);
    P.cek(`A ${tema}: bilah berbentuk pil (radius penuh) dan tidak membesar`, a.radius >= a.tinggi / 2 && hampir(a.tinggi, 52, 0.6), [a.radius, a.tinggi]);
    P.cek(`A ${tema}: kaca nyata: backdrop-filter berisi blur dan pembiasan url()`, /blur/.test(a.bf) && /url\(/.test(a.bf), a.bf);
    P.cek(`A ${tema}: latar bilah tembus pandang (alfa < 1)`, /rgba\(.*0?\.\d|color\(.*\/\s*0?\.\d/.test(a.bg), a.bg);
    P.cek(`A ${tema}: tanpa galat konsol (selain gerutan driver)`, s.konsol.filter(bukanGerutan).length === 0, s.konsol.filter(bukanGerutan));
    // Kaca tidak boleh menggeser tata letak: matikan lewat atribut dan ukur ulang.
    const ukur = await page.evaluate(() => {
      const nav = document.getElementById("rel");
      const rect = () => [...nav.querySelectorAll("#rel-utama a, .rel-pemicu, .rel-tombol, #ukuran")].map((e) => { const b = e.getBoundingClientRect(); return [Math.round(b.left * 10) / 10, Math.round(b.width * 10) / 10]; });
      const nb = nav.getBoundingClientRect();
      const dengan = { lebar: nb.width, butir: rect() };
      nav.dataset.kaca = "polos";
      const nb2 = nav.getBoundingClientRect();
      const tanpa = { lebar: nb2.width, butir: rect() };
      nav.dataset.kaca = "cair";
      return { dengan, tanpa };
    });
    P.cek(`A ${tema}: kaca tidak menggeser satu butir pun (lebar dan posisi sama dengan atau tanpa kaca)`,
      hampir(ukur.dengan.lebar, ukur.tanpa.lebar, 0.6) && ukur.dengan.butir.every((b, i) => hampir(b[0], ukur.tanpa.butir[i][0], 0.6) && hampir(b[1], ukur.tanpa.butir[i][1], 0.6)), ukur);
    if (process.env.FOTO) await page.screenshot({ path: `${process.env.FOTO}/bilah-${tema}.png`, clip: { x: 300, y: 0, width: 840, height: 90 } });
    await s.tutup();
  }
  // Tema kontras tinggi: bilah padat lama, penanda butir lama.
  const k = await buka({ tema: "kontras" }); const page = k.page;
  await tunggu(page, 400);
  const x = await page.evaluate(() => {
    const nav = document.getElementById("rel");
    const cs = getComputedStyle(nav);
    const kini = getComputedStyle(document.querySelector("#rel-utama a.kini"));
    return { kaca: nav.dataset.kaca, tk: nav.dataset.tk ?? null, kanvas: getComputedStyle(document.querySelector(".tk-kanvas")).display,
      bg: cs.backgroundColor, bf: cs.backdropFilter, kiniBg: kini.backgroundColor };
  });
  P.cek("A kontras: kaca mati (data-kaca polos), tanpa data-tk, kanvas tersembunyi", x.kaca === "polos" && x.tk === null && x.kanvas === "none", x);
  P.cek("A kontras: bilah padat (alfa 1) dan tanpa backdrop-filter", /^rgb\(/.test(x.bg) && (x.bf === "none" || x.bf === ""), [x.bg, x.bf]);
  P.cek("A kontras: butir aktif tetap bertanda lewat latarnya (penanda lama)", x.kiniBg !== "rgba(0, 0, 0, 0)" && x.kiniBg !== "transparent", x.kiniBg);
  await k.tutup();
}

/* ------------------------------------------------ B tetes mengikuti butir aktif */
if (jalan("B")) {
  const s = await buka({ gerak: "mati", tema: "gelap" }); const page = s.page;
  await sembunyikanSelainKanvas(page);
  await tunggu(page, 300);
  for (const [nama, hash] of RUTE) {
    await page.evaluate((h) => { location.hash = h; }, hash);
    await page.waitForFunction((n) => document.querySelector(`#rel [data-rel="${n}"]`)?.getAttribute("aria-current") != null, nama, { timeout: 8000 }).catch(() => {});
    await tunggu(page, 500);
    const e = await eksten(page);
    const b = await kotakButir(page, nama);
    P.cek(`B ${nama}: tetes tergambar di butir ${nama} (kiri dan kanan dalam 8 px dari kotaknya)`,
      e !== null && b !== null && hampir(e.kiri, b.kiri, 8) && hampir(e.kanan, b.kanan, 8), { eksten: e, butir: b && [b.kiri, b.kanan] });
  }
  await page.evaluate((h) => { location.hash = h; }, TANPA_BUTIR);
  await tunggu(page, 700);
  const tanpa = await page.evaluate(() => document.querySelectorAll("#rel [aria-current]").length);
  const e0 = await eksten(page);
  P.cek("B rute tanpa butir (halaman bahasa): tidak ada butir bertanda, dan tidak ada tetes tergambar", tanpa === 0 && e0 === null, { ditandai: tanpa, eksten: e0 });
  // Kembali ke butir: muncul LAGI di tempatnya, tidak terbang dari tempat yang sudah tiada.
  await page.evaluate(() => { location.hash = "#/pustaka"; });
  await tunggu(page, 600);
  const e1 = await eksten(page); const b1 = await kotakButir(page, "pustaka");
  P.cek("B dari rute tanpa butir kembali ke Pustaka: tetes muncul di Pustaka", e1 !== null && hampir(e1.kiri, b1.kiri, 8) && hampir(e1.kanan, b1.kanan, 8), { e1, kiri: b1.kiri });
  // Ukuran bilah berubah (setelan "Ukuran huruf" membesarkan semua butir): pengamat ukuran
  // harus menaruh tetes di kotak yang BARU, bukan membiarkannya di geometri lama.
  const lebarSebelum = (await kotakButir(page, "pustaka")).lebar;
  await page.evaluate(() => document.documentElement.style.setProperty("--ukuran-teks", "20px"));
  await tunggu(page, 900);
  const e2 = await eksten(page); const b2 = await kotakButir(page, "pustaka");
  P.cek("B ukuran huruf diperbesar (butir melebar): tetes mengikuti kotak butir yang baru",
    b2.lebar > lebarSebelum + 5 && e2 !== null && hampir(e2.kiri, b2.kiri, 8) && hampir(e2.kanan, b2.kanan, 8), { lebarSebelum, lebarSesudah: b2.lebar, e2, kotak: [b2.kiri, b2.kanan] });
  await s.tutup();

  // Gerak penuh: sesudah menetap, letak akhir sama saja.
  const g = await buka({ gerak: "penuh", tema: "gelap" });
  await sembunyikanSelainKanvas(g.page);
  await pasangCacah(g.page);
  await g.page.evaluate(() => { location.hash = "#/coba"; });
  const diam = await tungguDiam(g.page);
  const eg = await eksten(g.page); const bg = await kotakButir(g.page, "coba");
  P.cek("B gerak penuh: sesudah menetap tetes tepat di Ruang Coba", diam && eg !== null && hampir(eg.kiri, bg.kiri, 8) && hampir(eg.kanan, bg.kanan, 8), { diam, eg, kiri: bg.kiri });
  await g.tutup();
}

/* ------------------------------------------------ C GPU hanya saat ada yang bergerak */
if (jalan("C")) {
  const s = await buka({ gerak: "penuh" }); const page = s.page;
  await pasangCacah(page);
  const diam0 = await tungguDiam(page);
  const a0 = await cacah(page);
  await tunggu(page, 1500);
  const a1 = await cacah(page);
  P.cek("C tetes diam: nol gambar dalam 1,5 detik", diam0 && a1 === a0, { diam0, a0, a1 });

  await page.evaluate(() => { location.hash = "#/coba"; });
  await tunggu(page, 250);
  const b0 = await cacah(page);
  const kembaliDiam = await tungguDiam(page);
  const b1 = await cacah(page);
  // SwiftShader menggambar kasar (puluhan ms per bingkai), jadi yang ditagih jumlah SELURUH gerak,
  // bukan kecepatan: tetes yang melaju dan beriak menggambar belasan sampai puluhan bingkai.
  P.cek("C pindah butir di gerak penuh: gambar berjalan sampai menetap (belasan bingkai atau lebih)", b0 - a1 >= 1 && b1 - a1 >= 12, { awal: b0 - a1, total: b1 - a1 });
  await tunggu(page, 1200);
  P.cek("C sesudah menetap (dan riaknya habis) bingkai berhenti lagi", kembaliDiam && (await cacah(page)) === b1, { kembaliDiam });

  // Kursor di atas bilah: selama di atasnya gambar terus berjalan; pergi: berhenti.
  const bil = await kotakButir(page, "coba");
  await page.mouse.move(bil.kiri + 5, bil.atas + 10);
  await page.mouse.move(bil.kiri + 25, bil.atas + 12);
  const c0 = await cacah(page);
  await tunggu(page, 500);
  const c1 = await cacah(page);
  P.cek("C kursor di bilah (penuh): gambar terus berjalan walau penunjuk diam", c1 - c0 >= 3, c1 - c0);
  await page.mouse.move(700, 600);
  const henti = await tungguDiam(page);
  P.cek("C kursor pergi: bingkai berhenti", henti, henti);
  await s.tutup();

  const h = await buka({ gerak: "halus" });
  await pasangCacah(h.page);
  await tungguDiam(h.page);
  const hb = await kotakButir(h.page, "dasbor");
  const h0 = await cacah(h.page);
  await h.page.mouse.move(hb.kiri + 5, hb.atas + 10);
  await h.page.mouse.move(hb.kiri + 25, hb.atas + 12);
  await tunggu(h.page, 500);
  P.cek("C gerak halus: kursor di bilah tidak menyalakan gambar", (await cacah(h.page)) === h0, (await cacah(h.page)) - h0);
  await h.page.evaluate(() => { location.hash = "#/langit"; });
  await tunggu(h.page, 150);
  P.cek("C gerak halus: pindah butir tetap dijawab (gambar berjalan)", (await cacah(h.page)) - h0 >= 2, (await cacah(h.page)) - h0);
  await h.tutup();

  for (const [judul, opsi] of [["gerak mati", { gerak: "mati" }], ["prefers-reduced-motion (gerak penuh di setelan)", { gerak: "penuh", reduce: true }]]) {
    const m = await buka(opsi);
    await pasangCacah(m.page);
    await tungguDiam(m.page);
    const m0 = await cacah(m.page);
    await m.page.evaluate(() => { location.hash = "#/coba"; });
    await tunggu(m.page, 400);
    const dm = (await cacah(m.page)) - m0;
    await tunggu(m.page, 800);
    P.cek(`C ${judul}: pindah butir hanya satu sampai tiga gambar, tidak ada bingkai berantai`, dm >= 1 && dm <= 3 && (await cacah(m.page)) - m0 === dm, dm);
    await m.tutup();
  }
}

/* ------------------------------------------------ D kontras huruf bilah */
if (jalan("D")) {
  const HALAMAN = [["#/dasbor", "dasbor"], ["#/pustaka", "pustaka"], ["#/karier", "karier"]];
  const GULIR = [0, 700, 1600];
  for (const tema of [...TEMA, "kontras"]) {
    const s = await buka({ tema, gerak: "mati" }); const page = s.page;
    const hasil = {};
    let terburuk = 99;
    let di = "";
    for (const [hash, nama] of HALAMAN) {
      await page.evaluate((h) => { location.hash = h; }, hash);
      await tunggu(page, 900);
      for (const y of GULIR) {
        await page.evaluate((v) => window.scrollTo(0, v), y);
        await tunggu(page, 250);
        // Warna dibaca dari gaya SUNGGUHAN sebelum hurufnya disembunyikan.
        const info = await page.evaluate(() => {
          const teks = (el) => { const r = document.createRange(); r.selectNodeContents(el); const b = r.getBoundingClientRect(); return { x: b.x, y: b.y, width: b.width, height: b.height }; };
          const butir = [...document.querySelectorAll("#rel-utama a .nama, .rel-pemicu")].map((el) => ({
            nama: el.textContent.trim().replace(/\s*▾$/, ""), warna: getComputedStyle(el.closest("a, button") ?? el).color, kotak: teks(el),
          }));
          const cari = document.querySelector(".rel-tombol .rel-label");
          if (cari) butir.push({ nama: "Cari apa saja", warna: getComputedStyle(cari).color, kotak: teks(cari) });
          return butir;
        });
        await page.evaluate(() => {
          const st = document.createElement("style"); st.id = "uji-teks-transparan";
          st.textContent = "#rel *{color:transparent!important;text-shadow:none!important}";
          document.head.appendChild(st);
        });
        for (const it of info) {
          if (it.kotak.width < 4) continue;
          const r = await rasioTerburuk(page, { x: it.kotak.x, y: it.kotak.y, width: it.kotak.width, height: it.kotak.height }, bacaWarna(it.warna));
          const kunci = `${nama}@${y}`;
          hasil[kunci] = Math.min(hasil[kunci] ?? 99, Math.round(r * 100) / 100);
          if (r < terburuk) { terburuk = r; di = `${it.nama} ${kunci}`; }
        }
        await page.evaluate(() => document.getElementById("uji-teks-transparan")?.remove());
      }
    }
    // Tiga tema berkaca dituntut 5,0:1 (4,5 mutlak ditambah margin 0,5), bukan 4,5: isi di bawah kaca
    // berganti-ganti dan halaman uji hanyalah sampel. Terukur, tanpa peredupan latar tema malam jatuh ke
    // 4,69:1 (margin 0,19) dan tema terang DENGAN peredupan jatuh ke 4,92:1; dengan ambang 4,5 kedua
    // kekeliruan itu lolos. Tema kontras tidak berkaca dan tetap 4,5.
    const ambang = tema === "kontras" ? 4.5 : 5.0;
    P.cek(`D ${tema}: huruf bilah >= ${String(ambang).replace(".", ",")}:1 di atas kaca (terburuk ${Math.round(terburuk * 100) / 100} pada ${di})`, terburuk >= ambang, hasil);
    await s.tutup();
  }
}

/* ------------------------------------------------ E navigasi tetap bekerja */
if (jalan("E")) {
  const s = await buka({ gerak: "penuh" }); const page = s.page;
  await page.click('#rel [data-rel="pustaka"]');
  await tunggu(page, 600);
  const e = await page.evaluate(() => ({
    hash: location.hash, tanda: [...document.querySelectorAll("#rel-utama a")].filter((a) => a.getAttribute("aria-current") === "page").map((a) => a.dataset.rel),
    kini: [...document.querySelectorAll("#rel-utama a.kini")].map((a) => a.dataset.rel),
  }));
  P.cek("E klik Pustaka: rute berpindah, tepat satu butir aria-current dan satu .kini", e.hash === "#/pustaka" && e.tanda.join() === "pustaka" && e.kini.join() === "pustaka", e);
  await page.click(".rel-pemicu");
  await tunggu(page, 400);
  const p = await page.evaluate(() => {
    const nav = document.getElementById("rel").getBoundingClientRect();
    const pn = document.querySelector(".rel-panel").getBoundingClientRect();
    const a = document.querySelector('.rel-panel [data-rel="statistik"]').getBoundingClientRect();
    return { buka: document.querySelector(".rel-turun").classList.contains("buka"), panelAtas: pn.top, navBawah: nav.bottom, tinggi: pn.height, aLebar: a.width,
      expanded: document.querySelector(".rel-pemicu").getAttribute("aria-expanded"), latar: getComputedStyle(document.querySelector(".rel-panel")).backgroundColor };
  });
  P.cek("E panel Lainnya terbuka di bawah bilah, berisi butirnya, tetap latar padat", p.buka && p.expanded === "true" && p.panelAtas >= p.navBawah - 1 && p.tinggi > 40 && p.aLebar > 20 && /^rgb\(/.test(p.latar), p);
  await page.click('.rel-panel [data-rel="statistik"]');
  await tunggu(page, 800);
  const q = await page.evaluate(() => ({ hash: location.hash, pemicu: document.querySelector(".rel-pemicu").getAttribute("aria-current"), kini: document.querySelector(".rel-pemicu").classList.contains("kini"),
    utama: document.querySelectorAll("#rel-utama a[aria-current]").length }));
  P.cek("E klik Statistik di panel: pemicu Lainnya bertanda, tidak ada butir utama bertanda", q.hash === "#/statistik" && q.pemicu === "true" && q.kini && q.utama === 0, q);
  await s.tutup();
}

/* ------------------------------------------------ F konteks dicabut dan tema berganti */
if (jalan("F")) {
  const s = await buka({ gerak: "mati" }); const page = s.page;
  await tunggu(page, 400);
  const sebelum = await kotakButir(page, "dasbor");
  await page.evaluate(() => { document.querySelector(".tk-kanvas").getContext("webgl").getExtension("WEBGL_lose_context").loseContext(); });
  await tunggu(page, 500);
  const f = await page.evaluate(() => {
    const nav = document.getElementById("rel");
    const c = document.querySelector(".tk-cadangan").getBoundingClientRect();
    const cs = getComputedStyle(document.querySelector(".tk-cadangan"));
    return { tk: nav.dataset.tk, kanvas: getComputedStyle(document.querySelector(".tk-kanvas")).display, disp: cs.display, opa: cs.opacity, kiri: c.left, kanan: c.right };
  });
  P.cek("F konteks WebGL dicabut: pindah ke tetes cadangan (data-tk css), kanvas disembunyikan", f.tk === "css" && f.kanvas === "none" && f.disp === "block" && f.opa === "1", f);
  P.cek("F tetes cadangan tepat di butir aktif", hampir(f.kiri, sebelum.kiri, 0.6) && hampir(f.kanan, sebelum.kanan, 0.6), [f.kiri, f.kanan, sebelum.kiri, sebelum.kanan]);
  await s.tutup();

  const t = await buka({ gerak: "mati", tema: "gelap" }); const tp = t.page;
  await tp.evaluate(() => { document.documentElement.dataset.tema = "kontras"; document.dispatchEvent(new CustomEvent("tampilan-berubah")); });
  await tunggu(tp, 300);
  const k = await tp.evaluate(() => ({ kaca: document.getElementById("rel").dataset.kaca, tk: document.getElementById("rel").dataset.tk ?? null, kanvas: getComputedStyle(document.querySelector(".tk-kanvas")).display }));
  P.cek("F ganti ke tema kontras saat berjalan: kaca mati seketika", k.kaca === "polos" && k.tk === null && k.kanvas === "none", k);
  await tp.evaluate(() => { document.documentElement.dataset.tema = "terang"; document.dispatchEvent(new CustomEvent("tampilan-berubah")); });
  await tunggu(tp, 500);
  const k2 = await tp.evaluate(() => ({ kaca: document.getElementById("rel").dataset.kaca, tk: document.getElementById("rel").dataset.tk }));
  await sembunyikanSelainKanvas(tp);
  await tunggu(tp, 300);
  const e = await eksten(tp); const b = await kotakButir(tp, "dasbor");
  P.cek("F kembali ke tema terang: kaca hidup lagi dan tetes tergambar di butir aktif", k2.kaca === "cair" && k2.tk === "gl" && e !== null && hampir(e.kiri, b.kiri, 8) && hampir(e.kanan, b.kanan, 8), { k2, e, kiri: b.kiri });
  await t.tutup();
}

/* ------------------------------------------------ G tanpa WebGL */
if (jalan("G")) {
  const s = await buka({ gerak: "mati", argsChrome: ["--disable-3d-apis"] }); const page = s.page;
  await tunggu(page, 500);
  const g = await page.evaluate(() => ({ tk: document.getElementById("rel").dataset.tk, kaca: document.getElementById("rel").dataset.kaca,
    gl: !!document.createElement("canvas").getContext("webgl"), kanvas: getComputedStyle(document.querySelector(".tk-kanvas")).display }));
  P.cek("G tanpa WebGL: data-tk css, kaca tetap cair, kanvas tersembunyi", g.tk === "css" && g.kaca === "cair" && !g.gl && g.kanvas === "none", g);
  for (const [nama, hash] of RUTE) {
    await page.evaluate((h) => { location.hash = h; }, hash);
    await tunggu(page, 700);
    const c = await page.evaluate(() => { const e = document.querySelector(".tk-cadangan"); const b = e.getBoundingClientRect(); return { kiri: b.left, kanan: b.right, atas: b.top, bawah: b.bottom, opa: getComputedStyle(e).opacity }; });
    const b = await kotakButir(page, nama);
    P.cek(`G ${nama}: tetes cadangan menutupi kotak butir (selisih <= 0,6 px di keempat sisi)`,
      hampir(c.kiri, b.kiri, 0.6) && hampir(c.kanan, b.kanan, 0.6) && hampir(c.atas, b.atas, 0.6) && hampir(c.bawah, b.bawah, 0.6) && c.opa === "1", { c, b: [b.kiri, b.kanan, b.atas, b.bawah] });
  }
  await page.evaluate((h) => { location.hash = h; }, TANPA_BUTIR);
  await tunggu(page, 900);
  const o = await page.evaluate(() => getComputedStyle(document.querySelector(".tk-cadangan")).opacity);
  P.cek("G rute tanpa butir: tetes cadangan tidak tampak (opasitas 0)", o === "0", o);
  await s.tutup();
}

P.selesai();
