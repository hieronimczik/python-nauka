# slowniki

person = {
    "name": "Jan",
    "age": 30,
    "city": "Warszawa"
}
print(person["name"])  # Jan

person["job"] = "Programista" # dodawnie lementy
print(person)

# wyswietlanie samych kluczu
for key in person.keys():
    print(key)

# wyswietlanie samych wartosci
for value in person.values():
    print( value)

# wyswietlanie wszystkiego
for key, value in person.items():
    print(key, "->", value)

del person["city"] # usuniecie miasta