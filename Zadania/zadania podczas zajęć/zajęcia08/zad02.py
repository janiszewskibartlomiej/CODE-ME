przyklad = [1, [2, 3], [4, 5, [6, 7, 8], 9], 10, 11, [12], 13]

def wypisz_elementy_listy(lista):

    for element in lista:
        if isinstance(element, list):
            print('lista: ',element)
        else:
            print('element: ', element)

wypisz_elementy_listy(przyklad)

