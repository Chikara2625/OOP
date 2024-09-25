class gudang:
    def __init__(self):
        self.daftarBarang = []
        self.daftarKaryawan = []
        self.daftarkurir = []
        self.history = []

    def tambahBarang(self):
        Kode = input("Kode Barang\t: ")
        Nama = input("Nama Barang\t: ").lower()
        Jenis = input("Jenis Barang\t: ").lower()
        Quantity = int(input("Jumlah Barang\t: "))
        
        for item in self.daftarBarang:
            if item.nama == Nama:
                item.quantity += Quantity
                return
            
        newItem = barang(Kode, Nama, Jenis, Quantity)
        self.daftarBarang.append(newItem)
        
    def tambahKaryawan(self):
        Nik = input("NIK Karyawan\t:")
        Nama = input("Nama Karyawan\t:").lower()
        Gender = input("Gender\t:").lower()
        noHp = input("No.HP\t:")
        
        for person in self.daftarKaryawan:
            if person.nama == Nama:
                print(f"Registrasi Gagal, {Nama} Merupakan Karyawan")
                return
            
        newKaryawan = karyawan(Nik, Nama, Gender, noHp)
        self.daftarKaryawan.append(newKaryawan)

    def tambarKurir(self):
        newKurir = kurir()
        self.daftarkurir.append(newKurir)
        
    def listBarang(self):
        if(not self.daftarBarang):
            print("Gudang Kosong")
            return
        
        for i in range(len(self.daftarBarang)):
            print(f"{i + 1}. ", end="")
            self.daftarBarang[i].detail()
    
    def listKaryawan(self):
        if(not self.daftarKaryawan):
            print("Karyawan Tidak Ada")
            return
        
        for i in range(len(self.daftarKaryawan)):
            self.daftarKaryawan[i].detail()
    
    def listKurir(self):
        if(not self.daftarkurir):
            print("Kurir Tidak Ada")
            return
        
        for i in range(len(self.daftarkurir)):
            self.daftarkurir[i].detail()

class karyawan:
    def __init__(self, nik, nama, gender, noHp):
        self.nik = nik
        self.nama = nama
        self.gender = gender
        self.noHp = noHp

    def tambahBarang(self, namaBarang, quantity):
        namaBarang.tambah(quantity)

    def kurangBarang(self, namaBarang, quantity):
        namaBarang.kurang(quantity)

    def detail(self):
        print(f"NIK\t: {self.nik}")
        print(f"Nama\t: {self.nama}")
        print(f"Gender\t: {self.gender}")
        print(f"noHP\t: {self.noHp}")

class barang:
    def __init__(self, kode, nama, jenis, quantity):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.quantity = quantity
    
    def detail(self):
        print(f"Kode\t\t: {self.kode}")
        print(f"Nama\t\t: {self.nama.title()}")
        print(f"Jenis\t\t: {self.jenis.title()}")
        print(f"Quantity\t: {self.quantity}")

    def tambah(self, quantity):
        self.quantity += quantity
        print(f"Jumlah barang {self.nama} bertambah dari {self.quantity - quantity} menjadi {self.quantity}")

    def kurang(self, quantity):
        self.quantity -= quantity
        print(f"Jumlah barang {self.nama} bertambah dari {self.quantity + quantity} menjadi {self.quantity}")
