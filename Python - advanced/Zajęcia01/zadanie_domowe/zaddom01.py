class CzasBiegacza:

    def __init__(self, minuty, sekundy):
        if minuty >= 0:
            self._minuty = minuty
        else:
            raise ValueError('błedny zakres minut')
        if 0 <= sekundy < 60:
            self._sekundy = sekundy
        else:
            raise ValueError('nieprawidłowy zakres sekund')
        pass

    def __lt__(self, other):
        self.czas = self._minuty + self._sekundy
        other.czas = other._minuty + other._sekundy

        if self.czas < other.czas:
            return True
        else:
            return False

        if self.czas > other.czas:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._minuty + self._sekundy == other._minuty + other._sekundy:
            return True
        else:
            return False


    def __repr__(self):
        return f'czas: {self._minuty}min, {self._sekundy}sek'


if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    tablica = []
    # print(CzasBiegacza(10, 20))
    # print(CzasBiegacza(10, -20))
    # print(CzasBiegacza(-10, 20))
    tablica.append(CzasBiegacza(3,3))
    tablica.append(CzasBiegacza(2,3))
    tablica.append(CzasBiegacza(2,3))
    tablica.append(CzasBiegacza(1,1))
    tablica.append(CzasBiegacza(0,1))
    tablica.sort()
    print(tablica)
    pass
