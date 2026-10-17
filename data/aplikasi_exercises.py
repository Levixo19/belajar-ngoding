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
            "Entitas adalah kelas yang mewakili satu benda nyata: field-nya "
            "privat, dan method-nya menjawab pertanyaan tentang dirinya "
            "sendiri. Baca ulang materi 'Entitas: Benda Menjadi Kelas'.",
            "Kelas bantu di dalam kelas utama harus 'static class' supaya bisa "
            "dipakai dari main tanpa membuat objek kelas luarnya. Constructor "
            "mengisi empat field dan memulai stok dari 0. stokMenipis() memakai "
            "<=, bukan <, karena stok yang sama dengan minimum sudah terhitung "
            "menipis.",
            "toString() dipanggil otomatis oleh System.out.println(objek), jadi "
            "kamu nggak perlu menulis println(item.toString()). Isinya cukup "
            "merangkai kode + \" - \" + nama + \" (\" + stok + \" \" + satuan + \")\".",
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
            "Kodenya dirakit dari tiga angka yang masing-masing punya lebar "
            "tetap, dengan nol di depan kalau kurang. Tahun dan bulan dikirim "
            "dari luar dengan alasan yang sama seperti di materi 'Menulis Uji "
            "Otomatis: Mock, MockMvc, dan Uji Integrasi': uji harus bisa "
            "memilih sendiri nilai yang dipakai kode.",
            "Dua digit terakhir tahun didapat dengan sisa bagi: 2026 % 100 = "
            "26. Untuk nol di depan pakai String.format: \"%02d\" mengubah 8 jadi "
            "\"08\"; angka 0 berarti 'isi dengan nol', angka 2 berarti 'lebar dua "
            "karakter'.",
            "Pola lengkapnya \"FS-%02d%02d-%03d\" dengan tiga nilai berurutan: "
            "tahun % 100, bulan, lalu urut.",
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
            "Ini aturan bisnis paling dasar, dan tempatnya di service. Baca "
            "ulang materi 'Service: Tempat Aturan Bisnis Hidup', terutama soal "
            "memeriksa sebelum mengubah.",
            "Urutan pemeriksaan menentukan pesan mana yang muncul: periksa "
            "jumlah <= 0 lebih dulu, baru bandingkan dengan stok. Pesan "
            "penolakan dicetak di dalam keluar(), sedangkan baris 'keluar N -> "
            "sisa M' dan 'stok tetap M' dicetak di main dengan membandingkan "
            "stok sebelum dan sesudah pemanggilan.",
            "Pakai jumlah > stok, bukan jumlah >= stok. Dengan >=, permintaan "
            "15 dari stok 15 ikut ditolak padahal seharusnya boleh.",
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
            "Opname artinya menghitung fisik barang di rak, lalu sistem yang "
            "mencari selisihnya dengan angka di database. Contoh kenapa opname "
            "dibutuhkan ada di materi 'Dua Pengguna Bersamaan: Race Condition "
            "dan Penguncian'.",
            "Selisih = hasilHitung - stokSistem. Kalau hasilnya negatif, tanda "
            "minusnya sudah ikut saat angka diubah jadi teks. Untuk selisih "
            "positif kamu harus menambahkan '+' sendiri, karena Java nggak "
            "pernah mencetak tanda plus.",
            "Selisih nol cukup dicetak '0', dan String.valueOf(0) sudah "
            "menghasilkan itu, jadi cabang negatif dan nol bisa digabung: kalau "
            "selisih > 0 pakai \"+\" + selisih, selain itu "
            "String.valueOf(selisih).",
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
            "Buku besar adalah daftar jejak: tiap perubahan stok jadi satu "
            "baris mutasi yang nggak diubah lagi. Baca ulang materi 'Model "
            "Data: dari Benda Nyata ke Tabel' bagian mutasi.",
            "Simpan stok sebagai field static supaya bisa diubah dari catat() "
            "dan terbawa antar pemanggilan. Jangan menyimpan qty sebagai angka "
            "negatif: buku besar sungguhan menyimpan jumlah positif, dan "
            "arahnya ditentukan kolom jenis.",
            "Buat satu method bantu menambah(jenis) yang mengembalikan true "
            "untuk IN dan RETURN. Pakai dua kali: saat menghitung stok, dan "
            "saat memilih tanda + atau - waktu mencetak.",
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
            "Status peminjaman berpindah lewat aturan yang tetap. Baca ulang "
            "materi 'Enum dan Exception Buatan Sendiri' untuk keempat "
            "statusnya, dan 'Service: Tempat Aturan Bisnis Hidup' untuk cara "
            "menolak perpindahan yang nggak sah.",
            "Perpindahan yang sah cuma tiga: PENDING+setujui, PENDING+tolak, "
            "dan APPROVED+kembalikan; selain itu semuanya ditolak. Pakai satu "
            "variabel 'baru' yang mula-mula null, isi kalau cocok salah satu "
            "aturan, dan kalau sesudah semua pemeriksaan masih null, berarti "
            "perpindahannya nggak sah.",
            "Format pesan suksesnya memakai dua tanda minus dan panah: status + "
            "\" --\" + aksi + \"--> \" + baru. Pesan penolakannya: \"DITOLAK: dari \" "
            "+ status + \" tidak bisa \" + aksi.",
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
            "Kebiasaan yang dilatih: periksa semuanya dulu, baru ubah. Data "
            "yang rusak separuh jalan lebih buruk daripada permintaan yang "
            "ditolak utuh. Baca ulang materi 'Service: Tempat Aturan Bisnis "
            "Hidup'.",
            "Perulangan pertama cuma memeriksa: begitu ketemu satu baris yang "
            "stoknya kurang, cetak penolakan lalu keluar dari method sebelum "
            "menyentuh stok mana pun. Perulangan kedua baru berjalan kalau yang "
            "pertama selesai tanpa keluar, dan di situlah stok dikurangi.",
            "Perulangan pertama bentuknya for (Baris b : baris) { if "
            "(b.item.stok < b.jumlah) { cetak penolakan; return false; } }. "
            "Bukti kamu benar ada di baris 'APAR = 20' sesudah percobaan 1; "
            "kalau punyamu jadi 15, berarti stoknya diubah di perulangan yang "
            "sama dengan pemeriksaan.",
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
            "Ini soal otorisasi: orangnya sudah login, pertanyaannya tinggal "
            "dia boleh apa. Baca ulang materi 'Keamanan: Autentikasi vs "
            "Otorisasi'.",
            "Simpan dua kumpulan aksi sebagai array String, lalu buat method "
            "bantu adaDi(daftar, aksi) yang menelusuri isinya. Urutan "
            "logikanya: kalau aksi ada di daftar semua peran, izinkan; kalau "
            "ada di daftar admin, izinkan cuma bila perannya ADMIN; kalau nggak "
            "ada di kedua daftar, tolak.",
            "Perhatikan ADMIN aksiAsing juga DITOLAK. Admin pun nggak boleh "
            "diizinkan melakukan hal yang nggak pernah didaftarkan; inilah yang "
            "disebut 'tolak secara bawaan'. Jadi baris terakhir boleh() adalah "
            "return false.",
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
    {
        'title': 'Proyek Akhir: Gudang Alat Berlapis',
        'difficulty': 'Lanjut',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Gudang Alat Berlapis',
        '',
        'Gudang alat sekolah dipinjam belasan orang tiap hari, dan buku',
        'catatannya sudah tidak bisa dipercaya. Kamu diminta menuliskan',
        'aturannya sebagai program.',
        '',
        'Proyek ini menutup seluruh modul: bukan satu kelas berisi segalanya,',
        'melainkan LAPISAN yang tiap bagiannya punya satu tanggung jawab --',
        'domain, penyimpanan, layanan, dan antarmuka. Batas antar lapisan',
        'itulah yang diuji: layanan tidak boleh mencetak apa pun, dan',
        'antarmuka tidak boleh memutuskan aturan apa pun.',
        '',
        'Alat: Obeng 8, Tang 2, Bor Listrik 1.',
        '',
        'Yang harus ada di programmu:',
        '  1. Domain: enum Peran, class Alat, class Pinjam, dan DUA exception',
        '     berbeda -- AturanDilanggar dan TidakBerhak.',
        '  2. Repo memegang data (LinkedHashMap supaya urutannya tetap) dan',
        '     TIDAK tahu apa pun tentang aturan.',
        '  3. Service memeriksa SELURUH syarat lebih dulu, baru mengubah data.',
        '     Alat tidak ada, jumlah <= 0, stok kurang, dan pinjam lebih dari 3',
        '     tanpa peran PENYELIA.',
        '  4. Setiap perubahan yang berhasil dicatat di jurnal.',
        '  5. Antarmuka (main) hanya menangkap exception dan mencetak. Kedua',
        '     jenis exception ditangkap TERPISAH dan diberi label berbeda.',
        '  6. Permintaan yang diproses berurutan: Andi OBN 2, Andi TNG 3,',
        '     Bunga BOR 2, Bunga OBN 4 (petugas), Bunga OBN 3 (penyelia),',
        '     Cici XXX 1. Lalu Andi mengembalikan OBN, dan mencoba BOR.',
        '  7. Daftar peminjam diurut alfabetis sebelum dicetak.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  GUDANG ALAT - LAPORAN HARI INI',
        '  ==============================================',
        '  Kode  Nama              Tersedia',
        '  OBN   Obeng                    5',
        '  TNG   Tang                     2',
        '  BOR   Bor Listrik              1',
        '  ----------------------------------------------',
        '  Sedang dipinjam:',
        '    Bunga : 3 alat',
        '  ----------------------------------------------',
        '  Jurnal (3 kejadian):',
        '    PINJAM OBN x2 oleh Andi',
        '    PINJAM OBN x3 oleh Bunga',
        '    KEMBALI OBN x2 dari Andi',
        '  ----------------------------------------------',
        '  Permintaan ditolak (5):',
        '    [aturan] Andi - Tang tersisa 2, diminta 3',
        '    [aturan] Bunga - Bor Listrik tersisa 1, diminta 2',
        '    [hak]    Bunga - pinjam lebih dari 3 butuh penyelia',
        '    [aturan] Cici - alat tidak ada: XXX',
        '    [aturan] Andi - tidak ada pinjaman BOR atas nama Andi',
    ],
        "hints": [
            "Proyek ini menguji batas antar lapisan: domain, repo, service, dan "
            "antarmuka masing-masing punya satu tanggung jawab. Baca ulang "
            "materi 'Lapisan-lapisan Aplikasi Web' dan 'Enum dan Exception "
            "Buatan Sendiri'.",
            "Service memeriksa seluruh syarat dengan urutan ini: alat ada, "
            "jumlah positif, stok cukup, lalu lebih dari 3 butuh PENYELIA. Baru "
            "sesudah itu ia mengubah data dan menulis jurnal. Ini aturan, bukan "
            "gaya: sekali stok dikurangi lalu exception dilempar, datanya sudah "
            "rusak dan nggak ada yang mengembalikannya.",
            "Urutan blok catch menentukan siapa yang kena: yang lebih khusus "
            "lebih dulu. TidakBerhak dan AturanDilanggar bersaudara, jadi "
            "urutan keduanya bebas, tapi keduanya harus sebelum catch "
            "RuntimeException. Untuk menjumlahkan pinjaman per orang, "
            "hitung.merge(p.peminjam, p.jumlah, Integer::sum) nggak perlu "
            "memeriksa apakah kuncinya sudah ada.",
        ],
        'solution': """import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/* ------------------------------------------------------------------ domain */

enum Peran { PETUGAS, PENYELIA }

class Alat {
    final String kode;
    final String nama;
    int tersedia;

    Alat(String kode, String nama, int tersedia) {
        this.kode = kode;
        this.nama = nama;
        this.tersedia = tersedia;
    }
}

class Pinjam {
    final String kode;
    final String peminjam;
    final int jumlah;
    boolean dikembalikan = false;

    Pinjam(String kode, String peminjam, int jumlah) {
        this.kode = kode;
        this.peminjam = peminjam;
        this.jumlah = jumlah;
    }
}

class AturanDilanggar extends RuntimeException {
    AturanDilanggar(String pesan) { super(pesan); }
}

class TidakBerhak extends RuntimeException {
    TidakBerhak(String pesan) { super(pesan); }
}

/* ------------------------------------------------------------- penyimpanan */

class GudangRepo {
    private final Map<String, Alat> alat = new LinkedHashMap<>();
    private final List<Pinjam> pinjaman = new ArrayList<>();

    void simpan(Alat a) { alat.put(a.kode, a); }
    Alat cari(String kode) { return alat.get(kode); }
    List<Alat> semua() { return new ArrayList<>(alat.values()); }
    void catat(Pinjam p) { pinjaman.add(p); }
    List<Pinjam> pinjaman() { return pinjaman; }
}

/* ------------------------------------------------------------------ layanan */

class GudangService {
    private final GudangRepo repo;
    private final List<String> jurnal = new ArrayList<>();

    GudangService(GudangRepo repo) { this.repo = repo; }

    List<String> jurnal() { return jurnal; }

    /** Periksa DULU seluruh syaratnya, baru ubah apa pun. */
    void pinjam(Peran peran, String kode, String peminjam, int jumlah) {
        Alat a = repo.cari(kode);
        if (a == null) throw new AturanDilanggar("alat tidak ada: " + kode);
        if (jumlah <= 0) throw new AturanDilanggar("jumlah harus positif");
        if (jumlah > a.tersedia) {
            throw new AturanDilanggar(
                    a.nama + " tersisa " + a.tersedia + ", diminta " + jumlah);
        }
        if (jumlah > 3 && peran != Peran.PENYELIA) {
            throw new TidakBerhak("pinjam lebih dari 3 butuh penyelia");
        }
        a.tersedia -= jumlah;
        repo.catat(new Pinjam(kode, peminjam, jumlah));
        jurnal.add("PINJAM " + kode + " x" + jumlah + " oleh " + peminjam);
    }

    void kembalikan(String kode, String peminjam) {
        for (Pinjam p : repo.pinjaman()) {
            if (p.kode.equals(kode) && p.peminjam.equals(peminjam)
                    && !p.dikembalikan) {
                p.dikembalikan = true;
                repo.cari(kode).tersedia += p.jumlah;
                jurnal.add("KEMBALI " + kode + " x" + p.jumlah + " dari " + peminjam);
                return;
            }
        }
        throw new AturanDilanggar("tidak ada pinjaman " + kode + " atas nama " + peminjam);
    }

    Map<String, Integer> sedangDipinjam() {
        Map<String, Integer> hitung = new HashMap<>();
        for (Pinjam p : repo.pinjaman()) {
            if (!p.dikembalikan) {
                hitung.merge(p.peminjam, p.jumlah, Integer::sum);
            }
        }
        return hitung;
    }
}

/* -------------------------------------------------------------- antarmuka */

public class ProyekPeminjaman {
    static GudangService layanan;
    static List<String> ditolak = new ArrayList<>();

    static void coba(Peran peran, String kode, String siapa, int jumlah) {
        try {
            layanan.pinjam(peran, kode, siapa, jumlah);
        } catch (TidakBerhak e) {
            ditolak.add("[hak]    " + siapa + " - " + e.getMessage());
        } catch (AturanDilanggar e) {
            ditolak.add("[aturan] " + siapa + " - " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        GudangRepo repo = new GudangRepo();
        repo.simpan(new Alat("OBN", "Obeng", 8));
        repo.simpan(new Alat("TNG", "Tang", 2));
        repo.simpan(new Alat("BOR", "Bor Listrik", 1));
        layanan = new GudangService(repo);

        coba(Peran.PETUGAS,  "OBN", "Andi", 2);
        coba(Peran.PETUGAS,  "TNG", "Andi", 3);
        coba(Peran.PETUGAS,  "BOR", "Bunga", 2);
        coba(Peran.PETUGAS,  "OBN", "Bunga", 4);
        coba(Peran.PENYELIA, "OBN", "Bunga", 3);
        coba(Peran.PETUGAS,  "XXX", "Cici", 1);

        try {
            layanan.kembalikan("OBN", "Andi");
            layanan.kembalikan("BOR", "Andi");
        } catch (AturanDilanggar e) {
            ditolak.add("[aturan] Andi - " + e.getMessage());
        }

        System.out.println("GUDANG ALAT - LAPORAN HARI INI");
        System.out.println("==============================================");
        System.out.printf("%-6s%-16s%10s%n", "Kode", "Nama", "Tersedia");
        for (Alat a : repo.semua()) {
            System.out.printf("%-6s%-16s%10d%n", a.kode, a.nama, a.tersedia);
        }

        System.out.println("----------------------------------------------");
        System.out.println("Sedang dipinjam:");
        Map<String, Integer> pinjam = layanan.sedangDipinjam();
        List<String> nama = new ArrayList<>(pinjam.keySet());
        nama.sort(String::compareTo);
        for (String n : nama) System.out.println("  " + n + " : " + pinjam.get(n) + " alat");

        System.out.println("----------------------------------------------");
        System.out.println("Jurnal (" + layanan.jurnal().size() + " kejadian):");
        for (String j : layanan.jurnal()) System.out.println("  " + j);

        System.out.println("----------------------------------------------");
        System.out.println("Permintaan ditolak (" + ditolak.size() + "):");
        for (String d : ditolak) System.out.println("  " + d);
    }
}
""",
    },
]
