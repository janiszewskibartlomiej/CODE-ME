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

wierszyk = wierszyk.lower()

for znak_do_usuniecia in ['.', ',', '-', '"', ':']:
    wierszyk = wierszyk.replace(znak_do_usuniecia, '')

    #>>> 'Hello world'.replace('world', 'Guido')
    # 'Hello Guido'

wyrazy = wierszyk.split()

print('Liczba wyrazów:', len(wyrazy))

wyrazy.sort()  # posortowanie listy 'wyrazy'
# wyrazy = sorted(wyrazy)  # stworzenie nowej, posortowanej wersji listy 'wyrazy'

wyrazy_str = ', '.join(wyrazy)
print('Posortowane wyrazy:', wyrazy_str)

trzy_pierwsze = ', '.join(wyrazy[:3])
trzy_ostatnie = ', '.join(wyrazy[-3:])

print('Trzy pierwsze wyrazy:', trzy_pierwsze)
print('Trzy ostatnie wyrazy:', trzy_ostatnie)
