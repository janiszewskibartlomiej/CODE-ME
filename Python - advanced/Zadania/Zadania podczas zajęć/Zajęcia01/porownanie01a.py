#https://docs.python.org/3/reference/datamodel.html#object.__lt__

#object.__lt__(self, other)
# object.__le__(self, other)
# object.__eq__(self, other)
# object.__ne__(self, other)
# object.__gt__(self, other)
# object.__ge__(self, other)
# These are the so-called “rich comparison” methods.
# The correspondence between operator symbols and method names is as follows:
# x<y calls x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y),
# x!=y calls x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).

class Wyraz:
    """
    Klasa definiująca wyrazy, które można porównywać po liczbie liter
    """

    def __init__(self, tekst):
        self._tekst = tekst

    def __repr__(self):
        return self._tekst

    def __lt__(self, other):
        if len(self._tekst) < len(other._tekst):
            return True
        else:
            return False

    def __le__(self, other):
        if len(self._tekst) <= len(other._tekst):
            return True
        else:
            return False

    def __eq__(self, other):
        if len(self._tekst) == len(other._tekst):
            return True
        else:
            return False


if __name__ == '__main__':
    m = Wyraz('Magik')
    p = Wyraz('Prestidigitator')

    print(f'{m} > {p} : {m > p}')
    print(f'{m} < {p} : {m < p}')

    print(f'{m} >= {p} : {m >= p}')
    print(f'{m} <= {p} : {m <= p}')

    print(f'{m} == {p} : {m == p}')
    print(f'{m} != {p} : {m != p}')
