def wczytaj_liczbe():
    while True:
        tekst = input('Wpisz liczbę całkowitą: ')
        try:
            liczba = int(tekst)
            break  # można również wstawić tutaj `return liczba`
        except ValueError:
            print(f'"{tekst}" to nie jest poprawna liczba całkowita.')
    return liczba


liczba1 = wczytaj_liczbe()
liczba2 = wczytaj_liczbe()

suma = liczba1 + liczba2
print(f'Suma liczb {liczba1} i {liczba2} to {suma}')
