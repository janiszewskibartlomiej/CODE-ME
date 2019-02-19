def wypisz_elementy_listy(lista, poziom=0):
    for l in lista:
        if isinstance(l, list):
            wypisz_elementy_listy(l, poziom + 1)
        else:
            print('\t' * poziom, 'element:', l)


przyklad = [1, [2, 3], [4, 5, [6, 7, 8], 9], 10, 11, [12], 13]

wypisz_elementy_listy(przyklad)
