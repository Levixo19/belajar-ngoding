/* Memeriksa isi penutup dasbor (`layar/penutup-teks.ts`).
 *
 * Tidak ada JS lama untuk diadu (layarnya baru) dan tidak ada sisi Python untuk
 * direkam, jadi yang ditagih adalah SIFAT yang dijanjikan komentar kepala modulnya,
 * dengan oracle yang ditulis sendiri di sini (hitungan lurus, bukan salinan
 * rumusnya) atas kasus tangan ditambah ratusan profil acak berbenih tetap:
 *
 *   [butir]    dua butir pertama tetap; sisanya HANYA bila bernilai
 *   [hitung]   tiap angka sama dengan hitungan lurus dari data, tanpa pemotongan
 *   [urutan]   urutan butir tetap, tiap butir unik (dipakai sebagai key React)
 *   [bersih]   tanpa undefined, NaN, nol yang menegur, atau dash
 *   [judul]    judul = kalimat pembuka dasbor, alis = kemajuan hari ini
 *   [tautan]   tujuan sama dengan bilah atas, tidak ada yang baru
 *
 *     node --experimental-strip-types uji/banding-penutup.mjs
 */

import { readFileSync } from "node:fs";

import {
  KATA_RAKSASA, TAUTAN_KECIL, TAUTAN_UTAMA,
  alisPenutup, butirStrip, judulPenutup, ringkasStrip,
} from "../src/layar/penutup-teks.ts";
import { kalimatPembuka } from "../src/layar/dasbor-teks.ts";
import { NAMA_IKON } from "../src/komponen/ikon-bentuk.ts";

let cacah = 0;
let gagal = 0;
function adu(kategori, nama, ok, rinci = "") {
  cacah += 1;
  if (!ok) {
    gagal += 1;
    console.error(`[${kategori}] ${nama}${rinci === "" ? "" : "  " + JSON.stringify(rinci)}`);
  }
}

function acak(benih) {
  let a = benih >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const R = acak(20261028);
const bulat = (n) => Math.floor(R() * n);
/** Oracle format angka Indonesia: pemisah ribuan titik, tanpa pecahan. */
const idr = (n) => new Intl.NumberFormat("id-ID").format(n);

const GELAR = ["Pemula", "Penjelajah", "Arsitek", "Penjaga Bintang"];
function profil(o = {}) {
  const bahasa = o.bahasa ?? Array.from({ length: bulat(13) }, (_, i) => {
    const total = 20 + bulat(80);
    const materi = bulat(3) === 0 ? 0 : bulat(total + 1);
    return { key: "b" + i, label: "Bahasa " + i, siap: true, materi, total_materi: total, persen: materi === 0 ? 0 : Math.max(1, Math.round((materi / total) * 100)) };
  });
  return {
    xp: o.xp ?? 1 + bulat(20000), level: o.level ?? 1 + bulat(40), gelar: o.gelar ?? GELAR[bulat(GELAR.length)],
    di_level: 0, butuh_level: 100, streak: o.streak ?? bulat(40), xp_hari_ini: o.xp_hari_ini ?? bulat(120), target_harian: o.target_harian ?? 60,
    badge_dimiliki: o.badge_dimiliki ?? bulat(23), badge_total: o.badge_total ?? 22, heatmap: [], bahasa, langkah: [], kuis_jatuh_tempo: o.kuis_jatuh_tempo ?? bulat(9),
  };
}

/* ------------------------------------------------------------------- kasus tangan */
{
  const d = profil({ xp: 9666, level: 27, gelar: "Arsitek", streak: 1, badge_dimiliki: 0, kuis_jatuh_tempo: 0, bahasa: [
    { key: "py", label: "Python", siap: true, materi: 10, total_materi: 40, persen: 25 },
    { key: "js", label: "JavaScript", siap: true, materi: 0, total_materi: 44, persen: 0 },
  ] });
  const b = butirStrip(d);
  adu("butir", "dua butir pertama tetap", b[0] === "Level 27, Arsitek" && b[1] === `${idr(9666)} XP`, b);
  adu("butir", "materi dibaca dihitung dari jumlah, bukan dari satu bahasa", b[2] === `10 dari 84 materi dibaca`, b);
  adu("butir", "streak 1 tidak ditulis (hanya 2 ke atas)", !b.some((x) => /berturut/.test(x)), b);
  adu("butir", "lencana nol tidak ditulis", !b.some((x) => /lencana/.test(x)), b);
  adu("butir", "kuis nol tidak ditulis", !b.some((x) => /kuis/.test(x)), b);
  adu("butir", "satu kurikulum dijalani (yang persennya nol tidak dihitung)", b.includes("1 kurikulum dijalani"), b);
  adu("butir", "ringkasan = butir digabung koma, berakhir titik", ringkasStrip(d) === b.join(", ") + ".", ringkasStrip(d));

  const penuh = profil({ xp: 1250000, level: 5, gelar: "Pemula", streak: 12, badge_dimiliki: 3, badge_total: 22, kuis_jatuh_tempo: 4, bahasa: [
    { key: "a", label: "A", siap: true, materi: 1, total_materi: 1000, persen: 1 },
  ] });
  const p = butirStrip(penuh);
  adu("hitung", "angka besar memakai pemisah ribuan Indonesia", p[1] === "1.250.000 XP" && p[2] === "1 dari 1.000 materi dibaca", p);
  adu("urutan", "urutan tetap: level, XP, materi, streak, lencana, kurikulum, kuis", p.length === 7
    && /^Level/.test(p[0]) && /XP$/.test(p[1]) && /materi dibaca$/.test(p[2]) && /berturut-turut$/.test(p[3])
    && /lencana$/.test(p[4]) && /kurikulum dijalani$/.test(p[5]) && /menunggu diulang$/.test(p[6]), p);
  adu("hitung", "streak 2 sudah ditulis", butirStrip(profil({ streak: 2 })).some((x) => x === "2 hari berturut-turut"));

  // Semua materi nol: butir materi tidak ditulis (bukan "0 dari 40 materi dibaca").
  const kosong = butirStrip(profil({ bahasa: [{ key: "a", label: "A", siap: true, materi: 0, total_materi: 40, persen: 0 }], streak: 0, badge_dimiliki: 0, kuis_jatuh_tempo: 0 }));
  adu("butir", "tanpa satu pun materi dibaca: hanya dua butir tetap", kosong.length === 2, kosong);

  // Cacat yang ditemukan membaca sumber oracle: dijalaniDasbor memotong di enam untuk bento.
  const sepuluh = profil({ bahasa: Array.from({ length: 10 }, (_, i) => ({ key: "k" + i, label: "K" + i, siap: true, materi: 5, total_materi: 50, persen: 10 })) });
  adu("hitung", "sepuluh kurikulum dijalani ditulis 10, bukan terpotong di 6", butirStrip(sepuluh).includes("10 kurikulum dijalani"), butirStrip(sepuluh));
}

/* --------------------------------------------------------------------- acak */
const TERLARANG = /undefined|NaN|null|\[object|Infinity|-\d/;
for (let n = 0; n < 400; n++) {
  const d = profil();
  const b = butirStrip(d);
  const dijalani = d.bahasa.filter((x) => x.persen > 0).length;
  const materi = d.bahasa.reduce((a, x) => a + x.materi, 0);
  const total = d.bahasa.reduce((a, x) => a + x.total_materi, 0);
  const harap = [`Level ${idr(d.level)}, ${d.gelar}`, `${idr(d.xp)} XP`];
  if (materi > 0 && total > 0) harap.push(`${idr(materi)} dari ${idr(total)} materi dibaca`);
  if (d.streak >= 2) harap.push(`${idr(d.streak)} hari berturut-turut`);
  if (d.badge_dimiliki > 0) harap.push(`${idr(d.badge_dimiliki)} dari ${idr(d.badge_total)} lencana`);
  if (dijalani > 0) harap.push(`${idr(dijalani)} kurikulum dijalani`);
  if (d.kuis_jatuh_tempo > 0) harap.push(`${idr(d.kuis_jatuh_tempo)} kuis menunggu diulang`);
  adu("hitung", `acak #${n}: butir persis hitungan lurus dari data`, JSON.stringify(b) === JSON.stringify(harap), { b, harap });
  adu("urutan", `acak #${n}: tiap butir unik (dipakai sebagai key React)`, new Set(b).size === b.length, b);
  adu("butir", `acak #${n}: antara dua dan tujuh butir`, b.length >= 2 && b.length <= 7, b.length);
  adu("bersih", `acak #${n}: tanpa undefined, NaN, atau angka negatif`, b.every((x) => !TERLARANG.test(x)), b);
  adu("bersih", `acak #${n}: tidak ada butir yang menegur dengan nol`, b.every((x) => !/^0 /.test(x) && !/\b0 (hari|kuis|dari)\b/.test(x)), b);
  adu("bersih", `acak #${n}: tanpa dash`, b.every((x) => !x.includes("\u2014") && !x.includes("\u2013")), b);
  adu("judul", `acak #${n}: judul = kalimat pembuka dasbor`, judulPenutup(d) === kalimatPembuka(d), judulPenutup(d));
  adu("judul", `acak #${n}: alis = kemajuan hari ini dengan angka yang sama`, alisPenutup(d) === `Hari ini: ${idr(d.xp_hari_ini)} dari ${idr(d.target_harian)} XP`, alisPenutup(d));
}

/* -------------------------------------------------------------------- tautan */
{
  const semua = [...TAUTAN_UTAMA, ...TAUTAN_KECIL];
  const cangkang = readFileSync(new URL("../src/Cangkang.tsx", import.meta.url), "utf8");
  adu("tautan", "dua pil besar dan empat pil kecil", TAUTAN_UTAMA.length === 2 && TAUTAN_KECIL.length === 4, [TAUTAN_UTAMA.length, TAUTAN_KECIL.length]);
  adu("tautan", "href unik, semuanya hash rute", new Set(semua.map((t) => t.href)).size === semua.length && semua.every((t) => /^#\/[a-z]+$/.test(t.href)), semua.map((t) => t.href));
  adu("tautan", "label unik dan tidak kosong", new Set(semua.map((t) => t.label)).size === semua.length && semua.every((t) => t.label.trim() !== ""));
  for (const t of semua) {
    adu("tautan", `${t.label}: ikon ada di keluarga ikon aplikasi`, NAMA_IKON.includes(t.ikon), t.ikon);
    adu("tautan", `${t.label}: tujuan sama dengan butir bilah atas (tidak ada tujuan baru)`, cangkang.includes(`"${t.href}"`), t.href);
  }
  adu("tautan", "tidak ada tombol beraksen kedua: tautan Dasbor tidak ikut", !semua.some((t) => t.href === "#/dasbor"));
  adu("tautan", "kata raksasa tidak kosong dan satu kata", /^[a-z]+$/.test(KATA_RAKSASA), KATA_RAKSASA);
  for (const t of semua) {
    adu("bersih", `${t.label}: tanpa dash`, !t.label.includes("\u2014") && !t.label.includes("\u2013"));
  }
}

console.log(gagal ? `GAGAL: ${gagal} dari ${cacah} perbandingan` : `COCOK: ${cacah} perbandingan, isi penutup dasbor sesuai janji kepala modulnya`);
process.exit(gagal ? 1 : 0);
