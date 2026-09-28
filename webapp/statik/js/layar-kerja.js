/* Layar tempat kamu MENGERJAKAN sesuatu: kuis, latihan, dan ruang coba.
 *
 * Bagian terpenting di seluruh aplikasi ada di berkas ini, dan ia bukan
 * editornya melainkan `gambarBeda()` — tampilan yang muncul saat jawabanmu
 * hampir benar. Di situlah belajar sebenarnya terjadi: bukan waktu programnya
 * jalan, tapi waktu kamu melihat DI MANA persisnya outputmu berbeda, dan
 * kenapa. Diff-nya bernomor baris, menunjuk kolom pertama yang berbeda, dan
 * membuat spasi tersembunyi jadi kelihatan.
 *
 * Semua penilaian dilakukan server lewat runner.periksa. Tidak ada satu pun
 * keputusan "lulus" yang diambil di sini — layar ini hanya menggambarkannya.
 *
 * Importir: aplikasi.js.
 */

import {
  api, h, isikan, kosongkan, bilah, sorak, rayakan, salin, konfirmasi, jendela,
  jamMundur, kilau, tunda, medan, selisihHari, keadaan,
} from "./inti.js";
import {
  animasi, masuk, ungkap, getar, denyut, percikBara, magnet, skala, angkaKe,
  adaGerak,
} from "./gerak.js";
import { ikon } from "./ikon.js";
import { praKode } from "./sorot.js";
import { Editor } from "./editor.js";
import {
  tombolBookmark, tombolCatatan, kartuKeluaran, blokProsa,
} from "./layar-belajar.js";
import {
  pratinjauHtml, bisaDipratinjau, dokumenPratinjau, halamanDikarang,
} from "./pratinjau.js";

const HURUF = "ABCDEFGHIJ";

/** Jadwal ulangan dalam bahasa manusia.
 *
 *  Daftar kuis sudah memakai "ulang 3 hari lagi"; layar hasil dulu
 *  menampilkan "diulang lagi 2026-09-07" — tanggal ISO mentah, di layar yang
 *  justru paling sering dilihat. Dua cara bicara untuk satu fakta yang sama
 *  membuat pemakainya mengira keduanya hal yang berbeda. */
function jadwalRamah(iso) {
  const hari = selisihHari(iso);
  if (hari === null) return "diulang lagi " + iso;
  if (hari <= 0) return "sudah waktunya diulang";
  if (hari === 1) return "diulang lagi besok";
  return `diulang lagi ${hari} hari lagi`;
}

function buatSakelar(judul, ket, awal, saatUbah) {
  let nyala = awal;
  const tbl = h("button.sakelar" + (nyala ? ".on" : ""), {
    role: "switch", "aria-checked": String(nyala),
    onclick: () => {
      nyala = !nyala;
      tbl.classList.toggle("on", nyala);
      tbl.setAttribute("aria-checked", String(nyala));
      saatUbah(nyala);
    },
  }, h("div.isi", {}, h("b", {}, judul), h("span", {}, ket)), h("div.knop", {}));
  return tbl;
}

/* ==================================================================== kuis */

export async function layarKuis({ key, indeks }, ctx) {
  const b = await api.ambil("/api/bahasa", { key });
  const nomorKuis = Number(indeks);
  const q = b.kuis[nomorKuis];
  if (!q) throw new Error("Kuis tidak ditemukan.");

  const panggung = h("div.kuis-panggung");
  const el = h("div.masuk", {}, panggung);
  let bersihkan = null;

  function gambarPersiapan() {
    if (bersihkan) { bersihkan(); bersihkan = null; }
    const persen = q.total_soal ? q.terbaik / q.total_soal * 100 : 0;
    // Setelan "Acak bawaan" ADA di Pengaturan dan berlaku di terminal, tapi
    // layar ini dulu memakunya ke true — jadi mematikannya mengubah persis nol
    // hal di browser. Setelan yang tampak berfungsi tapi tidak mengubah apa pun
    // lebih buruk daripada setelan yang tidak ada (lihat AGENTS.md, catatan
    // `--ukuran-teks`). Nilainya dibaca dari /api/awal, yang disegarkan
    // layarAtur setiap kali pengaturannya disimpan.
    const bawaanAcak = ctx && ctx.awal && ctx.awal.konfigurasi
      && ctx.awal.konfigurasi.acak_bawaan;
    let acak = bawaanAcak ? Boolean(bawaanAcak.nilai) : true;
    let timer = false;

    isikan(panggung,
      h("header.kepala-besar", {},
        h("span.mata", {}, `${b.label} · kuis ${nomorKuis + 1} dari ${b.kuis.length}`),
        h("h1", {}, q.judul),
        h("p.kepala-sub", {}, `${q.soal} soal pilihan ganda. Jawaban yang `
          + "salah bukan kegagalan — ia yang memberi tahu bagian mana yang "
          + "perlu dibaca ulang."),
        h("div.kepala-aksi", {},
          h("div.deret.deret-rapat", {},
            h("span.pil", {}, ikon("kuis", { ukuran: 14, tebal: 1.9 }),
              `${q.soal} soal`),
            q.pernah ? h("span.pil", {}, `${q.percobaan}× dikerjakan`) : null),
          h("div.materi-alat", {},
            tombolBookmark(key, "kuis", indeks, q.bookmark)))),

      q.pernah ? h("div.kartu", { gaya: { marginBottom: "var(--s5)" } },
        h("div.rinci-atas", {},
          h("span", {}, "Skor terbaikmu"),
          h("b", { gaya: { fontFamily: "var(--f-kode)" } },
            `${q.terbaik}/${q.total_soal}`)),
        bilah(persen, persen >= 100 ? "tumbuh" : ""),
        h("div.deret.deret-rapat", { gaya: { marginTop: "var(--s3)" } },
          q.jatuh_tempo ? h("span.pil.pil-ungu", {}, "sudah waktunya diulang")
            : q.jadwal ? h("span.pil", {}, jadwalRamah(q.jadwal)) : null,
          q.salah_tersisa
            ? h("span.pil.pil-salah", {}, `${q.salah_tersisa} soal masih salah`)
            : null)) : null,

      // Tindakan utama berdiri PALING ATAS, setelannya menyusul di balik
      // panel yang dilipat. Dua sakelar selebar halaman yang harus dilewati
      // sebelum sampai ke tombol Mulai mengubah layar pembuka kuis jadi
      // formulir — padahal keduanya sudah punya nilai bawaan yang benar untuk
      // hampir semua orang, hampir setiap kali.
      h("div.deret", {},
        h("button.tbl.tbl-utama", {
          onclick: () => mulai({ mode: "penuh", acak, timer }),
        }, q.pernah ? "Kerjakan lagi" : "Mulai kuis"),
        q.salah_tersisa ? h("button.tbl", {
          onclick: () => mulai({ mode: "salah", acak, timer }),
        }, `Ulangi ${q.salah_tersisa} soal yang masih salah`) : null),

      q.salah_tersisa ? h("p.baris-sisi", { gaya: { margin: "var(--s4) 0" } },
        "Mode ulangan tidak menyentuh skor terbaikmu — ia hanya mengurangi "
        + "daftar soal yang masih salah.") : null,

      h("details.bantuan", { gaya: { marginTop: "var(--s5)" } },
        h("summary.bantuan-kepala", {},
          ikon("atur", { ukuran: 18 }),
          h("b", {}, "Setelan kuis"),
          h("span", {}, acak ? "soal diacak" : "urutan asli"),
          h("span.bantuan-lipat", {}, ikon("lanjut", { ukuran: 18 }))),
        h("div.bantuan-isi", {},
          buatSakelar("Acak urutan soal & opsi",
            "Supaya jawaban tidak bisa dihafal dari posisinya.",
            acak, (v) => { acak = v; }),
          buatSakelar("Mode timer",
            "Beri batas waktu. Berguna menjelang ujian; melelahkan untuk "
            + "latihan harian.", timer, (v) => { timer = v; }))),
    );
  }

  async function mulai(opsi) {
    try {
      jalankanSesi(await api.kirim("/api/kuis/mulai", { key, indeks, ...opsi }));
    } catch (e) {
      sorak(e.message, "salah");
    }
  }

  function jalankanSesi(sesi) {
    let nomor = 0;
    let sisaDetik = sesi.durasi;
    let jamId = 0;

    const jam = h("span.jam", {}, sesi.durasi ? jamMundur(sisaDetik) : "");
    const hitung = h("span", {}, `1 / ${sesi.total}`);
    const bar = bilah(0);
    const isi = h("div");

    isikan(panggung,
      h("div.kuis-kemajuan", {}, hitung, bar, jam,
        h("button.tbl.tbl-kecil.tbl-hantu", { onclick: keluar }, "Hentikan")),
      isi);

    if (sesi.durasi) {
      jamId = setInterval(() => {
        sisaDetik -= 1;
        jam.textContent = jamMundur(sisaDetik);
        jam.classList.toggle("menipis", sisaDetik <= 30);
        if (sisaDetik <= 0) { clearInterval(jamId); selesai(true); }
      }, 1000);
    }

    document.addEventListener("keydown", saatTombol);
    bersihkan = () => {
      clearInterval(jamId);
      document.removeEventListener("keydown", saatTombol);
    };

    async function keluar() {
      if (!await konfirmasi(
        "Hentikan kuis ini? Jawaban yang sudah masuk tidak akan dicatat.",
        { judul: "Hentikan kuis", labelYa: "Ya, hentikan" })) return;
      api.kirim("/api/kuis/batal", { sesi: sesi.sesi }).catch(() => {});
      gambarPersiapan();
    }

    function gambarSoal() {
      const s = sesi.soal[nomor];
      hitung.textContent = `${nomor + 1} / ${sesi.total}`;
      bar.setel(nomor / sesi.total * 100);

      // Hurufnya dibungkus <span> sendiri supaya centang/silang bisa
      // menggantikannya lewat ::after saat jawabannya terungkap. Warna hijau
      // dan merah saja tidak cukup untuk mata yang sulit membedakan keduanya,
      // dan di layar ini dua warna itulah SELURUH umpan baliknya.
      const tombol = s.options.map((teks, i) => h("button", {
        onclick: () => jawab(i, tombol),
      }, h("span.huruf", {}, h("span", {}, HURUF[i])), h("span", {}, teks)));

      const soalEl = h("div.kuis-soal", {}, s.q);
      const opsiEl = h("div.opsi", {}, tombol);
      isikan(isi, h("div", {},
        soalEl,
        opsiEl,
        h("p.baris-sisi", { gaya: { marginTop: "var(--s4)" } },
          `Tekan 1–${s.options.length} atau A–${HURUF[s.options.length - 1]} `
          + "untuk menjawab.")));

      // Soal berikutnya datang DARI KANAN, bukan dari bawah seperti isi layar
      // yang lain. Arahnya sengaja: ia menyampaikan "maju satu langkah" tanpa
      // satu kata pun, dan itu persis yang barusan terjadi.
      const jauh = 22 * skala();
      animasi(soalEl, {
        opacity: [0, 1],
        transform: [`translate3d(${jauh}px, 0, 0)`, "none"],
      }, { pegas: "jawab" });
      // Opsinya menyusul satu per satu. Jarak antar opsi dijaga sangat pendek
      // (26 md): kuis adalah tempat orang menunggu, dan urutan yang panjang di
      // tempat menunggu berubah jadi hambatan.
      animasi([...opsiEl.children], {
        opacity: [0, 1],
        transform: [`translate3d(${jauh * 0.6}px, 0, 0)`, "none"],
      }, { pegas: "jawab", delay: (i) => 40 + i * 26 });
    }

    async function jawab(pilihan, tombol) {
      for (const t of tombol) t.disabled = true;
      let r;
      try {
        r = await api.kirim("/api/kuis/jawab",
                            { sesi: sesi.sesi, nomor, pilihan });
      } catch (e) {
        sorak(e.message, "salah");
        gambarPersiapan();
        return;
      }

      tombol[r.jawaban_benar].classList.add("benar");
      if (!r.benar && tombol[pilihan]) tombol[pilihan].classList.add("salah");

      // Dua isyarat yang berbeda BENTUKNYA, bukan cuma warnanya: yang benar
      // mengembang sekali, yang salah bergetar mendatar. Warna hijau dan merah
      // saja tidak cukup untuk mata yang sulit membedakan keduanya.
      if (r.benar) {
        denyut(tombol[r.jawaban_benar]);
        percikBara(tombol[r.jawaban_benar], { jumlah: 7 });
      } else {
        if (tombol[pilihan]) getar(tombol[pilihan]);
        denyut(tombol[r.jawaban_benar]);
      }

      const lanjut = h("button.tbl.tbl-utama", { onclick: berikutnya },
        nomor + 1 >= sesi.total ? "Lihat hasil" : "Soal berikutnya →");

      isi.appendChild(h("div.penjelasan", {},
        h("b", {}, r.benar ? "Benar. " : "Belum tepat. "),
        r.penjelasan || (r.benar ? "" : "Jawaban yang benar disorot hijau."),
        h("div.deret", { gaya: { marginTop: "var(--s3)" } }, lanjut)));
      lanjut.focus();
    }

    function berikutnya() {
      nomor += 1;
      if (nomor >= sesi.total) selesai(false);
      else gambarSoal();
    }

    async function selesai(kehabisanWaktu) {
      clearInterval(jamId);
      try {
        gambarHasil(await api.kirim("/api/kuis/selesai", { sesi: sesi.sesi }),
                    kehabisanWaktu);
      } catch (e) {
        sorak(e.message, "salah");
        gambarPersiapan();
      }
    }

    function saatTombol(e) {
      if (e.target instanceof Element
          && e.target.matches("input, textarea, select")) return;
      const tombol = [...isi.querySelectorAll(".opsi button")];
      if (!tombol.length) return;
      if (tombol[0].disabled) {
        if (e.key === "Enter") {
          const lanjut = isi.querySelector(".penjelasan .tbl");
          if (lanjut) { e.preventDefault(); lanjut.click(); }
        }
        return;
      }
      const angka = parseInt(e.key, 10);
      const huruf = HURUF.indexOf(e.key.toUpperCase());
      const i = Number.isInteger(angka) && angka >= 1 ? angka - 1
              : huruf >= 0 ? huruf : -1;
      if (i >= 0 && i < tombol.length) { e.preventDefault(); tombol[i].click(); }
    }

    gambarSoal();
  }

  function gambarHasil(r, kehabisanWaktu) {
    if (bersihkan) { bersihkan(); bersihkan = null; }
    const persen = r.total ? r.benar / r.total * 100 : 0;
    const sempurna = r.benar === r.total && r.total > 0;
    rayakan(r, { diam: true });

    const kalimat = sempurna ? "Sempurna. Semua benar."
      : persen >= 80 ? "Bagus. Tinggal sedikit yang perlu dirapikan."
      : persen >= 50 ? "Separuh jalan. Baca ulang bagian yang salah, lalu "
                       + "ulangi soal itu saja."
      : "Ini tanda materinya belum menempel — dan itu wajar. Baca ulang "
        + "materinya dulu, jangan langsung mengulang kuisnya.";

    // Skornya dihitung naik dari nol. Di layar hasil, angka itu satu-satunya
    // hal yang benar-benar ditunggu — dan angka yang merangkak naik membuat
    // mata berhenti di situ tanpa perlu diperbesar atau diberi warna.
    const angkaBenar = h("span", {}, "0");
    if (adaGerak()) {
      setTimeout(() => angkaKe(angkaBenar, r.benar,
                               { dari: 0, durasi: 520 }), 180);
    } else {
      angkaBenar.textContent = String(r.benar);
    }

    isikan(panggung, h("div.masuk", {},
      h("header.kepala-besar", {},
        h("span.mata", {}, kehabisanWaktu ? "Waktu habis" : "Hasil"),
        h("h1", {}, angkaBenar, ` dari ${r.total} benar`),
        h("p.kepala-sub", {}, kalimat)),

      h("div.kartu", { gaya: { marginBottom: "var(--s5)" } },
        bilah(persen, persen >= 100 ? "tumbuh" : ""),
        h("div.deret.deret-rapat", { gaya: { marginTop: "var(--s3)" } },
          r.xp_tambah > 0 ? h("span.pil.pil-nyala", {}, `+${r.xp_tambah} XP`) : null,
          r.sesi_penuh
            ? h("span.pil", {}, `Terbaik ${r.terbaik}/${r.total_asli}`) : null,
          h("span.pil", {}, `${Math.round(r.detik)} detik`),
          r.jadwal ? h("span.pil.pil-ungu", {}, jadwalRamah(r.jadwal)) : null,
          r.salah_tersisa
            ? h("span.pil.pil-salah", {}, `${r.salah_tersisa} soal masih salah`)
            : h("span.pil.pil-tumbuh", {}, "tidak ada soal tersisa")),
        !r.sesi_penuh ? h("p.baris-sisi", { gaya: { margin: "var(--s3) 0 0" } },
          "Ini sesi ulangan, jadi skor terbaikmu sengaja tidak disentuh.") : null),

      // Tindakan berikutnya berdiri SEBELUM daftar tinjauan, bukan sesudahnya.
      // Tinjauan lima belas soal bisa sepanjang dua layar penuh, dan tombol
      // "Kerjakan lagi" yang tertimbun di dasarnya adalah tombol yang harus
      // dicari — padahal ia jawaban paling umum atas layar ini.
      h("div.deret", { gaya: { marginBottom: "var(--s6)" } },
        h("button.tbl.tbl-utama", { onclick: gambarPersiapan }, "Kerjakan lagi"),
        r.salah_tersisa ? h("button.tbl", {
          onclick: () => mulai({ mode: "salah", acak: true, timer: false }),
        }, `Ulangi ${r.salah_tersisa} yang masih salah`) : null,
        h("a.tbl.tbl-hantu", { href: "#/bahasa/" + key },
          "Kembali ke " + b.label)),

      h("span.mata", {}, "Tinjau jawaban"),
      tinjauSemua(r),
    ));
    window.scrollTo({ top: 0, behavior: "auto" });
    // Perayaannya menyusul sesudah hasilnya terpasang, supaya baranya memercik
    // dari kartu skor yang sudah ada di layar — bukan dari ruang kosong.
    if (sempurna) kilau(panggung.querySelector(".kartu"));
  }

  function tinjauSemua(r) {
    const daftar = h("div", { gaya: { display: "grid", gap: "var(--s2)" } },
      r.rincian.map((d, i) => tinjauSoal(d, i)));
    ungkap(daftar, { per: 24, maks: 240, geser: 8, pegas: "jawab" });
    return daftar;
  }

  function tinjauSoal(d, i) {
    const punya = d.pilihanmu !== null && d.pilihanmu !== undefined;
    return h("div.uji" + (d.benar ? ".lulus" : ".gagal"), {},
      h("div.uji-kepala", {},
        h("span.uji-cap", {}, d.benar ? "BENAR" : "SALAH"),
        h("span.uji-nama", {}, `${i + 1}. ${d.q}`)),
      !d.benar ? h("div.uji-badan", {},
        h("div", { gaya: { fontSize: "var(--t-ui)" } },
          h("div", { gaya: { color: "var(--salah)" } },
            "Jawabanmu: " + (punya ? d.options[d.pilihanmu] : "(tidak dijawab)")),
          h("div", { gaya: { color: "var(--tumbuh)" } },
            "Seharusnya: " + d.options[d.jawaban_benar])),
        d.penjelasan ? h("div.arti", {},
          h("b", {}, "Kenapa"), h("div", {}, d.penjelasan)) : null) : null);
  }

  gambarPersiapan();

  return {
    el, judul: q.judul,
    konteks: {
      balik: { label: b.label, href: "#/bahasa/" + key },
      bab: "Kuis",
      judul: q.judul,
      posisi: `${nomorKuis + 1} / ${b.kuis.length}`,
      langkah: true,
      sebelum: nomorKuis > 0 ? `#/kuis/${key}/${nomorKuis - 1}` : null,
      sesudah: nomorKuis + 1 < b.kuis.length
        ? `#/kuis/${key}/${nomorKuis + 1}` : null,
    },
    saatKeluar: () => { if (bersihkan) bersihkan(); },
  };
}

/* ================================================================= latihan */

export async function layarLatihan({ key, indeks }) {
  const x = await api.ambil("/api/latihan", { key, indeks });
  let hintTerbuka = 0;
  let status = x.status;

  // Panel hasil SELALU ADA, bahkan sebelum ada hasilnya — dan keadaan
  // kosongnya menjelaskan apa yang akan muncul di situ. Sebelumnya panel ini
  // baru lahir sesudah tombol ditekan, di bawah baris tombol; di layar pendek
  // itu berarti umpan balik yang paling ditunggu muncul di luar pandangan, dan
  // yang terlihat cuma tombol yang sekejap mati lalu hidup lagi.
  const hasil = h("div.kerja-hasil");
  // Pendengar `message` milik pratinjau dicabut tiap kali hasilnya diganti
  // DAN saat layarnya ditinggalkan; tanpa itu tiap klik Jalankan menyisakan
  // satu pendengar yang mengukur bingkai yang sudah tidak ada.
  let lepasPratinjau = null;
  const lepasPratinjauKini = () => {
    if (lepasPratinjau) { lepasPratinjau(); lepasPratinjau = null; }
  };
  const kotakStatus = h("span");

  function hasilKosong() {
    isikan(hasil, keadaan({
      jenis: "kosong",
      judul: x.dinilai ? "Hasil muncul di sini" : "Keluaran muncul di sini",
      ket: x.dinilai
        ? "Tekan Jalankan untuk melihat keluaran kodemu, atau Periksa jawaban "
          + "untuk mengadunya dengan kunci jawaban, baris per baris."
        : "Tekan Jalankan untuk melihat keluaran kodemu.",
    }));
  }

  // Tombol ini dirujuk dari dua tempat — dipasang di deret tombol, dan jadi
  // titik asal percikan bara saat latihannya lulus. Perayaan yang berangkat
  // dari tombol yang barusan ditekan terbaca sebagai jawaban atas tekanan itu;
  // perayaan yang muncul di tengah layar terbaca sebagai iklan.
  const tblPeriksa = x.dinilai
    ? h("button.tbl.tbl-utama", { onclick: () => periksa() },
        ikon("selesai", { ukuran: 17 }), "Periksa jawaban",
        h("kbd", {}, "Ctrl ⇧ ⏎"))
    : null;
  if (tblPeriksa) magnet(tblPeriksa, { kuat: 2.5 });

  function gambarStatus() {
    isikan(kotakStatus,
      status === "lulus" ? h("span.pil.pil-tumbuh", {},
          ikon("selesai", { ukuran: 13, tebal: 2 }), "LULUS")
      : status === "manual" ? h("span.pil.pil-tumbuh", {}, "ditandai selesai")
      : h("span.pil", {}, "belum selesai"));
  }
  gambarStatus();

  const editor = new Editor({
    bahasa: x.sorot,
    kode: x.kode,
    label: "Kode jawabanmu untuk " + x.judul,
    // Ruang kerja setinggi jendela: tinggi editor datang dari tata letak,
    // bukan dari jumlah barisnya. Lihat _ukur() di editor.js.
    isiRuang: true,
    saatUbah: tunda((kode) => simpan(kode, true), 1200),
    pintasan: {
      "ctrl+enter": () => jalankan(),
      "ctrl+shift+enter": () => periksa(),
      "ctrl+s": () => simpan(editor.nilai, false),
    },
  });

  async function simpan(kode, diam) {
    try {
      await api.kirim("/api/latihan/simpan", { key, indeks, kode });
      editor.catat("tersimpan");
      if (!diam) sorak("Tersimpan di " + x.berkas.nama, "tumbuh", 2);
    } catch (e) {
      if (!diam) sorak(e.message, "salah");
    }
  }

  function sibuk(pesan) {
    const kartu = h("div.kartu.deret", {},
      h("div.pusaran"), h("span", {}, pesan));
    isikan(hasil, kartu);
    masuk(kartu, { geser: 6, pegas: "jawab" });
  }

  async function jalankan() {
    sibuk("Menjalankan kodemu…");
    try {
      const kode = editor.nilai;
      const r = await api.kirim("/api/latihan/jalankan",
                                { key, indeks, kode });
      lepasPratinjauKini();
      isikan(hasil, kartuJalan(r, x, kode, (fn) => { lepasPratinjau = fn; }));
    } catch (e) {
      const kartu = kartuGalat(e.message);
      isikan(hasil, kartu);
      masuk(kartu, { geser: 6 });
    }
  }

  async function periksa() {
    sibuk("Menyiapkan kunci jawaban lalu menjalankan kodemu…");
    try {
      const r = await api.kirim("/api/latihan/periksa",
                                { key, indeks, kode: editor.nilai });
      isikan(hasil, kartuPeriksa(r, x));
      if (r.lulus) {
        kilau(tblPeriksa || hasil);
        status = "lulus";
        gambarStatus();
        denyut(kotakStatus.firstChild || kotakStatus);
        rayakan(r.hadiah);
      } else {
        // Belum lulus BUKAN kegagalan, jadi tidak ada getaran di sini. Yang
        // dibutuhkan cuma mata yang dibawa ke diff-nya, dan itu sudah dilakukan
        // oleh kartunya yang masuk. Menggetarkan layar tiap kali output belum
        // cocok akan membuat mencoba terasa seperti dihukum.
        hasil.scrollIntoView({ behavior: adaGerak() ? "smooth" : "auto",
                               block: "nearest" });
      }
    } catch (e) {
      isikan(hasil, kartuGalat(e.message));
    }
  }

  /* ------------------------------------------------------------- bantuan
   *
   * Satu panel bertingkat, bukan empat tombol sederajat di baris tindakan.
   *
   * Yang lama menaruh Jalankan, Periksa jawaban, Simpan, Buka petunjuk, Lihat
   * jawaban, dan Bandingkan dalam satu deret dengan bentuk yang hampir sama —
   * jadi pemula harus membaca keenamnya sebelum tahu mana yang mestinya
   * ditekan lebih dulu, dan "Lihat jawaban" duduk dua tombol dari "Periksa
   * jawaban". Untuk orang yang buntu, jalan termudah dan jalan terburuk tidak
   * boleh berjarak sama.
   *
   * Sekarang urutannya mengikuti urutan yang benar-benar menolong: petunjuk
   * satu per satu lebih dulu, dan jalan keluar terakhir ada DI BAWAHNYA, di
   * balik garis putus-putus. Panelnya sendiri tertutup sampai dibuka, jadi
   * layar orang yang sedang lancar tidak memuat satu pun tawaran menyerah. */

  const kotakHint = h("div");

  function gambarHint() {
    isikan(kotakHint,
      hintTerbuka === 0
        ? (x.hint.length ? h("p.baris-sisi", {},
            `Tersedia ${x.hint.length} petunjuk. Coba sendiri dulu — buntu `
            + "selama beberapa menit justru bagian yang mengajari.") : null)
        : h("div", { gaya: { display: "grid", gap: "var(--s2)" } },
            x.hint.slice(0, hintTerbuka).map((t, i) =>
              h("div.arti.masuk", {}, h("b", {}, "Petunjuk " + (i + 1)),
                h("div", {}, t)))));
  }
  gambarHint();

  function hintTombol() {
    if (!x.hint.length) return null;
    const tbl = h("button.tbl.tbl-kecil", {
      onclick: () => {
        hintTerbuka = Math.min(hintTerbuka + 1, x.hint.length);
        gambarHint();
        tbl.textContent = hintTerbuka >= x.hint.length
          ? "Semua petunjuk terbuka"
          : `Buka petunjuk berikutnya (${hintTerbuka + 1}/${x.hint.length})`;
        tbl.disabled = hintTerbuka >= x.hint.length;
      },
    }, `Buka petunjuk pertama (1/${x.hint.length})`);
    return tbl;
  }

  // Tombolnya dirujuk dari dua tempat supaya LABELNYA ikut berubah setelah
  // ditekan. Sebelumnya label itu dibekukan pada nilai `status` saat layar
  // digambar: sesudah menandai selesai, tombolnya masih berbunyi "Saya sudah
  // menyelesaikannya" — dan menekannya lagi justru MEMBATALKAN tandanya,
  // diam-diam, tanpa dialog konfirmasi apa pun.
  const tblManual = x.dinilai ? null : h("button.tbl.tbl-kecil", {
    onclick: () => tandaiManual(),
  }, status === "manual" ? "Batalkan tanda selesai"
                         : "Saya sudah menyelesaikannya");

  function gambarTombolManual() {
    if (!tblManual) return;
    tblManual.textContent = status === "manual"
      ? "Batalkan tanda selesai" : "Saya sudah menyelesaikannya";
  }

  async function tandaiManual() {
    const nyalakan = status !== "manual";
    if (nyalakan && !await konfirmasi(
      "Tandai latihan ini selesai? Ini penilaian jujur dari kamu sendiri — "
      + "mesin tidak memeriksanya.",
      { judul: "Tandai selesai", labelYa: "Ya, sudah selesai" })) return;
    try {
      const r = await api.kirim("/api/latihan/manual", { key, indeks, nyalakan });
      status = r.status;
      gambarStatus();
      gambarTombolManual();
      rayakan(r);
      sorak(nyalakan ? "Ditandai selesai." : "Tanda selesai dibatalkan.", "tumbuh");
    } catch (e) {
      sorak(e.message, "salah");
    }
  }

  async function lihatJawaban() {
    if (hintTerbuka < x.hint.length && !await konfirmasi(
      `Masih ada ${x.hint.length - hintTerbuka} petunjuk yang belum dibuka. `
      + "Melihat jawaban sekarang biasanya membuat latihan ini terasa mudah "
      + "padahal belum kamu kuasai. Tetap lihat?",
      { judul: "Lihat jawaban", labelYa: "Tetap lihat" })) return;

    const pilih = await jendela({
      judul: "Contoh solusi — " + x.judul,
      lebar: true,
      isi: h("div", {},
        h("p.kepala-sub", { gaya: { margin: "0 0 var(--s3)" } },
          "Ini cuma SATU cara. Kode yang berbeda belum tentu salah, selama "
          + "outputnya sama."),
        h("div.blok-kode", {}, praKode(x.token_solusi))),
      aksi: [{ label: "Salin", nilai: "salin" },
             { label: "Tutup", nilai: null, kelas: "tbl-utama" }],
    });
    if (pilih === "salin") salin(x.solusi);
  }

  async function bandingkan() {
    const baris = bedaBaris(x.solusi.split("\n"), editor.nilai.split("\n"));
    await jendela({
      judul: "Kodemu dibanding contoh solusi",
      lebar: true,
      isi: h("div", {},
        h("p.kepala-sub", { gaya: { margin: "0 0 var(--s3)" } },
          "Baris hijau dari contoh solusi, baris merah dari kodemu. Beda "
          + "tulisan itu wajar — yang menentukan lulus cuma outputnya."),
        h("div.diff", {}, baris.length
          ? baris.map((d) => h("div.diff-baris"
              + (d.tanda === "=" ? ".diff-sama"
                 : d.tanda === "-" ? ".diff-kurang" : ".diff-tambah"), {},
              h("span.diff-nomor", {}, String(d.nomor)),
              h("span.diff-tanda", {}, d.tanda === "=" ? "│" : d.tanda),
              h("span.diff-isi", {}, d.teks)))
          : h("div.diff-baris", {},
              h("span.diff-isi", {}, "Sama persis.")))),
      aksi: [{ label: "Tutup", nilai: null, kelas: "tbl-utama" }],
    });
  }

  const panelBantuan = h("details.bantuan", {},
    h("summary.bantuan-kepala", {},
      ikon("bantuan", { ukuran: 18 }),
      h("b", {}, "Buntu?"),
      h("span", {}, x.hint.length
        ? `${x.hint.length} petunjuk tersedia` : "lihat contoh solusi"),
      h("span.bantuan-lipat", {}, ikon("lanjut", { ukuran: 18 }))),
    h("div.bantuan-isi", {},
      kotakHint,
      hintTombol(),
      // Jalan keluar terakhir, dipisahkan garis putus-putus dan ditulis paling
      // redup. Bukan untuk menyembunyikannya — ia harus ada, dan orang yang
      // benar-benar buntu harus bisa menemukannya — melainkan supaya ia tidak
      // pernah jadi yang pertama terbaca oleh orang yang baru dua menit
      // mencoba.
      h("div.bantuan-akhir", {},
        h("button.tbl.tbl-kecil.tbl-hantu", { onclick: lihatJawaban },
          "Lihat contoh solusi"),
        h("button.tbl.tbl-kecil.tbl-hantu", { onclick: bandingkan },
          "Bandingkan dengan kodeku"))));

  const el = h("div.masuk.kerja", {},
    h("header.kepala-besar.kepala-latihan", {},
      h("div.kepala-judul", {},
        h("span.mata", {}, x.proyek
          ? `${x.label_bahasa} · proyek akhir`
          : `${x.label_bahasa} · latihan ${x.indeks + 1} dari ${x.jumlah}`),
        h("h1", {}, x.judul),
        x.proyek ? h("p.kepala-sub", {},
          "Tidak ada materi baru di sini. Yang diuji cuma satu: apakah yang "
          + "sudah kamu baca terpisah-pisah itu nyambung jadi satu program "
          + "yang jalan.") : null),
      h("div.kepala-aksi", {},
        h("div.deret.deret-rapat", {},
          x.proyek ? h("span.pil.pil-nyala", {}, "PROYEK AKHIR") : null,
          h("span.pil.t-" + x.tingkat, {},
            ikon("tingkat", { ukuran: 14, tebal: 1.9 }), x.tingkat),
          kotakStatus,
          x.dinilai
            ? h("span.pil.pil-tenang", {}, "dinilai otomatis")
            : h("span.pil.pil-kunci", {}, "tanpa nilai otomatis")),
        h("div.materi-alat", {},
          tombolBookmark(key, "latihan", indeks, x.bookmark),
          tombolCatatan(x.kunci, x.catatan, x.judul)))),

    // Dua panel: yang DIBACA di kiri, yang DIKERJAKAN di kanan. Susunan lama
    // menumpuk keduanya, jadi soalnya tergulir keluar layar tepat saat kode
    // mulai ditulis — dan menulis jawaban sambil lupa pertanyaannya adalah
    // cara tercepat mengerjakan latihan yang salah.
    h("div.kerja-tata", {},
      h("div.kerja-soal", {},
        h("section", {},
          h("span.mata", {}, "Soal"),
          h("div.kartu.prosa.prosa-soal", {},
            (x.soal_blok || []).map(blokProsa))),

        !x.dinilai ? keadaan({
          jenis: "kunci",
          judul: "Latihan ini tidak dinilai mesin",
          ket: x.alasan,
          aksi: tblManual ? [tblManual] : [],
        }) : null,

        kartuBerkas(x),

        x.setup ? h("section", {},
          h("span.mata", {},
            "Kondisi awal — sudah disiapkan, tak perlu kamu tulis"),
          h("div.blok-kode", {}, praKode(x.token_setup))) : null,

        x.stdin_list.length > 1 ? keadaan({
          gambar: "bantuan",
          judul: "Diuji dengan beberapa masukan",
          ket: `Kodemu dijalankan ${x.stdin_list.length} kali dengan input `
            + "berbeda, jadi jawaban yang di-hardcode tidak akan lolos.",
        }) : null),

      h("div.kerja-kode", {},
        editor.el,

        h("div.kerja-bawah", {},
          h("div.kerja-tindakan", {},
            // Dua tindakan utama berdiri sendiri, di kiri. Alat-alat
            // dikelompokkan rapat di kanan sebagai SATU benda. Jarak antar
            // kelompok lebih lebar daripada jarak di dalam kelompok — itu yang
            // membuat keduanya terbaca sebagai dua hal, bukan lima benda
            // sederajat yang harus dibaca semua sebelum memilih.
            h("div.kerja-utama", {},
              x.bisa_jalan
                ? h("button.tbl" + (x.dinilai ? "" : ".tbl-utama"),
                    { onclick: jalankan },
                    ikon("jalankan", { ukuran: 17 }), "Jalankan",
                    h("kbd", {}, "Ctrl ⏎"))
                : null,
              tblPeriksa),

            h("span.deret-kanan"),

            h("div.tbl-set", {},
              h("button.tbl.tbl-kecil", {
                onclick: () => simpan(editor.nilai, false),
                title: "Simpan ke berkas (Ctrl+S)",
              }, "Simpan"),
              h("button.tbl.tbl-kecil", {
                onclick: (e) => salin(editor.nilai, "Kode disalin.",
                                      e.currentTarget),
              }, "Salin"),
              h("button.tbl.tbl-kecil", {
                title: "Kembalikan editor ke kerangka kosong",
                onclick: async () => {
                  if (!await konfirmasi(
                    "Kembalikan editor ke kerangka kosong? Kodemu yang "
                    + "sekarang hilang.",
                    { judul: "Mulai dari nol", labelYa: "Ya, kosongkan",
                      bahaya: true })) return;
                  const r = await api.ambil("/api/latihan/kerangka",
                                            { key, indeks });
                  editor.nilai = r.kode;
                  simpan(r.kode, true);
                },
              }, "Kerangka"))),

          panelBantuan),

        hasil)),

    // TIDAK ada kaki "latihan sebelumnya / berikutnya" di sini, dan itu bukan
    // kelalaian. Ketiga tautannya — daftar latihan, mundur satu, maju satu —
    // sudah dibawa strip konteks yang menempel di atas, jadi kaki ini akan
    // mengulang tiga hal yang sudah terlihat sambil memakan sembilan puluh
    // piksel dari ruang kerja yang justru tidak boleh digulir.
  );

  hasilKosong();

  return {
    el, judul: x.judul,
    konteks: {
      balik: { label: x.label_bahasa, href: "#/bahasa/" + key },
      bab: x.proyek ? "Proyek akhir" : "Latihan",
      judul: x.judul,
      posisi: `${x.indeks + 1} / ${x.jumlah}`,
      langkah: true,
      sebelum: x.indeks > 0 ? `#/latihan/${key}/${x.indeks - 1}` : null,
      sesudah: x.indeks + 1 < x.jumlah
        ? `#/latihan/${key}/${x.indeks + 1}` : null,
    },
    // Tanpa ini, tiap kunjungan ke sebuah latihan meninggalkan satu Editor
    // yang masih terdaftar sebagai pendengar `resize` di window — dan lewat
    // penutupnya, seluruh DOM layar itu beserta isi latihannya ikut tertahan
    // di memori. Dua puluh latihan dalam satu malam berarti dua puluh salinan.
    saatKeluar: () => { editor.lepas(); lepasPratinjauKini(); },
  };
}

function kartuBerkas(x) {
  return h("section", {},
    h("span.mata", {}, "Berkas jawabanmu"),
    h("div.kartu.kartu-rapat", {},
      h("code", { gaya: { color: "var(--nyala)", fontWeight: "700" } },
        x.berkas.nama),
      // Path-nya dipatahkan di karakter mana pun, bukan digulir mendatar.
      // Versi sebelumnya memberinya penggulir sendiri di dalam kolom selebar
      // 360 px, dan hasilnya path yang TETAP terpotong plus satu bilah gulir
      // tambahan di tempat yang paling sedikit ruangnya.
      h("div.berkas-jalur", { gaya: { marginTop: "var(--s1)" } },
        "di " + x.berkas.folder),
      x.runner === "java" ? h("div.baris-sisi",
        { gaya: { marginTop: "var(--s2)" } },
        `Nama kelasnya harus ${x.berkas.nama.replace(/\.java$/, "")} — javac `
        + "mewajibkannya sama dengan nama berkas.") : null,
      x.berkas.perintah.length ? h("div.berkas-jalur",
        { gaya: { marginTop: "var(--s2)" } },
        "Di terminal: ",
        h("code", { gaya: { color: "var(--tenang)" } },
          x.berkas.perintah.join("   lalu   "))) : null,
      h("div.baris-sisi", { gaya: { marginTop: "var(--s2)" } },
        "Kode yang kamu tulis di sini tersimpan ke berkas itu, jadi bisa "
        + "dibuka di editor mana pun dan dijalankan dari terminal.")));
}

/* --------------------------------------------------------- hasil eksekusi */

function kartuGalat(pesan) {
  return keadaan({ jenis: "salah", gambar: "belum", judul: "Gagal", ket: pesan });
}

function kartuJalan(r, x, kode, simpanLepas) {
  // Untuk HTML dan CSS, "keluaran" adalah pohon struktur -- benar untuk
  // menilai, salah untuk ditonton. Di layar latihan justru di sinilah orang
  // paling ingin melihat halamannya: ia baru saja menulisnya sendiri.
  const dok = kode && bisaDipratinjau(x.runner)
    ? dokumenPratinjau(x.runner, kode) : "";
  let pv = null;
  if (dok) {
    pv = pratinjauHtml(dok);
    simpanLepas(pv.lepas);
  }
  return h("div.kartu.masuk", {},
    h("div.deret", { gaya: { marginBottom: "var(--s3)" } },
      h("h3", {}, dok ? "Halamanmu" : "Hasil menjalankan"),
      h("span.deret-kanan"),
      h("span.pil" + (r.kode_keluar === 0 ? ".pil-tumbuh" : ".pil-salah"), {},
        `kode keluar ${r.kode_keluar}`),
      h("span.pil", {}, r.detik + " detik")),
    r.stdin ? h("div", { gaya: { marginBottom: "var(--s2)" } },
      h("span.mata", {}, "Masukan yang dikirim"),
      h("div.terminal", {}, r.stdin)) : null,
    pv ? h("div", { gaya: { marginBottom: "var(--s3)" } },
      halamanDikarang(x.runner, kode) ? h("p.pratinjau-ket", {},
        "Halaman contoh ini dibuatkan dari pemilih di CSS-mu sendiri — ",
        h("b", {}, "bukan"), " berkas HTML-mu.") : null,
      pv.el) : null,
    h("span.mata", {}, dok ? "Struktur yang dinilai" : "Keluaran"),
    h("div.terminal", {}, r.keluaran),
    r.galat ? blokGalat(r.galat, r.fase) : null,
    r.timeout ? h("div.diagnosa", {}, h("span.panah", {}, "→"),
      h("div", {}, `Program dihentikan setelah ${x.batas_waktu} detik. `
        + "Kemungkinan ada loop yang tidak pernah berhenti.")) : null,
    r.catatan ? h("div.baris-sisi", { gaya: { marginTop: "var(--s2)" } },
      r.catatan) : null);
}

function blokGalat(g, fase) {
  return h("div", { gaya: { marginTop: "var(--s3)" } },
    h("span.mata", {},
      fase === "kompilasi" ? "Pesan dari compiler" : "Pesan error"),
    h("div.terminal.terminal-galat", {}, g.baris.join("\n")),
    g.artinya.length ? h("div.arti", {},
      h("b", {}, "Artinya"),
      g.artinya.map((t) => h("div", {}, "• " + t))) : null);
}

function kartuPeriksa(r, x) {
  if (!r.bisa_dinilai) {
    return keadaan({ jenis: "kunci", gambar: "belum",
                     judul: "Belum bisa dinilai", ket: r.alasan });
  }
  const lulus = r.uji.filter((u) => u.lulus).length;
  return h("div.masuk", {},
    h("div.kartu", { gaya: { marginBottom: "var(--s3)",
      borderColor: r.lulus ? "var(--tumbuh)"
        : "color-mix(in srgb, var(--salah) 40%, transparent)" } },
      h("div.deret", {},
        h("h3", { gaya: { color: r.lulus ? "var(--tumbuh)" : "var(--salah)" } },
          r.lulus ? "Benar. Outputmu sudah sesuai."
                  : "Belum sesuai — lihat bedanya di bawah."),
        h("span.deret-kanan"),
        h("span.pil", {}, `${lulus}/${r.uji.length} uji lulus`),
        h("span.pil", {}, r.detik + " detik")),
      !r.lulus ? h("p", { gaya: { margin: "var(--s2) 0 0",
                                  color: "var(--teks-2)",
                                  fontSize: "var(--t-ui)" } },
        "Baris hijau bertanda − adalah yang diharapkan; baris merah bertanda + "
        + "adalah punyamu.") : null),
    deretUji(r));
}

/* Hasil uji muncul satu per satu, urut dari uji pertama. Kalau uji ketiga yang
   gagal, urutan itulah yang membawa mata ke sana: dua kartu hijau lewat, lalu
   berhenti di yang merah. Muncul serentak tidak memberi arah apa pun. */
function deretUji(r) {
  const kotak = h("div", { gaya: { display: "grid", gap: "0" } },
    r.uji.map((u) => kartuUji(u)));
  ungkap(kotak, { per: 60, maks: 300, geser: 8, pegas: "jawab" });
  return kotak;
}

function kartuUji(u) {
  return h("div.uji" + (u.lulus ? ".lulus" : ".gagal"), {},
    h("div.uji-kepala", {},
      h("span.uji-cap", {}, u.lulus ? "LULUS" : "GAGAL"),
      h("span.uji-nama", {}, u.nama),
      u.stdin ? h("span.pil", {},
        "input: " + u.stdin.replace(/\n/g, "⏎").slice(0, 24)) : null),
    !u.lulus ? h("div.uji-badan", {},
      u.galat ? blokGalat(u.galat, "") : null,
      // Output benar tapi program berakhir dengan error: kasus ini pernah
      // dinyatakan lulus, yang justru menyembunyikan bug yang sedang dipelajari.
      u.output_cocok && u.kode_keluar !== 0 ? h("div.diagnosa", {},
        h("span.panah", {}, "→"),
        h("div", {}, "Outputmu sudah benar, TAPI program berakhir dengan error "
          + `(kode keluar ${u.kode_keluar}). Perbaiki dulu errornya.`)) : null,
      (u.mode === "regex" || u.mode === "mengandung")
        ? h("div", {},
            h("span.mata", {}, `Pola yang dicari (${u.mode})`),
            h("div.terminal", {}, u.harapan),
            h("span.mata", {}, "Hasilmu"),
            h("div.terminal", {}, u.aktual))
        : (u.beda ? gambarBeda(u.beda) : null)) : null);
}

/* -------------------------------------------------------------------- diff
 * Ini tampilan terpenting di aplikasi. Bentuknya:
 *
 *    1 │ Halo, namaku Andi!
 *    2 - Aku sedang belajar Python.    (diharapkan)
 *    2 + aku sedang belajar python.    (punyamu)
 *        ↑ beda mulai kolom 1
 *  → Isinya sudah benar, hanya beda HURUF BESAR/KECIL.
 *
 * Penunjuk kolom dibangun sebagai .diff-baris utuh dengan nomor dan tanda
 * kosong, bukan sebagai baris terpisah yang paddingnya dihitung tangan. Itu
 * satu-satunya cara memastikan tanda ↑ tetap sejajar dengan huruf yang
 * ditunjuknya di semua ukuran layar dan semua ukuran huruf. */

function gambarBeda(b) {
  const baris = [];
  let nomor = 0;
  for (const d of b.baris) {
    nomor += 1;
    if (d.tanda === "=") {
      baris.push(barisDiff(nomor, "│", d.harapan, "diff-sama", ""));
      continue;
    }
    if (d.tanda === "-" || d.tanda === "~") {
      baris.push(barisDiff(nomor, "-", d.harapan, "diff-kurang", "diharapkan"));
    }
    if (d.tanda === "+" || d.tanda === "~") {
      baris.push(barisDiff(nomor, "+", d.aktual, "diff-tambah", "punyamu"));
    }
    if (d.tanda === "~" && nomor === b.nomor_beda && b.kolom_beda) {
      baris.push(h("div.diff-baris", {},
        h("span.diff-nomor", {}, ""),
        h("span.diff-tanda", {}, ""),
        h("span.diff-isi.diff-tunjuk", {},
          " ".repeat(Math.max(0, b.kolom_beda - 1))
          + "↑ beda mulai kolom " + b.kolom_beda)));
    }
  }

  return h("div", {},
    h("div.diff", {}, baris),
    b.baris.some((d) => d.tampak) ? h("div.baris-sisi",
      { gaya: { marginTop: "var(--s2)" } },
      "· menandai spasi dan → menandai tab, supaya beda yang tak terlihat "
      + "jadi terlihat.") : null,
    b.catatan.map((c) => h("div.diagnosa", {},
      h("span.panah", {}, "→"), h("div", {}, c))));
}

function barisDiff(nomor, tanda, teks, kelas, ket) {
  return h("div.diff-baris." + kelas, {},
    h("span.diff-nomor", {}, String(nomor)),
    h("span.diff-tanda", {}, tanda),
    h("span.diff-isi", {}, teks === null || teks === undefined ? "" : teks),
    ket ? h("span.diff-ket", {}, "(" + ket + ")") : null);
}

/** Diff baris untuk membandingkan kode pelajar dengan solusi contoh.
 *  Memakai tabel subsekuens terpanjang bersama; masukannya puluhan baris, jadi
 *  biaya O(n·m) tidak pernah terasa. */
function bedaBaris(a, b) {
  const n = a.length;
  const m = b.length;
  const tabel = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      tabel[i][j] = a[i] === b[j]
        ? tabel[i + 1][j + 1] + 1
        : Math.max(tabel[i + 1][j], tabel[i][j + 1]);
    }
  }
  const keluar = [];
  let i = 0;
  let j = 0;
  let nomor = 0;
  while (i < n && j < m) {
    nomor += 1;
    if (a[i] === b[j]) { keluar.push({ tanda: "=", teks: a[i], nomor }); i++; j++; }
    else if (tabel[i + 1][j] >= tabel[i][j + 1]) {
      keluar.push({ tanda: "-", teks: a[i], nomor }); i++;
    } else {
      keluar.push({ tanda: "+", teks: b[j], nomor }); j++;
    }
  }
  while (i < n) { nomor += 1; keluar.push({ tanda: "-", teks: a[i++], nomor }); }
  while (j < m) { nomor += 1; keluar.push({ tanda: "+", teks: b[j++], nomor }); }
  return keluar.every((k) => k.tanda === "=") ? [] : keluar;
}

/* ============================================================== ruang coba */

export async function layarCoba(params, ctx) {
  // Satu runner bisa dipakai beberapa entri LANGUAGES ("Bikin Aplikasi" juga
  // memakai java), jadi daftarnya disaring supaya tiap runner muncul sekali.
  const daftar = [];
  const sudah = new Set();
  for (const b of ctx.awal.bahasa) {
    if (!b.siap || sudah.has(b.runner)) continue;
    sudah.add(b.runner);
    daftar.push(b);
  }

  // Bawaannya Python, bukan yang pertama di registry: ia yang paling mungkin
  // dipakai untuk mencoba sesuatu dengan cepat, dan paling sedikit upacaranya.
  const bawaan = sudah.has("python") ? "python"
    : (daftar[0] && daftar[0].runner) || "python";
  const diminta = params.bahasa || ctx.ingat("coba.bahasa");
  // Pilihan yang tersimpan bisa jadi menunjuk toolchain yang sudah dicopot;
  // jangan menyisakan <select> tanpa nilai yang cocok.
  let bahasa = sudah.has(diminta) ? diminta : bawaan;
  let kode = ctx.ingat("coba.kode." + bahasa) || contohAwal(bahasa);
  let judulContoh = "";

  // Dibuka dari tombol "Ruang Coba" di halaman materi: ambil blok kodenya.
  if (params.key && params.materi !== undefined) {
    try {
      const c = await api.ambil("/api/materi/contoh", {
        key: params.key, indeks: params.materi, bagian: params.bagian || 0 });
      bahasa = c.bahasa;
      kode = c.kode;
      judulContoh = c.judul;
    } catch (e) { sorak(e.message, "salah"); }
  }

  const keluaran = h("div.kerja-hasil");
  let lepasPratinjau = null;
  const lepasPratinjauKini = () => {
    if (lepasPratinjau) { lepasPratinjau(); lepasPratinjau = null; }
  };
  const masukan = h("textarea", {
    placeholder: "Masukan untuk program (stdin). Kosongkan kalau tidak dipakai.",
    gaya: { minHeight: "62px", fontFamily: "var(--f-kode)",
            fontSize: "var(--t-kecil)" },
    value: ctx.ingat("coba.stdin") || "",
  });
  masukan.addEventListener("input", () => ctx.ingat("coba.stdin", masukan.value));

  const simpanDraf = tunda((k, b) => ctx.ingat("coba.kode." + b, k), 700);

  const editor = new Editor({
    bahasa: sorotUntuk(bahasa, ctx),
    kode,
    label: "Ruang coba",
    // Sama seperti di layar latihan: tingginya datang dari tata letak.
    isiRuang: true,
    // Bahasanya dibawa sebagai argumen, BUKAN dibaca dari `bahasa` saat timer
    // akhirnya jalan. Kalau tidak: ketik di Python, langsung ganti pilihan ke
    // Java dalam 700 md, dan kode Python-mu tersimpan ke kunci draf Java —
    // menimpa apa pun yang ada di sana.
    saatUbah: (k) => simpanDraf(k, bahasa),
    pintasan: { "ctrl+enter": () => jalankan() },
  });

  const pilihBahasa = h("select", {
    "aria-label": "Bahasa yang dipakai",
    onchange: () => {
      ctx.ingat("coba.kode." + bahasa, editor.nilai);
      bahasa = pilihBahasa.value;
      ctx.ingat("coba.bahasa", bahasa);
      editor.bahasa = sorotUntuk(bahasa, ctx);
      editor.nilai = ctx.ingat("coba.kode." + bahasa) || contohAwal(bahasa);
    },
    gaya: { width: "auto" },
  }, daftar.map((b) => h("option",
    { value: b.runner, selected: b.runner === bahasa }, b.label)));

  const tblJalan = h("button.tbl.tbl-utama", { onclick: () => jalankan() },
    ikon("jalankan", { ukuran: 17 }), "Jalankan", h("kbd", {}, "Ctrl ⏎"));
  magnet(tblJalan, { kuat: 2.5 });

  async function jalankan() {
    tblJalan.disabled = true;
    const menunggu = h("div.kartu.deret", {},
      h("div.pusaran"), h("span", {}, "Menjalankan…"));
    isikan(keluaran, menunggu);
    masuk(menunggu, { geser: 6, pegas: "jawab" });
    try {
      const r = await api.kirim("/api/coba",
        { bahasa, kode: editor.nilai, stdin: masukan.value });
      // Kartu yang sama persis dengan yang dipakai halaman materi: untuk HTML
      // ia menampilkan HALAMANNYA lebih dulu, pohon strukturnya satu klik di
      // sebelahnya. Dulu yang muncul di sini cuma pohonnya -- orang yang baru
      // menulis <h1>Halo, Dunia!</h1> lalu menekan Jalankan menerima daftar
      // nama tag yang baru saja ia ketik sendiri: jawaban yang benar untuk
      // pertanyaan yang tidak sedang ia tanyakan.
      lepasPratinjauKini();
      const kartu = kartuKeluaran(r, bahasa, editor.nilai,
        () => { lepasPratinjauKini(); kosongkan(keluaran); },
        (fn) => { lepasPratinjau = fn; });
      kartu.classList.add("masuk");
      isikan(keluaran, kartu);
    } catch (e) {
      isikan(keluaran, kartuGalat(e.message));
    } finally {
      tblJalan.disabled = false;
    }
  }

  // Bentuk yang sama persis dengan ruang kerja latihan: yang DIBACA di kiri,
  // yang DIKERJAKAN di kanan, dan keduanya mengisi tinggi jendela. Dua layar
  // yang gunanya sama — menulis kode lalu menjalankannya — tidak punya alasan
  // untuk punya dua tata letak berbeda yang harus dipelajari terpisah.
  const el = h("div.masuk.kerja", {},
    h("header.kepala-besar.kepala-latihan", {},
      h("div.kepala-judul", {},
        h("span.mata", {}, "Tanpa nilai, tanpa catatan"),
        h("h1", {}, "Ruang Coba")),
      h("div.kepala-aksi", {},
        h("div.deret.deret-rapat", {}, pilihBahasa))),

    h("div.kerja-tata", {},
      h("div.kerja-soal", {},
        h("section", {},
          h("span.mata", {}, "Apa ini"),
          h("div.kartu", {},
            h("p", { gaya: { margin: "0" } }, judulContoh
              ? `Contoh dari materi: ${judulContoh}. Ubah sesukamu — yang di `
                + "materi tidak ikut berubah."
              : "Tempat mencoba apa pun. Tidak dinilai dan tidak menyentuh "
                + "progres — justru karena itu ia berguna."))),
        h("section", {}, medan("Masukan program (stdin)", masukan))),

      h("div.kerja-kode", {},
        editor.el,
        h("div.kerja-bawah", {},
          h("div.kerja-tindakan", {},
            h("div.kerja-utama", {}, tblJalan),
            h("span.deret-kanan"),
            h("div.tbl-set", {},
              h("button.tbl.tbl-kecil", {
                onclick: (e) => salin(editor.nilai, "Kode disalin.",
                                      e.currentTarget),
              }, "Salin")))),
        keluaran)),
  );

  isikan(keluaran, keadaan({
    jenis: "kosong",
    judul: "Keluaran muncul di sini",
    ket: "Tekan Jalankan (atau Ctrl+Enter) untuk menjalankan kodenya di "
      + "komputermu sendiri.",
  }));

  return {
    el, judul: "Ruang Coba",
    saatKeluar: () => { editor.lepas(); lepasPratinjauKini(); },
  };
}

function sorotUntuk(runner, ctx) {
  const b = ctx.awal.bahasa.find((x) => x.runner === runner);
  return b ? b.sorot : runner;
}

function contohAwal(bahasa) {
  return {
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
    css: '/* Coba ubah warnanya, lalu Jalankan lagi. */\nbody {\n'
       + '  background-color: #f5f5f5;\n  font-family: sans-serif;\n'
       + '  margin: 0;\n}\n\nh1 {\n  color: #333;\n'
       + '  text-align: center;\n}\n',
  }[bahasa] || "";
}
