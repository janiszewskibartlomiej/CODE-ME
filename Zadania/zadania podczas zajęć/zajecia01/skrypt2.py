cena_paliwa = 5.08

# pobieramy liczbę z klawiatury, będzie zapisana jako typ 'str'
dystans_str = input('Podaj liczbę kilometrów: ')

dystans = int(dystans_str)  # tutaj konwertujemy 'str' na 'int'

spalanie_na100km = 6.7
koszt = spalanie_na100km * dystans / 100 * cena_paliwa

print('Koszt wyprawy to:', koszt)
