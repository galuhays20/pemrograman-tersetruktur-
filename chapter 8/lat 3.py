banyak = int(input('Berapa banyak nama yang ingin dimasukan: '))
list_nama = []
for i in range(banyak):
        nama = input('Masukkan nama ke-' + str(i+1) + ': ')
        list_nama.append(nama)
list_nama.sort()
print('========================================')
for nama in list_nama:
        print(nama, '(', len(nama), 'karakter )')

