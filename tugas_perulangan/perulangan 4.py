#nama : Farrel Tiffany Valea
#No absen : 08
#Kelas : XI TKJ 1

#soal : 

jumlah_apel = 100
hari = 0

while jumlah_apel > 20:
    hari += 1
    penjualan = jumlah_apel * 0.10  # 10% dari jumlah apel saat ini
    jumlah_apel -= penjualan

print(f"Butuh {hari} hari agar sisa apel kurang dari 20 buah.")
