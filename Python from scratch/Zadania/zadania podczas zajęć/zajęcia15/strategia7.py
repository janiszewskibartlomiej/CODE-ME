from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik

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

# etap 7

lucznicy = []

for _ in range(3):
    lucznicy.append(Lucznik())

armia = rycerze + lucznicy

print(armia)

for wojownik in armia:
    wojownik.atakuj()

print(armia)