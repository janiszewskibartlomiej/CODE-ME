# wynik_dzielenia_przez_zero = 13 / 0  # odkomentuj, żeby zobaczyć wyjątek

print('Początek programu')

try:
    wynik_dzielenia_przez_zero = 13 / 0
except ZeroDivisionError:
    print('Ktoś próbował dzielić przez zero!')

print('Program działa dalej.')