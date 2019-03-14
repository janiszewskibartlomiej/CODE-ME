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
        return odczytaj_json()

    def __exit__(self, *args):
        pass


if __name__ == '__main__':
    with Dane() as d:
        klient = {'imie': 'Antoni', 'numer_telefonu': 123123123}
        d.append(klient)

        zapisz_json(d)
