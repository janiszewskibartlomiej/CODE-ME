def daj_funkcje_dodaj_nawiasy(znak):
    def dodaj_nawiasy(a, b):
        return f'({a} {znak} {b})'

    return dodaj_nawiasy


if __name__ == '__main__':
    dodaj_nawiasy_x = daj_funkcje_dodaj_nawiasy('x')

    zapis = dodaj_nawiasy_x(13, 17)

    print(zapis)
