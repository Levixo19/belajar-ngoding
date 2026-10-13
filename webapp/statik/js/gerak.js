/* Mesin gerak: pegas, urutan, pemicu, dan isyarat sentuh.
 *
 * Referensinya Motion (https://motion.dev). Yang dipinjam IDE-nya, bukan
 * kodenya — memasang librarynya berarti membatalkan janji "tanpa dependensi
 * luar" yang jadi dasar seluruh arsitektur ini (lihat AGENTS.md). Empat
 * gagasan yang ditiru:
 *
 *   · pegas sebagai satuan gerak bawaan, bukan "durasi + kurva". Gerak yang
 *     dijelaskan sebagai "sampai dalam 0,22 detik, pantul 6%" tetap masuk akal
 *     saat jaraknya berubah; "220ms ease-out" tidak.
 *   · urutan (stagger) sebagai fungsi indeks, bukan CSS nth-child.
 *   · pemicu (inView, scroll) terpisah dari animasinya.
 *   · isyarat (press, hover) dipasang dari JS, jadi bisa memakai pegas yang
 *     sama dan bisa dimatikan bersama yang lain.
 *
 * CARA KERJANYA. Solver pegas dijalankan SEKALI di depan untuk menghasilkan
 * easing `linear(...)` — sederet titik sampel dari kurvanya. Setelah itu
 * animasinya diserahkan bulat-bulat ke Web Animations API, yang menjalankannya
 * di compositor. Jadi gerak pegasnya sungguhan, tapi tidak ada satu frame pun
 * yang dihitung di thread utama: tiga puluh kartu yang masuk berbarengan tidak
 * membuat ketikan di editor tersendat. Hasil solvernya di-cache, karena yang
 * dipakai cuma segelintir pegas yang sama berulang kali.
 *
 * ATURAN GERAK — sama persis dengan yang tertulis di gaya.css, diulang di sini
 * karena berkas inilah yang paling gampang dipakai untuk melanggarnya:
 *
 *   · gerak interaksi menjawab dalam <= ~220 md. Yang dibatasi adalah waktu
 *     sampai gerakan TERLIHAT selesai (`durasiTampak`), bukan ekor pegasnya —
 *     ekor yang amplitudonya di bawah satu piksel tidak dilihat siapa pun.
 *   · gerak ambien minimal 3 detik dan amplitudonya kecil.
 *   · tidak ada satu pun animasi yang berkedip: opacity selalu bergerak satu
 *     arah dalam satu animasi.
 *   · `prefers-reduced-motion` dan [data-gerak] mematikan atau meredamnya,
 *     dan animasi tidak pernah jadi satu-satunya cara sebuah elemen terlihat.
 *
 * Separuh atas berkas ini MURNI — tanpa DOM sama sekali — supaya solvernya
 * bisa diadu dengan hasil hitungan tangan langsung di Node. Lihat
 * tests/test_web.py, kelas TestMesinGerak.
 *
 * Importir: inti.js, aplikasi.js, editor.js, dan seluruh layar-*.js.
 */

/* ========================================================== bagian murni */

export const DETIK = 1000;

export function jepit(n, bawah = 0, atas = 1) {
  return n < bawah ? bawah : n > atas ? atas : n;
}

export function antara(a, b, t) {
  return a + (b - a) * t;
}

/** Petakan angka dari satu rentang ke rentang lain — padanan `transform()`
 *  di Motion. Dipakai untuk hal seperti "posisi gulir 0–400px jadi opacity
 *  0–1" tanpa menulis ulang aritmetikanya tiap kali. */
export function petakan(nilai, dari, ke, { jepitHasil = true } = {}) {
  const [a0, a1] = dari;
  const [b0, b1] = ke;
  const t = a1 === a0 ? 0 : (nilai - a0) / (a1 - a0);
  const hasil = antara(b0, b1, t);
  if (!jepitHasil) return hasil;
  return b1 >= b0 ? jepit(hasil, b0, b1) : jepit(hasil, b1, b0);
}

/* ------------------------------------------------------------------ pegas
 *
 * Sebuah pegas dijelaskan dengan dua angka yang bisa dibayangkan:
 *
 *   durasiTampak  berapa detik sampai gerakannya TERLIHAT selesai
 *   pantul        0 = berhenti mulus, 0.3 = melewati tujuan sedikit lalu balik
 *
 * "Terlihat selesai" didefinisikan sebagai saat pertama menempuh 99% jarak.
 * Definisi itu dipilih setelah yang lebih jelas gagal: "waktu pertama
 * MENYENTUH sasaran" punya rumus tertutup yang rapi, t1 = (pi - acos(zeta)) /
 * omega_d, tapi untuk pegas yang nyaris tak berpantul kurvanya merayap ke
 * sasaran secara asimtotik — ia sudah 99,5% sampai jauh sebelum t1, sehingga
 * angka yang diminta tidak lagi mengendalikan apa pun yang terlihat. Dengan
 * pantul 0, "sampai dalam 0,28 detik" dan "sampai dalam 0,19 detik" keluar
 * sebagai animasi yang sama persis.
 *
 * 99% tidak punya rumus tertutup, tapi tidak membutuhkannya. Kurva pegas
 * berskala rapi terhadap waktu: f(t; omega_0, zeta) = g(omega_0 * t; zeta).
 * Jadi cukup dicari SEKALI, secara numerik, pada tiap zeta, di mana kurva
 * satuan g menembus 99% — sebut tau. Sesudah itu omega_0 = tau /
 * durasiTampak, dan kekakuan = massa * omega_0^2, redaman = 2 * zeta *
 * massa * omega_0. Hasilnya dicache per zeta.
 *
 * Kekakuan dan redaman mentah tetap bisa diberikan langsung kalau memang itu
 * yang diinginkan — tapi hampir tidak pernah, karena keduanya tidak berarti
 * apa-apa sampai disimulasikan.
 */

export const PEGAS = {
  /* Menjawab sentuhan: secepat mungkin tanpa terasa mendadak. */
  jawab:  { durasiTampak: 0.19, pantul: 0.05 },
  /* Bawaan untuk apa pun yang masuk ke layar. */
  halus:  { durasiTampak: 0.28, pantul: 0.00 },
  /* Untuk hal yang layak dirayakan sedikit: badge, lencana LULUS. Pantulnya
     dijaga di 0.26 karena pantulan itu mahal — tiap tambahan pantul
     memperpanjang ekor pegasnya jauh lebih cepat daripada yang diduga. */
  lentur: { durasiTampak: 0.22, pantul: 0.26 },
  /* Untuk elemen besar yang berpindah tempat — pantulan di benda besar
     terasa seperti kesalahan, bukan kelincahan. */
  berat:  { durasiTampak: 0.40, pantul: 0.00 },
  /* Angka yang berjalan naik dan bilah kemajuan. */
  panjang:{ durasiTampak: 0.60, pantul: 0.03 },
};

const PANTUL_BAWAAN = 0.06;
const DURASI_TAMPAK_BAWAAN = 0.3;

/** Terjemahkan pemerian pegas yang ramah manusia jadi parameter fisikanya. */
export function paramPegas(opsi = {}) {
  const massa = opsi.massa > 0 ? opsi.massa : 1;
  const kecepatan = Number(opsi.kecepatan) || 0;

  if (opsi.kekakuan || opsi.redaman) {
    return {
      kekakuan: opsi.kekakuan > 0 ? opsi.kekakuan : 170,
      redaman: opsi.redaman >= 0 ? opsi.redaman : 26,
      massa,
      kecepatan,
    };
  }

  const durasiTampak = opsi.durasiTampak > 0
    ? opsi.durasiTampak : DURASI_TAMPAK_BAWAAN;
  const pantul = opsi.pantul === undefined ? PANTUL_BAWAAN : opsi.pantul;
  // zeta = 1 berarti teredam kritis. 0.99 sudah tak terbedakan dari 1 oleh
  // mata, dan menghindarkan cabang kasus khusus di dalam solvernya.
  const zeta = jepit(1 - pantul, 0.05, 0.99);
  const omega0 = tauSampai(zeta) / durasiTampak;

  return {
    kekakuan: massa * omega0 * omega0,
    redaman: 2 * zeta * massa * omega0,
    massa,
    kecepatan,
  };
}

const _tau = new Map();

/** Pada kurva pegas satuan (omega_0 = 1), di waktu berapa ia menembus 99%?
 *
 *  Dicari sekali per zeta lalu disimpan: nilainya cuma bergantung pada zeta,
 *  dan zeta yang dipakai di seluruh aplikasi ini bisa dihitung dengan jari
 *  satu tangan. */
export function tauSampai(zeta, ambang = 0.99) {
  const kunci = `${zeta.toFixed(4)}|${ambang}`;
  const ada = _tau.get(kunci);
  if (ada !== undefined) return ada;

  const g = jalurPegas({ kekakuan: 1, redaman: 2 * zeta, massa: 1,
                         kecepatan: 0 });
  const langkah = 0.002;
  let hasil = 60;
  for (let t = 0; t <= 60; t += langkah) {
    if (g(t) >= ambang) { hasil = t; break; }
  }
  _tau.set(kunci, hasil);
  return hasil;
}

/** Kembalikan fungsi t(detik) -> kemajuan 0..1 untuk sebuah pegas.
 *
 *  Bentuk tertutup, bukan integrasi langkah demi langkah: tiga kasus (teredam
 *  kurang, kritis, lebih) masing-masing punya penyelesaian eksak, dan memakai
 *  rumusnya berarti hasilnya tidak bergantung pada ukuran langkah. */
export function jalurPegas(p) {
  const { kekakuan, redaman, massa, kecepatan } = p;
  const omega0 = Math.sqrt(kekakuan / massa);
  const zeta = redaman / (2 * Math.sqrt(kekakuan * massa));

  if (zeta < 1 - 1e-6) {
    const omegaD = omega0 * Math.sqrt(1 - zeta * zeta);
    const b = (zeta * omega0 - kecepatan) / omegaD;
    return (t) => 1 - Math.exp(-zeta * omega0 * t)
      * (Math.cos(omegaD * t) + b * Math.sin(omegaD * t));
  }
  if (zeta < 1 + 1e-6) {
    return (t) => 1 - Math.exp(-omega0 * t)
      * (1 + (omega0 - kecepatan) * t);
  }
  const akar = omega0 * Math.sqrt(zeta * zeta - 1);
  const r1 = -zeta * omega0 + akar;
  const r2 = -zeta * omega0 - akar;
  const c1 = (-kecepatan - r2) / (r1 - r2);
  const c2 = 1 - c1;
  return (t) => 1 - (c1 * Math.exp(r1 * t) + c2 * Math.exp(r2 * t));
}

const _kurvaTersimpan = new Map();

/* Di bawah 0,5% dari jarak tempuh, gerakan sudah lebih kecil daripada satu
   piksel untuk hampir semua animasi di aplikasi ini: perjalanan terpanjang
   yang ada di sini sekitar 40 px, dan 0,5% darinya adalah 0,2 px. Meneruskan
   sesudah itu cuma memperpanjang durasi tanpa ada yang melihat bedanya —
   dan ekor pegas yang panjang itulah yang membuat animasi pegas terkenal
   terasa lamban padahal puncaknya sudah lewat sejak lama. */
const DIAM = 0.005;
const BATAS_DETIK = 6;

/** Ubah sebuah pegas jadi { durasi, easing } yang bisa dipakai WAAPI.
 *
 *  easing-nya berupa `linear(a, b, c, ...)`: daftar sampel kurva pegasnya.
 *  Browser menyambungkan titik-titik itu jadi kurva, dan karena hasilnya
 *  easing biasa, animasinya berjalan di compositor. */
export function kurvaPegas(opsi = {}) {
  const p = paramPegas(opsi);
  const kunci = `${p.kekakuan.toFixed(4)}|${p.redaman.toFixed(4)}`
    + `|${p.massa}|${p.kecepatan}`;
  const tersimpan = _kurvaTersimpan.get(kunci);
  if (tersimpan) return tersimpan;

  const f = jalurPegas(p);
  const langkah = 1 / 240;
  let akhir = langkah;
  for (let t = langkah; t <= BATAS_DETIK; t += langkah) {
    if (Math.abs(1 - f(t)) > DIAM) akhir = t;
  }
  akhir = Math.min(akhir + langkah * 2, BATAS_DETIK);

  // Satu titik tiap ~16 md sudah melewati apa yang bisa dibedakan mata pada
  // 60 Hz; batas atasnya menjaga panjang stringnya tetap wajar.
  const titik = Math.min(140, Math.max(8, Math.round(akhir * 60)));
  const nilai = [];
  for (let i = 0; i <= titik; i++) {
    nilai.push(Math.round(f((i / titik) * akhir) * 10000) / 10000);
  }
  nilai[0] = 0;
  nilai[titik] = 1;

  const hasil = {
    durasi: Math.max(1, Math.round(akhir * DETIK)),
    easing: `linear(${nilai.join(",")})`,
    titik: nilai,
    param: p,
  };
  _kurvaTersimpan.set(kunci, hasil);
  return hasil;
}

/* ----------------------------------------------------------------- urutan */

/** Bangun fungsi indeks -> penundaan (md), padanan `stagger()` di Motion.
 *
 *  Bedanya satu: ada `maks`. Motion mengalikan jarak dengan penundaan begitu
 *  saja, jadi daftar 60 baris berarti baris terakhir menunggu dua detik.
 *  Di sini seluruh urutan dipadatkan supaya tidak pernah melewati `maks` —
 *  daftar panjang tetap terasa berurutan, tapi tidak pernah bikin menunggu. */
export function berurut(jumlah, opsi = {}) {
  const { mulai = 0, per = 34, dari = "awal", maks = 300 } = opsi;
  const n = Math.max(1, jumlah);
  const pusat = dari === "akhir" ? n - 1
    : dari === "tengah" ? (n - 1) / 2
    : typeof dari === "number" ? dari : 0;
  const jarakMaks = Math.max(pusat, n - 1 - pusat) || 1;
  const langkah = Math.min(per, maks / jarakMaks);
  return (i) => mulai + Math.abs(i - pusat) * langkah;
}

/* ======================================================== bagian ber-DOM */

const ADA_DOM = typeof document !== "undefined"
  && typeof window !== "undefined";

const _kurangiGerak = ADA_DOM && window.matchMedia
  ? window.matchMedia("(prefers-reduced-motion: reduce)")
  : null;

/* Browser yang belum mengenal easing `linear()` (Safari lama) tetap harus
   dapat animasi, cuma tanpa pantulannya. */
const DUKUNG_LINEAR = ADA_DOM && typeof CSS !== "undefined"
  && typeof CSS.supports === "function"
  && CSS.supports("animation-timing-function", "linear(0, 1)");

export const MULUS = "cubic-bezier(.32,.72,.36,1)";
export const KELUAR = "cubic-bezier(.4,0,1,1)";

/** "penuh" | "halus" | "mati".
 *
 *  Setelan sistem menang atas apa pun: kalau pemakainya sudah bilang ke sistem
 *  operasinya bahwa ia ingin gerak dikurangi, tidak ada saklar di halaman ini
 *  yang berhak membantahnya. */
export function tingkatGerak() {
  if (!ADA_DOM) return "mati";
  if (_kurangiGerak && _kurangiGerak.matches) return "mati";
  const d = document.documentElement.dataset.gerak;
  if (d === "mati") return "mati";
  if (d === "halus") return "halus";
  return "penuh";
}

export function adaGerak() { return tingkatGerak() !== "mati"; }
export function gerakPenuh() { return tingkatGerak() === "penuh"; }

/** Pengali amplitudo. Di tingkat "halus" jaraknya dipendekkan, bukan
 *  durasinya diperlambat: gerakan pendek yang tetap cepat terasa tenang,
 *  gerakan panjang yang diperlambat justru terasa berat. */
export function skala() {
  const t = tingkatGerak();
  return t === "penuh" ? 1 : t === "halus" ? 0.45 : 0;
}

/** Beri tahu saat tingkat gerak berubah — termasuk saat pemakainya mengubah
 *  setelan sistem di tengah sesi. */
export function saatGerakBerubah(fn) {
  if (!_kurangiGerak) return () => {};
  const bungkus = () => fn(tingkatGerak());
  _kurangiGerak.addEventListener("change", bungkus);
  return () => _kurangiGerak.removeEventListener("change", bungkus);
}

function keDaftar(x) {
  if (!x || !ADA_DOM) return [];
  if (x instanceof Element) return [x];
  if (typeof x.length === "number") {
    return Array.from(x).filter((e) => e instanceof Element);
  }
  return [];
}

function kendaliKosong() {
  return {
    animasi: [],
    selesai: Promise.resolve(),
    batal() {},
    tuntaskan() {},
  };
}

function gabungKendali(daftar) {
  const semua = daftar.flatMap((k) => k.animasi);
  return {
    animasi: semua,
    selesai: Promise.all(daftar.map((k) => k.selesai)),
    batal() { for (const k of daftar) k.batal(); },
    tuntaskan() { for (const k of daftar) k.tuntaskan(); },
  };
}

/** Padanan `animate()` di Motion.
 *
 *  @param sasaran  Element, NodeList, atau array Element
 *  @param bingkai  keyframes gaya WAAPI: { opacity: [0, 1], transform: [...] }
 *  @param opsi
 *     pegas     nama dari PEGAS, atau { durasiTampak, pantul, ... }
 *     durasi    md — mengalahkan durasi hasil pegas kalau diisi
 *     delay     md, atau fungsi (i, jumlah) -> md untuk urutan
 *     easing    dipakai kalau tidak ada pegas
 *     isi       nilai `fill` WAAPI; bawaannya "backwards"
 *     paksa     jalankan walaupun gerak sedang dimatikan (dipakai sangat
 *               jarang: hanya untuk gerak yang MENGGANTIKAN teks, bukan
 *               menghiasinya)
 *
 *  BINGKAI HARUS BERAKHIR DI KEADAAN ALAMI ELEMENNYA. Kalau gerak dimatikan,
 *  fungsi ini tidak menyentuh apa pun dan langsung selesai — jadi keadaan
 *  akhir animasi tidak boleh jadi satu-satunya cara elemen itu terlihat.
 */
export function animasi(sasaran, bingkai, opsi = {}) {
  const daftar = keDaftar(sasaran);
  if (!daftar.length) return kendaliKosong();
  if (!adaGerak() && !opsi.paksa) return kendaliKosong();
  if (typeof daftar[0].animate !== "function") return kendaliKosong();

  let durasi = opsi.durasi;
  let easing = opsi.easing || MULUS;

  const minta = opsi.pegas;
  if (minta) {
    const k = kurvaPegas(typeof minta === "string" ? (PEGAS[minta] || {}) : minta);
    if (durasi === undefined) durasi = k.durasi;
    if (DUKUNG_LINEAR) easing = k.easing;
  }
  if (durasi === undefined) durasi = 220;

  const hitungDelay = typeof opsi.delay === "function"
    ? opsi.delay
    : () => opsi.delay || 0;

  const jalan = daftar.map((el, i) => el.animate(bingkai, {
    duration: durasi,
    delay: hitungDelay(i, daftar.length),
    easing,
    fill: opsi.isi || "backwards",
    iterations: opsi.ulang || 1,
    direction: opsi.arah || "normal",
    composite: opsi.gabung || "replace",
  }));

  // `finished` menolak kalau animasinya dibatalkan. Itu bukan kesalahan —
  // membatalkan animasi adalah hal yang normal terjadi saat layar berganti —
  // jadi jangan biarkan ia jadi unhandled rejection yang mengotori konsol.
  const selesai = Promise.all(jalan.map((a) => a.finished.catch(() => {})));
  if (opsi.saatSelesai) selesai.then(() => opsi.saatSelesai());

  return {
    animasi: jalan,
    selesai,
    batal() { for (const a of jalan) a.cancel(); },
    tuntaskan() { for (const a of jalan) { try { a.finish(); } catch (e) { /* sudah usai */ } } },
  };
}

/* -------------------------------------------------------- masuk & keluar */

/** Satu elemen masuk: naik sedikit sambil muncul. Tidak ada yang meluncur
 *  dari samping — itu memberi kesan halamannya berpindah tempat, padahal yang
 *  berganti cuma isinya. */
export function masuk(sasaran, opsi = {}) {
  const s = skala();
  const geser = (opsi.geser === undefined ? 10 : opsi.geser) * s;
  const zum = antara(1, opsi.zum === undefined ? 0.988 : opsi.zum, s);
  return animasi(sasaran, {
    opacity: [0, 1],
    transform: [
      `translate3d(0, ${geser.toFixed(2)}px, 0) scale(${zum.toFixed(4)})`,
      "none",
    ],
  }, { pegas: "halus", ...opsi });
}

/** Kebalikannya, untuk sesuatu yang akan dibuang. Sengaja lebih cepat
 *  daripada masuknya: menunggu sesuatu pergi selalu terasa lebih lama
 *  daripada menunggu sesuatu datang. */
export function keluar(sasaran, opsi = {}) {
  const geser = (opsi.geser === undefined ? -7 : opsi.geser) * skala();
  return animasi(sasaran, {
    opacity: [1, 0],
    transform: ["none", `translate3d(0, ${geser.toFixed(2)}px, 0)`],
  }, { durasi: 130, easing: KELUAR, isi: "forwards", ...opsi });
}

/** Sekumpulan elemen masuk berurutan. */
export function masukBerurut(sasaran, opsi = {}) {
  const daftar = keDaftar(sasaran);
  if (!daftar.length) return kendaliKosong();
  const delay = berurut(daftar.length, opsi);
  return gabungKendali(
    daftar.map((el, i) => masuk(el, { ...opsi, delay: delay(i) })));
}

/* ------------------------------------------------------------- pemicu */

/** Padanan `inView()` di Motion. Callback boleh mengembalikan fungsi; fungsi
 *  itu dipanggil saat elemennya keluar lagi dari layar. */
export function saatTampak(sasaran, saatMasuk, opsi = {}) {
  const daftar = keDaftar(sasaran);
  if (!daftar.length) return () => {};
  if (typeof IntersectionObserver === "undefined") {
    for (const el of daftar) saatMasuk(el);
    return () => {};
  }
  const { tepi = "0px 0px -6% 0px", bagian = 0.1, sekali = true } = opsi;
  const saatKeluar = new Map();

  const pengamat = new IntersectionObserver((catatan) => {
    for (const c of catatan) {
      if (c.isIntersecting) {
        const balik = saatMasuk(c.target, c);
        if (typeof balik === "function") saatKeluar.set(c.target, balik);
        if (sekali) pengamat.unobserve(c.target);
      } else {
        const balik = saatKeluar.get(c.target);
        if (balik) { balik(c.target); saatKeluar.delete(c.target); }
      }
    }
  }, { rootMargin: tepi, threshold: bagian });

  for (const el of daftar) pengamat.observe(el);
  return () => pengamat.disconnect();
}

/* Pengaman: kalau karena satu dan lain hal pengamatnya tidak pernah menyala,
   apa pun yang sempat disembunyikan harus muncul kembali sendiri. Elemen yang
   tak terlihat selamanya adalah kegagalan yang jauh lebih buruk daripada
   animasi yang terlewat.

   TAPI pengaman ini tidak boleh asal menyala. Versi pertamanya mengosongkan
   opacity SEMUA anak pada detik 2,5 tanpa mematikan pemicunya — termasuk anak
   yang masih di bawah lipatan layar dan masih diamati. Akibatnya: pembaca
   menggulir turun, bagian itu tergambar penuh dulu, lalu callback pengamatnya
   menyala dan memasang animasi masuk ber-fill "backwards" yang menjatuhkannya
   kembali ke opacity 0 sebelum memudar naik lagi. Itu KEDIPAN, tepat di bawah
   mata orang yang sedang membaca — hal yang dilarang tanpa syarat di seluruh
   berkas ini.

   Yang benar: pengamannya bertanya "apakah pengamat ini pernah menyala sama
   sekali?". Kalau pernah, IntersectionObserver terbukti bekerja dan tidak ada
   yang perlu diselamatkan — biarkan sisanya diungkap saat tergulir, seperti
   yang dimaksudkan. Kalau belum pernah, sesuatu memang salah (atau seluruh
   wadahnya masih jauh di bawah lipatan); ungkap semuanya sekaligus DAN matikan
   pemicunya, supaya tidak ada satu pun animasi masuk yang menyusul di atas
   elemen yang sudah terlihat. */
const JAGA_MD = 2500;

/** Ungkap anak-anak sebuah wadah begitu tergulir ke layar, berurutan. */
export function ungkap(wadah, opsi = {}) {
  const induk = keDaftar(wadah)[0];
  if (!induk) return () => {};
  const anak = keDaftar(opsi.pilih ? induk.querySelectorAll(opsi.pilih)
                                   : induk.children);
  if (!anak.length || !adaGerak()) return () => {};

  for (const el of anak) el.style.opacity = "0";
  const delay = berurut(anak.length, opsi);
  const nomor = new Map(anak.map((el, i) => [el, i]));

  let pernahMenyala = false;
  let menyerah = false;
  let hentikan = () => {};

  const jaga = setTimeout(() => {
    if (pernahMenyala) return;
    menyerah = true;
    hentikan();
    for (const el of anak) el.style.opacity = "";
  }, JAGA_MD);

  hentikan = saatTampak(anak, (el) => {
    if (menyerah) return;
    pernahMenyala = true;
    el.style.opacity = "";
    masuk(el, { ...opsi, delay: delay(nomor.get(el) || 0) });
  }, opsi);

  return () => { clearTimeout(jaga); hentikan(); };
}

/** Padanan `scroll()` versi ringkas: panggil fungsi tiap kali posisi gulir
 *  berubah, paling banyak sekali per frame. */
export function saatGulir(fn, opsi = {}) {
  if (!ADA_DOM) return () => {};
  const sumber = opsi.sumber || window;
  let menunggu = false;
  let sebelumnya = 0;

  const hitung = () => {
    menunggu = false;
    const atas = sumber === window
      ? (window.scrollY || document.documentElement.scrollTop || 0)
      : sumber.scrollTop;
    const total = sumber === window
      ? document.documentElement.scrollHeight - window.innerHeight
      : sumber.scrollHeight - sumber.clientHeight;
    fn({
      atas,
      maju: total > 0 ? jepit(atas / total) : 0,
      turun: atas > sebelumnya,
    });
    sebelumnya = atas;
  };

  const saat = () => {
    if (menunggu) return;
    menunggu = true;
    requestAnimationFrame(hitung);
  };

  sumber.addEventListener("scroll", saat, { passive: true });
  window.addEventListener("resize", saat, { passive: true });
  hitung();
  return () => {
    sumber.removeEventListener("scroll", saat);
    window.removeEventListener("resize", saat);
  };
}

/* -------------------------------------------------------------- tata (FLIP)
 *
 * Animasi perpindahan tata letak dengan cara yang sama seperti Motion: ukur
 * posisi lama, biarkan perubahannya terjadi, ukur posisi baru, lalu balikkan
 * selisihnya dengan transform dan lepaskan. Yang dianimasikan cuma transform,
 * jadi tidak ada satu pun perhitungan tata letak per frame. */
export function tata(sasaran, ubah, opsi = {}) {
  const daftar = keDaftar(sasaran);
  if (!daftar.length || !adaGerak()) {
    ubah();
    return kendaliKosong();
  }
  const sebelum = daftar.map((el) => el.getBoundingClientRect());
  ubah();

  const kendali = [];
  daftar.forEach((el, i) => {
    const a = sebelum[i];
    const b = el.getBoundingClientRect();
    const dx = a.left - b.left;
    const dy = a.top - b.top;
    const sx = b.width > 0 ? a.width / b.width : 1;
    const sy = b.height > 0 ? a.height / b.height : 1;
    const diam = Math.abs(dx) < 0.5 && Math.abs(dy) < 0.5
      && Math.abs(sx - 1) < 0.005 && Math.abs(sy - 1) < 0.005;
    if (diam) return;
    kendali.push(animasi(el, {
      transform: [
        `translate3d(${dx.toFixed(2)}px, ${dy.toFixed(2)}px, 0)`
        + ` scale(${sx.toFixed(4)}, ${sy.toFixed(4)})`,
        "none",
      ],
    }, { pegas: "jawab", ...opsi }));
  });
  return gabungKendali(kendali);
}

/* --------------------------------------------------------------- angka */

/** Hitung sebuah angka naik dari nilai sekarang ke nilai baru.
 *
 *  Angka yang melompat begitu saja membuat orang bertanya "tadi berapa?".
 *  Angka yang berjalan naik menjawabnya tanpa satu kata pun — dan itu satu
 *  dari sedikit tempat di aplikasi ini yang animasinya benar-benar
 *  menyampaikan informasi, bukan menghiasinya. */
export function angkaKe(el, ke, opsi = {}) {
  if (!el) return () => {};
  const format = opsi.format || ((n) => String(Math.round(n)));
  const tujuan = Number(ke) || 0;
  const awal = opsi.dari === undefined
    ? Number(String(el.textContent || "").replace(/[^\d.-]/g, "")) || 0
    : Number(opsi.dari);

  // Lebar digit dipatok di MESIN dan SEBELUM cabang di bawah. Sesudahnya,
  // tingkat `mati` dan pemanggil yang angkanya tidak berubah tetap menukar
  // teksnya tanpa pernah mendapat properti ini — dan digit proporsional
  // menggeser apa pun yang berdiri di sebelahnya (generator CLS).
  el.style.fontVariantNumeric = "tabular-nums";

  if (!adaGerak() || awal === tujuan) {
    el.textContent = format(tujuan);
    return () => {};
  }

  const durasi = opsi.durasi || 620;
  const mulai = performance.now();
  let id = requestAnimationFrame(function langkah(kini) {
    const t = jepit((kini - mulai) / durasi);
    const e = 1 - Math.pow(1 - t, 3);            // easeOutCubic
    el.textContent = format(antara(awal, tujuan, e));
    if (t < 1) id = requestAnimationFrame(langkah);
    else el.textContent = format(tujuan);
  });
  return () => cancelAnimationFrame(id);
}

/* -------------------------------------------------------------- isyarat */

const BISA_TUNJUK = ADA_DOM && window.matchMedia
  && window.matchMedia("(hover: hover) and (pointer: fine)").matches;

/* Permukaan yang menjawab saat ditekan. Semuanya elemen yang memang bisa
   diklik — menganimasikan yang lain cuma menjanjikan sesuatu yang tidak
   terjadi. */
const BISA_DITEKAN =
  ".tbl, .baris, .opsi button, .kartu[href], .palet-item, .sakelar,"
  + " .rel-menu a, .tanda, .ikon-tombol, .medali.punya,"
  // Dua permukaan navbar yang sebelumnya diam saat ditekan padahal semua
  // tetangganya menjawab. Ditambahkan di sini, bukan dengan memanggil WAAPI
  // dari komponennya: pasangIsyarat() yang memegang pasangan tekan/lepas,
  // dan hanya lewat jalur itu pembatalannya dijamin.
  + " .rel-tombol, .rel-pemicu,"
  // `.pil[href]`, bukan `.pil`. Dari 58 pil di aplikasi ini, 56 adalah LABEL
  // statis ("dinilai otomatis", "terkunci", "5x dikerjakan") dan hanya 2 yang
  // berupa tautan. Memberi fisika tekan pada seluruh `.pil` membuat lima
  // puluh enam penanda mengecil saat disentuh lalu tidak melakukan apa-apa --
  // kebalikan dari janji bahwa yang menjawab sentuhan itu bisa ditekan.
  + " .pil[href], .ubin,"
  // Kepala bab adalah `<summary>`, dan ia satu-satunya permukaan besar di
  // halaman bahasa yang diam saat ditekan padahal seluruh tetangganya
  // menjawab. Didaftarkan di sini, BUKAN dengan memanggil tekan() dari
  // komponennya: `pasangIsyarat()` yang memegang pasangan tekan/lepas, dan
  // hanya lewat jalur itu pembatalannya dijamin (invarian #1).
  //
  // Aman untuk papan ketik tanpa syarat tambahan: jalur ini cuma menumpang
  // pointerdown/pointerup/pointercancel, jadi Enter pada `<summary>` — yang
  // memang cara membukanya dengan papan ketik — tidak pernah memicu tekan()
  // dan tidak ada animasi mengecil yang bisa tertinggal tanpa pasangannya.
  + " .bab-kepala";

/* Animasi "sedang ditekan" milik tiap elemen, supaya bisa dibatalkan saat
   jarinya diangkat. WeakMap, bukan Map: kalau tombolnya dibuang bersama layar
   yang menggantinya, catatannya ikut hilang sendiri. */
const _tekanan = new WeakMap();

/** Seberapa kecil sebuah tombol saat ditekan, disesuaikan dengan tingkat
 *  gerak. Di tingkat "halus" jaraknya separuh — tetap terasa, tapi jauh lebih
 *  tenang. */
function skalaTekan(opsi) {
  const dasar = opsi.skala === undefined ? 0.975 : opsi.skala;
  return 1 - (1 - dasar) * skala();
}

/** Tekan sekali: mengecil sedikit, lalu memantul balik dengan pegas. Kesan
 *  yang ditinggalkan bukan "ada animasi" melainkan "benda ini padat".
 *
 *  Hidup di tingkat "halus" juga, dan itu bukan kelonggaran: umpan balik
 *  sentuhan justru SATU-SATUNYA alasan tingkat tengah itu ada. Kalau ia ikut
 *  padam di situ, "halus" tidak ada bedanya dengan "mati". */
export function tekan(el, opsi = {}) {
  if (!adaGerak() || !el) return;
  const kecil = skalaTekan(opsi);
  // fill "forwards" wajib: selama jarinya masih menempel, tombolnya harus
  // TETAP kecil, bukan memantul balik sendiri setelah 90 md.
  _tekanan.set(el, animasi(el, { transform: ["none", `scale(${kecil})`] },
    { durasi: 90, easing: KELUAR, isi: "forwards" }));
}

export function lepas(el, opsi = {}) {
  if (!el) return;
  // Membatalkan yang menekan adalah keharusan, bukan kerapian. Animasi
  // ber-fill "forwards" tetap memaksakan nilai akhirnya SELAMANYA, jadi begitu
  // animasi memantul di bawah selesai mengisi, yang menekan akan menang lagi
  // dan tombolnya tinggal mengecil 2,5% untuk seterusnya. Satu tombol tidak
  // kelihatan; tiga puluh tombol yang pernah ditekan dalam satu sesi belajar
  // membuat seluruh antarmuka pelan-pelan menyusut.
  //
  // Dibatalkan SEBELUM memeriksa tingkat gerak: kalau gerak dimatikan tepat
  // di antara menekan dan melepas, yang menekan tetap harus dilepaskan.
  const menekan = _tekanan.get(el);
  if (menekan) { menekan.batal(); _tekanan.delete(el); }
  if (!adaGerak()) return;

  animasi(el, { transform: [`scale(${skalaTekan(opsi)})`, "none"] },
          { pegas: "lentur" });
}

/** Getar mendatar — dipakai untuk jawaban salah dan penolakan. Amplitudonya
 *  kecil dan simetris: ini isyarat "bukan itu", bukan hukuman. */
export function getar(el, opsi = {}) {
  const s = skala();
  if (!s || !el) return kendaliKosong();
  const a = (opsi.jarak === undefined ? 5 : opsi.jarak) * s;
  return animasi(el, {
    transform: ["none", `translateX(${-a}px)`, `translateX(${a * 0.8}px)`,
                `translateX(${-a * 0.4}px)`, "none"],
  }, { durasi: 300, easing: "ease-in-out", ...opsi });
}

/** Denyut sekali — untuk menarik mata ke sesuatu yang baru saja berubah.
 *  Sekali, tidak berulang: apa pun yang berdenyut terus akan diabaikan dalam
 *  satu menit dan mengganggu selamanya sesudahnya. */
export function denyut(el, opsi = {}) {
  const s = skala();
  if (!s || !el) return kendaliKosong();
  const besar = 1 + 0.028 * s;
  return animasi(el, {
    transform: ["none", `scale(${besar.toFixed(4)})`, "none"],
  }, { durasi: 340, easing: "ease-in-out", ...opsi });
}

/** Tombol utama mengikuti kursor beberapa piksel. Jaraknya sengaja kecil:
 *  yang dicari kesan "benda ini sadar kamu di sini", bukan benda yang lari
 *  dari kursor. Mati di layar sentuh — di sana tidak ada kursor untuk
 *  diikuti. */
export function magnet(el, opsi = {}) {
  if (!el || !BISA_TUNJUK) return () => {};
  const kuat = opsi.kuat === undefined ? 3 : opsi.kuat;
  let dipasang = false;

  const gerakkan = (e) => {
    if (!gerakPenuh()) return;
    const r = el.getBoundingClientRect();
    const x = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
    const y = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
    el.style.transform =
      `translate3d(${(jepit(x, -1, 1) * kuat).toFixed(2)}px,`
      + ` ${(jepit(y, -1, 1) * kuat * 0.6).toFixed(2)}px, 0)`;
    dipasang = true;
  };

  const lepaskan = () => {
    if (!dipasang) return;
    dipasang = false;
    const dari = el.style.transform;
    el.style.transform = "";
    animasi(el, { transform: [dari, "none"] }, { pegas: "lentur" });
  };

  el.addEventListener("pointermove", gerakkan);
  el.addEventListener("pointerleave", lepaskan);
  el.addEventListener("pointerdown", lepaskan);
  return () => {
    el.removeEventListener("pointermove", gerakkan);
    el.removeEventListener("pointerleave", lepaskan);
    el.removeEventListener("pointerdown", lepaskan);
    el.style.transform = "";
  };
}

/* -------------------------------------------------------------- perayaan */

/** Percikan bara dari sebuah elemen.
 *
 *  Bukan konfeti — tidak ada konfeti di bengkel mana pun, dan seluruh bahasa
 *  visual aplikasi ini adalah bara di atas meja kerja. Titik-titiknya naik,
 *  melebar sedikit, lalu padam. Opacity-nya bergerak satu arah saja, jadi
 *  tidak ada yang berkedip. */
export function percikBara(sumber, opsi = {}) {
  if (!gerakPenuh() || !ADA_DOM) return;
  const el = keDaftar(sumber)[0];
  const kotak = el ? el.getBoundingClientRect() : null;
  const x0 = kotak ? kotak.left + kotak.width / 2 : window.innerWidth / 2;
  const y0 = kotak ? kotak.top + kotak.height / 2 : window.innerHeight / 2;

  const jumlah = opsi.jumlah === undefined ? 16 : opsi.jumlah;
  const lapis = document.createElement("div");
  lapis.className = "bara-percik";
  lapis.setAttribute("aria-hidden", "true");
  document.body.appendChild(lapis);

  let terlama = 0;
  for (let i = 0; i < jumlah; i++) {
    const titik = document.createElement("i");
    const besar = 4 + Math.random() * 5;
    titik.style.left = `${x0}px`;
    titik.style.top = `${y0}px`;
    titik.style.width = `${besar}px`;
    titik.style.height = `${besar}px`;
    lapis.appendChild(titik);

    const sudut = (-Math.PI / 2) + (Math.random() - 0.5) * 1.5;
    const jarak = 60 + Math.random() * 130;
    const durasi = 900 + Math.random() * 700;
    terlama = Math.max(terlama, durasi);
    // Ditulis sebagai deret keyframe, bukan objek properti: baranya tetap
    // terang selama separuh perjalanan lalu padam, dan opacity karena itu
    // butuh tiga titik sementara transform cuma dua. Bentuk objek tidak bisa
    // memberi keduanya offset yang berbeda.
    titik.animate([
      { transform: "translate3d(0,0,0) scale(1)", opacity: 1, offset: 0 },
      { opacity: 0.9, offset: 0.45 },
      {
        transform: `translate3d(${(Math.cos(sudut) * jarak).toFixed(1)}px,`
          + ` ${(Math.sin(sudut) * jarak).toFixed(1)}px, 0) scale(0.25)`,
        opacity: 0,
        offset: 1,
      },
    ], {
      duration: durasi,
      delay: Math.random() * 220,
      easing: "cubic-bezier(.2,.7,.3,1)",
      fill: "forwards",
    });
  }
  setTimeout(() => lapis.remove(), terlama + 420);
}

/* ------------------------------------------------------- pasang sekali */

let sudahDipasang = false;

/** Pasang isyarat tekan untuk SELURUH aplikasi lewat satu pendengar.
 *
 *  Didelegasikan dari document, bukan dipasang per tombol: layar-layarnya
 *  membangun ulang DOM-nya sendiri terus-menerus, dan apa pun yang harus
 *  dipasang ulang tiap kali pasti akan terlewat di suatu tempat. */
export function pasangIsyarat() {
  if (!ADA_DOM || sudahDipasang) return;
  sudahDipasang = true;

  let ditekan = null;

  document.addEventListener("pointerdown", (e) => {
    if (!adaGerak()) return;
    if (e.button !== 0 && e.pointerType === "mouse") return;
    if (!(e.target instanceof Element)) return;
    const el = e.target.closest(BISA_DITEKAN);
    if (!el || el.hasAttribute("disabled")) return;
    if (el.closest("[data-gerak-lewat]")) return;
    ditekan = el;
    tekan(el);
  }, { passive: true });

  const selesaikan = () => {
    if (!ditekan) return;
    lepas(ditekan);
    ditekan = null;
  };
  document.addEventListener("pointerup", selesaikan, { passive: true });
  document.addEventListener("pointercancel", selesaikan, { passive: true });
  // Kursor yang keluar dari tombol sambil ditekan tidak memicu pointerup di
  // atas tombol itu. Tanpa baris ini tombolnya tertinggal dalam keadaan
  // mengecil, dan itu terlihat seperti aplikasi yang macet.
  document.addEventListener("pointerleave", selesaikan, { passive: true });
}

/* ------------------------------------------------- jembatan ke CSS 2026

   Dua fungsi di bawah adalah satu-satunya tempat mesin gerak ini menyentuh
   platform CSS modern. Keduanya sengaja ditulis di KAKI berkas: separuh atas
   gerak.js bebas-DOM supaya bisa diimpor langsung di Node (tests/test_web.py
   TestMesinGerak), dan janji itu hanya bertahan kalau kode ber-DOM tidak
   pernah dijalankan saat impor. Karena itu keduanya berupa fungsi yang
   menunggu dipanggil, bukan pernyataan tingkat modul. */

/** Nama preset -> nama token CSS yang diterbitkan untuknya.
 *
 *  Daftar ini adalah SATU-SATUNYA sumber nama token pegas. Blok ATURAN GERAK
 *  di kepala gaya.css menyalin daftar yang sama untuk dibaca manusia, dan
 *  tests/test_web.py mengadu keduanya supaya salinan itu tidak pernah
 *  melenceng diam-diam. */
export const TOKEN_PEGAS = {
  jawab: "--pegas-jawab",
  halus: "--pegas-halus",
  lentur: "--pegas-lentur",
  berat: "--pegas-berat",
  panjang: "--pegas-panjang",
};

let _kurvaTerbit = false;

/** Terbitkan kurva pegas hasil solver sebagai token CSS, sekali saat boot.
 *
 *  gaya.css sudah memuat cadangan `cubic-bezier` yang sah, jadi halaman tanpa
 *  JavaScript tetap punya kurva yang benar bentuknya. Yang ditambahkan di sini
 *  adalah kurva `linear(...)` yang PERSIS sama dengan yang dipakai animasi
 *  WAAPI — sehingga sebuah gerakan yang separuhnya CSS dan separuhnya JS tidak
 *  pernah memakai dua kurva berbeda.
 *
 *  Tiap kurva diterbitkan bersama durasinya (`--pegas-*-ms`), karena kurva
 *  pegas dinormalisasi terhadap durasinya sendiri: memakainya dengan durasi
 *  lain meregangkan pegasnya jadi gerakan yang lain sama sekali. */
export function terbitkanKurva(akar) {
  const el = akar || (typeof document !== "undefined"
    ? document.documentElement : null);
  if (!el || _kurvaTerbit) return false;
  for (const [nama, token] of Object.entries(TOKEN_PEGAS)) {
    const k = kurvaPegas(PEGAS[nama]);
    el.style.setProperty(token, k.easing);
    el.style.setProperty(token + "-ms", k.durasi + "ms");
  }
  _kurvaTerbit = true;
  return true;
}

/** Bungkus sebuah pemasangan DOM dengan View Transition kalau platform dan
 *  setelan gerak mengizinkan; kalau tidak, jalankan apa adanya.
 *
 *  Kontraknya sengaja dibuat membosankan: `fn` SELALU dipanggil tepat sekali,
 *  apa pun jawaban platformnya. Layar yang memakainya tidak perlu tahu apakah
 *  transisinya terjadi — kalau ia perlu tahu, itu tanda efeknya sudah jadi
 *  syarat kelengkapan, bukan hiasan.
 *
 *  Tingkat gerak ditanyakan ke `adaGerak()`, bukan dihitung ulang di sini:
 *  satu-satunya tempat yang boleh memutuskan tingkat gerak adalah
 *  `tingkatGerak()`. */
export function vt(fn) {
  if (typeof fn !== "function") return Promise.resolve();
  const bisa = typeof document !== "undefined"
    && typeof document.startViewTransition === "function";
  if (!bisa || !adaGerak()) {
    const hasil = fn();
    return Promise.resolve(hasil);
  }
  const t = document.startViewTransition(fn);
  // `.finished` menolak saat transisinya dilewati (mis. tab disembunyikan di
  // tengah jalan). Itu bukan kegagalan yang perlu diteruskan ke pemanggil:
  // pekerjaan DOM-nya sendiri sudah selesai.
  return t.finished.catch(() => {});
}
