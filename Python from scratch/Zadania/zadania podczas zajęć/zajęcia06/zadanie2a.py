def pole_prostokata(a, b):
    pole = a * b
    return pole


def obwod_prostokata(a, b):
    obwod = 2 * (a + b)
    return obwod


bok_a = int(input('Podaj bok a: '))
bok_b = int(input('Podaj bok a: '))

pole = pole_prostokata(bok_a, bok_b)
obwod = obwod_prostokata(bok_a, bok_b)

print('Prostokąt ma obwód: {} i pole: {}'.format(obwod, pole))
