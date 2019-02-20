class Kot:
    _lapy = 4

    def __init__(self, imie):
        self.imie = imie

    def __repr__(self):  #metoda reprezentation drukowania na ekran
        # zamiast info o obiekcie w pamieci. drukuje jedną bezpośrednią informację
        # a metoda def __str__ info dla człowieka [jest nadrzędny na repl].
        # wykozystujemy głównie repl!
        return f'Kot {self.imie}'

    def daj_glos(self):
        print("Miau!")


if __name__ == '__main__':
    k = Kot('Filemon')
    print(k)
    k.daj_glos()

    # print(str(k))
