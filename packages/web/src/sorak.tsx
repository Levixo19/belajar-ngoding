/* Toast dan salin-ke-papan-klip. Port `sorak()` dan `salin()` dari `inti.js`.
 *
 * API-nya sengaja tetap GLOBAL (`sorak("pesan")`), bukan context React. Di
 * versi JS ia dipanggil dari mana saja -- termasuk dari dalam penangan `catch`
 * yang tidak punya akses ke komponen mana pun -- dan membuatnya butuh provider
 * berarti setiap pemanggil harus jadi komponen lebih dulu. Yang dipakai di
 * sini toko kecil berlangganan: `sorak()` menambah pesan, `<Sorak />` yang
 * menggambarnya.
 *
 * SATU hal yang sengaja TIDAK diport: FLIP. Versi JS menggeser toast yang
 * sudah ada dengan `tata()` dari `gerak.js` supaya dua pemberitahuan yang
 * datang beruntun tidak melompat. Itu butuh mesin animasi utuh (962 baris),
 * dan di sini pengganti sementaranya animasi masuk biasa. Akibatnya jujur:
 * toast kedua yang datang cepat akan MELOMPAT alih-alih bergeser halus. Itu
 * perbedaan yang terlihat, jadi ia dicatat di sini dan bukan dibiarkan jadi
 * kejutan -- begitu `gerak.js` diport, FLIP-nya dipasang kembali.
 */

import { useEffect, useRef, useState } from "react";

import { tingkatGerak } from "./gerak.ts";

export type JenisSorak = "" | "tumbuh" | "salah";

interface Pesan {
  id: number;
  teks: string;
  jenis: JenisSorak;
}

let urut = 0;
let daftar: Pesan[] = [];
const pelanggan = new Set<(d: Pesan[]) => void>();

function siarkan() {
  for (const f of pelanggan) f(daftar);
}

/** Tampilkan pemberitahuan singkat. Bisa dipanggil dari mana saja. */
export function sorak(teks: string, jenis: JenisSorak = "", detik = 3.4): void {
  const pesan: Pesan = { id: (urut += 1), teks, jenis };
  daftar = [...daftar, pesan];
  siarkan();
  setTimeout(() => {
    daftar = daftar.filter((p) => p.id !== pesan.id);
    siarkan();
  }, detik * 1000);
}

/** Wadah toast. Dipasang sekali di akar aplikasi. */
export function Sorak() {
  const [isi, setIsi] = useState<Pesan[]>(daftar);
  useEffect(() => {
    pelanggan.add(setIsi);
    return () => {
      pelanggan.delete(setIsi);
    };
  }, []);
  return (
    <div id="sorak" aria-live="polite" role="status">
      {isi.map((p) => (
        <KotakSorak key={p.id} pesan={p} />
      ))}
    </div>
  );
}

function KotakSorak({ pesan }: { pesan: Pesan }) {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el || tingkatGerak() === "mati") return;
    // Berangkat dari tergeser dan sedikit mengecil, BUKAN `fill: "forwards"`
    // menuju keadaan yang benar: keadaan akhirnya memang keadaan alami
    // elemennya, jadi gerak yang dimatikan tetap menyisakan toast yang utuh.
    el.animate(
      {
        transform: ["translateY(18px) scale(.94)", "none"],
        opacity: [0, 1],
      },
      { duration: 360, easing: "cubic-bezier(.32,.72,.36,1)" },
    );
  }, []);
  return (
    <div
      ref={ref}
      className={"sorak" + (pesan.jenis ? " sorak-" + pesan.jenis : "")}
    >
      {pesan.teks}
    </div>
  );
}

/**
 * Salin teks ke papan klip, lalu beri tahu.
 *
 * `navigator.clipboard` cuma ada di konteks aman. Aplikasi ini dilayani dari
 * `127.0.0.1`, yang DIHITUNG aman oleh browser -- tapi jalur cadangannya tetap
 * dipertahankan: tombol Salin yang diam saja tanpa pesan apa pun adalah tombol
 * yang membuat orang mengira aplikasinya rusak.
 */
export async function salin(teks: string, pesan = "Kode disalin."): Promise<void> {
  try {
    if (navigator.clipboard && globalThis.isSecureContext) {
      await navigator.clipboard.writeText(teks);
      sorak(pesan, "tumbuh", 1.8);
      return;
    }
    throw new Error("papan klip tidak tersedia");
  } catch {
    // Cadangan: `<textarea>` sementara plus `execCommand`. Sudah usang, tapi
    // ia satu-satunya yang bekerja tanpa konteks aman.
    try {
      const ta = document.createElement("textarea");
      ta.value = teks;
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      document.execCommand("copy");
      ta.remove();
      sorak(pesan, "tumbuh", 1.8);
    } catch {
      sorak("Gagal menyalin. Pilih teksnya lalu tekan Ctrl+C.", "salah");
    }
  }
}

let pengumum: HTMLDivElement | null = null;

/**
 * Bacakan sebuah kalimat ke pembaca layar tanpa menampilkan apa pun.
 *
 * Bedanya dengan `sorak()`: toast MUNCUL di layar, jadi ia salah dipakai untuk
 * hal yang cuma perlu didengar. Hasil kuis dan hasil Periksa latihan dulu cuma
 * ditandai warna dan kelas; fokus pindah ke tombol berikutnya dan pembaca layar
 * hanya mendengar nama tombol itu (WCAG 4.1.3).
 *
 * Simpulnya dibuat di luar React dan dipakai ulang. Itu disengaja: ia hidup
 * lebih lama daripada layar mana pun yang memanggilnya, dan sebuah live region
 * yang ikut dilepas saat layar berganti tidak pernah sempat dibacakan. Isinya
 * DIKOSONGKAN dulu lalu diisi 60 ms kemudian -- pembaca layar mengabaikan teks
 * yang sama dengan yang sudah ada di situ.
 */
export function umumkan(teks: string): void {
  if (!pengumum) {
    pengumum = document.createElement("div");
    pengumum.className = "pengumum";
    pengumum.setAttribute("aria-live", "polite");
    pengumum.setAttribute("role", "status");
    document.body.appendChild(pengumum);
  }
  const el = pengumum;
  el.textContent = "";
  setTimeout(() => { el.textContent = teks; }, 60);
}
