LICZNIK = {'wartosc': 0}


def powieksz_licznik():
    LICZNIK['wartosc'] += 1  # to zadziała, ale nie jest zbyt eleganckie


if __name__ == '__main__':
    print(LICZNIK['wartosc'])

    powieksz_licznik()
    powieksz_licznik()
    powieksz_licznik()

    print(LICZNIK['wartosc'])
