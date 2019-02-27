# Zadanie 02 - 01

W tym zadaniu należy rozwinąć klasę `ParzysteLiczby` z pliku `iter02.py`.
Jako szablon do zadania wykorzystaj plik `zadanie0201.py` (możesz przenieść go poza ten katalog).

## Etap 1
- Dodaj do klasy możliwość podania górnej granicy, przy jakiej liczbie iterator przestanie podawać nowe liczby. Parametr ten ma być wymagany. Iterator ma przerwać podawanie liczb bezpośrednio przed górną granicą.
- Dodaj do klasy możliwość podania, od jakiej liczby iterator zacznie podawać liczby parzyste. Domyślna wartość ma wynosić 0.
- Zmodyfikuj klasę tak, aby podana powyżej liczba rzeczywiście była pierwszą, która jest będzie podana przez iterator.
- Liczby ujemne również są dopuszczalne.

## Etap 2
- Zmień nazwę klasy na `ZakresLiczb` i dodaj możliwość podania kroku, o jaki powiększona będzie kolejna zwrócona przez iterator liczba. Domyślną wartością ma być 1.
- W poprzednim etapie, użytkownik wpisując niepoprawny przedział nie dostawał żadnych liczb (co jest zgodne z intuicją). W obecnej sytuacji, podanie zerowego albo ujemnego kroku spowoduje, że iterator będzie generował liczby w nieskończoność. Zabezpiecz klasę przed tą sytuacją rzucając `ValueError` w inicjalizatorze.
