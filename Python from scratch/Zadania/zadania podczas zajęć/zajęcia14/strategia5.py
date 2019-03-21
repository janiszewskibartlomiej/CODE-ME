from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik

p = Rycerz()
print(p)
p.maszeruj(10)
print(p)
p.atakuj()
print(p)

l = Lucznik()
print(l)
l.maszeruj(15)
print(l)
l.atakuj()
print(l)
