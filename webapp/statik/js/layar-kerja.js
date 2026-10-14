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
  jamMundur, tunda, medan, selisihHari, keadaan,
} from "./inti.js";
import {
  animasi, masuk, ungkap, getar, denyut, percikBara, magnet, skala, angkaKe,
  adaGerak,
} from "./gerak.js";
import { ikon } from "./ikon.js";
import { praKode, token } from "./sorot.js";
import { Editor } from "./editor.js";
import {
  tombolBookmark, tombolCatatan, kartuKeluaran, blokProsa, saatSiap,
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
          + "salah bukan kegagalan. Ia yang memberi tahu bagian mana yang "
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
        "Mode ulangan tidak menyentuh skor terbaikmu; ia hanya mengurangi "
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

    const detak = () => {
      sisaDetik -= 1;
      jam.textContent = jamMundur(sisaDetik);
      jam.classList.toggle("menipis", sisaDetik <= 30);
      if (sisaDetik <= 0) { clearInterval(jamId); jamId = 0; selesai(true); }
    };
    const jalankanJam = () => {
      if (!jamId && sisaDetik > 0) jamId = setInterval(detak, 1000);
    };
    // Jamnya BERHENTI saat tabnya di latar, dan melanjutkan dari sisa detik
    // yang sama — bukan menghitung ulang dari penuh, dan bukan terus berjalan
    // di belakang punggung orangnya. SC 2.2.2 menelan batas waktu yang
    // berhitung sendiri juga: detik yang habis sementara tabnya tidak terlihat
    // adalah detik yang tidak pernah bisa dipakai siapa pun untuk menjawab.
    //
    // `sisaDetik` tidak disentuh di sini, dan itu seluruh triknya: yang
    // dihentikan pencacahnya, bukan angkanya. Melanjutkan berarti memasang
    // interval baru di atas angka yang sama.
    const saatTampil = () => {
      if (document.hidden) { clearInterval(jamId); jamId = 0; } else jalankanJam();
    };
    if (sesi.durasi) {
      jalankanJam();
      document.addEventListener("visibilitychange", saatTampil);
    }

    document.addEventListener("keydown", saatTombol);
    // Satu pintu keluar. Pendengar `visibilitychange` ikut dilepas DI SINI,
    // bukan lewat jalur pembersih kedua: dua pembersih berarti satu di
    // antaranya suatu hari terlupa di satu cabang keluar, dan pendengar yang
    // tertinggal menyalakan kembali jam milik kuis yang sudah ditutup.
    bersihkan = () => {
      clearInterval(jamId);
      document.removeEventListener("keydown", saatTombol);
      document.removeEventListener("visibilitychange", saatTampil);
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

      const soalEl = h("div.kuis-soal", { tabIndex: -1 }, s.q);
      const opsiEl = h("div.opsi", {}, tombol);
      isikan(isi, h("div", {},
        soalEl,
        opsiEl,
        h("p.baris-sisi", { gaya: { marginTop: "var(--s4)" } },
          `Tekan 1-${s.options.length} atau A-${HURUF[s.options.length - 1]} `
          + "untuk menjawab.")));

      // Soal berikutnya datang DARI KANAN, bukan dari bawah seperti isi layar
      // yang lain. Arahnya sengaja: ia menyampaikan "maju satu langkah" tanpa
      // satu kata pun, dan itu persis yang barusan terjadi.
      const jauh = 22 * skala();
      animasi(soalEl, {
        opacity: [0, 1],
        transform: [`translate3d(${jauh}px, 0, 0)`, "none"],
      }, { pegas: "jawab" });
      // Fokus mengikuti soal yang baru datang. Sesudah `lanjut.click()` ->
      // `berikutnya()` -> `gambarSoal()`, tombol `lanjut` sudah tidak ada di
      // DOM dan fokus jatuh ke `<body>`: pembaca layar lalu membacakan ruang
      // kosong, bukan pertanyaannya.
      //
      // `tabIndex: -1` di atas yang membuat sebuah `div` bisa menerima fokus
      // sama sekali -- tanpa itu `focus()` diam-diam tidak memindahkan apa pun
      // -- dan `-1`, bukan `0`, menjaganya DI LUAR urutan Tab (`inti.js:464`
      // melewati `[tabindex="-1"]` saat menghitung penghuni perangkap fokus).
      //
      // `preventScroll: true` mengikuti konvensi rumah (`aplikasi.js:272`,
      // `aplikasi.js:297`, `layar-belajar.js:2624`): memindahkan fokus tidak
      // boleh sekaligus menggeser halaman, karena soal berikutnya sudah
      // berada di tempat yang benar dan geseran kedua terasa seperti layar
      // yang meloncat sendiri.
      soalEl.focus({ preventScroll: true });
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
      //
      // Yang benar dapat `denyut` SAJA, dan partikelnya dianggarkan ke layar
      // hasil. Sebuah percikan per jawaban benar terdengar murah sampai
      // dikalikan dua puluh soal: yang tersisa bukan perayaan melainkan
      // kebisingan, dan yang paling dihukum justru orang yang menjawab benar
      // paling banyak. Ambangnya juga nyata — SC 2.3.1 menghitung <=3 pasang
      // perubahan luminansi per detik di >25% medan pandang, dan di 360 px
      // getar + percik + kilau bersamaan sudah mendekatinya.
      if (r.benar) {
        denyut(tombol[r.jawaban_benar]);
      } else {
        if (tombol[pilihan]) getar(tombol[pilihan]);
        denyut(tombol[r.jawaban_benar]);
      }

      const lanjut = h("button.tbl.tbl-utama", { onclick: berikutnya },
        nomor + 1 >= sesi.total ? "Lihat hasil" : "Soal berikutnya →");

      // Penjelasannya berdiri TEPAT DI BAWAH opsi yang dipilih, bukan di kaki
      // daftar. Umpan balik yang menjelaskan hanya bekerja kalau ia
      // berdampingan dengan kegagalannya: di kaki daftar, mata harus kembali
      // ke atas untuk mencocokkan "kenapa" dengan opsi mana yang tadi ditekan,
      // dan pada opsi kelima jarak itu sudah lebih panjang daripada
      // penjelasannya sendiri.
      //
      // `r.penjelasan` datang dari RESPONS /api/kuis/jawab, bukan dari muatan
      // soal — dan itu bukan kebetulan yang boleh "dioptimalkan": muatan soal
      // dijaga bersih dari kunci jawaban, jadi menaruh penjelasan di sana
      // berarti membocorkan jawabannya ke tab Network sebelum orangnya
      // menjawab.
      const blok = h("div.penjelasan", {},
        h("b", {}, r.benar ? "Benar. " : "Belum tepat. "),
        r.penjelasan || (r.benar ? "" : "Jawaban yang benar disorot hijau."),
        h("div.deret", { gaya: { marginTop: "var(--s3)" } }, lanjut));
      const dipilih = tombol[pilihan] || tombol[r.jawaban_benar];
      if (dipilih && dipilih.parentNode) {
        dipilih.parentNode.insertBefore(blok, dipilih.nextSibling);
      } else {
        isi.appendChild(blok);
      }
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
      : "Ini tanda materinya belum menempel, dan itu wajar. Baca ulang "
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
          // Pembanding dengan percobaan SEBELUMNYA -- bukan dengan rekor, yang
          // sudah diurus pil di atas. Penyebutnya `r.total_asli`: pada mode
          // ulangan `r.total` adalah jumlah soal yang diulang, dan
          // membandingkan `benar` sebuah subset dengan skor penuh adalah
          // membandingkan dua hal yang lain.
          //
          // Dua syarat, dan keduanya punya alasan yang sama pentingnya:
          // `sesi_penuh`, karena sesi ulangan sengaja tidak menyentuh skor;
          // dan `terakhir_sebelum !== null`, karena `null` berarti belum ada
          // percobaan sebelumnya -- dan "naik dari 0" untuk orang yang baru
          // pertama menyelesaikan kuis terbaca sebagai penghukuman.
          r.sesi_penuh && r.terakhir_sebelum !== null
            ? h("span.pil", {},
                r.benar > r.terakhir_sebelum ? "naik dari "
                  : r.benar < r.terakhir_sebelum ? "sebelumnya "
                  : "sama dengan ",
                `${r.terakhir_sebelum}/${r.total_asli}`) : null,
          // Percobaan PERTAMA tidak punya pembanding, dan diamnya layar di
          // situ terbaca sebagai ketiadaan -- bukan sebagai permulaan.
          // Cabang ini PELENGKAP pil di atas: `r.terakhir_sebelum === null`
          // sudah berarti "belum pernah ada percobaan penuh", jadi tidak ada
          // field baru yang dibutuhkan dan `api.py` tidak disentuh.
          //
          // Mode ulangan tetap DIAM di kedua cabang: `r.sesi_penuh` berdiri
          // di sini sama seperti di pil pembanding, karena sesi ulangan
          // sengaja tidak menyentuh skor dan "percobaan pertamamu" di sana
          // akan berbohong tentang apa yang baru saja terjadi.
          r.sesi_penuh && r.terakhir_sebelum === null
            ? h("span.pil", {}, "percobaan pertamamu") : null,
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
    window.scrollTo({ top: 0, behavior: "instant" });
    // Perayaannya menyusul sesudah hasilnya terpasang, supaya baranya memercik
    // dari kartu skor yang sudah ada di layar — bukan dari ruang kosong.
    if (sempurna) {
      const kartu = panggung.querySelector(".kartu");
      // Di sinilah anggaran partikelnya dibelanjakan: SATU panggilan per
      // kuis, pada kartu skor yang sudah ada di layar — bukan tujuh belas
      // kali di tujuh belas tombol.
      //
      // Jangan menaruh `kilau(kartu)` di atas baris ini. `kilau(dari)` bukan
      // cahaya saja: begitu diberi sebuah elemen ia ikut memanggil
      // `percikBara(dari)` TANPA opsi (inti.js:593), jadi jumlah bawaannya
      // — enam belas — memercik lebih dulu dan anggarannya jadi dua
      // panggilan. Terukur di Chrome 1280px, tema gelap, data-gerak
      // "penuh", tab terlihat: dua lapis `.bara-percik` berisi [16, 7]
      // titik dengan kilau, satu lapis berisi 7 titik tanpanya.
      percikBara(kartu, { jumlah: 7 });
    }
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

/* Ambang dan atap tangga "lihat jawaban". Keduanya diukur dari kurikulum,
 * bukan dipilih: dari 303 latihan, solusinya bermedian 21 baris, terpanjang
 * 167 baris, dan 76 di antaranya berpanjang <= 12 baris. */
const AMBANG_REKOR = 12;
const LANGKAH_REKOR = 3;

/** Pecah solusi jadi langkah-langkah yang bertumbuh DARI EKOR.
 *
 *  "Lihat contoh solusi" dulu satu pintu tanpa tangga: yang keluar seluruh
 *  programnya, sekaligus, dan sesudah itu tidak ada lagi yang bisa dikerjakan
 *  pelajar selain membacanya. Padahal yang paling sering dibutuhkan orang
 *  buntu bukan seluruh solusinya melainkan BARIS TERAKHIRNYA — di situ
 *  hasilnya dicetak, dan bentuk cetakan itulah yang biasanya tidak ketemu.
 *  Membuka dari KEPALA menyajikan import dan deklarasi, bagian yang justru
 *  sudah ada di editornya sendiri.
 *
 *  Tiap potongan adalah SUFIKS kontinu dari daftar aslinya. Rautan yang
 *  melompat-lompat akan menyajikan kode yang tidak pernah ada sebagai
 *  program, dan pelajar tidak punya cara tahu bagian mana yang disembunyikan.
 *
 *  Jumlah langkahnya ikut diukur: tiga langkah untuk solusi delapan baris
 *  berarti tiga klik untuk empat baris — tangga yang anak-anaknya lebih
 *  banyak daripada yang dinaiki. Jadi `<= AMBANG_REKOR` baris dapat DUA
 *  langkah, sisanya `LANGKAH_REKOR`, berapa pun panjangnya.
 *
 *  Langkah yang tidak menambah satu baris pun dibuang: solusi satu baris
 *  menghasilkan SATU potongan, bukan dua yang identik. Tombol "Lihat lebih
 *  banyak" yang tidak mengubah apa pun adalah tombol yang berujung penolakan.
 *
 *  Murni, tanpa DOM — itu yang membuatnya bisa diadu dari Node, dan sifatnya
 *  dipagari `test_web.TestRekorSolusi`.
 */
export function pisahRekor(baris, maksLangkah = LANGKAH_REKOR) {
  if (!Array.isArray(baris) || baris.length === 0) return [];
  const n = baris.length;
  const alami = n <= AMBANG_REKOR ? 2 : LANGKAH_REKOR;
  const langkah = Math.max(1, Math.min(alami, maksLangkah));
  const potongan = [];
  let panjangLalu = 0;
  for (let i = 1; i <= langkah; i++) {
    // Langkah terakhir dipatok ke `n` apa adanya, bukan dihitung. Pembulatan
    // yang meleset satu baris DI SITU berarti "seluruhnya" yang bukan
    // seluruhnya, dan yang hilang justru baris pertama programnya.
    const panjang = i === langkah ? n : Math.ceil((n * i) / langkah);
    if (panjang <= panjangLalu) continue;
    potongan.push(baris.slice(n - panjang));
    panjangLalu = panjang;
  }
  return potongan;
}

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

  /* Jembatan dari tombol baris pesan galat ke editor. DUA fungsi, bukan satu:
   * `bisa()` dipanggil saat MERENDER untuk memutuskan apakah tombolnya lahir,
   * `ke()` saat tombolnya diklik. Keduanya membaca isi editor SAAT ITU, bukan
   * kode yang dikirim tadi — di antara "Periksa jawaban" dan klik pada pesan
   * galatnya, orangnya mungkin sudah menghapus setengah berkasnya. */
  const tuju = {
    bisa: (n) => n >= 1 && n <= editor.nilai.split("\n").length,
    ke: (n) => editor.keBaris(n),
  };

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
      isikan(hasil, kartuJalan(r, x, kode,
                               (fn) => { lepasPratinjau = fn; }, tuju));
      // SESUDAH dipasang, bukan di dalam `kartuJalan`: yang diukur posisi
      // nyata di halaman, dan kartunya belum ada di halaman sebelum baris di
      // atas selesai.
      pinKeGalat(hasil);
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
      isikan(hasil, kartuPeriksa(r, x, tuju));
      if (r.lulus) {
        status = "lulus";
        gambarStatus();
        // SATU PERISTIWA, SATU DENYUT — aturan mesinnya sendiri
        // (inti.js:518). Jangan menambahkan `denyut()` di jalur ini: cabang
        // `capai` mesin sudah mendenyutkan `dari` (inti.js:554), dan denyut
        // kedua di sini membuat satu kali "latihan lulus" menggerakkan DUA
        // benda.
        //
        // DUA pengukuran di bawah, dan keduanya menyebut keadaannya sendiri —
        // tabel tanpa label itu angka yang suatu hari dibaca sebagai keadaan
        // yang salah. Keduanya: Chrome 1280x800, tema gelap,
        // `#/latihan/python/0`, identitas per ELEMEN dari `getAnimations()`
        // dengan `Element.prototype.animate` dibungkus dan disaring pada
        // durasi 340 ms + keyframe ber-`scale(`), lantai bising 0 benda di
        // kesembilan sel.
        //
        // SESUDAH — keadaan pohon ini, penuh/halus/mati:
        //     capai   2 / 2 / 0      acara   1 / 1 / 0      sentuh  0 / 0 / 0
        // Partikelnya: `capai` satu lapis `.bara-percik` berisi 7 titik di
        // `penuh`, 0 titik di `halus` (gerbang `gerakPenuh()`), 0 benda di
        // `mati`; `acara` satu lapis 26 titik; `sentuh` nol di semua tingkat.
        // Benda KEDUA pada `capai` bukan perayaan layar ini: `aplikasi.js:625`
        // mendenyutkan pencacah XP navbar atas event `progres-berubah`. Itu
        // penanda angka global, bukan penanda peristiwa lokal.
        //
        // SEBELUM — keadaan sewaktu denyut tangan masih ada, penuh/halus/mati:
        //     capai   3 / 3 / 0      acara   2 / 2 / 0      sentuh  1 / 1 / 0
        // Benda ketiga pada `capai` di tabel SEBELUM adalah pencacah XP yang
        // sama; yang dibuang benda PERTAMA — denyut tulisan tangan pada
        // `kotakStatus`.
        //
        // Yang dibuang denyut TANGAN pada `kotakStatus`, bukan `dari`-nya:
        // pil status tetap terbaca tanpa gerak sama sekali. `gambarStatus()`
        // di atas (:618) terukur mengubah LIMA hal serentak — teks
        // `belum selesai` -> `LULUS`, kelas `pil` -> `pil-tumbuh`, warna
        // rgb(179,166,198) -> rgb(52,211,153), latar rgb(29,22,48) -> tint
        // `--tumbuh` 11%, dan ikon 0 -> 1 svg — dan kartu hasil yang baru
        // terpasang berdiri di sebelahnya. Konsekuensi yang DISENGAJA: pada
        // `sentuh` tidak ada yang bergerak sama sekali, dan nol partikel.
        //
        // Perayaannya MENEMPEL pada tombol yang baru saja lulus, bukan
        // menyiram seluruh jendela. Jangan memasang `kilau()` di jalur ini:
        // ia overlay `position: fixed; inset: 0` selebar viewport, dan di
        // tema `terang` ia terukur MELEWATI syarat luas WCAG 2.3.1 — fraksi
        // jendela kilat 341x256 px = 0,3549 > 0,25 — dengan 100% pikselnya
        // berubah lebih GELAP (rerata -0,1603). Isyarat "selamat" yang
        // mengelapkan kertas adalah isyarat salah arah, dan inilah jalur
        // yang paling sering dilewati orang di layar ini.
        //
        // `{ dari }` bukan jalur baru: `tingkatRayakan()` menyimpulkan
        // `capai` untuk `xp_tambah > 0 && !diam`, dan cabang itu sudah
        // melakukan `denyut(dari)` + `percikBara(dari, { jumlah: 7 })` yang
        // memagari dirinya sendiri di `gerakPenuh()` (gerak.js:801).
        rayakan(r.hadiah, { dari: tblPeriksa || hasil });
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
            `Tersedia ${x.hint.length} petunjuk. Coba sendiri dulu; buntu `
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
      "Tandai latihan ini selesai? Ini penilaian jujur dari kamu sendiri: "
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

  /* Gerbangnya MENYATAKAN KEADAAN, tidak menghakimi. Kalimat sebelumnya
   * meramalkan bahwa pelajar akan merasa menguasai sesuatu yang belum ia
   * kuasai — sebuah tebakan tentang isi kepala orang yang menekannya, pada
   * satu-satunya permukaan yang hanya dibuka orang yang sudah buntu. Yang
   * tersisa sekarang cuma angkanya, plus satu kalimat yang menyebut buntu
   * sebagai bagian dari cara kerjanya, karena memang begitu.
   *
   * Kalimat lamanya sengaja TIDAK dikutip di sini: pagarnya
   * (`test_web.TestRekorSolusi.test_kalimat_menghakimi_sudah_tidak_ada`)
   * menyapu SELURUH berkas, dan sebuah komentar yang mengutip kalimat yang
   * dilarang akan memerahkan pagarnya sendiri. Itu bukan pagar yang cerewet —
   * itu satu-satunya bentuk yang tidak bisa diakali dengan memindahkan
   * kalimatnya ke tempat lain di berkas yang sama.
   *
   * Tangganya hidup di dalam BADAN dialog, bukan di `aksi`: setiap aksi kaki
   * menyelesaikan janji `jendela()` dan menutupnya (inti.js:429), jadi
   * "Lihat lebih banyak" sebagai aksi berarti tiga jendela untuk satu solusi.
   * Satu solusi, satu jendela.
   *
   * Dan gerbangnya memang DILEWATI begitu semua petunjuk terbuka: sesudah
   * petunjuk terakhir dibaca tidak ada lagi "coba sendiri dulu" yang tersisa
   * untuk dijaga, jadi menagih konfirmasi di situ cuma menghukum yang paling
   * gigih. Itu disengaja, bukan klausa yang lupa dibuang. */
  async function lihatJawaban() {
    const semua = x.solusi.split("\n");
    const rekor = pisahRekor(semua);
    if (!rekor.length) return;

    const tafsir = hintTerbuka === 0
      ? `${hintTerbuka} dari ${x.hint.length} petunjuk terbuka, belum ada `
        + "yang kamu buka. Petunjuk pertama biasanya sudah cukup, dan yang "
        + "tersisa tetap kamu yang kerjakan."
      : `Kamu membuka ${hintTerbuka} dari ${x.hint.length} petunjuk, itu `
        + "cara yang benar untuk buntu.";

    if (hintTerbuka < x.hint.length && !await konfirmasi(
      `${tafsir} Solusinya dibuka dari ekornya: ${rekor[0].length} baris `
      + `terakhir dulu, bukan ${semua.length} baris sekaligus.`,
      { judul: "Lihat contoh solusi",
        labelYa: "Buka baris terakhir" })) return;

    let langkah = 0;
    const blok = h("div.blok-kode");
    const kendali = h("div", {
      gaya: {
        display: "flex", flexWrap: "wrap", alignItems: "center",
        gap: "var(--s2)", marginTop: "var(--s3)",
      },
    });

    /* Keadaan akhir tiap langkah = keadaan alami DOM-nya. Nol animasi dan nol
     * `fill: "forwards"` di sini: apa yang sudah terbuka wajib tetap terbuka
     * pada gerak "mati", dan satu-satunya cara memastikannya adalah dengan
     * tidak pernah menggantungkan kehadirannya pada sebuah animasi. */
    function gambarRekor() {
      const potongan = rekor[langkah];
      const penuh = langkah >= rekor.length - 1;
      // Ditokenkan ULANG per potongan, bukan diraut dari `x.token_solusi`:
      // token bawaan server adalah token seluruh program, dan memotong
      // deretnya di tengah bisa membelah satu string atau satu komentar
      // jadi dua — yang terlihat pelajar kemudian warna yang terasa acak.
      isikan(blok, praKode(token(potongan.join("\n"), x.sorot)));
      isikan(kendali,
        h("span.pil", {}, penuh
          ? `seluruh ${semua.length} baris`
          : `${potongan.length} baris terakhir dari ${semua.length}`),
        penuh ? null : h("button.tbl.tbl-kecil", {
          onclick: () => { langkah += 1; gambarRekor(); },
        }, "Lihat lebih banyak"),
        // Salin baru ADA saat seluruhnya terbuka. Menyalin separuh solusi
        // adalah cara tercepat membuat jawaban yang salah terlihat sah: yang
        // tertempel jalan, outputnya cuma sebagian, dan yang disalahkan
        // pelajar adalah pemahamannya sendiri.
        penuh ? h("button.tbl.tbl-kecil.tbl-hantu", {
          onclick: () => salin(x.solusi),
        }, "Salin seluruhnya") : null);
    }
    gambarRekor();

    await jendela({
      judul: "Contoh solusi: " + x.judul,
      lebar: true,
      isi: h("div", {},
        h("p.kepala-sub", { gaya: { margin: "0 0 var(--s3)" } },
          "Ini cuma SATU cara. Kode yang berbeda belum tentu salah, selama "
          + "outputnya sama. Yang terbuka lebih dulu baris-baris TERAKHIR: "
          + "di situlah hasilnya dicetak, dan sering itu saja sudah cukup."),
        blok, kendali),
      aksi: [{ label: "Tutup", nilai: null, kelas: "tbl-utama" }],
    });
  }

  async function bandingkan() {
    const baris = pasangkanUbahan(
      bedaBaris(x.solusi.split("\n"), editor.nilai.split("\n")));
    await jendela({
      judul: "Kodemu dibanding contoh solusi",
      lebar: true,
      isi: h("div", {},
        h("p.kepala-sub", { gaya: { margin: "0 0 var(--s3)" } },
          "Baris hijau dari contoh solusi, baris merah dari kodemu. Yang "
          + "dicoret hilang dari kodemu, yang bergaris bawah kamu tambahkan. "
          + "Beda tulisan itu wajar. Yang menentukan lulus cuma outputnya."),
        h("div.diff", {}, baris.length
          ? baris.map((d) => h("div.diff-baris"
              + (d.tanda === "=" ? ".diff-sama"
                 : d.tanda === "-" ? ".diff-kurang" : ".diff-tambah"), {},
              h("span.diff-nomor", {}, String(d.nomor)),
              h("span.diff-tanda", {}, d.tanda === "=" ? "│" : d.tanda),
              h("span.diff-isi", {},
                d.segmen ? segmenKata(d.segmen) : d.teks)))
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
            ? h("span.pil", {}, "dinilai otomatis")
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
            "Kondisi awal (sudah disiapkan, tak perlu kamu tulis)"),
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
        `Nama kelasnya harus ${x.berkas.nama.replace(/\.java$/, "")}: javac `
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

/* Lebar perangkat yang bisa dipilih untuk pratinjau. Urutannya dari sempit ke
   lebar lalu "lebar penuh" di ujung, karena yang terakhir itu BUKAN sebuah
   lebar melainkan tiadanya pilihan — keadaan bawaan, dan tempatnya di ujung
   daftar supaya ia tidak terbaca sebagai angka keempat.

   Tiga angkanya bukan karangan: 360 lebar yang dipakai seluruh audit layar
   sempit di repo ini, 768 batas tablet, 1280 lebar laptop yang juga viewport
   baku pengukuran di sini. */
const LEBAR_PRATINJAU = [
  { v: 360, nama: "360", ket: "Tata ulang halamanmu selebar ponsel, 360 px" },
  { v: 768, nama: "768", ket: "Tata ulang halamanmu selebar tablet, 768 px" },
  { v: 1280, nama: "1280", ket: "Tata ulang halamanmu selebar laptop, 1280 px" },
  { v: 0, nama: "lebar penuh", ket: "Selebar panelnya sendiri" },
];

/* SATU-SATUNYA tempat lebar terpilih tinggal.
 *
 * Ia duduk di lingkup MODUL, bukan di dalam `kartuJalan`, dan itu bukan
 * kemalasan: closure kartu itu lahir baru setiap kali Jalankan ditekan, jadi
 * pilihan yang disimpan di sana lenyap tepat pada peristiwa yang paling sering
 * terjadi di layar ini. Pelajar yang sedang memeriksa halamannya di 360 px
 * menekan Jalankan untuk melihat akibat satu suntingan, dan menemukan
 * pratinjaunya melompat kembali ke lebar penuh — yang hilang bukan setelan
 * melainkan perbandingan yang sedang ia kerjakan.
 *
 * TIDAK di `localStorage` dan TIDAK di berkas mana pun. Ini alat periksa
 * sesaat, bukan preferensi tampilan: orang yang pernah mengintip halamannya di
 * 360 px tidak sedang menyatakan ia ingin selalu melihatnya begitu, dan
 * setelan yang bertahan melewati tutup-buka browser akan membuatnya menemukan
 * pratinjau sempit berbulan-bulan kemudian tanpa ingat pernah memintanya.
 *
 * `pratinjau.js` memegang nilai yang sudah DIKENAKAN, bukan salinan kedua
 * otoritas ini — hubungannya sama dengan tinggi yang dilaporkan halaman. */
let lebarPratinjau = 0;

/** Baris pil pemilih lebar perangkat untuk sebuah pratinjau.
 *
 *  Keadaan terpilih ditandai DUA kali: kelasnya dan `aria-pressed`. Warna
 *  tidak dibacakan pembaca layar, jadi `.tbl-pilih` sendirian berarti
 *  satu-satunya pelajar yang tidak bisa tahu lebar mana yang sedang berlaku
 *  adalah yang paling bergantung pada tahu. Bentuknya kembar dengan tab
 *  Tampilan/Struktur di `layar-belajar.js` (`kartuKeluaran`), dan kekembaran
 *  itu disengaja: dua pemilih yang bekerja sama di layar berbeda sebaiknya
 *  terlihat sama.
 */
function barisLebarPratinjau(pv) {
  const pil = LEBAR_PRATINJAU.map((p) => h("button.tbl.tbl-kecil", {
    data: { lebar: String(p.v) }, title: p.ket,
  }, p.nama));
  const tandai = () => {
    LEBAR_PRATINJAU.forEach((p, i) => {
      const kini = p.v === lebarPratinjau;
      pil[i].classList.toggle("tbl-pilih", kini);
      pil[i].classList.toggle("tbl-hantu", !kini);
      pil[i].setAttribute("aria-pressed", String(kini));
    });
  };
  pil.forEach((b, i) => b.addEventListener("click", () => {
    lebarPratinjau = LEBAR_PRATINJAU[i].v;
    pv.setLebar(lebarPratinjau);
    tandai();
  }));
  tandai();
  // Jaraknya dari tangga `--s`, bukan dari angka piksel, dan inline karena
  // baris ini tidak membawa satu pun aturan gaya BARU: pilnya sudah `.tbl`,
  // labelnya sudah `.mata`. Presedennya `kartuJalan` di bawah, yang menyetel
  // jarak antar-bagiannya dengan cara yang sama.
  return h("div.pratinjau-lebar", {
    gaya: {
      display: "flex", flexWrap: "wrap", alignItems: "center",
      gap: "var(--s2)", marginBottom: "var(--s2)",
    },
  }, h("span.mata", {}, "Lebar perangkat"), ...pil);
}

function kartuJalan(r, x, kode, simpanLepas, tuju) {
  // Untuk HTML dan CSS, "keluaran" adalah pohon struktur -- benar untuk
  // menilai, salah untuk ditonton. Di layar latihan justru di sinilah orang
  // paling ingin melihat halamannya: ia baru saja menulisnya sendiri.
  const dok = kode && bisaDipratinjau(x.runner)
    ? dokumenPratinjau(x.runner, kode) : "";
  let pv = null;
  if (dok) {
    // Lebar yang sedang berlaku dikirim SAAT DIBUAT, bukan dipasang sesudahnya
    // lewat `setLebar`. Bedanya satu frame yang terlihat: kartu yang lahir di
    // lebar penuh lalu disempitkan akan menggambar halamannya sekali di lebar
    // yang salah lebih dulu.
    pv = pratinjauHtml(dok, { lebar: lebarPratinjau });
    simpanLepas(pv.lepas);
  }
  return h("div.kartu.masuk", {},
    h("div.deret", { gaya: { marginBottom: "var(--s3)" } },
      h("h3", {}, dok ? "Halamanmu" : "Hasil menjalankan"),
      h("span.deret-kanan"),
      h("span.pil" + (r.kode_keluar === 0 ? ".pil-tumbuh" : ".pil-salah"), {},
        `kode keluar ${r.kode_keluar}`),
      h("span.pil", {}, r.detik + " detik"),
      // Sinyal overflow panel, dan ia lahir TERSEMBUNYI: yang menyalakannya
      // cuma pengukuran di `pinKeGalat()`, bukan dugaan dari panjang keluaran.
      // Tanpa chip ini keluaran 301 baris di tata letak lebar terbaca sebagai
      // keluaran 8 baris — satu-satunya isyarat hari ini sebuah bilah gulir
      // setipis `scrollbar-width: thin` (gaya.css:4890).
      h("span.pil.pil-tenang", { hidden: true, data: { lebih: "bawah" } },
        "keluaran lebih panjang dari panel, gulir ke bawah")),
    r.stdin ? h("div", { gaya: { marginBottom: "var(--s2)" } },
      h("span.mata", {}, "Masukan yang dikirim"),
      h("div.terminal", {}, r.stdin)) : null,
    pv ? h("div", { gaya: { marginBottom: "var(--s3)" } },
      halamanDikarang(x.runner, kode) ? h("p.pratinjau-ket", {},
        "Halaman contoh ini dibuatkan dari pemilih di CSS-mu sendiri: ",
        h("b", {}, "bukan"), " berkas HTML-mu.") : null,
      barisLebarPratinjau(pv),
      pv.el) : null,
    h("span.mata", {}, dok ? "Struktur yang dinilai" : "Keluaran"),
    h("div.terminal", {}, r.keluaran),
    r.galat ? blokGalat(r.galat, r.fase, tuju, true) : null,
    r.timeout ? h("div.diagnosa", {}, h("span.panah", {}, "→"),
      h("div", {}, `Program dihentikan setelah ${x.batas_waktu} detik. `
        + "Kemungkinan ada loop yang tidak pernah berhenti.")) : null,
    r.catatan ? h("div.baris-sisi", { gaya: { marginTop: "var(--s2)" } },
      r.catatan) : null);
}

/* Isyarat bahwa pengguna sudah mengambil alih gulir panel hasil. Daftarnya
   kembar dengan `SENTUHAN_GULIR` di layar-belajar.js dan alasannya sama:
   `keydown` bisa datang karena panel yang bisa digulir juga bisa difokus. */
const SENTUHAN_HASIL = ["wheel", "pointerdown", "keydown"];

/* Batas waktu pengamat ukuran panel hasil. Angkanya kembar dengan
   `PIN_BARA_MS` (layar-belajar.js:766) dan itu disengaja: keduanya menjawab
   satu pertanyaan — berapa lama sebuah pengamat boleh hidup di layar yang
   dibuka lalu ditinggal. */
const PIN_HASIL_MS = 4000;

/** Nyalakan sinyal "ada lebih di bawah", lalu antar panel ke pesan galatnya.
 *
 *  Panel hasil DIPAGARI tingginya, tapi hanya di tata letak lebar:
 *  `gaya.css:4890` memberi `.kerja-hasil { overflow-y: auto; max-height:
 *  46cqh }` di dalam `@container panggung (min-width: 1100px)`, dengan
 *  `container-type: size` di `.kerja-kode` (`gaya.css:4873`). Akibatnya
 *  keluaran panjang + blok galat di bawahnya = blok galat SELURUHNYA di luar
 *  jendela panel sementara `scrollTop` tetap 0, dan satu-satunya isyarat
 *  bahwa jawabannya ada di bawah sebuah bilah gulir setipis `thin`.
 *
 *  Dua hal yang dikerjakan di sini, dan keduanya dari PENGUKURAN:
 *
 *    (1) chip `[data-lebih="bawah"]` dinyalakan kalau `scrollHeight >
 *        clientHeight`. Bukan dari panjang keluaran — di tata letak sempit
 *        panel ini tidak dipagari sama sekali, jadi menebaknya dari jumlah
 *        baris akan memasang sinyal palsu di layar yang tidak memotong apa pun.
 *    (2) kalau ada blok galat DAN ia tidak muat, panel ITU SENDIRI digulir
 *        dengan `scrollTop` sampai puncak bloknya ada di puncak jendela panel.
 *
 *  `scrollIntoView` DILARANG di sini: ia menggulir SEMUA leluhur termasuk
 *  dokumen — kelas bug yang sama yang membuat `bawaKeTengah()` ada. Dan tanpa
 *  animasi apa pun: `scroll-behavior` tidak mewaris dari `html`, jadi yang
 *  terhitung pada `.kerja-hasil` adalah `auto` dan `scrollTop =` sudah instan
 *  di ketiga tingkat gerak. Guliran dan sinyalnya tetap terjadi pada tingkat
 *  `mati` — keduanya INFORMASI, bukan hiasan.
 *
 *  Pengukurannya lewat `saatSiap()`, bukan `requestAnimationFrame` polos:
 *  layar dibangun utuh sebelum router menempelkannya, jadi rect yang dibaca
 *  di frame pemasangan bisa nol (invarian #15a).
 *
 *  Dan `saatSiap` menjawab "sudah terpasang dan punya ukuran", BUKAN
 *  "ukurannya sudah berhenti berubah" — untuk HTML/CSS tinggi kartu BERTAMBAH
 *  sesudah iframe pratinjau melaporkan dirinya (`pratinjau.js`; AGENTS.md
 *  melarang `transition: height` justru karena itu). Karena itu pengamat
 *  ukuran mengawasi KARTUNYA, bukan cuma panelnya: panel ber-`max-height`
 *  tidak pernah berubah ukuran ketika isinya tumbuh.
 *
 *  Pin-nya WAJIB lepas. Posisi gulir adalah keadaan PENGGUNA, dan merebutnya
 *  kembali sesudah dia menggeser sendiri lebih buruk daripada tidak mem-pin
 *  sama sekali. Bentuknya sengaja kembar dengan `pinKeHariIni()`
 *  (layar-belajar.js:801): putus pada sentuhan pertama, dan putus pada batas
 *  waktu. */
function pinKeGalat(panel) {
  const chipBawah = panel.querySelector('[data-lebih="bawah"]');
  const blok = panel.querySelector("[data-galat]");
  const chipAtas = blok ? blok.querySelector('[data-lebih="atas"]') : null;

  /* Posisi blok galat relatif jendela panel, diambil dari KOORDINAT LAYOUT.
   *
   * `getBoundingClientRect()` termasuk transform, dan kartu hasilnya
   * `div.kartu.masuk`: `@keyframes masuk` (gaya.css:1192) berangkat dari
   * `translateY(7px)` selama `--sedang` 220 md (gaya.css:442). Mengukur dengan
   * rect berarti menggulir ke tempat yang akan BERPINDAH tujuh piksel ke atas
   * begitu animasinya selesai — dan `ResizeObserver` tidak akan pernah
   * menangkapnya, karena transform tidak mengubah satu kotak layout pun.
   *
   * Terukur, Chrome 152, `#/latihan/python/0`, 300 baris + ZeroDivisionError:
   * pada `penuh` residu -3 -> -6 -> -7 seiring translateY 3,39 -> 0,41 -> 0 px
   * (animasi 50 -> 133 -> 220 md) dengan `scrollTop` 532; pada `mati`, tempat
   * `gaya.css:5125` mematikan animasinya, `transform: none` dan `scrollTop`
   * 525 -- tepat tujuh kurang, residu 0. Selisihnya ADALAH translateY-nya.
   *
   * Jalan keluarnya DUA, dan yang pertama saya coba lalu tolak: akumulasi
   * `offsetTop` sampai akar memang buta terhadap transform, tapi `offsetTop`
   * membulatkan ke bilangan bulat — terukur residunya pindah dari -7 ke +1,
   * lebih baik tapi belum nol, dan sisa satu piksel itu pembulatannya sendiri.
   *
   * Yang dipakai: rect (sub-piksel) DIKURANGI translateY simpul yang
   * beranimasi di antara blok dan panel. Lingkarannya naik sampai `panel`
   * supaya ia tetap benar kalau suatu hari ada dua simpul bertransform
   * bersarang, bukan cuma kartunya. */
  const geserTransform = () => {
    let dy = 0;
    for (let n = blok; n && n !== panel; n = n.parentElement) {
      const t = getComputedStyle(n).transform;
      if (t && t !== "none") dy += new DOMMatrixReadOnly(t).m42;
    }
    return dy;
  };

  const kotak = () => {
    const kp = panel.getBoundingClientRect();
    const kb = blok.getBoundingClientRect();
    const dy = geserTransform();
    return { atas: kb.top - kp.top - dy, bawah: kb.bottom - kp.top - dy };
  };

  const pasang = () => {
    // Chipnya DISEMBUNYIKAN lebih dulu, lalu panelnya diukur. Terukur kenapa:
    // di 655x754 panel sempat `scroll 784 > client 777` saat kartu masih
    // tumbuh, lalu mengendap di `817 == 817` — tidak memotong apa pun. Kalau
    // tinggi chip ikut memutuskan, panel yang pas-pasan berkedip: chip muncul
    // -> panelnya memotong -> chip tetap muncul, selamanya, atas keadaan yang
    // sudah tidak ada. Keputusan ini karena itu dibuat dari keadaan TANPA
    // chip, dan dibuat ulang setiap kali ukurannya berubah.
    if (chipBawah) chipBawah.hidden = true;
    if (chipAtas) chipAtas.hidden = true;

    // DUA syarat, dan syarat pertama yang paling mudah dilupakan: panelnya
    // harus benar-benar MEMOTONG. Di tata letak sempit `overflow-y` terhitung
    // `visible`, dan di sana `scrollHeight` terukur melebihi `clientHeight`
    // PERMANEN tujuh piksel — margin anak yang menyembul dari kotak yang tidak
    // memotong apa pun. Selisih tinggi sendirian karena itu bukan "ada lebih
    // di bawah"; ia cuma "ada margin". Yang menjawab "memotong" adalah
    // propertinya, bukan selisihnya.
    const cs = getComputedStyle(panel);
    const memotong = cs.overflowY === "auto" || cs.overflowY === "scroll";
    const lebih = memotong && panel.scrollHeight > panel.clientHeight;
    if (chipBawah) chipBawah.hidden = !lebih;
    if (!lebih || !blok) return;

    let k = kotak();
    if (k.atas >= 0 && k.bawah <= panel.clientHeight) return;

    // Chipnya dinyalakan SEBELUM rect-nya dipakai menggulir. `.mata` dan chip
    // ini masing-masing memakai barisnya sendiri, jadi reveal menggeser isi
    // blok ke bawah — rect yang dibaca sebelum reveal akan mendarat sependek
    // tinggi chip itu.
    if (chipAtas) { chipAtas.hidden = false; k = kotak(); }

    const geser = (d) => {
      const maks = panel.scrollHeight - panel.clientHeight;
      panel.scrollTop = Math.max(0, Math.min(maks, panel.scrollTop + d));
    };
    // SATU guliran, bukan dua. Versi sebelumnya memanggil `geser()` kedua kali
    // dengan alasan yang terukur SALAH ("menyalakan chip menggeser isi di atas
    // blok, jadi delta pertama 7 px kelebihan"). Tujuh piksel itu bukan dari
    // chip melainkan dari `translateY` animasi masuk, dan koreksi kedua tidak
    // pernah menutupnya karena ia membaca rect yang sama-sama ter-transform.
    // Dengan `kotak()` memakai koordinat layout, `atas` sesudah guliran
    // pertama adalah nol secara aritmetik -- guliran kedua jadi dusta yang
    // tidak melakukan apa-apa, dan dusta yang tidak melakukan apa-apa tetap
    // dusta.
    geser(k.atas);
  };

  saatSiap(panel, () => {
    pasang();
    if (typeof ResizeObserver !== "function") return;

    // Pengamatnya memanggil `pasang()` TANPA penjaga "tinggi berubah atau
    // tidak", dan itu koreksi atas versi pertama fungsi ini: penjaga seperti
    // itu membuat keputusan sesaat TERKUNCI — terukur, chip menyala di
    // 655x754 atas keadaan yang hilang 180 md kemudian, dan pin di 1280x800
    // berhenti 7 px kelebihan tanpa pernah mengoreksinya.
    //
    // Yang menahan lingkarannya bukan penjaga itu melainkan sifat `pasang()`
    // sendiri: ia IDEMPOTEN — dari keadaan apa pun ia mendarat di keadaan yang
    // sama, jadi tik kedua menghasilkan ukuran yang identik dan peramban tidak
    // mengirim pemberitahuan ketiga. Dan karena ia dipanggil ulang, pin-nya
    // MENUJU alih-alih menembak sekali.
    let lepas = () => {};
    const pengamat = new ResizeObserver(() => pasang());
    const jam = setTimeout(() => lepas(), PIN_HASIL_MS);

    lepas = () => {
      clearTimeout(jam);
      pengamat.disconnect();
      for (const nama of SENTUHAN_HASIL) panel.removeEventListener(nama, lepas);
    };
    for (const nama of SENTUHAN_HASIL) {
      panel.addEventListener(nama, lepas, { passive: true });
    }
    pengamat.observe(panel);
    // Kartu hasilnya, bukan cuma panelnya: panel ber-`max-height` tidak pernah
    // berubah ukuran ketika kartu di dalamnya tumbuh — dan pratinjau iframe
    // justru tumbuh SESUDAH frame pemasangan.
    if (panel.firstElementChild) pengamat.observe(panel.firstElementChild);
    // Dan BLOK GALATNYA sendiri. Sejarahnya layak ditulis karena ia menandai
    // batas pengamat ukuran: residu -7 px dulu dikira pelayangan tata letak
    // dan blok ini ditambahkan untuk menangkapnya — TIDAK berhasil, angkanya
    // tidak bergerak sedikit pun. Sebabnya kemudian terukur: `translateY`
    // animasi masuk, yang tidak mengubah satu kotak layout pun sehingga
    // `ResizeObserver` memang buta terhadapnya. Yang menutupnya `kotak()` yang
    // kini memakai koordinat layout. Blok ini tetap diamati karena ia memang
    // kotak yang relevan kalau ISINYA berubah tinggi (galat yang bertambah
    // baris), bukan karena ia pernah memperbaiki residu itu.
    if (blok) pengamat.observe(blok);
  });
}

/* Nomor baris yang disebut SATU baris pesan galat, atau 0 kalau ia tidak
 * menyebut satu pun.
 *
 * Kedua pola di bawah PORT dari `inti/galat.py` — `_POLA_BARIS_BERKAS` dan
 * `_POLA_KATA_LINE` — dan kekembarannya disengaja. Menambah field `nomor` di
 * responsnya berarti dua tempat membentuk satu angka, padahal geserannya
 * sudah selesai di server: `_galat_json` memanggil `rapikan()` dengan
 * `baris_setup`, jadi nomor yang sampai ke sini SUDAH menunjuk berkas milik
 * pelajar. Presedennya `sorot.js` sebagai port `inti/sorot.py`; yang membayar
 * kekembaran ini `TestLompatKeBarisGalat` (tests/test_web.py:9021), yang
 * menjalankan `node` atas korpus `tests/test_galat.py` dan mengadu kedua pola
 * di bawah dengan padanannya di Python — jadi kekembarannya diukur, bukan
 * dipercaya.
 *
 * Baris setup tidak pernah lolos sebagai angka: `rapikan()` menukar nomor
 * yang jatuh di bawah 1 dengan teks `[bagian KONDISI AWAL]`. Itu sebabnya
 * tombolnya tidak bisa menunjuk baris yang bukan tulisan pelajar. */
const POLA_BARIS_BERKAS = /[\w./\\-]+\.\w+:(\d+)/;
const POLA_KATA_LINE = /\bline (\d+)/;

function nomorDiBaris(teks) {
  const m = POLA_BARIS_BERKAS.exec(teks) || POLA_KATA_LINE.exec(teks);
  return m ? parseInt(m[1], 10) : 0;
}

/* Satu baris pesan galat = satu simpul. Yang menyebut nomor jadi <button>
 * yang mengantar caret ke baris itu; yang tidak tetap teks biasa — jadi blok
 * galat tanpa satu pun nomor terlihat PERSIS seperti sebelum tombol ini ada.
 *
 * Nomornya dibaca dari `g.baris`, teks yang benar-benar dirender, bukan dari
 * `g.mentah`: `_galat_json` meringkas `mentah` jadi maksimal 14 baris, jadi
 * nomor yang hanya hidup di `mentah` akan melahirkan tombol untuk baris yang
 * tidak bisa dibaca siapa pun di layar ini.
 *
 * Tombolnya juga tidak lahir kalau editornya tidak punya baris sebanyak itu.
 * Tombol yang berakhir "baris itu tidak ada" lebih buruk daripada tidak ada
 * tombol — dan `tuju.bisa()` menjawabnya dari isi editor saat ini, bukan dari
 * panjang kode yang dikirim tadi. */
function barisGalat(baris, tuju) {
  const simpul = [];
  baris.forEach((teks, i) => {
    const pisah = i < baris.length - 1 ? "\n" : "";
    const n = tuju ? nomorDiBaris(teks) : 0;
    if (n && tuju.bisa(n)) {
      simpul.push(h("button", {
        type: "button",
        "aria-label": "Ke baris " + n,
        onclick: () => tuju.ke(n),
        gaya: {
          font: "inherit", color: "inherit", background: "none",
          border: "0", padding: "0", margin: "0", textAlign: "left",
          whiteSpace: "inherit", cursor: "pointer",
          borderBottom: "var(--tebal-garis) dotted currentColor",
        },
      }, teks));
      if (pisah) simpul.push(pisah);
    } else {
      simpul.push(teks + pisah);
    }
  });
  return simpul;
}

/* `denganLebih` dipakai HANYA oleh kartu Jalankan, dan bawaannya palsu supaya
 * pemanggil di `kartuUji` berperilaku byte-identik: di sana blok galat tinggal
 * di dalam kartu uji yang sudah pendek, dan panel tidak pernah digulir ke
 * sana. Chipnya lahir TERSEMBUNYI — `pinKeGalat()` yang menyalakannya, dan
 * hanya kalau panel benar-benar digulir.
 *
 * Yang TIDAK berubah: `barisGalat(g.baris, tuju)` dan isinya. Teks baris galat
 * yang dirender adalah kontrak hun 3, dan chip ini berdiri di luar `.terminal`
 * — bukan di dalamnya. */
function blokGalat(g, fase, tuju, denganLebih) {
  return h("div", { data: { galat: "1" }, gaya: { marginTop: "var(--s3)" } },
    h("span.mata", {},
      fase === "kompilasi" ? "Pesan dari compiler" : "Pesan error"),
    denganLebih
      ? h("span.pil.pil-tenang", { hidden: true, data: { lebih: "atas" } },
          "panel digulir ke pesan ini; keluaran lengkap ada di atasnya")
      : null,
    h("div.terminal.terminal-galat", {}, barisGalat(g.baris, tuju)),
    g.artinya.length ? h("div.arti", {},
      h("b", {}, "Artinya"),
      g.artinya.map((t) => h("div", {}, "• " + t))) : null);
}

function kartuPeriksa(r, x, tuju) {
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
                  : "Belum sesuai. Lihat bedanya di bawah."),
        h("span.deret-kanan"),
        h("span.pil", {}, `${lulus}/${r.uji.length} uji lulus`),
        h("span.pil", {}, r.detik + " detik")),
      !r.lulus ? h("p", { gaya: { margin: "var(--s2) 0 0",
                                  color: "var(--teks-2)",
                                  fontSize: "var(--t-ui)" } },
        "Baris hijau bertanda − adalah yang diharapkan; baris merah bertanda + "
        + "adalah punyamu.") : null),
    deretUji(r, tuju));
}

/* Hasil uji muncul satu per satu, urut dari uji pertama. Kalau uji ketiga yang
   gagal, urutan itulah yang membawa mata ke sana: dua kartu hijau lewat, lalu
   berhenti di yang merah. Muncul serentak tidak memberi arah apa pun. */
function deretUji(r, tuju) {
  const kotak = h("div", { gaya: { display: "grid", gap: "0" } },
    r.uji.map((u) => kartuUji(u, tuju)));
  ungkap(kotak, { per: 60, maks: 300, geser: 8, pegas: "jawab" });
  return kotak;
}

function kartuUji(u, tuju) {
  return h("div.uji" + (u.lulus ? ".lulus" : ".gagal"), {},
    h("div.uji-kepala", {},
      h("span.uji-cap", {}, u.lulus ? "LULUS" : "GAGAL"),
      h("span.uji-nama", {}, u.nama),
      u.stdin ? h("span.pil", {},
        "input: " + u.stdin.replace(/\n/g, "⏎").slice(0, 24)) : null),
    !u.lulus ? h("div.uji-badan", {},
      u.galat ? blokGalat(u.galat, "", tuju) : null,
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
    const kata = d.tanda === "~" ? bedaKata(d.harapan, d.aktual) : null;

    // Pasangan yang berbeda HANYA pada spasi diciutkan jadi satu baris. Dua
    // baris penuh untuk "halo··dunia" lawan "halo·dunia" tidak menambah satu
    // pun keterangan: keduanya terbaca identik dari ujung ke ujung, dan yang
    // sebenarnya membedakannya sudah ditandai di dalam segmennya.
    //
    // `d.tampak` SATU-SATUNYA yang memutuskan "bedanya cuma spasi", dan yang
    // memilikinya `api._beda_json`: di sana `tampak` dihitung sekali dengan
    // membandingkan kedua sisi modulo spasi, dan di sana pula `harapan` dan
    // `aktual` lalu DITUKAR dengan hasil `beda.tampakkan` (`inti/beda.py`,
    // `SPASI_TAMPAK`/`TAB_TAMPAK`). Konsekuensinya mengikat ke baris ini:
    // begitu `tampak` menyala, tidak ada satu pun spasi asli yang tersisa di
    // string yang sampai ke `bedaKata` -- semuanya sudah jadi `·` dan `→`,
    // dan bagi `pecahToken` keduanya token BUKAN-spasi seperti huruf mana
    // pun. Jadi jangan pernah menghitung ulang jawabannya dari teks itu:
    // predikat kedua pernah berdiri persis di sini, menuntut "seluruh segmen
    // yang berubah cuma spasi", dan karena teksnya sudah ditukar lebih dulu
    // predikat itu mustahil benar -- cabang ini terukur tidak pernah menyala
    // satu kali pun, justru pada pasangan yang jadi alasannya ditulis.
    //
    // Baris `=` tidak bisa sampai ke sini: ia sudah `continue` di atas, DAN
    // `kata` null untuknya karena cuma `~` yang dihitung. Dua pagar untuk
    // satu hal, dan itu disengaja -- `tampak` menyala untuk baris `=` juga,
    // karena kedua sisinya memang persis sama (`inti/beda.py:189`).
    //
    // `kata` tetap diperiksa, dan juga bukan basa-basi: baris ciut merender
    // `kata.gabung`, dan `bedaKata` boleh menyerah -- di atas BATAS_SEL_KATA,
    // atau tanpa satu token jangkar. Untuk baris sepanjang itu dua baris
    // penuh memang jawaban yang benar.
    //
    // Penunjuk kolom ↑ sengaja TIDAK ikut di baris ciut: segmen spasi yang
    // dicoret menunjuk karakternya sendiri, dan itu lebih tepat daripada
    // sebuah nomor kolom yang dihitung terhadap `harapan` lalu dipasang di
    // bawah teks GABUNGAN yang kolomnya sudah bergeser.
    if (kata && d.tampak) {
      baris.push(barisDiff(nomor, "~", null, "diff-sama", "spasi saja",
                           kata.gabung));
      continue;
    }

    if (d.tanda === "-" || d.tanda === "~") {
      baris.push(barisDiff(nomor, "-", d.harapan, "diff-kurang", "diharapkan",
                           kata && kata.kiri));
    }
    if (d.tanda === "+" || d.tanda === "~") {
      baris.push(barisDiff(nomor, "+", d.aktual, "diff-tambah", "punyamu",
                           kata && kata.kanan));
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

/* Parameter `segmen` opsional dan sengaja TERAKHIR: enam pemanggil lama
 * memanggilnya dengan lima argumen dan harus tetap berarti persis sama. Kalau
 * ia ada, ia yang dipakai dan `teks` diabaikan -- segmen itu sendiri sudah
 * memuat seluruh teks barisnya, dan menggambar keduanya akan menampilkan baris
 * yang sama dua kali. */
function barisDiff(nomor, tanda, teks, kelas, ket, segmen) {
  return h("div.diff-baris." + kelas, {},
    h("span.diff-nomor", {}, String(nomor)),
    h("span.diff-tanda", {}, tanda),
    h("span.diff-isi", {}, segmen
      ? segmenKata(segmen)
      : (teks === null || teks === undefined ? "" : teks)),
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

/* Atap biaya `bedaKata`, dalam SEL tabel (jumlah token kiri x kanan).
 *
 * Baris keluaran bisa sepanjang apa pun -- yang menulisnya pelajar, bukan
 * kurikulum -- sementara tabel LCS-nya O(n*m). Tanpa atap, satu baris keluaran
 * puluhan ribu huruf cukup untuk menggantung tab-nya, dan yang terlihat bukan
 * error melainkan tombol Jalankan yang berhenti menjawab. Di atas atap ini
 * `bedaKata` menyerah dan mengembalikan `null`, lalu pemanggilnya menggambar
 * baris utuh seperti sebelum hun ini -- yang hilang granularitasnya, bukan
 * diff-nya. */
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

function pecahToken(s) {
  // `match` dengan bendera /g tidak mewarisi `lastIndex`, jadi polanya boleh
  // dibagi antar panggilan tanpa membuat hasilnya bergantung urutan panggilan.
  return s.match(POLA_TOKEN_KATA) || [];
}

/** Diff per-KATA di dalam satu pasang baris yang sudah diketahui berubah.
 *
 *  `bedaBaris` di atas dan `Beda.baris` di Python sama-sama berhenti di
 *  tingkat BARIS: keduanya bisa mengatakan "baris ini berubah", tidak satu pun
 *  bisa mengatakan KATA MANA. Untuk baris sepanjang satu kalimat keluaran itu
 *  berarti pekerjaan membandingkan dua baris panjang tetap diserahkan ke mata
 *  pelajar -- padahal justru itu yang bisa dikerjakan komputer.
 *
 *  MURNI, dan itu syarat, bukan sifat kebetulan: dua string masuk, segmen
 *  keluar. Tidak menyentuh DOM, tidak memanggil `h()`, tidak membaca jam,
 *  tidak memakai acak. `tests/test_web.TestBedaKata` MENGEKSTRAK sumber fungsi
 *  ini beserta dua tetangganya lalu menjalankannya di Node tanpa satu pun
 *  modul lain -- jadi begitu ia mulai memanggil sesuatu dari luar, tesnya
 *  MERAH, dan kemurniannya berhenti jadi klaim di komentar.
 *
 *  Keluarannya tiga daftar segmen atas token yang sama:
 *
 *    kiri    `=`/`-`      baris harapan, dengan yang hilang ditandai
 *    kanan   `=`/`+`      baris pelajar, dengan yang bertambah ditandai
 *    gabung  `=`/`-`/`+`  satu baris inline memuat kedua sisi dalam urutan
 *                         dokumen, dipakai saat pasangannya diciutkan
 *
 *  Dan HANYA ketiganya. Tidak ada predikat "bedanya cuma spasi" di sini.
 *  Pernah ada, dan ia tidak pernah bisa benar: satu-satunya yang menanyakannya
 *  adalah `gambarBeda`, dan teks yang ia serahkan sudah ditukar `api._beda_json`
 *  jadi versi ber-`·`/`→` lebih dulu -- jadi yang tersisa untuk diperiksa bukan
 *  lagi spasi. Keputusan itu sekarang milik `d.tampak` seorang. Pemanggil yang
 *  kedua, `pasangkanUbahan` di jalur diff KODE, tidak pernah menanyakannya.
 *
 *  Mengembalikan `null` -- artinya "gambar saja baris utuh" -- di tiga
 *  keadaan, dan ketiganya dipilih, bukan kelalaian:
 *
 *  * Salah satu sisi bukan string, atau tokennya nol. Tidak ada yang
 *    dibandingkan.
 *  * Tabelnya melewati BATAS_SEL_KATA. Alasannya di atas.
 *  * Nol token BUKAN-SPASI yang sama. Kalau dua baris tidak punya satu kata
 *    pun yang sama, menyoroti semua kata sama informatifnya dengan menyoroti
 *    seluruh baris -- cuma jauh lebih berisik. Yang diperiksa sengaja token
 *    bukan-spasi: hampir setiap pasang baris berbagi sebuah spasi, jadi
 *    memeriksa "ada token yang sama" saja akan membuat pagar ini tidak pernah
 *    menyala sama sekali.
 */
function bedaKata(a, b) {
  if (typeof a !== "string" || typeof b !== "string") return null;
  const ta = pecahToken(a);
  const tb = pecahToken(b);
  const n = ta.length;
  const m = tb.length;
  if (!n || !m || n * m > BATAS_SEL_KATA) return null;

  const tabel = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      tabel[i][j] = ta[i] === tb[j]
        ? tabel[i + 1][j + 1] + 1
        : Math.max(tabel[i + 1][j], tabel[i][j + 1]);
    }
  }

  const kiri = [];
  const kanan = [];
  const gabung = [];
  // Token bersebelahan yang bertanda sama dilebur jadi satu segmen. Bukan demi
  // DOM yang ringkas: segmen per token membuat "dua kata berurutan berubah"
  // tampil sebagai dua kotak dengan jeda di antaranya, dan yang terbaca jadi
  // dua ubahan terpisah padahal cuma satu.
  const dorong = (daftar, tanda, teks) => {
    const akhir = daftar[daftar.length - 1];
    if (akhir && akhir.tanda === tanda) akhir.teks += teks;
    else daftar.push({ tanda, teks });
  };
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (ta[i] === tb[j]) {
      dorong(kiri, "=", ta[i]);
      dorong(kanan, "=", tb[j]);
      dorong(gabung, "=", ta[i]);
      i++;
      j++;
    } else if (tabel[i + 1][j] >= tabel[i][j + 1]) {
      dorong(kiri, "-", ta[i]);
      dorong(gabung, "-", ta[i]);
      i++;
    } else {
      dorong(kanan, "+", tb[j]);
      dorong(gabung, "+", tb[j]);
      j++;
    }
  }
  while (i < n) { dorong(kiri, "-", ta[i]); dorong(gabung, "-", ta[i]); i++; }
  while (j < m) { dorong(kanan, "+", tb[j]); dorong(gabung, "+", tb[j]); j++; }

  const jangkar = kiri.filter((s) => s.tanda === "=").map((s) => s.teks).join("");
  if (jangkar.trim() === "") return null;

  return { kiri, kanan, gabung };
}

/** Segmen `bedaKata` -> anak-anak `.diff-isi`.
 *
 *  Yang TIDAK berubah keluar sebagai string, bukan span. Dua sebabnya: ia
 *  tidak butuh gaya apa pun, dan dengan begitu cacah anak ELEMEN `.diff-isi`
 *  langsung sama dengan cacah ubahan -- sebuah klaim yang bisa diadu dari
 *  luar, bukan cuma dilihat.
 *
 *  Ubahan ditandai BENTUK, bukan warna: coretan untuk yang hilang, garis bawah
 *  untuk yang bertambah. Warna di baris ini sudah dipakai habis oleh
 *  `.diff-kurang`/`.diff-tambah` untuk membedakan SISI, jadi memakai warna
 *  lagi untuk membedakan SEGMEN berarti satu kanal memikul dua arti -- dan
 *  bagi orang yang tidak membedakan merah-hijau, nol di antaranya terbaca.
 *  Tint latarnya `currentColor`, jadi ia mewarisi token baris itu sendiri dan
 *  tetap benar di keempat tema tanpa satu nilai warna pun dituliskan di sini.
 *
 *  Gayanya INLINE karena `gaya.css` beku di hun ini; itu sekaligus yang
 *  membuat coretannya tidak bisa ditimpa -- nol aturan `text-decoration` di
 *  lembar gaya menyentuh `.diff-kata`, dan nol di antaranya `!important`. */
function segmenKata(bagian) {
  return bagian.map((s) => (s.tanda === "="
    ? s.teks
    : h("span.diff-kata", {
        gaya: {
          background: "color-mix(in srgb, currentColor 16%, transparent)",
          borderRadius: "2px",
          textDecoration: s.tanda === "-" ? "line-through" : "underline",
          textUnderlineOffset: "2px",
        },
      }, s.teks)));
}

/** Pasangkan `-` dengan `+` yang menggantikannya di keluaran `bedaBaris`.
 *
 *  `bedaBaris` memancarkan baris yang berubah sebagai DUA butir lepas,
 *  sementara `Beda.baris` di Python memancarkannya sebagai satu `~` berisi
 *  kedua sisi. Perbedaan bentuk itu sengaja TIDAK diseragamkan di dalam
 *  `bedaKata`: begitu perjodohannya ikut masuk ke sana, fungsi itu berhenti
 *  bisa diuji sebagai fungsi atas dua string. Jadi ia tinggal di sini, dan
 *  cuma di jalur diff KODE.
 *
 *  Aturannya: dalam satu deret `-` yang langsung disusul deret `+`, butir
 *  ke-n dipasangkan dengan butir ke-n. Sisanya -- deret yang lebih panjang di
 *  satu sisi, atau `-` tanpa `+` sesudahnya -- dibiarkan utuh tanpa segmen,
 *  karena baris yang tidak punya lawan memang tidak punya "kata yang berubah";
 *  ia seluruhnya hilang atau seluruhnya baru. MURNI: masuk daftar, keluar
 *  daftar BARU; butir aslinya tidak disentuh. */
function pasangkanUbahan(baris) {
  const keluar = baris.map((d) => ({ ...d }));
  let i = 0;
  while (i < keluar.length) {
    if (keluar[i].tanda !== "-") { i++; continue; }
    let k = i;
    while (k < keluar.length && keluar[k].tanda === "-") k++;
    let t = k;
    while (t < keluar.length && keluar[t].tanda === "+") t++;
    const pasang = Math.min(k - i, t - k);
    for (let p = 0; p < pasang; p++) {
      const kata = bedaKata(keluar[i + p].teks, keluar[k + p].teks);
      if (!kata) continue;
      keluar[i + p].segmen = kata.kiri;
      keluar[k + p].segmen = kata.kanan;
    }
    i = t > k ? t : k;
  }
  return keluar;
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
              ? `Contoh dari materi: ${judulContoh}. Ubah sesukamu; yang di `
                + "materi tidak ikut berubah."
              : "Tempat mencoba apa pun. Tidak dinilai dan tidak menyentuh "
                + "progres, dan justru karena itu ia berguna."))),
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
