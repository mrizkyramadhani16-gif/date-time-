"""Konversi dua arah Unix timestamp dengan zona eksplisit."""
from datetime import datetime, timezone, timedelta

wib = timezone(timedelta(hours=7), "WIB")
asal = datetime(2026, 10, 14, 13, 30, tzinfo=wib)
angka = asal.timestamp()
utc = datetime.fromtimestamp(angka, timezone.utc)
kembali = datetime.fromtimestamp(angka, wib)
print("Tanggal asal WIB:", asal.isoformat())
print("Unix timestamp (detik):", angka)
print("Hasil UTC:", utc.isoformat())
print("Hasil WIB:", kembali.isoformat())
print("Konversi bolak-balik sama:", kembali == asal)
print("Epoch UTC:", datetime.fromtimestamp(0, timezone.utc))
assert kembali == asal
assert utc.timestamp() == angka
