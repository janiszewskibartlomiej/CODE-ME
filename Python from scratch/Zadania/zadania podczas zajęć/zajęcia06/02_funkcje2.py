# funkcja, która przyjmuje jeden parametr i nie zwraca żadnej wartości


def dodaj_sto(liczba):
    wynik = liczba + 100
    print(f'{liczba} + 100 = {wynik}')


wartosc = 23

# funkcja, która nie ma wewnątrz swojego bloku wyrażenia `return` zwraca `None`
nowa_wartosc = dodaj_sto(wartosc)

print(nowa_wartosc)
