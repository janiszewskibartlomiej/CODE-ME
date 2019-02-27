class TekstWRamce:
    def __init__(self, tekst):
        self.tekst = tekst

    def __doc__(self):
        return "Klasa opakowująca tekst w ramkę z zadanego znaku"

    def __call__(self, znak='*'):
        """
        Zwraca tekst w ramce
        :param znak: znak użyty do stworzenia ramki
        :return: tekst w ramce
        """
        linia = znak * (len(self.tekst) + 2)
        linia_z_tekstem = f'{znak}{self.tekst}{znak}'
        return f'{linia}\n{linia_z_tekstem}\n{linia}'


if __name__ == '__main__':
    twr = TekstWRamce('Beautiful is better than ugly')
    print(twr())
    help(twr)

    print(twr.__doc__())  # subtelna różnica
