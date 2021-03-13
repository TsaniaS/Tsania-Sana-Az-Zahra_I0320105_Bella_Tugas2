#menampilkan informasi program
print("Selamat Datang di Program Hitung")

print("")
print("Menghitung Luas Persegi Panjang")

#input nilai panjang
panjang = float(input("Masukkan panjang: "))

#input nilai lebar
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar
print("Luas persegi panjang adalah", luas, "satuan")

print("==================================================")

print ("")
print("Menghitung Luas Lingkaran")

#input nilai jari-jari
jari_jari = float(input("Masukkan jari-jari: "))
phi = 3.14

luaslingkaran = jari_jari * jari_jari * phi
print("Luas lingkaran adalah", luaslingkaran, "satuan")

print("==================================================")

print("")
print("Menghitung Luas Permukaan Kubus")

#input nilai panjang sisi
sisi = float(input("Masukkan panjang sisi: "))

LuasPermukaanKubus = 6 * sisi * sisi
print("Luas permukaan kubus adalah", LuasPermukaanKubus, "satuan")

print("==================================================")

print("")
print("Konversi Suhu Celcius ke Fahrenheit")

#input suhu dalam celcius
C = float(input("Masukkan suhu dalam °C = "))
F = ((9/5)*C) + 32
print("Suhu dalam °F = ", F, "°F" )

print("==================================================")

print("")
print("Konversi Suhu Reamur ke Fahrenheit")

#input suhu dalam Reamur
R = float(input("Memasukkan suhu dalam °R = "))
K = ((5/4)*R) + 273
print("Suhu dalam °K = ", K, "°K")

print("")
print("Yey anda sudah berada di akhir program!")