imiona = ['Alicja', 'Genowefa', 'Dionizy']

print(imiona)

indeks_imienia = int(input('Wisz numer imienia które chcesz usunąć:'))
if indeks_imienia < len(imiona):
    usuwane_imie = imiona.pop(indeks_imienia)
    print(imiona)

else:
    print('Liczba jest poza zakresem!')
    exit()

