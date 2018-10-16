class Plecak:
    def __init__(self, pojemnosc):
        self.pojemnosc_plecaka = pojemnosc
        self.kolor_plecaka = 'zielony'
        self.zawartosc = []

    def __repr__(self):
        return f'Plecak koloru {self.kolor_plecaka} ma pojemność {self.pojemnosc_plecaka} L.'

    def dodaj_przedmiot(self, przedmiot):
        self.zawartosc.append(przedmiot)

    def ile_przedmiotow(self):
        return len(self.zawartosc)


p1 = Plecak(30)
print(p1.zawartosc)

if __name__ == '__main__':

    p1.dodaj_przedmiot('konserwa')
    p1.dodaj_przedmiot('latarka')
    p1.dodaj_przedmiot('kanapka')
    p1.dodaj_przedmiot('termos')
    p1.dodaj_przedmiot('nóż')
    p1.dodaj_przedmiot('śpiwór')
    ilosc_przedmiotow = p1.ile_przedmiotow()
    print(f'W plecaku znajduje się {ilosc_przedmiotow} przedmiótw: {p1.zawartosc}')

