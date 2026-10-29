/** Pengelolaan data belajar: laporan, ekspor, impor, cadangan, pulihkan dari
 *  salinan, dan reset.
 *
 *  Padanan `blokData()` dan `blokBahaya()` di `layar-lain.js`. Keduanya dipakai
 *  DUA layar di antarmuka lama -- `blokData` di Statistik dan di Pengaturan,
 *  `blokBahaya` hanya di Pengaturan -- jadi keduanya tinggal di sini, bukan
 *  disalin ke dua berkas.
 *
 *  Yang mengikat, dan alasannya bukan selera:
 *
 *  * **Reset SEMUA menuntut dua dialog**, dan yang kedua menuntut kata `HAPUS`
 *    diketik. Ketikan yang tidak cocok menggetarkan tombol pemicunya (kotaknya
 *    sudah tertutup) lalu menghapus NOL. Ia menghapus XP, level, streak, badge, dan seluruh riwayat di semua
 *    bahasa; tombol semacam itu tidak boleh pernah bisa ditekan karena salah
 *    sasaran.
 *  * **Reset tidak menyentuh catatan pribadi.** Catatan tinggal di berkasnya
 *    sendiri justru karena reset ada dan dipakai. Kalimat itu ikut digambar,
 *    karena yang menenangkan orang bukan faktanya melainkan tahunya.
 *  * **Halaman dimuat ulang sesudah impor dan reset.** Progres yang dibaca
 *    seluruh layar lain sudah berubah di server, dan menyisakan layar yang
 *    menampilkan angka lama lebih buruk daripada satu kedipan muat ulang.
 */

// `useState` saja: isian di dalam dialog dicatat lewat `onChange` ke objek
// biasa yang dibuat ULANG tiap kali dialognya dibuka, bukan `useRef` yang
// hidup selama komponennya hidup -- dua pembukaan berurutan tidak boleh
// saling melihat isian satu sama lain.
//
// JANGAN membaca elemen isian lewat `ref` SESUDAH `await tanya(...)`: React
// memanggil callback `ref` dengan null begitu dialognya tertutup dan elemennya
// dilepas, jadi nilainya selalu hilang. Reset SEMUA dan Impor progres dulu
// rusak persis begitu: "HAPUS" yang benar terbaca kosong, berkas yang dipilih
// terbaca tidak ada. Pagarnya `TestIsiDialogTidakMemakaiRef`.
import { useRef, useState } from "react";

import { Pilihan } from "./Pilihan.tsx";
import * as api from "../api.ts";
import { adaGerak } from "../gerak.ts";
import { salin, sorak } from "../sorak.tsx";
import { hariIniISO, tanggalLokal, tanggalRamah } from "../waktu.ts";
import { useJendela } from "./Jendela.tsx";

interface BahasaRingkas { key: string; label: string }

/** Satu salinan progres bertanggal, bentuk `GET /api/data/cadangan`. */
interface Salinan {
  nama: string; waktu: string; xp: number; materi: number; sah: boolean;
}

/** "27 Okt 2026, 17.02 · 30 XP · 3 materi dibaca". */
function labelSalinan(s: Salinan): string {
  const t = tanggalLokal(s.waktu);
  const kapan = t
    ? `${tanggalRamah(s.waktu)}, `
      + t.toLocaleTimeString("id-ID", { hour: "2-digit", minute: "2-digit" })
    : s.nama;
  return `${kapan} · ${s.xp} XP · ${s.materi} materi dibaca`;
}

/** Pilihan salinan di dialog Pulihkan. Dialognya dibangun sebagai JSX statis
 *  untuk `tanya()`, jadi keadaan pilihannya tinggal di komponen ini dan hasilnya
 *  dicatat ke objek `dipilih` yang dibaca pemanggil sesudah dialog ditutup. */
function PilihSalinan({ salinan, dipilih }: { salinan: Salinan[]; dipilih: { nama: string } }) {
  const [nama, setNama] = useState(dipilih.nama);
  return (
    <Pilihan
      label="Salinan progres yang dipulihkan"
      namaTombol="Salinan progres yang dipulihkan"
      nilai={nama}
      opsi={salinan.map((s) => ({ id: s.nama, nama: labelSalinan(s) }))}
      onUbah={(v) => { dipilih.nama = v; setNama(v); }}
    />
  );
}

/** Unduh teks sebagai berkas. URL objeknya dilepas lagi supaya blob-nya tidak
 *  menggantung di memori tab selama tab itu hidup. */
function unduh(isi: string, nama: string, tipe: string): void {
  const url = URL.createObjectURL(new Blob([isi], { type: tipe }));
  const a = document.createElement("a");
  a.href = url;
  a.download = nama;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

/** Getar penolakan. Padanan `getar()` di `gerak.js`; dipagari `adaGerak()`
 *  karena ia gerak yang berangkat sendiri, bukan umpan balik sentuhan. */
function getar(el: HTMLElement | null): void {
  if (!el || !adaGerak()) return;
  el.animate(
    {
      transform: ["none", "translateX(-5px)", "translateX(4px)",
                  "translateX(-2px)", "none"],
    },
    { duration: 260, easing: "ease-out" });
}

/** Pesan untuk pengguna dari apa pun yang dilempar `api.*`. */
function pesanGalat(e: unknown): string {
  return e instanceof Error ? e.message : String(e);
}

export function BlokData() {
  const { tanya } = useJendela();
  // Penjaga klik ganda, BUKAN `disabled`: tombol yang sedang berfokus lalu
  // dinonaktifkan membuat fokus papan ketik jatuh ke <body>, dan selama dialog
  // Laporan terbuka tombolnya tetap mati sehingga `Jendela` tidak bisa
  // mengembalikan fokus kepadanya.
  const sedang = useRef("");

  async function lihatLaporan() {
    if (sedang.current === "laporan") return;
    sedang.current = "laporan";
    try {
      const r = await api.ambil<{ markdown: string }>("laporan");
      const pilih = await tanya({
        judul: "Laporan kemajuan",
        lebar: true,
        isi: (
          <div>
            <p className="kepala-sub" style={{ margin: "0 0 var(--s3)" }}>
              Format Markdown, siap ditempel ke mana pun.
            </p>
            <div className="pra" style={{ maxHeight: "50vh", overflow: "auto" }}>
              {r.markdown}
            </div>
          </div>
        ),
        aksi: [
          { label: "Salin", nilai: "salin" },
          { label: "Unduh .md", nilai: "unduh" },
          { label: "Tutup", nilai: null, kelas: "tbl-utama" },
        ],
      });
      if (pilih === "salin") await salin(r.markdown, "Laporan disalin.");
      if (pilih === "unduh") {
        unduh(r.markdown, "laporan-belajar.md", "text/markdown");
      }
    } catch (e) {
      sorak("Gagal memuat laporan: " + pesanGalat(e), "salah", 6);
    } finally {
      sedang.current = "";
    }
  }

  async function ekspor() {
    if (sedang.current === "ekspor") return;
    sedang.current = "ekspor";
    try {
      const r = await api.ambil<{ progres: unknown }>("data/ekspor");
      const nama = "progres-belajar-" + hariIniISO() + ".json";
      unduh(JSON.stringify(r.progres, null, 2), nama, "application/json");
      sorak("Progres diekspor ke " + nama, "tumbuh");
    } catch (e) {
      sorak("Gagal mengekspor: " + pesanGalat(e), "salah", 6);
    } finally {
      sedang.current = "";
    }
  }

  async function impor() {
    // Berkasnya dicatat SAAT dipilih. Membaca `medan.current` sesudah dialog
    // tertutup mengembalikan null: React memanggil callback `ref` dengan null
    // begitu kotaknya dilepas, jadi berkas yang dipilih selalu hilang.
    const dipilih = { berkas: null as File | null };
    const pilih = await tanya({
      judul: "Impor progres",
      isi: (
        <div>
          <p>
            Progres yang sekarang akan diganti. Salinannya disimpan lebih dulu,
            bertanggal, di sebelah berkas aslinya.
          </p>
          <input
            type="file"
            accept=".json,application/json"
            aria-label="Berkas progres untuk diimpor"
            onChange={(e) => { dipilih.berkas = e.target.files?.[0] ?? null; }}
          />
        </div>
      ),
      aksi: [
        { label: "Batal", nilai: false },
        { label: "Impor", nilai: true, kelas: "tbl-bahaya" },
      ],
    });
    if (pilih !== true) return;
    const berkas = dipilih.berkas;
    if (!berkas) {
      sorak("Pilih berkas progres lebih dulu. Tidak ada yang diimpor.", "salah");
      return;
    }
    try {
      const teks = await berkas.text();
      const r = await api.kirim<{ cadangan: string }>(
        "data/impor", { progres: JSON.parse(teks) });
      sorak("Progres diimpor. Cadangan lama: " + r.cadangan, "tumbuh", 6);
      setTimeout(() => location.reload(), 900);
    } catch (e) {
      sorak("Gagal mengimpor: " + (e as Error).message, "salah", 6);
    }
  }

  async function pulihkan() {
    if (sedang.current === "pulihkan") return;
    sedang.current = "pulihkan";
    try {
      const r = await api.ambil<{ salinan: Salinan[]; maks: number }>(
        "data/cadangan");
      const bisa = r.salinan.filter((s) => s.sah);
      if (bisa.length === 0) {
        sorak("Belum ada salinan progres yang bisa dipulihkan. Salinan dibuat "
              + "otomatis sebelum reset atau impor, dan lewat tombol Buat "
              + "cadangan.", "");
        return;
      }
      // Pilihannya dicatat lewat `onChange` ke objek biasa, bukan dibaca dari
      // `ref` sesudah dialog tertutup (lihat catatan di kepala berkas).
      const takTerbaca = r.salinan.length - bisa.length;
      const dipilih = { nama: bisa[0]!.nama };
      const pilih = await tanya({
        judul: "Pulihkan dari salinan",
        isi: (
          <div>
            <p>
              Progres yang sekarang diganti dengan isi salinan yang kamu pilih.
              Keadaan sekarang disimpan lebih dulu sebagai salinan baru, jadi
              pemulihan ini sendiri bisa dibalik dengan memulihkan salinan itu.
              Yang disimpan paling banyak {r.maks} salinan terbaru.
              {takTerbaca > 0
                ? ` ${takTerbaca} salinan lain tidak bisa dibaca, jadi tidak `
                  + "ditawarkan di sini."
                : ""}
            </p>
            <PilihSalinan salinan={bisa} dipilih={dipilih} />
          </div>
        ),
        aksi: [
          { label: "Batal", nilai: false },
          { label: "Pulihkan", nilai: true, kelas: "tbl-bahaya" },
        ],
      });
      if (pilih !== true) return;
      const hasil = await api.kirim<{ cadangan: string }>(
        "data/impor", { cadangan: dipilih.nama });
      const simpan = /[\\/]/.test(hasil.cadangan)
        ? " Keadaan sebelumnya tersimpan sebagai "
          + hasil.cadangan.split(/[\\/]/).pop() + "."
        : "";
      sorak("Progres dipulihkan." + simpan, "tumbuh", 6);
      setTimeout(() => location.reload(), 900);
    } catch (e) {
      sorak("Gagal memulihkan: " + pesanGalat(e), "salah", 6);
    } finally {
      sedang.current = "";
    }
  }

  async function cadangkan() {
    if (sedang.current === "cadangan") return;
    sedang.current = "cadangan";
    try {
      const r = await api.kirim<{ cadangan: string }>("data/cadangkan", {});
      sorak(r.cadangan ? "Cadangan dibuat: " + r.cadangan
                       : "Belum ada progres untuk dicadangkan.",
            r.cadangan ? "tumbuh" : "");
    } catch (e) {
      sorak("Gagal membuat cadangan: " + pesanGalat(e), "salah", 6);
    } finally {
      sedang.current = "";
    }
  }

  return (
    <section>
      <span className="mata">Data belajarmu</span>
      <div className="kartu deret">
        <button className="tbl tbl-hantu" onClick={lihatLaporan}>
          Laporan kemajuan (Markdown)
        </button>
        <button className="tbl tbl-hantu" onClick={ekspor}>
          Ekspor progres
        </button>
        <button className="tbl tbl-hantu" onClick={impor}>Impor progres</button>
        <button className="tbl tbl-hantu" onClick={pulihkan}>
          Pulihkan dari salinan
        </button>
        <button className="tbl tbl-hantu" onClick={cadangkan}>
          Buat cadangan
        </button>
      </div>
    </section>
  );
}

export function BlokBahaya({ bahasa }: { bahasa: BahasaRingkas[] }) {
  const { tanya, konfirmasi } = useJendela();
  const [kunci, setKunci] = useState(bahasa[0]?.key ?? "");

  const nama = bahasa.find((b) => b.key === kunci)?.label ?? kunci;

  async function resetSatu() {
    const ya = await konfirmasi(
      `Hapus progres ${nama}? Materi, kuis, dan latihan ${nama} kembali ke `
      + "awal, termasuk bookmark, jadwal ulang kuis, dan riwayat skornya. "
      + "XP, level, streak, dan badge-mu tetap ada. Salinan progres "
      + "disimpan lebih dulu di sebelah berkas progresnya, jadi bisa "
      + "dipulihkan lewat tombol Pulihkan dari salinan di Data belajarmu.",
      { judul: "Reset " + nama, labelYa: "Hapus progres " + nama,
        bahaya: true });
    if (!ya) return;
    let r: { cadangan: string };
    try {
      r = await api.kirim<{ cadangan: string }>(
        "data/reset", { bagian: kunci, konfirmasi: "HAPUS" });
    } catch (e) {
      sorak(`Gagal menghapus progres ${nama}: ${pesanGalat(e)}`, "salah", 8);
      return;
    }
    sorak(`Progres ${nama} dihapus. Cadangan: ${r.cadangan || "-"}`,
          "tumbuh", 6);
    setTimeout(() => location.reload(), 900);
  }

  async function resetSemua(pemicu: HTMLElement) {
    const ya = await konfirmasi(
      "Ini menghapus XP, level, streak, badge, dan seluruh riwayat di semua "
      + "bahasa sekaligus. Salinan progres disimpan lebih dulu di sebelah "
      + "berkas progresnya dan bisa dipulihkan lewat tombol Pulihkan dari "
      + "salinan di Data belajarmu. Catatan pribadimu tidak ikut terhapus.",
      { judul: "Reset seluruh progres", labelYa: "Lanjut", bahaya: true });
    if (!ya) return;

    // Dialog KEDUA, dan ia menuntut kata kuncinya diketik. Satu klik "Ya" yang
    // salah sasaran tidak boleh cukup untuk menghapus catatan belajar
    // sungguhan. Yang diketik dicatat SAAT diketik: sesudah dialog tertutup
    // elemennya sudah dilepas dan `ref`-nya bernilai null, jadi membacanya
    // belakangan membuat "HAPUS" yang benar pun selalu dianggap salah.
    const diketik = { nilai: "" };
    const lagi = await tanya({
      judul: "Konfirmasi terakhir",
      isi: (
        <div>
          <p>
            Ketik HAPUS di bawah untuk mengonfirmasi. Salinan progres disimpan
            lebih dulu, jadi tindakan ini masih bisa dipulihkan lewat tombol
            Pulihkan dari salinan di Data belajarmu.
          </p>
          <input
            type="text"
            placeholder="HAPUS"
            aria-label="Ketik HAPUS untuk mengonfirmasi"
            onChange={(e) => { diketik.nilai = e.target.value; }}
          />
        </div>
      ),
      aksi: [
        { label: "Batal", nilai: false },
        { label: "Hapus semuanya", nilai: true, kelas: "tbl-bahaya" },
      ],
    });
    if (lagi !== true) return;
    if (diketik.nilai.trim() !== "HAPUS") {
      getar(pemicu);
      sorak("Kata konfirmasi tidak cocok. Tidak ada yang dihapus.", "salah");
      return;
    }
    let r: { cadangan: string };
    try {
      r = await api.kirim<{ cadangan: string }>(
        "data/reset", { bagian: "semua", konfirmasi: "HAPUS" });
    } catch (e) {
      sorak("Gagal menghapus progres: " + pesanGalat(e), "salah", 8);
      return;
    }
    sorak("Semua progres dihapus. Cadangan: " + (r.cadangan || "-"),
          "tumbuh", 6);
    setTimeout(() => location.reload(), 1200);
  }

  return (
    <section>
      <span className="mata">Menghapus progres</span>
      <div
        className="kartu"
        style={{
          borderColor: "color-mix(in srgb, var(--salah) 32%, transparent)",
        }}
      >
        <p style={{ color: "var(--teks-2)", fontSize: "var(--t-ui)" }}>
          Sebelum menghapus, salinan progres bertanggal disimpan di sebelah
          berkas progresnya (10 terbaru dipertahankan) dan bisa dipilih lagi di
          Pulihkan dari salinan. Catatan pribadimu tidak ikut terhapus; ia
          tinggal di berkas yang lain.
        </p>
        <div className="deret">
          <Pilihan
            label="Bahasa yang direset"
            namaTombol="Bahasa yang direset"
            gaya={{ width: "auto", minWidth: "14rem" }}
            nilai={kunci}
            opsi={bahasa.map((b) => ({ id: b.key, nama: b.label }))}
            onUbah={setKunci}
          />
          <button className="tbl tbl-bahaya" onClick={resetSatu}>
            Reset satu bahasa
          </button>
          <span className="deret-kanan" />
          <button className="tbl tbl-bahaya"
                  onClick={(e) => resetSemua(e.currentTarget)}>
            Reset SEMUA progres
          </button>
        </div>
      </div>
    </section>
  );
}
