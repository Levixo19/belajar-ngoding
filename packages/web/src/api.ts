/* Klien API: satu-satunya tempat yang tahu soal token dan bentuk galat.
 *
 * Padanan `webapp/statik/js/inti.js` bagian `ambil()`/`kirim()`. Yang berubah
 * cuma tipenya; aturannya sama, termasuk satu yang mudah dilanggar: setiap
 * `/api/*` menuntut header `X-Belajar-Token`, dan tokennya ditanam ke halaman
 * oleh server (produksi) atau oleh plugin Vite (dev).
 *
 * Yang DITAMBAHKAN di sini, karena sisi dev punya kegagalan yang tidak ada di
 * produksi: kalau placeholder tokennya tidak pernah diganti, berarti server
 * Python tidak hidup. Membiarkannya jadi 403 berarti pelajar -- dan saya
 * sendiri nanti -- membaca "Token tidak sah. Muat ulang halaman.", saran yang
 * tidak akan pernah menolong karena memuat ulang Vite tidak menyalakan server
 * Python. Jadi keadaan itu dikenali dan dikatakan apa adanya.
 */

/** Token per-jalannya server. Ditanam ke halaman, bukan diletakkan di URL. */
const TOKEN = (() => {
  const nilai = (globalThis as { TOKEN_BELAJAR?: string }).TOKEN_BELAJAR ?? "";
  // Placeholder yang belum tergantikan berarti dev server jalan tanpa server
  // Python di belakangnya. Diperlakukan sebagai "tidak ada token" supaya
  // pesannya lahir di satu tempat, di bawah.
  return nilai === "__TOKEN_BELAJAR__" ? "" : nilai;
})();

const PESAN_TANPA_SERVER =
  "Server Python tidak hidup, jadi tidak ada token untuk memanggil API. " +
  "Nyalakan `python3 belajar-web.py --tanpa-browser --port 7788` dengan " +
  "profil terpisah, lalu muat ulang halaman ini.";

/** Galat API yang membawa kode HTTP-nya, supaya layar bisa membedakannya. */
export class GalatApi extends Error {
  readonly kode: number;
  constructor(pesan: string, kode: number) {
    super(pesan);
    this.name = "GalatApi";
    this.kode = kode;
  }
}

async function urai(tanggapan: Response): Promise<unknown> {
  const teks = await tanggapan.text();
  let muatan: unknown = null;
  try {
    muatan = teks ? JSON.parse(teks) : null;
  } catch {
    // Server ini selalu menjawab JSON untuk `/api/*`. Badan yang bukan JSON
    // berarti sesuatu di depannya yang menjawab -- proksi, atau halaman galat.
    // Menyebutnya "JSON tidak sah" lebih jujur daripada melaporkan `null`.
    throw new GalatApi(
      `Jawaban dari server bukan JSON (${tanggapan.status}).`,
      tanggapan.status,
    );
  }
  if (!tanggapan.ok) {
    const pesan =
      (muatan as { galat?: string } | null)?.galat ??
      `Permintaan gagal (${tanggapan.status}).`;
    throw new GalatApi(pesan, tanggapan.status);
  }
  return muatan;
}

/** GET `/api/<jalur>` dengan parameter kueri. */
export async function ambil<T>(
  jalur: string,
  kueri: Record<string, string | number | undefined> = {},
): Promise<T> {
  if (!TOKEN) throw new GalatApi(PESAN_TANPA_SERVER, 0);
  const alamat = new URL(`/api/${jalur}`, globalThis.location.origin);
  for (const [k, v] of Object.entries(kueri)) {
    if (v !== undefined) alamat.searchParams.set(k, String(v));
  }
  const tanggapan = await fetch(alamat, {
    headers: { "X-Belajar-Token": TOKEN },
  });
  return (await urai(tanggapan)) as T;
}

/** POST `/api/<jalur>` dengan muatan JSON. */
export async function kirim<T>(jalur: string, muatan: unknown = {}): Promise<T> {
  if (!TOKEN) throw new GalatApi(PESAN_TANPA_SERVER, 0);
  const tanggapan = await fetch(`/api/${jalur}`, {
    method: "POST",
    headers: {
      "X-Belajar-Token": TOKEN,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(muatan),
  });
  return (await urai(tanggapan)) as T;
}
