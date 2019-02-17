while True:
    tekst = input('Wpisz liczbę całkowitą: ')
    try:
        liczba = int(tekst)
        break
    except ValueError:
        print(f'"{tekst}" to nie jest poprawna liczba całkowita.')

print(f'Wczytana liczba całkowita to: {liczba}')

