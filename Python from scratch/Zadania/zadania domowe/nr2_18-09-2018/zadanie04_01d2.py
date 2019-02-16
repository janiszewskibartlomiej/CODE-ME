skladniki = []

while True:
    liczba = int(input('Wpisz liczbę: '))

    if liczba < 0:
        continue

    skladniki.append(liczba)

    skladniki_str = list(map(str, skladniki))

    lewa_strona = ' + '.join(skladniki_str)

    suma = sum(skladniki)

    print(lewa_strona, '=', suma)

    if suma > 100:
        break


