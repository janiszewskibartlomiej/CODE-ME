# dokumentacja tutaj: https://docs.python.org/3/library/pathlib.html

import pathlib

kat = pathlib.Path()

print(kat)  #drukuje kropkę ktora informuje o bierzacym katalogu
print(kat.absolute())  # drukuje całą ścieżkę

nowy_kat = kat / 'nowy_katalog'  # przeciążony operator "/" tworzy ścieżkę

print(nowy_kat)
print(nowy_kat.absolute())

print(f'Czy "{nowy_kat}" istnieje? {nowy_kat.exists()}') #drukuje czy isniej katalog

# poniższa linijka stworzy katalog
nowy_kat.mkdir()

print(f'Czy "{nowy_kat}" istnieje? {nowy_kat.exists()}')
