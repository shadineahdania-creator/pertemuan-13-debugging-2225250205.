# Pertemuan 13 - Debugging dan Testing

Nama: Shadine Ahania Sofyan
NIM: 2225250205
Kelas: 3B

## Kasus

Program yang diuji adalah program pengolahan nilai mahasiswa menggunakan Python. Program memiliki tiga fungsi, yaitu `hitung_rata_rata()` untuk menghitung rata-rata nilai, `status()` untuk menentukan kelulusan mahasiswa, dan `nilai_tertinggi()` untuk mencari nilai tertinggi.

Pengujian dilakukan untuk menemukan bug pada program awal, membandingkan hasil aktual dengan hasil yang diharapkan, memperbaiki kesalahan, dan melakukan pengujian ulang (*retest*).

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` (rata-rata) | 75.0 | 60.0 | FAIL |
| T2 | `[100, 80]` (rata-rata) | 90.0 | 36.0 | FAIL |
| T3 | `60` (status) | Lulus | Tidak lulus | FAIL |
| T4 | `59` (status) | Tidak lulus | Tidak lulus | PASS |
| T5 | `[80, 60, 90, 70]` (nilai tertinggi) | 90 | 0 | FAIL |

## Bug Report

### Bug 1 — Perhitungan Rata-rata

- Gejala: Hasil rata-rata tidak sesuai dengan data nilai.
- Lokasi: Fungsi `hitung_rata_rata()`.
- Akar penyebab: Program selalu membagi jumlah nilai dengan angka 5, meskipun jumlah data berbeda.
- Perbaikan: Mengganti pembagi menjadi `len(nilai)` agar sesuai dengan jumlah data. Untuk data kosong, program mengembalikan nilai 0.

### Bug 2 — Status Kelulusan

- Gejala: Mahasiswa dengan nilai 60 dinyatakan tidak lulus.
- Lokasi: Fungsi `status()`.
- Akar penyebab: Program menggunakan operator `>` sehingga nilai yang sama dengan 60 tidak memenuhi kondisi kelulusan.
- Perbaikan: Mengganti operator `>` menjadi `>=` agar nilai 60 termasuk kategori lulus.

### Bug 3 — Nilai Tertinggi

- Gejala: Program menghasilkan nilai tertinggi 0 meskipun terdapat nilai yang lebih besar.
- Lokasi: Fungsi `nilai_tertinggi()`.
- Akar penyebab: Program menggunakan kondisi `x < tertinggi`, sehingga variabel tidak diperbarui ketika menemukan nilai yang lebih besar.
- Perbaikan: Mengganti kondisi menjadi `x > tertinggi` dan menginisialisasi nilai tertinggi dari elemen pertama list. List kosong ditangani dengan mengembalikan `None`.

## Retest

Setelah perbaikan, seluruh test case dijalankan kembali untuk memastikan hasilnya sesuai dengan expected result.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

Hasil retest menunjukkan bahwa ketiga bug berhasil diperbaiki dan seluruh test case memenuhi hasil yang diharapkan.

## Cara Menjalankan

Jalankan program melalui terminal VS Code dengan perintah:

```bash
python praktik/praktik_4_debugging.py
```

Jika menggunakan Python 3 secara khusus, dapat juga menjalankan:

```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah menggunakan breakpoint dan Step Over pada VS Code. Teknik ini membantu mengamati perubahan nilai variabel pada setiap baris program sehingga penyebab kesalahan lebih mudah ditemukan. Selain itu, test case membantu membandingkan hasil aktual dengan hasil yang diharapkan, sedangkan retest memastikan bahwa perbaikan berhasil dan tidak menimbulkan kesalahan baru.