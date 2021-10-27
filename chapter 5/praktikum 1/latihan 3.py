print ("======Status Kelulusan Ujian Mahasiswa======")
nama= (input("Nama : "))
mtk=int(input("Nilai Matematika :"))
bhsindo=int(input("Nilai Bahasa.indonesia :"))
ipa=int(input("Nilai Ipa :"))
if (mtk<0) or (bhsindo<0) or (ipa<0) or (mtk>100) or (bhsindo>100) or (ipa>100):
        print("Maaf input ada yang tidak valid")
elif (mtk>70) and(bhsindo>60) and (ipa>60):
     print("Status kelulusan", nama, "Dinyatakan LULUS")
else:
    print("Status kelulusan", nama,"Dinyatakan TIDAK LULUS")
    print("sebab")
    if (mtk<70):
        print("nilai matematika kurang dari 70")
    if(bhsindo<60):
        print("nilai bahasa indonesia kurang dari 60")
    if(ipa<60):
        print("nilai ipa kurang dari 60")

