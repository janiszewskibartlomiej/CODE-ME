from datetime import datetime

data_urodzenia = input('Wprowadź datę urodzin celebryty w formacie [RRRR-MM-DD]:')

try:
    konwertowanie_daty = datetime.strptime(data_urodzenia, '%Y-%m-%d')
except ValueError:
    print('Wprowadzono nie prawiłowe dane!')
    exit()

teraz = datetime.now()
wiek_celebryty = teraz - konwertowanie_daty

print('Wiek celebryty to: {} lat i {} dni.'.format(wiek_celebryty.days // 365, wiek_celebryty.days % 365))
