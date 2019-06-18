from functools import reduce

liczby = [-3, 4, 3, -1, 2]

# wynik = reduce(lambda x, y: max(x, y), liczby)  # bez sensu komplikacja :)

wynik = reduce(max, liczby)

print('Największa liczba to:', wynik)
