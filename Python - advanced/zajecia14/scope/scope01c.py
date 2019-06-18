LICZNIK = 0


def powieksz_licznik():
    global LICZNIK

    LICZNIK += 1


if __name__ == '__main__':
    print(LICZNIK)

    powieksz_licznik()
    powieksz_licznik()
    powieksz_licznik()

    print(LICZNIK)
