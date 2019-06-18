import random
from functools import wraps


def ramka(func):
    @wraps(func)  # ten dekorator "przepina" część atrybutów dekorowanej funkcji
    def dodaj_ramke(*args, **kwargs):
        print('--------------------------')
        wynik = func(*args, **kwargs)
        print('--------------------------')
        return wynik

    return dodaj_ramke


@ramka
def znaczki(ile_razy):
    """
    Funkcja drukująca losowy znaczek Unicode z arbitralnie wybranego przedziału
    https://en.wikipedia.org/wiki/Miscellaneous_Symbols
    """
    for _ in range(ile_razy):
        symbol = chr(random.randint(9728, 9760))
        print(symbol, end=' ')
    print()


if __name__ == '__main__':
    znaczki(5)

    print()

    print(znaczki.__name__)
    print(znaczki.__doc__)
