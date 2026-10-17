RUST_EXERCISES = [
    {
        "title": "Latihan 1: Perkenalan Diri",
        "difficulty": "Mudah",
        "question": [
            "Buat program Rust yang menampilkan tepat tiga baris:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Rust.",
            "  Rust menjamin keamanan memori saat kompilasi.",
        ],
        "hints": [
            "Program Rust dimulai dari satu fungsi utama, dan teks dicetak lewat makro. Baca ulang materi \"Pengenalan Rust & Instalasi\".",
            "Tulis fn main() dengan tiga pemanggilan println!, satu untuk tiap baris. Tanda seru menandakan makro, dan setiap pernyataan diakhiri titik koma.",
        ],
        "solution": """fn main() {
    println!("Halo, namaku Andi!");
    println!("Aku sedang belajar Rust.");
    println!("Rust menjamin keamanan memori saat kompilasi.");
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
            "Yang diuji: pembagian bilangan bulat dan konversi tipe yang harus ditulis sendiri. Baca ulang materi \"Variabel, Mutabilitas & Tipe Data\".",
            "a / b dengan dua bilangan bulat memotong sisanya, jadi 17 / 5 hasilnya 3. Untuk baris desimal, ubah keduanya ke f64 dengan as, lalu cetak dua angka di belakang koma.",
            "Nama variabel boleh langsung di dalam kurung kurawal, misalnya \"{a} + {b} = {}\". Format dua desimal: {:.2}.",
        ],
        "solution": """fn main() {
    let a = 17;
    let b = 5;

    println!("{a} + {b} = {}", a + b);
    println!("{a} - {b} = {}", a - b);
    println!("{a} * {b} = {}", a * b);
    println!("{a} / {b} = {}", a / b);
    println!("{a} % {b} = {}", a % b);
    println!("{a} / {b} = {:.2} (desimal)", a as f64 / b as f64);
}""",
    },
    {
        "title": "Latihan 3: Konversi Suhu",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka suhu Celsius dari input.",
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
        ],
        "hints": [
            "Kamu perlu membaca satu baris dari input, membersihkannya, lalu mengubahnya jadi angka pecahan. Baca ulang materi \"Membaca Masukan & Berkas\".",
            "Siapkan String kosong yang mutable, isi lewat read_line, buang karakter pindah baris dengan trim, lalu parse ke f64. Tulis rumusnya dengan literal pecahan (9.0, 5.0, 32.0), karena f64 nggak bisa dicampur bilangan bulat. Jangan cetak apa pun sebelum membaca input.",
            "parse perlu tahu tipe tujuannya, dan anotasi di variabel sudah cukup: let c: f64 = baris.trim().parse().unwrap();",
        ],
        "stdin": "25\n",
        "solution": """use std::io;

fn main() {
    let mut baris = String::new();
    io::stdin().read_line(&mut baris).unwrap();
    let c: f64 = baris.trim().parse().unwrap();

    let f = c * 9.0 / 5.0 + 32.0;
    let k = c + 273.15;

    println!("Celsius    : {c:.2}");
    println!("Fahrenheit : {f:.2}");
    println!("Kelvin     : {k:.2}");
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
            "match di Rust bisa mencocokkan rentang angka dan menghasilkan nilai. Baca ulang materi \"Pattern Matching: match & if let\" dan \"Percabangan & Perulangan\".",
            "Baca nilai sebagai u32, lalu isi grade dari sebuah match dengan satu cabang per rentang dan _ untuk sisanya. Status cukup if-else yang juga menghasilkan nilai.",
            "Rentang inklusif ditulis 85..=100 => 'A'. Versi .. tanpa = nggak memasukkan batas atasnya.",
        ],
        "stdin_list": ["92\n", "78\n", "65\n", "45\n", "12\n"],
        "solution": """use std::io;

fn main() {
    let mut baris = String::new();
    io::stdin().read_line(&mut baris).unwrap();
    let nilai: u32 = baris.trim().parse().unwrap();

    let grade = match nilai {
        85..=100 => 'A',
        75..=84 => 'B',
        60..=74 => 'C',
        40..=59 => 'D',
        _ => 'E',
    };

    let status = if nilai >= 75 { "Lulus" } else { "Tidak Lulus" };

    println!("Grade: {grade}");
    println!("Status: {status}");
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
            "Tabel butuh perulangan bersarang dan format lebar tetap. Baca ulang materi \"Percabangan & Perulangan\".",
            "Perulangan luar untuk baris, dalam untuk kolom. Awali tiap baris dengan dua spasi, cetak sel tanpa pindah baris, beri tiga spasi sesudah setiap sel kecuali yang kelima, lalu pindah baris.",
            "print! nggak pindah baris, println!() kosong cuma pindah baris. Rata kanan selebar 2: {:2}, misalnya untuk hasil b * k.",
        ],
        "solution": """fn main() {
    for b in 1..=5 {
        print!("  ");
        for k in 1..=5 {
            print!("{b} x {k} = {:2}", b * k);
            if k < 5 {
                print!("   ");
            }
        }
        println!();
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
            "  Data      : [78, 92, 65, 88, 71, 95, 59, 83]",
            "  Terurut   : [59, 65, 71, 78, 83, 88, 92, 95]",
            "  Jumlah    : 8",
            "  Total     : 631",
            "  Rata-rata : 78.88",
            "  Tertinggi : 95",
            "  Terendah  : 59",
            "  Di atas rata-rata: 4",
        ],
        "hints": [
            "Latihan ini soal metode iterator sederhana dan mengurutkan salinan. Baca ulang materi \"Vec & HashMap\" dan \"Closure & Iterator\".",
            "Jumlahkan dengan iter().sum(), hitung rata-rata dengan konversi as f64, lalu ambil max dan min (keduanya Option). Urutkan salinannya, bukan Vec aslinya, karena baris Data masih butuh urutan awal. Untuk yang di atas rata-rata: filter lalu count.",
            "Salinan dibuat dengan .to_vec() lalu .sort(). {:?} mencetak Vec dalam bentuk [a, b, c].",
        ],
        "solution": """fn main() {
    let nilai = vec![78, 92, 65, 88, 71, 95, 59, 83];

    let total: i32 = nilai.iter().sum();
    let rata = total as f64 / nilai.len() as f64;

    let mut urut = nilai.to_vec();
    urut.sort();

    let di_atas = nilai.iter().filter(|n| (**n as f64) > rata).count();

    println!("Data      : {nilai:?}");
    println!("Terurut   : {urut:?}");
    println!("Jumlah    : {}", nilai.len());
    println!("Total     : {total}");
    println!("Rata-rata : {rata:.2}");
    println!("Tertinggi : {}", nilai.iter().max().unwrap());
    println!("Terendah  : {}", nilai.iter().min().unwrap());
    println!("Di atas rata-rata: {di_atas}");
}""",
    },
    {
        "title": "Latihan 7: Balik Teks & Palindrom",
        "difficulty": "Menengah",
        "question": [
            "Baca satu baris teks dari input.",
            "Tampilkan:",
            "  Asli    : teks aslinya",
            "  Dibalik : teksnya dibalik huruf per huruf",
            "  Huruf   : jumlah huruf tanpa spasi",
            "  Palindrom: ya / bukan (abaikan spasi dan besar-kecil huruf)",
            "",
            "Untuk input 'Kasur ini rusak', output yang benar:",
            "  Asli    : Kasur ini rusak",
            "  Dibalik : kasur ini rusaK",
            "  Huruf   : 13",
            "  Palindrom: ya",
        ],
        "hints": [
            "String di Rust diproses per karakter lewat chars(). Baca ulang materi \"Slice & String\".",
            "Simpan baris tanpa karakter pindah baris di ujungnya. Untuk palindrom, buang spasi, jadikan huruf kecil, lalu bandingkan dengan kebalikannya. Jumlah huruf dihitung dari versi tanpa spasi. Jangan cetak apa pun sebelum read_line.",
            "Membalik teks: s.chars().rev().collect::<String>(). Membuang spasi: filter pada chars() dengan !c.is_whitespace().",
        ],
        "stdin_list": ["Kasur ini rusak\n", "Belajar Rust\n", "Ini\n"],
        "solution": """use std::io;

fn balik(s: &str) -> String {
    s.chars().rev().collect()
}

fn main() {
    let mut baris = String::new();
    io::stdin().read_line(&mut baris).unwrap();
    let teks = baris.trim_end_matches('\\n').trim_end_matches('\\r');

    let rapat: String = teks.chars().filter(|c| !c.is_whitespace()).collect();
    let bersih = rapat.to_lowercase();
    let palindrom = bersih == balik(&bersih);

    println!("Asli    : {teks}");
    println!("Dibalik : {}", balik(teks));
    println!("Huruf   : {}", rapat.chars().count());
    println!("Palindrom: {}", if palindrom { "ya" } else { "bukan" });
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
            "Menghitung kemunculan adalah pekerjaan HashMap, dan mengurutkan hasilnya butuh Vec. Baca ulang materi \"Vec & HashMap\".",
            "Pecah kalimat dengan split_whitespace, lalu naikkan hitungan tiap kata lewat entry API. HashMap nggak punya urutan, jadi kumpulkan pasangannya ke Vec dan urutkan: jumlah menurun dulu, kalau sama baru abjad naik.",
            "Menaikkan hitungan: *hitung.entry(kata).or_insert(0) += 1; dua kunci urutan: b.1.cmp(a.1).then(a.0.cmp(b.0)). Rata kiri 7: {kata:<7}.",
        ],
        "solution": """use std::collections::HashMap;

fn main() {
    let kalimat = "kucing makan ikan kucing tidur ikan kucing";

    let mut hitung: HashMap<&str, u32> = HashMap::new();
    for kata in kalimat.split_whitespace() {
        *hitung.entry(kata).or_insert(0) += 1;
    }

    let mut pasangan: Vec<(&&str, &u32)> = hitung.iter().collect();
    pasangan.sort_by(|a, b| b.1.cmp(a.1).then(a.0.cmp(b.0)));

    for (kata, n) in &pasangan {
        println!("{kata:<7}: {n}");
    }

    println!("---");
    println!("Kata unik  : {}", hitung.len());
    println!("Total kata : {}", kalimat.split_whitespace().count());
}""",
    },
    {
        "title": "Latihan 9: Struct Murid dengan Method",
        "difficulty": "Menengah",
        "question": [
            "Buat struct Murid dengan field nama (String) dan nilai (u32).",
            "",
            "Tambahkan di blok impl:",
            "  - fn baru(nama: &str, nilai: u32) -> Self",
            "  - fn grade(&self) -> char : >=85 A, >=75 B, >=60 C, sisanya D",
            "  - fn lulus(&self) -> bool : nilai >= 75",
            "  - fn ringkas(&self) -> String berbentuk \"Andi     92 A\"",
            "    (nama rata kiri 8, nilai rata kanan 3, spasi, grade)",
            "",
            "Di main, buat tiga murid: Andi 92, Budi 78, Cici 64.",
            "Cetak ringkasan ketiganya, lalu jumlah yang lulus dan",
            "rata-ratanya.",
            "",
            "Output yang benar:",
            "  Andi     92 A",
            "  Budi     78 B",
            "  Cici     64 C",
            "  ---",
            "  Lulus     : 2 dari 3",
            "  Rata-rata : 78.00",
        ],
        "hints": [
            "Struct plus blok impl: fungsi terkait untuk membuat objek, method &self untuk membaca. Baca ulang materi \"Struct\".",
            "baru nggak punya self, jadi dipanggil lewat Murid::baru. grade memakai match atas rentang nilai. ringkas memakai format!, yang bekerja seperti println! tapi mengembalikan String. Di main, hitung yang lulus dengan filter lalu count.",
            "Format ringkas: nama rata kiri 8 dan nilai rata kanan 3, yaitu {:<8}{:>3} lalu spasi dan grade.",
        ],
        "solution": """struct Murid {
    nama: String,
    nilai: u32,
}

impl Murid {
    fn baru(nama: &str, nilai: u32) -> Self {
        Murid { nama: nama.to_string(), nilai }
    }

    fn grade(&self) -> char {
        match self.nilai {
            85..=u32::MAX => 'A',
            75..=84 => 'B',
            60..=74 => 'C',
            _ => 'D',
        }
    }

    fn lulus(&self) -> bool {
        self.nilai >= 75
    }

    fn ringkas(&self) -> String {
        format!("{:<8}{:>3} {}", self.nama, self.nilai, self.grade())
    }
}

fn main() {
    let kelas = vec![
        Murid::baru("Andi", 92),
        Murid::baru("Budi", 78),
        Murid::baru("Cici", 64),
    ];

    for m in &kelas {
        println!("{}", m.ringkas());
    }

    let lulus = kelas.iter().filter(|m| m.lulus()).count();
    let total: u32 = kelas.iter().map(|m| m.nilai).sum();

    println!("---");
    println!("Lulus     : {lulus} dari {}", kelas.len());
    println!("Rata-rata : {:.2}", total as f64 / kelas.len() as f64);
}""",
    },
    {
        "title": "Latihan 10: Enum Bentuk & Trait",
        "difficulty": "Lanjut",
        "question": [
            "Buat trait Bangun dengan method luas() -> f64 dan nama() -> String.",
            "",
            "Buat tiga struct yang mengimplementasinya:",
            "  Persegi { sisi }, Lingkaran { jari }, dan",
            "  PersegiPanjang { panjang, lebar }",
            "",
            "Pakai PI = 3.14159 untuk lingkaran.",
            "",
            "Di main, masukkan Persegi(4.0), Lingkaran(3.0), dan",
            "PersegiPanjang(6.0, 3.0) ke dalam SATU Vec<Box<dyn Bangun>>,",
            "lalu telusuri sekali untuk mencetak semuanya dan totalnya.",
            "",
            "Output yang benar:",
            "  Persegi            16.00",
            "  Lingkaran          28.27",
            "  PersegiPanjang     18.00",
            "  ------------------------",
            "  TOTAL              62.27",
            "",
            "Nama rata kiri 16, luas rata kanan 8 dengan dua desimal.",
            "Garis pemisah 24 tanda minus.",
        ],
        "hints": [
            "Satu Vec bisa berisi tipe yang berbeda kalau isinya trait object. Baca ulang materi \"Trait\" dan \"Smart Pointer: Box, Rc & RefCell\".",
            "Definisikan trait Bangun, lalu impl untuk tiap struct. Vec-nya bertipe Vec<Box<dyn Bangun>>; Box perlu karena ukuran tiap struct berbeda. Telusuri sekali: cetak tiap baris dan tambahkan luasnya ke total.",
            "Isi Vec: Box::new(Persegi { sisi: 4.0 }). Format baris: {:<16}{:>8.2}. Garis pemisah: \"-\".repeat(24).",
        ],
        "solution": """trait Bangun {
    fn luas(&self) -> f64;
    fn nama(&self) -> String;
}

struct Persegi {
    sisi: f64,
}

struct Lingkaran {
    jari: f64,
}

struct PersegiPanjang {
    panjang: f64,
    lebar: f64,
}

const PI: f64 = 3.14159;

impl Bangun for Persegi {
    fn luas(&self) -> f64 {
        self.sisi * self.sisi
    }
    fn nama(&self) -> String {
        "Persegi".to_string()
    }
}

impl Bangun for Lingkaran {
    fn luas(&self) -> f64 {
        PI * self.jari * self.jari
    }
    fn nama(&self) -> String {
        "Lingkaran".to_string()
    }
}

impl Bangun for PersegiPanjang {
    fn luas(&self) -> f64 {
        self.panjang * self.lebar
    }
    fn nama(&self) -> String {
        "PersegiPanjang".to_string()
    }
}

fn main() {
    let semua: Vec<Box<dyn Bangun>> = vec![
        Box::new(Persegi { sisi: 4.0 }),
        Box::new(Lingkaran { jari: 3.0 }),
        Box::new(PersegiPanjang { panjang: 6.0, lebar: 3.0 }),
    ];

    let mut total = 0.0;
    for b in &semua {
        println!("{:<16}{:>8.2}", b.nama(), b.luas());
        total += b.luas();
    }

    println!("{}", "-".repeat(24));
    println!("{:<16}{:>8.2}", "TOTAL", total);
}""",
    },
    {
        "title": "Latihan 11: Result & Operator Tanya",
        "difficulty": "Lanjut",
        "question": [
            "Buat enum GalatNilai dengan dua varian:",
            "  BukanAngka(String) dan DiLuarRentang(i32)",
            "",
            "Buat fn parse_nilai(teks: &str) -> Result<i32, GalatNilai> yang:",
            "  - membuang spasi di ujung lalu mengurai jadi i32",
            "  - mengembalikan BukanAngka kalau gagal diurai",
            "  - mengembalikan DiLuarRentang kalau di luar 0..=100",
            "",
            "Buat fn rata_rata(semua: &[&str]) -> Result<f64, GalatNilai>",
            "yang memakai operator ? sehingga satu kegagalan membatalkan",
            "seluruh perhitungan.",
            "",
            "Uji parse_nilai dengan: \"88\", \" 92 \", \"abc\", \"150\", \"-3\"",
            "Lalu uji rata_rata dengan [\"80\",\"90\",\"100\"] dan",
            "[\"80\",\"xx\",\"100\"].",
            "",
            "Output yang benar:",
            "     88 -> 88",
            "    92  -> 92",
            "    abc -> bukan angka: abc",
            "    150 -> di luar 0..100: 150",
            "     -3 -> di luar 0..100: -3",
            "  baik  : Ok(90.0)",
            "  rusak : Err(BukanAngka(\"xx\"))",
            "",
            "Teks masukan dicetak rata kanan selebar 5.",
        ],
        "hints": [
            "Galat buatan sendiri berupa enum, dan operator ? meneruskannya ke pemanggil. Baca ulang materi \"Penanganan Galat: panic! & Result\".",
            "parse_nilai: trim, parse ke i32, ubah galat parse jadi BukanAngka, lalu cek rentang 0..=100. rata_rata menjumlahkan hasil parse_nilai dengan ?, jadi kegagalan pertama langsung dikembalikan. Pasang derive(Debug) pada enum supaya bisa dicetak dengan {:?}.",
            "map_err mengganti tipe galatnya sebelum ?: .map_err(|_| GalatNilai::BukanAngka(...))?. Cek rentang: (0..=100).contains(&n). Teks masukan rata kanan 5: {t:>5}.",
        ],
        "solution": """#[derive(Debug)]
enum GalatNilai {
    BukanAngka(String),
    DiLuarRentang(i32),
}

fn parse_nilai(teks: &str) -> Result<i32, GalatNilai> {
    let n: i32 = teks
        .trim()
        .parse()
        .map_err(|_| GalatNilai::BukanAngka(teks.trim().to_string()))?;

    if !(0..=100).contains(&n) {
        return Err(GalatNilai::DiLuarRentang(n));
    }
    Ok(n)
}

fn rata_rata(semua: &[&str]) -> Result<f64, GalatNilai> {
    let mut total = 0;
    for t in semua {
        total += parse_nilai(t)?;
    }
    Ok(total as f64 / semua.len() as f64)
}

fn main() {
    for t in ["88", " 92 ", "abc", "150", "-3"] {
        match parse_nilai(t) {
            Ok(n) => println!("{t:>5} -> {n}"),
            Err(GalatNilai::BukanAngka(s)) => println!("{t:>5} -> bukan angka: {s}"),
            Err(GalatNilai::DiLuarRentang(n)) => {
                println!("{t:>5} -> di luar 0..100: {n}")
            }
        }
    }

    println!("baik  : {:?}", rata_rata(&["80", "90", "100"]));
    println!("rusak : {:?}", rata_rata(&["80", "xx", "100"]));
}""",
    },
    {
        "title": "Latihan 12: Rantai Iterator",
        "difficulty": "Lanjut",
        "question": [
            "Buat struct Transaksi { barang: String, kategori: String,",
            "jumlah: i64, harga: i64 } dan isi daftar berikut:",
            "  Kopi  Minuman  3  25000",
            "  Teh   Minuman  5  15000",
            "  Roti  Makanan  2  20000",
            "  Nasi  Makanan  4  30000",
            "  Jus   Minuman  1  35000",
            "",
            "Dengan rantai iterator, tampilkan:",
            "  1. Semua transaksi bersubtotal, terurut subtotal MENURUN.",
            "     Kalau subtotalnya sama, urutkan nama barang MENAIK.",
            "  2. Total keseluruhan",
            "  3. Jumlah transaksi di atas 50000",
            "  4. Nama barang termahal subtotalnya",
            "",
            "Output yang benar:",
            "  Nasi       Makanan     4 x  30000 =   120000",
            "  Kopi       Minuman     3 x  25000 =    75000",
            "  Teh        Minuman     5 x  15000 =    75000",
            "  Roti       Makanan     2 x  20000 =    40000",
            "  Jus        Minuman     1 x  35000 =    35000",
            "  ---",
            "  Total     : 345000",
            "  Di atas 50rb: 3",
            "  Termahal  : Nasi",
            "",
            "Kolom: barang rata kiri 11, kategori rata kiri 11, jumlah",
            "rata kanan 2, harga rata kanan 6, subtotal rata kanan 8.",
        ],
        "hints": [
            "Ini latihan rantai iterator: map, sort_by, filter, sum, dan max_by_key. Baca ulang materi \"Closure & Iterator\".",
            "Hitung subtotal sekali dengan map ke pasangan (transaksi, subtotal), kumpulkan ke Vec, lalu urutkan: subtotal menurun, kalau sama nama barang naik. Total, hitungan di atas 50000, dan barang termahal masing-masing cukup satu rantai pendek.",
            "Dua kunci urutan: b.1.cmp(&a.1).then(a.0.barang.cmp(&b.0.barang)). sum::<i64>() butuh turbofish kalau tipenya nggak bisa disimpulkan, dan max_by_key mengembalikan Option.",
        ],
        "solution": """struct Transaksi {
    barang: String,
    kategori: String,
    jumlah: i64,
    harga: i64,
}

fn main() {
    let data: Vec<Transaksi> = vec![
        ("Kopi", "Minuman", 3, 25000),
        ("Teh", "Minuman", 5, 15000),
        ("Roti", "Makanan", 2, 20000),
        ("Nasi", "Makanan", 4, 30000),
        ("Jus", "Minuman", 1, 35000),
    ]
    .into_iter()
    .map(|(b, k, j, h)| Transaksi {
        barang: b.to_string(),
        kategori: k.to_string(),
        jumlah: j,
        harga: h,
    })
    .collect();

    let mut baris: Vec<(&Transaksi, i64)> =
        data.iter().map(|t| (t, t.jumlah * t.harga)).collect();
    baris.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.barang.cmp(&b.0.barang)));

    for (t, sub) in &baris {
        println!(
            "{:<11}{:<11}{:>2} x {:>6} = {:>8}",
            t.barang, t.kategori, t.jumlah, t.harga, sub
        );
    }

    let total: i64 = data.iter().map(|t| t.jumlah * t.harga).sum();
    let besar = data.iter().filter(|t| t.jumlah * t.harga > 50000).count();
    let termahal = data.iter().max_by_key(|t| t.jumlah * t.harga).unwrap();

    println!("---");
    println!("Total     : {total}");
    println!("Di atas 50rb: {besar}");
    println!("Termahal  : {}", termahal.barang);
}""",
    },
    {
        "title": "Latihan 13: Generic & Batasan Trait",
        "difficulty": "Lanjut",
        "question": [
            "Buat struct generic Kotak<T> dengan field isi: Vec<T> dan",
            "muat: usize.",
            "",
            "Di blok impl<T: std::fmt::Display> Kotak<T>, tambahkan:",
            "  - fn baru(muat: usize) -> Self",
            "  - fn masuk(&mut self, x: T) -> bool  (false kalau penuh)",
            "  - fn keluar(&mut self) -> Option<T>  (ambil dari DEPAN)",
            "  - fn ringkas(&self) -> String berbentuk \"[a, b] 2/3\"",
            "",
            "Di main, buat Kotak<i32> muat 3 dan Kotak<String> muat 2,",
            "lalu buktikan keduanya bekerja dengan kode yang sama.",
            "",
            "Output yang benar:",
            "  masuk 10: true",
            "  masuk 20: true",
            "  masuk 30: true",
            "  masuk 40: false",
            "  [10, 20, 30] 3/3",
            "  keluar: Some(10)",
            "  [20, 30] 2/3",
            "  ---",
            "  masuk apel: true",
            "  masuk jeruk: true",
            "  masuk mangga: false",
            "  [apel, jeruk] 2/2",
        ],
        "hints": [
            "Struct generic dengan batasan trait: satu kode untuk banyak tipe. Baca ulang materi \"Generic\" dan \"Trait\".",
            "masuk menolak kalau panjang isi sudah sama dengan muat. keluar mengambil dari depan: None kalau kosong, selain itu buang elemen indeks 0. ringkas mengubah tiap isi jadi String, menggabungkannya dengan koma, lalu menambahkan hitungan isi/muat.",
            "Batasan Display membuat x.to_string() bisa dipanggil. Gabungkan dengan join(\", \"), dan ambil dari depan dengan remove(0).",
        ],
        "solution": """use std::fmt::Display;

struct Kotak<T> {
    isi: Vec<T>,
    muat: usize,
}

impl<T: Display> Kotak<T> {
    fn baru(muat: usize) -> Self {
        Kotak { isi: Vec::new(), muat }
    }

    fn masuk(&mut self, x: T) -> bool {
        if self.isi.len() >= self.muat {
            return false;
        }
        self.isi.push(x);
        true
    }

    fn keluar(&mut self) -> Option<T> {
        if self.isi.is_empty() {
            None
        } else {
            Some(self.isi.remove(0))
        }
    }

    fn ringkas(&self) -> String {
        let daftar: Vec<String> = self.isi.iter().map(|x| x.to_string()).collect();
        format!("[{}] {}/{}", daftar.join(", "), self.isi.len(), self.muat)
    }
}

fn main() {
    let mut angka: Kotak<i32> = Kotak::baru(3);
    for n in [10, 20, 30, 40] {
        println!("masuk {n}: {}", angka.masuk(n));
    }
    println!("{}", angka.ringkas());
    println!("keluar: {:?}", angka.keluar());
    println!("{}", angka.ringkas());

    println!("---");
    let mut buah: Kotak<String> = Kotak::baru(2);
    for b in ["apel", "jeruk", "mangga"] {
        println!("masuk {b}: {}", buah.masuk(b.to_string()));
    }
    println!("{}", buah.ringkas());
}""",
    },
    {
        "title": "Latihan 14: Ownership, Borrowing & Lifetime",
        "difficulty": "Sulit",
        "question": [
            "Tulis program yang menunjukkan ownership bekerja, dengan",
            "empat fungsi:",
            "",
            "  fn ambil(s: String) -> usize        mengambil kepemilikan",
            "  fn pinjam(s: &str) -> usize         meminjam untuk membaca",
            "  fn ubah(s: &mut String)             menambahkan \"!\" di akhir",
            "  fn lebih_panjang<'a>(a: &'a str, b: &'a str) -> &'a str",
            "",
            "Di main, tunjukkan berurutan:",
            "  1. Copy pada angka: a=5, b=a, keduanya tetap sah",
            "  2. clone pada String supaya keduanya tetap sah",
            "  3. ambil() mengonsumsi variabelnya",
            "  4. pinjam() tidak mengonsumsi",
            "  5. ubah() menyunting lewat &mut",
            "  6. lebih_panjang() dengan dua &str",
            "  7. Sebuah blok dalam, untuk menunjukkan nilai dilepas di akhir scope",
            "",
            "Output yang benar:",
            "  copy    : a=5 b=5",
            "  clone   : s1=halo s2=halo",
            "  ambil   : panjang 5",
            "  pinjam  : rust masih ada, panjangnya 4",
            "  ubah    : rust!",
            "  panjang : pemrograman",
            "  blok    : hidup sebentar",
            "  selesai",
        ],
        "hints": [
            "Latihan ini memperagakan Copy, clone, move, pinjaman, dan lifetime. Baca ulang materi \"Ownership: Aturan Inti Rust\", \"Reference & Borrowing\", dan \"Lifetime\".",
            "Angka bersifat Copy, jadi b = a membuat keduanya tetap sah; String butuh clone. Sesudah ambil(s), s nggak boleh dipakai lagi. pinjam bertipe &str tapi tetap menerima &String. ubah butuh variabel let mut dan dipanggil dengan &mut. Blok dalam memperlihatkan nilai dilepas di kurung kurawal penutupnya.",
            "lebih_panjang butuh 'a karena ada dua referensi masuk dan satu keluar, jadi compiler perlu tahu kembaliannya hidup selama keduanya.",
        ],
        "solution": """fn ambil(s: String) -> usize {
    s.len()
}

fn pinjam(s: &str) -> usize {
    s.len()
}

fn ubah(s: &mut String) {
    s.push('!');
}

fn lebih_panjang<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() > b.len() {
        a
    } else {
        b
    }
}

fn main() {
    let a = 5;
    let b = a;
    println!("copy    : a={a} b={b}");

    let s1 = String::from("halo");
    let s2 = s1.clone();
    println!("clone   : s1={s1} s2={s2}");

    let s3 = String::from("dunia");
    println!("ambil   : panjang {}", ambil(s3));

    let mut s4 = String::from("rust");
    println!("pinjam  : {s4} masih ada, panjangnya {}", pinjam(&s4));

    ubah(&mut s4);
    println!("ubah    : {s4}");

    let x = String::from("pemrograman");
    let y = String::from("rust");
    println!("panjang : {}", lebih_panjang(&x, &y));

    {
        let sementara = String::from("hidup sebentar");
        println!("blok    : {sementara}");
    }
    println!("selesai");
}""",
    },
    {
        "title": "Latihan 15: Mesin Keadaan dengan Enum",
        "difficulty": "Sulit",
        "question": [
            "Buat enum Keadaan { Draf, Ditinjau, Disetujui, Ditolak, Terbit }",
            "dan enum Aksi { Kirim, Setujui, Tolak, Terbitkan, Tarik }.",
            "",
            "Buat fn lanjut(k: Keadaan, a: Aksi) -> Result<Keadaan, String>",
            "dengan aturan transisi:",
            "  Draf      + Kirim      -> Ditinjau",
            "  Ditinjau  + Setujui    -> Disetujui",
            "  Ditinjau  + Tolak      -> Ditolak",
            "  Disetujui + Terbitkan  -> Terbit",
            "  Ditolak   + Tarik      -> Draf",
            "  selain itu -> Err(\"<Aksi> tidak sah dari <Keadaan>\")",
            "",
            "Di main, jalankan urutan aksi berikut dari Draf dan cetak",
            "hasil tiap langkah:",
            "  Kirim, Terbitkan, Setujui, Tolak, Terbitkan, Tarik",
            "",
            "Kalau sebuah aksi ditolak, keadaannya TIDAK berubah.",
            "",
            "Output yang benar:",
            "  Draf      + Kirim      -> Ditinjau",
            "  Ditinjau  + Terbitkan  -> DITOLAK: Terbitkan tidak sah dari Ditinjau",
            "  Ditinjau  + Setujui    -> Disetujui",
            "  Disetujui + Tolak      -> DITOLAK: Tolak tidak sah dari Disetujui",
            "  Disetujui + Terbitkan  -> Terbit",
            "  Terbit    + Tarik      -> DITOLAK: Tarik tidak sah dari Terbit",
            "  ---",
            "  keadaan akhir: Terbit",
            "",
            "Keadaan rata kiri 10, aksi rata kiri 11.",
        ],
        "hints": [
            "Mesin keadaan paling rapi ditulis dengan match atas pasangan nilai enum. Baca ulang materi \"Enum & Option\" dan \"Pattern Matching: match & if let\".",
            "Pasang derive Debug, Clone, Copy, PartialEq pada kedua enum. lanjut mencocokkan (k, a) dengan satu cabang per transisi yang sah, dan _ untuk sisanya yang mengembalikan Err. Di main, simpan keadaan di variabel mut dan perbarui cuma kalau hasilnya Ok.",
            "{:?} mencetak nama varian. Supaya bisa diratakan, ubah dulu jadi String, misalnya format!(\"{sebelum:?}\"), lalu cetak dengan {:<10}.",
        ],
        "solution": """#[derive(Debug, Clone, Copy, PartialEq)]
enum Keadaan {
    Draf,
    Ditinjau,
    Disetujui,
    Ditolak,
    Terbit,
}

#[derive(Debug, Clone, Copy, PartialEq)]
enum Aksi {
    Kirim,
    Setujui,
    Tolak,
    Terbitkan,
    Tarik,
}

fn lanjut(k: Keadaan, a: Aksi) -> Result<Keadaan, String> {
    match (k, a) {
        (Keadaan::Draf, Aksi::Kirim) => Ok(Keadaan::Ditinjau),
        (Keadaan::Ditinjau, Aksi::Setujui) => Ok(Keadaan::Disetujui),
        (Keadaan::Ditinjau, Aksi::Tolak) => Ok(Keadaan::Ditolak),
        (Keadaan::Disetujui, Aksi::Terbitkan) => Ok(Keadaan::Terbit),
        (Keadaan::Ditolak, Aksi::Tarik) => Ok(Keadaan::Draf),
        _ => Err(format!("{a:?} tidak sah dari {k:?}")),
    }
}

fn main() {
    let mut keadaan = Keadaan::Draf;

    let urutan = [
        Aksi::Kirim,
        Aksi::Terbitkan,
        Aksi::Setujui,
        Aksi::Tolak,
        Aksi::Terbitkan,
        Aksi::Tarik,
    ];

    for a in urutan {
        let sebelum = keadaan;
        match lanjut(keadaan, a) {
            Ok(baru) => {
                keadaan = baru;
                println!("{:<10}+ {:<11}-> {baru:?}", format!("{sebelum:?}"), format!("{a:?}"));
            }
            Err(e) => {
                println!("{:<10}+ {:<11}-> DITOLAK: {e}", format!("{sebelum:?}"), format!("{a:?}"));
            }
        }
    }

    println!("---");
    println!("keadaan akhir: {keadaan:?}");
}""",
    },
    {
        "title": "Latihan 16: Proyek Akhir - Inventaris Gudang",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Bangun sistem inventaris yang MEMISAHKAN tiga lapisan:",
            "model (data), layanan (aturan), dan antarmuka (cetak).",
            "",
            "MODEL",
            "  struct Barang { kode: String, nama: String, stok: i64, harga: i64 }",
            "  enum Gerak { Masuk, Keluar }",
            "  enum GalatGudang dengan varian:",
            "    KodeSudahAda(String), KodeTidakDikenal(String),",
            "    JumlahTidakSah(i64), StokTidakCukup { punya, diminta }",
            "  Implementasikan Display untuk GalatGudang dengan pesan:",
            "    \"kode B01 sudah ada\"",
            "    \"kode B09 tidak dikenal\"",
            "    \"jumlah 0 tidak sah\"",
            "    \"stok cuma 4, diminta 10\"",
            "",
            "LAYANAN  struct Gudang berisi HashMap<String, Barang>",
            "  - daftar(Barang) -> Result<(), GalatGudang>",
            "  - catat(&str, Gerak, i64) -> Result<i64, GalatGudang>",
            "    urutan periksa: kode dulu, lalu jumlah, baru kecukupan stok",
            "  - semua() -> Vec<&Barang> terurut kode",
            "  - nilai_persediaan() -> i64",
            "  - stok_menipis(batas) -> Vec<&Barang> terurut stok naik",
            "  Gudang TIDAK BOLEH memanggil println! sama sekali.",
            "",
            "ANTARMUKA (main)",
            "  Daftarkan B01 Kabel 10 15000, B02 Adaptor 4 85000,",
            "            B03 Mouse 25 120000",
            "  Jalankan: Masuk B01 15, Keluar B02 10, Keluar B03 5,",
            "            Masuk B09 1, Keluar B03 0",
            "  Lalu cetak tabel stok, nilai persediaan, dan stok menipis <10.",
            "",
            "Output yang benar:",
            "  Masuk B01 15 -> stok 25",
            "  Keluar B02 10 -> DITOLAK: stok cuma 4, diminta 10",
            "  Keluar B03 5 -> stok 20",
            "  Masuk B09 1 -> DITOLAK: kode B09 tidak dikenal",
            "  Keluar B03 0 -> DITOLAK: jumlah 0 tidak sah",
            "  ---",
            "  B01  Kabel       25     15000      375000",
            "  B02  Adaptor      4     85000      340000",
            "  B03  Mouse       20    120000     2400000",
            "  ---",
            "  nilai persediaan: 3115000",
            "  stok menipis (<10): B02 Adaptor (4)",
            "",
            "Kolom tabel: kode rata kiri 5, nama rata kiri 12, stok rata",
            "kanan 2, harga rata kanan 10, subtotal rata kanan 12.",
        ],
        "hints": [
            "Kuncinya memisahkan lapisan: Gudang cuma mengembalikan Result, main yang mencetak. Baca ulang materi \"Proyek Utuh: Menggabungkan Semuanya\" dan \"Trait Standar & Konversi\" (bagian Display).",
            "catat memeriksa berurutan: cari barangnya dulu (galat kode), lalu jumlah harus positif, baru hitung stok baru dan tolak kalau hasilnya negatif. HashMap di Rust urutannya berubah tiap kali program jalan, jadi semua() dan stok_menipis() wajib mengurutkan sebelum mengembalikan.",
            "get_mut pada HashMap memberi &mut ke nilainya, dan ok_or_else mengubah Option jadi Result: .get_mut(kode).ok_or_else(|| GalatGudang::KodeTidakDikenal(...))?. Dengan impl Display, main cukup mencetak {e}.",
        ],
        "solution": """use std::collections::HashMap;
use std::fmt;

// ---------------------------------------------------------------- MODEL
#[derive(Debug, Clone)]
struct Barang {
    kode: String,
    nama: String,
    stok: i64,
    harga: i64,
}

#[derive(Debug, Clone, Copy)]
enum Gerak {
    Masuk,
    Keluar,
}

#[derive(Debug)]
enum GalatGudang {
    KodeSudahAda(String),
    KodeTidakDikenal(String),
    JumlahTidakSah(i64),
    StokTidakCukup { punya: i64, diminta: i64 },
}

impl fmt::Display for GalatGudang {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            GalatGudang::KodeSudahAda(k) => write!(f, "kode {k} sudah ada"),
            GalatGudang::KodeTidakDikenal(k) => write!(f, "kode {k} tidak dikenal"),
            GalatGudang::JumlahTidakSah(n) => write!(f, "jumlah {n} tidak sah"),
            GalatGudang::StokTidakCukup { punya, diminta } => {
                write!(f, "stok cuma {punya}, diminta {diminta}")
            }
        }
    }
}

// -------------------------------------------------------------- LAYANAN
struct Gudang {
    isi: HashMap<String, Barang>,
}

impl Gudang {
    fn baru() -> Self {
        Gudang { isi: HashMap::new() }
    }

    fn daftar(&mut self, b: Barang) -> Result<(), GalatGudang> {
        if self.isi.contains_key(&b.kode) {
            return Err(GalatGudang::KodeSudahAda(b.kode));
        }
        self.isi.insert(b.kode.clone(), b);
        Ok(())
    }

    fn catat(&mut self, kode: &str, gerak: Gerak, jumlah: i64)
        -> Result<i64, GalatGudang>
    {
        let b = self
            .isi
            .get_mut(kode)
            .ok_or_else(|| GalatGudang::KodeTidakDikenal(kode.to_string()))?;

        if jumlah <= 0 {
            return Err(GalatGudang::JumlahTidakSah(jumlah));
        }

        let baru = match gerak {
            Gerak::Masuk => b.stok + jumlah,
            Gerak::Keluar => b.stok - jumlah,
        };
        if baru < 0 {
            return Err(GalatGudang::StokTidakCukup {
                punya: b.stok,
                diminta: jumlah,
            });
        }

        b.stok = baru;
        Ok(baru)
    }

    fn semua(&self) -> Vec<&Barang> {
        let mut v: Vec<&Barang> = self.isi.values().collect();
        v.sort_by(|a, b| a.kode.cmp(&b.kode));
        v
    }

    fn nilai_persediaan(&self) -> i64 {
        self.isi.values().map(|b| b.stok * b.harga).sum()
    }

    fn stok_menipis(&self, batas: i64) -> Vec<&Barang> {
        let mut v: Vec<&Barang> = self.isi.values().filter(|b| b.stok < batas).collect();
        v.sort_by(|a, b| a.stok.cmp(&b.stok).then(a.kode.cmp(&b.kode)));
        v
    }
}

// ------------------------------------------------------------ ANTARMUKA
fn main() {
    let mut g = Gudang::baru();

    for (kode, nama, stok, harga) in [
        ("B01", "Kabel", 10, 15_000),
        ("B02", "Adaptor", 4, 85_000),
        ("B03", "Mouse", 25, 120_000),
    ] {
        g.daftar(Barang {
            kode: kode.to_string(),
            nama: nama.to_string(),
            stok,
            harga,
        })
        .unwrap();
    }

    let langkah: [(&str, Gerak, i64); 5] = [
        ("B01", Gerak::Masuk, 15),
        ("B02", Gerak::Keluar, 10),
        ("B03", Gerak::Keluar, 5),
        ("B09", Gerak::Masuk, 1),
        ("B03", Gerak::Keluar, 0),
    ];

    for (kode, gerak, n) in langkah {
        match g.catat(kode, gerak, n) {
            Ok(stok) => println!("{gerak:?} {kode} {n} -> stok {stok}"),
            Err(e) => println!("{gerak:?} {kode} {n} -> DITOLAK: {e}"),
        }
    }

    println!("---");
    for b in g.semua() {
        println!(
            "{:<5}{:<12}{:>2}{:>10}{:>12}",
            b.kode,
            b.nama,
            b.stok,
            b.harga,
            b.stok * b.harga
        );
    }

    println!("---");
    println!("nilai persediaan: {}", g.nilai_persediaan());

    let menipis: Vec<String> = g
        .stok_menipis(10)
        .iter()
        .map(|b| format!("{} {} ({})", b.kode, b.nama, b.stok))
        .collect();
    println!("stok menipis (<10): {}", menipis.join(", "));
}""",
    },
]
