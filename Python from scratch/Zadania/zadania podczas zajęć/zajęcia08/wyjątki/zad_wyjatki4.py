print('Początek programu')

try:
    wartosc = 13 / 0
except ZeroDivisionError:
    print('Dzielenie przez zero!')
    raise ZeroDivisionError('Ten wyjątek rzuciłem sam.')
finally:
    print('Ta linijka będzie zawsze wykonana')

print('Koniec programu')
