#nama : Farrel Tiffany Valea
#No absen : 08
#Kelas : XI TKJ 1

#soal : 

nilai_investasi = 10000  # Nilai investasi awal dalam dollar
tahun = 0

while nilai_investasi <= 20000:
    tahun += 1
    pertumbuhan_investasi = nilai_investasi * 0.06  # 6% dari nilai investasi saat ini
    nilai_investasi += pertumbuhan_investasi

print(f"Butuh {tahun} tahun agar nilai investasi melebihi 20.000 dollar.")
