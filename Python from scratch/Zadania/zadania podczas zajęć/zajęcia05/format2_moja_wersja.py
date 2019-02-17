# F-string

slowo = 'pies'
liczba = 17

tekst0 = f'to jest liczba: {slowo} a to jest: {liczba}'
print(tekst0)

tekst1 = 'to jest liczba: {} a to jest: {}'.format('tekst', 17)

print(tekst1)

tekst2 = 'to jest liczba: {1} a to jest: {0}'.format('tekst', 17)

print(tekst2)

tekst3 = 'Trzy razy liczba {0}, {0} i jeszcze {0}'.format(19)

print(tekst3)

tekst4 = 'Nazywam się {imię} {nazwisko}'.format(imię="Alojzy", nazwisko='Kowalski')

print(tekst4)