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
    
