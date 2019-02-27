class TekstWRamce:
    def __init__(self, tekst):
        self.tekst = tekst

    def __call__(self, znak='*'):
        linia = znak * (len(self.tekst) + 2)
        linia_z_tekstem = f'{znak}{self.tekst}{znak}'
        return f'{linia}\n{linia_z_tekstem}\n{linia}'


if __name__ == '__main__':
    twr = TekstWRamce('Beautiful is better than ugly')
    print(twr())   #wołanie klasy z nawiasami oznacza dla python żeby wywołac funkcję
    print(twr('x'))
