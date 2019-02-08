import json

lista_numerow = []
print(lista_numerow)
wpis = {'imie': 'Bartek', 'numer': 11}
lista_numerow.append(wpis)

print(lista_numerow)

with open('ksiazka_numerow.json', mode='w') as plik:
    json.dump(lista_numerow, plik)

test = open('ksiazka_numerow.json', mode='r', encoding='cp1250')
zawartosc = test.read()
print(zawartosc)
