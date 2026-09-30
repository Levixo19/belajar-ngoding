/* Kerangka aplikasi: pemuatan awal, router, rel navigasi, strip konteks,
 * palet perintah, dan pintasan papan ketik.
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
  api, h, isikan, $, kosongkan, sorak, memuat, tunda, jendela, jendelaTerbuka,
  tutupJendelaKini, bilah, keadaan, GalatApi,
} from "./inti.js";
import {
  masuk, keluar, masukBerurut, tata, angkaKe, denyut, saatGulir, pasangIsyarat,
  adaGerak, gerakPenuh, jepit, saatGerakBerubah, terbitkanKurva, vt,
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

// Layar yang butuh ruang penuh: pembaca materi memakai tiga kolom, dan editor
// lebih enak tanpa batas lebar.
const LAYAR_LEBAR = new Set(["latihan", "coba", "materi"]);
// Layar yang mengisi TINGGI jendela alih-alih tumbuh dari isinya: dua layar
// tempat orang MENULIS KODE. Editor yang setinggi isinya berarti kerangka tiga
// baris menyisakan empat ratus piksel kosong di bawahnya — ruang kerja yang
// menolak dipakai bekerja. Keduanya memakai tata letak yang sama persis
// (.kerja), karena gunanya memang sama dan dua bentuk berbeda untuk satu
// pekerjaan berarti dua bentuk yang harus dipelajari.
//
// Aturan tingginya sendiri baru menyala di container yang cukup lebar (lihat
// gaya.css) — di ponsel, bentuk yang benar tetap satu kolom yang digulir biasa.
const LAYAR_PENUH = new Set(["latihan", "coba"]);

// Layar yang isinya pada dasarnya SATU kolom daftar, dan karena itu memakai
// ukuran halaman yang lebih sempit (lihat `#layar.kolom` di gaya.css). Yang
// TIDAK ada di sini cuma dua: dasbor, yang memang dua kolom, dan tiga layar
// di LAYAR_LEBAR di atas.
//
// Alasannya bukan kelapangan. Daftar satu kolom yang dipaksa selebar 1164 px
// menaruh judul materi di tepi kiri dan penanda miliknya di tepi kanan dengan
// delapan ratus piksel kosong di antaranya — dan dua ujung yang sejauh itu
// berhenti terbaca sebagai satu baris.
const LAYAR_KOLOM = new Set([
  "bahasa", "kuis", "bookmark", "catatan", "cari", "statistik", "atur",
]);

// Ambang layar sempit. ANGKA INI DIPAKAI JUGA DI gaya.css (blok @media 860px)
// untuk memutuskan apakah navigasinya berbentuk baris atau panel. Dua tempat
// yang harus tetap cocok: kalau berubah di sini, ubah juga di sana — kalau
// tidak, tombol menu berhenti berbuat apa-apa tepat di pita lebar tempat
// panelnya justru satu-satunya jalan ke menu.
const AMBANG_PANEL = 860;

const MENU_UTAMA = [
  ["dasbor", "dasbor", "Dasbor", "#/dasbor"],
  ["coba", "jalankan", "Ruang Coba", "#/coba"],
];
const MENU_LAIN = [
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

/* URUTAN PERGANTIAN LAYAR — DIWARISI S05/S06, JANGAN DISUSUN ULANG PER LAYAR.
 *
 * View Transitions belum dipasang di sini; bentuknya sudah ditetapkan.
 *
 * Yang perlu dipahami lebih dulu: pohon pseudo VT SELALU berisi RASTER —
 * potret keadaan lama dan potret keadaan baru. Tidak ada satu pun bagiannya
 * yang merupakan DOM hidup. Selama sebuah grup beranimasi, DOM hidup di
 * bawahnya TERTUTUP oleh overlay grup itu.
 *
 * Root dijadikan no-op —
 *
 *   ::view-transition-group(root),
 *   ::view-transition-old(root),
 *   ::view-transition-new(root) { animation: none; }
 *
 * — dan yang membuatnya bekerja BUKAN "potret barunya hidup", melainkan
 * durasi grup root menjadi 0s sehingga overlay-nya dilepas seketika. Sesudah
 * dilepas, isi layar kembali jadi DOM sungguhan dan masukBerurut() berjalan
 * normal dari t=0.
 *
 * Grup yang masih beranimasi hanyalah yang diberi `view-transition-name`, dan
 * selama animasinya elemen itu terwakili raster, bukan dirinya sendiri. Maka
 * mengeluarkannya dari stagger adalah KEHARUSAN, bukan pilihan gaya:
 * menganimasikan DOM yang sedang tertutup raster berarti menggerakkan sesuatu
 * yang tidak terlihat, lalu ia melompat ke keadaan akhirnya saat overlay
 * dilepas.
 *
 * Empat langkah, pada urutan ini:
 *
 *   1. await keluar() pada DOM hidup — seperti sekarang, jangan diubah.
 *   2. vt(() => pasang DOM baru) — dengan root no-op, jadi VT tidak pernah
 *      menyilangkan seluruh layar.
 *   3. masuk() + masukBerurut() pada DOM hidup, TANPA menyentuh elemen yang
 *      punya `view-transition-name`.
 *   4. pasangUkuran() tetap dipanggil dua kali pada urutan yang sama; layar
 *      lama tidak boleh ditata ulang ke lebar layar baru sebelum memudar.
 *
 * Satu elemen tidak boleh punya `view-transition-name` DAN digerakkan tata()
 * sekaligus — penanda rel (.rel-tanda) adalah kasus yang paling mungkin
 * melanggarnya. Kalau itu terjadi, pilih salah satu; jangan dua-duanya. */
async function gambarRute({ pindahFokus = true } = {}) {
  const { nama, params } = uraikanRute();
  const panggung = $("#layar");
  const giliran = ++nomorGambar;

  if (bersihLayar) { bersihLayar(); bersihLayar = null; }
  // Navigasi menyala SEKARANG: ia umpan balik atas klik barusan, dan umpan
  // balik yang menunggu data datang tidak lagi terbaca sebagai jawaban.
  tandaiRel(nama, params.key);

  /* Ukuran halaman baru dipasang bersama ISI yang baru, tidak sebelumnya.
     Ada tiga ukuran (lihat LAYAR_LEBAR / LAYAR_KOLOM di atas), dan menyetelnya
     di awal berarti layar LAMA — yang masih terlihat, masih memudar —
     ditata ulang ke lebar layar berikutnya lebih dulu. Yang terlihat bukan
     pergantian melainkan isi lama yang melompat melebar atau menyempit tepat
     sebelum hilang, dan lompatan itu justru paling besar di perpindahan yang
     paling sering dilakukan: dari halaman bahasa (960 px) ke ruang kerja
     latihan (penuh). */
  const pasangUkuran = () => {
    panggung.classList.toggle("lebar", LAYAR_LEBAR.has(nama));
    panggung.classList.toggle("kolom", LAYAR_KOLOM.has(nama));
    panggung.classList.toggle("penuh", LAYAR_PENUH.has(nama));
  };

  // Isi lama diberangkatkan lebih dulu, TAPI tidak ditunggu: permintaannya
  // jalan berbarengan. Di layar yang datanya cepat, keduanya selesai hampir
  // bersamaan dan yang terlihat cuma satu pergantian yang mulus.
  const isiLama = [...panggung.children];
  const pergi = isiLama.length ? keluar(isiLama).selesai : Promise.resolve();

  let kerangka = null;
  const timer = setTimeout(() => {
    if (giliran !== nomorGambar) return;
    kerangka = memuat();
    kosongkan(panggung);
    // Kerangka pemuatan sudah termasuk isi yang baru: ia berdiri di ukuran
    // halaman tujuan, bukan di ukuran halaman yang barusan ditinggalkan.
    pasangUkuran();
    panggung.appendChild(kerangka);
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
  pasangUkuran();
  if (galat) {
    const el = layarGagal(galat);
    panggung.appendChild(el);
    // Gerbang yang SAMA berlaku di sini, dan alasannya juga sama: layar
    // kegagalan pun harus diumumkan pembaca layar — justru pada saat orangnya
    // paling perlu tahu apa yang terjadi. Tanpa baris ini, "Coba lagi" yang
    // gagal lagi meninggalkan fokus di `body` dan tidak ada yang mengabarkan
    // apa pun.
    if (pindahFokus) panggung.focus({ preventScroll: true });
    gambarKonteks(null);
    masukLayar(el);
  } else {
    panggung.appendChild(hasil.el);
    bersihLayar = hasil.saatKeluar || null;
    document.title = (hasil.judul ? hasil.judul + " · " : "") + "Belajar Ngoding";
    gambarKonteks(hasil.konteks || null);
    /* Fokus pindah ke panggung di setiap navigasi, dan itu memang benar: ia
       yang membuat pembaca layar mengumumkan layar baru alih-alih diam. Yang
       TIDAK benar melakukannya pada render BOOT, dan bedanya bukan kerapian —
       Chrome memulai navigasi fokus berurutan dari elemen TERAKHIR yang
       difokuskan, bukan dari kepala dokumen. Memfokuskan panggung saat memuat
       memindahkan titik mula Tab ke tengah dokumen, dan `#lompat-isi` — butir
       fokus PERTAMA dokumen (`index.html:24`) — baru tercapai sesudah menab
       seluruh halaman lalu memutar balik: terukur 32 tekan di `#/atur`.
       Jumlah ini bergantung konfigurasi (saklar "buka semua bab", dan lebar
       rail pada 1100 px); yang TIDAK bergantung apa pun ialah angka SESUDAH:
       1 tekan, di semua rute.

       Karena itu gerbangnya sebuah parameter, BUKAN penghapusan panggilannya:
       yang boot mengoper `false` sekali, dan setiap navigasi sesudahnya
       memakai default `true` sehingga pengumumannya tetap hidup. Sebuah
       `hashchange` mengoper Event, dan Event tidak punya properti
       `pindahFokus` — jadi di sana pun yang berlaku default itu. */
    if (pindahFokus) panggung.focus({ preventScroll: true });
    // Gulir balik ke atas dilakukan TANPA animasi, apa pun setelan geraknya.
    // Ini bukan gerak yang menyampaikan sesuatu — halamannya sudah berganti —
    // dan gulir mulus sejauh dua ribu piksel berarti isi baru yang sudah
    // terpasang tetap tak terlihat selama hampir satu detik. Lebih buruk lagi,
    // ia sempat ditabrak scrollIntoView milik layar berikutnya, dan yang
    // tertinggal halaman yang berhenti entah di mana di tengah teks.
    window.scrollTo({ top: 0, behavior: "instant" });
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
    h("header.kepala-besar", {},
      h("span.mata", {}, "Gagal memuat"),
      h("h1", {}, serverMati ? "Server tidak menjawab"
                             : "Halaman tidak bisa dibuka")),
    keadaan({
      jenis: "salah",
      gambar: "belum",
      judul: e.message,
      ket: serverMati
        ? "Jendela terminal tempat `python3 belajar-web.py` berjalan mungkin "
          + "sudah ditutup. Nyalakan lagi, lalu tekan Coba lagi."
        : "Halaman ini tidak bisa diambil dari server.",
      aksi: [
        h("button.tbl.tbl-utama", { onclick: () => gambarRute() }, "Coba lagi"),
        h("a.tbl.tbl-hantu", { href: "#/dasbor" }, "Ke dasbor"),
      ],
    }));
}

/* --------------------------------------------------------- strip konteks
 *
 * Pengganti remah roti. Yang membedakan keduanya bukan bentuk melainkan ISI:
 * remah roti mengulang judul halaman, sedangkan strip ini membawa empat hal
 * yang TIDAK ada di halamannya sendiri — bab mana yang sedang dijalani, posisi
 * ke berapa dari berapa, seberapa jauh bab itu, dan satu langkah ke depan.
 *
 * Layar yang tidak punya konteks (dasbor, statistik, pengaturan) memanggilnya
 * dengan null, dan stripnya tidak dirender sama sekali — 44 piksel itu kembali
 * jadi milik isinya. */

function gambarKonteks(k) {
  const el = $("#konteks");
  const panggung = $("#panggung");
  if (!k) {
    el.hidden = true;
    kosongkan(el);
    panggung.classList.remove("berkonteks");
    return;
  }

  // Tombol langkah yang tidak punya tujuan tetap DIGAMBAR, sebagai <span>
  // redup. Melepasnya dari DOM akan mengubah lebar strip tiap kali pindah
  // materi, dan pergeseran sepuluh piksel di bilah yang menempel terbaca
  // sebagai halaman yang goyang — bukan sebagai tombol yang tidak ada.
  const langkah = (arah, href, judul) => {
    const gambar = ikon(arah === "sebelum" ? "kembali" : "lanjut", { ukuran: 18 });
    return href
      ? h("a", { href, title: judul || "", "aria-label": judul || arah }, gambar)
      : h("span", { "aria-hidden": "true" }, gambar);
  };

  isikan(el,
    h("a.konteks-balik", { href: k.balik.href },
      ikon("kembali", { ukuran: 16 }), k.balik.label),

    h("div.konteks-tengah", {},
      k.bab ? h("span.konteks-bab", {}, k.bab) : null,
      k.judul ? h("span.konteks-judul", {}, k.judul) : null),

    k.posisi || k.persen !== undefined
      ? h("div.konteks-maju", {},
          k.posisi ? h("span.konteks-angka", {}, k.posisi) : null,
          k.persen !== undefined ? bilah(k.persen, "", { diam: true }) : null)
      : null,

    k.langkah
      ? h("div.konteks-langkah", {},
          langkah("sebelum", k.sebelum, k.judul_sebelum),
          langkah("sesudah", k.sesudah, k.judul_sesudah))
      : null);

  el.hidden = false;
  panggung.classList.add("berkonteks");
}

/* --------------------------------------------------------------------- rel */

function butirMenu(nama, gambar, label, href) {
  return h("li", {}, h("a", { href, data: { layar: nama } },
    h("span.ikon", {}, ikon(gambar)), h("span.nama", {}, label)));
}

function bangunRel() {
  const utama = kosongkan($("#rel-utama"));
  for (const [nama, gambar, label, href] of MENU_UTAMA) {
    utama.appendChild(butirMenu(nama, gambar, label, href));
  }

  /* Daftar ini tumbuh dari sebelas jadi sembilan belas butir. Satu kolom datar
     sepanjang itu berarti 42% isinya ada di bawah lipatan panel dan harus
     diburu dengan menggulir. Dua hal yang memperbaikinya, dan keduanya
     struktural, bukan kosmetik:

     1. Bahasa dirender dua kolom (CSS), jadi tujuh belas butir muat utuh.
     2. Kurikulum yang BUKAN bahasa pemrograman dipisah di bawah judulnya
        sendiri. "Bikin Aplikasi" dan "CLI Fedora" mengajarkan cara berpikir
        dan cara mengoperasikan sistem; menaruhnya berbaris di antara Rust dan
        Kotlin membuat pelajar mengira keduanya bahasa yang belum ia kenal.

     Penandanya datang dari `b.tematik` (asalnya LANGUAGES di main.py), bukan
     dari mencocokkan label di sini. */
  const butirBahasa = (b) => h("li", {}, h("a", {
    href: "#/bahasa/" + b.key,
    data: { layar: "bahasa", key: b.key },
    kelas: b.siap ? "" : "mati",
    title: b.siap ? "" : `Kode ${b.label} belum bisa dijalankan: butuh `
                         + b.hilang.join(", "),
  },
    h("span.nama", {}, b.label),
    h("span.rel-persen", {}, Math.round(b.persen) + "%")));

  const bahasa = kosongkan($("#rel-bahasa"));
  for (const b of ctx.awal.bahasa.filter((x) => !x.tematik)) {
    bahasa.appendChild(butirBahasa(b));
  }

  const tematik = ctx.awal.bahasa.filter((x) => x.tematik);
  const kotakTematik = $("#rel-tematik");
  kotakTematik.hidden = tematik.length === 0;
  const daftarTematik = kosongkan($("#rel-tematik-daftar"));
  for (const b of tematik) {
    daftarTematik.appendChild(butirBahasa(b));
  }

  const lain = kosongkan($("#rel-kaki"));
  for (const [nama, gambar, label, href] of MENU_LAIN) {
    lain.appendChild(butirMenu(nama, gambar, label, href));
  }
}

/* Seberapa jauh penanda mendatar menjorok ke dalam dari tepi butir menu, di
   tiap sisi. Angkanya menyamai `left/right: 22%` pada ::before yang
   digantikannya. */
const SISIP_TANDA = 0.22;

/** Tandai di mana pemakainya sedang berada.
 *
 *  Dua hal yang gampang dianggap satu padahal bukan:
 *
 *  1. `aria-current="page"` adalah SATU-SATUNYA penanda posisi yang sampai ke
 *     pembaca layar. Kelas `.kini` cuma mengubah warna, dan warna tidak pernah
 *     dibacakan.
 *
 *  2. Butir aktif tidak selalu terlihat. Tujuh belas dari sembilan belas
 *     sasaran navigasi di sini tinggal di dalam panel yang tertutup —
 *     SELURUH sebelas bahasa, plus Statistik, Bookmark, Catatanku, dan
 *     Pengaturan. Untuk butir seperti itu penanda yang meluncur tidak punya
 *     tempat berdiri (`offsetWidth` nol), jadi versi sebelumnya
 *     memadamkannya. Akibatnya di halaman bahasa — tujuan yang paling sering
 *     dibuka di aplikasi ini — navigasi berhenti menjawab "aku di mana" sama
 *     sekali: tidak ada satu butir pun yang menyala. Yang benar bukan
 *     memadamkan penandanya melainkan memindahkannya ke PEMICU panel tempat
 *     butir itu tinggal. Panel boleh tertutup; tombolnya tetap di layar, dan
 *     tombol itu memang jalan menuju halaman yang sedang dibuka. */
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
    if (kini) a.setAttribute("aria-current", "page");
    else a.removeAttribute("aria-current");
    if (kini) aktif = a;
  }

  // Pemicu panel yang MEMUAT butir aktif ikut ditandai; penandanya berdiri di
  // situ selama butir aslinya belum punya lebar.
  let pengganti = null;
  for (const turun of document.querySelectorAll("#rel .rel-turun")) {
    const pemicu = $(".rel-pemicu", turun);
    if (!pemicu) continue;
    const memuat = aktif !== null && turun.contains(aktif);
    pemicu.classList.toggle("kini", memuat);
    // Bukan "page": pemicunya sendiri bukan halaman, ia jalan MENUJU halaman
    // yang sedang dibuka. `true` nilai yang tepat untuk hubungan itu.
    if (memuat) pemicu.setAttribute("aria-current", "true");
    else pemicu.removeAttribute("aria-current");
    if (memuat && !aktif.offsetWidth) pengganti = pemicu;
  }

  pindahkanTanda(pengganti || aktif);
  if (window.innerWidth <= AMBANG_PANEL) $("#cangkang").classList.remove("rel-buka");
}

/** Geser penanda posisi ke butir menu yang sedang aktif.
 *
 *  Meluncur, bukan padam-lalu-menyala di tempat lain. Perpindahan yang
 *  terlihat itulah yang membuat navbar terbaca sebagai satu daftar utuh: mata
 *  mengikuti garisnya dan jadi tahu SEBERAPA JAUH ia berpindah, bukan cuma
 *  bahwa ia berpindah.
 *
 *  Sejak navigasinya mendatar, yang digeser `left`/`width`, bukan
 *  `top`/`height`. Butir yang tersembunyi di dalam panel yang sedang tertutup
 *  tidak punya posisi yang berarti (offsetWidth-nya nol), jadi penandanya
 *  dipadamkan alih-alih diletakkan di tempat yang salah. */
function pindahkanTanda(aktif) {
  const rel = $("#rel");
  const tanda = $(".rel-tanda", rel);
  if (!tanda) return;

  if (!aktif || !aktif.offsetWidth) {
    tanda.style.opacity = "0";
    rel.classList.remove("pakai-tanda");
    return;
  }
  rel.classList.add("pakai-tanda");

  const pasang = () => {
    // offsetLeft dihitung terhadap induk berposisi terdekat, yang belum tentu
    // #rel. Selisih kotak batas keduanya menjawabnya tanpa perlu menebak.
    const kiri = aktif.getBoundingClientRect().left
      - rel.getBoundingClientRect().left;
    const lebar = aktif.offsetWidth;
    tanda.style.left = (kiri + lebar * SISIP_TANDA) + "px";
    tanda.style.width = (lebar * (1 - SISIP_TANDA * 2)) + "px";
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

/** Garis tipis di kaki bilah navigasi yang mengikuti posisi gulir.
 *
 *  Hanya muncul kalau halamannya memang panjang: di layar yang muat sekali
 *  lihat, ia akan selalu penuh dan cuma jadi garis hiasan yang membingungkan. */
/* Browser yang bisa menggerakkan bilah ini sendiri lewat scroll-timeline.
   Diperiksa SEKALI: jawabannya tidak berubah sepanjang umur halaman, dan
   menanyakannya tiap rute berarti membayar parse CSS di jalur navigasi. */
const MAJU_LEWAT_CSS = typeof CSS !== "undefined" && CSS.supports
  && CSS.supports("animation-timeline: scroll(root block)");

/** Pasang bilah kemajuan baca.
 *
 *  SATU MESIN PER BROWSER, bukan dua yang saling menimpa. Di browser yang
 *  mendukung scroll-timeline, `transform` bilah ini sepenuhnya milik CSS dan
 *  pendengar gulirnya TIDAK dipasang sama sekali -- bukan dipasang lalu
 *  dibiarkan menulis nilai yang sama diam-diam. Di browser lain, CSS-nya
 *  tidak pernah menyala (ia di balik @supports) dan JS yang memegangnya.
 *
 *  Yang tidak ikut pindah: kelas `.tampak`. Ia menggerakkan `opacity`, bukan
 *  `transform`, jadi ia bukan mesin kedua untuk properti yang sama -- dan
 *  syaratnya ("halamannya memang cukup panjang untuk digulir") tidak bisa
 *  dinyatakan CSS. Di jalur CSS ia dihitung sekali per rute, bukan per frame.
 *
 *  `data-mesin` ditulis supaya jumlah mesin yang hidup bisa DIBUKTIKAN dari
 *  luar, bukan disimpulkan dari membaca kode ini. */
function pasangMajuBaca() {
  const garis = $("#maju-baca");
  if (!garis) return;
  if (lepasGulir) { lepasGulir(); lepasGulir = null; }

  const cukupPanjang = () =>
    document.documentElement.scrollHeight - window.innerHeight > 260;

  if (MAJU_LEWAT_CSS) {
    garis.dataset.mesin = "css";
    garis.style.transform = "";
    garis.classList.toggle("tampak", cukupPanjang());
    return;
  }

  garis.dataset.mesin = "js";
  lepasGulir = saatGulir(({ maju }) => {
    garis.classList.toggle("tampak", cukupPanjang());
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
    isikan(hasil, ...(daftar.length
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
      : [h("div.palet-kosong", {}, "Tidak ada yang cocok.")]));
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

/** Buka-tutup panel menu. Sejak navigasinya mendatar, hanya ada satu hal yang
 *  bisa dilipat — panel di layar sempit — jadi tidak ada lagi cabang "tutup
 *  kolom kiri" untuk layar lebar. Di layar lebar tombolnya memang disembunyikan
 *  CSS, tapi pintasan Ctrl+B tetap sampai ke sini, dan membuat pintasan itu
 *  mengubah sesuatu yang tak terlihat lebih membingungkan daripada diam. */
function alihRel() {
  if (window.innerWidth > AMBANG_PANEL) return;
  const cangkang = $("#cangkang");
  const buka = cangkang.classList.toggle("rel-buka");
  $("#rel-alih").setAttribute("aria-expanded", String(buka));
}

/** Panel yang turun dari navbar: daftar bahasa dan menu "Lainnya".
 *
 *  Keduanya memakai satu fungsi, bukan dua yang mirip. Aturannya sama persis —
 *  buka lewat pemicunya, tutup lewat Esc, klik di luar, atau begitu ada tautan
 *  di dalamnya yang dipakai. Yang terakhir itu penting: aplikasi ini tidak
 *  memuat ulang halaman, jadi panel yang dibuka tidak akan tertutup sendiri
 *  oleh perpindahan layar.
 *
 *  Membuka satu panel menutup yang lain. Dua daftar yang menggantung bersamaan
 *  dari satu baris adalah dua daftar yang saling menutupi. */
const penutupPanel = [];

function pasangTurun(id) {
  const turun = $("#" + id);
  if (!turun) return;
  const pemicu = $(".rel-pemicu", turun);

  const setel = (buka) => {
    turun.classList.toggle("buka", buka);
    pemicu.setAttribute("aria-expanded", String(buka));
  };
  penutupPanel.push(setel);

  pemicu.addEventListener("click", (e) => {
    e.stopPropagation();
    const buka = !turun.classList.contains("buka");
    for (const tutup of penutupPanel) tutup(false);
    setel(buka);
  });
  turun.addEventListener("click", (e) => {
    if (e.target.closest("a")) setel(false);
  });
  document.addEventListener("click", (e) => {
    if (!turun.contains(e.target)) setel(false);
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") setel(false);
  });
}

/** Ganti tema tanpa kedipan.
 *
 *  Mengganti nilai variabel CSS mengubah puluhan warna dalam satu frame, dan
 *  pergantian mendadak seluruh layar persis apa yang dilarang aturan gerak di
 *  gaya.css. Kelas `alih-tema` memberi transisi warna 260 md ke semuanya, lalu
 *  dilepas lagi — kalau dibiarkan menempel, setiap :hover sesudahnya ikut jadi
 *  lengket. */
let lepasTema = 0;

export function gantiTema(ev) {
  const akar = document.documentElement;

  /* DUA JALUR, DAN TIDAK PERNAH BERSAMAAN.
     View Transition memotret layar lama dan baru lalu menyilangkan keduanya,
     sedangkan `alih-tema` memasang transisi warna pada SETIAP elemen. Kalau
     keduanya hidup, satu properti yang sama (warna latar dan teks) digerakkan
     dua mesin: potret "baru" terambil saat warnanya masih di tengah jalan,
     lalu DOM hidup melanjutkan transisinya sendiri di bawah lingkaran. Yang
     terlihat bukan satu sapuan melainkan dua crossfade bertumpuk, dan paling
     kentara di terang <-> kontras karena jarak warnanya paling jauh.

     Yang dipilih: di jalur VT temanya berganti SEKETIKA, dan lingkaranlah
     yang membawa perubahannya -- potret lama memakai tema lama sepenuhnya,
     potret baru memakai tema baru sepenuhnya. `alih-tema` tidak dipasang di
     sini sama sekali. Jalur lamanya tetap utuh untuk browser tanpa VT dan
     untuk tingkat gerak di bawah "penuh". */
  const bisaLingkar = typeof document.startViewTransition === "function"
    && gerakPenuh();

  if (!bisaLingkar) {
    if (adaGerak()) {
      akar.classList.add("alih-tema");
      clearTimeout(lepasTema);
      // 320, bukan 260: kepala 60 md supaya kelasnya tidak dicabut di tengah
      // transisi 260 md yang dipasangnya (gaya.css html.alih-tema).
      lepasTema = setTimeout(() => akar.classList.remove("alih-tema"), 320);
    }
    sorak("Tema: " + temaBerikutnya(), "", 1.6);
    return;
  }

  // Pusat lingkaran adalah tombol yang diklik; jari-jarinya sudut terjauh,
  // supaya sapuannya selalu menutup layar berapa pun posisi tombolnya.
  const kotak = ev && ev.currentTarget && ev.currentTarget.getBoundingClientRect
    ? ev.currentTarget.getBoundingClientRect() : null;
  const x = kotak ? kotak.left + kotak.width / 2 : window.innerWidth;
  const y = kotak ? kotak.top + kotak.height / 2 : 0;
  const jari = Math.hypot(Math.max(x, window.innerWidth - x),
                          Math.max(y, window.innerHeight - y));
  akar.style.setProperty("--tema-x", x + "px");
  akar.style.setProperty("--tema-y", y + "px");
  akar.style.setProperty("--tema-r", jari + "px");
  akar.classList.add("lingkar-tema");

  vt(() => {
    // sorak() dipanggil di dalam callback supaya pengumumannya ikut terpotret
    // bersama tema barunya, bukan menyusul sesudah sapuannya selesai.
    sorak("Tema: " + temaBerikutnya(), "", 1.6);
  }).then(() => {
    akar.classList.remove("lingkar-tema");
    for (const n of ["--tema-x", "--tema-y", "--tema-r"]) {
      akar.style.removeProperty(n);
    }
  });
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

  // Kurva pegas hasil solver diterbitkan sebagai token CSS sebelum apa pun
  // digambar. gaya.css sudah punya cadangan cubic-bezier yang sah, jadi ini
  // bukan syarat tampil — ia menyamakan kurva yang dipakai CSS dengan yang
  // dipakai WAAPI, supaya satu gerakan tidak pernah punya dua bentuk.
  terbitkanKurva();

  try {
    ctx.awal = await api.ambil("/api/awal");
  } catch (e) {
    isikan(document.body, h("div.tanpa-js", {},
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
  pasangTurun("rel-turun-bahasa");
  pasangTurun("rel-turun-lain");

  $("#lompat-isi").addEventListener("click", () => {
    const layar = $("#layar");
    layar.focus();
    layar.scrollIntoView({ block: "start",
                           behavior: adaGerak() ? "smooth" : "auto" });
  });
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
  // Render pertama TIDAK memindahkan fokus: kalau ia memindahkannya, Tab
  // pertama sesudah halaman termuat berangkat dari tengah dokumen dan tautan
  // "Lompat ke isi" jadi permukaan yang ada tapi tidak bisa dipakai. Lihat
  // gerbang `pindahFokus` di `gambarRute()`.
  await gambarRute({ pindahFokus: false });
}

mulai();
