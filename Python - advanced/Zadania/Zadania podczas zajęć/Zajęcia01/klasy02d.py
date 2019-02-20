#  tu mamy opis jak metody dander działają:
#  https://docs.python.org/3/reference/datamodel.html#special-method-names


class Kot:
    _lapy = 4

    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f'Ten kot ma na imie: {self.imie}'

    def __repr__(self):
        return f'Kot {self.imie}'

    def daj_glos(self):
        print("Miau!")


if __name__ == '__main__':
    f = Kot('Filemon')
    print(f)  # __str__ jest używane zamiast __repr__

    b = Kot('Bonifacy')
    print(b)

    lista_kotow = [f, b]
    print(lista_kotow)  # UWAGA! Tutaj jest używany __repr__ !
