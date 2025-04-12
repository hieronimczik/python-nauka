# Zadanie 

class Zwierze():
    def __init__(self, imie, wiek, gatunek):
        self.imie = imie 
        self.wiek = wiek 
        self.gatunek = gatunek 
         
    def przedstaw_sie(self):
        print(f"Jestem {self.gatunek}, mam na imie {self.imie}, mam {self.wiek} lat")

class Pies(Zwierze):
    def szczekaj(self):
        print("Hau Hau")

class Kot(Zwierze): 
    def mialcz(self):
        print("Miau")

pies = Pies("Marian", 5, "pies")
kot = Kot("Bandi", 7, "kot")

pies.przedstaw_sie()
pies.szczekaj()
kot.przedstaw_sie()
kot.mialcz()
