# nama: Farrel Tiffany
# kelas: XI TKJ1
# nomor absen: 09
# Soal: Di toko online, hitung diskon berdasarkan total belanjaan  pelanggan
total_belanja = float(input("total belanjaan anda"))

if total_belanja > 500000:
    diskon = total_belanja * 0.10
elif total_belanja >= 300000:
    diskon = total_belanja * 0.05
else:
    diskon= 0

total_pembayaran = total_belanja - diskon
print(f"total pembayaran setelah diskon: {total_pembayaran}")
