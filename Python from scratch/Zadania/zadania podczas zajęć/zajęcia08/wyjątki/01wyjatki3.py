print('Początek programu')

lista = []

try:
    wartosc = lista[13]  # ta operacja rzuci IndexError, czego nie obsługujemy
    13 / 0
except ZeroDivisionError:
    print('Ktoś próbuje dzielić przez zero!')
else:
    print('Poprawne obliczenia, nie było wyjątku.')
finally:
    print('Ta linijka zostanie wypisana ZAWSZE!')

print("Koniec programu")