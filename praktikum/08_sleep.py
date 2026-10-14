"""Jeda singkat dan jam digital terbatas agar program selesai."""
import time
from datetime import datetime, timezone, timedelta

wib = timezone(timedelta(hours=7), "WIB")
print("Mulai jeda 0.2 detik")
mulai = time.perf_counter()
hasil = time.sleep(0.2)
durasi = time.perf_counter() - mulai
print(f"Durasi terukur: {durasi:.6f} detik")
print("Nilai kembali sleep:", hasil)
print("Jam digital WIB (3 tampilan, jeda 0.2 detik):")
for nomor in range(3):
    print(nomor + 1, datetime.now(wib).strftime("%H:%M:%S.%f"))
    if nomor < 2:
        time.sleep(0.2)
print("Selesai")
assert durasi >= 0.2
assert hasil is None
