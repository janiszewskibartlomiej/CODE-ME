def pole_prostokata(dlugosc,szerokosc):
    return dlugosc * szerokosc

def obwod_prostokata(dlugosc,szerokosc):
    return (dlugosc+szerokosc) * 2

def narysuj_prostokat(dlugosc,szerokosc):
    prostokat = szerokosc ('x')
    return print(f'{prostokat}\n'*dlugosc)

dlugosc_boku = input("Wprowadz dlugosc boku a")
dlugosc_boku = int(dlugosc_boku)
szerokosc_boku = input("Wprowadz szerokosc boku b")
szerokosc_boku = int(szerokosc_boku)
narysuj_prostokat(dlugosc_boku,szerokosc_boku)