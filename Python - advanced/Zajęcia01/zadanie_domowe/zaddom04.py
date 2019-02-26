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

    def __add__(self, other):
        minuty_nowe = self._minuty + other._minuty
        sekundy_nowe = self._sekundy + other._sekundy
        if sekundy_nowe >= 60:
            sekundy_nowe -= 60
            minuty_nowe += 1
        return CzasBiegacza(minuty_nowe, sekundy_nowe)

    def __sub__(self, other):
        try:
            odejmowane_minuty = self._minuty - other._minuty
            odejmowane_sekundy = self._sekundy - other._sekundy
            if odejmowane_sekundy < 0:
                try:
                    odejmowane_minuty -= 1
                    odejmowane_sekundy +=60

                except:
                    ValueError('ujemny wynik')
        except:
            ValueError('ujemny wynik !')

        return CzasBiegacza(odejmowane_minuty, odejmowane_sekundy)

if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    tablica = []

    tablica.append(CzasBiegacza(3, 3))
    tablica.append(CzasBiegacza(2, 3))
    tablica.append(CzasBiegacza(2, 3))
    tablica.append(CzasBiegacza(1, 1))
    tablica.append(CzasBiegacza(0, 1))
    print(tablica)

    for index, element in enumerate(tablica): print(f'nr indexu: {index}| {element}')

    print(tablica[0] > tablica[1])
    print(tablica[2] > tablica[3])
    print(tablica[3] > tablica[4])
    print(tablica[4] > tablica[1])

    czas1 = CzasBiegacza(1, 59)
    czas1 += CzasBiegacza(1, 59)
    print(czas1)

    czas2 = CzasBiegacza(2, 1)
    czas2 += CzasBiegacza(3, 2)
    print('\n', czas2)

    czas3 = CzasBiegacza(1, 59)
    czas3 -= CzasBiegacza(1, 58)
    print('\n',czas3)

    czas4 = CzasBiegacza(2, 1)
    czas4 -= CzasBiegacza(0, 22)
    print('\n', czas4)

    czas5 = CzasBiegacza(2, 1)
    czas5 -= CzasBiegacza(2, 22)
    print('\n', czas5)
    pass

