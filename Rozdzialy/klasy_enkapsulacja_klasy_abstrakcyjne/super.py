# Funkcja super() pozwala odwołać się do metody lub konstruktora klasy bazowej,
#  np. żeby nie duplikować kodu przy dziedziczeniu.
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

class Student(Osoba):
    def __init__(self, imie, wiek, uczelnia):
        super().__init__(imie, wiek)  # wywołanie konstruktora Osoba
        self.uczelnia = uczelnia

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, mam {self.wiek} lat i studiuje na {self.uczelnia}.")


s = Student("Bartek", 22, "UJ")
s.przedstaw_sie()
