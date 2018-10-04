gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]

def ile_razy_wygral(imie):
    #lista_imion = []
    for element in gracze:
        #lista = list(element.values())
        #lista_imion.append(lista)
        if imie == element['imie']:
            print('Gracz {} wygrał(a) {} gier.'.format(imie, element['wygrane']))

ile_razy_wygral('Celina')
ile_razy_wygral('Barnaba')
ile_razy_wygral('Danuta')
ile_razy_wygral('Alojzy')

