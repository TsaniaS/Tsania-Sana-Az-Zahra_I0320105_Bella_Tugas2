print("         BIODATA          ")
#Data Pribadi
Nama = "Nama : Tsania Sana Az Zahra"
NIM = "NIM : I0320105"
Kelas = "Kelas : C"
Prodi = "Prodi : Teknik Industri"
Fakultas = "Fakultas : Teknik"
Universitas = "Universitas : Universitas Sebelas Maret"
print("Data Pribadi\n", Nama, "\n", NIM, "\n", Kelas, "\n", Prodi,"\n", Fakultas, "\n", Universitas)
print("")

#Alamat Rumah
Jalan = "Jl.Mahesa Jenar No. 18"
RT = '04'
RW = '01'
Desa = "Gentan"
Kecamatan = "Baki"
Kabupaten = "Sukoharjo"
print("Alamat\n", Jalan,",", RT, "/", RW, ",", Desa, ",", Kecamatan, ",", Kabupaten)
print("")

#Tinggi Badan
Tinggi = float((5*100)-345.2)
print("Tinggi saya adalah", Tinggi, "cm")

#Berat Badan
Berat = float((3*150)-(198.7*2))
print("Berat badan saya adalah", Berat, "kg")
print("")

#Kelahiran
TanggalLahir = int(153/9)
BulanLahir = int(2560/320)
TahunLahir = int(1001*2)
print("Tanggal lahir saya yaitu", TanggalLahir, "-", BulanLahir, "-", TahunLahir)

#Umur
TanggalSekarang = 12
BulanSekarang = 3
TahunSekarang = 2021

Umur = (TanggalSekarang - TanggalLahir) + ((BulanSekarang - BulanLahir)*30) + ((TahunSekarang - TahunLahir)*365)
Hari = int(((Umur)%365)/30)
Bulan = int(((Umur)%365)/30)
Tahun = int ((Umur)/365)
print("Umur saya adalah", Tahun, "tahun,", Bulan, "bulan, dan",  Hari, "hari")
print("")

#Ukuran Sepatu
UkuranSepatu = int(3627/93)
print("Ukuran sepatu saya adalah", UkuranSepatu)



