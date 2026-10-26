/** Pengelolaan data belajar: laporan, ekspor, impor, cadangan, dan reset.
 *
 *  Padanan `blokData()` dan `blokBahaya()` di `layar-lain.js`. Keduanya dipakai
 *  DUA layar di antarmuka lama -- `blokData` di Statistik dan di Pengaturan,
 *  `blokBahaya` hanya di Pengaturan -- jadi keduanya tinggal di sini, bukan
 *  disalin ke dua berkas.
 *
 *  Yang mengikat, dan alasannya bukan selera:
 *
 *  * **Reset SEMUA menuntut dua dialog**, dan yang kedua menuntut kata `HAPUS`
 *    diketik. Ketikan yang tidak cocok menggetarkan medannya lalu menghapus
 *    NOL. Ia menghapus XP, level, streak, badge, dan seluruh riwayat di semua
 *    bahasa; tombol semacam itu tidak boleh pernah bisa ditekan karena salah
 *    sasaran.
 *  * **Reset tidak menyentuh catatan pribadi.** Catatan tinggal di berkasnya
 *    sendiri justru karena reset ada dan dipakai. Kalimat itu ikut digambar,
 *    karena yang menenangkan orang bukan faktanya melainkan tahunya.
 *  * **Halaman dimuat ulang sesudah impor dan reset.** Progres yang dibaca
 *    seluruh layar lain sudah berubah di server, dan menyisakan layar yang
 *    menampilkan angka lama lebih buruk daripada satu kedipan muat ulang.
 */

// `useState` saja: medan di dalam dialog dipegang objek `{current}` biasa
// yang dibuat ULANG tiap kali dialognya dibuka, bukan `useRef` yang
// hidup selama komponennya hidup -- dua pembukaan berurutan tidak boleh
// saling melihat medan satu sama lain.
import { useState } from "react";
import * as api from "../api.ts";
import { adaGerak } from "../gerak.ts";
import { salin, sorak } from "../sorak.tsx";
import { hariIniISO } from "../waktu.ts";
import { useJendela } from "./Jendela.tsx";

interface BahasaRingkas { key: string; label: string }

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

export function BlokData() {
  const { tanya } = useJendela();
  const [sibuk, setSibuk] = useState("");

  async function lihatLaporan() {
    setSibuk("laporan");
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
    } finally {
      setSibuk("");
    }
  }

  async function ekspor() {
    setSibuk("ekspor");
    try {
      const r = await api.ambil<{ progres: unknown }>("data/ekspor");
      const nama = "progres-belajar-" + hariIniISO() + ".json";
      unduh(JSON.stringify(r.progres, null, 2), nama, "application/json");
      sorak("Progres diekspor ke " + nama, "tumbuh");
    } finally {
      setSibuk("");
    }
  }

  async function impor() {
    const medan = { current: null as HTMLInputElement | null };
    const pilih = await tanya({
      judul: "Impor progres",
      isi: (
        <div>
          <p>
            Progres yang sekarang akan DIGANTI. Salinannya dicadangkan otomatis
            lebih dulu, di sebelah berkas aslinya.
          </p>
          <input
            type="file"
            accept=".json,application/json"
            aria-label="Berkas progres untuk diimpor"
            ref={(el) => { medan.current = el; }}
          />
        </div>
      ),
      aksi: [
        { label: "Batal", nilai: false },
        { label: "Impor", nilai: true, kelas: "tbl-bahaya" },
      ],
    });
    const berkas = medan.current?.files?.[0];
    if (pilih !== true || !berkas) return;
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

  async function cadangkan() {
    setSibuk("cadangan");
    try {
      const r = await api.kirim<{ cadangan: string }>("data/cadangkan", {});
      sorak(r.cadangan ? "Cadangan dibuat: " + r.cadangan
                       : "Belum ada progres untuk dicadangkan.",
            r.cadangan ? "tumbuh" : "");
    } finally {
      setSibuk("");
    }
  }

  return (
    <section>
      <span className="mata">Data belajarmu</span>
      <div className="kartu deret">
        <button className="tbl tbl-hantu" onClick={lihatLaporan}
                disabled={sibuk === "laporan"}>
          Laporan kemajuan (Markdown)
        </button>
        <button className="tbl tbl-hantu" onClick={ekspor}
                disabled={sibuk === "ekspor"}>
          Ekspor progres
        </button>
        <button className="tbl tbl-hantu" onClick={impor}>Impor progres</button>
        <button className="tbl tbl-hantu" onClick={cadangkan}
                disabled={sibuk === "cadangan"}>
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
      `Hapus SELURUH progres ${nama}? Materi, kuis, dan latihannya kembali `
      + "ke nol. Ini tidak bisa dibatalkan.",
      { judul: "Reset " + nama, labelYa: "Hapus progres " + nama,
        bahaya: true });
    if (!ya) return;
    const r = await api.kirim<{ cadangan: string }>(
      "data/reset", { bagian: kunci, konfirmasi: "HAPUS" });
    sorak(`Progres ${nama} dihapus. Cadangan: ${r.cadangan || "-"}`,
          "tumbuh", 6);
    setTimeout(() => location.reload(), 900);
  }

  async function resetSemua() {
    const ya = await konfirmasi(
      "Ini menghapus XP, level, streak, badge, dan seluruh riwayat di SEMUA "
      + "bahasa sekaligus.",
      { judul: "Reset seluruh progres", labelYa: "Lanjut", bahaya: true });
    if (!ya) return;

    // Dialog KEDUA, dan ia menuntut kata kuncinya diketik. Satu klik "Ya" yang
    // salah sasaran tidak boleh cukup untuk menghapus catatan belajar
    // sungguhan.
    const medan = { current: null as HTMLInputElement | null };
    const lagi = await tanya({
      judul: "Konfirmasi terakhir",
      isi: (
        <div>
          <p>
            Ketik HAPUS di bawah untuk mengonfirmasi. Cadangan dibuat lebih
            dulu, tapi jangan mengandalkan itu.
          </p>
          <input
            type="text"
            placeholder="HAPUS"
            aria-label="Ketik HAPUS untuk mengonfirmasi"
            ref={(el) => { medan.current = el; }}
          />
        </div>
      ),
      aksi: [
        { label: "Batal", nilai: false },
        { label: "Hapus semuanya", nilai: true, kelas: "tbl-bahaya" },
      ],
    });
    if (lagi !== true) return;
    if ((medan.current?.value ?? "").trim() !== "HAPUS") {
      getar(medan.current);
      sorak("Kata konfirmasi tidak cocok. Tidak ada yang dihapus.", "salah");
      return;
    }
    const r = await api.kirim<{ cadangan: string }>(
      "data/reset", { bagian: "semua", konfirmasi: "HAPUS" });
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
          Cadangan otomatis dibuat sebelum menghapus, di sebelah berkas
          progresnya. Catatan pribadimu tidak ikut terhapus; ia tinggal di
          berkas yang lain.
        </p>
        <div className="deret">
          <select
            aria-label="Bahasa yang direset"
            style={{ width: "auto" }}
            value={kunci}
            onChange={(e) => setKunci(e.target.value)}
          >
            {bahasa.map((b) => (
              <option key={b.key} value={b.key}>{b.label}</option>
            ))}
          </select>
          <button className="tbl tbl-bahaya" onClick={resetSatu}>
            Reset satu bahasa
          </button>
          <span className="deret-kanan" />
          <button className="tbl tbl-bahaya" onClick={resetSemua}>
            Reset SEMUA progres
          </button>
        </div>
      </div>
    </section>
  );
}
