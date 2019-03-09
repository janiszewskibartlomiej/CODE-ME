# etap 4

from random import uniform
#
# lista_liczb = []
# for x in range(10):
#     x = round(uniform(0, 100), 3)
#     lista_liczb.append(x)

lista_liczb = [round(uniform(0, 100), 3) for x in range(10)]

print(lista_liczb)
