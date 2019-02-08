imiona = ['Alicja', 'Genowefa', 'Dionizy']

print(imiona)

nowe_imie = input('Wpisz nowe imię: ')
imiona.append(nowe_imie)

print(imiona)

imiona[0] = 'Guido'

print(imiona)

indeks_imienia = int(input('Wisz numer imienia które chcesz zmienić:'))
zmiana_imienia = input('Wpisz nowe imie: ')

imiona[indeks_imienia] = zmiana_imienia

print(imiona)
