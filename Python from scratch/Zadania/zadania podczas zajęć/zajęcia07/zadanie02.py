tekst = input('Wpisz liczbę całkowitą: ')

try:
    liczba = int(tekst)
except ValueError:
    print(f'"{tekst}" to nie jest poprawna liczba całkowita.')
    exit()

print(f'Wczytana liczba całkowita to: {liczba}')

