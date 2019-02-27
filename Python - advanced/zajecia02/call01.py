class TekstWRamce:
    def __init__(self, tekst):
        self.tekst = tekst

    def daj_tekst_w_ramce(self, znak='*'):
        linia = znak * (len(self.tekst) + 2)
        linia_z_tekstem = f'{znak}{self.tekst}{znak}'
        return f'{linia}\n{linia_z_tekstem}\n{linia}'


if __name__ == '__main__':
    twr = TekstWRamce('Beautiful is better than ugly')
    print(twr.daj_tekst_w_ramce())
    print(twr.daj_tekst_w_ramce('x'))
    print()
    # moja ciekawośći - wywołanie klasy
    print(TekstWRamce('Beautiful is better than ugly').daj_tekst_w_ramce())
    #print(TekstWRamce.daj_tekst_w_ramce())
    print(TekstWRamce('Beautiful is better than ugly').daj_tekst_w_ramce)
