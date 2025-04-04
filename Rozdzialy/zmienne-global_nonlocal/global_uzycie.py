counter = 0

# Jeśli chcesz zmienić globalną zmienną wewnątrz funkcji, musisz użyć słowa kluczowego global.
def add_one():
    global counter
    counter += 1

add_one()
print(counter)  # 1

# Bez global, Python uzna, że counter to nowa lokalna zmienna i rzuci błąd UnboundLocalError.