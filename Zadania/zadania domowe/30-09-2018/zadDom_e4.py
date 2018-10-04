gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]

def dodaj_gre(zwyciezca, przegrany):

    for element in gracze:
        if element['imie'] == zwyciezca:
            element['wygrane'] += 1

    print(gracze)

dodaj_gre('Celina','Alojzy')
dodaj_gre('Barnaba', 'Danuta')


