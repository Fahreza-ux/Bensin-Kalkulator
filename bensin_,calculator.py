import os
from datetime import datetime

print("🚗 Kalkulator Konsumsi Bensin 🚗")

# File untuk menyimpan history
HISTORY_FILE = "history_bensin.txt"

def simpan_history(menu, data1, data2, hasil):
    """Menyimpan history perhitungan ke file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        if menu == "1":
            file.write(f"{timestamp} | Konsumsi | Jarak: {data1}km, Bensin: {data2}L -> {hasil}L/100km\n")
        else:
            file.write(f"{timestamp} | Jarak Tempuh | Bensin: {data1}L, Konsumsi: {data2}L/100km -> {hasil}km\n")

def baca_history():
    """Membaca dan menampilkan history"""
    if not os.path.exists(HISTORY_FILE):
        print("📝 Belum ada history")
        return
    
    print("\n📜 HISTORY PERHITUNGAN:")
    print("=" * 50)
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines[-10:]:  # Tampilkan 10 entry terakhir
            print(line.strip())
    print("=" * 50)

def hapus_history():
    """Menghapus semua history"""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("✅ History berhasil dihapus")
    else:
        print("📝 Tidak ada history untuk dihapus")

def main():
    while True:
        print("\nPilih menu:")
        print("1. Hitung konsumsi bensin")
        print("2. Hitung jarak tempuh") 
        print("3. Lihat history")
        print("4. Hapus history")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan (1-5): ")
        
        if pilihan == "1":
            try:
                jarak = float(input("Jarak tempuh (km): "))
                bensin = float(input("Bensin terpakai (liter): "))
                konsumsi = (bensin / jarak) * 100
                print(f"📊 Konsumsi: {konsumsi:.2f} liter/100km")
                
                # Simpan ke history
                simpan_history("1", jarak, bensin, f"{konsumsi:.2f}")
                
            except:
                print("❌ Input harus angka!")
                
        elif pilihan == "2":
            try:
                bensin = float(input("Jumlah bensin (liter): "))
                konsumsi = float(input("Konsumsi mobil (liter/100km): "))
                jarak = (bensin / konsumsi) * 100
                print(f"📍 Jarak tempuh: {jarak:.2f} km")
                
                # Simpan ke history
                simpan_history("2", bensin, konsumsi, f"{jarak:.2f}")
                
            except:
                print("❌ Input harus angka!")
                
        elif pilihan == "3":
            baca_history()
            
        elif pilihan == "4":
            konfirmasi = input("Yakin hapus semua history? (y/n): ")
            if konfirmasi.lower() == 'y':
                hapus_history()
                
        elif pilihan == "5":
            print("👋 Terima kasih!")
            break
            
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()
