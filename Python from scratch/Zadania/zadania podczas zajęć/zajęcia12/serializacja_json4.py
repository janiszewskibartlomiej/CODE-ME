import json

plik = open('warzywa.json', mode='r')

dane = json.load(plik)

print(dane)
print(type(dane))

print(dane[0]['nazwa'])