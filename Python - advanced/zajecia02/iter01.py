class ParzysteLiczby:
    def __init__(self):
        self.liczba = 0

    def __next__(self):
        self.liczba += 2
        return self.liczba

    def __iter__(self):
        return self


if __name__ == '__main__':
    p_licz = ParzysteLiczby()

    for liczba in p_licz:
        print(liczba)
