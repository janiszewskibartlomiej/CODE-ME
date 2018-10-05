przyklad = [1, [2, 3], [4, 5, [6, 7, 8], 9], 10, 11, [12], 13]

def wypisz_elementy_listy(lista, poziom=0):
    for element in lista:
        if isinstance(element, list):
            wypisz_elementy_listy(element, poziom + 1)  # może też być poziom=poziom + 1
        else:
            print('\t' * poziom, 'element: ', element)

wypisz_elementy_listy(przyklad)
