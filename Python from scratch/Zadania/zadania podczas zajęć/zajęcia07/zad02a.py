liczba_calkowita = input('Wpisz liczbę całkowitą: ')

try:
    wpisane_znaki = int(liczba_calkowita)
    wpisane_znaki is not int
    while True:
        continue

except ValueError:

    while wpisane_znaki is not int:
        print(f'{liczba_calkowita} to nie jest liczba całkowita')
        continue

print(f'Wpisana liczba to {wpisane_znaki}')
