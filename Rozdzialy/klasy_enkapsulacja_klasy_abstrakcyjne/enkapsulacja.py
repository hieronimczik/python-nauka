# _zmienna → konwencja: traktuj jako prywatną
# __zmienna → zmienna staje się trudniej dostępna (name mangling)

class KontoBankowe:
    def __init__(self, imie, saldo):
        self.imie = imie
        self.__saldo = saldo  # prywatne

    def wplac(self, kwota):
        self.__saldo += kwota

    def wyplac(self, kwota):
        if kwota <= self.__saldo:
            self.__saldo -= kwota
        else:
            print("Za mało środków!")

    def pokaz_saldo(self):
        return self.__saldo


konto = KontoBankowe("Ala", 1000)
konto.wplac(500)
konto.wyplac(300)
print(konto.pokaz_saldo())  # 1200
