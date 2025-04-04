# zbiory

colors = {"czerwony", "zielony", "niebieski"}
colors.add("żółty")
colors.add("czerwony")  # nie zostanie dodany drugi raz
print(colors)

# operacje na zbiorach 

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # suma -> {1, 2, 3, 4, 5}
print(a & b)   # część wspólna -> {3}
print(a - b)   # różnica -> {1, 2}


# Usuwanie elementów ze zbiorów

# REMOVE
colors.remove("zielony") # usuniecie elementu zielony
print(colors) 

#colors.remove("różowy")  # ❌ KeyError – bo go nie ma!

# DISCARD
colors.discard("niebieski")
colors.discard("turkusowy")  # nie ma? trudno, program leci dalej

# POP
element = colors.pop() # Usuwa losowy element bo w zbiorach nie ma kolejnosci
print("Usunięto:", element)

# CLEAR 
colors.clear() # usuwa wszystkie elementy
print(colors)  # set()
