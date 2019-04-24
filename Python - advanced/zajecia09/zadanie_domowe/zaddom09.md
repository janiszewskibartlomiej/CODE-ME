# Zadanie domowe 08

## Wprowadzenie
Zadanie przedstawia prosty symulator plecaka harcerza. Plik `zaddom09_db_init.py` tworzy bazę danych i zapełnia ją przykładowymi danymi. Skrypt sql wykonywany przez ten plik jest umieszczony w pliku `db_init.sql`.

Zwróć uwagę na definicję kolumny `rodzaj`, która dopuszcza tylko dwie wartości: `sprzet` albo `jedzenie`.

Plik `zaddom09_db_init.py` nie powinien być modyfikowany.

## Etap 1 - dodawanie przedmiotów do plecaka
Uzupełnij plik `zaddom09_dodaj.py` tak, aby po udzieleniu odpowiedzi na cztery pytania, został dodany do bazy opisany przedmiot.

#### Dla chętnych:
Skrypt powinien być odporny na błędne dane podane przez użytkownika. Należy uniemożliwić użytkownikowi wpisanie tekstu gdy prosimy o liczbę a także wymusić wpisanie poprawnego rodzaju sprzętu.

Rodzaj dodawanego sprzętu powinien być wybierany przez podanie całego wyrazu lub tylko pierwszej litery (wielkiej lub małej).

## Etap 2 - wypisanie zawartości plecaka
Uzupełnij plik `zaddom09_info.py` tak, aby po uruchomieniu go, na ekran wypisana została:
- lista sprzętów w kolejności alfabetycznej
- prowiant w kolejności alfabetycznej
- zsumowana waga wszystkich przedmiotów w plecaku

Poniżej przykładowy ekran, po uruchomieniu skryptu z niezmodyfikowanymi danymi w bazie danych:
```
Sprzęt:
Latarka czołowa
Skarpety
Szczoteczka do zębów

Jedzenie:
Wafelek czekoladowy

Waga zawartości: 1.4400000000000002g
```
