# Zadanie 1:

Napisz program, który będzie wczytywał liczby całkowite z klawiatury tak długo, aż ich suma będzie większa niż 100.
Ponadto:
- Po każdym wprowadzeniu liczby z klawiatury wypisze tę liczbę i wszystkie wpisane do tej pory, oraz sumę, w komunikacie:

> "Suma liczb (lista wpisanych liczb) to: (tutaj obliczona suma)


## Rozszerzenie a:
(Uwaga: każde rozszerzenie powinno być osobnym plikiem.)

Program ma ignorować liczby ujemne i zero. Jeśli użytkownik wpisze taką liczbę, nie ma być ona dodana do sumy ani zapamiętana, ale program ma wczytywać liczby dalej.

## Rozszerzenie b:
Funkcja `sum(lista)` zwraca sumę wszystkich elementow listy `lista`. Zmodyfikuj program tak, aby wykorzystał tę funkcję. W tym programie użyj pętli `while True`.

## Rozszerzenie c (trudniejsze):
Zmień komunikat wypisywany po każdej wpisanej liczbie, aby brzmiał tak:

> "1 + 2 + 18 = 21"

gdy wpisane zostały liczby 1, 2, 18, oraz tak:

> "4 = 4"

gdy wpisana została tylko jedna liczba, 4.