# wynik_dzielenia_przez_zero = 13 / 0  # odkomentuj, żeby zobaczyć wyjątek

print("Początek programu")

try:
    wynik_dzielenia_przez_zero = 13 / 0
except ZeroDivisionError:
    pass  # uciszając wyjątek tracimy potencjalnie ważną informację

print('Program działa dalej.')