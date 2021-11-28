import random
string = input('Masukkan String yang ingin dirubah : ')
looping = (int(input('Mau Berapa Kali? ')))
def shuffleString(x, n):
    listString = list()
    while True:
        i = ''.join(random.sample(string, len(string)))
        if i in listString:
            continue
        else:
            listString.append(i)
            n-=1
            if n==0:
                print(listString)
                break

print('randomString(', string, looping,') -> ', end='')
shuffleString(string, looping)
