"""Tanggal dan waktu aktual sesuai jam komputer saat eksekusi."""
from datetime import date, datetime, timezone, timedelta

wib = timezone(timedelta(hours=7), "WIB")
sekarang = datetime.now(timezone.utc)
print("Tanggal lokal mesin:", date.today())
print("Datetime lokal mesin:", datetime.now().isoformat())
print("Datetime UTC:", sekarang.isoformat())
print("Datetime WIB:", sekarang.astimezone(wib).isoformat())
print("Tanggal WIB:", sekarang.astimezone(wib).strftime("%d/%m/%Y"))
print("Catatan: waktu aktual berubah setiap program dijalankan.")
assert sekarang.astimezone(wib).timestamp() == sekarang.timestamp()
