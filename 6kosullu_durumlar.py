yas = int(input("Yasinizi girin:"))

if yas < 18:
    print("Mekana giremezsiniz!")
else:
    print("Hosgeldiniz :)")

islem = int(input("İslemi Giriniz:"))

if islem == 1:
    print("İslem 1'i sectiniz...")
elif islem == 2:
    print("İslem 2'yi sectiniz...")
else:
    print("Gecersiz islem...")