import jednostki.wojownik
from jednostki.lucznik import Lucznik
from jednostki.rycerz import Rycerz

rycerze = []

for element in range(4):
    r = Rycerz()
    rycerze.append(r)

print(rycerze)

for element in rycerze:
    element.maszeruj(2000)

print(rycerze)

rycerze.append(Rycerz())

print(rycerze)

for element in rycerze:
    element.atakuj()

print(rycerze)
