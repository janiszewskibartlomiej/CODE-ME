class ParzysteLiczby:
    def __init__(self):
        self.liczba = 0

    def __next__(self):
        self.liczba += 2

        if self.liczba > 100:
            raise StopIteration
        return self.liczba

    def __iter__(self):
        return self


if __name__ == '__main__':
    pass  # tutaj możesz testować działanie funkcji
