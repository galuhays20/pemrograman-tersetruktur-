from datetime import *

tglskrng = datetime.date(datetime.now())
tglkembali = tglskrng + timedelta(days=7)

myFile= open('data_perpus.txt', 'a+')

while True:
    kode = input('Masukkan Kode Member\t: ')
    nama = input('Masukkan Nama Member\t: ')
    judulBuku = input('Masukkan Judul Buku\t: ')

    data=kode + '|' + nama + '|'+ judulBuku + '|' + str(tglskrng) + '|'+ str(tglkembali) + '\n'
    myFile.write(data)

    lanjut = input('\nUlangi lagi (y/n) : ')
    print('')
    if lanjut in ('n', 'N'):
        myFile.close()
        break
        
