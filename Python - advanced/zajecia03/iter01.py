class ParzysteLiczby:
    def __init__(self):
        self.liczba = 0

    def __next__(self):
        self.liczba += 2

        if self.liczba > 100:  # najwyraźniej, nie chcemy liczb parzystych większych niż 100 :)
            raise StopIteration
        return self.liczba

    def __iter__(self):
        return self


if __name__ == '__main__':
    p_licz = ParzysteLiczby()

    for liczba in p_licz:
        print(liczba)
