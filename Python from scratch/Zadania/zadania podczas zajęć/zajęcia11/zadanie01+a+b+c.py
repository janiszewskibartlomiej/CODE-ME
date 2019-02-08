from datetime import datetime

while True:

    try:
        data_urodzenia = input('Wprowadź datę urodzin celebryty w formacie [RRRR-MM-DD]:')
        konwertowanie_daty = datetime.strptime(data_urodzenia, '%Y-%m-%d')
        teraz = datetime.now()
        wiek_celebryty = teraz - konwertowanie_daty
        print('Wiek celebryty to: {} lat i {} dni.'.format(wiek_celebryty.days // 365, wiek_celebryty.days % 365))
        exit()

    except ValueError:
        print('Wprowadzono nie prawiłowe dane!')
        continue
