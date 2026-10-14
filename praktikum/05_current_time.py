"""Jam saat ini menggunakan datetime dan modul time."""
from datetime import datetime, timezone, timedelta
import time

wib = timezone(timedelta(hours=7), "WIB")
print("Jam lokal (datetime):", datetime.now().strftime("%H:%M:%S"))
print("Jam lokal (time):", time.strftime("%H:%M:%S", time.localtime()))
saat_ini = datetime.now(timezone.utc)
print("Jam UTC:", saat_ini.strftime("%H:%M:%S"))
print("Jam WIB:", saat_ini.astimezone(wib).strftime("%H:%M:%S"))
print("Objek time WIB:", saat_ini.astimezone(wib).timetz())
print("Zona lokal mesin:", time.tzname)
