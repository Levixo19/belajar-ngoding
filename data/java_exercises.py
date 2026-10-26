JAVA_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program yang menampilkan:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Java.",
            "",
            "Tulis PERSIS seperti di atas, termasuk nama Andi -- penilaian",
            "membandingkan outputmu huruf demi huruf.",
            "",
            "Keluaran yang diharapkan:",
            "    Halo, namaku Andi!",
            "    Aku sedang belajar Java.",
        ],
        "hints": [
            "Satu baris keluaran butuh satu perintah cetak. Baca ulang materi 'Pengenalan Java & Persiapan' bagian program pertamamu.",
            "Pakai System.out.println() dua kali, satu untuk tiap baris. Teksnya diapit tanda kutip ganda, dan tiap perintah ditutup titik koma (;).",
            "Penilaian membandingkan huruf demi huruf, jadi salin teksnya apa adanya, termasuk koma, tanda seru, dan titik di akhir baris kedua.",
        ],
        "solution": """public class Halo {
    public static void main(String[] args) {
        System.out.println("Halo, namaku Andi!");
        System.out.println("Aku sedang belajar Java.");
    }
}""",
    },
    {
        "title": "Latihan 2: Kalkulator Sederhana",
        "difficulty": "Mudah",
        "question": [
            "Buat program dengan 2 variabel int (misal 15 dan 4).",
            "Tampilkan hasil: penjumlahan, pengurangan, perkalian,",
            "pembagian (int), dan sisa bagi.",
            "",
            "Keluaran yang diharapkan:",
            "    15 + 4 = 19",
            "    15 - 4 = 11",
            "    15 * 4 = 60",
            "    15 / 4 = 3",
            "    15 % 4 = 3",
        ],
        "hints": [
            "Simpan kedua angka di variabel int, lalu hitung dengan operator aritmetika. Materi 'Operator' membahas kelimanya, termasuk sisa bagi.",
            "Operatornya +, -, *, /, dan %. Ingat, int dibagi int hasilnya int: 15 / 4 jadi 3, pecahannya dibuang, dan sisanya bisa diambil lewat %.",
            "Format tiap baris seperti 15 + 4 = 19. Rangkai dengan +, misalnya a + \" + \" + b + \" = \" + (a + b); kurung terakhir wajib, kalau nggak angkanya disambung jadi teks \"154\".",
        ],
        "solution": """public class Kalkulator {
    public static void main(String[] args) {
        int a = 15;
        int b = 4;

        System.out.println(a + " + " + b + " = " + (a + b));
        System.out.println(a + " - " + b + " = " + (a - b));
        System.out.println(a + " * " + b + " = " + (a * b));
        System.out.println(a + " / " + b + " = " + (a / b));
        System.out.println(a + " % " + b + " = " + (a % b));
    }
}""",
    },
    {
        "title": "Latihan 3: Cek Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Buat program: baca satu angka nilai memakai Scanner.",
            "Jika nilai >= 75 tampilkan 'Lulus', selain itu 'Tidak Lulus'.",
            "",
            "Jangan cetak teks prompt apa pun. Program hanya boleh mengeluarkan",
            "satu baris berisi Lulus atau Tidak Lulus.",
            "",
            "Untuk input 80, keluarannya:",
            "    Lulus",
        ],
        "hints": [
            "Kamu perlu membaca satu angka lalu memilih satu dari dua keluaran. Baca ulang 'String & Scanner (Input)' untuk membaca input dan 'Percabangan (if / switch)' untuk if-else.",
            "Import Scanner dari java.util, buat Scanner yang membaca System.in, ambil angkanya dengan nextInt(), lalu bandingkan dengan 75 memakai >=. Jangan cetak teks prompt apa pun.",
            "Bagian pembacanya: Scanner sc = new Scanner(System.in); lalu int nilai = sc.nextInt(); Ingat: kalau sesudah nextInt() kamu memanggil nextLine(), tambahkan satu sc.nextLine() dulu untuk membuang sisa barisnya.",
        ],
        # Beberapa input supaya SEMUA cabang benar-benar diuji; dengan
        # satu input saja, jawaban yang di-hardcode ikut dinyatakan benar.
        "stdin_list": ["80\n", "60\n"],
        "solution": """import java.util.Scanner;

public class CekNilai {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int nilai = sc.nextInt();

        if (nilai >= 75) {
            System.out.println("Lulus");
        } else {
            System.out.println("Tidak Lulus");
        }
        sc.close();
    }
}""",
    },
    {
        "title": "Latihan 4: Deret Angka Genap",
        "difficulty": "Menengah",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20",
            "beserta total jumlahnya.",
            "",
            "Keluaran yang diharapkan (dua baris):",
            "",
            "  2 4 6 8 10 12 14 16 18 20",
            "  Total: 110",
        ],
        "hints": [
            "Ini soal perulangan plus pengecekan genap. Materi 'Perulangan (Loop)' dan operator sisa bagi di materi 'Operator' yang kamu perlukan.",
            "Loop dari 1 sampai 20. Kalau angkanya habis dibagi 2 (n % 2 == 0), cetak angka itu diikuti spasi lewat System.out.print tanpa ln, lalu tambahkan ke variabel total. Sesudah loop, pindah baris dan cetak totalnya.",
            "Keluarannya dua baris: deret '2 4 6 ... 20' lalu 'Total: 110'. Spasi di ujung baris pertama nggak dihitung.",
        ],
        "solution": """public class Genap {
    public static void main(String[] args) {
        int total = 0;
        for (int i = 1; i <= 20; i++) {
            if (i % 2 == 0) {
                System.out.print(i + " ");
                total += i;
            }
        }
        System.out.println();
        System.out.println("Total: " + total);
    }
}""",
    },
    {
        "title": "Latihan 5: Pola Bintang",
        "difficulty": "Menengah",
        "question": [
            "Buat pola segitiga siku-siku dari bintang:",
            "  *",
            "  **",
            "  ***",
            "  ****",
            "  *****",
            "",
            "Keluaran yang diharapkan:",
            "    *",
            "    **",
            "    ***",
            "    ****",
            "    *****",
        ],
        "hints": [
            "Pola bertingkat seperti ini dibuat dengan perulangan di dalam perulangan. Baca ulang bagian perulangan bersarang (nested loop) di materi 'Perulangan (Loop)'.",
            "Loop luar menghitung baris dari 1 sampai 5. Loop dalam mencetak bintang sebanyak nomor baris itu, jadi batasnya bergantung pada variabel loop luar.",
            "Di loop dalam pakai System.out.print(\"*\") tanpa ln supaya bintangnya berderet. Sesudah loop dalam selesai, panggil System.out.println() untuk ganti baris.",
        ],
        "solution": """public class PolaBintang {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}""",
    },
    {
        "title": "Latihan 6: Nilai Terbesar dalam Array",
        "difficulty": "Menengah",
        "question": [
            "Buat program untuk mencari nilai terbesar dan terkecil",
            "dari array berikut:",
            "int[] data = {23, 5, 87, 12, 55, 99, 31};",
            "",
            "Keluaran yang diharapkan:",
            "    Terbesar: 99",
            "    Terkecil: 5",
        ],
        "hints": [
            "Mencari nilai terbesar dan terkecil berarti menelusuri array sambil mengingat juara sementara. Baca ulang materi 'Array' bagian menelusuri isi array dengan loop.",
            "Anggap elemen pertama sebagai terbesar sekaligus terkecil. Telusuri sisanya satu per satu, dan ganti juaranya tiap kali ketemu yang lebih besar atau lebih kecil.",
            "Mulai dengan int max = data[0]; dan int min = data[0]; lalu di dalam loop: if (data[i] > max) max = data[i]; Keluaran yang dinilai dua baris: 'Terbesar: 99' dan 'Terkecil: 5'.",
        ],
        "solution": """public class CariMinMax {
    public static void main(String[] args) {
        int[] data = {23, 5, 87, 12, 55, 99, 31};

        int max = data[0];
        int min = data[0];

        for (int i = 1; i < data.length; i++) {
            if (data[i] > max) max = data[i];
            if (data[i] < min) min = data[i];
        }

        System.out.println("Terbesar: " + max);
        System.out.println("Terkecil: " + min);
    }
}""",
    },
    {
        "title": "Latihan 7: Method Hitung Luas",
        "difficulty": "Menengah",
        "question": [
            "Buat 3 method:",
            "  1. luasPersegi(int sisi)      -> sisi * sisi",
            "  2. luasPersegiPanjang(p, l)   -> p * l",
            "  3. luasLingkaran(double r)    -> Math.PI * r * r",
            "Panggil ketiganya di main dan tampilkan hasilnya.",
            "",
            "Keluaran yang diharapkan:",
            "    Persegi (5): 25",
            "    Persegi Panjang (4x6): 24",
            "    Lingkaran (r=7): 154",
        ],
        "hints": [
            "Latihan ini soal membuat method yang menerima parameter dan mengembalikan nilai. Materi 'Method (Fungsi)' membahas return dan tipe kembalian.",
            "Buat tiga method static di luar main. Dua yang pertama mengembalikan int; luasLingkaran mengembalikan double dan memakai Math.PI yang sudah disediakan Java.",
            "Panggil dengan nama method lalu argumennya, misalnya luasPersegi(5). Keluaran yang dinilai: 'Persegi (5): 25', 'Persegi Panjang (4x6): 24', dan 'Lingkaran (r=7): 154'; luas lingkarannya dibulatkan dengan Math.round().",
        ],
        "solution": """public class Luas {
    static int luasPersegi(int sisi) {
        return sisi * sisi;
    }

    static int luasPersegiPanjang(int p, int l) {
        return p * l;
    }

    static double luasLingkaran(double r) {
        return Math.PI * r * r;
    }

    public static void main(String[] args) {
        System.out.println("Persegi (5): " + luasPersegi(5));
        System.out.println("Persegi Panjang (4x6): " + luasPersegiPanjang(4, 6));
        System.out.println("Lingkaran (r=7): " + Math.round(luasLingkaran(7)));
    }
}""",
    },
    {
        "title": "Latihan 8: Class BankAccount",
        "difficulty": "Menengah",
        "question": [
            "Buat class Rekening dengan:",
            "  - attribute private: nomor (String), saldo (double)",
            "  - constructor mengisi keduanya",
            "  - method getter untuk nomor dan saldo",
            "  - method setor(double) dan tarik(double)",
            "    (tarik hanya boleh jika saldo cukup)",
            "  - method info() menampilkan nomor & saldo",
            "",
            "Keluaran yang diharapkan:",
            "    No: 12345 | Saldo: 100000.0",
            "    Berhasil setor: 50000.0",
            "    Berhasil tarik: 20000.0",
            "    Gagal: saldo tidak cukup.",
            "    No: 12345 | Saldo: 130000.0",
        ],
        "hints": [
            "Ini latihan encapsulation: data disembunyikan dengan private dan cuma bisa diubah lewat method. Baca ulang materi 'OOP: Encapsulation' dan 'Anggota Class: Constructor, static, dan Konstanta'.",
            "Di constructor, parameter yang namanya sama dengan field dibedakan dengan this. tarik() memeriksa dulu apakah jumlahnya positif dan saldonya cukup, lalu mengembalikan boolean: true kalau berhasil, false kalau gagal.",
            "Penilai mengikuti main contoh: rekening \"12345\" bersaldo 100000, info(), setor 50000, tarik 20000, tarik 200000, lalu info() lagi. Barisnya: 'No: 12345 | Saldo: 100000.0', 'Berhasil setor: 50000.0', 'Berhasil tarik: 20000.0', 'Gagal: saldo tidak cukup.', 'No: 12345 | Saldo: 130000.0'.",
        ],
        "solution": """public class Rekening {
    private String nomor;
    private double saldo;

    public Rekening(String nomor, double saldo) {
        this.nomor = nomor;
        this.saldo = saldo;
    }

    public String getNomor() { return nomor; }
    public double getSaldo() { return saldo; }

    public void setor(double jumlah) {
        if (jumlah > 0) {
            saldo += jumlah;
            System.out.println("Berhasil setor: " + jumlah);
        }
    }

    public boolean tarik(double jumlah) {
        if (jumlah > 0 && jumlah <= saldo) {
            saldo -= jumlah;
            System.out.println("Berhasil tarik: " + jumlah);
            return true;
        }
        System.out.println("Gagal: saldo tidak cukup.");
        return false;
    }

    public void info() {
        System.out.println("No: " + nomor + " | Saldo: " + saldo);
    }

    public static void main(String[] args) {
        Rekening r = new Rekening("12345", 100000);
        r.info();
        r.setor(50000);
        r.tarik(20000);
        r.tarik(200000);   // gagal
        r.info();
    }
}""",
    },
    {
        "title": "Latihan 9: Pewarisan Hewan",
        "difficulty": "Menengah",
        "question": [
            "Buat class Hewan (nama, method bersuara()).",
            "Buat subclass Kucing dan Anjing yang me-@Override bersuara().",
            "Di main, buat array Hewan berisi keduanya dan",
            "panggil bersuara() untuk semua (polymorphism).",
            "",
            "Keluaran yang diharapkan:",
            "    Tom: Meow!",
            "    Bobby: Guk!",
        ],
        "hints": [
            "Ini latihan inheritance dan polymorphism: satu array bertipe induk berisi objek anak, dan tiap objek menjalankan versinya sendiri. Baca ulang 'OOP: Inheritance (Pewarisan)' dan 'OOP: Polymorphism'.",
            "Kucing dan Anjing meng-extends Hewan dan memanggil super(nama) di constructor-nya. Masing-masing menimpa bersuara() dengan @Override. Di main, isi array Hewan dengan keduanya lalu telusuri dengan for-each.",
            "Keluaran yang dinilai: 'Tom: Meow!' lalu 'Bobby: Guk!', jadi kucingnya bernama Tom dan anjingnya Bobby. Array-nya bisa ditulis Hewan[] hewan = {new Kucing(\"Tom\"), new Anjing(\"Bobby\")};",
        ],
        "solution": """class Hewan {
    String nama;
    Hewan(String nama) { this.nama = nama; }
    void bersuara() {
        System.out.println(nama + " bersuara.");
    }
}

class Kucing extends Hewan {
    Kucing(String nama) { super(nama); }
    @Override
    void bersuara() {
        System.out.println(nama + ": Meow!");
    }
}

class Anjing extends Hewan {
    Anjing(String nama) { super(nama); }
    @Override
    void bersuara() {
        System.out.println(nama + ": Guk!");
    }
}

public class Main {
    public static void main(String[] args) {
        Hewan[] hewan = {new Kucing("Tom"), new Anjing("Bobby")};
        for (Hewan h : hewan) {
            h.bersuara();
        }
    }
}""",
    },
    {
        "title": "Latihan 10: Interface & Exception",
        "difficulty": "Lanjut",
        "question": [
            "1. Buat interface Hitung dengan method hitung(double a, double b).",
            "2. Buat class Tambah dan Kurang yang implements Hitung.",
            "3. Di main, tangani pembagian dengan nol memakai try-catch.",
            "",
            "Keluaran yang diharapkan:",
            "    Tambah: 13.0",
            "    Kurang: 7.0",
            "    Error: pembagian dengan nol!",
        ],
        "hints": [
            "Ada dua konsep di sini: interface sebagai kontrak, dan try-catch untuk menangkap error. Baca ulang 'OOP: Abstract & Interface' dan 'Exception Handling'.",
            "Method di interface otomatis public abstract, jadi di class yang meng-implements-nya method itu wajib ditulis public. Uji Tambah dan Kurang dengan angka 10 dan 3, lalu picu pembagian int 10 / 0 di dalam try dan tangkap ArithmeticException.",
            "Keluaran yang dinilai: 'Tambah: 13.0', 'Kurang: 7.0', lalu 'Error: pembagian dengan nol!'. Ada .0 karena hitung() mengembalikan double. Jebakan: pembagian double seperti 10.0 / 0 nggak melempar exception (hasilnya Infinity), jadi yang dibagi nol harus int.",
        ],
        "solution": """interface Hitung {
    double hitung(double a, double b);
}

class Tambah implements Hitung {
    public double hitung(double a, double b) { return a + b; }
}

class Kurang implements Hitung {
    public double hitung(double a, double b) { return a - b; }
}

public class Main {
    public static void main(String[] args) {
        Hitung t = new Tambah();
        Hitung k = new Kurang();
        System.out.println("Tambah: " + t.hitung(10, 3));
        System.out.println("Kurang: " + k.hitung(10, 3));

        try {
            int hasil = 10 / 0;
            System.out.println(hasil);
        } catch (ArithmeticException e) {
            System.out.println("Error: pembagian dengan nol!");
        }
    }
}""",
    },
    {
        "title": "Latihan 11: Filter & Transform dengan Stream",
        "difficulty": "Lanjut",
        "question": [
            "Diberikan List<String> nama = List.of(\"Andi\",\"Budi\",\"Citra\",",
            "\"Dedi\",\"Eka\",\"Farhan\"). Menggunakan Stream API:",
            "  1. Ambil nama yang panjangnya lebih dari 4 huruf.",
            "  2. Ubah jadi huruf besar semua.",
            "  3. Urutkan berdasarkan abjad.",
            "  4. Gabungkan jadi satu String dipisah ', '.",
            "Lakukan dalam satu rangkaian stream (method chaining).",
            "",
            "Keluaran yang diharapkan:",
            "    CITRA, FARHAN",
        ],
        "hints": [
            "Rangkaian stream bekerja seperti ban berjalan: tiap langkah mengolah hasil langkah sebelumnya. Baca ulang materi 'Stream API', terutama operasi perantara dan Collectors.",
            "Urutannya: saring yang panjangnya lebih dari 4 (filter), ubah ke huruf besar (map), urutkan (sorted), lalu kumpulkan jadi satu String (collect). Jangan lupa import java.util.stream.Collectors.",
            "Untuk huruf besar pakai method reference String::toUpperCase, dan untuk langkah terakhir Collectors.joining(\", \"). Hasil yang benar cuma satu baris: CITRA, FARHAN.",
        ],
        "solution": """import java.util.List;
import java.util.stream.Collectors;

public class FilterNama {
    public static void main(String[] args) {
        List<String> nama = List.of("Andi", "Budi", "Citra", "Dedi", "Eka", "Farhan");

        String hasil = nama.stream()
                .filter(s -> s.length() > 4)
                .map(String::toUpperCase)
                .sorted()
                .collect(Collectors.joining(", "));

        System.out.println(hasil);   // CITRA, FARHAN
    }
}""",
    },
    {
        "title": "Latihan 12: Kotak Generic",
        "difficulty": "Lanjut",
        "question": [
            "Buat class generic Pasangan<K, V> yang menyimpan sepasang",
            "nilai (key & value) dengan:",
            "  - constructor mengisi key & value",
            "  - getter getKey() dan getValue()",
            "  - method tukar() yang mengembalikan Pasangan<V, K> baru",
            "    dengan posisi key-value dibalik",
            "Uji dengan Pasangan<String, Integer> lalu tukar posisinya.",
            "",
            "Keluaran yang diharapkan:",
            "    (Andi, 20)",
            "    (20, Andi)",
        ],
        "hints": [
            "Class generic memakai parameter tipe seperti K dan V, yang baru ditentukan saat objeknya dibuat. Baca ulang materi 'Generics'.",
            "Simpan key bertipe K dan value bertipe V sebagai field private, isi lewat constructor, lalu buat getter-nya. tukar() mengembalikan Pasangan<V, K>: urutan parameter tipenya dibalik, begitu juga isinya.",
            "Isi tukar() cukup satu baris yang membuat Pasangan baru dengan value di depan dan key di belakang; diamond <> menyimpulkan tipenya sendiri. Supaya println mencetak (Andi, 20) lalu (20, Andi), timpa toString() supaya mengembalikan \"(\" + key + \", \" + value + \")\".",
        ],
        "solution": """public class Pasangan<K, V> {
    private K key;
    private V value;

    public Pasangan(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }

    public Pasangan<V, K> tukar() {
        return new Pasangan<>(value, key);
    }

    @Override
    public String toString() {
        return "(" + key + ", " + value + ")";
    }

    public static void main(String[] args) {
        Pasangan<String, Integer> p = new Pasangan<>("Andi", 20);
        System.out.println(p);           // (Andi, 20)

        Pasangan<Integer, String> terbalik = p.tukar();
        System.out.println(terbalik);    // (20, Andi)
    }
}""",
    },
    {
        "title": "Latihan 13: Simulasi Antrian dengan Multithreading",
        "difficulty": "Sulit",
        "question": [
            "Buat class LoketAntrian dengan method synchronized layani()",
            "yang mensimulasikan pelayanan nasabah (Thread.sleep 100ms lalu",
            "cetak 'Nasabah ke-N dilayani'). Buat 5 thread yang memanggil",
            "layani() secara bersamaan. Pastikan penomoran nasabah tidak",
            "tumpang tindih (race condition) dengan synchronized + counter.",
            "",
            "Keluaran yang diharapkan:",
            "    Nasabah ke-1 mulai dilayani...",
            "    Nasabah ke-1 selesai dilayani.",
            "    Nasabah ke-2 mulai dilayani...",
            "    Nasabah ke-2 selesai dilayani.",
            "    Nasabah ke-3 mulai dilayani...",
            "    Nasabah ke-3 selesai dilayani.",
            "    Nasabah ke-4 mulai dilayani...",
            "    Nasabah ke-4 selesai dilayani.",
            "    Nasabah ke-5 mulai dilayani...",
            "    Nasabah ke-5 selesai dilayani.",
            "    Semua nasabah selesai dilayani.",
        ],
        "hints": [
            "Race condition terjadi kalau beberapa thread mengubah data yang sama bersamaan. Baca ulang 'Multithreading & Concurrency Dasar', bagian synchronized, start(), dan join().",
            "Jadikan counter field LoketAntrian dan naikkan di dalam method synchronized layani(), lalu simpan nomornya di variabel lokal sebelum Thread.sleep(100). Kelima thread harus memanggil objek loket yang sama; start() semuanya dulu, baru join() semuanya.",
            "Thread.sleep() bisa melempar InterruptedException, jadi bungkus dengan try-catch. Tiap nasabah mencetak 'Nasabah ke-N mulai dilayani...' dan 'Nasabah ke-N selesai dilayani.', lalu di akhir 'Semua nasabah selesai dilayani.'. Thread-nya bisa dibuat dengan new Thread(loket::layani).",
        ],
        "solution": """class LoketAntrian {
    private int counter = 0;

    public synchronized void layani() {
        counter++;
        int nomorSaya = counter;
        System.out.println("Nasabah ke-" + nomorSaya + " mulai dilayani...");
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Nasabah ke-" + nomorSaya + " selesai dilayani.");
    }
}

public class SimulasiAntrian {
    public static void main(String[] args) throws InterruptedException {
        LoketAntrian loket = new LoketAntrian();
        Thread[] nasabah = new Thread[5];

        for (int i = 0; i < 5; i++) {
            nasabah[i] = new Thread(loket::layani);
        }
        for (Thread t : nasabah) {
            t.start();
        }
        for (Thread t : nasabah) {
            t.join();
        }
        System.out.println("Semua nasabah selesai dilayani.");
    }
}""",
    },
    {
        "title": "Latihan 14: Sistem Manajemen Mahasiswa (JDBC + OOP)",
        "difficulty": "Sulit",
        "question": [
            "Rancang (tulis kode, tidak perlu database sungguhan) sebuah",
            "class MahasiswaRepository yang memakai JDBC untuk:",
            "  1. simpan(Mahasiswa m)   -> INSERT data baru",
            "  2. cariByNim(int nim)    -> SELECT satu data, kembalikan Optional<Mahasiswa>",
            "  3. semua()               -> SELECT semua data, kembalikan List<Mahasiswa>",
            "Gunakan PreparedStatement, try-with-resources, dan Optional",
            "untuk cariByNim (agar aman jika data tidak ditemukan).",
        ],
        "hints": [
            "Tiap method repository membuka koneksi, menjalankan satu query, lalu menutup semuanya. Baca ulang 'JDBC: Menghubungkan Java ke Database' dan 'Optional & Null Safety'.",
            "Buat dulu class Mahasiswa (nim, nama, jurusan, ipk). Di tiap method, buka Connection dan PreparedStatement di dalam try-with-resources, isi tanda tanyanya dengan setInt/setString/setDouble, lalu pakai executeUpdate() untuk INSERT dan executeQuery() untuk SELECT.",
            "Di cariByNim: kalau rs.next() bernilai true, kembalikan Optional.of(new Mahasiswa(...)); kalau nggak, Optional.empty(). Di semua(), ulangi while (rs.next()) dan tambahkan tiap baris ke ArrayList.",
        ],
        "auto_check": False,
        "alasan_tidak_dicek": "butuh server database MySQL dan driver JDBC",
        "solution": """import java.sql.*;
import java.util.*;

class Mahasiswa {
    int nim;
    String nama, jurusan;
    double ipk;

    Mahasiswa(int nim, String nama, String jurusan, double ipk) {
        this.nim = nim; this.nama = nama; this.jurusan = jurusan; this.ipk = ipk;
    }

    @Override
    public String toString() {
        return nim + " - " + nama + " - " + jurusan + " - " + ipk;
    }
}

class MahasiswaRepository {
    private final String url = "jdbc:mysql://localhost:3306/belajar_db";
    private final String user = "root";
    private final String pass = "password";

    public void simpan(Mahasiswa m) throws SQLException {
        String sql = "INSERT INTO mahasiswa (nim, nama, jurusan, ipk) VALUES (?, ?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(url, user, pass);
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, m.nim);
            stmt.setString(2, m.nama);
            stmt.setString(3, m.jurusan);
            stmt.setDouble(4, m.ipk);
            stmt.executeUpdate();
        }
    }

    public Optional<Mahasiswa> cariByNim(int nim) throws SQLException {
        String sql = "SELECT nim, nama, jurusan, ipk FROM mahasiswa WHERE nim = ?";
        try (Connection conn = DriverManager.getConnection(url, user, pass);
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, nim);
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(new Mahasiswa(
                            rs.getInt("nim"), rs.getString("nama"),
                            rs.getString("jurusan"), rs.getDouble("ipk")));
                }
                return Optional.empty();
            }
        }
    }

    public List<Mahasiswa> semua() throws SQLException {
        List<Mahasiswa> hasil = new ArrayList<>();
        String sql = "SELECT nim, nama, jurusan, ipk FROM mahasiswa";
        try (Connection conn = DriverManager.getConnection(url, user, pass);
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {
            while (rs.next()) {
                hasil.add(new Mahasiswa(rs.getInt("nim"), rs.getString("nama"),
                        rs.getString("jurusan"), rs.getDouble("ipk")));
            }
        }
        return hasil;
    }
}""",
    },
    {
        "title": "Latihan 15: Unit Test untuk Rekening Bank",
        "difficulty": "Sulit",
        "question": [
            "Menggunakan class Rekening dari Latihan 8, tulis unit test",
            "dengan JUnit 5 yang mencakup:",
            "  1. setor() menambah saldo dengan benar.",
            "  2. tarik() mengurangi saldo jika cukup.",
            "  3. tarik() mengembalikan false jika saldo tidak cukup",
            "     (dan saldo TIDAK berubah).",
            "  4. Gunakan @BeforeEach untuk membuat objek Rekening baru",
            "     sebelum setiap test agar antar-test tidak saling memengaruhi.",
        ],
        "hints": [
            "Tiap tes harus mulai dari objek yang segar supaya hasil satu tes nggak memengaruhi tes lain. Baca ulang 'Unit Testing dengan JUnit', bagian anotasi dan assertion.",
            "Jadikan Rekening field di class tes, lalu isi ulang di method bertanda @BeforeEach. Buat satu method @Test untuk tiap kasus: setor, tarik yang berhasil, dan tarik yang gagal.",
            "Cek saldo dengan assertEquals(harapan, rekening.getSaldo()). Untuk kasus gagal pakai assertFalse(rekening.tarik(999999)), lalu pastikan saldonya masih 100000.",
        ],
        "auto_check": False,
        "alasan_tidak_dicek": "butuh pustaka JUnit 5 dan class Rekening terpisah",
        "solution": """import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

class RekeningTest {
    Rekening rekening;

    @BeforeEach
    void setUp() {
        rekening = new Rekening("12345", 100000);
    }

    @Test
    void testSetorMenambahSaldo() {
        rekening.setor(50000);
        assertEquals(150000, rekening.getSaldo());
    }

    @Test
    void testTarikBerhasilJikaSaldoCukup() {
        boolean hasil = rekening.tarik(30000);
        assertTrue(hasil);
        assertEquals(70000, rekening.getSaldo());
    }

    @Test
    void testTarikGagalJikaSaldoTidakCukup() {
        boolean hasil = rekening.tarik(999999);
        assertFalse(hasil);
        assertEquals(100000, rekening.getSaldo());  // saldo tidak berubah
    }
}""",
    },
    {
        'title': 'Proyek Akhir: Simulasi Lift Gedung',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Simulasi Lift Gedung',
        '',
        'Lift di gedung 5 lantai sering dikeluhkan: kadang naik padahal semua',
        'yang menunggu ada di bawah. Sebelum mengganti panel kendalinya, kamu',
        'diminta MENIRU perilakunya dulu dalam program, supaya bisa dilihat',
        'detik demi detik apa yang sebenarnya terjadi.',
        '',
        'Ini bukan program yang mengumpulkan data lalu mencetak laporan. Ini',
        'SIMULASI: ada keadaan yang berubah tiap detik, dan setiap barisnya',
        'adalah potret keadaan itu.',
        '',
        'Permintaan yang masuk (detik, dari lantai, ke lantai):',
        '  detik 0: lantai 3 -> 1',
        '  detik 1: lantai 1 -> 5',
        '  detik 4: lantai 4 -> 2',
        'Simulasi berjalan 12 detik.',
        '',
        'Yang harus ada di programmu:',
        '  1. enum Arah { NAIK, TURUN, DIAM }.',
        '  2. class Lift dengan method detak() yang menjalankan SATU detik:',
        '     turunkan penumpang yang sampai, naikkan yang menunggu di lantai',
        '     ini, lalu bergerak satu lantai ke arah tujuan.',
        '  3. Penumpang di dalam lift selalu didahulukan; kalau lift kosong,',
        '     barulah ia menjemput yang menunggu paling lama.',
        '  4. Antrean penunggu memakai Deque (addLast / removeFirst).',
        "  5. Kolom Kejadian berisi 'naik', 'turun', 'turun naik', atau kosong.",
        '  6. Di akhir: jumlah penumpang sampai tujuan, total lantai yang',
        '     dilewati, dan posisi akhir lift.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  SIMULASI LIFT GEDUNG 5 LANTAI',
        '  =============================================',
        '  Detik Lantai  Arah    Dalam   Antre   Kejadian',
        '  0     2       NAIK    0       1       ',
        '  1     3       NAIK    0       2       ',
        '  2     2       TURUN   1       1       naik',
        '  3     1       TURUN   1       1       ',
        '  4     2       NAIK    1       1       turun naik',
        '  5     3       NAIK    1       1       ',
        '  6     4       NAIK    1       1       ',
        '  7     5       NAIK    2       0       naik',
        '  8     4       TURUN   1       0       turun',
        '  9     3       TURUN   1       0       ',
        '  10    2       TURUN   1       0       ',
        '  11    2       DIAM    0       0       turun',
        '  ---------------------------------------------',
        '  Penumpang sampai tujuan : 3',
        '  Lantai yang dilewati    : 11',
        '  Posisi akhir            : lantai 2',
    ],
        "hints": [
            "Simulasi ini berjalan per detik, dan antrean penunggunya bekerja first-in first-out. Baca ulang 'Antrean dan Tumpukan: Queue, Deque, dan ArrayDeque' dan 'Enum: Himpunan Nilai Tetap'.",
            "Tiap detak() punya tiga langkah berurutan: turunkan penumpang yang tujuannya lantai ini, naikkan penunggu di lantai ini, lalu tentukan tujuan (penumpang di dalam lebih dulu, kalau kosong penunggu paling lama) dan bergerak satu lantai. Untuk memeriksa penunggu tanpa merusak urutannya, ambil satu per satu sebanyak ukuran antrean, dan kembalikan yang nggak cocok ke belakang dengan addLast().",
            "Antreannya Deque<Permintaan> menunggu = new ArrayDeque<>(); dengan addLast() untuk mengantre dan removeFirst() untuk mengambil yang paling lama menunggu. Menghapus dari List sambil melooping-nya harus dari belakang, for (int i = didalam.size() - 1; i >= 0; i--), kalau nggak indeksnya bergeser.",
        ],
        'solution': """import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

enum Arah { NAIK, TURUN, DIAM }

class Permintaan {
    final int detik;
    final int dariLantai;
    final int keLantai;

    Permintaan(int detik, int dariLantai, int keLantai) {
        this.detik = detik;
        this.dariLantai = dariLantai;
        this.keLantai = keLantai;
    }

    Arah arah() { return keLantai > dariLantai ? Arah.NAIK : Arah.TURUN; }
}

class Lift {
    private int lantai = 1;
    private Arah arah = Arah.DIAM;
    private final Deque<Permintaan> menunggu = new ArrayDeque<>();
    private final List<Permintaan> didalam = new ArrayList<>();
    private int totalLantaiDilewati = 0;
    private int totalDiangkut = 0;

    int getLantai() { return lantai; }
    Arah getArah() { return arah; }
    int getDidalam() { return didalam.size(); }
    int getMenunggu() { return menunggu.size(); }
    int getTotalLantaiDilewati() { return totalLantaiDilewati; }
    int getTotalDiangkut() { return totalDiangkut; }

    void panggil(Permintaan p) { menunggu.addLast(p); }

    /** Satu detik berlalu. Mengembalikan catatan kejadian, "" kalau sepi. */
    String detak() {
        StringBuilder catatan = new StringBuilder();

        // 1. Turunkan yang sudah sampai.
        for (int i = didalam.size() - 1; i >= 0; i--) {
            if (didalam.get(i).keLantai == lantai) {
                didalam.remove(i);
                totalDiangkut++;
                catatan.append("turun ");
            }
        }
        // 2. Naikkan yang menunggu di lantai ini.
        int jumlah = menunggu.size();
        for (int i = 0; i < jumlah; i++) {
            Permintaan p = menunggu.removeFirst();
            if (p.dariLantai == lantai) {
                didalam.add(p);
                catatan.append("naik ");
            } else {
                menunggu.addLast(p);
            }
        }
        // 3. Tentukan arah: penumpang di dalam lebih dulu, baru yang menunggu.
        int tujuan = -1;
        if (!didalam.isEmpty()) tujuan = didalam.get(0).keLantai;
        else if (!menunggu.isEmpty()) tujuan = menunggu.peekFirst().dariLantai;

        if (tujuan == -1 || tujuan == lantai) {
            arah = Arah.DIAM;
        } else if (tujuan > lantai) {
            arah = Arah.NAIK;
            lantai++;
            totalLantaiDilewati++;
        } else {
            arah = Arah.TURUN;
            lantai--;
            totalLantaiDilewati++;
        }
        return catatan.toString().trim();
    }
}

public class SimulasiLift {
    public static void main(String[] args) {
        Lift lift = new Lift();
        Permintaan[] jadwal = {
            new Permintaan(0, 3, 1),
            new Permintaan(1, 1, 5),
            new Permintaan(4, 4, 2),
        };

        System.out.println("SIMULASI LIFT GEDUNG 5 LANTAI");
        System.out.println("=============================================");
        System.out.printf("%-6s%-8s%-8s%-8s%-8s%s%n",
                "Detik", "Lantai", "Arah", "Dalam", "Antre", "Kejadian");

        for (int detik = 0; detik < 12; detik++) {
            for (Permintaan p : jadwal) {
                if (p.detik == detik) lift.panggil(p);
            }
            String kejadian = lift.detak();
            System.out.printf("%-6d%-8d%-8s%-8d%-8d%s%n",
                    detik, lift.getLantai(), lift.getArah(),
                    lift.getDidalam(), lift.getMenunggu(), kejadian);
        }

        System.out.println("---------------------------------------------");
        System.out.println("Penumpang sampai tujuan : " + lift.getTotalDiangkut());
        System.out.println("Lantai yang dilewati    : " + lift.getTotalLantaiDilewati());
        System.out.println("Posisi akhir            : lantai " + lift.getLantai());
    }
}
""",
    },
]
