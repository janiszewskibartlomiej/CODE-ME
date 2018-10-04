gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]

def wypisz_imiona_graczy(lista):
    for element in lista:
        print('Imię gracza: ',element['imie'])

wypisz_imiona_graczy(gracze)