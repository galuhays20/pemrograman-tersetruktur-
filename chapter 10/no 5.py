data = open('databilangan.txt', 'r')
hasil = open('hasilbilangan.txt', 'w')

baca = data.readlines()

for i in range(len(baca)):
    bil = baca[i].replace('\n', '')
    bil2= bil.split("|")
    hasil.write(str(int(bil2[0])+int(bil2[1]))+'\n')
data.close()
hasil.close()
