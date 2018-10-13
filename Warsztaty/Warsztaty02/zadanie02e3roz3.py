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
        print([])
        exit()
    odczyt = json.load(wczytanie)
    print('Liczba wczytanych wpisów: ', len(odczyt))
    return odczyt

lista = wczytaj_liste_wpisow()


def menu():
    while True:
        pytanie = input('Czy wczytać nowy wpis [wybierz "t" lub "n"]:')
        if pytanie in 'tT':
            dodanie_danych(lista)
            print(wczytaj_liste_wpisow())
        if pytanie in 'nN':
            break


if __name__ == '__main__':
    menu()
