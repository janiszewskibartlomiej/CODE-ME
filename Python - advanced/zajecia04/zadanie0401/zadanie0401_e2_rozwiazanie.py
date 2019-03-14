import json


def odczytaj_json():
    try:
        plik = open('dane.json', mode='r')
        dane = json.load(plik)
        plik.close()
        return dane
    except FileNotFoundError:
        return []


def zapisz_json(dane):
    plik = open('dane.json', mode='w')
    json.dump(dane, plik)
    plik.close()


class Dane:
    def __enter__(self):
        self._dane = odczytaj_json()
        return self._dane

    def __exit__(self, *args):
        zapisz_json(self._dane)


if __name__ == '__main__':
    with Dane() as d:
        klient = {'imie': 'Antoni', 'numer_telefonu': 123123123}
        d.append(klient)
