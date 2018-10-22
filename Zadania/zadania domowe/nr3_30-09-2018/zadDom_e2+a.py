gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]

def lista_imion_graczy(lista,posortowane=False):
    lista_imion = []
    for element in lista:
        lista_wartosci = element['imie']
        lista_imion.append(lista_wartosci)
    if posortowane == False:
        print(lista_imion)
    else:
        lista_imion.sort()
        print(lista_imion)

lista_imion_graczy(gracze)
print()
lista_imion_graczy(gracze,12)
lista_imion_graczy(gracze,True)
lista_imion_graczy(gracze,1)

