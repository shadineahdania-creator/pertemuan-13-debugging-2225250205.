try:
    with open("nilai.txt", "r") as file:
        for baris in file:
            print(baris.strip())
except FileNotFoundError:
    print("File tidak ditemukan")