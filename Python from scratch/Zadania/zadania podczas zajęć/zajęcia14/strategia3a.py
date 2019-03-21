class Wojownik:
    def __repr__(self):
        return f'Wojownik: hp={self._zycie}, exp={self._doswiadczenie}'  # Straciliśmy informację kto jest kim!

    def maszeruj(self, dystans):
        print(f'Wojownik: Przeszedłem {dystans}m')
        self._doswiadczenie += 0.02 * dystans


class Rycerz(Wojownik):
    def __init__(self):
        self._zycie = 60
        self._doswiadczenie = 0

    def atakuj(self):
        print('Rycerz: Machnąłem mieczem!')
        self._doswiadczenie += 0.3


class Lucznik(Wojownik):
    def __init__(self):
        self._zycie = 40
        self._doswiadczenie = 0

    def atakuj(self):
        print('Łucznik: Wypuściłem strzałę!')
        self._doswiadczenie += 0.4


if __name__ == '__main__':
    p = Rycerz()
    print(p)
    p.maszeruj(10)
    print(p)
    p.atakuj()
    print(p)

    l = Lucznik()
    print(l)
    l.maszeruj(15)
    print(l)
    l.atakuj()
    print(l)
