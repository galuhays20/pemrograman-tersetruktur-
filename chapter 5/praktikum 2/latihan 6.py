from random import randint

angka = randint(1, 100)
score = 100

print("Hai.. nama saya galuhayu, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")


while(True):

    jwb = int(input("Tebakan Kamu: "))
    if (jwb > angka):
        print("Hehehe… Bilangan tebakan anda terlalu besar")
        score -= 2
    elif (jwb < angka):
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
        score -= 2
    else:
        print("Tebakan kamu benar!!")
        print("Skor Kamu adalah", score)
        break
    if (score < 0):
        score = 0
