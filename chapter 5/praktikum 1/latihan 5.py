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
        continue

    statMenikah = int(input("Masukkan Status (1: Menikah, 2: Belum): "))

    if (statMenikah == 1):
        status = "Menikah"
        tunjMenikah = 10 / 100 * gajiPokok
        jumAnak = int(input("Masukkan jumlah Anak  : "))
        tunjAnak = 5 / 100 * gajiPokok
        tunjAnak = tunjAnak * jumAnak
        break
    elif (statMenikah == 2):
        status = "Belum Menikah"
        tunjMenikah = 0
        tunjAnak = 0
        jumAnak = "-"
        break
    else:
        print("Status Menikah Tidak Valid")

gajiKotor = gajiPokok + tunjMenikah + tunjAnak
potongan = persen / 100 * gajiKotor
gajiBersih = gajiKotor - potongan

print("=====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-------------------------------------")
print("Nama Karyawan    : " + namaKar + " (Kode : " + kodeKar + ")")
print("Golongan         : " + golKar)
print("Status Menikah   : " + status)
print("Jumlah Anak      : " + str(jumAnak))
print("-------------------------------------")
print("Gaji Pokok       : Rp.", gajiPokok)
print("Tunjangan Menikah: Rp.", int(tunjMenikah))
print("Tunjangan Anak   : Rp.", int(tunjAnak))
print("-------------------------------------")
print("Gaji Kotor       : Rp.", int(gajiKotor))
print("Potongan (" + str(persen) + "%)  : Rp.", int(potongan))
print("-------------------------------------")
print("Gaji Bersih      : Rp.", int(gajiBersih))
print("-------------------------------------")
