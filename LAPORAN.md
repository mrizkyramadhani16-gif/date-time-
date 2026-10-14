# Laporan Hasil Pengerjaan

## Praktikum Python: datetime dan time

## 1. Tujuan dan ruang lingkup

Mempraktikkan delapan topik dari tautan Programiz yang diberikan. Kode disusun sebagai contoh praktikum mandiri, bukan salinan seluruh contoh tutorial. Tidak ada soal atau rubrik tambahan pada pesan tugas.

## 2. Lingkungan dan cara menjalankan

Pengujian aktual: Python 3.12.14, Linux x86_64, 14 Oktober 2026. Waktu lokal lingkungan saat pengujian adalah WIB. Program hanya memakai standard library. Jalankan dari folder proyek:

```bash
python run_all.py
```

Di sebagian sistem gunakan `python3`. Program menyimpan stdout, stderr, dan exit code ke folder `hasil`. Waktu dinamis mengikuti jam komputer; hasil run ulang tidak harus sama persis. Laporan ini merekam run yang disertakan, bukan otomatis diperbarui oleh runner.

## 3. Ringkasan eksekusi

| No. | Program | Exit code | Status |
|---|---|---|---|
| 1 | `01_datetime.py` | 0 | Berhasil |
| 2 | `02_strftime.py` | 0 | Berhasil |
| 3 | `03_strptime.py` | 0 | Berhasil |
| 4 | `04_current_datetime.py` | 0 | Berhasil |
| 5 | `05_current_time.py` | 0 | Berhasil |
| 6 | `06_timestamp_datetime.py` | 0 | Berhasil |
| 7 | `07_time_module.py` | 0 | Berhasil |
| 8 | `08_sleep.py` | 0 | Berhasil |

Seluruh 8 program selesai dengan exit code 0. Pemeriksaan assert yang disertakan juga lolos. Demonstrasi input salah pada praktikum 3 merupakan penanganan error yang disengaja, bukan kegagalan run.

## 4. Hasil dan pembahasan

### 1. Dasar datetime

Kode: [praktikum/01_datetime.py](praktikum/01_datetime.py)

Sumber: https://www.programiz.com/python-programming/datetime

Output aktual:

```text
Tanggal: 2026-10-14
Tahun, bulan, hari: 2026 10 14
Waktu: 13:30:45.123456
Gabungan: 2026-10-14 13:30:45.123456
Batas pengumpulan: 2026-10-21 15:30:45.123456
Selisih: 7 days, 2:00:00
Total detik: 612000.0
Dengan zona: 2026-10-14 13:30:45.123456+07:00
```

Pembahasan: Program membuat date, time, dan datetime, kemudian menghitung tenggat tujuh hari dua jam. Hasil selisih adalah 612000 detik. Objek timedelta menyatakan durasi; penambahan otomatis menyesuaikan tanggal. Zona WIB pada contoh tetap ditandai dengan UTC+07:00.

### 2. Formatting dengan strftime

Kode: [praktikum/02_strftime.py](praktikum/02_strftime.py)

Sumber: https://www.programiz.com/python-programming/datetime/strftime

Output aktual:

```text
%Y -> 2026
%m -> 10
%d -> 14
%d/%m/%Y -> 14/10/2026
%H:%M:%S -> 13:30:45
%I:%M:%S %p -> 01:30:45 PM
%A, %d %B %Y -> Wednesday, 14 October 2026
%z %Z -> +0700 WIB
%c -> Wed Oct 14 13:30:45 2026
Jenis hasil: str
```

Pembahasan: Objek tanggal yang sama ditampilkan dalam beberapa pola. Hasil 14/10/2026 berasal dari %d/%m/%Y. %m adalah bulan, sedangkan %M adalah menit. Hasil formatting bertipe str. Nama hari, bulan, serta %c mengikuti locale lingkungan.

### 3. Parsing dengan strptime

Kode: [praktikum/03_strptime.py](praktikum/03_strptime.py)

Sumber: https://www.programiz.com/python-programming/datetime/strptime

Output aktual:

```text
Input: 14/10/2026 13:30:45
Hasil: 2026-10-14 13:30:45
Tipe: datetime
Hari/bulan: 2026-06-05
Bulan/hari: 2026-05-06
Input ditolak (ValueError): 31/02/2026
Input ditolak (ValueError): 14-10-2026
```

Pembahasan: Teks diubah menjadi datetime berdasarkan pola yang diberikan. Input 05/06/2026 menghasilkan 5 Juni atau 6 Mei sesuai urutan format. Tanggal 31 Februari dan pemisah yang tidak cocok ditolak melalui ValueError; exception ditangani sehingga program tetap selesai.

### 4. Tanggal dan waktu sekarang

Kode: [praktikum/04_current_datetime.py](praktikum/04_current_datetime.py)

Sumber: https://www.programiz.com/python-programming/datetime/current-datetime

Output aktual:

```text
Tanggal lokal mesin: 2026-10-14
Datetime lokal mesin: 2026-10-14T13:40:04.195051
Datetime UTC: 2026-10-14T06:40:04.195033+00:00
Datetime WIB: 2026-10-14T13:40:04.195033+07:00
Tanggal WIB: 14/10/2026
Catatan: waktu aktual berubah setiap program dijalankan.
```

Pembahasan: Program membaca jam aktual komputer, bukan memakai tanggal contoh. date.today() dan datetime.now() tanpa zona mengikuti waktu lokal mesin. UTC dikonversi ke WIB dari satu instant yang sama. Angka timestamp tetap sama meskipun tampilan jam berbeda.

### 5. Jam saat ini

Kode: [praktikum/05_current_time.py](praktikum/05_current_time.py)

Sumber: https://www.programiz.com/python-programming/datetime/current-time

Output aktual:

```text
Jam lokal (datetime): 13:40:04
Jam lokal (time): 13:40:04
Jam UTC: 06:40:04
Jam WIB: 13:40:04
Objek time WIB: 13:40:04.204403+07:00
Zona lokal mesin: ('WIB', 'WIB')
```

Pembahasan: Dua pendekatan menampilkan jam lokal melalui datetime dan time. UTC dan WIB ditampilkan secara eksplisit. Hasil pembacaan terpisah dapat berbeda jika pergantian detik terjadi di antara pemanggilan. Offset WIB dibuat dengan timezone standar tanpa dependensi eksternal.

### 6. Timestamp dan datetime

Kode: [praktikum/06_timestamp_datetime.py](praktikum/06_timestamp_datetime.py)

Sumber: https://www.programiz.com/python-programming/datetime/timestamp-datetime

Output aktual:

```text
Tanggal asal WIB: 2026-10-14T13:30:00+07:00
Unix timestamp (detik): 1791959400.0
Hasil UTC: 2026-10-14T06:30:00+00:00
Hasil WIB: 2026-10-14T13:30:00+07:00
Konversi bolak-balik sama: True
Epoch UTC: 1970-01-01 00:00:00+00:00
```

Pembahasan: Datetime 14 Oktober 2026 pukul 13:30 WIB dikonversi menjadi 1791959400 detik. Ketika ditampilkan sebagai UTC, waktunya menjadi 06:30 pada tanggal yang sama. Konversi kembali menghasilkan datetime asal. Zona eksplisit menghindari interpretasi lokal yang tidak disengaja.

### 7. Modul time

Kode: [praktikum/07_time_module.py](praktikum/07_time_module.py)

Sumber: https://www.programiz.com/python-programming/time

Output aktual:

```text
Timestamp aktual: 1791960004.2231278
ctime lokal: Wed Oct 14 13:30:00 2026
localtime: 2026-10-14 13:30:00
gmtime UTC: 2026-10-14 06:30:00
Tahun UTC: 2026 | Hari ke: 287
asctime UTC: Wed Oct 14 06:30:00 2026
mktime dari localtime: 1791959400.0
strptime -> struct_time, tahun: 2026
```

Pembahasan: Program membandingkan localtime dan gmtime, lalu memakai ctime, asctime, mktime, strftime, dan strptime. mktime menafsirkan input sebagai waktu lokal; gmtime menghasilkan UTC. time.strptime menghasilkan struct_time, berbeda dari datetime.strptime yang menghasilkan datetime.

### 8. Jeda dengan sleep

Kode: [praktikum/08_sleep.py](praktikum/08_sleep.py)

Sumber: https://www.programiz.com/python-programming/time/sleep

Output aktual:

```text
Mulai jeda 0.2 detik
Durasi terukur: 0.200098 detik
Nilai kembali sleep: None
Jam digital WIB (3 tampilan, jeda 0.2 detik):
1 13:40:04.441847
2 13:40:04.642011
3 13:40:04.842177
Selesai
```

Pembahasan: Jeda 0.2 detik diukur menggunakan perf_counter. Durasi aktual dapat lebih lama akibat penjadwalan sistem. sleep mengembalikan None dan menunda thread pemanggil. Jam digital dibatasi tiga tampilan agar eksekusi otomatis selesai; jeda antar tampilan juga 0.2 detik.

## 5. Kesimpulan

Delapan praktikum berhasil menunjukkan pembuatan objek tanggal, formatting, parsing, pembacaan jam aktual, konversi timestamp, fungsi modul time, dan jeda eksekusi. Hal yang perlu diperhatikan adalah format input, zona waktu, locale, serta perbedaan antara waktu kalender dan pengukuran durasi. Pengujian ini membuktikan contoh berjalan pada lingkungan yang dicatat, bukan pengujian seluruh kemungkinan input atau sistem operasi.

## 6. Referensi

1. [Dasar datetime](https://www.programiz.com/python-programming/datetime)
2. [Formatting dengan strftime](https://www.programiz.com/python-programming/datetime/strftime)
3. [Parsing dengan strptime](https://www.programiz.com/python-programming/datetime/strptime)
4. [Tanggal dan waktu sekarang](https://www.programiz.com/python-programming/datetime/current-datetime)
5. [Jam saat ini](https://www.programiz.com/python-programming/datetime/current-time)
6. [Timestamp dan datetime](https://www.programiz.com/python-programming/datetime/timestamp-datetime)
7. [Modul time](https://www.programiz.com/python-programming/time)
8. [Jeda dengan sleep](https://www.programiz.com/python-programming/time/sleep)

Diakses 14 Oktober 2026.
