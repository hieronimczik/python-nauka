# Dziedziczenie pozwala stworzyć nową klasę na bazie innej, czyli „dziedziczyć” funkcje i zmienne.

# Masz klasę Zwierze – ogólną

# Tworzysz klasę Pies, która dziedziczy po Zwierze

# Pies automatycznie ma wszystko co Zwierze, ale możesz dodać coś od siebie
class Rodzic:
    # coś tutaj
    pass

class Dziecko(Rodzic):
    # coś tutaj
    pass

#Klasa dzieczko moze:
# - używać metod i atrybutów klasy rodzica

# - nadpisywać metody, jeśli potrzebuje zachować się inaczej

# - dodać nowe metody/atrybuty tylko dla siebie