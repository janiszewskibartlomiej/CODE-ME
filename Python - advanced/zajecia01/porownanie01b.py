class Wyraz:
    """
    Klasa definiująca wyrazy, które można porównywać po liczbie liter
    """

    def __init__(self, wyraz):
        self._wyraz = wyraz

    def __repr__(self):
        return self._wyraz

    def __lt__(self, other):
        if len(self._wyraz) < len(other._wyraz):
            return True
        else:
            return False

    def __le__(self, other):
        if len(self._wyraz) <= len(other._wyraz):
            return True
        else:
            return False

    # bez __eq__() też działa


if __name__ == '__main__':
    m = Wyraz('Magik')
    p = Wyraz('Prestidigitator')

    print(f'{m} > {p} : {m > p}')
    print(f'{m} < {p} : {m < p}')

    print(f'{m} >= {p} : {m >= p}')
    print(f'{m} <= {p} : {m <= p}')

    print(f'{m} == {p} : {m == p}')
    print(f'{m} != {p} : {m != p}')
