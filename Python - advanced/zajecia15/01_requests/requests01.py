import requests

r = requests.get('https://api.abalin.net/get/today')

print(r.headers['content-type'])

dane_text = r.text

print(type(dane_text))
print(dane_text)

dane_json = r.json()  # dzięki requests, dostajemy tutaj od razu słownik

print(type(dane_json))
print(dane_json)
