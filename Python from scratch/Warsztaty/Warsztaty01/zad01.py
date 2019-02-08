ekwipunek = {'pieniądze':158.40,
             'sprzęt':['kompas', 'latarka', 'śpiwór'],
             'prowiant':['jabłko', 'woda', 'batonik', 'batonik']}

print('Lista ekwipunku to: ', ekwipunek)

print('Harcesz kupił karimatę za 29.99 zł')

ekwipunek['pieniądze'] = ekwipunek['pieniądze'] - 29.99

ekwipunek['sprzęt'].append('karimata')

print(ekwipunek)

print('Harcerz zjadł batonik')

ekwipunek['prowiant'].remove('batonik')

print(ekwipunek['prowiant'])

print('Harcerz ma 7 przedmiotów w plecaku: ', ekwipunek['sprzęt'] + ekwipunek['prowiant'])