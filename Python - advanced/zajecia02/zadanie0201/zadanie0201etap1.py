class ParzysteLiczby:
    def __init__(self, end, start=0): #atrybuty z wartością domyślna wrzucamy na koniec
        self.liczba = start
        self.end = end

    def __next__(self):
        if self.liczba >= self.end:
            raise StopIteration
        zwracana = self.liczba
        self.liczba += 2
        return zwracana

    def __iter__(self):
        return self


if __name__ == '__main__':
    liczby = ParzysteLiczby(80, -4)
    print(list(liczby))
    liczby = list(ParzysteLiczby(100))
    print('\n', liczby)
    liczby = list(ParzysteLiczby(20, 10))
    print('\n', liczby)
    pass  # tutaj możesz testować działanie funkcji
