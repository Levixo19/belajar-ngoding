"""Latihan modul "Bikin Aplikasi".

Seluruh latihan ditulis dalam Java murni tanpa framework. Tujuannya melatih
CARA BERPIKIR membangun aplikasi - memisahkan lapisan, menaruh aturan bisnis
di tempat yang benar, memeriksa sebelum mengubah - bukan menghafal anotasi
Spring yang bisa dicari kapan saja.

Semua solusi deterministik: tidak ada tanggal saat ini, tidak ada bilangan
acak, dan tidak ada yang membaca input. Ini syarat dari tests/test_solutions.py.
"""

APLIKASI_EXERCISES = [
    {
        "title": "Latihan 1: Entitas Item",
        "difficulty": "Mudah",
        "question": [
            "Buat kelas Item yang mewakili satu barang di gudang.",
            "",
            "Ketentuan:",
            "  - Field PRIVAT: kode, nama, satuan (String), stok, stokMinimum (int).",
            "  - Constructor menerima kode, nama, satuan, stokMinimum.",
            "    Stok awal selalu 0.",
            "  - setStok(int) dan getStok().",
            "  - stokMenipis() mengembalikan true kalau stok <= stokMinimum.",
            "  - toString() menghasilkan:  KODE - Nama (stok satuan)",
            "",
            "Di main, buat dua item lalu cetak persis seperti ini:",
            "",
            "FS-2608-001 - APAR Powder 6kg (20 tabung)",
            "Menipis: false",
            "FS-2608-002 - Selang 2.5 inci (8 roll)",
            "Menipis: true",
            "",
            "Item pertama stoknya 20 dengan minimum 5.",
            "Item kedua stoknya 8 dengan minimum 10.",
        ],
        "hints": [
            "Kelas bantu di dalam kelas utama harus 'static class' supaya bisa "
            "dipakai dari main tanpa membuat objek kelas luarnya.",
            "toString() dipanggil OTOMATIS oleh System.out.println(objek). "
            "Kamu tidak perlu menulis println(item.toString()).",
            "stokMenipis() memakai <= bukan <. Stok yang PERSIS sama dengan "
            "minimum sudah terhitung menipis.",
        ],
        "solution": """public class LatihanItem {

    static class Item {
        private String kode;
        private String nama;
        private String satuan;
        private int stok;
        private int stokMinimum;

        Item(String kode, String nama, String satuan, int stokMinimum) {
            this.kode = kode;
            this.nama = nama;
            this.satuan = satuan;
            this.stokMinimum = stokMinimum;
            this.stok = 0;
        }

        int getStok() { return stok; }
        void setStok(int stok) { this.stok = stok; }

        boolean stokMenipis() {
            return stok <= stokMinimum;
        }

        @Override
        public String toString() {
            return kode + " - " + nama + " (" + stok + " " + satuan + ")";
        }
    }

    public static void main(String[] args) {
        Item a = new Item("FS-2608-001", "APAR Powder 6kg", "tabung", 5);
        a.setStok(20);

        Item b = new Item("FS-2608-002", "Selang 2.5 inci", "roll", 10);
        b.setStok(8);

        System.out.println(a);
        System.out.println("Menipis: " + a.stokMenipis());
        System.out.println(b);
        System.out.println("Menipis: " + b.stokMenipis());
    }
}""",
        "mode": "persis",
    },
    {
        "title": "Latihan 2: Kode Item Otomatis",
        "difficulty": "Mudah",
        "question": [
            "B-iFAMS menerbitkan kode item otomatis dengan pola:",
            "",
            "    FS-YYMM-NNN",
            "",
            "  YY   dua digit terakhir tahun   (2026 -> 26)",
            "  MM   bulan dua digit            (8 -> 08)",
            "  NNN  nomor urut tiga digit      (1 -> 001)",
            "",
            "Buat method:",
            "",
            "    static String buatKode(int tahun, int bulan, int urut)",
            "",
            "Perhatikan: tahun dan bulan DIKIRIM sebagai parameter, bukan diambil",
            "dari tanggal hari ini. Fungsi yang bergantung pada waktu sekarang",
            "mustahil diuji - hasilnya berubah tiap hari.",
            "",
            "Cetak persis:",
            "",
            "FS-2608-001",
            "FS-2608-042",
            "FS-2601-999",
            "FS-2712-007",
        ],
        "hints": [
            "String.format(\"%02d\", 8) menghasilkan \"08\" - angka 0 di depan "
            "berarti 'isi dengan nol', angka 2 berarti 'lebar dua karakter'.",
            "Dua digit terakhir tahun didapat dengan sisa bagi: 2026 % 100 = 26.",
            "Pola lengkapnya: \"FS-%02d%02d-%03d\" dengan tiga nilai berurutan.",
        ],
        "solution": """public class LatihanKode {

    static String buatKode(int tahun, int bulan, int urut) {
        return String.format("FS-%02d%02d-%03d", tahun % 100, bulan, urut);
    }

    public static void main(String[] args) {
        System.out.println(buatKode(2026, 8, 1));
        System.out.println(buatKode(2026, 8, 42));
        System.out.println(buatKode(2026, 1, 999));
        System.out.println(buatKode(2027, 12, 7));
    }
}""",
        "mode": "persis",
    },
    {
        "title": "Latihan 3: Stok Tidak Boleh Negatif",
        "difficulty": "Mudah",
        "question": [
            "Aturan bisnis paling dasar di B-iFAMS: stok tidak boleh negatif.",
            "",
            "Buat method:",
            "",
            "    static int keluar(int stok, int jumlah)",
            "",
            "  - jumlah <= 0        -> tolak, kembalikan stok apa adanya",
            "  - jumlah > stok      -> tolak, kembalikan stok apa adanya",
            "  - selain itu         -> kembalikan stok - jumlah",
            "",
            "Setiap penolakan mencetak alasannya lebih dulu, dari DALAM method.",
            "",
            "Di main, mulai dari stok 20 lalu panggil berurutan dengan jumlah",
            "5, 15, 1, dan -3. Stok dibawa terus dari hasil sebelumnya.",
            "Setelah tiap pemanggilan, cetak 'keluar N -> sisa M' bila stok",
            "berubah, atau 'stok tetap M' bila tidak.",
            "",
            "Perhatikan pemanggilan kedua: stok 15 diminta 15. Ini BOLEH -",
            "mengambil seluruh sisa stok itu sah, yang dilarang cuma sampai",
            "minus. Batas seperti ini justru tempat kesalahan paling sering",
            "bersembunyi, jadi pastikan pembandingmu > bukan >=.",
            "",
            "Cetak persis:",
            "",
            "keluar 5 -> sisa 15",
            "keluar 15 -> sisa 0",
            "DITOLAK: diminta 1 tetapi stok hanya 0",
            "stok tetap 0",
            "DITOLAK: jumlah -3 tidak masuk akal",
            "stok tetap 0",
        ],
        "hints": [
            "Urutan pemeriksaan menentukan pesan mana yang muncul. Periksa "
            "jumlah <= 0 LEBIH DULU, baru bandingkan dengan stok.",
            "Pakai jumlah > stok, bukan jumlah >= stok. Dengan >= , permintaan "
            "15 dari stok 15 ikut ditolak padahal seharusnya boleh.",
            "Pesan penolakan dicetak DI DALAM method keluar(). Baris "
            "'keluar N -> sisa M' dan 'stok tetap M' dicetak di main, dengan "
            "membandingkan stok sebelum dan sesudah pemanggilan.",
        ],
        "solution": """public class LatihanStokNegatif {

    static int keluar(int stok, int jumlah) {
        if (jumlah <= 0) {
            System.out.println("DITOLAK: jumlah " + jumlah + " tidak masuk akal");
            return stok;
        }
        if (jumlah > stok) {
            System.out.println("DITOLAK: diminta " + jumlah
                    + " tetapi stok hanya " + stok);
            return stok;
        }
        return stok - jumlah;
    }

    public static void main(String[] args) {
        int stok = 20;
        int[] permintaan = { 5, 15, 1, -3 };

        for (int jumlah : permintaan) {
            int sebelum = stok;
            stok = keluar(stok, jumlah);
            if (stok != sebelum) {
                System.out.println("keluar " + jumlah + " -> sisa " + stok);
            } else {
                System.out.println("stok tetap " + stok);
            }
        }
    }
}""",
        "mode": "persis",
    },
    {
        "title": "Latihan 4: Opname Fisik",
        "difficulty": "Menengah",
        "question": [
            "Saat opname, petugas menghitung barang di rak lalu memasukkan HASIL",
            "HITUNGANNYA - bukan selisihnya. Sistem yang menghitung selisih sendiri.",
            "",
            "Ini penting: kalau petugas disuruh menghitung selisih sendiri, dia",
            "harus tahu angka sistem lebih dulu, dan itu justru membuat opname",
            "kehilangan gunanya sebagai pemeriksaan independen.",
            "",
            "Buat method:",
            "",
            "    static int opname(int stokSistem, int hasilHitung)",
            "",
            "Method mencetak satu baris lalu mengembalikan hasilHitung:",
            "",
            "    ADJUSTMENT <selisih bertanda> -> stok jadi <hasilHitung>",
            "",
            "Selisih positif diberi tanda +, negatif apa adanya, nol tanpa tanda.",
            "",
            "Di main, mulai dari stok 25 lalu panggil berurutan dengan",
            "hasilHitung 22, 30, dan 30. Stok dibawa terus.",
            "",
            "Cetak persis:",
            "",
            "ADJUSTMENT -3 -> stok jadi 22",
            "ADJUSTMENT +8 -> stok jadi 30",
            "ADJUSTMENT 0 -> stok jadi 30",
        ],
        "hints": [
            "Selisih = hasilHitung - stokSistem. Kalau hasilnya negatif, "
            "tandanya sudah ikut menempel saat diubah jadi teks.",
            "Untuk selisih positif kamu harus MENAMBAHKAN '+' sendiri, karena "
            "Java tidak pernah mencetak tanda plus.",
            "Selisih nol cukup dicetak sebagai '0'. String.valueOf(0) sudah "
            "menghasilkan itu, jadi cabang negatif dan nol bisa digabung.",
        ],
        "solution": """public class LatihanOpname {

    static int opname(int stokSistem, int hasilHitung) {
        int selisih = hasilHitung - stokSistem;
        String tanda;
        if (selisih > 0) {
            tanda = "+" + selisih;
        } else {
            tanda = String.valueOf(selisih);
        }
        System.out.println("ADJUSTMENT " + tanda + " -> stok jadi " + hasilHitung);
        return hasilHitung;
    }

    public static void main(String[] args) {
        int stok = 25;
        stok = opname(stok, 22);
        stok = opname(stok, 30);
        stok = opname(stok, 30);
    }
}""",
        "mode": "persis",
    },
    {
        "title": "Latihan 5: Buku Besar Mutasi Stok",
        "difficulty": "Menengah",
        "question": [
            "Setiap perubahan stok harus meninggalkan jejak: jenis, jumlah, sisa",
            "stok setelahnya, dan catatan. Kumpulan jejak ini disebut buku besar,",
            "dan tanpanya kamu tidak bisa menjawab 'kenapa stoknya jadi segini?'.",
            "",
            "Buat kelas Mutasi (static class) berisi jenis, qty, sisa, catatan.",
            "Simpan di ArrayList.",
            "",
            "Buat method catat(String jenis, int qty, String catatan) yang",
            "menyesuaikan stok lalu menambah satu baris ke buku besar:",
            "",
            "  IN dan RETURN  menambah stok",
            "  OUT dan JUNK   mengurangi stok",
            "",
            "Mulai dari stok 0, panggil berurutan:",
            "  IN 20     'Stok awal'",
            "  OUT 5     'Dipakai latihan'",
            "  JUNK 3    'Segel bocor'",
            "  RETURN 2  'Pengembalian'",
            "",
            "Setelah semuanya, cetak buku besar dengan format:",
            "  <jenis> <qty bertanda> sisa=<sisa> | <catatan>",
            "",
            "Cetak persis:",
            "",
            "IN +20 sisa=20 | Stok awal",
            "OUT -5 sisa=15 | Dipakai latihan",
            "JUNK -3 sisa=12 | Segel bocor",
            "RETURN +2 sisa=14 | Pengembalian",
        ],
        "hints": [
            "Simpan stok sebagai field static supaya bisa diubah dari method "
            "catat() dan tetap terbawa antar pemanggilan.",
            "Buat satu method bantu menambah(jenis) yang mengembalikan true "
            "untuk IN dan RETURN. Method itu dipakai dua kali: saat menghitung "
            "stok, dan saat menentukan tanda + atau - waktu mencetak.",
            "Jangan menyimpan qty sebagai angka negatif. Buku besar sungguhan "
            "menyimpan jumlah positif, dan arahnya ditentukan oleh kolom jenis.",
        ],
        "solution": """import java.util.ArrayList;
import java.util.List;

public class LatihanBukuBesar {

    static class Mutasi {
        String jenis;
        int qty;
        int sisa;
        String catatan;

        Mutasi(String jenis, int qty, int sisa, String catatan) {
            this.jenis = jenis;
            this.qty = qty;
            this.sisa = sisa;
            this.catatan = catatan;
        }
    }

    static int stok = 0;
    static List<Mutasi> bukuBesar = new ArrayList<Mutasi>();

    static boolean menambah(String jenis) {
        return jenis.equals("IN") || jenis.equals("RETURN");
    }

    static void catat(String jenis, int qty, String catatan) {
        if (menambah(jenis)) {
            stok = stok + qty;
        } else {
            stok = stok - qty;
        }
        bukuBesar.add(new Mutasi(jenis, qty, stok, catatan));
    }

    public static void main(String[] args) {
        catat("IN", 20, "Stok awal");
        catat("OUT", 5, "Dipakai latihan");
        catat("JUNK", 3, "Segel bocor");
        catat("RETURN", 2, "Pengembalian");

        for (Mutasi m : bukuBesar) {
            String tanda = menambah(m.jenis) ? "+" : "-";
            System.out.println(m.jenis + " " + tanda + m.qty
                    + " sisa=" + m.sisa + " | " + m.catatan);
        }
    }
}""",
        "mode": "persis",
    },
    {
        "title": "Latihan 6: Status Peminjaman",
        "difficulty": "Menengah",
        "question": [
            "Peminjaman punya siklus status yang tidak boleh dilompati:",
            "",
            "    PENDING --setujui--> APPROVED --kembalikan--> RETURNED",
            "       |",
            "       +----tolak-------> REJECTED",
            "",
            "APPROVED dan RETURNED tidak bisa ditolak. RETURNED sudah final.",
            "",
            "Buat method:",
            "",
            "    static String ubah(String status, String aksi)",
            "",
            "Kalau perpindahannya sah, cetak dan kembalikan status baru.",
            "Kalau tidak sah, cetak penolakan dan kembalikan status LAMA.",
            "",
            "Di main, mulai dari PENDING lalu jalankan aksi berurutan:",
            "  setujui, kembalikan, kembalikan",
            "Lalu mulai lagi dari PENDING dengan aksi:",
            "  kembalikan, tolak",
            "",
            "Cetak persis:",
            "",
            "PENDING --setujui--> APPROVED",
            "APPROVED --kembalikan--> RETURNED",
            "DITOLAK: dari RETURNED tidak bisa kembalikan",
            "DITOLAK: dari PENDING tidak bisa kembalikan",
            "PENDING --tolak--> REJECTED",
        ],
        "hints": [
            "Perpindahan yang sah cuma tiga: PENDING+setujui, PENDING+tolak, "
            "APPROVED+kembalikan. Selain itu semuanya ditolak.",
            "Pakai satu variabel 'baru' yang mula-mula null. Isi kalau cocok "
            "salah satu dari tiga aturan; kalau setelah semua pemeriksaan masih "
            "null, berarti perpindahannya tidak sah.",
            "Format pesan sukses memakai dua tanda minus dan panah: "
            "status + \" --\" + aksi + \"--> \" + baru",
        ],
        "solution": """public class LatihanStatus {

    static String ubah(String status, String aksi) {
        String baru = null;

        if (status.equals("PENDING") && aksi.equals("setujui")) {
            baru = "APPROVED";
        } else if (status.equals("PENDING") && aksi.equals("tolak")) {
            baru = "REJECTED";
        } else if (status.equals("APPROVED") && aksi.equals("kembalikan")) {
            baru = "RETURNED";
        }

        if (baru == null) {
            System.out.println("DITOLAK: dari " + status + " tidak bisa " + aksi);
            return status;
        }

        System.out.println(status + " --" + aksi + "--> " + baru);
        return baru;
    }

    public static void main(String[] args) {
        String s = "PENDING";
        s = ubah(s, "setujui");
        s = ubah(s, "kembalikan");
        s = ubah(s, "kembalikan");

        String t = "PENDING";
        t = ubah(t, "kembalikan");
        t = ubah(t, "tolak");
    }
}""",
        "mode": "persis",
    },
    {
        "title": "Latihan 7: Periksa Dulu, Ubah Belakangan",
        "difficulty": "Lanjut",
        "question": [
            "Ini kebiasaan yang membedakan kode pemula dari kode yang layak",
            "dipakai orang.",
            "",
            "Satu permintaan bisa berisi beberapa item. Kalau item kedua stoknya",
            "kurang, stok item pertama TIDAK BOLEH terlanjur berkurang. Data yang",
            "rusak separuh jalan lebih buruk daripada permintaan yang ditolak",
            "seluruhnya.",
            "",
            "Caranya: DUA perulangan. Perulangan pertama memeriksa semua baris.",
            "Perulangan kedua baru mengubah - dan hanya dijalankan kalau",
            "perulangan pertama lolos sepenuhnya.",
            "",
            "Buat kelas Item (nama, stok) dan Baris (item, jumlah).",
            "Buat method setujui(List<Baris>) yang mengembalikan boolean.",
            "Buat method tampilkan(List<Item>) yang mencetak '  nama = stok'.",
            "",
            "Siapkan APAR stok 20 dan Selang stok 3, lalu:",
            "  Percobaan 1: APAR 5, Selang 10   -> harus ditolak",
            "  Percobaan 2: APAR 5, Selang 3    -> harus berhasil",
            "",
            "Cetak persis:",
            "",
            "Stok awal:",
            "  APAR = 20",
            "  Selang = 3",
            "Percobaan 1: APAR 5, Selang 10",
            "DITOLAK: stok Selang tidak cukup (tersedia 3, diminta 10)",
            "  APAR = 20",
            "  Selang = 3",
            "Percobaan 2: APAR 5, Selang 3",
            "DISETUJUI",
            "  APAR = 15",
            "  Selang = 0",
        ],
        "hints": [
            "Perulangan pertama: begitu ketemu satu saja yang gagal, cetak "
            "penolakan lalu 'return false' SEBELUM menyentuh stok mana pun.",
            "Perulangan kedua baru boleh berjalan setelah perulangan pertama "
            "selesai tanpa return. Di situlah stok dikurangi.",
            "Bukti kamu benar ada di baris 'APAR = 20' setelah percobaan 1. "
            "Kalau punyamu jadi 15, berarti kamu mengubah di perulangan yang "
            "sama dengan pemeriksaan - persis kesalahan yang dilatih di sini.",
        ],
        "solution": """import java.util.ArrayList;
import java.util.List;

public class LatihanAtomik {

    static class Item {
        String nama;
        int stok;

        Item(String nama, int stok) {
            this.nama = nama;
            this.stok = stok;
        }
    }

    static class Baris {
        Item item;
        int jumlah;

        Baris(Item item, int jumlah) {
            this.item = item;
            this.jumlah = jumlah;
        }
    }

    static boolean setujui(List<Baris> baris) {
        for (Baris b : baris) {
            if (b.item.stok < b.jumlah) {
                System.out.println("DITOLAK: stok " + b.item.nama
                        + " tidak cukup (tersedia " + b.item.stok
                        + ", diminta " + b.jumlah + ")");
                return false;
            }
        }
        for (Baris b : baris) {
            b.item.stok = b.item.stok - b.jumlah;
        }
        System.out.println("DISETUJUI");
        return true;
    }

    static void tampilkan(List<Item> semua) {
        for (Item i : semua) {
            System.out.println("  " + i.nama + " = " + i.stok);
        }
    }

    public static void main(String[] args) {
        Item apar = new Item("APAR", 20);
        Item selang = new Item("Selang", 3);

        List<Item> semua = new ArrayList<Item>();
        semua.add(apar);
        semua.add(selang);

        System.out.println("Stok awal:");
        tampilkan(semua);

        System.out.println("Percobaan 1: APAR 5, Selang 10");
        List<Baris> satu = new ArrayList<Baris>();
        satu.add(new Baris(apar, 5));
        satu.add(new Baris(selang, 10));
        setujui(satu);
        tampilkan(semua);

        System.out.println("Percobaan 2: APAR 5, Selang 3");
        List<Baris> dua = new ArrayList<Baris>();
        dua.add(new Baris(apar, 5));
        dua.add(new Baris(selang, 3));
        setujui(dua);
        tampilkan(semua);
    }
}""",
        "mode": "persis",
    },
    {
        "title": "Latihan 8: Kontrol Akses Berbasis Peran",
        "difficulty": "Lanjut",
        "question": [
            "Latihan ini meniru bug nyata di B-iFAMS: penanda hak akses sudah",
            "ditulis di semua controller, tapi tidak pernah aktif. Semua orang",
            "yang berhasil login bisa memanggil endpoint admin lewat URL langsung.",
            "",
            "Buat method:",
            "",
            "    static boolean boleh(String peran, String aksi)",
            "",
            "Aksi yang HANYA boleh ADMIN:",
            "    tambahItem, ubahStok, setujuiPermintaan, hapusKategori",
            "",
            "Aksi yang boleh SEMUA peran yang sudah login:",
            "    lihatItem, lihatKategori, ajukanPermintaan",
            "",
            "Aksi yang tidak dikenal harus DITOLAK, bukan diizinkan. Sistem yang",
            "mengizinkan hal tak dikenal akan bocor tiap kali ada fitur baru.",
            "",
            "Uji kedua peran terhadap kedelapan aksi, cetak sebagai matriks.",
            "Format: <peran> <aksi> -> BOLEH atau DITOLAK",
            "",
            "Cetak persis:",
            "",
            "ADMIN tambahItem -> BOLEH",
            "ADMIN ubahStok -> BOLEH",
            "ADMIN setujuiPermintaan -> BOLEH",
            "ADMIN hapusKategori -> BOLEH",
            "ADMIN lihatItem -> BOLEH",
            "ADMIN lihatKategori -> BOLEH",
            "ADMIN ajukanPermintaan -> BOLEH",
            "ADMIN aksiAsing -> DITOLAK",
            "REQUESTER tambahItem -> DITOLAK",
            "REQUESTER ubahStok -> DITOLAK",
            "REQUESTER setujuiPermintaan -> DITOLAK",
            "REQUESTER hapusKategori -> DITOLAK",
            "REQUESTER lihatItem -> BOLEH",
            "REQUESTER lihatKategori -> BOLEH",
            "REQUESTER ajukanPermintaan -> BOLEH",
            "REQUESTER aksiAsing -> DITOLAK",
        ],
        "hints": [
            "Simpan dua kumpulan aksi sebagai array String, lalu buat method "
            "bantu adaDi(daftar, aksi) yang menelusuri isinya.",
            "Urutan logikanya: kalau aksi ada di daftar semua-peran, izinkan. "
            "Kalau ada di daftar admin, izinkan hanya bila peran ADMIN. "
            "Kalau tidak ada di kedua daftar, TOLAK.",
            "Perhatikan ADMIN aksiAsing juga DITOLAK. Admin pun tidak boleh "
            "diizinkan melakukan hal yang tidak pernah didaftarkan - inilah "
            "yang disebut 'tolak secara bawaan'.",
        ],
        "solution": """public class LatihanHakAkses {

    static String[] AKSI_ADMIN = {
        "tambahItem", "ubahStok", "setujuiPermintaan", "hapusKategori"
    };

    static String[] AKSI_SEMUA = {
        "lihatItem", "lihatKategori", "ajukanPermintaan"
    };

    static boolean adaDi(String[] daftar, String aksi) {
        for (String a : daftar) {
            if (a.equals(aksi)) {
                return true;
            }
        }
        return false;
    }

    static boolean boleh(String peran, String aksi) {
        if (adaDi(AKSI_SEMUA, aksi)) {
            return true;
        }
        if (adaDi(AKSI_ADMIN, aksi)) {
            return peran.equals("ADMIN");
        }
        return false;
    }

    public static void main(String[] args) {
        String[] peran = { "ADMIN", "REQUESTER" };
        String[] aksi = {
            "tambahItem", "ubahStok", "setujuiPermintaan", "hapusKategori",
            "lihatItem", "lihatKategori", "ajukanPermintaan", "aksiAsing"
        };

        for (String p : peran) {
            for (String a : aksi) {
                String hasil = boleh(p, a) ? "BOLEH" : "DITOLAK";
                System.out.println(p + " " + a + " -> " + hasil);
            }
        }
    }
}""",
        "mode": "persis",
    },
]
