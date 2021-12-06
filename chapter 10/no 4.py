dataFile = open("data.mhs.txt", "r")
datalist = []
data = dataFile.readlines()

for x in range(len(data)):
    pecahData = data[x].split("|")
    dataDict = {'nim': pecahData[0],'nama': pecahData[1],'alamat': pecahData[2]}
    datalist.append(dataDict)
    

while True:
    kunci = input('masukkan nim yang ingin dicari :')

    for i in range(len(datalist)):
        if kunci in datalist[i]['nim']:
            print()
            print('Data Mahasiswa')
            print('NIM :'+str(datalist[i]['nim']))
            print('NAMA :'+str(datalist[i]['nama']))
            print('ALAMAT :'+str(datalist[i]['alamat']))
            
    if kunci not in datalist[0]['nim']:
        if kunci not in datalist[1]['nim']:
            if kunci not in datalist[2]['nim']:
                print("\"Data mahasiswa tidak ditemukan\"")

    print()
    ulang = input('ingin mengulang (y/n) ?')
    print()
    if ulang in ('N', 'n'):
        print('Terimakasih telah mencoba')
        break
print(datalist)
dataFile.close()
