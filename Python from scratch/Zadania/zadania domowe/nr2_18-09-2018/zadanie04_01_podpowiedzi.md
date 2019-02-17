# Zadanie 2 (podpowiedzi):
- Pierwszymi działaniami programu powinno być zadeklarowanie zmiennej w której będzie przechowywana suma i pustej listy, do której dopisywane będą liczby.
- Nie wiadomo ile liczb zostanie wpisanych, więc w pętli `while` należy je wczytywać tak długo, aż ich suma przekroczy 100.

## Rozszerzenie a:
- Gdy już upewnimy się, że mamy liczbę ujemną, słowo kluczowe `continue` umożliwi nam przejście od razu do kolejnego powtórzenia pętli.

## Rozszerzenie b:
- Obliczając sumę z elementów listy, nie potrzebujemy już oddzielnej zmiennej przechowującej sumę. Pętla może być nieskończona a warunek wewnątrz niej, sprawdzający czy suma jest większa 100, wykonywałby polecenie `break`.

## Rozszerzenie c:
- `Metoda `.join()` skleja elementy listy, ale tylko gdy elementy te są stringami. Można: na bieżąco tworzyć oddzielną listę stringów obok listy liczb, użyć pętli `for` do użycia liczb z listy po kolei, użyć funkcji `map()` do stworzenia nowej sekwencji stringów z liczb, użyć "list comprehension" (https://hackernoon.com/list-comprehension-in-python-8895a785550b).