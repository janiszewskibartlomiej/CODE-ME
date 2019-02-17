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


bok_a = int(input('Podaj bok a: '))
bok_b = int(input('Podaj bok b: '))
opisz_prostokat(bok_a, bok_b)
