# Zadanie "Sklep" - etap 1:

Stwórz plik `zadanie_sklep.py` w którym:
- Na górze pliku umieść tę listę słowników:
```
slodycze = [
    {'nazwa': 'czekolada', 'cena': 2.69, 'czy_na_sztuki': True},
    {'nazwa': 'wafel', 'cena': 1.99, 'czy_na_sztuki': True},
    {'nazwa': 'ciastka', 'cena': 5.99, 'czy_na_sztuki': True}
]
```
Powyższa lista jest zdefiniowana globalnie, zatem nie przekazujemy jej jako argumentu do funkcji.

- Poniżej zdefiniuj cztery funkcje:
  1. Funkcja `wypisz_artykuly` nie przyjmuje żadnego parametru i nie zwraca żadnej wartości. Jej zadaniem jest wypisanie nazw sprzedawanych artykułów, jeden po drugim, każdy w nowej linii.
  2. Funkcja `podaj_cene` przyjmuje jeden argument: nazwę artykułu i nie zwraca żadnej wartości. Funkcja dla danego argumentu wypisuje na ekran komunikat: "(tutaj nazwa artykułu) kosztuje (tutaj cena)zł". Jeśli dany artykuł nie został znaleziony, nic się nie dzieje.
  3. Funkcja `zmien_cene` przyjmuje dwa argumenty: nazwę artykułu oraz nową cenę. Funkcja nie zwraca żadnej wartości. Dla podanego artykułu funkcja zmienia jego cenę na tę podaną jako argument do funkcji.
  4. Funkcja `dodaj_artykul` przyjmuje dwa argumenty: nazwę artykułu oraz jego cenę. Funkcja nie zwraca żadnej wartości. Funkcja tworzy artykuł, czyli słownik z trzema kluczami. Pod kluczami `nazwa` i `cena` zapisuje odpowiednie wartości przekazane z parametrów, a trzeci klucz: `czy_na_sztuki` ustawia na `True`. Nowy artykuł dodaje do listy `slodycze`.

- Na końcu pliku wywołaj funkcje w następujący sposób:
  - Wywołaj funkcję `wypisz_artykuly()`.
  - Użyj funkcji `podaj_cene()` do wypisania ceny czekolady.
  - Użyj funkcji `zmien_cene()` aby zmienic cene czekolady na 3.99 i ponownie wypisz na ekran cenę czekolady.
  - Użyj funkcji `dodaj_artykul()` aby dodać 'baton', który kosztuje 1.99 i ponownie wypisz na ekran wszystkie sprzedawane artykuły.