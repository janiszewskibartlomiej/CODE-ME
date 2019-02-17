cena_gazu = 2.08


if dystans is not 0:
    spalanie_na100km = 12.8
    koszt = spalanie_na100km * dystans / 100 * cena_gazu
    print('Koszt wyprawy to:')
    print(koszt)

elif dystans is 0:
    print('Podałeś o km')

elif dystans is not 0:
    print('to nie jest 0')

else:
    print('nie podałeś liczby całowitej')