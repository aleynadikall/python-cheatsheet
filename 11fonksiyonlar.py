def selamla():
    print("Merhaba")
    print("Nasilsin?")


# Fonksiyonumuzu tanimladik.

selamla()  # Fonksiyonumuzu cagirdik.
selamla()
selamla()


def selamla2(isim):
    print("Merhaba", isim)


selamla2("Aleyna")


# Varsayilan deger atama

def selamla3(isim="İsimsiz"):
    print("Merhaba", isim)


selamla3()
selamla3("Aleyna")


def toplama(a, b, c):
    print("Toplam:", a + b + c)


toplama(3, 4, 5)

b = toplama(7, 8, 9)

print(b)  # 24 yazdirir ama degeri cagrildigi yere dondurulmedigi icin None oldu.


def toplama2(a, b, c):
    return a + b + c
#output firlatmak icin return kullanmamiz gerekir.

toplam = toplama2(7, 8, 9)

print(toplam)
