print ("----Status Kelulusan Ujian Mahasiswa----")
nama= (input("Nama : "))
mtk=int(input("Nilai Matematika :"))
bhsindo=int(input("Nilai Bahasa.indonesia :"))
ipa=int(input("Nilai Ipa :"))
if(mtk>0) and(bhsindo>0) and (ipa>0):
        print("Maaf input ada yang tidak valid")
elif (mtk>70) and(bhsindo>60) and (ipa>60):
     print("Selamat Kepada", nama, "Dinyatakan LULUS")
else:
    print("Atas Nama",nama,"Dinyatakan TIDAK LULUS")
