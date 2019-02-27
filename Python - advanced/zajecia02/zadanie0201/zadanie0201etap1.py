class ParzysteLiczby:
    def __init__(self, gorna_granica, start=0):
        self.liczba = start-2
        self.maksimum = gorna_granica

    def __next__(self):
        self.liczba += 2

        if self.liczba > self.maksimum -2:
            raise StopIteration
        return self.liczba

    def __iter__(self):
        return self


if __name__ == '__main__':

    liczby = list(ParzysteLiczby(80, -4))
    print(liczby)
    pass  # tutaj możesz testować działanie funkcji
