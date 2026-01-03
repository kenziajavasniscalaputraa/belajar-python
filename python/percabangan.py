# Jenis Tiket Bioskop berdasarkan umur dan hari

#Kategori Umur :                      Harga Normal                      Harga di hari Rabu
#anak-anak (<12 tahun)                Rp. 25.000                        Rp. 20.000
#remaja (12-17 tahun)                 Rp. 35.000                        Rp. 35.000
#dewasa (>=18 tahun)                  Rp. 50.000                        Rp. 40.000

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
hari = input("Masukkan hari : ")

# Proses kategori umur
if umur < 3:
    kategori = "Balita"
    harga = 0
else:
    if umur < 12:
        kategori = "Anak-anak"
        if hari == "rabu":
            harga = 20000
        else:
            harga = 25000
    elif umur <= 17:
        kategori = "Remaja"
        if hari == "rabu":
            harga = 30000
        else:
            harga = 35000
    else:
        kategori = "Dewasa"
        if hari == "rabu":
            harga = 40000
        else:
            harga = 50000

# Output
print("Hasil Tiket")
print(f"Nama           : {nama}")
print(f"Umur           : {umur} tahun")
print(f"Kategori Umur  : {kategori}")
print(f"Harga Dibayar  : Rp. {harga:,}")