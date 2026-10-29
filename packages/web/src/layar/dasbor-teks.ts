/* Bagian MURNI dasbor. Port dari `webapp/statik/js/layar-belajar.js`.
 *
 * Dasbor adalah layar yang paling banyak MEMUTUSKAN tanpa menggambar apa pun
 * yang kelihatan salah kalau keputusannya meleset: ambang tingkat bara, jeda
 * terpanjang, paket "punya 30 menit", pembanding XP kemarin, dan empat cabang
 * kalimat pembuka. Semuanya angka, dan angka yang salah di dasbor tampil
 * dengan sangat yakin.
 *
 * Satu aturan yang tidak boleh hilang: **tidak ada satu pun persen, XP, atau
 * "hari belajar" yang dihitung ULANG di sini.** Semuanya datang dari
 * `/api/dasbor` -- `progress.py` untuk XP dan streak, `saran.py` untuk antrean
 * dan tantangan, `bab.py` untuk posisi. Yang dikerjakan berkas ini memformat
 * dan memilih.
 *
 * Pemisahannya dari `.tsx` punya sebab teknis: Node melucuti TIPE dari `.ts`
 * tapi tidak melucuti JSX, jadi hanya berkas `.ts` yang bisa diimpor
 * `uji/banding-dasbor.mjs`.
 */

import { angka } from "../util.ts";
import { selisihHari, tanggalLokal, tanggalRamah } from "../waktu.ts";

/* ------------------------------------------------------------ bentuk data */

export interface Langkah {
  tipe: string;
  bahasa: string;
  label_bahasa: string;
  judul: string;
  alasan: string;
  indeks: number;
  menit?: number;
}

export interface SelBara {
  tanggal: string;
  xp: number;
}

export interface BahasaDasbor {
  key: string;
  label: string;
  siap: boolean;
  materi: number;
  total_materi: number;
  persen: number;
}

export interface DataDasbor {
  xp: number;
  level: number;
  gelar: string;
  di_level: number;
  butuh_level: number;
  streak: number;
  xp_hari_ini: number;
  xp_kemarin?: number;
  hari_belajar_terakhir?: string | null;
  target_harian: number;
  badge_dimiliki: number;
  badge_total: number;
  heatmap: SelBara[];
  bahasa: BahasaDasbor[];
  langkah: Langkah[];
  tantangan?: Langkah | null;
  kuis_jatuh_tempo: number;
  nama?: string;
  posisi?: {
    key: string;
    label: string;
    bab?: number;
    bab_total?: number;
    bab_judul?: string;
    materi: number;
    total_materi: number;
  } | null;
}

/* --------------------------------------------------------------- sapaan */

/**
 * Sapaan menurut jam DINDING orang yang memakainya.
 *
 * Ambangnya 11/15/19, dan sengaja TIDAK dibulatkan ke 12/18: "Selamat siang"
 * yang baru dimulai pukul 12 membuat jam sebelas pagi disapa "pagi" padahal
 * sudah lewat tengah hari di percakapan sehari-hari, dan "malam" yang dimulai
 * pukul 18 memotong sore terlalu cepat.
 */
export function sapaJam(jam: number): string {
  return jam < 11
    ? "Selamat pagi"
    : jam < 15
      ? "Selamat siang"
      : jam < 19
        ? "Selamat sore"
        : "Selamat malam";
}

/**
 * Pecah sapaan jadi kata pertama dan sisanya, plus ekor bernama.
 *
 * Judulnya memuat satu pil GAMBAR di antara keduanya ("Selamat [gambar]
 * malam."), jadi yang dibutuhkan bukan satu string melainkan dua potongan.
 * Pilnya `aria-hidden` dan kosong teks, jadi pembaca layar tetap mendengar
 * "Selamat malam." apa adanya.
 */
export function pecahSapa(
  sapa: string,
  nama?: string,
): { awal: string; sisa: string } {
  const [awal, ...sisa] = sapa.split(" ");
  return {
    awal: awal ?? "",
    sisa: sisa.join(" ") + (nama ? `, ${nama}.` : "."),
  };
}

/**
 * Kalimat pembuka saat tidak ada langkah yang bisa ditawarkan.
 *
 * Urutan cabangnya bagian dari artinya: target yang sudah tercapai menang atas
 * streak, dan streak menang atas "kurang N XP lagi". Membalik dua yang pertama
 * membuat orang yang sudah menutup harinya tetap dikejar angka.
 */
export function kalimatPembuka(d: DataDasbor): string {
  if (d.xp_hari_ini >= d.target_harian) {
    return "Target hari ini sudah tercapai. Sisanya bonus.";
  }
  if (d.streak >= 2) {
    // Tanpa "Jaga apinya tetap menyala." yang masih ada di layar-belajar.js:
    // cabang ini hanya tampil saat target hari ini BELUM tercapai, jadi
    // dorongan itu terbaca sebagai peringatan bahwa streak akan padam. Satu-
    // satunya deviasi dari antarmuka lama; pembanding menyebutnya
    // (DORONGAN_STREAK_LAMA).
    return `Sudah ${d.streak} hari berturut-turut.`;
  }
  if (d.xp_hari_ini > 0) {
    return `Kurang ${d.target_harian - d.xp_hari_ini} XP lagi untuk menutup hari ini.`;
  }
  return "Belum ada yang dikerjakan hari ini.";
}

/* -------------------------------------------------------------- langkah */

/** Kata kerja untuk sebuah langkah, di dasbor yang sedang BERJALAN. */
export function labelLanjut(tipe: string): string {
  return (
    ({ materi: "Baca materi", kuis: "Kerjakan kuis", latihan: "Kerjakan latihan" } as
      Record<string, string>)[tipe] ?? "Lanjutkan"
  );
}

/** Kata kerja yang sama, di layar MULAI. Bedanya cuma cadangannya: di sana
 *  belum ada apa pun yang bisa "dilanjutkan". */
export function labelMulai(tipe: string): string {
  return (
    ({ materi: "Baca materi", kuis: "Kerjakan kuis", latihan: "Kerjakan latihan" } as
      Record<string, string>)[tipe] ?? "Mulai"
  );
}

export function tautanLangkah(s: Langkah): string {
  return `#/${s.tipe}/${s.bahasa}/${s.indeks}`;
}

/**
 * "Punya 30 menit?": langkah teratas, BERURUTAN, selama muat dalam 30 menit.
 *
 * Berurutan, bukan dipilih yang paling pas: antreannya sudah diurutkan
 * `saran.py` menurut apa yang paling berguna sekarang, dan mengurutkannya
 * ulang menurut durasi berarti menukar urutan belajar dengan permainan ransel.
 * Langkah tanpa `menit` memutus paketnya -- ia tidak bisa dijumlahkan, dan
 * menganggapnya nol akan menjanjikan tiga langkah dalam tiga puluh menit yang
 * salah satunya tak diketahui panjangnya.
 */
export function paketTigaPuluh(langkah: Array<Langkah | null | undefined>): {
  muat: Langkah[];
  total: number;
} {
  let total = 0;
  const muat: Langkah[] = [];
  for (const x of langkah) {
    if (!x) continue;
    if (!x.menit || total + x.menit > 30) continue;
    total += x.menit;
    muat.push(x);
  }
  return { muat, total };
}

/* --------------------------------------------------------- angka harian */

/**
 * Pembanding untuk angka hari ini.
 *
 * "38 XP" berdiri sendiri tidak menjawab "38 itu banyak atau sedikit BAGIKU".
 * Yang menjawabnya angka kemarin, dan itu datang dari server (`xp_kemarin`),
 * bukan dihitung ulang dari heatmap.
 *
 * Arahnya ditulis sebagai KATA ("naik 26"), bukan panah berwarna. Dua sebab:
 * keluarga ikon di repo ini tidak punya panah naik/turun, dan membedakan naik
 * dari turun hanya lewat warna melanggar WCAG 1.4.1 -- aturan yang sama yang
 * sudah dipakai untuk baris terhapus di diff.
 *
 * `beda > 0` DIPERTAHANKAN walau tidak bisa menggigit: diukur atas 301
 * pasangan ber-`beda === 0`, menggantinya dengan `>= 0` mengubah NOL keluaran,
 * karena `beda === 0 ? null` di bawah sudah membuang hasilnya lebih dulu. Yang
 * dijaganya rumus BERIKUTNYA -- begitu penjaga nol itu dilepas, `>= 0` akan
 * menulis "naik 0" -- jadi angkanya ditulis di sini alih-alih kodenya
 * disederhanakan.
 */
export function bandingHarian(d: DataDasbor): { teks: string; arah: string | null } {
  const beda = d.xp_hari_ini - (d.xp_kemarin || 0);
  const arah =
    beda > 0
      ? `naik ${angka(beda)}`
      : beda < 0
        ? `turun ${angka(-beda)}`
        : "sama seperti kemarin";
  return {
    teks: `Kemarin ${angka(d.xp_kemarin || 0)} XP`,
    arah: beda === 0 ? null : ` · ${arah}`,
  };
}

/**
 * Streak yang putus ditampilkan sebagai CELAH, bukan sebagai nol merah.
 *
 * Tanggalnya datang UTUH dari server (`hari_belajar_terakhir`), field yang
 * SAMA yang dipakai `progress.streak_aktif()` untuk memutuskan. Versi pertama
 * fungsi ini menyimpulkannya sendiri dari heatmap dengan mencari hari ber-XP
 * terakhir, dan itu definisi kedua yang langsung bertentangan dengan pil di
 * kartu yang sama: membaca materi tanpa menuntaskannya membuat streak hidup
 * sehari penuh tanpa menambah satu pun XP, jadi hari itu tidak punya entri
 * riwayat -- heatmap akan bilang "belum pernah belajar" sementara pilnya
 * bilang "1 hari".
 *
 * Tandanya sengaja dibalik: `selisihHari` menghitung dari HARI INI ke depan,
 * jadi masa lalu negatif -- dan "12 hari lalu" adalah negatif itu dibalik.
 */
export function celahBelajar(
  d: DataDasbor,
): { tanggal: string; selisih: number } | null {
  const tgl = d.hari_belajar_terakhir;
  if (!tgl) return null;
  const hari = tanggalLokal(tgl);
  const beda = selisihHari(tgl);
  const selisih = beda === null ? 0 : -beda;
  if (!hari || !selisih || selisih <= 0) return null;
  return {
    tanggal: hari.toLocaleDateString("id-ID", {
      weekday: "long",
      day: "numeric",
      month: "long",
    }),
    selisih,
  };
}

/** Rasio cincin level dan "panas"-nya (XP hari ini terhadap target). */
export function cincinAngka(d: DataDasbor): { rasio: number; panas: number } {
  const jepit = (n: number) => Math.max(0, Math.min(1, n));
  return {
    rasio: jepit(d.di_level / Math.max(1, d.butuh_level)),
    panas: jepit(d.xp_hari_ini / Math.max(1, d.target_harian)),
  };
}

/* -------------------------------------------------------------- minggu */

const NAMA_HARI = ["Min", "Sen", "Sel", "Rab", "Kam", "Jum", "Sab"];

export interface HariPekan {
  tanggal: string;
  xp: number;
  xpTeks: string;
  tinggi: number;
  nama: string;
  kini: boolean;
  capai: boolean;
  judul: string;
}

/**
 * Tujuh hari terakhir sebagai tujuh batang, hari ini di ujung.
 *
 * Tinggi batang diukur terhadap yang TERBESAR di antara target harian dan hari
 * terbaik minggu ini, supaya garis target selalu terlihat DAN hari yang
 * melewatinya memang terlihat melewatinya. Mengukurnya terhadap target saja
 * membuat hari 3x target menumpahkan batangnya; terhadap puncak saja membuat
 * garis targetnya keluar dari kotak di minggu yang buruk.
 *
 * `null` kalau heatmap belum tujuh hari: strip tujuh batang yang isinya empat
 * bukan "minggu ini", ia potongan yang terbaca seperti tiga hari kosong.
 */
export function pekanAngka(d: DataDasbor): {
  hari: HariPekan[];
  target: number;
  total: number;
  aktif: number;
} | null {
  const tujuh = (d.heatmap || []).slice(-7);
  if (tujuh.length < 7) return null;
  const puncak = Math.max(d.target_harian || 1, ...tujuh.map((x) => x.xp));
  return {
    target: ((d.target_harian || 0) / puncak) * 100,
    total: tujuh.reduce((t, x) => t + x.xp, 0),
    aktif: tujuh.filter((x) => x.xp > 0).length,
    hari: tujuh.map((x, i) => {
      const tgl = tanggalLokal(x.tanggal);
      const kini = i === tujuh.length - 1;
      return {
        tanggal: x.tanggal,
        xp: x.xp,
        xpTeks: x.xp ? angka(x.xp) : "",
        tinggi: (x.xp / puncak) * 100,
        nama: kini ? "Hari ini" : tgl ? (NAMA_HARI[tgl.getDay()] ?? "") : "",
        kini,
        capai: x.xp >= (d.target_harian || 1),
        judul: `${tanggalRamah(x.tanggal)}: ${angka(x.xp)} XP`,
      };
    }),
  };
}

/* ---------------------------------------------------------------- bara */

export interface SelPetak {
  tanggal: string;
  xp: number;
  tingkat: number;
  kini: boolean;
  judul: string;
}

/**
 * Hamparan enam bulan: sel kosong pembuka, lalu satu sel per hari.
 *
 * Sel kosong pembuka BUKAN hiasan: `.bara-petak` adalah `grid-auto-flow:
 * column` dengan tujuh baris yang berarti Senin..Minggu, jadi tanpa penggeser
 * ini seluruh kisi bergeser dan barisnya berhenti berarti "Senin".
 * `(getDay() + 6) % 7` memindahkan Minggu dari indeks 0 ke indeks 6.
 *
 * Empat tingkat, ambangnya DIHITUNG dari target harian yang bisa diubah di
 * Pengaturan -- bukan dari angka tetap. Itu sebabnya legenda di bawahnya diberi
 * kata ("sedikit" .. "banyak XP") alih-alih angka: angka apa pun di sana akan
 * jadi salinan kedua yang cepat basi.
 */
export function baraPetak(
  d: DataDasbor,
  hariIni: string,
): { kosong: number; sel: SelPetak[]; aktif: number } {
  const target = Math.max(1, d.target_harian);
  const pertama = d.heatmap[0];
  const awal = pertama ? tanggalLokal(pertama.tanggal) : null;
  return {
    kosong: awal ? (awal.getDay() + 6) % 7 : 0,
    aktif: d.heatmap.filter((s) => s.xp > 0).length,
    sel: d.heatmap.map((s) => ({
      tanggal: s.tanggal,
      xp: s.xp,
      tingkat: s.xp <= 0 ? 0 : s.xp < target * 0.5 ? 1 : s.xp < target ? 2 : 3,
      kini: s.tanggal === hariIni,
      judul: `${tanggalRamah(s.tanggal)}: ${s.xp} XP`,
    })),
  };
}

/**
 * Jeda terpanjang di dalam hamparan. `null` kalau di bawah sepekan.
 *
 * Hari-hari SEBELUM hari ber-XP pertama tidak dihitung: itu "belum mulai",
 * bukan jeda, dan tanpa pengecualian itu setiap profil baru akan dilaporkan
 * punya jeda enam bulan.
 *
 * Di bawah sepekan itu akhir pekan biasa. Menamainya "jeda" akan membuat
 * istirahat yang sehat terbaca sebagai kegagalan.
 */
export function jedaBara(
  heatmap: SelBara[],
): { panjang: number; akhir: number; kapan: string } | null {
  let jalan = 0;
  let panjang = 0;
  let akhir = -1;
  const mulai = heatmap.findIndex((s) => s.xp > 0);
  heatmap.forEach((s, i) => {
    if (mulai < 0 || i < mulai) return;
    if (s.xp > 0) {
      jalan = 0;
      return;
    }
    jalan += 1;
    if (jalan > panjang) {
      panjang = jalan;
      akhir = i;
    }
  });
  if (panjang < 7) return null;
  return {
    panjang,
    akhir,
    kapan:
      akhir === heatmap.length - 1
        ? "masih berlangsung"
        : `berakhir ${tanggalRamah((heatmap[akhir] as SelBara).tanggal)}`,
  };
}

/* --------------------------------------------------------- layar mulai */

/**
 * Jumlah materi, kuis, dan latihan SELURUH kurikulum.
 *
 * Dihitung dari daftar bahasa, tidak diketik. Kurikulum ini masih tumbuh;
 * kalimat sambutan yang menyebut "sebelas bahasa" adalah kalimat yang suatu
 * hari berbohong tanpa satu pun tes gagal.
 */
export function jumlahKurikulum(
  bahasa: Array<{ materi: number; kuis: number; latihan: number }>,
): { materi: number; kuis: number; latihan: number } {
  return bahasa.reduce(
    (t, b) => ({
      materi: t.materi + b.materi,
      kuis: t.kuis + b.kuis,
      latihan: t.latihan + b.latihan,
    }),
    { materi: 0, kuis: 0, latihan: 0 },
  );
}

/**
 * Penanda di satu ubin bahasa. `null` untuk yang "biasa".
 *
 * Baris ketiganya cuma muncul untuk DUA pengecualian, dan itu keputusan yang
 * gampang dibalik tanpa sadar:
 *
 *   "tanpa pasang apa pun"  HTML & CSS -- cukup aplikasi ini dan sebuah
 *                           browser. Klaim yang lebih kuat daripada sekadar
 *                           bisa dijalankan, dan itu sebabnya keduanya berdiri
 *                           paling depan di LANGUAGES.
 *   "butuh go"              compiler-nya belum ada di komputer INI.
 *
 * Keadaan ketiga -- "compiler-nya butuh dipasang, dan sudah" -- sengaja TIDAK
 * ditulis. Ia berlaku untuk hampir semua ubin, dan label yang sama berulang
 * tiga puluh kali berhenti dibaca: yang membawa arti justru pengecualiannya.
 * Garis dasarnya sudah dikatakan sekali di kepala bagian.
 */
export function tandaUbin(b: {
  siap: boolean;
  hilang?: string[];
  pasang?: string;
}): [kelas: string, teks: string] | null {
  if (!b.siap) return ["ubin-butuh", `butuh ${(b.hilang || []).join(", ")}`];
  if (!b.pasang) return ["ubin-bebas", "tanpa pasang apa pun"];
  return null;
}

/**
 * Bahasa yang sedang dijalani: yang persennya di atas nol, paling jauh dulu.
 *
 * Persennya datang dari `progress.statistik_bahasa` -- angka yang SAMA dengan
 * halaman bahasa. Enam diambil karena bento lama memuat enam; meja kerja
 * memotongnya lagi jadi empat di tempat pemakaiannya, bukan di sini.
 */
export function dijalaniDasbor(bahasa: BahasaDasbor[]): BahasaDasbor[] {
  return bahasa
    .filter((b) => b.persen > 0)
    .sort((a, b) => b.persen - a.persen)
    .slice(0, 6);
}
