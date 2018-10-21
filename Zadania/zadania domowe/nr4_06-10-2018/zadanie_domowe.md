# Zadanie domowe: "Loteria"

- Celem zadania jest stworzenie gry losowej przypominającej "Lotto".
- Nasza loteria będzie polegała na skreśleniu czterech liczb ze zbioru od 1 do 19.
- Poszczególne etapy zadania tworzą całość.

## Etap 1:
- Napisz funkcję `chybil_trafil`, która będzie zwracać posortowaną listę czterech różnych, losowo wybranych liczb. Funkcja nie powinna niczego pisać na ekran.
- Przetestuj tę funkcję, wywołując ją, jej wartość zapisując do zmiennej a następnie wypisując jej zawartość na ekran.

## Etap 2:
- Stwórz pustą listę `wszystkie_zaklady`, która będzie dostępna globalnie dla funkcji w naszym skrypcie.
- Napisz funkcję `dodaj_zaklad`, która będzie przyjmować jeden argument: `zaklad`. Tym argumentem będzie posortowana lista czterech liczb.
    - Powyższa funkcja ma dodać do listy `wszystkie_zaklady` zakład, który został do funkcji przekazany w argumencie. Jako, że zakład sam jest listą, w efekcie mamy dostać listę list.
    - Funkcja nie ma zwracać żadnej wartości.
- Przetestuj działanie tej funkcji w następujący sposób:
    - wypisz na ekran zawartość listy `wszystkie_zaklady`
    - stwórz samodzielnie listę czterech liczb: `moj_zaklad = [1, 2, 3, 4]`
    - uruchom funkcję `dodaj_zaklad` przekazując jej argument `moj_zaklad`.
    - ponownie wypisz na ekran zawartość listy `wszystkie_zaklady` i zobacz, czy `moj_zaklad` został dodany.

## Etap 3:
- Do listy `wszystkie_zaklady` dodaj jeszcze dziesięć zakładów wygenerowanych za pomocą funkcji `chybil_trafil`. Użyj do tego celu pętli `for` oraz funkcji `range()`.
- Tak jak poprzednio, wyświetl na ekran zawartość zmiennej `wszystkie_zaklady` aby przekonać się, że nowe zakłady zostały poprawnie dodane.

## Etap 4:
- Napisz funkcję `czy_jest_zwyciezca`, która będzie przyjmowała jeden argument `zwycieskie_liczby`, który będzie listą liczb (zakładamy, że przekazana lista jest posortowana).
    - Funkcja ma sprawdzać, czy lista `zwycięskie_liczby` znajduje się chociaż raz na liście `wszystkie_zaklady`. Jeśli tak: funkcja ma wypisać komunikat: "Mamy zwycięzcę I stopnia, który poprawnie skreślił liczby: (tutaj wpisz liczby)". Jeśli nikt nie skreślił prawidłowych liczb wyświetl komunikat: "Tym razem nie ma zwycięzcy"
- Przetestuj tę funkcję, przekazując jej jako `zwycieskie_liczby` listę `[1, 2, 3, 4]`, którą dołączyliśmy wcześniej i która wiemy, że znajduje się w naszej liście `wszystkie_zaklady`.

### Podpowiedź:
W Pythonie można w łatwy sposób sprawdzić, czy element `el` jest obecny na  liście `lst`:
```
el in lst
```
To wyrażenie zwróci `True` jeśli znalazł się na liście i `False` w przeciwnym przypadku, dzięki temu bez problemu można je wstawić do wyrażenia warunkowego `if`.

## Etap 5:
W tym etapie należy podzielić program na dwa pliki. Trzeba pamiętać, że gdy wyniesiemy funkcje do innego pliku, stracą one dostęp do globalnej zmiennej `wszystkie_zaklady`. Dodaj zatem do tych funkcji nowy argument `wszyskie_zaklady`. Następnie dodaj brakujący argument do wywołań tych funkcji.
- Zmodyfikuj funkcje i sprawdź czy program nadal działa. Uwaga! Jedna funkcja nie wymaga modyfikacji.
- Wynieś do pliku `loteria_funkcje.py` wszystkie funkcje. Zaimportuj je następnie w głównym pliku programu.
- Zmienna `wszystkie_zaklady` ma pozostać w głównym pliku.

## Etap 6:
W głównym programie:
- Pod zmienną `moje_liczby` wpisz "na sztywno", w kodzie swoje liczby i dodaj je do zakładów.
- Dolosuj jeszcze 100 kolejnych zakładów na "chybił trafił".
- Zadeklaruj zmienną `zwycieskie_liczby`, które również wylosuj metodą "chybił trafił".
- Wydrukuj na ekranie komunikat: "Zwycięskie liczby to dziś: (tutaj zwycieskie liczby)".
- Sprawdź czy wśród zakładów jest zwycięzca.
- Sprawdź czy Twoje liczby są zwycięskie.

### Epilog:
Mimo mocnego ograniczenia liczb biorących udział w grze, nadal ekstremalnie trudno jest wygrać w tę grę. Posteruj parametrami gry, aby zobaczyć przy jakich ustawieniach Twoja wygrana padła. Sprawdź ilu graczy musi wziąć udział, aby zwycięzca w ogóle zaczął się pojawiać.

### Rozszerzenie:
Dołącz do programu funkcję wczytującą liczby do zmiennej `moje_liczby` od Użytkownika z klawiatury.
- Funkcja ta ma być umieszczona w oddzielnym pliku i importowana do pliku głównego.
- Funkcja ma wczytywać wszystkie cztery liczby w jednej linii (konwencja, jak mają być pooddzielane od siebie liczby jest dowolna, ale Użytkownik musi być o tym poinformowany).
- Funkcja ma być odporna na wszystkie możliwe błędy Użytkownika.
- Funkcja ma zwracać posortowaną listę czterech różnych liczb z zakresu od 1 do 19 włącznie.