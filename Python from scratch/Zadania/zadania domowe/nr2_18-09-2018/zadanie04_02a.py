wierszyk = '''Nad rzeczką opodal krzaczka
Mieszkała kaczka-dziwaczka,
Lecz zamiast trzymać się rzeczki
Robiła piesze wycieczki.

Raz poszła więc do fryzjera:
"Poproszę o kilo sera!"

Tuż obok była apteka:
"Poproszę mleka pięć deka."

Z apteki poszła do praczki
Kupować pocztowe znaczki.'''

# AD 1
wierszyk = wierszyk.lower()

# AD 2
wyrazy = wierszyk.split()

# AD 3
print('Liczba wyrazów:', len(wyrazy))

# AD 4
wyrazy.sort()

# AD 5
wyrazy_str = ', '.join(wyrazy)
print('Posortowane wyrazy:', wyrazy_str)

# AD 6
trzy_pierwsze = ', '.join(wyrazy[:3])
trzy_ostatnie = ', '.join(wyrazy[-3:])

print('Trzy pierwsze wyrazy:', trzy_pierwsze)
print('Trzy ostatnie wyrazy:', trzy_ostatnie)
