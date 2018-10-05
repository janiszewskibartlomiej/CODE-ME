def rysuj_prostokont(a, b, znak='X'):
    for index in range(a):
        print(znak * b)


rysuj_prostokont(3, 5)

print()


def rysuj_prostokont(a, b, znak='#'):
    for index in range(a):
        print(znak * b)


rysuj_prostokont(4, 6)
print()
notacja = (5, 4)

rysuj_prostokont(*notacja)

slownik = {'a': 3, 'b': 4}
print()

rysuj_prostokont(**slownik)

