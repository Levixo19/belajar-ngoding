/* Preferensi TAMPILAN: localStorage dan `<html>`. Port dari `inti.js` +
 * `layar-lain.js`.
 *
 * Yang tinggal di sini sengaja cuma yang VISUAL -- tema, ukuran huruf, tingkat
 * gerak, lebar kolom baca. Semuanya milik browser ini saja, bukan berkas
 * progres: "tema yang enak di terminal" dan "tema yang enak di browser" tidak
 * harus sama, dan menaruhnya di berkas progres berarti mengganti tema ikut
 * tercatat sebagai kegiatan belajar.
 *
 * Preferensi SUARA dan getar TIDAK disentuh di sini, dan itu bukan kelupaan:
 * pemiliknya `webapp/statik/js/suara.js`, dan ia satu-satunya yang berhak
 * menerjemahkan kuncinya jadi nilai. Dua penulis untuk satu kunci berarti dua
 * ejaan untuk satu nilai, dan yang membacanya nanti cuma mengenali salah
 * satunya. Begitu `suara.js` ikut diport, ia yang membawa medannya -- bukan
 * berkas ini.
 *
 * Kuncinya DIBAGI dengan antarmuka lama (awalan `belajar.`), jadi orang yang
 * memakai keduanya melihat tema yang sama. Itu sebabnya bentuk nilainya tidak
 * boleh berubah.
 */

/** Awalan kunci. Sama dengan versi JS: localStorage-nya dibagi bersama. */
const AWALAN = "belajar.";

export function simpanLokal(kunci: string, nilai: unknown): void {
  try {
    localStorage.setItem(AWALAN + kunci, JSON.stringify(nilai));
  } catch {
    // Mode penyamaran atau kuota penuh. Preferensi tampilan yang gagal
    // tersimpan bukan alasan menggagalkan apa pun: halamannya tetap jalan,
    // cuma pilihannya tidak bertahan sampai muatan berikutnya.
  }
}

export function ambilLokal<T>(kunci: string, bawaan: T): T {
  try {
    const mentah = localStorage.getItem(AWALAN + kunci);
    return mentah === null ? bawaan : (JSON.parse(mentah) as T);
  } catch {
    return bawaan;
  }
}

export type KunciTema = "gelap" | "malam" | "terang" | "kontras";
export type KunciUkuran = "kecil" | "sedang" | "besar" | "sangat besar";
export type KunciGerak = "penuh" | "halus" | "mati";

export const TEMA: Array<[KunciTema, string, string]> = [
  ["gelap", "Gelap", "Grafit netral. Bawaan, untuk pemakaian sehari-hari."],
  ["malam", "Malam", "Serba hangat, kontras rendah. Untuk mata yang lelah."],
  ["terang", "Terang", "Kertas putih yang tenang. Untuk ruangan benderang."],
  ["kontras", "Kontras tinggi", "Warna dikuatkan, garis dipertebal."],
];

const UKURAN: Array<[KunciUkuran, number]> = [
  ["kecil", 15],
  ["sedang", 16],
  ["besar", 18],
  ["sangat besar", 20],
];

/* Tiga tingkat gerak, bukan saklar nyala/mati.
 *
 * Saklar dua posisi memaksa orang yang cuma terganggu oleh latar yang bergeser
 * untuk ikut membuang umpan balik tombol -- padahal umpan balik tombol bukan
 * hiasan, melainkan cara tahu bahwa tekanannya sampai. Tingkat tengah memberi
 * jalan keluar: semua yang bergerak SENDIRI padam, semua yang bergerak karena
 * DISENTUH tetap ada, dengan jarak yang dipangkas. */
export const GERAK: Array<[KunciGerak, string, string]> = [
  [
    "penuh",
    "Penuh",
    "Semua gerakan hidup: perpindahan berpegas, urutan masuk, denyut bara.",
  ],
  [
    "halus",
    "Halus",
    "Tidak ada yang bergerak sendiri. Umpan balik sentuhan tetap ada, " +
      "jaraknya dipendekkan. Pilihan yang tepat untuk sesi panjang.",
  ],
  ["mati", "Mati", "Tidak ada animasi sama sekali."],
];

export interface Tampilan {
  tema: KunciTema;
  ukuran: KunciUkuran;
  gerak: KunciGerak;
  lebarBaca: number;
}

/**
 * Baca tingkat gerak, dan TERJEMAHKAN nilai lama yang berupa boolean.
 *
 * Aplikasi ini dipakai tiap hari, jadi penerjemahan ini bukan kesopanan:
 * tanpa itu, siapa pun yang pernah mematikan animasi akan mendapati
 * animasinya MENYALA LAGI sesudah pembaruan. Jangan hapus cabang boolean-nya.
 */
function bacaGerak(): KunciGerak {
  const n = ambilLokal<unknown>("gerak", "penuh");
  if (n === true) return "penuh";
  if (n === false) return "mati";
  return GERAK.some((g) => g[0] === n) ? (n as KunciGerak) : "penuh";
}

export function bacaTampilan(): Tampilan {
  return {
    tema: ambilLokal<KunciTema>("tema", "gelap"),
    ukuran: ambilLokal<KunciUkuran>("ukuran", "sedang"),
    gerak: bacaGerak(),
    lebarBaca: ambilLokal<number>("lebarBaca", 72),
  };
}

/**
 * Simpan preferensi dan pasangkan ke `<html>`.
 *
 * `--ukuran-teks` dipasang di `<html>`, BUKAN `<body>`: satuan `rem` selalu
 * diukur terhadap font-size `<html>`. Memasangnya di body pernah membuat
 * setelan "Ukuran huruf" tidak mengubah satu pun teks berukuran rem -- dan di
 * halaman materi itu berarti NOL dari seratusan elemennya ikut membesar.
 * Setelan yang tampak berfungsi tapi tidak mengubah apa pun lebih buruk
 * daripada setelan yang tidak ada.
 */
export function terapkanTampilan(ubah?: Partial<Tampilan>): Tampilan {
  const t: Tampilan = { ...bacaTampilan(), ...(ubah ?? {}) };
  for (const [k, v] of Object.entries(t)) simpanLokal(k, v);

  const akar = document.documentElement;
  akar.dataset.tema = t.tema;
  akar.dataset.gerak = t.gerak;
  const px = (UKURAN.find((u) => u[0] === t.ukuran) ?? UKURAN[1]!)[1];
  akar.style.setProperty("--ukuran-teks", px + "px");
  akar.style.setProperty("--baca", t.lebarBaca + "ch");
  // Ctrl+J dan tombol tema di pil atas mengganti tema tanpa lewat layar
  // Pengaturan; kartu tema di sana mendengar siaran ini, kalau tidak "dipakai"
  // dan `aria-pressed`-nya tertinggal di tema lama.
  document.dispatchEvent(new CustomEvent("tampilan-berubah"));
  return t;
}

/** Putar ke tema berikutnya. Mengembalikan NAMA tema yang baru, untuk toast. */
export function temaBerikutnya(): string {
  const kini = bacaTampilan().tema;
  const i = TEMA.findIndex((t) => t[0] === kini);
  const berikut = TEMA[(i + 1) % TEMA.length]!;
  terapkanTampilan({ tema: berikut[0] });
  return berikut[1];
}

/**
 * Ingatan sesaat per layar: draf kode Ruang Coba, bahasa terpilih, stdin.
 *
 * Kuncinya memakai awalan `belajar.ingat.` yang SAMA dengan `ctx.ingat` di
 * `aplikasi.js`, dan itu syarat, bukan kebetulan: selama dua antarmuka masih
 * hidup berdampingan, draf yang ditulis di salah satunya harus ditemukan oleh
 * yang lain. Kalau prefiksnya berbeda, orang yang berpindah antarmuka
 * menemukan Ruang Coba kembali ke contoh awal -- dan yang hilang kode yang
 * baru saja ia tulis.
 *
 * Nilainya di-JSON-kan, juga sama dengan versi lama. `undefined` sebagai
 * argumen kedua berarti BACA; `null` saat gagal urai, bukan melempar --
 * localStorage yang penuh atau diblokir adalah keadaan normal di jendela
 * pribadi, dan draf yang tidak tersimpan tidak boleh menjatuhkan layarnya.
 */
/**
 * Ingatan yang isinya BUKAN string: daftar, objek, angka.
 *
 * `ingat()` di bawah hanya menerima dan mengembalikan string, dan itu cukup
 * untuk draf kode, tab terakhir, dan pilihan bahasa. Riwayat palet bukan salah
 * satunya -- ia sebuah array -- dan menitipkannya lewat `ingat()` dengan
 * `JSON.stringify` sendiri menghasilkan NILAI TERSANDI GANDA di localStorage:
 * `"\"[{...}]\""` alih-alih `[{...}]`.
 *
 * Itu bukan cuma tidak rapi. Kuncinya DIBAGI dengan antarmuka lama
 * (`ctx.ingat` di `aplikasi.js`), dan di sana nilainya diurai sekali lalu
 * langsung dipakai sebagai array -- jadi `.filter()` atas sebuah string
 * melempar, dan palet antarmuka lama berhenti bekerja karena sesuatu yang
 * dituliskan antarmuka BARU. Terukur di Chrome sebelum diperbaiki.
 *
 * Bentuk fungsi ini karena itu dibuat sama persis dengan `ctx.ingat`: satu
 * `JSON.stringify` saat menulis, satu `JSON.parse` saat membaca.
 */
export function ingatJson<T>(kunci: string, nilai?: T): T | null {
  const k = AWALAN + "ingat." + kunci;
  if (nilai === undefined) {
    try {
      return JSON.parse(localStorage.getItem(k) ?? "null") as T | null;
    } catch {
      return null;
    }
  }
  try {
    localStorage.setItem(k, JSON.stringify(nilai));
  } catch {
    /* penuh atau diblokir */
  }
  return nilai;
}

export function ingat(kunci: string, nilai?: string): string | undefined {
  const k = AWALAN + "ingat." + kunci;
  if (nilai === undefined) {
    try {
      const mentah = localStorage.getItem(k);
      if (mentah === null) return undefined;
      const v = JSON.parse(mentah);
      return typeof v === "string" ? v : undefined;
    } catch {
      return undefined;
    }
  }
  try {
    localStorage.setItem(k, JSON.stringify(nilai));
  } catch {
    /* penuh atau diblokir; draf hilang, layarnya tidak */
  }
  return nilai;
}
