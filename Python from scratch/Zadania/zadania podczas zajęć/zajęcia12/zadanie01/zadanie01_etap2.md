# Zadanie 01 "Logowanie czasu uruchomienia"
Rozszerzenia do zadania 01:

### Przygotowanie:
Stwórz plik `zadanie01.py`, który będzie połączeniem plików `odczyt.py` i `zapis.py`. Tym razem należy skopiować kod obu programów do jednego pliku, a nie importować. Stworzony plik ma:
- Na początku wyświetlić na ekranie dotychczasowe uruchomienia.
- Następnie, w nowej linii wyświetlić komunikat "Aktualne uruchomienie:"
- Na koniec zrobić to co robił plik `zapis.py`, czyli wyświetlić komunikat: "Skrypt został uruchomiony: (bieżący czas)" i dokleić linię z tym komunikatem do pliku `uruchomienia.log`.

### Rozszerzenie 1:
Powyższy program będzie działał tylko, gdy plik `uruchomienia.log` będzie istniał. Zmodyfikuj program tak, aby w przypadku, gdy `uruchomienia.log` nie istnieje, program zamiast wypisywać uruchomienia wraz z datami, napisał 'Brak historii uruchomień', a następnie kontytuował pracę.

### Rozszerzenie 2:
- Uporządkuj program (czyli zrób "refactor") wydzielając obecny kod do dwóch funkcji: `wypisanie_historii()` oraz `zapisanie_uruchomienia()`.
- Wywołaj obie funkcje wewnątrz bloku `if __name__ == '__main__':` dzięki czemu będzie można w przyszłości zaimportować funkcje bez uruchamiania ich.

### Rozszerzenie 3:
Zadbaj o to, aby używane pliki zostały zamknięte przez program. Użyj do tego menadżera kontekstu, czyli składni: `with open(nazwa_pliku, mode=tryb) as plik`. Wprowadź modyfikacje do obu funkcji.