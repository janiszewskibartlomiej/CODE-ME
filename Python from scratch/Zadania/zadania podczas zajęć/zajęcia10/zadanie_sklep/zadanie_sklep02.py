from maly_sklep import slodycze


def wypisz_artykuly():
    print('Sklep ma w asortymencie:')
    for artykul in slodycze:
        print(artykul['nazwa'])


def podaj_cene(nazwa):
    for artykul in slodycze:
        if nazwa == artykul['nazwa']:
            print('{} kosztuje {}zł'.format(nazwa, artykul['cena']))


def zmien_cene(nazwa, nowa_cena):
    for artykul in slodycze:
        if nazwa == artykul['nazwa']:
            artykul['cena'] = nowa_cena


def dodaj_artykul(nazwa, cena):
    nowy_artykul = {'nazwa': nazwa,
                    'cena': cena,
                    'czy_na_sztuki': True}
    slodycze.append(nowy_artykul)


wypisz_artykuly()
podaj_cene('czekolada')
zmien_cene('czekolada', 3.99)
podaj_cene('czekolada')
dodaj_artykul('baton', 1.99)
wypisz_artykuly()