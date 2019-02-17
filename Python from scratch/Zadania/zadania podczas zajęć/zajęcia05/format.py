liczba = 12
tekst = 'coś jest napisane'
logiczne = True
lista = [1, 2, 3]

print(liczba, tekst, logiczne, lista)  # ctrl + /

print('Zmienna liczba ma wartość:', liczba, 'a tu jest tekst:', tekst)

print('Zmienna liczba ma wartość: {} a tu jest tekst: {}'.format(liczba, tekst))

szablon = 'Zmienna liczba ma wartość: {} a tu jest tekst: {}'
print(szablon.format(liczba, tekst))
print(szablon.format(1234, 'zupełnie inny tekst'))
