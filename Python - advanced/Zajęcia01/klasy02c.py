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
    k = Kot('Filemon')
    print(k)  # __str__ jest używane zamiast __repr__
    k.daj_glos()

    # Jeśli bardzo chcemy, to wciąż możemy dostać się do __repr__
    print(k.__repr__())
