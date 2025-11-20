# Program Daftar Nilai Mahasiswa

mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\n=== MENU DATA NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    # --- Tambah Data ---
    if pilihan == '1':
        nama = input("Nama Mahasiswa: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        akhir = hitung_nilai_akhir(tugas, uts, uas)
        mahasiswa[nama] = {'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
        print(f"✅ Data {nama} berhasil ditambahkan!")

    # --- Ubah Data ---
    elif pilihan == '2':
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        if nama in mahasiswa:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))
            akhir = hitung_nilai_akhir(tugas, uts, uas)
            mahasiswa[nama] = {'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
            print(f"✏️ Data {nama} berhasil diubah!")
        else:
            print("❌ Nama tidak ditemukan!")

    # --- Hapus Data ---
    elif pilihan == '3':
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        if nama in mahasiswa:
            del mahasiswa[nama]
            print(f"🗑️ Data {nama} berhasil dihapus!")
        else:
            print("❌ Nama tidak ditemukan!")

    # --- Tampilkan Data ---
    elif pilihan == '4':
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        print("Nama\t\tTugas\tUTS\tUAS\tAkhir")
        print("-"*40)
        for nama, nilai in mahasiswa.items():
            print(f"{nama}\t\t{nilai['tugas']}\t{nilai['uts']}\t{nilai['uas']}\t{nilai['akhir']:.2f}")

    # --- Cari Data ---
    elif pilihan == '5':
        nama = input("Masukkan nama mahasiswa yang dicari: ")
        if nama in mahasiswa:
            nilai = mahasiswa[nama]
            print(f"\nData {nama}")
            print(f"Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Akhir: {nilai['akhir']:.2f}")
        else:
            print("❌ Nama tidak ditemukan!")
            print("Harap masukkan nama dengan benar")

    # --- Keluar ---
    elif pilihan == '6':
        print("👋 Terima kasih! Program selesai.")
        break

    else:
        print("⚠️ Pilihan tidak valid, silakan coba lagi.")
