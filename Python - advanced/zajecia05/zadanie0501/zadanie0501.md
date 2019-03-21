# Zadanie 05 - 01

Napisz aplikację internetową, która będzie zapisywać do pliku i odczytywać z niego jedną informację tekstową. Jako szablonu użyj pliku `zadanie0501.py`.

Aplikacja ma spełniać poniższe wymogi:
1. Aplikacja ma obsługiwać ścieżkę `/zapis/dane`, gdzie `dane` oznaczają dowolny ciąg znaków, który ma zostać zapisany.
    - dane mają być zapisane do pliku `baza.txt`
    - w przypadku poprawnego zapisania danych do pliku, na ekranie ma pojawić się komunikat: `Zapisano do bazy dane: "zapisane_dane"` 
2. Aplikacja ma obsługiwać ścieżkę `/odczyt`, pod którą:
    - jeśli plik `baza.txt` istnieje, wypisze na ekran komunikat: `Dane w bazie to: "zapisane_dane"` 
    - jeśli plik `baza.txt` nie istnieje, wypisze na ekran komunikat: `Najpierw zapisz coś do bazy!` 