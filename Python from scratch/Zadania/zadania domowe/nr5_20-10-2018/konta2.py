class Konto:
    def __init__(self):
        self._saldo = 0
        self._waluta = 'PLN'

    def __repr__(self):
        return f'Konto(saldo:{self._saldo}{self._waluta})'

    def wplata(self, kwota):
        print(f'Wpłacono {kwota}{self._waluta}')
        self._saldo += kwota

    def wyplata(self, kwota):
        if kwota > self._saldo:
            print('Brak środków na koncie!')
        else:
            print(f'Wypłacono {kwota}{self._waluta}')
            self._saldo -= kwota


class KontoOszczednosciowe(Konto):

    def __init__(self, oprocentowanie):
        super().__init__()
        self.oprocentowanie = oprocentowanie
        self.bezplatna_wyplata = True

    def dolicz_odsetki(self, dni):
        odsetki = self._saldo * (self.oprocentowanie / 365 / 100) * dni
        odsetki = round(odsetki, 2)
        print(f'Odsetki po {dni} dniach wynoszą {odsetki}{self._waluta}')
        self._saldo += odsetki

    def wyplata(self, kwota):
        super().wyplata(kwota)
        if self.bezplatna_wyplata:
            self.bezplatna_wyplata = False
        else:
            print('Pobrano 5PLN za wypłatę z konta oszczędnościowego.')
            self._saldo -= 5

