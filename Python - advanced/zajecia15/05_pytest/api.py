# ...

class ZlyFormatDanych(Exception):
    pass


def _policz_sume(przedmioty):
    suma = 0
    for przedmiot in przedmioty:
        try:
            if przedmiot['waga']:
                suma += przedmiot['ilosc'] * przedmiot['waga']
        except KeyError:
            raise ZlyFormatDanych('Przedmiot nie posiada klucza "ilosc" lub "waga"')
    return suma

# ...
