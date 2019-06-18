from functools import reduce

wynik = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

print(wynik)
