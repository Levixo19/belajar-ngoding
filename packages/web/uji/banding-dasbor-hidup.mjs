/* Memeriksa bagian murni "dasbor hidup" (`layar/dasbor-hidup-teks.ts`, `komponen/angka-hidup-teks.ts`).
 *
 * Tidak ada JS lama untuk diadu (susunannya baru) dan tidak ada sisi Python untuk direkam, jadi yang
 * ditagih adalah SIFAT yang dijanjikan komentar kepala modulnya, dengan oracle yang ditulis sendiri
 * di sini (hitungan lurus, bukan salinan rumusnya) atas kasus tangan ditambah ribuan kasus acak
 * berbenih tetap:
 *
 *   [tahap]   kemajuan angka: berhenti tepat di ujung, aman untuk t negatif atau bukan angka, monoton,
 *             bulat, selalu di antara dua ujungnya, melambat di ujung (ease-out)
 *   [durasi]  antara 450 dan 1.100 ms, tidak menurun terhadap jarak, simetris
 *   [rel]     bahasa untuk rel: hanya yang dijalani, posisi sekarang di depan, sisanya menurut persen,
 *             stabil pada persen sama, paling banyak MAKS_REL, masukan tidak diubah
 *   [teks]    tulisan panel: pembulatan biasa, lebar bilah dijepit 0..100
 *   [stat]    tiga angka hari ini: urutan, nilai, satuan, bilah, dan tanda tercapai
 *   [lencana] "dimiliki/total"
 *
 *     node --experimental-strip-types uji/banding-dasbor-hidup.mjs
 */

import { durasiAngka, tahapAngka } from "../src/komponen/angka-hidup-teks.ts";
import {
  MAKS_REL, statHariIni, teksLencana, teksRel, urutRel,
} from "../src/layar/dasbor-hidup-teks.ts";

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
const R = acak(20261029);
const bulat = (n) => Math.floor(R() * n);
/** Oracle format angka Indonesia: pemisah ribuan titik, tanpa pecahan. */
const idr = (n) => new Intl.NumberFormat("id-ID").format(n);

/* ----------------------------------------------------------------------- tahap */
{
  adu("tahap", "t = 0 mengembalikan dari", tahapAngka(10, 50, 0) === 10);
  adu("tahap", "t = 1 mengembalikan ke persis", tahapAngka(10, 50, 1) === 50);
  adu("tahap", "t melewati 1 tetap ke (bukan melampaui)", tahapAngka(10, 50, 1.5) === 50 && tahapAngka(10, 50, 99) === 50);
  adu("tahap", "t negatif aman: dari (cap waktu rAF bisa lebih awal dari saat diminta)", tahapAngka(10, 50, -0.3) === 10 && tahapAngka(10, 50, -1e9) === 10);
  adu("tahap", "t bukan angka aman: dari", tahapAngka(10, 50, NaN) === 10 && tahapAngka(10, 50, undefined) === 10);
  adu("tahap", "ease-out: pada separuh waktu sudah 87,5 persen jalan (dibulatkan 88)", tahapAngka(0, 100, 0.5) === 88);
  adu("tahap", "turun juga bekerja (ke < dari)", tahapAngka(100, 0, 0.5) === 13 && tahapAngka(100, 0, 1) === 0);
  adu("tahap", "dari sama dengan ke tidak bergerak", tahapAngka(7, 7, 0.3) === 7);
  for (let n = 0; n < 2000; n++) {
    const dari = bulat(20000);
    const ke = bulat(20000);
    const arah = ke >= dari ? 1 : -1;
    let sebelum = tahapAngka(dari, ke, 0);
    let baik = sebelum === dari;
    for (let i = 1; i <= 40; i++) {
      const v = tahapAngka(dari, ke, i / 40);
      const antara = v >= Math.min(dari, ke) && v <= Math.max(dari, ke);
      baik = baik && Number.isInteger(v) && antara && (v - sebelum) * arah >= 0;
      sebelum = v;
    }
    baik = baik && sebelum === ke;
    adu("tahap", `acak #${n}: ${dari} ke ${ke} bulat, di antara ujung, monoton, berakhir di ke`, baik, [dari, ke]);
    if (ke !== dari) {
      const tengah = tahapAngka(dari, ke, 0.5);
      const lurus = (dari + ke) / 2;
      adu("tahap", `acak #${n}: melambat di ujung (separuh waktu melewati titik tengah)`, arah > 0 ? tengah >= lurus : tengah <= lurus, [dari, ke, tengah]);
    }
  }
}

/* ---------------------------------------------------------------------- durasi */
{
  adu("durasi", "jarak nol: 450", durasiAngka(5, 5) === 450);
  adu("durasi", "jarak sangat jauh: 1.100", durasiAngka(0, 1e12) === 1100);
  adu("durasi", "satu satuan: 450 ditambah log10(2) kali 220", durasiAngka(0, 1) === 450 + Math.round(Math.log10(2) * 220));
  let lalu = durasiAngka(0, 0);
  let naik = true;
  for (let j = 1; j <= 5000; j += 7) {
    const d = durasiAngka(0, j);
    naik = naik && d >= lalu && d >= 450 && d <= 1100;
    lalu = d;
  }
  adu("durasi", "tidak menurun terhadap jarak dan selalu 450..1100", naik);
  for (let n = 0; n < 300; n++) {
    const a = bulat(50000), b = bulat(50000);
    adu("durasi", `acak #${n}: simetris (${a}, ${b})`, durasiAngka(a, b) === durasiAngka(b, a));
  }
}

/* ------------------------------------------------------------------------- rel */
function bahasa(i, persen) {
  const total = 20 + bulat(60);
  return { key: "b" + i, label: "Bahasa " + i, siap: true, materi: Math.min(total, Math.round((persen / 100) * total)), total_materi: total, persen };
}
{
  adu("rel", "MAKS_REL enam", MAKS_REL === 6);
  const tiga = [bahasa(0, 10), bahasa(1, 60), bahasa(2, 30)];
  adu("rel", "tanpa posisi: urut persen terbesar", urutRel(tiga, null).map((b) => b.key).join() === "b1,b2,b0");
  adu("rel", "posisi di depan walau persennya kecil", urutRel(tiga, "b0").map((b) => b.key).join() === "b0,b1,b2");
  adu("rel", "posisi yang persennya nol tidak ikut (belum dijalani)", urutRel([bahasa(0, 0), bahasa(1, 5)], "b0").map((b) => b.key).join() === "b1");
  adu("rel", "semua nol: kosong", urutRel([bahasa(0, 0), bahasa(1, 0)], null).length === 0);
  adu("rel", "posisi tidak dikenal diabaikan", urutRel(tiga, "tidak-ada").map((b) => b.key).join() === "b1,b2,b0");
  for (let n = 0; n < 600; n++) {
    const jumlah = bulat(14);
    const daftar = Array.from({ length: jumlah }, (_, i) => bahasa(i, bulat(4) === 0 ? 0 : [5, 12, 12, 40, 40, 73, 100][bulat(7)]));
    const salinan = JSON.stringify(daftar);
    const posisi = bulat(3) === 0 ? null : "b" + bulat(Math.max(1, jumlah));
    const maks = bulat(4) === 0 ? bulat(9) : undefined;
    const hasil = maks === undefined ? urutRel(daftar, posisi) : urutRel(daftar, posisi, maks);
    // oracle: dijalani, posisi dulu, persen menurun, urutan semula pada seri, lalu dipotong
    const batas = maks === undefined ? 6 : maks;
    const kandidat = daftar.map((b, i) => ({ b, i })).filter((x) => x.b.persen > 0);
    kandidat.sort((x, y) => (Number(y.b.key === posisi) - Number(x.b.key === posisi)) || (y.b.persen - x.b.persen) || (x.i - y.i));
    const harap = kandidat.slice(0, batas).map((x) => x.b.key);
    adu("rel", `acak #${n}: persis oracle (posisi ${posisi}, maks ${batas})`, hasil.map((b) => b.key).join() === harap.join(), { hasil: hasil.map((b) => b.key), harap });
    adu("rel", `acak #${n}: masukan tidak diubah`, JSON.stringify(daftar) === salinan);
    adu("rel", `acak #${n}: tidak lebih dari batas dan hanya yang persen > 0`, hasil.length <= batas && hasil.every((b) => b.persen > 0));
  }
}

/* ------------------------------------------------------------------------ teks */
{
  const t = teksRel({ key: "x", label: "X", siap: true, materi: 14, total_materi: 23, persen: 43.4 });
  adu("teks", "persen dibulatkan, materi apa adanya", t.persen === "43% selesai" && t.materi === "14/23 materi", t);
  adu("teks", "setengah dibulatkan ke atas (42,5 jadi 43)", teksRel({ key: "x", label: "X", siap: true, materi: 1, total_materi: 2, persen: 42.5 }).persen === "43% selesai");
  adu("teks", "lebar bilah dijepit: 130 jadi 100", teksRel({ key: "x", label: "X", siap: true, materi: 1, total_materi: 1, persen: 130 }).isi === 100);
  adu("teks", "lebar bilah dijepit: negatif jadi 0", teksRel({ key: "x", label: "X", siap: true, materi: 0, total_materi: 1, persen: -4 }).isi === 0);
  adu("teks", "persen 100 ditulis 100% selesai", teksRel({ key: "x", label: "X", siap: true, materi: 5, total_materi: 5, persen: 100 }).persen === "100% selesai");
  for (let n = 0; n < 300; n++) {
    const persen = R() * 130 - 5;
    const b = { key: "x", label: "X", siap: true, materi: bulat(60), total_materi: 1 + bulat(60), persen };
    const r = teksRel(b);
    adu("teks", `acak #${n}: tulisan dan jepitan`, r.persen === `${Math.round(persen)}% selesai` && r.materi === `${b.materi}/${b.total_materi} materi` && r.isi === Math.max(0, Math.min(100, persen)), r);
  }
}

/* ------------------------------------------------------------------------ stat */
function dasbor(o = {}) {
  return {
    xp: o.xp ?? 501, level: o.level ?? 5, gelar: o.gelar ?? "Penjelajah", di_level: o.di_level ?? 42, butuh_level: o.butuh_level ?? 197,
    streak: o.streak ?? 6, xp_hari_ini: o.xp_hari_ini ?? 30, xp_kemarin: o.xp_kemarin ?? 20, hari_belajar_terakhir: o.hari_belajar_terakhir ?? null,
    target_harian: o.target_harian ?? 60, badge_dimiliki: o.badge_dimiliki ?? 5, badge_total: o.badge_total ?? 22, heatmap: [], bahasa: [], langkah: [], kuis_jatuh_tempo: 0,
  };
}
{
  const s = statHariIni(dasbor());
  adu("stat", "tiga butir berurutan: hari, streak, level", s.map((x) => x.kunci).join() === "hari,streak,level");
  adu("stat", "hari: nilai, satuan, kemarin, bilah, belum tercapai", s[0].nilai === 30 && s[0].satuan === "dari 60 XP hari ini" && s[0].ket === "Kemarin 20 XP" && s[0].isi === 50 && s[0].capai === false, s[0]);
  adu("stat", "streak: nilai dan satuan", s[1].nilai === 6 && s[1].satuan === "hari berturut-turut" && s[1].isi === -1 && s[1].ket === "", s[1]);
  adu("stat", "level: nilai, gelar, rincian menuju level berikutnya", s[2].nilai === 5 && s[2].satuan === "Penjelajah" && s[2].ket === "501 XP, 42 dari 197 menuju level 6", s[2]);
  adu("stat", "level: bilah = di_level per butuh_level", Math.abs(s[2].isi - (42 / 197) * 100) < 1e-9, s[2].isi);
  const capai = statHariIni(dasbor({ xp_hari_ini: 60 }))[0];
  adu("stat", "tepat di target: tercapai, satuan menyebutnya, bilah penuh", capai.capai === true && capai.satuan === "XP hari ini · target 60 tercapai" && capai.isi === 100, capai);
  const lewat = statHariIni(dasbor({ xp_hari_ini: 500 }))[0];
  adu("stat", "jauh melewati target: bilah dijepit 100", lewat.isi === 100 && lewat.capai === true, lewat);
  const nol = statHariIni(dasbor({ streak: 0 }))[1];
  adu("stat", "tanpa streak: satuan jujur, nilai nol", nol.nilai === 0 && nol.satuan === "belum ada hari berurutan", nol);
  adu("stat", "target nol tidak membagi dengan nol", Number.isFinite(statHariIni(dasbor({ target_harian: 0, xp_hari_ini: 0 }))[0].isi));
  const tiga = new Date(); tiga.setDate(tiga.getDate() - 3);
  const iso = `${tiga.getFullYear()}-${String(tiga.getMonth() + 1).padStart(2, "0")}-${String(tiga.getDate()).padStart(2, "0")}`;
  const celah = statHariIni(dasbor({ streak: 0, hari_belajar_terakhir: iso }))[1];
  const hariTeks = tiga.toLocaleDateString("id-ID", { weekday: "long", day: "numeric", month: "long" });
  adu("stat", "streak putus: keterangan celah dengan tanggal dan selisih hari", celah.ket === `Terakhir belajar ${hariTeks}, 3 hari lalu`, celah.ket);
  adu("stat", "streak hidup: tanpa keterangan celah walau tanggal terakhir ada", statHariIni(dasbor({ streak: 4, hari_belajar_terakhir: iso }))[1].ket === "");
  for (let n = 0; n < 400; n++) {
    const target = bulat(5) === 0 ? 0 : 20 + bulat(200);
    const d = dasbor({
      xp: bulat(90000), level: 1 + bulat(40), di_level: bulat(300), butuh_level: bulat(5) === 0 ? 0 : 50 + bulat(400),
      streak: bulat(4) === 0 ? 0 : bulat(60), xp_hari_ini: bulat(400), xp_kemarin: bulat(300), target_harian: target,
    });
    const r = statHariIni(d);
    const kurang = Math.max(0, d.target_harian - d.xp_hari_ini);
    const ok = r.length === 3
      && r[0].nilai === d.xp_hari_ini && r[0].capai === (kurang === 0)
      && r[0].isi === Math.min(100, (d.xp_hari_ini / Math.max(1, d.target_harian)) * 100)
      && r[0].satuan === (kurang ? `dari ${idr(d.target_harian)} XP hari ini` : `XP hari ini · target ${idr(d.target_harian)} tercapai`)
      && r[0].ket === `Kemarin ${idr(d.xp_kemarin)} XP`
      && r[1].nilai === d.streak && r[1].satuan === (d.streak ? "hari berturut-turut" : "belum ada hari berurutan")
      && r[2].nilai === d.level && r[2].satuan === d.gelar
      && r[2].ket === `${idr(d.xp)} XP, ${idr(d.di_level)} dari ${idr(d.butuh_level)} menuju level ${idr(d.level + 1)}`
      && r[2].isi === Math.min(100, (d.di_level / Math.max(1, d.butuh_level)) * 100)
      && r.every((x) => !/undefined|NaN|null|Infinity/.test(JSON.stringify(x)));
    adu("stat", `acak #${n}: persis oracle dan bersih`, ok, r);
  }
}

/* --------------------------------------------------------------------- lencana */
{
  adu("lencana", "dimiliki per total", teksLencana(dasbor({ badge_dimiliki: 5, badge_total: 22 })) === "5/22");
  adu("lencana", "nol dimiliki tetap ditulis (angka, bukan teguran di sini)", teksLencana(dasbor({ badge_dimiliki: 0, badge_total: 22 })) === "0/22");
}

console.log(gagal ? `GAGAL: ${gagal} dari ${cacah} perbandingan` : `COCOK: ${cacah} perbandingan, isi dasbor hidup sesuai janji kepala modulnya`);
process.exit(gagal ? 1 : 0);
