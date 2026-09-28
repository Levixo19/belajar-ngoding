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
  rayakan, salin, tanggalRamah, jamRamah, selisihHari, jendela, tandai, GalatApi,
} from "./inti.js";
import {
  animasi, masuk, ungkap, saatTampak, denyut, percikBara, adaGerak, berurut,
} from "./gerak.js";
import { ikon, ikonTipe } from "./ikon.js";
import { praKode } from "./sorot.js";
import { Editor } from "./editor.js";
import {
  pratinjauHtml, bisaDipratinjau, dokumenPratinjau, halamanDikarang,
} from "./pratinjau.js";

function pilTipe(t) {
  return t === "kuis" ? ".pil-ungu" : t === "latihan" ? ".pil-nyala" : ".pil-tenang";
}

/** Pil bertanda jenis isi: ikon + kata. Ikonnya membuat jenisnya terbaca
 *  sebelum katanya sempat dibaca — dan di daftar sepanjang dua puluh baris,
 *  "sebelum dibaca" itu selisih yang besar. */
export function pilJenis(tipe) {
  return h("span.pil.pil-jenis" + pilTipe(tipe), {},
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
function saatSiap(el, fn, maks = 40) {
  let sisa = maks;
  const coba = () => {
    if (el.isConnected && el.clientWidth > 0) { fn(); return; }
    if (sisa-- > 0) requestAnimationFrame(coba);
  };
  requestAnimationFrame(coba);
}

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
        ? `${jenis}. Tidak perlu memasang apa pun — cukup aplikasi ini dan `
          + "browser yang sedang kamu buka."
        : `${jenis}. Langkah pertama di jalur ${s.label_bahasa}.`)),
    h("span.tbl.tbl-utama.tbl-besar", {},
      "Mulai", ikon("lanjut", { ukuran: 18 })));
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

function ubinBahasa(b) {
  const tanda = !b.siap
    ? ["ubin-butuh", `butuh ${b.hilang.join(", ")}`]
    : !b.pasang
      ? ["ubin-bebas", "tanpa pasang apa pun"]
      : null;
  return h("a.ubin", { href: "#/bahasa/" + b.key },
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

  const el = h("div", {},
    h("header.sambut", {},
      h("span.mata", {}, new Date().toLocaleDateString("id-ID",
        { weekday: "long", day: "numeric", month: "long", year: "numeric" })),
      h("h1", {}, d.nama ? `${sapa}, ${d.nama}.` : `${sapa}.`),
      h("p.sambut-sub", {}, kalimatPembuka(d))),

    h("div.dasbor", {},
      h("div.dasbor-utama", {},
        utama ? kartuLanjutkan(utama) : null,
        sisaLangkah.length || d.tantangan
          ? blokAntrean(sisaLangkah, d.tantangan, ctx) : null,
        blokBahasa(d.bahasa)),

      h("aside.dasbor-sisi", {},
        kartuBara(d),
        blokBara(d))),
  );
  return { el, judul: "Dasbor" };
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
    h("span.lanjutkan-nomor", {}, String(s.indeks + 1)),
    h("div.lanjutkan-isi", {},
      h("span.mata", {}, `${jenis} · ${s.label_bahasa}`),
      h("h2", {}, tanpaNomor(s.judul)),
      h("p", {}, s.alasan)),
    h("span.lanjutkan-tbl", {},
      h("span", {}, "Lanjutkan"),
      ikon("lanjut", { ukuran: 20 })));
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
    gaya: { "--panas": String(panas) },
    title: `${d.di_level} dari ${d.butuh_level} XP menuju level ${d.level + 1}`,
  }, svg, h("div.cincin-isi", {},
    h("div.cincin-angka", {}, String(d.level)),
    h("div.cincin-label", {}, "level")));

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

  // Dibandingkan tanggal ke tanggal, bukan cap waktu ke cap waktu: selisih
  // milidetik dibagi sehari lalu dibulatkan menghitung jam yang sudah berjalan
  // hari ini sebagai satu hari penuh.
  const hari = new Date(tgl + "T00:00:00");
  if (Number.isNaN(hari.getTime())) return null;
  const iniHari = new Date();
  iniHari.setHours(0, 0, 0, 0);
  const selisih = Math.round((iniHari - hari) / 86400000);
  if (selisih <= 0) return null;

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
      h("div.judul", {}, `${s.label_bahasa} — ${tanpaNomor(s.judul)}`),
      h("div.ket", {}, s.alasan)),
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

/** Bahasa yang sedang jalan. Yang belum disentuh sama sekali TIDAK ikut di
 *  sini — sebelas kartu 0% adalah daftar yang tidak bisa dipakai untuk
 *  memutuskan apa pun, dan tempat memilih bahasa baru sudah ada di menu
 *  Bahasa maupun di palet perintah. */
function blokBahasa(daftar) {
  const jalan = daftar.filter((b) => b.persen > 0);
  const tampil = jalan.length ? jalan : daftar.slice(0, 3);

  const petak = h("div.petak.petak-3", {}, tampil.map((b) => h("a.kartu.kartu-rapat", {
      href: "#/bahasa/" + b.key, gaya: { color: "inherit" },
    },
      h("div.rinci-atas", {},
        h("b", {}, b.label),
        h("span.rinci-angka", {}, bulat(b.persen) + "%")),
      bilah(b.persen, b.persen >= 100 ? "tumbuh" : ""),
      h("div.rinci-angka", { gaya: { marginTop: "var(--s2)" } },
        `${b.materi}/${b.total_materi} materi · ${b.kuis}/${b.total_kuis} kuis`
        + ` · ${b.latihan_lulus + b.latihan_manual}/${b.total_latihan} latihan`),
      b.siap ? null
             : h("div.pil.pil-kunci", { gaya: { marginTop: "var(--s2)" } },
                 "toolchain belum ada"))));
  ungkap(petak, { per: 30, maks: 240, geser: 10 });

  return h("section", {},
    h("div.bagian-kepala", {},
      h("span.mata", {},
        jalan.length ? "Sedang kamu jalani" : "Mulai dari salah satu"),
      h("span.baris-sisi", {}, `${daftar.length} bahasa tersedia`)),
    petak);
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
  const delay = berurut(bara.length, { per: 12, maks: 340, dari: "akhir" });

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
      animasi(el, { opacity: [0, 1], transform: ["scale(.35)", "none"] },
              { pegas: "jawab", delay: delay(i) });
    });
  }, { bagian: 0.15 });
}

function blokBara(d) {
  const target = Math.max(1, d.target_harian);
  const petak = h("div.bara-petak");
  const hariIni = new Date().toISOString().slice(0, 10);

  // Sisipkan sel kosong supaya kolom pertama jatuh di hari yang benar. Tanpa
  // ini seluruh kisi bergeser dan barisnya tidak lagi berarti "Senin".
  const pertama = d.heatmap[0];
  if (pertama) {
    const hari = (new Date(pertama.tanggal + "T00:00:00").getDay() + 6) % 7;
    for (let i = 0; i < hari; i++) {
      petak.appendChild(h("div", { gaya: { width: "11px", height: "11px" } }));
    }
  }
  const menyala = [];
  for (const s of d.heatmap) {
    const tingkat = s.xp <= 0 ? 0 : s.xp < target * 0.5 ? 1 : s.xp < target ? 2 : 3;
    const sel = h("div.bara-sel" + (tingkat ? ".bara-" + tingkat : "")
      + (s.tanggal === hariIni ? ".bara-kini" : ""),
      { title: `${tanggalRamah(s.tanggal)} — ${s.xp} XP` });
    if (tingkat) menyala.push(sel);
    petak.appendChild(sel);
  }
  nyalakanBara(petak, menyala);

  const aktif = d.heatmap.filter((s) => s.xp > 0).length;
  return h("section", {},
    h("span.mata", {}, "Bara — enam bulan terakhir"),
    h("div.kartu.kartu-rapat", {},
      petak,
      h("div.bara-legenda", {},
        h("span", {}, `${aktif} hari menyala`),
        h("span", { gaya: { marginLeft: "auto" } }, "dingin"),
        h("div.bara-sel"), h("div.bara-sel.bara-1"),
        h("div.bara-sel.bara-2"), h("div.bara-sel.bara-3"),
        h("span", {}, "panas"))));
}

/* ================================================================ bahasa */

export async function layarBahasa({ key }, ctx) {
  const b = await api.ambil("/api/bahasa", { key });
  const s = b.statistik;

  const isi = h("div");
  const daftarTab = ["materi", "kuis", "latihan"];
  const kunciTab = "tab." + key;

  const tombolTab = daftarTab.map((t) => h("button.tbl.tbl-hantu", {
    onclick: () => pilih(t),
    data: { tab: t },
  }, ikon(ikonTipe(t), { ukuran: 17 }),
     `${t[0].toUpperCase()}${t.slice(1)}`,
     h("span.tab-jumlah", {}, String(b[t].length))));

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
    const baru = t === "kuis" ? daftarKuis(b)
      : t === "latihan" ? daftarLatihan(b)
      : daftarMateri(b);

    // Berganti tab bukan berpindah halaman: daftarnya diganti di tempat, dan
    // gerakannya sengaja lebih pendek daripada pergantian layar supaya
    // perbedaan itu terbaca.
    isikan(isi, baru);
    if (berganti) masuk(baru, { geser: 7, pegas: "jawab" });
  }

  const el = h("div.masuk", {},
    h("header.kepala-besar", {},
      h("span.mata", {}, "Bahasa"),
      h("h1", {}, b.label),
      h("p.kepala-sub", {}, kalimatBahasa(b, s)),
      barisFakta(b, s)),

    kartuLanjutBahasa(b, key),

    b.siap ? null : blokToolchain(b),
    b.catatan ? keadaan({ gambar: "bantuan", judul: "Perlu diketahui",
                          ket: b.catatan }) : null,

    h("div.deret.tab-deret", {},
      tombolTab,
      // Dipisahkan dari tiga tab di sebelahnya, dan sengaja BUKAN .tbl-hantu:
      // dengan bentuk yang sama persis, ia terbaca sebagai "tab keempat yang
      // sedang tidak aktif" — padahal menekannya meninggalkan halaman ini.
      h("a.tbl.tbl-pergi.deret-kanan", { href: "#/coba?bahasa=" + b.runner },
        ikon("jalankan", { ukuran: 17 }), "Ruang coba " + b.label,
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
    return `Semuanya sudah kamu selesaikan — ${total} bagian, tuntas.`;
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
  const kuis = b.kuis.find((q) => !q.pernah || q.jatuh_tempo);
  const latihan = b.latihan.find(
    (e) => e.status !== "lulus" && e.status !== "manual");

  let s = null;
  if (materi) {
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
                           : "Semua materi terbaca — sekarang ujinya." };
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
      + "berjalan penuh; yang mati hanya penilaian otomatis latihan — dan "
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
function daftarMateri(b) {
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
            ? h("p.bab-bebas", {}, "Penguncian bab sedang dimatikan — semua "
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
      h("div.senarai", {}, b.materi.map((m) => barisMateri(b, m)))));
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

  wadah.appendChild(petaBab(daftar, sedang));

  const petak = h("div.bab-daftar", {}, daftar.map((bab) => h(
    "details.bab"
      + (bab.status === "terkunci" ? ".bab-terkunci"
         : bab.status === "tuntas" ? ".bab-tuntas" : "")
      + (bab === sedang ? ".bab-kini" : ""),
    { id: "bab-" + bab.nomor,
      "aria-label": `Bab ${bab.nomor}: ${bab.judul}`,
      // Yang terbuka cuma bab yang sedang dikerjakan — dan kalau tidak ada
      // satu pun yang berstatus "terbuka" (semuanya tuntas), bab PERTAMA yang
      // dibuka supaya halaman ini tidak pernah tampil sebagai sebelas kepala
      // tanpa satu pun isi.
      open: bab === sedang || (!sedang && bab === daftar[0]) },
    kepalaBab(bab),
    h("div.bab-isi", {},
      bab.status === "terkunci" ? catatanKunci(bab, bab === pintu) : null,
      h("div.senarai", {}, bab.materi
        .map((i) => materi.get(i))
        .filter(Boolean)
        .map((m) => barisMateri(b, m)))))));

  // Yang diungkap BAB-nya, bukan tiap barisnya. Sesudah dikelompokkan, satuan
  // yang berarti di halaman ini adalah bab — dan mengungkapkan dua puluh baris
  // satu per satu di dalam kepala bab yang sudah berdiri duluan cuma
  // memperpanjang urutannya tanpa menambah arti.
  ungkap(petak, { per: 40, maks: 240, geser: 9, pegas: "jawab" });
  wadah.appendChild(petak);
  return wadah;
}

/** Peta bab: seluruh bab bahasa ini dalam satu baris segmen bernomor.
 *
 *  Ini kompensasi langsung dari pelipatan di bawahnya. Begitu isi bab boleh
 *  tertutup, harus ada satu tempat yang tetap memperlihatkan JALUR
 *  keseluruhannya — ada berapa, sudah sampai mana, dan mana yang masih
 *  terkunci — tanpa satu gulir pun. */
function petaBab(daftar, sedang) {
  return h("nav.peta-bab", { "aria-label": "Peta bab" },
    daftar.map((bab) => h("a." + (bab.status === "tuntas" ? "peta-tuntas"
        : bab.status === "terkunci" ? "peta-terkunci"
        : bab === sedang ? "peta-kini" : "peta-jalan"), {
      href: "#bab-" + bab.nomor,
      title: `Bab ${bab.nomor} · ${bab.judul} — ${bab.selesai}/${bab.jumlah} `
        + `materi (${bab.label_tingkat.toLowerCase()})`,
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
      h("i", { gaya: { opacity: String(0.35 + 0.65 * (bab.persen / 100)) } }))));
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
function kepalaBab(bab) {
  return h("summary.bab-kepala", {},
    h("span.bab-nomor", {}, String(bab.nomor).padStart(2, "0")),
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
      h("span.bab-angka", {}, `${bab.selesai}/${bab.jumlah} materi`),
      bilah(bab.persen, bab.status === "tuntas" ? "tumbuh" : "")),
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
        ? h("div.ket", {}, "berhenti di tengah — belum dihitung selesai") : null),
    m.bookmark ? h("span.pil.pil-nyala", {}, "ditandai") : null,
    h("span.baris-sisi.sembunyi-hp", {}, `${m.bagian} bagian`),
  ];
  if (m.terkunci) return h("div.baris.baris-terkunci", {}, isi);
  return h("a.baris", {
    href: `#/materi/${b.key}/${m.indeks}`,
    kelas: m.status === "selesai" ? "selesai" : "",
  }, isi);
}

function ungkapSenarai(el) {
  ungkap(el, { per: 24, maks: 260, geser: 8, pegas: "jawab" });
  return el;
}

function daftarKuis(b) {
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
          : `${q.soal} soal · belum pernah dikerjakan`)),
      q.jatuh_tempo ? h("span.pil.pil-ungu", {}, "saatnya diulang")
        : (q.pernah && hari !== null && hari > 0
            ? h("span.pil.sembunyi-hp", {}, `ulang ${hari} hari lagi`) : null),
      q.salah_tersisa
        ? h("span.pil.pil-salah", {}, `${q.salah_tersisa} masih salah`) : null,
      q.pernah ? h("span.sembunyi-hp", { gaya: { width: "56px", flex: "none" } },
        bilah(persen, persen >= 100 ? "tumbuh" : "")) : null);
  })));
}

function daftarLatihan(b) {
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
    !e.dinilai ? h("span.pil.sembunyi-hp", {}, "tanpa nilai otomatis") : null))));
}

/* ================================================================ materi */

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
      rayakan(await api.kirim("/api/materi/selesai",
                              { key, indeks, tuntas: true }));
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
    tblSelesai,
    m.sesudah
      ? h("button.tbl.tbl-utama", { onclick: () => tandaiSelesai(true) },
          potong(m.sesudah, 26), ikon("lanjut", { ukuran: 17 }))
      : null);

  const el = h("div.masuk.materi-tata", {},
    kolom,

    h("div.materi-utama", {},
      // Kepala dipangkas. Yang dulu berdiri di sini: satu baris mata, judul,
      // lalu EMPAT pil dan dua tombol berteks penuh — dua ratus piksel
      // metadata sebelum kata pertama pelajaran. Tiga dari empat pil itu
      // ("6 bagian", "2 contoh kode", "belum tuntas") menjawab pertanyaan
      // yang belum ditanyakan siapa pun saat halaman baru dibuka; mereka
      // turun ke KAKI artikel, tempat pertanyaannya memang muncul. Yang
      // bertahan di atas cuma posisi — dan itu pun sekarang ikut dibawa strip
      // konteks yang menempel, jadi ia tidak pernah hilang saat digulir.
      h("header.kepala-besar.kepala-materi", {},
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
              : null),
          h("div.materi-alat", {},
            tombolBookmark(key, "materi", indeks, m.bookmark),
            tombolCatatan(m.kunci, m.catatan, m.judul)))),

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
    h("header.kepala-besar", {},
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
    return { el: h("aside.materi-peta.materi-peta-kosong"), bersihkan() {} };
  }

  const tautan = butir.map((x) => h("a", {
    href: "#",
    onclick: (e) => {
      e.preventDefault();
      const sasaran = artikel.children[x.i];
      if (sasaran) {
        sasaran.scrollIntoView({
          behavior: adaGerak() ? "smooth" : "auto", block: "start" });
      }
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
  let hentikan = () => {};
  if (typeof IntersectionObserver !== "undefined") {
    const pengamat = new IntersectionObserver(() => {
      let aktif = -1;
      butir.forEach((x, n) => {
        const anak = artikel.children[x.i];
        if (anak && anak.getBoundingClientRect().top <= window.innerHeight * 0.34) {
          aktif = n;
        }
      });
      tautan.forEach((a, n) => a.classList.toggle("kini", n === aktif));
    }, { rootMargin: "-30% 0px -55% 0px", threshold: [0, 1] });

    for (const x of butir) {
      const anak = artikel.children[x.i];
      if (anak) pengamat.observe(anak);
    }
    hentikan = () => pengamat.disconnect();
  }
  return { el, bersihkan: hentikan };
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
    return h("section", {},
      b.judul ? h("h3", {}, b.judul) : null,
      b.blok.map(blokProsa));
  }
  return blokKode(b, i, m, key, bhs, bersih);
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
      "Halaman contoh ini dibuatkan dari pemilih di CSS-mu sendiri — ",
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
 * tanda kurung kosong, tanda sama dengan berkutip, dan akhiran berkas.
 * Properti CSS telanjang seperti `color` atau `grid` TIDAK ikut — kata-kata
 * itu muncul sebagai kata biasa di kalimat Indonesia, dan menandainya sebagai
 * kode berarti menaruh kotak di tengah kalimat yang bukan kode.
 *
 * Hasilnya 1.123 chip di seluruh kurikulum, dan 87% blok prosa tidak
 * memilikinya sama sekali. Itu yang membuatnya jadi penanda: kalau setiap
 * paragraf punya, tidak ada yang punya.
 */
const POLA_KODE = new RegExp(
  "</?[a-zA-Z][\\w-]*\\s*/?>"                    // <tag> </tag> <br/>
  + "|\\b[a-zA-Z_][\\w.]*\\(\\)"                    // fungsi()
  + "|\\b[a-zA-Z-]+=\"[^\"]{1,30}\""              // atribut="nilai"
  + "|\\b[\\w-]+\\.(?:py|js|java|c|cpp|h|css|html|sql|sh|go|json|txt|md)\\b",
  "g");

/** Teks -> [string | <code>] siap dijadikan anak sebuah elemen. */
function berkode(teks) {
  const keluar = [];
  let akhir = 0;
  POLA_KODE.lastIndex = 0;
  let m;
  while ((m = POLA_KODE.exec(teks)) !== null) {
    if (m.index > akhir) keluar.push(teks.slice(akhir, m.index));
    keluar.push(h("code", {}, m[0]));
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
  return h(d.urut ? "ol" : "ul", {}, d.butir.map((x) =>
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
  const bisaJalan = p.bisa_dijalankan && bhs && bhs.siap;

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
        bahasa: bhs.runner,
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
      bahasa: m.sorot,
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

  return h("div.blok-kode", {},
    h("div.blok-kepala", {},
      p.nama ? h("span.berkas", {}, p.nama)
             : h("span", {}, b.judul || p.instruksi),
      h("span.lencana", {}, lencana),
      h("div.blok-alat", {},
        tblJalan, tblUbah, tblPulih,
        h("button.tbl.tbl-kecil.tbl-hantu", {
          onclick: (e) => salin(b.kode, "Kode disalin.", e.currentTarget),
        }, "Salin"),
        // Ruang Coba tetap ada, tapi tidak lagi jadi satu-satunya jalan: untuk
        // kerja yang lebih panjang (stdin, ganti bahasa, draf tersimpan) ia
        // punya yang tidak muat di sini.
        p.bisa_dijalankan ? h("a.tbl.tbl-kecil.tbl-hantu", {
          title: "Buka di Ruang Coba — layar penuh, bisa diberi masukan (stdin)",
          href: `#/coba?key=${key}&materi=${m.indeks}&bagian=${i}`,
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
    judul: "Catatan — " + judul,
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
      h("header.kepala-besar", {},
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
                     : h("a.pil" + pilTipe(x.tipe),
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
      h("header.kepala-besar", {},
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

export async function layarCari({ q, tipe }) {
  const kata = q || "";
  const saring = tipe || "semua";
  const hasil = kata.length >= 2
    ? (await api.ambil("/api/cari", { q: kata, tipe: saring })).hasil : [];

  const medan = h("input", {
    type: "text", value: kata, placeholder: "Cari di 11 bahasa sekaligus…",
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
    h("header.kepala-besar", {},
      h("span.mata", {}, "Pencarian"),
      h("h1", {}, "Cari"),
      h("p.kepala-sub", {}, "Menjangkau judul, isi materi, soal kuis, dan "
        + "solusi latihan di sebelas bahasa sekaligus.")),
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
                  r.cuplikan ? " — " : "",
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
