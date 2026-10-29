/* Layar yang dipakai untuk MEMBACA: dasbor, halaman bahasa, pembaca materi,
 * pencarian, bookmark, dan catatan.
 *
 * Pertanyaan yang dijawab dasbor bukan "apa saja capaianku" melainkan "habis
 * ini ngapain". Aplikasi ini menyimpan 339 materi, 67 kuis, dan 175 latihan di
 * sebelas bahasa; buat orang yang baru mulai, daftar sepanjang itu bukan
 * kekayaan melainkan kelumpuhan. Bab bertingkat menjawab separuhnya — mana yang
 * boleh dibuka sekarang — dan Langkah Berikutnya menjawab sisanya.
 *
 * Importir: aplikasi.js, layar-kerja.js.
 */

import {
  api, h, isikan, kosongkan, bilah, bulat, angka, kosong, keadaan, sorak,
  rayakan, salin, tanggalRamah, jamRamah, selisihHari, tanggalLokal, hariIniISO,
  jendela, jendelaTerbuka, tandai, tunda, GalatApi, ambilLokal, simpanLokal,
} from "./inti.js";
import {
  animasi, masuk, ungkap, saatTampak, denyut, percikBara, adaGerak, gerakPenuh,
  berurut, tata, saatGulir, tingkatGerak,
} from "./gerak.js";
import { ikon, ikonTipe } from "./ikon.js";
import { praKode } from "./sorot.js"; import { gambarVisual } from "./visual.js"; import { tombolJejak } from "./jejak.js"; import { petaRasi, dariBahasa, panelLangitMeja } from "./rasi.js";
import { Editor } from "./editor.js";
import { barisTautan } from "./layar-pustaka.js";
import { gerakBeranda } from "./beranda.js";  // kalimatGulir/akordeon/marquee: tak dipakai meja kerja
import { sampul, kepalaBersampul } from "./sampul.js";
import {
  pratinjauHtml, bisaDipratinjau, dokumenPratinjau, halamanDikarang,
} from "./pratinjau.js";

/** Pil bertanda jenis isi: ikon + kata. Ikonnya membuat jenisnya terbaca
 *  sebelum katanya sempat dibaca — dan di daftar sepanjang dua puluh baris,
 *  "sebelum dibaca" itu selisih yang besar.
 *
 *  Warnanya NETRAL untuk ketiga jenis. Dulu kuis, latihan, dan materi
 *  masing-masing punya warna sendiri, sehingga satu daftar memuat tiga warna
 *  untuk informasi yang sudah dibawa ikon dan katanya — dan warna aksen
 *  (latihan) ikut tenggelam di antara dua warna lain yang sama kerasnya. */
export function pilJenis(tipe) {
  return h("span.pil.pil-jenis", {},
    ikon(ikonTipe(tipe), { ukuran: 14, tebal: 1.9 }), tipe);
}

function potong(t, n) {
  return t && t.length > n ? t.slice(0, n - 1) + "…" : t;
}

/** Buang awalan penomoran dari judul.
 *
 *  Judul di kurikulum sudah membawa nomornya sendiri ("2. Variabel & Tipe
 *  Data"), dan tiap daftar di sini juga punya kolom nomor tersendiri — jadi
 *  yang terbaca "2  2. Variabel & Tipe Data". Di kolom selebar 250 px,
 *  pengulangan itu memakan ruang yang justru paling dibutuhkan judulnya.
 *  Nomornya dibuang di TAMPILAN saja; datanya tidak disentuh, karena judul
 *  itu juga dipakai sebagai kunci progres (lihat AGENTS.md — judul wajib unik
 *  per bahasa, dan mengubahnya berarti kehilangan progres). */
function tanpaNomor(judul) {
  return String(judul || "").replace(/^\s*\d+\.\s*/, "");
}

/** Jalankan `fn` begitu `el` benar-benar sudah terpasang DAN punya ukuran.
 *
 *  Layar dibangun utuh sebelum router menempelkannya — dan router menunggu
 *  animasi keluar layar sebelumnya selesai lebih dulu. Jadi antara "elemennya
 *  jadi" dan "elemennya ada di halaman" bisa lewat sepuluh frame, dan apa pun
 *  yang diukur di antaranya mengembalikan nol: getBoundingClientRect() semua
 *  nol, scrollWidth nol, clientWidth nol.
 *
 *  Yang terjadi kalau itu diabaikan bukan error melainkan diam — jalur materi
 *  yang seharusnya digulir ke butir yang sedang dibaca berhenti di butir
 *  pertama, dan cuma di sebagian pemuatan, tergantung frame mana yang menang. */
export function saatSiap(el, fn, maks = 40) {
  let sisa = maks;
  const coba = () => {
    if (el.isConnected && el.clientWidth > 0) { fn(); return; }
    if (sisa-- > 0) requestAnimationFrame(coba);
  };
  requestAnimationFrame(coba);
}

/** Bawa sebuah butir ke tengah WADAHNYA, tanpa pernah menggulir dokumen.
 *
 *  Ini pengganti `scrollIntoView({block:"center"})`, dan penggantiannya bukan
 *  soal selera. `scrollIntoView` menggulir SEMUA leluhur yang bisa digulir,
 *  termasuk dokumen — jadi membuka materi ke-13 lewat navigasi dalam aplikasi
 *  mendaratkan pembacanya sembilan ratus piksel di bawah judul, di tengah
 *  kalimat, pada halaman yang belum pernah ia lihat. Yang dimaksud cuma
 *  "gulir jalurnya", dan itulah yang dilakukan di sini.
 *
 *  Dua arah diurus sekaligus karena jalur materi memang berganti arah: kolom
 *  tegak yang menggulir ke bawah di layar lebar, satu jalur yang menggulir ke
 *  samping di layar sempit. */
function bawaKeTengah(wadah, butir) {
  if (!wadah || !butir) return;
  const w = wadah.getBoundingClientRect();
  const b = butir.getBoundingClientRect();
  if (wadah.scrollHeight > wadah.clientHeight + 4) {
    wadah.scrollTop += (b.top - w.top) - (w.height - b.height) / 2;
  }
  if (wadah.scrollWidth > wadah.clientWidth + 4) {
    wadah.scrollLeft += (b.left - w.left) - (w.width - b.width) / 2;
  }
}

/* ================================================================ dasbor */

export async function layarDasbor(_params, ctx) {
  const d = await api.ambil("/api/dasbor");
  // Belum ada apa pun yang dikerjakan: layarnya sendiri yang berbeda, bukan
  // dasbor biasa yang kebetulan semua angkanya nol. Alasannya ada di komentar
  // layarMulai().
  if (d.xp === 0) return layarMulai(d, ctx);
  return dasborBerjalan(d, ctx);
}

/** Layar untuk orang yang belum mengerjakan apa pun.
 *
 *  Dasbor biasa untuk profil baru berbunyi begini: heatmap 182 hari yang
 *  seluruhnya dingin, sebelas kartu bahasa yang semuanya "0% · 0/44 materi ·
 *  0/7 kuis · 0/19 latihan", "streak terputus", dan "0/22 badge". Hal pertama
 *  yang dilihat orang yang baru mulai adalah katalog kegagalan yang bahkan
 *  belum sempat ia lakukan — dan tidak satu pun dari angka itu menjawab
 *  pertanyaan yang sebenarnya ia bawa, yaitu "aku mulai dari mana".
 *
 *  Yang menggantikannya satu pertanyaan dan tiga pintu. Angka-angkanya tetap
 *  ada; mereka muncul sendiri begitu ada yang bisa dihitung.
 *
 *  Pintu pertama datang dari `saran.py` lewat `/api/dasbor` — bukan dari
 *  tebakan di sini. Antrean "habis ini ngapain" sudah punya satu tempat
 *  tinggal, dan membuat tempat kedua berarti dua jawaban berbeda untuk
 *  pertanyaan yang sama. */
function layarMulai(d, ctx) {
  const langkah = d.langkah[0];
  const bahasa = ctx.awal.bahasa || [];
  const aturan = ctx.awal.aturan_bab || {};

  // Angkanya DIHITUNG dari daftar bahasa, tidak diketik. Kurikulum ini masih
  // tumbuh; kalimat sambutan yang menyebut "sebelas bahasa" adalah kalimat
  // yang suatu hari berbohong tanpa satu pun tes gagal.
  const jml = bahasa.reduce((t, b) => ({
    materi: t.materi + b.materi,
    kuis: t.kuis + b.kuis,
    latihan: t.latihan + b.latihan,
  }), { materi: 0, kuis: 0, latihan: 0 });

  const el = h("div.mulai.masuk-urut", {},
    h("header.sambut.sambut-tengah", {},
      h("span.mata", {}, "Selamat datang"),
      h("h1", {}, "Mau mulai dari mana?"),
      h("p.sambut-sub", {},
        `${angka(bahasa.length)} bahasa · ${angka(jml.materi)} materi · `
        + `${angka(jml.kuis)} kuis · ${angka(jml.latihan)} latihan. `
        + "Pilih satu; sisanya menunggu dan tidak ke mana-mana.")),

    // SATU tindakan utama, dan ia datang dari `saran.py` lewat /api/dasbor —
    // bukan dari tebakan di sini. Antrean "habis ini ngapain" sudah punya satu
    // tempat tinggal, dan membuat tempat kedua berarti dua jawaban berbeda
    // untuk satu pertanyaan.
    langkah ? kartuMulaiUtama(langkah, bahasa) : null,

    // Semua bahasa, bukan dua. Menyembunyikan sembilan di balik menu pada
    // layar yang justru bertanya "mau mulai dari mana" berarti menjawab
    // pertanyaannya dengan setengah katalog — dan orang yang sedang menimbang
    // apakah aplikasi ini sepadan waktunya tidak punya cara melihat isinya.
    // Yang belum bisa DIJALANKAN di komputer ini tetap ikut: materi dan
    // kuisnya jalan penuh tanpa satu pun compiler, dan penandanya dipasang
    // sebelum diklik, bukan sesudah.
    h("section.mulai-pilih", {},
      h("div.bagian-kepala", {},
        h("span.mata", {}, "Atau pilih sendiri"),
        // Dihitung dari `siap`, bukan diketik: yang terpasang di satu komputer
        // belum tentu terpasang di komputer berikutnya, dan kalimat yang
        // menyebut angkanya sendiri akan salah di mesin orang lain.
        h("span.bagian-ket", {},
          `${angka(bahasa.filter((b) => b.siap).length)} dari `
          + `${angka(bahasa.length)} bisa dijalankan di komputer ini`)),
      kisiUbin(bahasa.filter((b) => !b.tematik)),
      // Dua kurikulum terakhir bukan bahasa pemrograman: satu mengajarkan cara
      // BERPIKIR membangun aplikasi, satu lagi cara MENGOPERASIKAN sistem.
      // Berbaris sebagai ubin ke-18 dan ke-19 di kisi yang sama, keduanya
      // terbaca sebagai dua bahasa asing yang belum pernah pelajar dengar --
      // dan "Bikin Aplikasi" bahkan terbaca seperti nama bahasa. Judul kecil
      // ini memberi tahu apa yang sedang ia lihat sebelum ia mengkliknya.
      ...(bahasa.some((b) => b.tematik) ? [
        h("div.bagian-kepala.bagian-kepala-lanjutan", {},
          h("span.mata", {}, "Bukan bahasa, tapi tetap kurikulum"),
          h("span.bagian-ket", {},
            "Cara berpikir dan cara mengoperasikan, bukan sintaks")),
        kisiUbin(bahasa.filter((b) => b.tematik)),
      ] : [])),

    h("a.pintu-tenang", { href: "#/coba" },
      h("span.ikon-bulat", {}, ikon("jalankan", { ukuran: 18 })),
      h("div.pintu-isi", {},
        h("b", {}, "Belum mau memilih?"),
        h("span", {}, "Ruang Coba: tulis kode apa saja, jalankan, lihat "
          + "hasilnya. Tidak dinilai, tidak menyentuh progres.")),
      h("span.baris-panah", {}, ikon("lanjut", { ukuran: 18 }))),

    h("section", {},
      h("span.mata", {}, "Cara kerjanya"),
      h("div.kartu.kartu-aturan", {},
        // Kalimat aturannya datang dari `bab.KALIMAT_ATURAN` lewat /api/awal,
        // TIDAK ditulis ulang di sini. Tiga permukaan menjelaskan aturan yang
        // sama ke pelajar; rumusan yang disalin bisa melenceng satu per satu
        // tanpa satu tes pun gagal, dan yang dibaca jadi dua aturan berbeda
        // tergantung dari pintu mana orangnya sampai.
        h("p.aturan-utama", {}, aturan.aturan || ""),
        aturan.tingkat && aturan.tingkat.length
          ? h("dl.tingkat-daftar", {}, aturan.tingkat.flatMap((t) => [
              h("dt", { kelas: "pil t-" + t.nama }, t.label),
              h("dd", {}, t.ket),
            ])) : null,
        aturan.pintu_darurat
          ? h("p.aturan-pintu", {},
              h("span", {}, aturan.pintu_darurat),
              h("a.tbl.tbl-kecil.tbl-hantu", { href: "#/atur" }, "Buka Pengaturan"))
          : null)),
  );

  return { el, judul: "Mulai" };
}

/** Kartu "mulai di sini" untuk orang yang belum mengerjakan apa pun.
 *
 *  Aksen dipakai sebagai GARIS kartu dan sebagai isi TOMBOLNYA, bukan sebagai
 *  latar kartunya. Latar aksen sudah punya satu pemilik di seluruh aplikasi —
 *  `.lanjutkan` di dasbor — dan yang membuat kartu itu berarti "ini yang
 *  sedang kamu kerjakan" justru batas tersebut. Layar ini belum melanjutkan
 *  apa pun: yang ditawarkannya awal, bukan sambungan. */
function kartuMulaiUtama(s, bahasa) {
  const b = bahasa.find((x) => x.key === s.bahasa);
  const jenis = { materi: "Baca materi", kuis: "Kerjakan kuis",
                  latihan: "Kerjakan latihan" }[s.tipe] || "Mulai";
  return h("a.mulai-utama", { href: tautanLangkah(s) },
    h("div.mulai-utama-isi", {},
      h("span.mata.mata-nyala", {}, `Disarankan · ${s.label_bahasa}`),
      h("h2", {}, tanpaNomor(s.judul)),
      h("p", {}, b && !b.pasang
        ? `${jenis}. Tidak perlu memasang apa pun: cukup aplikasi ini dan `
          + "browser yang sedang kamu buka."
        : `${jenis}. Langkah pertama di jalur ${s.label_bahasa}.`)),
    h("span.tbl.tbl-utama.tbl-besar", {},
      "Mulai", ikon("lanjut", { ukuran: 18 })));
}

/** Panah memindah fokus antar-ubin, dengan satu ubin saja yang ikut Tab.
 *
 *  Kisi sembilan belas tautan berarti sembilan belas perhentian Tab sebelum
 *  sampai ke apa pun di bawahnya. Pola roving tabindex memampatkannya jadi
 *  satu: Tab masuk ke kisi, panah berjalan di dalamnya, Tab keluar lagi.
 *
 *  Jumlah kolom dihitung dari POSISI NYATA tiap ubin, bukan dari CSS: kisinya
 *  `auto-fill`, jadi jumlah kolomnya berubah mengikuti lebar jendela dan tidak
 *  pernah tertulis di satu tempat yang bisa dibaca. Menebaknya dari breakpoint
 *  berarti panah bawah melompat salah tiap kali lebarnya di antara dua ambang.
 *
 *  Tidak ada role ARIA yang ditambahkan. Ini sekumpulan tautan, bukan grid
 *  data; memberinya role="grid" menuntut struktur baris/sel yang tidak ada,
 *  dan pembaca layar akan menjanjikan navigasi yang tidak pernah disediakan. */
function kisiUbin(daftar) {
  const petak = h("div.ubin-bahasa", {}, daftar.map(ubinBahasa));
  panahAntarUbin(petak);
  return petak;
}

function panahAntarUbin(petak) {
  const ubin = [...petak.children].filter((el) => el.classList.contains("ubin"));
  if (ubin.length < 2) return;
  for (const [i, el] of ubin.entries()) el.tabIndex = i === 0 ? 0 : -1;

  const kolom = () => {
    const atas = ubin[0].getBoundingClientRect().top;
    let n = 0;
    for (const el of ubin) {
      if (Math.abs(el.getBoundingClientRect().top - atas) > 1) break;
      n++;
    }
    return Math.max(1, n);
  };

  petak.addEventListener("keydown", (e) => {
    const i = ubin.indexOf(document.activeElement);
    if (i < 0) return;
    const k = kolom();
    const tuju = { ArrowRight: i + 1, ArrowLeft: i - 1,
                   ArrowDown: i + k, ArrowUp: i - k,
                   Home: 0, End: ubin.length - 1 }[e.key];
    if (tuju === undefined) return;
    e.preventDefault();
    const j = Math.max(0, Math.min(ubin.length - 1, tuju));
    ubin[i].tabIndex = -1;
    ubin[j].tabIndex = 0;
    ubin[j].focus();
  });
}

/** Satu ubin bahasa di layar mulai.
 *
 *  Baris ketiganya cuma muncul untuk DUA PENGECUALIAN, dan itu keputusan yang
 *  gampang dibalik tanpa sadar:
 *
 *    "tanpa pasang apa pun"  HTML & CSS — cukup aplikasi ini dan sebuah
 *                            browser. Klaim yang lebih kuat daripada sekadar
 *                            bisa dijalankan, dan itu sebabnya keduanya
 *                            berdiri paling depan di LANGUAGES.
 *    "butuh go"              compiler-nya belum ada di komputer INI.
 *
 *  Keadaan ketiga — "compiler-nya butuh dipasang, dan sudah" — sengaja TIDAK
 *  ditulis. Ia berlaku untuk delapan dari sebelas ubin, dan label yang sama
 *  berulang delapan kali berhenti dibaca: yang membawa arti justru
 *  pengecualiannya. Garis dasarnya sudah dikatakan sekali di kepala bagian
 *  ("10 dari 11 bisa dijalankan di komputer ini"), jadi ubin tanpa penanda
 *  berarti "yang biasa" dan tidak ada yang hilang.
 *
 *  Keduanya dihitung dari jawaban server — `siap` dari runner.py, `pasang`
 *  dari registry bahasa — bukan ditebak. Yang belum siap TETAP ditampilkan
 *  dan tetap bisa dibuka: materi dan kuisnya jalan penuh, yang mati cuma
 *  penilaian otomatis latihannya. Penandanya dipasang SEBELUM diklik —
 *  aturan yang sama dipakai bab terkunci dan antrean saran. */
function ubinBahasa(b) {
  const tanda = !b.siap
    ? ["ubin-butuh", `butuh ${b.hilang.join(", ")}`]
    : !b.pasang
      ? ["ubin-bebas", "tanpa pasang apa pun"]
      : null;
  return h("a.ubin", { href: "#/bahasa/" + b.key },
    h("span.ubin-sampul", {}, sampul(b.key, { bahasa: b.key, lebar: 360, tinggi: 120 })),
    h("b.ubin-nama", {}, b.label),
    h("span.ubin-jml", {}, `${b.materi} materi · ${b.latihan} latihan`),
    tanda ? h("span.ubin-tanda", { kelas: tanda[0] }, tanda[1]) : null);
}

function dasborBerjalan(d, ctx) {
  const jam = new Date().getHours();
  const sapa = jam < 11 ? "Selamat pagi" : jam < 15 ? "Selamat siang"
             : jam < 19 ? "Selamat sore" : "Selamat malam";

  // Langkah PERTAMA diangkat keluar dari daftar dan diberi kartunya sendiri.
  // Inilah perubahan susunan yang paling menentukan di seluruh dasbor: yang
  // dibutuhkan orang yang belajar dari nol bukan ringkasan capaiannya,
  // melainkan satu kalimat yang menjawab "sekarang aku ngapain". Sisanya —
  // level, XP, bara enam bulan — tetap ada, tapi di KOLOM SEBELAH, bukan di
  // bawahnya: yang sudah terjadi tidak boleh mendorong yang harus dikerjakan
  // ke bawah lipatan layar.
  const [utama, ...sisaLangkah] = d.langkah;

  // BERANDA (rombak 2026-10-14). Urutannya bab demi bab, masing-masing
  // dengan jarak lapang:
  //   1. Hero Editorial Split: sapaan di kiri, satu-satunya tindakan utama
  //      (kartu Lanjutkan) di kanan.
  //   2. Bento: level, minggu ini, antrean, Peta Karier, Pustaka -- kisi
  //      `grid-auto-flow: dense` yang tidak menyisakan sel kosong.
  //   3. Kalimat perjalanan yang menyala kata demi kata saat digulir.
  //   4. Akordeon bahasa yang sedang dijalani.
  //   5. Hamparan ritme enam bulan, lalu marquee seluruh kurikulum dan ajakan
  //      penutup.
  // Bahasa yang sedang dijalani diurutkan dari persen server; tidak ada
  // persen yang dihitung di sini.
  const dijalani = d.bahasa.filter((b) => b.persen > 0)
    .sort((a, b) => b.persen - a.persen).slice(0, 6);
  const bento = h("div.bento", {},
    h("div.bento-level", {}, kartuBara(d)),
    h("div.bento-pekan", {}, pekanIni(d)),
    // Antrean pindah ke kolom kanan meja kerja (dasborMeja), di atas lipatan.
    null,
    h("div.bento-karier", {}, ubinKarier()),
    h("div.bento-pustaka", {},
      ubinPustaka(utama ? utama.bahasa : null, utama ? utama.label_bahasa : null)));

  const el = dasborMeja(d, ctx, { utama, sisaLangkah, dijalani, bento, sapa });
  // MEJA KERJA (rombak 2026-10-17, dipilih pemilik). Susunan beranda lama
  // (hero editorial, kalimat gulir, akordeon, marquee, ajakan penutup) adalah
  // landing page: tinggi 3709 px di 1440x900, antrean "habis ini apa" baru
  // mulai di y=1168, dan tiga tombol beraksen menuju materi yang sama.
  // Yang dibawa pelajar ke dasbor cuma satu pertanyaan, dan jawabannya
  // sekarang di atas lipatan. Susunannya, dari atas:
  //
  //   1. Meja kini (kiri): tanggal, sapaan, POSISI ("Python · Bab 4 dari 11
  //      · 14/44 materi", dari /api/dasbor -> posisi, dihitung bab.py), lalu
  //      kartu Lanjutkan: satu-satunya permukaan beraksen di layar ini.
  //   2. Antrean (kanan, sejajar): langkah berikutnya dari saran.py, dan
  //      jumlah kuis yang menunggu diulang. Kolom kanan, bukan di bawah:
  //      yang harus dikerjakan tidak boleh didorong ke bawah lipatan.
  //   3. Ringkasan: level, minggu ini, Peta Karier, Pustaka (bento lama).
  //   4. Bahasa yang sedang dijalani sebagai baris: sampul kecil, persen
  //      yang SELALU terlihat (akordeon lama menyembunyikannya sampai
  //      di-hover), dan bilah. Tanpa nomor 01-04: nomor di aplikasi ini
  //      berarti urutan, dan bahasa-bahasa ini bukan urutan.
  //   5. Ritme enam bulan (blokBara) dengan sampulnya.
  //
  // Yang dibuang: kalimat yang menyala saat digulir, marquee seluruh
  // kurikulum, dan ajakan penutup berpepatah. Ketiganya hiasan; sampul SVG
  // tetap dipakai di kartu, baris bahasa, dan ritme. gerakBeranda() tetap
  // dipanggil di bawah; tanpa .beranda-hero dan .beranda-kalimat-isi ia
  // tidak menemukan apa pun untuk digerakkan, dan itu yang diinginkan:
  // meja kerja diam. Kalimatnya pendek-pendek: dasbor dibaca sekilas,
  // bukan ditelaah.
  ungkap(bento, { per: 60, maks: 360, geser: 18, pegas: "halus" });
  let lepasGerak = () => {};
  saatSiap(el, () => { lepasGerak = gerakBeranda(el); });
  return { el, judul: "Dasbor", saatKeluar: () => lepasGerak() };
}

/** Sapaan beranda dengan satu pil gambar DI DALAM judulnya, sesudah kata
 *  pertama ("Selamat [gambar] malam."). Pilnya sampul bahasa yang sedang
 *  dijalani, jadi gambar pertama yang dilihat pagi itu adalah pelajaran yang
 *  menunggu. Judulnya tetap terbaca utuh: pil itu aria-hidden dan kosong
 *  teks, jadi pembaca layar mendengar "Selamat malam." apa adanya. */
function judulSapa(sapa, nama, bahasa) {
  const [awal, ...sisa] = sapa.split(" ");
  return h("h1", {},
    awal, " ",
    h("span.judul-pil", { "aria-hidden": "true" },
      sampul(bahasa ? `${bahasa}/sapa` : "sapa", { bahasa, ragam: "gelombang", lebar: 240, tinggi: 110 })),
    " ", sisa.join(" ") + (nama ? `, ${nama}.` : "."));
}

/** Kartu tindakan utama dasbor.
 *
 *  Satu-satunya benda di halaman ini yang memakai warna aksen sebagai LATAR,
 *  bukan sekadar garis. Itu batas yang dijaga ketat di seluruh aplikasi: kalau
 *  dua hal sama-sama memakai aksen pekat, tidak ada lagi yang namanya "yang
 *  sedang kamu kerjakan". */
function kartuLanjutkan(s) {
  const jenis = { materi: "Baca materi", kuis: "Kerjakan kuis",
                  latihan: "Kerjakan latihan" }[s.tipe] || "Lanjutkan";
  return h("a.lanjutkan", { href: tautanLangkah(s) },
    h("span.lanjutkan-sampul", {},
      sampul(`${s.bahasa}/${s.tipe}/${s.indeks}`, { bahasa: s.bahasa, lebar: 640, tinggi: 260 })),
    h("span.lanjutkan-nomor", {}, String(s.indeks + 1)),
    h("div.lanjutkan-isi", {},
      h("span.mata", {}, `${jenis} · ${s.label_bahasa}` + (s.menit ? ` · ≈${s.menit} menit` : "")),
      h("h2", {}, tanpaNomor(s.judul)),
      h("p", {}, s.alasan)),
    h("span.lanjutkan-tbl", {},
      h("span", {}, "Lanjutkan"),
      ikon("lanjut", { ukuran: 20 })));
}

/** Ubin Peta Karier di dasbor: profesi yang paling dekat dicapai.
 *
 *  Kesiapannya dibaca dari /api/karier, dihitung pelajar/karier.py -- tidak
 *  ada persen yang dihitung ulang di sini. Ubin lahir dengan isi yang sudah
 *  bermakna (judul dan tautan), lalu angkanya menyusul; kalau permintaannya
 *  gagal, yang tertinggal tetap tautan yang benar. */
function ubinKarier() {
  const isi = h("span.meja-ubin-isi", {}, "Lihat profesi yang bisa kamu tuju.");
  const el = h("a.meja-ubin-satu", { href: "#/karier" },
    h("span.meja-ubin-sampul", {}, sampul("karier", { ragam: "orbit", lebar: 480, tinggi: 200 })),
    h("span.meja-ubin-kepala", {}, ikon("karier", { ukuran: 18 }), "Peta karier"),
    isi);
  api.ambil("/api/karier").then((k) => {
    const p = k.profesi.find((x) => x.id === k.tujuan) || [...k.profesi].sort((a, b) => b.kesiapan - a.kesiapan)[0];  // tujuan pilihan pelajar dulu (Pengaturan / Peta Karier)
    if (!p || (p.kesiapan <= 0 && p.id !== k.tujuan)) return;
    el.setAttribute("href", "#/karier/" + p.id);
    isikan(isi, h("b", {}, (p.id === k.tujuan ? "Tujuanmu: " : "") + p.nama),
      h("span.meja-ubin-angka", {}, `${bulat(p.kesiapan)}% siap`),
      h("span.bilah.meja-ubin-bilah", {},
        h("i", { gaya: { width: `${Math.min(100, p.kesiapan)}%` } })));
  }).catch(() => { /* tautannya tetap benar tanpa angka */ });
  return el;
}

/** Ubin Pustaka di dasbor: bacaan gratis untuk bahasa yang sedang dipelajari. */
function ubinPustaka(kunci, label) {
  const href = kunci ? "#/pustaka?kurikulum=" + encodeURIComponent(kunci) : "#/pustaka";
  const isi = h("span.meja-ubin-isi", {}, "Buku, kursus, dan proyek gratis.");
  const el = h("a.meja-ubin-satu", { href },
    h("span.meja-ubin-sampul", {}, sampul("pustaka", { bahasa: kunci, ragam: "kisi", lebar: 480, tinggi: 200 })),
    h("span.meja-ubin-kepala", {}, ikon("pustaka", { ukuran: 18 }),
      label ? `Bacaan ${label}` : "Pustaka"),
    isi);
  if (kunci) {
    api.ambil("/api/pustaka", { kurikulum: kunci, bahasa: "id" }).then((r) => {
      const pertama = r.hasil[0];
      const total = Object.values(r.segi.bahasa).reduce((a, b) => a + b, 0);
      isikan(isi,
        pertama ? h("b", {}, pertama.judul) : null,
        h("span.meja-ubin-angka", {},
          `${angka(total)} tautan, ${angka(r.total)} berbahasa Indonesia`));
    }).catch(() => { /* tautannya tetap benar tanpa angka */ });
  }
  return el;
}

function kalimatPembuka(d) {
  if (d.xp_hari_ini >= d.target_harian) {
    return "Target hari ini sudah tercapai. Sisanya bonus.";
  }
  if (d.streak >= 2) {
    return `Sudah ${d.streak} hari berturut-turut. Jaga apinya tetap menyala.`;
  }
  if (d.xp_hari_ini > 0) {
    return `Kurang ${d.target_harian - d.xp_hari_ini} XP lagi untuk menutup hari ini.`;
  }
  return "Belum ada yang dikerjakan hari ini.";
}

/** Minggu ini: tujuh hari terakhir sebagai tujuh batang, hari ini di ujung.
 *
 *  Hamparan enam bulan menjawab "seperti apa ritmeku"; strip ini menjawab
 *  pertanyaan yang lebih dekat — "minggu ini aku ke mana saja" — tanpa harus
 *  mencari tujuh sel kecil di ujung kanan sebuah kisi. Datanya tujuh entri
 *  terakhir `heatmap` dari /api/dasbor (terlama -> hari ini, hari kosong ikut
 *  tercatat), jadi tidak ada hitungan kedua di sini.
 *
 *  Tinggi batang diukur terhadap yang TERBESAR di antara target harian dan
 *  hari terbaik minggu ini, supaya garis target selalu terlihat dan hari yang
 *  melewatinya memang terlihat melewatinya. Tingginya ditulis langsung di
 *  gaya inline — keadaan alaminya — tidak dianimasikan dari nol. */
function pekanIni(d) {
  const hari = (d.heatmap || []).slice(-7);
  if (hari.length < 7) return null;
  const puncak = Math.max(d.target_harian || 1, ...hari.map((x) => x.xp));
  const nama = ["Min", "Sen", "Sel", "Rab", "Kam", "Jum", "Sab"];
  const target = (d.target_harian || 0) / puncak * 100;
  const total = hari.reduce((t, x) => t + x.xp, 0);
  const aktif = hari.filter((x) => x.xp > 0).length;

  return h("section.pekan", { "aria-label": "Tujuh hari terakhir" },
    h("div.bagian-kepala", {},
      h("span.mata", {}, "Minggu ini"),
      h("span.baris-sisi", {},
        `${angka(total)} XP dalam ${aktif} dari 7 hari`)),
    petakPekan(target, hari.map((x, i) => {
        const tgl = tanggalLokal(x.tanggal);
        const kini = i === hari.length - 1;
        return h("div.pekan-hari" + (kini ? ".kini" : "")
                   + (x.xp >= (d.target_harian || 1) ? ".capai" : ""),
          { title: `${tanggalRamah(x.tanggal)}: ${angka(x.xp)} XP` },
          h("span.pekan-xp", {}, x.xp ? angka(x.xp) : ""),
          h("span.pekan-batang", {},
            h("i", { gaya: { height: (x.xp / puncak * 100) + "%" } })),
          h("span.pekan-nama", {}, kini ? "Hari ini"
            : tgl ? nama[tgl.getDay()] : ""));
      })));
}

/** Kisi tujuh hari dengan garis target di ketinggian `target` (persen).
 *  Lewat setProperty karena `h()` menyalin `gaya` dengan Object.assign, dan
 *  Object.assign ke `style` diam-diam membuang properti kustom `--*` —
 *  gradien yang memakainya lalu tidak sah dan seluruh latarnya hilang. */
function petakPekan(target, isi) {
  const petak = h("div.pekan-petak", {}, isi);
  petak.style.setProperty("--target", target + "%");
  return petak;
}

function cincinLevel(d) {
  const R = 56;
  const keliling = 2 * Math.PI * R;
  const rasio = Math.max(0, Math.min(1, d.di_level / Math.max(1, d.butuh_level)));
  const panas = Math.max(0, Math.min(1, d.xp_hari_ini / Math.max(1, d.target_harian)));
  const NS = "http://www.w3.org/2000/svg";

  const svg = document.createElementNS(NS, "svg");
  svg.setAttribute("viewBox", "0 0 132 132");
  svg.setAttribute("aria-hidden", "true");

  const alur = document.createElementNS(NS, "circle");
  const isi = document.createElementNS(NS, "circle");
  for (const [c, kelas] of [[alur, "alur"], [isi, "isi"]]) {
    c.setAttribute("cx", "66");
    c.setAttribute("cy", "66");
    c.setAttribute("r", String(R));
    c.setAttribute("fill", "none");
    c.setAttribute("stroke-width", "7");
    c.setAttribute("class", kelas);
    svg.appendChild(c);
  }
  const akhir = keliling * (1 - rasio);
  isi.setAttribute("stroke-dasharray", String(keliling));
  // Nilai AKHIR dipasang langsung; animasinya cuma berangkat dari lingkaran
  // kosong. Kalau gerak dimatikan atau animasinya dibatalkan, yang tertinggal
  // tetap busur dengan panjang yang benar — bukan lingkaran kosong.
  isi.setAttribute("stroke-dashoffset", String(akhir));

  const cincin = h("div.cincin", {
    title: `${d.di_level} dari ${d.butuh_level} XP menuju level ${d.level + 1}`,
  }, svg, h("div.cincin-isi", {},
    h("div.cincin-angka", {}, String(d.level)),
    h("div.cincin-label", {}, "level")));
  cincin.style.setProperty("--panas", String(panas));  // lihat petakPekan()

  // Busurnya baru digambar saat cincinnya benar-benar terlihat. Kalau dasbor
  // dibuka sudah dalam keadaan tergulir, mengisi busur di luar layar berarti
  // membuang satu-satunya gerakan yang pantas dilihat di halaman ini.
  saatTampak(cincin, () => {
    animasi(isi, { strokeDashoffset: [String(keliling), String(akhir)] },
            { pegas: "panjang", durasi: 900 });
  }, { bagian: 0.35 });
  return cincin;
}

function kartuBara(d) {
  const kurang = Math.max(0, d.target_harian - d.xp_hari_ini);
  return h("div.kartu.kartu-level", {},
    cincinLevel(d),
    h("div.kartu-level-isi", {},
      h("h2", {}, d.gelar),
      h("div.kartu-level-ket", {},
        `${angka(d.xp)} XP · ${d.di_level}/${d.butuh_level} menuju level `
        + `${d.level + 1}`),
      bilah(d.di_level / Math.max(1, d.butuh_level) * 100),

      h("div.target", {},
        h("div.target-baris", {},
          h("span", {}, "Target hari ini"),
          h("b", { kelas: kurang ? "" : "tercapai" },
            kurang ? `${d.xp_hari_ini}/${d.target_harian} XP` : "tercapai")),
        bilah(d.xp_hari_ini / Math.max(1, d.target_harian) * 100,
              kurang ? "" : "tumbuh")),

      bandingHarian(d),
      d.streak ? null : celahBelajar(d),

      h("div.deret.deret-rapat", {},
        h("span.pil" + (d.streak ? ".pil-nyala" : ""), {},
          ikon("api", { ukuran: 14, tebal: 1.9 }),
          d.streak ? `${d.streak} hari belajar` : "belum ada hari berurutan"),
        h("a.pil" + (d.badge_dimiliki ? ".pil-ungu" : ""),
          { href: "#/statistik" },
          ikon("bintang", { ukuran: 14, tebal: 1.9 }),
          `${d.badge_dimiliki}/${d.badge_total}`))));
}

/** Pembanding untuk angka hari ini.
 *
 *  "38 XP" berdiri sendiri tidak menjawab "38 itu banyak atau sedikit BAGIKU".
 *  Yang menjawabnya angka kemarin, dan itu datang dari server (`xp_kemarin`),
 *  bukan dihitung ulang dari heatmap di sini.
 *
 *  Arahnya ditulis sebagai KATA ("naik 26"), bukan panah berwarna. Dua sebab:
 *  keluarga ikon di repo ini tidak punya panah naik/turun, dan membedakan naik
 *  dari turun hanya lewat warna melanggar WCAG 1.4.1 — aturan yang sama yang
 *  sudah dipakai untuk baris terhapus di diff. */
function bandingHarian(d) {
  const beda = d.xp_hari_ini - (d.xp_kemarin || 0);
  const arah = beda > 0 ? `naik ${angka(beda)}`
             : beda < 0 ? `turun ${angka(-beda)}`
             : "sama seperti kemarin";
  return h("div.banding", {},
    `Kemarin ${angka(d.xp_kemarin || 0)} XP`,
    beda === 0 ? null : h("span.banding-arah", {}, ` · ${arah}`));
}

/** Streak yang putus ditampilkan sebagai CELAH, bukan sebagai nol merah.
 *
 *  Tanggalnya datang UTUH dari server (`hari_belajar_terakhir`), yaitu field
 *  yang sama yang dipakai progress.streak_aktif() untuk memutuskan. Versi
 *  pertama fungsi ini menyimpulkannya sendiri dari heatmap dengan mencari hari
 *  ber-XP terakhir, dan itu definisi kedua yang langsung bertentangan dengan
 *  pil di kartu yang sama: membaca materi tanpa menuntaskannya membuat streak
 *  hidup sehari penuh tanpa menambah satu pun XP, jadi hari itu tidak punya
 *  entri riwayat — heatmap akan bilang "belum pernah belajar" sementara
 *  pilnya bilang "1 hari".
 *
 *  Yang dikerjakan di sini tinggal dua: memformat tanggalnya, dan menghitung
 *  selisih TANGGAL ke TANGGAL. Tidak ada tombol memperbaiki, tidak ada freeze
 *  yang bisa dipilih. Jalan masuk kembalinya kartu Lanjutkan di kolom sebelah,
 *  yang isinya dari saran.py. */
function celahBelajar(d) {
  const tgl = d.hari_belajar_terakhir;
  if (!tgl) return null;

  // Aritmetika tanggalnya milik `selisihHari()`, bukan milik layar ini. Versi
  // pertama menyalin tiga barisnya ke sini, dan salinan itu langsung menjadi
  // rumus kedua untuk pertanyaan yang sama. Tandanya sengaja dibalik di satu
  // tempat yang terlihat: `selisihHari` menghitung dari HARI INI ke depan,
  // jadi masa lalu negatif -- dan "12 hari lalu" adalah negatif itu dibalik.
  const hari = tanggalLokal(tgl);
  const selisih = -selisihHari(tgl);
  if (!hari || !selisih || selisih <= 0) return null;

  return h("div.celah", {},
    h("span", {}, "Hari belajar terakhir: "),
    h("b", {}, hari.toLocaleDateString("id-ID",
      { weekday: "long", day: "numeric", month: "long" })),
    h("span.celah-jarak", {}, ` · ${angka(selisih)} hari lalu`));
}

function tautanLangkah(s) {
  return `#/${s.tipe}/${s.bahasa}/${s.indeks}`;
}

/** Antrean hari ini: sisa langkah dari `saran.py` PLUS tantangan harian, jadi
 *  satu daftar.
 *
 *  Sebelumnya keduanya dua blok terpisah dengan dua judul, dan tantangannya
 *  bahkan punya kartunya sendiri lengkap dengan tombol — padahal keduanya
 *  menjawab pertanyaan yang sama persis ("apa lagi yang bisa kukerjakan
 *  sekarang") dan disusun modul yang sama. Dua daftar untuk satu pertanyaan
 *  memaksa orang membandingkan keduanya sebelum memilih. */
function blokAntrean(langkah, tantangan, ctx) {
  const siap = new Map((ctx.awal.bahasa || []).map((b) => [b.key, b.siap]));
  const baris = (s, cap) => h("a.baris", { href: tautanLangkah(s) },
    pilJenis(s.tipe),
    h("div.isi", {},
      h("div.judul", {}, tanpaNomor(s.judul)),
      h("div.ket", {}, `${s.label_bahasa} · ${s.alasan}` + (s.menit ? ` · ≈${s.menit} menit` : ""))),
    cap ? h("span.pil.pil-ungu.sembunyi-hp", {}, cap) : null,
    // Ditandai SEBELUM diklik, bukan sesudah. Latihan di bahasa yang
    // toolchain-nya belum terpasang tetap bisa dikerjakan dan ditandai
    // selesai sendiri — yang mati cuma penilaian otomatisnya — tapi orang
    // berhak tahu itu sebelum membuka halamannya, bukan sesudah menulis
    // tiga puluh baris kode. Aturan yang sama dipakai daftar materi untuk
    // bab yang masih terkunci: tandai lebih dulu, jangan menolak belakangan.
    s.tipe === "latihan" && siap.get(s.bahasa) === false
      ? h("span.pil.pil-kunci", {}, "tanpa nilai otomatis") : null,
    h("span.baris-panah", {}, ikon("lanjut", { ukuran: 18 })));

  const senarai = h("div.senarai", {},
    langkah.map((s) => baris(s, null)),
    tantangan ? baris(tantangan, "tantangan hari ini") : null);
  ungkap(senarai, { per: 46, geser: 10 });

  return h("section", {},
    h("div.bagian-kepala", {},
      h("span.mata", {}, "Antrean berikutnya"),
      h("a", { href: "#/cari" }, "Cari isi lain")),
    senarai);
}

/* Berapa banyak bara yang boleh menyala satu per satu.
 *
 * Angka ini pernah tidak ada, dan akibatnya terukur: seluruh 186 sel
 * dianimasikan sekaligus, 207 animasi hidup dalam satu frame, dan frame
 * terburuk melar sampai 255 md — tersendat persis di saat yang seharusnya
 * paling menyenangkan dilihat. Membatasinya bukan cuma lebih ringan, tapi juga
 * lebih benar: yang menarik perhatian di hamparan ini adalah hari-hari yang
 * MENYALA, bukan ratusan kotak dingin yang ikut berkedip masuk. */
const BARA_MAKS_ANIMASI = 48;

/** Kisi masuk sebagai satu kesatuan; bara yang menyala menyusul satu per satu,
 *  dari hari ini mundur ke belakang. Yang sedang dijalani lebih berarti
 *  daripada yang sudah lewat enam bulan lalu, jadi ia yang muncul lebih dulu. */
function nyalakanBara(petak, menyala) {
  if (!adaGerak()) return;
  const bara = menyala.slice(-BARA_MAKS_ANIMASI);

  // Di `halus` kaskadenya dilepas, bukan dipendekkan. Empat puluh delapan sel
  // yang menyala berurutan adalah contoh paling murni dari "bergerak SENDIRI":
  // tidak ada yang menunggunya, tidak ada pertanyaan yang dijawabnya, ia cuma
  // berlangsung -- dan di layar yang sama ada pil streak dan angka XP yang
  // justru ingin dibaca. Yang tetap hidup: kisinya masuk sebagai SATU kejadian,
  // bukan empat puluh delapan. Capnya tidak disentuh, `saatTampak` dan pengaman
  // 2,5 detik tetap di tempatnya, dan tiap sel tetap berakhir di keadaan
  // alaminya. Tingkatnya ditanyakan ke `gerakPenuh()`, yang meneruskan ke
  // `tingkatGerak()` -- satu-satunya yang boleh memutuskan (invarian #3).
  const delay = gerakPenuh()
    ? berurut(bara.length, { per: 12, maks: 340, dari: "akhir" })
    : () => 0;

  for (const el of bara) el.style.opacity = "0";

  // Pengamannya harus MEMATIKAN pemicunya, bukan cuma mengembalikan opacity.
  // Kalau tidak, kisi yang sudah telanjur terlihat akan dianimasikan masuk
  // dari nol begitu akhirnya tergulir ke layar — dan itu kedipan, bukan
  // animasi. Alasan lengkapnya ada di JAGA_MD, gerak.js.
  let menyerah = false;
  let hentikan = () => {};
  const jaga = setTimeout(() => {
    menyerah = true;
    hentikan();
    for (const el of bara) el.style.opacity = "";
  }, 2500);

  hentikan = saatTampak(petak, () => {
    if (menyerah) return;
    clearTimeout(jaga);
    masuk(petak, { geser: 6, zum: 1 });
    bara.forEach((el, i) => {
      el.style.opacity = "";
      // `scale`, BUKAN `transform`: `.bara-sel` punya `transition: transform`
      // untuk pembesaran hover, jadi menulis transform dari sini berarti dua
      // mesin pada satu properti (invarian #2). Properti transform mandiri
      // disusun SEBELUM `transform`, jadi keduanya bisa hidup bersamaan tanpa
      // saling menimpa: WAAPI memiliki `scale`, CSS memiliki `transform`.
      animasi(el, { opacity: [0, 1], scale: ["0.35", "1"] },
              { pegas: "jawab", delay: delay(i) });
    });
  }, { bagian: 0.15 });
}

/* Batas waktu pengamat ukuran kisi bara. Terukur: penyusutan kotak yang
   menyebabkan pin pertama salah terjadi dalam satu-dua frame sesudah
   pemasangan, jadi empat detik adalah kelonggaran besar -- dan ia ada supaya
   pengamatnya tidak hidup selamanya di layar yang dibuka lalu ditinggal. */
const PIN_BARA_MS = 4000;

/* Isyarat bahwa pengguna sudah mengambil alih gulirnya sendiri. `keydown`
   hanya bisa datang karena `.bara-petak` sekarang bisa difokus. */
const SENTUHAN_GULIR = ["wheel", "pointerdown", "keydown"];

/** Pin kisi pada HARI INI, dan LEPAS begitu penggunanya menyentuhnya.
 *
 *  Terukur sebelum perbaikan, profil 182 hari, empat jalur pemuatan
 *  (pemuatan-pertama | reload | kembali-lewat-rute | kembali-dari-layar-bahasa):
 *
 *    360 px :  80 benar | 80 benar |  0 SALAH |  0 SALAH
 *    1100 px:  80 SALAH | 117 benar|  0 SALAH |  0 SALAH
 *
 *  `requestAnimationFrame` polos hanya menang pada pemuatan yang beruntung:
 *  layar dibangun UTUH sebelum router menempelkannya, dan router masih
 *  menunggu animasi keluar layar sebelumnya. Di jalur "kembali lewat rute"
 *  frame itu selalu kalah, `scrollWidth` masih nol, dan pin-nya menjadi nol --
 *  tanpa satu pun pesan galat. Itu yang diurus `saatSiap()`.
 *
 *  Tapi `saatSiap` menjawab "elemennya sudah terpasang dan punya ukuran",
 *  BUKAN "ukurannya sudah berhenti berubah". Di 1100 px pemuatan pertama,
 *  `clientWidth` petak menyusut 299 -> 262 SESUDAH pemasangan (kolom sisi
 *  menyempit begitu isi kolom utama selesai ditata), jadi pin yang dihitung
 *  pada 299 mendarat di 80 padahal ujung yang benar 117. Pengamat ukuran ini
 *  yang menutup selisih itu.
 *
 *  Dan ia WAJIB lepas. Posisi gulir adalah keadaan PENGGUNA, bukan keadaan
 *  komponen; merebutnya kembali sesudah dia menggeser sendiri lebih buruk
 *  daripada tidak mem-pin sama sekali. Jadi: putus pada sentuhan pertama, dan
 *  putus pada batas waktu.
 *
 *  Tanpa `scrollIntoView` (ia menggulir semua leluhur -- lihat `bawaKeTengah`)
 *  dan tanpa animasi: `scroll-behavior` terhitung pada `.bara-petak` adalah
 *  `auto`, karena properti itu tidak mewaris dari `html`. */
function pinKeHariIni(petak, geser) {
  const pasang = () => {
    petak.scrollLeft = petak.scrollWidth;
    // Kondisi penanda tinggal di dalam callback yang sama dengan pin-nya.
    // Dihitung di luar, ia menjawab pertanyaan tentang kotak yang belum ada
    // dan melaporkan "tidak ada yang tersembunyi" sementara lima bulan berada
    // di luar kotaknya.
    geser.hidden = petak.scrollWidth <= petak.clientWidth;
  };

  saatSiap(petak, () => {
    pasang();
    if (typeof ResizeObserver !== "function") return;

    // Bandingkan lebarnya sendiri sebelum memasang ulang: `pasang()` menyentuh
    // `geser.hidden`, dan pengamat yang bereaksi pada akibat tulisannya sendiri
    // adalah lingkaran pengamat-ukuran, bukan perbaikan.
    let lebarTerakhir = petak.clientWidth;
    let lepas = () => {};
    const pengamat = new ResizeObserver(() => {
      if (petak.clientWidth === lebarTerakhir) return;
      lebarTerakhir = petak.clientWidth;
      pasang();
    });
    const jam = setTimeout(() => lepas(), PIN_BARA_MS);

    lepas = () => {
      clearTimeout(jam);
      pengamat.disconnect();
      for (const nama of SENTUHAN_GULIR) petak.removeEventListener(nama, lepas);
    };
    for (const nama of SENTUHAN_GULIR) {
      petak.addEventListener(nama, lepas, { passive: true });
    }
    pengamat.observe(petak);
  });
}

function blokBara(d) {
  const target = Math.max(1, d.target_harian);
  // Kisi ini menggulir ke samping, jadi ia WAJIB bisa difokus: tanpa
  // `tabindex`, Chrome dan Safari tidak memberi pengguna papan ketik satu pun
  // cara menggeser isinya, dan sesudah pin di bawah yang tidak terjangkau itu
  // justru lima bulan pertamanya. `role="group"` + nama supaya yang diumumkan
  // bukan "grup" kosong. `:focus-visible` global (gaya.css:608) sudah memberi
  // cincinnya, jadi tidak ada gaya fokus baru yang perlu ditulis di sini.
  const petak = h("div.bara-petak", {
    tabindex: "0",
    role: "group",
    "aria-label": "Hamparan XP harian enam bulan terakhir, bisa digeser ke samping",
  });
  const hariIni = hariIniISO();

  // Sisipkan sel kosong supaya kolom pertama jatuh di hari yang benar. Tanpa
  // ini seluruh kisi bergeser dan barisnya tidak lagi berarti "Senin".
  const pertama = d.heatmap[0];
  if (pertama) {
    const hari = (tanggalLokal(pertama.tanggal).getDay() + 6) % 7;
    for (let i = 0; i < hari; i++) {
      // Sel sungguhan berkelas, bukan div bergaya inline: ukurannya satu angka
      // yang hidup di CSS bersama `.bara-sel` dan `.bara-petak`. Tiga salinan
      // angka yang sama, dan yang akan pecah diam-diam adalah salinan yang
      // tidak pernah dilihat siapa pun.
      petak.appendChild(h("div.bara-kosong", { "aria-hidden": "true" }));
    }
  }
  const menyala = [];
  for (const s of d.heatmap) {
    const tingkat = s.xp <= 0 ? 0 : s.xp < target * 0.5 ? 1 : s.xp < target ? 2 : 3;
    const sel = h("div.bara-sel" + (tingkat ? ".bara-" + tingkat : "")
      + (s.tanggal === hariIni ? ".bara-kini" : ""),
      { title: `${tanggalRamah(s.tanggal)}: ${s.xp} XP` });
    if (tingkat) menyala.push(sel);
    petak.appendChild(sel);
  }
  nyalakanBara(petak, menyala);

  // Penanda "kisi ini bisa digeser". Lahir tersembunyi dan baru dibuka kalau
  // isinya memang lebih lebar dari kotaknya -- di 500 dan 860 px ia tidak
  // muncul karena di sana tidak ada yang tersembunyi. Memakai `hidden`, bukan
  // `display`, supaya komponen ini tidak menjadi satu lagi yang menyetel
  // display sendiri dan lupa mengembalikannya.
  // Arahnya disebut, bukan cuma keberadaannya. Sesudah kisinya dipin di ujung
  // kanan, yang tersembunyi ada di KIRI — penanda tanpa arah menyuruh orang
  // mencari ke tempat yang salah.
  const geser = h("span.bara-geser", { hidden: true },
    "· geser ke kiri untuk yang lebih lama");

  pinKeHariIni(petak, geser);

  const aktif = d.heatmap.filter((s) => s.xp > 0).length;
  return h("section", {},
    h("span.mata", {}, "Bara enam bulan terakhir"),
    h("div.kartu.kartu-rapat", {},
      petak,
      jedaBara(d.heatmap),
      h("div.bara-legenda", {},
        // "hari ber-XP", bukan "hari menyala" dan bukan "hari belajar".
        // `riwayat_harian` cuma mencatat hari yang MENGHASILKAN XP; hari yang
        // isinya bacaan setengah menaikkan streak tanpa meninggalkan entri
        // apa pun di sini. Kalimat yang menyebut "belajar" akan berdiri di
        // sebelah pil streak dan membantahnya (invarian #11).
        h("span", {}, `${angka(aktif)} hari ber-XP`),
        geser,
        // Rampa diberi kata di kedua ujungnya, bukan angka ambang: ambangnya
        // dihitung dari target harian yang bisa diubah, jadi angka apa pun di
        // sini akan jadi salinan kedua yang cepat basi.
        h("div.bara-rampa", {},
          h("span", {}, "sedikit"),
          h("div.bara-sel"), h("div.bara-sel.bara-1"),
          h("div.bara-sel.bara-2"), h("div.bara-sel.bara-3"),
          h("span", {}, "banyak XP")))));
}

/** Jeda terpanjang di dalam hamparan — dirender DI BAWAH kisi, bukan di dalamnya.
 *
 *  Letaknya bukan selera. `.bara-petak` adalah `grid-auto-flow: column` dengan
 *  tujuh baris tetap yang berarti Senin..Minggu; satu sisipan teks di dalamnya
 *  menelan satu slot dan menggeser SELURUH kolom sesudahnya — hari Rabu pindah
 *  ke baris Selasa, tanpa satu pun pesan galat, dan komponennya berhenti
 *  berarti sambil tetap terlihat rapi.
 *
 *  Kenapa jeda dan bukan total: hamparan enam bulan menunjukkan RITME. Yang
 *  tidak bisa dibaca dari ratusan kotak kecil justru yang paling ingin
 *  diketahui — di mana putusnya, dan apakah putusnya sudah selesai. */
function jedaBara(heatmap) {
  let jalan = 0, panjang = 0, akhir = -1; const mulai = heatmap.findIndex((s) => s.xp > 0);  // sebelum hari pertama ber-XP: belum mulai, bukan jeda
  heatmap.forEach((s, i) => {
    if (mulai < 0 || i < mulai) return; if (s.xp > 0) { jalan = 0; return; }
    jalan += 1;
    if (jalan > panjang) { panjang = jalan; akhir = i; }
  });
  // Di bawah sepekan itu akhir pekan biasa, bukan jeda. Menamainya "jeda" akan
  // membuat istirahat yang sehat terbaca sebagai kegagalan.
  if (panjang < 7) return null;

  const kapan = akhir === heatmap.length - 1
    ? "masih berlangsung"
    : `berakhir ${tanggalRamah(heatmap[akhir].tanggal)}`;
  return h("p.bara-jeda", {},
    `Jeda terpanjang ${angka(panjang)} hari tanpa XP, `,
    h("span.bara-jeda-kapan", {}, kapan));
}

/* ================================================================ bahasa */

export async function layarBahasa({ key }, ctx) {
  const b = await api.ambil("/api/bahasa", { key });
  const s = b.statistik;

  const isi = h("div");
  const daftarTab = ["materi", "kuis", "latihan", "bacaan"];
  const kunciTab = "tab." + key;

  // Toolchain yang belum terpasang ditandai SEBELUM diklik, bukan sesudah.
  // Tanpa ini satu-satunya tempat yang mengatakannya adalah blokToolchain di
  // badan halaman — dan orang yang langsung menuju tab Latihan atau Ruang coba
  // baru mengetahuinya setelah sampai di layar yang tidak bisa menjalankan
  // apa pun. Keduanya TETAP bisa dibuka: materinya tetap terbaca, dan
  // perintah pemasangannya justru ada di halaman ini.
  const belumSiap = !b.siap;
  const capBelumSiap = () => h("span.pil.pil-kunci", {},
    "perlu " + (b.hilang && b.hilang.length ? b.hilang.join(", ") : "dipasang"));

  const tombolTab = daftarTab.map((t) => h("button.tbl.tbl-hantu", {
    onclick: () => pilih(t),
    data: { tab: t },
    title: belumSiap && t === "latihan"
      ? "Latihan tetap bisa dibaca, tapi kodenya belum bisa dijalankan di mesin ini."
      : null,
  }, ikon(t === "bacaan" ? "pustaka" : ikonTipe(t), { ukuran: 17 }),
     `${t[0].toUpperCase()}${t.slice(1)}`,
     h("span.tab-jumlah", {},
       String(t === "bacaan" ? b.pustaka.total : b[t].length)),
     belumSiap && t === "latihan" ? capBelumSiap() : null));

  let tabKini = null;

  function pilih(t) {
    if (t === tabKini) return;
    const berganti = tabKini !== null;
    tabKini = t;
    ctx.ingat(kunciTab, t);
    for (const tb of tombolTab) {
      const ini = tb.dataset.tab === t;
      // .tbl-pilih, bukan .tbl-utama. Tab yang sedang terbuka adalah KEADAAN,
      // bukan tindakan yang disarankan — dan mewarnainya aksen penuh membuat
      // ia bersaing dengan kartu Lanjutkan yang justru dimaksudkan untuk
      // ditekan.
      tb.classList.toggle("tbl-pilih", ini);
      tb.classList.toggle("tbl-hantu", !ini);
      tb.setAttribute("aria-pressed", String(ini));
    }
    const baru = t === "kuis" ? daftarKuis(b, ctx)
      : t === "latihan" ? daftarLatihan(b, ctx)
      : t === "bacaan" ? daftarBacaan(b)
      : daftarMateri(b, ctx);

    // Berganti tab bukan berpindah halaman: daftarnya diganti di tempat, dan
    // gerakannya sengaja lebih pendek daripada pergantian layar supaya
    // perbedaan itu terbaca.
    isikan(isi, baru);
    if (berganti) masuk(baru, { geser: 7, pegas: "jawab" });
  }

  const el = h("div.masuk", {},
    h("header.kepala-besar.kepala-bersampul", {},
      h("div.kepala-teks", {},
        h("span.mata", {}, "Bahasa"),
        h("h1", {}, b.label),
        h("p.kepala-sub", {}, kalimatBahasa(b, s)),
        barisFakta(b, s)),
      h("div.kepala-sampul.kepala-rasi", {}, petaRasi(dariBahasa(b), { tinggi: 250 }))),

    kartuLanjutBahasa(b, key),

    b.siap ? null : blokToolchain(b),
    b.catatan ? keadaan({ gambar: "bantuan", judul: "Perlu diketahui",
                          ket: b.catatan }) : null,

    h("div.deret.tab-deret", {},
      tombolTab,
      // Dipisahkan dari tiga tab di sebelahnya, dan sengaja BUKAN .tbl-hantu:
      // dengan bentuk yang sama persis, ia terbaca sebagai "tab keempat yang
      // sedang tidak aktif" — padahal menekannya meninggalkan halaman ini.
      b.tebak && b.siap ? h("a.tbl.tbl-pergi.deret-kanan", { href: "#/tebak/" + key, title: "Latih membaca kode: tebak keluaran contoh materi yang sudah kamu baca" }, ikon("kuis", { ukuran: 17 }), "Tebak keluaran") : null, h("a.tbl.tbl-pergi" + (b.tebak && b.siap ? "" : ".deret-kanan"), { href: "#/coba?bahasa=" + b.runner },
        ikon("jalankan", { ukuran: 17 }), "Ruang coba " + b.label,
        belumSiap ? capBelumSiap() : null,
        ikon("lanjut", { ukuran: 15 }))),
    isi,
  );

  pilih(ctx.ingat(kunciTab) || "materi");
  return {
    el,
    judul: b.label,
    konteks: {
      balik: { label: "Dasbor", href: "#/dasbor" },
      bab: b.label,
      // Kalimat ringkas bab SENGAJA tidak ikut di sini walau muat. Ia sudah
      // berdiri di badan halaman, dan strip ini menyembunyikan bagian
      // tengahnya di layar sempit — jadi menaruhnya di dua tempat berarti
      // mengulang di layar lebar dan menghilang di layar sempit, dua-duanya
      // salah untuk kalimat yang justru paling menerangkan halaman ini.
      posisi: `${s.materi}/${s.total_materi} materi`,
      persen: s.persen,
    },
  };
}

/** Satu kalimat yang menempatkan bahasa ini dalam gambar besar, sebelum angka
 *  apa pun muncul. Deretan "0/26 · 0/7 · 0/15" yang dulu berdiri di sini
 *  adalah jawaban atas pertanyaan yang belum ditanyakan siapa pun saat baru
 *  membuka sebuah halaman. */
function kalimatBahasa(b, s) {
  const total = s.total_materi + s.total_kuis + s.total_latihan;
  if (s.persen >= 100) {
    return `Semuanya sudah kamu selesaikan: ${total} bagian, tuntas.`;
  }
  if (s.persen <= 0) {
    return `Belum dimulai. Jalurnya ${s.total_materi} materi, diselingi `
      + `${s.total_kuis} kuis dan ${s.total_latihan} latihan.`;
  }
  return `Sudah ${bulat(s.persen)}% jalan. Lanjutkan dari tempat kamu berhenti.`;
}

/* Baris fakta di kepala halaman: beberapa angka berikon yang menjawab "apa
   isinya, seberapa besar, dan apakah bisa dijalankan di komputerku" — sebelum
   ada satu pun daftar yang perlu dibaca. */
function barisFakta(b, s) {
  const fakta = [
    ["materi", `${s.total_materi} materi`],
    ["kuis", `${s.total_kuis} kuis`],
    ["latihan", `${s.total_latihan} latihan`],
    [b.siap ? "selesai" : "belum",
     b.siap ? "kode bisa dijalankan"
            : "butuh " + (b.hilang || []).join(", ")],
  ];
  return h("div.fakta", {}, fakta.map(([gambar, teks], i) =>
    h("div.fakta-butir" + (i === 3 && !b.siap ? ".fakta-kurang" : ""), {},
      ikon(gambar, { ukuran: 19 }), h("span", {}, teks))));
}

/** Tindakan utama halaman bahasa: satu tautan menuju hal berikutnya.
 *
 *  Yang dipakai di sini hanya `status` yang SUDAH dikirim server — tidak ada
 *  satu pun keputusan "selesai" atau "lulus" yang dihitung ulang di browser.
 *  Aturan itu dipegang di seluruh antarmuka web (lihat AGENTS.md); yang
 *  dikerjakan fungsi ini murni memilih tautan mana yang paling masuk akal
 *  untuk ditawarkan lebih dulu.
 *
 *  Materi yang masih TERKUNCI dilewati. Menawarkannya sebagai tindakan utama
 *  berarti tombol paling terang di halaman ini berujung di layar penolakan —
 *  persis yang dilarang aturan "tidak boleh ada tombol yang berujung
 *  penolakan". Statusnya tetap dibaca dari server, tidak dihitung ulang. */
function kartuLanjutBahasa(b, key) {
  const materi = b.materi.find((m) => m.status !== "selesai" && !m.terkunci);
  const kuis = b.kuis.find((q) => q.jatuh_tempo || (!q.pernah && q.siap)) || b.kuis.find((q) => !q.pernah);
  const latihan = b.latihan.find(
    (e) => e.status !== "lulus" && e.status !== "manual");

  let s = null;
  if (materi && !(kuis && !kuis.pernah && kuis.siap && materi.status !== "sebagian")) {
    s = { tipe: "materi", indeks: materi.indeks, judul: materi.judul,
          mata: materi.status === "sebagian" ? "Lanjutkan bacaan"
                                             : "Mulai dari sini",
          ket: materi.status === "sebagian"
            ? "Kamu berhenti di tengah materi ini."
            : "Materi berikutnya yang belum dibaca." };
  } else if (kuis) {
    s = { tipe: "kuis", indeks: kuis.indeks, judul: kuis.judul,
          mata: "Uji pemahaman",
          ket: kuis.pernah ? "Sudah waktunya kuis ini diulang."
                           : "Semua materi yang diuji kuis ini sudah kamu baca." };
  } else if (latihan) {
    s = { tipe: "latihan", indeks: latihan.indeks, judul: latihan.judul,
          mata: "Tulis kodenya",
          ket: "Bagian yang mengubah bacaan jadi kemampuan." };
  }

  if (!s) {
    return keadaan({
      jenis: "tuntas",
      gambar: "selesai",
      judul: "Tidak ada yang tersisa di sini.",
      ket: "Materi, kuis, dan latihannya sudah kamu selesaikan semua. "
        + "Kuisnya akan muncul lagi sendiri saat waktunya diulang.",
    });
  }

  return h("a.lanjutkan.lanjutkan-rapat",
    { href: `#/${s.tipe}/${key}/${s.indeks}` },
    h("span.lanjutkan-nomor", {}, String(s.indeks + 1)),
    h("div.lanjutkan-isi", {},
      h("span.mata", {}, s.mata),
      h("h2", {}, tanpaNomor(s.judul)),
      h("p", {}, s.ket)),
    h("span.lanjutkan-tbl", {},
      h("span", {}, "Buka"), ikon("lanjut", { ukuran: 20 })));
}

function blokToolchain(b) {
  return keadaan({
    jenis: "salah",
    gambar: "belum",
    judul: `Kode ${b.label} belum bisa dijalankan di komputer ini`,
    ket: `Yang belum terpasang: ${b.hilang.join(", ")}. Materi dan kuis tetap `
      + "berjalan penuh; yang mati hanya penilaian otomatis latihan, dan "
      + "latihannya tetap bisa dikerjakan lalu ditandai selesai sendiri.",
    aksi: b.pasang ? [
      h("code.berkas-jalur", {}, b.pasang),
      h("button.tbl.tbl-kecil", {
        onclick: () => salin(b.pasang, "Perintah disalin. Tempel di terminal."),
      }, "Salin"),
    ] : [],
  });
}

/* Ketiga daftar di bawah memakai ungkap(): isinya baru masuk saat benar-benar
   tergulir ke layar. Beberapa bahasa punya lebih dari dua puluh materi, dan
   menganimasikan dua puluh baris sekaligus — sebagian besar di luar layar —
   cuma memperpanjang urutannya tanpa ada yang melihat. */

/** Daftar materi, dikelompokkan per bab dan BISA DILIPAT.
 *
 *  Yang TIDAK dilakukan di sini: memutuskan sendiri sebuah bab terkunci atau
 *  tidak. Statusnya sudah jadi saat sampai — dihitung `bab.py` lalu dikirim
 *  server (lihat AGENTS.md: definisi kedua tentang "boleh dibuka" adalah cara
 *  tercepat membuat terminal dan web berbeda pendapat soal hal yang sama).
 *  Kode di bawah cuma menggambarnya.
 *
 *  Pelipatannya menyelesaikan masalah paling nyata di halaman ini: HTML punya
 *  11 bab berisi 44 materi, dan dirender penuh semuanya halamannya lima ribu
 *  piksel — tanpa satu titik pun yang menjawab "ada berapa bab dan aku di
 *  mana" tanpa menggulir seluruhnya lebih dulu. Peta bab di atas menjawab itu
 *  dalam satu baris, dan yang terbuka secara bawaan cuma bab yang SEDANG
 *  dikerjakan.
 *
 *  Yang terkunci tetap ditampilkan — judulnya, tingkatnya, jumlah materinya,
 *  dan alasannya, semuanya di KEPALA bab yang tidak pernah ikut terlipat. Jadi
 *  tidak ada satu keterangan pun yang hilang; yang hilang cuma empat puluh
 *  baris judul materi yang memang belum boleh dibuka. */
function daftarMateri(b, ctx) {
  const daftar = b.bab || [];
  const wadah = h("div", {},
    b.bab_kalimat || b.buka_semua_bab
      ? h("div.bab-ringkas", {},
          b.bab_kalimat ? h("p", {}, b.bab_kalimat) : null,
          // Saat saklarnya menyala, yang perlu dijawab halaman ini bukan
          // "kenapa bab ini terbuka" melainkan "kenapa TIDAK ADA yang
          // terkunci" — dan pertanyaan itu datang berbulan-bulan sesudah
          // saklarnya dipindahkan, ketika alasannya sudah lama lupa.
          b.buka_semua_bab
            ? h("p.bab-bebas", {}, "Penguncian bab sedang dimatikan: semua "
                + "bab terbuka tanpa syarat. ",
                h("a", { href: "#/atur" }, "Ubah di Pengaturan"), ".")
            : null)
      : null);

  // Satu bab saja berarti tidak ada yang dikelompokkan: bahasa itu belum
  // punya pembagian bab, dan kepala "Semua materi" di atas seluruh daftarnya
  // cuma satu lapis tambahan yang tidak menjawab apa pun. Batas yang sama
  // dipakai bab.kalimat_ringkas(), yang juga diam kalau babnya cuma satu.
  if (daftar.length < 2) {
    wadah.appendChild(ungkapSenarai(
      h("div.senarai", {}, b.materi.map((m) => barisMateri(b, m))), ctx, b.key));
    return wadah;
  }

  const materi = new Map(b.materi.map((m) => [m.indeks, m]));
  // Bab terkunci PERTAMA adalah satu-satunya pintu yang benar-benar dihadapi
  // orang sekarang; sisanya menunggu di belakangnya. Jalan pintas ke
  // Pengaturan ditempel di situ saja — tawaran yang sama persis diulang tiga
  // kali di satu layar berhenti terbaca sebagai tawaran, dan mulai terbaca
  // sebagai bujukan untuk melewati jalurnya.
  const pintu = daftar.find((x) => x.status === "terkunci");
  const sedang = daftar.find((x) => x.status === "terbuka");

  wadah.appendChild(petaBab(daftar, sedang, ctx));

  const petak = h("div.bab-daftar", {}, daftar.map((bab) => {
    const terbuka = bab === sedang || (!sedang && bab === daftar[0]);
    return h(
      "details.bab"
        + (bab.status === "terkunci" ? ".bab-terkunci"
           : bab.status === "tuntas" ? ".bab-tuntas" : "")
        + (bab === sedang ? ".bab-kini" : ""),
      { id: "bab-" + bab.nomor,
        "aria-label": `Bab ${bab.nomor}: ${bab.judul}`,
        // Penyaring membaca tingkat dari DOM, bukan dari array paralel: array
        // kedua yang harus tetap seurutan dengan yang pertama adalah cara
        // termudah membuat chip "Dasar" menyembunyikan bab yang salah.
        data: { tingkat: bab.tingkat },
        // Yang terbuka cuma bab yang sedang dikerjakan — dan kalau tidak ada
        // satu pun yang berstatus "terbuka" (semuanya tuntas), bab PERTAMA yang
        // dibuka supaya halaman ini tidak pernah tampil sebagai sebelas kepala
        // tanpa satu pun isi.
        open: terbuka },
      kepalaBab(bab, sedang, b.key),
      // `.masuk-mandiri` (util S01) dipakai apa adanya, bukan mesin entrance
      // kedua. Ia `@starting-style` + `transition-behavior: allow-discrete`, jadi
      // di browser tanpa dukungan itu — dan saat gerak dimatikan — isinya tetap
      // muncul apa adanya, bukan tertinggal pada opacity nol.
      //
      // Bab yang SUDAH terbuka saat halaman digambar tidak mendapatkannya:
      // `@starting-style` juga menyala pada render pertama, dan itu akan
      // bertumpuk di atas koreografi masuk `.bab` yang membungkusnya. Bab yang
      // tertutup tidak merender isinya, jadi ia baru menyala saat benar-benar
      // dibuka — persis kejadian yang mau dijelaskan.
      h("div.bab-isi" + (terbuka ? "" : ".masuk-mandiri"), {},
        bab.status === "terkunci" ? catatanKunci(bab, bab === pintu) : null,
        h("div.senarai", {}, bab.materi
          .map((i) => materi.get(i))
          .filter(Boolean)
          .map((m) => barisMateri(b, m)))));
  }));

  // Yang diungkap BAB-nya, bukan tiap barisnya. Sesudah dikelompokkan, satuan
  // yang berarti di halaman ini adalah bab — dan mengungkapkan dua puluh baris
  // satu per satu di dalam kepala bab yang sudah berdiri duluan cuma
  // memperpanjang urutannya tanpa menambah arti.
  // Cap 240 ms dipertahankan apa adanya: `berurut()` membaginya
  // (maks / jarakMaks), jadi sebelas bab mendapat langkah ~24 ms dan totalnya
  // tetap di bawah cap tanpa satu angka pun perlu disetel ulang.
  ungkapSekali(petak, ctx, b.key,
               { per: 40, maks: 240, geser: 9, pegas: "jawab" });

  const saring = saringBab(petak, daftar, ctx);
  if (saring) wadah.appendChild(saring);
  wadah.appendChild(petak);
  return wadah;
}

/** Chip tingkat yang menyaring bab yang SUDAH ADA, bukan memuat ulang apa pun.
 *
 *  Labelnya dari server (invarian #12). Tanpa chip yang ditekan, semuanya
 *  tampil — jadi keadaan diamnya adalah keadaan lengkap, dan tidak ada pilihan
 *  bawaan yang diam-diam menyembunyikan sesuatu dari orang yang belum pernah
 *  menyentuh chip-nya.
 *
 *  Yang berpindah posisi digerakkan `tata()` (FLIP pada `transform`); yang
 *  baru muncul cuma memudar masuk. `width`/`height` tidak pernah dianimasikan:
 *  bab yang hilang menghilang dari alur kisi, dan menganimasikan tingginya
 *  berarti membayar layout tiap frame untuk sebelas kotak sekaligus.
 *
 *  Yang keluar TIDAK dipudarkan, dan itu keputusan yang diukur bukan
 *  kelalaian: memudarkan sesuatu yang berakhir di `display: none` menuntut
 *  lintasan tata letak KEDUA, dan lintasan kedua itu membuat FLIP yang tersisa
 *  mengukur geometri yang sudah salah. Hilangnya dijelaskan oleh bab-bab yang
 *  meluncur menutup celahnya — itu justru seluruh guna FLIP. */
function saringBab(petak, daftar, ctx) {
  const tersedia = (ctx && ctx.awal && ctx.awal.aturan_bab
    && ctx.awal.aturan_bab.tingkat) || [];
  const kelompok = tersedia.filter((t) => daftar.some((b) => b.tingkat === t.nama));
  // Satu tingkat berarti tidak ada yang bisa disaring; chip tunggal yang
  // menyembunyikan segalanya atau tidak sama sekali bukan penyaring.
  if (kelompok.length < 2) return null;

  const pilih = new Set();
  const jumlahEl = h("span.bab-saring-jml", { role: "status" }, "");
  const tombol = [];

  /** Setel keadaan tampak/tersembunyi tanpa menyentuh tata letak sama sekali.
   *
   *  Dipakai untuk gambar PERTAMA, saat `petak` masih lepas dari dokumen.
   *  Versi beranimasi di bawah memanggil `tata()`, dan `tata()` membaca
   *  `getBoundingClientRect()` — pada pohon yang belum terpasang angkanya nol,
   *  dan nol itu tidak datang sebagai galat. Kebetulan nol-lawan-nol membuat
   *  `tata()` menganggap semuanya diam dan tidak menganimasikan apa pun, jadi
   *  cacatnya tidak pernah terlihat; ia tetap pembacaan tata letak di waktu
   *  yang dilarang (invarian #15a), dan sesi berikutnya yang menambah satu
   *  elemen bergerak di sini akan menemukannya sebagai lompatan. */
  function gambarSaring() {
    const semua = [...petak.children];
    const setelah = new Set(semua.filter(
      (el) => pilih.size === 0 || pilih.has(el.dataset.tingkat)));
    for (const el of semua) el.hidden = !setelah.has(el);
    tandaiTombol();
    tulisJumlah(setelah.size, semua.length);
    return { semua, setelah };
  }

  function tandaiTombol() {
    for (const tb of tombol) {
      const aktif = pilih.has(tb.dataset.tingkat);
      tb.classList.toggle("tbl-pilih", aktif);
      tb.classList.toggle("tbl-hantu", !aktif);
      tb.setAttribute("aria-pressed", String(aktif));
    }
  }

  function tulisJumlah(tampil, total) {
    jumlahEl.textContent = pilih.size === 0
      ? `${total} bab, semuanya ditampilkan`
      : `${tampil} dari ${total} bab ditampilkan`;
  }

  function terapkan() {
    const semua = [...petak.children];
    const lolos = (el) => pilih.size === 0 || pilih.has(el.dataset.tingkat);
    const setelah = new Set(semua.filter(lolos));
    const tetap = semua.filter((el) => !el.hidden && setelah.has(el));
    const baru = semua.filter((el) => el.hidden && setelah.has(el));

    /* `tetap` saja yang di-FLIP: elemen tersembunyi punya kotak batas nol, jadi
       memasukkannya ke `tata()` akan menghasilkan translasi sebesar seluruh
       halaman.

       Kalimat itu benar SEKARANG, dan ia tidak benar saat pertama kali ditulis.
       S05 mengirimnya sebagai premis, bukan sebagai pengukuran — dan `.bab`
       waktu itu tidak ada di daftar pemulih `[hidden]` (gaya.css), jadi
       `hidden` tidak pernah menyembunyikan apa pun: kotaknya penuh, tinggi
       `.bab-daftar` tidak bergerak (1623 -> 1623), dan `tata()` menganggap
       semuanya diam. Seluruh koreografi di bawah tidak pernah sekali pun
       berjalan, dan suite tetap hijau karena tesnya membaca atribut.

       Sesudah `.bab[hidden]` dipasang, angkanya diukur ulang dan koreografinya
       ternyata benar apa adanya — tidak ada yang perlu disederhanakan:

         saring ke `dasar`    : tinggi 1623 -> 714,  0 transform
                                (penyintasnya awalan DOM, memang tidak bergeser)
         saring ke `menengah` : tinggi 1623 -> 630,  5 transform
         saring ke `mahir`    : tinggi 1623 -> 227,  2 transform,
                                translate3d(0, 1396px) = tepat selisih tingginya

       `scale` tetap 1,0000 di semuanya, jadi tidak ada teks yang direntangkan. */
    tata(tetap, () => {
      for (const el of semua) el.hidden = !setelah.has(el);
    }, { pegas: "jawab" });

    for (const el of baru) {
      // `ungkap()` bisa meninggalkan `opacity: 0` inline pada bab yang belum
      // pernah tergulir ke layar. Dibersihkan dulu: kalau tidak, animasi ini
      // berakhir di nilai inline itu dan babnya tetap tak terlihat — keadaan
      // akhir animasi wajib keadaan alami elemennya.
      el.style.opacity = "";
      animasi(el, { opacity: [0, 1] }, { pegas: "halus" });
    }

    tandaiTombol();
    tulisJumlah(setelah.size, semua.length);
  }

  for (const t of kelompok) {
    const jml = daftar.filter((b) => b.tingkat === t.nama).length;
    const tb = h("button.tbl.tbl-hantu.bab-saring", {
      type: "button",
      title: t.ket,
      "aria-pressed": "false",
      data: { tingkat: t.nama },
      onclick: () => {
        if (pilih.has(t.nama)) pilih.delete(t.nama);
        else pilih.add(t.nama);
        terapkan();
      },
    }, t.label, h("span.tab-jumlah", {}, String(jml)));
    tombol.push(tb);
  }

  gambarSaring();
  return h("div.deret.bab-saring-deret", {},
    h("span.mata", {}, "Saring tingkat"), tombol,
    h("span.deret-kanan", {}, jumlahEl));
}

/** Peta bab: seluruh bab bahasa ini dalam satu baris segmen bernomor.
 *
 *  Ini kompensasi langsung dari pelipatan di bawahnya. Begitu isi bab boleh
 *  tertutup, harus ada satu tempat yang tetap memperlihatkan JALUR
 *  keseluruhannya — ada berapa, sudah sampai mana, dan mana yang masih
 *  terkunci — tanpa satu gulir pun. */
function segmenBab(bab, sedang) {
  return h("a." + (bab.status === "tuntas" ? "peta-tuntas"
      : bab.status === "terkunci" ? "peta-terkunci"
      : bab === sedang ? "peta-kini" : "peta-jalan"), {
      href: "#bab-" + bab.nomor,
      // Bab terkunci membawa ALASANNYA, bukan cuma penanda bahwa ia terkunci.
      // Kalimatnya datang utuh dari `bab.py` (invarian #12); halaman ini tidak
      // merumuskan ulang aturannya, cuma meneruskannya ke tempat yang bisa
      // dibaca sebelum diklik.
      title: `Bab ${bab.nomor} · ${bab.judul}: ${bab.selesai}/${bab.jumlah} `
        + `materi (${bab.label_tingkat.toLowerCase()})`
        + (bab.alasan ? ". " + bab.alasan : ""),
      // Tautan ini menunjuk id di halaman yang sama, bukan rute. Router
      // membaca fragmen sebagai alamat layar, jadi pemindahannya diurus di
      // sini dan hash-nya tidak pernah ikut berubah — kalau tidak, mengeklik
      // "Bab 5" akan mendarat di dasbor.
      onclick: (e) => {
        e.preventDefault();
        const sasaran = document.getElementById("bab-" + bab.nomor);
        if (!sasaran) return;
        sasaran.open = true;
        sasaran.scrollIntoView({
          behavior: adaGerak() ? "smooth" : "auto", block: "start" });
      },
    },
      h("span", {}, String(bab.nomor)),
      h("i", { gaya: { opacity: String(0.35 + 0.65 * (bab.persen / 100)) } }));
}

/** Peta bab: satu rail per tingkat, bukan satu barisan panjang tanpa batas.
 *
 *  Sebelas bab dalam satu deretan menjawab "ada berapa", tapi tidak menjawab
 *  "sampai mana yang masih dasar". Tingkat adalah pembagian yang sudah dipakai
 *  kurikulumnya sendiri — labelnya dan keterangannya datang dari server
 *  (`ctx.awal.aturan_bab.tingkat`, yang isinya `bab.LABEL_TINGKAT` dan
 *  `bab.KETERANGAN_TINGKAT`), jadi halaman ini tidak menamai tingkat dengan
 *  kata-katanya sendiri (invarian #12).
 *
 *  Bab terkunci TETAP ditampilkan, beserta alasannya di `title` — yang
 *  disembunyikan cuma daftar judul materinya, dan itu ada di `<details>`
 *  di bawah, bukan di sini.
 *
 *  Rail tidak ikut disaring chip tingkat: yang digambarkannya adalah SELURUH
 *  jalur bahasa itu, dan jalur yang ikut menyusut saat disaring berhenti bisa
 *  menjawab "ada berapa seluruhnya". */
function petaBab(daftar, sedang, ctx) {
  const tersedia = (ctx && ctx.awal && ctx.awal.aturan_bab
    && ctx.awal.aturan_bab.tingkat) || [];
  const kelompok = tersedia.filter((t) => daftar.some((b) => b.tingkat === t.nama));

  const nav = h("nav.peta-bab", { "aria-label": "Peta bab" },
    kelompok.length
      ? kelompok.map((t) => {
          const isi = daftar.filter((b) => b.tingkat === t.nama);
          return h("div.peta-tingkat", {},
            h("span.peta-label", { title: t.ket }, t.label,
              h("span.peta-jml", {}, String(isi.length))),
            h("div.peta-rel", {}, isi.map((bab) => segmenBab(bab, sedang))));
        })
      // Server tanpa `aturan_bab` (atau bahasa yang semua babnya satu tingkat)
      // tetap dapat railnya, cuma tanpa kepala tingkat. Tidak ada label yang
      // dikarang di sini sebagai gantinya.
      : h("div.peta-rel", {}, daftar.map((bab) => segmenBab(bab, sedang))));

  /* TIDAK ADA pemusatan gulir di sini, dan itu hasil pengukuran, bukan
   * kelalaian. Versi pertama fungsi ini memanggil `saatSiap()` +
   * `bawaKeTengah()` untuk membawa `.peta-kini` ke tengah rail-nya. Lalu
   * dihitung: bab terbanyak dalam SATU tingkat di seluruh 19 bahasa adalah
   * lima (python, menengah). Lima segmen butuh 5x42 + 4x4 = 226 px; rail
   * tersempit yang ada — kolom isi pada viewport 360 px — 336 px. Diukur di
   * keempat ukuran huruf (15/16/18/20 px) railnya tetap tidak meluber:
   * `scrollWidth - clientWidth = 0` di semuanya.
   *
   * Jadi pemusatan itu kode yang tidak bisa pernah berjalan, dan repo ini sudah
   * empat kali kena cacat "aturan yang tidak menggambar apa pun". Yang
   * sebenarnya menyelesaikan masalahnya adalah pengelompokan per tingkat itu
   * sendiri: sebelas segmen berderet memang perlu digulir, tiga rail berisi
   * empat sampai lima segmen tidak.
   *
   * `overflow-x: auto` di CSS TETAP ada dan itu bukan hal yang sama: ia pagar
   * deklaratif yang menjaga `min-width: 42px` tidak menumpahkan rail ke halaman
   * kalau suatu hari sebuah bahasa punya dua belas bab dalam satu tingkat. Yang
   * dibuang adalah mesin yang berjalan tiap render lalu tidak melakukan apa
   * pun — termasuk satu pembacaan `getBoundingClientRect` yang tidak
   * dibutuhkan siapa pun. */
  return nav;
}

/** Cincin persen kecil yang MEMELUK nomor bab.
 *
 *  Menggantikan bilah di ujung kanan kepala, bukan menemaninya: dua gambar
 *  untuk satu angka adalah satu gambar yang tidak dipercaya. Yang dimenangkan
 *  dengan memindahkannya ke kolom nomor adalah pembandingan — kolom itu sudah
 *  jadi penggaris halaman ini, sebelas cincinnya berjajar rata pada ukuran yang
 *  sama persis, dan "bab mana yang paling jauh" terbaca tanpa membaca angka.
 *
 *  Pola `cincinLevel`: `stroke-dashoffset` AKHIR dipasang langsung, animasinya
 *  cuma berangkat dari lingkaran kosong. Kalau gerak dimatikan, animasinya
 *  dibatalkan, atau JS tidak jalan sama sekali, yang tertinggal tetap busur
 *  dengan panjang yang benar (keadaan akhir = keadaan alami).
 *
 *  Hanya bab yang SEDANG dikerjakan yang beranimasi. Sebelas busur yang
 *  mengisi diri bersamaan adalah sebelas gerakan yang tidak menjawab satu
 *  pertanyaan pun — anggaran gerak halaman ini sudah dipakai koreografi masuk
 *  daftarnya. */
function cincinBab(bab, animasikan) {
  const R = 15;
  const keliling = 2 * Math.PI * R;
  const akhir = keliling * (1 - Math.max(0, Math.min(1, bab.persen / 100)));
  const NS = "http://www.w3.org/2000/svg";

  const svg = document.createElementNS(NS, "svg");
  svg.setAttribute("viewBox", "0 0 36 36");
  svg.setAttribute("aria-hidden", "true");
  let isi = null;
  for (const kelas of ["alur", "isi"]) {
    const c = document.createElementNS(NS, "circle");
    c.setAttribute("cx", "18");
    c.setAttribute("cy", "18");
    c.setAttribute("r", String(R));
    c.setAttribute("fill", "none");
    c.setAttribute("stroke-width", "3");
    c.setAttribute("class", kelas);
    svg.appendChild(c);
    if (kelas === "isi") isi = c;
  }
  isi.setAttribute("stroke-dasharray", String(keliling));
  isi.setAttribute("stroke-dashoffset", String(akhir));

  const el = h("div.bab-cincin", {},
    svg, h("span.bab-nomor", {}, String(bab.nomor).padStart(2, "0")));
  if (animasikan) {
    saatTampak(el, () => {
      animasi(isi, { strokeDashoffset: [String(keliling), String(akhir)] },
              { pegas: "panjang", durasi: 700 });
    }, { bagian: 0.4 });
  }
  return el;
}

/** Kepala satu bab: nomor besar, tingkat, judul, satu kalimat isi, kemajuan.
 *
 *  NOMOR ADALAH ARSITEKTUR — ini penerapannya yang paling langsung. Nomor bab
 *  tampil sebesar judulnya sendiri, di kolomnya sendiri, dengan angka tabular
 *  supaya sebelas bab berjajar rata. Mata memakai kolom itu sebagai penggaris,
 *  dan "aku di bab berapa" berhenti butuh dibaca.
 *
 *  Tingkat memakai warnanya sendiri (hijau → cyan → pink) dan sengaja BUKAN
 *  aksen, walau tangga kesulitan latihan memakainya. Di halaman ini ada satu
 *  bab yang sedang dikerjakan, dan aksen sudah dipakai untuk menandai bab itu;
 *  memberi warna yang sama kepada setiap pil "Menengah" berarti membuat
 *  penanda itu hilang di tengah keramaian. */
function kepalaBab(bab, sedang, kunci) {
  return h("summary.bab-kepala", {},
    cincinBab(bab, bab === sedang),
    h("div.bab-teks", {},
      h("div.bab-atas", {},
        h("span.pil.bab-tingkat.bab-" + bab.tingkat,
          { title: "Tingkat " + bab.label_tingkat.toLowerCase() },
          bab.label_tingkat),
        bab.status === "terkunci"
          ? h("span.pil.bab-cap", {}, "belum terbuka") : null,
        bab.status === "tuntas"
          ? h("span.pil.pil-tumbuh", {},
              ikon("selesai", { ukuran: 13, tebal: 2 }), "tuntas") : null),
      h("h3.bab-judul", {}, bab.judul),
      bab.ket ? h("p.bab-ket", {}, bab.ket) : null),
    h("div.bab-maju", {},
      h("span.bab-angka", {}, `${bab.selesai}/${bab.jumlah} materi`)),
    // Benih dan ukurannya SAMA dengan sampul di kepala materi bab ini, jadi
    // gambar yang dilihat di daftar adalah gambar yang menyambut di halaman.
    h("span.bab-sampul", { kelas: bab.status === "terkunci" ? "bab-sampul-kunci" : "" },
      sampul(`${kunci}/bab-${bab.nomor}`, { bahasa: kunci, lebar: 320, tinggi: 220 })),
    h("span.bab-lipat", {}, ikon("lanjut", { ukuran: 18 })));
}

/** Kenapa sebuah bab masih terkunci, dan — sekali saja — jalan keluarnya.
 *
 *  Kalimatnya datang utuh dari `bab.py`; ia sudah menyebut berapa materi lagi
 *  yang kurang dan di bab mana. Menyusun ulang kalimat itu di sini berarti
 *  aturan yang sama dijelaskan dengan dua cara berbeda di dua antarmuka. */
function catatanKunci(bab, tawarkanJalan) {
  return h("div.bab-kunci", {},
    h("span", {}, bab.alasan),
    tawarkanJalan
      ? h("a.bab-kunci-jalan", { href: "#/atur" },
          "Sudah pernah belajar bahasa ini? Buka semua bab di Pengaturan.")
      : null);
}

/** Satu baris materi. Yang terkunci tetap ditampilkan utuh — judulnya,
 *  nomornya, panjangnya — tapi bukan sebagai tautan.
 *
 *  Sengaja <div>, bukan <a> yang dimatikan lewat CSS: baris yang tidak bisa
 *  dibuka juga tidak boleh disinggahi Tab, dan pembaca layar tidak boleh
 *  mengumumkannya sebagai tautan. Menyembunyikannya sama sekali bukan
 *  pilihan — orang perlu tahu apa yang menantinya, dan itu justru seluruh
 *  alasan bab ini ada. */
function barisMateri(b, m) {
  const isi = [
    h("span.nomor", {}, String(m.indeks + 1)),
    h("span.titik" + (m.status === "selesai" ? ".selesai"
      : m.status === "sebagian" ? ".sedang" : ""), {}),
    h("div.isi", {},
      h("div.judul", {}, tanpaNomor(m.judul)),
      m.status === "sebagian"
        ? h("div.ket", {}, "berhenti di tengah, belum dihitung selesai") : null),
    m.bookmark ? h("span.pil.pil-nyala", {}, "ditandai") : null,
    h("span.baris-sisi.sembunyi-hp", {}, m.menit ? `≈${m.menit} menit` : `${m.bagian} bagian`),
  ];
  if (m.terkunci) return h("div.baris.baris-terkunci", {}, isi);
  return h("a.baris", {
    href: `#/materi/${b.key}/${m.indeks}`,
    kelas: m.status === "selesai" ? "selesai" : "",
  }, isi);
}

/* Prefiks kunci ingatan untuk "daftar bahasa ini sudah pernah dikoreografikan".
   Ikut `belajar.ingat.*` yang sudah dipakai tab terakhir dan draf ruang coba;
   bentuk penuhnya `belajar.ingat.dirender.<bahasa>` dan ia dikunci tes sendiri. */
const KUNCI_DIRENDER = "dirender.";

/** Ungkap sebuah daftar SEKALI per bahasa, tidak tiap kali layarnya digambar.
 *
 *  Halaman bahasa adalah tujuan paling sering dibuka di aplikasi ini, dan
 *  jalur yang paling sering dilalui bukan "buka pertama kali" melainkan
 *  "kembali dari materi yang baru dibaca". Mengulang koreografi 44 baris pada
 *  setiap kali kembali membuat gerakan yang tadinya menyenangkan berubah jadi
 *  pajak: ia menunda daftar yang sudah dihafal orangnya, di layar yang ia
 *  buka justru untuk melanjutkan. Itu cara tercepat membuat aplikasi terasa
 *  lambat, dan ia tidak muncul sebagai satu pun angka yang jelek.
 *
 *  Yang dimatikan HANYA gerakan masuknya. Daftarnya tetap lengkap, tetap
 *  terbaca, tetap tanpa JS — `ungkap()` yang tidak dipanggil berarti tidak ada
 *  yang pernah menyetel `opacity: 0`, jadi keadaan diamnya memang keadaan
 *  akhirnya (keadaan akhir = keadaan alami). */
function ungkapSekali(el, ctx, key, opsi) {
  if (!ctx || !key) { ungkap(el, opsi); return el; }
  if (ctx.ingat(KUNCI_DIRENDER + key)) return el;
  ctx.ingat(KUNCI_DIRENDER + key, 1);
  ungkap(el, opsi);
  return el;
}

function ungkapSenarai(el, ctx, key) {
  return ungkapSekali(el, ctx, key,
                      { per: 24, maks: 260, geser: 8, pegas: "jawab" });
}

/** Tab Bacaan: ringkasan Pustaka untuk satu kurikulum. Pilihan tautannya
 *  dan urutannya diputuskan inti/pustaka.py, sama dengan yang dicetak menu
 *  bahasa di terminal; layar ini cuma menambah jalan ke Pustaka lengkap. */
function daftarBacaan(b) {
  const p = b.pustaka;
  const semua = "#/pustaka?kurikulum=" + encodeURIComponent(b.key);
  if (!p.total) {
    return kosong("Belum ada bacaan untuk " + b.label,
      "Pustaka tetap bisa dijelajah untuk bahasa dan topik lain.",
      h("a.tbl.tbl-hantu", { href: "#/pustaka" }, "Buka Pustaka"));
  }
  const labelJenis = Object.fromEntries(p.per_jenis.map((j) => [j.jenis, j.label]));
  return h("div", {},
    h("p.baris-sisi", { gaya: { margin: "0 0 var(--s3)" } },
      `${angka(p.total)} tautan gratis untuk ${b.label}: buku, kursus, `
      + "proyek, dan lainnya. Yang berbahasa Indonesia tampil lebih dulu."),
    h("div.deret.deret-rapat", { gaya: { marginBottom: "var(--s4)" } },
      p.per_jenis.map((j) => h("a.tbl.tbl-kecil.tbl-hantu", {
        href: semua + "&jenis=" + j.jenis,
      }, j.label, h("span.tab-jumlah", {}, angka(j.jumlah))))),
    h("div.senarai", {}, p.pembuka.map((e) => barisTautan(e, labelJenis))),
    h("div.deret", { gaya: { marginTop: "var(--s4)" } },
      h("a.tbl.tbl-pergi", { href: semua },
        ikon("pustaka", { ukuran: 17 }), `Semua ${angka(p.total)} bacaan ${b.label}`,
        ikon("lanjut", { ukuran: 15 }))));
}

function daftarKuis(b, ctx) {
  return ungkapSenarai(h("div.senarai", {}, b.kuis.map((q) => {
    const persen = q.total_soal ? q.terbaik / q.total_soal * 100 : 0;
    const hari = selisihHari(q.jadwal);
    return h("a.baris", { href: `#/kuis/${b.key}/${q.indeks}` },
      h("span.nomor", {}, String(q.indeks + 1)),
      h("span.titik" + (q.pernah && q.terbaik === q.total_soal ? ".selesai"
        : q.pernah ? ".sedang" : ""), {}),
      h("div.isi", {},
        h("div.judul", {}, q.judul),
        h("div.ket", {}, q.pernah
          ? `Terbaik ${q.terbaik}/${q.total_soal} · ${q.percobaan}× dikerjakan`
            + (q.terakhir_waktu ? ` · terakhir ${jamRamah(q.terakhir_waktu)}` : "")
          : `${q.soal} soal · ` + (q.siap ? "semua materi yang diujinya sudah kamu baca" : `${q.sisa_materi} materi yang diujinya belum dibaca`))),
      q.jatuh_tempo ? h("span.pil.pil-ungu", {}, "saatnya diulang")
        : (q.pernah && hari !== null && hari > 0
            ? h("span.pil.sembunyi-hp", {}, `ulang ${hari} hari lagi`) : null),
      q.salah_tersisa
        ? h("span.pil.pil-salah", {}, `${q.salah_tersisa} masih salah`) : null,
      q.pernah ? h("span.sembunyi-hp", { gaya: { width: "56px", flex: "none" } },
        bilah(persen, persen >= 100 ? "tumbuh" : "")) : null);
  })), ctx, b.key);
}

function daftarLatihan(b, ctx) {
  return ungkapSenarai(h("div.senarai", {}, b.latihan.map((e) => h("a.baris", {
    href: `#/latihan/${b.key}/${e.indeks}`,
    kelas: [e.status === "lulus" || e.status === "manual" ? "selesai" : "",
            e.proyek ? "baris-proyek" : ""].filter(Boolean).join(" "),
  },
    h("span.nomor", {}, String(e.indeks + 1)),
    h("span.titik" + (e.status === "lulus" || e.status === "manual" ? ".selesai"
      : e.status === "dibuka" ? ".sedang" : ""), {}),
    h("div.isi", {},
      h("div.judul", {}, e.judul),
      e.status === "lulus" ? h("div.ket", {}, "lulus dengan kodemu sendiri")
        : e.status === "manual" ? h("div.ket", {}, "ditandai selesai manual")
        : !e.dinilai && e.alasan ? h("div.ket", {}, e.alasan) : null),
    e.proyek ? h("span.pil.pil-nyala", {}, "PROYEK AKHIR") : null,
    h("span.pil.t-" + e.tingkat, {}, e.tingkat),
    !e.dinilai ? h("span.pil.sembunyi-hp", {}, "tanpa nilai otomatis") : null))),
    ctx, b.key);
}

/* ================================================================ materi */

/* ---------------------------------------------------------- posisi baca */

/** Berapa lama posisi baca yang tersimpan masih berarti.
 *
 *  Dua belas jam: cukup untuk "aku tinggal sebentar lalu balik", terlalu
 *  pendek untuk menarik orang ke tengah materi yang sudah ia lupakan. Posisi
 *  yang basi lebih buruk daripada tidak ada posisi — ia mendaratkan orang di
 *  paragraf tanpa konteks dan terbaca sebagai halaman yang rusak. */
const BACA_KEDALUWARSA_MS = 12 * 60 * 60 * 1000;

/** Berapa lama diam sebelum kartu aksi menyingkir.
 *
 *  Di bawah lima detik dengan sengaja: SC 2.2.2 menuntut penahan untuk apa pun
 *  yang bergerak sendiri lebih dari lima detik, dan yang di sini berhenti
 *  sendiri jauh sebelum itu — sekali sembunyi, ia tidak melakukan apa-apa lagi
 *  sampai ada yang menggulir. */
const AKSI_DIAM_MS = 4000;

/** Materi yang sudah pernah digambar SEJAK DOKUMEN INI DIMUAT.
 *
 *  Sengaja `Set` di memori dan BUKAN localStorage: muat-ulang dan alamat yang
 *  diketik harus berarti "mulai dari atas". Yang dipulihkan cuma perjalanan
 *  bolak-balik di dalam satu sesi — membuka materi, melihat sesuatu di layar
 *  lain, lalu kembali. Ini tidak memperbaiki F5, dan tidak berpura-pura. */
const materiPernahDigambar = new Set();

function kunciBaca(key, indeks) {
  return `baca.${key}.${indeks}`;
}

/** Pulihkan posisi baca — HANYA dari dalam callback `saatSiap`.
 *
 *  Kenapa tidak boleh di badan pembangun layar, dan ini konstruktif bukan
 *  selera: `gambarRute()` menjalankan `appendChild` lalu
 *  `window.scrollTo({ top: 0 })` secara SENKRON, sementara `saatSiap()`
 *  mem-poll lewat `requestAnimationFrame`. Jadi callback ini tidak mungkin
 *  mendahului `scrollTo(0)` itu — sedangkan `scrollTo`/`scrollTop` yang
 *  dipanggil senkron dari badan pembangun berjalan SEBELUM layarnya terpasang,
 *  dan nol yang dihasilkannya diam saja (invarian #15a).
 *
 *  `behavior: "instant"`, BUKAN `"auto"` — dan bedanya bukan gaya penulisan.
 *  CSSOM-View mendefinisikan `"auto"` sebagai "ikuti `scroll-behavior` kotak
 *  yang digulir", dan `gaya.css:541` memasang `html { scroll-behavior: smooth }`.
 *  Jadi `"auto"` MULUS di tingkat gerak `penuh` dan `halus`; yang instan cuma
 *  `"mati"`, karena di sana `gaya.css:5137` menimpanya jadi `auto`. Terukur
 *  sebelum diperbaiki: pemulihan ke 700 px menghasilkan sembilan cuplikan yang
 *  berubah sepanjang ~650 ms. `"instant"` mengabaikan `scroll-behavior` dan
 *  terjadi sinkron, apa pun setelannya.
 *
 *  Tetap SENGAJA tidak ditanyakan ke `adaGerak()`, dan alasan itu tidak berubah:
 *  mengembalikan orang ke tempat ia berhenti bukan gerak yang menyampaikan
 *  sesuatu, dan menggulir mulus dua ribu piksel berarti isi yang sudah
 *  terpasang tetap tak terlihat selama hampir sedetik. */
function pulihkanBaca(ctx, key, indeks) {
  const tanda = key + "." + indeks;
  if (!materiPernahDigambar.has(tanda)) {
    materiPernahDigambar.add(tanda);
    return;
  }
  const simpan = ctx && ctx.ingat(kunciBaca(key, indeks));
  if (!simpan || typeof simpan.y !== "number" || simpan.y <= 0) return;
  if (Date.now() - (simpan.t || 0) > BACA_KEDALUWARSA_MS) return;

  // Dokumen bisa memendek sejak terakhir dibaca (bab terbuka, blok terlipat).
  // Dijepit ke ujung bawahnya, bukan dikembalikan ke atas: "berhenti di bawah"
  // jauh lebih dekat ke maksud orangnya daripada "mulai dari awal lagi".
  const maks = Math.max(
    0, document.documentElement.scrollHeight - window.innerHeight);
  window.scrollTo({ top: Math.min(simpan.y, maks), behavior: "instant" });
}

export async function layarMateri({ key, indeks }, ctx) {
  // Dua permintaan sekaligus, bukan berurutan: daftar materi bahasa ini
  // dipakai untuk kolom kiri, dan menunggunya setelah materinya sendiri
  // selesai berarti membayar dua kali perjalanan untuk satu layar.
  //
  // allSettled, bukan all: materi yang babnya belum terbuka dijawab 403, dan
  // 403 di sini BUKAN kegagalan — ia jawaban yang punya layarnya sendiri.
  // Dengan Promise.all, penolakan yang pertama membuat permintaan bahasa yang
  // sudah telanjur jalan jadi penolakan tanpa penangkap, dan justru data
  // itulah yang dibutuhkan untuk menjelaskan apa yang sedang terkunci.
  const [jawabMateri, jawabBahasa] = await Promise.allSettled([
    api.ambil("/api/materi", { key, indeks }),
    api.ambil("/api/bahasa", { key }),
  ]);
  const b = jawabBahasa.status === "fulfilled" ? jawabBahasa.value : null;

  if (jawabMateri.status === "rejected") {
    const galat = jawabMateri.reason;
    // 403 juga dipakai untuk token yang sudah tidak sah (servernya dinyalakan
    // ulang sementara tab ini terbuka), dan pembedanya sederhana: penguncian
    // bab cuma berlaku untuk satu materi, jadi permintaan bahasanya pasti
    // tetap berhasil. Kalau KEDUANYA ditolak, yang tertutup bukan babnya
    // melainkan sesinya — dan itu punya penanganannya sendiri di inti.js.
    if (b && galat instanceof GalatApi && galat.kode === 403) {
      return layarMateriTerkunci(key, indeks, galat.message, b, ctx);
    }
    throw galat;
  }
  if (!b) throw jawabBahasa.reason;

  const m = jawabMateri.value;
  const berbab = (b.bab || []).length > 1;
  let status = m.status;

  // Dibuka tapi belum tuntas dicatat sebagai "sebagian" — tanpa XP. Aturannya
  // milik progress.py: materi dihitung selesai HANYA kalau dibaca sampai
  // habis, dan antarmuka ini tidak berhak melonggarkannya.
  if (status === "baru") {
    api.kirim("/api/materi/selesai", { key, indeks, tuntas: false }).catch(() => {});
    status = "sebagian";
  }

  const capSelesai = h("span.pil" + (status === "selesai" ? ".pil-tumbuh" : ""), {},
    status === "selesai" ? "sudah dibaca tuntas" : "belum tuntas");
  // Bukan .tbl-utama: di kaki halaman ia berdiri tepat di sebelah tombol
  // "materi berikutnya", dan dua tombol beraksen bersebelahan membuat keduanya
  // sama-sama tidak terbaca sebagai pilihan utama. Lagi pula tombol ini
  // hampir selalu sudah tidak perlu ditekan — membaca sampai bawah sudah
  // menandainya sendiri.
  const tblSelesai = h("button.tbl", { onclick: () => tandaiSelesai(false) },
    status === "selesai" ? "Sudah selesai ✓" : "Tandai selesai");

  async function tandaiSelesai(pindah) {
    if (status !== "selesai") {
      status = "selesai";
      capSelesai.textContent = "sudah dibaca tuntas";
      capSelesai.classList.add("pil-tumbuh");
      tblSelesai.textContent = "Sudah selesai ✓";
      const hasil = await api.kirim("/api/materi/selesai",
                                    { key, indeks, tuntas: true }); rayakan(hasil); tawarkanKuisSiap(kaki, key, hasil);
    }
    if (pindah && m.sesudah) location.hash = `#/materi/${key}/${m.indeks + 1}`;
    else await tawarkanPintuBaru();
  }

  /** Tawarkan materi berikutnya kalau bab yang memuatnya BARU SAJA terbuka.
   *
   *  Saat halaman ini digambar, tetangga di bab yang masih terkunci sengaja
   *  dikosongkan server — jadi materi terakhir sebuah bab datang tanpa tombol
   *  "berikutnya". Yang menuntaskan bab itu justru pembacaan halaman ini
   *  sendiri, dan tanpa langkah di bawah orang yang baru saja menyelesaikan
   *  sebuah bab berdiri di halaman yang satu-satunya jalannya ke BELAKANG,
   *  tepat pada momen yang seharusnya jadi hadiahnya.
   *
   *  Yang TIDAK dilakukan di sini: menyimpulkan sendiri bahwa babnya sudah
   *  terbuka. "Ini materi terakhir bab, berarti bab berikutnya terbuka" adalah
   *  definisi KEDUA tentang penguncian, dan begitu ada dua, terminal dan web
   *  akan berbeda pendapat tentang pintu yang sama (lihat AGENTS.md).
   *  Jawabannya ditanyakan ulang ke server dan cuma dibacakan. */
  // Penanda "sedang bertanya". Tanpa ini, pengamat yang menyalakan penandaan
  // tuntas dan tombol "Tandai selesai" yang ditekan sepersekian detik sesudahnya
  // sama-sama sampai ke sini sebelum jawaban pertama tiba -- dan kakinya dapat
  // DUA tombol yang menawarkan materi yang sama.
  let bertanya = false;

  async function tawarkanPintuBaru() {
    if (bertanya || m.sesudah || m.indeks + 1 >= m.jumlah
        || kaki.querySelector(".tbl-pintu")) {
      return;
    }
    bertanya = true;
    let baru;
    // Gagal bertanya = tidak menawarkan apa-apa. Tombol yang muncul karena
    // tebakan lebih buruk daripada tombol yang tidak muncul: yang pertama
    // mengantar ke layar "belum terbuka" sesudah menjanjikan kebalikannya.
    try {
      baru = await api.ambil("/api/bahasa", { key });
    } catch (e) {
      bertanya = false;
      return;
    }

    const lanjut = (baru.materi || []).find((x) => x.indeks === m.indeks + 1);
    if (!lanjut || lanjut.terkunci) {
      bertanya = false;      // masih terkunci: boleh ditanyakan lagi nanti
      return;
    }

    segarkanKunci(baru);
    const bb = (baru.bab || []).find((x) => (x.materi || []).includes(lanjut.indeks));
    const tbl = h("a.tbl.tbl-utama.tbl-pintu",
      { href: `#/materi/${key}/${lanjut.indeks}` },
      bb ? `Bab ${bb.nomor} terbuka: ${potong(tanpaNomor(lanjut.judul), 22)}`
         : potong(tanpaNomor(lanjut.judul), 26),
      ikon("lanjut", { ukuran: 17 }));
    kaki.appendChild(tbl);
    // masuk(), bukan animasi ber-fill: keadaan akhirnya keadaan alami tombol
    // itu, jadi gerak yang dimatikan berarti tombolnya langsung ada — bukan
    // hilang selamanya.
    masuk(tbl, { geser: 7, pegas: "jawab" });
  }

  /** Buka kunci butir-butir kolom kiri yang sudah tidak terkunci lagi.
   *
   *  Kolom itu digambar sekali, dari keadaan saat halaman dibuka. Membiarkannya
   *  berarti tombol di kaki halaman mengumumkan "Bab 3 terbuka" sementara
   *  seluruh Bab 3 di sebelahnya masih tertulis "terkunci" — dua jawaban
   *  berbeda untuk pertanyaan yang sama, di satu layar.
   *
   *  Digambar ulang di tempat, BUKAN dibangun ulang: `kolomMateri()` membawa
   *  butir yang sedang dibaca ke tengah jalurnya, dan menjalankannya lagi
   *  berarti merenggut posisi baca orang yang baru saja sampai di dasar
   *  halaman. */
  function segarkanKunci(baru) {
    for (const x of baru.materi || []) {
      const a = kolom.querySelector(`a[data-indeks="${x.indeks}"]`);
      if (!a || x.terkunci || !a.classList.contains("terkunci")) continue;
      a.classList.remove("terkunci");
      a.removeAttribute("title");
      a.href = `#/materi/${key}/${x.indeks}`;
    }
    for (const x of baru.bab || []) {
      const ang = kolom.querySelector(`[data-bab="${x.nomor}"] .materi-rel-bab-angka`);
      if (!ang || x.status === "terkunci") continue;
      ang.classList.remove("kunci");
      ang.textContent = `${x.selesai}/${x.jumlah}`;
    }
  }

  // Sampai di ujung halaman = benar-benar dibaca habis. Ini padanan web dari
  // paginasi terminal, yang juga hanya menandai tuntas kalau halaman
  // terakhirnya dilewati.
  const penanda = h("div", { gaya: { height: "1px" } });
  const pengamat = new IntersectionObserver((catatan) => {
    if (catatan.some((c) => c.isIntersecting) && status !== "selesai") {
      tandaiSelesai(false);
    }
  }, { rootMargin: "0px 0px -40px 0px" });

  const jumlahKode = m.bagian.filter((x) => x.jenis === "kode").length;

  // Editor sisipan di dalam artikel harus dilepas saat layar berganti; kalau
  // tidak, pendengar papan ketik dan pengamat ukurannya hidup terus di
  // belakang layar berikutnya.
  const bersihEditor = [];
  const artikel = artikelMateri(m, key, b, bersihEditor);
  const peta = petaBagian(m, artikel);
  /* Lapisan papan ketik dipasang SEKARANG, bukan di dalam `saatSiap`.
     Alasannya asimetris dengan tetangganya di bawah dan itu yang mengikat:
     `saatGulir()` memanggil fungsinya sekali saat didaftarkan, jadi mendaftar
     terlalu awal membuatnya membaca gulir layar LAMA. `addEventListener` tidak
     punya panggilan pertama itu — dan penjaga `artikel.isConnected` di dalam
     penangannya sudah membuat penekanan sebelum terpasang jadi tidak berarti
     apa-apa. Yang tersisa cuma keuntungannya: pelepasnya sudah pasti ada
     sebelum `saatKeluar` mungkin dipanggil. */
  const fokus = pasangFokus();
  const lepasTombol = pintasanPembaca(artikel, peta, fokus);
  // Dipegang di variabel, bukan ditulis langsung di dalam pohonnya: keduanya
  // masih berubah SESUDAH halaman jadi, saat materi ini ditandai tuntas dan
  // bab berikutnya ikut terbuka (lihat tawarkanPintuBaru()).
  const kolom = kolomMateri(m, b, key);
  const kaki = h("nav.materi-kaki", {},
    // `sebelum`/`sesudah` sengaja dikosongkan server kalau tetangganya
    // ada di bab yang masih terkunci. Memakai `m.indeks > 0` saja pernah
    // cukup; sekarang tidak lagi — tombol tanpa nama yang mengantar ke
    // 403 adalah cara paling membingungkan untuk memberi tahu bahwa
    // sesuatu belum boleh dibuka.
    m.indeks > 0 && m.sebelum
      ? h("a.tbl.tbl-hantu", { href: `#/materi/${key}/${m.indeks - 1}` },
          ikon("kembali", { ukuran: 17 }), potong(m.sebelum, 26))
      : h("a.tbl.tbl-hantu", { href: "#/bahasa/" + key },
          ikon("kembali", { ukuran: 17 }), "Daftar materi"),
    h("span.deret-kanan"),
    m.sesudah
      ? h("button.tbl.tbl-utama", { onclick: () => tandaiSelesai(true) },
          potong(m.sesudah, 26), ikon("lanjut", { ukuran: 17 }))
      : null);

  /* Kartu aksi di tepi: RELOKASI, bukan duplikasi.
   *
   * Ketiga kontrolnya pindah, tidak disalin — `tblSelesai` keluar dari
   * `nav.materi-kaki`, dan `tombolBookmark`/`tombolCatatan` keluar dari
   * `div.materi-alat` yang karena itu bubar. Kaki tetap memegang tautan
   * sebelum/sesudah dan tombol beraksen "selesai lalu lanjut", yang SENGAJA
   * tidak ikut naik: ia satu-satunya permukaan beraksen di layar ini, dan
   * menaikkannya membuat tindakan utama yang kedua. */
  const kartuAksi = h("aside.aksi-tepi.masuk-mandiri",
    { "aria-label": "Tindakan untuk materi ini" },
    tblSelesai,
    tombolBookmark(key, "materi", indeks, m.bookmark),
    tombolCatatan(m.kunci, m.catatan, m.judul),
    fokus.tbl);

  const el = h("div.masuk.materi-tata", {},
    kolom,

    h("div.materi-utama", {},
      /* Kartu tinggal DI SINI, bukan di antara anak `.materi-tata`.
         `.materi-tata` adalah kisi dua kolom (>=1130) dan tiga kolom (>=1380)
         dengan tepat tiga item tata letak: rail, kolom utama, peta bagian.
         Selama kartunya `fixed` ia tidak memakan track — tapi begitu sebuah
         aturan membuatnya `static`, ia jadi item keempat yang ditempatkan
         otomatis dan MENGGESER saudara-saudaranya. Di dalam `.materi-utama`
         (yang `display: block`) `static` cuma berarti satu baris di atas kepala
         materi, dan `fixed` tidak berubah sama sekali. */
      kartuAksi,
      // Kepala dipangkas. Yang dulu berdiri di sini: satu baris mata, judul,
      // lalu EMPAT pil dan dua tombol berteks penuh — dua ratus piksel
      // metadata sebelum kata pertama pelajaran. Tiga dari empat pil itu
      // ("6 bagian", "2 contoh kode", "belum tuntas") menjawab pertanyaan
      // yang belum ditanyakan siapa pun saat halaman baru dibuka; mereka
      // turun ke KAKI artikel, tempat pertanyaannya memang muncul. Yang
      // bertahan di atas cuma posisi — dan itu pun sekarang ikut dibawa strip
      // konteks yang menempel, jadi ia tidak pernah hilang saat digulir.
      h("header.kepala-besar.kepala-materi", {},
        // Sampul per BAB, bukan per materi: materi dalam bab yang sama berbagi
        // gambar, jadi berpindah bab terasa seperti berpindah ruang.
        h("div.kepala-sampul.kepala-sampul-kecil", {},
          sampul(berbab && m.bab ? `${key}/bab-${m.bab.nomor}` : `${key}/materi`,
                 { bahasa: key, lebar: 320, tinggi: 220 })),
        h("span.mata", {},
          berbab && m.bab
            ? `Bab ${m.bab.nomor} · ${m.bab.judul}`
            : `${m.label_bahasa} · materi ${m.indeks + 1} dari ${m.jumlah}`),
        h("h1", {}, tanpaNomor(m.judul)),
        h("div.kepala-aksi", {},
          h("div.deret.deret-rapat", {},
            h("span.pil", {}, `materi ${m.indeks + 1} dari ${m.jumlah}`),
            berbab && m.bab
              ? h("span.pil.bab-tingkat.bab-" + m.bab.tingkat,
                  { title: `Tingkat ${m.bab.label_tingkat.toLowerCase()} · `
                    + `${m.bab.selesai} dari ${m.bab.jumlah} materi bab ini `
                    + "sudah dibaca tuntas" },
                  m.bab.label_tingkat)
              : null))),

      artikel,

      h("div.materi-meta", {},
        capSelesai,
        h("span.pil", {}, ikon("bagian", { ukuran: 14, tebal: 1.9 }),
          `${m.bagian.length} bagian`),
        jumlahKode
          ? h("span.pil", {}, ikon("latihan", { ukuran: 14, tebal: 1.9 }),
              `${jumlahKode} contoh kode`)
          : null),

      kaki,
      penanda),

    peta.el,
  );

  setTimeout(() => pengamat.observe(penanda), 80);

  /* Posisi baca: dipulihkan sekali, lalu gulirnya jadi milik pengguna.
   *
   * Pendengarnya sengaja didaftarkan DI DALAM callback, sesudah pemulihan.
   * `saatGulir()` memanggil fungsinya sekali saat didaftarkan; kalau ia
   * didaftarkan di badan pembangun, panggilan pertama itu terjadi sebelum
   * layarnya terpasang dan yang tersimpan adalah posisi gulir layar LAMA.
   *
   * Tanpa `ResizeObserver` dengan sadar: ini bukan pin. Sekali pulih, tidak
   * ada lagi yang merebut gulirnya kembali (invarian #15b). */
  let keluarMateri = false;
  let lepasBaca = () => {};
  let lepasAksi = () => {};
  saatSiap(el, () => {
    if (keluarMateri) return;
    pulihkanBaca(ctx, key, indeks);
    /* Penanda bagian dapat PEMANGGIL KEDUA dari jalur gulir.
     *
     * Aturannya tidak disalin ke sini — yang didaftarkan `tandaiAktif()` milik
     * `petaBagian`, fungsi yang sama yang dipanggil observernya. Pelepasnya
     * pun tidak dipegang di sini: ia digabung ke `peta.bersihkan()`, yang sudah
     * dipanggil `saatKeluar`, supaya layar ini tetap punya satu pintu keluar.
     *
     * Di dalam `saatSiap`, bukan di badan pembangun: `saatGulir()` memanggil
     * fungsinya sekali saat pendaftaran, dan panggilan pertama di badan
     * pembangun akan mengukur artikel yang belum terpasang (invarian #15a). */
    peta.ikutiGulir(() => !keluarMateri);
    /* Kartu aksi menyingkir sesudah diam, dan HANYA di luar `mati`.
     *
     * Menyembunyikan diri adalah perubahan keadaan yang terjadi sendiri, jadi
     * ia milik `halus`/`penuh`. Tingkatnya ditanya ke `tingkatGerak()` — satu-
     * satunya yang boleh memutuskannya — bukan dengan membaca `data-gerak`
     * sendiri dari DOM.
     *
     * Penjaga `keluarMateri` bukan kerapian di sini, dan bedanya dengan
     * pemulihan posisi baca itu yang mengikat: tulisan yang terlambat di sana
     * cuma menyimpan angka milik layarnya sendiri, sedangkan callback yang
     * terlambat DI SINI menyentuh DOM — dan `tunda()` tidak punya gagang
     * batal, jadi sebuah penundaan yang berangkat tepat sebelum layar berganti
     * akan mendarat sesudahnya. */
    if (tingkatGerak() !== "mati") {
      const sembunyikan = tunda(() => {
        if (keluarMateri) return;
        // Jangan pernah menyingkir saat kartunya sedang dipakai: Tab masuk ke
        // sini, dan kartu yang hilang saat digulir mencabut fokus dari orang
        // yang sedang memindahkannya.
        if (kartuAksi.matches(":hover, :focus-within")) return;
        /* Cuma sembunyikan kartu yang memang MELAYANG.
           Di tier tiga kolom kartunya ikut aliran, dan menyembunyikan kotak
           yang ada di aliran memendekkan dokumen — scroll anchoring lalu
           menggeser gulir, dan penampil yang mendengar gulir memunculkannya
           lagi. Lingkaran itu sudah dibunuh sekali lewat `fixed`; keputusan
           tier tiga kolom melahirkannya kembali kalau gerbang ini tidak ada.

           Yang ditanya HASILNYA, bukan ambang lebarnya. Menyalin `1380` ke JS
           berarti satu angka hidup di dua bahasa — preseden repo ini
           (`AMBANG_PANEL`, `AMBANG_RUANG`) menunjukkan bahwa itu menuntut
           pagarnya sendiri. Dan karena ia dibaca SAAT callback berjalan, ia
           tetap benar sesudah jendelanya diubah ukuran melintasi tier. */
        if (getComputedStyle(kartuAksi).position === "static") return;
        kartuAksi.hidden = true;
      }, AKSI_DIAM_MS);
      let atasTerakhir = null;
      lepasAksi = saatGulir(({ atas }) => {
        if (keluarMateri) return;
        /* Menyembunyikan kartu MEMENDEKKAN dokumen, dan pemendekan itu sendiri
           memicu `scroll`. Tanpa penjaga ini penyembunyian membangunkan
           penampilnya sendiri: terukur, penundaan berangkat di 327 ms, menyala
           di ~4327 ms, lalu dua peristiwa gulir datang di 4693 dan 4710 ms
           tanpa satu pun jari menyentuh apa pun — dan kartunya kembali.

           `atas` datang dari `saatGulir`, jadi tidak ada angka kedua yang
           dibaca sendiri di sini. */
        if (atas === atasTerakhir) return;
        atasTerakhir = atas;
        kartuAksi.hidden = false;
        sembunyikan();
      });
    }

    let yTerakhir = -1;
    lepasBaca = saatGulir(tunda(({ atas }) => {
      // `atas` datang dari `saatGulir` yang sudah menghitungnya sekali per
      // frame; membaca `window.scrollY` lagi di sini berarti dua definisi
      // untuk satu angka yang sama.
      if (atas === yTerakhir) return;
      yTerakhir = atas;
      ctx.ingat(kunciBaca(key, indeks), { y: atas, t: Date.now() });
    }, 400));
  });

  const bab = berbab && m.bab ? m.bab : null;
  return {
    el,
    judul: m.judul,
    konteks: {
      balik: { label: b.label, href: "#/bahasa/" + key },
      bab: bab ? `Bab ${bab.nomor}` : b.label,
      judul: bab ? bab.judul : "",
      posisi: `${m.indeks + 1} / ${m.jumlah}`,
      persen: bab ? bab.persen : b.statistik.persen,
      langkah: true,
      sebelum: m.sebelum ? `#/materi/${key}/${m.indeks - 1}` : null,
      sesudah: m.sesudah ? `#/materi/${key}/${m.indeks + 1}` : null,
      judul_sebelum: m.sebelum || "",
      judul_sesudah: m.sesudah || "",
    },
    saatKeluar: () => {
      keluarMateri = true;
      lepasBaca();
      lepasAksi();
      lepasTombol();
      fokus.lepas();
      pengamat.disconnect();
      peta.bersihkan();
      for (const lepas of bersihEditor) lepas();
    },
  };
}

/** Layar untuk alamat materi yang babnya belum terbuka (403 dari server).
 *
 *  Pesan error mentah di tengah layar gagal akan benar sekaligus tidak
 *  berguna: yang dibutuhkan orang yang baru saja menekan sebuah tautan bukan
 *  "Kesalahan 403" melainkan tiga hal — apa yang tadi diminta, kenapa belum
 *  boleh, dan ke mana sekarang. Ketiganya ada di layar ini, dan yang ketiga
 *  dibuat paling besar karena itulah satu-satunya yang bisa ditindaklanjuti.
 *
 *  Kalimat `pesan` datang utuh dari `bab.py` lewat server. Ia sudah menyebut
 *  berapa materi lagi yang kurang dan di bab mana; menulis ulang di sini
 *  berarti aturan yang sama dijelaskan dengan dua cara berbeda. */
function layarMateriTerkunci(key, indeks, pesan, b, ctx) {
  const nomor = Number(indeks);
  const label = b ? b.label : key;
  const m = b ? (b.materi || []).find((x) => x.indeks === nomor) : null;
  const bab = b ? (b.bab || []).find(
    (x) => (x.materi || []).includes(nomor)) : null;

  const el = h("div.masuk", {},
    kepalaBersampul(bab ? `${key}/bab-${bab.nomor}` : `${key}/materi`, { bahasa: key },
      h("span.mata", {}, "Belum terbuka"),
      h("h1", {}, m ? tanpaNomor(m.judul) : "Materi ini belum terbuka"),
      // Kalimat aturannya datang dari server, bukan ditulis ulang di sini:
      // ia tinggal di bab.py bersama logika yang menegakkannya, jadi terminal
      // dan browser mustahil menjelaskan aturan yang sama dengan dua rumusan
      // berbeda.
      h("p.kepala-sub", {}, (ctx && ctx.awal && ctx.awal.aturan_bab
        ? ctx.awal.aturan_bab.aturan
        : "Bab ini belum terbuka."))),

    keadaan({
      jenis: "kunci",
      gambar: "belum",
      judul: bab ? `Bab ${bab.nomor} · ${bab.judul}` : "Kenapa belum bisa dibuka",
      ket: pesan,
      aksi: [
        h("a.tbl.tbl-utama", { href: "#/bahasa/" + key },
          ikon("kembali", { ukuran: 17 }), "Kembali ke " + label),
        h("a.tbl.tbl-hantu", { href: "#/atur" },
          "Buka semua bab di Pengaturan"),
      ],
    }));

  return {
    el,
    judul: "Belum terbuka",
    konteks: { balik: { label, href: "#/bahasa/" + key },
               bab: "Belum terbuka" },
  };
}

/** Kolom kiri: seluruh materi bahasa ini, dengan yang sedang dibuka disorot.
 *
 *  Ini pinjaman paling langsung dari The Odin Project, dan alasannya sama:
 *  saat sedang membaca, pertanyaan "ini bagian ke berapa dari berapa, dan apa
 *  sesudahnya" muncul terus-menerus. Menjawabnya lewat tombol Kembali berarti
 *  membuang tempat membaca untuk memeriksa peta.
 *
 *  Babnya ikut masuk sebagai sub-judul di antara butir-butirnya. Bentuknya
 *  satu daftar, bukan beberapa daftar bertumpuk, dan itu bukan soal rapi: di
 *  layar sempit kolom ini berubah jadi satu jalur yang digulir mendatar, dan
 *  memecahnya jadi empat jalur terpisah berarti empat penggulir kecil
 *  bertumpuk di atas bacaan — persis di tempat yang paling sedikit ruangnya. */
function kolomMateri(m, b, key) {
  // Peta nomor -> bab. Tiap materi cuma membawa nomor babnya, sedangkan yang
  // perlu digambar di sub-judul adalah judul, kemajuan, dan alasan kuncinya.
  const daftarBab = b.bab || [];
  const bab = new Map(daftarBab.map((x) => [x.nomor, x]));
  // Satu bab saja = tidak ada yang dikelompokkan; lihat daftarMateri().
  const berbab = daftarBab.length > 1;
  let babKini = null;

  const butir = [];
  for (const x of b.materi) {
    if (berbab && x.bab !== babKini) {
      babKini = x.bab;
      const bb = bab.get(babKini);
      if (bb) {
        const kunci = bb.status === "terkunci";
        // `data-bab` dan `data-indeks` di bawah bukan hiasan: keduanya jalan
        // yang dipakai layarMateri() untuk membuka kunci butir-butir di sini
        // begitu babnya terbuka, tanpa membangun ulang seluruh kolomnya.
        butir.push(h("li.materi-rel-bab", { data: { bab: String(bb.nomor) } },
          h("span.materi-rel-bab-judul", {}, `Bab ${bb.nomor} · ${bb.judul}`),
          // Angkanya ditandai berbeda saat babnya terkunci karena keduanya
          // tidak sama pentingnya: di layar sempit "3/7" boleh mengalah demi
          // judul yang utuh, sedangkan "terkunci" adalah satu-satunya
          // keterangan yang menjelaskan kenapa butir di bawahnya tidak bisa
          // ditekan. Yang menyembunyikannya ada di gaya.css.
          h("span.materi-rel-bab-angka" + (kunci ? ".kunci" : ""), {},
            kunci ? "terkunci" : `${bb.selesai}/${bb.jumlah}`)));
      }
    }

    const kini = x.indeks === m.indeks;
    // Yang terkunci tetap ditulis dengan bentuk yang sama persis — jalurnya
    // harus terbaca utuh — tapi TANPA href. <a> tanpa href bukan tautan bagi
    // siapa pun: tidak bisa diklik, tidak disinggahi Tab, dan tidak
    // diumumkan pembaca layar sebagai tautan.
    const a = h("a" + (kini ? ".kini" : "") + (x.terkunci ? ".terkunci" : ""), {
      data: { indeks: String(x.indeks) },
      href: x.terkunci ? null : `#/materi/${key}/${x.indeks}`,
      title: x.terkunci && bab.get(x.bab) ? bab.get(x.bab).alasan : null,
      "aria-current": kini ? "page" : null,
    },
      h("span.materi-rel-nomor", {}, String(x.indeks + 1)),
      h("span.materi-rel-judul", {}, tanpaNomor(x.judul)),
      x.status === "selesai"
        ? ikon("selesai", { ukuran: 16, kelas: "materi-rel-tanda" })
        : x.status === "sebagian"
          ? ikon("sedang", { ukuran: 16, kelas: "materi-rel-tanda" })
          : null);
    butir.push(h("li", {}, a));
  }

  const daftar = h("ol.materi-rel-daftar", {}, butir);

  // Tidak ada tautan "kembali ke bahasa" di kepala jalur ini, dan itu bukan
  // kelalaian: strip konteks yang menempel di atas halaman sudah membawanya,
  // selalu terlihat, di tempat yang sama di semua layar belajar. Dua jalan
  // pulang yang berjarak empat puluh piksel bukan dua pilihan — ia satu
  // pilihan yang digambar dua kali.
  const el = h("aside.materi-rel", {},
    h("div.mata", {}, `Materi · ${b.statistik.materi}/${b.statistik.total_materi}`),
    daftar);

  // Jalurnya menggulir sendiri. Tanpa baris ini, membuka materi ke-20 dari 26
  // menampilkan jalur yang tergulir di paling atas — butir yang sedang dibaca
  // ada di luar pandangan, dan yang terlihat justru daftar yang sudah lama
  // dilewati. Yang digulir CUMA wadahnya; lihat bawaKeTengah().
  saatSiap(daftar, () => {
    const kini = daftar.querySelector("a.kini");
    if (!kini) return;
    bawaKeTengah(el, kini);
    bawaKeTengah(daftar, kini);
  });
  return el;
}

/** Label peta halaman untuk sebuah bagian prosa.
 *
 *  Sebagian besar bagian di kurikulum ini tidak punya judul sendiri —
 *  penulisnya memang menulis mengalir, bukan berjudul-judul. Kalimat
 *  pertamanya dipakai sebagai gantinya, TAPI dipotong di batas KATA dan jauh
 *  lebih pendek daripada sebelumnya. Alasannya: peta yang berisi kalimat
 *  setengah jadi ("Di aplikasi ini HTML tidak digambar seperti d…") lebih
 *  lambat dipindai daripada peta berisi frasa pendek. Peta dibaca dengan
 *  MELIRIK, bukan dengan membaca — dan potongan di tengah kata memaksa mata
 *  berhenti untuk menebak kata apa yang terpotong. */
function labelPeta(bg) {
  const blok = (bg.blok || []).find(
    (x) => x.jenis !== "pra" && (x.teks || (x.butir && x.butir.length)));
  if (!blok) return "";
  const teks = String(blok.teks
    || (blok.butir && blok.butir[0] && blok.butir[0].teks) || "")
    .replace(/\s+/g, " ").trim();
  if (!teks) return "";
  // Berhenti di tanda baca akhir kalimat pertama kalau ada dan cukup pendek;
  // kalau tidak, potong di batas kata — tidak pernah di tengah kata.
  const titik = teks.search(/[.!?:](\s|$)/);
  let awal = titik > 8 && titik < 52 ? teks.slice(0, titik) : teks;
  if (awal.length > 44) {
    const batas = awal.lastIndexOf(" ", 44);
    awal = awal.slice(0, batas > 20 ? batas : 44) + "…";
  }
  return awal;
}

/** Bawa sebuah bagian ke tepi atas kolom baca, TANPA `scrollIntoView`.
 *
 *  Aturan repo: `scrollIntoView` menggulir semua leluhur yang bisa digulir —
 *  itu sebabnya `bawaKeTengah()` ada. Di sini yang digulir memang dokumennya,
 *  jadi masalahnya bukan leluhur melainkan PENDARATANNYA: `block: "start"`
 *  menghormati `scroll-padding-top`, dan nilai itu terukur 26 px lebih kecil
 *  daripada dasar chrome yang menempel di pembaca (72 px lawan 98 px) karena
 *  `--lengket-atas` diisi ulang di subtree `#panggung`, tempat yang tidak bisa
 *  dilihat aturan di `html`.
 *
 *  Sesudah CSS-nya diperbaiki, jarak itu dibaca dari `scrollPaddingTop` yang
 *  SUDAH terhitung, bukan disalin sebagai angka. Jadi tidak ada angka kedua
 *  yang bisa melenceng: kalau CSS-nya berubah, pendaratannya ikut.
 *
 *  Pembacaan tata letak di sini terjadi di dalam `onclick` — elemennya sudah
 *  lama terpasang, jadi ia bukan kasus invarian #15(a). */
function bawaKeAtas(sasaran) {
  const pad = parseFloat(
    getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
  const atas = sasaran.getBoundingClientRect().top + window.scrollY - pad;
  window.scrollTo({ top: Math.max(0, atas),
                    behavior: adaGerak() ? "smooth" : "auto" });
}

/** Kolom kanan: peta bagian di halaman ini, dengan penanda yang mengikuti
 *  posisi baca.
 *
 *  Bedanya dengan daftar isi biasa: penandanya BERGERAK. Di materi sepanjang
 *  empat bagian itu mungkin berlebihan; di materi yang panjang, ia satu-satunya
 *  hal yang menjawab "aku sudah sampai mana" tanpa harus menggulir balik. */
function petaBagian(m, artikel) {
  const butir = [];
  m.bagian.forEach((bg, i) => {
    let judul = bg.judul;
    if (!judul && bg.jenis === "kode") {
      judul = (bg.petunjuk && bg.petunjuk.nama) || "Contoh kode";
    }
    if (!judul && bg.jenis === "prosa") judul = labelPeta(bg);
    if (!judul) return;
    butir.push({ i, judul, jenis: bg.jenis });
  });

  if (butir.length < 2) {
    // `lompat` dan `ikutiGulir` tetap ada di cabang ini. Peta kosong adalah
    // KEADAAN, bukan ketiadaan objek: pemanggilnya tidak boleh dipaksa
    // menanyakan cabang mana yang sedang aktif sebelum berani memanggil.
    return { el: h("aside.materi-peta.materi-peta-kosong"),
             bersihkan() {}, lompat() { return null; }, ikutiGulir() {} };
  }

  const tautan = butir.map((x) => h("a", {
    href: "#",
    onclick: (e) => {
      e.preventDefault();
      const sasaran = artikel.children[x.i];
      if (sasaran) bawaKeAtas(sasaran);
    },
  },
    ikon(x.jenis === "kode" ? "latihan" : "bagian", { ukuran: 14, tebal: 1.9 }),
    h("span", {}, x.judul)));

  const el = h("aside.materi-peta", {},
    h("div.mata", {}, "Di halaman ini"),
    h("nav.materi-peta-daftar", {}, tautan));

  // Bagian yang sedang dibaca = bagian TERAKHIR yang tepinya sudah melewati
  // sepertiga atas layar. Aturan "yang paling banyak terlihat" terdengar lebih
  // benar tapi terasa gelisah: penandanya melompat bolak-balik tiap kali dua
  // bagian pendek bergantian mengisi layar.
  /** Aturan penandanya, dan ia hidup DI SINI saja — nol salinan.
   *
   *  Dua pemanggil, satu aturan. `IntersectionObserver` di bawah menangkap
   *  perubahan yang terjadi TANPA gulir (tata letak yang bergeser, gambar yang
   *  selesai dimuat, jendela yang diubah ukurannya); langganan gulir di
   *  `layarMateri` menangkap perpindahan yang TIDAK melintasi ambang observer.
   *  Menyalin lima baris ini ke pemanggil kedua akan membuat dua aturan yang
   *  boleh berbeda, dan yang pertama kali berbeda tidak akan ada yang tahu. */
  function tandaiAktif() {
    let aktif = -1;
    butir.forEach((x, n) => {
      const anak = artikel.children[x.i];
      if (anak && anak.getBoundingClientRect().top <= window.innerHeight * 0.34) {
        aktif = n;
      }
    });
    tautan.forEach((a, n) => a.classList.toggle("kini", n === aktif));
  }

  /* Kenapa observernya TIDAK cukup sendirian, dan ini terukur bukan dikira:
     ia hanya dipanggil ulang kalau ada bagian yang MELINTASI ambangnya. Dari
     puncak halaman ke bagian pertama (gulir 0 -> 241 px di 1440), bagian 0
     sudah memotong pita `rootMargin` di KEDUA posisi — tidak ada ambang yang
     dilewati, callback tidak jalan, dan `.kini` tetap -1 padahal aturan di
     atas sudah memberi jawaban 0. Penekanan `]` berikutnya membaca -1 lagi dan
     mendarat di tempat yang sama; tautan rail yang diklik punya gejala yang
     persis sama, dan sudah punya jauh sebelum lapisan papan ketik ada.

     Observernya tetap: ia satu-satunya yang menangkap perubahan tanpa gulir. */
  let hentikan = () => {};
  if (typeof IntersectionObserver !== "undefined") {
    const pengamat = new IntersectionObserver(tandaiAktif,
      { rootMargin: "-30% 0px -55% 0px", threshold: [0, 1] });

    for (const x of butir) {
      const anak = artikel.children[x.i];
      if (anak) pengamat.observe(anak);
    }
    hentikan = () => pengamat.disconnect();
  }

  /** Pemanggil kedua: jalur gulir. Didaftarkan dari LUAR, dari dalam callback
   *  `saatSiap` di `layarMateri` — invarian #15(a): mendaftarkannya di badan
   *  pembangun berarti `saatGulir` memanggil fungsinya sekali saat pendaftaran,
   *  dan panggilan pertama itu akan mengukur elemen yang belum terpasang.
   *
   *  `masihHidup` adalah penjaga `keluarMateri` milik layarnya, dioper sebagai
   *  fungsi supaya nilainya dibaca SAAT frame berjalan, bukan saat berlangganan.
   *
   *  Pelepasnya digabung ke `bersihkan()`, jadi `saatKeluar` tetap satu pintu
   *  dan tidak ada pelepas kedua yang bisa terlupa. */
  let lepasGulir = () => {};
  function ikutiGulir(masihHidup) {
    lepasGulir();
    lepasGulir = saatGulir(() => { if (masihHidup()) tandaiAktif(); });
  }
  /** Pindah satu bagian, ke arah `arah` (+1 / -1), dan kembalikan sasarannya.
   *
   *  Tiga hal yang SUDAH ada dipakai apa adanya, dan itu yang penting:
   *  daftarnya `butir` (yang juga menggambar tautannya), pendaratannya
   *  `bawaKeAtas()` (yang membaca `scroll-padding-top` terhitung, bukan angka
   *  salinan), dan "bagian yang sedang dibaca" dibaca dari tautan ber-`.kini`
   *  -- yaitu jawaban `tandaiAktif()` di atas, bukan hitungan kedua.
   *
   *  Penandanya berpindah sesudah gulir mendarat karena `tandaiAktif()`
   *  dipanggil lagi dari jalur gulir, BUKAN karena fungsi ini menyetelnya.
   *  Kalimat versi pertama di sini berbunyi "penandanya milik observer itu,
   *  ia berpindah sendiri" — dan itu salah dalam satu keadaan yang terukur:
   *  dari puncak halaman observernya tidak pernah dipanggil ulang, `.kini`
   *  tetap -1, dan penekanan kedua mendarat di tempat yang sama. Fungsi ini
   *  tetap tidak menyetel satu kelas pun, dan itu yang mengikat: dua mesin
   *  yang boleh menulis satu penanda adalah dua mesin yang suatu hari menulis
   *  dua jawaban berbeda.
   *
   *  Dijepit di ujung, tidak dilingkar (preseden `panahAntarUbin`). */
  function lompat(arah) {
    const i = tautan.findIndex((a) => a.classList.contains("kini"));
    const tuju = Math.max(0, Math.min(butir.length - 1, i + arah));
    const sasaran = artikel.children[butir[tuju].i];
    if (!sasaran) return null;
    bawaKeAtas(sasaran);
    return sasaran;
  }

  return { el, bersihkan: () => { lepasGulir(); hentikan(); }, lompat, ikutiGulir };
}

/** Mode fokus pembaca: kolom daftar materi dan peta halaman disingkirkan,
 *  kolom baca berdiri sendiri di tengah, dan navbar meredup sampai disentuh.
 *
 *  Untuk sesi membaca yang panjang, yang melelahkan bukan teksnya melainkan
 *  semua yang bukan teks: dua kolom di kiri-kanan yang terus tertangkap sudut
 *  mata, dan bilah navigasi yang tidak pernah dipakai selama membaca. Strip
 *  konteks (kembali, posisi, maju-mundur) TIDAK ikut disembunyikan — tanpa
 *  itu mode fokus berubah jadi jalan buntu.
 *
 *  Pilihannya diingat per browser (preferensi tampilan, bukan capaian
 *  belajar), tapi kelasnya hidup HANYA selama pembaca terpasang: `lepas()`
 *  wajib dipanggil `saatKeluar`, atau navbar dasbor ikut redup. */
function pasangFokus() {
  const akar = document.documentElement;
  let nyala = ambilLokal("fokus_baca", false) === true;
  const tbl = h("button.ikon-tombol", { type: "button", onclick: () => alih() },
    ikon("panel", { ukuran: 19, tebal: 1.7 }));

  function setel() {
    akar.classList.toggle("fokus-baca", nyala);
    tbl.classList.toggle("aktif", nyala);
    tbl.setAttribute("aria-pressed", String(nyala));
    tbl.title = nyala ? "Keluar dari mode fokus (F)" : "Mode fokus (F)";
    tbl.setAttribute("aria-label", tbl.title);
  }
  function alih() {
    nyala = !nyala;
    simpanLokal("fokus_baca", nyala);
    setel();
    return true;
  }
  setel();
  return { tbl, alih, lepas: () => akar.classList.remove("fokus-baca") };
}

/* Tabel pintasan pembaca materi. SATU tabel, dibaca penangan di bawah — bukan
   deretan cabang `if` yang tersebar.
   Kolom pertamanya lambang yang DITAMPILKAN, dan itu disengaja: daftar bantuan
   `PINTASAN` di `layar-lain.js` adalah definisi KEDUA dari lapisan ini, dan dua
   definisi yang tidak pernah dibandingkan adalah dua definisi yang suatu hari
   berbeda tanpa ada yang menyadarinya. Yang membandingkannya sebuah tes bentuk,
   bukan kesepakatan lisan.

   `?` sengaja TIDAK di sini. Pemiliknya `aplikasi.js` (`tampilkanBantuan()`),
   dan tombol yang punya dua pemilik adalah tombol yang perilakunya bergantung
   pada urutan pendaftaran pendengar. */
const PINTASAN_PEMBACA = [
  ["j", "Blok kode berikutnya", (a) => a.blok(+1)],
  ["k", "Blok kode sebelumnya", (a) => a.blok(-1)],
  ["]", "Bagian berikutnya", (a) => a.bagian(+1)],
  ["[", "Bagian sebelumnya", (a) => a.bagian(-1)],
  ["f", "Mode fokus", (a) => a.fokus()],
  ["⏎", "Jalankan blok kode yang sedang difokus", (a) => a.jalankan()],
];

// `e.key` untuk Enter berbunyi "Enter"; tabel di atas memakai lambang yang
// dibaca orang di daftar bantuan. Terjemahannya tinggal di satu tempat ini.
const TOMBOL_TAMPIL = { Enter: "⏎" };

/** Lapisan papan ketik untuk halaman materi: `j`/`k` antar blok kode, `[`/`]`
 *  antar bagian, `⏎` menjalankan blok yang sedang difokus.
 *
 *  Kenapa blok kode yang dapat pintasan, dan bukan paragraf: blok kode satu-
 *  satunya hal di halaman ini yang bisa DIKERJAKAN. Menggulir prosa sudah
 *  punya alatnya sendiri di setiap peramban; melompat ke contoh berikutnya lalu
 *  menjalankannya tanpa melepas papan ketik tidak punya.
 *
 *  BENTURAN YANG DITERIMA APA ADANYA: `g` lalu `j`. `aplikasi.js` memakai
 *  rangkaian ala Vim `g` + huruf, dan `j` bukan salah satu tujuannya — jadi
 *  menekan `g` lalu `j` memindahkan fokus satu blok kode, sementara `tombolG`
 *  di sana masih menyala sampai 900 ms. Menyalin keadaan `tombolG` ke layar ini
 *  akan membuat dua salinan satu keadaan, dan itu ongkos yang lebih besar
 *  daripada benturannya. Ditulis di sini supaya ia tercatat sebagai keputusan,
 *  bukan ditemukan lagi sebagai kejutan.
 *
 *  Mengembalikan fungsi pelepas — WAJIB dipanggil `saatKeluar` (preseden
 *  `layar-kerja.js:520`). Pendengar `keydown` di `document` yang tertinggal
 *  membuat dua layar bereaksi terhadap satu tombol. */
function pintasanPembaca(artikel, peta, fokus) {
  // Urutan sasaran dihitung dari posisi VERTIKAL nyata, bukan dari urutan
  // dokumen. Keduanya sama hari ini; yang membuat mereka berbeda adalah
  // perubahan tata letak apa pun di kemudian hari, dan saat itu terjadi yang
  // benar adalah yang dilihat mata.
  const daftarBlok = () => [...artikel.querySelectorAll(".blok-kode")]
    .sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);

  function keBlok(arah) {
    const daftar = daftarBlok();
    if (!daftar.length) return false;
    let tuju;
    const i = daftar.indexOf(document.activeElement);
    if (i >= 0) {
      tuju = i + arah;
    } else {
      // Belum ada blok yang difokus: titik mulainya POSISI BACA, bukan blok
      // pertama halaman. Orang yang sudah menggulir ke tengah materi lalu
      // menekan `j` bermaksud "yang berikutnya dari sini", dan melempar
      // fokusnya ke atas halaman membuang tempat bacanya.
      const bawah = daftar.findIndex(
        (el) => el.getBoundingClientRect().top > window.innerHeight / 2);
      const pertama = bawah < 0 ? daftar.length : bawah;
      tuju = arah > 0 ? pertama : pertama - 1;
    }
    // DIJEPIT di ujung, tidak dilingkar — preseden `panahAntarUbin` (:292).
    // Melingkar berarti satu penekanan di blok terakhir memindahkan layar
    // sejauh seluruh halaman, dan tidak ada yang meminta perpindahan sebesar
    // itu dari tombol yang artinya "berikutnya".
    const j = Math.max(0, Math.min(daftar.length - 1, tuju));
    // Pendaratannya lewat `bawaKeAtas()` yang sama dengan peta bagian, lalu
    // fokus TANPA gulir bawaan: dua mesin yang menggulir satu elemen akan
    // saling menimpa, dan yang menang bergantung waktu.
    bawaKeAtas(daftar[j]);
    daftar[j].focus({ preventScroll: true });
    return true;
  }

  function keBagian(arah) {
    return Boolean(peta.lompat(arah));
  }

  function jalankanBlokFokus() {
    const blok = document.activeElement;
    if (!(blok instanceof Element) || !blok.classList.contains("blok-kode")) {
      return false;
    }
    // Jalur jalannya yang SUDAH ADA, ditanya lewat tombolnya. "Bisa
    // dijalankan" sudah punya satu definisi (`p.bisa_dijalankan && bhs.siap`
    // di `blokKode`), dan tombol ini adalah HASIL definisi itu — menanyakannya
    // lewat tombol berarti tidak ada definisi kedua yang bisa melenceng, dan
    // `/api/coba` tetap disentuh dari satu tempat saja.
    //
    // Blok tanpa tombol tidak mengubah apa pun. Itu KEADAAN, bukan galat:
    // ilustrasi dan potongan memang tidak bisa dijalankan, dan mengeluh soal
    // itu berarti menyalahkan orang atas bentuk materinya sendiri.
    const tbl = blok.querySelector(".blok-alat .tbl-utama");
    if (!tbl) return false;
    tbl.click();
    return true;
  }

  const aksi = { blok: keBlok, bagian: keBagian, jalankan: jalankanBlokFokus,
                 fokus: () => fokus.alih() };

  function saatTombol(e) {
    /* Tiga penjaga, berurutan, dan urutannya bukan selera.
     *
     * (1) `defaultPrevented`. Pemilik pintasan global `aplikasi.js`, dan
     *     pendengarnya terdaftar di `mulai()` — jadi ia SELALU berjalan lebih
     *     dulu daripada pendengar layar mana pun. Kasus nyatanya `Ctrl+J`:
     *     `e.key` -nya "j", dan tanpa penjaga ini satu penekanan mengganti tema
     *     SEKALIGUS melompat satu blok kode. `stopPropagation()` akan
     *     "menyelesaikan" itu dari sisi yang salah — ia membungkam pemiliknya,
     *     dan pemilik yang dibungkam tidak pernah tahu ia dibungkam.
     * (2) Medan isian. Di editor blok kode, mengetik `jjk` harus menulis tiga
     *     huruf. Ini satu-satunya penjaga yang kegagalannya langsung terasa.
     * (3) `artikel.isConnected`. Pendengarnya di `document`, jadi jangkauannya
     *     seluruh aplikasi; yang membatasinya pada layar ini cuma kalimat ini
     *     dan pelepasan di `saatKeluar`. Dua-duanya ada, dan yang kedua saja
     *     tidak cukup: pelepasan yang telat satu frame masih sempat
     *     menggerakkan layar berikutnya. */
    if (e.defaultPrevented) return;
    /* (1b) Dialog yang terbuka. Ini BUKAN pengulangan (1), dan bedanya yang
       membuatnya perlu: `defaultPrevented` menjawab "tombol ini sudah dipunyai
       siapa", sedangkan yang ditanya di sini "bolehkah halaman di belakang
       dialog bergerak". Dua pertanyaan berbeda, dan hanya satu yang dijawab
       oleh jawaban pertama.

       Terukur: `?` membuka dialog bantuan (fokus di tombol Tutup, gulir 900),
       lalu satu `j` memindahkan fokus ke sebuah blok kode dan gulir ke 2018,
       lalu `]` ke 2677 — sementara dialognya masih menggantung di atas halaman
       yang barusan dipindahkan di belakangnya. Tidak ada satu pun galat.

       Jalur bermodifier tidak pernah bocor lewat sini: `Ctrl+K` menaruh fokus
       di medan isian palet, jadi ia tertahan penjaga (2) — yang bocor cuma
       tombol satu huruf tanpa modifier, yaitu tepat lapisan ini.

       `jendelaTerbuka()` diimpor dari `inti.js`, PEMILIK dialognya. Memanggil
       milik pemilik bukan menyalin keadaan siapa pun; yang dilarang justru dua
       hal yang menghindarinya — `stopPropagation()` (membungkam pemilik
       pintasan) dan membaca DOM sendiri untuk menebak ada dialog (definisi
       kedua dari "sedang ada jendela"). */
    if (jendelaTerbuka()) return;
    if (e.target instanceof Element
        && e.target.matches("input, textarea, select, [contenteditable]")) return;
    if (!artikel.isConnected) return;

    const kunci = TOMBOL_TAMPIL[e.key] || e.key;
    const baris = PINTASAN_PEMBACA.find(([tombol]) => tombol === kunci);
    if (!baris) return;
    // `preventDefault()` HANYA kalau benar-benar ada yang dikerjakan. `⏎` yang
    // mendarat saat fokusnya bukan blok kode wajib tetap menekan tombol atau
    // membuka tautan yang sedang difokus.
    if (baris[2](aksi)) e.preventDefault();
  }

  document.addEventListener("keydown", saatTombol);
  return () => document.removeEventListener("keydown", saatTombol);
}

/** Bagian-bagian materi muncul saat tergulir ke tempatnya.
 *
 *  Ini satu-satunya tempat di aplikasi yang gerakannya benar-benar mengikuti
 *  kecepatan MEMBACA, bukan kecepatan mengeklik. Jaraknya kecil dan urutannya
 *  pendek: yang dicari kesan halaman yang terbuka mengikuti mata, bukan
 *  pertunjukan yang menuntut ditonton sebelum boleh membaca. */
function artikelMateri(m, key, bhs, bersih) {
  const artikel = h("article.prosa", {},
    m.bagian.map((b, i) => bagianMateri(b, i, m, key, bhs, bersih)));
  ungkap(artikel, { per: 30, maks: 180, geser: 9, pegas: "halus" });
  return artikel;
}

/** Satu blok prosa (teks, daftar, pra, catatan) -> elemen.
 *
 *  Diekspor karena soal latihan memakai pengurai yang sama: contoh keluaran
 *  berkolom di dalam soal butuh perlakuan yang persis sama dengan tabel di
 *  dalam materi, dan menuliskannya dua kali berarti suatu hari keduanya akan
 *  berbeda tanpa ada yang menyadarinya.
 */
export function blokProsa(blk) {
  if (blk.jenis === "pra") return h("div.pra", {}, blk.teks);
  if (blk.jenis === "daftar") return senarai(blk);
  // Blok berperan ("Jebakan: ...", "Aturan ...") diberi kotaknya sendiri.
  // Kelas dasarnya tetap yang lama, jadi blok tanpa peran tidak berubah.
  const dasar = blk.jenis === "catatan" ? "div.catatan-prosa" : "div.par";
  const kelas = blk.peran ? dasar + ".peran.peran-" + blk.peran : dasar;
  return h(kelas, {}, berkode(blk.teks));
}

function bagianMateri(b, i, m, key, bhs, bersih) {
  if (b.jenis === "prosa") {
    return h(b.judul === "Di dunia nyata" ? "section.dunia-nyata" : "section", {},
      b.judul ? h("h3", {}, b.judul) : null,
      b.blok.map(blokProsa), (b.visual || []).map(gambarVisual));
  }
  return b.visual ? h("div.blok-bergambar", {}, blokKode(b, i, m, key, bhs, bersih), b.visual.map(gambarVisual)) : blokKode(b, i, m, key, bhs, bersih);
}

/* Kartu keluaran satu kali jalan.
 *
 * Untuk bahasa yang MENCETAK sesuatu, keluarannya memang teks dan kartunya
 * cuma membingkainya. Untuk HTML tidak: `struktur.py` mengubahnya jadi pohon
 * elemen karena mesin penilaian di sini bekerja dengan membandingkan keluaran,
 * dan HTML tidak punya keluaran. Pohon itu WAJIB tetap ada — ia yang dinilai,
 * dan ia juga satu-satunya cara melihat apa yang sebenarnya terjadi pada
 * markup yang tag penutupnya lupa ditulis. Tapi ia jawaban untuk pertanyaan
 * lain daripada yang sedang ditanyakan orang yang baru saja mengetik
 * <h1>Halo, Dunia!</h1>.
 *
 * Jadi keduanya ditampilkan, dengan yang dicari lebih dulu: Tampilan di depan,
 * Struktur satu klik di sebelahnya.
 */
export function kartuKeluaran(r, runner, kode, saatTutup, simpanLepas) {
  const lulus = r.kode_keluar === 0;
  const pohon = h("div.terminal", {},
    r.keluaran || "(program ini tidak mencetak apa pun)");
  const isi = h("div.keluaran-isi");
  const tab = h("div.keluaran-tab");

  const dok = bisaDipratinjau(runner) && kode.trim()
    ? dokumenPratinjau(runner, kode) : "";
  const bisa = !!dok;
  if (bisa) {
    const dikarang = halamanDikarang(runner, kode);
    const pv = pratinjauHtml(dok);
    simpanLepas(pv.lepas);
    const tblLihat = h("button.tbl.tbl-kecil.tbl-pilih", {}, "Tampilan");
    const tblPohon = h("button.tbl.tbl-kecil.tbl-hantu", {}, "Struktur");
    // Keduanya tinggal di DOM dan cuma disembunyikan bergantian. Mencabut
    // lalu memasang ulang <iframe> MEMUAT ULANG dokumennya: halaman yang
    // punya skrip akan menjalankannya lagi dari awal, animasi mengulang, dan
    // tingginya diukur ulang dari nol -- semua itu hanya karena seseorang
    // ingin mengintip pohon strukturnya sebentar lalu kembali.
    const ket = dikarang ? h("p.pratinjau-ket", {},
      "Halaman contoh ini dibuatkan dari pemilih di CSS-mu sendiri: ",
      h("b", {}, "bukan"),
      " berkas HTML-mu. Gunanya satu: melihat aturan mana mengenai apa.") : null;
    const pilih = (lihat) => {
      pv.el.hidden = !lihat;
      pohon.hidden = lihat;
      // Keterangannya menerangkan HALAMANNYA, bukan pohonnya; membiarkannya
      // berdiri di atas daftar aturan membuatnya menerangkan hal yang salah.
      if (ket) ket.hidden = !lihat;
      tblLihat.classList.toggle("tbl-pilih", lihat);
      tblLihat.classList.toggle("tbl-hantu", !lihat);
      tblPohon.classList.toggle("tbl-pilih", !lihat);
      tblPohon.classList.toggle("tbl-hantu", lihat);
      tblLihat.setAttribute("aria-pressed", String(lihat));
      tblPohon.setAttribute("aria-pressed", String(!lihat));
    };
    tblLihat.addEventListener("click", () => pilih(true));
    tblPohon.addEventListener("click", () => pilih(false));
    tab.append(tblLihat, tblPohon);
    // Halaman yang DIBUATKAN wajib mengaku. CSS tidak menggambar apa pun
    // sendirian, jadi untuk blok CSS murni halamannya disusun dari pemilih di
    // aturannya sendiri -- berguna, tapi bukan berkas milik siapa pun. Tanpa
    // kalimat ini, yang terlihat adalah markup yang tidak pernah ia tulis dan
    // tidak akan pernah ia temukan lagi di mana pun.
    isikan(isi, ket, pv.el, pohon);
    pilih(true);
  } else {
    isikan(isi, pohon);
  }

  return h("div.keluaran-kartu" + (lulus ? "" : ".keluaran-salah"), {},
    h("div.keluaran-kepala", {},
      h("span.mata", {}, !bisa ? "Keluaran"
        : halamanDikarang(runner, kode) ? "Hasilnya" : "Halamanmu"),
      bisa ? tab : null,
      h("span.deret-kanan"),
      h("span.pil" + (lulus ? ".pil-tumbuh" : ".pil-salah"), {},
        "kode keluar " + r.kode_keluar),
      h("span.pil", {}, r.detik + " detik"),
      h("button.tbl.tbl-kecil.tbl-hantu",
        { title: "Tutup keluaran", onclick: saatTutup }, "Tutup")),
    isi,
    r.galat ? h("div.arti", {}, h("b", {}, "Artinya"),
                h("div", {}, r.galat.artinya || r.galat.mentah)) : null);
}

/* Potongan kode yang duduk DI DALAM kalimat: nama tag, panggilan fungsi,
 * atribut, nama berkas.
 *
 * Prosa teknis yang seluruhnya berhuruf sama membuat mata kehilangan satu
 * pembeda yang paling banyak menghemat waktu: mana yang harus dibaca sebagai
 * bahasa, mana yang harus dibaca huruf demi huruf. Di kalimat seperti
 * "<p> tidak boleh memuat <div>", keduanya adalah nama yang harus diketik
 * persis — dan kalau tampil sama dengan kata "memuat" di sebelahnya, satu-
 * satunya cara mengenalinya adalah sudah tahu lebih dulu.
 *
 * Polanya sengaja cuma yang MUSTAHIL jadi kata Indonesia biasa: kurung sudut,
 * tanda kurung kosong, tanda sama dengan berkutip, akhiran berkas, dan `kode`.
 * Properti CSS telanjang seperti `color` atau `grid` TIDAK ikut — kata-kata
 * itu muncul sebagai kata biasa di kalimat Indonesia, dan menandainya sebagai
 * kode berarti menaruh kotak di tengah kalimat yang bukan kode.
 *
 * Hasilnya 1.123 chip di seluruh kurikulum, dan 87% blok prosa tidak
 * memilikinya sama sekali. Itu yang membuatnya jadi penanda: kalau setiap
 * paragraf punya, tidak ada yang punya.
 */
const POLA_KODE = new RegExp(
  "`[^`]+`|</?[a-zA-Z][\\w-]*\\s*/?>"             // `kode` <tag> </tag> <br/>
  + "|\\b[a-zA-Z_][\\w.]*\\(\\)"                    // fungsi()
  + "|\\b[a-zA-Z-]+=\"[^\"]{1,30}\""              // atribut="nilai"
  + "|\\b[\\w-]+\\.(?:py|js|java|c|cpp|h|css|html|sql|sh|go|json|txt|md)\\b",
  "g");

/** Teks -> [string | <code>] siap dijadikan anak sebuah elemen. */
export function berkode(teks) {
  const keluar = [];
  let akhir = 0;
  POLA_KODE.lastIndex = 0;
  let m;
  while ((m = POLA_KODE.exec(teks)) !== null) {
    if (m.index > akhir) keluar.push(teks.slice(akhir, m.index));
    keluar.push(h("code", {}, m[0][0] === "`" ? m[0].slice(1, -1) : m[0]));
    akhir = m.index + m[0].length;
  }
  if (!keluar.length) return [teks];
  if (akhir < teks.length) keluar.push(teks.slice(akhir));
  return keluar;
}

/* Daftar butir materi.
 *
 * Sebuah butir bukan cuma sebaris teks: ia boleh membawa contoh kode kecil
 * miliknya sendiri dan boleh punya daftar anak. Ketiganya digambar DALAM
 * <li> yang sama supaya hubungannya terbaca — contoh yang diletakkan sebagai
 * saudara di luar butirnya berdiri sejajar dengan butir berikutnya, dan
 * pembaca layar mengumumkannya sebagai isi yang tidak dimiliki siapa pun.
 */
function senarai(d) {
  return h(d.urut ? "ol" : "ul", { start: d.mulai > 1 ? d.mulai : null }, d.butir.map((x) =>
    h("li", {}, berkode(x.teks),
      (x.blok || []).map((sub) => sub.jenis === "pra"
        ? h("div.pra.pra-butir", {}, sub.teks)
        : h("div.par.par-butir", {}, berkode(sub.teks))),
      x.anak ? senarai(x.anak) : null)));
}

function blokKode(b, i, m, key, bhs, bersih) {
  const p = b.petunjuk;
  const lencana = {
    program: "berkas utuh", potongan: "potongan", sesi: "sesi",
    multi: "beberapa berkas", ilustrasi: "ilustrasi",
  }[p.jenis] || p.jenis;

  // Menjalankan butuh DUA syarat, dan keduanya jawaban server: blok ini
  // memang program utuh (`bisa_dijalankan` dari berkas.py) DAN toolchain-nya
  // benar-benar terpasang di mesin ini (`siap` dari runner.py). Menyalakan
  // tombolnya tanpa syarat kedua berarti menawarkan sesuatu yang selalu
  // berakhir dengan "belum terpasang" -- tombol yang berujung penolakan,
  // persis yang dihindari daftar materi untuk bab yang masih terkunci.
  const bisaJalan = p.bisa_dijalankan && (b.siap ?? (bhs && bhs.siap));

  const keluaran = h("div.blok-keluaran");
  // Pendengar `message` milik pratinjau harus dicabut saat keluarannya
  // diganti ATAU layarnya ditinggalkan; kalau tidak, setiap kali tombol
  // Jalankan ditekan tertinggal satu pendengar yang mengukur bingkai yang
  // sudah tidak ada.
  let lepasPratinjau = null;
  const lepasPratinjauKini = () => {
    if (lepasPratinjau) { lepasPratinjau(); lepasPratinjau = null; }
  };
  bersih.push(lepasPratinjauKini);
  const pre = praKode(b.token);
  const sarung = h("div.blok-sarung", {}, pre);

  let editor = null;               // null selama blok masih baca-saja
  let sedangJalan = false;

  const tblJalan = bisaJalan
    ? h("button.tbl.tbl-kecil.tbl-utama",
        { title: "Jalankan kode ini di komputermu (Ctrl+Enter)" },
        ikon("jalankan", { ukuran: 14, tebal: 2 }), "Jalankan")
    : null;
  const tblUbah = bisaJalan
    ? h("button.tbl.tbl-kecil.tbl-hantu",
        { title: "Ubah kodenya lalu jalankan lagi" }, "Utak-atik")
    : null;
  const tblPulih = h("button.tbl.tbl-kecil.tbl-hantu",
    { hidden: true, title: "Kembalikan ke kode aslinya" }, "Kembalikan");

  /** Jalankan isi blok ini dan tunjukkan hasilnya TEPAT DI BAWAHNYA.
   *
   *  Sebelum ini tombolnya melempar ke Ruang Coba: layar lain, alamat lain,
   *  dan kembali berarti kehilangan posisi baca. Untuk pertanyaan sekecil
   *  "keluarnya apa kalau ini dijalankan?", perpindahan layar itu ongkos yang
   *  jauh lebih besar daripada pertanyaannya -- dan yang terjadi bukan orang
   *  membayar ongkosnya, melainkan orang berhenti bertanya.
   *
   *  Ini TIDAK menilai apa pun. /api/coba tidak menyentuh progres sama sekali;
   *  definisi "lulus" tetap cuma satu dan tempatnya runner.periksa. */
  async function jalankan() {
    if (sedangJalan) return;
    sedangJalan = true;
    tblJalan.disabled = true;
    const menunggu = h("div.keluaran-kartu.deret", {},
      h("div.pusaran"), h("span", {}, "Menjalankan…"));
    isikan(keluaran, menunggu);
    masuk(menunggu, { geser: 5, pegas: "jawab" });
    try {
      const r = await api.kirim("/api/coba", {
        bahasa: b.bahasa || bhs.runner,
        kode: editor ? editor.nilai : b.kode,
      });
      lepasPratinjauKini();
      const kartu = kartuKeluaran(r, bhs.runner, editor ? editor.nilai : b.kode,
        () => { lepasPratinjauKini(); kosongkan(keluaran); },
        (fn) => { lepasPratinjau = fn; });
      isikan(keluaran, kartu);
      masuk(kartu, { geser: 6, pegas: "jawab" });
    } catch (e) {
      const kartu = h("div.keluaran-kartu.keluaran-salah", {},
        h("div.terminal", {}, e.message));
      isikan(keluaran, kartu);
      masuk(kartu, { geser: 6 });
    } finally {
      sedangJalan = false;
      tblJalan.disabled = false;
    }
  }

  /** Ganti tampilan baca-saja jadi editor sungguhan, di tempat.
   *
   *  Membaca kode orang lain dan MENGUBAHNYA lalu melihat apa yang rusak
   *  adalah dua kegiatan yang sangat berbeda, dan yang kedua itulah yang
   *  mengajari. Kodenya tidak pernah ditimpa: `b.kode` tetap utuh, jadi
   *  "Kembalikan" selalu bisa. */
  function utakAtik() {
    if (editor) { editor.fokus(); return; }
    editor = new Editor({
      bahasa: b.sorot || m.sorot,
      kode: b.kode,
      label: "Utak-atik kode: " + (p.nama || b.judul || m.judul),
      pintasan: { "ctrl+enter": () => jalankan() },
    });
    bersih.push(() => { if (editor) editor.lepas(); });
    isikan(sarung, editor.el);
    masuk(editor.el, { geser: 6, pegas: "jawab" });
    tblUbah.hidden = true;
    tblPulih.hidden = false;
    editor.fokus();
  }

  function pulihkan() {
    if (!editor) return;
    editor.lepas();
    editor = null;
    isikan(sarung, pre);
    masuk(pre, { geser: 6, pegas: "jawab" });
    tblUbah.hidden = false;
    tblPulih.hidden = true;
    kosongkan(keluaran);
  }

  if (tblJalan) tblJalan.addEventListener("click", jalankan);
  if (tblUbah) tblUbah.addEventListener("click", utakAtik);
  tblPulih.addEventListener("click", pulihkan);

  /* `tabindex="-1"`, bukan `"0"`: pembungkusnya harus bisa DIFOKUS supaya
     `j`/`k` punya sasaran dan `⏎` punya pemilik, tapi ia tidak boleh
     menambah satu pun perhentian Tab. Tombol di `.blok-alat` sudah native dan
     sudah ada di urutan Tab; menambahkan pembungkusnya berarti setiap contoh
     kode menyisipkan satu perhentian kosong di antara tombol-tombol yang
     memang berguna. Cincin fokusnya dipinjam dari `:focus-visible` global
     (`gaya.css:608`) -- tidak ada gaya fokus baru di sini. */
  return h("div.blok-kode", { tabindex: "-1" },
    h("div.blok-kepala", {},
      p.nama ? h("span.berkas", {}, p.nama)
             : h("span", {}, b.judul || p.instruksi),
      h("span.lencana", {}, lencana),
      h("div.blok-alat", {},
        tblJalan, tblUbah, tblPulih,
        h("button.tbl.tbl-kecil.tbl-hantu", {
          onclick: (e) => salin(b.kode, "Kode disalin.", e.currentTarget),
        }, "Salin"),
        // "Lihat jalannya" (jejak.js): rekaman langkah demi langkah dari
        // /api/jejak. Hanya Python, dan hanya contoh yang tidak menunggu input.
        bisaJalan && (b.bahasa || bhs.runner) === "python" && !/\binput\s*\(/.test(b.kode)
          ? tombolJejak(b.kode, b.token, () => (editor ? editor.nilai : b.kode)) : null,
        // Ruang Coba tetap ada, tapi tidak lagi jadi satu-satunya jalan: untuk
        // kerja yang lebih panjang (stdin, ganti bahasa, draf tersimpan) ia
        // punya yang tidak muat di sini.
        p.bisa_dijalankan ? h("a.tbl.tbl-kecil.tbl-hantu", {
          title: "Buka di Ruang Coba: layar penuh, bisa diberi masukan (stdin)",
          href: `#/coba?key=${key}&materi=${m.indeks}&bagian=${b.bagian ?? i}`,
        }, "Ruang Coba") : null)),
    sarung,
    p.perintah.length
      ? h("div.blok-kaki", {}, "Jalankan: ",
          h("span.perintah", {}, p.perintah.join("   lalu   ")))
      : p.keterangan ? h("div.blok-kaki", {}, p.keterangan)
      : (p.instruksi && !p.nama) ? h("div.blok-kaki", {}, p.instruksi) : null,
    keluaran);
}

/* ========================================================= bagian bersama */

/** Tombol bookmark. Sebuah ikon-tombol, bukan tombol berteks: ia berdiri di
 *  kepala halaman bersama tombol catatan, dan dua tombol berteks penuh di situ
 *  memakan lebar yang seharusnya jadi milik judulnya.
 *
 *  Keadaannya disampaikan tiga hal sekaligus — warna, ketebalan garis ikon,
 *  dan `aria-pressed` — bukan warna saja. Tombol yang cuma berubah warna
 *  adalah tombol yang keadaannya hilang untuk mata yang sulit membedakan
 *  warna, dan tidak pernah ada sama sekali untuk pembaca layar. */
export function tombolBookmark(key, tipe, indeks, aktif) {
  const gambar = h("span");
  const tbl = h("button.ikon-tombol", {
    onclick: async () => {
      const r = await api.kirim("/api/bookmark", { key, tipe, indeks });
      setel(r.bookmark);
      // Hanya saat DITANDAI. Melepas tanda tidak dirayakan — perayaan untuk
      // membatalkan sesuatu membingungkan, bukan menyenangkan.
      if (r.bookmark) { denyut(tbl); percikBara(tbl, { jumlah: 6 }); }
      sorak(r.bookmark ? "Masuk bookmark." : "Dihapus dari bookmark.", "", 1.8);
    },
  }, gambar);

  function setel(ada) {
    isikan(gambar, ikon("bookmark", { ukuran: 19, tebal: ada ? 2.4 : 1.7 }));
    tbl.classList.toggle("aktif", ada);
    tbl.setAttribute("aria-pressed", String(ada));
    tbl.title = ada ? "Hapus dari bookmark" : "Simpan ke bookmark";
    tbl.setAttribute("aria-label", tbl.title);
  }
  setel(Boolean(aktif));
  return tbl;
}

export function tombolCatatan(kunci, catatan, judul) {
  const gambar = h("span");
  const tbl = h("button.ikon-tombol", {
    onclick: () => bukaCatatan(kunci, judul, tbl),
  }, gambar);

  tbl.setelCatatan = (punya) => {
    isikan(gambar, ikon("catatan", { ukuran: 19, tebal: punya ? 2.4 : 1.7 }));
    tbl.classList.toggle("aktif", punya);
    tbl.title = punya ? "Catatanmu untuk halaman ini (tersimpan)"
                      : "Tulis catatan untuk halaman ini";
    tbl.setAttribute("aria-label", tbl.title);
  };
  tbl.setelCatatan(Boolean(catatan && catatan.teks));
  return tbl;
}

export async function bukaCatatan(kunci, judul, tbl) {
  const kini = await api.ambil("/api/catatan", { kunci });
  const area = h("textarea", {
    "aria-label": "Catatan pribadimu untuk " + judul,
    value: kini.teks || "",
    placeholder: "Tulis dengan kalimatmu sendiri: apa inti halaman ini, dan "
      + "bagian mana yang tadi sempat membingungkan.",
    gaya: { minHeight: "220px" },
  });

  const pilih = await jendela({
    judul: "Catatan: " + judul,
    isi: h("div", {},
      h("p.kepala-sub", { gaya: { margin: "0 0 var(--s3)" } },
        "Menuliskan ulang dengan bahasa sendiri adalah cara paling murah "
        + "untuk tahu apakah kamu benar-benar paham."),
      area,
      kini.diubah ? h("div.baris-sisi", { gaya: { marginTop: "var(--s2)" } },
        "Terakhir diubah " + jamRamah(kini.diubah)) : null),
    aksi: [{ label: "Batal", nilai: false },
           { label: "Simpan", nilai: true, kelas: "tbl-utama" }],
  });
  if (pilih !== true) return null;

  const hasil = await api.kirim("/api/catatan", { kunci, teks: area.value });
  if (tbl && tbl.setelCatatan) tbl.setelCatatan(Boolean(hasil.teks));
  sorak(hasil.teks ? "Catatan disimpan." : "Catatan dikosongkan.", "tumbuh", 2);
  return hasil;
}

/* ============================================================== bookmark */

export async function layarBookmark() {
  const isi = h("div");

  async function segarkan() {
    const b = await api.ambil("/api/bookmark");
    isikan(isi,
      b.daftar.length
        ? ungkapSenarai(h("div.senarai", {}, b.daftar.map((x) => h("a.baris", {
            href: `#/${x.tipe}/${x.bahasa}/${x.indeks}`,
          },
            pilJenis(x.tipe),
            h("div.isi", {},
              h("div.judul", {}, x.judul),
              h("div.ket", {}, x.label_bahasa)),
            h("span.baris-panah", {}, ikon("lanjut", { ukuran: 18 }))))))
        : kosong("Belum ada bookmark",
            "Buka materi, kuis, atau latihan mana pun, lalu tekan ikon pita di "
            + "kepala halamannya.",
            h("a.tbl.tbl-utama", { href: "#/dasbor" }, "Ke dasbor")),
      b.basi ? keadaan({
        jenis: "kunci",
        judul: `${b.basi} bookmark menunjuk halaman yang sudah tidak ada`,
        ket: "Biasanya karena kurikulumnya diperbarui dan judulnya berubah.",
        aksi: [h("button.tbl.tbl-kecil", { onclick: async () => {
          const r = await api.kirim("/api/bookmark/bersihkan", {});
          sorak(`${r.dibuang} bookmark basi dibuang.`, "tumbuh");
          segarkan();
        } }, "Bersihkan")],
      }) : null);
  }
  await segarkan();

  return {
    el: h("div.masuk", {},
      kepalaBersampul("bookmark", { ragam: "pecahan" },
        h("span.mata", {}, "Tersimpan"),
        h("h1", {}, "Bookmark"),
        h("p.kepala-sub", {}, "Halaman yang kamu tandai untuk dibuka lagi.")),
      isi),
    judul: "Bookmark",
  };
}

/* =============================================================== catatan */

export async function layarCatatan() {
  const isi = h("div");

  async function segarkan() {
    const c = await api.ambil("/api/catatan/semua");
    isikan(isi,
      c.daftar.length
        ? h("div.senarai", {}, c.daftar.map((x) => h("div.kartu", {},
            h("div.deret", { gaya: { marginBottom: "var(--s3)" } },
              x.basi ? h("span.pil.pil-salah", {}, "halaman sudah tidak ada")
                     : h("a.pil",
                         { href: `#/${x.tipe}/${x.bahasa}/${x.indeks}` },
                         `${x.label_bahasa} · ${x.judul}`),
              h("span.deret-kanan.baris-sisi", {}, jamRamah(x.diubah)),
              h("button.tbl.tbl-kecil.tbl-hantu", {
                onclick: async () => {
                  if (await bukaCatatan(x.kunci, x.judul)) segarkan();
                },
              }, "Ubah")),
            h("div.par", { gaya: { margin: "0", color: "var(--teks-2)" } },
              x.teks))))
        : kosong("Belum ada catatan",
            "Buka materi mana pun, lalu tekan ikon pena di kepala halamannya."));
  }
  await segarkan();

  return {
    el: h("div.masuk", {},
      kepalaBersampul("catatan", { ragam: "gelombang" },
        h("span.mata", {}, "Milikmu sendiri"),
        h("h1", {}, "Catatanku"),
        h("p.kepala-sub", {}, "Menuliskan ulang dengan bahasamu sendiri "
          + "adalah cara paling murah untuk tahu apakah kamu benar-benar "
          + "paham. Disimpan terpisah dari progres, jadi menghapus progres "
          + "tidak ikut menghapus tulisanmu.")),
      isi),
    judul: "Catatanku",
  };
}

/* ================================================================== cari */

export async function layarCari({ q, tipe }, ctx) {
  const kata = q || "";
  // Dihitung dari daftar bahasa, tidak diketik: kalimat ini dulu berbunyi
  // "11 bahasa" dan tetap begitu sesudah kurikulumnya jadi dua puluh.
  const nBahasa = ctx && ctx.awal ? ctx.awal.bahasa.length : 0;
  const saring = tipe || "semua";
  const hasil = kata.length >= 2
    ? (await api.ambil("/api/cari", { q: kata, tipe: saring })).hasil : [];

  const medan = h("input", {
    type: "text", value: kata, placeholder: nBahasa ? `Cari di ${nBahasa} bahasa sekaligus…` : "Cari di semua bahasa…",
    "aria-label": "Kata yang dicari",
    gaya: { fontSize: "var(--t-baca)" },
  });
  medan.addEventListener("keydown", (e) => {
    if (e.key === "Enter") ganti(medan.value, saring);
  });

  function ganti(k, t) {
    location.hash = "#/cari?q=" + encodeURIComponent(k)
      + (t !== "semua" ? "&tipe=" + t : "");
  }

  const el = h("div.masuk", {},
    kepalaBersampul("cari", { ragam: "orbit" },
      h("span.mata", {}, "Pencarian"),
      h("h1", {}, "Cari"),
      h("p.kepala-sub", {}, "Menjangkau judul, isi materi, soal kuis, dan "
        + "solusi latihan di semua bahasa sekaligus. Mencari buku atau kursus? ",
        h("a", { href: "#/pustaka" + (kata ? "?q=" + encodeURIComponent(kata) : "") },
          "Cari di Pustaka"), ".")),
    medan,
    h("div.deret.deret-rapat", { gaya: { margin: "var(--s4) 0 var(--s5)" } },
      ["semua", "materi", "kuis", "latihan"].map((t) =>
        h("button.tbl.tbl-kecil" + (t === saring ? ".tbl-pilih" : ".tbl-hantu"),
          { onclick: () => ganti(medan.value, t),
            "aria-pressed": String(t === saring) },
          t[0].toUpperCase() + t.slice(1)))),

    kata.length < 2
      ? kosong("Ketik minimal dua huruf",
          "Coba: pointer, rekursi, JOIN, closure, malloc, interface.")
      : hasil.length
        ? h("div", {},
            h("div.baris-sisi", { gaya: { marginBottom: "var(--s3)" } },
              `${hasil.length} hasil untuk "${kata}"`),
            // Penanda "terkunci" dipasang SEBELUM diklik, bukan sesudah.
            // Tautannya sengaja tetap hidup: menekannya mendarat di layar yang
            // menjelaskan apa yang kurang, dan itu jawaban yang lebih berguna
            // daripada baris yang tidak bisa ditekan sama sekali. Yang tidak
            // boleh terjadi cuma satu — orang mengklik tanpa satu pun isyarat
            // lebih dulu.
            ungkapSenarai(h("div.senarai", {}, hasil.map((r) => h("a.baris", {
              href: `#/${r.tipe}/${r.bahasa}/${r.indeks}`,
            },
              pilJenis(r.tipe),
              h("div.isi", {},
                h("div.judul", {}, tandai(r.judul, kata)),
                h("div.ket", {}, r.label_bahasa,
                  r.cuplikan ? ": " : "",
                  r.cuplikan ? tandai(r.cuplikan, kata) : "")),
              r.terkunci ? h("span.pil.pil-kunci", {}, "terkunci") : null)))))
        : kosong(`Tidak ada yang cocok dengan "${kata}"`,
            "Coba kata yang lebih pendek, atau matikan saringan tipe."),
  );

  setTimeout(() => {
    medan.focus();
    medan.setSelectionRange(medan.value.length, medan.value.length);
  }, 40);
  return { el, judul: "Cari" };
}

/** Tawarkan kuis yang BARU SAJA siap karena materi ini tuntas.
 *
 *  Server yang memutuskan kesiapannya (pelajar/kuis_materi.py: semua materi
 *  yang diuji kuis itu sudah dibaca); di sini cuma dibacakan. Tombolnya
 *  sengaja bukan tbl-utama: kaki materi sudah punya tindakan utamanya
 *  (materi berikutnya), dan dua permukaan beraksen berarti nol. */
function tawarkanKuisSiap(kaki, key, hasil) {
  const kuis = (hasil && hasil.kuis_siap) || [];
  if (!kuis.length || kaki.querySelector(".tbl-kuis-siap")) return;
  const q = kuis[0];
  const tbl = h("a.tbl.tbl-kuis-siap", { href: `#/kuis/${key}/${q.indeks}` },
    ikon("kuis", { ukuran: 17 }),
    `${potong(q.judul, 30)} siap: semua materinya sudah kamu baca`);
  kaki.appendChild(tbl);
  masuk(tbl, { geser: 7, pegas: "jawab" });
}

/** Dasbor sebagai meja kerja: yang harus dikerjakan di atas lipatan.
 *  Alasan susunannya ditulis di dasborBerjalan(), di tempat ia dipanggil. */
function dasborMeja(d, ctx, { utama, sisaLangkah, dijalani, bento, sapa }) {
  const p = d.posisi;
  const posisi = p ? h("p.meja-posisi", {},
    h("a", { href: "#/bahasa/" + p.key }, h("b", {}, p.label)),
    p.bab ? ` · Bab ${p.bab} dari ${p.bab_total}: ${p.bab_judul}` : "",
    ` · ${p.materi}/${p.total_materi} materi`) : null;
  // "Punya 30 menit?": langkah teratas, berurutan, selama muat dalam 30 menit.
  // Menitnya perkiraan server (pelajar/waktu.py), dijumlahkan saja di sini.
  let total = 0;
  const muat = [utama, ...sisaLangkah].filter(Boolean).filter((x) => {
    if (!x.menit || total + x.menit > 30) return false;
    total += x.menit; return true;
  });
  const paket = muat.length > 1
    ? h("p.meja-paket", {}, ikon("waktu", { ukuran: 16 }),
        `Punya 30 menit? ${muat.length} langkah teratas kira-kira ${total} menit.`)
    : null;
  const ulang = d.kuis_jatuh_tempo > 2
    ? h("p.meja-catatan", {}, `${d.kuis_jatuh_tempo} kuis menunggu diulang. `
        + "Dua yang paling mendesak sudah ada di antrean; sisanya bisa besok.")
    : null;

  return h("div.meja", {},
    h("section.meja-atas", {},
      h("div.meja-kini", {},
        h("span.mata", {}, new Date().toLocaleDateString("id-ID",
          { weekday: "long", day: "numeric", month: "long", year: "numeric" })),
        judulSapa(sapa, d.nama, utama ? utama.bahasa : null),
        posisi, paket,
        utama ? kartuLanjutkan(utama) : h("p.sambut-sub", {}, kalimatPembuka(d))),
      h("div.meja-antrean", {},
        sisaLangkah.length || d.tantangan
          ? blokAntrean(sisaLangkah, d.tantangan, ctx)
          : h("p.sambut-sub", {}, kalimatPembuka(d)),
        ulang,
        // Di kolom kanan, bukan di bawah: kolom kiri (sapaan + kartu) lebih
        // tinggi daripada antrean, dan ruang di bawah antrean itulah tempat
        // persen tiap bahasa terlihat tanpa menggulir.
        barisBahasaMeja(dijalani.slice(0, 4)))),
    panelLangitMeja(p ? p.key : null),
    bento,
    h("section.meja-ritme", {}, blokBara(d),
      h("div.ritme-sampul", {}, sampul("ritme", { ragam: "gelombang", lebar: 480, tinggi: 360 }))));
}

/** Bahasa yang sedang dijalani: satu baris per bahasa, persennya selalu
 *  terlihat. Persen dan jumlah materi dari server (statistik_bahasa); persen
 *  itu ikut menghitung kuis dan latihan, jadi labelnya menyebut "selesai",
 *  bukan "materi". */
function barisBahasaMeja(daftar) {
  if (!daftar.length) return null;
  return h("section.meja-bahasa", { "aria-label": "Bahasa yang sedang kamu jalani" },
    h("h2.meja-judul", {}, "Yang sedang kamu jalani"),
    h("div.meja-bahasa-daftar", {}, daftar.map((b) => h("a.meja-bahasa-baris", {
      href: "#/bahasa/" + b.key,
    },
      h("span.meja-bahasa-sampul", {}, sampul(b.key, { bahasa: b.key, lebar: 160, tinggi: 100 })),
      h("span.meja-bahasa-nama", {}, b.label),
      h("span.meja-bahasa-ket", {}, `${b.materi}/${b.total_materi} materi`),
      h("span.meja-bahasa-bilah", {}, bilah(Math.min(100, b.persen), b.persen >= 100 ? "tumbuh" : "")),
      h("b.meja-bahasa-persen", {}, `${Math.round(b.persen)}% selesai`)))));
}
