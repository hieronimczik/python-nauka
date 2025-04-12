# Zadanie 1 
class Samochod(): 
    def __init__(self, przebieg):
        self.__przebieg = przebieg

    def odczytaj_przebieg(self):
        print(f"Przebieg pojazdu: {self.__przebieg} km")

    def dodaj_przebieg(self, ilosc): 
        self.__przebieg += ilosc 
        print(f"Nowy przebieg pojazdu: {self.__przebieg} km")

pojazd = Samochod(125)
pojazd.odczytaj_przebieg()
pojazd.dodaj_przebieg(15)

# Zadanie 2 

from abc import ABC, abstractmethod

class Zwierze(ABC): 
    @abstractmethod 
    def wydaj_dzwiek(self): 
        pass

class Pies(Zwierze): 
    def wydaj_dzwiek(self):
        print("Hau hau") 

class Kot(Zwierze): 
    def wydaj_dzwiek(self):
        print("Miau")

p = Pies()
p.wydaj_dzwiek()
k = Kot()
k.wydaj_dzwiek()

# Zadanie 3 

class Produkt(): 
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa 
        self.cena = cena 

class Elektronika(Produkt): 
    def __init__(self,nazwa,cena,gwarancja):
        super().__init__(nazwa,cena)
        self.gwarancja = gwarancja