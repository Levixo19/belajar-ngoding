/* Saluran umpan balik NON-VISUAL: bunyi sintetis dan haptik perangkat.
 *
 * Satu modul untuk dua saluran, dan itu bukan penghematan baris. Keduanya
 * menjawab pertanyaan yang sama — "bolehkah aplikasi ini mengganggu orang
 * lewat indra selain mata?" — dan keduanya tunduk pada satu kebijakan yang
 * tidak boleh punya dua rumusan: BAWAAN MATI, dan tidak pernah jadi
 * satu-satunya cara mengetahui apa pun. Memisahkannya jadi dua berkas
 * menghasilkan dua tempat yang suatu hari berbeda pendapat soal kebijakan itu,
 * dan yang kalah adalah orang yang mematikan salah satunya lalu mendapati
 * yang lain tetap berbunyi.
 *
 * Importir: HANYA inti.js. Nol layar memuat berkas ini, sama seperti bahasa
 * gerak: layar yang butuh bunyi memanggil lewat `inti.js`, dan kalau sebuah
 * layar butuh bunyi yang tidak ada di tiga tingkat di bawah, itu tanda
 * tingkatnya salah — bukan tanda layar perlu API baru.
 *
 * Yang SENGAJA TIDAK ada di sini, dan masing-masing punya alasannya:
 *
 *   * Nol aset dan nol pustaka. Tidak ada `new Audio(`, `<audio>`, `.mp3`,
 *     `.wav`, dan tidak ada data-URI biner. Seluruh aplikasi ini berdiri tanpa
 *     satu dependensi pun dan tanpa langkah build; sebuah berkas bunyi adalah
 *     dependensi yang kebetulan tidak punya package.json. Tiga isyarat di
 *     bawah dibangkitkan oleh osilator, dan totalnya nol byte di disk.
 *
 *   * Nol bunyi per penekanan tombol. Umpan balik tekan tinggal di `tekan()`
 *     di gerak.js dan tetap di sana — bunyi per klik adalah bunyi yang paling
 *     sering dibenci di aplikasi mana pun, dan menambahkannya berarti ribuan
 *     isyarat per sesi untuk informasi yang tombolnya sudah sampaikan dengan
 *     mengecil.
 *
 *   * Nol bunyi per jawaban kuis, termasuk untuk jawaban yang SALAH. Yang
 *     boleh berbunyi cuma hasil akhirnya, satu kali. "Pilihanmu salah" sudah
 *     punya salurannya sendiri — goyang visual lewat `getar()` di gerak.js —
 *     dan menggandakannya jadi bunyi mengubah kuis latihan jadi deretan
 *     teguran. Perhatikan bahwa `getar()` di gerak.js adalah GOYANG VISUAL
 *     (`translateX`), bukan haptik; fungsi haptik di berkas ini sengaja
 *     bernama `sentuhPerangkat()` supaya dua saluran berbeda tidak pernah
 *     berbagi satu nama.
 *
 *   * Nol fanfare, nol loop, nol ambien, nol bunyi perpindahan rute, dan nol
 *     bunyi untuk kabar buruk seperti streak yang terputus.
 */

/* Kunci localStorage. Dibaca di SATU tempat — `bacaSuara()` di bawah — dan
   tidak ada layar yang menyentuhnya sendiri. Preferensi ini tinggal di
   peramban, BUKAN di `konfigurasi.SKEMA`: yang tinggal di SKEMA adalah yang
   tentang BELAJAR dan karena itu harus sama di terminal maupun web, sedangkan
   "boleh berbunyi di browser ini" tidak punya arti apa pun di terminal. */
const KUNCI_TINGKAT = "belajar.suara";
const KUNCI_GETAR = "belajar.getarPerangkat";

/* Tiga tingkat, dan yang tengah bukan kompromi malas.
 *
 * Saklar dua posisi memaksa orang yang cuma tidak ingin diberi selamat untuk
 * ikut membuang isyarat naik level — padahal naik level adalah peristiwa yang
 * memang jarang dan memang layak ditandai. Tingkat tengah memberi jalan
 * keluar: yang paling jarang terjadi tetap berbunyi, yang rutin diam. */
export const SUARA = [
  ["mati", "Mati",
   "Tidak ada bunyi sama sekali. Ini bawaannya."],
  ["halus", "Halus",
   "Hanya peristiwa yang jarang: naik level dan badge baru. "
   + "XP yang bertambah tetap diam."],
  ["penuh", "Penuh",
   "Naik level, badge baru, dan satu nada pendek tiap kali XP bertambah."],
];

/** Satu-satunya yang berhak memutuskan tingkat suara.
 *
 *  Kembarannya `tingkatGerak()` di gerak.js, dan alasannya sama: begitu ada
 *  tempat kedua yang menyimpulkan, dua permukaan akan berbeda pendapat tentang
 *  setelan yang sama dan tidak ada yang tahu mana yang benar.
 *
 *  Yang TIDAK ikut memutuskan di sini: `prefers-reduced-motion`. Itu memang
 *  satu-satunya yang menang atas pilihan gerak, tapi mengopelnya ke sini
 *  membuat dua pertanyaan berbeda punya satu jawaban — dan akibatnya salah
 *  satu tidak bisa dimatikan sendiri. Orang yang memakai pembaca layar sering
 *  justru MEMINTA gerak dikurangi sambil tetap mau mendengar konfirmasi; orang
 *  yang bekerja di ruang terbuka ingin kebalikannya. Keduanya sah, dan satu
 *  saklar tidak bisa melayani keduanya.
 *
 *  Nilai yang tidak dikenal — termasuk bentuk lama atau berkas localStorage
 *  yang disunting tangan — jatuh ke "mati", bukan ke "penuh". Sisi salahnya
 *  dipilih: setelan rusak yang membuat aplikasi diam cuma membingungkan,
 *  setelan rusak yang membuatnya berbunyi di ruang rapat tidak bisa dibatalkan
 *  sesudah terjadi. */
export function bacaSuara() {
  let n = null;
  try { n = localStorage.getItem(KUNCI_TINGKAT); }
  catch (e) { return "mati"; }
  if (n === null) return "mati";
  let nilai = n;
  try { nilai = JSON.parse(n); } catch (e) { /* nilai mentah, pakai apa adanya */ }
  return SUARA.some((s) => s[0] === nilai) ? nilai : "mati";
}

/** Saklar haptik BERDIRI SENDIRI — ia bukan tingkat keempat dari `suara`.
 *
 *  Keduanya terpisah karena situasinya terpisah: telepon di dalam saku di
 *  kereta adalah tempat getar berguna dan bunyi tidak sopan, dan laptop di
 *  meja adalah kebalikannya tepat. Menumpangkan haptik pada tingkat `suara`
 *  berarti satu dari dua situasi itu tidak punya setelan yang benar. */
export function bacaGetar() {
  try { return localStorage.getItem(KUNCI_GETAR) === "true"; }
  catch (e) { return false; }
}

/** Simpan preferensi. Dipanggil `terapkanTampilan()` lewat `inti.js`. */
export function setelSuara({ suara, getarPerangkat } = {}) {
  try {
    if (suara !== undefined && SUARA.some((s) => s[0] === suara)) {
      localStorage.setItem(KUNCI_TINGKAT, JSON.stringify(suara));
    }
    if (getarPerangkat !== undefined) {
      localStorage.setItem(KUNCI_GETAR, String(Boolean(getarPerangkat)));
    }
  } catch (e) { /* mode penyamaran atau kuota penuh: abaikan */ }
  return { suara: bacaSuara(), getarPerangkat: bacaGetar() };
}

/* ------------------------------------------------------------ mesin bunyi */

/* Peramban MENOLAK membuat AudioContext yang berbunyi sebelum ada gestur asli,
   dan konteks yang ditolak masuk ke keadaan "suspended" selamanya — jadi
   membuatnya di tingkat modul bukan cuma sia-sia, ia menukar satu-satunya
   konteks yang akan pernah ada dengan konteks yang mati. Karena itu ia dibuat
   LAZILY, pada isyarat pertama yang benar-benar diminta, dan saat idle ia
   di-`suspend()` — bukan `close()`. `close()` tidak bisa dibatalkan: isyarat
   berikutnya harus membangun konteks baru, dan konteks baru di luar gestur
   adalah konteks yang ditolak. */
let konteks = null;
let plafon = null;
let hidup = 0;
let jamIdle = null;

const IDLE_MS = 20000;
/* Dua isyarat bersamaan masih terbaca sebagai dua kejadian; tiga terbaca
   sebagai satu akor, dan akor yang tidak diminta siapa pun adalah bunyi yang
   salah. Yang ketiga DIBUANG, bukan diantre — isyarat yang datang 300 md
   terlambat menjelaskan kejadian yang sudah lewat dari layar. */
const MAKS_BARENG = 2;

/** Ada gestur yang sah? Dibaca lewat deteksi fitur, tanpa satu pun pendengar
 *  di tingkat modul: pendengar global berarti berkas ini menyentuh `document`
 *  saat diimpor, dan yang ingin dijaga bukan "tidak melempar" melainkan
 *  "tidak menyentuh". Peramban yang tidak punya `userActivation` tidak
 *  diblokir — di situ kebijakan autoplay-nya sendiri yang jadi pagarnya. */
function adaGestur() {
  const ua = typeof navigator !== "undefined" && navigator.userActivation;
  return ua ? Boolean(ua.hasBeenActive) : true;
}

function Konteks() {
  if (typeof window === "undefined") return null;
  return window.AudioContext || window.webkitAudioContext || null;
}

function pastikanKonteks() {
  if (konteks) return konteks;
  const K = Konteks();
  if (!K) return null;
  try {
    konteks = new K();
    /* SATU GainNode master sebagai plafon, dan tiap isyarat menggantung di
       bawahnya. Tanpa plafon, "agak terlalu keras" cuma bisa dibetulkan
       dengan menyunting tiap isyarat satu per satu — dan satu yang terlewat
       cukup untuk membuat seluruh setelan terasa tidak bekerja. */
    plafon = konteks.createGain();
    plafon.gain.value = 0.085;
    plafon.connect(konteks.destination);
  } catch (e) {
    konteks = null;
    plafon = null;
  }
  return konteks;
}

function tundaIdle() {
  if (jamIdle) clearTimeout(jamIdle);
  jamIdle = setTimeout(() => {
    jamIdle = null;
    if (konteks && hidup === 0 && konteks.state === "running") {
      try { konteks.suspend(); } catch (e) { /* sudah ditutup peramban */ }
    }
  }, IDLE_MS);
}

/** Satu nada berselubung, dijadwalkan seluruhnya lewat `AudioParam`.
 *
 *  Amplopnya TIDAK digerakkan putaran `requestAnimationFrame` yang menulis
 *  volume tiap frame: penjadwal audio berjalan di utasnya sendiri dengan
 *  ketepatan sub-milidetik, sementara rAF berhenti total saat tab tidak
 *  terlihat — dan isyarat yang amplopnya berhenti di tengah adalah nada yang
 *  menggantung sampai tabnya dibuka lagi.
 *
 *  Serangannya 8 md dan peredamannya eksponensial. Nada yang mulai seketika
 *  menghasilkan klik di awal (lompatan tak-kontinu di bentuk gelombangnya),
 *  dan peredaman linier menuju nol terdengar dipotong, bukan selesai. */
function nada(mulai, { hz, lama, puncak = 1 }) {
  const osc = konteks.createOscillator();
  const amp = konteks.createGain();
  osc.type = "sine";
  osc.frequency.setValueAtTime(hz, mulai);
  amp.gain.setValueAtTime(0.0001, mulai);
  amp.gain.linearRampToValueAtTime(puncak, mulai + 0.008);
  amp.gain.exponentialRampToValueAtTime(0.0001, mulai + lama);
  osc.connect(amp);
  amp.connect(plafon);
  osc.start(mulai);
  osc.stop(mulai + lama + 0.02);
  return osc;
}

/* Tiga isyarat, dan tiap-tiapnya ≤ 120 md. Angkanya bukan selera: lebih
   panjang dari itu dan bunyinya mulai terdengar sebagai MUSIK — sesuatu yang
   punya awal, tengah, dan akhir, yang karena itu menuntut didengarkan sampai
   habis. Yang dibutuhkan di sini cuma tanda baca.

   Nadanya diambil dari satu triad supaya tiga isyarat terdengar berasal dari
   satu keluarga, persis seperti dua puluh empat ikon garis di `ikon.js` yang
   sengaja satu keluarga. */
const ISYARAT = {
  /* Naik level atau badge baru — yang paling jarang terjadi. Dua nada NAIK,
     karena arah naik adalah satu-satunya hal yang bisa dibedakan telinga
     tanpa dilatih lebih dulu. */
  acara: [{ hz: 587.33, lama: 0.055, pada: 0 },
          { hz: 880.00, lama: 0.075, pada: 0.045 }],
  /* XP bertambah. Satu nada, dan sengaja nada TENGAH triad-nya: ia terdengar
     sebagai bagian dari keluarga yang sama tanpa terdengar sebagai kesimpulan. */
  capai: [{ hz: 739.99, lama: 0.07, pada: 0 }],
  /* Peragaan di kartu Pengaturan. Sama dengan `capai` supaya yang didengar
     orang saat memilih memang yang akan ia dengar sesudahnya. */
  contoh: [{ hz: 739.99, lama: 0.07, pada: 0 }],
};

/* Tingkat mana yang membunyikan isyarat mana. Tabel, bukan rantai `if`:
   pertanyaan "apa yang terdengar di 'halus'?" harus bisa dijawab dengan
   membaca satu baris. */
const IZIN = {
  mati: [],
  halus: ["acara"],
  penuh: ["acara", "capai", "contoh"],
};

/** Bunyikan satu isyarat, kalau tingkatnya mengizinkan.
 *
 *  Yang dimatikan pada tingkat "mati" adalah JALUR PANGGILNYA, bukan
 *  volumenya: fungsi ini keluar sebelum `pastikanKonteks()`, jadi peramban
 *  orang yang mematikan suara tidak pernah membuat AudioContext sama sekali.
 *  Menyetel plafon ke nol akan "terdengar" sama tapi tetap menyalakan mesin
 *  audio, dan mesin audio yang menyala adalah daya yang terpakai untuk
 *  menghasilkan keheningan. */
export function isyarat(jenis) {
  const tingkat = bacaSuara();
  if (!(IZIN[tingkat] || []).includes(jenis)) return false;
  if (!ISYARAT[jenis]) return false;
  if (hidup >= MAKS_BARENG) return false;
  if (!adaGestur()) return false;
  if (!pastikanKonteks()) return false;

  try {
    if (konteks.state === "suspended") konteks.resume();
    const t0 = konteks.currentTime + 0.005;
    hidup += 1;
    let terakhir = null;
    for (const n of ISYARAT[jenis]) {
      terakhir = nada(t0 + n.pada, n);
    }
    /* `hidup` diturunkan oleh osilator TERAKHIR yang selesai, bukan oleh
       sebuah `setTimeout` yang menebak durasinya. Timer akan melenceng
       setiap kali tabnya di latar belakang, dan yang terjadi bukan error
       melainkan penghitung yang tidak pernah kembali ke nol — alias isyarat
       yang berhenti bekerja selamanya sesudah dua kali. */
    if (terakhir) terakhir.onended = () => { hidup = Math.max(0, hidup - 1); };
    else hidup = Math.max(0, hidup - 1);
    tundaIdle();
    return true;
  } catch (e) {
    hidup = Math.max(0, hidup - 1);
    return false;
  }
}

/* ----------------------------------------------------------------- haptik */

/* 18 md. Di bawah ~10 md sebagian perangkat tidak menghasilkan apa pun sama
   sekali; di atas ~30 md yang terasa berhenti jadi tanda baca dan mulai jadi
   alarm. Satu sentakan, PERNAH, dan tidak ada ritme berulang: pola seperti
   `[30, 50, 30]` adalah kosakata notifikasi sistem, dan aplikasi yang
   meminjamnya sedang berpura-pura lebih penting daripada dirinya. */
const SENTAK_MS = 18;

/** Satu sentakan haptik, kalau perangkatnya punya dan saklarnya nyala.
 *
 *  Deteksi fitur, tanpa polifil, dan tanpa pesan apa pun kalau tidak ada:
 *  "perangkatmu tidak bisa bergetar" adalah kalimat yang tidak bisa
 *  ditindaklanjuti siapa pun. Hanya untuk KONFIRMASI — dan sengaja tidak
 *  pernah untuk kegagalan: jawaban latihan yang salah sudah pernah diberi
 *  haptik di layar kerja dan dibuang lagi dengan alasan yang tertulis di
 *  sana, karena menggetarkan telepon seseorang karena ia belum paham adalah
 *  hukuman yang dikirim ke tubuhnya. */
export function sentuhPerangkat(ms = SENTAK_MS) {
  if (!bacaGetar()) return false;
  if (!adaHaptik()) return false;
  const lama = Math.max(1, Math.min(30, Number(ms) || SENTAK_MS));
  try { return Boolean(navigator.vibrate(lama)); }
  catch (e) { return false; }
}

/** Perangkat ini punya motor getar?
 *
 *  Tinggal di SINI, bukan di layar Pengaturan yang menampilkan saklarnya.
 *  Layar yang menanyai `navigator.vibrate` sendiri adalah saluran haptik
 *  kedua — ia punya pendapatnya sendiri tentang apa yang dianggap "ada", dan
 *  pendapat kedua yang kebetulan hari ini sama dengan yang pertama adalah
 *  pendapat kedua yang suatu hari tidak.
 *
 *  Dipakai untuk menandai saklarnya SEBELUM ditekan: aturan "tidak boleh ada
 *  tombol yang berujung penolakan" berlaku untuk saklar juga, dan hampir
 *  seluruh desktop mendarat di cabang "tidak ada". */
export function adaHaptik() {
  return typeof navigator !== "undefined"
    && typeof navigator.vibrate === "function";
}

/** Catat preferensi ke akar dokumen, TANPA menyentuh mesin audio.
 *
 *  Ini yang boleh berjalan saat halaman dimuat — dan satu-satunya yang boleh.
 *  `terapkanTampilan()` berjalan sebelum ada gestur apa pun, jadi apa pun yang
 *  membangun AudioContext dari sana akan membangunnya dalam keadaan ditolak.
 *  Yang ditulis cuma atribut, supaya CSS dan pagar tes bisa melihat setelan
 *  yang sedang berlaku tanpa membaca localStorage sendiri. */
export function tandaiPreferensi(akar) {
  if (!akar || !akar.dataset) return;
  akar.dataset.suara = bacaSuara();
  akar.dataset.getar = bacaGetar() ? "ya" : "tidak";
}

/** Hanya untuk pagar tes: laporkan keadaan mesin tanpa membangunkannya.
 *
 *  Pagar §3.3 menagih "nol konstruksi AudioContext sebelum satu gestur pun"
 *  sebagai ANGKA, dan angka itu harus datang dari modulnya sendiri — sebuah
 *  tes yang menghitung konstruksi dengan mengintip stub-nya saja masih bisa
 *  hijau di atas modul yang membangun konteksnya lewat jalan lain. */
export function keadaanSuara() {
  return {
    tingkat: bacaSuara(),
    getar: bacaGetar(),
    konteksAda: konteks !== null,
    hidup,
  };
}
