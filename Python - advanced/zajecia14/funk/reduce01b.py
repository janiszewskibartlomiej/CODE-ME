from functools import reduce
from operator import mul

wynik = reduce(mul, [1, 2, 3, 4, 5])

print(wynik)
