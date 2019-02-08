class Rycerz:
    def __init__(self):
        self._zycie = 60
        self.doswiadczenie = 0

    def __repr__(self):
        return '{}: hp={}, exp={}'.format('Rycerz', self.zycie, self.doswiadczenie)

    def maszeruj(self, dystans):
        print('{}: Przeszedłem {} m.'.format('Rycerz', dystans))
        self.doswiadczenie += 0.2 * (dystans)

    def atakuj(self, dystans):
        print('{}: Machnołem mieczem!'.format('Rycerz'))
        self.doswiadczenie += 0.3 *(dystans)

if __name__ == '__main__':
    r= Rycerz()
    print(r)
    r.maszeruj(10)
    r.atakuj()
    print(r)
