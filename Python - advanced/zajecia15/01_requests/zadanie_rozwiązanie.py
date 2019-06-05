import requests

params = {'day': 31, 'month': 12, 'country': 'pl'}  # kto obchodzi imieniny w Japonii?

r = requests.get('https://api.abalin.net/get/namedays', params=params)

print(r.url)

dane = r.json()

# kto ma  imieniny w polsce 31 grudnia?

print(dane)

imiona = dane['data']['name_pl']
imiona = imiona.split(', ')
print(imiona)
print('Imieniny obchodzą dziś:')

for imie in imiona:
    print(imie)