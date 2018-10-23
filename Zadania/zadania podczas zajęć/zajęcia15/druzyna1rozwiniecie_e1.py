from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik


class Druzyna:
    def __init__(self):
        self.wojownicy = []

    def dodaj_wojownika(self, wojownik):
        self.wojownicy.append(wojownik)

    def marsz(self, dystans):
        for w in self.wojownicy:
            w.maszeruj(dystans)

    def atak(self):
        for w in self.wojownicy:
            w.atakuj()

if __name__ == '__main__':
    d = Druzyna()

    r = Rycerz()
    d.dodaj_wojownika(r)

    # nie musimy tworzyć zmiennej
    d.dodaj_wojownika(Lucznik())

    d.marsz(1000)
    print()
    d.atak()