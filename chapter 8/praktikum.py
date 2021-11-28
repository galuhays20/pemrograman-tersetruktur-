#nomer 1
print('list a dan b')
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('a =',a)
print('b =',b)

#nomer 2
#Menyisipkan angka pada list a dan b
a.insert(3, 10)
b.insert(2, 15)
print('setelah disisipi angka')
print('a =', a)
print('b =', b)

#nomer 3
#Menyisipkan angka pada list a dan b
a.append(4)
b.append(8)
print('setelah disisipi angka')
print('a =', a)
print('b =', b)

#nomor 4
#Mengurutkan list a dan b secara ascending
a.sort()
b.sort()
print('setelah sorting  ascending')
print('a =', a)
print('b =', b)

#nomor 5
#Mendefinisikan list c yang elemennya dari sublist a[0-7]
#Mendefinisikan list d yang elemennya dari sublist b[2-9]
c = a[:8]
d = b[2:10]
print('mendefinisikan list c dan d')
print('c =', c)
print('d =', d)

#nomor 6
#penjumlahan  elemen c dan d
print('penjumlahan elemen c dan d = e ')
hasil=[]
hasil=[]
if len(c) == len(d):
    for i in range(len(c)):
        baris=c[i]+d[i]
        hasil.append(baris)
    print('e = ',hasil)

#nomor 7
#list bentuk tuple
print('list a bentuk tuple')
list_e = hasil
tuple_e = tuple(hasil)
print('e =',tuple_e)

#nomor 8
#nilai minimum dari elemen tuple_e
print('Nilai minimum dari tuple', tuple_e, 'adalah', min(tuple_e))
#nilai maximum dari elemen tuple_e
print('Nilai maximum dari tuple', tuple_e, 'adalah', max(tuple_e))
#penjumlah seluruh elemen tuple_e
print('Jumlah seluruh elemen tuple', tuple_e, 'adalah', sum(tuple_e))

#nomor 9
#Variabel myString
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)

#nomor 10
#Melihat karakter huruf penyusun myString
print
huruf = set(myString)
print('Huruf penyusun =', huruf)

#nomor 11
#Mengurutkan himpunan karakter huruf berdasarkan alfabet
list_huruf = list(huruf)
list_huruf.sort()
print('Setelah diurutkan alfabet', list_huruf)
       
