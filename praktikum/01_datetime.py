"""Objek tanggal, waktu, datetime, dan durasi."""
from datetime import date, time, datetime, timedelta, timezone

tanggal = date(2026, 10, 14)
jam = time(13, 30, 45, 123456)
jadwal = datetime.combine(tanggal, jam)
batas = jadwal + timedelta(days=7, hours=2)
print("Tanggal:", tanggal)
print("Tahun, bulan, hari:", tanggal.year, tanggal.month, tanggal.day)
print("Waktu:", jam)
print("Gabungan:", jadwal)
print("Batas pengumpulan:", batas)
print("Selisih:", batas - jadwal)
print("Total detik:", (batas - jadwal).total_seconds())
wib = timezone(timedelta(hours=7), "WIB")
print("Dengan zona:", jadwal.replace(tzinfo=wib))
assert (batas - jadwal).total_seconds() == 612000
