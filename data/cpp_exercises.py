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
            "Gunakan cout << ... << endl; untuk tiap baris.",
            "Jangan lupa #include <iostream> dan using namespace std;.",
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
            "int a = 15, b = 4;",
            "cout << a << \" + \" << b << \" = \" << (a+b) << endl;",
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
            "int nilai; cin >> nilai;",
            "Jangan ada cout sebelum cin -- penilaian membandingkan output.",
            "Gunakan if-else biasa.",
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
            "vector<int> genap; lalu push_back di dalam loop for jika i%2==0.",
            "Gunakan range-based for untuk mencetak & akumulasi total.",
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
            "Gunakan nested loop (for di dalam for).",
            "string(n, '*') membuat string berisi n karakter '*' berulang.",
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
            "max_element/min_element dari <algorithm> (ingat: hasilnya iterator, pakai * untuk deref).",
            "sort(v.begin(), v.end(), greater<int>()); untuk descending.",
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
            "Compiler membedakan berdasarkan jumlah & tipe parameter.",
            "double luas(double r) { ... } - beda tipe dari int luas(int sisi).",
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
            "class Rekening { private: ... public: Rekening(string p, double s) : pemilik(p), saldo(s) {} ... };",
            "tarik return true jika saldo cukup, false jika tidak.",
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
            "map<string,string> kontak; kontak[\"Andi\"] = \"0812xxxx\";",
            "for (const auto &p : kontak) { cout << p.first << \": \" << p.second; }",
            "if (kontak.count(\"Zaki\") == 0) { ... }",
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
            "virtual void bersuara() di base class, override di subclass.",
            "vector<Hewan*> daftar = { new Kucing(...), new Anjing(...) };",
            "Jangan lupa virtual destructor & delete tiap elemen di akhir.",
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
            "virtual double luas() = 0; virtual double keliling() = 0;",
            "Lingkaran butuh nilai PI (bisa const double PI = 3.14159;).",
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
            "Vector2D operator+(const Vector2D &lain) const { return Vector2D(x+lain.x, y+lain.y); }",
            "friend ostream& operator<<(ostream &os, const Vector2D &v) {...}",
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
            "template <typename T> T cariMax(vector<T> data) { ... }",
            "template <typename T> class StackSederhana { private: vector<T> data; public: ... };",
            "pop(): ambil data.back(), lalu data.pop_back().",
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
            "#include <stdexcept> untuk runtime_error.",
            "class NilaiNegatifException : public exception { ... const char* what() const noexcept override {...} };",
            "#include <cmath> untuk sqrt().",
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
            "vector<unique_ptr<Karyawan>> daftar;",
            "daftar.push_back(make_unique<Karyawan>(\"Andi\", 5000000));",
            "Akses lewat -> karena elemen vector adalah unique_ptr.",
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
            "sort(v.begin(), v.end(), [](const Produk &a, const Produk &b){ return a.harga > b.harga; });",
            "accumulate butuh lambda sebagai operator kustom untuk tipe non-angka langsung.",
            "find_if(v.begin(), v.end(), [](const Produk &p){ return p.stok < 10; });",
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
            "struct Node { int data; unique_ptr<Node> next; Node(int d): data(d), next(nullptr) {} };",
            "head adalah unique_ptr<Node> juga; tambahDiAwal butuh std::move(head).",
            "tampilkan() bisa pakai raw pointer sementara (Node*) untuk iterasi tanpa memindah kepemilikan.",
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
            "cariByNim: gunakan find_if, jika iterator == end() maka throw runtime_error.",
            "rataRataIpk: accumulate dengan lambda karena field ipk ada di dalam objek.",
            "topMahasiswa: max_element dengan lambda comparator.",
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
]
