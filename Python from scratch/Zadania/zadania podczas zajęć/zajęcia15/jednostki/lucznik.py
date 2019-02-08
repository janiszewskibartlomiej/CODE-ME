from jednostki.wojownik import Wojownik

class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self.zycie = 40
    def atakuj(self):
        print('Łucznik: Wypuściłem strzałę!')
        self.doswiadczenie += 0.4
