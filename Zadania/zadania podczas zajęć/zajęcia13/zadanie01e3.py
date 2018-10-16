class Plecak:
    def __init__(self, pojemnosc):
        self.pojemnosc_plecaka = pojemnosc
        self.kolor_plecaka = 'zielony'
        self.zawartosc = []

    def __repr__(self):
        return f'Plecak koloru {self.kolor_plecaka} ma pojemność {self.pojemnosc_plecaka} L.'

    def dodaj_przedmiot(self, przedmiot):
        self.zawartosc.append(przedmiot)

p1 = Plecak(30)
print(p1.zawartosc)

p1.dodaj_przedmiot('konserwa')
print(p1.zawartosc)
