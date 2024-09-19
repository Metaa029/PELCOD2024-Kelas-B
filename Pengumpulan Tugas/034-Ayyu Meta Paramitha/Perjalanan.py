print("Pada suatu hari terdapat dua orang sahabat yang ingin merencanakan liburan bersama.")
print("Meta: ")
orang1 = input(":")
print("Lusi: ")
orang2 = input(":")
tempat_wisata = input("Tempat wisata yang akan dikunjungi:")
tanggal_berangkat = input("Tanggal berangkat : ")
tanggal_kembali = input("Tanggal kembali : ")
jam_berangkat = input("Jam berangkat : ")
jam_kembali = input("Jam kembali : ")
jarak_tempuh = input("Jarak tempuh ke tempat wisata (dalam km): ")
waktu_tempuh = input("Waktu tempuh (dalam jam): ")

print("==============================================")
print(orang1, ": besok kita mau ke mana?")
print(orang2, ": kita akan ke", tempat_wisata)
print(orang1, ": kita berangkat kapan?")
print(orang2, ": kita berangkat pada tanggal", tanggal_berangkat, "pukul", jam_berangkat)
print(orang1, ": dan pulangnya?")
print(orang2, ": kita kembali pada tanggal", tanggal_kembali, "pukul", jam_kembali)
print(orang1, ": berapa jauh jaraknya?")
print(orang2, ": jaraknya sekitar", jarak_tempuh, "km")
print(orang1, ": berapa lama perjalanan?")
print(orang2, ": waktu tempuhnya sekitar", waktu_tempuh, "jam")

# Menghitung apakah waktu tempuh sesuai dengan jarak tempuh
jarak = float(jarak_tempuh)
waktu = float(waktu_tempuh)
rata_rata_kecepatan = jarak / waktu

hasil = tanggal_berangkat == tanggal_kembali
print("apakah tanggal berangkat sama dengan tanggal pulang")
print(hasil)

print(orang1, ": jadi rata-rata kecepatan kita adalah", rata_rata_kecepatan, "km/jam")
print(orang2, ": oke, jadi besok kita berangkat pagi-pagi.")
print(orang1, ": iya, mari kita siap-siap.")
print("Akhirnya mereka siap untuk liburan dan berangkat bersama ke", tempat_wisata)
