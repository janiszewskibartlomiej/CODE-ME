def dodaj_jawnie(a, b):
    wynik = a + b
    print(f'{a} + {b} = {wynik}')
    return wynik


if __name__ == '__main__':
    funkcja = dodaj_jawnie  # uwaga, nie ma nawiasów!

    print(type(funkcja))

    w = funkcja(13, 17)

    print(w)

    print("Czy to jest ten sam obiekt?", funkcja is dodaj_jawnie)
