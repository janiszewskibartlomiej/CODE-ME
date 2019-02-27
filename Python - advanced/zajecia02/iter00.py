#https://docs.python.org/3/glossary.html#term-iterable

class ParzysteLiczby:
    def __init__(self):
        self.liczba = 0


if __name__ == '__main__':
    p_licz = ParzysteLiczby()

    # poniższa pętla nie ma prawa działać
    for liczba in p_licz:
        print(liczba)
