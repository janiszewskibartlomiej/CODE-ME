def funkcja_liniowa(a, b):
    return lambda x: a * x + b


konkretna_funkcja = funkcja_liniowa(2, 1)

print(konkretna_funkcja)

wynik = konkretna_funkcja(5)
print(wynik)

wynik = konkretna_funkcja(6)
print(wynik)

wynik = konkretna_funkcja(7)
print(wynik)
