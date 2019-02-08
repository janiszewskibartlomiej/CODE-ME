import json


def dodanie_danych(lista=[]):
    podaj_imie = input('Proszę podać imię:')
    podaj_numer = input('Prosze podać numer telefonu: ')
    imie = str(podaj_imie)

    try:
        numer = int(podaj_numer)
        slownik_z_danych = {'imie': imie, 'numer': numer}
        lista.append(slownik_z_danych)

        with open('ksiazka_numerow.json', mode='w') as plik:
            json.dump(lista, plik)


    except ValueError:
        print('Wpisałeś nie poprawny numer!')


def wczytaj_liste_wpisow():
    try:
        wczytanie = open('ksiazka_numerow.json', mode='r')
    except FileNotFoundError:
        lista = []
        print(lista)
        exit()
    odczyt = json.load(wczytanie)
    print('Liczba wczytanych wpisów: ', len(odczyt))
    return odczyt


if __name__ == '__main__':
    lista = wczytaj_liste_wpisow()
    print(lista)
    dodanie_danych(lista)
    print(lista)
