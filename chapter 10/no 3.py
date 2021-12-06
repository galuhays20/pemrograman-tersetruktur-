file = open('data.mhs.txt','a')
def inputMhs(myFile,nim,nama,alamat):
    data = open(myFile, "a")
    data.write("{}|{}|{}\n".format(nim,nama,alamat))
    data.close()
myFile = "data.mhs.txt"
jawab = "y"
while jawab == "y":
    nim = input('Masukkan NIM\t: ')
    nama = input('Masukkan Nama\t: ')
    alamat = input('Masukkan Alamat\t: ')
    inputMhs(myFile,nim,nama,alamat)
    jawab = input('\nUlangi input lagi (y/n) : ')
if jawab == "y":
    (myFile)
    


dataFile = open("data.mhs.txt", "r")

datalist = []

data = dataFile.readlines()

for i in range(len(data)):
    pecahData = data[i].split("|")
    dataDict = {'nim': pecahData[0],'nama': pecahData[1],'alamat': pecahData[2]}
    datalist.append(dataDict)
    
print(datalist)

dataFile.close()
