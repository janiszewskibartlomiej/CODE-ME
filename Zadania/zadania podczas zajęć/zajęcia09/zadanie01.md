# Zadanie 01
Stwórz plik `geometria.py`, który będzie zawierał:
- funkcję `pole_prostokata` przyjmującą dwa argumenty: `a` i `b` odpowiadające dwóm bokom prostokąta. W przypadku gdy któryś bok będzie liczbą mniejszą od zera, funkcja ma zwrócić `None`, w pozostałych przypadkach ma zwrócić obliczone pole prostokąta.
- zmienną `WARTOSC_PI` ustawioną na wybrane przez Ciebie przybliżenie liczby Pi. Jako, że zmienna ta będzie używana jako stała, zgodnie z konwencją jest zapisywana WIELKIMI literami.
- funkcję `pole_kola` przyjmującą argument `r` oznaczający promień koła. Funkcja ma zwracać obliczone pole koła jeśli promień jest większy lub równy zero. Do obliczeń funkcja ma używać stałej `WARTOŚĆ_PI`. Jeśli promień jest mniejszy od zera, ma zwrócić `None`.

Następnie, stwórz plik `zadanie1.py`, który zaimportuje obie funkcje i stałą `WARTOSC_PI`. Następnie:
- Obliczy pole prostokąta o bokach `7.5` i `8.3` i wypisze na ekran stosowny komunikat.
- Obliczy pole prostokąta o bokach `4` i `-3` i wypisze na ekran stosowny komunikat.
- Obliczy pole koła o promieniu `3.57` i wypisze na ekran komunikat:
> Pole koła wynosi (tutaj obliczone pole) dla PI=(tutaj przyjęte przybliżenie PI).

## Rozszerzenie a:
- Próba obliczenia pola figury, której bok lub promień jest ujemny, jest poważnym błędem, który postanowiliśmy zasygnalizować wyjątkiem.
- Gdy funkcja zostanie wywołana z ujemnym parametrem, ma zostać "rzucony" wyjątek `ValueError`, który przerwie działanie programu.
- Aby uczynić wyjątek bardziej pomocnym dla użytkownika, dołącz do rzucanego wyjątku wiadomość, informującą co się stało. Użyj składni `ValueError('Treść komunikatu')`.
- Gdy upewnisz się, że wyjątki pojawiają się w odpowiednich momentach, wykomentuj w pliku `zadanie1.py` wywołanie funkcji z błędnymi argumentami.

## Rozszerzenie b:
- Zmodyfikuj funkcję `pole_prostokata` tak, aby gdy podany jest jeden argument, obliczane było pole kwadratu, a gdy podane są dwa argumenty, obliczane jest pole prostokąta. Podanie innej ilości atrybutów, ma być błędem.