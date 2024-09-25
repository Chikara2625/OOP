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
        print("4. Tambah Barang")
        print("5. Barang Masuk")
        print("6. Barang Keluar")
        print("0. Keluar")
        n = int(input("Pilihan : "))
        if(n == 1):
            Gudang.listBarang()
        elif(n == 2):
            Gudang.listKaryawan()
        elif(n == 3):
            Gudang.listKurir()
        elif(n == 4):
            Gudang.tambahBarangBaru()
        elif(n == 5):
            Gudang.tambahBarang()
        elif(n == 6):
            Gudang.kurangBarang()
        input()

Gudang = gudang()
showMenu()