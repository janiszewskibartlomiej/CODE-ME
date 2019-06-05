import requests

params = {'country': 'jp'}  # kto obchodzi imieniny w Japonii?

r = requests.get('https://api.abalin.net/get/today', params=params)

print(r.url)

print(r.status_code)  # status odpowiedzi
print(r.reason)  # opis statusu

dane = r.json()

print(dane)
