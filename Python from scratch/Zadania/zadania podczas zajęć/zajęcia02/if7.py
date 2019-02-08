liczba = int(input("Podaj liczbę całkowitą: "))

if liczba > 0 and liczba < 100:
    print('Liczba jest z zakresu (0, 100)')

# wersja druga

if 0 < liczba < 100:
    print('Liczba jest z zakresu (0, 100)')

# ctrl + / komentuje cały zaznaczony kod

# oprócz operatora 'and' jest jeszcze 'or' (czyli 'lub')

if 0 < liczba or liczba< 100:
    print('Liczba jest z zakresu (0, 100)')