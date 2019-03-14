# Zadanie 04 - 01

Otwórz plik `zadanie0401.py`. Jest to prosty skrypt, który odczytuje listę z pliku `dane.json`, dopisuje do niej słownik z danymi klienta, a następnie zapisuje zmodyfikowaną listę z powrotem do tego samego pliku.

W tym zadaniu nie ma potrzeby modyfikowania funkcji `odczytaj_json()` oraz `zapisz_json()`.

## Etap 1

Napisz context manager `Dane`, który:
- w metodzie `__enter__()` wczyta listę z pliku `dane.json` i zwróci ją jako obiekt.
- będzie posiadał metodę `__exit__()` ale nie będzie ona nic robiła.

Zmodyfikuj kod skryptu w bloku `if-main` tak, aby korzystał z context managera `Dane`, ale nie używał funkcji `odczytaj_json()`. zmodyfikowaną listę nadal należy zapisywać przy użyciu funkcji `zapisz_json()`.

## Etap 2

Zmodyfikuj context manager `Dane` tak, aby:
- w metodzie `__enter__()` dane z pliku zapisane były najpierw do atrybutu `self._dane` a następnie ten atrybut był zwrócony.
- w metodzie `__exit__()` wywołana ma być funkcja `zapisz_json()`, która zapisze do pliku aktualną zawartość obiektu `self._dane`.

Jeśli twój context manager działa poprawnie, możesz usunąć z bloku `if-main` użycie funkcji `zapisz_json()`
 
