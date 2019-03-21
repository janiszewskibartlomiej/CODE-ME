from jednostki2.wojownik import Wojownik


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__(60)

    def atakuj(self):
        print('Rycerz: Machnąłem mieczem!')
        self._doswiadczenie += 0.3
