#membuka dan mau membaca file d:/data.txt
file= open("d:/data.txt", "r")

#baca baris pertama dari file
#simpan kedalam variable bil1 sbg integer
bil1 = int(file.readline())

#baca baris pertama dari file
#simpan ke dalam variabel bil2 sbg integer
bil2 = int(file.readline())

#hitung dan tampilkan hasil bagi
hasil = bil1/bil2
print(bil1,'dibagi',bil2,'sama dengan',hasil)
