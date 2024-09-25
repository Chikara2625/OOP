class gudang:
    def __init__(self):
        self.daftarBarang = []
        self.daftarKaryawan = []
        self.daftarCustomer = []
        self.daftarKurir = []

    def tambahBarangBaru(self):
        Kode = input("Kode Barang\t: ")
        Nama = input("Nama Barang\t: ").lower()
        Jenis = input("Jenis Barang\t: ").lower()
        Quantity = int(input("Jumlah Barang\t: "))
        newItem = barang(Kode, Nama, Jenis, Quantity)
        self.daftarBarang.append(newItem)
        
    def tambahKaryawan(self):
        Nik = input("NIK Karyawan\t:")
        Nama = input("Nama Karyawan\t:")
        Gender = input("Gender\t:").upper()
        noHp = input("No.HP\t:")
        newKaryawan = karyawan(Nik, Nama, Gender, noHp)
        self.daftarKaryawan.append(newKaryawan)

    def menambahkanKurir(self):
        id = input("Id Kurir: ")
        nama = input ("Nama: ")
        gender = input("Gender: ").upper()
        hp= input("No. hp: ")
        kurirBaru = kurir(id, nama, gender, hp)
        self.daftarKurir.append(kurirBaru)




    def listBarang(self):
        if(not self.daftarBarang):
            print("Gudang Kosong")
            return
        
        for i in range(len(self.daftarBarang)):
            self.daftarBarang[i].detail()
    
    def listKaryawan(self):
        for i in range(len(self.daftarKaryawan)):
            self.daftarKaryawan[i].detail()
    
    def listKurir(self):
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
        print(f"NIK\t\t: {self.nik}")
        print(f"Nama\t\t: {self.nama}")
        print(f"Gender\t\t: {self.gender}")
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

class kurir:
    def __init__(self, id, nama, gender, hp):
        self.idKurir = id
        self.namaKurir = nama
        self.genderKurir = gender
        self.hpKurir = hp
        # listKurir = []
    def detail(self):
        print(f"Kode\t\t: {self.idKurir}")
        print(f"Nama\t\t: {self.namaKurir.title()}")
        print(f"Gender\t\t: {self.genderKurir}")
        print(f"No. hp\t: {self.hpKurir}")
    # def menambahkanKurir(self, id, nama, gender, hp):
