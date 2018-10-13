import json

lista_numerow = []
print(lista_numerow)
wpis = {'imie': 'Bartek', 'numer': 511111511}
lista_numerow.append(wpis)
print(lista_numerow)

with open('ksiazka_numerow.json', mode='w') as plik:
    json.dump(lista_numerow, plik)


def wczytywanie_danych(lista=[]):
    podaj_imie = input('Proszę podać imię:')
    podaj_numer = input('Prosze podać numer telefonu: ')
    imie = str(podaj_imie)
    numer = int(podaj_numer)
    slownik_z_danych = {'imie': imie, 'numer': numer}
    lista_numerow.append(slownik_z_danych)
    with open('ksiazka_numerow.json', mode='w') as plik:
        json.dump(lista_numerow, plik)


wczytywanie_danych()
