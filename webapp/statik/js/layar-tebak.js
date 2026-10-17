/* Tebak keluarannya: latihan membaca kode dari contoh materi yang sudah dibaca.
 *
 * Pemilihan kartunya (yang terakhir salah ditebak dulu, lalu yang belum pernah
 * dicoba) dan kuncinya (keluaran NYATA dari menjalankan contohnya) dua-duanya
 * milik server: pelajar/tebak.py lewat /api/tebak/kartu dan /api/tebak. Layar
 * ini cuma menampilkan dan mengirim tebakan. Bukan latihan: tidak ada definisi
 * "lulus" di sini, dan tidak menyentuh latihan_lulus. */

import { api, h, isikan, rayakan, keadaan } from "./inti.js";
import { ikon } from "./ikon.js";
import { praKode } from "./sorot.js";
import { kepalaBersampul } from "./sampul.js";
import { masuk } from "./gerak.js";

const tanpaNomor = (t) => String(t).replace(/^\s*\d+\.\s*/, "");

export async function layarTebak({ key }, ctx) {
  const d = await api.ambil("/api/tebak/kartu", { key });
  const bhs = (ctx.awal.bahasa || []).find((b) => b.key === key) || { label: key };
  const kepala = kepalaBersampul(`${key}/tebak`, { bahasa: key, pita: true, ragam: "kisi" },
    h("span.mata", {}, `Latih baca kode · ${bhs.label}`),
    h("h1", {}, "Tebak keluarannya"),
    h("p.kepala-sub", {}, "Baca contohnya, tulis apa yang menurutmu tercetak, lalu "
      + "periksa. Kuncinya keluaran asli dari menjalankan kode itu."));
  const konteks = { balik: { label: bhs.label, href: "#/bahasa/" + key }, bab: "Latih baca kode",
                    judul: "Tebak keluarannya" };

  if (!d.kartu.length) {
    const alasan = !d.siap
      ? `${bhs.label} belum terpasang di komputermu, jadi contohnya belum bisa dijalankan.`
      : d.layak
        ? "Belum ada contoh dari materi yang sudah kamu baca. Baca satu-dua materi dulu, "
          + "contohnya akan muncul di sini."
        : `Kurikulum ${bhs.label} tidak punya contoh program yang bisa ditebak keluarannya.`;
    return { el: h("div", {}, kepala, keadaan("kosong", "Belum ada yang bisa ditebak", alasan,
      h("a.tbl", { href: "#/bahasa/" + key }, "Ke halaman " + bhs.label))), judul: "Tebak keluarannya",
      konteks };
  }

  const isi = h("div.tebak-isi");
  const el = h("div", {}, kepala, isi);
  let nomor = 0, benar = 0;

  function gambar() {
    if (nomor >= d.kartu.length) return gambarRekap();
    const k = d.kartu[nomor];
    const area = h("textarea.tebak-tebakan", { rows: 5, spellcheck: false,
      "aria-label": "Tebakan keluaranmu", placeholder: "Tulis keluarannya di sini, baris demi baris." });
    const hasil = h("div.tebak-hasil", { role: "status" });
    const tblPeriksa = h("button.tbl.tbl-utama", { type: "button" }, "Periksa tebakan");
    const kartu = h("section.kartu.tebak-kartu", {},
      h("div.tebak-kepala", {},
        h("span.mata", {}, `Kartu ${nomor + 1} dari ${d.kartu.length}`),
        h("a", { href: `#/materi/${key}/${k.indeks}` }, "dari materi " + tanpaNomor(k.judul))),
      h("div.blok-sarung", {}, praKode(k.token)),
      h("label.tebak-label", {}, "Menurutmu, apa yang tercetak?"), area,
      h("div.deret", {}, tblPeriksa), hasil);
    tblPeriksa.addEventListener("click", async () => {
      tblPeriksa.disabled = true;
      isikan(hasil, h("div.deret", {}, h("div.pusaran"), h("span", {}, "Menjalankan contohnya…")));
      try {
        const r = await api.kirim("/api/tebak", { key, indeks: k.indeks, kode: k.kode, tebakan: area.value });
        if (r.benar) benar += 1;
        rayakan(r, { diam: !r.benar });
        const lanjut = h("button.tbl" + (r.benar ? ".tbl-utama" : ""), { type: "button" },
          nomor + 1 < d.kartu.length ? "Kartu berikutnya" : "Lihat hasil", ikon("lanjut", { ukuran: 16 }));
        lanjut.addEventListener("click", () => { nomor += 1; gambar(); });
        isikan(hasil,
          h("p.tebak-vonis", { kelas: r.benar ? "tebak-benar" : "tebak-belum" },
            r.benar ? "Tepat. Kamu membaca kodenya dengan benar." : "Belum tepat. Bandingkan dengan keluaran aslinya:"),
          r.benar ? null : barisBeda(r.beda),
          h("div.tebak-asli", {}, h("span.mata", {}, "Keluaran asli"), h("pre.terminal", {}, r.keluaran)),
          h("div.deret", {}, lanjut));
        area.readOnly = true;
        lanjut.focus();
      } catch (e) {
        tblPeriksa.disabled = false;
        isikan(hasil, h("p.tebak-vonis.tebak-belum", {}, e.message));
      }
    });
    isikan(isi, kartu);
    masuk(kartu, { geser: 8, pegas: "jawab" });
    area.focus();
  }

  function gambarRekap() {
    const kartu = h("section.kartu.tebak-kartu", {},
      h("span.mata", {}, "Selesai"),
      h("h2", {}, `${benar} dari ${d.kartu.length} tebakan tepat`),
      h("p", {}, benar === d.kartu.length
        ? "Semua tepat. Contoh yang sudah kamu kuasai akan muncul lebih jarang."
        : "Contoh yang tadi meleset akan muncul lebih dulu di sesi berikutnya."),
      h("div.deret", {},
        h("a.tbl.tbl-utama", { href: `#/tebak/${key}?ulang=${Date.now()}` }, "Sesi lagi"),
        h("a.tbl", { href: "#/bahasa/" + key }, "Kembali ke " + bhs.label)));
    isikan(isi, kartu);
    masuk(kartu, { geser: 8, pegas: "jawab" });
  }

  gambar();
  return { el, judul: "Tebak keluarannya", konteks };
}

/** Perbandingan baris demi baris, dari beda.bandingkan di server. */
function barisBeda(b) {
  if (!b || !b.baris) return null;
  return h("div.tebak-beda", {},
    b.ringkas ? h("p", {}, b.ringkas) : null,
    h("table.tebak-tabel", {},
      h("thead", {}, h("tr", {}, h("th", {}, "Asli"), h("th", {}, "Tebakanmu"))),
      h("tbody", {}, b.baris.map((r) => h("tr", { kelas: r.tanda === "=" ? "" : "tebak-beda-baris" },
        h("td", {}, h("code", {}, r.harapan ?? "")),
        h("td", {}, h("code", {}, r.aktual ?? "")))))));
}
