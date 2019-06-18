def daj_funkcje_dodajaca_nawiasy(znak):
    def dodaj_nawiasy(a, b):
        return f'({a} {znak} {b})'

    return dodaj_nawiasy


if __name__ == '__main__':
    dodaj_nawiasy_x = daj_funkcje_dodajaca_nawiasy('x')

    print(dodaj_nawiasy_x.__closure__)
    print(dodaj_nawiasy_x.__closure__[0].cell_contents)  # da się dostać do zapisanych danych

    dodaj_nawiasy_x.__closure__[0].cell_contents = '$$$'  # a nawet modyfikować!

    zapis = dodaj_nawiasy_x(13, 17)

    print(zapis)
