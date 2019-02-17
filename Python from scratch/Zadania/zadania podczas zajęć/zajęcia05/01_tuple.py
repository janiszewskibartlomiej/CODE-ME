pusta_krotka = tuple()
print(pusta_krotka)

adres = ('Fundacja CODE:ME', 'aleja Wojska Polskiego 41', '80-268 Gdańsk')

# można też tak wprowadzać dane
adres = ('Fundacja CODE:ME',
         'aleja Wojska Polskiego 41',
         '80-268 Gdańsk')

print(adres)

print(adres[0])

nazwa, ulica, kod_i_miasto = adres

print(nazwa)
print(ulica)
