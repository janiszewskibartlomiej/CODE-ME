# Zadanie 10

Muzycy zespołu The Beatles byli utalentowanymi multiinstrumentalistami. W tym zadaniu uzupełnimy istniejącą bazę danych o informacje o instrumentach opanowanych przez każdego beatlesa.

## Etap 1: tabela "instrumenty"

Uzupełnij skrypt `02_instrumenty.sql` tak, aby znajdowały się w nim dwa zapytania:

- Pierwsze zapytanie ma stworzyć tabelę, w której będą następujące kolumny:
    - `id`, która będzie kluczem głównym (już gotowe, nie trzeba modyfikować)
    - `id_muzyka`, która będzie kluczem obcym, powiązanym z kolumną `id` tabeli `beatles`
    - `nazwa`, która będzie przechowywać nazwę instrumentu
    
- Drugie zapytanie wypełni tabelę `instrumenty` danymi zgodnymi z poniższą wiedzą:
    - John Lennon gra na: 'wokal', 'gitara', 'pianino', 'harmonijka ustna'
    - Paul McCartney gra na: 'wokal', 'bas', 'gitara', 'pianino'
    - George Harrison gra na: 'gitara', 'wokal', 'sitar', 'pianino'
    - Ringo Starr gra na: 'perkusja', 'wokal'
    
## Etap 2: skrypt "zadanie10.py"   

Napisz zapytanie, które dla podanego imienia muzyka zwróci instrumenty, na których gra.
