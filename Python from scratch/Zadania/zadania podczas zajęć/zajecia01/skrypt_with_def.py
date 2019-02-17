def koszt_gazu(dystans, cena=2.08):
    spalanie_na100km = 12.8
    koszt = spalanie_na100km * dystans / 100 * cena
    print(f'Koszt wyprawy to: {koszt:.2f} zł')


dystans = int(input('Podaj przejechany dystans:'))
koszt_gazu(dystans)