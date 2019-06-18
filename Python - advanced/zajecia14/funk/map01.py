liczby_str = input('Wpisz liczby oddzielone spacją: ')

liczby_lista_str = liczby_str.split()

liczby_lista_int = map(int, liczby_lista_str)

for l in liczby_lista_int:
    print(l, type(l))
