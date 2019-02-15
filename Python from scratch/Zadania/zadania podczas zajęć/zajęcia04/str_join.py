imiona = ['Artur', 'Barbara', 'Celina']

liczby = [5,6,78,4]

print(''.join(imiona))

print(' '.join(imiona))

print('XXX'.join(imiona))

#moje sprawdzenie join w liczbach
print('-----------')
print(liczby, type(liczby))
str_liczby = str(liczby)
print(str_liczby, type(str_liczby))
print('+'.join(str_liczby))