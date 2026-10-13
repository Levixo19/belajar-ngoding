/* Pratinjau halaman: menjalankan HTML pelajar di browser yang sedang ia pakai.
 *
 * Kenapa ini ada. Seluruh mesin penilaian di aplikasi ini bekerja dengan
 * membandingkan KELUARAN, dan HTML tidak mencetak apa pun — jadi `struktur.py`
 * membacanya jadi pohon elemen dan pohon itulah yang jadi "keluarannya".
 * Untuk menilai, itu keputusan yang benar dan tidak boleh diubah (lihat
 * AGENTS.md). Untuk DITONTON pelajar, itu jawaban yang salah: orang yang baru
 * menulis <h1>Halo, Dunia!</h1> ingin melihat tulisan Halo, Dunia — bukan
 * daftar menjorok berisi nama-nama tag yang baru saja ia ketik sendiri.
 *
 * Yang dibutuhkan untuk menampilkannya sudah ada di ruangan: browser itu
 * sendiri. Tidak ada server, tidak ada pustaka, tidak ada permintaan jaringan.
 *
 * Keamanan. Bingkainya dipasang `sandbox="allow-scripts"` TANPA
 * `allow-same-origin`, dan kombinasi itu bukan pilihan sembarangan — ia aturan
 * yang diajarkan kurikulum ini sendiri di materi HTML 13: memberi keduanya
 * sekaligus untuk berkas se-asal membuat sandbox-nya sia-sia, karena skrip di
 * dalamnya bisa meraih dokumen induknya. Tanpa `allow-same-origin`, isi
 * bingkai duduk di asal buram: skripnya jalan (itu bagian dari pelajaran),
 * tapi ia tidak bisa membaca DOM induk, cookie, maupun localStorage aplikasi.
 *
 * Importir: layar-belajar.js, layar-kerja.js.
 */

import { h } from "./inti.js";

/* Tinggi awal sebelum halamannya sempat melapor. Dipilih cukup untuk contoh
   sepanjang satu-dua paragraf; hampir semua contoh di kurikulum lebih pendek
   dari ini, jadi yang terlihat bukan bingkai kosong yang menyusut melainkan
   halaman yang langsung pas. */
const TINGGI_AWAL = 260;
const TINGGI_MAKS = 560;
const KELONGGARAN = 8;

/* Pelapor tinggi yang diselipkan ke dalam halaman pelajar.
 *
 * Bingkai berasal buram tidak bisa diukur dari luar — `contentDocument`-nya
 * memang sengaja tidak terjangkau. Jadi yang mengukur harus penghuninya
 * sendiri, dan satu-satunya jalan keluar yang tersisa adalah postMessage.
 * Induknya tetap tidak mempercayai isinya begitu saja: ia mencocokkan
 * `event.source` dengan jendela bingkainya sendiri sebelum memakai angkanya.
 *
 * ResizeObserver dipakai, bukan cuma `load`: gambar yang baru selesai diunduh
 * dan `@font-face` yang baru terpasang mengubah tinggi SESUDAH load, dan
 * bingkai yang berhenti mengukur di situ menyisakan potongan bawah halaman
 * yang terpotong tanpa sebab yang kelihatan. */
const PELAPOR = `
<script>
(function () {
  function lapor() {
    var b = document.body;
    if (!b) return;
    /* Tingginya diukur dari TEPI BAWAH TERJAUH anak-anak body, bukan dari
       scrollHeight sebuah elemen.

       Dua jebakan sekaligus dihindari di sini, dan keduanya sudah menggigit:

       1. scrollHeight <html> MELINGKAR. <html> mengisi tinggi bingkainya,
          jadi angkanya melaporkan ulang tinggi yang barusan dipasang
          induknya -- halaman berisi satu judul dan satu paragraf melapor
          321px karena bingkainya memang 260px, lalu tidak pernah menyusut.
       2. Kotak body MELUPAKAN margin yang kolaps. Margin atas <h1> kolaps
          keluar melewati body, jadi kotak body mulai DI BAWAH judulnya dan
          tingginya kurang -- halaman yang sama terpotong di 95px.

       Tepi bawah anak terjauh tidak punya keduanya: ia diukur relatif
       terhadap viewport bingkai, dan margin yang kolaps sudah termasuk di
       dalam posisinya. */
    var bawah = 0;
    for (var i = 0; i < b.children.length; i++) {
      var r = b.children[i].getBoundingClientRect();
      if (r.height || r.width) bawah = Math.max(bawah, r.bottom);
    }
    if (!bawah) {
      /* Tidak ada satu pun anak yang punya kotak. Dua sebab yang sangat
         berbeda: halamannya memang kosong, ATAU dokumennya belum ditata sama
         sekali (pengukuran pertama berjalan saat readyState masih "loading").
         Membedakannya penting -- melaporkan 8px untuk yang kedua membuat
         bingkai menyusut jadi satu baris lalu melompat lagi begitu tata
         letaknya selesai, dan lompatan itu tepat di bawah mata orang yang
         baru menekan Jalankan. */
      if (b.children.length) return;
      bawah = b.getBoundingClientRect().bottom;
    }
    /* Margin BAWAH tidak ikut dalam getBoundingClientRect, dan margin bawah
       anak terakhir kolaps bersama margin bawah body -- yang berlaku yang
       TERBESAR, bukan jumlahnya. Melupakan ini menyisakan satu bilah gulir
       tipis di halaman yang sebenarnya sudah muat: <p> bermargin 16px di
       dalam body bermargin 8px kurang tepat 8 piksel. */
    var sisa = 0, anak = b.children[b.children.length - 1];
    if (anak) sisa = parseFloat(getComputedStyle(anak).marginBottom || 0);
    sisa = Math.max(sisa, parseFloat(getComputedStyle(b).marginBottom || 0));
    var t = bawah + sisa;
    /* Koreksi terakhir, dan arahnya cuma satu: MENUMBUHKAN.
       Ukuran dari anak-anak body melewatkan hal-hal yang tidak duduk di alur
       normal -- elemen ber-position absolute, bayangan, garis luar. Kalau
       dokumennya benar-benar meluber melewati bingkainya, scrollHeight tahu
       itu dan angkanya dipakai. Kalau tidak meluber, ia diabaikan: nilainya
       sekurang-kurangnya setinggi bingkai, jadi memakainya di situ berarti
       kembali ke jebakan melingkar yang membuat bingkai tidak pernah bisa
       menyusut lagi. */
    if (document.documentElement.scrollHeight > innerHeight) {
      t = Math.max(t, document.documentElement.scrollHeight);
    }
    parent.postMessage({ pratinjauTinggi: Math.ceil(t) }, "*");
  }

  addEventListener("load", lapor);
  addEventListener("resize", lapor);
  addEventListener("message", function (e) {
    if (e.data && e.data.pratinjauMinta) lapor();
  });
  if (window.ResizeObserver && document.body) {
    new ResizeObserver(lapor).observe(document.body);
  }
  lapor();
})();
<\/script>`;

/** Bingkai pratinjau untuk sebuah dokumen HTML utuh.
 *
 *  `opsi.lebar` menyetel lebar PERANGKAT yang disimulasikan, dalam piksel.
 *  Nol atau tidak diisi berarti keadaan ALAMI bingkainya: `width: 100%` dari
 *  gaya.css, nol transform, nol gaya inline pada wadahnya -- persis seperti
 *  sebelum sakelar lebar ada. Itu kontrak, bukan kebetulan: `layar-belajar.js`
 *  memanggil fungsi ini tanpa `opsi`, dan halaman materi tidak boleh berubah
 *  satu simpul pun karena fitur yang hidup di layar lain.
 *
 *  Yang disetel adalah lebar BINGKAINYA, bukan wadahnya. Bedanya seluruh
 *  gunanya fitur ini: halaman di dalam bingkai 360 px benar-benar MENATA ULANG
 *  dirinya di 360 px -- media query-nya menyala, `auto-fill` jatuh ke satu
 *  kolom, teksnya membungkus di tempat yang berbeda. Wadah yang disempitkan
 *  cuma MEMOTONG halaman yang tetap ditata selebar aslinya, dan yang terlihat
 *  bukan pelajaran melainkan separuh halaman yang hilang.
 *
 *  @param {string} kode  HTML apa adanya, seperti yang ditulis pelajar.
 *  @param {{lebar?: number}} opsi
 *  @returns {{el: HTMLElement, lepas: function, setLebar: function}}
 */
export function pratinjauHtml(kode, opsi = {}) {
  const bingkai = h("iframe.pratinjau-bingkai", {
    title: "Pratinjau halaman",
    sandbox: "allow-scripts",
    // Kode pelajar apa adanya, ditambah pelapor tinggi di ujungnya. Ditempel
    // di BELAKANG supaya nomor baris apa pun yang muncul di pesan error
    // browser tetap cocok dengan yang ia lihat di editor.
    srcdoc: kode + PELAPOR,
    // TANPA loading="lazy", dan itu bukan kelalaian. Kartu keluaran hampir
    // selalu lahir di bawah lipatan layar, jadi bingkai bermuat-malas
    // menerima dokumen KOSONG lebih dulu -- pelapornya jalan, mengukur body
    // tanpa anak, dan melapor 8px. Yang terlihat: kotak putih setinggi satu
    // baris di bawah kode yang barusan dijalankan. Lagi pula tidak ada yang
    // dihemat: bingkainya baru dibuat saat tombolnya ditekan.
  });
  bingkai.style.height = TINGGI_AWAL + "px";
  const wadah = h("div.pratinjau", {}, bingkai);

  // Lebar perangkat yang SEDANG terpasang. Ini bukan otoritasnya: yang
  // memutuskan `layar-kerja.js`, karena pilihannya harus bertahan melewati
  // kartu hasil yang dirender ulang — dan kartu itu membuang objek ini.
  // Yang disimpan di sini cuma nilai yang sudah dikenakan, sejajar dengan
  // `tinggiTerpasang` di bawahnya.
  let lebarPasang = Number(opsi.lebar) || 0;
  let tinggiTerpasang = TINGGI_AWAL;

  /* Kenakan lebar + tinggi + skala sebagai SATU keputusan.
   *
   * Urutannya mengikat, dan membaliknya sudah salah secara aritmetik:
   * tinggi yang diskalakan adalah tinggi HASIL CLAMP, bukan angka mentah
   * yang dilaporkan halaman. Yang benar `lebar -> k -> tinggi x k`;
   * menukar dua langkah terakhir membuat wadah lebih tinggi daripada yang
   * dibutuhkan pada `k = 1` dan memangkas isinya pada `k < 1`.
   *
   * Kenapa SKALA dan bukan `overflow-x: auto`: menggulir ke samping
   * menyembunyikan separuh halaman yang justru mau dibandingkan, dan pen
   * gulir bersarang di dalam `.kerja-hasil` berarti dua mesin pada satu
   * sumbu — salah satunya `wheel`, yang di sana adalah isyarat putus-pin
   * (`layar-kerja.js`, `SENTUHAN_HASIL`).
   *
   * Dan bingkainya TIDAK dibuat ulang. Pelapor tinggi di dalamnya sudah
   * mendengarkan `resize`, jadi mengubah `style.width` saja cukup; menulis
   * ulang `srcdoc` berarti memutar ulang animasi dan skrip halaman pelajar
   * di depan matanya sendiri, setiap kali ia menekan pil lebar.
   *
   * Jalur `lebarPasang === 0` mengosongkan kembali SEMUA yang dipasangnya.
   * Itu bentuk yang sama dengan aturan animasi di AGENTS.md: keadaan akhir
   * sebuah sakelar wajib keadaan alami elemennya, supaya "lebar penuh"
   * benar-benar mengembalikan bingkai ke rupa tanpa fitur ini — bukan ke
   * tiruannya yang kebetulan mirip. */
  const kenakan = () => {
    bingkai.style.height = tinggiTerpasang + "px";
    if (!lebarPasang) {
      // Menghapus properti yang memang belum pernah disetel adalah no-op,
      // jadi jalur bawaan menyisakan atribut gaya berisi `height` saja.
      bingkai.style.width = "";
      bingkai.style.transform = "";
      bingkai.style.transformOrigin = "";
      bingkai.style.marginRight = "";
      bingkai.style.marginBottom = "";
      wadah.style.height = "";
      return;
    }
    // `clientWidth` wadah, bukan `offsetWidth`: `.pratinjau` punya border,
    // dan lebar yang tersedia untuk bingkainya adalah lebar DALAM-nya.
    const tersedia = wadah.clientWidth;
    const k = tersedia > 0 ? Math.min(1, tersedia / lebarPasang) : 1;
    bingkai.style.width = lebarPasang + "px";
    // `top left`, bukan bawaan `center`: dengan titik tengah, halaman yang
    // mengecil ikut bergeser ke dalam dan tepi kirinya tidak lagi sejajar
    // dengan tepi kiri wadahnya.
    bingkai.style.transformOrigin = "top left";
    bingkai.style.transform = k < 1 ? `scale(${k})` : "";
    const tinggiGambar = Math.round(tinggiTerpasang * k);
    /* Margin negatif, dan ini bukan hiasan — ia menutup satu cacat TERUKUR.
     *
     * `transform` tidak mengubah satu kotak tata letak pun, jadi bingkai
     * `width: 1280px` yang tergambar selebar 761 px TETAP menyumbang kotak
     * 1280 px ke daerah luber wadahnya. Terukur di 1280x800: `.pratinjau`
     * melapor `scrollWidth 1280` vs `clientWidth 761`, dan `scrollLeft`-nya
     * benar-benar bisa digeser ke 400 — wadah itu diam-diam jadi pen gulir
     * ber-bilah tersembunyi, yang isinya separuh halaman yang justru sedang
     * dibandingkan. Dokumen dan `.kerja-hasil` tidak ikut kena (keduanya
     * terukur `scrollWidth == clientWidth`), jadi gejalanya memang tidak
     * terlihat — dan itu yang membuatnya pantas ditutup sekarang, bukan
     * nanti.
     *
     * Margin negatif menyamakan kotak MARGIN bingkai dengan kotak yang
     * TERGAMBAR, jadi tidak ada lagi yang tersisa untuk diluberi. Ia aman
     * justru karena `transform-origin` ada di `top left`: yang digambar
     * duduk di pojok kiri atas, dan ruang yang dicabut margin negatif
     * adalah ruang yang memang sudah kosong.
     *
     * Dipasang hanya pada `k < 1`. Pada `k = 1` tidak ada yang berlebih,
     * dan margin negatif nol piksel cuma akan menambah satu properti ke
     * atribut gaya tanpa mengubah apa pun. */
    bingkai.style.marginRight = k < 1
      ? -Math.round(lebarPasang - tersedia) + "px" : "";
    bingkai.style.marginBottom = k < 1
      ? -(tinggiTerpasang - tinggiGambar) + "px" : "";
    wadah.style.height = tinggiGambar + "px";
  };
  kenakan();

  function saatPesan(e) {
    if (e.source !== bingkai.contentWindow) return;
    const t = e.data && e.data.pratinjauTinggi;
    if (typeof t !== "number" || !isFinite(t)) return;
    // Kelonggaran beberapa piksel, dan sisi salahnya dipilih sadar: ruang
    // kosong setipis ini di bawah halaman tidak terlihat siapa pun,
    // sedangkan KEKURANGAN satu piksel memunculkan bilah gulir sepanjang
    // bingkai — dan bilah gulir pada halaman yang sebenarnya sudah muat
    // membaca sebagai "ada yang belum kamu lihat di bawah sana".
    tinggiTerpasang = Math.min(TINGGI_MAKS, Math.max(72, t + KELONGGARAN));
    kenakan();
    bingkai.classList.toggle("pratinjau-penuh", t + KELONGGARAN > TINGGI_MAKS);
  }
  addEventListener("message", saatPesan);
  // Beberapa hal mengubah tinggi SESUDAH dokumennya siap: gambar yang baru
  // selesai diunduh, dan font yang baru terpasang. ResizeObserver di dalam
  // menangkap keduanya, tapi hanya kalau ia sempat dipasang -- halaman yang
  // skripnya gagal (dan di kurikulum ini halaman yang sengaja salah memang
  // ada) tidak pernah melapor sama sekali. Satu pengukuran ulang saat load
  // menutup itu tanpa membuat halaman yang sehat berkedip.
  bingkai.addEventListener("load", () => {
    try { bingkai.contentWindow.postMessage({ pratinjauMinta: 1 }, "*"); }
    catch (e) { /* asal buram menolak; pelapor di dalam sudah mengurusnya */ }
  });

  return {
    el: wadah,
    // `lepas()` tetap melepas SATU pendengar dan tidak lebih. Sakelar lebar
    // sengaja tidak menambah kanal kedua: ia tidak mengamati ukuran wadah dan
    // tidak mendengarkan `resize` jendela, jadi tidak ada apa pun baru yang
    // bisa tertinggal hidup di belakang layar berikutnya. Harganya diketahui
    // dan dipilih: jendela yang diubah ukurannya SAAT sebuah lebar terpasang
    // menyisakan `k` lama sampai halaman di dalamnya melaporkan tingginya
    // lagi. Pengamat ukuran di atas wadah yang tingginya DISETEL fungsi ini
    // sendiri adalah umpan balik yang memberi makan dirinya, dan menukar
    // cacat yang kecil dan terbatas dengan cacat yang tidak berujung bukan
    // pertukaran yang baik.
    lepas: () => removeEventListener("message", saatPesan),
    setLebar: (w) => {
      lebarPasang = Number(w) || 0;
      kenakan();
    },
  };
}

/* ==================================================================== CSS
 *
 * CSS tidak menggambar apa pun sendirian — ia butuh markup untuk dikenai.
 * Karena itu keluaran CSS di aplikasi ini berupa daftar aturan yang sudah
 * dirapikan: bisa dinilai, bisa dibandingkan, dan memang perlu ada. Tapi ia
 * juga jawaban yang tidak pernah ditanyakan orang yang baru menulis
 * `.kartu { border: 1px solid #ddd }` — yang ingin ia tahu cuma satu:
 * kelihatannya jadi seperti apa.
 *
 * Dua jalan, dan yang pertama dicoba lebih dulu karena ia jujur tanpa syarat:
 *
 * 1. Blok yang SUDAH berisi markup (11 dari 40 blok kode di materi CSS
 *    berbentuk halaman utuh dengan <style> di dalamnya) dipratinjau apa
 *    adanya. Tidak ada yang dikarang.
 * 2. Blok CSS murni dikenakan pada halaman contoh yang DIBUATKAN dari
 *    pemilihnya sendiri. Ini memang karangan, jadi ia diberi label sebagai
 *    karangan — lihat `pratinjauCss`. Yang didapat sebagai gantinya: pelajar
 *    melihat aturan mana mengenai apa, dan pemilih yang tidak mengenai apa
 *    pun jadi kelihatan justru karena contohnya dibuat DARI pemilih itu.
 */

/* Elemen yang tidak sah berdiri sendiri di <body>. Menaruh <li> langsung di
   body membuat browser menampilkannya sebagai teks polos tanpa bulatan, dan
   pelajar akan menyimpulkan aturannya tidak berlaku. */
const INDUK_WAJIB = {
  li: "ul", td: "tr", th: "tr", tr: "table", tbody: "table", thead: "table",
  option: "select", figcaption: "figure", legend: "fieldset",
  summary: "details", dt: "dl", dd: "dl", source: "video", caption: "table",
};

/* Isi contoh. Elemen kosong tidak punya tinggi, dan aturan yang mengenai
   sesuatu yang tak terlihat sama saja dengan aturan yang tidak berlaku. */
const TEKS_CONTOH = {
  h1: "Judul Halaman", h2: "Sub Judul", h3: "Judul Bagian",
  h4: "Judul Kecil", h5: "Judul Lebih Kecil", h6: "Judul Terkecil",
  a: "sebuah tautan", button: "Tombol", label: "Label isian",
  li: "Butir daftar", td: "sel tabel", th: "kepala kolom",
  code: "kode()", strong: "tebal", em: "miring", small: "kecil",
  blockquote: "Kutipan contoh.", figcaption: "Keterangan gambar",
  summary: "Klik untuk buka", dt: "Istilah", dd: "Penjelasan istilah",
  p: "Paragraf contoh. Cukup panjang supaya tinggi baris, warna, dan "
   + "lebar kolomnya benar-benar kelihatan saat aturanmu berlaku.",
};
const TEKS_BAWAAN = "Teks contoh";

/* Elemen yang isinya bukan teks. */
const KOSONG = new Set(["img", "input", "br", "hr", "source", "video", "audio",
                        "canvas", "iframe", "textarea", "select"]);

const MAKS_CONTOH = 14;

/** Buang komentar CSS tanpa menyentuh isi string. */
function tanpaKomentar(css) {
  return css.replace(/\/\*[\s\S]*?\*\//g, " ");
}

/** Semua pemilih di sebuah lembar CSS, termasuk yang di dalam @media.
 *
 *  Ditulis tangan sebagai pemindai kurung, bukan regex tunggal: pemilih
 *  bersarang di dalam at-rule dan deklarasi yang memuat kurung kurawal
 *  (seperti nilai `grid-template-areas`) membuat regex apa pun salah hitung.
 */
function pemilihDi(css) {
  const teks = tanpaKomentar(css);
  const keluar = [];
  let mulai = 0, dalam = 0;
  for (let i = 0; i < teks.length; i++) {
    const c = teks[i];
    if (c === "{") {
      const kepala = teks.slice(mulai, i).trim();
      dalam += 1;
      if (kepala.startsWith("@")) {
        // At-rule: preludenya bukan pemilih. @media & @supports MEMUAT
        // pemilih, @keyframes memuat persentase yang bukan pemilih.
        if (/^@(media|supports|layer|container|scope)\b/.test(kepala)) {
          mulai = i + 1;
          continue;
        }
        // Lewati seluruh badan at-rule lain.
        let d = 1;
        while (++i < teks.length && d) {
          if (teks[i] === "{") d += 1;
          else if (teks[i] === "}") d -= 1;
        }
        dalam -= 1;
        mulai = i + 1;
        continue;
      }
      if (kepala) keluar.push(kepala);
      // Lewati badan aturannya.
      let d = 1;
      while (++i < teks.length && d) {
        if (teks[i] === "{") d += 1;
        else if (teks[i] === "}") d -= 1;
      }
      dalam -= 1;
      mulai = i + 1;
    } else if (c === "}") {
      dalam = Math.max(0, dalam - 1);
      mulai = i + 1;
    }
  }
  return keluar;
}

/** Satu pemilih sederhana -> {tag, kelas[], id, atribut{}} */
function uraiSederhana(bagian) {
  // Pseudo-class dan pseudo-element dibuang: keadaan seperti :hover tidak bisa
  // ditunjukkan pada halaman diam, dan ::before butuh elemen tuannya — yang
  // justru itulah yang sedang dibuat.
  const bersih = bagian.replace(/::?[\w-]+(\([^)]*\))?/g, "");
  const tag = (bersih.match(/^[a-zA-Z][\w-]*/) || [""])[0].toLowerCase();
  const kelas = (bersih.match(/\.[\w-]+/g) || []).map((x) => x.slice(1));
  const id = (bersih.match(/#[\w-]+/) || [""])[0].slice(1);
  const atribut = {};
  for (const a of bersih.match(/\[[^\]]+\]/g) || []) {
    const m = a.slice(1, -1).match(/^([\w-]+)\s*(?:[~^|*$]?=\s*['"]?([^'"\]]*)['"]?)?/);
    if (m) atribut[m[1]] = m[2] === undefined ? "" : m[2];
  }
  return { tag, kelas, id, atribut };
}

/** Rantai keturunan sebuah pemilih -> potongan HTML bersarang. */
function contohUntuk(pemilih) {
  // Kombinator diratakan jadi keturunan biasa: > + ~ semuanya cukup
  // diwujudkan sebagai "ada di dalam", dan membedakannya hanya menambah
  // kerumitan tanpa menambah yang terlihat.
  const rantai = pemilih.replace(/\s*[>+~]\s*/g, " ").split(/\s+/)
    .filter(Boolean);
  if (!rantai.length) return "";

  let dalam = "";
  let butuh = "";          // induk yang diminta elemen di sebelah dalam
  for (let i = rantai.length - 1; i >= 0; i--) {
    const { tag, kelas, id, atribut } = uraiSederhana(rantai[i]);
    let nama = tag || "div";
    if (nama === "html" || nama === "body") nama = "div";
    /* Kalau yang di sebelah dalam menuntut induk tertentu dan pemilih ini
       TIDAK menyebut tag apa pun, pakai induk itu sebagai tagnya.
       `.menu > li` jadi <ul class="menu"><li>, bukan
       <div class="menu"><ul><li>. Bedanya menentukan: menyisipkan <ul> di
       tengah memutus hubungan "anak langsung", jadi aturannya tidak berlaku
       dan yang dilihat pelajar adalah CSS-nya seolah tidak bekerja. */
    if (butuh && !tag) nama = butuh;
    const sifat = [];
    if (kelas.length) sifat.push(` class="${kelas.join(" ")}"`);
    if (id) sifat.push(` id="${id}"`);
    for (const [k, v] of Object.entries(atribut)) {
      sifat.push(v ? ` ${k}="${v}"` : ` ${k}`);
    }
    if (butuh && nama !== butuh) {
      // Tagnya disebut eksplisit dan bukan induk yang sah; sisipkan induknya.
      dalam = `<${butuh}>${dalam}</${butuh}>`;
    }
    if (KOSONG.has(nama)) {
      dalam = `<${nama}${sifat.join("")}>` + dalam;
    } else {
      const isi = dalam || TEKS_CONTOH[nama] || TEKS_BAWAAN;
      dalam = `<${nama}${sifat.join("")}>${isi}</${nama}>`;
    }
    butuh = INDUK_WAJIB[nama] || "";
  }
  // Elemen terluar pun bisa menuntut induk (`li` sendirian, tanpa `ul`).
  if (butuh) dalam = `<${butuh}>${dalam}</${butuh}>`;
  return dalam;
}

/** Halaman contoh untuk sebuah lembar CSS. "" kalau tidak ada yang bisa dibuat. */
export function halamanDariCss(css) {
  const sudah = new Set();
  const potongan = [];
  for (const aturan of pemilihDi(css)) {
    for (const satu of aturan.split(",")) {
      const p = satu.trim();
      // `body`, `html`, `:root` memang mengenai halamannya sendiri — CSS-nya
      // sudah dipasang di <head>, jadi tidak ada yang perlu dibuat untuknya.
      if (!p || /^(html|body|:root|\*)$/i.test(p)) continue;
      const kunci = p.replace(/\s+/g, " ");
      if (sudah.has(kunci)) continue;
      sudah.add(kunci);
      const x = contohUntuk(kunci);
      if (x) potongan.push(x);
      if (potongan.length >= MAKS_CONTOH) break;
    }
    if (potongan.length >= MAKS_CONTOH) break;
  }
  if (!potongan.length) return "";
  return `<!doctype html>
<html lang="id">
<head><meta charset="utf-8">
<style>
${css}
</style></head>
<body>
${potongan.join("\n")}
</body>
</html>`;
}

/** Apakah sebuah blok kode sudah berupa dokumen HTML utuh? */
export function adaMarkup(kode) {
  return /<\s*(!doctype|html|body|div|p|h[1-6]|ul|ol|section|nav|header|footer|main|article|span|a|button|img|table|form)\b/i
    .test(kode);
}

/** Bahasa yang hasilnya lebih baik DILIHAT daripada dibaca sebagai teks. */
export function bisaDipratinjau(runner) {
  return runner === "html" || runner === "css";
}

/** Dokumen yang harus dimuat ke bingkai untuk sebuah blok, atau "". */
export function dokumenPratinjau(runner, kode) {
  if (runner === "html") return kode;
  if (runner !== "css") return "";
  // Materi CSS sering menulis halaman utuh ber-<style> di dalamnya; itu bukan
  // karangan siapa pun dan dipratinjau apa adanya.
  if (adaMarkup(kode)) return kode;
  return halamanDariCss(kode);
}

/** Apakah halamannya DIBUATKAN (bukan milik pelajar)? Menentukan labelnya. */
export function halamanDikarang(runner, kode) {
  return runner === "css" && !adaMarkup(kode);
}
