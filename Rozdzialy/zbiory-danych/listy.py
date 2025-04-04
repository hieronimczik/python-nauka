#listy 


owoce = ["jabłko", "banan", "pomarancza"] # inicjowanie listy
print(owoce[0])  # wyswietlanie indexu 0 czyli pierwszego elementy listy , wypisze: jabłko

owoce.append("śliwka") # dodanie nowej wartosci do listy
print(owoce) # wyswietli cala liste

owoce.remove("jabłko") # usuniecie wartosci z listy
print(owoce)

owoce.pop() # usuniecie ostatniego elementu listy
print(owoce)

print(len(owoce))   # liczba elementów

if "kiwi" in owoce:          # sprawdzenie obecności
    print("jest w liscie")
else: 
    print("nie ma")

for fruit in owoce: # petla po liscie
    print(fruit)