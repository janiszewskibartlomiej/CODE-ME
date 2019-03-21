from jednostki.rycerz import Rycerz

rycerze = []

for _ in range(4):
    rycerze.append(Rycerz())

print(rycerze)

for rycerz in rycerze:
    rycerz.maszeruj(2000)

rycerze.append(Rycerz())

for rycerz in rycerze:
    rycerz.atakuj()

print(rycerze)