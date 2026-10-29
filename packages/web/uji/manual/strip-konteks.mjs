/* Strip konteks ("bar bab": tombol kembali, bab, judul, posisi, panah) selebar ISI, bukan selebar jendela.
 *
 * Dulu `#konteks` membentang selebar `#panggung`: di jendela 1853 px tombol kembalinya di x=16 dan
 * panahnya di x=1837, sementara isi pembaca materi cuma 271 sampai 1583. Sekarang lebarnya dibatasi
 * `--konteks-maks` (1312 px, lebar tiga kolom pembaca materi) dan ditengahkan.
 *
 *   BELAJAR_URL=http://127.0.0.1:7792/ node uji/manual/strip-konteks.mjs
 *
 * Hanya GET, terhadap server berprofil SEMENTARA (lihat `lib.mjs`); menolak port 7777.
 */

import { URL_DASAR, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Strip konteks selebar isi");
const dekat = (a, b, t = 1) => Math.abs(a - b) <= t;
const ukur = (page) => page.evaluate(() => {
  const k = (q) => { const e = document.querySelector(q); if (!e) return null; const b = e.getBoundingClientRect(); return { kiri: b.left, kanan: b.right, w: b.width, h: b.height }; };
  const peta = document.querySelector(".materi-peta");
  return {
    strip: k("#konteks"), balik: k(".konteks-balik"), langkah: k(".konteks-langkah"), rel: k(".materi-rel"),
    peta: peta && getComputedStyle(peta).display !== "none" ? k(".materi-peta") : null,
    meluber: document.documentElement.scrollWidth - document.documentElement.clientWidth,
  };
});

for (const [lebar, tinggi] of [[1280, 800], [1440, 900], [1853, 1000], [2560, 1300]]) {
  const s = await mulai({ lebar, tinggi, tema: "terang", gerak: "mati", hash: "#/materi/html/1", tunggu: ".materi-tata" });
  const r = await ukur(s.page);
  const n = `${lebar}px materi`;
  P.cek(`${n}: strip tidak lebih lebar dari 1312 px`, !!r.strip && r.strip.w <= 1312.5, r.strip);
  P.cek(`${n}: strip ditengahkan di jendela`, !!r.strip && dekat(r.strip.kiri, lebar - r.strip.kanan), r.strip);
  P.cek(`${n}: tombol kembali dan panah berada di dalam strip`, !!r.strip && !!r.balik && !!r.langkah && r.balik.kiri >= r.strip.kiri && r.langkah.kanan <= r.strip.kanan + 0.5, { balik: r.balik, langkah: r.langkah });
  P.cek(`${n}: tinggi strip tetap 44 px`, !!r.strip && dekat(r.strip.h, 44), r.strip?.h);
  P.cek(`${n}: halaman tidak meluber ke samping`, r.meluber <= 0, r.meluber);
  if (lebar >= 1440) {
    P.cek(`${n}: tepi strip sejajar dengan daftar bab di kiri dan peta halaman di kanan`, !!r.rel && !!r.peta && dekat(r.strip.kiri, r.rel.kiri) && dekat(r.strip.kanan, r.peta.kanan), { strip: r.strip, rel: r.rel, peta: r.peta });
  } else {
    P.cek(`${n}: di jendela sempit strip memenuhi lebar jendela (perilaku lama tidak berubah)`, !!r.strip && dekat(r.strip.w, lebar), r.strip);
  }
  await s.tutup();
}

for (const [hash, tunggu] of [["#/bahasa/html", "#konteks"], ["#/latihan/html/0", "#konteks"]]) {
  const s = await mulai({ lebar: 1853, tinggi: 1000, tema: "terang", gerak: "mati", hash, tunggu });
  const r = await ukur(s.page);
  P.cek(`1853px ${hash}: layar lain yang memakai strip yang sama juga tidak lebih lebar dari 1312 px`, !!r.strip && r.strip.w <= 1312.5 && dekat(r.strip.kiri, 1853 - r.strip.kanan) && r.meluber <= 0, r.strip);
  await s.tutup();
}

P.selesai();
