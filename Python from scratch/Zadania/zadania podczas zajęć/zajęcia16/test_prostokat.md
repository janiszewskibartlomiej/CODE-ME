# Zadanie - test prostokata

Korzystając z dokumentacji (https://docs.python.org/3/library/unittest.html) i przykładów z zajęć zmodyfikuj plik **test_prostokata.py** w następujący sposób:

- w metodzie (teście) `test_repr_zwraca_dobry_opis` wpisz wartość zmiennej `oczekiwana` tak, aby test przechodził.
- w metodzie (teście) `test_pole_jest_obliczone_prawidlowo` przetestuj metodę `pole` z klasy `Prostokat`. Aby to zrobić:
    - stwórz nowy obiekt klasy `Prostokat` o konkretnych parametrach.
    - używając metody `self.assertEquals` porównaj wartość obliczoną przez metodę `pole` z wartością, której się spodziewasz.
- napisz czwarty test, która sprawdzi, czy metoda `czy_kwadrat` działa poprawnie. W tym celu:
    - stwórz nowy obiekt `p1` klasy `Prostokat` o dwóch różnych bokach.
    - używając metody `self.assertFalse` sprawdź czy metoda `p1.czy_kwadrat()` faktycznie zwraca `False`.
    - stwórz nowy obiekt `p2` klasy `Prostokat` o dwóch równych sobie bokach.
    - używając metody `self.assertTrue` sprawdź czy metoda `p2.czy_kwadrat()` faktycznie zwraca `True`.

## Rozszerzenie:
Jest jeszcze jedna funkcjonalność, która nie została przetestowana. Nie sprawdziliśmy, czy podczas próby stworzenia obiektu `Prostokat` z ujemnymi bokami rzucony będzie wyjątek. Znajdź w dokumentacji jak napisać test, który sprawdzi pojawienie się wyjątku w danej sytuacji, a następnie napisz taki test dla klasy `Prostokat`.
