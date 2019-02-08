def pole_prostokonta(a, b):
    wynik = a * b
    return wynik

def obwod_prostokonta(a, b):
    wynik = a + b
    return wynik

dl_a = int(input('Podaj długość boku a: '))
dl_b = int(input('Podaj długość boku b: '))

print('Prostokont ma obwód:', obwod_prostokonta(dl_a, dl_b), 'i pole:', pole_prostokonta(dl_a, dl_b))
