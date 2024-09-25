from database import barang
from database import karyawan
from database import gudang

def showMenu():
    while(True):
        print("Program Pengolahan Gudang")
        print("Menu : ")
        print("1. Daftar Barang")
        print("2. Daftar Karyawan")
        print("3. Daftar Kurir")
        print("4. Tambah Karyawan")
        print("5. Tambah Kurir")
        print("6. Barang Masuk")
        print("7. Barang Keluar")
        print("8. Lihat Riwayat")
        print("0. Keluar")
        n = int(input("Pilihan : "))
        if(n == 1):
            Gudang.listBarang()
        elif(n == 2):
            Gudang.listKaryawan()
        elif(n == 3):
            Gudang.listKurir()
        elif(n == 4):
            Gudang.tambahKaryawan()
        elif(n == 5):
            Gudang.tambahKurir()
        elif(n == 6):
            Gudang.tambahBarang()
        elif(n == 7):
            Gudang.kurangBarang()
        elif(n == 8):
            Gudang.riwayat()
        elif(n == 0):
            break
        else:
            print("Menu Tidak Ditemukan")
        input("Spasi Untuk Melanjutkan ")

Gudang = gudang()
showMenu()