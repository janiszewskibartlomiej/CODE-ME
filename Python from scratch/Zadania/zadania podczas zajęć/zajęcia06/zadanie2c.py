def pole_prostokata(a, b):
    pole = a * b
    return pole


def obwod_prostokata(a, b):
    obwod = 2 * (a + b)
    return obwod


def opisz_prostokat(a, b):
    pole = pole_prostokata(a, b)
    obwod = obwod_prostokata(a, b)
    print('Prostokąt ma obwód: {} i pole: {}'.format(obwod, pole))


def narysuj_prostokat(a, b):
    for x in range(a):
        print('X' * b)


bok_a = int(input('Podaj bok a: '))
bok_b = int(input('Podaj bok a: '))
opisz_prostokat(bok_a, bok_b)
narysuj_prostokat(bok_a, bok_b)
