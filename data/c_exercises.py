C_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program yang menampilkan:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar C.",
            "(Nama boleh diganti dengan nama sendiri)",
        ],
        "hints": [
            "Gunakan printf() untuk tiap baris.",
            "Jangan lupa #include <stdio.h> dan return 0; di akhir main.",
            "Karakter \\n untuk baris baru.",
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
            "int a = 15, b = 4;",
            "Pembagian int/int = int, sisa dibuang.",
            "Gunakan %d untuk mencetak int.",
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
            "Buat program: minta input nilai dari user (scanf),",
            "jika nilai >= 75 tampilkan 'Lulus', selain itu 'Tidak Lulus'.",
        ],
        "hints": [
            "int nilai; scanf(\"%d\", &nilai);",
            "Gunakan if-else biasa.",
        ],
        "solution": """#include <stdio.h>

int main(void) {
    int nilai;

    printf("Masukkan nilai: ");
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
        "difficulty": "Sedang",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20",
            "beserta total jumlahnya.",
        ],
        "hints": [
            "Gunakan for dan cek i % 2 == 0.",
            "Accumulate total dengan variabel int, mulai dari 0.",
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
        "difficulty": "Sedang",
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
            "printf(\"*\") tanpa \\n di loop dalam, printf(\"\\\\n\") setelah loop dalam selesai.",
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
        "difficulty": "Sedang",
        "question": [
            "Buat program untuk mencari nilai terbesar dan terkecil",
            "dari array berikut:",
            "int data[] = {23, 5, 87, 12, 55, 99, 31};",
        ],
        "hints": [
            "Asumsikan elemen pertama sebagai max/min awal.",
            "Loop dari indeks 1, bandingkan dengan max/min saat ini.",
            "Gunakan sizeof(data)/sizeof(data[0]) untuk jumlah elemen.",
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
        "difficulty": "Sedang",
        "question": [
            "Buat 3 fungsi:",
            "  1. luasPersegi(int sisi)          -> sisi * sisi",
            "  2. luasPersegiPanjang(int p, int l) -> p * l",
            "  3. luasLingkaran(double r)         -> 3.14159 * r * r",
            "Panggil ketiganya di main dan tampilkan hasilnya.",
        ],
        "hints": [
            "Buat function prototype di atas main(), definisi di bawah.",
            "luasLingkaran bertipe kembali double.",
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
        "difficulty": "Sedang",
        "question": [
            "Buat fungsi panjangString(char s[]) yang menghitung panjang",
            "string TANPA memakai strlen() (loop manual sampai ketemu '\\0').",
            "Buat juga fungsi balikString(char s[]) yang membalik isi",
            "string tersebut secara in-place (mengubah array aslinya).",
        ],
        "hints": [
            "int i = 0; while (s[i] != '\\0') { i++; }",
            "Untuk balik: tukar s[i] dengan s[n-1-i] untuk i dari 0 sampai n/2.",
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
        "difficulty": "Sedang",
        "question": [
            "Buat struct Mahasiswa (nama[50], umur, ipk).",
            "Buat array of struct berisi 3 mahasiswa dengan data bebas.",
            "Tampilkan semua data, lalu hitung & tampilkan rata-rata IPK.",
        ],
        "hints": [
            "typedef struct { char nama[50]; int umur; double ipk; } Mahasiswa;",
            "Mahasiswa daftar[3] = { {...}, {...}, {...} };",
            "Loop untuk menampilkan & menjumlahkan ipk.",
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
        "difficulty": "Menengah",
        "question": [
            "Buat fungsi tukar(int *a, int *b) yang menukar nilai dua",
            "variabel int memakai pointer. Buat juga fungsi",
            "urutkanTiga(int *a, int *b, int *c) yang mengurutkan tiga",
            "variabel dari kecil ke besar (memakai tukar() di dalamnya).",
        ],
        "hints": [
            "void tukar(int *a, int *b) { int temp = *a; *a = *b; *b = temp; }",
            "Bandingkan pasangan (a,b), (b,c), (a,b) lagi - mirip bubble sort 3 elemen.",
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
        "difficulty": "Menengah",
        "question": [
            "Buat program yang meminta jumlah data (n) dari user, lalu",
            "meng-alokasikan array int secara dinamis dengan malloc()",
            "sebesar n. Isi array dengan angka kelipatan 5 (5, 10, 15, ...),",
            "tampilkan semua isinya, lalu bebaskan (free) memorinya.",
        ],
        "hints": [
            "int *arr = malloc(n * sizeof(int)); SELALU cek arr == NULL.",
            "arr[i] = (i + 1) * 5;",
            "Jangan lupa free(arr); di akhir program.",
        ],
        "solution": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Jumlah data: ");
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
        "difficulty": "Menengah",
        "question": [
            "Buat struct Rekening (nomor[20], saldo).",
            "Buat fungsi setor(Rekening *r, double jumlah) dan",
            "tarik(Rekening *r, double jumlah) yang mengembalikan int",
            "(1 jika berhasil, 0 jika saldo tidak cukup untuk tarik).",
            "Semua fungsi harus MENGUBAH struct asli lewat pointer.",
        ],
        "hints": [
            "void setor(Rekening *r, double jumlah) { r->saldo += jumlah; }",
            "int tarik(Rekening *r, double jumlah) { if (jumlah <= r->saldo) {...return 1;} return 0; }",
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
        "difficulty": "Menengah",
        "question": [
            "Buat 3 fungsi operasi (tambah, kurang, kali) bertipe",
            "int(int, int). Buat fungsi prosesArray(int arr[], int n,",
            "int (*operasi)(int, int)) yang menerapkan operasi tersebut",
            "SECARA BERURUTAN (akumulasi) ke semua elemen array.",
            "Uji dengan array {1,2,3,4,5} untuk ketiga operasi.",
        ],
        "hints": [
            "int hasil = arr[0]; for (i=1;i<n;i++) hasil = operasi(hasil, arr[i]);",
            "Panggil prosesArray(data, 5, tambah); dst.",
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
        "difficulty": "Menengah",
        "question": [
            "Buat program yang menulis 3 baris data (nama dan nilai,",
            "dipisah spasi) ke file 'nilai.txt' dengan fprintf(). Lalu",
            "baca kembali file tersebut baris per baris dengan fgets()",
            "dan tampilkan ke layar.",
        ],
        "hints": [
            "FILE *fp = fopen(\"nilai.txt\", \"w\"); SELALU cek NULL.",
            "fprintf(fp, \"%s %d\\\\n\", nama, nilai);",
            "Baca ulang dengan mode \"r\" dan fgets() dalam loop while.",
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
            "int stack[100]; int top = -1;  // -1 berarti kosong",
            "push: stack[++top] = nilai;",
            "pop: return stack[top--]; (cek isEmpty dulu sebelum pop!)",
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
            "cariNode: loop dari head, bandingkan current->data dengan nilai.",
            "hapusNode: perlu tracking 'previous' node untuk menyambung ulang pointer.",
            "Kasus khusus: menghapus HEAD (previous == NULL).",
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
            "Bubble sort: nested loop, tukar jika arr[j] > arr[j+1].",
            "Binary search: butuh array TERURUT, bandingkan dengan elemen tengah,",
            "lalu persempit ke kiri/kanan berdasarkan hasil perbandingan.",
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
            "typedef struct { char nama[50]; int nim; double ipk; } Mahasiswa;",
            "Mahasiswa *data = malloc(n * sizeof(Mahasiswa));",
            "Loop untuk cari IPK max (mirip Latihan 6, tapi field struct).",
            "fprintf(fp, \"%s %d %.2f\\\\n\", data[i].nama, data[i].nim, data[i].ipk);",
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
]
