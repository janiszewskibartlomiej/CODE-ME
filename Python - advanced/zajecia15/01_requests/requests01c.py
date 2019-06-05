import requests

r = requests.get('https://api.abalin.net/get/today?country=pl')

dane = r.json()

# kto ma dziś imieniny w polsce?

print(dane)

imiona = dane['data']['name_pl']
imiona = imiona.split(', ')

print('Imieniny obchodzą dziś:')

for imie in imiona:
    print(imie)
