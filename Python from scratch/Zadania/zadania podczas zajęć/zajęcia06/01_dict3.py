czlowiek = {'imie': 'Guido',
            'nazwisko': 'van Rossum',
            'rok_urodzenia': 1956}

for k in czlowiek:
    print('Klucz: {}, wartość: {}'.format(k, czlowiek[k]))

print()
# można też tak:

for k, w in czlowiek.items():
    print('Klucz: {}, wartość: {}'.format(k, w))

print()
# można jeszcze tak (ale nie polecam):

for krotka in czlowiek.items():
    print('Klucz: {}, wartość: {}'.format(krotka[0], krotka[1]))

