# Zadanie domowe 08

## Wstęp
Na podstawie pliku `wc.py` stwórz plik `zaddom08.py`, do którego będzie można przekazywać parametry z linii poleceń.
Większość logiki programu `wc.py` znajduje się w pliku `wc_funkcje.py`, którego **nie wolno modyfikować**.

# Etap 1
W tym etapie umożliwimy użytkownikowi ustawianie poziomu logowania z linii poleceń. Przykładowo, uruchomienie programu poleceniem `python zaddom08.py --loglevel DEBUG` powinno ustawić poziom logowania na `logging.DEBUG`.

Dodaj opcjonalny parametr `--loglevel`, który:
- będzie przyjmował dokładnie jeden argument z linii poleceń
- będzie miał odpowiadającą mu krótką wersję `-l`
- będzie miał opis informujący o swoim działaniu
- w przypadku uruchomienia programu bez tego parametru, program ma ustawić poziom logowania na `logging.WARNING`. (Aby uzyskać to działanie, dodając parametr skorzystaj z argumentu `default`)

Gdy upewnisz się, że powyższe kroki są spełnione:
- Zmodyfikuj argument `--loglevel` tak, aby dało się podać tylko argument spośród obsługiwanych opcji (Wszystkie wbudowane poziomy logowania można znaleźć pod `logging._nameToLevel`).

# Etap 2
W tym etapie umożliwimy użytkownikowi podać plik, którego zawartość ma być przeanalizowana. Przykładowo, uruchomienie programu poleceniem `python zaddom08 zen.txt` powinno uruchomić program z poziomem logowania `logging.WARNING` i przeanalizować plik o nazwie `zen.txt`.

- Dodaj parametr pozycyjny `plik`.
- Podanie parametru powinno być wymagane do działania programu. 
- Parametr ten ma mieć opis informujący o jego działaniu.

# Etap 3 (dla chętnych)
UNIXowy program `wc` ma również kilka innych flag, takich jak:
- `-ln`, która powoduje, że wypisana jest tylko liczba linii (oryginalnie jest `-l`, u nas jest zmienione z powodu konflinktu nazw)
- `-w`, która powoduje, że wypisana jest tylko liczba słów
- `-c`, która powoduje, że wypisana jest tylko liczba bajtów


Dodaj powyższe argumenty opcjonalne pamiętając, że w naszym programie (w przeciwieństwie do oryginału) argumenty te wykluczają się wzajemnie.
- Powyższe parametry nie przyjmują dalszego argumentu, wystarczy tylko myślnik i litera/litery.
- Aby użyć flag `-w` oraz `-c` należy zmodyfikować funkcję `wc()` z pliku `wc_funkcje.py`. Na ten moment zaimplementowany jest tylko szablon `pelny` oraz `linie`.
- Przykładowe polecenie używające jednego z powyższych parametrów: `python zaddom8.py -w zen.txt`
Podpowiedź: https://stackoverflow.com/questions/11154946/require-either-of-two-arguments-using-argparse
 
