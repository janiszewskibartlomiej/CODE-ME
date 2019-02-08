class Konto:
    def __init__(self):
        self.saldo = 0
        self.waluta = 'PLN'


    def wplata(self, kwota):
        self.saldo += kwota
        print('Wpłacono {}{}'.format(kwota, self.waluta))


    def wyplata(self,kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
        else:
            print('Brak środków na koncie!')

        print('Wypłacono {}{}'.format(kwota, self.waluta))

    def __repr__(self):
        return 'Konto(saldo: {:.2f}{})'.format(self.saldo, self.waluta)

class KontoOszczednosciowe(Konto):
    def __init__(self, procent):
        super().__init__()
        self.oprocentowanie = float(procent)

    def dolicz_odsetki(self, dni):
        odsetki_dzienne = self.oprocentowanie/365
        odsetki_procentowo = odsetki_dzienne*dni
        kwota_odsetek = (self.saldo*odsetki_procentowo)/100
        self.saldo += kwota_odsetek

        print('Odsetki po {} dniach wynoszą {:.2f}{}'.format(dni, kwota_odsetek, self.waluta))
