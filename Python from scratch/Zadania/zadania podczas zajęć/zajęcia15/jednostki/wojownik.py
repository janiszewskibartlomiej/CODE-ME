class Wojownik:
    def __init__(self):
        self.doswiadczenie = 0

    def __repr__(self):
        nazwa = self.__class__.__name__
        return '{}: hp={}, exp={}'.format(nazwa, self.zycie, self.doswiadczenie)

    def maszeruj(self, dystans):
        nazwa = self.__class__.__name__
        print('{}: Przeszedłem {} m.'.format(nazwa, dystans))
        self.doswiadczenie += 0.2 * (dystans)
