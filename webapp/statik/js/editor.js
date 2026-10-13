/* Editor kode: textarea telanjang, disulap jadi editor yang enak dipakai.
 *
 * Kenapa bukan CodeMirror atau Monaco? Karena keduanya berarti megabita
 * dependensi, langkah build, dan janji "tanpa dependensi luar" yang batal.
 * Yang benar-benar dibutuhkan pemula sebenarnya sedikit dan bisa dibuat
 * sendiri: penyorotan, nomor baris, indentasi otomatis, kurung yang menutup
 * sendiri, dan Tab yang menambah indentasi alih-alih memindahkan fokus.
 *
 * Caranya: sebuah <textarea> berteks TRANSPARAN diletakkan persis di atas
 * <pre> berisi versi tersorot dari teks yang sama. Yang terlihat adalah
 * <pre>-nya; yang menerima ketikan adalah textarea-nya. Kursor asli browser
 * tetap dipakai lewat caret-color, jadi seleksi, seret, klik dua kali, dan
 * pembaca layar semuanya tetap bekerja seperti pada textarea biasa.
 *
 * Syarat mutlak penyelarasan itu: font, ukuran, tinggi baris, padding, dan
 * tab-size KEDUANYA harus sama persis. Beda satu piksel dan kursor akan
 * mendarat di huruf yang salah pada baris panjang. Semua nilai itu dikunci
 * berdampingan di gaya.css, pada blok `.editor-lapis > pre, > textarea`.
 *
 * Importir: layar-belajar.js, layar-kerja.js.
 */

import { h, tunda } from "./inti.js";
import { animasi, adaGerak, skala } from "./gerak.js";
import { token, keFragmen } from "./sorot.js";

const INDENT = "    ";                    // 4 spasi, konsisten dengan kurikulum
const TINGGI_MAKS = 0.62;                 // bagian dari tinggi jendela

/* Berapa lama nomor baris yang baru dituju tetap tersorot. Cukup lama untuk
 * ditemukan mata yang baru berpindah dari pesan galat ke editor, cukup pendek
 * untuk tidak jadi penanda permanen kedua di sebelah penanda baris aktif. */
const SOROT_TUJU_MS = 1400;

/* Di atas lebar ini, editor yang diminta `isiRuang` berhenti mengukur dirinya
 * dari isi dan menyerahkan tingginya kepada tata letak.
 *
 * ANGKANYA HARUS SAMA dengan ambang `@container panggung (min-width: 1100px)`
 * di gaya.css — di sanalah ruang kerja latihan berubah jadi dua panel setinggi
 * jendela. Kalau keduanya berbeda, ada pita lebar tempat CSS memberi editornya
 * satu baris grid setinggi sisa layar sementara JS tetap memaksa tinggi hasil
 * pengukuran isi: yang terlihat editor pendek menggantung di dalam kotak
 * tinggi, atau sebaliknya editor yang meluber melewati kakinya.
 *
 * #panggung membentang selebar viewport (tidak ada kolom tetap di kirinya),
 * jadi innerWidth adalah pengganti yang cukup tepat untuk lebar containernya. */
const AMBANG_RUANG = 1100;

const PASANGAN = { "(": ")", "[": "]", "{": "}", '"': '"', "'": "'", "`": "`" };

const KOMENTAR = {
  python: "# ", javascript: "// ", java: "// ", c: "// ", cpp: "// ",
  go: "// ", bash: "# ", sql: "-- ", aplikasi: "// ",
  csharp: "// ", rust: "// ", kotlin: "// ", typescript: "// ",
  php: "// ", ruby: "# ", fedora: "# ",
  // Visual Basic memakai kutip TUNGGAL untuk komentar, bukan garis miring.
  vb: "' ",
  fedora: "# ",
};

function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

export class Editor {
  /**
   * @param {object} opsi
   *   bahasa    kunci aturan penyorot
   *   kode      isi awal
   *   saatUbah  dipanggil (kode) setiap perubahan, sudah ditunda
   *   pintasan  { "ctrl+enter": fn, ... } — dijalankan sebelum perilaku bawaan
   *   isiRuang  true = tingginya diserahkan kepada tata letak, bukan diukur
   *             dari isi. Dipakai ruang kerja latihan; lihat _ukur().
   */
  constructor({ bahasa = "python", kode = "", saatUbah, pintasan = {},
                label = "Editor kode", isiRuang = false } = {}) {
    this.bahasa = bahasa;
    this.saatUbah = saatUbah;
    this.pintasan = pintasan;
    this.isiRuang = isiRuang;

    this.nomor = h("pre.editor-nomor", { "aria-hidden": "true" });
    this.sorotan = h("pre", { "aria-hidden": "true" });
    this.teks = h("textarea", {
      spellcheck: false, autocapitalize: "off", autocomplete: "off",
      wrap: "off", "aria-label": label,
    });
    this.lapis = h("div.editor-lapis", {}, this.sorotan, this.teks);

    this.jumlahBaris = h("span", {}, "1 baris");
    this.posisi = h("span", {}, "Brs 1, Kol 1");
    this.pesan = h("span.tersimpan", {});
    this.kaki = h("div.editor-kaki", {},
      this.posisi, this.jumlahBaris, this.pesan,
      h("span.sembunyi-hp", { gaya: { marginLeft: "auto" } },
        "Tab menambah indentasi · Ctrl+/ komentari"));

    this.el = h("div.editor", {}, this.nomor, this.lapis, this.kaki);

    // Nomor baris yang sedang disorot `keBaris()`, atau 0. Ia FIELD, bukan
    // kelas yang ditempel ke sebuah node: lihat alasannya di `_gambarNomor`.
    this._tujuBaris = 0;

    this.teks.value = kode;
    // Chrome menaruh kursor di AKHIR teks setelah .value diisi, sehingga baris
    // terakhirlah yang tersorot di gutter sebelum editor disentuh sama sekali.
    // Yang benar adalah baris pertama: di situ mata mulai membaca.
    this.teks.setSelectionRange(0, 0);
    this._pasangPeristiwa();
    this.gambar();
  }

  /* --------------------------------------------------------------- isi */

  get nilai() { return this.teks.value; }

  set nilai(v) {
    const berubah = this.teks.value !== v;
    this.teks.value = v;
    this.gambar();
    // Isi editor hanya berganti sendiri karena satu sebab: sesuatu di luar
    // yang menggantinya — "Kerangka kosong", contoh dari materi, pindah bahasa
    // di ruang coba. Tanpa tanda apa pun, perubahan sebesar itu bisa terlewat
    // sama sekali kalau mata sedang di tempat lain di halaman.
    if (berubah && adaGerak()) {
      animasi(this.sorotan, { opacity: [0.35, 1] }, { durasi: 200 });
    }
  }

  fokus() {
    this.teks.focus();
    return this;
  }

  catat(pesan) {
    this.pesan.textContent = pesan || "";
    if (pesan) {
      // "tersimpan" muncul sendiri di kaki editor, jauh dari tempat mata
      // sedang mengetik. Satu gerakan pendek 6 px adalah satu-satunya cara ia
      // punya kesempatan tertangkap penglihatan tepi.
      animasi(this.pesan, {
        opacity: [0, 1],
        transform: ["translateY(4px)", "none"],
      }, { pegas: "jawab" });
      clearTimeout(this._catatId);
      this._catatId = setTimeout(() => { this.pesan.textContent = ""; }, 2600);
    }
  }

  /** Antar caret ke baris `n` (1-based); true kalau barisnya memang ada.
   *
   *  Dipakai tombol per baris pada blok pesan galat di ruang kerja latihan.
   *  Mengembalikan `false` untuk nomor di luar jumlah baris TANPA melempar dan
   *  tanpa menggeser apa pun — pemanggilnya yang memutuskan tidak menawarkan
   *  tombol, karena tombol yang berakhir "baris itu tidak ada" lebih buruk
   *  daripada tidak ada tombol sama sekali.
   *
   *  Guliran menyentuh SATU wadah lalu diselaraskan lewat `_selaraskan()`
   *  (:286). `scrollIntoView` tidak dipakai di sini dengan sengaja: ia
   *  menggulir setiap leluhur yang bisa digulir, termasuk dokumen — jadi
   *  melompat ke baris 40 akan ikut memindahkan halamannya, dan pesan galat
   *  yang baru saja diklik orangnya hilang dari pandangan.
   *
   *  Pada tingkat gerak `mati`, caret dan guliran TETAP pindah: keduanya
   *  informasi, bukan hiasan. Yang padam cuma sorotnya. */
  keBaris(n) {
    const baris = this.teks.value.split("\n");
    if (!Number.isInteger(n) || n < 1 || n > baris.length) return false;

    let pos = 0;
    for (let i = 0; i < n - 1; i++) pos += baris[i].length + 1;

    this.teks.focus();
    this.teks.setSelectionRange(pos, pos);

    // Guliran disetel SESUDAH fokus dan caret, dan urutan itu terukur, bukan
    // selera: `focus()` pada textarea yang belum fokus menggulir caret ke
    // dalam pandangan sendiri, jadi menyetel `scrollTop` lebih dulu membuat
    // Chrome menariknya kembali ke posisi caret yang LAMA. Pada panggilan
    // pertama — editor belum disentuh, yaitu kasus paling umum di sini karena
    // orang mengklik tombol galat tanpa mampir ke editor — `scrollTop`
    // terukur tetap 0 dari 828 yang diminta.
    //
    // Tinggi baris dibaca dari gaya terhitung, bukan diketik: angkanya hidup
    // di `gaya.css` (`line-height` pada `.editor-lapis > pre, > textarea`),
    // dan dua tempat yang menyimpan satu angka akan berbeda suatu hari.
    const g = getComputedStyle(this.teks);
    const tinggiBaris = parseFloat(g.lineHeight) || 0;
    const puncak = (parseFloat(g.paddingTop) || 0) + (n - 1) * tinggiBaris;
    const ruang = this.teks.clientHeight;
    const batas = Math.max(0, this.teks.scrollHeight - ruang);
    this.teks.scrollTop = Math.min(
      batas, Math.max(0, puncak - (ruang - tinggiBaris) / 2));

    this._tujuBaris = adaGerak() ? n : 0;
    this._segarkanTanda();
    this._selaraskan();

    if (this._tujuBaris) {
      clearTimeout(this._tujuId);
      this._tujuId = setTimeout(() => {
        this._tujuBaris = 0;
        this._segarkanTanda();
      }, SOROT_TUJU_MS);
      // Amplitudo dari `skala()` (gerak.js:303), bukan angka tetap: di tingkat
      // `halus` sorotnya datang lebih tipis, bukan lebih lambat. Bingkainya
      // berakhir di `opacity: 1` — keadaan alami elemennya — dan `animasi()`
      // memakai `fill: "backwards"` kecuali diminta lain, jadi tidak ada nilai
      // yang dipaksakan sesudah animasinya selesai.
      animasi(this.nomor.querySelector("b.editor-tuju"),
              { opacity: [1 - 0.7 * skala(), 1] }, { durasi: 180 });
    }
    return true;
  }

  /* ----------------------------------------------------------- tampilan */

  gambar() {
    const isi = this.teks.value;

    // Baris terakhir tidak akan terlihat kalau teksnya berakhir dengan
    // newline: <pre> memangkas satu baris kosong di ujung. Satu newline
    // tambahan menutup selisih itu, dan tidak pernah kelihatan karena ia
    // memang kosong.
    this.sorotan.textContent = "";
    this.sorotan.appendChild(this._fragmenKurung(token(isi, this.bahasa)));
    this.sorotan.appendChild(document.createTextNode("\n"));

    const baris = isi.split("\n");
    this._gambarNomor(baris.length);
    this.jumlahBaris.textContent = `${baris.length} baris`;
    this._ukur();
    this._selaraskan();
  }

  _gambarNomor(jumlah) {
    const kini = this._barisKursor();
    // Sorot baris tujuan dibaca DARI FIELD, di sini, pada setiap penggambaran.
    //
    // Baris berikutnya membuang SELURUH isi gutter lalu membangunnya ulang,
    // dan itu terjadi pada tiap `keyup` dan tiap `click` (:318-:319) lewat
    // `_segarkanTanda`. Menempelkan kelas sorot ke node `<b>` hasil panggilan
    // sebelumnya karena itu tidak pernah selamat satu ketikan pun — dan
    // `keBaris()` sendiri MEMINDAHKAN kursor, jadi penggambaran ulang terjadi
    // tepat pada saat sorotnya baru dipasang. Yang padam oleh timer adalah
    // nilai fieldnya; timernya memanggil penggambar ini lagi.
    const tuju = this._tujuBaris || 0;
    this.nomor.textContent = "";
    for (let i = 1; i <= jumlah; i++) {
      const teks = i + (i < jumlah ? "\n" : "");
      // Baris yang sedang disunting ditandai — di berkas 60 baris, tanpa itu
      // mudah kehilangan jejak posisi setelah menggulir.
      if (i === tuju) this.nomor.appendChild(h("b.editor-tuju", {}, teks));
      else if (i === kini) this.nomor.appendChild(h("b", {}, teks));
      else this.nomor.appendChild(document.createTextNode(teks));
    }
    this._gambarPita();
  }

  _ukur() {
    // Di ruang kerja yang setinggi jendela, tinggi editor BUKAN urusan isinya.
    // Kerangka latihan tiga baris di atas empat ratus piksel ruang kosong
    // adalah ruang kerja yang menolak dipakai bekerja — jadi di sana tata
    // letak yang memberi tinggi, dan editor cuma mengisinya. Kelas
    // `.editor-isi-ruang` di gaya.css yang mengurus sisanya.
    if (this.isiRuang && window.innerWidth >= AMBANG_RUANG) {
      this.el.classList.add("editor-isi-ruang");
      this.teks.style.height = "100%";
      this.lapis.style.height = "100%";
      this.nomor.style.maxHeight = "";
      return;
    }
    this.el.classList.remove("editor-isi-ruang");

    // Tumbuh mengikuti isi sampai batas, lalu menggulir sendiri. Editor yang
    // tingginya tetap memaksa menggulir sejak baris pertama; yang tumbuh tanpa
    // batas mendorong tombol Periksa keluar layar.
    const maks = Math.round(window.innerHeight * TINGGI_MAKS);
    this.teks.style.height = "auto";
    const tinggi = Math.min(maks, Math.max(150, this.teks.scrollHeight));
    this.teks.style.height = tinggi + "px";
    this.lapis.style.height = tinggi + "px";
    this.nomor.style.maxHeight = tinggi + "px";
  }

  _selaraskan() {
    this.sorotan.scrollTop = this.teks.scrollTop;
    this.sorotan.scrollLeft = this.teks.scrollLeft;
    this.nomor.scrollTop = this.teks.scrollTop;
    this._gambarPita();
  }

  _perbaruiPosisi() {
    const sampai = this.teks.value.slice(0, this.teks.selectionStart);
    const baris = sampai.split("\n");
    this.posisi.textContent =
      `Brs ${baris.length}, Kol ${baris[baris.length - 1].length + 1}`;
  }

  _barisKursor() {
    return this.teks.value.slice(0, this.teks.selectionStart).split("\n").length;
  }

  _segarkanTanda() {
    this._perbaruiPosisi();
    this._gambarNomor(this.teks.value.split("\n").length);
  }

  /* ---------------------------------------------------------- peristiwa */

  _pasangPeristiwa() {
    const beritahu = tunda(() => {
      if (this.saatUbah) this.saatUbah(this.teks.value);
    }, 420);

    this.teks.addEventListener("input", () => { this.gambar(); beritahu(); });
    this.teks.addEventListener("scroll", () => this._selaraskan());
    this.teks.addEventListener("keyup", () => this._segarkanTanda());
    this.teks.addEventListener("click", () => this._segarkanTanda());
    this.teks.addEventListener("keydown", (e) => this._saatTombol(e));

    // Satu-satunya pendengar yang dipasang di luar elemen editor sendiri, dan
    // karena itu satu-satunya yang harus dilepas tangan. Penanganannya
    // disimpan supaya `lepas()` punya rujukan yang sama persis untuk dicabut —
    // `tunda()` mengembalikan fungsi BARU tiap dipanggil, jadi memanggilnya
    // dua kali menghasilkan dua fungsi berbeda dan removeEventListener tidak
    // akan mencopot apa pun.
    this._saatUkur = tunda(() => this._ukur(), 160);
    window.addEventListener("resize", this._saatUkur);
  }

  /* ---------------------------------------------------- pita baris aktif */

  /** Tulis letak pita baris aktif ke dua custom property di `this.lapis`.
   *
   *  Angkanya dibaca dari gaya TERHITUNG, bukan diketik: `line-height` dan
   *  `padding-top` hidup di gaya.css (blok `.editor-lapis > pre, > textarea`),
   *  dan satu angka yang disimpan di dua tempat akan berbeda suatu hari. Idiom
   *  bacanya sama persis dengan yang sudah dipakai `keBaris()`.
   *
   *  Nomor barisnya datang dari `_barisKursor()` — sumber yang SAMA dengan yang
   *  dipakai gutter. Menghitungnya ulang dari `selectionStart` di sini berarti
   *  dua definisi "baris mana yang aktif" di dalam satu kelas, dan suatu hari
   *  nomor yang menyala dan pita yang menyala akan menunjuk baris berbeda.
   *
   *  Yang ditulisi `this.lapis`, BUKAN `this.sorotan`: `set nilai()`
   *  menganimasikan `opacity` sorotan lewat WAAPI setiap isi editor diganti,
   *  dan menumpangkan keadaan pita pada elemen yang sedang dianimasikan berarti
   *  dua mesin berebut satu elemen.
   *
   *  Dua titik panggilnya metode yang memang sudah ada, bukan pendengar baru:
   *  `_gambarNomor()` (tiap `input`/`keyup`/`click` lewat `_segarkanTanda`) dan
   *  `_selaraskan()` (tiap `scroll`). Semua jalur — mengetik, menggulir,
   *  `keBaris()`, penggantian isi, kursor pindah — lewat salah satunya. */
  _gambarPita() {
    const g = getComputedStyle(this.teks);
    const { atas, tinggi } = posisiPita({
      baris: this._barisKursor(),
      tinggiBaris: parseFloat(g.lineHeight) || 0,
      paddingAtas: parseFloat(g.paddingTop) || 0,
      scrollTop: this.teks.scrollTop,
    });
    this.lapis.style.setProperty("--pita-atas", atas + "px");
    this.lapis.style.setProperty("--pita-tinggi", tinggi + "px");
  }

  /* ------------------------------------------------- tampilan (lanjutan) */

  /** Fragmen tersorot yang kurungnya ikut membawa kedalamannya.
   *
   *  Pemetaan jenis token -> `<span class="tk-...">` TETAP milik `keFragmen()`
   *  di sorot.js, satu-satunya tempatnya. Yang ditambahkan di sini cuma
   *  ATRIBUT, dan itu sebabnya metode ini menyusuri `childNodes` hasil
   *  `keFragmen` sejajar dengan potongannya alih-alih membangun span sendiri:
   *  `keFragmen` menambahkan tepat satu simpul per entri, jadi potongan ke-i
   *  selalu simpul ke-i. Menyalin pemetaan kelasnya ke sini berarti dua
   *  tempat yang harus ingat bahwa jenis `teks` BUKAN span — dan yang kedua
   *  tidak dipagari oleh apa pun.
   *
   *  Penjagaan `setAttribute` bukan kehati-hatian berlebihan: potongan
   *  berjenis `teks` mendarat sebagai simpul teks yang tidak punya metode
   *  itu. Potongan kurung selalu `operator`, jadi ia selalu span — tapi
   *  syaratnya ditulis atas BENTUK simpulnya, bukan atas keyakinan itu.
   *
   *  Ia duduk di bawah blok peristiwa, bukan di sebelah `gambar()` tempatnya
   *  sewajarnya, karena anchor `(:286)` dan `(:318-:319)` di komentar berkas
   *  ini adalah klaim atas nomor baris yang diadu `TestAlamatKomentar` —
   *  menyisipkan metode di atasnya membuat ketiganya menunjuk baris lain.
   *
   *  Rangkaiannya dibaca dari DALAM ke luar, dan urutan itu TIDAK mengubah
   *  keluarannya: membaliknya diukur memberi nol beda atas seluruh korpus
   *  kurikulum. Yang mengikat dua invarian di pagar korpusnya —
   *  `korpusWarnaBerNewline` dan `korpusIndenRengket`, keduanya nol — dan
   *  itulah yang diterangkan docstring `pisahInden`. */
  _fragmenKurung(daftar) {
    const potongan = pisahInden(pisahKurung(daftar));
    const wadah = keFragmen(potongan);
    const simpul = wadah.childNodes;
    for (let i = 0; i < potongan.length; i++) {
      const warna = potongan[i][2];
      const el = simpul[i];
      if (warna === null || !el || !el.setAttribute) continue;
      if (warna === YATIM) el.setAttribute("data-yatim", "");
      else el.setAttribute("data-warna", String(warna));
    }
    return wadah;
  }

  /** Lepaskan editor dari halaman.
   *
   *  WAJIB dipanggil dari `saatKeluar` layar yang memakainya. Tanpa itu,
   *  pendengar `resize` di atas tetap terdaftar dan memegang instance ini,
   *  yang memegang `this.el`, yang memegang seluruh pohon DOM layarnya —
   *  termasuk soal, hint, dan solusi contoh yang tadi diunduh. Tidak ada satu
   *  pun dari itu yang bisa dikumpulkan sampah selama tab masih terbuka. */
  lepas() {
    window.removeEventListener("resize", this._saatUkur);
    clearTimeout(this._catatId);
    // Timer sorot `keBaris()` memanggil `_segarkanTanda()`, yang menulis ke
    // gutter. Dibiarkan hidup, ia menggambar ke pohon DOM layar yang sudah
    // ditinggalkan — dan memegang instance ini selama sisa detiknya.
    clearTimeout(this._tujuId);
  }

  _saatTombol(e) {
    const kombinasi = [
      e.ctrlKey || e.metaKey ? "ctrl" : "",
      e.shiftKey ? "shift" : "",
      e.altKey ? "alt" : "",
      e.key.toLowerCase(),
    ].filter(Boolean).join("+");

    const fn = this.pintasan[kombinasi];
    if (fn) { e.preventDefault(); fn(); return; }

    if (kombinasi === "ctrl+/" || kombinasi === "ctrl+shift+7") {
      e.preventDefault(); this._alihKomentar(); return;
    }
    if (e.key === "Tab") { e.preventDefault(); this._tab(e.shiftKey); return; }
    if (e.key === "Enter") { e.preventDefault(); this._enter(); return; }
    if (e.key === "Backspace") { this._hapusMundur(e); return; }
    if (PASANGAN[e.key]) { this._kurung(e); return; }
    if (e.key === ")" || e.key === "]" || e.key === "}") { this._lewatiTutup(e); }
  }

  /* -------------------------------------------------------- penyuntingan */

  _sisip(teks, pilihMulai, pilihAkhir) {
    const t = this.teks;
    // setRangeText menjaga riwayat undo browser tetap utuh. Menulis ulang
    // t.value membuang seluruh riwayat itu, dan Ctrl+Z yang tidak berfungsi
    // adalah cara tercepat kehilangan kepercayaan pada sebuah editor.
    t.setRangeText(teks, t.selectionStart, t.selectionEnd, "end");
    if (pilihMulai !== undefined) {
      t.setSelectionRange(pilihMulai,
                          pilihAkhir === undefined ? pilihMulai : pilihAkhir);
    }
    this._sesudahUbah();
  }

  _sisipRentang(teks, awal, akhir, kursor) {
    this.teks.setRangeText(teks, awal, akhir, "end");
    this.teks.setSelectionRange(kursor, kursor);
    this._sesudahUbah();
  }

  _sesudahUbah() {
    this.gambar();
    this._perbaruiPosisi();
    if (this.saatUbah) this.saatUbah(this.teks.value);
  }

  _batasBaris() {
    const t = this.teks;
    const nilai = t.value;
    const awal = nilai.lastIndexOf("\n", t.selectionStart - 1) + 1;
    let akhir = nilai.indexOf("\n", t.selectionEnd);
    if (akhir < 0) akhir = nilai.length;
    return [awal, akhir];
  }

  _tab(mundur) {
    const t = this.teks;
    const banyakBaris =
      t.value.slice(t.selectionStart, t.selectionEnd).includes("\n");

    if (!banyakBaris && !mundur) { this._sisip(INDENT); return; }

    const [awal, akhir] = this._batasBaris();
    const blok = t.value.slice(awal, akhir);
    let geser = 0;
    const baru = blok.split("\n").map((baris, i) => {
      if (mundur) {
        const buang = baris.startsWith(INDENT)
          ? INDENT.length
          : (baris.match(/^(?: {1,3}|\t)/) || [""])[0].length;
        if (i === 0) geser = -buang;
        return baris.slice(buang);
      }
      if (i === 0) geser = INDENT.length;
      return baris.trim() ? INDENT + baris : baris;
    }).join("\n");

    const mulaiLama = t.selectionStart;
    const akhirLama = t.selectionEnd;
    t.setRangeText(baru, awal, akhir, "preserve");
    t.setSelectionRange(Math.max(awal, mulaiLama + geser),
                        akhirLama + (baru.length - blok.length));
    this.gambar();
    if (this.saatUbah) this.saatUbah(t.value);
  }

  _indentasiBaris(pos) {
    const nilai = this.teks.value;
    const awal = nilai.lastIndexOf("\n", pos - 1) + 1;
    return (nilai.slice(awal, pos).match(/^[ \t]*/) || [""])[0];
  }

  _enter() {
    const t = this.teks;
    const nilai = t.value;
    const pos = t.selectionStart;
    const luar = this._indentasiBaris(pos);
    let indentasi = luar;

    const sebelum = nilai.slice(0, pos).trimEnd();
    if (/[{[(:]$/.test(sebelum)) indentasi += INDENT;

    // Kursor tepat di antara sepasang kurung: buka jadi tiga baris, dengan
    // penutupnya sejajar pembukanya. Ini gerakan yang paling sering dilakukan
    // tangan dan paling melelahkan kalau harus manual.
    const kiri = nilai[pos - 1];
    const kanan = nilai[t.selectionEnd];
    if (kiri && kanan && PASANGAN[kiri] === kanan && "([{".includes(kiri)) {
      this._sisip("\n" + indentasi + "\n" + luar, pos + 1 + indentasi.length);
      return;
    }
    this._sisip("\n" + indentasi);
  }

  _kurung(e) {
    const t = this.teks;
    const buka = e.key;
    const tutup = PASANGAN[buka];
    const terpilih = t.value.slice(t.selectionStart, t.selectionEnd);

    if (terpilih) {           // bungkus yang sedang dipilih
      e.preventDefault();
      const awal = t.selectionStart;
      this._sisip(buka + terpilih + tutup, awal + 1, awal + 1 + terpilih.length);
      return;
    }

    // Kutip di tengah kata bukan pembuka string, melainkan apostrof: "don't",
    // "it's". Menutupnya otomatis di situ selalu salah.
    if (buka === tutup) {
      const kiri = t.value[t.selectionStart - 1] || "";
      const kanan = t.value[t.selectionStart] || "";
      if (kanan === buka) { e.preventDefault(); this._majuSatu(); return; }
      if (/[\w"'`]/.test(kiri) || /\w/.test(kanan)) return;
    }

    e.preventDefault();
    const pos = t.selectionStart;
    this._sisip(buka + tutup, pos + 1);
  }

  _lewatiTutup(e) {
    // Mengetik ")" tepat di depan ")" yang tadi dibuat otomatis: lewati saja,
    // jangan menumpuknya jadi "))".
    if (this.teks.selectionStart === this.teks.selectionEnd
        && this.teks.value[this.teks.selectionStart] === e.key) {
      e.preventDefault();
      this._majuSatu();
    }
  }

  _majuSatu() {
    const p = this.teks.selectionStart + 1;
    this.teks.setSelectionRange(p, p);
    this._perbaruiPosisi();
  }

  _hapusMundur(e) {
    const t = this.teks;
    if (t.selectionStart !== t.selectionEnd) return;
    const pos = t.selectionStart;

    // Hapus sepasang kurung kosong sekaligus.
    const kiri = t.value[pos - 1];
    const kanan = t.value[pos];
    if (kiri && PASANGAN[kiri] === kanan) {
      e.preventDefault();
      this._sisipRentang("", pos - 1, pos + 1, pos - 1);
      return;
    }
    // Di dalam indentasi, hapus satu tingkat penuh, bukan satu spasi.
    const awalBaris = t.value.lastIndexOf("\n", pos - 1) + 1;
    const depan = t.value.slice(awalBaris, pos);
    if (depan.length >= INDENT.length && !depan.trim()
        && depan.length % INDENT.length === 0) {
      e.preventDefault();
      this._sisipRentang("", pos - INDENT.length, pos, pos - INDENT.length);
    }
  }

  _alihKomentar() {
    const tanda = KOMENTAR[this.bahasa] || "# ";
    const potong = tanda.trimEnd();
    const t = this.teks;
    const [awal, akhir] = this._batasBaris();
    const blok = t.value.slice(awal, akhir);
    const baris = blok.split("\n");

    const berisi = baris.filter((b) => b.trim());
    const semuaKomentar = berisi.length > 0
      && berisi.every((b) => b.trimStart().startsWith(potong));

    const baru = baris.map((b) => {
      if (!b.trim()) return b;
      if (semuaKomentar) {
        return b.replace(
          new RegExp("^(\\s*)" + escapeRegex(potong) + " ?"), "$1");
      }
      const depan = (b.match(/^\s*/) || [""])[0];
      return depan + tanda + b.slice(depan.length);
    }).join("\n");

    t.setRangeText(baru, awal, akhir, "select");
    this.gambar();
    if (this.saatUbah) this.saatUbah(t.value);
  }
}

/* ======================================================= kurung berpasangan
 *
 * Deklarasi-deklarasi di bawah tinggal di KAKI berkas, bukan di sebelah
 * `PASANGAN` tempatnya sewajarnya, karena nol baris boleh bertambah di atas
 * kelas `Editor`: tiga anchor telanjang di komentar berkas ini (`(:286)`,
 * `(:318-:319)`) adalah klaim atas nomor baris, dan `TestAlamatKomentar`
 * mengadunya. Deklarasi `const` di tingkat modul sudah selesai dievaluasi
 * sebelum satu pun editor menggambar, jadi urutannya tidak berpengaruh.
 */

/* Kurung = entri `PASANGAN` yang pembuka dan penutupnya BERBEDA.
 *
 * Tiga entri lain di sana (`"`, `'`, dan backtick) menutup DIRINYA SENDIRI,
 * jadi mereka tidak punya kedalaman: tidak ada cara membedakan yang membuka
 * dari yang menutup tanpa menghitung string — dan menghitung string justru
 * yang dilarang di `pisahKurung` di bawah. Menurunkan daftarnya dari
 * `PASANGAN` alih-alih menuliskannya ulang berarti kurung yang ditutup
 * sendiri oleh editor dan kurung yang diwarnai di sini mustahil berbeda
 * pendapat tentang apa yang berpasangan dengan apa. */
const TUTUP_DARI = {};   // pembuka -> penutupnya
const BUKA_DARI = {};    // penutup -> pembukanya
for (const pembuka of Object.keys(PASANGAN)) {
  if (PASANGAN[pembuka] === pembuka) continue;
  TUTUP_DARI[pembuka] = PASANGAN[pembuka];
  BUKA_DARI[PASANGAN[pembuka]] = pembuka;
}

/* Berapa warna yang digilir. Empat sudah cukup jauh untuk mata; kedalaman
 * kelima memakai warna pertama lagi, dan pada kedalaman itu yang menolong
 * memang bukan warna kelima melainkan indentasinya. */
const WARNA_KURUNG = 4;

/* Penanda kurung yatim. Ia menempati slot yang sama dengan angka kedalaman
 * karena keduanya menjawab satu pertanyaan — "kurung ini diwarnai bagaimana"
 * — dan dua slot untuk satu pertanyaan berarti ada keadaan yang bisa ditulis
 * tapi tidak punya arti (yatim DAN berkedalaman 2). */
const YATIM = "yatim";

/** Pecah token kurung dari `token()` jadi potongan yang membawa kedalaman.
 *
 *  Masukan `[[jenis, teks], ...]` dari sorot.js, keluaran
 *  `[[jenis, teks, warna], ...]` dengan `warna`:
 *
 *    null      bukan kurung — mayoritas potongan
 *    0..3      kedalaman % 4; pembuka dan penutup SEPASANG dapat angka sama
 *    "yatim"   penutup tanpa pembuka, atau penutup yang jenisnya tidak cocok
 *
 *  Angka pasangan itu keluar sendiri dari urutan pembacaannya: pembuka
 *  membaca tinggi tumpukan SEBELUM push, penutup membacanya SESUDAH pop.
 *
 *  Tiga sifat yang mengikat:
 *
 *  1. HANYA jenis `operator` yang dihitung. Di kurikulum ini ada 2.270
 *     kurung di dalam token `string`, 981 di `komentar`, dan 83 di `khusus`;
 *     satu `(` di dalam komentar yang ikut dihitung meracuni kedalaman
 *     SELURUH kode sesudahnya, dan yang terlihat pelajar cuma warna yang
 *     terasa acak — tanpa satu pun error yang bisa dicari sebabnya.
 *  2. Pasangannya dihitung per jenis: `]` tidak menutup `(`. Ia yatim, dan
 *     `(`-nya tetap terbuka, karena itulah yang sebenarnya terjadi pada
 *     kodenya.
 *  3. Kedalaman tidak pernah negatif — tumpukan cuma dipangkas kalau
 *     puncaknya memang pembuka yang cocok.
 *
 *  Dan satu syarat yang sama sekali bukan soal warna: GABUNGAN seluruh
 *  `teks` keluaran WAJIB identik byte-per-byte dengan gabungan masukannya.
 *  Lapisan sorot ini duduk persis di bawah textarea yang transparan (lihat
 *  blok `.editor-lapis > pre, > textarea` di gaya.css); satu karakter
 *  selisih dan kursor mendarat di huruf yang salah pada baris panjang, tanpa
 *  satu pun error di mana pun. Itu pula sebabnya span `operator` DIBELAH
 *  alih-alih diwarnai utuh: dari 40.287 token operator ber-kurung di
 *  kurikulum ini, 9.045 rengket dengan karakter lain — `):` di ujung
 *  `def f(a, b):` salah satunya, dan mewarnainya utuh berarti ikut mewarnai
 *  titik duanya. */
export function pisahKurung(daftar) {
  const hasil = [];
  const tumpukan = [];
  for (const pasang of daftar || []) {
    const jenis = pasang[0];
    const teks = pasang[1];
    if (jenis !== "operator") {
      hasil.push([jenis, teks, null]);
      continue;
    }

    let mulai = 0;
    for (let i = 0; i < teks.length; i++) {
      const c = teks[i];
      const buka = TUTUP_DARI[c] !== undefined;
      const tutup = BUKA_DARI[c] !== undefined;
      if (!buka && !tutup) continue;

      // Apa pun di antara dua kurung tetap satu potongan `operator` biasa.
      if (i > mulai) hasil.push([jenis, teks.slice(mulai, i), null]);
      mulai = i + 1;

      if (buka) {
        hasil.push([jenis, c, tumpukan.length % WARNA_KURUNG]);
        tumpukan.push(c);
      } else if (tumpukan[tumpukan.length - 1] === BUKA_DARI[c]) {
        tumpukan.pop();
        hasil.push([jenis, c, tumpukan.length % WARNA_KURUNG]);
      } else {
        hasil.push([jenis, c, YATIM]);
      }
    }
    // Ekor sesudah kurung terakhir. Token tanpa kurung sama sekali lewat di
    // sini utuh, satu potongan, persis seperti sebelum fitur ini ada.
    if (mulai < teks.length) hasil.push([jenis, teks.slice(mulai), null]);
  }
  return hasil;
}

/** Letak pita baris aktif di dalam `.editor-lapis`, dalam piksel angka murni.
 *
 *  Murni dan tanpa DOM — itulah yang membuatnya bisa diadu dari Node tanpa
 *  peramban sama sekali (`TestPitaBarisAktif` di tests/test_web.py). Yang
 *  memanggilnya satu: `_gambarPita()`, yang membaca ketiga angka masukannya
 *  dari gaya terhitung.
 *
 *  `tinggi` SELALU `tinggiBaris` apa adanya, dan tidak pernah dikoreksi oleh
 *  `baris`: pita setinggi dua baris berbohong soal di mana kursornya berdiri,
 *  dan pita setinggi nol tidak menandai apa pun.
 *
 *  `atas` TIDAK dijepit ke nol, dan itu syarat, bukan kelalaian. Kalau baris
 *  kursor sudah tergulir keluar dari pandangan, hasilnya memang negatif, dan
 *  `overflow: hidden` pada `.editor-lapis` memotongnya sampai habis — persis
 *  yang benar, karena yang tidak terlihat memang tidak boleh ditandai.
 *  Menjepitnya dengan `Math.max(0, ...)` justru memarkir pita di tepi atas
 *  sebagai garis macet yang mengaku "baris aktifmu di sini" padahal kursornya
 *  jauh di atas layar; satu-satunya hal yang lebih buruk daripada tidak ada
 *  penanda adalah penanda yang menunjuk tempat yang salah. */
export function posisiPita({ baris, tinggiBaris, paddingAtas, scrollTop }) {
  const n = Math.max(1, baris);
  return {
    atas: paddingAtas + (n - 1) * tinggiBaris - scrollTop,
    tinggi: tinggiBaris,
  };
}

/* ========================================================= pemandu indentasi
 *
 * Banner sendiri, bukan tumpangan di blok `kurung berpasangan` di atas: yang
 * di bawah ini tidak menghitung satu pun kurung, dan judul bagian yang
 * menaungi fungsi yang bukan bagiannya berhenti memberi tahu apa pun.
 */

/** Belah deretan spasi pembuka baris jadi potongan ber-jenis `indentasi`.
 *
 *  Masukan dan keluarannya sebentuk dengan `pisahKurung()` di atas —
 *  `[[jenis, teks, warna], ...]` — dan itu bukan kebetulan: keduanya dirangkai
 *  jadi satu di `_fragmenKurung()`. Kelas CSS-nya lahir tanpa satu baris pun
 *  berubah di sorot.js, karena `keFragmen()` memetakan setiap jenis yang BUKAN
 *  `teks` jadi `<span class="tk-<jenis>">`. Melahirkannya di pemindai justru
 *  yang dilarang: ada DUA implementasi pemindai (sorot.js dan inti/sorot.py)
 *  dan `TestPenyorotJavaScript` mengadu keluaran keduanya byte-per-byte.
 *
 *  URUTANNYA — fungsi ini di LUAR, `pisahKurung` di dalam — bukan soal
 *  benar-salah: dibalik, keluarannya diukur IDENTIK, nol beda atas 1.399 blok
 *  kode kurikulum dan keempat belas kasus `SIFAT` pagarnya. Potongan
 *  `indentasi` cuma berisi spasi, jadi tidak ada satu kurung pun yang bisa
 *  bersembunyi di dalamnya.
 *
 *  Yang mengikat dua invarian yang MEMBUAT keduanya setara, dan keduanya
 *  dipagar `test_invarian_slot_tiga_atas_korpus`: `korpusWarnaBerNewline` nol
 *  (tak satu pun potongan BERWARNA memuat baris baru, jadi pembelahan di sini
 *  mustahil menyentuh slot ketiga yang bukan `null` — dan dengan itu atribut
 *  `data-warna` di `_fragmenKurung()` tidak perlu tahu fungsi ini ada) dan
 *  `korpusIndenRengket` nol. Begitu salah satunya memerah, yang ditulis ulang
 *  paragraf ini — bukan rangkaiannya.
 *
 *  Tiga hal yang TIDAK dikerjakannya, dan ketiganya putusan:
 *
 *  1. Ia tidak tahu apa pun soal lebar, satuan `ch`, atau angka 4. Geometri
 *     tinggal di SATU tempat, dan tempat itu aturan `.tk-indentasi` di
 *     gaya.css — yang sama yang sudah memegang `tab-size` dan `line-height`
 *     lapisan ini. Dua tempat yang mengukur satu hal akan berbeda suatu hari.
 *  2. Baris yang dibuka TAB tidak dibelah sama sekali. Lebar sebuah tab
 *     ditentukan `tab-size`, bukan jumlah karakternya, jadi pemandu yang
 *     digambar per karakter mendarat di kolom yang bukan tempat tingkatnya
 *     mulai — penanda yang salah, bukan penanda yang kurang.
 *  3. Deret spasi yang MENGAKHIRI barisnya bukan indentasi: kalau sesudahnya
 *     cuma `\n` atau habis, ia sisa baris kosong dan tidak menandai kedalaman
 *     apa pun. Korpus kurikulum tidak punya satu pun baris seperti itu, tapi
 *     yang digambar editor ini teks PELAJAR, yang bisa memuatnya.
 *
 *  Dan satu syarat yang sama dengan milik `pisahKurung`: GABUNGAN seluruh
 *  `teks` keluaran WAJIB identik byte-per-byte dengan gabungan masukannya,
 *  karena lapisan ini duduk persis di bawah textarea transparan. Ia dipagari
 *  pagar yang SAMA, atas seluruh blok kode dan solusi kurikulum, sebab kedua
 *  fungsi ini memang satu rangkaian. */
export function pisahInden(daftar) {
  // Dihitung atas teks GABUNGAN, bukan per potongan, supaya satu deret yang
  // telanjur terpotong dua token tetap terbaca sebagai satu deret. Lookahead
  // `[^ \n]`-lah yang menolak spasi sisa di baris kosong (butir 3 di atas).
  const utuh = (daftar || []).map((p) => p[1]).join("");
  const deret = [];
  const pola = /(^|\n)( +)(?=[^ \n])/g;
  for (let m; (m = pola.exec(utuh)) !== null; ) {
    const mulai = m.index + m[1].length;
    deret.push([mulai, mulai + m[2].length]);
  }

  const hasil = [];
  let ke = 0;                       // deret pertama yang belum terlewati
  let pos = 0;                      // offset potongan ini di dalam `utuh`
  for (const pasang of daftar || []) {
    const jenis = pasang[0];
    const teks = pasang[1];
    const warna = pasang[2] === undefined ? null : pasang[2];
    // Potongan berteks kosong diteruskan, bukan dibuang: susun-ulang memang
    // tetap identik tanpanya, tapi `_fragmenKurung()` memasangkan potongan
    // ke-i dengan simpul ke-i, dan jumlah yang berubah di tengah jalan adalah
    // kelas kegagalan yang tidak menimbulkan error di mana pun.
    if (!teks) { hasil.push([jenis, teks, warna]); continue; }

    const ujung = pos + teks.length;
    while (ke < deret.length && deret[ke][1] <= pos) ke++;
    let batas = pos;
    for (let j = ke; j < deret.length && deret[j][0] < ujung; j++) {
      const a = Math.max(pos, deret[j][0]);
      const b = Math.min(ujung, deret[j][1]);
      if (a > batas) hasil.push([jenis, teks.slice(batas - pos, a - pos), warna]);
      hasil.push(["indentasi", teks.slice(a - pos, b - pos), null]);
      batas = b;
    }
    if (batas < ujung) hasil.push([jenis, teks.slice(batas - pos), warna]);
    pos = ujung;
  }
  return hasil;
}
