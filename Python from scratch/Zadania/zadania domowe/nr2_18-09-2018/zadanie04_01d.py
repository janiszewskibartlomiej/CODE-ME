skladniki = []

while True:
    liczba = int(input('Wpisz liczbę: '))

    if liczba < 0:
        continue

    skladniki.append(liczba)

    lewa_strona = ''

    # Stwórz kawałek równania (liczby z plusem po prawej) dla wszystkich liczb BEZ OSTATNIEJ
    for s in skladniki[:-1]:
        lewa_strona += str(s) + ' + '

    # Na koniec dodaj tę ostatnią liczbę, już bez plusa
    lewa_strona += str(skladniki[-1])

    suma = sum(skladniki)

    print(lewa_strona, '=', suma)

    if suma > 100:
        break


