C_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program yang menampilkan:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar C.",
            "",
            "Tulis PERSIS seperti di atas, termasuk nama Andi -- penilaian",
            "membandingkan outputmu huruf demi huruf.",
        ],
        "hints": [
            "Baca ulang materi \"Input & Output (printf & scanf)\": tiap baris keluaran cukup dicetak dengan satu printf().",
            "Kerangkanya: #include <stdio.h>, fungsi int main(void), dua printf, lalu return 0; di akhir main. Akhiri tiap teks dengan \\n supaya pindah baris.",
        ],
        "solution": """#include <stdio.h>

int main(void) {
    printf("Halo, namaku Andi!\\n");
    printf("Aku sedang belajar C.\\n");
    return 0;
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
            "Lihat materi \"Operator\": ada lima operator aritmetika (+ - * / %), dan pembagian int dengan int membuang sisa di belakang koma.",
            "Pakai a = 15 dan b = 4 supaya keluaranmu cocok dengan penilai. Cetak satu baris per operasi dengan %d, formatnya seperti 15 + 4 = 19.",
            "Untuk mencetak tanda % lewat printf, tulis %% di format string. Baris sisa bagi jadinya berbentuk \"%d %% %d = %d\\n\".",
        ],
        "solution": """#include <stdio.h>

int main(void) {
    int a = 15, b = 4;

    printf("%d + %d = %d\\n", a, b, a + b);
    printf("%d - %d = %d\\n", a, b, a - b);
    printf("%d * %d = %d\\n", a, b, a * b);
    printf("%d / %d = %d\\n", a, b, a / b);
    printf("%d %% %d = %d\\n", a, b, a % b);   // %% untuk cetak karakter %
    return 0;
}""",
    },
    {
        "title": "Latihan 3: Cek Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Buat program: baca satu angka nilai dari input dengan scanf,",
            "jika nilai >= 75 tampilkan 'Lulus', selain itu 'Tidak Lulus'.",
            "",
            "Jangan cetak teks ajakan apa pun. Program hanya boleh mengeluarkan",
            "satu baris berisi Lulus atau Tidak Lulus.",
        ],
        "hints": [
            "Bekalnya materi \"Input & Output (printf & scanf)\" untuk membaca angka dan \"Percabangan (if / else / switch)\" untuk memilih satu dari dua kalimat.",
            "Baca nilai dengan scanf dan %d, jangan lupa & di depan nama variabel. Jangan ada printf sebelum scanf: penilai membandingkan seluruh keluaran, jadi teks ajakan seperti \"Masukkan nilai:\" bikin jawabanmu dianggap salah.",
            "Satu if-else cukup: kalau nilai >= 75 cetak Lulus, selain itu cetak Tidak Lulus, masing-masing diakhiri \\n.",
        ],
        # Dua input supaya KEDUA cabang benar-benar diuji. Dengan satu input
        # saja, program yang cuma menulis printf("Lulus") ikut dinyatakan benar.
        "stdin_list": ["80\n", "60\n"],
        "solution": """#include <stdio.h>

int main(void) {
    int nilai;

    scanf("%d", &nilai);

    if (nilai >= 75) {
        printf("Lulus\\n");
    } else {
        printf("Tidak Lulus\\n");
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 4: Deret Angka Genap",
        "difficulty": "Menengah",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20",
            "beserta total jumlahnya.",
        ],
        "hints": [
            "Baca materi \"Perulangan (for, while, do-while)\" dan operator sisa bagi di \"Operator\". Angka genap adalah angka yang sisa baginya dengan 2 sama dengan 0.",
            "Siapkan variabel total yang mulai dari 0. Ulangi dari 1 sampai 20; kalau angkanya genap, cetak angka itu diikuti satu spasi lalu tambahkan ke total. Sesudah loop, pindah baris dan cetak Total: diikuti jumlahnya.",
            "Pengecekan genapnya: if (i % 2 == 0) di dalam for.",
        ],
        "solution": """#include <stdio.h>

int main(void) {
    int total = 0;
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) {
            printf("%d ", i);
            total += i;
        }
    }
    printf("\\nTotal: %d\\n", total);
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
            "Ini soal nested loop (loop di dalam loop) dari materi \"Perulangan (for, while, do-while)\". Loop luar mengatur baris, loop dalam mengatur banyak bintang di baris itu.",
            "Baris ke-i berisi i bintang. Di loop dalam cetak satu * tanpa \\n; begitu loop dalam selesai, cetak \\n untuk pindah baris.",
            "Batas loop dalam ikut loop luar: for (int j = 1; j <= i; j++).",
        ],
        "solution": """#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\\n");
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 6: Nilai Terbesar & Terkecil dalam Array",
        "difficulty": "Menengah",
        "question": [
            "Buat program untuk mencari nilai terbesar dan terkecil",
            "dari array berikut:",
            "int data[] = {23, 5, 87, 12, 55, 99, 31};",
        ],
        "hints": [
            "Materi \"Array\" membahas cara menelusuri array dengan for dan menghitung jumlah elemennya.",
            "Anggap elemen pertama sebagai nilai terbesar sekaligus terkecil sementara. Telusuri mulai indeks 1, dan perbarui keduanya tiap ketemu nilai yang lebih besar atau lebih kecil. Cetak Terbesar: lalu Terkecil:, masing-masing satu baris.",
            "Jumlah elemen bisa dihitung dengan sizeof(data) / sizeof(data[0]), jadi kamu nggak perlu menulis angka 7 sendiri.",
        ],
        "solution": """#include <stdio.h>

int main(void) {
    int data[] = {23, 5, 87, 12, 55, 99, 31};
    int n = sizeof(data) / sizeof(data[0]);

    int max = data[0];
    int min = data[0];

    for (int i = 1; i < n; i++) {
        if (data[i] > max) max = data[i];
        if (data[i] < min) min = data[i];
    }

    printf("Terbesar: %d\\n", max);
    printf("Terkecil: %d\\n", min);
    return 0;
}""",
    },
    {
        "title": "Latihan 7: Function Hitung Luas",
        "difficulty": "Menengah",
        "question": [
            "Buat 3 fungsi:",
            "  1. luasPersegi(int sisi)          -> sisi * sisi",
            "  2. luasPersegiPanjang(int p, int l) -> p * l",
            "  3. luasLingkaran(double r)         -> 3.14159 * r * r",
            "Panggil ketiganya di main dan tampilkan hasilnya.",
        ],
        "hints": [
            "Baca materi \"Function (Fungsi)\", terutama bagian prototype: deklarasi fungsi di atas main(), definisi lengkapnya di bawah.",
            "Dua fungsi pertama mengembalikan int, luasLingkaran mengembalikan double. Panggil dengan sisi 5, persegi panjang 4 x 6, dan jari-jari 7. Luas lingkaran dicetak dengan dua angka di belakang koma (%.2f).",
            "Format keluaran yang dinilai: Persegi (5): 25, lalu Persegi Panjang (4x6): 24, lalu Lingkaran (r=7): 153.94, masing-masing satu baris.",
        ],
        "solution": """#include <stdio.h>

int luasPersegi(int sisi);
int luasPersegiPanjang(int p, int l);
double luasLingkaran(double r);

int main(void) {
    printf("Persegi (5): %d\\n", luasPersegi(5));
    printf("Persegi Panjang (4x6): %d\\n", luasPersegiPanjang(4, 6));
    printf("Lingkaran (r=7): %.2f\\n", luasLingkaran(7));
    return 0;
}

int luasPersegi(int sisi) {
    return sisi * sisi;
}

int luasPersegiPanjang(int p, int l) {
    return p * l;
}

double luasLingkaran(double r) {
    return 3.14159 * r * r;
}""",
    },
    {
        "title": "Latihan 8: Manipulasi String Manual",
        "difficulty": "Menengah",
        "question": [
            "Buat fungsi panjangString(char s[]) yang menghitung panjang",
            "string TANPA memakai strlen() (loop manual sampai ketemu '\\0').",
            "Buat juga fungsi balikString(char s[]) yang membalik isi",
            "string tersebut secara in-place (mengubah array aslinya).",
        ],
        "hints": [
            "Materi \"String (Array of Char)\" menjelaskan bahwa string C diakhiri karakter '\\0'. Panjang string adalah banyaknya karakter sebelum tanda itu.",
            "panjangString: mulai dari indeks 0 dan maju terus selama karakternya belum '\\0'. balikString: tukar karakter pertama dengan terakhir, kedua dengan kedua dari belakang, dan berhenti di tengah (n / 2).",
            "Pasangan indeks i adalah n - 1 - i; simpan s[i] di variabel sementara sebelum menimpanya. Solusi contoh memakai kata \"Belajar\" dan mencetak Panjang: 7 lalu Dibalik: rajaleB.",
        ],
        "solution": """#include <stdio.h>

int panjangString(char s[]) {
    int i = 0;
    while (s[i] != '\\0') {
        i++;
    }
    return i;
}

void balikString(char s[]) {
    int n = panjangString(s);
    for (int i = 0; i < n / 2; i++) {
        char temp = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = temp;
    }
}

int main(void) {
    char kata[] = "Belajar";
    printf("Panjang: %d\\n", panjangString(kata));

    balikString(kata);
    printf("Dibalik: %s\\n", kata);   // ralajeB
    return 0;
}""",
    },
    {
        "title": "Latihan 9: Struct Mahasiswa & Array of Struct",
        "difficulty": "Menengah",
        "question": [
            "Buat struct Mahasiswa (nama[50], umur, ipk).",
            "Buat array of struct berisi 3 mahasiswa dengan data bebas.",
            "Tampilkan semua data, lalu hitung & tampilkan rata-rata IPK.",
        ],
        "hints": [
            "Baca materi \"Struct\": typedef struct membuat tipe baru, dan field diakses dengan tanda titik.",
            "Isi array tiga elemen langsung saat deklarasi dengan kurung kurawal bersarang, satu pasang kurung per mahasiswa. Lalu pakai satu loop untuk mencetak tiap mahasiswa sekaligus menjumlahkan IPK-nya; rata-ratanya total dibagi 3.",
            "Data yang dipakai penilai: Andi 20 tahun IPK 3.5, Budi 22 tahun IPK 3.2, Citra 21 tahun IPK 3.8. Formatnya Andi, 20 tahun, IPK 3.50 (IPK pakai %.2f), dan baris terakhir Rata-rata IPK: 3.50.",
        ],
        "solution": """#include <stdio.h>

typedef struct {
    char nama[50];
    int umur;
    double ipk;
} Mahasiswa;

int main(void) {
    Mahasiswa daftar[3] = {
        {"Andi", 20, 3.5},
        {"Budi", 22, 3.2},
        {"Citra", 21, 3.8}
    };

    double totalIpk = 0;
    for (int i = 0; i < 3; i++) {
        printf("%s, %d tahun, IPK %.2f\\n",
               daftar[i].nama, daftar[i].umur, daftar[i].ipk);
        totalIpk += daftar[i].ipk;
    }

    printf("Rata-rata IPK: %.2f\\n", totalIpk / 3);
    return 0;
}""",
    },
    {
        "title": "Latihan 10: Pointer & Fungsi Tukar (Swap)",
        "difficulty": "Lanjut",
        "question": [
            "Buat fungsi tukar(int *a, int *b) yang menukar nilai dua",
            "variabel int memakai pointer. Buat juga fungsi",
            "urutkanTiga(int *a, int *b, int *c) yang mengurutkan tiga",
            "variabel dari kecil ke besar (memakai tukar() di dalamnya).",
        ],
        "hints": [
            "Baca materi \"Pointer Dasar\": fungsi yang menerima alamat variabel (parameter pointer) bisa mengubah variabel milik pemanggil lewat dereference.",
            "tukar butuh satu variabel sementara. urutkanTiga cukup tiga perbandingan: a dengan b, b dengan c, lalu a dengan b lagi, dan tukar kalau urutannya terbalik. Ini bubble sort untuk tiga elemen.",
            "Di dalam urutkanTiga, a dan b sudah berupa pointer, jadi panggil tukar(a, b) tanpa &. Solusi contoh memakai x = 30, y = 10, z = 20 dan mencetak Sebelum: 30 10 20 lalu Sesudah: 10 20 30.",
        ],
        "solution": """#include <stdio.h>

void tukar(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void urutkanTiga(int *a, int *b, int *c) {
    if (*a > *b) tukar(a, b);
    if (*b > *c) tukar(b, c);
    if (*a > *b) tukar(a, b);
}

int main(void) {
    int x = 30, y = 10, z = 20;

    printf("Sebelum: %d %d %d\\n", x, y, z);
    urutkanTiga(&x, &y, &z);
    printf("Sesudah: %d %d %d\\n", x, y, z);   // 10 20 30
    return 0;
}""",
    },
    {
        "title": "Latihan 11: Dynamic Array dengan Malloc",
        "difficulty": "Lanjut",
        "question": [
            "Buat program yang membaca jumlah data (n) dari input, lalu",
            "meng-alokasikan array int secara dinamis dengan malloc()",
            "sebesar n. Isi array dengan angka kelipatan 5 (5, 10, 15, ...),",
            "tampilkan semua isinya, lalu bebaskan (free) memorinya.",
            "",
            "Jangan cetak teks ajakan. Untuk input 5, outputnya:",
            "  Isi array: 5 10 15 20 25",
        ],
        "hints": [
            "Baca materi \"Dynamic Memory Allocation (malloc, calloc, free)\": ukuran yang diminta adalah n kali ukuran satu int, dan hasil malloc selalu dicek sebelum dipakai.",
            "Langkahnya: baca n tanpa teks ajakan, alokasikan, cek apakah hasilnya NULL, isi elemen ke-i dengan (i + 1) * 5, cetak Isi array: diikuti angka-angkanya (tiap angka diikuti spasi), lalu free.",
            "Alokasinya: int *arr = malloc(n * sizeof(int)); Kalau arr == NULL, cetak pesan lalu return 1. Sesudah free(arr), isi arr = NULL supaya nggak jadi dangling pointer.",
        ],
        # Tanpa stdin, scanf gagal dan n tetap tak terinisialisasi: kunci
        # jawabannya jadi "Isi array:" kosong dan seluruh materi malloc,
        # perulangan, serta free tidak pernah diuji sama sekali.
        "stdin_list": ["5\n", "1\n"],
        "solution": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int *arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Alokasi memori gagal!\\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = (i + 1) * 5;
    }

    printf("Isi array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\\n");

    free(arr);
    arr = NULL;
    return 0;
}""",
    },
    {
        "title": "Latihan 12: Rekening Bank dengan Struct & Pointer",
        "difficulty": "Lanjut",
        "question": [
            "Buat struct Rekening (nomor[20], saldo).",
            "Buat fungsi setor(Rekening *r, double jumlah) dan",
            "tarik(Rekening *r, double jumlah) yang mengembalikan int",
            "(1 jika berhasil, 0 jika saldo tidak cukup untuk tarik).",
            "Semua fungsi harus MENGUBAH struct asli lewat pointer.",
        ],
        "hints": [
            "Baca materi \"Struct\", bagian pointer ke struct: lewat pointer, field diubah dengan operator panah (->), dan perubahannya mengenai struct aslinya.",
            "setor menambah saldo kalau jumlahnya positif. tarik cuma mengurangi saldo kalau jumlahnya positif dan nggak melebihi saldo; kembalikan 1 kalau berhasil, 0 kalau nggak. Panggil keduanya dengan &r.",
            "Skenario solusi contoh: nomor 12345 (isi dengan strcpy), saldo awal 100000, setor 50000, tarik 20000, lalu tarik 999999. Saldo dicetak dengan %.2f: Saldo setelah setor: 150000.00, lalu Tarik 20000 berhasil? 1, saldo: 130000.00, dan seterusnya.",
        ],
        "solution": """#include <stdio.h>
#include <string.h>

typedef struct {
    char nomor[20];
    double saldo;
} Rekening;

void setor(Rekening *r, double jumlah) {
    if (jumlah > 0) {
        r->saldo += jumlah;
    }
}

int tarik(Rekening *r, double jumlah) {
    if (jumlah > 0 && jumlah <= r->saldo) {
        r->saldo -= jumlah;
        return 1;
    }
    return 0;
}

int main(void) {
    Rekening r;
    strcpy(r.nomor, "12345");
    r.saldo = 100000;

    setor(&r, 50000);
    printf("Saldo setelah setor: %.2f\\n", r.saldo);

    int berhasil = tarik(&r, 20000);
    printf("Tarik 20000 berhasil? %d, saldo: %.2f\\n", berhasil, r.saldo);

    berhasil = tarik(&r, 999999);
    printf("Tarik 999999 berhasil? %d, saldo: %.2f\\n", berhasil, r.saldo);
    return 0;
}""",
    },
    {
        "title": "Latihan 13: Function Pointer sebagai Callback",
        "difficulty": "Lanjut",
        "question": [
            "Buat 3 fungsi operasi (tambah, kurang, kali) bertipe",
            "int(int, int). Buat fungsi prosesArray(int arr[], int n,",
            "int (*operasi)(int, int)) yang menerapkan operasi tersebut",
            "SECARA BERURUTAN (akumulasi) ke semua elemen array.",
            "Uji dengan array {1,2,3,4,5} untuk ketiga operasi.",
        ],
        "hints": [
            "Baca materi \"Function Pointer\": parameter bertipe pointer ke fungsi bisa diisi nama fungsi apa pun yang bentuknya sama, di sini int(int, int).",
            "Mulai hasil dari elemen pertama, lalu untuk tiap elemen berikutnya hitung hasil = operasi(hasil, elemen). Panggil prosesArray tiga kali dengan tambah, kurang, dan kali, ditulis tanpa tanda kurung.",
            "Keluaran solusi contoh: Total (tambah): 15, Hasil kurang berurutan: -13, dan Hasil kali (faktorial 5): 120, masing-masing satu baris.",
        ],
        "solution": """#include <stdio.h>

int tambah(int a, int b) { return a + b; }
int kurang(int a, int b) { return a - b; }
int kali(int a, int b)   { return a * b; }

int prosesArray(int arr[], int n, int (*operasi)(int, int)) {
    int hasil = arr[0];
    for (int i = 1; i < n; i++) {
        hasil = operasi(hasil, arr[i]);
    }
    return hasil;
}

int main(void) {
    int data[] = {1, 2, 3, 4, 5};
    int n = 5;

    printf("Total (tambah): %d\\n", prosesArray(data, n, tambah));
    printf("Hasil kurang berurutan: %d\\n", prosesArray(data, n, kurang));
    printf("Hasil kali (faktorial 5): %d\\n", prosesArray(data, n, kali));
    return 0;
}""",
    },
    {
        "title": "Latihan 14: Membaca & Menulis File Nilai Mahasiswa",
        "difficulty": "Lanjut",
        "question": [
            "Buat program yang menulis 3 baris data (nama dan nilai,",
            "dipisah spasi) ke file 'nilai.txt' dengan fprintf(). Lalu",
            "baca kembali file tersebut baris per baris dengan fgets()",
            "dan tampilkan ke layar.",
        ],
        "hints": [
            "Baca materi \"File I/O\": fopen dengan mode \"w\" untuk menulis dan \"r\" untuk membaca, dan hasilnya selalu dicek terhadap NULL.",
            "Tulis tiga baris dengan fprintf, tutup berkasnya dengan fclose, lalu buka lagi untuk dibaca. Baca dengan fgets di dalam while sampai fgets mengembalikan NULL, dan cetak tiap baris apa adanya; baris dari fgets sudah membawa \\n sendiri.",
            "Data solusi contoh: Andi 85, Budi 70, Citra 92. Sebelum isinya dicetak, ada satu baris judul: Isi file nilai.txt:",
        ],
        "solution": """#include <stdio.h>

int main(void) {
    FILE *fp = fopen("nilai.txt", "w");
    if (fp == NULL) {
        printf("Gagal membuka file!\\n");
        return 1;
    }

    fprintf(fp, "Andi 85\\n");
    fprintf(fp, "Budi 70\\n");
    fprintf(fp, "Citra 92\\n");
    fclose(fp);

    FILE *fp2 = fopen("nilai.txt", "r");
    if (fp2 == NULL) {
        printf("Gagal membuka file untuk membaca!\\n");
        return 1;
    }

    char baris[100];
    printf("Isi file nilai.txt:\\n");
    while (fgets(baris, sizeof(baris), fp2) != NULL) {
        printf("%s", baris);
    }
    fclose(fp2);
    return 0;
}""",
    },
    {
        "title": "Latihan 15: Implementasi Stack dengan Array",
        "difficulty": "Sulit",
        "question": [
            "Implementasikan struktur data STACK (LIFO - Last In First Out)",
            "menggunakan array, dengan fungsi:",
            "  1. push(int nilai)  -> tambah elemen ke puncak stack",
            "  2. pop()            -> hapus & kembalikan elemen puncak",
            "  3. isEmpty()        -> cek apakah stack kosong",
            "Gunakan variabel global 'top' untuk melacak posisi puncak.",
        ],
        "hints": [
            "Stack itu LIFO: yang terakhir masuk, pertama keluar. Bekalnya materi \"Array\" dan \"Lingkup, Masa Hidup & Kelas Penyimpanan Variabel\" (untuk variabel global).",
            "Pakai array global dan variabel top yang mulai dari -1, artinya kosong. push menaikkan top dulu baru menyimpan; pop mengambil elemen di top baru menurunkannya. Cek kosong sebelum pop dan cek penuh sebelum push.",
            "isEmpty cukup mengembalikan top == -1. Solusi contoh push 10, 20, 30, lalu pop tiga kali (Pop: 30, Pop: 20, Pop: 10) dan terakhir mencetak Stack kosong? 1.",
        ],
        "solution": """#include <stdio.h>

#define MAX 100

int stack[MAX];
int top = -1;   // -1 menandakan stack kosong

int isEmpty(void) {
    return top == -1;
}

void push(int nilai) {
    if (top >= MAX - 1) {
        printf("Stack penuh!\\n");
        return;
    }
    stack[++top] = nilai;
}

int pop(void) {
    if (isEmpty()) {
        printf("Stack kosong!\\n");
        return -1;
    }
    return stack[top--];
}

int main(void) {
    push(10);
    push(20);
    push(30);

    printf("Pop: %d\\n", pop());   // 30 (elemen TERAKHIR masuk, PERTAMA keluar)
    printf("Pop: %d\\n", pop());   // 20
    printf("Pop: %d\\n", pop());   // 10
    printf("Stack kosong? %d\\n", isEmpty());   // 1 (true)

    return 0;
}""",
    },
    {
        "title": "Latihan 16: Linked List - Insert, Delete & Search",
        "difficulty": "Sulit",
        "question": [
            "Perluas linked list dari materi 18 dengan menambah fungsi:",
            "  1. cariNode(Node *head, int nilai) -> kembalikan 1 jika",
            "     ditemukan, 0 jika tidak.",
            "  2. hapusNode(Node *head, int nilai) -> hapus node PERTAMA",
            "     yang punya nilai tersebut, kembalikan head yang baru.",
            "Pastikan memori node yang dihapus di-free().",
        ],
        "hints": [
            "Baca materi \"Linked List: Struktur Data Dinamis\". Mencari cukup menelusuri dari head; menghapus butuh node sebelumnya supaya sambungannya bisa dipindah.",
            "hapusNode: jalan dengan dua pointer, current dan previous, sampai ketemu nilainya. Kalau nggak ketemu, kembalikan head apa adanya. Kalau yang dihapus head (previous masih NULL), head baru adalah node sesudahnya; selain itu sambungkan previous->next ke current->next. Terakhir free(current).",
            "Solusi contoh membangun 10 -> 20 -> 30 -> NULL dengan tambahDiAwal, mencetak Cari 20? 1 dan Cari 99? 0, lalu menghapus 20 jadi 10 -> 30 -> NULL. Bebaskan sisa node di akhir main.",
        ],
        "solution": """#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node* tambahDiAwal(Node *head, int nilai) {
    Node *baru = (Node*) malloc(sizeof(Node));
    baru->data = nilai;
    baru->next = head;
    return baru;
}

int cariNode(Node *head, int nilai) {
    Node *current = head;
    while (current != NULL) {
        if (current->data == nilai) return 1;
        current = current->next;
    }
    return 0;
}

Node* hapusNode(Node *head, int nilai) {
    Node *current = head;
    Node *previous = NULL;

    while (current != NULL && current->data != nilai) {
        previous = current;
        current = current->next;
    }

    if (current == NULL) return head;   // tidak ditemukan

    if (previous == NULL) {
        head = current->next;   // hapus HEAD
    } else {
        previous->next = current->next;   // sambung ulang, lompati current
    }
    free(current);
    return head;
}

void tampilkan(Node *head) {
    for (Node *c = head; c != NULL; c = c->next) {
        printf("%d -> ", c->data);
    }
    printf("NULL\\n");
}

int main(void) {
    Node *head = NULL;
    head = tambahDiAwal(head, 30);
    head = tambahDiAwal(head, 20);
    head = tambahDiAwal(head, 10);
    tampilkan(head);                        // 10 -> 20 -> 30 -> NULL

    printf("Cari 20? %d\\n", cariNode(head, 20));   // 1
    printf("Cari 99? %d\\n", cariNode(head, 99));   // 0

    head = hapusNode(head, 20);
    tampilkan(head);                        // 10 -> 30 -> NULL

    // Bebaskan sisa node
    while (head != NULL) {
        Node *temp = head;
        head = head->next;
        free(temp);
    }
    return 0;
}""",
    },
    {
        "title": "Latihan 17: Bubble Sort & Binary Search",
        "difficulty": "Sulit",
        "question": [
            "Implementasikan fungsi bubbleSort(int arr[], int n) untuk",
            "mengurutkan array dari kecil ke besar. Setelah terurut,",
            "implementasikan binarySearch(int arr[], int n, int target)",
            "yang mengembalikan indeks target (atau -1 jika tidak ada),",
            "menggunakan algoritma binary search (bukan linear search).",
        ],
        "hints": [
            "Bekalnya materi \"Array\" dan \"Function (Fungsi)\"; cara kerja binary search juga disinggung di \"C Generik: void *, qsort & Fungsi Variadic\". Binary search cuma jalan di array yang sudah terurut.",
            "Bubble sort: dua loop bersarang, tukar dua elemen bertetangga kalau yang kiri lebih besar. Binary search: simpan batas kiri dan kanan, cek elemen tengah; kalau target lebih besar geser kiri ke tengah + 1, kalau lebih kecil geser kanan ke tengah - 1, dan berhenti saat kiri melewati kanan.",
            "Hitung tengah dengan kiri + (kanan - kiri) / 2 supaya nggak overflow. Data solusi contoh {64, 25, 12, 22, 11, 90, 45}; sesudah diurutkan, 22 ada di indeks 2 dan 99 menghasilkan -1.",
        ],
        "solution": """#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int binarySearch(int arr[], int n, int target) {
    int kiri = 0, kanan = n - 1;

    while (kiri <= kanan) {
        int tengah = kiri + (kanan - kiri) / 2;

        if (arr[tengah] == target) {
            return tengah;
        } else if (arr[tengah] < target) {
            kiri = tengah + 1;
        } else {
            kanan = tengah - 1;
        }
    }
    return -1;   // tidak ditemukan
}

int main(void) {
    int data[] = {64, 25, 12, 22, 11, 90, 45};
    int n = sizeof(data) / sizeof(data[0]);

    bubbleSort(data, n);
    printf("Setelah diurutkan: ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\\n");

    int idx = binarySearch(data, n, 22);
    printf("Index dari 22: %d\\n", idx);

    idx = binarySearch(data, n, 99);
    printf("Index dari 99 (tidak ada): %d\\n", idx);
    return 0;
}""",
    },
    {
        "title": "Latihan 18: Simulasi Database Mahasiswa (Struct + Dynamic Array + File)",
        "difficulty": "Sulit",
        "question": [
            "Gabungkan semua konsep: buat program yang:",
            "  1. Membuat array of struct Mahasiswa (nama, nim, ipk) secara",
            "     DINAMIS dengan malloc() sejumlah n (dari input user).",
            "  2. Mengisi data dengan nilai contoh (boleh hardcode untuk n=3).",
            "  3. Menyimpan SEMUA data ke file 'mahasiswa.txt' dengan fprintf().",
            "  4. Menampilkan mahasiswa dengan IPK TERTINGGI.",
            "  5. Membebaskan (free) memori array di akhir program.",
        ],
        "hints": [
            "Ini gabungan materi \"Struct\", \"Dynamic Memory Allocation (malloc, calloc, free)\", dan \"File I/O\". Kerjakan satu bagian sampai jalan, baru tambah bagian berikutnya.",
            "Urutannya: malloc array of struct untuk n = 3 dan cek NULL, isi datanya (nama pakai strcpy), tulis semuanya ke mahasiswa.txt dengan fprintf, cari indeks IPK tertinggi seperti di Latihan 6, cetak, lalu free. Kalau fopen gagal, free dulu sebelum return.",
            "Data contoh: Andi 101 3.5, Budi 102 3.9, Citra 103 3.2. Satu-satunya keluaran di layar: Mahasiswa dengan IPK tertinggi: Budi (IPK 3.90).",
        ],
        "solution": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nama[50];
    int nim;
    double ipk;
} Mahasiswa;

int main(void) {
    int n = 3;
    Mahasiswa *data = (Mahasiswa*) malloc(n * sizeof(Mahasiswa));
    if (data == NULL) {
        printf("Alokasi memori gagal!\\n");
        return 1;
    }

    strcpy(data[0].nama, "Andi"); data[0].nim = 101; data[0].ipk = 3.5;
    strcpy(data[1].nama, "Budi"); data[1].nim = 102; data[1].ipk = 3.9;
    strcpy(data[2].nama, "Citra"); data[2].nim = 103; data[2].ipk = 3.2;

    // Simpan ke file
    FILE *fp = fopen("mahasiswa.txt", "w");
    if (fp == NULL) {
        printf("Gagal membuka file!\\n");
        free(data);
        return 1;
    }
    for (int i = 0; i < n; i++) {
        fprintf(fp, "%s %d %.2f\\n", data[i].nama, data[i].nim, data[i].ipk);
    }
    fclose(fp);

    // Cari IPK tertinggi
    int idxMax = 0;
    for (int i = 1; i < n; i++) {
        if (data[i].ipk > data[idxMax].ipk) {
            idxMax = i;
        }
    }
    printf("Mahasiswa dengan IPK tertinggi: %s (IPK %.2f)\\n",
           data[idxMax].nama, data[idxMax].ipk);

    free(data);   // WAJIB, karena hasil malloc()
    data = NULL;
    return 0;
}""",
    },
    {
        'title': 'Proyek Akhir: Pencari Jalan Keluar Labirin',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Pencari Jalan Keluar Labirin',
        '',
        "Sebuah gudang digambar sebagai peta karakter: '#' tembok, '.' lorong,",
        "'S' pintu masuk, 'K' pintu keluar. Petugas keamanan ingin tahu jalur",
        'TERPENDEK dari S ke K, dan mana saja sudut yang tidak bisa dicapai',
        'sama sekali.',
        '',
        'Ini bukan soal mencetak tabel. Yang diuji: apakah kamu bisa memilih',
        'struktur data yang tepat, mengurus memori yang kamu minta sendiri,',
        'dan menelusuri balik sebuah jalur.',
        '',
        'Peta (7 baris x 11 kolom) ditulis sebagai array of string di program.',
        '',
        'Yang harus ada di programmu:',
        '  1. BFS memakai antrean buatan sendiri (array + indeks depan/belakang),',
        '     bukan rekursi -- rekursi memberi jalur, tapi belum tentu terpendek.',
        '  2. Dua matriks pendamping: jarak[][] dan asal[][] untuk menelusuri',
        '     balik jalurnya dari K ke S.',
        '  3. Urutan arah dipatok: atas, kanan, bawah, kiri.',
        '  4. Memori diminta dengan malloc dan WAJIB di-free sebelum keluar.',
        "  5. Peta dicetak ulang dengan jalur ditandai '*' (S dan K tetap utuh).",
        '  6. Laporkan panjang jalur, jumlah petak terjangkau, dan jumlah petak',
        '     kosong yang tidak terjangkau.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  PENCARI JALAN KELUAR LABIRIN',
        '  ============================',
        '  ###########',
        '  #S**#*****#',
        '  #.#*#*###*#',
        '  #.#***#..*#',
        '  #.#####.#*#',
        '  #.......#K#',
        '  ###########',
        '  ----------------------------',
        '  Panjang jalur terpendek : 16 langkah',
        '  Petak yang terjangkau   : 30',
        '  Petak kosong tak terjangkau : 0',
    ],
        'hints': [
            "BFS (breadth-first search) menjelajah petak selapis demi selapis dari S, jadi saat K pertama kali tercapai, jalurnya pasti terpendek. Bekalnya ada di materi \"Array\", \"Struct\", dan \"Dynamic Memory Allocation (malloc, calloc, free)\".",
            "Antrean cukup array Titik plus dua indeks: depan untuk mengambil, belakang untuk menambah. Isi jarak[][] dengan -1 sebagai tanda belum dikunjungi. Tiap kali mengambil satu petak, coba empat tetangganya dengan urutan atas, kanan, bawah, kiri; lewati yang di luar peta, tembok, atau sudah punya jarak, lalu catat jarak dan asalnya sebelum dimasukkan ke antrean.",
            "typedef struct { int b, k; } Titik; antreannya malloc(sizeof(Titik) * BARIS * KOLOM), dan arah ditulis sebagai dua array sejajar DB[4] = {-1,0,1,0} dan DK[4] = {0,1,0,-1}. Untuk jalur, mulai dari K dan ikuti asal[][] mundur sambil mengisi jalur[i] dari indeks panjang turun ke 0, jadi hasilnya sudah urut dari S ke K.",
        ],
        'solution': """/* Pencari Jalan Keluar Labirin -- BFS di atas array dua dimensi. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BARIS 7
#define KOLOM 11

typedef struct { int b, k; } Titik;

static const char *PETA[BARIS] = {
    "###########",
    "#S..#.....#",
    "#.#.#.###.#",
    "#.#...#...#",
    "#.#####.#.#",
    "#.......#K#",
    "###########",
};

/* Empat arah, ditulis sebagai dua larik supaya urutannya jelas dan tetap:
   atas, kanan, bawah, kiri. Urutan ini menentukan jalur mana yang ditemukan
   lebih dulu saat ada dua jalur sama panjang. */
static const int DB[4] = {-1, 0, 1, 0};
static const int DK[4] = {0, 1, 0, -1};

static int cari_huruf(char huruf, Titik *keluar) {
    for (int b = 0; b < BARIS; b++)
        for (int k = 0; k < KOLOM; k++)
            if (PETA[b][k] == huruf) { keluar->b = b; keluar->k = k; return 1; }
    return 0;
}

int main(void) {
    Titik mulai, akhir;
    if (!cari_huruf('S', &mulai) || !cari_huruf('K', &akhir)) {
        printf("Peta tidak punya S atau K.\\n");
        return 1;
    }

    int jarak[BARIS][KOLOM];
    Titik asal[BARIS][KOLOM];
    for (int b = 0; b < BARIS; b++)
        for (int k = 0; k < KOLOM; k++) { jarak[b][k] = -1; asal[b][k].b = -1; }

    Titik *antre = malloc(sizeof(Titik) * BARIS * KOLOM);
    if (!antre) return 1;
    int depan = 0, belakang = 0;

    antre[belakang++] = mulai;
    jarak[mulai.b][mulai.k] = 0;

    while (depan < belakang) {
        Titik t = antre[depan++];
        for (int i = 0; i < 4; i++) {
            int nb = t.b + DB[i], nk = t.k + DK[i];
            if (nb < 0 || nb >= BARIS || nk < 0 || nk >= KOLOM) continue;
            if (PETA[nb][nk] == '#') continue;
            if (jarak[nb][nk] != -1) continue;
            jarak[nb][nk] = jarak[t.b][t.k] + 1;
            asal[nb][nk] = t;
            antre[belakang].b = nb; antre[belakang].k = nk; belakang++;
        }
    }

    printf("PENCARI JALAN KELUAR LABIRIN\\n");
    printf("============================\\n");

    if (jarak[akhir.b][akhir.k] == -1) {
        printf("Tidak ada jalan dari S ke K.\\n");
        free(antre);
        return 0;
    }

    /* Telusuri balik dari K ke S, lalu balik urutannya. */
    int panjang = jarak[akhir.b][akhir.k];
    Titik *jalur = malloc(sizeof(Titik) * (panjang + 1));
    if (!jalur) { free(antre); return 1; }
    Titik t = akhir;
    for (int i = panjang; i >= 0; i--) { jalur[i] = t; t = asal[t.b][t.k]; }

    char gambar[BARIS][KOLOM + 1];
    for (int b = 0; b < BARIS; b++) { strcpy(gambar[b], PETA[b]); }
    for (int i = 1; i < panjang; i++) gambar[jalur[i].b][jalur[i].k] = '*';

    for (int b = 0; b < BARIS; b++) printf("%s\\n", gambar[b]);

    printf("----------------------------\\n");
    printf("Panjang jalur terpendek : %d langkah\\n", panjang);
    int terjangkau = 0;
    for (int b = 0; b < BARIS; b++)
        for (int k = 0; k < KOLOM; k++)
            if (jarak[b][k] != -1) terjangkau++;
    printf("Petak yang terjangkau   : %d\\n", terjangkau);

    int buntu = 0;
    for (int b = 0; b < BARIS; b++)
        for (int k = 0; k < KOLOM; k++) {
            if (jarak[b][k] == -1 && PETA[b][k] != '#') buntu++;
        }
    printf("Petak kosong tak terjangkau : %d\\n", buntu);

    free(jalur);
    free(antre);
    return 0;
}
""",
    },
]
