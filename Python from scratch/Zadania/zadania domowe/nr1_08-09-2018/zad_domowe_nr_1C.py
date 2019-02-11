str = input('Podaj liczbę całkowitą: ')

if str == '' or ' ' or not int:
    print('Nie podano żadnej liczby całkowiej! ')
    exit()

liczba = int(str)

if liczba == 0:
    print('Podano liczbę 0, która nie może być dzielona ')
    exit()


if liczba % 2 == 0:
    print('Liczba ', liczba, ' jest podzielna przez 2')

    if liczba % 4 == 0:
        print('Liczba ', liczba, ' jest podzielna przez 4')

if liczba % 3 == 0:
    print('Liczba ', liczba, ' jest podzielna przez 3')
    if liczba % 9 == 0:
        print('Liczba ', liczba, ' jest podzielna przez 9')
if liczba % 5 == 0:
    print('Liczba ', liczba, ' jest podzielna przez 5')
if liczba % 6 == 0:
    print('Liczba ', liczba, ' jest podzielna przez 6')

if liczba % 10 == 0:
    print('Liczba ', liczba, ' jest podzielna przez 10')
