class Lucznik:
    def __init__(self):
        self.zycie = 40
        self.doswiadczenie = 0
        self.strzaly = 5

    def __repr__(self):
        return '{}: hp={}, exp={}'.format('Łucznik', self.zycie, self.doswiadczenie)

    def maszeruj(self, dystans):
        print('{}: Przeszedłem {} m.'.format('Łucznik', dystans))
        self.doswiadczenie += 0.2 * (dystans)

    def atakuj(self, dystans):
        print('{}: Wypuściłem strzałę!'.format('Łucznik'))
        self.doswiadczenie += 0.4 * (dystans)


if __name__ == '__main__':
    r = Lucznik()
    print(r)
    r.maszeruj(10)
    r.atakuj(10)
    print(r)
