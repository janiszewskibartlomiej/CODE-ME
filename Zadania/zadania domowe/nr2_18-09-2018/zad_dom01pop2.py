tablica_wpisanych_liczb = []

while True:
    liczba_calkowita = int(input('Wpisz liczbę całkowitą: '))

    tablica_wpisanych_liczb.append(liczba_calkowita)

    if sum(tablica_wpisanych_liczb) < 100:

        print('Suma liczb: ', tablica_wpisanych_liczb, 'to: ', sum(tablica_wpisanych_liczb))

        continue

    print('Suma wprowadzonych liczb jest większa niż 100! ')
    break



