def wypisz_artykuly(lista_artykulow):
    # artykuly = []
    for element in lista_artykulow:
        #   artykuly.append(elementy['nazwa'])
        print(element['nazwa'])



def podaj_cene(nazwa, lista_artykulow):
    for artykul in lista_artykulow:
        if artykul['nazwa'] == nazwa:
            print('{} kosztuje {} zł.'.format(nazwa, artykul['cena']))


def zmien_cene(nazwa, cena, lista_artykulow):
    for produkt in lista_artykulow:
        if produkt['nazwa'] == nazwa:
            produkt['cena'] = cena
    print(lista_artykulow)



def dodaj_artykul(nazwa, cena, lista_artykulow):
    nowy_artykul = {'nazwa': nazwa, 'cena' : cena, 'czy_na_sztuki' : True}
    lista_artykulow.append(nowy_artykul)