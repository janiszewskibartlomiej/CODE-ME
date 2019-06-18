LICZNIK = 0


def powieksz_licznik():
    LICZNIK += 1  # to nie zadziała!


if __name__ == '__main__':
    print(LICZNIK)

    powieksz_licznik()
    powieksz_licznik()
    powieksz_licznik()

    print(LICZNIK)
