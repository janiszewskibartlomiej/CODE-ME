liczba_str = input('Wpisz liczbę całkowią: ')
liczba = int(liczba_str)

liczba_podzielna_przez_2 = liczba % 2
liczba_podzielna_przez_3 = liczba % 3
liczba_podzielna_przez_4 = liczba % 4
liczba_podzielna_przez_5 = liczba % 5
liczba_podzielna_przez_6 = liczba % 6
liczba_podzielna_przez_9 = liczba % 9
liczba_podzielna_przez_10 = liczba % 10

if liczba == 0:
    print('Podano liczbę 0, która nie może być dzielona ')
    exit()
if liczba_podzielna_przez_2 == 0:
    print('Liczba ', liczba,' jest podzielna przez 2')

    if liczba_podzielna_przez_4 == 0 :
        print('Liczba ', liczba, ' jest podzielna przez 4')

if liczba_podzielna_przez_3 == 0:
    print('Liczba ', liczba,' jest podzielna przez 3')
    if liczba_podzielna_przez_9 == 0:
        print('Liczba ', liczba, ' jest podzielna przez 9')
if liczba_podzielna_przez_5 == 0:
    print('Liczba ', liczba,' jest podzielna przez 5')
if liczba_podzielna_przez_6 == 0:
    print('Liczba ', liczba,' jest podzielna przez 6')

if liczba_podzielna_przez_10 == 0:
    print('Liczba ', liczba,' jest podzielna przez 10')




