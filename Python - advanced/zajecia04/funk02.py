def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def podziel(a, b):
    return a / b


if __name__ == '__main__':
    lista_funkcji = [dodaj, odejmij, pomnoz, podziel]

    wybrana_funkcja = lista_funkcji[1]

    nazwa = wybrana_funkcja.__name__
    print(nazwa)

    a = 31
    b = 7
    wynik = wybrana_funkcja(a, b)
    print(f'{a} {nazwa} {b} = {wynik}')
