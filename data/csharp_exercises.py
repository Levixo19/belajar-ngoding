CSHARP_EXERCISES = [
    {
        "title": "Latihan 1: Perkenalan Diri",
        "difficulty": "Mudah",
        "question": [
            "Buat program C# yang menampilkan tepat tiga baris:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar C#.",
            "  Bahasa ini berjalan di atas .NET.",
        ],
        "hints": [
            "Program C# terdiri dari sebuah class dengan satu titik masuk, tempat eksekusi dimulai. Baca ulang materi Pengenalan C# & .NET kalau lupa kerangkanya.",
            "Kerangkanya: using System; di paling atas, lalu class Program yang berisi method static void Main(). Di dalam Main, cetak satu kalimat per baris.",
            "Console.WriteLine(\"...\") mencetak teksnya lalu pindah baris, jadi cukup tiga panggilan, satu per kalimat.",
        ],
        "solution": """using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Halo, namaku Andi!");
        Console.WriteLine("Aku sedang belajar C#.");
        Console.WriteLine("Bahasa ini berjalan di atas .NET.");
    }
}""",
    },
    {
        "title": "Latihan 2: Kalkulator Dua Bilangan",
        "difficulty": "Mudah",
        "question": [
            "Buat dua variabel a = 17 dan b = 5.",
            "Tampilkan hasil operasi dengan format persis:",
            "  17 + 5 = 22",
            "  17 - 5 = 12",
            "  17 * 5 = 85",
            "  17 / 5 = 3",
            "  17 % 5 = 2",
            "  17 / 5 = 3.40 (desimal)",
        ],
        "hints": [
            "Pembagian dua int membuang sisanya, sedangkan pembagian yang melibatkan double menyimpan pecahannya. Baca ulang materi Operator & Ekspresi.",
            "Cetak tiap baris dengan string interpolasi. Untuk baris desimal, ubah salah satu operand jadi double sebelum membagi, lalu format dengan penentu F2 supaya tampil dua angka di belakang titik.",
            "Supaya pemisah desimalnya titik di komputer mana pun, setel di awal Main: CultureInfo.CurrentCulture = CultureInfo.InvariantCulture; (butuh using System.Globalization;). Bagian desimalnya bisa ditulis {(double)a / b:F2}.",
        ],
        "solution": """using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;

        int a = 17, b = 5;

        Console.WriteLine($"{a} + {b} = {a + b}");
        Console.WriteLine($"{a} - {b} = {a - b}");
        Console.WriteLine($"{a} * {b} = {a * b}");
        Console.WriteLine($"{a} / {b} = {a / b}");
        Console.WriteLine($"{a} % {b} = {a % b}");
        Console.WriteLine($"{a} / {b} = {(double)a / b:F2} (desimal)");
    }
}""",
    },
    {
        "title": "Latihan 3: Konversi Suhu",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka suhu dalam Celsius dari input.",
            "Tampilkan konversinya ke Fahrenheit dan Kelvin.",
            "",
            "Rumus:",
            "  F = C * 9 / 5 + 32",
            "  K = C + 273.15",
            "",
            "Untuk input 25, output yang benar:",
            "  Celsius    : 25.00",
            "  Fahrenheit : 77.00",
            "  Kelvin     : 298.15",
            "",
            "Kolom angka rata kiri tepat setelah tanda titik dua dan spasi.",
        ],
        "hints": [
            "Latihan ini soal membaca input, mengubah teks jadi angka, dan memformat keluaran. Baca ulang materi Variabel, Tipe Data & Konversi serta Input, Output & String.",
            "Baca satu baris dengan Console.ReadLine(), ubah ke double, hitung F dan K pakai rumus di soal, lalu cetak ketiganya dengan dua desimal. Jangan mencetak apa pun sebelum membaca input.",
            "double.Parse(teks, CultureInfo.InvariantCulture) membaca angka berpemisah titik di komputer mana pun. Label bisa diratakan dengan {\"Celsius\",-11} atau dengan menulis spasinya langsung.",
        ],
        "stdin": "25\n",
        "solution": """using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;

        double c = double.Parse(Console.ReadLine()!, CultureInfo.InvariantCulture);
        double f = c * 9 / 5 + 32;
        double k = c + 273.15;

        Console.WriteLine($"Celsius    : {c:F2}");
        Console.WriteLine($"Fahrenheit : {f:F2}");
        Console.WriteLine($"Kelvin     : {k:F2}");
    }
}""",
    },
    {
        "title": "Latihan 4: Grade & Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka nilai (0-100) dari input.",
            "Tampilkan grade sesuai aturan:",
            "  >= 85 : A",
            "  >= 75 : B",
            "  >= 60 : C",
            "  >= 40 : D",
            "  selain itu : E",
            "",
            "Lalu tampilkan status Lulus kalau nilai >= 75,",
            "atau Tidak Lulus kalau kurang.",
            "",
            "Untuk input 78, output yang benar:",
            "  Grade: B",
            "  Status: Lulus",
        ],
        "hints": [
            "Kamu perlu memetakan rentang nilai ke huruf, dan pola relasional di switch expression pas untuk itu. Baca ulang materi Percabangan: if, switch & Pattern Matching.",
            "Urutkan lengan dari batas tertinggi ke terendah, karena lengan pertama yang cocok yang dipakai. Lengan _ di akhir menangkap sisanya, setara default. Untuk status, operator ternary sudah cukup.",
            "Bentuknya: string grade = nilai switch { >= 85 => \"A\", >= 75 => \"B\", ..., _ => \"E\" }; lalu nilai >= 75 ? \"Lulus\" : \"Tidak Lulus\".",
        ],
        "stdin_list": ["92\n", "78\n", "65\n", "45\n", "12\n"],
        "solution": """using System;

class Program
{
    static void Main()
    {
        int nilai = int.Parse(Console.ReadLine()!);

        string grade = nilai switch
        {
            >= 85 => "A",
            >= 75 => "B",
            >= 60 => "C",
            >= 40 => "D",
            _     => "E",
        };

        Console.WriteLine($"Grade: {grade}");
        Console.WriteLine($"Status: {(nilai >= 75 ? "Lulus" : "Tidak Lulus")}");
    }
}""",
    },
    {
        "title": "Latihan 5: Tabel Perkalian",
        "difficulty": "Mudah",
        "question": [
            "Tampilkan tabel perkalian 1 sampai 5 dengan format persis:",
            "",
            "  1 x 1 =  1   1 x 2 =  2   1 x 3 =  3   1 x 4 =  4   1 x 5 =  5",
            "  2 x 1 =  2   2 x 2 =  4   2 x 3 =  6   2 x 4 =  8   2 x 5 = 10",
            "  3 x 1 =  3   3 x 2 =  6   3 x 3 =  9   3 x 4 = 12   3 x 5 = 15",
            "  4 x 1 =  4   4 x 2 =  8   4 x 3 = 12   4 x 4 = 16   4 x 5 = 20",
            "  5 x 1 =  5   5 x 2 = 10   5 x 3 = 15   5 x 4 = 20   5 x 5 = 25",
            "",
            "Tiap baris diawali dua spasi. Hasil perkaliannya rata kanan",
            "selebar 2 karakter, dan tiap sel dipisah tiga spasi.",
        ],
        "hints": [
            "Tabel berarti dua perulangan bersarang: perulangan luar untuk baris, perulangan dalam untuk kolom. Baca ulang materi Perulangan: for, while, foreach.",
            "Di awal tiap baris cetak dua spasi. Di perulangan dalam, cetak satu sel dengan Console.Write (tanpa pindah baris), lalu pemisah tiga spasi kecuali untuk sel terakhir. Sesudah perulangan dalam selesai, panggil Console.WriteLine() untuk pindah baris.",
            "Rata kanan selebar 2 ditulis {b * k,2} di dalam interpolasi, jadi satu sel berbentuk $\"{b} x {k} = {b * k,2}\".",
        ],
        "solution": """using System;

class Program
{
    static void Main()
    {
        for (int b = 1; b <= 5; b++)
        {
            Console.Write("  ");
            for (int k = 1; k <= 5; k++)
            {
                Console.Write($"{b} x {k} = {b * k,2}");
                if (k < 5) Console.Write("   ");
            }
            Console.WriteLine();
        }
    }
}""",
    },
    {
        "title": "Latihan 6: Statistik Nilai",
        "difficulty": "Menengah",
        "question": [
            "Diberikan array nilai berikut di dalam kodemu:",
            "  78, 92, 65, 88, 71, 95, 59, 83",
            "",
            "Tampilkan statistiknya dengan format persis:",
            "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
            "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
            "  Jumlah    : 8",
            "  Total     : 631",
            "  Rata-rata : 78.88",
            "  Tertinggi : 95",
            "  Terendah  : 59",
            "  Di atas rata-rata: 4",
        ],
        "hints": [
            "Kamu perlu menelusuri array untuk total, nilai tertinggi, dan terendah, lalu menelusurinya lagi untuk menghitung yang di atas rata-rata. Baca ulang materi Array & Indeks.",
            "Hitung total, tertinggi, dan terendah dalam satu foreach. Rata-rata dibagi sebagai double supaya bukan pembagian bulat. Untuk baris Terurut, urutkan salinan array: Array.Sort mengubah array aslinya, padahal baris Data masih butuh urutan asli.",
            "Salinan array: (int[])nilai.Clone(). Menggabungkan isi array jadi satu teks: string.Join(\", \", array). Setel CultureInfo.InvariantCulture supaya 78.88 memakai titik.",
        ],
        "solution": """using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;

        int[] nilai = { 78, 92, 65, 88, 71, 95, 59, 83 };

        int total = 0, tertinggi = nilai[0], terendah = nilai[0];
        foreach (int n in nilai)
        {
            total += n;
            if (n > tertinggi) tertinggi = n;
            if (n < terendah) terendah = n;
        }
        double rata = (double)total / nilai.Length;

        int diAtas = 0;
        foreach (int n in nilai)
            if (n > rata) diAtas++;

        int[] urut = (int[])nilai.Clone();
        Array.Sort(urut);

        Console.WriteLine($"Data      : {string.Join(", ", nilai)}");
        Console.WriteLine($"Terurut   : {string.Join(", ", urut)}");
        Console.WriteLine($"Jumlah    : {nilai.Length}");
        Console.WriteLine($"Total     : {total}");
        Console.WriteLine($"Rata-rata : {rata:F2}");
        Console.WriteLine($"Tertinggi : {tertinggi}");
        Console.WriteLine($"Terendah  : {terendah}");
        Console.WriteLine($"Di atas rata-rata: {diAtas}");
    }
}""",
    },
    {
        "title": "Latihan 7: Balik Teks & Palindrom",
        "difficulty": "Menengah",
        "question": [
            "Baca satu baris teks dari input.",
            "Tampilkan:",
            "  1. Teks aslinya",
            "  2. Teks yang dibalik",
            "  3. Jumlah huruf (spasi tidak dihitung)",
            "  4. Apakah palindrom (abaikan spasi dan besar-kecil huruf)",
            "",
            "Untuk input 'Kasur ini rusak', output yang benar:",
            "  Asli    : Kasur ini rusak",
            "  Dibalik : kasur ini rusaK",
            "  Huruf   : 13",
            "  Palindrom: ya",
            "",
            "Kalau bukan palindrom, baris terakhir berbunyi 'Palindrom: bukan'.",
        ],
        "hints": [
            "Latihan ini soal mengolah string: membalik, membuang spasi, dan menyamakan besar-kecil huruf. Baca ulang materi Input, Output & String.",
            "Buat method kecil untuk membalik string. Buang spasi dulu untuk menghitung huruf, lalu bandingkan versi tanpa spasi berhuruf kecil dengan kebalikannya. Jangan mencetak apa pun sebelum Console.ReadLine() pertama.",
            "Membalik: ubah jadi char[] dengan ToCharArray(), panggil Array.Reverse, lalu bentuk lagi dengan new string(...). Spasi dibuang dengan Replace(\" \", \"\").",
        ],
        "stdin_list": ["Kasur ini rusak\n", "Belajar C sharp\n", "Ini\n"],
        "solution": """using System;

class Program
{
    static string Balik(string s)
    {
        char[] c = s.ToCharArray();
        Array.Reverse(c);
        return new string(c);
    }

    static void Main()
    {
        string teks = Console.ReadLine() ?? "";

        string rapat = teks.Replace(" ", "");
        string bersih = rapat.ToLowerInvariant();
        bool palindrom = bersih == Balik(bersih);

        Console.WriteLine($"Asli    : {teks}");
        Console.WriteLine($"Dibalik : {Balik(teks)}");
        Console.WriteLine($"Huruf   : {rapat.Length}");
        Console.WriteLine($"Palindrom: {(palindrom ? "ya" : "bukan")}");
    }
}""",
    },
    {
        "title": "Latihan 8: Menghitung Frekuensi Kata",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat berikut di dalam kodemu:",
            "  \"kucing makan ikan kucing tidur ikan kucing\"",
            "",
            "Hitung berapa kali tiap kata muncul, lalu tampilkan",
            "terurut dari yang paling sering. Kalau jumlahnya sama,",
            "urutkan berdasarkan abjad.",
            "",
            "Output yang benar:",
            "  kucing : 3",
            "  ikan   : 2",
            "  makan  : 1",
            "  tidur  : 1",
            "  ---",
            "  Kata unik  : 4",
            "  Total kata : 7",
            "",
            "Nama kata rata kiri selebar 7 karakter.",
        ],
        "hints": [
            "Menghitung kemunculan paling pas memakai Dictionary, dengan kata sebagai kunci dan jumlahnya sebagai nilai. Baca ulang materi List, Dictionary & Koleksi Generik dan LINQ: Bertanya pada Data.",
            "Pecah kalimat per spasi, lalu untuk tiap kata naikkan hitungannya satu. Urutkan pasangan kunci-nilai menurut jumlah menurun, lalu menurut kata menaik kalau jumlahnya sama. Total kata adalah panjang hasil pecahan; kata unik adalah jumlah isi Dictionary.",
            "TryGetValue(k, out int n) mengisi n dengan 0 kalau kunci belum ada, jadi cukup hitung[k] = n + 1. Urutan dua tingkat: OrderByDescending(p => p.Value).ThenBy(p => p.Key). Nama rata kiri: {p.Key,-7}.",
        ],
        "solution": """using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        string kalimat = "kucing makan ikan kucing tidur ikan kucing";
        string[] kata = kalimat.Split(' ');

        var hitung = new Dictionary<string, int>();
        foreach (string k in kata)
        {
            hitung.TryGetValue(k, out int n);
            hitung[k] = n + 1;
        }

        foreach (var p in hitung.OrderByDescending(p => p.Value)
                                .ThenBy(p => p.Key, StringComparer.Ordinal))
            Console.WriteLine($"{p.Key,-7}: {p.Value}");

        Console.WriteLine("---");
        Console.WriteLine($"Kata unik  : {hitung.Count}");
        Console.WriteLine($"Total kata : {kata.Length}");
    }
}""",
    },
    {
        "title": "Latihan 9: Class Murid dengan Validasi",
        "difficulty": "Menengah",
        "question": [
            "Buat class Murid dengan:",
            "  - property Nama (hanya bisa dibaca dari luar)",
            "  - property Nilai yang MENOLAK nilai di luar 0..100 dengan",
            "    melempar ArgumentOutOfRangeException",
            "  - property terhitung Grade: >=85 A, >=75 B, >=60 C, sisanya D",
            "  - override ToString berbentuk: \"Andi    92 A\"",
            "    (nama rata kiri 8, nilai rata kanan 3, spasi, grade)",
            "",
            "Di Main, buat tiga murid: Andi 92, Budi 78, Cici 64.",
            "Cetak ketiganya, lalu coba mengisi nilai Andi dengan 150",
            "dan tangkap exception-nya.",
            "",
            "Output yang benar:",
            "  Andi     92 A",
            "  Budi     78 B",
            "  Cici     64 C",
            "  Ditolak: nilai di luar 0..100",
        ],
        "hints": [
            "Class ini butuh tiga jenis property: yang cuma bisa dibaca dari luar, yang memvalidasi saat diisi, dan yang dihitung dari property lain. Baca ulang materi Property, Constructor & Inisialisasi.",
            "Simpan nilai di field privat dan tulis setter bentuk panjang yang melempar ArgumentOutOfRangeException kalau nilainya di luar 0..100. Di constructor, isi lewat property Nilai supaya validasinya ikut jalan. Grade cocok ditulis sebagai property terhitung dengan switch expression.",
            "Property hanya-baca: public string Nama { get; }. Setter yang memvalidasi: get => _nilai; set { if (...) throw ...; _nilai = value; }. Bungkus percobaan nilai 150 dengan try / catch (ArgumentOutOfRangeException).",
        ],
        "solution": """using System;

class Murid
{
    private int _nilai;

    public string Nama { get; }

    public int Nilai
    {
        get => _nilai;
        set
        {
            if (value < 0 || value > 100)
                throw new ArgumentOutOfRangeException(nameof(value),
                    "nilai di luar 0..100");
            _nilai = value;
        }
    }

    public string Grade => _nilai switch
    {
        >= 85 => "A",
        >= 75 => "B",
        >= 60 => "C",
        _     => "D",
    };

    public Murid(string nama, int nilai)
    {
        Nama = nama;
        Nilai = nilai;
    }

    public override string ToString() => $"{Nama,-8}{Nilai,3} {Grade}";
}

class Program
{
    static void Main()
    {
        var kelas = new[]
        {
            new Murid("Andi", 92),
            new Murid("Budi", 78),
            new Murid("Cici", 64),
        };

        foreach (Murid m in kelas) Console.WriteLine(m);

        try
        {
            kelas[0].Nilai = 150;
        }
        catch (ArgumentOutOfRangeException)
        {
            Console.WriteLine("Ditolak: nilai di luar 0..100");
        }
    }
}""",
    },
    {
        "title": "Latihan 10: Bangun Datar Polimorfik",
        "difficulty": "Lanjut",
        "question": [
            "Buat abstract class Bangun dengan property Nama,",
            "serta method abstract Luas() dan Keliling().",
            "",
            "Turunkan tiga class: Persegi(sisi), PersegiPanjang(p, l),",
            "dan Segitiga(alas, tinggi, sisiA, sisiB, sisiC).",
            "",
            "Di Main, masukkan Persegi(4), PersegiPanjang(6, 3), dan",
            "Segitiga(6, 4, 5, 5, 6) ke dalam satu array bertipe Bangun,",
            "lalu telusuri sekali untuk mencetak semuanya.",
            "",
            "Output yang benar:",
            "  Persegi         16.00    16.00",
            "  PersegiPanjang  18.00    18.00",
            "  Segitiga        12.00    16.00",
            "  ------------------------------",
            "  TOTAL           46.00    50.00",
            "",
            "Nama rata kiri 16, luas dan keliling rata kanan 5 dengan",
            "dua desimal, dipisah empat spasi.",
        ],
        "hints": [
            "Satu array bertipe induk yang berisi berbagai turunan, lalu satu perulangan yang memanggil method yang sama: itulah polimorfisme. Baca ulang materi Pewarisan & Polimorfisme.",
            "Abstract class Bangun menyimpan Nama dan mendeklarasikan Luas() serta Keliling() sebagai abstract. Tiap turunan menyimpan ukurannya sendiri dan meng-override keduanya. Di Main, satu foreach mencetak tiap bangun sambil menjumlahkan total. Luas segitiga = alas * tinggi / 2, kelilingnya jumlah ketiga sisi.",
            "Constructor turunan memanggil induknya dengan : base(\"Persegi\"). Satu baris tabel: {b.Nama,-16}{b.Luas(),5:F2}, dan setel CultureInfo.InvariantCulture supaya desimalnya memakai titik.",
        ],
        "solution": """using System;
using System.Globalization;

abstract class Bangun
{
    public string Nama { get; }
    protected Bangun(string nama) => Nama = nama;

    public abstract double Luas();
    public abstract double Keliling();
}

class Persegi : Bangun
{
    private readonly double _s;
    public Persegi(double s) : base("Persegi") => _s = s;
    public override double Luas() => _s * _s;
    public override double Keliling() => 4 * _s;
}

class PersegiPanjang : Bangun
{
    private readonly double _p, _l;
    public PersegiPanjang(double p, double l) : base("PersegiPanjang")
        => (_p, _l) = (p, l);
    public override double Luas() => _p * _l;
    public override double Keliling() => 2 * (_p + _l);
}

class Segitiga : Bangun
{
    private readonly double _alas, _tinggi, _a, _b, _c;
    public Segitiga(double alas, double tinggi, double a, double b, double c)
        : base("Segitiga")
        => (_alas, _tinggi, _a, _b, _c) = (alas, tinggi, a, b, c);
    public override double Luas() => _alas * _tinggi / 2;
    public override double Keliling() => _a + _b + _c;
}

class Program
{
    static void Main()
    {
        CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;

        Bangun[] semua =
        {
            new Persegi(4),
            new PersegiPanjang(6, 3),
            new Segitiga(6, 4, 5, 5, 6),
        };

        double totalLuas = 0, totalKeliling = 0;
        foreach (Bangun b in semua)
        {
            Console.WriteLine($"{b.Nama,-16}{b.Luas(),5:F2}    {b.Keliling(),5:F2}");
            totalLuas += b.Luas();
            totalKeliling += b.Keliling();
        }

        Console.WriteLine(new string('-', 30));
        Console.WriteLine($"{"TOTAL",-16}{totalLuas,5:F2}    {totalKeliling,5:F2}");
    }
}""",
    },
    {
        "title": "Latihan 11: Laporan Penjualan dengan LINQ",
        "difficulty": "Lanjut",
        "question": [
            "Buat record Transaksi(string Barang, string Kategori, int Jumlah,",
            "int Harga) dan isi daftar berikut:",
            "  Kopi      Minuman   3   25000",
            "  Teh       Minuman   5   15000",
            "  Roti      Makanan   2   20000",
            "  Nasi      Makanan   4   30000",
            "  Jus       Minuman   1   35000",
            "",
            "Dengan LINQ, tampilkan:",
            "  1. Semua transaksi bersubtotal, terurut subtotal menurun",
            "  2. Total keseluruhan",
            "  3. Rekap per kategori terurut abjad",
            "  4. Barang dengan subtotal tertinggi",
            "",
            "Output yang benar:",
            "  Nasi       Makanan     4 x  30000 =   120000",
            "  Teh        Minuman     5 x  15000 =    75000",
            "  Kopi       Minuman     3 x  25000 =    75000",
            "  Roti       Makanan     2 x  20000 =    40000",
            "  Jus        Minuman     1 x  35000 =    35000",
            "  ---",
            "  Total: 345000",
            "  Makanan: 160000 (2 transaksi)",
            "  Minuman: 185000 (3 transaksi)",
            "  Tertinggi: Nasi",
            "",
            "Kolom: barang rata kiri 11, kategori rata kiri 11, jumlah rata",
            "kanan 2, harga rata kanan 6, subtotal rata kanan 8. Urutan",
            "subtotal menurun; kalau sama, urutkan abjad barangnya menurun",
            "(itu sebabnya Teh mendahului Kopi).",
        ],
        "hints": [
            "Ini latihan menyusun query LINQ: menghitung kolom baru, mengurutkan dua tingkat, mengelompokkan, dan mencari yang terbesar. Baca ulang materi LINQ: Bertanya pada Data dan Struct, Record & Tipe Nilai.",
            "Hitung subtotal sekali lewat Select ke objek baru, lalu urutkan menurun menurut subtotal dan, kalau sama, menurun menurut nama barang. Untuk rekap, kelompokkan per kategori lalu urutkan kuncinya. Barang tertinggi bisa dicari dengan mengurutkan menurun lalu mengambil yang pertama.",
            "Urutan dua tingkat: OrderByDescending(x => x.Sub).ThenByDescending(x => x.Barang). Rekap: GroupBy(t => t.Kategori).OrderBy(g => g.Key), lalu g.Sum(...) dan g.Count(). MaxBy ada sejak .NET 6; kalau ragu, pakai OrderByDescending(...).First().",
        ],
        "solution": """using System;
using System.Collections.Generic;
using System.Linq;

record Transaksi(string Barang, string Kategori, int Jumlah, int Harga);

class Program
{
    static void Main()
    {
        var data = new List<Transaksi>
        {
            new("Kopi", "Minuman", 3, 25000),
            new("Teh",  "Minuman", 5, 15000),
            new("Roti", "Makanan", 2, 20000),
            new("Nasi", "Makanan", 4, 30000),
            new("Jus",  "Minuman", 1, 35000),
        };

        var baris = data.Select(t => new
                        {
                            t.Barang, t.Kategori, t.Jumlah, t.Harga,
                            Sub = t.Jumlah * t.Harga,
                        })
                        .OrderByDescending(x => x.Sub)
                        .ThenByDescending(x => x.Barang, StringComparer.Ordinal);

        foreach (var b in baris)
            Console.WriteLine($"{b.Barang,-11}{b.Kategori,-11}{b.Jumlah,2} x "
                            + $"{b.Harga,6} = {b.Sub,8}");

        Console.WriteLine("---");
        Console.WriteLine($"Total: {data.Sum(t => t.Jumlah * t.Harga)}");

        foreach (var g in data.GroupBy(t => t.Kategori)
                              .OrderBy(g => g.Key, StringComparer.Ordinal))
            Console.WriteLine($"{g.Key}: {g.Sum(t => t.Jumlah * t.Harga)} "
                            + $"({g.Count()} transaksi)");

        var teratas = data.OrderByDescending(t => t.Jumlah * t.Harga).First();
        Console.WriteLine($"Tertinggi: {teratas.Barang}");
    }
}""",
    },
    {
        "title": "Latihan 12: Dompet dengan Exception Sendiri",
        "difficulty": "Lanjut",
        "question": [
            "Buat exception SaldoKurangException yang menyimpan property",
            "Kurang (decimal) dan pesan \"Saldo kurang <angka>\".",
            "",
            "Buat class Dompet dengan saldo awal, method Setor(jumlah)",
            "dan Bayar(jumlah). Keduanya menolak jumlah <= 0 dengan",
            "ArgumentOutOfRangeException. Bayar melempar",
            "SaldoKurangException kalau saldo tidak cukup.",
            "",
            "Di Main mulai dengan saldo 50000, lalu jalankan berurutan:",
            "  Bayar 20000, Bayar -5, Bayar 100000, Setor 30000, Bayar 55000",
            "",
            "Output yang benar:",
            "  Bayar 20000 -> sisa 30000",
            "  Bayar -5 -> DITOLAK: jumlah tidak sah",
            "  Bayar 100000 -> GAGAL: kurang 70000",
            "  Setor 30000 -> sisa 60000",
            "  Bayar 55000 -> sisa 5000",
        ],
        "hints": [
            "Exception buatan sendiri adalah class biasa yang mewarisi Exception dan boleh membawa data tambahan. Baca ulang materi Exception & Penanganan Galat.",
            "SaldoKurangException menyimpan property Kurang dan meneruskan pesannya ke constructor induk. Dompet memeriksa jumlah <= 0 lebih dulu, baru kecukupan saldo. Di Main, telusuri daftar langkah dan bungkus tiap langkah dengan try/catch, dengan catch yang paling spesifik ditulis lebih dulu.",
            "Pesan diteruskan ke induk dengan : base($\"Saldo kurang {kurang}\"). Saldo sebaiknya { get; private set; } supaya nggak bisa diubah dari luar. Decimal seperti 50000m tercetak 50000, tanpa angka di belakang titik.",
        ],
        "solution": """using System;

class SaldoKurangException : Exception
{
    public decimal Kurang { get; }
    public SaldoKurangException(decimal kurang)
        : base($"Saldo kurang {kurang}") => Kurang = kurang;
}

class Dompet
{
    public decimal Saldo { get; private set; }

    public Dompet(decimal awal) => Saldo = awal;

    public void Setor(decimal jumlah)
    {
        if (jumlah <= 0)
            throw new ArgumentOutOfRangeException(nameof(jumlah));
        Saldo += jumlah;
    }

    public void Bayar(decimal jumlah)
    {
        if (jumlah <= 0)
            throw new ArgumentOutOfRangeException(nameof(jumlah));
        if (jumlah > Saldo)
            throw new SaldoKurangException(jumlah - Saldo);
        Saldo -= jumlah;
    }
}

class Program
{
    static void Main()
    {
        var d = new Dompet(50000m);

        (string aksi, decimal nilai)[] langkah =
        {
            ("Bayar", 20000m), ("Bayar", -5m), ("Bayar", 100000m),
            ("Setor", 30000m), ("Bayar", 55000m),
        };

        foreach (var (aksi, nilai) in langkah)
        {
            try
            {
                if (aksi == "Setor") d.Setor(nilai); else d.Bayar(nilai);
                Console.WriteLine($"{aksi} {nilai} -> sisa {d.Saldo}");
            }
            catch (SaldoKurangException e)
            {
                Console.WriteLine($"{aksi} {nilai} -> GAGAL: kurang {e.Kurang}");
            }
            catch (ArgumentOutOfRangeException)
            {
                Console.WriteLine($"{aksi} {nilai} -> DITOLAK: jumlah tidak sah");
            }
        }
    }
}""",
    },
    {
        "title": "Latihan 13: Antrean Generik Berbatas",
        "difficulty": "Lanjut",
        "question": [
            "Buat class generic AntreanTerbatas<T> dengan kapasitas tetap:",
            "  - Masuk(T) mengembalikan bool: false kalau sudah penuh",
            "  - Keluar() mengembalikan T?; default kalau kosong",
            "  - property Jumlah dan Penuh",
            "  - override ToString: \"[a, b, c] 3/3\"",
            "",
            "Di Main, buat AntreanTerbatas<string> kapasitas 3, lalu:",
            "masukkan Andi, Budi, Cici, Dedi; keluarkan dua kali;",
            "masukkan Euis; cetak keadaannya di tiap langkah penting.",
            "",
            "Output yang benar:",
            "  masuk Andi: True",
            "  masuk Budi: True",
            "  masuk Cici: True",
            "  masuk Dedi: False",
            "  [Andi, Budi, Cici] 3/3",
            "  keluar: Andi",
            "  keluar: Budi",
            "  masuk Euis: True",
            "  [Cici, Euis] 2/3",
        ],
        "hints": [
            "Antrean itu FIFO: yang pertama masuk, pertama keluar. Class generic memakai T sebagai pengganti tipe isinya. Baca ulang materi Generic: Tipe sebagai Parameter.",
            "Simpan isinya di List<T> dan kapasitasnya di field. Masuk mengembalikan false kalau sudah penuh. Keluar mengambil elemen di index 0 lalu menghapusnya, atau mengembalikan default kalau kosong. Jumlah dan Penuh cukup property terhitung dari isi List.",
            "Untuk kasus kosong: return default; (kembaliannya T?). Ambil lalu buang yang terdepan: T barang = _isi[0]; _isi.RemoveAt(0);. ToString menggabungkan isinya dengan string.Join(\", \", _isi).",
        ],
        "solution": """using System;
using System.Collections.Generic;

class AntreanTerbatas<T>
{
    private readonly List<T> _isi = new();
    private readonly int _muat;

    public AntreanTerbatas(int muat) => _muat = muat;

    public int Jumlah => _isi.Count;
    public bool Penuh => _isi.Count >= _muat;

    public bool Masuk(T barang)
    {
        if (Penuh) return false;
        _isi.Add(barang);
        return true;
    }

    public T? Keluar()
    {
        if (_isi.Count == 0) return default;
        T barang = _isi[0];
        _isi.RemoveAt(0);
        return barang;
    }

    public override string ToString()
        => $"[{string.Join(", ", _isi)}] {Jumlah}/{_muat}";
}

class Program
{
    static void Main()
    {
        var antre = new AntreanTerbatas<string>(3);

        foreach (string nama in new[] { "Andi", "Budi", "Cici", "Dedi" })
            Console.WriteLine($"masuk {nama}: {antre.Masuk(nama)}");

        Console.WriteLine(antre);
        Console.WriteLine($"keluar: {antre.Keluar()}");
        Console.WriteLine($"keluar: {antre.Keluar()}");
        Console.WriteLine($"masuk Euis: {antre.Masuk("Euis")}");
        Console.WriteLine(antre);
    }
}""",
    },
    {
        "title": "Latihan 14: Penjelas Nilai dengan Pattern Matching",
        "difficulty": "Sulit",
        "question": [
            "Buat method static string Jelaskan(object? o) yang memakai SATU",
            "switch expression untuk menjelaskan isinya:",
            "  null                      -> \"kosong\"",
            "  int negatif               -> \"bilangan negatif <n>\"",
            "  int 0                     -> \"nol\"",
            "  int genap                 -> \"bilangan genap <n>\"",
            "  int lain                  -> \"bilangan ganjil <n>\"",
            "  string kosong             -> \"teks kosong\"",
            "  string                    -> \"teks <panjang> huruf\"",
            "  bool                      -> \"benar\" atau \"salah\"",
            "  int[] panjang > 3         -> \"array panjang\"",
            "  int[] lain                -> \"array <n> elemen\"",
            "  selain itu                -> \"tipe lain: <NamaTipe>\"",
            "",
            "Uji dengan: null, -7, 0, 4, 9, \"\", \"halo\", true, false,",
            "array {1,2}, array {1,2,3,4}, dan 3.14",
            "",
            "Output yang benar:",
            "  kosong",
            "  bilangan negatif -7",
            "  nol",
            "  bilangan genap 4",
            "  bilangan ganjil 9",
            "  teks kosong",
            "  teks 4 huruf",
            "  benar",
            "  salah",
            "  array 2 elemen",
            "  array panjang",
            "  tipe lain: Double",
        ],
        "hints": [
            "Satu switch expression bisa mencocokkan tipe, nilai, properti, dan syarat tambahan sekaligus. Baca ulang materi Percabangan: if, switch & Pattern Matching.",
            "Urutan lengan menentukan hasil: pola yang lebih sempit harus ditulis lebih dulu. Untuk int, tulis negatif dulu, lalu 0, lalu genap, baru sisanya. Untuk string, yang kosong dulu. Lengan _ di akhir menangkap tipe lain.",
            "Pola properti: string { Length: 0 } dan int[] { Length: > 3 }. Syarat tambahan dengan when: int n when n % 2 == 0. Nama tipe saat program jalan: o.GetType().Name.",
        ],
        "solution": """using System;

class Program
{
    static string Jelaskan(object? o) => o switch
    {
        null                     => "kosong",
        int n when n < 0         => $"bilangan negatif {n}",
        0                        => "nol",
        int n when n % 2 == 0    => $"bilangan genap {n}",
        int n                    => $"bilangan ganjil {n}",
        string { Length: 0 }     => "teks kosong",
        string s                 => $"teks {s.Length} huruf",
        bool b                   => b ? "benar" : "salah",
        int[] { Length: > 3 }    => "array panjang",
        int[] a                  => $"array {a.Length} elemen",
        _                        => $"tipe lain: {o.GetType().Name}",
    };

    static void Main()
    {
        object?[] contoh =
        {
            null, -7, 0, 4, 9, "", "halo", true, false,
            new[] { 1, 2 }, new[] { 1, 2, 3, 4 }, 3.14,
        };

        foreach (object? o in contoh)
            Console.WriteLine(Jelaskan(o));
    }
}""",
    },
    {
        "title": "Latihan 15: Riwayat Harga dengan Record",
        "difficulty": "Sulit",
        "question": [
            "Buat record Produk(string Nama, string Kategori, decimal Harga).",
            "",
            "Mulai dari daftar:",
            "  Kopi     Minuman  25000",
            "  Teh      Minuman  15000",
            "  Roti     Makanan  20000",
            "",
            "Kerjakan berurutan dan cetak hasilnya:",
            "  1. Cetak ketiganya apa adanya (pakai ToString bawaan record).",
            "  2. Buat versi baru Kopi dengan harga 27000 memakai `with`,",
            "     lalu cetak keduanya untuk membuktikan yang lama tak berubah.",
            "  3. Buktikan kesetaraan berbasis nilai: bandingkan Kopi lama",
            "     dengan Produk baru berisi data yang sama persis.",
            "  4. Pecah salah satu record dengan deconstruction.",
            "  5. Cetak total harga per kategori, terurut abjad.",
            "",
            "Output yang benar:",
            "  Produk { Nama = Kopi, Kategori = Minuman, Harga = 25000 }",
            "  Produk { Nama = Teh, Kategori = Minuman, Harga = 15000 }",
            "  Produk { Nama = Roti, Kategori = Makanan, Harga = 20000 }",
            "  ---",
            "  lama : Produk { Nama = Kopi, Kategori = Minuman, Harga = 25000 }",
            "  baru : Produk { Nama = Kopi, Kategori = Minuman, Harga = 27000 }",
            "  sama nilainya? True",
            "  sama objeknya? False",
            "  pecah: Roti / Makanan / 20000",
            "  ---",
            "  Makanan: 20000",
            "  Minuman: 40000",
        ],
        "hints": [
            "record sudah membuatkan ToString, kesetaraan berbasis nilai, with, dan deconstruction untukmu. Baca ulang materi Struct, Record & Tipe Nilai.",
            "Cetak record apa adanya untuk melihat ToString bawaannya. Buat versi baru dengan with lalu cetak keduanya. Bandingkan dengan == untuk nilai dan ReferenceEquals untuk objek. Pecah dengan deconstruction, lalu rekap harga per kategori dengan GroupBy.",
            "lama with { Harga = 27000m } membuat salinan, yang lama nggak berubah. Deconstruction berbentuk var (nama, kategori, harga) = produk;.",
        ],
        "solution": """using System;
using System.Collections.Generic;
using System.Linq;

record Produk(string Nama, string Kategori, decimal Harga);

class Program
{
    static void Main()
    {
        var daftar = new List<Produk>
        {
            new("Kopi", "Minuman", 25000m),
            new("Teh",  "Minuman", 15000m),
            new("Roti", "Makanan", 20000m),
        };

        foreach (Produk p in daftar) Console.WriteLine(p);

        Console.WriteLine("---");
        Produk lama = daftar[0];
        Produk baru = lama with { Harga = 27000m };
        Console.WriteLine($"lama : {lama}");
        Console.WriteLine($"baru : {baru}");

        var kembar = new Produk("Kopi", "Minuman", 25000m);
        Console.WriteLine($"sama nilainya? {lama == kembar}");
        Console.WriteLine($"sama objeknya? {ReferenceEquals(lama, kembar)}");

        var (nama, kategori, harga) = daftar[2];
        Console.WriteLine($"pecah: {nama} / {kategori} / {harga}");

        Console.WriteLine("---");
        foreach (var g in daftar.GroupBy(p => p.Kategori)
                                .OrderBy(g => g.Key, StringComparer.Ordinal))
            Console.WriteLine($"{g.Key}: {g.Sum(p => p.Harga)}");
    }
}""",
    },
    {
        "title": "Latihan 16: Proyek Akhir - Sistem Inventaris Gudang",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Bangun sistem inventaris yang MEMISAHKAN tiga lapisan:",
            "model (data), layanan (aturan), dan antarmuka (cetak).",
            "",
            "MODEL",
            "  record Barang(string Kode, string Nama, int Stok, decimal Harga)",
            "  enum Gerak { Masuk, Keluar }",
            "",
            "LAYANAN  class Gudang",
            "  - Daftar(Barang) menolak kode kembar dengan",
            "    InvalidOperationException",
            "  - Catat(kode, Gerak, jumlah):",
            "      * kode tidak dikenal -> KeyNotFoundException",
            "      * jumlah <= 0 -> ArgumentOutOfRangeException",
            "      * Keluar melebihi stok -> InvalidOperationException",
            "      * selain itu stok diperbarui",
            "  - NilaiPersediaan() = jumlah dari Stok * Harga",
            "  - StokMenipis(batas) = barang berstok < batas, terurut stok naik",
            "  - Semua = daftar barang terurut kode",
            "",
            "ANTARMUKA (Main)",
            "  Daftarkan: B01 Kabel 10 15000, B02 Adaptor 4 85000,",
            "             B03 Mouse 25 120000",
            "  Lalu jalankan berurutan dan cetak hasil tiap langkah:",
            "    daftar ulang B01, Masuk B01 15, Keluar B02 10,",
            "    Keluar B03 5, Masuk B09 1, Keluar B03 0",
            "  Terakhir cetak tabel stok, nilai persediaan, dan stok menipis",
            "  di bawah 10.",
            "",
            "Output yang benar:",
            "  daftar B01 -> DITOLAK: kode sudah ada",
            "  Masuk B01 15 -> stok 25",
            "  Keluar B02 10 -> DITOLAK: stok tidak cukup",
            "  Keluar B03 5 -> stok 20",
            "  Masuk B09 1 -> DITOLAK: kode tidak dikenal",
            "  Keluar B03 0 -> DITOLAK: jumlah tidak sah",
            "  ---",
            "  B01  Kabel         25       15000      375000",
            "  B02  Adaptor        4       85000      340000",
            "  B03  Mouse         20      120000     2400000",
            "  ---",
            "  Nilai persediaan: 3115000",
            "  Stok menipis (<10): B02 Adaptor (4)",
            "",
            "Kolom tabel: kode rata kiri 5, nama rata kiri 12, stok rata",
            "kanan 4, harga rata kanan 12, subtotal rata kanan 12.",
        ],
        "hints": [
            "Kuncinya pemisahan lapisan: Gudang cuma menyimpan aturan dan nggak pernah memanggil Console, Main yang mencetak. Itu yang membuat Gudang bisa diuji tanpa membaca layar. Baca ulang materi Membangun Aplikasi Konsol Utuh dan Exception & Penanganan Galat.",
            "Simpan barang di Dictionary<string, Barang> berkunci kode. Di Catat, urutan pemeriksaan menentukan pesan yang muncul: periksa kode dulu, lalu jumlah, baru kecukupan stok. Di Main, bungkus tiap langkah dengan try/catch-nya sendiri supaya satu kegagalan nggak menghentikan langkah berikutnya.",
            "Record itu immutable, jadi stok diperbarui dengan with: _isi[kode] = b with { Stok = stokBaru };. InvalidOperationException dipakai untuk dua hal (kode kembar dan stok kurang), jadi tampilkan e.Message-nya.",
        ],
        "solution": """using System;
using System.Collections.Generic;
using System.Linq;

// ---------------------------------------------------------------- MODEL
record Barang(string Kode, string Nama, int Stok, decimal Harga);

enum Gerak { Masuk, Keluar }

// -------------------------------------------------------------- LAYANAN
class Gudang
{
    private readonly Dictionary<string, Barang> _isi = new();

    public IEnumerable<Barang> Semua
        => _isi.Values.OrderBy(b => b.Kode, StringComparer.Ordinal);

    public void Daftar(Barang b)
    {
        if (_isi.ContainsKey(b.Kode))
            throw new InvalidOperationException("kode sudah ada");
        _isi[b.Kode] = b;
    }

    public int Catat(string kode, Gerak gerak, int jumlah)
    {
        if (!_isi.TryGetValue(kode, out Barang? b))
            throw new KeyNotFoundException("kode tidak dikenal");
        if (jumlah <= 0)
            throw new ArgumentOutOfRangeException(nameof(jumlah),
                "jumlah tidak sah");

        int stokBaru = gerak == Gerak.Masuk ? b.Stok + jumlah : b.Stok - jumlah;
        if (stokBaru < 0)
            throw new InvalidOperationException("stok tidak cukup");

        _isi[kode] = b with { Stok = stokBaru };
        return stokBaru;
    }

    public decimal NilaiPersediaan()
        => _isi.Values.Sum(b => b.Stok * b.Harga);

    public IEnumerable<Barang> StokMenipis(int batas)
        => _isi.Values.Where(b => b.Stok < batas)
                      .OrderBy(b => b.Stok)
                      .ThenBy(b => b.Kode, StringComparer.Ordinal);
}

// ------------------------------------------------------------ ANTARMUKA
class Program
{
    static Gudang gudang = new();

    static void CobaDaftar(Barang b)
    {
        try
        {
            gudang.Daftar(b);
            Console.WriteLine($"daftar {b.Kode} -> terdaftar");
        }
        catch (InvalidOperationException e)
        {
            Console.WriteLine($"daftar {b.Kode} -> DITOLAK: {e.Message}");
        }
    }

    static void CobaCatat(string kode, Gerak gerak, int jumlah)
    {
        string label = $"{gerak} {kode} {jumlah}";
        try
        {
            int stok = gudang.Catat(kode, gerak, jumlah);
            Console.WriteLine($"{label} -> stok {stok}");
        }
        catch (KeyNotFoundException e)
        {
            Console.WriteLine($"{label} -> DITOLAK: {e.Message}");
        }
        catch (ArgumentOutOfRangeException)
        {
            Console.WriteLine($"{label} -> DITOLAK: jumlah tidak sah");
        }
        catch (InvalidOperationException e)
        {
            Console.WriteLine($"{label} -> DITOLAK: {e.Message}");
        }
    }

    static void Main()
    {
        gudang.Daftar(new Barang("B01", "Kabel", 10, 15000m));
        gudang.Daftar(new Barang("B02", "Adaptor", 4, 85000m));
        gudang.Daftar(new Barang("B03", "Mouse", 25, 120000m));

        CobaDaftar(new Barang("B01", "Kabel Lain", 5, 10000m));
        CobaCatat("B01", Gerak.Masuk, 15);
        CobaCatat("B02", Gerak.Keluar, 10);
        CobaCatat("B03", Gerak.Keluar, 5);
        CobaCatat("B09", Gerak.Masuk, 1);
        CobaCatat("B03", Gerak.Keluar, 0);

        Console.WriteLine("---");
        foreach (Barang b in gudang.Semua)
            Console.WriteLine($"{b.Kode,-5}{b.Nama,-12}{b.Stok,4}{b.Harga,12}"
                            + $"{b.Stok * b.Harga,12}");

        Console.WriteLine("---");
        Console.WriteLine($"Nilai persediaan: {gudang.NilaiPersediaan()}");

        string menipis = string.Join(", ",
            gudang.StokMenipis(10).Select(b => $"{b.Kode} {b.Nama} ({b.Stok})"));
        Console.WriteLine($"Stok menipis (<10): {menipis}");
    }
}""",
    },
]
