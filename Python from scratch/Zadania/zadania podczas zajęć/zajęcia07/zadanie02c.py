def wczytaj_liczbe(nr=None):
    if nr is None:
        pytanie = 'Wpisz liczbę całkowitą: '
    else:
        pytanie = f'Wpisz liczbę całkowitą numer {nr}:'

    while True:
        tekst = input(pytanie)
        try:
            liczba = int(tekst)
            break  # można również wstawić tutaj `return liczba`
        except ValueError:
            print(f'"{tekst}" to nie jest poprawna liczba całkowita.')
    return liczba


liczby = []

for i in range(1, 6):
    liczba = wczytaj_liczbe(nr=i)
    liczby.append(liczba)

suma = sum(liczby)
print(f'Suma liczb {liczby} to {suma}')
