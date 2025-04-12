class Samochod: # tworzenie klasy
    pass

moj_samochod = Samochod() # tworzenie obiektu 
print(type(moj_samochod))

# To specjalna metoda, która uruchamia się automatycznie, gdy tworzysz obiekt (__init__).
class Owoc:
    def __init__(self, kolor, ksztalt):
        self.kolor = kolor 
        self.ksztalt = ksztalt
# self to odniesienie do konkretnego obiektu. Zawsze pierwsze w metodach.

owoc1 = Owoc("czerwony", "okrągły")
print(owoc1.kolor)
print(owoc1.ksztalt)

# przyklad klasy
class Samochod2:
    def __init__(self, marka, kolor):
        self.marka = marka 
        self.kolor = kolor 

    def przedstaw_sie(self):
        print(f"Jestem samochodem marki: {self.marka}")

autko = Samochod2("Audi", "Czarny")
autko.przedstaw_sie()

# przyklad pelnej klasy
class Gracz:
    def __init__(self, nick, hp):
        self.nick = nick
        self.hp = hp

    def pokaz_info(self):
        print(f"{self.nick} ma {self.hp} punktów życia.")

    def otrzymaj_obrazenia(self, dmg):
        self.hp -= dmg
        print(f"{self.nick} otrzymał {dmg} obrażeń.")

g1 = Gracz("Gracz", 100)
g1.pokaz_info()
g1.otrzymaj_obrazenia(25)
g1.pokaz_info()
