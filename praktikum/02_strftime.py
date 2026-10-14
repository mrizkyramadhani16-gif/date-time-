"""Mengubah datetime menjadi string dengan format berbeda."""
from datetime import datetime, timezone, timedelta

contoh = datetime(2026, 10, 14, 13, 30, 45,
                  tzinfo=timezone(timedelta(hours=7), "WIB"))
pola = ["%Y", "%m", "%d", "%d/%m/%Y", "%H:%M:%S",
        "%I:%M:%S %p", "%A, %d %B %Y", "%z %Z", "%c"]
for format_tanggal in pola:
    hasil = contoh.strftime(format_tanggal)
    print(f"{format_tanggal} -> {hasil}")
assert contoh.strftime("%d/%m/%Y") == "14/10/2026"
print("Jenis hasil:", type(hasil).__name__)
