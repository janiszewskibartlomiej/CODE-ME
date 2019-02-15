# imiona = ['Alicja', 'Genowefa', 'Dionizy']
#
# print(imiona)
#
# indeks_imienia = int(input('Wisz numer imienia które chcesz usunąć:'))
# if indeks_imienia < len(imiona):
#     usuwane_imie = imiona.pop(indeks_imienia)
#     print(imiona)
#
# else:
#     print('Liczba jest poza zakresem!')
#     exit()
#

imiona = ['Alicja', 'Genowefa', 'Dionizy']

print(imiona)

index = int(input('Proszę podać indeks imienia, które chcesz usunąć: '))

zakres = len(imiona)

# print(zakres)

# print(imiona[-3])

if index > zakres - 1 or index < -3:

    print('Indeks jest poza zakresem')

else:
    print(imiona[index])
    usuniecie = imiona.pop(index)
    print('Imię które zostało usunięt: ', usuniecie)  # imiona[index])

print(imiona)
