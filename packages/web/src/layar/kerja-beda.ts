/* Bagian MURNI ruang kerja: tangga "lihat jawaban", diff baris, diff kata.
 *
 * Port bagian non-DOM `webapp/statik/js/layar-kerja.js`. Keempat algoritma di
 * sini punya satu sifat yang sama dan satu akibat yang sama kalau bergeser:
 * mereka memutuskan apa yang pelajar LIHAT sebagai perbedaan antara kode yang
 * ia tulis dan kode yang benar. Satu karakter yang hilang di tengah jalan
 * menggambar baris yang TIDAK pernah ditulis siapa pun, dan tidak ada cara ia
 * tahu bedanya. Pagarnya `uji/banding-kerja.mjs`.
 *
 * `bedaBaris` di sini TIDAK menggantikan `bersama/src/beda.ts`. Yang di sana
 * port `inti/beda.py` -- ia menjawab "kenapa keluaranmu beda" dengan diagnosis
 * (nyaris, ringkas, kolom pertama yang beda). Yang di sini jalur TAMPILAN:
 * diff baris dan kata untuk digambar berdampingan, yang di Python memang tidak
 * pernah ada karena terminal tidak punya tempat untuk itu.
 */

import { selisihHari } from "../waktu.ts";

/* Ambang dan atap tangga "lihat jawaban". Keduanya diukur dari kurikulum,
 * bukan dipilih: dari 558 latihan bersolusi, solusinya bermedian 35 baris,
 * terpanjang 399 baris, dan 79 di antaranya berpanjang <= 12 baris.
 *
 * Angkanya diukur ulang saat port ini dibuat. Komentar di `layar-kerja.js`
 * masih menyebut "303 latihan, median 21, terpanjang 167" -- benar saat
 * ditulis, basi sesudah 12 kurikulum tech stack masuk. Yang berubah cuma
 * kalimatnya; kedua ambangnya masih tepat untuk sebaran yang baru. */
const AMBANG_REKOR = 12;
export const LANGKAH_REKOR = 3;

/**
 * Pecah solusi jadi langkah-langkah yang bertumbuh DARI EKOR.
 *
 * "Lihat contoh solusi" dulu satu pintu tanpa tangga: yang keluar seluruh
 * programnya, sekaligus, dan sesudah itu tidak ada lagi yang bisa dikerjakan
 * pelajar selain membacanya. Padahal yang paling sering dibutuhkan orang buntu
 * bukan seluruh solusinya melainkan BARIS TERAKHIRNYA -- di situ hasilnya
 * dicetak, dan bentuk cetakan itulah yang biasanya tidak ketemu. Membuka dari
 * KEPALA menyajikan import dan deklarasi, bagian yang justru sudah ada di
 * editornya sendiri.
 *
 * Tiap potongan adalah SUFIKS kontinu dari daftar aslinya. Rautan yang
 * melompat-lompat akan menyajikan kode yang tidak pernah ada sebagai program,
 * dan pelajar tidak punya cara tahu bagian mana yang disembunyikan.
 *
 * Jumlah langkahnya ikut diukur: tiga langkah untuk solusi delapan baris
 * berarti tiga klik untuk empat baris -- tangga yang anak-anaknya lebih banyak
 * daripada yang dinaiki. Jadi `<= AMBANG_REKOR` baris dapat DUA langkah,
 * sisanya `LANGKAH_REKOR`, berapa pun panjangnya.
 *
 * Langkah yang tidak menambah satu baris pun dibuang: solusi satu baris
 * menghasilkan SATU potongan, bukan dua yang identik. Tombol "Lihat lebih
 * banyak" yang tidak mengubah apa pun adalah tombol yang berujung penolakan.
 */
export function pisahRekor(
  baris: string[] | null | undefined,
  maksLangkah: number = LANGKAH_REKOR,
): string[][] {
  if (!Array.isArray(baris) || baris.length === 0) return [];
  const n = baris.length;
  const alami = n <= AMBANG_REKOR ? 2 : LANGKAH_REKOR;
  const langkah = Math.max(1, Math.min(alami, maksLangkah));
  const potongan: string[][] = [];
  let panjangLalu = 0;
  for (let i = 1; i <= langkah; i++) {
    // Langkah terakhir dipatok ke `n` apa adanya, bukan dihitung. Pembulatan
    // yang meleset satu baris DI SITU berarti "seluruhnya" yang bukan
    // seluruhnya, dan yang hilang justru baris pertama programnya.
    //
    // Pin ini TIDAK PERNAH mengubah hasilnya untuk rumus yang sekarang:
    // `Math.ceil((n * langkah) / langkah) === n` di seluruh 558 solusi x
    // keempat nilai `maksLangkah` (diukur, bukan diduga -- baterai mutasi yang
    // menemukannya, lewat sel yang mencabut pin ini dan tetap hijau). Ia
    // DIPERTAHANKAN karena yang dijaganya bukan rumus ini melainkan rumus
    // BERIKUTNYA: begitu pembilangnya diganti, pin ini satu-satunya yang
    // menahan langkah terakhir tetap berarti "seluruhnya".
    const panjang = i === langkah ? n : Math.ceil((n * i) / langkah);
    if (panjang <= panjangLalu) continue;
    potongan.push(baris.slice(n - panjang));
    panjangLalu = panjang;
  }
  return potongan;
}

/**
 * "diulang lagi besok" dan kawan-kawannya, dari tanggal ISO.
 *
 * Tanpa ini layar yang paling sering dilihat menampilkan "diulang lagi
 * 2026-09-07" -- tanggal ISO mentah. Dua cara bicara untuk satu fakta yang
 * sama membuat pemakainya mengira keduanya hal yang berbeda.
 */
export function jadwalRamah(iso: string | null | undefined): string {
  const hari = selisihHari(iso);
  if (hari === null) return "diulang lagi " + iso;
  if (hari <= 0) return "sudah waktunya diulang";
  if (hari === 1) return "diulang lagi besok";
  return `diulang lagi ${hari} hari lagi`;
}

/* Nomor baris di dalam sebuah baris pesan galat.
 *
 * Yang dicari pola `berkas.ext:NN` lebih dulu, lalu `line NN`. Nol berarti
 * barisnya tidak menyebut nomor mana pun -- dan baris seperti itu tetap
 * digambar sebagai teks biasa, bukan tombol. Pagar itu penting: `setup` dan
 * `verifikasi` ditempel di sekitar kode pelajar, jadi ada nomor baris yang
 * jatuh di luar tulisannya sendiri. */
const POLA_BARIS_BERKAS = /[\w./\\-]+\.\w+:(\d+)/;
const POLA_KATA_LINE = /\bline (\d+)/;

export function nomorDiBaris(teks: string): number {
  const m = POLA_BARIS_BERKAS.exec(teks) || POLA_KATA_LINE.exec(teks);
  return m ? parseInt(m[1] as string, 10) : 0;
}

export type Tanda = "=" | "-" | "+";
export interface Segmen { tanda: Tanda; teks: string }
export interface ButirBeda {
  tanda: Tanda;
  teks: string;
  nomor: number;
  segmen?: Segmen[];
}

/**
 * Diff baris untuk membandingkan kode pelajar dengan solusi contoh.
 *
 * Memakai tabel subsekuens terpanjang bersama; masukannya puluhan baris, jadi
 * biaya O(n*m) tidak pernah terasa. Daftar kosong berarti "tidak ada bedanya"
 * -- pemanggilnya yang memutuskan apa yang digambar untuk keadaan itu.
 */
export function bedaBaris(a: string[], b: string[]): ButirBeda[] {
  const n = a.length;
  const m = b.length;
  const tabel = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--) {
    const baris = tabel[i] as Uint16Array;
    const bawah = tabel[i + 1] as Uint16Array;
    for (let j = m - 1; j >= 0; j--) {
      baris[j] = a[i] === b[j]
        ? (bawah[j + 1] as number) + 1
        : Math.max(bawah[j] as number, baris[j + 1] as number);
    }
  }
  const keluar: ButirBeda[] = [];
  let i = 0;
  let j = 0;
  let nomor = 0;
  while (i < n && j < m) {
    nomor += 1;
    if (a[i] === b[j]) {
      keluar.push({ tanda: "=", teks: a[i] as string, nomor });
      i++;
      j++;
    } else if ((tabel[i + 1] as Uint16Array)[j]! >= (tabel[i] as Uint16Array)[j + 1]!) {
      keluar.push({ tanda: "-", teks: a[i] as string, nomor });
      i++;
    } else {
      keluar.push({ tanda: "+", teks: b[j] as string, nomor });
      j++;
    }
  }
  while (i < n) { nomor += 1; keluar.push({ tanda: "-", teks: a[i++] as string, nomor }); }
  while (j < m) { nomor += 1; keluar.push({ tanda: "+", teks: b[j++] as string, nomor }); }
  return keluar.every((k) => k.tanda === "=") ? [] : keluar;
}

/* Atap biaya `bedaKata`, dalam SEL tabel (jumlah token kiri x kanan).
 *
 * Baris keluaran bisa sepanjang apa pun -- yang menulisnya pelajar, bukan
 * kurikulum -- sementara tabel LCS-nya O(n*m). Tanpa atap, satu baris keluaran
 * puluhan ribu huruf cukup untuk menggantung tab-nya, dan yang terlihat bukan
 * error melainkan tombol Jalankan yang berhenti menjawab. Di atas atap ini
 * `bedaKata` menyerah dan mengembalikan `null`, lalu pemanggilnya menggambar
 * baris utuh -- yang hilang granularitasnya, bukan diff-nya. */
const BATAS_SEL_KATA = 40000;

/* Pemecah token yang WAJIB lossless: `pecahToken(s).join("") === s`.
 *
 * Tiga alternatifnya menutup seluruh ruang karakter -- deretan spasi, deretan
 * huruf/angka, lalu satu karakter apa pun yang bukan spasi -- karena diff yang
 * kehilangan satu karakter di tengah jalan akan menggambar baris yang TIDAK
 * pernah ditulis siapa pun, dan pelajar tidak punya cara tahu bedanya.
 * `\p{L}` dipakai, bukan `\w`, supaya huruf beraksen tidak pecah jadi tiga
 * token di tengah satu kata. */
const POLA_TOKEN_KATA = /\s+|[\p{L}\p{N}_]+|[^\s]/gu;

export function pecahToken(s: string): string[] {
  // `match` dengan bendera /g tidak mewarisi `lastIndex`, jadi polanya boleh
  // dibagi antar panggilan tanpa membuat hasilnya bergantung urutan panggilan.
  return s.match(POLA_TOKEN_KATA) || [];
}

/**
 * Diff per-KATA di dalam satu pasang baris yang sudah diketahui berubah.
 *
 * `bedaBaris` di atas dan `Beda.baris` di Python sama-sama berhenti di tingkat
 * BARIS: keduanya bisa mengatakan "baris ini berubah", tidak satu pun bisa
 * mengatakan KATA MANA. Untuk baris sepanjang satu kalimat keluaran itu berarti
 * pekerjaan membandingkan dua baris panjang tetap diserahkan ke mata pelajar --
 * padahal justru itu yang bisa dikerjakan komputer.
 *
 * Keluarannya tiga daftar segmen atas token yang sama:
 *
 *   kiri    `=`/`-`      baris harapan, dengan yang hilang ditandai
 *   kanan   `=`/`+`      baris pelajar, dengan yang bertambah ditandai
 *   gabung  `=`/`-`/`+`  satu baris inline memuat kedua sisi dalam urutan
 *                        dokumen, dipakai saat pasangannya diciutkan
 *
 * Dan HANYA ketiganya. Tidak ada predikat "bedanya cuma spasi" di sini. Pernah
 * ada, dan ia tidak pernah bisa benar: teks yang diserahkan penggambarnya sudah
 * ditukar `api._beda_json` jadi versi ber-`·`/`→` lebih dulu, jadi yang tersisa
 * untuk diperiksa bukan lagi spasi.
 *
 * Mengembalikan `null` -- artinya "gambar saja baris utuh" -- di tiga keadaan,
 * dan ketiganya dipilih, bukan kelalaian:
 *
 * * Salah satu sisi bukan string, atau tokennya nol. Tidak ada yang
 *   dibandingkan.
 * * Tabelnya melewati BATAS_SEL_KATA. Alasannya di atas.
 * * Nol token BUKAN-SPASI yang sama. Kalau dua baris tidak punya satu kata pun
 *   yang sama, menyoroti semua kata sama informatifnya dengan menyoroti seluruh
 *   baris -- cuma jauh lebih berisik. Yang diperiksa sengaja token bukan-spasi:
 *   hampir setiap pasang baris berbagi sebuah spasi, jadi memeriksa "ada token
 *   yang sama" saja akan membuat pagar ini tidak pernah menyala sama sekali.
 */
export function bedaKata(
  a: unknown, b: unknown,
): { kiri: Segmen[]; kanan: Segmen[]; gabung: Segmen[] } | null {
  if (typeof a !== "string" || typeof b !== "string") return null;
  const ta = pecahToken(a);
  const tb = pecahToken(b);
  const n = ta.length;
  const m = tb.length;
  if (!n || !m || n * m > BATAS_SEL_KATA) return null;

  const tabel = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--) {
    const baris = tabel[i] as Uint16Array;
    const bawah = tabel[i + 1] as Uint16Array;
    for (let j = m - 1; j >= 0; j--) {
      baris[j] = ta[i] === tb[j]
        ? (bawah[j + 1] as number) + 1
        : Math.max(bawah[j] as number, baris[j + 1] as number);
    }
  }

  const kiri: Segmen[] = [];
  const kanan: Segmen[] = [];
  const gabung: Segmen[] = [];
  // Token bersebelahan yang bertanda sama dilebur jadi satu segmen. Bukan demi
  // DOM yang ringkas: segmen per token membuat "dua kata berurutan berubah"
  // tampil sebagai dua kotak dengan jeda di antaranya, dan yang terbaca jadi
  // dua ubahan terpisah padahal cuma satu.
  const dorong = (daftar: Segmen[], tanda: Tanda, teks: string) => {
    const akhir = daftar[daftar.length - 1];
    if (akhir && akhir.tanda === tanda) akhir.teks += teks;
    else daftar.push({ tanda, teks });
  };
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (ta[i] === tb[j]) {
      dorong(kiri, "=", ta[i] as string);
      dorong(kanan, "=", tb[j] as string);
      dorong(gabung, "=", ta[i] as string);
      i++;
      j++;
    } else if ((tabel[i + 1] as Uint16Array)[j]! >= (tabel[i] as Uint16Array)[j + 1]!) {
      dorong(kiri, "-", ta[i] as string);
      dorong(gabung, "-", ta[i] as string);
      i++;
    } else {
      dorong(kanan, "+", tb[j] as string);
      dorong(gabung, "+", tb[j] as string);
      j++;
    }
  }
  while (i < n) {
    dorong(kiri, "-", ta[i] as string);
    dorong(gabung, "-", ta[i] as string);
    i++;
  }
  while (j < m) {
    dorong(kanan, "+", tb[j] as string);
    dorong(gabung, "+", tb[j] as string);
    j++;
  }

  const jangkar = kiri.filter((s) => s.tanda === "=").map((s) => s.teks).join("");
  if (jangkar.trim() === "") return null;

  return { kiri, kanan, gabung };
}

/**
 * Pasangkan `-` dengan `+` yang menggantikannya di keluaran `bedaBaris`.
 *
 * `bedaBaris` memancarkan baris yang berubah sebagai DUA butir lepas,
 * sementara `Beda.baris` di Python memancarkannya sebagai satu `~` berisi
 * kedua sisi. Perbedaan bentuk itu sengaja TIDAK diseragamkan di dalam
 * `bedaKata`: begitu perjodohannya ikut masuk ke sana, fungsi itu berhenti bisa
 * diuji sebagai fungsi atas dua string. Jadi ia tinggal di sini, dan cuma di
 * jalur diff KODE.
 *
 * Aturannya: dalam satu deret `-` yang langsung disusul deret `+`, butir ke-n
 * dipasangkan dengan butir ke-n. Sisanya -- deret yang lebih panjang di satu
 * sisi, atau `-` tanpa `+` sesudahnya -- dibiarkan utuh tanpa segmen, karena
 * baris yang tidak punya lawan memang tidak punya "kata yang berubah"; ia
 * seluruhnya hilang atau seluruhnya baru. MURNI: masuk daftar, keluar daftar
 * BARU; butir aslinya tidak disentuh.
 */
export function pasangkanUbahan(baris: ButirBeda[]): ButirBeda[] {
  const keluar: ButirBeda[] = baris.map((d) => ({ ...d }));
  let i = 0;
  while (i < keluar.length) {
    if ((keluar[i] as ButirBeda).tanda !== "-") { i++; continue; }
    let k = i;
    while (k < keluar.length && (keluar[k] as ButirBeda).tanda === "-") k++;
    let t = k;
    while (t < keluar.length && (keluar[t] as ButirBeda).tanda === "+") t++;
    const pasang = Math.min(k - i, t - k);
    for (let p = 0; p < pasang; p++) {
      const kiriButir = keluar[i + p] as ButirBeda;
      const kananButir = keluar[k + p] as ButirBeda;
      const kata = bedaKata(kiriButir.teks, kananButir.teks);
      if (!kata) continue;
      kiriButir.segmen = kata.kiri;
      kananButir.segmen = kata.kanan;
    }
    i = t > k ? t : k;
  }
  return keluar;
}

/* Isi awal Ruang Coba per bahasa.
 *
 * Diadu BYTE-PER-BYTE dengan `contohAwal` di `layar-kerja.js`, dan itu bukan
 * ketelitian berlebihan: satu salah ketik di salah satu dari sembilan belas
 * string ini berarti Ruang Coba terbuka dengan program yang tidak bisa
 * dikompilasi, pada bahasa yang mungkin tidak ada yang mencobanya selama
 * berbulan-bulan -- dan yang pertama menemukannya pelajar, yang akan menyangka
 * dirinya salah. */
const CONTOH: Record<string, string> = {
  python: 'nama = "dunia"\nprint(f"Halo, {nama}!")\n',
  javascript: 'const nama = "dunia";\nconsole.log(`Halo, ${nama}!`);\n',
  java: 'public class Coba {\n    public static void main(String[] args) {\n'
      + '        System.out.println("Halo, dunia!");\n    }\n}\n',
  c: '#include <stdio.h>\n\nint main(void) {\n'
   + '    printf("Halo, dunia!\\n");\n    return 0;\n}\n',
  cpp: '#include <iostream>\nusing namespace std;\n\nint main() {\n'
     + '    cout << "Halo, dunia!" << endl;\n    return 0;\n}\n',
  go: 'package main\n\nimport "fmt"\n\nfunc main() {\n'
    + '\tfmt.Println("Halo, dunia!")\n}\n',
  bash: '#!/usr/bin/env bash\nnama="dunia"\necho "Halo, $nama!"\n',
  sql: 'CREATE TABLE murid (nama TEXT, nilai INTEGER);\n'
     + "INSERT INTO murid VALUES ('Andi', 90), ('Budi', 75);\n"
     + 'SELECT nama, nilai FROM murid ORDER BY nilai DESC;\n',
  html: '<!DOCTYPE html>\n<html lang="id">\n<head>\n'
      + '  <meta charset="utf-8">\n  <title>Halaman Pertamaku</title>\n'
      + '</head>\n<body>\n  <h1>Halo, dunia!</h1>\n'
      + '  <p>Ini paragraf pertamaku.</p>\n</body>\n</html>\n',
  csharp: 'using System;\n\nclass Program\n{\n'
        + '    static void Main()\n    {\n'
        + '        Console.WriteLine("Halo, dunia!");\n    }\n}\n',
  vb: 'Imports System\n\nModule Program\n    Sub Main()\n'
    + '        Console.WriteLine("Halo, dunia!")\n    End Sub\nEnd Module\n',
  rust: 'fn main() {\n    let nama = "dunia";\n'
      + '    println!("Halo, {nama}!");\n}\n',
  php: '<?php\n$nama = "dunia";\necho "Halo, $nama!\\n";\n',
  ruby: 'nama = "dunia"\nputs "Halo, #{nama}!"\n',
  kotlin: 'fun main() {\n    val nama = "dunia"\n'
        + '    println("Halo, $nama!")\n}\n',
  typescript: 'const nama: string = "dunia";\nconsole.log(`Halo, ${nama}!`);\n',
  fedora: '#!/usr/bin/env bash\n\nset -euo pipefail\n\n'
        + 'nama="dunia"\nprintf \'Halo, %s!\\n\' "$nama"\n',
  git: '#!/usr/bin/env bash\n\nset -euo pipefail\n\n'
     + '# Bekerja di direktori sementara supaya repositorimu sendiri\n'
     + '# tidak pernah tersentuh -- idiom yang sama dengan kerangka\n'
     + '# editor latihan Git.\n'
     + 'kerja="$(mktemp -d)"\ntrap \'rm -rf "$kerja"\' EXIT\n'
     + 'cd "$kerja"\n\n'
     + 'git init -q\ngit config user.name "Andi"\n'
     + 'git config user.email "andi@contoh.id"\n\n'
     + 'echo "Halo, dunia!" > catatan.txt\ngit add catatan.txt\n'
     + 'git commit -qm "Catatan pertama"\n\n'
     + '# Hash dan tanggal berbeda di tiap mesin, jadi yang dicetak\n'
     + '# subjeknya saja.\n'
     + 'git log --pretty=format:\'- %s\' | cat\n',
  css: '/* Coba ubah warnanya, lalu Jalankan lagi. */\nbody {\n'
     + '  background-color: #f5f5f5;\n  font-family: sans-serif;\n'
     + '  margin: 0;\n}\n\nh1 {\n  color: #333;\n'
     + '  text-align: center;\n}\n',
};

export function contohAwal(bahasa: string): string {
  return CONTOH[bahasa] || "";
}
