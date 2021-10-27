kode= input("Masukkan Kode Karyawan : ")
nama= input("Masukkan Nama Karyawan : ")
while(True):
    gol= str(input("Masukkan Golongan : "))
    if (gol=="A") or (gol=="a"):
        gjp= 10000000
        pot= 2.5
        break
    elif (gol=="B") or (gol=="b"):
        gjp= 8500000
        pot= 2.0
        break
    elif (gol=="C") or (gol=="c"):
        gjp= 7000000
        pot= 1.5
        break
    elif (gol=="D") or (gol=="d"):
        gjp= 5500000
        pot= 1.0
        break
    else:
        print("Golongan Tidak Valid")
pot2= pot/100*gjp
gaji= gjp-pot2
print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-------------------------------------")
print("Nama Karyawan         : ", nama, "( Kode : ", kode, ")")
print("Golongan              : ", gol)
print("-------------------------------------")
print("Gaji Pokok            : Rp.", gjp)
print("Potongan (", pot, "%)     : Rp.",int(pot2))
print("-------------------------------------")
print("Gaji Bersih           : Rp.", int(gaji))
