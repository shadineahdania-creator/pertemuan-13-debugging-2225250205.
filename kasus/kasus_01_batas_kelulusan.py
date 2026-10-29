def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

print(status_lulus(59))
print(status_lulus(60))
print(status_lulus(61))