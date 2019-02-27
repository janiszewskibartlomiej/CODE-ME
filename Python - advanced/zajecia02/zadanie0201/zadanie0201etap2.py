class ZakresLiczb:
    def __init__(self, gorna_granica, start=0, krok=1):
        self.liczba = start-2
        self.maksimum = gorna_granica
        self.co_ile = krok
        if krok <=0:

            raise ValueError('Podano błedny zakres skoku')

    def __next__(self):
        self.liczba += self.co_ile



        if self.liczba > self.maksimum -2:
            raise StopIteration
        return self.liczba

    def __iter__(self):
        return self


if __name__ == '__main__':
    liczby2 = list(ZakresLiczb(77, -4, 2))
    print(liczby2)
    print('---------')
    liczby = list(ZakresLiczb(77, -4, -2))
    print(liczby)
    pass  # tutaj możesz testować działanie funkcji
