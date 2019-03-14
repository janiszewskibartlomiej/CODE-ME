def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def podziel(a, b):
    return a / b


def uzyj_funkcji(fun, a, b):
    nazwa = fun.__name__
    wynik = fun(a, b)
    print(f'{a} {nazwa} {b} = {wynik}')
    return wynik


if __name__ == '__main__':
    uzyj_funkcji(odejmij, 11, 17)
