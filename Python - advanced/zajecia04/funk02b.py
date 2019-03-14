import random


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

    wybrana_funkcja = random.choice(lista_funkcji)

    a = 31
    b = 7
    nazwa = wybrana_funkcja.__name__
    wynik = wybrana_funkcja(a, b)
    print(f'{a} {nazwa} {b} = {wynik}')
