class ZakresLiczb:
    def __init__(self, end, start=0, step=1):
        self.liczba = start
        self.end = end

        if step <= 0:
            raise ValueError('Podano błedny zakres skoku')
        self.step = step

    def __next__(self):

        if self.liczba > self.end:
            raise StopIteration

        zwracana = self.liczba
        self.liczba += self.step
        return zwracana

    def __iter__(self):
        return self


if __name__ == '__main__':
    liczby2 = list(ZakresLiczb(77, -4, 2))
    print(liczby2)
    print('---------')
    liczby = list(ZakresLiczb(81, 1, 3))
    print(liczby)
    print('---------')
    liczby = list(ZakresLiczb(97, 12, 1))
    print(liczby)
    print('---------')
    liczby = ZakresLiczb(77, -4, -2)
    print(list(liczby))
    pass  # tutaj możesz testować działanie funkcji
