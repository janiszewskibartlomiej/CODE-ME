class Plecak:
    def __init__(self, pojemnosc, kolor):
        self.pojemnosc_plecaka = pojemnosc
        self.kolor_plecaka = 'zielony'

    def __repr__(self):
        return f'Plecak koloru {self.kolor_plecaka} ma pojemność {self.pojemnosc_plecaka} L.'


p1 = Plecak(3, 'czarny')
print(p1)

