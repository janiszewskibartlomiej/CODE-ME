liczba_calkowita = input('Wpisz liczbę całkowitą: ')

try:
    wpisane_znaki = int(liczba_calkowita)
    wpisane_znaki is not int

except ValueError:
    print(f'{liczba_calkowita} to nie jest liczba całkowita')
    exit()

print(f'Wpisana liczba to {wpisane_znaki}')
