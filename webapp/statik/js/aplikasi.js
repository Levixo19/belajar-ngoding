/* Kerangka aplikasi: pemuatan awal, router, rel navigasi, palet perintah,
 * dan pintasan papan ketik.
 *
 * Router-nya berbasis fragmen URL (#/materi/java/3). Itu pilihan yang
 * disengaja: server ini menyajikan satu halaman dan sekumpulan endpoint JSON,
 * dan fragmen tidak pernah ikut terkirim ke server sama sekali. Akibatnya
 * menyenangkan — tombol Kembali browser bekerja, setiap layar punya alamat
 * yang bisa disimpan sebagai bookmark browser, dan memuat ulang halaman
 * mengembalikanmu ke tempat yang sama.
 *
 * Palet perintah (Ctrl+K) sengaja dibuat lebih dulu daripada menu apa pun.
 * Dengan 11 bahasa dan ratusan halaman isi, menelusuri rel satu per satu adalah
 * cara paling lambat untuk sampai ke tujuan yang sudah kamu tahu namanya.
 *
 * Titik masuk aplikasi: dimuat index.html sebagai <script type="module">.
 */

import {
  api, h, $, kosongkan, sorak, memuat, tunda, jendela, jendelaTerbuka,
  tutupJendelaKini, GalatApi,
} from "./inti.js";
import {
  masuk, keluar, masukBerurut, tata, angkaKe, denyut, saatGulir, pasangIsyarat,
  adaGerak, jepit, saatGerakBerubah,
} from "./gerak.js";
import { ikon } from "./ikon.js";
import { pasangAturan } from "./sorot.js";
import {
  layarDasbor, layarBahasa, layarMateri, layarCari, layarBookmark, layarCatatan,
} from "./layar-belajar.js";
import { layarKuis, layarLatihan, layarCoba } from "./layar-kerja.js";
import {
  layarStatistik, layarAtur, terapkanTampilan, temaBerikutnya, tampilkanBantuan,
} from "./layar-lain.js";

const LAYAR = {
  dasbor: layarDasbor,
  bahasa: layarBahasa,
  materi: layarMateri,
  kuis: layarKuis,
  latihan: layarLatihan,
  coba: layarCoba,
  cari: layarCari,
  bookmark: layarBookmark,
  catatan: layarCatatan,
  statistik: layarStatistik,
  atur: layarAtur,
};

// Layar yang butuh ruang penuh: editor lebih enak tanpa batas lebar, dan
// pembaca materi memakai tiga kolom (daftar materi, bacaan, peta halaman).
const LAYAR_LEBAR = new Set(["latihan", "coba", "materi"]);

const MENU_UTAMA = [
  ["dasbor", "dasbor", "Dasbor", "#/dasbor"],
  ["coba", "jalankan", "Ruang Coba", "#/coba"],
];
const MENU_KAKI = [
  ["catatan", "catatan", "Catatanku", "#/catatan"],
  ["bookmark", "bookmark", "Bookmark", "#/bookmark"],
  ["statistik", "statistik", "Statistik", "#/statistik"],
  ["atur", "atur", "Pengaturan", "#/atur"],
];

const ctx = {
  awal: null,
  /** Ingatan ringan antar layar: tab yang terakhir dibuka, draf ruang coba.
   *  Disimpan di localStorage supaya bertahan setelah halaman dimuat ulang —
   *  kode yang sedang dicoba-coba tidak boleh hilang cuma karena F5. */
  ingat(kunci, nilai) {
    const k = "belajar.ingat." + kunci;
    if (nilai === undefined) {
      try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; }
    }
    try { localStorage.setItem(k, JSON.stringify(nilai)); } catch (e) { /* penuh */ }
    return nilai;
  },
  segarkanUkuran,
};

let bersihLayar = null;
/* Penomoran permintaan gambar. Tanpa ini, dua klik cepat berturut-turut
   membuat dua gambarRute() berjalan bersamaan, dan yang datanya lebih lambat
   menimpa yang lebih cepat — sehingga layar yang tampil bukan yang terakhir
   diminta. Dengan animasi masuk-keluar, jendela terjadinya justru melebar,
   jadi penjaganya jadi wajib. */
let nomorGambar = 0;
let lepasGulir = null;

/* -------------------------------------------------------------------- rute */

function uraikanRute() {
  const mentah = location.hash.replace(/^#\/?/, "");
  const [jalur, kueri] = mentah.split("?");
  const bagian = jalur.split("/").filter(Boolean);
  const params = {};
  for (const [k, v] of new URLSearchParams(kueri || "")) params[k] = v;

  const nama = bagian[0] || "dasbor";
  if (bagian[1]) params.key = decodeURIComponent(bagian[1]);
  if (bagian[2]) params.indeks = decodeURIComponent(bagian[2]);
  return { nama: LAYAR[nama] ? nama : "dasbor", params };
}

/* Berapa lama menunggu sebelum menampilkan kerangka pemuatan.
 * Hampir semua layar di sini selesai jauh di bawah angka ini karena datanya
 * datang dari proses di komputer yang sama. Menampilkan kerangka lebih cepat
 * dari itu justru membuat perpindahan terasa lebih berat, bukan lebih cepat:
 * yang terlihat jadi tiga keadaan (lama -> kerangka -> baru) padahal dua sudah
 * cukup. */
const AMBANG_KERANGKA = 240;

async function gambarRute() {
  const { nama, params } = uraikanRute();
  const panggung = $("#layar");
  const giliran = ++nomorGambar;

  if (bersihLayar) { bersihLayar(); bersihLayar = null; }
  panggung.classList.toggle("lebar", LAYAR_LEBAR.has(nama));
  tandaiRel(nama, params.key);

  // Isi lama diberangkatkan lebih dulu, TAPI tidak ditunggu: permintaannya
  // jalan berbarengan. Di layar yang datanya cepat, keduanya selesai hampir
  // bersamaan dan yang terlihat cuma satu pergantian yang mulus.
  const isiLama = [...panggung.children];
  const pergi = isiLama.length ? keluar(isiLama).selesai : Promise.resolve();

  let kerangka = null;
  const timer = setTimeout(() => {
    if (giliran !== nomorGambar) return;
    kerangka = memuat();
    kosongkan(panggung).appendChild(kerangka);
    masuk(kerangka, { geser: 6 });
  }, AMBANG_KERANGKA);

  let hasil = null;
  let galat = null;
  try {
    hasil = await LAYAR[nama](params, ctx);
  } catch (e) {
    galat = e;
  }
  clearTimeout(timer);
  await pergi;
  // Rute sudah berganti lagi selama menunggu: buang hasil ini diam-diam.
  // Menempelkannya berarti menampilkan halaman yang sudah tidak diminta.
  if (giliran !== nomorGambar) {
    // Layar yang dibuang tetap sempat membangun DOM-nya, dan sebagian layar
    // memasang IntersectionObserver di situ (pembaca materi, misalnya).
    // Pembersihnya tidak akan pernah dipanggil lewat jalur biasa karena
    // layarnya tidak pernah ditempel — jadi panggil di sini.
    if (hasil && hasil.saatKeluar) hasil.saatKeluar();
    return;
  }

  kosongkan(panggung);
  if (galat) {
    const el = layarGagal(galat);
    panggung.appendChild(el);
    gambarJejak([{ label: "Tidak bisa dibuka" }]);
    masukLayar(el);
  } else {
    panggung.appendChild(hasil.el);
    bersihLayar = hasil.saatKeluar || null;
    document.title = (hasil.judul ? hasil.judul + " · " : "") + "Belajar Ngoding";
    gambarJejak(hasil.jejak || []);
    panggung.focus({ preventScroll: true });
    window.scrollTo(0, 0);
    masukLayar(hasil.el);
  }
  segarkanUkuran();
}

/** Masukkan isi layar baru.
 *
 *  Layar yang menandai dirinya `.masuk-urut` punya blok-blok setara yang
 *  masuk satu per satu; sisanya masuk sebagai satu kesatuan. Kelas `.masuk`
 *  dilepas lebih dulu karena gaya.css masih memakainya untuk blok yang muncul
 *  di TENGAH layar yang sudah berdiri — dan dua animasi masuk pada elemen yang
 *  sama akan saling menimpa. */
function masukLayar(el) {
  el.classList.remove("masuk");
  if (el.classList.contains("masuk-urut")) {
    masukBerurut([...el.children], { per: 42, maks: 260, geser: 12 });
    return;
  }
  masuk(el, { geser: 12 });
}

function layarGagal(e) {
  const serverMati = e instanceof GalatApi && e.kode === 0;
  return h("div.masuk", {},
    h("div.kepala", {}, h("div", {},
      h("span.mata", {}, "Gagal memuat"),
      h("h1", {}, serverMati ? "Server tidak menjawab"
                             : "Halaman tidak bisa dibuka"),
      h("p.sub", {}, e.message))),
    h("div.deret", {},
      h("button.tbl.tbl-utama", { onclick: () => gambarRute() }, "Coba lagi"),
      h("a.tbl.tbl-hantu", { href: "#/dasbor" }, "Ke dasbor")));
}

function gambarJejak(jejak) {
  const el = kosongkan($("#jejak"));
  el.appendChild(h("a.sembunyi-hp", { href: "#/dasbor" }, "Belajar"));
  for (const j of jejak) {
    el.appendChild(h("span.pisah", {}, "›"));
    el.appendChild(j.href ? h("a", { href: j.href }, j.label)
                          : h("span.kini", {}, j.label));
  }
}

/* --------------------------------------------------------------------- rel */

function bangunRel() {
  const utama = kosongkan($("#rel-utama"));
  for (const [nama, gambar, label, href] of MENU_UTAMA) {
    utama.appendChild(h("li", {}, h("a", { href, data: { layar: nama } },
      h("span.ikon", {}, ikon(gambar)), h("span.nama", {}, label))));
  }

  const bahasa = kosongkan($("#rel-bahasa"));
  for (const b of ctx.awal.bahasa) {
    bahasa.appendChild(h("li", {}, h("a", {
      href: "#/bahasa/" + b.key,
      data: { layar: "bahasa", key: b.key },
      kelas: b.siap ? "" : "mati",
      title: b.siap ? "" : `Kode ${b.label} belum bisa dijalankan: butuh `
                           + b.hilang.join(", "),
    },
      h("span.nama", {}, b.label),
      h("span.rel-persen", {}, Math.round(b.persen) + "%"))));
  }

  const kaki = kosongkan($("#rel-kaki"));
  for (const [nama, gambar, label, href] of MENU_KAKI) {
    kaki.appendChild(h("li", {}, h("a", { href, data: { layar: nama } },
      h("span.ikon", {}, ikon(gambar)), h("span.nama", {}, label))));
  }
}

/* Tinggi penanda posisi di rel — sama dengan ::before yang digantikannya. */
const TINGGI_TANDA = 19;

function tandaiRel(nama, key) {
  let aktif = null;
  for (const a of document.querySelectorAll("#rel .rel-menu a")) {
    const langsung = a.dataset.layar === nama
      && (!a.dataset.key || a.dataset.key === key);
    // Materi, kuis, dan latihan adalah anak dari sebuah bahasa: rel harus
    // tetap menunjukkan bahasa mana yang sedang dibuka.
    const anak = ["materi", "kuis", "latihan"].includes(nama)
      && a.dataset.layar === "bahasa" && a.dataset.key === key;
    const kini = langsung || anak;
    a.classList.toggle("kini", kini);
    if (kini) aktif = a;
  }
  pindahkanTanda(aktif);
  if (window.innerWidth <= 820) $("#cangkang").classList.remove("rel-buka");
}

/** Geser penanda posisi ke butir menu yang sedang aktif.
 *
 *  Meluncur, bukan padam-lalu-menyala di tempat lain. Perpindahan yang
 *  terlihat itulah yang membuat rel terbaca sebagai satu daftar utuh: mata
 *  mengikuti garisnya dan jadi tahu SEBERAPA JAUH ia berpindah, bukan cuma
 *  bahwa ia berpindah. */
function pindahkanTanda(aktif) {
  const rel = $("#rel");
  const tanda = $(".rel-tanda", rel);
  if (!tanda) return;

  if (!aktif) {
    tanda.style.opacity = "0";
    rel.classList.remove("pakai-tanda");
    return;
  }
  rel.classList.add("pakai-tanda");

  const pasang = () => {
    tanda.style.top =
      (aktif.offsetTop + (aktif.offsetHeight - TINGGI_TANDA) / 2) + "px";
    tanda.style.height = TINGGI_TANDA + "px";
    tanda.style.opacity = "1";
  };

  // Kemunculan pertama tidak dianimasikan: meluncur dari sudut kiri atas
  // halaman saat aplikasi baru dibuka bukan perpindahan, cuma keramaian.
  if (tanda.style.opacity !== "1" || !adaGerak()) { pasang(); return; }
  tata(tanda, pasang, { pegas: "jawab" });
}

/* ------------------------------------------------------------------ ukuran */

let xpTerakhir = null;

async function segarkanUkuran() {
  try {
    const d = await api.ambil("/api/dasbor");

    const streak = $("#tanda-streak");
    const streakAngka = streak.querySelector(".tanda-angka");
    const streakNaik = Number(streakAngka.textContent) < d.streak;
    angkaKe(streakAngka, d.streak);
    streak.classList.toggle("menyala", d.streak > 0);
    streak.title = d.streak
      ? `Streak ${d.streak} hari berjalan · rekor ${d.streak_rekor} hari`
      : "Streak terputus. Kerjakan satu hal apa pun hari ini untuk memulai lagi.";
    if (streakNaik && xpTerakhir !== null) denyut(streak);

    const xp = $("#tanda-xp");
    // Angka XP berjalan naik, tidak melompat. Ini salah satu dari sedikit
    // animasi di aplikasi ini yang benar-benar MENYAMPAIKAN sesuatu: melihat
    // 43 merangkak jadi 68 memberi tahu berapa yang barusan didapat, dan
    // angka yang berganti begitu saja tidak pernah bisa.
    angkaKe(xp.querySelector(".tanda-angka"), d.xp);
    if (xpTerakhir !== null && d.xp > xpTerakhir) denyut(xp);
    xpTerakhir = d.xp;
    xp.title = `Level ${d.level} — ${d.gelar} · ${d.xp_hari_ini} dari `
      + `${d.target_harian} XP hari ini`;

    for (const b of d.bahasa) {
      const a = document.querySelector(`#rel-bahasa a[data-key="${b.key}"]`);
      if (a) {
        angkaKe(a.querySelector(".rel-persen"), b.persen,
                { format: (n) => Math.round(n) + "%" });
      }
    }
  } catch (e) { /* ukuran cuma hiasan; kegagalannya tak boleh mengganggu */ }
}

/** Ganti karakter Unicode di bilah atas dan tombol pencarian dengan ikon
 *  garis yang sama keluarganya dengan sisa aplikasi.
 *
 *  Ditulis di sini, bukan langsung di index.html, karena ikonnya berupa SVG
 *  yang dibangun dari JS — dan menaruh dua puluh baris <svg> mentah di dalam
 *  HTML akan membuat kerangka halamannya jauh lebih sulit dibaca daripada
 *  gunanya. */
function pasangIkonBilah() {
  const pasang = (sel, nama, ukuran = 20) => {
    const el = $(sel);
    if (!el) return;
    const gambar = ikon(nama, { ukuran });
    if (gambar) kosongkan(el).appendChild(gambar);
  };
  pasang("#rel-alih", "panel");
  pasang("#tombol-tema", "tema");
  pasang("#tombol-bantuan", "bantuan");
  const cari = $(".rel-tombol .ikon");
  if (cari) kosongkan(cari).appendChild(ikon("cari", { ukuran: 18 }));
}

/* ------------------------------------------------------------- maju baca */

/** Garis tipis di bawah bilah atas yang mengikuti posisi gulir.
 *
 *  Hanya muncul kalau halamannya memang panjang: di layar yang muat sekali
 *  lihat, ia akan selalu penuh dan cuma jadi garis hiasan yang membingungkan. */
function pasangMajuBaca() {
  const garis = $("#maju-baca");
  if (!garis) return;
  if (lepasGulir) lepasGulir();
  lepasGulir = saatGulir(({ maju }) => {
    const bisaDigulir =
      document.documentElement.scrollHeight - window.innerHeight;
    garis.classList.toggle("tampak", bisaDigulir > 260);
    garis.style.transform = `scaleX(${jepit(maju).toFixed(4)})`;
  });
}

/* ------------------------------------------------------------------- palet */

function daftarPerintah() {
  const daftar = [
    { label: "Dasbor", ket: "Ringkasan dan langkah berikutnya", href: "#/dasbor" },
    { label: "Ruang Coba", ket: "Jalankan kode apa saja", href: "#/coba" },
    { label: "Catatanku", ket: "Semua catatan pribadimu", href: "#/catatan" },
    { label: "Bookmark", ket: "Halaman yang kamu tandai", href: "#/bookmark" },
    { label: "Statistik", ket: "XP, badge, toolchain", href: "#/statistik" },
    { label: "Pengaturan", ket: "Tema, target harian, data", href: "#/atur" },
  ];
  for (const b of ctx.awal.bahasa) {
    daftar.push({
      label: b.label,
      ket: `${b.materi} materi · ${b.kuis} kuis · ${b.latihan} latihan`,
      href: "#/bahasa/" + b.key,
      tipe: "bahasa",
    });
  }
  return daftar;
}

function saringPerintah(daftar, kata) {
  if (!kata) return daftar;
  const k = kata.toLowerCase();
  return daftar.filter(
    (d) => (d.label + " " + (d.ket || "")).toLowerCase().includes(k));
}

function bukaPalet() {
  const perintah = daftarPerintah();
  const medan = h("input.palet-cari", {
    type: "text",
    placeholder: "Ke mana? Ketik nama bahasa, materi, atau apa pun…",
    "aria-label": "Cari perintah atau isi",
  });
  const hasil = h("div.palet-hasil");
  let pilihan = 0;
  let baris = [];

  function sorotPilihan() {
    hasil.querySelectorAll(".palet-item").forEach((el, i) => {
      el.classList.toggle("pilih", i === pilihan);
      if (i === pilihan) el.scrollIntoView({ block: "nearest" });
    });
  }

  function buka(d) {
    tutupJendelaKini();
    location.hash = d.href;
  }

  function gambar(daftar) {
    baris = daftar;
    pilihan = 0;
    hasil.replaceChildren(...(daftar.length
      ? daftar.map((d, i) => h("button.palet-item", {
          onclick: () => buka(d),
          onmousemove: () => { pilihan = i; sorotPilihan(); },
        },
          h("span.pil" + (d.tipe === "kuis" ? ".pil-ungu"
            : d.tipe === "latihan" ? ".pil-nyala"
            : d.tipe === "materi" ? ".pil-tenang" : ""), {}, d.tipe || "buka"),
          h("div.isi", {},
            h("div.judul", {}, d.label),
            d.ket ? h("div.cuplik", {}, d.ket) : null)))
      : [h("div", { gaya: { padding: "22px", textAlign: "center",
                            color: "var(--redup)" } },
          "Tidak ada yang cocok.")]));
    sorotPilihan();
    // Hanya sepuluh teratas yang dianimasikan. Sisanya ada di bawah lipatan
    // layar, dan menganimasikan yang tidak terlihat cuma membuang tenaga
    // sambil memperpanjang urutannya.
    masukBerurut([...hasil.children].slice(0, 10),
                 { per: 22, maks: 130, geser: 6, pegas: "jawab" });
  }

  const cariIsi = tunda(async (kata) => {
    if (kata.length < 2) return;
    try {
      const r = await api.ambil("/api/cari", { q: kata });
      // Perintah tetap di atas: kalau kamu mengetik "python", yang kamu maksud
      // hampir pasti bahasanya — bukan salah satu dari puluhan materi yang
      // kebetulan menyebut kata itu.
      gambar([...saringPerintah(perintah, kata),
              ...r.hasil.slice(0, 40).map((x) => ({
                label: `${x.label_bahasa} — ${x.judul}`,
                ket: x.cuplikan,
                tipe: x.tipe,
                href: `#/${x.tipe}/${x.bahasa}/${x.indeks}`,
              }))]);
    } catch (e) { /* biarkan hasil perintah yang sudah tampil */ }
  }, 220);

  medan.addEventListener("input", () => {
    const kata = medan.value.trim();
    gambar(saringPerintah(perintah, kata));
    cariIsi(kata);
  });

  medan.addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown" || (e.ctrlKey && e.key === "n")) {
      e.preventDefault();
      pilihan = Math.min(pilihan + 1, baris.length - 1);
      sorotPilihan();
    } else if (e.key === "ArrowUp" || (e.ctrlKey && e.key === "p")) {
      e.preventDefault();
      pilihan = Math.max(pilihan - 1, 0);
      sorotPilihan();
    } else if (e.key === "Enter" && baris[pilihan]) {
      e.preventDefault();
      buka(baris[pilihan]);
    }
  });

  gambar(perintah);

  return jendela({
    isi: h("div", {}, medan, hasil,
      h("div.palet-kaki", {},
        h("span", {}, h("kbd", {}, "↑↓"), " pilih"),
        h("span", {}, h("kbd", {}, "⏎"), " buka"),
        h("span", {}, h("kbd", {}, "Esc"), " tutup"))),
    saatBuka: () => medan.focus(),
  });
}

/* ---------------------------------------------------------------- pintasan */

let tombolG = false;

function alihRel() {
  const cangkang = $("#cangkang");
  if (window.innerWidth <= 820) cangkang.classList.toggle("rel-buka");
  else cangkang.classList.toggle("rel-tutup");
}

/** Ganti tema tanpa kedipan.
 *
 *  Mengganti nilai variabel CSS mengubah puluhan warna dalam satu frame, dan
 *  pergantian mendadak seluruh layar persis apa yang dilarang aturan gerak di
 *  gaya.css. Kelas `alih-tema` memberi transisi warna 260 md ke semuanya, lalu
 *  dilepas lagi — kalau dibiarkan menempel, setiap :hover sesudahnya ikut jadi
 *  lengket. */
let lepasTema = 0;

export function gantiTema() {
  const akar = document.documentElement;
  if (adaGerak()) {
    akar.classList.add("alih-tema");
    clearTimeout(lepasTema);
    lepasTema = setTimeout(() => akar.classList.remove("alih-tema"), 320);
  }
  sorak("Tema: " + temaBerikutnya(), "", 1.6);
}

function pasangPintasan() {
  document.addEventListener("keydown", (e) => {
    // `instanceof Element` bukan kehati-hatian berlebihan: sasaran keydown
    // tidak selalu elemen (bisa document itu sendiri), dan memanggil
    // .matches() di atasnya melempar TypeError yang membunuh SELURUH
    // penanganan pintasan tanpa satu pun pesan.
    const diMedan = e.target instanceof Element
      && e.target.matches("input, textarea, select");

    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      if (!jendelaTerbuka()) bukaPalet();
      return;
    }
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "b" && !diMedan) {
      e.preventDefault();
      alihRel();
      return;
    }
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "j") {
      e.preventDefault();
      gantiTema();
      return;
    }
    if (diMedan || e.ctrlKey || e.metaKey || e.altKey) return;
    // Dialog yang terbuka menahan SEMUA pintasan satu huruf. Tanpa ini,
    // menekan G lalu D sambil membaca dialog "Lihat jawaban" memindahkan
    // halaman di belakangnya ke dasbor, dan dialognya tertinggal menggantung
    // di atas layar yang sudah bukan miliknya.
    if (jendelaTerbuka()) return;

    if (e.key === "?") {
      e.preventDefault();
      tampilkanBantuan();
      return;
    }
    // Rangkaian ala Vim: G lalu satu huruf. Aman karena hanya aktif di luar
    // medan isian, jadi tidak pernah bertabrakan dengan pengetikan.
    if (e.key.toLowerCase() === "g") {
      tombolG = true;
      setTimeout(() => { tombolG = false; }, 900);
      return;
    }
    if (tombolG) {
      const tujuan = { d: "#/dasbor", c: "#/coba", s: "#/statistik",
                       b: "#/bookmark", n: "#/catatan", p: "#/atur" };
      const ke = tujuan[e.key.toLowerCase()];
      tombolG = false;
      if (ke) { e.preventDefault(); location.hash = ke; }
    }
  });
}

/* ------------------------------------------------------------------- mulai */

async function mulai() {
  terapkanTampilan();

  try {
    ctx.awal = await api.ambil("/api/awal");
  } catch (e) {
    document.body.replaceChildren(h("div.tanpa-js", {},
      h("h1", {}, "Tidak bisa menghubungi server"),
      h("p", {}, e.message),
      h("p", {}, "Jalankan lagi dengan: ",
        h("code", {}, "python3 belajar-web.py"))));
    return;
  }

  pasangAturan(ctx.awal.aturan_sorot);
  bangunRel();
  pasangPintasan();

  pasangIsyarat();
  pasangMajuBaca();
  pasangIkonBilah();

  $("#rel-alih").addEventListener("click", alihRel);
  $("#tombol-tema").addEventListener("click", gantiTema);
  $("#tombol-bantuan").addEventListener("click", tampilkanBantuan);
  $("#tanda-xp").addEventListener("click",
    () => { location.hash = "#/statistik"; });
  $("#tanda-streak").addEventListener("click",
    () => { location.hash = "#/statistik"; });
  $(".rel-tombol[data-buka='palet']").addEventListener("click", bukaPalet);

  // Setiap kali progres berubah, angka di bilah atas ikut menyesuaikan tanpa
  // perlu memuat ulang halaman.
  document.addEventListener("progres-berubah", () => segarkanUkuran());

  window.addEventListener("hashchange", gambarRute);

  // Penanda rel dipatok dalam piksel, jadi ia harus dihitung ulang setiap kali
  // rel berubah tinggi atau lebar — termasuk saat panelnya disembunyikan.
  window.addEventListener("resize", tunda(() => {
    const { nama, params } = uraikanRute();
    tandaiRel(nama, params.key);
  }, 160));

  // Setelan "kurangi gerak" di sistem bisa diubah di tengah sesi. Kalau itu
  // terjadi, penanda rel harus berhenti meluncur mulai detik itu juga.
  saatGerakBerubah(() => {
    const { nama, params } = uraikanRute();
    tandaiRel(nama, params.key);
  });

  // Kerangka aplikasinya muncul dengan satu gerakan pendek sesudah data awal
  // tiba. Yang dianimasikan cuma KEMUNCULANNYA — keadaan bawaan #cangkang
  // tetap terlihat, jadi kegagalan apa pun di sini tidak pernah menyisakan
  // halaman kosong.
  masuk($("#cangkang"), { geser: 0, zum: 0.994, durasi: 260 });
  await gambarRute();
}

mulai();
