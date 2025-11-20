# Buat Dictionary daftar kontak
kontak = {
    "Fijar": "081267888",
    "Diaz": "087677776"
}

# menampilkan kontak Fijar
print("Kontak Fijar:", kontak["Fijar"])

# menambah kontak baru Rizz
kontak["Rizz"] = "087654544"

# mengubah nomor Fijar
kontak["Fijar"] = "088999776"

# menampilkan semua nama
print("Daftar Nama:", kontak.keys())

# menampilkan semua nomor
print("Daftar Nomor:", kontak.values())

# menampilkan semua nama dan nomornya
print("Daftar Kontak:")
for nama, nomor in kontak.items():
    print(nama, ":", nomor)

# menghapus kontak Fijar
del kontak["Fijar"]

# menampilkan setelah Fijar dihapus
print("Daftar Kontak setelah Fijar dihapus:", kontak)
