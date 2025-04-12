# Zadanie 1 

class Zwierze:
    def __init__(self, gatunek, wiek):
        self.gatunek = gatunek 
        self.wiek = wiek 
    
    def przedstaw_sie(self):
        print(f"Jestem {self.gatunek}, mam {self.wiek} lat.")

zwierzak = Zwierze("Małpa", 10)
zwierzak.przedstaw_sie()


# Zadanie 2 

class BankKonto():
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo 

    def wplac(self, kwota):
        self.saldo += kwota 

    def wyplac(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota 
            print(f"Wypłacono ") 
    
    def pokaz_saldo(self):
        print(f"Saldo konta {self.saldo}, wlasciciel {self.wlasciciel}")

konto = BankKonto("Oliwier H", 500)
konto.wplac(15)
konto.wyplac(5)
konto.pokaz_saldo()

# Zadanie 3 

class Postac(): 
    def __init__(self, nick, hp, atak):
        self.nick = nick
        self.hp = hp 
        self.atak = atak

    def atakuj(self, cel):
        cel.hp -= self.atak 
        if cel.hp <= 0:
            print(f"Postac {cel.nick} nie zyje, zostal zabity przez {self.nick}")
        else:
            print(f"{cel.nick} zostal zaatakowany  przez {self.nick}, zadal mu {self.atak}. {cel.nick} ma {cel.hp}")

gracz1 = Postac("Gracz1", 100, 60)
gracz2 = Postac("Gracz2", 100, 15)

gracz1.atakuj(gracz2)
gracz1.atakuj(gracz2)