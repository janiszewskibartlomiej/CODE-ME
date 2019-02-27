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

    # klasy ParzysteLiczby można teraz użyć wszędzie, gdzie przyjmowany jest obiekt Iterable
    lista_liczb_parzystych = list(p_licz)
    print(lista_liczb_parzystych)
