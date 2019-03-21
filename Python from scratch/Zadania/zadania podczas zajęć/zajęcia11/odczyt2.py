plik = open('dane-cp1250.txt', 'r')  # domyślnym kodowaniem na Windowsie jest cp1250

zawartosc = plik.read(20)

print(zawartosc)

print(f'wczytano {len(zawartosc)} znaków')