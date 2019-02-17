def rysuj_prostokat(a, b, znak='X'):
    for i in range(a):
        print(znak * b)


rysuj_prostokat(3, 5)
rysuj_prostokat(4, 6, '#')

prostokat1 = (5, 4)
rysuj_prostokat(*prostokat1)

prostokat2 = {'a': 3, 'b': 4}

rysuj_prostokat(**prostokat2, znak='O')
