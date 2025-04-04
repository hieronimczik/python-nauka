# Gdy masz funkcję zagnieżdżoną w innej funkcji, nonlocal pozwala zmieniać zmienne z funkcji nadrzędnej (ale nie globalne!).

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x)

outer()  # 15

# Bez nonlocal, zmienna x w inner byłaby nową lokalną zmienną, a x w outer pozostałby bez zmian.