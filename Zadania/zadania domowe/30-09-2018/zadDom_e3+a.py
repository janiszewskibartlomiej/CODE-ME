gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]

def ile_razy_wygral(imie):
    # lista_imion = []
    for element in gracze:
        # lista_wygranych = element['imie']
        # lista_imion.append(lista_wygranych)
         suma = element['wygrane'] + element['przegrane']
        wynik_dzielenia = (element['wygrane'] / suma) * 100
        if imie == element['imie']:

            print('Gracz {} wygrał(a) {} gier ({:.2f}% wszystkich).'
                  .format(imie, element['wygrane'], wynik_dzielenia))


ile_razy_wygral('Celina')
ile_razy_wygral('Barnaba')
ile_razy_wygral('Danuta')
ile_razy_wygral('Alojzy')
ile_razy_wygral('alojzy')
