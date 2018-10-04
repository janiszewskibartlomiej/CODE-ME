# Zadanie "Lista słowników"

Program będzie pracował na poniższej liście słowników:
```
gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]
```

### Uwagi:
- W tych zadaniach używamy słownika `gracze` jako obiektu dostępnego globalnie. Nie musimy przekazywać go do funkcji jako argument.
- Żeby utrzymać porządek w kodzie, każdy etap zapisz w oddzielnym pliku.

## Etap 1:
- Napisz funkcję `wypisz_imiona_graczy`, która nie będzie przyjmować żadnego argumentu, ani zwracać wartości.
- Funkcja wypisze imiona graczy na ekran. Jedno imię w jednej linii.
- Wywołaj tę funckję

## Etap 2:
- Napisz funkcję `lista_imion_graczy`, która nie będzie pryjmować żadnego argumentu.
- Funkcja ma zwracać listę zawierającą imiona graczy.
- Zapisz wartość zwróconą przez tę funkcję do zmiennej i wydrukuj ją na ekranie.
- **Rozszerzenie a**: Dodaj do funkcji argument domyślny `posortowane` ustawiony na `False`. Jeśli użytkownik nie przekaże tego argumentu, funkcja działa jak poprzednio. Jeśli użytkownik ustawi ten argument na `True`, funkcja zwróci posortowaną listę imion.

## Etap 3:
- Napisz funkcję `ile_razy_wygral`, która przyjmuje jeden argument: imię zawodnika.
- Dla zadanego imienia funkcja ma wypisać komunikat, np.: 'Gracz "Barnaba" wygrał(a) 9 gier.'
- **Rozszerzenie a**: Rozszerz komunikat o to, jakim procentem wszystkich gier, są jego wygrane, np.: 'Gracz "Barnaba" wygrał(a) 9 gier (64% wszystkich).'
- **Rozszerzenie b**: Jeśli wpisano imię, którego nie ma na liście, wyświetl stosowny komunikat.

## Etap 4:
- Napisz funkcję `dodaj_gre`, która przyjmuje dwa argumenty: `zwyciezca` i `przegrany`. Te argumenty, to imiona graczy z listy `gracze`.
- Funkcja ma doliczyć jedno zwycięstwo wygranemu i jedną porażkę przegranemu.
- Wywołaj funkcję a następnie wypisz na ekran słownik `gracze`, aby upewnić sie, że zmiany zostały zapisane.

## Etap 5:
- Napisz funkcję `dodaj_gracza`, która przyjmie jeden argument: imię nowego gracza.
- Stwórz słownik, z tymi samymi kluczami, co inni gracze. Nowy gracz ma na starcie 0 zwycięstw i 0 porażek.
- Wywołaj funkcję z nowym imieniem a następnie wypisz na ekran słownik `gracze`, aby upewnić sie, że zmiany zostały zapisane.
