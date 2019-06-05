import requests

params = {'country': 'pl'}

r = requests.get('https://api.abalin.net/get/today', params=params)

print(r.url)  # dowód na to, że url rzeczywiście został złożony

dane = r.json()

# kto ma dziś imieniny w polsce?

print(dane)

imiona = dane['data']['name_pl']
imiona = imiona.split(', ')

print('Imieniny obchodzą dziś:')

for imie in imiona:
    print(imie)
