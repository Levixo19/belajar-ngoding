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
        ],
        "hints": [
            "Gunakan System.out.println() untuk setiap baris.",
            "Teks harus diapit tanda kutip ganda.",
            "Jangan lupa titik koma (;) di akhir statement.",
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
        ],
        "hints": [
            "int a = 15; int b = 4;",
            "Pembagian int / int = int, sisa dibuang.",
            "Operator: +, -, *, /, %",
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
        ],
        "hints": [
            "import java.util.Scanner; lalu Scanner sc = new Scanner(System.in);",
            "int nilai = sc.nextInt();",
            "Gunakan if-else atau ternary.",
            "Ingat: setelah nextInt, jika pakai nextLine tambah sc.nextLine().",
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
            "Contoh output: 2 4 6 8 10 12 14 16 18 20, Total: 110",
        ],
        "hints": [
            "Gunakan for dan cek n % 2 == 0.",
            "Kumpulkan dalam StringBuilder atau cetak dengan System.out.print.",
            "Accumulate total dengan variabel int.",
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
        ],
        "hints": [
            "Gunakan nested loop (for di dalam for).",
            "Loop luar untuk baris, loop dalam untuk jumlah bintang per baris.",
            "System.out.print(\"*\") tanpa ln, lalu System.out.println() ganti baris.",
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
        ],
        "hints": [
            "Asumsikan elemen pertama sebagai nilai terbesar/terkecil.",
            "Loop semua elemen, bandingkan satu per satu.",
            "Ganti nilai maks/min jika ditemukan yang lebih besar/kecil.",
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
        ],
        "hints": [
            "Math.PI sudah disediakan Java.",
            "Method persegi/panjang kembalian int, lingkaran double.",
            "Panggil dengan nama method lalu argumen: luasPersegi(5).",
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
        ],
        "hints": [
            "Gunakan this.nomor = nomor; untuk membedakan attribute.",
            "tarik harus mengembalikan boolean atau memeriksa saldo.",
            "Semua attribute private, akses lewat method.",
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
        ],
        "hints": [
            "class Kucing extends Hewan.",
            "@Override void bersuara() dengan suara masing-masing.",
            "Hewan[] daftar = {new Kucing(...), new Anjing(...)}; lalu loop.",
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
        ],
        "hints": [
            "Interface method otomatis public abstract.",
            "class Tambah implements Hitung { public double hitung(...) {...} }",
            "try { double x = 10 / 0; } catch (ArithmeticException e) {...}",
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
        ],
        "hints": [
            "Gunakan .filter(s -> s.length() > 4).",
            "Gunakan .map(String::toUpperCase).",
            "Gunakan .sorted() lalu Collectors.joining(\", \").",
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
        ],
        "hints": [
            "class Pasangan<K, V> { private K key; private V value; ... }",
            "Method tukar mengembalikan tipe Pasangan<V, K> (kebalikan generic).",
            "new Pasangan<>(value, key) di dalam method tukar().",
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
        ],
        "hints": [
            "Gunakan variabel counter (int) sebagai attribute class, increment di dalam method synchronized.",
            "Method synchronized void layani() { counter++; ...; Thread.sleep(100); }",
            "Buat 5 Thread yang semuanya memanggil objek LoketAntrian yang SAMA, lalu start() semua & join() semua.",
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
            "Buat dulu class Mahasiswa (nim, nama, jurusan, ipk) dengan getter.",
            "Setiap method buka Connection sendiri lewat try-with-resources.",
            "cariByNim: jika rs.next() true, return Optional.of(...); jika tidak, Optional.empty().",
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
            "@BeforeEach void setUp() { rekening = new Rekening(...); }",
            "assertEquals(expected, actual) untuk cek nilai saldo.",
            "assertFalse(rekening.tarik(jumlahBesar)) untuk kasus gagal.",
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
]
