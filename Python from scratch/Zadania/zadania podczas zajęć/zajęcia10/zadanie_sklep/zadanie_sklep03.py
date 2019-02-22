from duzy_sklep import slodycze, warzywa_i_owoce


def wypisz_artykuly(lista_artykulow):
    print('Sklep ma w asortymencie:')
    for artykul in lista_artykulow:
        print(artykul['nazwa'])


def podaj_cene(nazwa, lista_artykulow):
    for artykul in lista_artykulow:
        if nazwa == artykul['nazwa']:
            print('{} kosztuje {}zł'.format(nazwa, artykul['cena']))


def zmien_cene(nazwa, nowa_cena, lista_artykulow):
    for artykul in lista_artykulow:
        if nazwa == artykul['nazwa']:
            artykul['cena'] = nowa_cena


def dodaj_artykul(nazwa, cena, lista_artykulow):
    nowy_artykul = {'nazwa': nazwa,
                    'cena': cena,
                    'czy_na_sztuki': True}
    lista_artykulow.append(nowy_artykul)


wypisz_artykuly(slodycze)
podaj_cene('czekolada', slodycze)
zmien_cene('czekolada', 3.99, slodycze)
podaj_cene('czekolada', slodycze)
dodaj_artykul('baton', 1.99, slodycze)
wypisz_artykuly(slodycze)

wypisz_artykuly(warzywa_i_owoce)
