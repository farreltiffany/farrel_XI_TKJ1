#nama : Farrel Tiffany Valea
#No absen : 08
#Kelas : XI TKJ 1

#soal : 

jarak = 5  # Jarak awal dalam kilometer
minggu = 0

while jarak <= 10:
    minggu += 1
    pertambahan_jarak = jarak * 0.10  # 10% dari jarak saat ini
    jarak += pertambahan_jarak

print(f"Butuh {minggu} minggu agar pelari dapat berlari lebih dari 10 kilometer.")
