def wczytaj_liczby():
    while True:
        moje_liczby = input('Prosze podać 4 liczby losowania oddzielone przecinkami z przedziłu od 1 do 19: ')
        moje_liczby.split()
        lista = []
        for element in moje_liczby:
            try:
                liczba = int(element)
            except ValueError:
                print(f'wartość "{element}" nie jest liczbą.')
                break


            if not 20>liczba>=0:
                    print(f' liczba {liczba} nie należy do przedziału od 1 do 19.')
                    break
            if liczba in lista:
                print(f'liczba {liczba} powtórzyła się.')
                break
            lista.append(element)

            if len(lista) != 4:
                print('Wpisz zakład jeszcze raz.')
                continue

        return sorted(moje_liczby)



wczytaj_liczby()