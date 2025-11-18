print("🚗 Kalkulator Konsumsi Bensin 🚗")

def main():
    while True:
        print("\nPilih menu:")
        print("1. Hitung konsumsi bensin")
        print("2. Hitung jarak tempuh") 
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan (1-3): ")
        
        if pilihan == "1":
            try:
                jarak = float(input("Jarak tempuh (km): "))
                bensin = float(input("Bensin terpakai (liter): "))
                konsumsi = (bensin / jarak) * 100
                print(f"Konsumsi: {konsumsi:.2f} liter/100km")
            except:
                print("Input harus angka!")
                
        elif pilihan == "2":
            try:
                bensin = float(input("Jumlah bensin (liter): "))
                konsumsi = float(input("Konsumsi mobil (liter/100km): "))
                jarak = (bensin / konsumsi) * 100
                print(f"Jarak tempuh: {jarak:.2f} km")
            except:
                print("Input harus angka!")
                
        elif pilihan == "3":
            print("Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
