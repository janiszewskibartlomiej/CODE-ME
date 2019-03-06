# etap 3
from zadanie0302_e1 import zaokraglone

liczby = [74.59, 52.812, 41.329, 23.323, 78.828, 74.6, 49.828, 3.685, 88.161, 62.02]


polskie = [(str(element)).replace('.',',') for element in liczby] # tutaj wypełnij
polskie_z_e1 = [(str(element)).replace('.',',') for element in zaokraglone] # tutaj wypełnij
print(polskie)
print()
print(polskie_z_e1)