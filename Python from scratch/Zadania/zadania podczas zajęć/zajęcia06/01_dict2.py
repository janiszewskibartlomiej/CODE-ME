czlowiek = {'imie': 'Guido',
            'nazwisko': 'van Rossum',
            'rok_urodzenia': 1906}

for k in czlowiek.keys():
    print(k)

print()

print(czlowiek.keys())  # to jest specjalny obiekt "dict_keys", ułatwiający iterację
print(list(czlowiek.keys()))  # można zrobić zwykłą listę z "dict_keys"

print()

for wartosc in czlowiek.values():
    print(wartosc)

print()

print(czlowiek.values()) # to jest specjalny obiekt "dict_values", ułatwiający iterację
print(list(czlowiek.values()))  # można zrobić zwykłą listę z "dict_values"
