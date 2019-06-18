def funkcja_liniowa(a, b):
    return lambda x: a * x + b


konkretna_funkcja = funkcja_liniowa(2, -3)

wynik = konkretna_funkcja(5)
print(wynik)

wynik = konkretna_funkcja(6)
print(wynik)

wynik = konkretna_funkcja(7)
print(wynik)
