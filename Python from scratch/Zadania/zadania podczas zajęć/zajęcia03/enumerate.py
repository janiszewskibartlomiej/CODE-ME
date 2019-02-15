imiona = ['Artur', 'Barbara', 'Czesław', 'Danuta']

print(imiona)

print(enumerate(imiona))  # to co tu otrzymujemy to obiekt iteratora

# Iterator zwraca nowe elementy, gdy zostanie "odpytany", np. przez
# pętle for, albo przez funkcję list(), która tworzy nową listę.

print(list(enumerate(imiona)))  # Stworzyliśmy listę, która ma cztery elementy.

# Każdy element składa się z tupli (krotki), która z kolei składa się z
# indeksu i wartości, z której nowa lista powstała.

nowa_lista = list(enumerate(imiona))

print(nowa_lista[2])
print(nowa_lista[2][0])
print(nowa_lista[2][1])