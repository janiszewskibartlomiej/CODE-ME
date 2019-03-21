from jednostki2.wojownik import Wojownik


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__(40)

    def atakuj(self):
        print('Łucznik: Wypuściłem strzałę!')
        self._doswiadczenie += 0.4
