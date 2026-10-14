"""Mengubah string menjadi datetime dan menangani input salah."""
from datetime import datetime

teks = "14/10/2026 13:30:45"
hasil = datetime.strptime(teks, "%d/%m/%Y %H:%M:%S")
print("Input:", teks)
print("Hasil:", hasil)
print("Tipe:", type(hasil).__name__)
ambigu = "05/06/2026"
print("Hari/bulan:", datetime.strptime(ambigu, "%d/%m/%Y").date())
print("Bulan/hari:", datetime.strptime(ambigu, "%m/%d/%Y").date())
for salah in ["31/02/2026", "14-10-2026"]:
    try:
        datetime.strptime(salah, "%d/%m/%Y")
    except ValueError:
        print("Input ditolak (ValueError):", salah)
    else:
        raise AssertionError("Input tidak valid seharusnya ditolak")
assert hasil == datetime(2026, 10, 14, 13, 30, 45)
