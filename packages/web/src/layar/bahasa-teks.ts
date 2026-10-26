/* Bagian MURNI halaman bahasa. Port dari `webapp/statik/js/layar-belajar.js`.
 *
 * Yang masuk ke sini cuma yang memutuskan sesuatu: kalimat mana yang dibaca di
 * kepala halaman, dan tautan mana yang ditawarkan sebagai tindakan utama.
 * Keduanya tidak menggambar apa pun, jadi keduanya bisa diadu langsung dengan
 * JS yang masih melayani aplikasi lama (`uji/banding-bahasa.mjs`).
 *
 * Pemisahannya punya sebab teknis, bukan selera: Node melucuti TIPE dari `.ts`
 * tapi tidak melucuti JSX dari `.tsx`, jadi hanya berkas `.ts` yang bisa
 * diimpor pembandingnya.
 *
 * Satu aturan yang tidak boleh hilang saat diport: **tidak ada satu pun
 * keputusan "selesai" atau "lulus" yang dihitung ulang di sini.** Statusnya
 * sudah jadi saat sampai -- `runner.periksa` untuk latihan, `bab.py` untuk
 * penguncian, `progress` untuk XP. Yang dikerjakan berkas ini murni memilih
 * mana yang paling masuk akal ditawarkan lebih dulu.
 */

/** Statistik satu kurikulum, apa adanya dari `/api/bahasa`. */
export interface StatBahasa {
  materi: number;
  total_materi: number;
  total_kuis: number;
  total_latihan: number;
  persen: number;
}

export interface MateriRingkas {
  indeks: number;
  judul: string;
  status: string;
  terkunci?: boolean;
}

export interface KuisRingkas {
  indeks: number;
  judul: string;
  pernah?: boolean;
  siap?: boolean;
  jatuh_tempo?: boolean;
}

export interface LatihanRingkas {
  indeks: number;
  judul: string;
  status: string;
}

/**
 * Satu kalimat yang menempatkan bahasa ini dalam gambar besar, SEBELUM angka
 * apa pun muncul.
 *
 * Deretan "0/26 · 0/7 · 0/15" yang dulu berdiri di sini adalah jawaban atas
 * pertanyaan yang belum ditanyakan siapa pun saat baru membuka sebuah halaman.
 */
export function kalimatBahasa(s: StatBahasa): string {
  const total = s.total_materi + s.total_kuis + s.total_latihan;
  if (s.persen >= 100) {
    return `Semuanya sudah kamu selesaikan: ${total} bagian, tuntas.`;
  }
  if (s.persen <= 0) {
    return (
      `Belum dimulai. Jalurnya ${s.total_materi} materi, diselingi ` +
      `${s.total_kuis} kuis dan ${s.total_latihan} latihan.`
    );
  }
  return `Sudah ${Math.round(Number(s.persen) || 0)}% jalan. Lanjutkan dari tempat kamu berhenti.`;
}

/** Satu butir baris fakta: nama ikon (dipakai versi lama) dan teksnya. */
export interface Fakta {
  gambar: string;
  teks: string;
  kurang: boolean;
}

/**
 * Baris fakta di kepala halaman.
 *
 * Menjawab "apa isinya, seberapa besar, dan apakah bisa dijalankan di
 * komputerku" sebelum ada satu pun daftar yang perlu dibaca. Butir keempat
 * yang menandai toolchain hilang DIBERI kelas sendiri: ia satu-satunya yang
 * bukan sekadar angka melainkan sebuah kabar.
 */
export function faktaBahasa(
  s: StatBahasa,
  siap: boolean,
  hilang: string[] | null | undefined,
): Fakta[] {
  return [
    { gambar: "materi", teks: `${s.total_materi} materi`, kurang: false },
    { gambar: "kuis", teks: `${s.total_kuis} kuis`, kurang: false },
    { gambar: "latihan", teks: `${s.total_latihan} latihan`, kurang: false },
    {
      gambar: siap ? "selesai" : "belum",
      teks: siap ? "kode bisa dijalankan" : "butuh " + (hilang || []).join(", "),
      kurang: !siap,
    },
  ];
}

/** Tindakan utama halaman bahasa. `null` berarti tidak ada yang tersisa. */
export interface Lanjut {
  tipe: "materi" | "kuis" | "latihan";
  indeks: number;
  judul: string;
  mata: string;
  ket: string;
}

/**
 * Pilih SATU hal berikutnya untuk ditawarkan di kartu Lanjutkan.
 *
 * Materi yang masih TERKUNCI dilewati, dan itu bukan kehati-hatian berlebihan:
 * menawarkannya sebagai tindakan utama berarti tombol paling terang di halaman
 * ini berujung di layar penolakan -- persis yang dilarang aturan "tidak boleh
 * ada tombol yang berujung penolakan".
 *
 * Syarat panjang di cabang pertama membaca begini: materi menang, KECUALI ada
 * kuis yang belum pernah dikerjakan padahal seluruh materi yang diujinya sudah
 * dibaca DAN pelajarnya tidak sedang berhenti di tengah sebuah materi. Yang
 * dijaganya satu urutan belajar: habis membaca satu blok materi, yang paling
 * berguna bukan membaca blok berikutnya melainkan menguji yang baru dibaca --
 * tapi orang yang berhenti di tengah kalimat lebih baik diantar kembali ke
 * kalimat itu.
 */
export function pilihLanjut(b: {
  materi: MateriRingkas[];
  kuis: KuisRingkas[];
  latihan: LatihanRingkas[];
}): Lanjut | null {
  const materi = b.materi.find((m) => m.status !== "selesai" && !m.terkunci);
  const kuis =
    b.kuis.find((q) => q.jatuh_tempo || (!q.pernah && q.siap)) ??
    b.kuis.find((q) => !q.pernah);
  const latihan = b.latihan.find(
    (e) => e.status !== "lulus" && e.status !== "manual",
  );

  if (
    materi &&
    !(kuis && !kuis.pernah && kuis.siap && materi.status !== "sebagian")
  ) {
    return {
      tipe: "materi",
      indeks: materi.indeks,
      judul: materi.judul,
      mata: materi.status === "sebagian" ? "Lanjutkan bacaan" : "Mulai dari sini",
      ket:
        materi.status === "sebagian"
          ? "Kamu berhenti di tengah materi ini."
          : "Materi berikutnya yang belum dibaca.",
    };
  }
  if (kuis) {
    return {
      tipe: "kuis",
      indeks: kuis.indeks,
      judul: kuis.judul,
      mata: "Uji pemahaman",
      ket: kuis.pernah
        ? "Sudah waktunya kuis ini diulang."
        : "Semua materi yang diuji kuis ini sudah kamu baca.",
    };
  }
  if (latihan) {
    return {
      tipe: "latihan",
      indeks: latihan.indeks,
      judul: latihan.judul,
      mata: "Tulis kodenya",
      ket: "Bagian yang mengubah bacaan jadi kemampuan.",
    };
  }
  return null;
}
