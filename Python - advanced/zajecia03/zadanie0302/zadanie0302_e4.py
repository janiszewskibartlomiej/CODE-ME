# etap 4

from random import uniform

lista_liczb = []
for x in range(10):
    x = round(uniform(0, 100), 3)
    lista_liczb.append(x)

print(lista_liczb)
