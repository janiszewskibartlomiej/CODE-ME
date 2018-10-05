while True:
    tekst = input("Wpisz tekst z klawiatury:")

    zwrot_info = 'Wyraz "{}" ma {} znaków\n\n' \
                 'Wyraz ten zaczyna się na literę "{}".'.format(tekst, len(tekst), tekst[0])

    if ' ' in tekst:
        continue
    print(zwrot_info)