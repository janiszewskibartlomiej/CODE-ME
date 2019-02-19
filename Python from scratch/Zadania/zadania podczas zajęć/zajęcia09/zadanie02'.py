liczba1 = int(input('Wpisz liczbę naturalną nr 1:'))
liczba2 = int(input('Wpisz liczbę naturalną nr 2:'))

import math
wyliczenie = math.gcd(liczba1, liczba2)

print(f'Największy wspólny dzielnik liczb {liczba1} i {liczba2} to: {wyliczenie}')