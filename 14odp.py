class Account:
    def __init__(self, isim, numara, bakiye):  # objemizi olustururken cagirdigimiz ilk fonksiyon init'tir.
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye

    def hesapBilgileri(self):
        print("İsim: ", self.isim)
        print("Numara: ", self.numara)
        print("Bakiye: ", self.bakiye)

    def paraCek(self, miktar):
        if (self.bakiye - miktar < 0):
            print("Bakiyeniz yeterli degil....")
        else:
            self.bakiye -= miktar
            print("Yeni bakiye:", self.bakiye)

    def paraYatir(self, miktar):
        self.bakiye += miktar
        print("Yeni bakiye:", self.bakiye)


account = Account("Aleyna Dikal", 123456, 1000)
account.hesapBilgileri()
account.paraCek(1200)
account.paraCek(800)
account.paraYatir(200)
