# Zadanie 09 - 01

W tym zadaniu stwórz plik `0901_create.py`, który stworzy bazę danych, w której znajdować się będzie tabela z danymi zwierzaków z bajek animowanych.

## Skrypt ma realizować poniższe zadania:
- W wyniu uruchomienia skryptu stworzony ma zostać plik 
`zadanie09_baza.db`, w którym przechowywana będzie baza danych.
    - Na ten moment nie obsługujemy sytuacji, w której baza już istnieje 

- Skrypt ma stworzyć tabelę `zwierzaki` w bazie danych. 
    - Tabela ma posiadać kolumnę `id`, która nie może być pusta, ma być unikalnym kluczem własnym i ma być autoinkrementowana.  
    - Pozostałe kolumny mają odpowiadać danym w pliku `zwierzaki.csv`.
    - Kolumna `imie` nie może być pusta.
    - Dane te zostaną dodane do bazy w późniejszym etapie.