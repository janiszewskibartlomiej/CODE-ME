from datetime import datetime

data_urodzenia = input('Wprowadź datę urodzin celebryty w formacie [RRRR-MM-DD]:')
konwertowanie_daty = datetime.strptime(data_urodzenia, '%Y-%m-%d')
teraz = datetime.now()
wiek_celebryty = teraz - konwertowanie_daty
print('Wiek celebryty to:', wiek_celebryty.days // 365)