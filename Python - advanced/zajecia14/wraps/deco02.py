import random


def ramka(func):
    def dodaj_ramke(*args, **kwargs):
        print('--------------------------')
        wynik = func(*args, **kwargs)
        print('--------------------------')
        return wynik

    # porawione, ale jest to niezbyt eleganckie...
    dodaj_ramke.__name__ = func.__name__
    dodaj_ramke.__doc__ = func.__doc__

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
