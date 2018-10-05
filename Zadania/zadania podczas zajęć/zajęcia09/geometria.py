def pole_prostokonta(a, b):
    if a < 0 or b < 0:
        return None
    else:
        pole = a * b
        return pole


WARTOSC_PI = 3.14


def pole_kola(r):
    if r >= 0:
        pole = WARTOSC_PI * r ** 2
        return pole
    else:
         return None