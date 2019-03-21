# Zadanie 05 - 02

Zmodyfikuj rozwiązanie zadania 05 - 01. Samo działanie aplikacji ma być takie samo, natomiast różnić mają się ścieżki (endpointy). Rozwiązanie zapisz w pliku `zadanie0502.py`.

1. W celu zapisania danych należy wysłać zapytanie na endpoint `/zapis` zamiast tak jak poprzednio `/zapis/dane`.
2. Dane mają być teraz przekazywane za pomocą "query stringa", pod parametrem `dane`.
3. W przypadku wysłania zapytania na ścieżkę `/zapis` (bez query parametru `dane`) aplikacja ma wypisać na ekran `Brak danych do zapisu` i pozostawić plik `baza.txt` bez zmian.

Przykładowo: ścieżka `/zapis/przyklad` ma teraz być odpowiadać ścieżce `/zapis?dane=przyklad`

  