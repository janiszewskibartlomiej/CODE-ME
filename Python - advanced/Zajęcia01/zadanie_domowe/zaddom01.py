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


    def __repr__(self):
        return f'czas: {self._minuty}min, {self._sekundy}sek'



if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy

    print(CzasBiegacza(10, 20))
    print(CzasBiegacza(10, -20))
    print(CzasBiegacza(-10, 20))

    pass

