def funkcja_liniowa(a, b):
    return lambda x: a * x + b


def rysuj_funkcje(f, min, max):
    for x in range(min, max):
        # print(f(x))
        print(f'x: {x}\t y: {f(x)}')  # trochę ładniej


if __name__ == '__main__':
    konkretna_funkcja = funkcja_liniowa(2, -3)

    rysuj_funkcje(konkretna_funkcja, -5, 5)
