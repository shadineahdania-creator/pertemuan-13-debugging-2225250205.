# --- FUNGSI HASIL PERBAIKAN ---
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


# --- MENJALANKAN TEST CASE ---
print("=== UJI COBA TEST CASE ===")
print("T1 (Rata-rata) :", hitung_rata_rata([80, 60, 90, 70]))  # Expected: 75.0
print("T2 (Rata-rata) :", hitung_rata_rata([100, 80]))         # Expected: 90.0
print("T3 (Status 60)  :", status(60))                        # Expected: Lulus
print("T4 (Status 59)  :", status(59))                        # Expected: Tidak lulus
print("T5 (Tertinggi)  :", nilai_tertinggi([80, 60, 90, 70]))  # Expected: 90