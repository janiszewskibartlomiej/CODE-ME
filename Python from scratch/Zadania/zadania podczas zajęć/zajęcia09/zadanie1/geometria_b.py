WARTOSC_PI = 3.14


def pole_prostokata(a, b=None):
    if b is None:
        b = a
    if a < 0 or b < 0:
        raise ValueError('Bok prostokąta nie może mieć ujemnej długości.')
    return a * b


def pole_kola(r):
    if r < 0:
        raise ValueError('Promień koła nie może mieć ujemnej długości.')
    return WARTOSC_PI * r ** 2
