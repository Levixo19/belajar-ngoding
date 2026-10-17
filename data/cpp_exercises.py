CPP_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program yang menampilkan:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar C++.",
            "",
            "Tulis PERSIS seperti di atas, termasuk nama Andi -- penilaian",
            "membandingkan outputmu huruf demi huruf.",
        ],
        "hints": [
            "Baca materi \"Input/Output Modern (cin & cout)\": cout mencetak teks, dan endl memindah ke baris baru.",
            "Kerangkanya: #include <iostream>, using namespace std;, int main(), dua baris cout yang masing-masing diakhiri endl, lalu return 0;.",
        ],
        "solution": """#include <iostream>
using namespace std;

int main() {
    cout << "Halo, namaku Andi!" << endl;
    cout << "Aku sedang belajar C++." << endl;
    return 0;
}""",
    },
    {
        "title": "Latihan 2: Kalkulator Sederhana",
        "difficulty": "Mudah",
        "question": [
            "Buat program dengan 2 variabel int (misal 15 dan 4).",
            "Tampilkan hasil: penjumlahan, pengurangan, perkalian,",
            "pembagian (int), dan sisa bagi menggunakan cout.",
        ],
        "hints": [
            "Operator aritmetikanya sama dengan di C; yang baru cuma cara mencetaknya, lihat materi \"Input/Output Modern (cin & cout)\". Pembagian int dengan int membuang sisa di belakang koma.",
            "Pakai a = 15 dan b = 4 supaya keluaranmu cocok dengan penilai. Satu baris per operasi dengan format seperti 15 + 4 = 19: sambung angka dan teks dengan <<, dan bungkus operasinya dengan kurung supaya jelas.",
            "Contoh satu baris: cout << a << \" + \" << b << \" = \" << (a + b) << endl; empat baris lainnya polanya sama. Di cout, tanda % bisa ditulis langsung, nggak perlu %% seperti printf.",
        ],
        "solution": """#include <iostream>
using namespace std;

int main() {
    int a = 15, b = 4;

    cout << a << " + " << b << " = " << (a + b) << endl;
    cout << a << " - " << b << " = " << (a - b) << endl;
    cout << a << " * " << b << " = " << (a * b) << endl;
    cout << a << " / " << b << " = " << (a / b) << endl;
    cout << a << " % " << b << " = " << (a % b) << endl;
    return 0;
}""",
    },
    {
        "title": "Latihan 3: Cek Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Buat program: baca satu angka nilai dari input dengan cin,",
            "jika nilai >= 75 tampilkan 'Lulus', selain itu 'Tidak Lulus'.",
            "",
            "Jangan cetak teks ajakan apa pun. Program hanya boleh mengeluarkan",
            "satu baris berisi Lulus atau Tidak Lulus.",
        ],
        "hints": [
            "Baca materi \"Input/Output Modern (cin & cout)\" untuk membaca angka dengan cin, lalu satu if-else dengan kondisi nilai >= 75.",
            "Baca nilai dengan cin >> ke variabel int. Jangan ada cout sebelum cin: penilai membandingkan seluruh keluaran, jadi teks ajakan seperti \"Masukkan nilai:\" bikin jawabanmu dianggap salah.",
            "Cabang if mencetak Lulus, cabang else mencetak Tidak Lulus, masing-masing diakhiri endl.",
        ],
        # Dua input supaya KEDUA cabang benar-benar diuji.
        "stdin_list": ["80\n", "60\n"],
        "solution": """#include <iostream>
using namespace std;

int main() {
    int nilai;

    cin >> nilai;

    if (nilai >= 75) {
        cout << "Lulus" << endl;
    } else {
        cout << "Tidak Lulus" << endl;
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 4: Deret Angka Genap dengan Vector",
        "difficulty": "Menengah",
        "question": [
            "Menggunakan vector<int>, kumpulkan semua bilangan genap",
            "dari 1 sampai 20, tampilkan semuanya beserta total jumlahnya.",
        ],
        "hints": [
            "Baca materi \"STL: Vector & Array Container\": vector bisa tumbuh lewat push_back, dan isinya bisa ditelusuri dengan range-based for.",
            "Ulangi i dari 1 sampai 20 dan masukkan i ke vector kalau genap (sisa baginya dengan 2 nol). Lalu telusuri vector-nya: cetak tiap angka diikuti spasi sambil menambahkannya ke total yang mulai dari 0. Terakhir pindah baris dan cetak Total: diikuti jumlahnya.",
            "Range-based for bentuknya for (int n : genap) { ... }, jadi kamu nggak perlu indeks sama sekali.",
        ],
        "solution": """#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> genap;
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) {
            genap.push_back(i);
        }
    }

    int total = 0;
    for (int n : genap) {
        cout << n << " ";
        total += n;
    }
    cout << endl << "Total: " << total << endl;
    return 0;
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
            "Cara paling langsung sama seperti di C: nested loop, loop luar untuk baris dan loop dalam untuk bintang. Dasar string C++ ada di materi \"String C++ Lebih Dalam & stringstream\".",
            "Baris ke-i berisi i bintang. Dengan nested loop: cetak satu '*' di loop dalam, lalu endl sesudah loop dalam selesai.",
            "Versi lebih pendek: string(i, '*') membuat string berisi i karakter '*', jadi isi loop luar cukup satu baris cout << string(i, '*') << endl;.",
        ],
        "solution": """#include <iostream>
#include <string>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        cout << string(i, '*') << endl;
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 6: Statistik Nilai dengan Vector & Algorithm",
        "difficulty": "Menengah",
        "question": [
            "Diberikan vector<int> nilai = {80,90,75,85,60,95,70}.",
            "Tampilkan nilai terbesar, terkecil, rata-rata, dan versi",
            "terurut (descending) menggunakan <algorithm>.",
        ],
        "hints": [
            "Baca materi \"STL: Algorithm Library\": max_element, min_element, dan sort bekerja dengan pasangan iterator begin() dan end().",
            "max_element dan min_element mengembalikan iterator, jadi ambil nilainya dengan *. Rata-rata adalah jumlah semua nilai dibagi banyaknya; pastikan pembagiannya pecahan, bukan bagi int. Urutan menurun didapat dari sort dengan pembanding greater<int>().",
            "accumulate dari <numeric> menjumlahkan isinya: accumulate(nilai.begin(), nilai.end(), 0). Bagi dengan (double) nilai.size() supaya hasilnya 79.2857, bukan 79. Format keluaran: Terbesar: 95, Terkecil: 60, Rata-rata: 79.2857, lalu Urutan menurun: diikuti angka-angkanya.",
        ],
        "solution": """#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    vector<int> nilai = {80, 90, 75, 85, 60, 95, 70};

    int terbesar = *max_element(nilai.begin(), nilai.end());
    int terkecil = *min_element(nilai.begin(), nilai.end());
    double rata = accumulate(nilai.begin(), nilai.end(), 0) / (double) nilai.size();

    cout << "Terbesar: " << terbesar << endl;
    cout << "Terkecil: " << terkecil << endl;
    cout << "Rata-rata: " << rata << endl;

    sort(nilai.begin(), nilai.end(), greater<int>());
    cout << "Urutan menurun: ";
    for (int n : nilai) cout << n << " ";
    cout << endl;
    return 0;
}""",
    },
    {
        "title": "Latihan 7: Function Overload Hitung Luas",
        "difficulty": "Menengah",
        "question": [
            "Buat 3 fungsi bernama SAMA 'luas' (function overloading):",
            "  1. luas(int sisi)          -> luas persegi (sisi * sisi)",
            "  2. luas(int p, int l)      -> luas persegi panjang (p * l)",
            "  3. luas(double r)          -> luas lingkaran (3.14159 * r * r)",
            "Panggil ketiganya dan tampilkan hasilnya.",
        ],
        "hints": [
            "Baca materi \"Function Overloading & Default Parameter\": compiler memilih versi fungsi dari jumlah dan tipe argumen yang kamu kirim.",
            "Tulis tiga fungsi bernama luas: versi (int) mengembalikan sisi * sisi, versi (int, int) mengembalikan p * l, dan versi (double) bertipe kembali double. Saat memanggil versi lingkaran, kirim 7.0, bukan 7; angka 7 bertipe int dan akan memanggil luas persegi.",
            "Keluaran solusi contoh: Persegi (5): 25, lalu Persegi Panjang (4x6): 24, lalu Lingkaran (r=7.0): 153.938, masing-masing satu baris.",
        ],
        "solution": """#include <iostream>
using namespace std;

int luas(int sisi) {
    return sisi * sisi;
}

int luas(int p, int l) {
    return p * l;
}

double luas(double r) {
    return 3.14159 * r * r;
}

int main() {
    cout << "Persegi (5): " << luas(5) << endl;
    cout << "Persegi Panjang (4x6): " << luas(4, 6) << endl;
    cout << "Lingkaran (r=7.0): " << luas(7.0) << endl;
    return 0;
}""",
    },
    {
        "title": "Latihan 8: Class Rekening dengan Encapsulation",
        "difficulty": "Menengah",
        "question": [
            "Buat class Rekening dengan:",
            "  - atribut private: pemilik (string), saldo (double)",
            "  - constructor mengisi keduanya",
            "  - getter getSaldo() const",
            "  - method setor(double) dan tarik(double) (return bool)",
        ],
        "hints": [
            "Baca materi \"Encapsulation: private, public, protected\" dan \"Constructor & Destructor\": atribut disembunyikan di private, dan cuma method public yang boleh mengubahnya.",
            "Constructor mengisi pemilik dan saldo, paling rapi lewat initializer list. getSaldo diberi const karena cuma membaca. setor menambah saldo kalau jumlahnya positif; tarik mengurangi saldo dan mengembalikan true kalau jumlahnya positif dan saldonya cukup, selain itu false.",
            "Skenario solusi contoh: Rekening(\"Andi\", 100000), setor 50000, cetak Saldo: 150000, lalu tarik 20000 dan 999999, lalu Saldo akhir: 130000. cout mencetak bool sebagai 1 atau 0, jadi barisnya Tarik 20000 berhasil? 1.",
        ],
        "solution": """#include <iostream>
#include <string>
using namespace std;

class Rekening {
private:
    string pemilik;
    double saldo;
public:
    Rekening(string p, double s) : pemilik(p), saldo(s) {}

    double getSaldo() const { return saldo; }

    void setor(double jumlah) {
        if (jumlah > 0) saldo += jumlah;
    }

    bool tarik(double jumlah) {
        if (jumlah > 0 && jumlah <= saldo) {
            saldo -= jumlah;
            return true;
        }
        return false;
    }
};

int main() {
    Rekening r("Andi", 100000);
    r.setor(50000);
    cout << "Saldo: " << r.getSaldo() << endl;

    cout << "Tarik 20000 berhasil? " << r.tarik(20000) << endl;
    cout << "Tarik 999999 berhasil? " << r.tarik(999999) << endl;
    cout << "Saldo akhir: " << r.getSaldo() << endl;
    return 0;
}""",
    },
    {
        "title": "Latihan 9: Map untuk Buku Kontak",
        "difficulty": "Menengah",
        "question": [
            "Menggunakan map<string,string>, buat buku kontak dengan",
            "3 entri (nama -> nomor telepon). Tampilkan semua kontak",
            "TERURUT berdasarkan nama, lalu cek satu kontak yang mungkin",
            "tidak ada dengan aman (tanpa error) memakai .count().",
        ],
        "hints": [
            "Baca materi \"STL: Map, Set & Pair\": map menyimpan pasangan kunci-nilai dan selalu terurut menurut kuncinya.",
            "Isi tiga kontak dengan kontak[nama] = nomor. Telusuri dengan range-based for; tiap elemen adalah pair, jadi namanya .first dan nomornya .second. Untuk nama yang belum tentu ada, cek dengan .count(), karena kontak[nama] justru menambahkan entri kosong kalau namanya belum ada.",
            "Data solusi contoh: Andi 0812-1111-1111, Budi 0813-2222-2222, Citra 0812-3333-3333, dicetak sebagai Andi: 0812-1111-1111. Nama yang dicek Zaki, dengan pesan Zaki tidak ditemukan.",
        ],
        "solution": """#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, string> kontak;
    kontak["Andi"] = "0812-1111-1111";
    kontak["Budi"] = "0813-2222-2222";
    kontak["Citra"] = "0812-3333-3333";

    for (const auto &pasangan : kontak) {   // otomatis terurut berdasarkan nama
        cout << pasangan.first << ": " << pasangan.second << endl;
    }

    if (kontak.count("Zaki") == 0) {
        cout << "Zaki tidak ditemukan" << endl;
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 10: Inheritance & Virtual Function Hewan",
        "difficulty": "Lanjut",
        "question": [
            "Buat class Hewan (nama, virtual method bersuara()).",
            "Buat subclass Kucing dan Anjing yang override bersuara().",
            "Buat vector<Hewan*> berisi keduanya, panggil bersuara() untuk",
            "semua (polymorphism), lalu bersihkan memori dengan delete.",
        ],
        "hints": [
            "Baca materi \"Polymorphism & Virtual Function\": method yang diberi virtual di class induk akan menjalankan versi anak walau dipanggil lewat pointer ke induk.",
            "Hewan menyimpan nama (protected supaya anak bisa memakainya) dan punya method virtual bersuara(). Kucing dan Anjing meneruskan nama ke constructor Hewan lalu override bersuara(). Simpan objek hasil new di vector<Hewan*>, panggil bersuara() lewat loop, lalu delete tiap elemen.",
            "Beri Hewan destructor virtual (virtual ~Hewan() {}) supaya delete lewat Hewan* membersihkan objek anak dengan benar. Keluaran solusi contoh: Tom: Meong! lalu Bobby: Guk!",
        ],
        "solution": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Hewan {
protected:
    string nama;
public:
    Hewan(string n) : nama(n) {}
    virtual void bersuara() {
        cout << nama << " bersuara." << endl;
    }
    virtual ~Hewan() {}
};

class Kucing : public Hewan {
public:
    Kucing(string n) : Hewan(n) {}
    void bersuara() override {
        cout << nama << ": Meong!" << endl;
    }
};

class Anjing : public Hewan {
public:
    Anjing(string n) : Hewan(n) {}
    void bersuara() override {
        cout << nama << ": Guk!" << endl;
    }
};

int main() {
    vector<Hewan*> daftar = { new Kucing("Tom"), new Anjing("Bobby") };

    for (Hewan *h : daftar) {
        h->bersuara();
    }

    for (Hewan *h : daftar) {
        delete h;      // virtual destructor memastikan cleanup benar
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 11: Abstract Class Bentuk Geometris",
        "difficulty": "Lanjut",
        "question": [
            "Buat abstract class Bentuk dengan pure virtual function",
            "luas() dan keliling(). Buat subclass Persegi dan",
            "Lingkaran yang implement keduanya. Buat vector<Bentuk*>",
            "dan tampilkan luas+keliling semua bentuk.",
        ],
        "hints": [
            "Baca materi \"Abstract Class & Pure Virtual Function\": method yang diakhiri = 0 wajib diisi class turunan, dan class induknya nggak bisa dibuat objeknya.",
            "Persegi menyimpan sisi (luas sisi * sisi, keliling 4 * sisi); Lingkaran menyimpan jari-jari (luas PI * r * r, keliling 2 * PI * r). Simpan new Persegi(5) dan new Lingkaran(7) di vector<Bentuk*>, cetak keduanya dalam satu loop, lalu delete.",
            "Pakai PI = 3.14159 dan format Luas: 25, Keliling: 20 per bentuk. Jangan lupa destructor virtual di Bentuk.",
        ],
        "solution": """#include <iostream>
#include <vector>
using namespace std;

class Bentuk {
public:
    virtual double luas() = 0;
    virtual double keliling() = 0;
    virtual ~Bentuk() {}
};

class Persegi : public Bentuk {
private:
    double sisi;
public:
    Persegi(double s) : sisi(s) {}
    double luas() override { return sisi * sisi; }
    double keliling() override { return 4 * sisi; }
};

class Lingkaran : public Bentuk {
private:
    double radius;
    const double PI = 3.14159;
public:
    Lingkaran(double r) : radius(r) {}
    double luas() override { return PI * radius * radius; }
    double keliling() override { return 2 * PI * radius; }
};

int main() {
    vector<Bentuk*> bentuk = { new Persegi(5), new Lingkaran(7) };

    for (Bentuk *b : bentuk) {
        cout << "Luas: " << b->luas() << ", Keliling: " << b->keliling() << endl;
    }

    for (Bentuk *b : bentuk) delete b;
    return 0;
}""",
    },
    {
        "title": "Latihan 12: Operator Overloading Vector2D",
        "difficulty": "Lanjut",
        "question": [
            "Buat class Vector2D (x, y) dengan overload operator:",
            "  + (penjumlahan dua vector)",
            "  - (pengurangan dua vector)",
            "  == (membandingkan kesamaan)",
            "  << (agar bisa langsung di-cout)",
        ],
        "hints": [
            "Baca materi \"Operator Overloading\": operator ditulis sebagai fungsi bernama operator+, operator==, dan seterusnya.",
            "+ dan - mengembalikan Vector2D baru dari penjumlahan atau pengurangan tiap komponen; == mengembalikan true kalau x dan y sama-sama cocok. Ketiganya bisa jadi method const yang menerima const Vector2D&. << beda sendiri: operan kirinya ostream, jadi ia ditulis sebagai fungsi friend dan mengembalikan ostream-nya.",
            "Bentuk <<: friend ostream& operator<<(ostream &os, const Vector2D &v) { os << ...; return os; }. Formatnya (x, y), jadi solusi contoh dengan a(1, 2) dan b(3, 4) mencetak a + b = (4, 6), a - b = (-2, -2), dan a == Vector2D(1,2)? 1.",
        ],
        "solution": """#include <iostream>
using namespace std;

class Vector2D {
public:
    double x, y;
    Vector2D(double x = 0, double y = 0) : x(x), y(y) {}

    Vector2D operator+(const Vector2D &lain) const {
        return Vector2D(x + lain.x, y + lain.y);
    }
    Vector2D operator-(const Vector2D &lain) const {
        return Vector2D(x - lain.x, y - lain.y);
    }
    bool operator==(const Vector2D &lain) const {
        return x == lain.x && y == lain.y;
    }
    friend ostream& operator<<(ostream &os, const Vector2D &v) {
        os << "(" << v.x << ", " << v.y << ")";
        return os;
    }
};

int main() {
    Vector2D a(1, 2), b(3, 4);

    cout << "a + b = " << (a + b) << endl;
    cout << "a - b = " << (a - b) << endl;
    cout << "a == Vector2D(1,2)? " << (a == Vector2D(1, 2)) << endl;
    return 0;
}""",
    },
    {
        "title": "Latihan 13: Template Function & Class Stack",
        "difficulty": "Lanjut",
        "question": [
            "Buat function template cariMax(vector<T> data) yang",
            "mengembalikan elemen terbesar (tanpa memakai algorithm STL,",
            "loop manual). Buat juga class template StackSederhana<T>",
            "dengan method push(T), pop(), dan isEmpty(), berbasis vector<T>.",
        ],
        "hints": [
            "Baca materi \"Templates (Generic Programming)\": fungsi atau class cukup ditulis sekali dengan parameter tipe T, lalu compiler membuatkan versinya untuk tiap tipe yang dipakai.",
            "cariMax: anggap data[0] terbesar, lalu bandingkan dengan sisa elemen lewat loop biasa. StackSederhana menyimpan vector<T> secara private; push memanggil push_back, isEmpty memanggil empty(), dan pop mengambil elemen paling belakang lalu membuangnya.",
            "Di pop, simpan dulu data.back() ke variabel, baru panggil data.pop_back(), lalu kembalikan variabelnya; pop_back sendiri nggak mengembalikan apa-apa. Solusi contoh mencetak Max: 9 dari {5, 8, 2, 9, 1}, lalu push Andi, Budi, Citra dan pop sampai kosong (Citra, Budi, Andi).",
        ],
        "solution": """#include <iostream>
#include <vector>
using namespace std;

template <typename T>
T cariMax(vector<T> data) {
    T maks = data[0];
    for (size_t i = 1; i < data.size(); i++) {
        if (data[i] > maks) maks = data[i];
    }
    return maks;
}

template <typename T>
class StackSederhana {
private:
    vector<T> data;
public:
    void push(T nilai) { data.push_back(nilai); }
    T pop() {
        T atas = data.back();
        data.pop_back();
        return atas;
    }
    bool isEmpty() const { return data.empty(); }
};

int main() {
    vector<int> angka = {5, 8, 2, 9, 1};
    cout << "Max: " << cariMax(angka) << endl;

    StackSederhana<string> stack;
    stack.push("Andi");
    stack.push("Budi");
    stack.push("Citra");

    while (!stack.isEmpty()) {
        cout << stack.pop() << endl;   // Citra, Budi, Andi (LIFO)
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 14: Exception Handling Kalkulator",
        "difficulty": "Lanjut",
        "question": [
            "Buat fungsi bagi(double a, double b) yang throw",
            "runtime_error jika b == 0. Buat class custom exception",
            "NilaiNegatifException untuk kasus akar dari bilangan negatif",
            "pada fungsi akarKuadrat(double x). Uji keduanya dengan try-catch.",
        ],
        "hints": [
            "Baca materi \"Exception Handling\": throw melempar objek exception, dan catch yang tipenya cocok akan menangkapnya.",
            "bagi melempar runtime_error (dari <stdexcept>) kalau b == 0. NilaiNegatifException mewarisi exception, menyimpan pesannya sendiri, dan override what(). akarKuadrat melempar exception itu kalau x < 0, selain itu mengembalikan sqrt(x) dari <cmath>. Uji keduanya dengan dua blok try-catch terpisah.",
            "Bentuk what(): const char* what() const noexcept override { return pesan.c_str(); }. Solusi contoh mencetak 5 dari bagi(10, 2), lalu Error: Tidak bisa membagi dengan nol!, lalu Error khusus: Tidak bisa akar dari bilangan negatif!",
        ],
        "solution": """#include <iostream>
#include <stdexcept>
#include <cmath>
using namespace std;

class NilaiNegatifException : public exception {
private:
    string pesan;
public:
    NilaiNegatifException(string p) : pesan(p) {}
    const char* what() const noexcept override {
        return pesan.c_str();
    }
};

double bagi(double a, double b) {
    if (b == 0) {
        throw runtime_error("Tidak bisa membagi dengan nol!");
    }
    return a / b;
}

double akarKuadrat(double x) {
    if (x < 0) {
        throw NilaiNegatifException("Tidak bisa akar dari bilangan negatif!");
    }
    return sqrt(x);
}

int main() {
    try {
        cout << bagi(10, 2) << endl;
        cout << bagi(10, 0) << endl;
    } catch (const runtime_error &e) {
        cout << "Error: " << e.what() << endl;
    }

    try {
        cout << akarKuadrat(-9) << endl;
    } catch (const NilaiNegatifException &e) {
        cout << "Error khusus: " << e.what() << endl;
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 15: Smart Pointer untuk Manajemen Objek",
        "difficulty": "Sulit",
        "question": [
            "Buat class Karyawan (nama, gaji) dengan constructor &",
            "destructor yang mencetak pesan. Gunakan vector<unique_ptr<Karyawan>>",
            "untuk menyimpan 3 karyawan, TANPA new/delete manual. Tampilkan",
            "total gaji semua karyawan menggunakan loop atas vector tersebut.",
        ],
        "hints": [
            "Baca materi \"Smart Pointer: unique_ptr & shared_ptr\": unique_ptr menghapus objeknya sendiri saat ia hilang, jadi kamu nggak perlu menulis delete.",
            "Constructor Karyawan mencetak pesan ditambahkan, destructor mencetak pesan dibersihkan. Buat objeknya dengan make_unique<Karyawan>(nama, gaji) dan masukkan ke vector lewat push_back. Tiap elemen vector adalah unique_ptr, jadi akses gajinya dengan ->.",
            "Total 18000000 tercetak sebagai 1.8e+07 kalau dibiarkan, jadi pasang cout << fixed << setprecision(0); dari <iomanip> di awal main. Pesan Karyawan Andi dibersihkan. dan seterusnya muncul sendiri di akhir main, saat vector-nya dihancurkan.",
        ],
        "solution": """#include <iostream>
#include <iomanip>
#include <vector>
#include <memory>
#include <string>
using namespace std;

class Karyawan {
public:
    string nama;
    double gaji;
    Karyawan(string n, double g) : nama(n), gaji(g) {
        cout << "Karyawan " << nama << " ditambahkan." << endl;
    }
    ~Karyawan() {
        cout << "Karyawan " << nama << " dibersihkan." << endl;
    }
};

int main() {
    cout << fixed << setprecision(0);   // hindari notasi ilmiah (mis. 1.8e+07)

    vector<unique_ptr<Karyawan>> daftar;
    daftar.push_back(make_unique<Karyawan>("Andi", 5000000));
    daftar.push_back(make_unique<Karyawan>("Budi", 6000000));
    daftar.push_back(make_unique<Karyawan>("Citra", 7000000));

    double total = 0;
    for (const auto &k : daftar) {
        total += k->gaji;
    }
    cout << "Total gaji: " << total << endl;

    return 0;
}   // SEMUA unique_ptr otomatis membersihkan objeknya di sini, tanpa delete manual!""",
    },
    {
        "title": "Latihan 16: Sistem Inventori dengan STL Lengkap",
        "difficulty": "Sulit",
        "question": [
            "Buat class Produk (nama, harga, stok). Simpan beberapa produk",
            "dalam vector<Produk>. Menggunakan <algorithm>:",
            "  1. Urutkan produk berdasarkan harga TERTINGGI ke terendah.",
            "  2. Hitung total nilai inventori (harga * stok semua produk)",
            "     dengan accumulate + lambda.",
            "  3. Cari produk dengan stok < 10 menggunakan find_if.",
        ],
        "hints": [
            "Baca materi \"STL: Algorithm Library\" dan \"Lambda Expression & Fitur Modern C++\": sort, accumulate, dan find_if bisa menerima lambda sebagai aturan buatanmu sendiri.",
            "sort dengan lambda pembanding yang bernilai true kalau harga a lebih besar dari harga b. Total nilai adalah jumlah harga * stok tiap produk; kalau pakai accumulate, ia butuh lambda karena elemennya Produk, bukan angka. find_if dengan lambda stok < 10 mengembalikan iterator, jadi cek dulu iteratornya != end() sebelum dipakai.",
            "Data solusi contoh: Laptop 7500000 stok 5, Mouse 150000 stok 50, Keyboard 350000 stok 8, Monitor 2000000 stok 15. Pasang cout << fixed << setprecision(0); supaya harga besar nggak tercetak dalam notasi ilmiah. Format: Laptop: 7500000, Total nilai inventori: 77800000, Stok menipis: Laptop (stok: 5).",
        ],
        "solution": """#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

class Produk {
public:
    string nama;
    double harga;
    int stok;
    Produk(string n, double h, int s) : nama(n), harga(h), stok(s) {}
};

int main() {
    cout << fixed << setprecision(0);   // hindari notasi ilmiah untuk angka besar

    vector<Produk> produk = {
        Produk("Laptop", 7500000, 5),
        Produk("Mouse", 150000, 50),
        Produk("Keyboard", 350000, 8),
        Produk("Monitor", 2000000, 15)
    };

    // 1. Urutkan berdasarkan harga tertinggi
    sort(produk.begin(), produk.end(), [](const Produk &a, const Produk &b) {
        return a.harga > b.harga;
    });
    for (const auto &p : produk) {
        cout << p.nama << ": " << p.harga << endl;
    }

    // 2. Total nilai inventori (harga * stok)
    double totalNilai = 0;
    for (const auto &p : produk) {
        totalNilai += p.harga * p.stok;
    }
    cout << "Total nilai inventori: " << totalNilai << endl;

    // 3. Cari produk dengan stok < 10
    auto it = find_if(produk.begin(), produk.end(), [](const Produk &p) {
        return p.stok < 10;
    });
    if (it != produk.end()) {
        cout << "Stok menipis: " << it->nama << " (stok: " << it->stok << ")" << endl;
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 17: Linked List Modern dengan Smart Pointer",
        "difficulty": "Sulit",
        "question": [
            "Implementasikan ulang linked list (seperti materi C) TAPI",
            "dengan gaya C++ modern: pakai unique_ptr<Node> untuk 'next',",
            "sehingga TIDAK PERLU fungsi bebasSemua/free manual sama sekali -",
            "memori otomatis terbebaskan lewat chain unique_ptr.",
        ],
        "hints": [
            "Baca materi \"Smart Pointer: unique_ptr & shared_ptr\" dan \"RAII & Move Semantics (Lanjutan)\": unique_ptr nggak bisa disalin, cuma bisa dipindah dengan std::move.",
            "Node berisi data dan unique_ptr<Node> next. LinkedList memegang unique_ptr<Node> head. Menambah di awal: buat node baru, pindahkan head lama ke next milik node baru, lalu pindahkan node baru ke head. Destructor nggak perlu ditulis: saat head hilang, seluruh rantai ikut terhapus.",
            "Untuk menampilkan, telusuri dengan pointer mentah yang cuma meminjam: Node *current = head.get(); lalu maju dengan current = current->next.get(). Keluaran solusi contoh: 10 -> 20 -> 30 -> NULL.",
        ],
        "solution": """#include <iostream>
#include <memory>
using namespace std;

struct Node {
    int data;
    unique_ptr<Node> next;
    Node(int d) : data(d), next(nullptr) {}
};

class LinkedList {
private:
    unique_ptr<Node> head;
public:
    void tambahDiAwal(int nilai) {
        auto baru = make_unique<Node>(nilai);
        baru->next = move(head);     // pindahkan kepemilikan head lama ke baru->next
        head = move(baru);           // head sekarang memiliki node baru
    }

    void tampilkan() const {
        Node *current = head.get();   // raw pointer HANYA untuk 'meminjam', tidak memiliki
        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next.get();
        }
        cout << "NULL" << endl;
    }
};   // Destructor otomatis (implicit) membersihkan SELURUH chain unique_ptr!

int main() {
    LinkedList list;
    list.tambahDiAwal(30);
    list.tambahDiAwal(20);
    list.tambahDiAwal(10);

    list.tampilkan();   // 10 -> 20 -> 30 -> NULL

    return 0;
    // TIDAK ADA delete/free manual - semua node otomatis dibersihkan
    // secara berantai saat objek 'list' keluar scope di akhir main().
}""",
    },
    {
        "title": "Latihan 18: Sistem Manajemen Mahasiswa Lengkap (OOP + STL + Exception)",
        "difficulty": "Sulit",
        "question": [
            "Gabungkan semua konsep: buat class Mahasiswa (nim, nama, ipk)",
            "dan class ManajemenMahasiswa yang menyimpan vector<Mahasiswa>",
            "dengan method:",
            "  1. tambah(Mahasiswa m) - tambah data baru",
            "  2. cariByNim(int nim) - throw exception jika tidak ditemukan",
            "  3. rataRataIpk() - hitung rata-rata IPK semua mahasiswa",
            "  4. topMahasiswa() - kembalikan mahasiswa dengan IPK tertinggi",
        ],
        "hints": [
            "Ini gabungan materi \"Exception Handling\", \"STL: Algorithm Library\", dan \"Lambda Expression & Fitur Modern C++\". Bikin class Mahasiswa dulu, lalu tambahkan method ManajemenMahasiswa satu per satu.",
            "cariByNim: find_if dengan lambda yang menangkap nim; kalau iteratornya sama dengan end(), throw runtime_error. rataRataIpk: accumulate dengan nilai awal 0.0 dan lambda yang menambahkan ipk tiap mahasiswa, karena ipk ada di dalam objek. topMahasiswa: max_element dengan lambda yang membandingkan ipk.",
            "Data solusi contoh: (101, Andi, 3.5), (102, Budi, 3.9), (103, Citra, 3.2), lalu cari NIM 999. Keluarannya: Rata-rata IPK: 3.53333, Top mahasiswa: Budi (IPK 3.9), dan Error: Mahasiswa dengan NIM 999 tidak ditemukan! (pesannya disusun dengan to_string(nim)).",
        ],
        "solution": """#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <numeric>
#include <string>
using namespace std;

class Mahasiswa {
public:
    int nim;
    string nama;
    double ipk;
    Mahasiswa(int n, string nm, double i) : nim(n), nama(nm), ipk(i) {}
};

class ManajemenMahasiswa {
private:
    vector<Mahasiswa> daftar;
public:
    void tambah(const Mahasiswa &m) {
        daftar.push_back(m);
    }

    Mahasiswa cariByNim(int nim) {
        auto it = find_if(daftar.begin(), daftar.end(),
            [nim](const Mahasiswa &m) { return m.nim == nim; });
        if (it == daftar.end()) {
            throw runtime_error("Mahasiswa dengan NIM " + to_string(nim) + " tidak ditemukan!");
        }
        return *it;
    }

    double rataRataIpk() const {
        if (daftar.empty()) return 0.0;
        double total = accumulate(daftar.begin(), daftar.end(), 0.0,
            [](double acc, const Mahasiswa &m) { return acc + m.ipk; });
        return total / daftar.size();
    }

    Mahasiswa topMahasiswa() const {
        return *max_element(daftar.begin(), daftar.end(),
            [](const Mahasiswa &a, const Mahasiswa &b) { return a.ipk < b.ipk; });
    }
};

int main() {
    ManajemenMahasiswa manajemen;
    manajemen.tambah(Mahasiswa(101, "Andi", 3.5));
    manajemen.tambah(Mahasiswa(102, "Budi", 3.9));
    manajemen.tambah(Mahasiswa(103, "Citra", 3.2));

    cout << "Rata-rata IPK: " << manajemen.rataRataIpk() << endl;

    Mahasiswa top = manajemen.topMahasiswa();
    cout << "Top mahasiswa: " << top.nama << " (IPK " << top.ipk << ")" << endl;

    try {
        manajemen.cariByNim(999);
    } catch (const runtime_error &e) {
        cout << "Error: " << e.what() << endl;
    }
    return 0;
}""",
    },
    {
        'title': 'Proyek Akhir: Kalkulator Ekspresi',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Kalkulator Ekspresi',
        '',
        'Tulis kalkulator yang menerima ekspresi sebagai TEKS dan menghitungnya',
        'sendiri -- tanpa memanggil apa pun yang sudah bisa mengevaluasi string.',
        '',
        'Ini proyek yang menguji rekursi dan kepemilikan memori sekaligus.',
        "Ekspresi dipecah jadi POHON: '2 + 3 * 4' harus jadi",
        '(2 + (3 * 4)), bukan ((2 + 3) * 4), dan pohon itulah yang dihitung.',
        '',
        'Tujuh ekspresi diuji, tiga di antaranya memang salah dan harus',
        'melaporkan galat tanpa membuat program berhenti.',
        '',
        'Yang harus ada di programmu:',
        '  1. Tata bahasa tiga tingkat, masing-masing satu fungsi:',
        "       ekspresi := suku (('+' | '-') suku)*",
        "       suku     := faktor (('*' | '/') faktor)*",
        "       faktor   := angka | '(' ekspresi ')' | '-' faktor",
        '     Tingkatan inilah yang membuat * lebih kuat daripada +.',
        '  2. Simpul pohon sebagai class abstrak dengan method virtual murni',
        '     nilai() dan tulis(); Angka dan Operasi menurunkannya.',
        '  3. Kepemilikan pakai std::unique_ptr -- tidak ada delete manual.',
        '  4. class turunan std::runtime_error sendiri untuk galat sintaks.',
        '  5. Pembagian dengan nol dan sisa karakter tak terbaca juga galat.',
        '  6. Nilai dihitung SEBELUM baris dicetak, supaya pesan galat tidak',
        '     muncul menggantung di tengah baris.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  KALKULATOR EKSPRESI',
        '  ====================================================',
        '  2 + 3 * 4           (2 + (3 * 4)) = 14',
        '  (2 + 3) * 4         ((2 + 3) * 4) = 20',
        '  10 / 4              (10 / 4) = 2.5',
        '  -5 + 2 * (3 - 1)    ((0 - 5) + (2 * (3 - 1))) = -1',
        '  8 / (3 - 3)         GALAT: pembagian dengan nol',
        '  2 + * 3             GALAT: karakter tak terduga: *',
        '  (1 + 2              GALAT: kurung tutup hilang',
        '  ----------------------------------------------------',
        '  Ekspresi diuji : 7',
    ],
        'hints': [
            "Ini recursive descent parser: tiap baris tata bahasa jadi satu fungsi, dan fungsi tingkat atas memanggil tingkat di bawahnya. Bekalnya ada di materi \"Abstract Class & Pure Virtual Function\", \"Smart Pointer: unique_ptr & shared_ptr\", dan \"Exception Handling\".",
            "ekspresi() memanggil suku(), suku() memanggil faktor(), dan faktor() memanggil ekspresi() lagi untuk isi kurung. Itu rekursinya, dan itu juga yang membuat kurung bersarang bekerja sendiri. Tanda minus di depan cukup diperlakukan sebagai 0 - faktor(), jadi nggak perlu jenis simpul baru.",
            "using Pohon = std::unique_ptr<Simpul>; lalu bentuk simpul operasi dengan std::make_unique<Operasi>(op, std::move(kiri), suku()). Hitung nilai() dulu ke variabel, baru cetak tulis() dan hasilnya, supaya galat pembagian dengan nol nggak muncul di tengah baris.",
        ],
        'solution': """// Kalkulator Ekspresi -- recursive descent parser dengan pohon sintaks.
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

class GalatSintaks : public std::runtime_error {
public:
    explicit GalatSintaks(const std::string& pesan)
        : std::runtime_error(pesan) {}
};

struct Simpul {
    virtual ~Simpul() = default;
    virtual double nilai() const = 0;
    virtual std::string tulis() const = 0;
};

using Pohon = std::unique_ptr<Simpul>;

class Angka : public Simpul {
    double a;
public:
    explicit Angka(double a) : a(a) {}
    double nilai() const override { return a; }
    std::string tulis() const override {
        std::string s = std::to_string(a);
        s.erase(s.find_last_not_of('0') + 1);
        if (!s.empty() && s.back() == '.') s.pop_back();
        return s;
    }
};

class Operasi : public Simpul {
    char op;
    Pohon kiri, kanan;
public:
    Operasi(char op, Pohon kiri, Pohon kanan)
        : op(op), kiri(std::move(kiri)), kanan(std::move(kanan)) {}
    double nilai() const override {
        double a = kiri->nilai(), b = kanan->nilai();
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/':
                if (b == 0) throw GalatSintaks("pembagian dengan nol");
                return a / b;
        }
        throw GalatSintaks(std::string("operator tak dikenal: ") + op);
    }
    std::string tulis() const override {
        return "(" + kiri->tulis() + " " + op + " " + kanan->tulis() + ")";
    }
};

class Pengurai {
    std::string teks;
    size_t i = 0;

    void lewatiSpasi() { while (i < teks.size() && teks[i] == ' ') i++; }

    // faktor := angka | '(' ekspresi ')' | '-' faktor
    Pohon faktor() {
        lewatiSpasi();
        if (i >= teks.size()) throw GalatSintaks("ekspresi terpotong");
        if (teks[i] == '-') {
            i++;
            return std::make_unique<Operasi>('-', std::make_unique<Angka>(0),
                                             faktor());
        }
        if (teks[i] == '(') {
            i++;
            Pohon d = ekspresi();
            lewatiSpasi();
            if (i >= teks.size() || teks[i] != ')')
                throw GalatSintaks("kurung tutup hilang");
            i++;
            return d;
        }
        size_t awal = i;
        while (i < teks.size() && (isdigit(teks[i]) || teks[i] == '.')) i++;
        if (awal == i)
            throw GalatSintaks(std::string("karakter tak terduga: ") + teks[i]);
        return std::make_unique<Angka>(std::stod(teks.substr(awal, i - awal)));
    }

    // suku := faktor (('*' | '/') faktor)*
    Pohon suku() {
        Pohon kiri = faktor();
        while (true) {
            lewatiSpasi();
            if (i < teks.size() && (teks[i] == '*' || teks[i] == '/')) {
                char op = teks[i++];
                kiri = std::make_unique<Operasi>(op, std::move(kiri), faktor());
            } else return kiri;
        }
    }

public:
    explicit Pengurai(std::string t) : teks(std::move(t)) {}

    // ekspresi := suku (('+' | '-') suku)*
    Pohon ekspresi() {
        Pohon kiri = suku();
        while (true) {
            lewatiSpasi();
            if (i < teks.size() && (teks[i] == '+' || teks[i] == '-')) {
                char op = teks[i++];
                kiri = std::make_unique<Operasi>(op, std::move(kiri), suku());
            } else return kiri;
        }
    }

    Pohon uraiPenuh() {
        Pohon p = ekspresi();
        lewatiSpasi();
        if (i < teks.size())
            throw GalatSintaks(std::string("sisa yang tak terbaca: ")
                               + teks.substr(i));
        return p;
    }
};

int main() {
    std::vector<std::string> uji = {
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 / 4",
        "-5 + 2 * (3 - 1)",
        "8 / (3 - 3)",
        "2 + * 3",
        "(1 + 2",
    };

    std::cout << "KALKULATOR EKSPRESI\\n";
    std::cout << "====================================================\\n";
    for (const auto& e : uji) {
        std::cout << e;
        for (size_t s = e.size(); s < 20; s++) std::cout << ' ';
        try {
            Pengurai p(e);
            Pohon pohon = p.uraiPenuh();
            // Nilai dihitung LEBIH DULU, baru dicetak bersama bentuk
            // pohonnya. Kalau dibalik, ekspresi yang gagal saat dihitung
            // (pembagian dengan nol) sudah telanjur mencetak separuh baris,
            // dan pesan galatnya muncul menggantung di tengahnya.
            double hasil = pohon->nilai();
            std::cout << pohon->tulis() << " = " << hasil << '\\n';
        } catch (const GalatSintaks& g) {
            std::cout << "GALAT: " << g.what() << '\\n';
        }
    }
    std::cout << "----------------------------------------------------\\n";
    std::cout << "Ekspresi diuji : " << uji.size() << '\\n';
    return 0;
}
""",
    },
]
