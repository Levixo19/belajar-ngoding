"""Kurikulum "Bikin Aplikasi".

Jembatan antara "sudah paham sintaks Java" dan "bisa membangun aplikasi web
sendiri". Studi kasusnya B-iFAMS - aplikasi inventori Gudang Fire & Safety
PT Badak NGL - termasuk beberapa bug nyata yang pernah ditemukan di sana,
karena kesalahan sungguhan lebih mengajar daripada contoh yang selalu benar.

Latihan modul ini memakai runner Java biasa: seluruh konsep dilatih dalam
Java murni tanpa framework, supaya yang dipelajari adalah CARA BERPIKIRNYA,
bukan hafalan anotasi.
"""

APLIKASI_MATERIALS = [
    {
        "title": "1. Dari Skrip ke Aplikasi",
        "sections": [
            {
                "body": [
                    "Kamu sudah bisa menulis program Java yang jalan. Lalu kenapa",
                    "membangun aplikasi terasa jauh lebih sulit?",
                    "",
                    "Karena keduanya memang beda jenis.",
                    "",
                    "SKRIP",
                    "  - Dijalankan sekali, selesai, mati.",
                    "  - Satu orang yang memakai: kamu sendiri.",
                    "  - Datanya hilang setelah program berhenti.",
                    "  - Kalau error, kamu yang lihat dan kamu yang benahi.",
                    "",
                    "APLIKASI",
                    "  - Hidup terus, menunggu permintaan datang.",
                    "  - Banyak orang memakai bersamaan, dengan hak berbeda-beda.",
                    "  - Datanya harus selamat walau aplikasi dimatikan.",
                    "  - Kalau error, orang lain yang kena, dan kamu belum tentu tahu.",
                    "",
                    "Empat perbedaan itu melahirkan hampir semua kerumitan yang akan",
                    "kamu temui. Database ada karena data harus selamat. Login ada",
                    "karena penggunanya banyak dan tidak sederajat. Log ada karena",
                    "error terjadi saat kamu tidak menonton.",
                ]
            },
            {
                "heading": "Skrip: hitung stok sekali jalan",
                "code": """public class HitungStok {
    public static void main(String[] args) {
        int stok = 20;
        stok = stok - 5;
        System.out.println("Sisa stok: " + stok);
    }
}"""
            },
            {
                "body": [
                    "Program di atas benar. Tapi coba tanya:",
                    "",
                    "  - Kalau program dimatikan, angka 15 itu ke mana?",
                    "  - Kalau dua petugas mengurangi stok bersamaan, siapa yang menang?",
                    "  - Siapa yang mengurangi? Kapan? Kenapa?",
                    "  - Bagaimana kalau seseorang mengurangi 999 padahal stok cuma 20?",
                    "",
                    "Empat pertanyaan itu yang mengubah skrip 5 baris menjadi aplikasi",
                    "puluhan berkas. Bukan karena Java-nya makin rumit, tapi karena",
                    "kenyataannya memang rumit.",
                    "",
                    "Tiga di antaranya dijawab relatif awal: database menjawab yang",
                    "pertama, log dan pencatatan pelaku menjawab yang ketiga, aturan bisnis",
                    "di service menjawab yang keempat.",
                    "",
                    "Yang kedua - dua petugas mengurangi stok bersamaan - sengaja",
                    "digantung paling lama, karena jawabannya butuh hampir semua materi",
                    "sebelumnya. Ia dibuka di materi Dua Pengguna Bersamaan: Race Condition",
                    "dan Penguncian. Jadi kalau di tengah jalan kamu merasa pertanyaan itu",
                    "terlewat begitu saja, ia tidak terlewat - ia sedang menunggu gilirannya.",
                    "",
                    "PATOKAN UNTUK MODUL INI",
                    "",
                    "Aplikasi yang kita bedah bernama B-iFAMS. Isinya kira-kira:",
                    "",
                    "  - 8 jenis benda yang disimpan (item, kategori, mutasi, dst.)",
                    "  - 6 controller",
                    "  - sekitar 15 halaman",
                    "",
                    "Skalanya menengah-kecil. Untuk developer Java berpengalaman:",
                    "3-6 minggu. Untuk yang baru belajar: 6-12 bulan, dan hasil",
                    "pertamanya kemungkinan besar dibongkar ulang. Itu normal dan",
                    "bukan tanda kamu gagal.",
                ]
            },
        ],
    },
    {
        "title": "2. Lapisan-lapisan Aplikasi Web",
        "sections": [
            {
                "body": [
                    "Ini konsep terpenting di seluruh modul ini. Kalau cuma satu hal",
                    "yang nempel dari sini, semoga yang ini.",
                    "",
                    "Aplikasi web disusun berlapis. Tiap lapisan punya satu tugas, dan",
                    "hanya boleh bicara ke lapisan tepat di bawahnya.",
                    "",
                    "  Browser",
                    "     |  permintaan HTTP: GET /items/61",
                    "     v",
                    "  SERVER APLIKASI (Tomcat) + FILTER",
                    "     |            menerima koneksi mentah, memilihkan controller yang",
                    "     |            tepat, dan menyaring lebih dulu - misalnya menolak",
                    "     |            permintaan dari orang yang belum login. Kodenya bukan",
                    "     |            tulisanmu; isinya dibahas di materi Server Aplikasi.",
                    "     v",
                    "  CONTROLLER    menerjemahkan HTTP <-> Java. Tidak tahu SQL.",
                    "     |",
                    "     v",
                    "  SERVICE       tempat ATURAN BISNIS hidup. Tidak tahu HTTP.",
                    "     |",
                    "     v",
                    "  DAO           satu-satunya yang bicara ke database.",
                    "     |",
                    "     v",
                    "  DATABASE      menyimpan data secara permanen.",
                    "",
                    "Perhatikan kalimat 'tidak tahu' di tiap lapisan. Itu bukan",
                    "kekurangan, itu justru intinya.",
                ]
            },
            {
                "body": [
                    "KENAPA REPOT-REPOT DIPISAH?",
                    "",
                    "Bayangkan aturan 'stok tidak boleh negatif'. Aturan ini harus",
                    "berlaku di mana pun stok berkurang:",
                    "",
                    "  - saat petugas mencatat barang keluar",
                    "  - saat permintaan peminjaman disetujui",
                    "  - saat barang ditandai rusak",
                    "",
                    "Kalau aturannya ditulis di controller, kamu menulisnya TIGA KALI.",
                    "Suatu hari salah satunya lupa diperbarui, dan stok jadi negatif",
                    "lewat jalur yang terlupakan itu.",
                    "",
                    "Kalau aturannya ditulis sekali di service, ketiga jalur memanggil",
                    "service yang sama. Mustahil ada jalur yang lolos.",
                    "",
                    "ATURAN PRAKTIS",
                    "",
                    "  Controller  tipis. Ambil input, panggil service, pilih halaman.",
                    "              Kalau ada 'if' rumit di sini, biasanya salah tempat.",
                    "",
                    "  Service     tebal. Semua keputusan ada di sini.",
                    "",
                    "  DAO         bodoh. Cuma simpan dan ambil. Tidak boleh memutuskan.",
                ]
            },
            {
                "heading": "Contoh nyata dari B-iFAMS",
                "code": """// CONTROLLER - tipis, cuma menghubungkan
@RequestMapping(value = "/{id}/stock", method = RequestMethod.POST)
public String sesuaikanStok(@PathVariable Long id,
                            @RequestParam MovementType type,
                            @RequestParam int qty,
                            RedirectAttributes ra) {
    try {
        stockService.catatMutasi(id, type, qty);   // keputusan bukan di sini
        ra.addFlashAttribute("success", "Mutasi tersimpan.");
    } catch (StokTidakCukupException e) {
        ra.addFlashAttribute("error", e.getMessage());
    }
    return "redirect:/items/" + id;
}"""
            },
            {
                "body": [
                    "Lihat controller di atas: tidak ada satu pun aturan bisnis.",
                    "Ia cuma menerima, memanggil, dan menentukan halaman berikutnya.",
                    "Keputusan 'boleh atau tidak' ada di dalam catatMutasi().",
                    "",
                    "Kalau besok ada halaman baru yang juga mengurangi stok, halaman",
                    "itu tinggal memanggil catatMutasi() dan otomatis ikut terlindungi.",
                    "",
                    "SEBELUM KAMU MENYALAHKAN DIRI SENDIRI",
                    "",
                    "Kode di atas penuh benda yang memang BELUM dijelaskan: baris berawalan",
                    "@ seperti @RequestMapping dan @PathVariable, tipe MovementType,",
                    "objek RedirectAttributes, dan StokTidakCukupException. Itu disengaja.",
                    "",
                    "Semuanya dibuka satu per satu nanti - MovementType dan exception di",
                    "materi Enum dan Exception, deretan @ dan RedirectAttributes di materi",
                    "Anotasi Controller. Yang diminta darimu di sini cuma satu: melihat",
                    "bahwa controller ini tidak memutuskan apa-apa.",
                    "",
                    "Jadi kalau bagian ini terasa buram, hampir pasti yang menghalangi",
                    "sintaks yang belum diperkenalkan, bukan gagasan lapisannya.",
                ]
            },
        ],
    },
    {
        "title": "3. Model Data: dari Benda Nyata ke Tabel",
        "sections": [
            {
                "body": [
                    "Sebelum menulis kode, gambar dulu di kertas: BENDA APA SAJA yang",
                    "disimpan sistem ini, dan bagaimana hubungannya.",
                    "",
                    "Bagian ini paling sering diremehkan dan paling mahal kalau salah.",
                    "Mengubah model data setelah aplikasi berisi data asli itu berat -",
                    "seperti mengganti pondasi rumah yang sudah ditinggali.",
                    "",
                    "CARA MENEMUKAN BENDANYA",
                    "",
                    "Baca dokumen kebutuhan, lalu lingkari semua KATA BENDA-nya.",
                    "",
                    "  'Petugas mencatat item baru beserta kategorinya, lalu setiap",
                    "   perubahan stok dicatat sebagai mutasi. Pekerja dari seksi lain",
                    "   mengajukan permintaan peminjaman barang.'",
                    "",
                    "Kata benda: petugas, item, kategori, stok, mutasi, pekerja,",
                    "permintaan, barang.",
                    "",
                    "Beberapa ternyata sama (petugas & pekerja = pengguna; barang &",
                    "item = item). Beberapa bukan benda tapi sifat (stok = angka milik",
                    "item, bukan benda tersendiri).",
                    "",
                    "Sisanya jadi tabel.",
                ]
            },
            {
                "heading": "Model data B-iFAMS",
                "code": """Kategori ---punya banyak---> Item ---punya banyak---> MutasiStok
                              |
                              +---muncul di---> BarisPermintaan
                                                     ^
                                                     | berisi banyak
                                                Permintaan
                                                     ^
                                                     | mengajukan
                                                 Pengguna"""
            },
            {
                "body": [
                    "TIGA JENIS HUBUNGAN",
                    "",
                    "  Satu ke banyak (paling sering)",
                    "    Satu kategori punya banyak item.",
                    "    Satu item punya banyak baris mutasi.",
                    "    Caranya: tabel 'banyak' menyimpan id si 'satu'.",
                    "    Tabel item punya kolom category_id.",
                    "",
                    "  Banyak ke banyak",
                    "    Satu permintaan berisi banyak item,",
                    "    satu item muncul di banyak permintaan.",
                    "    Caranya: bikin tabel penghubung di tengah.",
                    "    Di B-iFAMS namanya request_item.",
                    "",
                    "  Satu ke satu (jarang)",
                    "    Biasanya tanda dua tabel itu sebenarnya satu.",
                    "",
                    "SATU PERTANYAAN YANG MENYELAMATKAN",
                    "",
                    "Untuk tiap kolom, tanya: 'kalau ini berubah, apa yang harus",
                    "ikut berubah?' Kalau jawabannya banyak, model datamu belum benar.",
                    "",
                    "Contoh: kalau nama item disimpan juga di tabel mutasi, maka",
                    "mengganti nama item harus memperbarui ratusan baris mutasi. Itu",
                    "tanda seharusnya mutasi cukup menyimpan item_id saja.",
                ]
            },
        ],
    },
    {
        "title": "4. Entitas: Benda Menjadi Kelas",
        "sections": [
            {
                "body": [
                    "Tiap benda di model data jadi satu kelas Java. Kelas semacam ini",
                    "disebut ENTITAS, dan bentuknya sangat sederhana: field privat,",
                    "getter, setter. Tidak ada logika rumit di dalamnya.",
                    "",
                    "Kelas seperti ini sering dijuluki POJO - Plain Old Java Object.",
                    "Namanya terdengar merendahkan, padahal justru pujian: artinya",
                    "kelas biasa yang tidak terikat framework apa pun.",
                    "",
                    "KENAPA FIELD-NYA PRIVAT?",
                    "",
                    "Supaya nilainya cuma bisa diubah lewat pintu yang kamu kendalikan.",
                    "Kalau field publik, siapa pun bisa menulis item.stok = -5 dari mana",
                    "saja, dan kamu tidak punya tempat untuk mencegahnya.",
                ]
            },
            {
                "heading": "Entitas Item yang disederhanakan",
                "code": """public class Item {
    private Long id;
    private String kode;
    private String nama;
    private String satuan;
    private int stok;
    private int stokMinimum;

    public Item(String kode, String nama, String satuan, int stokMinimum) {
        this.kode = kode;
        this.nama = nama;
        this.satuan = satuan;
        this.stokMinimum = stokMinimum;
        this.stok = 0;
    }

    public String getKode()   { return kode; }
    public String getNama()   { return nama; }
    public String getSatuan() { return satuan; }
    public int getStok()      { return stok; }
    public void setStok(int stok) { this.stok = stok; }

    public boolean isStokMenipis() {
        return stok <= stokMinimum;
    }

    @Override
    public String toString() {
        return kode + " - " + nama + " (" + stok + " " + satuan + ")";
    }
}"""
            },
            {
                "body": [
                    "Perhatikan method isStokMenipis(). Ini contoh logika yang PANTAS",
                    "ada di entitas: ia cuma menjawab pertanyaan tentang dirinya",
                    "sendiri, tidak butuh data lain, tidak menyentuh database.",
                    "",
                    "Bandingkan dengan 'apakah item ini boleh dipinjam?' - itu butuh",
                    "tahu status junk, tanggal kedaluwarsa, dan jumlah yang diminta.",
                    "Pertanyaan seperti itu tempatnya di service, bukan di entitas.",
                    "",
                    "GARIS PEMISAHNYA",
                    "",
                    "  Di entitas   : pertanyaan yang bisa dijawab dari field sendiri.",
                    "  Di service   : keputusan yang butuh data lain atau efek samping.",
                    "",
                    "KENAPA isStokMenipis(), BUKAN stokMenipis()?",
                    "",
                    "Dan kenapa ada getSatuan() padahal tidak ada satu baris pun di materi",
                    "ini yang memanggilnya?",
                    "",
                    "Karena halaman yang menampilkan item nanti ditulis begini:",
                    "",
                    "  Stok saat ini: ${item.stok} ${item.satuan}",
                    "",
                    "Tulisan ${item.satuan} TIDAK membaca field satuan - ia mencari method",
                    "bernama getSatuan(). Begitu juga ${item.stokMenipis}, yang mencari",
                    "isStokMenipis(). Awalan get dan is di situ bukan selera penamaan,",
                    "melainkan syarat; boolean boleh memakai is, sisanya harus get.",
                    "",
                    "Di program Java murni nama apa pun jalan, jadi kesalahan ini tidak",
                    "pernah ketahuan sampai halamannya dibuka. Aturan lengkapnya - beserta",
                    "gejalanya kalau salah - ada di materi Tampilan.",
                ]
            },
        ],
    },
    {
        "title": "5. Enum dan Exception Buatan Sendiri",
        "sections": [
            {
                "body": [
                    "Dua nama sudah beberapa kali lewat di contoh kode modul ini tanpa pernah",
                    "dijelaskan dari mana asalnya: Status.PENDING dan AturanDilanggar.",
                    "",
                    "Keduanya bukan bawaan Java. Keduanya ditulis sendiri oleh pembuat",
                    "aplikasinya, satu berkas masing-masing, dan letaknya persis di sebelah",
                    "entitas. Hampir tiap aplikasi Java punya sepasang tipe pendukung seperti",
                    "ini. Sekarang giliran kita membuatnya.",
                    "",
                    "ENUM: DAFTAR NILAI YANG SUDAH HABIS DISEBUT",
                    "",
                    "Status sebuah permintaan cuma boleh salah satu dari empat: PENDING,",
                    "APPROVED, REJECTED, RETURNED. Tidak ada yang kelima, dan itu bukan",
                    "kebetulan - itu keputusan yang diambil sadar-sadar saat merancang.",
                    "",
                    "Kalau statusnya disimpan sebagai String, tidak ada apa pun yang menjaga",
                    "keputusan itu:",
                    "",
                    "  p.setStatus(\"APROVED\");    // salah ketik, tetap dikompilasi",
                    "  p.setStatus(\"approved\");   // beda huruf besar-kecil, tetap dikompilasi",
                    "  p.setStatus(\"Selasa\");     // ngawur sekalian, tetap dikompilasi",
                    "",
                    "Ketiganya baru ketahuan saat aplikasi jalan. Dan kalau apesnya baris itu",
                    "jarang dilewati, ketahuannya berbulan-bulan kemudian - saat sebuah",
                    "permintaan mendadak tidak pernah muncul di daftar mana pun, karena",
                    "layar daftar mencari \"APPROVED\" sedangkan di database tertulis \"APROVED\".",
                    "",
                    "Enum memindahkan penjagaan itu ke compiler. Status.APROVED tidak",
                    "dikompilasi sama sekali. Kesalahannya berhenti di laptopmu, bukan di",
                    "server, dan itulah seluruh alasan enum ada.",
                ],
            },
            {
                "heading": "Status dan MovementType, dari deklarasi sampai dijalankan",
                "code": """public class DemoStatus {

    // Di proyek sungguhan tiap tipe ini tinggal di berkasnya sendiri:
    // Status.java dan MovementType.java. Di sini digabung jadi satu
    // supaya bisa langsung dijalankan.

    enum Status {
        PENDING, APPROVED, REJECTED, RETURNED
    }

    enum MovementType {
        IN("Masuk", 1),
        OUT("Keluar", -1);

        private final String label;
        private final int arah;

        MovementType(String label, int arah) {
            this.label = label;
            this.arah = arah;
        }

        public String getLabel() { return label; }

        public int terapkan(int stok, int jumlah) {
            return stok + arah * jumlah;
        }
    }

    static String pesan(Status s) {
        switch (s) {
            case PENDING:  return "Menunggu persetujuan";
            case APPROVED: return "Sudah disetujui";
            case REJECTED: return "Ditolak";
            case RETURNED: return "Barang sudah kembali";
            default:       throw new IllegalStateException("Status belum ditangani: " + s);
        }
    }

    public static void main(String[] args) {
        Status s = Status.PENDING;

        System.out.println("toString  : " + s);
        System.out.println("name()    : " + s.name());
        System.out.println("ordinal() : " + s.ordinal());
        System.out.println("pesan     : " + pesan(s));

        // Enum dibandingkan dengan ==, bukan equals.
        System.out.println("s == Status.PENDING : " + (s == Status.PENDING));

        System.out.println("Semua nilai Status:");
        for (Status x : Status.values()) {
            System.out.println("  " + x.ordinal() + " " + x.name());
        }

        int stok = 20;
        for (MovementType t : MovementType.values()) {
            stok = t.terapkan(stok, 5);
            System.out.println(t.getLabel() + " 5 -> stok " + stok);
        }

        System.out.println("Dari teks : " + Status.valueOf("APPROVED"));
    }
}""",
            },
            {
                "body": [
                    "ENUM BUKAN SEKADAR DAFTAR NAMA",
                    "",
                    "Lihat MovementType di atas: ia punya field, constructor, dan method",
                    "sendiri. Itu bukan fitur aneh - enum memang KELAS. Bedanya cuma satu,",
                    "objeknya sudah ditentukan habis di baris pertama dan tidak ada satu pun",
                    "kode yang bisa membuat yang baru.",
                    "",
                    "Itu yang membuatnya jauh lebih berguna daripada sekadar kumpulan",
                    "konstanta. Pertanyaan 'mutasi ini menambah atau mengurangi stok?' punya",
                    "SATU jawaban, dan jawabannya tinggal di dalam MovementType sendiri.",
                    "Tanpa enum, pertanyaan itu berubah jadi if-else yang tersebar di berapa",
                    "pun tempat stok dihitung - dan suatu hari salah satunya lupa diperbarui.",
                    "",
                    "Perhatikan juga titik komanya. Daftar konstanta ditutup dengan ';'",
                    "sebelum field dan method menyusul. Lupa titik koma itu error pertama",
                    "yang hampir pasti kamu temui saat menulis enum yang ada isinya.",
                    "",
                    "JEBAKAN 1: DI SINI PAKAI ==, BUKAN equals",
                    "",
                    "Materi String mengajarkan aturan keras: bandingkan String dengan",
                    ".equals(), jangan pernah dengan ==. Untuk enum aturan itu tidak berlaku,",
                    "dan malah dibalik - enum dibandingkan dengan ==.",
                    "",
                    "Sebabnya: tiap konstanta enum cuma punya SATU objek seumur hidup",
                    "program. Status.PENDING di baris mana pun adalah objek yang sama persis,",
                    "jadi == pasti benar. Dan ia membawa dua keuntungan lagi:",
                    "",
                    "  - 'p.getStatus() == Status.PENDING' aman walau statusnya null;",
                    "    'p.getStatus().equals(...)' meledak jadi NullPointerException.",
                    "  - membandingkan dua tipe enum berbeda ditolak compiler",
                    "    (\"incomparable types\"), sedangkan equals() cuma diam-diam false.",
                    "",
                    "Satu catatan sintaks yang sering bikin bingung: di dalam switch, label",
                    "cabangnya ditulis POLOS - 'case PENDING:', bukan 'case Status.PENDING:'.",
                    "Menuliskan nama enumnya di depan justru ditolak compiler.",
                    "",
                    "JEBAKAN 2: ordinal() DAN CARA MENYIMPAN ENUM DI DATABASE",
                    "",
                    "ordinal() mengembalikan posisi konstanta: PENDING 0, APPROVED 1, dan",
                    "seterusnya. Angka itu ringkas, enak dipandang, dan sangat menggoda untuk",
                    "disimpan. Jangan.",
                    "",
                    "Nomor itu bukan milikmu, melainkan milik URUTAN PENULISAN. Suatu hari",
                    "seseorang menyisipkan satu konstanta baru di tengah:",
                    "",
                    "  PENDING, REVIEW, APPROVED, REJECTED, RETURNED",
                    "",
                    "Kode tetap dikompilasi, tes tetap hijau, aplikasi tetap start. Tapi tiap",
                    "baris lama yang berisi 1 - dulu berarti APPROVED - sekarang dibaca",
                    "sebagai REVIEW, dan yang 2 jadi APPROVED. Ribuan baris berubah arti tanpa",
                    "satu pun UPDATE pernah dijalankan, dan tidak ada error yang muncul.",
                    "",
                    "Yang disimpan seharusnya name()-nya: teks \"APPROVED\", yang artinya tetap",
                    "sama walau urutan konstantanya diacak besok. ordinal() dipakai untuk",
                    "mengurutkan tampilan, tidak untuk apa pun yang bertahan lebih lama dari",
                    "satu kali jalan.",
                    "",
                    "Di Hibernate ini cuma satu anotasi di entitas:",
                    "",
                    "  @Enumerated(EnumType.STRING)    disimpan sebagai teks    <- pakai ini",
                    "  @Enumerated(EnumType.ORDINAL)   disimpan sebagai angka   <- jebakan tadi",
                    "",
                    "Dan bagian paling menipunya: ORDINAL adalah nilai bawaannya. Field enum",
                    "yang lupa ditandai sama sekali juga tersimpan sebagai angka. Diamnya",
                    "compiler di sini bukan tanda semuanya beres.",
                    "",
                    "Kebalikannya, Status.valueOf(\"APPROVED\") mengubah teks jadi enum lagi -",
                    "dan melempar IllegalArgumentException kalau teksnya tidak dikenal. Itu",
                    "justru yang kamu mau: data kotor berhenti di pintu masuk.",
                ],
            },
            {
                "heading": "Kelas exception sendiri, dan lapisan mana yang menangkap",
                "body": [
                    "Satu catch menangkap keduanya, karena StokTidakCukupException adalah",
                    "turunan AturanDilanggar. Menangkap induknya berarti otomatis ikut",
                    "menangkap semua pelanggaran aturan yang ditambahkan belakangan.",
                    "",
                    "CONSTRUCTOR KEDUA ITU BUKAN HIASAN",
                    "",
                    "AturanDilanggar(String pesan, Throwable penyebab) dipakai saat kamu",
                    "menangkap error dari bawah lalu melemparnya ulang dengan bahasa",
                    "aplikasimu sendiri:",
                    "",
                    "  try {",
                    "      itemDao.simpan(item);",
                    "  } catch (SQLException e) {",
                    "      throw new AturanDilanggar(\"Gagal menyimpan item.\", e);",
                    "  }",
                    "",
                    "Kalau penyebabnya tidak ikut dibawa, stack trace di log berhenti di",
                    "barismu dan jejak SQLException aslinya lenyap. Kamu jadi tahu ada yang",
                    "gagal, tapi tidak pernah tahu kenapa - dan itu jenis log yang paling",
                    "menyiksa dibaca jam dua pagi.",
                ],
                "code": """public class DemoAturan {

    // Di proyek sungguhan: AturanDilanggar.java dan
    // StokTidakCukupException.java, masing-masing satu berkas.

    static class AturanDilanggar extends RuntimeException {
        public AturanDilanggar(String pesan) {
            super(pesan);
        }

        public AturanDilanggar(String pesan, Throwable penyebab) {
            super(pesan, penyebab);
        }
    }

    static class StokTidakCukupException extends AturanDilanggar {
        public StokTidakCukupException(String nama, int tersedia, int diminta) {
            super("Stok tidak mencukupi untuk " + nama
                    + " (tersedia " + tersedia + ", diminta " + diminta + ").");
        }
    }

    // SERVICE - perhatikan: tidak ada satu pun kata 'throws' di sini.
    static void catatKeluar(String nama, int stok, int jumlah) {
        if (jumlah <= 0)
            throw new AturanDilanggar("Jumlah mutasi harus lebih dari nol.");
        if (stok < jumlah)
            throw new StokTidakCukupException(nama, stok, jumlah);
        System.out.println("OK      : " + nama + " keluar " + jumlah
                + ", sisa " + (stok - jumlah));
    }

    // CONTROLLER - satu-satunya lapisan yang menangkap.
    static void coba(String nama, int stok, int jumlah) {
        try {
            catatKeluar(nama, stok, jumlah);
        } catch (AturanDilanggar e) {
            System.out.println("DITOLAK : " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        coba("APAR", 20, 5);
        coba("Selang", 3, 10);
        coba("APAR", 20, 0);
    }
}""",
            },
            {
                "body": [
                    "KENAPA extends RuntimeException, BUKAN extends Exception?",
                    "",
                    "Materi Exception Handling di modul Java membuat contohnya dengan",
                    "'extends Exception'. Itu exception CHECKED: begitu sebuah method bisa",
                    "melemparnya, method itu wajib menulis 'throws', dan setiap pemanggilnya",
                    "wajib menangkap atau ikut menulis 'throws'.",
                    "",
                    "Bayangkan akibatnya di aplikasi berlapis. Aturan bisnis dilanggar jauh di",
                    "dalam service, tapi yang tahu cara menyampaikannya ke pengguna cuma",
                    "controller. Kalau checked, kata 'throws AturanDilanggar' harus ditempel",
                    "di setiap method sepanjang jalur - service, service yang memanggilnya,",
                    "controller - semata-mata untuk mengantar satu pesan lewat.",
                    "",
                    "Karena itu pelanggaran aturan bisnis dibuat UNCHECKED, yaitu turunan",
                    "RuntimeException. Ia melompati semua lapisan di tengah tanpa satu pun",
                    "'throws', lalu ditangkap di satu tempat yang memang tahu mau diapakan.",
                    "",
                    "Ini sekaligus menjawab hal yang mungkin sempat terasa ganjil: method",
                    "setujui() di materi Service melempar AturanDilanggar tanpa menulis",
                    "'throws' apa-apa di tanda tangannya. Itu sah persis karena AturanDilanggar",
                    "unchecked. Andai ia turunan Exception, kode itu tidak akan dikompilasi.",
                    "",
                    "PATOKAN MEMILIH",
                    "",
                    "  Checked    keadaan di luar kendalimu yang memang wajar terjadi dan",
                    "             bisa dipulihkan: berkas hilang, koneksi putus.",
                    "  Unchecked  pelanggaran aturan yang seharusnya tidak terjadi:",
                    "             stok kurang, status salah, id tidak ada.",
                    "",
                    "SATU PERAN SATU NAMA",
                    "",
                    "Di aplikasi ini nama bakunya AturanDilanggar - satu kelas induk untuk",
                    "semua pelanggaran aturan bisnis. StokTidakCukupException yang muncul di",
                    "contoh controller adalah TURUNANNYA, dibuat terpisah karena kasus stok",
                    "cukup sering perlu ditangani sendiri, misalnya untuk menawarkan jumlah",
                    "alternatif alih-alih sekadar menolak.",
                    "",
                    "Aturan mainnya: bikin turunan baru hanya kalau ada tempat yang",
                    "benar-benar menangkapnya secara terpisah. Kalau semua penangkapnya sama",
                    "saja, satu kelas dengan pesan berbeda sudah cukup. Puluhan kelas",
                    "exception yang selalu ditangkap bersama-sama cuma menambah berkas.",
                    "",
                    "Dan sekali sebuah nama dipilih, pakai nama itu di seluruh aplikasi. Dua",
                    "kelas berbeda untuk satu peran yang sama adalah cara paling halus",
                    "membuat sebuah catch diam-diam melewatkan setengah kasusnya.",
                ],
            },
        ],
    },
    {
        "title": "6. DAO: Satu-satunya Pintu ke Database",
        "sections": [
            {
                "body": [
                    "DAO singkatan dari Data Access Object. Tugasnya satu: menerjemahkan",
                    "antara objek Java dan baris tabel. Tidak lebih.",
                    "",
                    "Aturannya keras: SELURUH SQL di aplikasimu harus ada di dalam DAO.",
                    "Kalau ada SQL bocor ke controller atau service, kamu kehilangan",
                    "kemampuan menjawab pertanyaan 'siapa saja yang menyentuh tabel ini?'",
                    "",
                    "BENTUK BAKUNYA",
                    "",
                    "  simpan(objek)        -> INSERT atau UPDATE",
                    "  cariById(id)         -> SELECT satu baris",
                    "  cariSemua()          -> SELECT banyak baris",
                    "  hapus(id)            -> DELETE",
                    "",
                    "Plus pencarian khusus sesuai kebutuhan, misalnya:",
                    "",
                    "  cariStokMenipis()",
                    "  cariAkanKedaluwarsa(int hari)",
                ]
            },
            {
                "heading": "DAO sebagai antarmuka",
                "code": """public interface ItemDao {
    Item cariById(Long id);
    List<Item> cariSemua();
    List<Item> cariStokMenipis();
    void simpan(Item item);
    void hapus(Long id);
}"""
            },
            {
                "body": [
                    "Kenapa dibuat interface dulu, bukan langsung kelas?",
                    "",
                    "Karena service cukup tahu APA yang bisa dilakukan, tidak perlu tahu",
                    "CARANYA. Hari ini implementasinya pakai Hibernate ke Oracle; besok",
                    "bisa diganti ke PostgreSQL atau bahkan ke daftar di memori untuk",
                    "keperluan pengujian - dan service tidak perlu diubah sebaris pun.",
                    "",
                    "Ini bukan teori. Latihan di modul ini memakai DAO versi memori,",
                    "sehingga kamu bisa melatih logika service tanpa memasang database",
                    "apa pun.",
                    "",
                    "HIBERNATE MENGERJAKAN BAGIAN MEMBOSANKANNYA",
                    "",
                    "Menulis SQL manual untuk tiap tabel itu melelahkan dan rawan salah",
                    "ketik. Hibernate membacanya dari anotasi di entitas lalu membuatkan",
                    "SQL-nya sendiri. Kamu cukup menandai:",
                    "",
                    "  @Entity              kelas ini mewakili sebuah tabel",
                    "  @Table(name=\"item\")  nama tabelnya",
                    "  @Id                  kolom kunci utama",
                    "  @Column              pengaturan kolom",
                    "  @ManyToOne           hubungan ke tabel lain",
                    "",
                    "Tapi hati-hati: Hibernate menyembunyikan SQL, bukan menghapusnya.",
                    "Saat aplikasi melambat, kamu tetap harus bisa membaca SQL yang",
                    "dihasilkannya. Karena itu belajar SQL tidak bisa dilewati.",
                ]
            },
        ],
    },
    {
        "title": "7. Hubungan Antar Entitas dan Kapan Datanya Diambil",
        "sections": [
            {
                "body": [
                    "Materi Entitas sudah mengubah benda jadi kelas, materi DAO sudah",
                    "mengurung seluruh SQL di satu pintu. Tapi entitas Item di sana",
                    "meninggalkan dua lubang yang belum pernah dijelaskan.",
                    "",
                    "Lubang pertama: baris paling atas berbunyi private Long id, dan tidak",
                    "ada satu pun kode di seluruh modul ini yang pernah mengisinya.",
                    "",
                    "Lubang kedua: materi 3 menggambar 'Kategori punya banyak Item' -",
                    "padahal kelas Item tidak punya field kategori sama sekali, dan kelas",
                    "Kategori belum pernah ditulis.",
                    "",
                    "Dua lubang itu isi materi ini.",
                    "",
                    "SIAPA YANG MENGISI id",
                    "",
                    "Bukan kamu. Nomornya dibuat DATABASE saat barisnya pertama kali",
                    "disimpan, lalu Hibernate menyalinnya kembali ke objekmu setelah INSERT",
                    "berhasil. Kamu cuma menyebutkan cara pembuatannya:",
                    "",
                    "  @Id                                kolom ini kunci utama",
                    "  @GeneratedValue(strategy = ...)    siapa yang membuat nilainya",
                    "",
                    "Strategi yang benar-benar dipakai orang ada dua:",
                    "",
                    "  IDENTITY   kolomnya sendiri yang menghitung naik.",
                    "             Ini AUTO_INCREMENT di MySQL, serial di PostgreSQL.",
                    "",
                    "  SEQUENCE   ada benda terpisah di database - namanya sequence -",
                    "             yang tugasnya membagikan nomor. Cara khas Oracle, jadi",
                    "             inilah yang dipakai B-iFAMS.",
                    "",
                    "  AUTO       serahkan pilihannya ke Hibernate. Enak sampai suatu hari",
                    "             ia memilih hal yang tidak kamu duga.",
                    "",
                    "TIGA JEBAKAN DI SEKITAR SATU BARIS ITU",
                    "",
                    "1. Jangan mengisi id sendiri untuk objek baru.",
                    "   Bagi Hibernate, id yang sudah terisi adalah tanda 'baris ini sudah",
                    "   ada di database'. Menyimpannya berubah jadi UPDATE ke baris yang",
                    "   tidak pernah ada, dan yang kamu dapat bukan pesan yang menjelaskan",
                    "   melainkan 'Batch update returned unexpected row count from update",
                    "   [0]; actual row count: 0'. Perhatikan konstruktor Item di materi 4:",
                    "   ia memang tidak menyentuh id sama sekali. Sekarang kamu tahu kenapa",
                    "   itu benar.",
                    "",
                    "2. Pakai Long, bukan long.",
                    "   Objek yang belum pernah disimpan harus bisa berkata 'aku belum",
                    "   punya id'. Hanya tipe pembungkus yang bisa bernilai null; dengan",
                    "   long primitif, id-nya 0 dan pemeriksaan if (item.getId() == null)",
                    "   tidak bisa ditulis sama sekali.",
                    "",
                    "3. Kalau memakai SEQUENCE, allocationSize harus cocok.",
                    "   Bawaan JPA-nya 50: Hibernate mengambil satu nomor dari sequence",
                    "   lalu menganggap 49 nomor sesudahnya sudah jadi miliknya. Kalau",
                    "   sequence di Oracle ternyata naik satu-satu, dua aplikasi yang",
                    "   berjalan bersamaan akan membagikan id yang sama dan INSERT-nya",
                    "   bentrok. Angka di anotasi wajib sama dengan INCREMENT BY di",
                    "   database.",
                ],
            },
            {
                "heading": "Dua sisi satu hubungan, dan cuma satu yang punya kolom",
                "body": [
                    "Sebuah hubungan ditulis DUA KALI - sekali di tiap kelas - tapi hanya",
                    "SATU sisi yang benar-benar punya kolom di database.",
                    "",
                    "Ingat aturan materi 3: tabel di sisi 'banyak' yang menyimpan id si",
                    "'satu'. Jadi kolom category_id ada di tabel item; di tabel category",
                    "tidak ada apa pun tentang item. Sisi yang memegang kolomnya disebut",
                    "SISI PEMILIK.",
                    "",
                    "  Item      @ManyToOne + @JoinColumn      sisi pemilik, punya kolomnya",
                    "  Kategori  @OneToMany(mappedBy = ...)    sisi cermin, cuma memantulkan",
                    "",
                    "mappedBy artinya 'kolomnya bukan urusanku, tanya sebelah'. Nilainya -",
                    "\"kategori\" - adalah NAMA FIELD di kelas Item. Bukan nama kolom",
                    "category_id, bukan nama tabel, bukan nama kelas. Salah ketik di situ",
                    "membuat aplikasi menolak start dengan pesan 'mappedBy reference an",
                    "unknown target entity property'. Untungnya ini jenis kesalahan yang",
                    "berteriak.",
                    "",
                    "YANG TIDAK BERTERIAK ADA DUA",
                    "",
                    "1. Lupa mappedBy sama sekali.",
                    "   @OneToMany tanpa mappedBy tidak dianggap salah. JPA justru membuat",
                    "   TABEL PENGHUBUNG ketiga (category_items) untuk mencatat hubungan",
                    "   yang sudah tercatat di kolom category_id. Dua tempat mencatat hal",
                    "   yang sama, dan cepat atau lambat isinya berbeda.",
                    "",
                    "2. Mengisi sisi cermin saja.",
                    "   kategori.getItems().add(item) terasa benar, dan selama masih di",
                    "   memori memang terlihat benar. Tapi Hibernate cuma menyimpan sisi",
                    "   pemilik, jadi setelah commit kolom category_id item itu tetap NULL.",
                    "   Item-nya 'masuk kategori' sampai aplikasi di-restart, lalu hilang",
                    "   dari sana tanpa pernah ada error.",
                    "",
                    "Obatnya bukan kedisiplinan mengingat dua baris, melainkan satu method",
                    "yang mengurus kedua sisi sekaligus - tambahItem() di bawah ini.",
                ],
                "code": """// Kategori.java
@Entity
@Table(name = "category")
public class Kategori {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE,
                    generator = "kategori_gen")
    @SequenceGenerator(name = "kategori_gen",
                       sequenceName = "CATEGORY_SEQ",
                       allocationSize = 1)          // sama dgn INCREMENT BY
    private Long id;

    private String nama;

    // SISI CERMIN. "kategori" di bawah adalah nama FIELD di kelas Item.
    @OneToMany(mappedBy = "kategori")
    private List<Item> items = new ArrayList<>();

    public List<Item> getItems() { return items; }

    // Satu-satunya cara menambah item, supaya tidak ada yang lupa
    // memasang sisi pemiliknya.
    public void tambahItem(Item item) {
        items.add(item);
        item.setKategori(this);   // <-- baris inilah yang benar-benar disimpan
    }
}

// Item.java
@Entity
@Table(name = "item")
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String kode;
    private int stok;

    // SISI PEMILIK: kolom category_id ada di tabel item.
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "category_id")
    private Kategori kategori;

    public Kategori getKategori() { return kategori; }
    public void setKategori(Kategori kategori) { this.kategori = kategori; }
}""",
            },
            {
                "heading": "Induk, anak, dan siapa yang ikut terhapus",
                "body": [
                    "Kategori dan Item hidup sendiri-sendiri: menghapus satu kategori tidak",
                    "boleh ikut menghapus itemnya.",
                    "",
                    "Permintaan dan BarisPermintaan tidak begitu. Satu baris permintaan",
                    "('APAR CO2 3kg, 2 buah') tidak berarti apa-apa tanpa permintaan yang",
                    "memuatnya. Hubungan seperti ini disebut induk-anak, dan JPA punya dua",
                    "saklar untuknya:",
                    "",
                    "  cascade = CascadeType.ALL    apa pun yang kulakukan pada induk,",
                    "                               lakukan juga pada anak-anaknya",
                    "  orphanRemoval = true         anak yang dikeluarkan dari koleksi",
                    "                               berarti dihapus dari database",
                    "",
                    "Tanpa cascade, menyimpan Permintaan baru berujung pada error yang",
                    "sering bikin bingung: 'object references an unsaved transient",
                    "instance'. Terjemahannya: induknya siap disimpan, anaknya belum",
                    "pernah disimpan, dan tidak ada yang diperintahkan menyimpannya.",
                    "",
                    "Tanpa orphanRemoval, mengeluarkan satu baris dari daftar tidak",
                    "mengubah apa pun di database. Barisnya tetap utuh di tabel",
                    "request_item lengkap dengan request_id-nya, dan begitu permintaannya",
                    "dimuat ulang, baris yang tadi 'dihapus' muncul kembali. Bentuk",
                    "sebaliknya lebih buruk lagi: baris yang induknya benar-benar hilang",
                    "tetap tinggal di tabel, menggantung tanpa siapa-siapa. Materi 13",
                    "menceritakan wajah lain dari kejadian itu di B-iFAMS - itemnya",
                    "dihapus, permintaannya tertinggal menunjuk ke ketiadaan, dan layar",
                    "tidak menunjukkan apa pun.",
                    "",
                    "CASCADE ARAHNYA SATU",
                    "",
                    "Dari induk ke anak, tidak pernah sebaliknya. Menempelkan",
                    "cascade = ALL pada @ManyToOne - dari anak ke induk - mengubah 'hapus",
                    "satu item' menjadi 'hapus kategorinya sekalian, beserta seluruh item",
                    "lain di dalamnya'. Tidak ada error, tidak ada peringatan; yang ada",
                    "cuma data yang lenyap.",
                    "",
                    "Patokannya: cascade REMOVE hanya untuk bagian yang memang mati",
                    "bersama induknya. MutasiStok milik sebuah Item TIDAK termasuk - ia",
                    "catatan riwayat, dan riwayat justru harus selamat.",
                    "",
                    "Jangan tertukar dengan ON DELETE CASCADE milik database. Yang di",
                    "anotasi bekerja di Java sebelum SQL dikirim; yang di database bekerja",
                    "bahkan untuk DELETE yang diketik langsung lewat sqlplus.",
                    "",
                    "KAPAN @ManyToMany BOLEH DIPAKAI",
                    "",
                    "Materi 3 menyebut tabel penghubung request_item untuk 'satu",
                    "permintaan berisi banyak item, satu item muncul di banyak",
                    "permintaan'. @ManyToMany menuliskan persis hubungan itu tanpa kelas",
                    "tambahan - JPA yang mengurus tabel tengahnya.",
                    "",
                    "B-iFAMS tetap tidak memakainya, dan alasannya penting: tabel",
                    "penghubungnya punya kolom sendiri, yaitu jumlah yang diminta.",
                    "@ManyToMany cuma sanggup mencatat 'A tersambung ke B'; tidak ada",
                    "tempat menaruh kolom ketiga. Begitu tabel penghubung punya kolomnya",
                    "sendiri, ia naik pangkat jadi entitas biasa - dan namanya",
                    "BarisPermintaan.",
                    "",
                    "Yang tersisa untuk @ManyToMany adalah sambungan polos, misalnya",
                    "pengguna dan perannya - ADMIN dan REQUESTER, yang dibahas nanti di",
                    "materi Keamanan.",
                    "",
                    "Satu catatan untuk membaca kode nyata: tabel permintaannya bernama",
                    "item_request sedangkan tabel penghubungnya request_item. Dua kata",
                    "yang sama, tinggal dibalik. Jangan menebak dari nama - baca @Table.",
                ],
                "code": """// Permintaan.java -- INDUK
@Entity
@Table(name = "item_request")
public class Permintaan {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToMany(mappedBy = "permintaan",
               cascade = CascadeType.ALL,   // simpan induk = simpan anak
               orphanRemoval = true)        // dikeluarkan dari list = DELETE
    private List<BarisPermintaan> baris = new ArrayList<>();

    // Pemohon TIDAK di-cascade: ia milik bersama, bukan bagian dari
    // permintaan ini. Menghapus permintaan tidak boleh menghapus orangnya.
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "requester_id")
    private Pengguna pemohon;

    public List<BarisPermintaan> getBaris() { return baris; }
}

// BarisPermintaan.java -- ANAK. Inilah tabel request_item dari materi 3,
// naik pangkat jadi entitas karena punya kolom sendiri: jumlah.
@Entity
@Table(name = "request_item")
public class BarisPermintaan {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "request_id")
    private Permintaan permintaan;   // nama field ini yang ditunjuk mappedBy

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "item_id")
    private Item item;

    private int jumlah;              // kolom milik tabel penghubung
}

// Pengguna.java -- @ManyToMany yang sah: tabel tengahnya polos,
// cuma dua kolom id dan tidak ada kolom tambahan.
@Entity
@Table(name = "app_user")
public class Pengguna {

    @ManyToMany
    @JoinTable(name = "user_role",
               joinColumns = @JoinColumn(name = "user_id"),
               inverseJoinColumns = @JoinColumn(name = "role_id"))
    private Set<Peran> peran = new HashSet<>();
}""",
            },
            {
                "heading": "Kapan datanya diambil: LAZY, EAGER, dan error paling sering",
                "body": [
                    "Saat Hibernate memuat sebuah Permintaan, apakah baris-barisnya ikut",
                    "diambil? Kamu yang menentukan, lewat fetch:",
                    "",
                    "  FetchType.EAGER   ambil sekalian, sekarang juga",
                    "  FetchType.LAZY    tunda; ambil kalau nanti benar-benar disentuh",
                    "",
                    "Bawaannya berbeda per anotasi, dan tidak ada yang bisa menebaknya:",
                    "",
                    "  @OneToMany     LAZY     koleksi, ditunda",
                    "  @ManyToMany    LAZY",
                    "  @ManyToOne     EAGER    ikut terbawa, mau atau tidak",
                    "  @OneToOne      EAGER",
                    "",
                    "Itu sebabnya di semua kode di atas @ManyToOne selalu ditulis ulang",
                    "dengan fetch = FetchType.LAZY. Kalau dibiarkan, memuat satu",
                    "BarisPermintaan ikut memuat Item-nya, yang ikut memuat Kategori-nya,",
                    "dan seterusnya - satu baris kecil menyeret setengah database.",
                    "",
                    "GETTER RELASI BUKAN SEKADAR MENGEMBALIKAN FIELD",
                    "",
                    "Ini kalimat terpenting di materi ini.",
                    "",
                    "Pada relasi LAZY, Hibernate tidak menaruh List biasa di field itu. Ia",
                    "menaruh penyamar (proxy) yang isinya masih kosong. Sentuhan pertama -",
                    "size(), perulangan, get(0) - barulah menembakkan SELECT.",
                    "",
                    "Artinya baris ini, yang sudah kamu baca di materi Service:",
                    "",
                    "  for (BarisPermintaan baris : p.getBaris())",
                    "",
                    "bukan pembacaan field. Itu sebuah query. Dan query yang duduk di",
                    "dalam perulangan adalah query yang jumlahnya ikut tumbuh bersama",
                    "datanya.",
                    "",
                    "LazyInitializationException",
                    "",
                    "Penundaan itu cuma berlaku selama sesi Hibernate masih terbuka -",
                    "biasanya selama method @Transactional di service masih berjalan.",
                    "Padahal JSP baru dirender SESUDAH service selesai. Jadi baris ini di",
                    "tampilan:",
                    "",
                    "  <c:forEach items=\"${permintaan.baris}\" var=\"b\">",
                    "",
                    "menyentuh koleksi yang sesinya sudah ditutup, dan hasilnya:",
                    "",
                    "  org.hibernate.LazyInitializationException: failed to lazily",
                    "  initialize a collection of role: model.Permintaan.baris -",
                    "  could not initialize proxy - no Session",
                    "",
                    "TIGA CARA MENUTUPNYA",
                    "",
                    "1. Sentuh selagi transaksinya masih terbuka.",
                    "   Cukup p.getBaris().size() di dalam service. Paling cepat ditulis,",
                    "   paling jelek dibaca: sebaris kode yang kelihatannya tidak",
                    "   melakukan apa-apa, dan orang berikutnya akan menghapusnya.",
                    "",
                    "2. Minta sekalian di query-nya, pakai JOIN FETCH. Lihat kode di bawah.",
                    "",
                    "3. Jangan kirim entitas ke tampilan sama sekali. Susun objek berisi",
                    "   data siap tampil di dalam service, lalu kirim objek itu. Namanya",
                    "   DTO, dan ada materinya sendiri sebentar lagi.",
                    "",
                    "SATU CARA YANG SEBAIKNYA TIDAK",
                    "",
                    "Membiarkan sesi terbuka sampai halaman selesai dirender - namanya",
                    "Open Session In View, dan di Spring Boot saklarnya",
                    "spring.jpa.open-in-view yang bawaannya MENYALA. Error-nya memang",
                    "hilang. Penyebabnya tidak: query-nya tetap ditembakkan satu per satu,",
                    "sekarang dari dalam JSP, di tempat yang tidak seorang pun mengira ada",
                    "query. Itu persis bahan bakar masalah di bagian berikutnya.",
                ],
                "code": """// Di dalam DAO. Sebutkan apa yang ikut dibawa; jangan berharap
// koleksinya "ada saja" waktu JSP membutuhkannya.
public Permintaan cariByIdLengkap(Long id) {
    return em.createQuery(
              "SELECT DISTINCT p FROM Permintaan p "
            + "LEFT JOIN FETCH p.baris b "     // koleksinya ikut terisi
            + "LEFT JOIN FETCH b.item "        // sekalian item tiap baris
            + "WHERE p.id = :id", Permintaan.class)
            .setParameter("id", id)
            .getSingleResult();
}

// LEFT, bukan INNER: permintaan yang barisnya kosong tetap harus ketemu.
// DISTINCT karena JOIN mengembalikan satu baris hasil per BarisPermintaan,
// sehingga tanpa itu satu Permintaan muncul berkali-kali.
// Dan satu koleksi saja per query: dua JOIN FETCH ke dua koleksi sekaligus
// menghasilkan MultipleBagFetchException - atau, kalau lolos, perkalian
// silang 5 baris x 4 lampiran = 20 baris hasil.""",
            },
            {
                "heading": "Masalah N+1, dihitung sendiri",
                "body": [
                    "Gabungkan dua hal barusan: getter relasi itu query, dan halaman daftar",
                    "memanggil getter untuk SETIAP baris.",
                    "",
                    "Halaman 'Daftar Kategori' yang menampilkan jumlah item tiap kategori",
                    "menembakkan:",
                    "",
                    "  1 query    SELECT * FROM category",
                    "  N query    SELECT * FROM item WHERE category_id = ?   satu per baris",
                    "",
                    "Itulah masalah N+1. Namanya membosankan, akibatnya tidak: dengan 8",
                    "kategori kamu tidak akan merasakan apa pun. Dengan 2.000 item dan",
                    "ratusan pengguna, halaman yang sama butuh puluhan detik - dan yang",
                    "sampai ke telingamu cuma 'aplikasinya lemot'.",
                    "",
                    "CARA MELIHATNYA",
                    "",
                    "Hibernate mau menunjukkan SQL-nya kalau diminta:",
                    "",
                    "  hibernate.show_sql=true      cetak tiap SQL yang dikirim",
                    "  hibernate.format_sql=true    supaya terbaca, bukan satu baris panjang",
                    "",
                    "Di Spring Boot: spring.jpa.show-sql=true, atau lebih baik",
                    "logging.level.org.hibernate.SQL=DEBUG supaya ikut masuk ke log.",
                    "",
                    "Lalu buka SATU halaman dan HITUNG barisnya. Kalau satu halaman daftar",
                    "mencetak 41 SELECT untuk 40 baris data, kamu baru saja menemukan N+1",
                    "tanpa perlu menebak-nebak.",
                    "",
                    "CARA MENGHITUNG YANG SEHARUSNYA",
                    "",
                    "Patokannya: satu query per TABEL yang datanya kamu butuhkan, bukan",
                    "satu query per baris. Daftar 40 item beserta nama kategorinya",
                    "seharusnya 1 query (sekali JOIN) atau 2 (item dulu, lalu semua",
                    "kategorinya sekaligus). Bukan 41.",
                    "",
                    "Selain JOIN FETCH, ada @BatchSize(size = 20) di koleksinya: Hibernate",
                    "mengumpulkan id yang masih tertunda lalu menembak satu",
                    "SELECT ... WHERE category_id IN (...). 41 query jadi 3. Bukan yang",
                    "tercepat, tapi paling murah dipasang di kode lama yang tidak berani",
                    "kamu ubah query-nya.",
                    "",
                    "Program di bawah menirukan keduanya tanpa database apa pun, supaya",
                    "angkanya bisa kamu lihat sendiri. Jalankan, lalu tambah isi",
                    "TABEL_ITEM dan tambah satu kategori - perhatikan angka mana yang ikut",
                    "membesar, dan angka mana yang tetap 1.",
                ],
                "code": """import java.util.*;

/* Meniru cara Hibernate memuat relasi LAZY, tanpa database sungguhan:
   koleksinya masih kosong saat entitas induk dimuat, dan SELECT baru
   ditembak saat getter-nya dipanggil untuk pertama kali. */
public class DemoNPlusSatu {

    static int query = 0;          // berapa kali database ditanyai

    static class Item {
        final String kategori, nama;
        Item(String kategori, String nama) {
            this.kategori = kategori;
            this.nama = nama;
        }
    }

    static final Item[] TABEL_ITEM = {
        new Item("APAR", "APAR CO2 3kg"),
        new Item("APAR", "APAR Powder 6kg"),
        new Item("SCBA", "Masker SCBA"),
        new Item("SCBA", "Tabung SCBA 6.8L"),
        new Item("APD",  "Sarung tangan tahan api"),
    };

    static class Kategori {
        final String nama;
        List<Item> items;          // null = koleksinya belum dimuat
        Kategori(String nama) { this.nama = nama; }

        List<Item> getItems() {    // getter yang diam-diam menembak SELECT
            if (items == null) items = selectItemMilik(nama);
            return items;
        }
    }

    static List<Kategori> tigaKategori() {
        return new ArrayList<>(Arrays.asList(
                new Kategori("APAR"),
                new Kategori("SCBA"),
                new Kategori("APD")));
    }

    // SELECT * FROM category
    static List<Kategori> selectKategori() {
        query++;
        return tigaKategori();
    }

    // SELECT * FROM item WHERE category_id = ?   <- satu per kategori
    static List<Item> selectItemMilik(String kategori) {
        query++;
        List<Item> hasil = new ArrayList<>();
        for (Item i : TABEL_ITEM)
            if (i.kategori.equals(kategori)) hasil.add(i);
        return hasil;
    }

    // SELECT ... FROM category LEFT JOIN item ...  <- tetap satu query
    static List<Kategori> selectKategoriJoinFetchItem() {
        query++;
        List<Kategori> hasil = tigaKategori();
        for (Kategori k : hasil) {
            k.items = new ArrayList<>();
            for (Item i : TABEL_ITEM)
                if (i.kategori.equals(k.nama)) k.items.add(i);
        }
        return hasil;
    }

    static void cetak(List<Kategori> daftar) {
        for (Kategori k : daftar) {
            int jumlah = k.getItems().size();
            System.out.println("  " + k.nama + ": " + jumlah + " item");
        }
        System.out.println("  -> query terpakai: " + query);
    }

    public static void main(String[] args) {
        query = 0;
        System.out.println("Cara LAZY polos:");
        cetak(selectKategori());

        query = 0;
        System.out.println("Cara JOIN FETCH:");
        cetak(selectKategoriJoinFetchItem());
    }
}""",
            },
        ],
    },
    {
        "title": "8. Wadah Objek Spring: Bean dan Injeksi Dependensi",
        "sections": [
            {
                "body": [
                    "Balik sebentar ke materi Service. Kelas RequestService dibuka begini:",
                    "",
                    "  private final ItemDao itemDao;",
                    "  private final RequestDao requestDao;",
                    "",
                    "Dua field. Sekarang cari di kelas itu: tidak ada constructor, tidak ada",
                    "setter, tidak ada satu pun 'new ItemDaoImpl()'. Tidak ada satu baris pun",
                    "yang mengisi kedua field itu.",
                    "",
                    "Kalau kamu menyalin kelas itu apa adanya lalu memanggil setujui(), yang",
                    "kamu dapat adalah NullPointerException di baris pertama - itemDao masih",
                    "null. Jadi di aplikasi sungguhan, SIAPA yang mengisinya?",
                    "",
                    "Jawabannya bukan Java. Jawabannya Spring. Dan cara kerjanya adalah hal",
                    "yang paling sering tidak pernah dijelaskan ke orang yang baru membuka",
                    "proyek Spring - padahal baris pertama hampir setiap kelas di proyek",
                    "seperti itu justru tentang ini.",
                    "",
                    "WADAH OBJEK",
                    "",
                    "Saat aplikasi dinyalakan, sebelum permintaan pertama datang, Spring",
                    "membuat satu objek besar bernama ApplicationContext. Orang menyebutnya",
                    "WADAH (container). Tugasnya tiga:",
                    "",
                    "  1. MEMBUAT objek-objek yang dibutuhkan aplikasi.",
                    "  2. MENYIMPANNYA selama aplikasi hidup.",
                    "  3. MENYERAHKANNYA ke objek lain yang membutuhkannya.",
                    "",
                    "Objek yang dikelola wadah punya nama sendiri: BEAN. Sebuah bean cuma",
                    "objek Java biasa - tidak ada yang ajaib padanya, tidak ada kelas induk",
                    "yang harus diwarisi. Yang membedakannya dari objek biasa hanya satu:",
                    "bukan kamu yang mengetik 'new', melainkan wadah.",
                    "",
                    "Menyerahkan barang yang dibutuhkan KE DALAM sebuah objek, alih-alih",
                    "menyuruh objek itu mencarinya sendiri, namanya INJEKSI DEPENDENSI",
                    "(dependency injection). 'Dependensi' berarti benda yang dibutuhkan:",
                    "RequestService bergantung pada ItemDao, jadi ItemDao adalah dependensinya.",
                    "Nama besarnya Inversion of Control - itu sebabnya wadahnya sering disebut",
                    "'IoC container' di dokumentasi.",
                    "",
                    "KENAPA REPOT? KENAPA TIDAK 'new' SAJA?",
                    "",
                    "Kalau tiap kelas membuat sendiri barang yang dibutuhkannya:",
                    "",
                    "  - RequestService terikat mati ke satu implementasi DAO. Materi DAO",
                    "    menjanjikan implementasinya bisa ditukar tanpa mengubah service;",
                    "    begitu ada 'new ItemDaoImpl()' di dalam service, janji itu batal.",
                    "  - Saat menguji, kamu tidak punya celah untuk menyelipkan DAO palsu.",
                    "  - Objek mahal seperti koneksi database dibuat berulang-ulang, padahal",
                    "    seharusnya satu saja dipakai bersama.",
                    "  - Urutan pembuatannya jadi urusanmu. Di aplikasi berisi 40 kelas yang",
                    "    saling membutuhkan, urutan itu tidak enak dipelihara tangan.",
                ],
            },
            {
                "heading": "Wadahnya tidak ajaib - ini versi Java murninya",
                "code": """import java.util.*;

public class WadahMini {

    public static void main(String[] args) {
        // Beginilah kira-kira yang dikerjakan Spring saat aplikasi start:
        // buat yang paling bawah dulu, lalu serahkan ke yang membutuhkan.
        ItemDao dao = new ItemDaoMemori();
        StokService service = new StokService(dao);

        service.kurangi("APAR-6KG", 3);
        service.kurangi("APAR-6KG", 30);
    }
}

interface ItemDao {
    int stok(String kode);
    void simpan(String kode, int jumlah);
}

class ItemDaoMemori implements ItemDao {

    private final Map<String, Integer> tabel = new HashMap<String, Integer>();

    ItemDaoMemori() {
        tabel.put("APAR-6KG", 20);
    }

    public int stok(String kode) {
        return tabel.get(kode);
    }

    public void simpan(String kode, int jumlah) {
        tabel.put(kode, jumlah);
    }
}

class StokService {

    private final ItemDao itemDao;          // final: wajib terisi, tak bisa null

    StokService(ItemDao itemDao) {          // satu-satunya jalan masuk
        this.itemDao = itemDao;
    }

    void kurangi(String kode, int jumlah) {
        int sekarang = itemDao.stok(kode);
        if (sekarang < jumlah) {
            System.out.println("Ditolak: stok " + kode + " cuma " + sekarang);
            return;
        }
        itemDao.simpan(kode, sekarang - jumlah);
        System.out.println("Sisa stok " + kode + ": " + itemDao.stok(kode));
    }
}""",
            },
            {
                "body": [
                    "Jalankan program di atas. Keluarannya:",
                    "",
                    "  Sisa stok APAR-6KG: 17",
                    "  Ditolak: stok APAR-6KG cuma 17",
                    "",
                    "Dua baris di main() itulah seluruh isi gagasannya. StokService tidak tahu",
                    "DAO-nya versi memori; ia cuma tahu ada sesuatu bertipe ItemDao yang",
                    "diserahkan lewat constructor. Kalau besok DAO-nya diganti versi Oracle,",
                    "StokService tidak berubah sebaris pun. Spring melakukan persis hal ini,",
                    "cuma untuk 40 kelas sekaligus dan tanpa kamu ketik di main().",
                    "",
                    "PENANDA KELAS: SIAPA YANG DIJADIKAN BEAN",
                    "",
                    "Wadah tadi tahu harus membuat apa karena kamu mengetiknya. Spring tidak",
                    "punya main() semacam itu, jadi ia diberi tahu lewat anotasi:",
                    "",
                    "  @Component   penanda dasar: 'buatkan satu bean dari kelas ini'",
                    "  @Controller  sama artinya, untuk lapisan controller",
                    "  @Service     sama artinya, untuk lapisan service",
                    "  @Repository  sama artinya, untuk lapisan DAO",
                    "",
                    "Tiga yang bawah sebenarnya @Component juga - cuma diberi nama sesuai",
                    "lapisan di materi Lapisan-lapisan Aplikasi Web. Buat Spring, @Service dan",
                    "@Component nyaris identik. Bedanya buat MANUSIA: sekali lihat baris",
                    "pertama sebuah kelas, kamu langsung tahu ia duduk di lapisan mana.",
                    "",
                    "Satu yang benar-benar berbeda: @Repository juga menyalakan penerjemah",
                    "error database. Tanpa itu, kegagalan Hibernate atau JDBC keluar sebagai",
                    "exception khas pustaka masing-masing; dengan @Repository, semuanya",
                    "diterjemahkan jadi satu keluarga DataAccessException milik Spring -",
                    "sehingga service-mu tidak perlu tahu database apa yang dipakai.",
                    "",
                    "Di contoh kode nanti kamu juga akan melihat @PersistenceContext di dalam",
                    "ItemDaoImpl. Itu injeksi juga, cuma yang menyerahkan bukan Spring",
                    "melainkan JPA, dan yang diserahkan adalah EntityManager - pintu ke",
                    "Hibernate. Cukup dikenali dulu; isinya urusan materi DAO dan entitas.",
                    "",
                    "BAGAIMANA SPRING MENEMUKANNYA: COMPONENT SCAN",
                    "",
                    "Anotasi saja tidak cukup - Spring tidak menyisir seluruh isi hard disk.",
                    "Ia diberi satu titik awal, lalu memeriksa semua kelas di bawahnya:",
                    "",
                    "  <context:component-scan base-package=\"com.badak.ifams\" />",
                    "",
                    "atau versi anotasinya:",
                    "",
                    "  @ComponentScan(\"com.badak.ifams\")",
                    "",
                    "'Paket' (package) adalah baris pertama tiap berkas Java, dan isinya WAJIB",
                    "sama dengan susunan foldernya di bawah src/main/java - susunan yang",
                    "dibedah lengkap nanti di materi Maven dan Struktur Proyek:",
                    "",
                    "  src/main/java/com/badak/ifams/service/RequestService.java",
                    "     -> package com.badak.ifams.service;",
                    "",
                    "JEBAKAN YANG SERING MEMAKAN WAKTU SEHARI: kelasmu sudah diberi @Service",
                    "dengan benar, tapi paketnya di luar base-package - misalnya",
                    "com.badak.util.LaporanService. Spring tidak pernah melihatnya, bean-nya",
                    "tidak pernah dibuat, dan aplikasi gagal start dengan",
                    "NoSuchBeanDefinitionException. Pesannya menyebut tipe yang dicari, bukan",
                    "paket yang salah, jadi orang sering mencari ke arah yang keliru.",
                    "",
                    "KONVENSI ItemService + ItemServiceImpl",
                    "",
                    "Di banyak proyek kamu akan menemukan pasangan: sebuah interface bernama",
                    "ItemService, dan sebuah kelas ItemServiceImpl yang mengimplementasikannya.",
                    "Anotasi @Service menempel di Impl-nya, sedangkan yang diminta kelas lain",
                    "adalah interface-nya. Persis pola yang sudah dipakai materi DAO.",
                    "",
                    "Kalau implementasinya memang cuma satu dan tidak pernah ditukar, interface",
                    "itu sebenarnya tidak menambah apa-apa - dan proyek modern makin sering",
                    "melewatkannya. Tapi di kode lama pola ini ada di mana-mana, jadi jangan",
                    "kaget menemukan interface yang cuma punya satu pemakai.",
                ],
                "code": """// src/main/java/com/badak/ifams/dao/ItemDao.java
package com.badak.ifams.dao;

public interface ItemDao {              // kontraknya - lihat materi DAO
    Item cariById(Long id);
    void simpan(Item item);
}


// src/main/java/com/badak/ifams/dao/ItemDaoImpl.java
package com.badak.ifams.dao;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;

@Repository                             // "buatkan satu bean dari kelas ini"
public class ItemDaoImpl implements ItemDao {

    @PersistenceContext
    private EntityManager em;           // diserahkan JPA, bukan oleh @Autowired

    public Item cariById(Long id) {
        return em.find(Item.class, id);
    }

    public void simpan(Item item) {
        em.merge(item);
    }
}


// src/main/java/com/badak/ifams/service/RequestService.java
package com.badak.ifams.service;

import com.badak.ifams.dao.ItemDao;
import com.badak.ifams.dao.RequestDao;
import org.springframework.stereotype.Service;

@Service
public class RequestService {

    private final ItemDao itemDao;
    private final RequestDao requestDao;

    public RequestService(ItemDao itemDao, RequestDao requestDao) {
        this.itemDao = itemDao;         // Spring yang mengisi kedua argumen ini
        this.requestDao = requestDao;
    }

    // setujui(...) isinya persis seperti di materi Service -
    // bedanya sekarang field-nya benar-benar terisi.
}""",
            },
            {
                "body": [
                    "INJEKSI LEWAT CONSTRUCTOR",
                    "",
                    "Perhatikan RequestService di atas: tidak ada anotasi apa pun di field-nya.",
                    "Dependensinya masuk lewat argumen constructor, dan Spring mengisinya",
                    "dengan mencocokkan TIPE - ia mencari bean bertipe ItemDao di wadah,",
                    "menemukan ItemDaoImpl, lalu menyerahkannya.",
                    "",
                    "Sejak Spring 4.3, kelas yang cuma punya SATU constructor tidak perlu",
                    "ditandai apa pun. Di kode yang lebih tua kamu akan melihat @Autowired",
                    "menempel di constructor itu; artinya sama persis, jadi jangan bingung",
                    "melihat dua bentuk yang berbeda mengerjakan hal yang sama.",
                    "",
                    "BENTUK LAMA: @Autowired DI FIELD",
                    "",
                    "  @Service",
                    "  public class RequestService {",
                    "      @Autowired",
                    "      private ItemDao itemDao;      // tanpa final, tanpa constructor",
                    "  }",
                    "",
                    "Bentuk ini masih sangat banyak ditemui dan memang lebih pendek. Tiga",
                    "kerugiannya nyata:",
                    "",
                    "  1. Field-nya tidak bisa 'final'. Dengan constructor, compiler MEMAKSA",
                    "     field terisi sebelum objeknya selesai dibuat - secara struktur",
                    "     mustahil null. Dengan @Autowired di field, objeknya sudah ada lebih",
                    "     dulu dan field-nya diisi belakangan lewat refleksi; ada jeda saat",
                    "     nilainya masih null.",
                    "",
                    "  2. Sulit diuji. Untuk menguji service dengan DAO palsu, kamu butuh",
                    "     jalan masuk. Constructor adalah jalan masuk itu, dan tanpa framework",
                    "     apa pun: new RequestService(daoPalsu, requestPalsu). Dengan field",
                    "     injection tidak ada jalan masuk sama sekali - kamu harus menyalakan",
                    "     seluruh Spring, atau membobol field lewat refleksi.",
                    "",
                    "  3. Dependensi yang menumpuk jadi tak terlihat. Constructor dengan",
                    "     delapan argumen kelihatan jelek - dan memang seharusnya begitu,",
                    "     karena kelas yang butuh delapan benda memang kebanyakan tugas.",
                    "     Anotasi di field menyembunyikan gejala itu sampai terlambat.",
                    "",
                    "Aturan praktisnya: TULIS constructor injection di kode baru, KENALI field",
                    "injection saat membaca kode lama.",
                    "",
                    "KALAU KELASNYA BUKAN MILIKMU",
                    "",
                    "@Service dan saudara-saudaranya cuma bisa ditempel di kelas yang kamu",
                    "tulis sendiri. Lalu bagaimana dengan DataSource, PasswordEncoder, atau",
                    "ObjectMapper - kelas milik pustaka orang lain yang berkasnya saja tidak",
                    "kamu punya?",
                    "",
                    "Untuk itu ada @Configuration: kelas yang isinya RESEP, bukan logika",
                    "aplikasi. Tiap method ber-@Bean adalah satu resep. Spring memanggil method",
                    "itu sekali saat start, lalu memasukkan nilai kembaliannya ke wadah sebagai",
                    "bean. Nama bean-nya diambil dari nama method-nya, jadi method dataSource()",
                    "menghasilkan bean bernama 'dataSource'.",
                    "",
                    "Perhatikan juga passwordEncoder() di bawah: begitu ia jadi bean, kelas",
                    "mana pun tinggal meminta PasswordEncoder di constructor-nya dan pasti",
                    "dapat objek yang sama - tidak ada lagi kemungkinan satu bagian aplikasi",
                    "memakai algoritma sandi yang berbeda dari bagian lain.",
                ],
                "code": """package com.badak.ifams.config;

import javax.sql.DataSource;
import org.apache.commons.dbcp.BasicDataSource;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
public class KonfigurasiAplikasi {

    // Nilainya dibaca dari src/main/resources/jdbc.properties, tidak diketik
    // di sini. Alasannya dibahas di materi konfigurasi & rahasia.
    @Value("${jdbc.url}")      private String url;
    @Value("${jdbc.user}")     private String user;
    @Value("${jdbc.password}") private String sandi;

    @Bean                               // nama bean-nya: "dataSource"
    public DataSource dataSource() {
        BasicDataSource ds = new BasicDataSource();
        ds.setDriverClassName("oracle.jdbc.OracleDriver");
        ds.setUrl(url);
        ds.setUsername(user);
        ds.setPassword(sandi);
        ds.setMaxActive(20);            // kelas milik pustaka orang lain:
        return ds;                      // tidak bisa ditempeli @Repository
    }

    @Bean                               // nama bean-nya: "passwordEncoder"
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}""",
            },
            {
                "body": [
                    "DUA WADAH, BUKAN SATU",
                    "",
                    "Sampai sini kita bicara seolah wadahnya satu. Di aplikasi Spring MVC gaya",
                    "lama - termasuk B-iFAMS - wadahnya ADA DUA. Inilah penjelasan yang",
                    "dijanjikan materi Keamanan.",
                    "",
                    "  WADAH WEB (anak)      dibuat DispatcherServlet",
                    "    resepnya   dispatcher-servlet.xml",
                    "    isinya     @Controller, view resolver, handler mapping",
                    "       |",
                    "       |   anak boleh melihat isi induknya",
                    "       v",
                    "  WADAH ROOT (induk)    dibuat ContextLoaderListener",
                    "    resepnya   applicationContext.xml",
                    "    isinya     @Service, @Repository, DataSource, PasswordEncoder",
                    "",
                    "Panahnya SEARAH, dan itu intinya. Controller di wadah web boleh meminta",
                    "bean service dari wadah root. Sebaliknya tidak bisa: penghuni wadah root",
                    "tidak tahu-menahu soal isi wadah web.",
                    "",
                    "Susunannya masuk akal kalau dilihat dari umurnya. Wadah root berisi hal",
                    "yang tidak ada urusannya dengan web - aturan bisnis, database - dan hidup",
                    "selama aplikasi hidup. Wadah web berisi mesin penerjemah HTTP saja.",
                    "",
                    "KENAPA ANOTASI HAK AKSES BISA DIAM SAJA",
                    "",
                    "Anotasi seperti @PreAuthorize tidak bekerja sendiri. Yang menghidupkannya",
                    "adalah satu baris konfigurasi:",
                    "",
                    "  <security:global-method-security pre-post-annotations=\"enabled\" />",
                    "",
                    "Baris itu menyuruh WADAH membungkus tiap bean ber-@PreAuthorize dengan",
                    "lapisan pemeriksa (proxy) yang menolak panggilan sebelum method aslinya",
                    "jalan. Dan ia cuma membungkus penghuni wadah TEMPAT BARIS ITU DITULIS.",
                    "",
                    "Kalau baris itu ditaruh di applicationContext.xml sementara controller-nya",
                    "tinggal di wadah web, hasilnya persis bug yang diceritakan materi",
                    "Keamanan: penandanya lengkap, ejaannya benar, tidak ada error, tidak ada",
                    "peringatan - dan tidak satu pun aktif. Sekarang kamu tahu mekanismenya,",
                    "bukan cuma ceritanya.",
                    "",
                    "Aturan praktisnya: konfigurasi yang mengubah PERILAKU bean harus tinggal",
                    "di wadah tempat bean itu berada.",
                    "",
                    "  @PreAuthorize di controller  -> aktifkan di dispatcher-servlet.xml",
                    "  @PreAuthorize di service     -> aktifkan di applicationContext.xml",
                    "",
                    "Jebakan yang sama juga mengintai @Transactional dari materi Service.",
                    "Ia pun bekerja lewat proxy, jadi ia pun bisa diam saja - dan sebuah",
                    "@Transactional yang diam berarti perubahan setengah jalan tidak pernah",
                    "dibatalkan. Penghidupnya, <tx:annotation-driven/>, harus berada di wadah",
                    "yang sama dengan service-nya.",
                    "",
                    "Di Spring Boot masalah ini hilang karena wadahnya kembali satu. Tapi",
                    "aplikasi lama yang kemungkinan besar kamu warisi masih memakai susunan",
                    "dua wadah ini, jadi mengenalinya bukan pengetahuan sejarah.",
                    "",
                    "SATU BEAN, SATU OBJEK, DIPAKAI RAMAI-RAMAI",
                    "",
                    "Terakhir, dan ini menjebak hampir semua orang sekali seumur hidup.",
                    "",
                    "Secara bawaan tiap bean dibuat TEPAT SATU KALI (scope singleton). Bukan",
                    "satu per pengguna, bukan satu per permintaan - satu untuk seluruh umur",
                    "aplikasi. Objek RequestService yang sama dipakai bersamaan oleh semua",
                    "orang yang sedang membuka aplikasi.",
                    "",
                    "Konsekuensinya keras: JANGAN PERNAH menyimpan data milik satu pengguna",
                    "di field sebuah bean.",
                    "",
                    "  @Service",
                    "  public class RequestService {",
                    "      private String petugasSaatIni;   // BOM WAKTU",
                    "  }",
                    "",
                    "Dua petugas menyetujui permintaan pada detik yang sama, dan yang kedua",
                    "menimpa nilai milik yang pertama. Nama penyetuju tercatat salah di",
                    "riwayat mutasi. Bug seperti ini nyaris mustahil dilacak dari laporan",
                    "pengguna, karena ia hanya muncul kalau dua orang kebetulan berbarengan -",
                    "dan tidak pernah muncul saat kamu mengujinya sendirian.",
                    "",
                    "Yang boleh tinggal di field sebuah bean hanyalah dependensi: benda yang",
                    "sama untuk semua orang, seperti itemDao tadi. Data milik satu permintaan",
                    "diedarkan lewat ARGUMEN method - seperti namaPetugas di",
                    "setujui(requestId, namaPetugas) pada materi Service. Sekarang jelas kenapa",
                    "parameter itu ada di sana alih-alih disimpan sebagai field.",
                ],
            },
        ],
    },
    {
        "title": "9. Service: Tempat Aturan Bisnis Hidup",
        "sections": [
            {
                "body": [
                    "Kalau aplikasimu punya 'otak', letaknya di sini.",
                    "",
                    "Service menjawab pertanyaan yang tidak bisa dijawab satu entitas",
                    "sendirian, dan mengatur urutan langkah yang harus terjadi bersamaan.",
                    "",
                    "CONTOH: MENYETUJUI PEMINJAMAN",
                    "",
                    "Satu tombol 'Setujui' di layar sebenarnya memicu rantai keputusan:",
                    "",
                    "  1. Apakah permintaannya masih berstatus PENDING?",
                    "  2. Apakah itemnya masih aktif, bukan junk?",
                    "  3. Apakah itemnya belum kedaluwarsa?",
                    "  4. Apakah stoknya mencukupi?",
                    "  5. Kurangi stok item.",
                    "  6. Catat mutasi keluar, sebutkan nomor permintaannya.",
                    "  7. Ubah status jadi APPROVED.",
                    "  8. Catat siapa yang menyetujui dan kapan.",
                    "",
                    "Delapan langkah, dan tidak boleh setengah jalan.",
                ]
            },
            {
                "heading": "Bentuk service-nya",
                "code": """public class RequestService {

    private final ItemDao itemDao;
    private final RequestDao requestDao;

    public void setujui(Long requestId, String namaPetugas) {
        Permintaan p = requestDao.cariById(requestId);

        if (p.getStatus() != Status.PENDING)
            throw new AturanDilanggar("Permintaan sudah diproses.");

        for (BarisPermintaan baris : p.getBaris()) {
            Item item = baris.getItem();

            if (item.isJunk())
                throw new AturanDilanggar(item.getNama() + " berstatus junk.");

            if (item.getStok() < baris.getJumlah())
                throw new AturanDilanggar("Stok tidak mencukupi untuk "
                        + item.getNama() + " (tersedia " + item.getStok()
                        + ", diminta " + baris.getJumlah() + ").");
        }

        for (BarisPermintaan baris : p.getBaris()) {
            Item item = baris.getItem();
            item.setStok(item.getStok() - baris.getJumlah());
            itemDao.simpan(item);
            catatMutasi(item, MovementType.OUT, baris.getJumlah(),
                        "Dipinjam - permintaan " + p.getKode(), namaPetugas);
        }

        p.setStatus(Status.APPROVED);
        p.setDiprosesOleh(namaPetugas);
        requestDao.simpan(p);
    }
}"""
            },
            {
                "body": [
                    "Perhatikan susunannya: SEMUA pemeriksaan dilakukan lebih dulu di",
                    "perulangan pertama, baru perubahan dilakukan di perulangan kedua.",
                    "",
                    "Kenapa tidak digabung saja jadi satu perulangan?",
                    "",
                    "Karena kalau permintaan berisi 5 item dan item kelima ternyata",
                    "stoknya kurang, dengan satu perulangan stok item 1-4 sudah terlanjur",
                    "berkurang saat error dilempar. Data jadi rusak separuh jalan.",
                    "",
                    "Pola 'periksa semua dulu, ubah belakangan' ini nama akademisnya",
                    "atomicity - dan ini salah satu kebiasaan yang membedakan kode",
                    "pemula dari kode yang layak dipakai orang.",
                    "",
                    "TRANSAKSI",
                    "",
                    "Untuk perlindungan yang lebih kuat, database punya TRANSAKSI:",
                    "sekumpulan perubahan yang dianggap satu kesatuan. Kalau ada yang",
                    "gagal di tengah, semuanya dibatalkan otomatis.",
                    "",
                    "Di Spring caranya cukup menempelkan @Transactional di method.",
                    "Tapi anotasi itu baru berguna kalau kamu paham kenapa dibutuhkan -",
                    "dan alasannya persis yang barusan dijelaskan.",
                    "",
                    "Satu detail yang selalu mengejutkan: secara bawaan @Transactional",
                    "membatalkan perubahan HANYA kalau yang dilempar exception unchecked,",
                    "yaitu turunan RuntimeException. Exception checked justru dibiarkan",
                    "lewat sementara transaksinya tetap di-commit. Itulah alasan teknis",
                    "kenapa AturanDilanggar dibuat turunan RuntimeException - bukan sekadar",
                    "supaya kata throws tidak perlu ditulis di sepanjang jalur.",
                    "",
                    "SATU PENGAKUAN, SUPAYA KAMU TIDAK MERASA AMAN TERLALU CEPAT",
                    "",
                    "Pola periksa-dulu-ubah-belakangan melindungi dari GAGAL DI TENGAH",
                    "JALAN. Ia tidak melindungi dari dua permintaan yang berjalan bersamaan",
                    "dan sama-sama BERHASIL: keduanya bisa lolos pemeriksaan stok yang sama",
                    "sebelum salah satunya sempat mengurangi.",
                    "",
                    "Itu masalah lain dengan penangkal lain, dan ada materinya sendiri -",
                    "Dua Pengguna Bersamaan. Untuk sekarang cukup tahu lubang itu ada.",
                ]
            },
        ],
    },
    {
        "title": "10. Controller: Menerjemahkan HTTP",
        "sections": [
            {
                "body": [
                    "Browser tidak mengenal objek Java. Ia cuma tahu mengirim teks",
                    "lewat HTTP dan menerima HTML. Controller adalah penerjemahnya.",
                    "",
                    "ISI SEBUAH PERMINTAAN HTTP",
                    "",
                    "  METHOD   GET (ambil) atau POST (kirim/ubah). Ada beberapa lagi",
                    "           yang dipakai API - daftar lengkapnya di bawah.",
                    "  PATH     /items/61",
                    "  PARAM    ?cari=apar   atau data formulir",
                    "  HEADER   keterangan tambahan, termasuk cookie sesi",
                    "",
                    "GET DAN POST TIDAK BOLEH TERTUKAR",
                    "",
                    "GET harus AMAN: memanggilnya berkali-kali tidak mengubah apa pun.",
                    "POST boleh mengubah data.",
                    "",
                    "Kenapa penting? Karena browser dan mesin pencari bebas memanggil",
                    "GET kapan saja - saat pengguna menekan tombol kembali, saat",
                    "halaman di-refresh, saat tautan di-preview. Kalau menghapus data",
                    "dibuat sebagai GET, satu kali refresh bisa menghapus dua kali.",
                    "",
                    "TUJUH METHOD YANG PERLU KAMU KENAL",
                    "",
                    "  GET      ambil sesuatu, jangan mengubah apa pun",
                    "  POST     kirim sesuatu yang baru, atau jalankan sebuah aksi",
                    "  PUT      ganti SELURUH isi benda di alamat itu dengan yang dikirim",
                    "  PATCH    ganti sebagian field saja, sisanya dibiarkan",
                    "  DELETE   hapus benda di alamat itu",
                    "  HEAD     sama persis dengan GET, tapi balasannya cuma header tanpa",
                    "           isi - dipakai untuk mengecek ada-tidaknya sesuatu",
                    "  OPTIONS  tanya method apa saja yang boleh di alamat ini; browser",
                    "           mengirimnya sendiri sebelum permintaan lintas-domain",
                    "",
                    "Halaman B-iFAMS cuma memakai dua yang pertama, dan itu bukan kemalasan:",
                    "formulir HTML memang cuma bisa GET dan POST. Lima sisanya baru muncul",
                    "kalau yang memanggil bukan formulir melainkan program lain - itu urusan",
                    "materi REST.",
                    "",
                    "DUA SIFAT YANG SELAMA INI DIPAKAI TANPA DISEBUT NAMANYA",
                    "",
                    "  AMAN        method yang tidak mengubah apa pun: GET, HEAD, OPTIONS.",
                    "              Sifat inilah yang membuat browser, mesin pencari, dan",
                    "              tombol refresh merasa berhak memanggilnya kapan saja.",
                    "",
                    "  IDEMPOTEN   method yang dipanggil dua kali hasilnya sama dengan",
                    "              dipanggil sekali: PUT dan DELETE. Menghapus item 61 dua",
                    "              kali tetap berujung pada satu keadaan yang sama, yaitu",
                    "              item 61 tidak ada. Yang AMAN otomatis idempoten juga -",
                    "              yang tidak mengubah apa pun tentu sama saja dipanggil",
                    "              sekali atau sepuluh kali.",
                    "",
                    "POST bukan keduanya, dan di situlah bahayanya: dua kali POST mutasi",
                    "stok berarti stok berkurang dua kali. Ingat kalimat ini - beberapa",
                    "paragraf lagi ia jadi seluruh alasan pola POST-REDIRECT-GET.",
                ]
            },
            {
                "heading": "Peta rute B-iFAMS",
                "code": """GET   /items                 daftar semua item
GET   /items/new             formulir tambah item
POST  /items                 simpan item baru
GET   /items/{id}            detail satu item
GET   /items/{id}/edit       formulir ubah item
POST  /items/{id}            simpan perubahan
POST  /items/{id}/stock      catat mutasi stok
POST  /items/{id}/junk       tandai rusak
POST  /requests/{id}/approve setujui permintaan"""
            },
            {
                "body": [
                    "Tiap baris di daftar itu - satu method DITAMBAH satu path - namanya",
                    "ENDPOINT. Kata itu akan muncul terus: di dokumentasi, di soal latihan,",
                    "dan dalam percakapan sehari-hari (\"endpoint admin\", \"endpoint yang",
                    "membalas JSON\"). Artinya selalu sama, yaitu satu alamat yang bisa",
                    "dipanggil beserta method-nya. Karena itu GET /items dan POST /items",
                    "adalah DUA endpoint, walau path-nya sama persis.",
                    "",
                    "Pola penamaan ini namanya REST. Perhatikan keteraturannya: kata",
                    "benda jamak untuk kumpulan, id untuk satu benda, kata kerja hanya",
                    "muncul untuk aksi yang tidak sekadar simpan/ambil.",
                    "",
                    "Keteraturan ini bukan gaya-gayaan. Dengan pola yang konsisten,",
                    "orang bisa menebak alamat halaman yang belum pernah dilihatnya -",
                    "termasuk kamu sendiri enam bulan lagi.",
                    "",
                    "POLA POST-REDIRECT-GET",
                    "",
                    "Setelah POST berhasil, JANGAN langsung menampilkan halaman.",
                    "Balas dengan perintah pindah alamat (redirect), lalu biarkan",
                    "browser meminta halamannya lewat GET.",
                    "",
                    "Tanpa ini, pengguna yang menekan refresh setelah menyimpan akan",
                    "mengirim formulir yang sama dua kali. Di B-iFAMS itu berarti",
                    "stok berkurang dua kali dari satu pencatatan.",
                    "",
                    "Di kode tadi kamu sudah melihatnya:",
                    "",
                    "  return \"redirect:/items/\" + id;",
                ]
            },
        ],
    },
    {
        "title": "11. Anotasi Controller dan Jalan Data ke Tampilan",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menjelaskan APA tugas controller. Sekarang bagian yang",
                    "paling bikin bingung saat pertama kali membuka kode Spring orang lain:",
                    "baris-baris berawalan @ di atas kelas dan di atas method.",
                    "",
                    "Anotasi bukan perintah yang dijalankan. Ia LABEL. Saat aplikasi menyala,",
                    "Spring membaca semua kelas, melihat labelnya, dan menyusun satu tabel:",
                    "alamat mana dilayani method mana. Sesudah itu barulah permintaan yang",
                    "masuk dicocokkan ke tabel tadi.",
                    "",
                    "Ada akibat yang perlu kamu ingat baik-baik: salah tulis di dalam anotasi",
                    "TIDAK membuat compiler marah. Kodenya terkompilasi mulus, aplikasinya",
                    "menyala, dan yang muncul di browser cuma 404. Compiler tidak tahu alamat",
                    "mana yang kamu maksud - ia cuma melihat sebuah String.",
                    "",
                    "ALAMATNYA DISUSUN DUA TINGKAT",
                    "",
                    "  @Controller                 kelas ini melayani permintaan web",
                    "  @RequestMapping(\"/items\")   semua method di dalamnya berawalan /items",
                    "",
                    "lalu tiap method menambahkan sisanya:",
                    "",
                    "  @GetMapping             ->  GET   /items",
                    "  @GetMapping(\"/{id}\")    ->  GET   /items/61",
                    "  @PostMapping(\"/{id}\")   ->  POST  /items/61",
                    "",
                    "JEBAKAN PERTAMA. Kelasnya sudah dilabeli /items, lalu di method ditulis",
                    "@GetMapping(\"/items/{id}\") karena itu memang alamat yang diinginkan.",
                    "Yang terbentuk justru /items/items/61, dan halaman detail tidak pernah",
                    "ketemu. Awalan di kelas tidak digantikan oleh method - ia MENDAHULUI.",
                    "",
                    "LIMA BENTUK RINGKAS, DAN BENTUK LAMANYA",
                    "",
                    "  @GetMapping      mengambil, tidak mengubah apa pun",
                    "  @PostMapping     mengirim atau menyimpan",
                    "  @PutMapping      mengganti seluruh isi sebuah benda",
                    "  @DeleteMapping   menghapus",
                    "  @PatchMapping    mengubah sebagiannya saja",
                    "",
                    "Kelimanya baru ada sejak Spring 4.3. Sebelum itu - dan di kode lawas yang",
                    "masih dipakai sampai hari ini - bentuknya panjang:",
                    "",
                    "  @RequestMapping(value = \"/{id}/stock\", method = RequestMethod.POST)",
                    "",
                    "artinya sama persis dengan",
                    "",
                    "  @PostMapping(\"/{id}/stock\")",
                    "",
                    "Kamu akan bertemu keduanya di dalam satu proyek yang sama. Itu bukan tanda",
                    "ada yang salah, cuma umur kodenya yang beda.",
                    "",
                    "Satu hal lagi sebelum melihat kodenya: @Controller sekaligus menjadikan",
                    "kelas ini sebuah bean. Itu sebabnya field itemService di bawah bisa terisi",
                    "sendiri tanpa satu pun 'new' - cara kerjanya sudah dibahas di materi bean",
                    "dan injeksi dependensi.",
                ],
            },
            {
                "heading": "Satu controller B-iFAMS, selengkapnya",
                "code": """@Controller
@RequestMapping("/items")
public class ItemController {

    private final ItemService itemService;
    private final StockService stockService;

    @GetMapping
    public String daftar(
            @RequestParam(required = false, defaultValue = "") String cari,
            Model model) {
        model.addAttribute("items", itemService.cari(cari));
        model.addAttribute("cari", cari);
        return "items/list";
    }

    @GetMapping("/{id}")
    public String detail(@PathVariable Long id, Model model) {
        model.addAttribute("item", itemService.ambil(id));
        model.addAttribute("history", stockService.riwayat(id));
        return "items/detail";
    }

    // Bentuk lama; sama artinya dengan @PostMapping("/{id}/stock").
    @RequestMapping(value = "/{id}/stock", method = RequestMethod.POST)
    public String sesuaikanStok(@PathVariable Long id,
                                @RequestParam MovementType type,
                                @RequestParam int qty,
                                RedirectAttributes ra) {
        try {
            stockService.catatMutasi(id, type, qty);
            ra.addFlashAttribute("success", "Mutasi tersimpan.");
        } catch (StokTidakCukupException e) {
            ra.addFlashAttribute("error", e.getMessage());
        }
        return "redirect:/items/" + id;
    }

    // Bentuk lain yang sering ditemui: nama halaman dan datanya
    // dibungkus jadi satu objek, bukan dipisah return + parameter.
    @GetMapping("/{id}/print")
    public ModelAndView cetak(@PathVariable Long id) {
        ModelAndView mv = new ModelAndView("items/print");
        mv.addObject("item", itemService.ambil(id));
        return mv;
    }
}""",
            },
            {
                "body": [
                    "JALAN MASUK: DARI ALAMAT KE PARAMETER JAVA",
                    "",
                    "Dua anotasi mengisi parameter method dari isi permintaan HTTP:",
                    "",
                    "  @PathVariable Long id     mengambil {id} dari ALAMAT-nya: /items/61",
                    "  @RequestParam int qty     mengambil ?qty=5 atau field formulir bernama qty",
                    "",
                    "Patokan gampangnya: kalau nilainya menunjuk BENDA MANA, ia bagian dari",
                    "alamat (@PathVariable). Kalau nilainya cuma menyetel atau menyaring, ia",
                    "parameter (@RequestParam). Karena itu /items/61 memakai path variable,",
                    "sedangkan /items?cari=apar memakai request param.",
                    "",
                    "YANG SEBENARNYA TERJADI DI SITU: KONVERSI",
                    "",
                    "HTTP tidak mengenal tipe. Yang datang dari browser SELALU teks. Tulisan",
                    "\"61\" di alamat dan tulisan \"5\" di formulir sama-sama String.",
                    "",
                    "Spring-lah yang mengubahnya jadi Long, int, atau bahkan enum MovementType",
                    "sesuai tipe yang kamu tulis di parameter. Ini nyaman, tapi jangan lupa:",
                    "konversi bisa GAGAL, dan gagalnya terjadi SEBELUM satu baris pun kodemu",
                    "jalan.",
                    "",
                    "  /items/abc          -> \"abc\" tidak bisa jadi Long",
                    "  ?qty=dua            -> \"dua\" tidak bisa jadi int",
                    "  ?type=KELUAR        -> tidak ada konstanta itu di enum MovementType",
                    "",
                    "Ketiganya berakhir sebagai error 400 dari Spring, bukan sebagai exception",
                    "di service-mu. Jadi jangan menulis pemeriksaan \"kalau qty bukan angka\" di",
                    "dalam method - method itu tidak akan pernah dipanggil.",
                    "",
                    "PARAMETER YANG BOLEH TIDAK ADA",
                    "",
                    "Secara bawaan @RequestParam WAJIB ada. Membuka /items tanpa ?cari= akan",
                    "gagal 400 kalau parameternya ditulis polos. Karena itu di kode di atas:",
                    "",
                    "  @RequestParam(required = false, defaultValue = \"\") String cari",
                    "",
                    "required = false membolehkannya hilang, defaultValue mengisinya kalau",
                    "memang hilang. Sekali defaultValue diberi nilai, required otomatis jadi",
                    "false - jadi kamu tidak akan pernah menerima null di situ, dan tidak perlu",
                    "menulis penjaga null yang tidak ada gunanya.",
                ],
            },
            {
                "body": [
                    "JALAN KELUAR: JEMBATAN KE HALAMAN",
                    "",
                    "Dua baris ini yang selama ini tidak pernah disebut, padahal tanpanya",
                    "halaman JSP tidak punya apa-apa untuk ditampilkan:",
                    "",
                    "  public String detail(@PathVariable Long id, Model model)",
                    "  model.addAttribute(\"history\", stockService.riwayat(id));",
                    "",
                    "Kamu cukup MENULIS parameter bernama Model, dan Spring yang mengisinya.",
                    "Model itu sekadar kotak berisi pasangan nama-nilai. Apa pun yang kamu",
                    "masukkan ke kotak itu bisa dipanggil dari halaman lewat ${nama}.",
                    "",
                    "Inilah asal-usul ${item.nama} dan <c:forEach items=\"${history}\"> di materi",
                    "Tampilan. \"history\" di JSP adalah \"history\" yang kamu ketik di sini.",
                    "",
                    "NAMANYA HARUS SAMA PERSIS - DAN INI JEBAKAN PALING SERING",
                    "",
                    "addAttribute(\"history\", ...) lalu di JSP ditulis ${histori}: JSP TIDAK",
                    "melapor error. Ia menganggap nilainya kosong dan mencetak string kosong.",
                    "Yang kamu lihat adalah tabel tanpa baris, atau judul yang hilang, tanpa",
                    "satu pun pesan galat di layar maupun di log.",
                    "",
                    "Kalau sebuah halaman tampak kosong padahal datanya jelas ada di database,",
                    "curigai nama atributnya lebih dulu - sebelum membongkar service dan DAO.",
                    "",
                    "\"items/detail\" ITU BUKAN NAMA BERKAS",
                    "",
                    "return \"items/detail\" bukan berarti ada berkas bernama items/detail.",
                    "Yang mengurusnya komponen bernama view resolver: ia menempelkan awalan dan",
                    "akhiran yang tertulis di konfigurasi Spring.",
                    "",
                    "  awalan  /WEB-INF/views/   +  \"items/detail\"  +  akhiran  .jsp",
                    "  hasil   /WEB-INF/views/items/detail.jsp",
                    "",
                    "Folder WEB-INF itu yang sudah kamu lihat di struktur proyek Maven. Ia",
                    "sengaja dipilih karena isinya tidak bisa diminta langsung dari browser -",
                    "satu-satunya jalan ke JSP itu lewat controller.",
                    "",
                    "Method cetak() di kode tadi memakai bentuk lain yang juga sering",
                    "ditemui: ModelAndView membungkus nama halaman DAN datanya jadi satu",
                    "objek, lalu objek itu yang di-return. Isinya sama saja - view resolver",
                    "tetap memperlakukan \"items/print\" persis seperti hitungan di atas.",
                    "",
                    "Program berikut menirukan ketiga hal tadi dengan Java polos, tanpa Spring,",
                    "supaya kelihatan bahwa isinya memang sesederhana itu.",
                ],
                "code": """import java.util.LinkedHashMap;
import java.util.Map;

public class JembatanTampilan {

    // "Model" milik Spring pada dasarnya cuma kotak nama-nilai.
    static Map<String, Object> model = new LinkedHashMap<>();

    // Flash attribute: kotak terpisah yang isinya HABIS sekali dibaca.
    static Map<String, Object> flash = new LinkedHashMap<>();

    // Yang dikerjakan view resolver atas String yang kamu return.
    static String resolusiView(String nama) {
        return "/WEB-INF/views/" + nama + ".jsp";
    }

    // Yang dikerjakan ${...} di JSP: mencari nama itu di dalam model.
    static String isiLubang(String nama) {
        Object nilai = model.get(nama);
        return nilai == null ? "" : String.valueOf(nilai);
    }

    static String bacaFlash(String nama) {
        Object nilai = flash.remove(nama);
        return nilai == null ? "" : String.valueOf(nilai);
    }

    public static void main(String[] args) {
        model.put("item", "APAR 3kg");
        model.put("history", "3 baris mutasi");
        flash.put("success", "Mutasi tersimpan.");

        System.out.println("halaman     : " + resolusiView("items/detail"));
        System.out.println("${item}     : [" + isiLubang("item") + "]");
        System.out.println("${history}  : [" + isiLubang("history") + "]");
        System.out.println("${histori}  : [" + isiLubang("histori") + "]");

        System.out.println("sesudah redirect: [" + bacaFlash("success") + "]");
        System.out.println("lalu di-refresh : [" + bacaFlash("success") + "]");
    }
}""",
            },
            {
                "body": [
                    "Perhatikan baris ${histori} di keluarannya: kurung sikunya kosong, dan",
                    "tidak ada yang mengeluh. Itu persis yang terjadi di halaman sungguhan.",
                    "",
                    "REDIRECT DAN PESAN YANG BERTAHAN SATU KALI",
                    "",
                    "Dua baris terakhir program tadi menjelaskan bagian yang tersisa. Materi",
                    "sebelumnya menyuruh setiap POST diakhiri redirect supaya refresh tidak",
                    "mengirim formulir dua kali:",
                    "",
                    "  return \"redirect:/items/\" + id;",
                    "",
                    "Awalan \"redirect:\" mencegat view resolver: Spring tidak mencari JSP mana",
                    "pun, ia membalas \"pindah ke alamat ini\" dan browser meminta ulang lewat",
                    "GET. Tapi itu permintaan BARU. Model yang tadi kamu isi sudah dibuang",
                    "bersama permintaan yang lama.",
                    "",
                    "Di situlah pesan \"Mutasi tersimpan.\" hilang kalau ditaruh di Model biasa.",
                    "Pasangan wajibnya:",
                    "",
                    "  RedirectAttributes ra                         parameter di method POST",
                    "  ra.addFlashAttribute(\"success\", \"...\")        titipkan pesannya",
                    "",
                    "Flash attribute dititipkan di sesi, dipindahkan ke model permintaan",
                    "berikutnya, lalu langsung dibuang. Halaman tujuan bisa membacanya sebagai",
                    "${success}; sekali pengguna me-refresh halaman itu, pesannya sudah tidak",
                    "ada lagi - dan memang begitu yang diinginkan.",
                    "",
                    "Jangan tertukar dengan addAttribute() milik RedirectAttributes: yang itu",
                    "menempel di alamat sebagai ?success=..., sehingga pesannya terpampang di URL",
                    "dan tidak hilang walau halamannya di-refresh berkali-kali.",
                    "",
                    "NAMA POLANYA: MVC",
                    "",
                    "Model - View - Controller. Seluruh modul ini sebenarnya sedang mengajarkan",
                    "pola itu, dan sekarang ketiga bagiannya sudah kamu lihat utuh:",
                    "",
                    "  Model       data yang dikirim: entitas, daftar, dan kotak addAttribute",
                    "  View        JSP yang mencetaknya jadi HTML",
                    "  Controller  yang memilih siapa dipanggil dan halaman mana ditampilkan",
                    "",
                    "Namanya menempel di banyak tempat yang sudah kamu lewati: spring-webmvc",
                    "di pom.xml, dan folder src/main/webapp di tiap proyek. Sekarang keduanya",
                    "tidak lagi cuma nama.",
                ],
            },
        ],
    },
    {
        "title": "12. DTO dan Validasi Masukan",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menunjukkan bagaimana isi permintaan HTTP masuk menjadi",
                    "parameter Java. Pertanyaan berikutnya tidak boleh dilewati: apakah isinya",
                    "masuk akal?",
                    "",
                    "DUA PEMERIKSAAN YANG SERING TERTUKAR",
                    "",
                    "  VALIDASI BENTUK   'apakah masukannya berbentuk benar?'",
                    "    wajib diisi, panjang maksimum, harus angka, format tanggal, surel.",
                    "    Untuk menjawabnya cukup melihat masukan itu sendiri.",
                    "",
                    "  ATURAN BISNIS     'apakah yang diminta boleh dilakukan?'",
                    "    stok tidak boleh negatif, permintaan harus masih PENDING, kode unik.",
                    "    Untuk menjawabnya kamu butuh data lain: isi database, keadaan saat ini.",
                    "",
                    "Patokannya satu kalimat: kalau untuk memutuskan kamu perlu membuka database,",
                    "itu aturan bisnis; kalau cukup melihat isi formulirnya, itu validasi bentuk.",
                    "",
                    "Keduanya tinggal di tempat berbeda, dan itu disengaja:",
                    "",
                    "  bentuk   diperiksa di controller, SEBELUM service dipanggil",
                    "  bisnis   diperiksa di service, ditolak dengan melempar AturanDilanggar",
                    "",
                    "Kenapa aturan bisnis tidak sekalian ditempel jadi anotasi di formulir? Karena",
                    "formulir bukan satu-satunya pintu. Impor CSV, endpoint REST, dan tugas",
                    "terjadwal tidak lewat formulir mana pun - kalau aturannya menempel di sana,",
                    "ketiganya lolos tanpa diperiksa. Alasannya persis sama dengan materi",
                    "Lapisan-lapisan Aplikasi Web: aturan ditulis sekali, di tempat yang dilewati",
                    "semua jalur.",
                    "",
                    "JANGAN PERNAH PERCAYA DATA DARI BROWSER",
                    "",
                    "Formulir HTML punya atribut required, dan JavaScript bisa memeriksa isian",
                    "sebelum dikirim. Keduanya BERJALAN DI KOMPUTER PENGGUNA. Artinya penggunalah",
                    "yang memegang kendali penuh atas keduanya:",
                    "",
                    "  - JavaScript-nya bisa dimatikan,",
                    "  - atribut required bisa dihapus lewat inspect element dalam lima detik,",
                    "  - atau browsernya dilewati sama sekali:",
                    "",
                    "      curl -X POST http://server/items -d \"kode=&nama=&stokMinimum=-99\"",
                    "",
                    "Server tidak punya cara membedakan permintaan itu dari permintaan browser",
                    "sungguhan. Yang sampai kepadanya cuma teks dengan bentuk yang sama.",
                    "",
                    "Jadi pemeriksaan di browser tetap berguna - pengguna tahu salahnya tanpa",
                    "menunggu perjalanan ke server - tapi ia KENYAMANAN, bukan pengamanan. Setiap",
                    "pemeriksaan di browser wajib punya kembaran di server, dan yang di server",
                    "itulah satu-satunya yang benar-benar berlaku.",
                ],
            },
            {
                "body": [
                    "OBJEK FORMULIR, ALIAS DTO",
                    "",
                    "Formulir 'tambah item' punya lima isian. Yang menampungnya BUKAN entitas Item,",
                    "melainkan kelas terpisah bernama ItemForm.",
                    "",
                    "Kelas semacam itu disebut DTO - Data Transfer Object. Isinya cuma data yang",
                    "sedang berpindah antar lapisan: field, getter, setter, tanpa perilaku.",
                    "Bentuknya mirip entitas (materi Entitas), tapi tugasnya beda - entitas mewakili",
                    "satu baris tabel, DTO mewakili satu percakapan.",
                    "",
                    "KENAPA TIDAK LANGSUNG PAKAI ENTITAS Item SAJA?",
                    "",
                    "Pertanyaan yang wajar; dua kelas berisi field mirip kelihatan mubazir. Tiga",
                    "alasan, dan ketiganya pernah menggigit orang sungguhan.",
                    "",
                    "1. ADA FIELD YANG TIDAK BOLEH DIISI PENGGUNA.",
                    "   Item punya id, stok, dan dibuatOleh. Kalau formulirnya diikat langsung ke",
                    "   Item, penyerang tinggal menambahkan field yang tidak ada di layar:",
                    "",
                    "     curl -X POST http://server/items -d \"nama=APAR&stok=9999&id=61\"",
                    "",
                    "   dan Spring dengan patuh memanggil setStok(9999) lalu setId(61). Pengikatan",
                    "   bekerja berdasarkan NAMA; ia tidak tahu mana yang kamu maksudkan untuk",
                    "   diisi pengguna. Kolom yang tidak ditampilkan tidak pernah otomatis menjadi",
                    "   kolom yang terlarang. Nama lubang ini: mass assignment.",
                    "",
                    "2. ENTITAS TERIKAT DATABASE.",
                    "   Item punya relasi ke Kategori yang diambil MALAS (materi Hubungan Antar",
                    "   Entitas). Melempar entitas mentah ke tampilan atau ke JSON membuat relasi",
                    "   itu tersentuh di luar sesi - LazyInitializationException - sekaligus",
                    "   membocorkan struktur tabelmu ke luar: nama kolom, id internal, dan field",
                    "   seperti passwordHash yang kebetulan ikut terbawa.",
                    "",
                    "3. BENTUK FORMULIR MEMANG TIDAK SAMA DENGAN BENTUK TABEL.",
                    "   Tanggal di formulir cuma String \"26-08-2026\"; di entitas ia LocalDate.",
                    "   Formulir ganti sandi punya dua isian (baru dan ulangi) yang tidak punya",
                    "   satu pun kolom padanan.",
                    "",
                    "ANOTASI BEAN VALIDATION",
                    "",
                    "Aturan bentuknya ditulis sebagai anotasi di atas field DTO, bukan sebagai if",
                    "berderet di controller. Yang paling sering dipakai:",
                    "",
                    "  @NotNull                     tidak boleh null",
                    "  @NotBlank                    String: bukan null, bukan kosong, bukan spasi",
                    "  @NotEmpty                    bukan null dan panjangnya bukan nol",
                    "  @Size(min=..., max=...)      panjang String atau jumlah isi daftar",
                    "  @Min / @Max                  batas nilai angka",
                    "  @Positive / @PositiveOrZero  harus di atas nol / nol ke atas",
                    "  @Email                       bentuk alamat surel",
                    "  @Pattern(regexp=...)         harus cocok dengan pola",
                    "  @Past / @Future              tanggal harus sudah lewat / belum datang",
                    "",
                    "Semuanya menerima message=\"...\", dan SELALU isi. Pesan bawaannya berbahasa",
                    "Inggris dan berbunyi 'must not be blank' - benar secara teknis, tidak berguna",
                    "bagi petugas gudang yang sedang menatap layar.",
                    "",
                    "DUA JEBAKAN YANG MENJELASKAN PILIHAN TIPE DI KODE BAWAH",
                    "",
                    "Pertama, isian teks yang dikosongkan pengguna TIDAK mengirim null; ia mengirim",
                    "String kosong \"\". Karena itu @NotNull di kolom teks selalu lolos dan tidak",
                    "menjaga apa pun. Untuk teks wajib isi, yang benar @NotBlank.",
                    "",
                    "Kedua, untuk angka pakai Integer, bukan int. Isian angka yang dikosongkan juga",
                    "datang sebagai \"\", dan \"\" tidak bisa jadi int. Dengan Integer hasilnya null,",
                    "dan @NotNull-mu sempat berbicara: 'Stok minimum wajib diisi.' Dengan int,",
                    "pengikatannya gagal lebih dulu dan yang muncul pesan teknis Spring.",
                    "",
                    "Dua hal terakhir sebelum kodenya. Anotasi ini butuh implementasinya ada di",
                    "pom.xml (Hibernate Validator, atau spring-boot-starter-validation) - tanpa itu",
                    "seluruh anotasimu cuma hiasan yang tidak pernah dijalankan. Dan paketnya",
                    "pernah berganti nama: javax.validation.* di proyek lama, jakarta.validation.*",
                    "sejak Jakarta EE 9. Isinya sama, import-nya beda, dan mencampur keduanya",
                    "adalah sebab umum 'anotasinya ada tapi tidak jalan'.",
                ],
                "code": """public class ItemForm {

    @NotBlank(message = "Kode wajib diisi.")
    @Size(max = 20, message = "Kode maksimal 20 karakter.")
    @Pattern(regexp = "[A-Z]{3}-[0-9]{3}",
             message = "Format kode: 3 huruf besar, tanda hubung, 3 angka (APR-003).")
    private String kode;

    @NotBlank(message = "Nama wajib diisi.")
    @Size(max = 50, message = "Nama maksimal 50 karakter.")
    private String nama;

    @NotBlank(message = "Satuan wajib dipilih.")
    private String satuan;

    @NotNull(message = "Stok minimum wajib diisi.")
    @Min(value = 0, message = "Stok minimum tidak boleh negatif.")
    private Integer stokMinimum;      // Integer, bukan int - lihat jebakan kedua

    @NotNull(message = "Kategori wajib dipilih.")
    private Long kategoriId;          // cukup id-nya, bukan objek Kategori

    // Tidak ada field id, stok, maupun dibuatOleh di sini. Itu disengaja:
    // yang tidak punya setter tidak akan pernah bisa diisi dari luar.

    public String getKode() { return kode; }
    public void setKode(String kode) { this.kode = kode; }

    public Integer getStokMinimum() { return stokMinimum; }
    public void setStokMinimum(Integer stokMinimum) { this.stokMinimum = stokMinimum; }

    // getter dan setter serupa untuk nama, satuan, dan kategoriId
}""",
            },
            {
                "body": [
                    "@ModelAttribute: DARI ISI FORMULIR JADI OBJEK JAVA",
                    "",
                    "@RequestParam mengambil satu nilai. Untuk formulir berisi lima isian, menulis",
                    "lima @RequestParam melelahkan - dan tidak ada tempat menempelkan aturannya.",
                    "",
                    "@ModelAttribute mengambil semuanya sekaligus. Cara kerjanya sederhana, dan",
                    "justru kesederhanaan itu yang membuatnya gampang salah: untuk tiap field yang",
                    "datang, Spring mencari SETTER yang namanya cocok.",
                    "",
                    "  <input name=\"kode\">          ->  form.setKode(...)",
                    "  <input name=\"stokMinimum\">   ->  form.setStokMinimum(...)",
                    "",
                    "Cocok berarti cocok huruf per huruf. Kalau di HTML tertulis name=\"stok_minimum\"",
                    "atau name=\"namaItem\", tidak ada setter yang cocok, TIDAK ADA error, dan field",
                    "itu tinggal null. Pengguna lalu melihat 'Nama wajib diisi' padahal ia",
                    "jelas-jelas mengetik namanya. Program di bagian berikutnya memperagakannya.",
                    "",
                    "Objek itu sekaligus masuk ke Model dengan nama yang sama, jadi halaman",
                    "formulirnya bisa membaca ${itemForm.nama} tanpa kamu memanggil addAttribute.",
                    "",
                    "@Valid DAN BindingResult",
                    "",
                    "Anotasi di DTO tidak melakukan apa-apa sendirian - ia cuma label, dan baru",
                    "dibaca kalau parameternya ditandai @Valid:",
                    "",
                    "  public String simpan(@Valid @ModelAttribute(\"itemForm\") ItemForm form,",
                    "                       BindingResult result, ...)",
                    "",
                    "@Valid berarti 'periksa objek ini'. BindingResult adalah tempat hasilnya",
                    "ditulis: daftar kesalahan, masing-masing menempel pada NAMA FIELD-nya.",
                    "",
                    "TIGA JEBAKAN, DAN KETIGANYA SERING",
                    "",
                    "1. BindingResult WAJIB PERSIS SESUDAH objek yang divalidasi.",
                    "   Menyelipkan Model di antara keduanya membuat aplikasi menolak menyala:",
                    "   'An Errors/BindingResult argument is expected to be declared immediately",
                    "   after the model attribute'. Aturan ini ada karena satu method boleh punya",
                    "   lebih dari satu objek formulir, dan Spring harus tahu hasil pemeriksaan ini",
                    "   milik yang mana. Urutan parameternyalah yang menentukan.",
                    "",
                    "2. LUPA MENULIS BindingResult SAMA SEKALI mengubah perilakunya total.",
                    "   Tanpa penampung hasil, Spring tidak punya tempat menaruh kesalahannya, jadi",
                    "   ia melempar exception dan pengguna menerima halaman error. Formulirnya tidak",
                    "   muncul lagi dan semua yang sudah diketik hilang. Satu parameter itu yang",
                    "   membedakan 'halaman error' dari 'formulir dengan pesan merah'.",
                    "",
                    "3. SESUDAH hasErrors(), JANGAN REDIRECT.",
                    "   Materi Controller mengajarkan setiap POST diakhiri redirect. Itu berlaku",
                    "   untuk POST yang BERHASIL. Untuk yang gagal validasi, kamu justru",
                    "   mengembalikan nama halaman formulirnya langsung - return \"items/form\" -",
                    "   karena redirect membuang permintaan ini beserta BindingResult dan seluruh",
                    "   isian yang tadi diketik. Yang tersisa formulir kosong tanpa keterangan.",
                    "",
                    "Satu catatan tentang kode di bawah: daftarKategori diisi ulang di setiap jalur",
                    "yang menampilkan formulir. Itu memang perlu, karena model dibuang bersama",
                    "permintaan sebelumnya. Kalau terasa berulang, obatnya sebuah method beranotasi",
                    "@ModelAttribute tanpa alamat, yang dijalankan sebelum SETIAP method di kelas",
                    "itu.",
                ],
                "code": """@Controller
@RequestMapping("/items")
public class ItemController {

    private final ItemService itemService;
    private final KategoriService kategoriService;

    // Formulir kosong. Objeknya HARUS sudah ada di model, kalau tidak
    // <form:form modelAttribute="itemForm"> di JSP gagal menemukannya.
    @GetMapping("/new")
    public String formTambah(Model model) {
        model.addAttribute("itemForm", new ItemForm());
        model.addAttribute("daftarKategori", kategoriService.cariSemua());
        return "items/form";
    }

    @PostMapping
    public String simpan(@Valid @ModelAttribute("itemForm") ItemForm form,
                         BindingResult result,       // WAJIB tepat sesudah form
                         Model model,
                         RedirectAttributes ra) {

        if (result.hasErrors()) {                    // validasi BENTUK gagal
            model.addAttribute("daftarKategori", kategoriService.cariSemua());
            return "items/form";                     // tampilkan ulang, JANGAN redirect
        }

        try {
            Item item = itemService.buat(form);      // aturan BISNIS dinilai di sini
            ra.addFlashAttribute("success", "Item " + item.getKode() + " tersimpan.");
            return "redirect:/items/" + item.getId();

        } catch (KodeSudahDipakai e) {
            // Aturan bisnis yang gagal pun boleh ditempelkan ke field-nya, supaya
            // pesannya muncul di tempat yang sama dengan pesan @NotBlank tadi.
            result.rejectValue("kode", "duplikat", e.getMessage());
            model.addAttribute("daftarKategori", kategoriService.cariSemua());
            return "items/form";
        }
    }
}""",
            },
            {
                "body": [
                    "MENAMPILKAN KESALAHANNYA DI TEMPAT YANG BENAR",
                    "",
                    "Mengembalikan \"items/form\" saja belum cukup. Pengguna perlu tahu FIELD MANA",
                    "yang salah, bukan sekadar bahwa ada yang salah. Satu tulisan 'Terjadi",
                    "kesalahan' di atas formulir berisi delapan isian adalah cara menyuruh orang",
                    "menebak-nebak.",
                    "",
                    "Di JSP, taglib form milik Spring yang mengurusnya:",
                    "",
                    "  <form:form modelAttribute=\"itemForm\" method=\"post\" action=\"/items\">",
                    "    <form:input path=\"nama\" />",
                    "    <form:errors path=\"nama\" cssClass=\"galat\" />",
                    "    <form:select path=\"kategoriId\" items=\"${daftarKategori}\" />",
                    "    <form:errors path=\"*\" />",
                    "  </form:form>",
                    "",
                    "Dua hal penting di situ. Pertama, path=\"nama\" adalah nama FIELD di ItemForm,",
                    "dan nama itu pula yang dipakai anotasi tadi untuk menandai kesalahannya -",
                    "sehingga pesan @NotBlank milik field nama muncul persis di sebelah isian nama.",
                    "",
                    "Kedua, <form:input> mengisi ulang nilai yang tadi diketik, diambil dari objek",
                    "yang masih ada di model. Inilah yang membuat pengguna tidak perlu mengetik",
                    "ulang tujuh isian yang sudah benar hanya karena satu isian salah - dan inilah",
                    "yang hilang begitu kamu redirect.",
                    "",
                    "Program di bawah menirukan ketiga langkahnya dengan Java polos tanpa Spring:",
                    "pengikatan berdasarkan nama setter, pemeriksaan yang mengumpulkan SEMUA",
                    "kesalahan sekaligus (bukan berhenti di yang pertama), lalu keputusan",
                    "tampilkan-ulang atau lanjut. Jalankan, dan perhatikan kasus ketiga.",
                ],
                "code": """import java.lang.reflect.Method;
import java.util.LinkedHashMap;
import java.util.Map;

public class ValidasiForm {

    /* Objek formulir. Semua field String, persis seperti yang datang dari HTTP. */
    public static class ItemForm {
        private String kode = "";
        private String nama = "";
        private String stokMinimum = "";

        public void setKode(String v)        { this.kode = v; }
        public void setNama(String v)        { this.nama = v; }
        public void setStokMinimum(String v) { this.stokMinimum = v; }

        public String getKode()        { return kode; }
        public String getNama()        { return nama; }
        public String getStokMinimum() { return stokMinimum; }
    }

    /* Peniru BindingResult: kesalahan disimpan PER NAMA FIELD, bukan satu pesan. */
    static class Hasil {
        Map<String, String> galat = new LinkedHashMap<>();
        void tolak(String field, String pesan) { galat.putIfAbsent(field, pesan); }
        boolean adaGalat() { return !galat.isEmpty(); }
    }

    /* Yang dikerjakan @ModelAttribute: cocokkan name di <input> dengan setter. */
    static ItemForm ikat(Map<String, String> formulir) throws Exception {
        ItemForm form = new ItemForm();
        for (Map.Entry<String, String> field : formulir.entrySet()) {
            String nama = field.getKey();
            String setter = "set" + Character.toUpperCase(nama.charAt(0)) + nama.substring(1);
            try {
                Method m = ItemForm.class.getMethod(setter, String.class);
                m.invoke(form, field.getValue());
            } catch (NoSuchMethodException e) {
                System.out.println("  diabaikan diam-diam: tidak ada " + setter + "()");
            }
        }
        return form;
    }

    /* Yang dikerjakan @NotBlank, @Size, @Min: semua dijalankan, tidak berhenti di awal. */
    static Hasil periksa(ItemForm form) {
        Hasil hasil = new Hasil();
        if (form.getKode().trim().isEmpty())
            hasil.tolak("kode", "Kode wajib diisi.");
        if (form.getNama().trim().isEmpty())
            hasil.tolak("nama", "Nama wajib diisi.");
        if (form.getNama().length() > 50)
            hasil.tolak("nama", "Nama maksimal 50 karakter.");
        try {
            if (Integer.parseInt(form.getStokMinimum().trim()) < 0)
                hasil.tolak("stokMinimum", "Stok minimum tidak boleh negatif.");
        } catch (NumberFormatException e) {
            hasil.tolak("stokMinimum", "Stok minimum harus berupa angka.");
        }
        return hasil;
    }

    static void tanganiPost(Map<String, String> formulir) throws Exception {
        System.out.println("POST /items " + formulir);
        ItemForm form = ikat(formulir);
        Hasil hasil = periksa(form);
        if (hasil.adaGalat()) {
            System.out.println("  hasErrors() -> tampilkan ulang items/form:");
            for (Map.Entry<String, String> g : hasil.galat.entrySet())
                System.out.println("    " + g.getKey() + " : " + g.getValue());
        } else {
            System.out.println("  bentuknya sah -> lanjut ke service");
        }
        System.out.println();
    }

    public static void main(String[] args) throws Exception {
        Map<String, String> lengkap = new LinkedHashMap<>();
        lengkap.put("kode", "APR-003");
        lengkap.put("nama", "APAR 3kg");
        lengkap.put("stokMinimum", "5");
        tanganiPost(lengkap);

        // Spasi doang: lolos kalau cuma dicek null, ditolak oleh @NotBlank.
        Map<String, String> kosong = new LinkedHashMap<>();
        kosong.put("kode", "   ");
        kosong.put("nama", "");
        kosong.put("stokMinimum", "dua");
        tanganiPost(kosong);

        // Di HTML-nya tertulis name="namaItem", padahal setter-nya setNama().
        Map<String, String> salahName = new LinkedHashMap<>();
        salahName.put("kode", "APR-004");
        salahName.put("namaItem", "APAR 6kg");
        salahName.put("stokMinimum", "-1");
        tanganiPost(salahName);
    }
}""",
            },
            {
                "body": [
                    "Perhatikan kasus ketiga di keluarannya. Penggunanya mengisi nama dengan benar,",
                    "servernya tidak mengeluh apa pun, dan yang muncul di layar tetap 'Nama wajib",
                    "diisi.' Satu huruf salah di atribut name sebuah <input> sudah cukup. Kalau",
                    "suatu hari sebuah field terasa 'tidak mau masuk', periksa nama itu lebih dulu.",
                    "",
                    "PEMETAAN: DARI ItemForm KE Item",
                    "",
                    "Setelah lolos, isi DTO harus dipindahkan ke entitas. Bagian ini sering terasa",
                    "pekerjaan sia-sia, padahal justru di sinilah perlindungannya:",
                    "",
                    "  Item item = new Item(form.getKode(), form.getNama(),",
                    "                       form.getSatuan(), form.getStokMinimum());",
                    "  item.setKategori(kategoriDao.cariById(form.getKategoriId()));",
                    "  // stok, id, dan dibuatOleh sengaja TIDAK diambil dari formulir",
                    "",
                    "Baris komentar terakhir itu seluruh alasan lapisan ini ada. Yang tidak disebut",
                    "di pemetaan tidak akan pernah bisa diisi dari luar - bukan karena kamu ingat",
                    "melarangnya, tapi karena tidak ada jalannya. Perlindungan yang bekerja karena",
                    "bentuk kodenya jauh lebih awet daripada yang bergantung pada kedisiplinan.",
                    "",
                    "Tempatnya di sebuah kelas ItemMapper tersendiri, atau di dalam method",
                    "itemService.buat(form). Yang penting ia tidak berserakan di controller.",
                    "",
                    "Arah sebaliknya juga dipakai: halaman ubah memetakan Item MENJADI ItemForm",
                    "supaya isiannya sudah terisi, dan endpoint yang membalas JSON memetakan Item",
                    "jadi ItemResponse yang cuma berisi field yang boleh dilihat pemanggil.",
                    "",
                    "MAPSTRUCT: PEMETAAN YANG DITULISKAN COMPILER",
                    "",
                    "Menulis pemetaan tangan untuk dua puluh DTO memang membosankan. MapStruct",
                    "memangkasnya - kamu cukup mendeklarasikan antarmuka:",
                    "",
                    "  @Mapper",
                    "  public interface ItemMapper {",
                    "      Item toEntity(ItemForm form);",
                    "      ItemForm toForm(Item item);",
                    "  }",
                    "",
                    "dan MapStruct MEMBUATKAN kelas implementasinya saat kompilasi: kode Java biasa",
                    "yang bisa kamu buka dan baca di target/generated-sources. Salah nama field",
                    "ketahuan sebagai error kompilasi, bukan sebagai nilai null di produksi. Dan",
                    "perlindungan tadi tetap berlaku - MapStruct hanya bisa menyalin field yang ADA",
                    "di ItemForm, jadi selama stok dan id tidak kamu taruh di DTO, tidak ada yang",
                    "bisa menyalinnya.",
                    "",
                    "Bandingkan dengan jalan pintas yang sering dipakai orang:",
                    "",
                    "  BeanUtils.copyProperties(form, item);",
                    "",
                    "Ia menyalin field yang namanya sama, saat aplikasi jalan, tanpa memeriksa apa",
                    "pun waktu kompilasi. Salah nama berarti nilainya diam-diam tidak tersalin -",
                    "jenis bug yang sama persis dengan name=\"namaItem\" tadi, cuma pindah lapisan.",
                    "",
                    "RINGKASNYA SATU PERJALANAN",
                    "",
                    "  1. Browser mengirim teks lewat POST.",
                    "  2. @ModelAttribute mengikatnya ke ItemForm lewat setter yang namanya cocok.",
                    "  3. @Valid menjalankan anotasi di ItemForm; hasilnya masuk ke BindingResult.",
                    "  4. hasErrors() -> kembalikan halaman formulirnya, dengan pesan per field.",
                    "  5. Bersih -> petakan ke entitas, panggil service, biar aturan BISNIS menilai.",
                    "  6. Berhasil -> redirect, pesan suksesnya dititipkan lewat flash attribute.",
                    "",
                    "Langkah 4 dan 5 sama-sama penolakan, tapi jenisnya berbeda - dan bedanya",
                    "terbaca dari kode status yang dibalas server. Itu bahasan materi berikutnya.",
                ],
            },
        ],
    },
    {
        "title": "13. Kode Status HTTP dan Penanganan Error Terpusat",
        "sections": [
            {
                "body": [
                    "Materi Controller membedah apa yang MASUK ke aplikasi. Sekarang arah",
                    "sebaliknya: apa yang dikirim server balik ke browser.",
                    "",
                    "Setiap permintaan HTTP selalu dijawab. Selalu - tidak ada permintaan yang",
                    "dibiarkan menggantung, bahkan yang gagal total sekalipun. Dan bentuk",
                    "jawabannya selalu sama:",
                    "",
                    "ISI SEBUAH BALASAN HTTP",
                    "",
                    "  BARIS STATUS   HTTP/1.1 404 Not Found",
                    "                 versi, lalu ANGKA, lalu kalimat pendek",
                    "  HEADER         Content-Type, Content-Length, Location, Set-Cookie",
                    "  BARIS KOSONG   pemisah antara kepala dan isi",
                    "  BADAN          isinya: HTML halaman, JSON, atau memang kosong",
                    "",
                    "Kalimat 'Not Found' itu untuk manusia. Yang dibaca program adalah",
                    "ANGKANYA. Menggantinya jadi 'Tidak Ketemu' tidak mengubah apa pun;",
                    "mengganti angkanya mengubah segalanya.",
                    "",
                    "LIMA KELUARGA, DIKENALI DARI ANGKA PERTAMANYA",
                    "",
                    "  1xx   masih berlangsung. Praktis tidak pernah kamu tulis sendiri.",
                    "  2xx   BERHASIL.",
                    "  3xx   belum selesai: ambil dulu alamat lain.",
                    "  4xx   permintaannya yang salah - kesalahan ada di SISI PENGIRIM.",
                    "  5xx   permintaannya wajar, SERVER yang gagal memenuhinya.",
                    "",
                    "GARIS ANTARA 4xx DAN 5xx ITU PEMBAGIAN TANGGUNG JAWAB",
                    "",
                    "Ia menjawab satu pertanyaan: siapa yang harus memperbaiki?",
                    "",
                    "  4xx   pengirimnya. Mengulang permintaan yang sama persis akan gagal",
                    "        lagi; datanya dulu yang harus dibetulkan.",
                    "  5xx   kamu, yang menulis servernya. Pengguna tidak melakukan kesalahan",
                    "        apa pun dan tidak punya cara memperbaikinya sendiri.",
                    "",
                    "Pembagian itu bukan filosofi. Alat pemantau menghitung 5xx dan",
                    "membangunkan orang tengah malam; 4xx tidak membangunkan siapa-siapa,",
                    "karena wajar ada terus-menerus. Menaruh kegagalan di keluarga yang keliru",
                    "berarti salah satu dari dua hal: kamu dibangunkan gara-gara pengguna",
                    "salah ketik, atau kerusakan sungguhan mengendap berbulan-bulan tanpa",
                    "seorang pun tahu.",
                    "",
                    "JEBAKAN PALING SERING: GAGAL, TAPI MEMBALAS 200",
                    "",
                    "Bentuknya begini, dan kelihatan sangat masuk akal:",
                    "",
                    "  } catch (Exception e) {",
                    "      model.addAttribute(\"error\", e.getMessage());",
                    "      return \"error\";     // halaman 'terjadi kesalahan' -- statusnya 200",
                    "  }",
                    "",
                    "Di layar semuanya benar: pengguna membaca pesan kesalahan. Tapi semua yang",
                    "membaca ANGKANYA - pemantau, access log, JavaScript di halaman, aplikasi",
                    "lain yang memanggilmu - menerima 200 dan menyimpulkan permintaannya",
                    "berhasil.",
                    "",
                    "Kerusakan yang dibalas 200 tidak pernah muncul di grafik mana pun.",
                ],
            },
            {
                "heading": "Melihatnya sendiri: curl -i, tab Network, dan access log",
                "body": [
                    "Kode status bukan barang abstrak. Ada tiga cara melihatnya, dan tak satu",
                    "pun butuh memasang sesuatu:",
                    "",
                    "  Tab Network   Tekan F12 di browser, pilih Network, lalu muat ulang",
                    "                halaman. Ada kolom Status. Klik satu barisnya untuk",
                    "                melihat header lengkap permintaan dan balasannya.",
                    "",
                    "  curl -i       Huruf i berarti 'ikutkan headernya'. Tanpa -i kamu cuma",
                    "                melihat badannya - dan justru angkanya yang hilang.",
                    "                curl -I (huruf besar) mengambil kepalanya saja.",
                    "",
                    "  Access log    Tomcat menulis satu baris untuk SETIAP permintaan di",
                    "                logs/localhost_access_log.txt: waktu, method, path, kode",
                    "                status, dan ukuran balasan.",
                    "",
                    "Yang terakhir itu menyambung ke langkah 'Verifikasi: baca log' di materi",
                    "Deploy. Sesudah menukar .war, yang dicari bukan cuma 'halamannya muncul',",
                    "tapi juga: adakah 5xx di access log yang tadi belum ada?",
                    "",
                    "Berikut tiga balasan B-iFAMS apa adanya.",
                ],
                "code": """$ curl -i http://localhost:8080/items/61

HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
Content-Length: 8241

<!DOCTYPE html>
<html> ... isi halaman detail item ...


$ curl -i -X POST http://localhost:8080/items/61/stock -d "type=OUT&qty=5"

HTTP/1.1 302 Found
Location: http://localhost:8080/items/61
Content-Length: 0

(badannya memang kosong -- browser disuruh meminta alamat di Location.
 Inilah wujud sebenarnya dari pola POST-Redirect-GET.)


$ curl -i http://localhost:8080/items/9999

HTTP/1.1 404 Not Found
Content-Type: text/html;charset=UTF-8

<!DOCTYPE html>
<html> ... halaman "item tidak ditemukan" ...


Dan inilah jejak yang ketiganya tinggalkan di access log Tomcat
(zona waktunya dibuang di sini supaya muat sebaris):

10.10.1.42 - budi [26/Aug/2026:09:14:02] "GET /items/61 HTTP/1.1" 200 8241
10.10.1.42 - budi [26/Aug/2026:09:14:20] "POST /items/61/stock HTTP/1.1" 302 0
10.10.1.42 - andi [26/Aug/2026:09:15:07] "GET /items/9999 HTTP/1.1" 404 1180

Kolom sesudah alamat IP itu nama pengguna yang sedang login. Kolom itulah
yang membuat deretan 401 dan 403 bisa ditelusuri sampai ke orangnya.""",
            },
            {
                "body": [
                    "ANGKA YANG BENAR-BENAR AKAN KAMU TEMUI",
                    "",
                    "Daftar resminya panjang. Yang ini sudah cukup untuk bertahun-tahun,",
                    "lengkap dengan penyebabnya di B-iFAMS:",
                    "",
                    "  200 OK           GET /items berhasil, halamannya dikirim.",
                    "  201 Created      sesuatu yang baru berhasil dibuat, dan alamat barunya",
                    "                   disebut di header Location. Lazim di API.",
                    "  204 No Content   berhasil, dan memang tidak ada yang perlu dikirim",
                    "                   balik. Biasanya jawaban DELETE.",
                    "  302 Found        'ambil alamat lain dulu'. Inilah balasan setiap",
                    "                   redirect, termasuk sesudah POST /items/61/stock.",
                    "  400 Bad Request  permintaannya tidak bisa diterima apa adanya: qty=dua",
                    "                   padahal parameternya int, atau formulirnya gagal",
                    "                   validasi seperti di materi DTO.",
                    "  401 Unauthorized kamu belum login, atau sesimu sudah kedaluwarsa.",
                    "  403 Forbidden    kamu sudah login, tapi perannya tidak berhak.",
                    "  404 Not Found    /items/9999 tidak ada di database, ATAU alamat itu",
                    "                   memang tidak pernah dibuat.",
                    "  405 Method Not Allowed   alamatnya benar, methodnya salah:",
                    "                   /items/1/stock cuma melayani POST, dan kamu",
                    "                   membukanya lewat GET dari kolom alamat.",
                    "  409 Conflict     bentrok dengan keadaan sekarang: kode item sudah",
                    "                   dipakai item lain, atau permintaan sudah disetujui",
                    "                   orang lain sedetik sebelumnya.",
                    "  500 Internal Server Error   ada exception yang tidak tertangkap.",
                    "",
                    "404 PUNYA DUA ARTI YANG SANGAT BERBEDA",
                    "",
                    "  Alamatnya tidak dikenal        Spring tidak punya method untuk pola",
                    "                                 itu. Salah ketik di @GetMapping, atau",
                    "                                 aplikasinya belum ter-deploy.",
                    "  Alamat dikenal, datanya tidak  Controller jalan, service dipanggil,",
                    "                                 dan item 9999 memang tidak ada.",
                    "",
                    "Membedakannya menghemat waktu: yang pertama biasanya tidak meninggalkan",
                    "jejak apa pun di log aplikasi, yang kedua meninggalkan. Kalau SELURUH",
                    "alamat aplikasimu 404, berhentilah mencari di database - carilah di",
                    "deploy-nya.",
                    "",
                    "DUA PENOLAKAN YANG SAMA-SAMA SALAH DI SISI PENGIRIM",
                    "",
                    "Materi DTO memisahkan dua jenis penolakan: bentuk masukan yang tidak sah",
                    "(kosong, kepanjangan, bukan angka) dan aturan bisnis yang dilanggar (stok",
                    "tidak cukup). Keduanya 4xx - pengirimnya yang harus membetulkan. Yang",
                    "berbeda adalah cara membalasnya:",
                    "",
                    "  Formulir HTML  halaman formulirnya dikirim ulang lengkap dengan pesan",
                    "                 per field. Karena yang di-return nama halaman, statusnya",
                    "                 200 - dan untuk halaman yang dibaca manusia itu masih",
                    "                 wajar, karena pesannya memang terpampang di layar.",
                    "  API JSON       penolakan yang sama WAJIB 400. Pemanggilnya tidak punya",
                    "                 mata; angka itulah satu-satunya cara ia tahu datanya",
                    "                 tidak tersimpan.",
                    "",
                    "Sedangkan bentrok dengan keadaan sekarang - kode item sudah dipakai,",
                    "permintaan sudah disetujui orang lain - lebih tepat 409 daripada 400:",
                    "masukannya tidak salah bentuk, dunianya yang keburu berubah.",
                    "",
                    "401 VERSUS 403 - BEDANYA TIDAK SEPELE",
                    "",
                    "  401  'aku tidak tahu kamu siapa'          -> obatnya: login.",
                    "  403  'aku tahu persis kamu siapa, dan kamu tetap tidak boleh'",
                    "       -> login ulang tidak menolong sama sekali; perannya yang kurang.",
                    "",
                    "Bedanya paling terasa saat membaca log. Deretan 401 berarti banyak orang",
                    "datang tanpa sesi yang sah - bisa jadi umur sesinya kependekan dan orang",
                    "terlempar keluar di tengah kerja. Deretan 403 dari SATU akun berarti hal",
                    "yang lain sama sekali: seseorang mengetuk pintu yang bukan haknya, atau",
                    "perannya salah dipasang. Dua penyakit berbeda, dua obat berbeda.",
                    "",
                    "Ini juga yang membuat daftar pembuktian di materi Keamanan bisa",
                    "dipercaya. Di sana akun REQUESTER memanggil /items/new dan hasilnya harus",
                    "403. Kalau yang muncul justru 401, pengujian itu tidak membuktikan apa-apa",
                    "soal hak akses - yang barusan terbukti cuma bahwa kamu belum login.",
                    "",
                    "SIAPA YANG MENENTUKAN ANGKANYA",
                    "",
                    "Sampai hari ini kamu belum pernah menulis satu angka pun, dan halamanmu",
                    "tetap berjalan. Itu karena ada tiga jalur, dan yang pertama bekerja",
                    "diam-diam.",
                    "",
                    "1. BAWAAN. Method controller selesai tanpa melempar apa pun -> 200.",
                    "   Yang di-return berawalan \"redirect:\" -> 302 plus header Location.",
                    "   Exception lolos keluar tanpa ada yang menanganinya -> 500.",
                    "",
                    "2. @ResponseStatus DI KELAS EXCEPTION-NYA. Ditempel sekali di",
                    "   deklarasinya, lalu berlaku di semua controller yang melemparnya:",
                    "",
                    "     @ResponseStatus(HttpStatus.NOT_FOUND)",
                    "     public class DataTidakDitemukan extends RuntimeException { }",
                    "",
                    "3. ResponseEntity, yang membungkus status + header + badan sekaligus",
                    "   sebagai nilai kembalian:",
                    "",
                    "     return ResponseEntity.status(HttpStatus.CONFLICT).body(pesan);",
                    "",
                    "   Bentuk ini dipakai saat yang dibalas DATA, bukan halaman - dan",
                    "   dibahas tuntas di materi REST yang membalas JSON.",
                ],
            },
            {
                "body": [
                    "MASALAH TRY/CATCH DI SETIAP CONTROLLER",
                    "",
                    "Sampai sini penanganan error di modul ini selalu berbentuk sama: try/catch",
                    "di dalam method controller, lalu pesannya dititipkan ke flash attribute.",
                    "",
                    "Untuk satu method itu benar dan enak dibaca. Sekarang hitung akibatnya di",
                    "aplikasi berisi 6 controller dan puluhan method:",
                    "",
                    "  - Blok yang isinya sama persis disalin puluhan kali.",
                    "  - Aturan 'nama pesannya error' ikut ditulis puluhan kali. Suatu hari",
                    "    satu ditulis \"errors\", dan halamannya diam tanpa pesan apa pun.",
                    "  - Ada jenis kegagalan baru? Kamu harus ingat menambahkannya di semua",
                    "    tempat, dan tidak ada yang mengingatkan kalau satu terlewat.",
                    "",
                    "Dan yang paling mahal: SATU method yang lupa dibungkus tidak menghasilkan",
                    "pesan apa pun. Exception-nya naik terus sampai keluar dari aplikasi, dan",
                    "yang dilihat pengguna adalah halaman putih berisi stack trace - nama",
                    "kelasmu, nama tabelmu, kadang potongan SQL - terpampang di layar orang",
                    "yang tidak seharusnya melihat isi dapurmu. Statusnya memang 500, tapi 500",
                    "yang bocor.",
                    "",
                    "SATU KELAS UNTUK SEMUA CONTROLLER",
                    "",
                    "Karena itu di kode nyata try/catch tadi MENGHILANG dari controller dan",
                    "pindah ke satu kelas tersendiri. Siapkan dirimu, karena inilah yang paling",
                    "membingungkan saat pertama kali membaca repo orang: kamu mencari 'di mana",
                    "exception ini ditangkap?' dan tidak menemukan apa pun di controller.",
                    "Memang tidak ada. Yang menangkapnya duduk di kelas lain, dan tidak ada",
                    "satu baris pun yang memanggil kelas itu.",
                    "",
                    "  @ControllerAdvice       kelas ini berlaku untuk SEMUA controller",
                    "  @RestControllerAdvice   sama, tapi balasannya JSON, bukan nama halaman",
                    "  @ExceptionHandler(AturanDilanggar.class)",
                    "                          method ini dipanggil kalau exception itu lolos",
                    "                          dari controller mana pun",
                    "",
                    "Pemanggilannya tidak terlihat di kode, persis seperti anotasi lain: Spring",
                    "membaca labelnya saat aplikasi menyala, lalu memasang kelas itu di",
                    "belakang setiap controller. Kelas ini juga sebuah bean, jadi service dan",
                    "logger di dalamnya terisi dengan cara yang sama seperti di controller.",
                    "",
                    "Kalau ada dua handler yang sama-sama cocok, yang dipilih adalah tipenya",
                    "yang PALING DEKAT. Jadi handler untuk Exception tidak menelan semuanya -",
                    "ia berfungsi sebagai jaring terakhir bagi yang tidak terduga.",
                ],
                "code": """@ControllerAdvice
public class PenanganGalatGlobal {

    private static final Logger log =
            LoggerFactory.getLogger(PenanganGalatGlobal.class);

    // Aturan bisnis dilanggar -> 400. Pesannya AMAN dibaca pengguna,
    // karena kita sendiri yang menulisnya di service.
    @ExceptionHandler(AturanDilanggar.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public String aturanDilanggar(AturanDilanggar e, Model model) {
        model.addAttribute("pesan", e.getMessage());
        return "error/400";
    }

    // Barangnya memang tidak ada -> 404.
    @ExceptionHandler(DataTidakDitemukan.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public String tidakDitemukan(DataTidakDitemukan e, Model model) {
        model.addAttribute("pesan", e.getMessage());
        return "error/404";
    }

    // Jaring terakhir: apa pun yang tidak terduga -> 500.
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public String takTerduga(Exception e, Model model) {
        log.error("Permintaan gagal", e);      // jejak lengkap ke log
        model.addAttribute("pesan",
                "Terjadi kesalahan. Catat waktunya, lalu hubungi petugas.");
        return "error/500";                    // bukan stack trace ke layar
    }
}""",
            },
            {
                "body": [
                    "PETA YANG PANTAS KAMU HAFAL",
                    "",
                    "  AturanDilanggar     -> 400   salah di sisi pengirim; pesannya boleh",
                    "                               dibaca pengguna apa adanya",
                    "  DataTidakDitemukan  -> 404   barangnya memang tidak ada",
                    "  tidak berhak        -> 403   diurus lapisan keamanan, bukan advice ini",
                    "  sisanya             -> 500   bug. Pesan aslinya ke log, bukan ke layar.",
                    "",
                    "Baris terakhir itu yang membedakan aplikasi yang layak dipakai orang.",
                    "Pengguna menerima kalimat yang bisa ia tindak lanjuti, sementara jejak",
                    "lengkapnya - beserta stack trace - tersimpan di log untukmu. Cara menulis",
                    "log yang benar dibahas di materi Log.",
                    "",
                    "Bagian yang paling sulit dipercaya dari @ControllerAdvice adalah",
                    "'dipanggil tanpa ada yang memanggil'. Program berikut membongkarnya",
                    "dengan Java polos, tanpa Spring sama sekali: sebuah controller yang cuma",
                    "melempar, sebuah penangan terpusat, dan sebuah pembungkus yang menirukan",
                    "pekerjaan Spring.",
                    "",
                    "Jalankan, lalu perhatikan tiga hal. Controller-nya benar-benar tidak",
                    "punya try/catch. Keempat permintaan berakhir di empat angka yang berbeda.",
                    "Dan pada kasus 500, yang masuk ke log berbeda dari yang dilihat pengguna.",
                ],
                "code": """import java.util.LinkedHashMap;
import java.util.Map;

public class PenanganGalat {

    // Dua exception buatan sendiri. Yang baru di sini: masing-masing
    // punya satu kode status yang pantas untuknya.
    static class DataTidakDitemukan extends RuntimeException {
        DataTidakDitemukan(String pesan) { super(pesan); }
    }
    static class AturanDilanggar extends RuntimeException {
        AturanDilanggar(String pesan) { super(pesan); }
    }

    static Map<Long, Integer> stok = new LinkedHashMap<>();
    static Map<Long, String> nama = new LinkedHashMap<>();

    // CONTROLLER. Perhatikan: TIDAK ADA satu pun try/catch di sini.
    // Tugasnya cuma melempar; yang menerjemahkan ada di tempat lain.
    static String catatKeluar(Long id, int qty) {
        Integer sisa = stok.get(id);
        if (sisa == null)
            throw new DataTidakDitemukan("Item " + id + " tidak ada.");
        if (qty > sisa)
            throw new AturanDilanggar("Stok tidak cukup: tersedia " + sisa
                    + ", diminta " + qty + ".");

        // Bug yang sengaja ditinggal: nama item 62 tidak pernah didaftarkan.
        String keterangan = "Keluar " + qty + " " + nama.get(id).toUpperCase();
        stok.put(id, sisa - qty);
        System.out.println("   [log] " + keterangan);
        return "redirect:/items/" + id;
    }

    // Inilah isi @ControllerAdvice: SATU tempat yang mengubah exception
    // menjadi kode status, untuk semua controller sekaligus.
    static String tangani(RuntimeException e) {
        if (e instanceof DataTidakDitemukan)
            return "404 " + e.getMessage();
        if (e instanceof AturanDilanggar)
            return "400 " + e.getMessage();
        System.out.println("   [log] " + e.getClass().getSimpleName()
                + " -- ini bug, bukan salah pengguna");
        return "500 Terjadi kesalahan di server. Sudah dicatat di log.";
    }

    // Yang dikerjakan Spring: panggil controller, dan kalau ada exception
    // yang lolos, serahkan ke penangan terpusat di atas.
    static String layani(Long id, int qty) {
        try {
            String hasil = catatKeluar(id, qty);
            return hasil.startsWith("redirect:")
                    ? "302 Location: " + hasil.substring(9)
                    : "200 " + hasil;
        } catch (RuntimeException e) {
            return tangani(e);
        }
    }

    public static void main(String[] args) {
        stok.put(61L, 20);
        stok.put(62L, 5);
        nama.put(61L, "APAR 3kg");

        System.out.println("POST /items/61/stock qty=5");
        System.out.println("   -> " + layani(61L, 5));
        System.out.println("POST /items/61/stock qty=99");
        System.out.println("   -> " + layani(61L, 99));
        System.out.println("POST /items/70/stock qty=1");
        System.out.println("   -> " + layani(70L, 1));
        System.out.println("POST /items/62/stock qty=1");
        System.out.println("   -> " + layani(62L, 1));

        System.out.println("sisa stok item 61: " + stok.get(61L));
        System.out.println("sisa stok item 62: " + stok.get(62L));
    }
}""",
            },
        ],
    },
    {
        "title": "14. Log: Melihat Apa yang Terjadi Saat Kamu Tidak Menonton",
        "sections": [
            {
                "body": [
                    "Modul ini sudah dua kali menyuruhmu membaca log. Di materi pertama:",
                    "'Log ada karena error terjadi saat kamu tidak menonton.' Di materi",
                    "deploy, langkah verifikasi: 'Log start-up bersih, tidak ada exception.'",
                    "",
                    "Yang belum pernah disebut: baris-baris di dalam log itu tidak muncul",
                    "sendiri. KODEMU yang menulisnya, satu per satu, dengan sengaja. Kalau",
                    "kodemu tidak pernah menulis apa-apa ke sana, log-nya kosong - dan saat",
                    "seseorang menelepon bilang 'stoknya salah sejak kemarin', kamu tidak",
                    "punya apa pun untuk dibaca selain menebak.",
                    "",
                    "Inilah beda paling nyata antara skrip dan aplikasi. Di skrip, kamu",
                    "menonton layarnya sendiri. Di aplikasi, kejadiannya berlangsung di",
                    "server, pada jam kamu tidak ada, untuk orang yang tidak bisa kamu",
                    "tanyai. Log adalah satu-satunya mata yang tertinggal di sana.",
                    "",
                    "KENAPA System.out.println TIDAK CUKUP",
                    "",
                    "println memang mencetak sesuatu. Tapi satu baris println tidak membawa",
                    "lima hal yang justru paling kamu butuhkan nanti:",
                    "",
                    "  1. WAKTU. Tanpa jam, baris 'stok kurang' tidak bisa dicocokkan dengan",
                    "     keluhan pengguna yang bilang 'tadi sekitar jam sebelas'.",
                    "",
                    "  2. TINGKAT. Ini kabar biasa atau kebakaran? Semua baris println",
                    "     terlihat sama pentingnya, jadi tidak ada yang bisa disaring.",
                    "",
                    "  3. ASAL. Kelas mana yang bicara? Dengan 40 kelas, 'gagal menyimpan'",
                    "     bisa datang dari mana saja.",
                    "",
                    "  4. SAKLAR. println tidak bisa dimatikan tanpa menyunting kode,",
                    "     membangun ulang, dan deploy ulang. Log bisa dimatikan per paket",
                    "     lewat satu berkas konfigurasi, tanpa menyentuh kodenya.",
                    "",
                    "  5. TEMPAT MENDARAT. Di laptopmu, keluaran println lenyap begitu",
                    "     terminalnya ditutup. Di server ia tercampur ke berkas keluaran",
                    "     server (di Tomcat: catalina.out), berbaur dengan keluaran Tomcat",
                    "     sendiri, tanpa format, dan tanpa kaitan apa pun dengan pengaturan",
                    "     log aplikasimu.",
                    "",
                    "BENTUK SATU BARIS LOG",
                    "",
                    "  14:22:07.318 WARN [http-nio-8080-exec-4] b.b.service.ItemService - Stok item 61 kurang",
                    "",
                    "  14:22:07.318             kapan, sampai milidetiknya",
                    "  WARN                     tingkat: perlu dilihat, tapi bukan kiamat",
                    "  [http-nio-8080-exec-4]   thread: permintaan yang mana. Kalau empat orang",
                    "                           mengklik bersamaan, dari sinilah baris milik satu",
                    "                           orang bisa dipisahkan dari baris orang lain",
                    "  b.b.service.ItemService  nama logger - hampir selalu nama kelas penulisnya,",
                    "                           dipendekkan otomatis oleh pengaturan tampilan;",
                    "                           aslinya id.badak.bifams.service.ItemService",
                    "  Stok item 61 kurang      pesan yang kamu tulis sendiri",
                    "",
                    "Empat bagian pertama datang gratis. Bagian terakhir sepenuhnya",
                    "tanggung jawabmu, dan itulah yang menentukan log-mu berguna atau tidak.",
                ],
            },
            {
                "heading": "Logger di dalam sebuah service",
                "code": """import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ItemService {

    private static final Logger log = LoggerFactory.getLogger(ItemService.class);

    private final ItemDao itemDao;

    public ItemService(ItemDao itemDao) {
        this.itemDao = itemDao;
    }

    public void catatMutasi(Long id, MovementType jenis, int qty) {
        log.debug("Mutasi masuk: item={} jenis={} qty={}", id, jenis, qty);

        Item item = itemDao.cariById(id);
        if (item.getStok() < qty) {
            log.warn("Stok item {} tidak cukup: tersedia {}, diminta {}",
                     id, item.getStok(), qty);
            throw new AturanDilanggar("Stok tidak mencukupi.");
        }

        item.setStok(item.getStok() - qty);
        try {
            itemDao.simpan(item);
        } catch (RuntimeException e) {
            log.error("Gagal menyimpan item {} setelah mutasi", id, e);
            throw new AturanDilanggar("Mutasi gagal disimpan, coba lagi.");
        }

        log.info("Mutasi {} qty {} pada item {} tersimpan, sisa {}",
                 jenis, qty, id, item.getStok());
    }
}""",
            },
            {
                "body": [
                    "BEDAH BARIS DEKLARASINYA",
                    "",
                    "  private static final Logger log = LoggerFactory.getLogger(ItemService.class);",
                    "",
                    "Baris ini berdiri di puncak hampir tiap kelas service di proyek Java",
                    "mana pun. Kalau kamu pernah membaca kode orang lain dan bingung dari",
                    "mana 'log' tiba-tiba muncul di tengah method padahal tidak",
                    "dideklarasikan di situ - jawabannya baris ini, jauh di atas, satu kali",
                    "untuk seluruh kelas.",
                    "",
                    "  private   urusan kelas ini sendiri, bukan untuk dipinjam kelas lain.",
                    "",
                    "  static    SATU logger untuk KELASNYA, bukan satu untuk tiap objek.",
                    "            Tanpa static, tiap objek yang dibuat harus mencari loggernya",
                    "            lagi dan menyimpan satu rujukan tambahan - sia-sia, karena",
                    "            hasilnya sama persis untuk semua objek kelas itu.",
                    "",
                    "  final     ditetapkan sekali, tidak pernah diganti.",
                    "",
                    "  log       ini cuma NAMA VARIABEL, bukan kata kunci Java. Sebagian",
                    "            proyek menamainya logger atau LOG. Artinya sama saja.",
                    "",
                    "KENAPA PARAMETERNYA KELAS ITU SENDIRI",
                    "",
                    "getLogger(ItemService.class) tidak mengambil apa-apa dari isi kelasnya.",
                    "Yang diambil cuma NAMANYA lengkap dengan paketnya, dan nama itulah yang",
                    "dicetak di tiap baris log, sekaligus yang dipakai konfigurasi untuk",
                    "menyetel tingkat per paket (bagian berikutnya).",
                    "",
                    "JEBAKAN YANG SANGAT SERING. Kelas ItemDao dibuat dengan menyalin",
                    "ItemService, dan baris logger ikut tersalin apa adanya. Hasilnya semua",
                    "baris dari ItemDao mengaku dirinya ItemService. Compiler diam saja -",
                    "dari sisi Java memang tidak ada yang salah. Kamu baru sadar berbulan",
                    "kemudian, saat menyetel ItemDao ke DEBUG dan tidak satu baris pun muncul.",
                    "",
                    "SATU HAL, DUA NAMA: SLF4J DAN LOGBACK",
                    "",
                    "org.slf4j.Logger itu INTERFACE - persis seperti ItemDao di materi DAO:",
                    "ia mengumumkan APA yang bisa dilakukan, tanpa satu baris pun CARA",
                    "melakukannya. Yang benar-benar menulis ke berkas adalah mesin di",
                    "belakangnya: Logback, atau Log4j2, atau logger bawaan Java.",
                    "LoggerFactory.getLogger() mencari mesin itu saat aplikasi menyala, lalu",
                    "menyambungkannya sendiri.",
                    "",
                    "Kenapa harus dipisah begitu? Karena Spring, Hibernate, dan tiap pustaka",
                    "yang kamu pakai juga menulis log. Kalau masing-masing memilih mesinnya",
                    "sendiri, satu aplikasi punya empat berkas log dengan empat format",
                    "berbeda. Dengan SLF4J semuanya bicara lewat satu antarmuka, dan KAMU",
                    "yang memilih satu mesin untuk semuanya.",
                    "",
                    "Akibat praktisnya: di kode aplikasimu import-nya SELALU org.slf4j.*.",
                    "Nama Logback muncul di pom.xml dan di berkas konfigurasi, bukan di kode.",
                    "Melihat import ch.qos.logback di dalam sebuah service hampir selalu",
                    "tanda seseorang asal pilih saat IDE menawarkan daftar import.",
                    "",
                    "Kalau saat start-up muncul 'SLF4J: Failed to load class",
                    "org.slf4j.impl.StaticLoggerBinder' - di SLF4J versi baru bunyinya 'No",
                    "SLF4J providers were found' - artinya antarmukanya ada tapi mesinnya",
                    "tidak. Aplikasi tetap jalan, log-nya hilang semua, dan tidak ada satu",
                    "error pun sesudah itu. Yang kurang biasanya dependensi logback-classic",
                    "di pom.xml.",
                    "",
                    "KENAPA {} DAN BUKAN PENYAMBUNGAN STRING",
                    "",
                    "  log.debug(\"Mutasi masuk: item=\" + id + \" qty=\" + qty);   // hindari",
                    "  log.debug(\"Mutasi masuk: item={} qty={}\", id, qty);      // begini",
                    "",
                    "Bentuk pertama tetap MERANGKAI kalimatnya walaupun tingkat DEBUG sedang",
                    "mati. Di produksi yang berjalan di INFO, baris itu bekerja penuh untuk",
                    "membuat teks yang langsung dibuang. Satu baris tidak terasa; satu baris",
                    "di dalam perulangan 5.000 item terasa.",
                    "",
                    "Bentuk kedua menyerahkan potongannya apa adanya. Kalau tingkatnya",
                    "sedang mati, tidak ada yang dirangkai sama sekali.",
                    "",
                    "Placeholder-nya {} - bukan %s dan bukan %d. Ia tidak peduli tipe",
                    "datanya, tapi jumlahnya harus sepadan dengan jumlah argumen sesudah",
                    "pesannya.",
                    "",
                    "MELETAKKAN EXCEPTION: SATU ATURAN YANG MENENTUKAN SEGALANYA",
                    "",
                    "  log.error(\"Gagal menyimpan item {}\", id, e);",
                    "",
                    "Ada satu {} tapi DUA argumen. Itu bukan salah hitung. SLF4J melihat",
                    "argumen terakhir bertipe Throwable dan memperlakukannya khusus: ia",
                    "tidak dimasukkan ke placeholder, melainkan dicetak lengkap dengan",
                    "SELURUH stack trace-nya di bawah pesanmu. Jadi jangan sediakan {}",
                    "untuk exception-nya - cukup taruh ia paling belakang.",
                    "",
                    "Bandingkan dengan bentuk yang paling sering ditulis pemula:",
                    "",
                    "  log.error(\"Gagal menyimpan item \" + id + \": \" + e.getMessage());",
                    "",
                    "Yang tercatat cuma sepotong kalimat, misalnya 'connection is closed'.",
                    "Baris mana yang meledak, siapa yang memanggilnya, apa penyebab di",
                    "bawahnya - hilang semuanya. Dan kalau exception-nya kebetulan tidak",
                    "punya pesan (NullPointerException sering begitu), yang tertulis di",
                    "log-mu adalah 'Gagal menyimpan item 61: null'. Kamu tahu ada yang",
                    "gagal, dan tidak tahu apa pun selain itu.",
                    "",
                    "JANGAN MENCATAT KEGAGALAN YANG SAMA BERKALI-KALI",
                    "",
                    "Kalau sebuah method menulis log.error lalu melempar exception-nya lagi",
                    "ke atas, dan lapisan di atasnya melakukan hal yang sama, satu kegagalan",
                    "muncul tiga kali dengan tiga stack trace hampir kembar - dan yang",
                    "membacanya mengira ada tiga masalah. Pilih satu tempat: di penangan",
                    "terpusat @ControllerAdvice dari materi sebelumnya, atau di tempat kamu",
                    "masih memegang keterangan yang tidak dibawa exception-nya, seperti id",
                    "item pada contoh di atas.",
                    "",
                    "YANG TIDAK BOLEH MASUK LOG",
                    "",
                    "Log dibaca lebih banyak orang daripada dugaanmu: disalin ke tiket,",
                    "dikirim lewat surel ke vendor, disimpan berminggu-minggu, dan terbuka",
                    "bagi siapa pun yang punya akses ke server. Perlakukan berkas log",
                    "sebagai dokumen yang akan dibaca orang luar.",
                    "",
                    "  - Sandi, token, isi cookie sesi. Termasuk yang 'cuma akun uji'.",
                    "  - Nomor KTP, nomor telepon, alamat, data pribadi lainnya.",
                    "  - Objek permintaan secara utuh. Ini jebakan yang paling halus:",
                    "",
                    "      log.info(\"Percobaan login: {}\", form);",
                    "",
                    "    Terlihat tidak berbahaya, sampai kamu ingat toString() yang",
                    "    dibuatkan IDE atau Lombok mencetak SEMUA field kelas itu - termasuk",
                    "    password. Sebut yang kamu maksud satu per satu: form.getUsername().",
                ],
            },
            {
                "heading": "logback.xml: menyetel tingkat dan tempat mendaratnya",
                "body": [
                    "LIMA TINGKAT, DARI YANG PALING CEREWET",
                    "",
                    "  TRACE   sangat halus, jarang dipakai. Isi tiap putaran perulangan.",
                    "  DEBUG   yang kamu butuhkan saat memburu bug: parameter yang masuk,",
                    "          cabang if mana yang diambil, berapa baris hasil query.",
                    "  INFO    peristiwa wajar yang pantas dicatat: aplikasi start, 42 item",
                    "          dimuat, permintaan 8813 disetujui oleh siapa.",
                    "  WARN    aneh tapi masih tertangani: mutasi ditolak karena stok kurang,",
                    "          login gagal, konfigurasi kosong lalu dipakai nilai bawaan.",
                    "  ERROR   ada yang GAGAL dan seseorang harus mengerjakan sesuatu.",
                    "",
                    "Garis yang paling sering salah ditarik ada di antara WARN dan ERROR.",
                    "Pertanyaannya bukan 'seberapa parah', tapi: ADAKAH MANUSIA YANG HARUS",
                    "TURUN TANGAN? Pengguna meminta 999 padahal stok 20 itu WARN - aplikasi",
                    "bekerja persis sebagaimana mestinya, dan yang keliru bukan kodenya.",
                    "Database tidak bisa dihubungi itu ERROR.",
                    "",
                    "Kalau semua ditulis sebagai ERROR, tidak ada lagi yang benar-benar",
                    "ERROR, dan log yang penuh peringatan palsu akan diabaikan justru pada",
                    "hari peringatannya sungguhan.",
                    "",
                    "Konfigurasinya satu berkas bernama logback.xml di src/main/resources -",
                    "folder yang sama dengan jdbc.properties pada materi Maven. Ia dibaca",
                    "sekali saat aplikasi start, jadi mengubahnya menuntut restart.",
                    "",
                    "EMPAT HAL YANG PERLU KAMU KENALI DI DALAMNYA",
                    "",
                    "  <pattern>          susunan tiap baris: persis lima bagian yang",
                    "                     dibedah di awal materi ini.",
                    "",
                    "  <root level>       tingkat bawaan untuk SEMUA logger yang tidak",
                    "                     disebut khusus. Di produksi: INFO.",
                    "",
                    "  <logger name>      bukan nama berkas, melainkan AWALAN nama logger.",
                    "                     Menyetel id.badak.bifams berarti menyetel semua",
                    "                     kelas di bawah paket itu sekaligus - dan itu baru",
                    "                     bekerja kalau tiap kelas memanggil getLogger",
                    "                     dengan kelasnya sendiri. Saat memburu bug, inilah",
                    "                     yang kamu turunkan sebentar ke DEBUG.",
                    "",
                    "  <maxHistory>       berkasnya berganti tiap hari (bifams.2026-08-25.log,",
                    "                     bifams.2026-08-26.log, ...) dan yang lebih tua dari",
                    "                     30 hari dihapus sendiri. Tanpa ini, log tumbuh terus",
                    "                     sampai disk server penuh.",
                    "",
                    "Baris org.hibernate.SQL menjawab janji di materi DAO: naikkan ia ke",
                    "DEBUG sebentar, dan SQL yang dibuatkan Hibernate muncul di log-mu.",
                    "",
                    "Dan satu jebakan operasional: DEBUG yang lupa dikembalikan ke INFO",
                    "setelah selesai memburu bug. Ia menulis ratusan kali lebih banyak",
                    "baris, membuat log membengkak sampai disk penuh, dan aplikasi yang",
                    "mati karena disk penuh tidak memberi gejala apa pun yang mengarah ke",
                    "log sebagai penyebabnya.",
                ],
                "code": """<configuration>

  <!-- Ke mana barisnya ditulis. Rolling = ganti berkas tiap ganti hari. -->
  <appender name="BERKAS" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>/opt/tomcat/logs/bifams.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
      <fileNamePattern>/opt/tomcat/logs/bifams.%d{yyyy-MM-dd}.log</fileNamePattern>
      <maxHistory>30</maxHistory>
    </rollingPolicy>
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} %-5level [%thread] %logger{36} - %msg%n</pattern>
    </encoder>
  </appender>

  <!-- Tingkat bawaan untuk semua logger yang tidak disebut khusus. -->
  <root level="INFO">
    <appender-ref ref="BERKAS"/>
  </root>

  <!-- Paket kita sendiri, dan SQL yang dibuatkan Hibernate. -->
  <logger name="id.badak.bifams" level="INFO"/>
  <logger name="org.hibernate.SQL" level="INFO"/>

</configuration>""",
            },
            {
                "heading": "Stack trace: bacaan sehari-hari di berkas log",
                "body": [
                    "Di server, berkasnya kamu ikuti hidup-hidup dengan satu perintah:",
                    "",
                    "  tail -f /opt/tomcat/logs/bifams.log",
                    "",
                    "Biarkan jendela itu terbuka sambil kamu mengklik halamannya di browser.",
                    "Inilah isi sebenarnya dari langkah 'Verifikasi: buka halamannya, baca",
                    "log' di materi Deploy - dan cara tercepat melihat exception yang tidak",
                    "pernah sampai ke layar pengguna.",
                    "",
                    "Yang paling sering kamu temukan di sana adalah STACK TRACE. Begini",
                    "rupanya - ini keluaran sungguhan dari program kecil di bawah, yang",
                    "sengaja dibuat meledak supaya kamu punya satu untuk dibaca sendiri:",
                    "",
                    "  java.lang.RuntimeException: gagal menyimpan item 61",
                    "      at ContohStackTrace.simpanItem(ContohStackTrace.java:14)",
                    "      at ContohStackTrace.main(ContohStackTrace.java:20)",
                    "  Caused by: java.lang.IllegalStateException: connection is closed",
                    "      at ContohStackTrace.simpanKeDatabase(ContohStackTrace.java:5)",
                    "      at ContohStackTrace.simpanItem(ContohStackTrace.java:10)",
                    "      ... 1 more",
                    "  Aplikasi tetap hidup, permintaan berikutnya dilayani.",
                    "",
                    "EMPAT LANGKAH MEMBACANYA",
                    "",
                    "1. Baris paling atas menyebut exception yang PALING AKHIR terjadi,",
                    "   bukan penyebabnya. Pemula berhenti di sini lalu salah menuduh.",
                    "",
                    "2. Baris 'at ...' di bawahnya adalah rantai siapa memanggil siapa,",
                    "   dibaca dari atas ke bawah. Yang paling atas tempat kejadiannya,",
                    "   yang paling bawah titik masuknya.",
                    "",
                    "3. Lompat ke 'Caused by' PALING BAWAH. Di situlah penyebab yang",
                    "   sesungguhnya. Stack trace nyata bisa punya tiga sampai empat lapis",
                    "   Caused by, dan yang paling bawah itu yang harus kamu perbaiki -",
                    "   sisanya cuma pembungkus.",
                    "",
                    "4. Di antara puluhan baris 'at org.springframework...' dan",
                    "   'at org.apache.catalina...', cari BARIS PERTAMA yang memuat nama",
                    "   paketmu sendiri. Hampir selalu di situ letak kesalahannya, karena",
                    "   kode Spring jarang salah - ia cuma memanggil kodemu.",
                    "",
                    "'... 1 more' berarti sisa jejaknya sama persis dengan yang sudah",
                    "tercetak di atas, jadi tidak diulang. Di aplikasi sungguhan angkanya",
                    "bisa '... 87 more', dan 87 baris itu memang tidak menarik.",
                    "",
                    "Perhatikan baris terakhir keluaran itu: aplikasinya TIDAK mati. Satu",
                    "permintaan gagal, sisanya tetap dilayani. Itu sebabnya sebuah aplikasi",
                    "bisa tampak sehat dari luar sementara log-nya penuh ERROR - dan itu",
                    "sebabnya log dibaca, bukan ditunggu sampai ada yang mengeluh.",
                    "",
                    "Jalankan program di bawah, lalu cocokkan keluarannya dengan jejak yang",
                    "barusan dibedah.",
                ],
                "code": """public class ContohStackTrace {

    static void simpanKeDatabase(Long id) {
        // Anggap koneksi ke database sedang putus.
        throw new IllegalStateException("connection is closed");
    }

    static void simpanItem(Long id) {
        try {
            simpanKeDatabase(id);
        } catch (RuntimeException penyebab) {
            // Kegagalan teknis dibungkus jadi kegagalan yang punya arti,
            // TANPA membuang penyebab aslinya: ia jadi argumen kedua.
            throw new RuntimeException("gagal menyimpan item " + id, penyebab);
        }
    }

    public static void main(String[] args) {
        try {
            simpanItem(61L);
        } catch (RuntimeException e) {
            // Beginilah rupa yang ditulis log.error("...", e) ke berkas log.
            // Bawaan printStackTrace() menulis ke System.err; di sini sengaja
            // diarahkan ke System.out supaya urutan barisnya utuh.
            e.printStackTrace(System.out);
        }
        System.out.println("Aplikasi tetap hidup, permintaan berikutnya dilayani.");
    }
}""",
            },
        ],
    },
    {
        "title": "15. Tampilan: JSP, Tiles, dan Kenapa Dipisah",
        "sections": [
            {
                "body": [
                    "Controller sudah menyiapkan data. Sekarang data itu harus jadi",
                    "HTML yang bisa dibaca manusia.",
                    "",
                    "JSP adalah HTML yang boleh disisipi data. Bentuknya HTML biasa,",
                    "dengan lubang-lubang kecil tempat nilai dari Java dimasukkan.",
                ]
            },
            {
                "heading": "Potongan JSP",
                "code": """<h1>${item.nama}</h1>
<p>Stok saat ini: ${item.stok} ${item.satuan}</p>

<table>
  <tr><th>Waktu</th><th>Jenis</th><th>Qty</th><th>Sisa</th></tr>
  <c:forEach var="m" items="${history}">
    <tr>
      <td>${m.waktu}</td>
      <td>${m.jenis}</td>
      <td>${m.qty}</td>
      <td>${m.sisaStok}</td>
    </tr>
  </c:forEach>
</table>"""
            },
            {
                "body": [
                    "  ${item.nama}   diganti nilai dari objek yang dikirim controller",
                    "  <c:forEach>    mengulang blok untuk tiap baris daftar",
                    "",
                    "ATURAN YANG MEMBUAT ${item.nama} MENEMUKAN NILAINYA",
                    "",
                    "${item.nama} tidak membaca field bernama nama. Ia memanggil method",
                    "getNama(). Namanya aturan JavaBeans: buang awalan get, kecilkan huruf",
                    "pertamanya, dan itulah nama yang boleh ditulis di tampilan. Khusus",
                    "boolean awalannya boleh is - ${item.stokMenipis} di bawah menuntut",
                    "adanya isStokMenipis(), bukan stokMenipis().",
                    "",
                    "Kalau getter-nya salah nama, gejalanya ada dua dan dua-duanya",
                    "menyesatkan. Yang pertama PropertyNotFoundException, yang menyebut nama",
                    "PROPERTI - jadi kamu membaca kata satuan padahal yang kurang method",
                    "getSatuan(). Yang kedua lebih buruk: lubang kosong di halaman tanpa",
                    "error sama sekali, sehingga terlihat seperti datanya yang tidak ada",
                    "padahal getter-nyalah yang salah eja.",
                    "",
                    "Aturan yang sama dipakai di dua tempat lain. Nama field di balasan",
                    "JSON juga diambil dari getter, dan nama kolom yang ditebak Hibernate",
                    "untuk properti tanpa @Column juga. Jadi satu salah paham di sini",
                    "merembet ke tiga tempat sekaligus - dan cuma satu dari ketiganya yang",
                    "memberimu pesan error.",
                    "",
                    "APACHE TILES: MENGHINDARI SALIN-TEMPEL",
                    "",
                    "Lima belas halaman B-iFAMS punya bagian yang sama persis: header,",
                    "menu samping, footer. Kalau ditulis ulang di tiap halaman, mengganti",
                    "satu menu berarti menyunting lima belas berkas.",
                    "",
                    "Tiles memisahkan rangka dari isi:",
                    "",
                    "  layout.jsp   rangka: header + menu + <lubang isi> + footer",
                    "  detail.jsp   cuma bagian isinya saja",
                    "",
                    "Ganti menu sekali di layout, lima belas halaman ikut berubah.",
                    "",
                    "SATU ATURAN YANG TIDAK BOLEH DILANGGAR",
                    "",
                    "JANGAN menaruh keputusan bisnis di JSP.",
                    "",
                    "  Boleh    : <c:if test=\"${item.stokMenipis}\"> tampilkan lencana",
                    "  Terlarang: <c:if test=\"${item.stok <= item.stokMin}\">",
                    "",
                    "Yang pertama bertanya pada objek. Yang kedua MEMUTUSKAN di tampilan -",
                    "dan keputusan itu akan berbeda dengan yang di service begitu",
                    "aturannya berubah.",
                    "",
                    "Contoh paling mahal dari pelanggaran ini menunggu di materi Keamanan:",
                    "menyembunyikan tombol di tampilan disangka sama dengan melarang",
                    "aksinya. Ternyata tidak.",
                ]
            },
        ],
    },
    {
        "title": "16. REST yang Membalas JSON",
        "sections": [
            {
                "body": [
                    "Sampai materi tadi, tiap controller berakhir dengan salah satu dari dua hal: nama",
                    "halaman JSP, atau perintah redirect. Balasannya selalu HTML - halaman jadi, siap",
                    "dilihat mata manusia.",
                    "",
                    "Ada bentuk balasan kedua untuk pola alamat yang persis sama: DATA MENTAH, hampir",
                    "selalu JSON. Server tidak lagi menyusun halaman; ia mengirim isinya saja dan",
                    "membiarkan pihak lain yang menggambarnya.",
                    "",
                    "  GET /items/61       -> <html> ... <h1>APAR 6kg</h1> ... </html>   (halaman penuh)",
                    "  GET /api/items/61   -> {\"id\":61,\"kode\":\"APAR-004\",\"nama\":\"APAR 6kg\"}",
                    "",
                    "KENAPA HAMPIR SEMUA PROYEK JAVA BARU MEMILIH YANG KEDUA",
                    "",
                    "Karena browser bukan lagi satu-satunya yang memanggil server:",
                    "",
                    "  - aplikasi HP Android dan iOS tidak bisa menampilkan JSP",
                    "  - halaman web modern memuat datanya sendiri lewat JavaScript, tanpa memuat ulang",
                    "  - sistem lain - aplikasi keuangan, dasbor manajemen - mengambil data langsung",
                    "",
                    "Satu server yang membalas JSON melayani ketiganya. Satu server yang membalas JSP",
                    "cuma melayani browser. Itu sebabnya banyak repo Java di GitHub hari ini tidak",
                    "punya satu pun berkas .jsp, dan kamu akan sering membaca kode seperti ini.",
                    "",
                    "SATU ANOTASI YANG MENGUBAH ARTI 'return'",
                    "",
                    "  @Controller       String yang dikembalikan dibaca sebagai NAMA HALAMAN",
                    "  @RestController   yang dikembalikan dibaca sebagai ISI BALASAN itu sendiri",
                    "",
                    "@RestController sebenarnya cuma singkatan: @Controller + @ResponseBody, ditempel",
                    "sekaligus ke seluruh method di kelas itu. Di kode lawas kamu akan menemui bentuk",
                    "panjangnya - @Controller di kelas, @ResponseBody di tiap method - dan artinya sama.",
                    "",
                    "JEBAKANNYA ADA DI SINI, DAN PESAN ERRORNYA TIDAK MENOLONG",
                    "",
                    "Kelas ditulis @Controller (lupa Rest), method-nya mengembalikan objek Item. Spring",
                    "tidak mengeluh saat start. Saat dipanggil, ia mencari HALAMAN bernama hasil",
                    "toString() objek itu - sesuatu seperti 'APAR-004 - APAR 6kg (3 tabung)' - lalu",
                    "gagal dengan 404 atau 500 yang tidak menyebut kata JSON sama sekali.",
                    "",
                    "Kebalikannya sama menyesatkan: @RestController di kelas yang mengembalikan",
                    "\"items/detail\" tidak menampilkan halaman apa pun. Yang sampai ke browser adalah",
                    "tulisan items/detail - dua belas karakter, apa adanya.",
                ],
            },
            {
                "heading": "Peta rute API dan status yang dibalasnya",
                "code": """GET    /api/items                200  daftar item, JSON berbentuk array [ ... ]
GET    /api/items?cari=apar      200  daftar tersaring; kalau nihil tetap 200 dengan []
POST   /api/items                201  item baru dibuat; header Location menunjuk alamatnya
GET    /api/items/61             200  satu item
GET    /api/items/999            404  tidak ada; badan balasan kosong
PUT    /api/items/61             200  ganti SELURUH isi item
PATCH  /api/items/61             200  ganti sebagian field saja
DELETE /api/items/61             204  terhapus, dan memang tidak ada yang perlu dikirim
POST   /api/items/61/stock       200  aksi yang bukan sekadar simpan/ambil""",
            },
            {
                "heading": "Controller-nya: ResponseEntity dan @RequestBody",
                "body": [
                    "Bandingkan peta rute di atas dengan peta rute di materi Controller: di sana semua",
                    "yang mengubah data memakai POST. Bukan karena PUT dan DELETE tidak ada, tapi",
                    "karena formulir HTML memang cuma bisa GET dan POST - tidak ada cara menulis",
                    "<form method=\"delete\">. Klien JSON tidak punya batasan itu, jadi API memakai",
                    "method yang sebenarnya.",
                    "",
                    "RESPONSEENTITY: MENGATUR STATUS, HEADER, DAN BADAN SEKALIGUS",
                    "",
                    "Kalau method mengembalikan Item polos, kamu cuma menentukan BADAN balasan;",
                    "statusnya selalu 200. Begitu perlu 201 atau 404, bungkus dengan ResponseEntity:",
                    "",
                    "  ResponseEntity.ok(item)                        200 + badan",
                    "  ResponseEntity.notFound().build()              404, tanpa badan",
                    "  ResponseEntity.noContent().build()             204, tanpa badan",
                    "  ResponseEntity.created(uri).body(item)         201 + header Location + badan",
                    "  ResponseEntity.status(HttpStatus.CONFLICT)     409, angkanya ditentukan tangan",
                    "",
                    ".build() dan .body(...) itu penutup yang wajib. Tanpa salah satunya kamu masih",
                    "memegang PEMBANGUNNYA, bukan balasannya, dan kodenya tidak akan dikompilasi.",
                    "",
                    "Arti tiap angkanya sudah dibahas di materi Kode Status HTTP; yang baru di sini",
                    "cuma cara menentukannya dari dalam controller.",
                    "",
                    "@RequestBody: ARAH SEBALIKNYA",
                    "",
                    "  @ModelAttribute ItemForm form   isi FORMULIR (kode=APAR-009&nama=...) jadi objek",
                    "  @RequestBody ItemRequest req    badan permintaan yang berisi JSON jadi objek",
                    "",
                    "Keduanya menghasilkan objek Java, tapi membaca dari tempat yang berbeda.",
                    "Menukarnya adalah salah satu bug paling membingungkan buat pemula: seluruh",
                    "field-nya null, tanpa satu pun pesan error. Yang salah bukan datanya - Spring",
                    "mencarinya di tempat yang memang tidak berisi apa-apa.",
                ],
                "code": """@RestController
@RequestMapping("/api/items")
public class ItemApiController {

    private final ItemService itemService;

    public ItemApiController(ItemService itemService) {
        this.itemService = itemService;
    }

    @GetMapping                                     // GET /api/items
    public List<ItemResponse> daftar() {
        List<ItemResponse> hasil = new ArrayList<>();
        for (Item item : itemService.cariSemua()) {
            hasil.add(ItemResponse.dari(item));
        }
        return hasil;                               // jadi array JSON, status 200
    }

    @GetMapping("/{id}")                            // GET /api/items/61
    public ResponseEntity<ItemResponse> satu(@PathVariable Long id) {
        Item item = itemService.cariById(id);
        if (item == null) {
            return ResponseEntity.notFound().build();        // 404, badan kosong
        }
        return ResponseEntity.ok(ItemResponse.dari(item));   // 200 + badan JSON
    }

    @PostMapping                                    // POST /api/items
    public ResponseEntity<ItemResponse> buat(@Valid @RequestBody ItemRequest req) {
        Item baru = itemService.simpanBaru(req.getKode(), req.getNama());
        URI lokasi = URI.create("/api/items/" + baru.getId());
        return ResponseEntity.created(lokasi)                // 201 + Location
                             .body(ItemResponse.dari(baru));
    }

    @DeleteMapping("/{id}")                         // DELETE /api/items/61
    public ResponseEntity<Void> hapus(@PathVariable Long id) {
        itemService.hapus(id);
        return ResponseEntity.noContent().build();           // 204, sengaja tanpa badan
    }
}""",
            },
            {
                "heading": "Jackson bukan sihir: nama field JSON diambil dari GETTER",
                "body": [
                    "Tidak ada satu baris pun di controller tadi yang menyusun teks JSON. Yang",
                    "mengerjakannya pustaka bernama Jackson, dipanggil Spring sendiri setelah",
                    "method-mu selesai. Kamu praktis tidak pernah memanggilnya langsung.",
                    "",
                    "Cara Jackson menentukan nama field-nya sudah kamu kenal dari materi Tampilan:",
                    "aturan JavaBeans, persis aturan yang membuat ${item.nama} di JSP menemukan",
                    "nilainya. Keduanya tidak melihat field - keduanya memanggil GETTER lalu memotong",
                    "awalannya dan mengecilkan huruf pertamanya.",
                    "",
                    "  getNama()         -> \"nama\"",
                    "  getStokMinimum()  -> \"stokMinimum\"",
                    "  isStokMenipis()   -> \"stokMenipis\"     (khusus boolean, awalannya boleh is)",
                    "",
                    "Akibatnya dua hal yang selalu mengagetkan orang: field TANPA getter tidak pernah",
                    "muncul di JSON, sedangkan getter TANPA field tetap muncul.",
                    "",
                    "DUA ANOTASI UNTUK MENIMPA ATURAN ITU",
                    "",
                    "  @JsonProperty(\"nama_lengkap\")   pakai nama ini, bukan hasil potongan getter",
                    "  @JsonIgnore                     jangan sertakan sama sekali",
                    "",
                    "@JsonProperty dipakai saat pihak yang memanggil menuntut ejaan tertentu - misalnya",
                    "nama_lengkap bergaris bawah, sementara di Java-mu namaLengkap.",
                    "",
                    "@JsonIgnore dipakai untuk dua hal, dan keduanya serius:",
                    "",
                    "  - kolom yang tidak boleh dilihat siapa pun: passwordHash, token, catatan internal",
                    "  - relasi yang berputar balik: Item punya daftar Mutasi, tiap Mutasi punya Item",
                    "",
                    "Yang kedua bukan sekadar jelek kalau dibiarkan. Jackson mengikuti relasi itu",
                    "bolak-balik tanpa henti sampai StackOverflowError, dan yang sampai ke pemanggil",
                    "adalah 500 tanpa penjelasan apa pun.",
                    "",
                    "Program di bawah menulis ulang bagian inti Jackson dalam Java murni - tanpa",
                    "pustaka apa pun - supaya aturannya bisa kamu lihat bekerja. Perhatikan",
                    "catatanInternal (punya field, tanpa getter) dan stokMenipis (punya getter,",
                    "tanpa field), lalu cocokkan dengan barisan JSON yang tercetak.",
                ],
                "code": """import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.Comparator;

public class JsonDariGetter {

    // Aturan JavaBeans: getNama() -> "nama", isAktif() -> "aktif".
    static String namaProperti(Method m) {
        if (m.getParameterCount() != 0) return null;
        String n = m.getName();
        if (n.startsWith("get") && n.length() > 3) n = n.substring(3);
        else if (n.startsWith("is") && n.length() > 2) n = n.substring(2);
        else return null;
        return Character.toLowerCase(n.charAt(0)) + n.substring(1);
    }

    static String keJson(Object objek) throws Exception {
        Method[] method = objek.getClass().getDeclaredMethods();
        Arrays.sort(method, Comparator.comparing(Method::getName));

        StringBuilder sb = new StringBuilder("{");
        boolean pertama = true;
        for (Method m : method) {
            String nama = namaProperti(m);
            if (nama == null) continue;             // bukan getter, lewati
            if (!pertama) sb.append(", ");
            pertama = false;
            Object nilai = m.invoke(objek);         // getter-nya benar-benar dipanggil
            sb.append('"').append(nama).append('"').append(": ");
            if (nilai instanceof String) sb.append('"').append(nilai).append('"');
            else sb.append(nilai);
        }
        return sb.append("}").toString();
    }

    public static void main(String[] args) throws Exception {
        Item item = new Item(61L, "APAR-004", "APAR 6kg", 3, 5);
        System.out.println(keJson(item));
    }
}

class Item {
    private Long id;
    private String kode;
    private String nama;
    private int stok;
    private int stokMinimum;
    private String catatanInternal = "rahasia gudang";   // field tanpa getter

    Item(Long id, String kode, String nama, int stok, int stokMinimum) {
        this.id = id;
        this.kode = kode;
        this.nama = nama;
        this.stok = stok;
        this.stokMinimum = stokMinimum;
    }

    public Long getId()     { return id; }
    public String getKode() { return kode; }
    public String getNama() { return nama; }
    public int getStok()    { return stok; }

    // Tidak ada field bernama stokMenipis, tapi tetap terbit di JSON.
    public boolean isStokMenipis() { return stok <= stokMinimum; }
}""",
            },
            {
                "heading": "Yang dikirim bukan entitas - dan cara melihatnya dengan curl",
                "body": [
                    "@JsonIgnore memang menambal, tapi ia menambal di tempat yang salah. Entitas itu",
                    "gambaran TABEL; balasan API itu janji ke pihak luar. Menyatukan keduanya berarti",
                    "setiap perubahan struktur tabel diam-diam mengubah janji itu.",
                    "",
                    "TIGA HAL YANG TERJADI KALAU ENTITAS DIKEMBALIKAN LANGSUNG",
                    "",
                    "  1. Relasi malas meledak. Hibernate baru mengisi relasi saat pertama kali dibaca,",
                    "     dan Jackson membacanya SETELAH transaksinya ditutup. Yang muncul",
                    "     LazyInitializationException - lihat lagi materi hubungan antar entitas.",
                    "     Error ini tidak pernah terjadi saat diuji lewat halaman JSP, karena di sana",
                    "     yang membaca relasinya JSP, saat transaksinya masih terbuka.",
                    "",
                    "  2. Kolom yang tidak boleh dilihat ikut terbawa. Tambah satu kolom hari ini,",
                    "     dan kolom itu langsung terkirim ke semua pemanggil besok - tanpa diputuskan",
                    "     siapa pun.",
                    "",
                    "  3. Nama kolom database bocor keluar. Rapikan nama field suatu hari, dan",
                    "     aplikasi HP buatan orang lain rusak tanpa kamu pernah tahu.",
                    "",
                    "Jalan keluarnya kelas terpisah - ItemResponse - berisi persis field yang mau",
                    "dijanjikan, plus satu method pembuat: 'public static ItemResponse dari(Item item)'.",
                    "Ini kembaran ItemForm di materi DTO, cuma arahnya keluar, bukan masuk. Lapisan",
                    "tambahan ini terasa berlebihan sampai suatu hari kamu perlu mengubah tabel tanpa",
                    "merusak siapa-siapa.",
                    "",
                    "MEMBUKTIKANNYA SENDIRI",
                    "",
                    "curl mengirim permintaan HTTP tanpa browser. Bendera -i menampilkan baris status",
                    "dan header, bukan cuma badannya - tanpa itu 404 dan 204 terlihat sama saja:",
                    "kosong. Bendera -X memilih method-nya, -H menambah header, -d mengisi badannya.",
                    "",
                    "Satu jebakan yang pasti kamu temui: lupa -H \"Content-Type: application/json\"",
                    "membuat server membalas 415 Unsupported Media Type, bukan 400. Datamu tidak",
                    "pernah sempat dibaca - server menolak jenis kirimannya lebih dulu.",
                ],
                "code": """$ curl -s localhost:8080/api/items/61
{"id":61,"kode":"APAR-004","nama":"APAR 6kg","stok":3,"stokMenipis":true}

$ curl -i -s localhost:8080/api/items/999
HTTP/1.1 404
Content-Length: 0

$ curl -i -s -X POST localhost:8080/api/items \\
       -H "Content-Type: application/json" \\
       -d '{"kode":"APAR-009","nama":"APAR 3kg"}'
HTTP/1.1 201
Location: /api/items/74
Content-Type: application/json

{"id":74,"kode":"APAR-009","nama":"APAR 3kg","stok":0,"stokMenipis":true}

$ curl -i -s -X DELETE localhost:8080/api/items/74
HTTP/1.1 204

$ curl -i -s -X POST localhost:8080/api/items -d 'kode=APAR-009'
HTTP/1.1 415""",
            },
        ],
    },
    {
        "title": "17. Maven dan Struktur Proyek",
        "sections": [
            {
                "body": [
                    "Aplikasi Java butuh puluhan pustaka buatan orang lain. Spring",
                    "sendiri terdiri dari belasan berkas jar, dan tiap jar butuh jar",
                    "lain lagi. Mengunduhnya satu per satu mustahil dikerjakan tangan.",
                    "",
                    "Maven mengurus itu. Kamu cukup menulis APA yang dibutuhkan di satu",
                    "berkas bernama pom.xml, Maven mengunduh semuanya beserta rantai",
                    "kebutuhannya, lalu merakit aplikasimu jadi satu berkas siap deploy.",
                ]
            },
            {
                "heading": "Sepotong pom.xml",
                "code": """<dependencies>
  <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>4.1.0.RELEASE</version>
  </dependency>
  <dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-core</artifactId>
    <version>4.1.12.Final</version>
  </dependency>
</dependencies>"""
            },
            {
                "body": [
                    "Tiga baris itu menarik puluhan jar sekaligus.",
                    "",
                    "STRUKTUR FOLDER YANG WAJIB DIIKUTI",
                    "",
                    "Maven tidak bertanya di mana kodemu - ia sudah menetapkannya.",
                    "",
                    "  pom.xml",
                    "  src/main/java/          kode Java",
                    "  src/main/resources/     konfigurasi (jdbc.properties)",
                    "  src/main/webapp/        halaman & aset",
                    "      WEB-INF/views/      JSP",
                    "      WEB-INF/spring/     konfigurasi Spring",
                    "      WEB-INF/web.xml     titik masuk aplikasi",
                    "  src/test/java/          kode pengujian",
                    "  target/                 hasil rakitan (jangan disimpan di Git)",
                    "",
                    "Awalnya terasa kaku. Manfaatnya baru terasa saat kamu membuka",
                    "proyek Java orang lain dan langsung tahu harus mencari di mana.",
                    "",
                    "DI DALAM src/main/java/, LAPISAN ITU JADI FOLDER SUNGGUHAN",
                    "",
                    "Aturan paket dari materi Bean berlaku penuh di sini: baris PERTAMA",
                    "tiap berkas .java menyebut paketnya, dan susunan folder wajib sama",
                    "persis dengan nama paket itu. Begitu digambar, lapisan-lapisan di",
                    "materi Lapisan-lapisan Aplikasi Web berhenti jadi diagram dan berubah",
                    "jadi folder yang bisa kamu buka:",
                    "",
                    "  src/main/java/",
                    "    com/badak/ifams/",
                    "      controller/   ItemController.java, RequestController.java",
                    "      service/      ItemService.java, RequestService.java",
                    "      dao/          ItemDao.java, ItemDaoImpl.java",
                    "      model/        Item.java, Permintaan.java, MovementType.java",
                    "",
                    "Berkas paling atas di daftar itu diawali baris:",
                    "",
                    "  package com.badak.ifams.controller;",
                    "",
                    "Sebelum import, sebelum apa pun kecuali komentar.",
                    "",
                    "MEMBACA SEBUAH import SAMPAI KE BERKASNYA",
                    "",
                    "Kemampuan kecil ini yang menentukan bisa-tidaknya kamu menyusuri repo",
                    "orang lain. Ambil satu baris import:",
                    "",
                    "  import com.badak.ifams.dao.ItemDao;",
                    "",
                    "Ganti tiap titik jadi garis miring, tempelkan .java, lalu cari di",
                    "bawah src/main/java/:",
                    "",
                    "  src/main/java/com/badak/ifams/dao/ItemDao.java",
                    "",
                    "Kalau berkasnya tidak ada di situ, kelasnya bukan milik proyek ini -",
                    "ia datang dari jar orang lain. Itulah bedanya import com.badak...",
                    "dengan import org.springframework...: yang pertama ada di depan",
                    "matamu, yang kedua diunduh Maven dan tidak akan pernah kamu temukan",
                    "di dalam src/.",
                    "",
                    "PERINTAH YANG DIPAKAI SEHARI-HARI",
                    "",
                    "  mvn clean          hapus hasil rakitan lama",
                    "  mvn compile        kompilasi saja",
                    "  mvn test           jalankan pengujian",
                    "  mvn package        rakit jadi .war atau .jar",
                    "",
                    "Biasanya digabung: mvn clean package",
                    "",
                    "Hasilnya muncul di target/. Berkas .war itulah yang disalin ke",
                    "server. Untuk B-iFAMS, ukurannya sekitar 25 MB.",
                ]
            },
            {
                "heading": "pom.xml selengkapnya: blok yang bukan <dependencies>",
                "body": [
                    "Potongan di awal materi ini cuma memperlihatkan <dependencies>, dan",
                    "karena itu ia tidak menyerupai pom.xml mana pun yang akan kamu buka.",
                    "Pom sungguhan punya beberapa blok lain, dan tiap blok menjawab satu",
                    "pertanyaan yang cepat atau lambat akan kamu tanyakan.",
                    "",
                    "  <packaging>    war atau jar. Inilah yang menentukan bentuk hasil",
                    "                 rakitan - jawaban atas 'kenapa keluarnya .war, bukan",
                    "                 .jar seperti proyek Java yang biasa kutulis?'",
                    "  <properties>   tempat menaruh angka versi dan setelan, ditulis",
                    "                 sekali lalu dipakai berkali-kali sebagai ${nama}",
                    "  <scope>        kapan sebuah jar dibutuhkan (tabelnya di bawah)",
                    "  <build>        nama berkas hasil rakitan dan daftar plugin, termasuk",
                    "                 penentu versi Java yang dipakai mengompilasi",
                    "",
                    "Blok <properties> itu yang menjelaskan pemandangan aneh di pom orang",
                    "lain: angka versi Java tidak ditulis di mana-mana, tapi proyeknya tetap",
                    "menolak sintaks baru. Yang mengaturnya dua baris maven.compiler di",
                    "situ - bukan versi java yang terpasang di komputermu.",
                    "",
                    "EMPAT SCOPE YANG DIPAKAI SEHARI-HARI",
                    "",
                    "  compile    bawaan kalau <scope> tidak ditulis sama sekali. Ada saat",
                    "             kompilasi, ada saat berjalan, dan ikut masuk ke .war.",
                    "  provided   ada saat kompilasi, TAPI tidak ikut masuk - karena",
                    "             servernya sudah menyediakan versinya sendiri.",
                    "  runtime    tidak disentuh kodemu saat kompilasi, tapi dibutuhkan",
                    "             saat berjalan. Driver database contoh bakunya.",
                    "  test       cuma ada untuk src/test/java. Tidak pernah ikut ke server.",
                    "",
                    "Tiga yang terakhir masing-masing punya penjelasan lebih panjang di",
                    "materi yang membutuhkannya. Di sini cukup tahu bahwa satu kata itulah",
                    "yang memutuskan isi berkas .war-mu.",
                ],
                "code": """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.badak</groupId>
  <artifactId>ifams</artifactId>
  <version>1.4.0</version>
  <packaging>war</packaging>              <!-- karena inilah hasilnya .war -->

  <properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <spring.version>4.1.0.RELEASE</spring.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>${spring.version}</version>   <!-- diambil dari <properties> -->
    </dependency>
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>3.1.0</version>
      <scope>provided</scope>               <!-- Tomcat sudah punya -->
    </dependency>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.13.2</version>
      <scope>test</scope>                   <!-- tidak ikut ke .war -->
    </dependency>
  </dependencies>

  <build>
    <finalName>ROOT</finalName>             <!-- hasilnya target/ROOT.war -->
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
      </plugin>
    </plugins>
  </build>
</project>""",
            },
            {
                "body": [
                    "SATU PERINTAH LAGI, DAN TEMPAT SEMUA JAR ITU MENDARAT",
                    "",
                    "  mvn install    sama seperti mvn package, ditambah menyalin hasilnya",
                    "                 ke repositori LOKAL di ~/.m2/repository",
                    "",
                    "Folder ~/.m2/repository adalah gudang Maven di komputermu. Setiap jar",
                    "yang pernah diunduh mendarat di sana dan dipakai ulang seterusnya -",
                    "itu sebabnya build pertama lama sekali dan build kedua tidak. Susunan",
                    "foldernya mengikuti groupId, artifactId, lalu versi:",
                    "",
                    "  ~/.m2/repository/org/springframework/spring-webmvc/4.1.0.RELEASE/",
                    "",
                    "Kapan mvn install dipakai? Kalau proyek LAIN di komputermu perlu",
                    "memakai hasil rakitan proyek ini sebagai dependency. Kalau tidak ada",
                    "yang membutuhkannya, mvn clean package sudah cukup.",
                    "",
                    "Dan kalau suatu hari build gagal dengan keluhan berkas jar rusak atau",
                    "checksum tidak cocok, tersangka pertamanya unduhan yang terputus di",
                    "folder itu. Hapus folder jar yang disebut pesan errornya, lalu build",
                    "lagi supaya diunduh ulang.",
                ]
            },
        ],
    },
    {
        "title": "18. Server Aplikasi: Tomcat, Servlet, dan DispatcherServlet",
        "sections": [
            {
                "body": [
                    "Materi Maven berhenti tepat di depan satu pertanyaan yang jarang",
                    "dijawab: berkas .war di folder target/ itu DIJALANKAN OLEH SIAPA?",
                    "",
                    "Program Java biasa kamu jalankan sendiri: java NamaKelas. JVM mencari",
                    "method main(), menjalankannya dari atas ke bawah, lalu program selesai",
                    "dan mati.",
                    "",
                    "Aplikasi web tidak punya main() sama sekali. Dicari di seluruh kode",
                    "B-iFAMS pun tidak akan ketemu. Yang punya main() adalah program LAIN",
                    "yang sudah menyala lebih dulu di server, dan aplikasimu menumpang di",
                    "dalamnya. Program itu namanya SERVER APLIKASI.",
                    "",
                    "NAMA-NAMA YANG AKAN KAMU TEMUI",
                    "",
                    "  Tomcat, Jetty        menyediakan bagian web saja. Sebutan tepatnya",
                    "                       SERVLET CONTAINER. Ini yang paling sering dipakai.",
                    "  WildFly, GlassFish,  membawa jauh lebih banyak lagi. Inilah yang secara",
                    "  WebLogic, WebSphere  resmi disebut server aplikasi penuh.",
                    "",
                    "Untuk aplikasi seukuran B-iFAMS, servlet container sudah cukup. Yang",
                    "dipakai di sana Tomcat.",
                    "",
                    "Sekarang materi Deploy jadi masuk akal: startup.sh dan shutdown.sh itu",
                    "MILIK TOMCAT, bukan milik aplikasimu. Yang kamu nyalakan dan matikan",
                    "adalah Tomcat; aplikasimu ikut hidup dan ikut mati karena ia menumpang.",
                    "",
                    "APA YANG SEBENARNYA TERJADI PADA BERKAS .war",
                    "",
                    "  1. mvn package menghasilkan satu .war. Isinya sebetulnya cuma zip:",
                    "     kelas hasil kompilasi, JSP, jar pustaka, dan WEB-INF/web.xml.",
                    "  2. Berkas itu disalin ke folder webapps/ milik Tomcat.",
                    "  3. Tomcat melihat ada berkas baru, MEMBONGKARNYA jadi folder bernama",
                    "     sama tanpa akhiran .war, lalu memuat kelas-kelas di dalamnya.",
                    "  4. Sejak itu Tomcat memanggil kodemu tiap kali ada permintaan masuk.",
                    "",
                    "Langkah 3 menjelaskan sesuatu yang di materi Deploy cuma lewat begitu",
                    "saja: aplikasi yang sudah di-deploy 'terhampar sebagai folder di",
                    "server'. Folder itu HASIL BONGKARAN, bukan sumbernya - dan deploy",
                    "berikutnya membongkar ulang menimpanya. Di situlah suntingan langsung",
                    "di server lenyap tanpa jejak.",
                    "",
                    "SIKLUS HIDUP YANG BUKAN MILIKMU",
                    "",
                    "Kodemu tidak memutuskan kapan ia mulai, kapan berhenti, atau berapa",
                    "banyak permintaan ditangani bersamaan. Semua itu keputusan container.",
                    "Kamu menulis potongan yang DIPANGGIL, bukan program yang MEMANGGIL.",
                    "",
                    "Akibat yang paling cepat menggigit: satu objek controller dipakai",
                    "BERSAMA oleh semua pengguna sekaligus. Menyimpan data satu pengguna di",
                    "field controller berarti pengguna lain ikut membacanya.",
                    "",
                    "NAMA BERKAS .war MENENTUKAN ALAMAT",
                    "",
                    "  ROOT.war      ->  http://server:8080/",
                    "  bifams.war    ->  http://server:8080/bifams/",
                    "",
                    "Potongan alamat di depan itu namanya CONTEXT PATH. Menyalin .war dengan",
                    "nama lain memindahkan seluruh alamat halaman sekaligus, dan tautan di",
                    "JSP yang ditulis href=\"/items\" mendadak menunjuk ke luar aplikasi.",
                    "",
                    "Karena itu alamat di JSP sebaiknya tidak diketik mulai dari garis",
                    "miring, melainkan lewat <c:url value=\"/items\"/> yang tahu context",
                    "path-nya sendiri.",
                ],
            },
            {
                "heading": "Servlet mentah: satu kelas untuk satu halaman",
                "body": [
                    "Kalau Tomcat yang memanggil kodemu, apa bentuk 'kodemu' itu? Namanya",
                    "SERVLET: kelas dengan method yang dipanggil container setiap kali ada",
                    "permintaan, dengan dua objek yang selalu ikut dibawa masuk.",
                    "",
                    "  HttpServletRequest    semua yang DIBAWA permintaan - path, parameter,",
                    "                        header, cookie, sesi, isi formulir.",
                    "  HttpServletResponse   tempat kamu MENGISI balasan - kode status,",
                    "                        header, dan isi halaman.",
                    "",
                    "Dua nama itu akan kamu temui terus, termasuk di kode Spring. Keduanya",
                    "berasal dari paket javax.servlet.http yang disediakan Tomcat, BUKAN",
                    "bagian dari Java standar. Itu sebabnya di pom.xml dependensinya diberi",
                    "tanda <scope>provided</scope>: dipakai saat kompilasi, tapi jangan ikut",
                    "dibungkus ke .war karena container sudah punya versinya sendiri.",
                    "",
                    "(Sejak Tomcat 10 paketnya berganti nama jadi jakarta.servlet. Kode lama",
                    "ber-javax.servlet tidak dikenali di sana, dan gejalanya cuma halaman",
                    "404 - bukan pesan error yang menyebut penyebabnya.)",
                    "",
                    "Sebelum ada Spring, satu halaman ditulis sebagai satu kelas seperti ini.",
                ],
                "code": """public class ItemServlet extends HttpServlet {

    private final ItemService itemService = new ItemService();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        String idTeks = req.getParameter("id");          // dari ?id=61
        if (idTeks == null) {
            resp.sendError(400, "Parameter id wajib diisi");
            return;
        }

        Item item = itemService.cariSatu(Long.valueOf(idTeks));
        req.setAttribute("item", item);                  // titipan untuk JSP

        req.getRequestDispatcher("/WEB-INF/views/item/detail.jsp")
           .forward(req, resp);
    }
}""",
            },
            {
                "heading": "web.xml: daftar yang dibaca Tomcat saat start",
                "body": [
                    "Dua hal dari kode barusan tidak berubah sampai sekarang. Pertama,",
                    "doGet() tidak MENGEMBALIKAN apa pun; balasan dibentuk dengan mengisi",
                    "objek resp. Kedua, method-nya dipilih dari method HTTP - doGet untuk",
                    "GET, doPost untuk POST.",
                    "",
                    "Masalahnya baru terasa saat halamannya banyak. Lima belas halaman",
                    "berarti lima belas kelas, masing-masing harus didaftarkan tangan",
                    "beserta alamatnya, dan isinya berulang-ulang: ambil parameter, ubah",
                    "jadi angka, tangani kalau bukan angka, pilih JSP.",
                    "",
                    "Dari situlah DispatcherServlet lahir. Ia SATU servlet yang didaftarkan",
                    "untuk semua alamat, lalu ia sendiri yang mencari method controller mana",
                    "yang cocok. Anotasi @RequestMapping bukan sihir: ia isi tabel petunjuk",
                    "milik servlet tunggal itu.",
                    "",
                    "Pendaftarannya ada di WEB-INF/web.xml - berkas yang di materi Maven",
                    "cuma disebut 'titik masuk aplikasi'. Isinya bukan kode yang berjalan,",
                    "melainkan daftar yang dibaca Tomcat SEKALI saat aplikasi dimuat:",
                    "",
                    "  context-param     alamat berkas resep untuk wadah root.",
                    "  listener          ContextLoaderListener - yang membuat wadah root.",
                    "  filter            kode yang berdiri di depan semua permintaan.",
                    "  filter-mapping    alamat mana yang lewat filter itu.",
                    "  servlet           DispatcherServlet, si penerima semua alamat.",
                    "  servlet-mapping   alamat mana yang diserahkan kepadanya.",
                    "",
                    "DUA WADAH SPRING ITU LAHIR DI SINI",
                    "",
                    "Materi bean menjelaskan kenapa wadahnya ada dua. Berkas inilah tempat",
                    "keduanya dibuat, dan sekarang barisnya bisa ditunjuk: wadah root lahir",
                    "dari <listener>, wadah web lahir dari <servlet>.",
                    "",
                    "Perhatikan juga dari mana nama berkas resepnya datang. Wadah root",
                    "membaca berkas yang ditulis di context-param. Wadah web, kalau tidak",
                    "diberi <init-param>contextConfigLocation</init-param> sendiri, mencari",
                    "/WEB-INF/<nama-servlet>-servlet.xml - itulah asal usul nama",
                    "dispatcher-servlet.xml yang muncul di mana-mana.",
                    "",
                    "Satu baris kecil yang mudah dilewat: <load-on-startup>1</load-on-startup>",
                    "menyuruh Tomcat membangun DispatcherServlet saat start, bukan menunggu",
                    "permintaan pertama. Tanpa itu, salah konfigurasi baru meledak di wajah",
                    "pengguna pertama - bukan di log start-up yang sedang kamu tonton.",
                ],
                "code": """<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="2.5">

  <context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>/WEB-INF/applicationContext.xml</param-value>
  </context-param>

  <listener>
    <listener-class>
      org.springframework.web.context.ContextLoaderListener
    </listener-class>
  </listener>

  <filter>
    <filter-name>encoding</filter-name>
    <filter-class>
      org.springframework.web.filter.CharacterEncodingFilter
    </filter-class>
    <init-param>
      <param-name>encoding</param-name>
      <param-value>UTF-8</param-value>
    </init-param>
  </filter>
  <filter-mapping>
    <filter-name>encoding</filter-name>
    <url-pattern>/*</url-pattern>
  </filter-mapping>

  <filter>
    <filter-name>springSecurityFilterChain</filter-name>
    <filter-class>
      org.springframework.web.filter.DelegatingFilterProxy
    </filter-class>
  </filter>
  <filter-mapping>
    <filter-name>springSecurityFilterChain</filter-name>
    <url-pattern>/*</url-pattern>
  </filter-mapping>

  <servlet>
    <servlet-name>dispatcher</servlet-name>
    <servlet-class>
      org.springframework.web.servlet.DispatcherServlet
    </servlet-class>
    <load-on-startup>1</load-on-startup>
  </servlet>
  <servlet-mapping>
    <servlet-name>dispatcher</servlet-name>
    <url-pattern>/</url-pattern>
  </servlet-mapping>

</web-app>""",
            },
            {
                "body": [
                    "Sekarang diagram lapisan di materi 2 bisa dilengkapi. Di sana Browser",
                    "menyambung langsung ke CONTROLLER; kenyataannya di antara keduanya ada",
                    "empat perhentian yang selalu terlihat saat membaca kode nyata.",
                    "",
                    "  Browser",
                    "     |  GET /items/61",
                    "     v",
                    "  TOMCAT             membaca teks HTTP dari soket, menjadikannya",
                    "                     objek HttpServletRequest",
                    "     |",
                    "     v",
                    "  RANTAI FILTER      encoding, lalu Spring Security. BOLEH MENOLAK",
                    "                     di sini, dan controller tidak akan dipanggil.",
                    "     |",
                    "     v",
                    "  DispatcherServlet  satu servlet untuk semua alamat",
                    "     |",
                    "     v",
                    "  HANDLER MAPPING    alamat mana --> method controller mana",
                    "     |",
                    "     v",
                    "  CONTROLLER         mulai dari sini kode tulisanmu sendiri",
                    "     |  return \"item/detail\"",
                    "     v",
                    "  VIEW RESOLVER      nama view --> /WEB-INF/views/item/detail.jsp",
                    "     |",
                    "     v",
                    "  JSP                diisi data, jadi HTML",
                    "     |",
                    "     v",
                    "  Browser            balasan 200 beserta halamannya",
                    "",
                    "FILTER: KODE YANG BERDIRI SEBELUM SEMUANYA",
                    "",
                    "Filter adalah kelas yang dipanggil container SEBELUM servlet, untuk",
                    "setiap permintaan yang alamatnya cocok. Ia menerima permintaan yang",
                    "sama, boleh mengubahnya, boleh meneruskannya, dan boleh menghentikannya",
                    "di tempat. Bentuknya selalu mirip ini:",
                    "",
                    "  public void doFilter(req, resp, chain) {",
                    "      // sebelum controller",
                    "      chain.doFilter(req, resp);   // teruskan ke perhentian berikutnya",
                    "      // sesudah controller",
                    "  }",
                    "",
                    "Kalau chain.doFilter() tidak dipanggil, perjalanan berhenti di situ.",
                    "Itulah cara sebuah permintaan ditolak sebelum sempat menyentuh",
                    "controller.",
                    "",
                    "DI SITULAH SPRING SECURITY BEKERJA",
                    "",
                    "Baris springSecurityFilterChain di web.xml tadi bukan pelengkap:",
                    "seluruh pemeriksaan login dan hak akses tingkat URL berjalan sebagai",
                    "filter, jauh sebelum DispatcherServlet melihat alamatnya. Materi",
                    "Keamanan menyebutnya 'lapis URL' - inilah wujudnya.",
                    "",
                    "Tiga akibat yang perlu kamu ingat saat mencari masalah:",
                    "",
                    "  - Permintaan bisa dibalas 302 ke halaman login atau 403 padahal",
                    "    controller-nya tidak pernah dijalankan. Log di dalam controller",
                    "    tetap sepi, dan itu BUKAN tanda alamatnya salah ketik.",
                    "  - Menambah baris log di controller untuk mencari kenapa halaman",
                    "    kosong tidak akan menolong kalau yang menolak berdiri di depan.",
                    "  - Urutan filter menentukan hasil, dan urutannya diambil dari urutan",
                    "    <filter-mapping> di web.xml. Filter encoding harus berdiri sebelum",
                    "    apa pun yang membaca parameter; kalau tidak, huruf beraksen dan",
                    "    tanda baca sudah terlanjur salah dibaca saat filter itu jalan.",
                    "",
                    "JEBAKAN: <url-pattern>/</url-pattern> BUKAN /*",
                    "",
                    "Perhatikan di web.xml tadi filter dipetakan ke /* sedangkan servlet ke",
                    "/. Itu memang beda, dan keduanya benar.",
                    "",
                    "  /    'apa pun yang tidak ditangani servlet lain'. Ini yang benar",
                    "       untuk DispatcherServlet. Konsekuensinya berkas statis seperti",
                    "       /css/gaya.css ikut masuk ke sana, jadi harus ada aturan khusus",
                    "       yang melayaninya - di Spring MVC: <mvc:resources>.",
                    "  /*   benar-benar semua alamat, TERMASUK saat controller mem-forward",
                    "       ke JSP. JSP-nya balik lagi ke DispatcherServlet, tidak ada",
                    "       controller yang cocok untuk /WEB-INF/views/item/detail.jsp, dan",
                    "       halamanmu jadi 404 walau controller sudah berjalan benar.",
                    "",
                    "Bedanya satu karakter, dan gejalanya sama sekali tidak menunjuk ke situ.",
                    "",
                    "Kalau suatu hari kamu membuka proyek Spring Boot lalu tidak menemukan",
                    "web.xml sama sekali: berkasnya memang sudah tidak ada, pendaftarannya",
                    "pindah ke kode Java, dan Tomcat-nya ikut dibungkus ke dalam jar",
                    "aplikasi. Rantai perjalanan di atas tetap sama persis - ia cuma tidak",
                    "lagi terlihat di satu berkas. Materi berikutnya membahasnya.",
                ],
            },
            {
                "heading": "Cuplikan log start-up Tomcat",
                "body": [
                    "Materi Deploy menutup dengan 'verifikasi: buka halamannya, baca log'.",
                    "Log yang dimaksud ada di folder logs/ milik Tomcat, dan yang paling",
                    "sering dibuka bernama catalina.out:",
                    "",
                    "  tail -f /opt/tomcat/logs/catalina.out",
                    "",
                    "Bacalah SAAT startup.sh dijalankan, bukan sesudahnya. Perintah itu",
                    "kembali seketika sambil menulis 'Tomcat started', dan kalimat itu cuma",
                    "berarti prosesnya menyala - sama sekali bukan berarti aplikasimu",
                    "berhasil dimuat.",
                    "",
                    "TIGA PENANDA BAHWA SEMUANYA NORMAL",
                    "",
                    "  - 'Deploying web application archive ...' - bongkarannya mulai.",
                    "  - 'Root WebApplicationContext: initialization completed' dan",
                    "    \"FrameworkServlet 'dispatcher': initialization completed\" - kedua",
                    "    wadah Spring berhasil dibangun. Kalau salah satunya tidak muncul,",
                    "    berhenti dan cari sebabnya sekarang.",
                    "  - 'Server startup in ... ms' - Tomcat siap melayani.",
                    "",
                    "YANG PALING MENYESATKAN SAAT GAGAL",
                    "",
                    "Kalau wadah root gagal dibangun - misalnya sebuah bean meminta bean",
                    "lain yang tidak ada - aplikasimu tidak dimuat, TAPI TOMCAT TETAP",
                    "MENYALA. Port 8080 tetap menjawab, 'Server startup' tetap tercetak,",
                    "dan semua halamanmu membalas 404.",
                    "",
                    "Angka 404 itulah jebakannya: ia terbaca seperti 'alamatnya salah',",
                    "sehingga orang menghabiskan waktu memeriksa @RequestMapping, padahal",
                    "penyebabnya sudah tercetak lengkap di log beberapa detik sebelumnya.",
                    "Cara membaca tumpukan galatnya sendiri sudah dibahas di materi Log.",
                    "",
                    "Satu kegagalan lain yang khas: java.net.BindException: Address already",
                    "in use. Artinya masih ada Tomcat lain yang hidup - shutdown.sh kembali",
                    "seketika, tapi proses JVM-nya belum tentu sudah benar-benar mati.",
                    "Periksa dengan ps sebelum menyalakan lagi.",
                ],
                "code": """START-UP YANG SEHAT, sudah dipangkas seperlunya

INFO: Deploying web application archive webapps/ROOT.war
INFO: Root WebApplicationContext: initialization started
INFO: Root WebApplicationContext: initialization completed    <-- wadah root jadi
INFO: Initializing Spring FrameworkServlet 'dispatcher'
INFO: FrameworkServlet 'dispatcher': initialization completed <-- wadah web jadi
INFO: Deployment of web application archive ROOT.war has finished
INFO: Starting ProtocolHandler ["http-bio-8080"]
INFO: Server startup in 12043 ms                              <-- Tomcat siap


START-UP YANG GAGAL, dan tetap terlihat seperti berhasil

INFO: Deploying web application archive webapps/ROOT.war
INFO: Root WebApplicationContext: initialization started
SEVERE: Context initialization failed
org.springframework.beans.factory.BeanCreationException: Error creating
  bean with name 'itemService': Injection of autowired dependencies failed;
  nested exception is NoSuchBeanDefinitionException: No qualifying bean of
  type [b.b.dao.ItemDao] found
SEVERE: Error listenerStart                       <-- wadah root GAGAL dibuat
SEVERE: Context [] startup failed due to previous errors
INFO: Starting ProtocolHandler ["http-bio-8080"]
INFO: Server startup in 4102 ms                   <-- Tomcat tetap menyala""",
            },
        ],
    },
    {
        "title": "19. Spring Boot dan Spring Data JPA",
        "sections": [
            {
                "body": [
                    "Sebelum lanjut, satu hal harus disampaikan terus terang.",
                    "",
                    "Susunan proyek yang kamu pelajari sejauh ini - web.xml, folder",
                    "WEB-INF/spring, JSP, berkas .war yang disalin ke Tomcat - itu susunan",
                    "LAMA. Ia masih hidup dan masih dipakai di banyak aplikasi internal,",
                    "B-iFAMS salah satunya, jadi mempelajarinya sama sekali tidak sia-sia.",
                    "",
                    "Tapi kalau kamu membuka repo Java web mana pun di GitHub hari ini,",
                    "kemungkinan besar tidak ada satu pun berkas yang kamu kenali di sana:",
                    "tidak ada web.xml, tidak ada WEB-INF, tidak ada .war. Yang ada malah",
                    "folder repository/ berisi antarmuka KOSONG yang anehnya berfungsi.",
                    "",
                    "Kabar baiknya, cara berpikirnya sama persis. Lapisan tetap lapisan,",
                    "service tetap tempat aturan bisnis hidup, dan seluruh SQL tetap lewat",
                    "satu pintu. Yang berganti cuma penanda jalannya. Jadi yang kamu",
                    "butuhkan bukan belajar ulang dari nol, melainkan sebuah peta padanan.",
                    "",
                    "PETA PADANANNYA",
                    "",
                    "  Yang sudah kamu pelajari        Padanannya di Spring Boot",
                    "  -----------------------------   ----------------------------------",
                    "  web.xml + XML konfigurasi       @SpringBootApplication",
                    "  jdbc.properties + bean XML      application.properties / .yml",
                    "  <dependency> satu per satu      starter: spring-boot-starter-web",
                    "  .war disalin ke webapps/        satu .jar, Tomcat DI DALAM jar itu",
                    "  startup.sh milik Tomcat         java -jar app.jar",
                    "  DAO + implementasi Hibernate    interface extends JpaRepository",
                    "  JSP + Apache Tiles              Thymeleaf + th:fragment",
                    "",
                    "Sisa materi ini menyusuri tabel itu baris per baris.",
                    "",
                    "SATU BARIS BISA DITUNTASKAN SEKARANG JUGA",
                    "",
                    "Yang paling gampang, baris terakhir: Thymeleaf, pengganti JSP. Semua",
                    "perintahnya berupa ATRIBUT di dalam tag HTML biasa, bukan tag asing:",
                    "",
                    "  <table>",
                    "    <tr th:each=\"m : ${riwayat}\">",
                    "      <td th:text=\"${m.waktu}\">01 Jan 2026</td>",
                    "      <td th:text=\"${m.qty}\">10</td>",
                    "    </tr>",
                    "  </table>",
                    "",
                    "  th:each   mengulang elemen ini untuk tiap baris - persis <c:forEach>",
                    "  th:text   mengisi isi elemen - persis ${m.waktu} di JSP",
                    "",
                    "Karena perintahnya cuma atribut, berkasnya tetap HTML yang sah dan",
                    "bisa dibuka langsung di browser tanpa server. Teks '01 Jan 2026' di",
                    "dalam <td> itu contoh tampilan yang akan TERTIMPA data asli saat",
                    "dijalankan - itu sebabnya halamannya bisa digarap tanpa menyalakan",
                    "aplikasi. Berkasnya tinggal di src/main/resources/templates/, dan",
                    "rangka bersama pengganti Apache Tiles dibuat dengan th:fragment dan",
                    "th:replace.",
                    "",
                    "Aturan dari materi Tampilan tetap berlaku bulat-bulat: jangan menaruh",
                    "keputusan bisnis di sini. th:if=\"${item.stokMenipis}\" boleh,",
                    "th:if=\"${item.stok <= item.stokMin}\" tidak.",
                    "",
                    "Baris tabel lainnya butuh penjelasan lebih panjang. Mulai dari berkas",
                    "yang paling sering kamu buka: pom.xml.",
                ],
            },
            {
                "heading": "pom.xml versi Boot: parent dan starter",
                "body": [
                    "Perubahan pertamanya mengejutkan: hampir semua <version> HILANG.",
                    "",
                    "Yang mengurusnya blok <parent> di bagian paling atas berkas. Blok itu",
                    "menunjuk spring-boot-starter-parent: sebuah daftar panjang berisi",
                    "'kalau kamu memakai pustaka X, versinya sekian' untuk ratusan pustaka",
                    "yang sudah diuji COCOK SATU SAMA LAIN. Kamu cukup menyebut apa yang",
                    "dibutuhkan; versinya diputuskan dari sana. Menaikkan versi Boot pun",
                    "berarti mengganti satu angka di <parent>, bukan puluhan angka yang",
                    "tersebar di seluruh berkas.",
                    "",
                    "Kenapa itu berharga? Karena kesalahan paling melelahkan di proyek Java",
                    "lama bukan salah ketik, melainkan tabrakan versi: Spring menuntut satu",
                    "versi pustaka pendukung, Hibernate menuntut versi lain, dan aplikasinya",
                    "mati saat start dengan NoSuchMethodError yang tidak menyebut namamu",
                    "sama sekali. Bandingkan dengan pom.xml di materi Maven, tempat tiap",
                    "versi ditulis tangan satu per satu - di situlah tabrakan seperti itu",
                    "lahir.",
                    "",
                    "STARTER: SATU BARIS, PULUHAN JAR",
                    "",
                    "  spring-boot-starter-web         Spring MVC + Tomcat + JSON (Jackson)",
                    "  spring-boot-starter-data-jpa    Hibernate + JPA + pengelola transaksi",
                    "  spring-boot-starter-security    Spring Security",
                    "  spring-boot-starter-validation  @NotNull, @Size, dan kawan-kawan",
                    "  spring-boot-starter-test        JUnit + Mockito + perkakas uji Spring",
                    "",
                    "Starter bukan pustaka. Ia daftar belanja: isinya tidak ada satu baris",
                    "kode pun, cuma sekumpulan dependency lain. Itu sebabnya satu baris",
                    "bisa menarik puluhan jar sekaligus.",
                    "",
                    "Satu hal yang TIDAK ikut starter: driver database. Ia bergantung pada",
                    "database yang kamu pakai, jadi tetap disebut sendiri. Dan",
                    "<scope>runtime</scope> di situ berarti 'kodeku tidak menyentuh",
                    "kelasnya, tapi aplikasinya butuh saat berjalan'.",
                    "",
                    "Bentuknya jadi begini - hitung sendiri berapa <version> yang tersisa:",
                ],
                "code": """<parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.2.5</version>
</parent>

<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
  </dependency>
  <dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <scope>runtime</scope>
  </dependency>
</dependencies>""",
            },
            {
                "heading": "Titik masuk, dan konfigurasi yang menggantikan XML",
                "body": [
                    "Pertanyaan berikutnya saat membuka repo Boot: konfigurasinya mana?",
                    "",
                    "Jawabannya dua berkas, dan dua-duanya tercetak di bawah. Yang pertama",
                    "sebuah kelas Java berisi main() - ya, main(), seperti program Java",
                    "biasa. Aplikasi Boot tidak lagi ditumpangkan ke Tomcat: KODEMU yang",
                    "menyalakan server, karena Tomcat-nya ikut terbungkus di dalam jar.",
                    "",
                    "@SpringBootApplication sendiri cuma tiga anotasi yang dijadikan satu:",
                    "",
                    "  @Configuration             kelas ini boleh berisi definisi bean",
                    "  @ComponentScan             pindai paket ini dan seluruh sub-paketnya",
                    "  @EnableAutoConfiguration   sisanya biar Spring yang menebak",
                    "",
                    "JEBAKAN YANG MENJERAT HAMPIR SETIAP ORANG SEKALI",
                    "",
                    "@ComponentScan memindai mulai dari PAKET tempat kelas itu berada, ke",
                    "bawah. Taruh BifamsApplication di id.badak.bifams.app sementara",
                    "service-mu di id.badak.bifams.service, dan service itu tidak akan",
                    "pernah ditemukan. Pesan errornya pun tidak menyinggung pemindaian sama",
                    "sekali - yang muncul cuma keluhan bahwa bean yang dibutuhkan controller",
                    "tidak ada. Aturan praktisnya: kelas ini tinggal di paket TERATAS,",
                    "sendirian, di atas semua paket lain.",
                    "",
                    "MENJALANKANNYA",
                    "",
                    "  mvn spring-boot:run     saat mengembangkan; Ctrl+C untuk berhenti",
                    "  mvn clean package       menghasilkan target/bifams-0.0.1.jar",
                    "  java -jar target/bifams-0.0.1.jar        di server",
                    "",
                    "Tidak ada .war yang disalin ke webapps/, tidak ada startup.sh milik",
                    "Tomcat. Jar-nya besar - puluhan MB - karena berisi seluruh pustaka",
                    "PLUS servernya sendiri. Urutan deploy di materi Deploy tetap berlaku;",
                    "yang berubah cuma langkah 'tukar .war' jadi 'tukar .jar lalu jalankan",
                    "ulang'. Perjalanan satu permintaan juga tidak berubah sedikit pun:",
                    "filter, DispatcherServlet, controller, view - semuanya masih di sana,",
                    "cuma tidak lagi didaftarkan tangan di web.xml.",
                    "",
                    "AUTO-CONFIGURATION: KENAPA BANYAK HAL SUDAH JALAN",
                    "",
                    "@EnableAutoConfiguration membuat Spring mengintip isi classpath lalu",
                    "menebak apa yang kamu maksud:",
                    "",
                    "  ada starter-web              -> nyalakan Tomcat + DispatcherServlet",
                    "  ada driver + datasource.url  -> buatkan DataSource dan kolam koneksi",
                    "  ada starter-data-jpa         -> buatkan EntityManager + transaksi",
                    "",
                    "Semua bean yang dulu ditulis tangan di XML dibuatkan diam-diam. Nyaman,",
                    "sampai tebakannya meleset - dan saat itu kamu perlu melihat apa yang",
                    "sebenarnya diputuskan Spring untukmu:",
                    "",
                    "  java -jar app.jar --debug",
                    "",
                    "Log-nya akan memuat CONDITIONS EVALUATION REPORT: daftar 'Positive",
                    "matches' berisi apa saja yang dinyalakan beserta alasannya, dan",
                    "'Negative matches' berisi apa yang TIDAK dinyalakan beserta syarat yang",
                    "tidak terpenuhi. Kalau sesuatu yang kamu kira otomatis ternyata tidak",
                    "jalan, jawabannya hampir selalu ada di daftar negatif itu.",
                    "",
                    "DUA BARIS DI BERKAS PROPERTIES YANG PERLU DICATAT SEKARANG",
                    "",
                    "  ddl-auto=validate   Hibernate cuma MEMERIKSA apakah struktur tabel",
                    "                      cocok dengan entitas, tidak mengubahnya. Nilai",
                    "                      lain bisa merusak data produksi - ada materinya",
                    "                      sendiri nanti.",
                    "  ${DB_PASSWORD}      nilainya diisi dari variabel lingkungan saat",
                    "                      aplikasi dijalankan, supaya sandi produksi tidak",
                    "                      pernah ikut tersimpan di Git.",
                    "",
                    "Bentuk .yml adalah isi yang sama persis, ditulis bersarang: baris",
                    "spring.datasource.url menjadi 'spring:' lalu 'datasource:' lalu 'url:'",
                    "yang makin menjorok. Proyek memilih salah satu, jadi jangan bingung",
                    "menemui keduanya - dan yang menjorok itu tidak boleh memakai TAB,",
                    "hanya spasi.",
                    "",
                    "Inilah kedua berkasnya:",
                ],
                "code": """// ==== file: src/main/java/id/badak/bifams/BifamsApplication.java ====
package id.badak.bifams;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BifamsApplication {

    public static void main(String[] args) {
        SpringApplication.run(BifamsApplication.class, args);
    }
}

# ==== file: src/main/resources/application.properties ====
spring.datasource.url=jdbc:postgresql://10.10.1.187:5432/bifams
spring.datasource.username=bifams_fs
spring.datasource.password=${DB_PASSWORD}
spring.jpa.hibernate.ddl-auto=validate
spring.jpa.show-sql=true
server.port=8080
logging.level.id.badak.bifams=DEBUG""",
            },
            {
                "heading": "Repository: antarmuka kosong yang ternyata berfungsi",
                "body": [
                    "Sekarang folder yang paling membingungkan itu: repository/, berisi",
                    "antarmuka tanpa badan. Tidak ada satu pun kelas yang",
                    "mengimplementasikannya - jangan mencari ItemRepositoryImpl, ia memang",
                    "tidak ada.",
                    "",
                    "Yang terjadi: saat aplikasi start, Spring Data membaca antarmuka itu,",
                    "membuat sendiri sebuah objek yang mengimplementasikan seluruh",
                    "methodnya lengkap dengan SQL-nya, lalu mendaftarkannya sebagai bean.",
                    "Kamu menulis JANJI-nya; isinya dibuatkan.",
                    "",
                    "Dan sadari apa yang sebenarnya kamu lihat: ini persis DAO dari materi",
                    "5. Aturannya tidak berubah sebaris pun - seluruh akses database tetap",
                    "lewat satu pintu, service tetap tidak boleh tahu SQL. Yang hilang cuma",
                    "pekerjaan mengetik implementasinya. Bahkan alasan 'DAO dibuat sebagai",
                    "interface dulu' yang dulu terasa berlebihan sekarang jadi wajib: yang",
                    "kamu punya memang cuma interface-nya.",
                    "",
                    "METHOD YANG SUDAH ADA TANPA KAMU TULIS",
                    "",
                    "JpaRepository<Item, Long> berarti 'repository untuk entitas Item yang",
                    "id-nya bertipe Long'. Dari dua kata itu saja kamu langsung dapat:",
                    "",
                    "  DAO buatan tangan bikinanmu     Nama bakunya di Spring Data",
                    "  -----------------------------   ----------------------------------",
                    "  simpan(item)                    save(item)",
                    "  cariById(id)                    findById(id)",
                    "  cariSemua()                     findAll()",
                    "  hapus(id)                       deleteById(id)",
                    "  (tidak ada)                     existsById(id), count()",
                    "",
                    "Namanya Inggris baku dan sama persis di semua proyek Spring di dunia.",
                    "Itu justru gunanya: siapa pun yang membuka kodemu langsung tahu apa",
                    "isi method itu tanpa membacanya.",
                    "",
                    "Satu perbedaan yang wajib diperhatikan: findById TIDAK mengembalikan",
                    "Item, melainkan Optional<Item>. Itu disengaja - barisnya mungkin memang",
                    "tidak ada, dan Optional memaksamu memutuskan mau diapakan kalau tidak",
                    "ada, alih-alih menerima null diam-diam lalu kena NullPointerException",
                    "tiga baris kemudian di tempat yang tidak ada hubungannya:",
                    "",
                    "  Item item = itemRepository.findById(id)",
                    "          .orElseThrow(() -> new DataTidakDitemukan(\"Item \" + id));",
                    "",
                    "Tipe kembalian method buatanmu sendiri juga ikut bicara. Optional<Item>",
                    "berarti kamu BERJANJI hasilnya paling banyak satu baris - kalau",
                    "ternyata dua, yang kamu terima bukan salah satunya melainkan sebuah",
                    "exception. List<Item> berarti berapa pun boleh, dan kalau tidak ada",
                    "yang cocok yang kembali daftar KOSONG, bukan null.",
                    "",
                    "Bentuk lengkap satu repository:",
                ],
                "code": """public interface ItemRepository extends JpaRepository<Item, Long> {

    Optional<Item> findByKodeAndAktifTrue(String kode);

    List<Item> findByNamaContainingIgnoreCase(String kata);

    List<Item> findByStokLessThan(int batas);

    @Query("select i from Item i where i.stok <= i.stokMin and i.aktif = true")
    List<Item> cariStokMenipis();
}""",
            },
            {
                "heading": "Nama method itu cuma String yang dipotong-potong",
                "body": [
                    "Tiga method di berkas tadi tidak punya badan, tidak punya @Query, dan",
                    "tidak ada kode SQL-nya di mana pun. Toh ketiganya bekerja.",
                    "",
                    "Spring membaca NAMANYA, suku kata demi suku kata:",
                    "",
                    "  findBy      mulai baca syaratnya",
                    "  Nama        kolom nama",
                    "  Containing  LIKE %...%",
                    "  IgnoreCase  bandingkan tanpa peduli huruf besar-kecil",
                    "",
                    "Kata sambung yang paling sering dipakai: And, Or, Between, LessThan,",
                    "GreaterThan, Like, Containing, StartingWith, IgnoreCase, True, False,",
                    "IsNull, In, dan OrderBy...Desc di ujung.",
                    "",
                    "JEBAKANNYA ADA DI SALAH KETIK",
                    "",
                    "Tulis findByNmaKode dan javac tidak akan mengeluh sedikit pun -",
                    "baginya itu cuma sebuah method abstrak yang sah. Yang gagal adalah",
                    "APLIKASINYA SAAT START, dengan pesan semacam 'No property nma found",
                    "for type Item'. Jadi kalau aplikasi Boot menolak menyala sambil",
                    "menyebut nama property yang aneh, carilah salah ketiknya di nama",
                    "method repository, bukan di entitasnya.",
                    "",
                    "KALAU NAMANYA SUDAH TIDAK SANGGUP",
                    "",
                    "Begitu syaratnya rumit - dan itu cepat terjadi - nama methodnya",
                    "memanjang jadi kalimat yang tidak terbaca lagi. Di situ berhenti,",
                    "lalu tulis query-nya sendiri dengan @Query seperti cariStokMenipis()",
                    "tadi. Perhatikan isinya: 'select i from Item i' menyebut NAMA KELAS",
                    "Item beserta nama field-nya, bukan nama tabel dan nama kolom. Itu",
                    "JPQL, bukan SQL; Hibernate yang menerjemahkannya jadi SQL sesuai",
                    "database yang dipakai. Kalau kamu memang ingin menulis SQL apa adanya,",
                    "tambahkan nativeQuery = true di dalam @Query.",
                    "",
                    "BUKTIKAN SENDIRI",
                    "",
                    "Antarmuka kosong tadi terasa seperti sihir sampai kamu melihat",
                    "mekanismenya apa adanya: sebuah String yang dipotong di kata",
                    "sambungnya. Program di bawah melakukan persis itu - Java murni, tanpa",
                    "Spring sama sekali. Jalankan, dan keluarannya:",
                    "",
                    "  findByKode",
                    "      SELECT * FROM item WHERE kode = ?",
                    "  findByKodeAndAktifTrue",
                    "      SELECT * FROM item WHERE kode = ? AND aktif = true",
                    "  findByNamaContainingIgnoreCase",
                    "      SELECT * FROM item WHERE LOWER(nama) LIKE LOWER(?)",
                    "  findByStokLessThan",
                    "      SELECT * FROM item WHERE stok < ?",
                    "",
                    "Versi aslinya tentu jauh lebih lengkap - ia tahu tipe tiap field, tahu",
                    "relasi antar entitas, dan menghasilkan JPQL alih-alih SQL mentah - tapi",
                    "mekanismenya persis ini. Dan sekarang jelas juga kenapa salah ketik",
                    "nama field baru ketahuan saat aplikasi start: pemotongan nama itu",
                    "memang baru dikerjakan di situ, bukan saat dikompilasi.",
                ],
                "code": """public class NamaJadiQuery {

    // Meniru cara Spring Data membaca nama method lalu menyusun query.
    static String query(String namaMethod) {
        String sisa = namaMethod.substring("findBy".length());
        StringBuilder sql = new StringBuilder("SELECT * FROM item WHERE ");
        String[] bagian = sisa.split("And");
        for (int i = 0; i < bagian.length; i++) {
            if (i > 0) {
                sql.append(" AND ");
            }
            sql.append(syarat(bagian[i]));
        }
        return sql.toString();
    }

    static String syarat(String kata) {
        if (kata.endsWith("True")) {
            return kolom(potong(kata, 4)) + " = true";
        }
        if (kata.endsWith("LessThan")) {
            return kolom(potong(kata, 8)) + " < ?";
        }
        if (kata.endsWith("ContainingIgnoreCase")) {
            return "LOWER(" + kolom(potong(kata, 20)) + ") LIKE LOWER(?)";
        }
        return kolom(kata) + " = ?";
    }

    static String potong(String kata, int jumlah) {
        return kata.substring(0, kata.length() - jumlah);
    }

    // "StokMin" -> "stok_min", karena nama kolom ditulis begitu.
    static String kolom(String kata) {
        StringBuilder k = new StringBuilder();
        for (char c : kata.toCharArray()) {
            if (Character.isUpperCase(c) && k.length() > 0) {
                k.append('_');
            }
            k.append(Character.toLowerCase(c));
        }
        return k.toString();
    }

    public static void main(String[] args) {
        String[] contoh = {
            "findByKode",
            "findByKodeAndAktifTrue",
            "findByNamaContainingIgnoreCase",
            "findByStokLessThan",
        };
        for (String nama : contoh) {
            System.out.println(nama);
            System.out.println("    " + query(nama));
        }
    }
}""",
            },
        ],
    },
    {
        "title": "20. Login: Sesi, Sandi, dan CSRF",
        "sections": [
            {
                "body": [
                    "Materi berikutnya bertanya 'kamu boleh apa'. Sebelum itu ada",
                    "pertanyaan yang lebih dasar dan belum pernah dijawab di modul ini:",
                    "setelah tombol Login ditekan, APA sebenarnya yang berubah?",
                    "",
                    "HTTP TIDAK PUNYA INGATAN",
                    "",
                    "Tiap permintaan HTTP berdiri sendiri. Server menerima, menjawab,",
                    "lalu lupa. Permintaan berikutnya - dari orang yang sama, dari",
                    "browser yang sama - datang seperti orang yang belum pernah datang.",
                    "",
                    "  POST /login    -> 'oke, sandimu cocok'",
                    "  GET  /items    -> 'kamu siapa?'",
                    "",
                    "Ini bukan kelalaian yang bisa ditambal. Memang tidak ada apa pun di",
                    "HTTP yang menyambungkan dua permintaan itu: keduanya bisa tiba lewat",
                    "koneksi berbeda, dan dilayani thread yang berbeda pula.",
                    "",
                    "Jadi 'sudah login' harus DIBUAT. Tidak ada yang memberikannya gratis.",
                    "",
                    "SESI: SERVER MENCATAT, BROWSER MEMBAWA NOMORNYA",
                    "",
                    "Caranya dua bagian, dan kebanyakan orang cuma tahu setengahnya.",
                    "",
                    "  1. Server membuat catatan DI SISINYA SENDIRI: 'S1 = budi, ADMIN'.",
                    "     Catatan ini tidak pernah dikirim ke mana-mana.",
                    "  2. Server menitipkan NOMORNYA saja lewat header balasan:",
                    "",
                    "        Set-Cookie: JSESSIONID=S1",
                    "",
                    "Sejak itu browser mengirim ulang cookie tersebut di SETIAP permintaan",
                    "ke alamat yang sama - tanpa diminta, tanpa satu baris kode pun darimu:",
                    "",
                    "        Cookie: JSESSIONID=S1",
                    "",
                    "Itulah seluruh mekanismenya. 'Sudah login' bukan variabel di dalam",
                    "programmu; ia sebuah nomor yang bolak-balik dititipkan, plus catatan",
                    "di memori server yang bisa dicari dengan nomor itu.",
                    "",
                    "Ingat baik-baik kata 'tanpa diminta'. Di ujung materi ini kata itu",
                    "berubah jadi lubang keamanan bernama CSRF.",
                    "",
                    "TIGA PENGAMAN DI COOKIE ITU SENDIRI",
                    "",
                    "  HttpOnly   JavaScript di halaman tidak boleh membacanya. Tanpa ini,",
                    "             satu skrip nyasar cukup untuk menyalin sesi orang.",
                    "  Secure     cuma dikirim lewat HTTPS, tidak lewat HTTP polos.",
                    "  SameSite   browser menahan cookie ini untuk permintaan yang datang",
                    "             dari situs lain. Bantuan besar, tapi bukan pengganti",
                    "             token CSRF - versi browser lama tidak mematuhinya.",
                ],
            },
            {
                "heading": "Sesi dari dalam: gudang, cookie, dan jam yang berjalan",
                "body": [
                    "Objek yang kamu pegang di kode namanya HttpSession, didapat dari",
                    "HttpServletRequest yang sudah dikenal di materi Server Aplikasi:",
                    "request.getSession().",
                    "",
                    "  session.setAttribute(\"user\", u)   simpan ke catatan sisi server",
                    "  session.getAttribute(\"user\")      ambil lagi; hasilnya bertipe",
                    "                                    Object, jadi harus di-cast",
                    "  session.invalidate()              buang catatannya - inilah logout",
                    "  session.getId()                   nomor yang dititipkan tadi",
                    "",
                    "TIGA HAL YANG MEMBUAT SESI LENYAP SENDIRI",
                    "",
                    "  - Menganggur terlalu lama. Batasnya disetel, bukan hukum alam:",
                    "      web.xml      <session-config>",
                    "                     <session-timeout>30</session-timeout>",
                    "                   </session-config>       (satuannya menit)",
                    "      Spring Boot  server.servlet.session.timeout=30m",
                    "    Inilah kenapa kamu tiba-tiba dilempar ke halaman login setelah",
                    "    formulir ditinggal rapat satu jam.",
                    "  - Aplikasi di-restart. Catatan sesi hidup di MEMORI server, jadi",
                    "    deploy siang hari berarti semua orang yang sedang bekerja ikut",
                    "    keluar - termasuk yang formulirnya belum sempat disimpan.",
                    "  - Logout, lewat invalidate().",
                    "",
                    "JEBAKAN: SESI BUKAN GUDANG",
                    "",
                    "Karena praktis, orang mulai menitipkan apa saja ke sesi: hasil",
                    "pencarian, seluruh daftar item, keranjang berisi objek entitas. Tiap",
                    "sesi adalah memori server yang ditahan sampai timeout, dikali jumlah",
                    "orang yang sedang login. Simpan seperlunya - id pengguna dan perannya -",
                    "lalu ambil sisanya dari database saat memang dibutuhkan.",
                    "",
                    "Program di bawah bukan server sungguhan, tapi tiap barisnya adalah apa",
                    "yang benar-benar dikerjakan Tomcat. Jalankan, lalu perhatikan tiga hal",
                    "di keluarannya:",
                    "",
                    "  - permintaan pertama ditolak, padahal orangnya tahu sandi. Server",
                    "    memang belum punya alasan apa pun untuk mengenalinya.",
                    "  - permintaan di menit 50 ditolak walau cookie-nya sama persis.",
                    "  - nomor sesi setelah login kedua BEDA (S2), dan sesudah logout nomor",
                    "    itu tidak berarti apa-apa lagi.",
                ],
                "code": """import java.util.HashMap;
import java.util.Map;

// "Sesi" bukan barang ajaib. Isinya cuma sebuah peta di dalam server,
// plus satu nomor yang dititipkan ke browser lewat cookie.
public class SimulasiSesi {

    // Kunci = isi cookie JSESSIONID. Nilai = catatan satu pengunjung.
    static Map<String, Map<String, String>> gudang = new HashMap<>();
    static Map<String, Integer> terakhirDipakai = new HashMap<>();

    static int nomorSesi = 1;
    static int menit = 0;             // jam palsu, biar hasilnya selalu sama
    static final int BATAS_DIAM = 30; // mati setelah 30 menit menganggur

    // Yang dikerjakan server SETELAH sandi terbukti benar.
    static String buatSesi(String user) {
        String id = "S" + nomorSesi;  // aslinya panjang, acak, tak tertebak
        nomorSesi++;
        Map<String, String> isi = new HashMap<>();
        isi.put("user", user);        // session.setAttribute("user", user)
        gudang.put(id, isi);
        terakhirDipakai.put(id, menit);
        System.out.println("  <- Set-Cookie: JSESSIONID=" + id);
        return id;
    }

    // Dipanggil di SETIAP permintaan, sebelum controller mana pun jalan.
    static String siapaIni(String cookie) {
        Integer kapan = terakhirDipakai.get(cookie);
        if (kapan == null) return null;       // tak dikenal / sudah dibuang
        if (menit - kapan > BATAS_DIAM) {     // terlalu lama menganggur
            gudang.remove(cookie);
            terakhirDipakai.remove(cookie);
            return null;
        }
        terakhirDipakai.put(cookie, menit);   // tiap akses memperpanjang
        return gudang.get(cookie).get("user");   // session.getAttribute
    }

    static void minta(String jalur, String cookie) {
        String tampil = cookie.isEmpty() ? "(tanpa cookie)"
                                         : "Cookie: JSESSIONID=" + cookie;
        String user = siapaIni(cookie);
        System.out.println("menit " + menit + "  GET " + jalur
                + "  " + tampil);
        if (user == null) {
            System.out.println("  -> 302 ke /login  server tak kenal kamu");
        } else {
            System.out.println("  -> 200 halaman untuk " + user);
        }
    }

    public static void main(String[] args) {
        minta("/items", "");                 // belum login sama sekali

        System.out.println("menit " + menit + "  POST /login  budi, cocok");
        String cookie = buatSesi("budi");

        menit = 5;
        minta("/items", cookie);             // masih orang yang sama

        menit = 50;                          // 45 menit tak disentuh
        minta("/items", cookie);             // inilah "kok tiba-tiba logout"

        System.out.println("menit " + menit + "  POST /login  budi, cocok");
        cookie = buatSesi("budi");           // nomor sesinya BEDA
        minta("/items/61", cookie);

        System.out.println("menit " + menit + "  POST /logout");
        gudang.remove(cookie);               // session.invalidate()
        terakhirDipakai.remove(cookie);
        minta("/items/61", cookie);          // cookie lama tak berarti lagi
    }
}""",
            },
            {
                "body": [
                    "Sekarang pertanyaan yang tertunda sejak materi Service. Di sana ada:",
                    "",
                    "  public void setujui(Long requestId, String namaPetugas)",
                    "",
                    "Dari mana 'namaPetugas' datang? Kalau jawabannya 'dari formulir',",
                    "aplikasimu baru saja mengizinkan siapa pun mengaku sebagai orang lain.",
                    "Ubah satu input tersembunyi sebelum menekan Setujui, dan catatan",
                    "persetujuan mencantumkan nama yang bukan pelakunya - lengkap dengan",
                    "tanggal, rapi, dan salah.",
                    "",
                    "Aturannya keras dan tanpa pengecualian: apa pun yang dikirim pengirim",
                    "permintaan bisa dikarang. Identitas pelaku HANYA boleh diambil dari",
                    "sesi, karena cuma isi sesi yang ditentukan server.",
                    "",
                    "TIGA CARA MENGAMBILNYA - sumbernya sama, cuma jalannya beda",
                    "",
                    "  Principal principal   Tambahkan sebagai parameter method controller;",
                    "                        Spring yang mengisinya. principal.getName()",
                    "                        mengembalikan username.",
                    "  Authentication auth   Sama caranya, tapi ikut membawa perannya lewat",
                    "                        auth.getAuthorities().",
                    "  SecurityContextHolder Bisa dipanggil dari mana saja, termasuk service",
                    "                        yang tidak menerima parameter request.",
                    "",
                    "DUA JEBAKAN YANG PASTI KAMU TEMUI",
                    "",
                    "1. principal bisa null. Di halaman yang boleh dibuka tanpa login,",
                    "   parameter itu datang kosong, dan principal.getName() langsung jadi",
                    "   NullPointerException - di halaman yang justru paling ramai dibuka.",
                    "",
                    "2. SecurityContextHolder itu ThreadLocal: isinya menempel pada THREAD",
                    "   yang sedang melayani permintaan. Begitu pekerjaannya dilempar ke",
                    "   thread lain - @Async, ExecutorService, tugas terjadwal - isinya",
                    "   kosong dan getAuthentication() mengembalikan null. Kalau namanya",
                    "   dibutuhkan di sana, ambil dulu selagi masih di thread permintaan,",
                    "   lalu OPER sebagai parameter biasa.",
                ],
                "code": """// SALAH - namanya ikut dikirim pengirim, jadi bisa dikarang
@PostMapping("/requests/{id}/approve")
public String setujui(@PathVariable Long id,
                      @RequestParam String namaPetugas) {
    requestService.setujui(id, namaPetugas);
    return "redirect:/requests/" + id;
}

// BENAR - namanya diambil dari sesi, yang isinya ditentukan server
@PostMapping("/requests/{id}/approve")
public String setujui(@PathVariable Long id, Principal principal) {
    requestService.setujui(id, principal.getName());
    return "redirect:/requests/" + id;
}

// Di service yang tidak menerima parameter request, sumbernya tetap sama.
// Catatan: ini hanya sah di thread yang sedang melayani permintaan.
Authentication auth =
        SecurityContextHolder.getContext().getAuthentication();
String siapa = auth.getName();                      // "budi"
boolean admin = auth.getAuthorities().stream()
        .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"));""",
            },
            {
                "heading": "Sandi: yang disimpan bukan sandinya",
                "body": [
                    "Kolom password di tabel app_user. Apa isinya?",
                    "",
                    "  rahasia123                        <- salah, dan bukan salah kecil",
                    "  MD5 atau SHA-256 dari sandinya    <- masih salah",
                    "  $2a$10$N9qo8uLOickgx2ZMRZoMye..   <- ini yang benar",
                    "",
                    "KENAPA SANDI APA ADANYA ITU BENCANA",
                    "",
                    "Bukan cuma soal penyusup. Siapa pun yang boleh membaca tabel itu -",
                    "DBA, orang yang memegang berkas cadangan, kamu sendiri saat sedang",
                    "menelusuri bug - langsung memegang sandi semua orang. Dan karena orang",
                    "memakai sandi yang sama di banyak tempat, yang bocor bukan cuma akun",
                    "di aplikasimu.",
                    "",
                    "KENAPA MD5 DAN SHA JUGA TIDAK CUKUP",
                    "",
                    "Keduanya memang satu arah. Masalahnya, keduanya dirancang untuk CEPAT -",
                    "dan cepat justru yang tidak kamu inginkan di sini. Satu kartu grafis",
                    "biasa sanggup mencoba miliaran tebakan per detik, jadi 'satu arah'",
                    "tidak berarti banyak untuk sandi sependek yang biasa dipakai orang.",
                    "",
                    "Lebih parah lagi tanpa GARAM: sandi yang sama menghasilkan hash yang",
                    "sama persis. Satu tabel bocor langsung memperlihatkan siapa saja yang",
                    "bersandi '123456' - cukup lihat hash mana yang kembar - dan daftar",
                    "hash siap pakai yang beredar bebas menyelesaikan sisanya.",
                    "",
                    "BCRYPT: LAMBAT DENGAN SENGAJA, DAN BERGARAM",
                    "",
                    "  passwordEncoder.encode(\"rahasia123\")         saat mendaftar",
                    "  passwordEncoder.matches(mentah, tersimpan)   saat login",
                    "",
                    "Perhatikan yang TIDAK ada di daftar itu: decode(). Memang tidak ada,",
                    "dan itu bukan kekurangan yang perlu diakali.",
                    "",
                    "MEMBACA $2a$10$...",
                    "",
                    "  $2a$        versi algoritmanya",
                    "  $10$        biaya kerja: 2^10 putaran. Naik satu angka berarti dua",
                    "              kali lebih lambat - buat penebak maupun buat servermu.",
                    "  22 huruf    berikutnya: GARAMnya, diacak baru untuk tiap baris",
                    "  sisanya     hasil adukan sandi + garam",
                    "",
                    "Garamnya ikut tersimpan di teks yang sama, dan itu memang tidak",
                    "apa-apa - garam bukan rahasia. Tugasnya cuma satu: membuat dua orang",
                    "bersandi sama punya hash berbeda, sehingga tidak ada satu daftar pun",
                    "yang bisa disiapkan lebih dulu untuk semua orang sekaligus.",
                    "",
                    "Karena garamnya diacak, encode(\"rahasia123\") memberi hasil berbeda",
                    "tiap kali dipanggil. Itu normal, dan itu sebabnya login TIDAK boleh",
                    "membandingkan dengan tanda sama dengan - satu-satunya cara memeriksa",
                    "adalah matches(), yang mengambil garam dari hash tersimpan lalu",
                    "mengaduk ulang sandi yang barusan diketik.",
                    "",
                    "'LUPA SANDI' TIDAK MENGIRIM SANDI",
                    "",
                    "Akibat langsungnya: aplikasimu tidak tahu sandi siapa pun. Yang bisa",
                    "dilakukan cuma MERESET - kirim tautan berumur pendek, minta sandi",
                    "baru, simpan hash barunya.",
                    "",
                    "Jadikan ini alat ukur untuk aplikasi mana pun. Kalau sebuah situs",
                    "mengirimkan kembali sandi LAMAmu lewat email, itu bukti sandinya",
                    "tersimpan dalam bentuk yang bisa dibaca balik. (Dan jangan pernah",
                    "menaruh sandi di log - materi Log sudah menyebut ini.)",
                    "",
                    "Program berikut versi mainan yang garamnya sengaja dipatok supaya",
                    "hasilnya bisa kamu bandingkan. Untuk aplikasi sungguhan JANGAN menulis",
                    "sendiri: pakai BCryptPasswordEncoder dari Spring Security.",
                ],
                "code": """import java.security.MessageDigest;
import java.util.Base64;

// Versi mainan dari cara BCrypt bekerja, supaya kelihatan apa yang
// sebenarnya duduk di kolom password - dan bagaimana login masih bisa
// memeriksanya walau sandinya sendiri tidak pernah disimpan.
public class SimulasiSandi {

    // Satu arah: sandi -> hash bisa, hash -> sandi tidak ada jalannya.
    static String aduk(String garam, String sandi) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] h = (garam + ":" + sandi).getBytes("UTF-8");
        for (int i = 0; i < 2000; i++) {   // sengaja diperlambat
            h = md.digest(h);
        }
        return Base64.getEncoder().encodeToString(h).substring(0, 22);
    }

    // Yang masuk ke database. Garamnya ikut, di dalam teks yang sama.
    static String encode(String garam, String sandi) throws Exception {
        return "$toy$14$" + garam + "$" + aduk(garam, sandi);
    }

    // Saat login: sandi mentah diaduk ULANG dengan garam yang tersimpan.
    static boolean matches(String mentah, String tersimpan) throws Exception {
        int batas = tersimpan.lastIndexOf('$');
        String kepala = tersimpan.substring(0, batas);
        String garam = kepala.substring(kepala.lastIndexOf('$') + 1);
        return tersimpan.equals(encode(garam, mentah));
    }

    public static void main(String[] args) throws Exception {
        // Dua orang, sandi sama persis, garam beda -> barisnya beda.
        String budi = encode("gRm7pQ", "rahasia123");
        String siti = encode("xZ2kLd", "rahasia123");

        System.out.println("budi  " + budi);
        System.out.println("siti  " + siti);
        System.out.println();

        System.out.println("budi ketik rahasia123 -> "
                + matches("rahasia123", budi));
        System.out.println("budi ketik rahasia124 -> "
                + matches("rahasia124", budi));
        System.out.println("siti ketik rahasia123 -> "
                + matches("rahasia123", siti));
    }
}""",
            },
            {
                "heading": "CSRF, dan dua macam 403 yang gejalanya sama persis",
                "body": [
                    "Ingat lagi kalimat di awal: browser mengirim cookie sesi OTOMATIS ke",
                    "alamat tujuan, tanpa peduli siapa yang menyuruh permintaan itu dikirim.",
                    "",
                    "Budi sedang login di B-iFAMS. Di tab lain ia membuka halaman biasa yang",
                    "ternyata memuat formulir tersembunyi menuju alamat aplikasimu, plus",
                    "sebaris JavaScript yang mengirimnya sendiri. Browser Budi mengirim POST",
                    "itu LENGKAP dengan cookie sesinya, karena begitulah aturan cookie. Di",
                    "sisi server permintaan tersebut tampak sah sepenuhnya: sesi yang benar,",
                    "peran ADMIN yang benar, dan permintaan nomor 17 pun disetujui.",
                    "",
                    "Itulah CSRF. Bukan mencuri sesi - MEMINJAM sesi yang sudah ada.",
                    "",
                    "PENANGKALNYA: SESUATU YANG HANYA ADA DI HALAMANMU",
                    "",
                    "Server menaruh satu nilai acak di sesi, lalu menuliskan nilai yang sama",
                    "sebagai input tersembunyi bernama _csrf di setiap formulir. Permintaan",
                    "yang MENGUBAH data (POST, PUT, DELETE) ditolak kalau nilai itu tidak",
                    "ikut atau tidak cocok.",
                    "",
                    "Halaman penyerang tidak bisa menebaknya, dan tidak bisa membacanya dari",
                    "halamanmu - browser melarang satu situs membaca isi situs lain. Cookie",
                    "boleh ikut terkirim; isi halaman tidak boleh dibaca. Persis celah itu",
                    "yang ditutup token ini.",
                    "",
                    "Di Spring Security perlindungan ini menyala secara BAWAAN. Yang perlu",
                    "kamu urus cuma memastikan tokennya benar-benar tertulis di tiap",
                    "formulir - dan kalau memakai taglib form Spring, itu pun otomatis.",
                    "",
                    "403 KARENA CSRF vs 403 KARENA HAK AKSES",
                    "",
                    "Gejalanya sama persis: tombol ditekan, gagal, angkanya 403. Penyebabnya",
                    "berbeda jauh, dan menebak yang salah bisa membuang berhari-hari.",
                    "Keduanya juga ditolak di RANTAI FILTER (materi Server Aplikasi),",
                    "sebelum DispatcherServlet - itu sebabnya tidak ada satu pun baris log",
                    "dari service-mu, dan breakpoint di controller tidak pernah kena.",
                    "",
                    "  Pertanyaan pembeda               CSRF          Hak akses",
                    "  Bisa kena di GET?                tidak pernah  bisa",
                    "  Admin melakukan hal yang sama?   tetap 403     berhasil",
                    "  Semua formulir kena serentak?    sering        tidak, yang itu saja",
                    "  Parameter _csrf ikut terkirim?   tidak         ya",
                    "",
                    "  Nama exception di log:",
                    "    CSRF       MissingCsrfTokenException, InvalidCsrfTokenException",
                    "    Hak akses  AccessDeniedException",
                    "",
                    "Cara tercepat memastikannya: ulangi permintaan yang sama persis dari",
                    "akun ADMIN. Masih 403? Berarti hak akses bukan penyebabnya. Berhasil?",
                    "Berarti tokennya baik-baik saja dan yang kurang cuma perannya.",
                    "",
                    "Supaya exception-nya benar-benar terlihat, naikkan level logger",
                    "org.springframework.security ke DEBUG - caranya ada di materi Log.",
                    "Tanpa itu keduanya sama-sama diam, dan yang tersisa cuma angka 403 di",
                    "access log. Bedanya dengan 401 sudah dibahas di materi Kode Status:",
                    "401 berarti belum dikenal, 403 berarti sudah dikenal tapi ditolak.",
                    "",
                    "Dan penyebab paling sering dari 403 CSRF yang muncul serentak di semua",
                    "formulir: sesinya sudah kedaluwarsa, sehingga token di halaman lama",
                    "tidak cocok lagi dengan yang ada di sesi baru.",
                    "",
                    "API TANPA SESI",
                    "",
                    "Materi REST tadi membalas JSON untuk pemanggil yang bukan browser:",
                    "aplikasi ponsel, skrip, server lain. Mereka tidak punya urusan dengan",
                    "cookie. Sesi juga menyimpan catatannya di memori SATU server - begitu",
                    "aplikasinya dijalankan di dua server, catatan itu tidak ada di sebelah.",
                    "",
                    "Gantinya token, yang dikirim sendiri oleh pemanggil di tiap permintaan:",
                    "",
                    "  Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJidWRpIn0.Kx7t2Q",
                    "",
                    "Bentuk itu namanya JWT: tiga bagian dipisah titik - keterangan",
                    "algoritma, isi (siapa kamu, berlaku sampai kapan), dan tanda tangan.",
                    "Server tidak menyimpan apa-apa; ia cukup memeriksa tanda tangannya",
                    "masih cocok dengan kunci rahasianya.",
                    "",
                    "TIGA HAL YANG SERING SALAH DIMENGERTI",
                    "",
                    "  - JWT bukan enkripsi. Dua bagian pertama cuma base64:",
                    "    eyJzdWIiOiJidWRpIn0 kalau didekode berbunyi {\"sub\":\"budi\"}, dan",
                    "    siapa pun yang memegang tokennya bisa melakukannya. Jangan menaruh",
                    "    apa pun yang rahasia di sana.",
                    "  - Karena server tidak menyimpannya, token tidak bisa dicabut di",
                    "    tengah jalan. Logout di sisi klien cuma membuang tokennya; token",
                    "    yang terlanjur bocor tetap sah sampai kedaluwarsa. Itu sebabnya",
                    "    umurnya dibuat pendek.",
                    "  - Header Authorization TIDAK dikirim browser otomatis - beda dengan",
                    "    cookie. Justru itu yang membuat API bertoken kebal CSRF, dan",
                    "    kenapa konfigurasi API biasanya mematikan perlindungan CSRF",
                    "    dengan sadar, bukan karena malas.",
                    "",
                    "Terakhir, dua formulir di bawah ini: satu milikmu, satu lagi milik",
                    "penyerang. Yang menentukan nasib keduanya cuma satu baris.",
                ],
                "code": """<!-- Formulir aslinya, di aplikasimu. Baris tersembunyi itu pembedanya. -->
<form method="post" action="/requests/17/approve">
  <input type="hidden" name="${_csrf.parameterName}"
         value="${_csrf.token}"/>
  <button type="submit">Setujui</button>
</form>

<!-- Halaman milik orang lain, dibuka korban di tab sebelah. Cookie sesinya
     tetap ikut terkirim - itu aturan browser, bukan kelalaian aplikasimu.
     Yang tidak ikut cuma token _csrf, karena halaman ini tidak diizinkan
     membaca formulir di atas. Hasilnya 403, dan stok tidak jadi berkurang. -->
<form id="jebakan" method="post"
      action="http://bifams.internal/requests/17/approve">
  <input type="hidden" name="requestId" value="17"/>
</form>
<script>document.getElementById("jebakan").submit();</script>""",
            },
        ],
    },
    {
        "title": "21. Keamanan: Autentikasi vs Otorisasi",
        "sections": [
            {
                "body": [
                    "Dua kata yang mirip, sering tertukar, dan akibat tertukarnya fatal.",
                    "",
                    "  AUTENTIKASI  Siapa kamu?        -> proses login",
                    "  OTORISASI    Kamu boleh apa?    -> pemeriksaan hak akses",
                    "",
                    "Login yang benar tidak ada gunanya kalau setelah masuk semua orang",
                    "bisa melakukan segalanya.",
                    "",
                    "B-iFAMS punya dua peran:",
                    "",
                    "  ADMIN      petugas Fire & Safety. Kelola item, setujui permintaan.",
                    "  REQUESTER  pekerja seksi lain. Mengajukan dan melihat saja.",
                    "",
                    "DUA LAPIS PEMERIKSAAN",
                    "",
                    "  Lapis URL     'siapa pun bukan ADMIN, tolak /items/new'",
                    "  Lapis method  'method ini hanya boleh dipanggil ADMIN'",
                    "",
                    "Dan satu hal yang BUKAN pemeriksaan sama sekali: menyembunyikan",
                    "tombol di tampilan.",
                ]
            },
            {
                "body": [
                    "KISAH NYATA: BUG YANG MEMBUKA SEMUA PINTU",
                    "",
                    "Di B-iFAMS pernah ditemukan hal ini. Semua controller sudah diberi",
                    "penanda hak akses dengan benar:",
                    "",
                    "  @PreAuthorize(\"hasRole('ADMIN')\")",
                    "  public String hapus(...)",
                    "",
                    "Sembilan penanda di ItemController, lima di RequestController, dua",
                    "di CategoryController. Ditulis rapi, tidak ada yang salah ketik.",
                    "",
                    "Tapi seluruhnya TIDAK PERNAH AKTIF.",
                    "",
                    "Penyebabnya letak satu baris konfigurasi. Spring punya dua wadah",
                    "objek: satu untuk aplikasi umum, satu untuk bagian web. Perintah",
                    "yang MENGHIDUPKAN penanda itu ditaruh di wadah pertama, sementara",
                    "controller-nya tinggal di wadah kedua. Mekanisme penghidupnya",
                    "hanya bekerja pada penghuni wadah yang sama.",
                    "",
                    "Akibatnya: setiap orang yang berhasil login - peran apa pun - bisa",
                    "memanggil semua endpoint admin. Tombolnya memang disembunyikan di",
                    "layar, tapi mengetik alamatnya langsung tetap berhasil.",
                    "",
                    "PELAJARANNYA ADA TIGA, DAN KETIGANYA MAHAL",
                    "",
                    "1. Kode yang KELIHATAN benar belum tentu BERJALAN benar.",
                    "   Tidak ada error, tidak ada peringatan, semuanya tampak beres.",
                    "",
                    "2. Menguji sebagai admin tidak membuktikan apa pun tentang hak akses.",
                    "   Admin memang boleh segalanya. Bug ini hanya bisa terlihat kalau",
                    "   diuji dari akun berperan rendah.",
                    "",
                    "3. Jangan bergantung pada satu mekanisme saja.",
                    "   Perbaikannya bukan cuma memindahkan baris itu, tapi juga",
                    "   menambahkan aturan di lapis URL - supaya kalau penanda method",
                    "   mati lagi suatu hari, masih ada yang menahan.",
                ]
            },
            {
                "heading": "Cara membuktikannya - ini yang benar-benar dilakukan",
                "code": """Login sebagai akun berperan REQUESTER, lalu panggil langsung:

  GET  /items/new              -> 403   (ditolak)
  POST /items                  -> 403
  POST /items/1/stock          -> 403
  POST /categories             -> 403
  POST /requests/1/approve     -> 403

Sekaligus pastikan yang boleh TIDAK ikut terkunci:

  GET  /items                  -> 200   (boleh melihat)
  GET  /requests/new           -> 200   (boleh mengajukan)
  POST /requests               -> 400   (ditolak karena data kosong,
                                         BUKAN karena hak akses)"""
            },
            {
                "body": [
                    "Baris terakhir itu penting dan sering dilupakan. Kalau seluruh",
                    "pengujianmu cuma memastikan 'yang dilarang ditolak', kamu bisa",
                    "salah kunci sampai pengguna sah pun tidak bisa bekerja - dan itu",
                    "tetap lolos pengujian.",
                    "",
                    "Uji dua arah: yang dilarang harus ditolak, yang diizinkan harus",
                    "lewat.",
                ]
            },
        ],
    },
    {
        "title": "22. Database di Produksi",
        "sections": [
            {
                "body": [
                    "Database di laptopmu boleh diperlakukan seenaknya. Database",
                    "produksi tidak - isinya pekerjaan orang sungguhan.",
                    "",
                    "SATU PENGATURAN YANG BISA MENGHANCURKAN DIAM-DIAM",
                    "",
                    "Hibernate punya pengaturan bernama hbm2ddl.auto. Nilainya",
                    "menentukan apa yang terjadi pada struktur tabel saat aplikasi start:",
                    "",
                    "  none      jangan sentuh apa pun          <- aman",
                    "  validate  periksa cocok, tolak jalan     <- aman, disarankan",
                    "  update    ubah tabel agar cocok kode     <- BERBAHAYA di produksi",
                    "  create    hapus semua, bikin ulang       <- data lenyap seketika",
                    "",
                    "B-iFAMS dan B-Guest keduanya memakai 'update' di produksi.",
                    "",
                    "Artinya kalau seseorang mengganti nama field di kode Java, Hibernate",
                    "akan menambah kolom baru di tabel Oracle saat aplikasi di-restart,",
                    "dan meninggalkan kolom lama berisi data - tanpa memberi tahu siapa pun.",
                    "",
                    "Yang benar: pakai 'validate', dan setiap perubahan struktur tabel",
                    "ditulis sebagai skrip SQL yang ditinjau, dijalankan sadar-sadar,",
                    "dan disimpan di Git bersama kodenya. Itu namanya migrasi.",
                ]
            },
            {
                "heading": "Flyway: yang mengingat mana skrip yang sudah dijalankan",
                "body": [
                    "Menjalankan skrip SQL satu per satu dengan tangan sanggup bertahan",
                    "sampai skrip kelima. Sesudah itu tidak ada lagi yang ingat mana yang",
                    "sudah masuk di server uji dan mana yang baru di laptop.",
                    "",
                    "Dua alat mengurus persoalan itu: FLYWAY dan LIQUIBASE. Keduanya",
                    "mengerjakan hal yang sama; Flyway yang paling sering kamu temui, dan",
                    "cara kerjanya sederhana sekali.",
                    "",
                    "Skripnya ditaruh sebagai berkas biasa di dalam proyek:",
                    "",
                    "  src/main/resources/db/migration/V1__init.sql",
                    "  src/main/resources/db/migration/V2__tambah_kolom_satuan.sql",
                    "  src/main/resources/db/migration/V3__index_item_kode.sql",
                    "",
                    "Perhatikan bentuk namanya: huruf V, nomor urut, DUA garis bawah, lalu",
                    "keterangan singkat. Bukan hiasan - dari situlah Flyway tahu urutannya.",
                    "",
                    "Saat aplikasi start, Flyway membuka satu tabel bernama",
                    "flyway_schema_history di database itu sendiri, melihat sampai nomor",
                    "berapa yang sudah pernah dijalankan, menjalankan sisanya berurutan,",
                    "lalu mencatat yang baru di tabel yang sama. Database kosong dapat V1",
                    "sampai V3; database yang sudah sampai V2 cuma dapat V3. Kamu tidak",
                    "perlu tahu yang mana - itu justru intinya.",
                    "",
                    "Jadi folder db/migration di repo orang lain BUKAN tumpukan SQL yang",
                    "tidak pernah dipanggil kode mana pun. Ia satu-satunya riwayat resmi",
                    "bentuk tabelmu, dan riwayat itu dijalankan dengan urutan yang sama",
                    "persis di laptop, server uji, dan produksi.",
                    "",
                    "DUA ATURAN YANG MENYERTAINYA, DAN KEDUANYA KERAS",
                    "",
                    "  - Berkas yang SUDAH pernah jalan tidak boleh disunting lagi. Flyway",
                    "    menyimpan sidik jari isinya; mengubah satu spasi pun membuatnya",
                    "    menolak start sambil mengeluh checksum tidak cocok.",
                    "  - Ada yang salah di V2? Jangan perbaiki V2 - tambahkan V4 yang",
                    "    membetulkannya. Server produksi tidak bisa melupakan apa yang",
                    "    sudah terlanjur dijalankan di sana.",
                    "",
                    "Berpasangan dengan hbm2ddl.auto bernilai validate, hasilnya persis yang",
                    "kamu inginkan: Hibernate tidak pernah menyentuh struktur tabel, Flyway",
                    "yang mengubahnya secara sadar dan tercatat, dan Hibernate cuma bertugas",
                    "memeriksa apakah hasilnya masih cocok dengan kode.",
                ]
            },
            {
                "body": [
                    "SATU HAL LAGI: JANGAN SAMPAI SALAH DATABASE",
                    "",
                    "Ini kejadian sungguhan saat audit B-iFAMS.",
                    "",
                    "Di server aplikasi ada kontainer Docker bernama bifams-pg, berisi",
                    "database dengan nama tabel yang sama persis: app_user, item,",
                    "item_request. Sekilas itulah database aplikasinya.",
                    "",
                    "Ternyata bukan. Itu sisa versi lama yang belum dimatikan, dan",
                    "isinya kosong. Database yang sesungguhnya dipakai ada di MESIN LAIN,",
                    "memakai Oracle, bukan PostgreSQL.",
                    "",
                    "Akun uji yang dibuat ke sana tidak pernah bisa dipakai login, dan",
                    "butuh waktu cukup lama untuk sadar penyebabnya.",
                    "",
                    "CARA MENGHINDARINYA",
                    "",
                    "Jangan menebak dari nama. Baca konfigurasi aplikasi yang SEDANG",
                    "BERJALAN:",
                    "",
                    "  jdbc.url=jdbc:oracle:thin:@//10.10.1.187:1521/XE",
                    "  jdbc.username=BIFAMS_FS",
                    "",
                    "Baris itu sumber kebenarannya. Bukan nama kontainer, bukan ingatan,",
                    "bukan dokumentasi - karena dokumentasinya waktu itu juga salah.",
                    "",
                    "Dan sebelum mengubah data, buktikan dulu kamu di tempat yang benar:",
                    "cari satu baris yang kamu tahu pasti ada. Kalau tidak ketemu,",
                    "berarti kamu salah database.",
                ]
            },
        ],
    },
    {
        "title": "23. Satu Kode, Banyak Lingkungan: Konfigurasi dan Rahasia",
        "sections": [
            {
                "body": [
                    "Kode yang sama harus jalan di tiga tempat: laptopmu, server uji, dan",
                    "server produksi. Yang berbeda di antara ketiganya sedikit sekali, dan",
                    "tidak satu pun berupa logika:",
                    "",
                    "  alamat database   di laptop database kecil sendiri, di produksi Oracle",
                    "  tingkat log       di laptop catat semuanya, di produksi yang penting saja",
                    "  alamat surel      di laptop ke kotak uji, di produksi ke orang sungguhan",
                    "  kunci layanan     akun percobaan di laptop, akun berbayar di produksi",
                    "",
                    "Kalau nilai-nilai itu diketik langsung di dalam kode Java, kamu punya",
                    "dua pilihan yang sama-sama buruk: menyunting kode setiap kali deploy,",
                    "atau memelihara dua salinan kode yang perlahan menyimpang.",
                    "",
                    "Karena itu yang BERBEDA-BEDA dikeluarkan dari kode, ke berkas",
                    "konfigurasi. Kamu sudah melihat satu barisnya di materi sebelumnya:",
                    "",
                    "  jdbc.url=jdbc:oracle:thin:@//10.10.1.187:1521/XE",
                    "",
                    "Baris itu bukan kode. Ia data, dan tempatnya di src/main/resources/.",
                    "",
                    "TIGA ISTILAH YANG AKAN KAMU TEMUI",
                    "",
                    "  Lingkungan   satu tempat aplikasi berjalan: laptop, uji, produksi.",
                    "  Profil       nama satu set nilai konfigurasi untuk lingkungan itu.",
                    "  Rahasia      nilai yang tidak boleh dilihat orang lain: sandi, kunci.",
                    "",
                    "Dua yang pertama soal kerapian. Yang ketiga soal keamanan, dan salah",
                    "menanganinya adalah salah satu kebocoran yang paling sering terjadi di",
                    "GitHub.",
                ],
            },
            {
                "heading": "Satu berkas per lingkungan",
                "body": [
                    "Spring Boot sudah menyediakan mekanisme profil: berkas bernama",
                    "application-<profil>.properties otomatis dipakai kalau profil itu",
                    "aktif, menimpa nilai yang sama di application.properties.",
                    "",
                    "Susunan lama seperti B-iFAMS (Spring 4 + XML) tidak punya mekanisme",
                    "itu. Padanannya dikerjakan tangan: satu berkas jdbc.properties per",
                    "lingkungan, dan yang benar disalin ke server saat deploy. Bentuknya",
                    "beda, masalahnya sama persis.",
                ],
                "code": """src/main/resources/
  application.properties          <- berlaku untuk semua lingkungan
  application-dev.properties      <- dipakai hanya saat profil dev aktif
  application-prod.properties     <- dipakai hanya saat profil prod aktif

# ---- application.properties
app.nama=B-iFAMS
spring.profiles.active=dev

# ---- application-dev.properties
jdbc.url=jdbc:h2:mem:bifams
jdbc.username=sa
jdbc.password=
log.level=DEBUG

# ---- application-prod.properties
jdbc.url=jdbc:oracle:thin:@//10.10.1.187:1521/XE
jdbc.username=BIFAMS_FS
jdbc.password=${DB_PASSWORD}
log.level=WARN

# Memilih profil saat menjalankan, tanpa menyentuh satu berkas pun:
java -jar bifams.jar --spring.profiles.active=prod""",
            },
            {
                "heading": "Membaca nilainya dari kode",
                "body": [
                    "Berkas konfigurasi baru berguna kalau kode bisa membacanya. Ada dua",
                    "cara, dan keduanya akan kamu temui saat membaca proyek orang lain.",
                    "",
                    "  @Value                    ambil SATU nilai ke satu field.",
                    "  @ConfigurationProperties  ambil SEKELOMPOK nilai ke satu objek.",
                    "",
                    "Yang kedua dipakai kalau kuncinya berawalan sama. Sepuluh @Value",
                    "berawalan smtp. lebih enak jadi satu kelas berisi sepuluh field.",
                    "",
                    "SATU JEBAKAN BACA: ${...} DI SINI BUKAN ${...} DI JSP",
                    "",
                    "Bentuknya sama persis, artinya berbeda. Di JSP ${item.nama} adalah",
                    "nilai yang dikirim controller ke halaman. Di konfigurasi, ${jdbc.url}",
                    "adalah kunci di berkas properties atau nama variabel lingkungan.",
                    "Keduanya diselesaikan oleh mesin yang berbeda, pada waktu yang",
                    "berbeda pula.",
                ],
                "code": """@Component
public class KonfigurasiDatabase {

    @Value("${jdbc.url}")
    private String url;

    // Tanda titik dua memberi nilai cadangan: dipakai kalau kuncinya
    // memang tidak ada. Tanpa itu, aplikasi gagal start.
    @Value("${jdbc.pool.max:10}")
    private int maksKoneksi;
}

// Sekelompok nilai sekaligus: semua kunci berawalan "smtp."
@Component
@ConfigurationProperties(prefix = "smtp")
public class SmtpProperties {

    private String host;      // smtp.host
    private int port;         // smtp.port
    private String username;  // smtp.username

    // Getter dan setter wajib ada - lewat setter itulah Spring mengisinya.
}""",
            },
            {
                "heading": "Rahasia diisi saat dijalankan, bukan disimpan",
                "body": [
                    "Lihat lagi baris jdbc.password di berkas prod tadi. Yang tertulis di",
                    "situ cuma ${DB_PASSWORD}, bukan sandinya. Sandi aslinya tidak ada di",
                    "berkas mana pun di dalam proyek; ia dipasang di server sebagai",
                    "variabel lingkungan, lalu dibaca saat aplikasi dinyalakan:",
                    "",
                    "  export DB_PASSWORD='...'    lalu jalankan aplikasinya",
                    "",
                    "Program di bawah ini mengerjakan dengan tangan apa yang Spring",
                    "lakukan diam-diam. Jalankan, dan perhatikan baris terakhirnya.",
                ],
                "code": """import java.util.Map;
import java.util.Properties;

// Meniru cara Spring mengisi ${NAMA} dari variabel lingkungan saat start.
public class IsiPlaceholder {

    static String isi(String nilai, Map<String, String> lingkungan) {
        int awal = nilai.indexOf("${");
        if (awal < 0) return nilai;              // tidak ada placeholder
        int tutup = nilai.indexOf('}', awal);
        String nama = nilai.substring(awal + 2, tutup);

        String dari = lingkungan.get(nama);
        if (dari == null)
            throw new IllegalStateException(
                    "Variabel lingkungan " + nama + " belum diisi");

        return nilai.substring(0, awal) + dari + nilai.substring(tutup + 1);
    }

    public static void main(String[] args) {
        // Isi application-prod.properties, dibaca apa adanya.
        Properties konfig = new Properties();
        konfig.setProperty("jdbc.url",
                           "jdbc:oracle:thin:@//10.10.1.187:1521/XE");
        konfig.setProperty("jdbc.username", "BIFAMS_FS");
        konfig.setProperty("jdbc.password", "${DB_PASSWORD}");

        // Di server sungguhan isinya datang dari System.getenv().
        Map<String, String> lingkungan =
                Map.of("DB_PASSWORD", "sandi-dari-server");

        String[] kunci = {"jdbc.url", "jdbc.username", "jdbc.password"};
        for (String k : kunci) {
            String hasil = isi(konfig.getProperty(k), lingkungan);
            System.out.println(k + " = " + hasil);
        }

        // Variabel yang belum dipasang: aplikasi harus BERHENTI di sini,
        // bukan jalan terus lalu gagal saat pengguna pertama memakainya.
        try {
            isi("${SMTP_PASSWORD}", lingkungan);
        } catch (IllegalStateException e) {
            System.out.println("gagal start: " + e.getMessage());
        }
    }
}""",
            },
            {
                "body": [
                    "KENAPA SEREPOT ITU? KARENA SELURUH FOLDER PROYEK MASUK GIT",
                    "",
                    "Git dibaca banyak orang, disalin ke banyak laptop, dan sering diunggah",
                    "ke tempat yang bisa dilihat publik. Sandi produksi yang ikut di dalam",
                    "salah satu berkasnya ikut ke semua tempat itu sekaligus.",
                    "",
                    "DAN KALAU TELANJUR MASUK, MENGHAPUS BERKASNYA TIDAK CUKUP",
                    "",
                    "Ini bagian yang paling sering salah dimengerti. Git menyimpan RIWAYAT.",
                    "Menghapus baris sandinya lalu commit lagi cuma menambah satu commit",
                    "baru; commit yang lama masih ada, lengkap dengan sandinya, dan siapa",
                    "pun yang sudah menyalin repo itu bisa membacanya kapan saja.",
                    "",
                    "Satu-satunya langkah yang benar-benar menutup lubangnya: GANTI",
                    "SANDINYA. Membersihkan riwayat Git boleh dikerjakan sesudahnya, tapi",
                    "selama sandi lama masih berlaku, kebocorannya belum berhenti.",
                    "",
                    "BENTUK YANG LAZIM DI PROYEK JAVA",
                    "",
                    "Berkas .gitignore berisi daftar yang Git harus abaikan:",
                    "",
                    "  target/                       hasil rakitan, bisa dibuat ulang",
                    "  *.war                         sama, dan ukurannya puluhan MB",
                    "  application-local.properties  konfigurasi pribadi tiap orang",
                    "  jdbc.properties               berisi sandi - jangan pernah masuk",
                    "  .idea/  *.iml  .vscode/       setelan editor, bukan bagian aplikasi",
                    "",
                    "Materi Maven menyebut 'target/ jangan disimpan di Git'. Berkas inilah",
                    "cara memberitahunya.",
                    "",
                    "Tapi kalau berkas konfigurasinya diabaikan, orang berikutnya tidak tahu",
                    "kunci apa saja yang harus diisi. Karena itu satu berkas CONTOH tetap",
                    "ikut disimpan:",
                    "",
                    "  application-example.properties   (atau jdbc.properties.example)",
                    "    jdbc.url=jdbc:oracle:thin:@//ALAMAT:1521/XE",
                    "    jdbc.username=NAMA_USER",
                    "    jdbc.password=ISI_DI_SINI",
                    "",
                    "Isinya bentuk kuncinya, bukan nilainya. Langkah pertama menyiapkan",
                    "proyek di laptop baru: salin berkas contohnya, buang akhiran contohnya,",
                    "lalu isi nilainya sendiri.",
                    "",
                    "'KONFIGURASINYA KOK TIDAK ADA DI REPO?'",
                    "",
                    "Memang sengaja tidak ada, dan sekarang kamu tahu kenapa. Yang ada di",
                    "repo cuma berkas contohnya.",
                    "",
                    "Akibatnya langsung terasa di pekerjaan: kalau kamu perlu tahu database",
                    "mana yang DIPAKAI aplikasi yang sedang berjalan, jawabannya tidak ada",
                    "di source code. Jangan pula menebak dari nama kontainer - itu persis",
                    "kesalahan yang membuang waktu di materi sebelumnya. Cari di mesin yang",
                    "menjalankannya:",
                    "",
                    "  ps aux | grep java         argumen -D dan --spring.profiles.active",
                    "  cat /proc/<pid>/environ    variabel lingkungan proses itu",
                    "  berkas properties di dalam aplikasi yang sudah terhampar di server",
                    "",
                    "URUTAN MENANGNYA, DAN INI SERING MENGECOH",
                    "",
                    "  baris perintah  >  variabel lingkungan  >  isi berkas properties",
                    "",
                    "Yang paling dekat ke saat menjalankan selalu menang. Artinya berkas",
                    "properties yang barusan kamu baca bisa saja BUKAN nilai yang sedang",
                    "dipakai - karena satu argumen di baris perintah diam-diam menimpanya.",
                ],
            },
        ],
    },
    {
        "title": "24. Dua Pengguna Bersamaan: Race Condition dan Penguncian",
        "sections": [
            {
                "body": [
                    "Materi pertama mengajukan empat pertanyaan yang katanya mengubah skrip",
                    "lima baris jadi aplikasi puluhan berkas. Tiga sudah dijawab sepanjang",
                    "modul ini:",
                    "",
                    "  Ke mana angkanya kalau program mati?          -> database.",
                    "  Siapa yang mengurangi, kapan, kenapa?         -> tabel mutasi dan log.",
                    "  Bagaimana kalau diminta 999 padahal stok 20?  -> aturan di service.",
                    "",
                    "Yang keempat digantung sampai sekarang:",
                    "",
                    "  Kalau dua petugas mengurangi stok bersamaan, siapa yang menang?",
                    "",
                    "Jawabannya tidak enak. Bisa jadi TIDAK ADA yang menang, dan salah satu",
                    "pencatatan lenyap tanpa satu pun pesan error.",
                    "",
                    "URUTAN WAKTU YANG MERUSAKNYA",
                    "",
                    "Stok awal 20. Petugas A mencatat keluar 5, petugas B juga keluar 5.",
                    "Keduanya menekan tombol pada detik yang sama.",
                    "",
                    "  waktu  Permintaan A            Permintaan B            stok di tabel",
                    "  -----  ---------------------  ---------------------   -------------",
                    "    1    SELECT stok  -> 20                                    20",
                    "    2                           SELECT stok  -> 20             20",
                    "    3    hitung 20 - 5 = 15                                    20",
                    "    4                           hitung 20 - 5 = 15             20",
                    "    5    UPDATE stok = 15                                      15",
                    "    6                           UPDATE stok = 15               15",
                    "",
                    "Dua mutasi keluar tercatat di tabel mutasi. Stok cuma berkurang lima.",
                    "Lima unit barang hilang dari catatan, dan tidak ada baris log mana pun",
                    "yang menandainya. Ketahuannya berbulan-bulan kemudian saat stok opname,",
                    "waktu angka di rak tidak cocok dengan angka di layar.",
                    "",
                    "Nama kejadiannya LOST UPDATE: tulisan B menimpa tulisan A tanpa pernah",
                    "melihatnya. Nama keluarga besarnya RACE CONDITION - hasilnya ditentukan",
                    "siapa yang kebetulan lebih cepat, bukan oleh aturan yang kamu tulis.",
                ],
            },
            {
                "heading": "Membuktikannya sendiri: dua thread, satu angka",
                "body": [
                    "Selama belum pernah melihatnya, bug ini terasa seperti kekhawatiran",
                    "berlebihan. Program di bawah memerasnya keluar dengan sengaja.",
                    "",
                    "Dua thread mewakili dua permintaan HTTP yang datang bersamaan. Keduanya",
                    "menjalankan pola yang PERSIS sama dengan kode setujui() di materi",
                    "Service: baca stok, hitung di Java, tulis kembali.",
                    "",
                    "CyclicBarrier di situ cuma alat pemaksa. Ia menahan kedua thread sampai",
                    "sama-sama selesai membaca, supaya kejadian yang di server asli mungkin",
                    "cuma muncul sekali sebulan bisa kamu lihat setiap kali dijalankan.",
                ],
                "code": """import java.util.concurrent.CyclicBarrier;

public class StokBalapan {

    // Anggap ini kolom stok di tabel item: satu angka, dipakai bersama.
    private static int stok = 20;

    // Penahan supaya keduanya membaca dulu sebelum ada yang menulis.
    private static final CyclicBarrier BARENGAN = new CyclicBarrier(2);

    // Satu permintaan HTTP: catat barang keluar 5 unit.
    private static void catatKeluarLima() {
        try {
            int dibaca = stok;       // 1. BACA   -> keduanya dapat 20
            BARENGAN.await();        //    di server, ini cuma jeda biasa
            int hasil = dibaca - 5;  // 2. HITUNG di Java -> keduanya 15
            stok = hasil;            // 3. TULIS  -> keduanya menulis 15
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) throws Exception {
        Thread petugasA = new Thread(StokBalapan::catatKeluarLima);
        Thread petugasB = new Thread(StokBalapan::catatKeluarLima);
        petugasA.start();
        petugasB.start();
        petugasA.join();
        petugasB.join();

        System.out.println("Stok awal          : 20");
        System.out.println("Dua mutasi keluar  : 5 dan 5");
        System.out.println("Stok seharusnya    : 10");
        System.out.println("Stok yang tercatat : " + stok);
        System.out.println();
        System.out.println("Satu mutasi hilang. Tanpa error, tanpa jejak.");
    }
}""",
            },
            {
                "heading": "Dua jenis penguncian, dan kenapa @Transactional bukan salah satunya",
                "body": [
                    "Pertanyaan pertama yang selalu muncul: bukankah @Transactional dari",
                    "materi Service sudah mengurus ini?",
                    "",
                    "Tidak. Transaksi menjamin SEMUA-ATAU-TIDAK-SAMA-SEKALI: kalau langkah",
                    "kelima gagal, empat langkah sebelumnya ikut dibatalkan. Itu perlindungan",
                    "terhadap GAGAL DI TENGAH JALAN, bukan terhadap dua penulis yang",
                    "masing-masing berhasil sempurna.",
                    "",
                    "Lihat lagi tabel waktu tadi: tidak ada yang gagal di sana. A sukses, B",
                    "sukses, dua-duanya commit dengan tenang. Datanya rusak justru KARENA",
                    "semuanya berhasil. Isolation level bawaan Oracle, PostgreSQL, dan MySQL",
                    "membiarkan urutan itu lolos apa adanya.",
                    "",
                    "OPTIMISTIC LOCKING - BERBAIK SANGKA, TAPI MEMERIKSA",
                    "",
                    "Disebut optimistic karena tidak melarang siapa pun membaca. Ia cuma",
                    "memasang penanda supaya penulis yang datanya sudah basi ketahuan.",
                    "",
                    "Tambahkan satu kolom di tabel:",
                    "",
                    "  ALTER TABLE item ADD version NUMBER DEFAULT 0 NOT NULL;",
                    "",
                    "lalu satu field bertanda @Version di entitasnya. Inilah jawaban kolom",
                    "version yang selama ini kamu lihat di banyak tabel tanpa tahu gunanya.",
                    "",
                    "PESSIMISTIC LOCKING - MENGANTRE DI DEPAN BARISNYA",
                    "",
                    "Kebalikannya: barisnya dikunci lebih dulu, jadi tidak ada yang perlu",
                    "diulang karena tidak ada yang sempat bentrok. Harganya nyata:",
                    "permintaan lain BERHENTI MENUNGGU sampai transaksimu selesai, dan kalau",
                    "dua transaksi mengunci beberapa baris dengan urutan berlawanan, keduanya",
                    "saling menunggu selamanya - itulah deadlock. Penangkalnya: kunci dalam",
                    "urutan yang selalu sama, misalnya urut id, dan jaga transaksinya pendek.",
                ],
                "code": """@Entity
@Table(name = "item")
public class Item {

    @Id
    private Long id;

    private int stok;

    @Version                 // Hibernate yang mengisi. Jangan diset sendiri.
    private Long version;

    // getter & setter seperti biasa
}

// Sejak ada @Version, UPDATE yang dikirim Hibernate berbunyi begini:
//
//     UPDATE item SET stok = 15, version = 8
//      WHERE id = 61 AND version = 7
//
// Permintaan A menang: version di baris itu masih 7, 1 baris berubah.
// Permintaan B kalah : version sudah jadi 8, 0 baris berubah, dan Hibernate
//                      melempar OptimisticLockException.


// Versi pessimistic: kunci dulu, baru hitung. Wajib di dalam transaksi.
@Transactional
public void kurangiStok(Long itemId, int jumlah) {
    Item item = em.find(Item.class, itemId, LockModeType.PESSIMISTIC_WRITE);
    // SQL-nya: SELECT ... FROM item WHERE id = ? FOR UPDATE
    // Permintaan lain atas baris yang SAMA tertahan di baris ini sampai
    // transaksi ini commit atau rollback.

    if (item.getStok() < jumlah)
        throw new AturanDilanggar("Stok tidak mencukupi.");

    item.setStok(item.getStok() - jumlah);
}""",
            },
            {
                "heading": "Yang kalah harus diberi tahu, dan sering database yang pantas menghitung",
                "body": [
                    "OptimisticLockException itu kabar baik: aplikasimu berhasil menolak",
                    "penimpaan. Yang menentukan bagus atau tidaknya adalah apa yang kamu",
                    "lakukan sesudahnya.",
                    "",
                    "  JANGAN  ditelan diam-diam lalu disimpan ulang paksa. Itu sama saja",
                    "          kembali ke lost update, cuma sekarang kamu yang menyuruhnya.",
                    "  JANGAN  cuma menampilkan \"Terjadi kesalahan sistem\". Petugasnya akan",
                    "          menekan tombol yang sama lagi dengan data yang sama basinya.",
                    "  LAKUKAN suruh dia MEMUAT ULANG dan memutuskan dengan angka terbaru.",
                    "",
                    "Mengulang otomatis boleh, tapi hanya untuk operasi yang aman diulang -",
                    "misalnya menambah stok - dan dengan batas percobaan. Untuk keputusan",
                    "yang butuh pertimbangan manusia, manusianya yang harus melihat angka",
                    "barunya. Di Spring, exception JPA itu dibungkus jadi",
                    "ObjectOptimisticLockingFailureException.",
                    "",
                    "CARA KETIGA: BIARKAN DATABASE YANG MENGHITUNG",
                    "",
                    "Semua kerumitan tadi berakar pada satu hal: hitungannya dilakukan di",
                    "Java, di antara SELECT dan UPDATE. Kalau pengurangannya ditulis di dalam",
                    "UPDATE itu sendiri, celahnya hilang - database mengunci barisnya sendiri",
                    "selama satu pernyataan, dan syarat stok >= jumlah diperiksa SAAT ITU,",
                    "bukan semenit sebelumnya.",
                    "",
                    "Periksa JUMLAH BARIS yang berubah. Nol berarti syaratnya tak terpenuhi,",
                    "dan itu penolakan yang sah - bukan error tak terduga.",
                    "",
                    "Satu jebakan lanjutan: setelah UPDATE mentah begini, objek Item yang",
                    "masih dipegang Hibernate jadi basi. Jangan menyimpannya lagi dalam",
                    "transaksi yang sama; ambil ulang kalau memang masih dibutuhkan.",
                ],
                "code": """// --- DAO: satu pernyataan, tidak ada celah di tengah ---------------------
public int kurangiStok(Long itemId, int jumlah) {
    return em.createNativeQuery(
            "UPDATE item SET stok = stok - ?, version = version + 1 "
          + " WHERE id = ? AND stok >= ?")
        .setParameter(1, jumlah)
        .setParameter(2, itemId)
        .setParameter(3, jumlah)
        .executeUpdate();          // berapa baris yang benar-benar berubah
}

// --- Service: nol baris = ditolak, bukan error ---------------------------
@Transactional
public void catatKeluar(Long itemId, int jumlah, String namaPetugas) {
    int baris = itemDao.kurangiStok(itemId, jumlah);
    if (baris == 0)
        throw new AturanDilanggar("Stok tidak mencukupi, muat ulang.");

    catatMutasi(itemId, MovementType.OUT, jumlah, namaPetugas);
}

// --- Controller: yang kalah diberi kalimat yang bisa ditindaklanjuti -----
try {
    stockService.catatKeluar(id, qty, petugasLogin());
    ra.addFlashAttribute("success", "Mutasi tersimpan.");
} catch (ObjectOptimisticLockingFailureException e) {
    ra.addFlashAttribute("error",
            "Data item ini baru saja diubah petugas lain. "
          + "Muat ulang halaman, periksa stoknya, lalu coba lagi.");
}""",
            },
            {
                "body": [
                    "KENAPA BUG INI SELALU LOLOS PENGUJIAN",
                    "",
                    "Karena kamu mengujinya sendirian. Satu orang mengklik satu tombol tidak",
                    "akan pernah balapan dengan siapa pun. Bug ini menunggu hari sibuk -",
                    "tutup bulan, atau pagi setelah kiriman barang datang - lalu muncul",
                    "sebagai selisih stok yang tidak bisa dijelaskan siapa-siapa.",
                    "",
                    "Jadi jangan tunggu. Pancing sendiri, persis seperti program dua thread",
                    "tadi, tapi kali ini menembak service dan database sungguhan:",
                    "",
                    "  - dua thread, masing-masing memanggil service lewat KONEKSI SENDIRI",
                    "  - tahan keduanya dengan CountDownLatch supaya berangkat berbarengan",
                    "  - setelah keduanya selesai, baca ulang stok dari database",
                    "  - stok akhir harus 10, atau salah satunya ditolak dengan jelas",
                    "",
                    "Menguji ini memakai DAO memori tidak membuktikan apa-apa: yang sedang",
                    "diuji justru perilaku databasenya.",
                    "",
                    "JEBAKAN: MENGIRA synchronized MENYELESAIKANNYA",
                    "",
                    "Menaruh synchronized di method service memang menutup demo dua thread",
                    "tadi, dan itulah yang membuatnya berbahaya - ia terlihat berhasil.",
                    "Padahal ia hanya mengunci SATU JVM. Begitu aplikasinya dijalankan di dua",
                    "Tomcat di belakang load balancer, atau ada job batch, atau ada orang",
                    "menjalankan UPDATE lewat SQL, kunci itu tidak dilihat siapa pun.",
                    "",
                    "Cuma database yang melihat SEMUA penulis. Karena itu penjaganya harus",
                    "duduk di sana - di kolom version, di FOR UPDATE, atau di syarat WHERE.",
                    "",
                    "Materi Bean sudah menyebut satu tetangga dekat masalah ini: bean Spring",
                    "dibuat tunggal, jadi menyimpan data satu pengguna di field service",
                    "adalah bug yang menunggu giliran. Sekarang alasannya lengkap - objek",
                    "service itu memang dipakai semua permintaan secara bersamaan.",
                    "",
                    "RINGKASAN MEMILIH",
                    "",
                    "  Satu UPDATE yang menghitung sendiri   aturannya muat dalam satu",
                    "                                        WHERE. Termurah dan paling",
                    "                                        sederhana; coba ini dulu.",
                    "",
                    "  Optimistic (@Version)                 perubahannya menyentuh banyak",
                    "                                        field, atau formnya lama dibuka",
                    "                                        sebelum disimpan. Bentrokan",
                    "                                        jarang, mengulang pun murah.",
                    "",
                    "  Pessimistic (FOR UPDATE)              bentrokan sering dan mengulang",
                    "                                        tidak boleh terjadi. Bayarannya",
                    "                                        antrean; jaga transaksi pendek.",
                    "",
                    "Yang tidak boleh dipilih cuma satu: menganggap kejadian ini terlalu",
                    "jarang untuk diurus. Ia tidak jarang, ia cuma sunyi.",
                ],
            },
        ],
    },
    {
        "title": "25. Kontainer: Docker dan docker-compose",
        "sections": [
            {
                "body": [
                    "Materi Deploy mengajarkan satu cara memindahkan aplikasi: salin",
                    ".war ke folder webapps, matikan Tomcat, nyalakan lagi. Cara itu",
                    "masih banyak dipakai dan tidak salah. Tapi ia diam-diam berasumsi",
                    "bahwa servernya sudah punya Java versi yang tepat, Tomcat versi",
                    "yang tepat, dan setelan sistem yang sama dengan laptopmu.",
                    "",
                    "Kalau satu saja asumsi itu meleset, kamu masuk ke percakapan yang",
                    "paling melelahkan di pekerjaan ini: \"di laptopku jalan kok\".",
                    "",
                    "Yang biasanya jadi biang keroknya:",
                    "",
                    "  - Java 17 di laptop, Java 8 di server",
                    "    -> UnsupportedClassVersionError saat start",
                    "  - PostgreSQL 16 di laptop, 13 di server",
                    "    -> query yang tadinya jalan mendadak ditolak",
                    "  - zona waktu server UTC, laptop WIB",
                    "    -> jam yang tersimpan meleset 7 jam",
                    "  - Windows tidak membedakan huruf besar-kecil nama berkas,",
                    "    Linux membedakan -> Logo.png tidak ketemu di server",
                    "",
                    "Kontainer menutup celah itu dengan satu ide sederhana: yang dikirim",
                    "ke server bukan cuma aplikasimu, tapi aplikasimu BESERTA lingkungan",
                    "tempat ia berjalan - versi Java, isi foldernya, variabel",
                    "lingkungannya, sampai perintah yang menjalankannya. Semua sudah",
                    "ditentukan sejak di laptop dan dibekukan jadi satu paket.",
                    "",
                    "IMAGE VERSUS KONTAINER",
                    "",
                    "Dua kata ini terus tertukar, padahal bedanya persis seperti kelas",
                    "dan objek di Java.",
                    "",
                    "  IMAGE      Hasil build. Satu paket beku berisi sistem berkas",
                    "             lengkap: Java, aplikasimu, dan segalanya. Read-only.",
                    "             Punya nama dan tag, misalnya postgres:16.",
                    "",
                    "  KONTAINER  Satu instansi image yang SEDANG BERJALAN. Seperti",
                    "             hasil new, satu image bisa dijalankan jadi lima",
                    "             kontainer sekaligus dan masing-masing punya",
                    "             hidupnya sendiri.",
                    "",
                    "  image -> kontainer      sama seperti      class -> objek",
                    "",
                    "KONTAINER YANG MATI KEHILANGAN ISINYA",
                    "",
                    "Ini yang paling sering menyakiti pemula. Apa pun yang ditulis ke",
                    "dalam kontainer saat ia berjalan - berkas unggahan, isi database,",
                    "log - tersimpan di lapisan tulis milik kontainer ITU, bukan di",
                    "image-nya. Hapus kontainernya, lapisan itu ikut hilang.",
                    "",
                    "Jadi kalau suatu pagi seluruh isi database \"hilang sendiri\" padahal",
                    "tidak ada yang menghapus apa pun, tersangka pertamanya ini:",
                    "kontainer database dibuat ulang, dan datanya memang tidak pernah",
                    "disimpan di luar kontainer.",
                    "",
                    "Obatnya VOLUME - folder yang hidup di luar kontainer lalu",
                    "dipasangkan ke dalamnya. Kontainernya boleh dibuang dan dibuat",
                    "ulang berkali-kali; isi volume tetap.",
                ],
            },
            {
                "heading": "Dockerfile: resep membangun image aplikasi Java",
                "body": [
                    "TIGA HAL YANG BIKIN BERKAS ITU MASUK AKAL",
                    "",
                    "1. Tiap baris FROM, COPY, dan RUN menghasilkan satu LAPISAN yang",
                    "   disimpan di cache. Docker memakai ulang lapisan selama",
                    "   masukannya tidak berubah. Itu sebabnya pom.xml disalin sebelum",
                    "   src: mengubah satu baris kode Java tidak memaksa Maven",
                    "   mengunduh ulang seluruh dependensi.",
                    "",
                    "2. Ada DUA kali FROM karena alat untuk MEMBANGUN tidak dibutuhkan",
                    "   untuk MENJALANKAN. Image satu tahap ikut membawa Maven, seluruh",
                    "   source, dan folder ~/.m2. Yang menyeberang ke image akhir cuma",
                    "   yang disalin dengan COPY --from: satu berkas .jar.",
                    "",
                    "   Bedanya diukur dengan proyek main-main berisi satu kelas saja:",
                    "   838 MB satu tahap, 424 MB dua tahap. Proyek sungguhan dengan",
                    "   puluhan dependensi melebarkan jarak itu, bukan mempersempitnya.",
                    "",
                    "3. Tahap akhir memakai -jre, bukan -jdk. Compiler tidak perlu ada",
                    "   di server. Makin sedikit yang terpasang, makin sedikit yang bisa",
                    "   bermasalah dan makin sedikit yang perlu ditambal.",
                    "",
                    "Perhatikan juga mvn package di tahap 1 ikut menjalankan uji",
                    "otomatis. Kalau ada uji yang gagal, build berhenti dan image-nya",
                    "tidak pernah jadi - versi yang rusak tidak punya jalan ke server.",
                    "",
                    "JEBAKAN: BENTUK ENTRYPOINT",
                    "",
                    "  ENTRYPOINT [\"java\", \"-jar\", \"/app/app.jar\"]   <- bentuk daftar",
                    "  ENTRYPOINT java -jar /app/app.jar             <- bentuk kalimat",
                    "",
                    "Bentuk daftar menjalankan java langsung sebagai proses nomor 1 di",
                    "dalam kontainer. Bentuk kalimat membungkusnya dengan /bin/sh, dan",
                    "sh-lah yang jadi proses nomor 1. Akibatnya docker stop mengirim",
                    "sinyal berhenti ke sh, bukan ke Java: aplikasi tidak sempat menutup",
                    "koneksi database baik-baik, lalu dibunuh paksa setelah 10 detik.",
                    "",
                    "Berkas .dockerignore selalu menemani Dockerfile. Tanpa itu, target/",
                    "dan .git/ ikut terkirim setiap kali kamu build - lambat, dan",
                    "target/ berisi hasil rakitan LAMA yang tidak ada urusannya.",
                ],
                "code": """# ===== File: Dockerfile =====

# ---- Tahap 1: rakit. Perlu Maven dan seluruh source code. ----
FROM maven:3.9-eclipse-temurin-17 AS rakit
WORKDIR /src

# pom.xml disalin sendirian dulu. Selama pom.xml tidak berubah,
# hasil unduhan dependensinya dipakai ulang dari cache.
COPY pom.xml .
RUN mvn -B dependency:go-offline

COPY src ./src
RUN mvn -B clean package

# ---- Tahap 2: jalankan. Cukup JRE, tanpa Maven, tanpa source. ----
FROM eclipse-temurin:17-jre
WORKDIR /app

COPY --from=rakit /src/target/bifams.jar /app/app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]


# ===== File: .dockerignore =====
target/
.git/
*.war
application-local.properties""",
            },
            {
                "heading": "docker-compose.yml: aplikasi dan database sekali jalan",
                "body": [
                    "Satu perintah, docker compose up, menyalakan dua kontainer, membuat",
                    "jaringan pribadi buat mereka berdua, dan menyambungkannya. Lima",
                    "bagian berkas itu yang wajib dimengerti.",
                    "",
                    "NAMA LAYANAN JADI NAMA HOST",
                    "",
                    "Lihat jdbc:postgresql://db:5432/bifams. Kata \"db\" di situ bukan",
                    "singkatan basa-basi - itu nama layanan di berkas ini, dan di dalam",
                    "jaringan compose nama layanan otomatis berlaku sebagai nama host.",
                    "",
                    "Jebakan yang hampir semua orang kena sekali: menyalin URL dari",
                    "laptop yang berbunyi localhost:5432, lalu bingung kenapa hasilnya",
                    "Connection refused. Di dalam kontainer app, localhost adalah",
                    "kontainer app itu sendiri - bukan mesinmu, bukan kontainer db.",
                    "",
                    "PORTS: KIRI MESINMU, KANAN DALAM KONTAINER",
                    "",
                    "\"8080:8080\" meneruskan port 8080 di mesinmu ke port 8080 di dalam",
                    "kontainer app. Kalau 8080 sudah dipakai Tomcat lain, ganti yang",
                    "kirinya saja jadi \"9090:8080\" - isi kontainernya tidak perlu tahu.",
                    "",
                    "Perhatikan layanan db sengaja TIDAK punya ports. Ia tetap dijangkau",
                    "app lewat jaringan compose, tapi tidak terbuka ke jaringan luar.",
                    "",
                    "VOLUMES: BARIS YANG MENYELAMATKAN DATAMU",
                    "",
                    "data-db:/var/lib/postgresql/data memasang volume bernama data-db ke",
                    "folder tempat PostgreSQL menaruh datanya. Tanpa baris itu, yang",
                    "tadi dibahas di bagian pertama benar-benar terjadi: kontainer db",
                    "dibuat ulang, semua data ikut hilang.",
                    "",
                    "ENVIRONMENT: SANDI TIDAK DITULIS DI SINI",
                    "",
                    "${DB_PASSWORD} diisi dari berkas .env di sebelah docker-compose.yml,",
                    "dan .env masuk .gitignore. Alasannya sudah dibahas di materi",
                    "Konfigurasi dan Rahasia; yang penting di sini, docker-compose.yml",
                    "sendiri aman di-commit karena isinya tidak memuat sandi apa pun.",
                    "",
                    "DEPENDS_ON SAJA TIDAK CUKUP",
                    "",
                    "depends_on polos cuma menunggu kontainer db NYALA, bukan menunggu",
                    "PostgreSQL siap menerima koneksi - dan jarak antara keduanya bisa",
                    "beberapa detik. Aplikasi Java start lebih cepat, gagal connect,",
                    "lalu mati. Karena itu layanan db diberi healthcheck, dan app",
                    "menunggunya lewat condition: service_healthy.",
                    "",
                    "Satu catatan saat membaca berkas orang: compose lama diawali baris",
                    "version: \"3.8\". Sekarang baris itu tidak dipakai lagi dan malah",
                    "memunculkan peringatan. Kalau melihatnya, berkas itu tua, bukan",
                    "salah.",
                ],
                "code": """# ===== File: docker-compose.yml =====
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: bifams
      POSTGRES_USER: bifams
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - data-db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U bifams"]
      interval: 5s
      retries: 10

  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/bifams
      SPRING_DATASOURCE_USERNAME: bifams
      SPRING_DATASOURCE_PASSWORD: ${DB_PASSWORD}
    depends_on:
      db:
        condition: service_healthy

volumes:
  data-db:


# ===== File: .env =====
DB_PASSWORD=sandi-untuk-di-laptop-saja""",
            },
            {
                "body": [
                    "PERINTAH YANG DIPAKAI SEHARI-HARI",
                    "",
                    "Dijalankan di folder yang berisi docker-compose.yml:",
                    "",
                    "  docker compose up -d            nyalakan semua, -d = di latar",
                    "  docker compose up -d --build    sekaligus bangun ulang image-nya",
                    "  docker compose ps               apa yang hidup dan sehat",
                    "  docker compose logs -f app      ikuti log layanan app",
                    "  docker compose exec db bash     buka shell di kontainer db",
                    "  docker compose down             matikan; VOLUME tetap ada",
                    "  docker compose down -v          matikan DAN hapus volumenya",
                    "",
                    "Yang tanpa compose berlaku untuk seluruh mesin:",
                    "",
                    "  docker ps                       kontainer yang sedang berjalan",
                    "  docker ps -a                    termasuk yang sudah mati",
                    "  docker logs -f bifams-pg        log satu kontainer",
                    "  docker exec -it bifams-pg bash  masuk ke dalamnya",
                    "  docker images                   image tersimpan dan ukurannya",
                    "",
                    "Dua yang paling sering menyelamatkan: logs -f dan ps -a. Kontainer",
                    "yang mati tiga detik setelah dinyalakan TIDAK muncul di docker ps",
                    "polos, jadi seolah-olah tidak pernah ada - padahal alasan matinya",
                    "tertulis rapi di lognya.",
                    "",
                    "Dan hati-hati dengan -v. Di laptop, down -v itu berguna: database",
                    "bersih dalam hitungan detik. Diketik di server, ia menghapus volume",
                    "produksi tanpa bertanya apa-apa lebih dulu.",
                    "",
                    "KENAPA BERKAS INI YANG PERTAMA DIBUKA DI REPO ORANG LAIN",
                    "",
                    "Waktu membuka proyek Java di GitHub, pertanyaan pertamamu hampir",
                    "selalu sama: aplikasi ini butuh apa saja supaya hidup? README",
                    "sering menjawab setengah-setengah, dan yang lebih parah, README",
                    "bisa basi tanpa ada yang sadar.",
                    "",
                    "docker-compose.yml tidak bisa basi diam-diam: kalau isinya salah,",
                    "proyeknya tidak jalan sama sekali. Dan ia mendaftar semuanya -",
                    "database apa versi berapa, apakah butuh Redis, port apa yang",
                    "dipakai, variabel lingkungan apa yang harus diisi. Membacanya lima",
                    "menit sering lebih cepat daripada menebak-nebak dari kode.",
                ],
            },
            {
                "heading": "Database: di laptop ya, di produksi belum tentu",
                "body": [
                    "Di laptop, database di dalam kontainer nyaris tanpa kerugian.",
                    "Semua orang di tim dapat PostgreSQL versi yang sama persis tanpa",
                    "memasang apa pun, dan database bersih selalu sejauh dua perintah.",
                    "",
                    "Di produksi pertimbangannya berbalik. Kontainer justru DIRANCANG",
                    "untuk dibuang dan dibuat ulang tanpa ditangisi - itu kelebihannya.",
                    "Data database adalah satu-satunya bagian yang tidak boleh punya",
                    "sifat itu. Mengontainerkan database bukan mustahil, tapi kebanyakan",
                    "tempat memilih server database tersendiri atau database terkelola,",
                    "yang cadangan, replikasi, dan penyetelannya sudah jadi pekerjaan",
                    "orang lain.",
                    "",
                    "B-iFAMS persis begitu: aplikasinya di satu server, databasenya",
                    "Oracle di mesin lain.",
                    "",
                    "DAN DI SINILAH KISAH bifams-pg SELESAI",
                    "",
                    "Ingat kontainer bernama bifams-pg dari materi Database di Produksi?",
                    "Namanya menyebut aplikasinya, image-nya PostgreSQL, nama tabelnya",
                    "sama persis, dan statusnya Up. Empat petunjuk yang semuanya",
                    "menunjuk ke arah yang keliru.",
                    "",
                    "Nama kontainer cuma teks yang diketik seseorang bertahun-tahun lalu",
                    "dan tidak pernah diperbarui. Ia bukan bukti. Yang jadi bukti cuma",
                    "dua: isi kontainernya sendiri, dan konfigurasi yang sedang dipakai",
                    "proses aplikasinya.",
                ],
                "code": """$ docker ps -a
CONTAINER ID   IMAGE         STATUS         NAMES
9f3c1a2b4d5e   postgres:13   Up 8 months    bifams-pg
# (kolom COMMAND, CREATED, dan PORTS dibuang supaya muat di sini)

# Bukti 1: isi kontainernya apa? Tabelnya ada, tapi kosong.
$ docker exec -it bifams-pg psql -U postgres -d bifams
psql (13.14)
bifams=# SELECT count(*) FROM app_user;
 count
-------
     0
(1 row)

bifams=# \\q

# Bukti 2: aplikasinya sendiri menyambung ke mana?
# Kalau aplikasinya juga kontainer, tanya lingkungannya:
$ docker exec bifams-app env | grep -i datasource
SPRING_DATASOURCE_URL=jdbc:oracle:thin:@//10.10.1.187:1521/XE

# Kalau bukan, baca konfigurasi yang sedang dipakai Tomcat:
$ grep jdbc.url ROOT/WEB-INF/classes/jdbc.properties
jdbc.url=jdbc:oracle:thin:@//10.10.1.187:1521/XE""",
            },
        ],
    },
    {
        "title": "26. Deploy, Cadangan, dan Cara Mundur",
        "sections": [
            {
                "body": [
                    "Deploy artinya memindahkan aplikasi dari laptopmu ke server tempat",
                    "orang lain memakainya.",
                    "",
                    "URUTAN YANG DIPAKAI DI B-iFAMS",
                    "",
                    "  1. Rakit          mvn clean package  -> target/aplikasi.war",
                    "  2. CADANGKAN      salin .war lama yang sedang jalan",
                    "  3. Hentikan       shutdown.sh",
                    "  4. Tukar          .war baru menggantikan yang lama",
                    "  5. Nyalakan       startup.sh",
                    "  6. Verifikasi     buka halamannya, baca log",
                    "",
                    "LANGKAH 2 TIDAK BOLEH DILEWATI",
                    "",
                    "Sebelum menyentuh apa pun, simpan dulu versi yang sedang berjalan.",
                    "Kalau versi baru bermasalah, kamu bisa kembali dalam hitungan detik",
                    "alih-alih memperbaikinya dalam panik sementara pengguna menunggu.",
                    "",
                    "  cp webapps/ROOT.war ~/ROOT.war.sebelum-20260826",
                    "",
                    "Beri nama bertanggal. Enam bulan lagi kamu tidak akan ingat",
                    "'ROOT.war.backup2' itu versi yang mana.",
                ]
            },
            {
                "body": [
                    "AKIBAT shutdown.sh YANG BELUM PERNAH DISEBUT",
                    "",
                    "Materi Server Aplikasi sudah menjelaskan bahwa startup.sh dan",
                    "shutdown.sh itu milik Tomcat, bukan milik aplikasimu. Ada satu akibat",
                    "dari kenyataan itu yang perlu kamu sadari SEBELUM menekannya di server",
                    "sungguhan: kalau Tomcat itu menampung beberapa aplikasi sekaligus di",
                    "webapps/, shutdown.sh menjatuhkan semuanya - bukan cuma punyamu.",
                    "",
                    "Di server yang isinya satu aplikasi saja, ini tidak pernah terasa. Di",
                    "server yang dipakai bersama, langkah 3 dan 5 di atas berarti kamu",
                    "meminta seluruh penghuni server ikut menunggu, dan itu hal yang pantas",
                    "dikabarkan lebih dulu.",
                    "",
                    "ENAM LANGKAH ITU, DI TIGA BENTUK DEPLOY YANG SUDAH KAMU TEMUI",
                    "",
                    "  .war ke Tomcat   persis enam langkah di atas. Bentuk B-iFAMS.",
                    "  java -jar        Spring Boot; langkah 4 jadi 'tukar .jar'.",
                    "  ganti image      kontainer; langkah 3-5 jadi satu perintah.",
                    "",
                    "Yang penting bukan perbedaannya - itu sudah dibahas di materinya",
                    "masing-masing - melainkan bahwa urutan enam langkah tadi tidak berubah",
                    "sedikit pun di ketiganya, TERMASUK yang nomor dua. Cuma bentuk",
                    "cadangannya yang menyesuaikan: salinan berkas .war, salinan berkas",
                    ".jar, atau nomor versi image lama yang kamu catat sebelum menukarnya.",
                    "",
                    "Tanpa itu, 'kembali ke versi kemarin' berubah dari satu perintah jadi",
                    "satu malam yang panjang - dan cara paling modern sekalipun tidak",
                    "membebaskanmu dari langkah 6: buka halamannya, baca lognya.",
                ]
            },
            {
                "body": [
                    "LANGKAH 6 BUKAN SEKADAR 'APLIKASINYA NYALA'",
                    "",
                    "Halaman login muncul bukan bukti aplikasi sehat. Yang harus dicek:",
                    "",
                    "  - Log start-up bersih, tidak ada exception",
                    "  - Halaman yang kamu ubah benar-benar berubah",
                    "  - Halaman yang TIDAK kamu ubah masih normal",
                    "",
                    "Yang ketiga sering dilupakan, padahal justru di situ kerusakan",
                    "tak sengaja muncul.",
                    "",
                    "JEBAKAN: MENYUNTING LANGSUNG DI SERVER",
                    "",
                    "Aplikasi yang sudah di-deploy biasanya terhampar sebagai folder di",
                    "server. Menyunting berkas di situ terasa praktis - perubahannya",
                    "langsung terasa, tidak perlu build ulang.",
                    "",
                    "Masalahnya, perubahan itu ada DI SERVER SAJA. Begitu aplikasi",
                    "di-deploy ulang dari .war, perubahanmu hilang tanpa jejak - dan",
                    "biasanya kamu baru sadar berbulan-bulan kemudian saat bug lama",
                    "muncul lagi entah dari mana.",
                    "",
                    "Kalau terpaksa melakukannya, catat, dan segera lipat perubahan itu",
                    "ke source aslinya.",
                ]
            },
        ],
    },
    {
        "title": "27. Menguji Seperti Pengguna Sungguhan",
        "sections": [
            {
                "body": [
                    "Pengujian yang bermanfaat bukan 'coba klik-klik sebentar', tapi",
                    "menjalankan tiap alur sampai tuntas dengan hasil yang bisa diperiksa.",
                    "",
                    "TIGA TINGKAT",
                    "",
                    "  Unit         satu method diuji sendirian, tanpa database.",
                    "               Cepat, dijalankan tiap kali kode berubah.",
                    "",
                    "  Integrasi    beberapa lapisan bersama, dengan database.",
                    "               Lebih lambat, menangkap salah sambung antar lapisan.",
                    "",
                    "  Manual       manusia memakainya seperti pengguna asli.",
                    "               Paling lambat, tapi menangkap hal yang tak terpikirkan.",
                    "",
                    "SATU KEBIASAAN YANG PALING BERGUNA",
                    "",
                    "Untuk tiap aturan bisnis, uji DUA sisinya:",
                    "",
                    "  - kasus yang seharusnya BERHASIL",
                    "  - kasus yang seharusnya DITOLAK",
                    "",
                    "Menguji sisi berhasil saja meloloskan aplikasi yang tidak punya",
                    "pemeriksaan sama sekali. Menguji sisi ditolak saja meloloskan",
                    "aplikasi yang menolak segalanya.",
                ]
            },
            {
                "heading": "Contoh daftar uji untuk satu aturan",
                "code": """Aturan: stok tidak boleh negatif

  stok 20, keluar  5  -> berhasil, sisa 15
  stok 20, keluar 20  -> berhasil, sisa 0      (batas tepat)
  stok 20, keluar 21  -> DITOLAK               (lewat satu langkah)
  stok 20, keluar  0  -> ditolak, tidak masuk akal
  stok 20, keluar -5  -> ditolak, jangan sampai malah menambah

Perhatikan tiga baris tengah. Kesalahan hampir selalu bersembunyi
di BATAS, bukan di tengah-tengah."""
            },
            {
                "body": [
                    "PERIKSA DATANYA, JANGAN CUMA LAYARNYA",
                    "",
                    "Saat menguji B-iFAMS, penghapusan sebuah item terlihat berhasil:",
                    "pesan sukses muncul, daftar item kosong, seluruh penghitung di",
                    "beranda kembali nol. Semua tampak beres.",
                    "",
                    "Ternyata dua permintaan yang mengacu item itu masih tertinggal di",
                    "database - kini menggantung tanpa item sama sekali. Layar tidak",
                    "menunjukkannya karena halaman yang menampilkannya memang tidak",
                    "dibuka.",
                    "",
                    "Karena itu belajar SQL bukan pelengkap. Tanpa kemampuan membuka",
                    "database sendiri, kamu cuma bisa mempercayai apa yang aplikasi",
                    "mau tunjukkan padamu.",
                ]
            },
        ],
    },
    {
        "title": "28. Menulis Uji Otomatis: Mock, MockMvc, dan Uji Integrasi",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menutup dengan daftar uji yang ditulis di kertas, dan",
                    "materi Keamanan dengan daftar URL yang harus ditolak. Keduanya benar -",
                    "tapi daftar di kertas cuma berjalan kalau ada orang yang ingat",
                    "menjalankannya. Materi ini mengubah kedua daftar itu jadi kode.",
                    "",
                    "Dasar JUnit sudah dibahas di kurikulum Java, materi 'Unit Testing dengan",
                    "JUnit': @Test, @BeforeEach, assertEquals, assertThrows, dan pola",
                    "Arrange-Act-Assert. Di sini kita lanjut dari titik itu, bukan mengulang.",
                    "",
                    "DI MANA BERKAS UJINYA TINGGAL",
                    "",
                    "  src/main/java/com/bifams/service/ItemService.java      <- kodenya",
                    "  src/test/java/com/bifams/service/ItemServiceTest.java  <- ujinya",
                    "",
                    "Paketnya sama PERSIS; yang berbeda cuma akar foldernya - pembagian yang",
                    "sudah kamu lihat di materi Maven. Kesamaan paket itu bukan kebetulan:",
                    "dengan paket yang sama, uji boleh menyentuh method yang tidak public,",
                    "jadi kamu tidak perlu melonggarkan hak akses kode produksi cuma supaya",
                    "ada yang bisa mengujinya.",
                    "",
                    "Nama kelas ujinya = nama kelas yang diuji + 'Test'. Maven mencari pola",
                    "nama itu dan tidak mencari yang lain. Kelas bernama ItemServiceUji tetap",
                    "dikompilasi, tetap tersimpan rapi di Git, dan TIDAK PERNAH dijalankan -",
                    "dan diamnya kelihatan persis sama seperti lulus.",
                    "",
                    "KENAPA JUNIT TIDAK IKUT MASUK KE .war",
                    "",
                    "  <dependency>",
                    "    <groupId>org.mockito</groupId>",
                    "    <artifactId>mockito-core</artifactId>",
                    "    <version>3.12.4</version>",
                    "    <scope>test</scope>          <- satu baris ini yang menentukan",
                    "  </dependency>",
                    "",
                    "<scope>test</scope> berarti: pustaka ini ada saat mengompilasi dan",
                    "menjalankan uji, lalu TIDAK ikut dirakit ke hasil akhir. Itulah jawaban",
                    "kenapa berkas .war 25 MB di materi Maven tidak berisi JUnit sebaris pun.",
                    "Lupa menuliskannya bukan cuma membuat pustaka uji terkirim ke server;",
                    "yang lebih berbahaya, kode produksi jadi boleh meng-import Mockito tanpa",
                    "ditegur compiler.",
                    "",
                    "PERTANYAAN YANG DIGANTUNG MATERI SEBELUMNYA",
                    "",
                    "Materi sebelumnya bilang: 'Unit: satu method diuji sendirian, tanpa",
                    "database.' Terdengar masuk akal - sampai kamu melihat lagi ItemService.",
                    "Ia menyimpan sebuah ItemDao, dan tanpa DAO itu ia tidak bisa apa-apa.",
                    "",
                    "Jadi bagaimana caranya mendapat DAO yang bukan database?",
                    "",
                    "Jawabannya: buatkan penggantinya. Nama umumnya TEST DOUBLE - pemeran",
                    "pengganti, istilah yang dipinjam dari stuntman di film. Dua bentuknya",
                    "yang paling sering kamu temui:",
                    "",
                    "  FAKE   Kelas sungguhan yang kamu tulis sendiri, gudangnya sebuah List",
                    "         di memori, bukan tabel. Ia benar-benar menyimpan dan benar-",
                    "         benar mengembalikan. Materi DAO sudah menyebutnya 'DAO versi",
                    "         memori'; inilah nama resminya.",
                    "",
                    "  MOCK   Objek boneka yang dibuatkan pustaka. Tidak menyimpan apa pun.",
                    "         Ia cuma menjawab apa yang kamu suruh jawab, dan mencatat siapa",
                    "         memanggil apa - supaya kamu bisa memeriksanya sesudahnya.",
                    "",
                    "Yang di bawah ini FAKE, ditulis tangan seluruhnya, tanpa satu pustaka",
                    "pun. Simpan dan jalankan - inilah seluruh gagasan uji otomatis dalam",
                    "satu berkas yang bisa kamu bongkar sendiri.",
                ],
            },
            {
                "heading": "FAKE buatan tangan - program ini bisa langsung dijalankan",
                "code": """import java.util.ArrayList;
import java.util.List;

class Item {
    private final Long id;
    private final String nama;
    private int stok;

    Item(Long id, String nama, int stok) {
        this.id = id;
        this.nama = nama;
        this.stok = stok;
    }

    Long getId()        { return id; }
    int getStok()       { return stok; }
    void setStok(int s) { this.stok = s; }
}

class AturanDilanggar extends RuntimeException {
    AturanDilanggar(String pesan) { super(pesan); }
}

interface ItemDao {
    Item cariById(Long id);
    void simpan(Item item);
}

// FAKE: implementasi sungguhan, tapi gudangnya List, bukan Oracle.
class ItemDaoMemori implements ItemDao {
    final List<Item> isi = new ArrayList<Item>();
    int simpanDipanggil = 0;

    public Item cariById(Long id) {
        for (Item i : isi) {
            if (i.getId().equals(id)) return i;
        }
        return null;
    }

    public void simpan(Item item) {
        if (!isi.contains(item)) isi.add(item);
        simpanDipanggil++;
    }
}

class ItemService {
    private final ItemDao itemDao;          // final -> mustahil null

    ItemService(ItemDao itemDao) {          // injeksi lewat constructor
        this.itemDao = itemDao;
    }

    void keluarkan(Long id, int jumlah) {
        if (jumlah <= 0)
            throw new AturanDilanggar("Jumlah harus lebih dari nol.");

        Item item = itemDao.cariById(id);
        if (item.getStok() < jumlah)
            throw new AturanDilanggar("Stok tidak cukup.");

        item.setStok(item.getStok() - jumlah);
        itemDao.simpan(item);
    }
}

public class UjiDenganFake {

    static int gagal = 0;

    static ItemDaoMemori gudang() {         // peran @BeforeEach: selalu baru
        ItemDaoMemori dao = new ItemDaoMemori();
        dao.isi.add(new Item(1L, "APAR 3kg", 20));
        return dao;
    }

    static void cek(String judul, Object diharap, Object nyata) {
        boolean lulus = diharap.equals(nyata);
        if (!lulus) gagal++;
        System.out.println((lulus ? "LULUS  " : "GAGAL  ") + judul
                + "  (diharap " + diharap + ", nyata " + nyata + ")");
    }

    public static void main(String[] args) {
        // ---------- sisi yang seharusnya BERHASIL
        ItemDaoMemori dao = gudang();
        new ItemService(dao).keluarkan(1L, 5);

        cek("stok berkurang", 15, dao.cariById(1L).getStok());
        cek("simpan dipanggil sekali", 1, dao.simpanDipanggil);

        // ---------- sisi yang seharusnya DITOLAK
        ItemDaoMemori dao2 = gudang();
        String pesan = "";
        try {
            new ItemService(dao2).keluarkan(1L, 21);
        } catch (AturanDilanggar e) {
            pesan = e.getMessage();
        }

        cek("permintaan berlebih ditolak", "Stok tidak cukup.", pesan);
        cek("stok tidak berubah", 20, dao2.cariById(1L).getStok());
        cek("simpan tidak pernah dipanggil", 0, dao2.simpanDipanggil);

        System.out.println(gagal == 0 ? "Semua uji lulus."
                                      : gagal + " uji gagal.");
    }
}""",
            },
            {
                "heading": "Mockito - bentuk yang akan kamu temui di repo sungguhan",
                "body": [
                    "Program tadi memuat tiga hal yang tidak akan kamu tulis lagi seumur",
                    "hidup: kelas ItemDaoMemori, penghitung simpanDipanggil, dan fungsi",
                    "cek(). Ketiganya sudah disediakan pustaka. cek() digantikan assertion",
                    "JUnit, dua yang lain digantikan Mockito.",
                    "",
                    "  mock(ItemDao.class)                buat boneka dari sebuah antarmuka",
                    "  when(...).thenReturn(...)          ajari boneka menjawab apa",
                    "  verify(dao).simpan(item)           pastikan dipanggil, tepat sekali",
                    "  verify(dao, never()).hapus(any())  pastikan TIDAK pernah dipanggil",
                    "",
                    "Baris never() itu yang tidak bisa dilihat mata dari layar mana pun.",
                    "Sebuah service boleh saja menolak dengan benar, tapi terlanjur menyimpan",
                    "separuh perubahan sebelum ia menolak - persis bahaya yang dibahas di",
                    "materi Service. Hanya uji seperti ini yang menangkapnya.",
                    "",
                    "BENTUK BERANOTASI",
                    "",
                    "  @ExtendWith(MockitoExtension.class)",
                    "  class ItemServiceTest {",
                    "      @Mock        ItemDao itemDao;      // dibuatkan boneka",
                    "      @InjectMocks ItemService service;  // boneka disuntikkan ke sini",
                    "  }",
                    "",
                    "Artinya sama persis dengan memanggil mock() sendiri, cuma lebih pendek",
                    "kalau bonekanya banyak. @InjectMocks mencari constructor ItemService",
                    "lalu mengisinya dengan @Mock yang cocok tipenya.",
                    "",
                    "KENAPA SEMUA INI CUMA MUNGKIN LEWAT CONSTRUCTOR",
                    "",
                    "Perhatikan satu baris yang muncul di program tadi dan akan muncul lagi",
                    "di bawah: new ItemService(itemDao). Uji bisa memilih sendiri DAO mana",
                    "yang dipakai justru karena ItemService menerimanya lewat constructor.",
                    "Kelas yang memakai @Autowired di field tidak punya pintu masuk itu sama",
                    "sekali; alasan lengkapnya ada di materi bean, dan inilah wujud nyata",
                    "akibatnya.",
                    "",
                    "TIGA JEBAKAN YANG SUNGGUH MENJEBAK",
                    "",
                    "  1. mock() cuma bisa dibuat dari antarmuka atau kelas biasa - bukan",
                    "     dari method static, bukan dari kelas final. Kode yang penuh method",
                    "     static memang sulit diuji, dan itu salah satu alasan menghindarinya.",
                    "",
                    "  2. Method yang tidak kamu ajari mengembalikan nilai kosong: null untuk",
                    "     objek, 0 untuk angka, false untuk boolean. Lupa satu baris when()",
                    "     berujung NullPointerException di dalam service - dan yang tertuduh",
                    "     kelihatannya service-mu, padahal ujinya yang belum lengkap.",
                    "",
                    "  3. when(itemDao.cariById(1L)) cuma berlaku untuk 1L. Dipanggil dengan",
                    "     2L, boneka menjawab null. Pakai anyLong() kalau argumennya memang",
                    "     tidak penting bagi uji itu.",
                    "",
                    "Dua uji berikut memeriksa persis dua hal yang diperiksa program tadi.",
                ],
                "code": """import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import org.junit.jupiter.api.Test;

class ItemServiceTest {

    @Test
    void permintaanBerlebihDitolak() {
        // ARRANGE - buat boneka, lalu ajari ia menjawab
        ItemDao itemDao = mock(ItemDao.class);
        Item item = new Item(1L, "APAR 3kg", 20);
        when(itemDao.cariById(1L)).thenReturn(item);

        ItemService service = new ItemService(itemDao);

        // ACT + ASSERT - sisi yang harus DITOLAK
        AturanDilanggar e = assertThrows(AturanDilanggar.class,
                () -> service.keluarkan(1L, 21));
        assertEquals("Stok tidak cukup.", e.getMessage());

        // dan pastikan tidak ada yang terlanjur ditulis
        verify(itemDao, never()).simpan(any(Item.class));
    }

    @Test
    void mutasiWajarTersimpan() {
        ItemDao itemDao = mock(ItemDao.class);
        Item item = new Item(1L, "APAR 3kg", 20);
        when(itemDao.cariById(1L)).thenReturn(item);

        new ItemService(itemDao).keluarkan(1L, 5);

        assertEquals(15, item.getStok());
        verify(itemDao).simpan(item);      // tepat sekali, dengan item itu
    }
}""",
            },
            {
                "heading": "MockMvc - menguji lapisan web tanpa menyalakan server",
                "body": [
                    "Sejauh ini yang diuji baru service. Lapisan web punya perkakasnya",
                    "sendiri: MockMvc.",
                    "",
                    "Tidak ada Tomcat yang menyala, tidak ada port yang dibuka, tidak ada",
                    "browser. MockMvc menyusun objek permintaan HTTP langsung di memori lalu",
                    "menyerahkannya ke DispatcherServlet. Yang diuji tetap jalur sungguhan:",
                    "pemetaan URL, pembacaan parameter, filter keamanan, sampai nama view",
                    "yang dipilih.",
                    "",
                    "Sekarang buka lagi daftar di materi Keamanan - lima URL yang harus 403",
                    "dan tiga yang harus tetap lewat. Daftar itu dikerjakan tangan sekali,",
                    "lalu dilupakan. Dengan MockMvc, daftar yang sama jadi delapan method",
                    "@Test yang berjalan lagi setiap kali seseorang mengetik 'mvn test'.",
                    "",
                    "@WithMockUser(roles = \"REQUESTER\") adalah kuncinya: ia membuat uji",
                    "berpura-pura jadi akun berperan rendah, tanpa satu baris pun di tabel",
                    "pengguna. Kesalahan 'menguji sebagai admin' yang dibahas di materi",
                    "Keamanan jadi sulit dilakukan tanpa sadar, karena perannya tertulis",
                    "tepat di atas method.",
                    "",
                    "JEBAKAN: HIJAU KARENA ALASAN YANG SALAH",
                    "",
                    ".with(csrf()) menempelkan token yang dibahas di materi Login. Tanpa",
                    "baris itu, POST-mu ditolak 403 karena tokennya hilang - dan ujimu tetap",
                    "HIJAU, karena yang kamu tulis memang 'harapkan 403'. Kamu mengira sudah",
                    "membuktikan hak akses bekerja; yang terbukti cuma CSRF-nya bekerja.",
                    "",
                    "Cara memeriksanya murah: jalankan sekali uji yang sama sebagai ADMIN.",
                    "Kalau tetap 403, berarti bukan hak akses yang sedang kamu uji.",
                ],
                "code": """@WebMvcTest(ItemController.class)
class ItemControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private StockService stockService;     // service asli diganti boneka

    @Test
    @WithMockUser(username = "budi", roles = "REQUESTER")
    void requesterTidakBolehMengubahStok() throws Exception {
        mockMvc.perform(post("/items/1/stock")
                        .param("type", "OUT")
                        .param("qty", "5")
                        .with(csrf()))
                .andExpect(status().isForbidden());

        verify(stockService, never())
                .catatMutasi(anyLong(), any(), anyInt());
    }

    @Test
    @WithMockUser(roles = "REQUESTER")
    void requesterTetapBolehMelihatDaftar() throws Exception {
        mockMvc.perform(get("/items"))
                .andExpect(status().isOk())
                .andExpect(view().name("item/list"));
    }
}""",
            },
            {
                "body": [
                    "UJI INTEGRASI: SAAT BONEKANYA DISINGKIRKAN",
                    "",
                    "Sejauh ini semua tetangga ItemService diganti. Uji integrasi melakukan",
                    "kebalikannya: biarkan yang asli bekerja bersama-sama.",
                    "",
                    "  @SpringBootTest  Menyalakan SELURUH wadah Spring - semua bean, service",
                    "                   asli, DAO asli, database sungguhan. Paling meyakinkan,",
                    "                   paling lambat, dan langsung gagal kalau ada satu bean",
                    "                   saja yang tidak bisa dibuat.",
                    "",
                    "  @DataJpaTest     Hanya lapisan datanya: entitas, repository, dan sebuah",
                    "                   database sementara. Inilah yang membuktikan query-mu",
                    "                   benar-benar mengembalikan baris yang kamu maksud.",
                    "",
                    "  @WebMvcTest      Hanya lapisan web, seperti contoh di atas. Service-nya",
                    "                   tetap boneka, jadi ia bukan uji integrasi penuh.",
                    "",
                    "DATABASENYA DARI MANA?",
                    "",
                    "  H2              Database yang hidup di dalam memori proses uji. Cepat",
                    "                  dan tidak perlu dipasang. Harganya: dialek SQL-nya",
                    "                  bukan Oracle, jadi query yang lulus di H2 masih bisa",
                    "                  gagal di produksi.",
                    "",
                    "  Testcontainers  Menyalakan Oracle atau PostgreSQL sungguhan di dalam",
                    "                  Docker selama uji berjalan, lalu membuangnya. Lebih",
                    "                  lambat, tapi yang diuji database yang sama dengan yang",
                    "                  dipakai nanti.",
                    "",
                    "@Transactional di kelas uji membuat Spring MEMBATALKAN semua perubahan",
                    "begitu satu method uji selesai. Tanpa itu, uji pertama meninggalkan",
                    "barisnya, uji kedua gagal karena datanya sudah ada - lalu lulus lagi",
                    "kalau dijalankan sendirian. Uji yang hasilnya bergantung pada urutan",
                    "adalah jenis bug paling melelahkan yang bisa kamu buat sendiri.",
                    "",
                    "KAPAN UJI JUSTRU BERBOHONG",
                    "",
                    "Ini bagian terpenting dari seluruh materi ini.",
                    "",
                    "Uji yang SELURUH tetangganya boneka cuma membuktikan satu hal: kodemu",
                    "memanggil apa yang kamu suruh panggil. Kamu sendiri yang menulis",
                    "when(itemDao.cariById(1L)).thenReturn(item), lalu kamu memastikan",
                    "service memakai item itu. Yang tidak pernah tersentuh: apakah",
                    "cariById() yang SUNGGUHAN mengembalikan barang itu.",
                    "",
                    "Kolom yang salah nama? Uji mock tetap hijau. Query yang lupa 'WHERE",
                    "aktif = 1'? Tetap hijau. Hubungan entitas yang salah arah? Tetap hijau.",
                    "Yang menangkapnya cuma uji yang menyentuh database sungguhan - dan",
                    "itulah alasan @DataJpaTest ada.",
                    "",
                    "KESEIMBANGAN YANG LAZIM DIPAKAI",
                    "",
                    "  Banyak      uji unit ber-fake/mock atas aturan bisnis di service,",
                    "              karena di situlah keputusan yang bisa salah tinggal.",
                    "  Secukupnya  uji @DataJpaTest untuk tiap query yang tidak sepele.",
                    "  Sedikit     uji dari HTTP sampai tabel, untuk alur yang paling penting.",
                    "",
                    "Dan satu kebiasaan yang menutup lingkaran: setiap kali sebuah bug",
                    "ditemukan, tulis dulu uji yang GAGAL karena bug itu, baru perbaiki",
                    "kodenya. Ujinya jadi penjaga permanen - bukti tertulis bahwa bug yang",
                    "sama tidak akan diam-diam kembali enam bulan lagi.",
                    "",
                    "PENUTUP MODUL",
                    "",
                    "Materi ini sengaja tidak mengajarkan cara menempelkan anotasi",
                    "Spring satu per satu. Anotasi bisa dicari kapan saja; yang tidak",
                    "bisa dicari adalah pertimbangan di baliknya - kenapa aturan bisnis",
                    "ditaruh di service, kenapa periksa dulu baru ubah, kenapa hak akses",
                    "harus diuji dari akun yang tidak berhak.",
                    "",
                    "Latihan modul ini melatih semua itu dalam Java murni, tanpa",
                    "framework apa pun. Kalau kamu bisa menyelesaikannya, membaca kode",
                    "B-iFAMS tidak akan terasa seperti sihir lagi.",
                ],
            },
        ],
    },
]
