data = open('hasildata.txt','r')
hasil = open('datahasil.txt', 'a')

myFile = data.read()

mySet = set(myFile)

mySet.remove(' ')

myList = list(mySet)

myList.sort()

n = 2

file = myFile.replace(myList[0],chr(ord(myList[0])-n))

i = 1
while True:
    file = file.replace(myList[i],chr(ord(myList[i])-n))
    i+=1

    if(i==10):
        break
file =file.replace(chr(63), chr(89))
file =file.replace(chr(64), chr(90))

hasil.write(file)

data.close()
hasil.close()
