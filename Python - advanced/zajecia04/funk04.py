def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def podziel(a, b):
    return a / b


def kwadrat(a):  # nowa funkcja, jeden parametr
    return a ** 2


def uzyj_funkcji(fun, *args):
    # debug
    print('"args" zawiera:', args)

    nazwa = fun.__name__
    wynik = fun(*args)

    if len(args) == 1:
        print(f'{args[0]} {nazwa} = {wynik}')
    if len(args) == 2:
        print(f'{args[0]} {nazwa} {args[1]} = {wynik}')
    return wynik


if __name__ == '__main__':
    uzyj_funkcji(dodaj, 5, 7)
    uzyj_funkcji(kwadrat, 11)
