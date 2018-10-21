gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]

def lista_imion_graczy(lista):
    lista_imion = []
    for element in lista:
        lista_wartosci = element['imie']
        lista_imion.append(lista_wartosci)
    return lista_imion


print(lista_imion_graczy(gracze))