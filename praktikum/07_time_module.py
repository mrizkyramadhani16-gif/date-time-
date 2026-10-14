"""Fungsi utama modul time dan struct_time."""
import time

angka = 1791959400
lokal = time.localtime(angka)
utc = time.gmtime(angka)
print("Timestamp aktual:", time.time())
print("ctime lokal:", time.ctime(angka))
print("localtime:", time.strftime("%Y-%m-%d %H:%M:%S", lokal))
print("gmtime UTC:", time.strftime("%Y-%m-%d %H:%M:%S", utc))
print("Tahun UTC:", utc.tm_year, "| Hari ke:", utc.tm_yday)
print("asctime UTC:", time.asctime(utc))
print("mktime dari localtime:", time.mktime(lokal))
teks = "2026-10-14 13:30:00"
parsed = time.strptime(teks, "%Y-%m-%d %H:%M:%S")
print("strptime -> struct_time, tahun:", parsed.tm_year)
assert time.mktime(lokal) == angka
assert time.strftime("%Y-%m-%d %H:%M:%S", parsed) == teks
