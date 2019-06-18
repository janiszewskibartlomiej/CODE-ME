def funkcja_liniowa(a, b):
    return lambda x: a * x + b


def funkcja_kwadratowa(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


def rysuj_funkcje(f, min, max):
    for x in range(min, max):
        # print(f(x))
        print(f'x: {x}\t y: {f(x)}')  # trochę ładniej


if __name__ == '__main__':
    konkretna_funkcja = funkcja_kwadratowa(2, -1, -6)

    rysuj_funkcje(konkretna_funkcja, -5, 5)
