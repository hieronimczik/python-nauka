# Zadanie 1

lista = ["mango", "paluszki"]
lista.append("popcorn")
lista.remove("mango")

print("Lista zakupów")
for i in range(len(lista)):
    print(f"{i+1}. {lista[i]}")

# Zadanie 2

dane = {
    "imie": "Fabian",
    "wiek": 19,
    "miasto": "Bełk"
}

for key, value in dane.items():
    print(f"{key}, {value}")

# Zadanie 3

dni = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
for value in dni:
    print(value)

#Zadanie 4

gry1 = {"CS2", "Minecraft", "Clash Royal", "Dream League Soccer"}
gry2 = {"CS2", "Fortnite", "Clash Royal", "Timberman"}

wspolne = gry1 & gry2
print("Wspólne:")
for value in wspolne:
    print(f"- {value}")

rozne = gry1 - gry2
print("Różne:")
for value in rozne:
    print(f"- {value}")