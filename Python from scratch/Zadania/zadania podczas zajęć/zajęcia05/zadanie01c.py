while True:
    wyrazy = input('Wpisz dowolny wyraz: ')

    for wyraz in wyrazy.split():
        ile_znakow = len(wyraz)

        komunikat = 'Wyraz "{}" ma {} znaków.\n' \
                    'Wyraz ten zaczyna się na literę "{}"'.format(wyraz, ile_znakow, wyraz[0])

        print(komunikat)
    print()  # nowa linia, żeby oddzielić kolejne wpisania
