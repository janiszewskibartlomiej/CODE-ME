# Antywzorzec! zmienna 'czy_powtarzac' jest zbędna

czy_powtarzac = True

while czy_powtarzac:  # zamiast tego 'while True'
    odpowiedz = input('Napisz [koniec] jeśli chcesz zakończyć program: ')

    if odpowiedz == 'koniec':
        czy_powtarzac = False  # zamiast tego 'break'
    else:
        print('Wpisano:', odpowiedz)
