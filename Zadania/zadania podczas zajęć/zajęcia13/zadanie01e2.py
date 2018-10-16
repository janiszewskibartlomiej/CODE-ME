class Plecak:
    def __init__(self, pojemnosc):
        self.pojemnosc_plecaka = pojemnosc
        self.kolor_plecaka = 'zielony'

    def __repr__(self):
        return f'Plecak koloru {self.kolor_plecaka} ma pojemność {self.pojemnosc_plecaka} L.'


p1 = Plecak(30)
print(p1)
p2 = Plecak(45)
p2.kolor_plecaka = 'kamuflaż'
print(p2)

