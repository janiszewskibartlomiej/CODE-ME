# Zadanie - testy doświadczenia jednostek

# Etap 1:
- Do klasy `TestWojownik` dopisz test sprawdzający, czy doliczanie doświadczenia za marsz działa poprawnie.
    - Stwórz metodę `test_marsz`. Stwórz w tej metodzie obiekt klasy Wojownik i wydaj mu rozkaz przejścia dystansu 1000m. Sprawdź wartość atrybutu `doswiadczenie` tego obiektu z wartością, której się spodziewasz.

# Etap 2:
- Stwórz nową klasę `TestRycerz`, dziedziczącą po `unittest.TestCase`.
- Stwórz w niej metodę `test_atakuj`, w której przetestowane zostaną zmiany w doświadczeniu, po wykonaniu jednego ataku.
- Stwórz metodę `test_stworzenie_udane`, analogiczną do metody z klasy `TestWojownik`, testującą, czy nowo stworzony rycerz startuje z 60 pkt życia i 0 doświadczenia.

# Etap 3:
- Stwórz nową klasę `TestDruzyna`, dziedziczącą po `unittest.TestCase`.
- Przetestuj w niej dwie metody klasy `Drużyna`: `__init__()` oraz `dodaj_wojownika()`.