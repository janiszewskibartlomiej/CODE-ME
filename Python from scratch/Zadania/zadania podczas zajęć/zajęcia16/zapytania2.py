from urllib.request import urlopen
import json

# https://worldcup.sfg.io/matches/country?fifa_code=POL

with urlopen('https://worldcup.sfg.io/matches') as response:
    odpowiedz_json = response.read()
    mecze = json.loads(odpowiedz_json)

    ilosc_meczow = len(mecze)
    print(f'Rozegrano {ilosc_meczow} meczów.')

    numer_meczu = 20
    print(f'Szczegóły meczu {numer_meczu}:')
    mecz = mecze[numer_meczu]

    gospodarz = mecz['home_team_country']
    przyjezdny = mecz['away_team_country']
    print(f'Mecz pomiędzy {gospodarz} a {przyjezdny}')

    wygrany = mecz['winner']
    if wygrany == 'Draw':
        print('Mecz zakończony remisem')
    else:
        print(f'Mecz wygrany przez {wygrany}')

    statystyki_gospodarza = mecz['home_team']
    statystyki_przyjezdnego = mecz['away_team']

    print('Wynik: {}:{}'.format(statystyki_gospodarza['goals'], statystyki_przyjezdnego['goals']))

    pass
