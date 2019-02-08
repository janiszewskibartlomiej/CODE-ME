while True:
    liczba_calkowita = int(input('Wpisz liczbę całkowitą: '))
    tablica_wpisanych_liczb = []

    if sum(tablica_wpisanych_liczb) < 100:

        tablica_wpisanych_liczb.append(liczba_calkowita)

        print('Suma liczb: ', tablica_wpisanych_liczb, 'to: ', sum(tablica_wpisanych_liczb))
        continue

    else: print('Suma wprowadzonych liczb jest większa niż 100! ')

