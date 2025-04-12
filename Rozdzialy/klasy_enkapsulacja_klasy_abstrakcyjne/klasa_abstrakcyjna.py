from abc import ABC, abstractmethod

# Klasa abstrakcyjna
class Zwierze(ABC):
    @abstractmethod
    def daj_glos(self):
        pass

# Przykładowa klasa potomna
class Pies(Zwierze):
    def daj_glos(self):
        return "Hau!"

class Kot(Zwierze):
    def daj_glos(self):
        return "Miau"

# Nie możesz stworzyć obiektu klasy Zwierze:
# zwierze = Zwierze()  # Błąd!

# Ale możesz używać klas potomnych:
pies = Pies()
print(pies.daj_glos())  # Hau!

kot = Kot()
print(kot.daj_glos())  # Miau
