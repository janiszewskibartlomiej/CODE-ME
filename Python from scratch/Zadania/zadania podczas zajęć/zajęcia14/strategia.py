
from jednostki.lucznik import Lucznik
from jednostki.rycerz import Rycerz

if __name__ == '__main__':

    l = Lucznik()
    print(l)
    l.maszeruj(10)
    l.atakuj()
    print(l)

    r = Rycerz()
    print(r)
    r.maszeruj(10)
    r.atakuj()
    print(r)
