# Zadanie 01 "Logowanie czasu uruchomienia"

## Etap 1 - zapis
Stwórz plik `zapis.py`, który będzie logował swoje uruchomienia do pliku tekstowego.
- Po uruchomieniu skryptu, na ekranie ma zostać wyświetlony komunikat:
> Skrypt został uruchomiony: 2018-10-08 19:58:47.863648
- Ten sam komunikat ma zostać zapisany do pliku `uruchomienia.log`.
- Z każdym uruchomieniem plik `uruchomienia.log` ma powiększać się o jedną linię. (Podpowiedź: tryb, który tak się zachowuje to "append", czyli `'a'`)

## Etap 2 - odczyt
Stwórz plik `odczyt.py`, który będzie odczytywał dane zapisane w pliku `uruchomienia.log` i wypisywał je na ekranie.
- Przed wypisaniem linii odczytanych z pliku skrypt ma wypisać komunikat:
> Uruchomienia do tej pory:
