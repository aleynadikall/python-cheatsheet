file = open("dosya.txt", "w") # w açmak ve yazmak için kullanılan dosya kipidir.

file.write("Naber Java")

file.close() #her dosya işlemi gerçekleştiğinde bunun yapilmasi gerekir.

#ekleme yapmak icin a kipini kullanırız.
file = open("dosya.txt", "a")

file.write("Naber Python\n")
file.write("Naber C++\n")
file.write("Naber React")

file.close()

"""
a kipi hem dosyayi olusturabilir hem de zaten var olan dosyaya ekleme yapabilir.
w kipi ile ekleme yapılmaz cünkü w kipi önceki dosya icerigini siler.
"""

# dosya okuma r kipi ile yapilir.
file = open("dosya.txt", "r")
veri = file.read()
print(veri)
file.close()

file = open("dosya.txt", "r")
veri2 = file.read(14) #Naber JavaNabe yazdirir.
print(veri2)
file.close()

file = open("dosya.txt", "r")
file.seek(10)  # 10 ileri atar oradan itibaren okumaya baslar.
veri3 = file.read(14) #Naber JavaNabe yazdirir.
print(veri3)
file.close()

# for dongusu ile dosyamizi okuyabiliriz.
file = open("dosya.txt", "r")
for satir in file:
    print(satir)
file.close()


