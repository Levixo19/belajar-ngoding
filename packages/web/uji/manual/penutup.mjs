/* Pemeriksaan penutup dasbor (`layar/PenutupDasbor.tsx` + blok "penutup dasbor" di gaya.css),
 * diukur di peramban. Dasbor berprogres punya penutup; profil dengan XP 0 memakai layar mulai
 * dan TIDAK punya (bagian H, jalankan terhadap server berprofil BARU).
 *
 *   A  struktur dan tata letak di 1280x800, 1440x900, 1600x1000: pembungkus setinggi layar dan
 *      menempel ke dasar halaman, tanpa meluber ke samping, isi tengah tidak menimpa strip
 *   B  penyingkapan: lapisan `fixed` diam sementara pembungkusnya naik; yang terlihat hanya yang
 *      jatuh di dalam kotak pembungkus (uji sentuh), dan di puncak halaman tidak ada yang terlihat
 *   C  gerak: penuh, halus, mati, prefers-reduced-motion; animasi tak berhingga hanya selagi
 *      terlihat; kemunculan terhubung gulir berangkat dari tak terlihat dan berakhir di keadaan alami
 *   D  kontras empat tema dari piksel sungguhan (judul bergradien diukur dari piksel TINTA)
 *   E  papan ketik: Tab dari puncak sampai masuk ke penutup menggulir ke dasar, tiap perhentian
 *      terlihat dan tidak tertutup, "Kembali ke atas" bekerja dengan Enter
 *   F  magnet: pil mengikuti penunjuk hanya di gerak penuh dan kembali ke asal
 *   G  isi: ringkasan pembaca layar, alis, dan judul sama dengan angka nyata dari /api/dasbor;
 *      cetak menyembunyikan penutup
 *   H  profil baru (XP 0): tidak ada penutup
 *
 *   # bagian A sampai G: server berprofil berprogres
 *   HANYA=A,B,C,D,E,F,G BELAJAR_URL=http://127.0.0.1:7789/ node uji/manual/penutup.mjs
 *   # bagian H: server berprofil baru (XP 0)
 *   HANYA=H BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/penutup.mjs
 *
 * Jalankan terhadap server berprofil SEMENTARA (lihat `lib.mjs`); permintaan tulis dicegat dan
 * dihitung gagal. `FOTO=<direktori>` menyimpan tangkapan layar. Peringatan "GPU stall due to
 * ReadPixels" datang dari pengambilan tangkapan layar oleh SwiftShader dan disaring.
 */

import { URL_DASAR, lum, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Penutup dasbor");
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
const TEMA = ["gelap", "malam", "terang", "kontras"];
const bukanGerutan = (k) => !/GPU stall|GL Driver Message/.test(k);
const tunggu = (page, ms) => page.waitForTimeout(ms);
const hampir = (a, b, t) => Math.abs(a - b) <= t;

const buka = (opsi = {}) => mulai({
  // Menunggu `.meja` (akar dasbor berprogres), bukan `.pd-bungkus`: komponen yang dicabut harus menjadi
  // pemeriksaan GAGAL yang tercetak, bukan penantian yang kedaluwarsa dan mematikan seluruh skrip.
  lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/dasbor", tunggu: ".meja", ...opsi,
});

/** Gulir ke dasar halaman dan beri waktu satu dua bingkai (garis waktu gulir dan pengamat ikut berjalan). */
const keDasar = async (page) => {
  await page.evaluate(() => window.scrollTo({ top: 1e7, behavior: "instant" }));
  await tunggu(page, 450);
};
const keAtasHalaman = async (page) => {
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: "instant" }));
  await tunggu(page, 300);
};
/** Gulir sampai `bagian` (0..1) dari pembungkus sudah masuk dari bawah layar. */
const keBagian = async (page, bagian) => {
  await page.evaluate((b) => {
    const el = document.querySelector(".pd-bungkus");
    const atasDokumen = el.getBoundingClientRect().top + window.scrollY;
    window.scrollTo({ top: atasDokumen - window.innerHeight * (1 - b), behavior: "instant" });
  }, bagian);
  await tunggu(page, 450);
};

const bacaWarna = (c) => {
  const n = c.match(/[\d.]+/g).slice(0, 3).map(Number);
  return c.startsWith("color(") ? n.map((v) => v * 255) : n; // `color(srgb ...)` berkomponen 0..1
};
/** Alfa warna teks: `color(srgb r g b / a)` dan `rgba(r, g, b, a)`. Tanpa ini teks setengah transparan
 *  (`color-mix(... 30%, transparent)`) terbaca berkontras penuh. */
const bacaAlpha = (c) => {
  const n = c.match(/[\d.]+/g).map(Number);
  if (n.length < 4) return 1;
  return /%/.test(c.split("/")[1] ?? "") ? n[3] / 100 : n[3];
};

/** Luminansi tiap piksel di `kotak`, per baris. Tangkapan layar di-decode di halaman. */
async function luminansiKotak(page, kotak, denganRgb = false) {
  const png = await page.screenshot({ clip: kotak, type: "png" });
  return page.evaluate(async ([b64, rgbJuga]) => {
    const im = new Image(); im.src = "data:image/png;base64," + b64; await im.decode();
    const c = document.createElement("canvas"); c.width = im.width; c.height = im.height;
    const x = c.getContext("2d", { willReadFrequently: true }); x.drawImage(im, 0, 0);
    const d = x.getImageData(0, 0, c.width, c.height).data;
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    const baris = [], rgb = [];
    for (let y = 0; y < c.height; y++) {
      const r = [];
      for (let xx = 0; xx < c.width; xx++) {
        const i = (y * c.width + xx) * 4;
        r.push(0.2126 * f(d[i]) + 0.7152 * f(d[i + 1]) + 0.0722 * f(d[i + 2]));
        if (rgbJuga) rgb.push([d[i], d[i + 1], d[i + 2]]);
      }
      baris.push(r);
    }
    return { baris, rgb, tinggi: c.height };
  }, [png.toString("base64"), denganRgb]);
}
const persentil = (nilai, p) => {
  const a = [...nilai].sort((x, y) => x - y);
  return a[Math.min(a.length - 1, Math.floor((a.length * p) / 100))];
};
const kontrasDua = (l1, l2) => (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);

/** Kotak huruf pertama di dalam elemen ke-`indeks` yang cocok `sel` (Range pada simpul teksnya) dan warna teksnya. */
const teksDi = (page, sel, indeks = 0) => page.evaluate(([s, i]) => {
  const el = document.querySelectorAll(s)[i];
  if (!el) return null;
  const jalan = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
  let simpul = null;
  for (let n = jalan.nextNode(); n; n = jalan.nextNode()) { if (n.textContent.trim()) { simpul = n; break; } }
  if (!simpul) return null;
  const r = document.createRange(); r.selectNodeContents(simpul);
  const b = r.getBoundingClientRect();
  // Opasitas efektif = hasil kali opasitas semua leluhur: warna terhitung TIDAK memuatnya, jadi teks yang
  // diredupkan dengan `opacity` tampak lolos kontras padahal tidak (dilarang di seluruh aplikasi).
  let opasitas = 1;
  for (let n = simpul.parentElement; n; n = n.parentElement) opasitas *= parseFloat(getComputedStyle(n).opacity);
  return { kotak: { x: b.x, y: b.y, width: b.width, height: b.height }, warna: getComputedStyle(simpul.parentElement).color, teks: simpul.textContent.trim(), opasitas };
}, [sel, indeks]);

/** Rasio teks biasa: teks DISEMBUNYIKAN lebih dulu supaya yang diukur latar sungguhan di bawahnya. */
async function rasioTeks(page, sel, { luruskanStrip = false } = {}) {
  if (luruskanStrip) {
    await page.evaluate(() => {
      const st = document.createElement("style"); st.id = "uji-lurus";
      st.textContent = ".pd-strip { rotate: none !important; scale: none !important; }";
      document.head.appendChild(st);
    });
    await tunggu(page, 100);
  }
  let t = null;
  if (luruskanStrip) {
    // Butir pertama tersembunyi sebagian di luar layar (strip melebihi tepi): pilih yang utuh di dalam.
    const n = await page.evaluate((s) => document.querySelectorAll(s).length, sel);
    for (let i = 0; i < n && !t; i++) {
      const c = await teksDi(page, sel, i);
      if (c && c.kotak.x >= 8 && c.kotak.x + c.kotak.width <= 1272) t = c;
    }
  } else t = await teksDi(page, sel, 0);
  if (!t) {
    await page.evaluate(() => document.getElementById("uji-lurus")?.remove());
    return { rasio: 0, teks: "(tidak ada)", opasitas: 0 };
  }
  await page.evaluate(() => {
    const st = document.createElement("style"); st.id = "uji-teks-transparan";
    st.textContent = ".pd-isi *, .pd-isi *::before, .pd-isi *::after { color: transparent !important; -webkit-text-fill-color: transparent !important; text-shadow: none !important; }";
    document.head.appendChild(st);
  });
  const { baris, rgb } = await luminansiKotak(page, t.kotak, true);
  await page.evaluate(() => { document.getElementById("uji-teks-transparan")?.remove(); document.getElementById("uji-lurus")?.remove(); });
  const semua = baris.flat();
  // Teks setengah transparan dikomposit di atas latar (piksel bermedian luminansi), di ruang sRGB seperti peramban.
  const urut = semua.map((l, i) => [l, i]).sort((a, b) => a[0] - b[0]);
  const latar = rgb[urut[Math.floor(urut.length / 2)][1]];
  const alfa = bacaAlpha(t.warna);
  const lt = lum(bacaWarna(t.warna).map((v, k) => alfa * v + (1 - alfa) * latar[k]));
  const rasio = Math.min(kontrasDua(lt, persentil(semua, 1)), kontrasDua(lt, persentil(semua, 99)));
  return { rasio: Math.round(rasio * 100) / 100, teks: t.teks, opasitas: Math.round(t.opasitas * 1000) / 1000 };
}

/** Rasio judul bergradien: latarnya piksel tengah pita, tintanya piksel paling kontras di pita bawah
 *  judul (ujung gradien yang paling pudar). Arah ditentukan dari warna teks tubuh halaman. */
async function rasioJudul(page) {
  const b = await page.evaluate(() => { const r = document.querySelector("#pd-judul")?.getBoundingClientRect(); return r ? { x: r.x, y: r.y, width: r.width, height: r.height } : null; });
  if (!b || b.width < 1 || b.height < 1) return { rasio: 0, latar: 0, tinta: 0 };
  const { baris, tinggi } = await luminansiKotak(page, b);
  const pita = baris.slice(Math.floor(tinggi * 0.72)).flat();
  const latar = persentil(pita, 50);
  const warnaTubuh = await page.evaluate(() => getComputedStyle(document.body).color);
  const lebihTerang = lum(bacaWarna(warnaTubuh)) > latar;
  const tinta = lebihTerang ? persentil(pita, 99.7) : persentil(pita, 0.3);
  return { rasio: Math.round(kontrasDua(tinta, latar) * 100) / 100, latar: Math.round(latar * 1000) / 1000, tinta: Math.round(tinta * 1000) / 1000 };
}

/* ------------------------------------------------ A struktur dan tata letak */
if (jalan("A")) {
  for (const [lebar, tinggi] of [[1280, 800], [1440, 900], [1600, 1000]]) {
    const s = await buka({ lebar, tinggi }); const page = s.page;
    await keDasar(page);
    const a = await page.evaluate(() => {
      const b = document.querySelector(".pd-bungkus");
      // Tanpa pembungkus (komponen dicabut) pemeriksaan di bawah harus GAGAL, bukan mati karena TypeError.
      if (!b) return { jumlah: document.querySelectorAll(".pd-bungkus").length, pil: [], innerH: window.innerHeight, innerW: window.innerWidth, meluber: 0 };
      const cs = getComputedStyle(b);
      const rect = (e) => { const r = e.getBoundingClientRect(); return { atas: r.top, bawah: r.bottom, kiri: r.left, kanan: r.right, lebar: r.width, tinggi: r.height }; };
      const isi = b.querySelector(".pd-isi");
      const strip = b.querySelector(".pd-strip");
      const tengah = b.querySelector(".pd-tengah");
      const kaki = b.querySelector(".pd-kaki");
      // Tepi BAWAH strip miring pada koordinat x tertentu, dari kotak asli (sebelum rotate dan scale)
      // dan matriks yang sama dengan yang dipasang CSS. Kotak pembatas peramban terlalu konservatif:
      // ia memuat ujung kiri strip yang sudah di luar layar.
      let tepiStrip = null;
      if (strip) {
        const cx = strip.offsetLeft + strip.offsetWidth / 2, cy = strip.offsetTop + strip.offsetHeight / 2;
        const sudut = parseFloat(getComputedStyle(strip).rotate) || 0, skala = parseFloat(getComputedStyle(strip).scale) || 1;
        const m = new DOMMatrix().translate(cx, cy).rotate(sudut).scale(skala).translate(-cx, -cy);
        const y = strip.offsetTop + strip.offsetHeight;
        const p1 = m.transformPoint(new DOMPoint(strip.offsetLeft, y)), p2 = m.transformPoint(new DOMPoint(strip.offsetLeft + strip.offsetWidth, y));
        tepiStrip = (x) => p1.y + ((x - p1.x) / (p2.x - p1.x)) * (p2.y - p1.y);
      }
      const alis = b.querySelector(".pd-alis")?.getBoundingClientRect();
      const kecil = [...b.querySelectorAll(".pd-pil-kecil")].map((e) => e.getBoundingClientRect().bottom);
      const jarakAlis = alis && tepiStrip ? alis.top - Math.max(tepiStrip(alis.left), tepiStrip(alis.right)) : null;
      return {
        jarakAlis, jarakKaki: kaki && kecil.length ? kaki.getBoundingClientRect().top - Math.max(...kecil) : null,
        jumlah: document.querySelectorAll(".pd-bungkus").length,
        b: rect(b), clip: cs.clipPath, timeline: cs.viewTimelineName, labelled: b.getAttribute("aria-labelledby"),
        judulId: !!document.getElementById("pd-judul"), tag: b.tagName,
        isiPos: isi && getComputedStyle(isi).position, isiRect: isi && rect(isi),
        stripAria: strip?.getAttribute("aria-hidden"), stripRect: strip && rect(strip),
        srAda: !!b.querySelector(".pd-sr"), tengah: tengah && rect(tengah), kaki: kaki && rect(kaki),
        meluber: document.documentElement.scrollWidth - document.documentElement.clientWidth,
        pil: [...b.querySelectorAll("a.pd-pil")].map((e) => e.getAttribute("href")),
        tombolAtas: b.querySelectorAll("button.pd-atas[aria-label='Kembali ke atas']").length,
        innerH: window.innerHeight, innerW: window.innerWidth,
      };
    });
    const w = `${lebar}x${tinggi}`;
    P.cek(`A ${w}: tepat satu penutup, berupa <section> bernama oleh judulnya (aria-labelledby ke #pd-judul)`, a.jumlah === 1 && a.tag === "SECTION" && a.labelled === "pd-judul" && a.judulId, a);
    P.cek(`A ${w}: pembungkus setinggi layar dan menempel ke dasar halaman (bawah = ${a.innerH}, atas = 0)`, !!a.b && hampir(a.b.tinggi, a.innerH, 1) && hampir(a.b.bawah, a.innerH, 1) && hampir(a.b.atas, 0, 1), a.b);
    P.cek(`A ${w}: selebar layar penuh dan tidak meluber ke samping`, !!a.b && hampir(a.b.lebar, a.innerW, 1) && hampir(a.b.kiri, 0, 1) && a.meluber <= 0, { lebar: a.b?.lebar, meluber: a.meluber });
    P.cek(`A ${w}: penyingkapan dipasang (clip-path inset(0), garis waktu bernama --pd)`, a.clip === "inset(0px)" && a.timeline === "--pd", { clip: a.clip, timeline: a.timeline });
    P.cek(`A ${w}: lapisan isi fixed di gerak penuh dan menempel ke layar (atas 0, tinggi layar)`, a.isiPos === "fixed" && hampir(a.isiRect.atas, 0, 1) && hampir(a.isiRect.tinggi, a.innerH, 1), { pos: a.isiPos, rect: a.isiRect });
    P.cek(`A ${w}: strip aria-hidden, ringkasannya ada sebagai teks pembaca layar`, a.stripAria === "true" && a.srAda, [a.stripAria, a.srAda]);
    P.cek(`A ${w}: pil alis jatuh di bawah tepi bawah strip miring (jarak >= 8 px, terukur ${Math.round(a.jarakAlis ?? -999)})`,
      a.jarakAlis !== null && a.jarakAlis >= 8, { jarakAlis: a.jarakAlis });
    P.cek(`A ${w}: pil kecil paling bawah berhenti di atas kaki (jarak >= 8 px, terukur ${Math.round(a.jarakKaki ?? -999)})`,
      a.jarakKaki !== null && a.jarakKaki >= 8, { jarakKaki: a.jarakKaki });
    P.cek(`A ${w}: dua pil besar, empat pil kecil, satu tombol "Kembali ke atas"; semua tujuan hash rute`,
      a.pil.length === 6 && a.pil.every((h) => /^#\/[a-z]+$/.test(h)) && a.tombolAtas === 1, a.pil);
    P.cek(`A ${w}: tanpa galat konsol (selain gerutan driver)`, s.konsol.filter(bukanGerutan).length === 0, s.konsol.filter(bukanGerutan));
    if (process.env.FOTO) await page.screenshot({ path: `${process.env.FOTO}/penutup-${w}.png` });
    await s.tutup();
  }
}

/* ------------------------------------------------ B penyingkapan */
if (jalan("B")) {
  const s = await buka(); const page = s.page;
  /** Tiap titik uji di baris `ys` (piksel layar): apakah yang paling atas di sana bagian dari lapisan penutup. */
  const kenaIsi = (ys) => page.evaluate((nilai) => {
    const hasil = [];
    for (const y of nilai) for (const x of [80, 360, 720, 1080, 1360]) {
      const e = document.elementFromPoint(x, y);
      hasil.push(!!e?.closest(".pd-isi"));
    }
    return hasil;
  }, ys);
  const posisiIsi = () => page.evaluate(() => { const r = document.querySelector(".pd-isi").getBoundingClientRect(); return { atas: r.top, tinggi: r.height }; });
  const posisiBungkus = () => page.evaluate(() => { const r = document.querySelector(".pd-bungkus").getBoundingClientRect(); return { atas: r.top, bawah: r.bottom }; });

  await keAtasHalaman(page);
  const nol = await kenaIsi([20, 220, 450, 680, 880]);
  P.cek("B puncak halaman: tidak ada satu titik pun di layar yang mengenai lapisan penutup", nol.every((v) => v === false), nol);

  await keBagian(page, 0.5);
  const bungkus = await posisiBungkus();
  const tengah = bungkus.atas;
  const di = await kenaIsi([tengah + 120, tengah + 300, tengah + 420]);
  const luar = await kenaIsi([tengah - 40, tengah - 200, 40]);
  P.cek(`B separuh tersingkap (pembungkus mulai di y=${Math.round(tengah)}): titik di dalam kotaknya mengenai lapisan penutup`, di.every(Boolean), di);
  P.cek("B separuh tersingkap: titik di atas tepi pembungkus (masih dasbor) TIDAK mengenai lapisan penutup", luar.every((v) => v === false), luar);
  const isi50 = await posisiIsi();

  await keBagian(page, 0.8);
  const isi80 = await posisiIsi();
  const b80 = await posisiBungkus();
  P.cek("B lapisan isi DIAM sementara pembungkus naik (atas lapisan sama di 50% dan 80%)",
    hampir(isi50.atas, isi80.atas, 0.5) && hampir(isi50.atas, 0, 1) && b80.atas < tengah - 100, { isi50, isi80, bungkus50: tengah, bungkus80: b80.atas });

  await keDasar(page);
  const penuhDasar = await kenaIsi([100, 450, 800]);
  P.cek("B dasar halaman: seluruh layar adalah penutup", penuhDasar.every(Boolean), penuhDasar);
  if (process.env.FOTO) {
    await keBagian(page, 0.5); await page.screenshot({ path: `${process.env.FOTO}/penutup-separuh.png` });
    await keDasar(page); await page.screenshot({ path: `${process.env.FOTO}/penutup-dasar.png` });
  }
  await s.tutup();
}

/* ------------------------------------------------ C gerak */
if (jalan("C")) {
  const baca = (page) => page.evaluate(() => {
    const b = document.querySelector(".pd-bungkus");
    const cs = (sel) => getComputedStyle(b.querySelector(sel));
    return {
      penuh: b.dataset.penuh, tampak: b.dataset.tampak, isiPos: cs(".pd-isi").position,
      jalur: cs(".pd-jalur").animationName, aurora: cs(".pd-aurora").animationName,
      jalurJalan: cs(".pd-jalur").animationPlayState, judulTimeline: cs(".pd-judul").animationTimeline,
      judulOpasitas: parseFloat(cs(".pd-judul").opacity),
    };
  });
  for (const [judul, opsi, penuh] of [
    ["penuh", { gerak: "penuh" }, true], ["halus", { gerak: "halus" }, false],
    ["mati", { gerak: "mati" }, false], ["prefers-reduced-motion", { gerak: "penuh", reduce: true }, false],
  ]) {
    const s = await buka(opsi); const page = s.page;
    await keAtasHalaman(page);
    const jauh = await baca(page);
    await keBagian(page, 0.4);
    const sebagian = await baca(page);
    await keDasar(page);
    const dasar = await baca(page);
    P.cek(`C ${judul}: data-penuh = ${penuh ? "ya" : "tidak"}, lapisan isi ${penuh ? "fixed" : "absolute (bagian statis biasa)"}`,
      dasar.penuh === (penuh ? "ya" : "tidak") && dasar.isiPos === (penuh ? "fixed" : "absolute"), dasar);
    P.cek(`C ${judul}: jauh di bawah layar tidak ada animasi tak berhingga yang berjalan (strip dan aurora diam)`, jauh.tampak === "tidak" && jauh.jalur === "none" && jauh.aurora === "none", jauh);
    if (penuh) {
      P.cek("C penuh di dasar: strip berjalan (pd-geser, berjalan) dan aurora bernapas (pd-napas)", dasar.tampak === "ya" && dasar.jalur === "pd-geser" && dasar.jalurJalan === "running" && dasar.aurora === "pd-napas", dasar);
      P.cek("C penuh: kemunculan terhubung gulir (garis waktu --pd), judul belum penuh di 40% dan penuh di dasar",
        sebagian.judulTimeline.includes("--pd") && sebagian.judulOpasitas < 0.6 && hampir(dasar.judulOpasitas, 1, 0.001), { sebagian: sebagian.judulOpasitas, dasar: dasar.judulOpasitas, garis: sebagian.judulTimeline });
    } else {
      P.cek(`C ${judul}: tanpa animasi sama sekali di dasar (strip, aurora), judul tampil utuh sejak 40%`,
        dasar.jalur === "none" && dasar.aurora === "none" && hampir(sebagian.judulOpasitas, 1, 0.001) && !sebagian.judulTimeline.includes("--pd"), { dasar, sebagian });
    }
    await s.tutup();
  }
}

/* ------------------------------------------------ D kontras */
if (jalan("D")) {
  for (const tema of TEMA) {
    const s = await buka({ tema, gerak: "mati" }); const page = s.page;
    await keDasar(page);
    const ambang = tema === "kontras" ? 7 : 4.5;
    const judul = await rasioJudul(page);
    const opJudul = await page.evaluate(() => {
      let o = 1;
      for (let n = document.querySelector("#pd-judul"); n; n = n.parentElement) o *= parseFloat(getComputedStyle(n).opacity);
      return Math.round(o * 1000) / 1000;
    });
    P.cek(`D ${tema}: judul bergradien >= ${ambang}:1 pada piksel tintanya (terukur ${judul.rasio}) dan tanpa peredupan opacity (efektif ${opJudul})`,
      judul.rasio >= ambang && opJudul >= 0.999, { ...judul, opJudul });
    for (const [nama, sel, opsi] of [
      ["alis", ".pd-alis", {}], ["catatan privasi", ".pd-catatan", {}], ["pil besar", ".pd-pil-besar .pd-inti > span", {}],
      ["pil kecil", ".pd-pil-kecil > span", {}], ["butir strip", ".pd-kelompok li", { luruskanStrip: true }],
    ]) {
      const r = await rasioTeks(page, sel, opsi);
      P.cek(`D ${tema}: ${nama} "${r.teks}" >= ${ambang}:1 (terukur ${r.rasio}) dan tanpa peredupan opacity (efektif ${r.opasitas})`, r.rasio >= ambang && r.opasitas >= 0.999, r);
    }
    if (tema === "kontras") {
      // Aturan "tanpa hiasan" keputusan desain, bukan jaminan kontras (kontras tetap tinggi walau hiasan muncul),
      // jadi ditagih langsung dari gaya terhitung.
      const hiasan = await page.evaluate(() => [".pd-aurora", ".pd-kisi", ".pd-raksasa"].map((q) => {
        const e = document.querySelector(q);
        return e ? getComputedStyle(e).display : "(tidak ada)";
      }));
      P.cek("D kontras: aurora, kisi, dan kata raksasa tidak digambar (display none)", hiasan.every((d) => d === "none"), hiasan);
    }
    if (process.env.FOTO) await page.screenshot({ path: `${process.env.FOTO}/penutup-kontras-${tema}.png` });
    await s.tutup();
  }
  // Kasus terburuk gerak penuh: aurora di puncak napasnya (opasitas 1, skala 1,1) di belakang teks.
  for (const tema of ["gelap", "terang"]) {
    const s = await buka({ tema, gerak: "penuh" }); const page = s.page;
    await keDasar(page);
    await page.evaluate(() => {
      for (const a of document.querySelector(".pd-aurora").getAnimations()) { a.pause(); a.currentTime = 7999; }
    });
    await tunggu(page, 150);
    const judul = await rasioJudul(page);
    const catatan = await rasioTeks(page, ".pd-catatan");
    const alis = await rasioTeks(page, ".pd-alis");
    P.cek(`D ${tema} aurora di puncak napas: judul ${judul.rasio}, alis ${alis.rasio}, catatan ${catatan.rasio} semuanya >= 4,5:1`,
      judul.rasio >= 4.5 && alis.rasio >= 4.5 && catatan.rasio >= 4.5, { judul, alis, catatan });
    await s.tutup();
  }
}

/* ------------------------------------------------ E papan ketik */
if (jalan("E")) {
  for (const [judul, opsi] of [["penuh", { gerak: "penuh" }], ["mati", { gerak: "mati" }]]) {
    const s = await buka(opsi); const page = s.page;
    await keAtasHalaman(page);
    await page.evaluate(() => document.body.focus());
    let tekan = 0, masuk = false;
    while (tekan < 300 && !masuk) {
      await page.keyboard.press("Tab");
      tekan += 1;
      masuk = await page.evaluate(() => !!document.activeElement?.closest(".pd-isi"));
    }
    P.cek(`E ${judul}: Tab dari puncak sampai masuk ke penutup (${tekan} tekanan)`, masuk, tekan);
    await tunggu(page, 1400);
    const t = await page.evaluate(() => {
      const b = document.querySelector(".pd-bungkus").getBoundingClientRect();
      const f = document.activeElement.getBoundingClientRect();
      return { bawah: b.bottom, atas: b.top, innerH: window.innerHeight, f: { atas: f.top, bawah: f.bottom, kiri: f.left, kanan: f.right } };
    });
    P.cek(`E ${judul}: sesudah fokus masuk, halaman tergulir ke dasar (penutup terlihat utuh)`, hampir(t.bawah, t.innerH, 2) && hampir(t.atas, 0, 2), t);
    P.cek(`E ${judul}: tautan yang berfokus terlihat di dalam layar`, t.f.atas >= 0 && t.f.bawah <= t.innerH && t.f.kiri >= 0 && t.f.kanan <= 1440, t.f);

    // Seluruh perhentian di dalam penutup: terlihat, tidak tertutup, dan punya cincin fokus.
    const rinci = [];
    for (let n = 0; n < 9; n++) {
      const d = await page.evaluate(() => {
        const a = document.activeElement;
        if (!a?.closest(".pd-isi")) return null;
        const r = a.getBoundingClientRect();
        const tepat = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
        const cs = getComputedStyle(a);
        return {
          nama: (a.getAttribute("aria-label") || a.textContent || "").trim(),
          terlihat: r.width > 0 && r.height > 0 && r.top >= 0 && r.bottom <= window.innerHeight,
          tidakTertutup: !!tepat && a.contains(tepat),
          cincin: cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) >= 2,
        };
      });
      if (!d) break;
      rinci.push(d);
      await page.keyboard.press("Tab");
    }
    P.cek(`E ${judul}: tujuh perhentian Tab di dalam penutup (dua besar, empat kecil, satu ke atas)`, rinci.length === 7, rinci.map((r) => r.nama));
    P.cek(`E ${judul}: tiap perhentian terlihat penuh, tidak tertutup apa pun, dan punya cincin fokus`, rinci.every((r) => r.terlihat && r.tidakTertutup && r.cincin), rinci.filter((r) => !(r.terlihat && r.tidakTertutup && r.cincin)));

    // Enter pada "Kembali ke atas" mengembalikan ke puncak halaman.
    await page.focus("button.pd-atas");
    await page.keyboard.press("Enter");
    await tunggu(page, 1800);
    const y = await page.evaluate(() => window.scrollY);
    P.cek(`E ${judul}: Enter pada "Kembali ke atas" menggulir ke puncak (scrollY ${Math.round(y)})`, y <= 2, y);
    await s.tutup();
  }
}

/* ------------------------------------------------ F magnet */
if (jalan("F")) {
  for (const [judul, opsi, harapGeser] of [
    ["penuh", { gerak: "penuh" }, true], ["mati", { gerak: "mati" }, false],
    ["prefers-reduced-motion", { gerak: "penuh", reduce: true }, false],
  ]) {
    const s = await buka(opsi); const page = s.page;
    await keDasar(page);
    const t = await page.evaluate(() => { const r = document.querySelector(".pd-pil-besar").getBoundingClientRect(); return { x: r.left, y: r.top, w: r.width, h: r.height }; });
    await page.mouse.move(t.x + t.w * 0.3, t.y + t.h / 2);
    await page.mouse.move(t.x + t.w * 0.9, t.y + t.h * 0.8, { steps: 4 });
    await tunggu(page, 200);
    const geser = await page.evaluate(() => { const e = document.querySelector(".pd-pil-besar"); return { inline: e.style.transform, dihitung: getComputedStyle(e).transform }; });
    if (harapGeser) P.cek("F penuh: pil besar bergeser mengikuti penunjuk (transform inline tak nol)", /translate3d/.test(geser.inline) && geser.dihitung !== "none", geser);
    else P.cek(`F ${judul}: pil besar TIDAK bergeser`, geser.inline === "" && geser.dihitung === "none", geser);
    await page.mouse.move(8, 8);
    await tunggu(page, 1100);
    const lepas = await page.evaluate(() => { const e = document.querySelector(".pd-pil-besar"); return { inline: e.style.transform, dihitung: getComputedStyle(e).transform, animasi: e.getAnimations().length }; });
    P.cek(`F ${judul}: penunjuk pergi, pil kembali ke asal (tanpa transform tertinggal, tanpa animasi menggantung)`, lepas.inline === "" && lepas.dihitung === "none" && lepas.animasi === 0, lepas);
    await s.tutup();
  }
}

/* ------------------------------------------------ G isi dari data nyata, dan cetak */
if (jalan("G")) {
  const s = await buka({ gerak: "mati" }); const page = s.page;
  await keDasar(page);
  const g = await page.evaluate(async () => {
    const j = await (await fetch("/api/dasbor", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR ?? "" } })).json();
    const id = (n) => new Intl.NumberFormat("id-ID").format(n);
    // `?.` di seluruh akses: komponen yang dicabut harus jadi pemeriksaan GAGAL, bukan TypeError yang mematikan skrip.
    const sr = document.querySelector(".pd-sr")?.textContent ?? "";
    const dijalani = j.bahasa.filter((b) => b.persen > 0).length;
    const materi = j.bahasa.reduce((a, b) => a + b.materi, 0);
    const total = j.bahasa.reduce((a, b) => a + b.total_materi, 0);
    return {
      sr, alis: document.querySelector(".pd-alis")?.textContent.trim() ?? "", judul: document.querySelector("#pd-judul")?.textContent.trim() ?? "",
      sambut: document.querySelector(".sambut-sub")?.textContent.trim() ?? "(tidak ada)",
      harap: {
        level: `Level ${id(j.level)}, ${j.gelar}`, xp: `${id(j.xp)} XP`, materi: `${id(materi)} dari ${id(total)} materi dibaca`,
        kurikulum: `${id(dijalani)} kurikulum dijalani`, alis: `Hari ini: ${id(j.xp_hari_ini)} dari ${id(j.target_harian)} XP`,
        adaMateri: materi > 0, adaKurikulum: dijalani > 0,
      },
    };
  });
  P.cek("G ringkasan pembaca layar memuat level, gelar, dan XP persis seperti /api/dasbor", g.sr.includes(g.harap.level) && g.sr.includes(g.harap.xp), { sr: g.sr, harap: g.harap });
  P.cek("G ringkasan memuat materi dibaca dan kurikulum dijalani bila ada, dan tidak menulisnya bila nol",
    g.sr.includes(g.harap.materi) === g.harap.adaMateri && g.sr.includes(g.harap.kurikulum) === g.harap.adaKurikulum, { sr: g.sr, harap: g.harap });
  P.cek("G alis = kemajuan XP hari ini dan target harian dari data nyata", g.alis === g.harap.alis, { alis: g.alis, harap: g.harap.alis });
  // Kalimat pembuka dasbor (`.sambut-sub`) hanya tampil bila tidak ada kartu Lanjutkan atau antrean; di profil
  // yang punya keduanya, judul penutup justru satu-satunya tempat kalimat itu terlihat. Maka bersyarat.
  P.cek(`G judul penutup tidak kosong, dan bila dasbor menampilkan kalimat pembuka yang sama ia identik (sambut: ${g.sambut === "(tidak ada)" ? "tidak tampil" : "tampil"})`,
    g.judul !== "" && (g.sambut === "(tidak ada)" || g.judul === g.sambut), { judul: g.judul, sambut: g.sambut });
  P.cek("G ringkasan bersih (tanpa undefined, NaN, null, dash)", !/undefined|NaN|null|\[object|\u2014|\u2013/.test(g.sr + g.alis + g.judul), g.sr);
  await s.tutup();

  // SIMULASI: profil uji punya XP tetapi nol materi dibaca, jadi butir materi, streak, lencana, kurikulum,
  // dan kuis tidak pernah muncul di atas. Respons /api/dasbor diubah di SISI KLIEN (server tidak menulis apa pun)
  // supaya ketujuh butir tampil; yang diadu isi ringkasan dan strip dengan hitungan lurus dari data yang sama.
  const sim = await buka({ gerak: "mati" });
  let diubah = null;
  await sim.page.route(/\/api\/dasbor(\?|$)/, async (r) => {
    const resp = await r.fetch(); const j = await resp.json();
    j.streak = 5; j.badge_dimiliki = 3; j.kuis_jatuh_tempo = 4;
    j.bahasa[0].materi = 10; j.bahasa[0].persen = 25;
    diubah = j;
    await r.fulfill({ response: resp, body: JSON.stringify(j), contentType: "application/json" });
  });
  await sim.page.reload({ waitUntil: "load" });
  await sim.page.waitForSelector(".pd-bungkus");
  await keDasar(sim.page);
  const k = await sim.page.evaluate((j) => {
    const id = (n) => new Intl.NumberFormat("id-ID").format(n);
    const dijalani = j.bahasa.filter((b) => b.persen > 0).length;
    const materi = j.bahasa.reduce((a, b) => a + b.materi, 0);
    const total = j.bahasa.reduce((a, b) => a + b.total_materi, 0);
    const harap = [`Level ${id(j.level)}, ${j.gelar}`, `${id(j.xp)} XP`, `${id(materi)} dari ${id(total)} materi dibaca`,
      `${id(j.streak)} hari berturut-turut`, `${id(j.badge_dimiliki)} dari ${id(j.badge_total)} lencana`,
      `${id(dijalani)} kurikulum dijalani`, `${id(j.kuis_jatuh_tempo)} kuis menunggu diulang`];
    const kelompok = [...document.querySelectorAll(".pd-kelompok")].map((u) => [...u.querySelectorAll("li")].map((li) => li.textContent));
    return { harap, sr: document.querySelector(".pd-sr")?.textContent ?? "", kelompok: kelompok.length, sama: kelompok.every((l) => JSON.stringify(l) === JSON.stringify(harap)) };
  }, diubah ?? { level: 0, gelar: "", xp: 0, bahasa: [], badge_total: 0 });
  P.cek("G2 (simulasi respons) ringkasan memuat ketujuh butir, urut, persis hitungan lurus dari data", diubah !== null && k.sr === k.harap.join(", ") + ".", { sr: k.sr, harap: k.harap });
  P.cek("G2 (simulasi respons) tiap salinan strip memuat ketujuh butir yang sama, urut (delapan kelompok)", k.kelompok === 8 && k.sama, { kelompok: k.kelompok, sama: k.sama });
  P.cek("G2 (simulasi respons) tanpa galat konsol, termasuk peringatan key ganda React", sim.konsol.filter(bukanGerutan).length === 0, sim.konsol.filter(bukanGerutan));
  await sim.tutup();

  const c = await buka({ gerak: "penuh" });
  await c.page.emulateMedia({ media: "print" });
  const p = await c.page.evaluate(() => getComputedStyle(document.querySelector(".pd-bungkus")).display);
  P.cek("G cetak: penutup disembunyikan (display none), kertas tidak memuat layar yang hanya bermakna di layar", p === "none", p);
  await c.tutup();
}

/* ------------------------------------------------ H profil baru (XP 0) */
if (jalan("H")) {
  const s = await mulai({ lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/dasbor", tunggu: ".tbl-utama.tbl-besar" });
  const page = s.page;
  await keDasar(page);
  const h = await page.evaluate(() => ({
    pembungkus: document.querySelectorAll(".pd-bungkus").length, isi: document.querySelectorAll(".pd-isi").length,
  }));
  P.cek("H profil baru (XP 0): layar mulai tidak punya penutup (tanpa pembungkus, tanpa lapisan)", h.pembungkus === 0 && h.isi === 0, h);
  await s.tutup();
}

P.selesai();
