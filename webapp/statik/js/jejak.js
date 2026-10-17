/* "Lihat jalannya": langkah demi langkah sebuah contoh Python.
 *
 * Datanya dari /api/jejak (inti/jejak.py): tiap langkah membawa baris yang
 * AKAN dijalankan, peristiwanya, isi seluruh tumpukan pemanggilan, dan
 * panjang keluaran sejauh itu. Layar ini cuma memutar ulang rekaman itu;
 * tidak ada eksekusi di browser dan tidak ada yang menyentuh progres.
 *
 * Yang sengaja diperlihatkan, karena di situ pemula paling sering salah
 * bayangan:
 *   * baris yang baru saja jalan (redup) dan yang akan jalan (kuningan);
 *   * variabel yang BERUBAH di langkah ini ditandai;
 *   * dua nama yang memegang objek yang SAMA diberi nomor objek yang sama,
 *     jadi "kok list-ku ikut berubah" terjawab dengan melihat, bukan dengan
 *     dijelaskan. */

import { api, h, isikan, umumkan } from "./inti.js";

const JEDA_PUTAR = 750;

/** Token server ([jenis, teks]) dipecah per baris. */
function tokenPerBaris(token) {
  const baris = [[]];
  for (const [jenis, teks] of token || []) {
    String(teks).split("\n").forEach((p, i) => {
      if (i > 0) baris.push([]);
      if (p) baris[baris.length - 1].push([jenis, p]);
    });
  }
  return baris;
}

function barisKode(pasangan) {
  return pasangan.map(([jenis, teks]) => (jenis === "teks" ? teks : h("span.tk-" + jenis, {}, teks)));
}

function kalimat(l, adaBerikut) {
  const atas = l.tumpukan[l.tumpukan.length - 1] || { nama: "", isi: {} };
  if (l.p === "panggil") {
    const arg = Object.entries(atas.isi).map(([k, v]) => `${k}=${v.r}`).join(", ");
    return `Masuk ke fungsi ${atas.nama}(${arg}).`;
  }
  if (l.p === "kembali") return `${atas.nama} selesai dan mengembalikan ${l.nilai ? l.nilai.r : "None"}.`;
  if (l.p === "galat") return `Galat di baris ${l.baris}: ${l.galat}.`;
  return `Baris ${l.baris} akan dijalankan.` + (adaBerikut ? "" : " Ini langkah terakhir yang tercatat.");
}

/** Tombol "Lihat jalannya" untuk satu blok kode Python di materi.
 *  `ambilKode()` mengembalikan kode terkini (bisa sudah diutak-atik);
 *  token server hanya dipakai kalau kodenya masih yang asli. */
export function tombolJejak(kodeAsli, token, ambilKode) {
  return h("button.tbl.tbl-kecil.tbl-hantu", {
    title: "Putar ulang program ini baris demi baris, lengkap dengan isi variabelnya",
    onclick: (e) => {
      const blok = e.currentTarget.closest(".blok-kode");
      if (!blok) return;
      const lama = blok.querySelector(":scope > .jejak");
      if (lama) { lama.remove(); return; }
      const kode = ambilKode();
      const panel = h("section.jejak", { "aria-label": "Jalannya program" });
      blok.appendChild(panel);
      muat(panel, kode, kode === kodeAsli ? token : null);
    },
  }, "Lihat jalannya");
}

async function muat(panel, kode, token) {
  isikan(panel, h("div.deret", {}, h("div.pusaran"), h("span", {}, "Merekam jalannya program…")));
  let r;
  try {
    r = await api.kirim("/api/jejak", { bahasa: "python", kode });
  } catch (e) {
    if (!panel.isConnected) return;
    isikan(panel, h("p.jejak-galat", {}, e.message));
    return;
  }
  if (!panel.isConnected) return;   // panel ditutup sebelum rekaman tiba
  if (!r.langkah.length) {
    isikan(panel, h("p.jejak-galat", {}, r.galat || "Tidak ada langkah yang tercatat."));
    return;
  }
  gambar(panel, r, token ? tokenPerBaris(token) : kode.split("\n").map((t) => [["teks", t]]));
}

function gambar(panel, r, baris) {
  let kini = 0, timer = null;
  const n = r.langkah.length;
  const daftar = h("ol.jejak-kode", {}, baris.map((p, i) => h("li", { data: { baris: i + 1 } },
    h("span.jejak-nomor", {}, i + 1), h("code", {}, barisKode(p)))));
  const bingkai = h("div.jejak-bingkai");
  const keluaran = h("pre.terminal.jejak-keluaran");
  const ket = h("p.jejak-ket", { "aria-live": "polite" });
  const hitung = h("span.jejak-hitung");
  const geser = h("input.jejak-geser", { type: "range", min: 0, max: n - 1, value: 0, "aria-label": "Pilih langkah" });
  const tbl = (label, judul, fn) => h("button.tbl.tbl-kecil.tbl-hantu", { title: judul, "aria-label": judul, onclick: fn }, label);
  const tblPutar = tbl("Putar", "Putar otomatis", () => (timer ? berhenti() : putar()));

  function berhenti() {
    if (timer) clearInterval(timer);
    timer = null;
    tblPutar.textContent = "Putar";
    ket.setAttribute("aria-live", "polite");
  }
  function putar() {
    if (kini >= n - 1) ke(0);
    tblPutar.textContent = "Jeda";
    // Selama diputar, kalimat tiap langkah tidak dibacakan satu per satu:
    // pembaca layar akan mengantrekannya tanpa henti tiap 750 ms.
    ket.setAttribute("aria-live", "off");
    timer = setInterval(() => {
      // Panel yang sudah dilepas (layar berganti, tombol Tutup) mematikan
      // pengatur waktunya sendiri: tidak ada pendengar yang tertinggal.
      if (!panel.isConnected || kini >= n - 1) { berhenti(); return; }
      ke(kini + 1);
    }, JEDA_PUTAR);
  }

  function ke(nomor) {
    kini = Math.max(0, Math.min(n - 1, nomor));
    const l = r.langkah[kini];
    const lalu = kini > 0 ? r.langkah[kini - 1] : null;
    const akhir = kini === n - 1;
    geser.value = kini;
    hitung.textContent = `Langkah ${kini + 1} dari ${n}`;
    for (const li of daftar.children) {
      const b = Number(li.dataset.baris);
      li.classList.toggle("jejak-kini", b === l.baris);
      li.classList.toggle("jejak-lalu", !!lalu && b === lalu.baris && b !== l.baris);
    }
    isikan(bingkai, l.tumpukan.map((f, i) => {
      const sebelum = lalu && lalu.tumpukan[i] && lalu.tumpukan[i].nama === f.nama ? lalu.tumpukan[i].isi : null;
      const isi = Object.entries(f.isi);
      return h("div.jejak-satu" + (i === l.tumpukan.length - 1 ? ".jejak-atas" : ""), {},
        h("div.jejak-nama", {}, f.nama),
        isi.length
          ? h("table", {}, h("tbody", {}, isi.map(([k, v]) => {
              const berubah = sebelum && (!sebelum[k] || sebelum[k].r !== v.r);
              return h("tr" + (berubah ? ".jejak-berubah" : ""), {},
                h("th", { scope: "row" }, k),
                h("td", {}, h("code", {}, v.r),
                  v.id ? h("span.jejak-objek", { title: "Nama dengan nomor objek yang sama memegang objek yang sama" },
                    "objek " + v.id) : null));
            })))
          : h("p.jejak-kosong", {}, "belum ada variabel"));
    }));
    keluaran.textContent = r.keluaran.slice(0, akhir ? r.keluaran.length : l.keluar) || " ";
    let teks = kalimat(l, !akhir);
    if (akhir && r.terpotong) teks += " Rekaman berhenti di sini karena programnya terlalu panjang.";
    if (akhir && r.galat) teks += ` Program berhenti: ${r.galat}`;
    ket.textContent = teks;
    const li = daftar.children[l.baris - 1];
    if (li) daftar.scrollTop = Math.max(0, li.offsetTop - daftar.clientHeight / 2);
  }

  geser.addEventListener("input", () => { berhenti(); ke(Number(geser.value)); });
  panel.addEventListener("keydown", (e) => {
    if (e.target === geser) return;
    if (e.key === "ArrowRight") { e.preventDefault(); berhenti(); ke(kini + 1); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); berhenti(); ke(kini - 1); }
  });

  isikan(panel,
    h("div.jejak-kepala", {},
      h("b", {}, "Jalannya program"), hitung,
      h("button.tbl.tbl-kecil.tbl-hantu", { onclick: () => { berhenti(); panel.remove(); } }, "Tutup")),
    h("div.jejak-tata", {},
      daftar,
      h("div.jejak-kanan", {},
        h("div.jejak-label", {}, "Variabel"), bingkai,
        h("div.jejak-label", {}, "Keluaran sejauh ini"), keluaran)),
    ket,
    h("div.jejak-alat", {},
      tbl("⏮", "Ke awal", () => { berhenti(); ke(0); }),
      tbl("◀", "Mundur satu langkah", () => { berhenti(); ke(kini - 1); }),
      tblPutar,
      tbl("▶", "Maju satu langkah", () => { berhenti(); ke(kini + 1); }),
      tbl("⏭", "Ke akhir", () => { berhenti(); ke(n - 1); }),
      geser));
  panel.tabIndex = -1;
  ke(0);
  panel.focus({ preventScroll: true });
  umumkan(`Rekaman siap: ${n} langkah. Panah kiri dan kanan untuk berpindah langkah.`);
}
