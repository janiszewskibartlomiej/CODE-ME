czlowiek = {'imie': 'Guido', 'nazwisko': 'van Rossum', 'programista': True}
print(czlowiek)

# dodajemy nowy klucz
czlowiek['rok_urodzenia'] = 1906
print(czlowiek)

# modyfikujemy istniejący klucz. Guido nie jest taki stary :)
czlowiek['rok_urodzenia'] = 1956
print(czlowiek)


# nie potrzebujemy tego pola
czlowiek.pop('programista')

# można też tak: (zakomentuj powyżej i odkomentuj poniżej)
# del czlowiek['programista']

print(czlowiek)
