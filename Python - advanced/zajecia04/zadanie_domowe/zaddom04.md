# Zadanie domowe 04

W pliku `zaddom04.py` znajdziesz funkcję `przykladowa_funkcja()`, która wykonuje swoje zadanie przez pewien czas.
W tym zadaniu będziemy chcieli zmierzyć czas wykonywania danej funkcji.

## Etap 1

Napisz funkcję `timer()`, która jako argument przyjmuje inną funkcję. Po wywołaniu funkcji `timer()`, przekazana jej funkcja ma zostać wywołana, a czas, jaki zajęło jej to wywołanie, ma zostać wypisany w nowej linii. Format wypisanej informacji: `Czas wykonania: 0:00:04.213313`. Przy mierzeniu czasu wykonania można wykorzystać metodę `now()` klasy `datetime` z modułu `datetime`.


## Etap 2

Napisz dekorator `timer_dekorator()`, który będzie mierzył czas działania funkcji tak samo, jak robiła to funkcja `timer()`. Wywołaj udekorowaną funkcję `przykladowa_funkcja()`, aby sprawdzić, czy rezultat jest taki sam jak w etapie 1.
