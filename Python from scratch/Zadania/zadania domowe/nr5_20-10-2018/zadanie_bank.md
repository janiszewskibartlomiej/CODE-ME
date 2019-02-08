# Zadanie - bank
Do treści zadania dołączony jest plik `bank.py`. Tego pliku **nie wolno** modyfikować. Twoim zadaniem jest napisać nowy plik `konta.py`, dzięki któremu uruchomiony skrypt `bank.py` wypisze na ekran poniższe linie:

```
Wpłacono 3700PLN
Konto(saldo:3700PLN)
Wypłacono 2000PLN
Konto(saldo:1700PLN)
Brak środków na koncie!

Wpłacono 4500PLN
Konto(saldo:4500PLN)
Odsetki po 30 dniach wynoszą 5.55PLN
Konto(saldo:4505.55PLN)
```

### Szczegółowa treść zadania:
- plik `konta.py` ma zawierać dwie klasy.
- klasa `Konto`:
    - ma posiadać dwa atrybuty:
        - `saldo` - zainicjalizowane na wartosć `0`
        - `waluta` - zainicjalizowane na wartość `'PLN'`
    - ma posiadać metodę `__repr__`, która opisze konto tak jak w przykładzie powyżej.
    - ma posiadać metodę `wplata`, która przyjmuje jeden argument: `kwota`.
        - metoda dopisuje kwotę do salda
        - metoda wypisuje komunikat zgodny z tym, w przykładzie.
    - ma posiadać metodę `wypłata`, która przyjmuje jeden argument: `kwota`.
        - jeśli na koncie jest wystarczająca ilość środków, metoda odejmuje kwotę od salda
        - jeśli środki są niewystarczające, metoda nie odejmie nic z salda.
        - w obu przypadkach metoda wypisuje komunikat zgodny z tym, w przykładzie.
- klasa `KontoOszczednosciowe`:
    - dziedziczy po klasie `Konto`
    - posiada jeden dodatkowy atrybut w stosunku do klasy nadrzędnej: `oprocentowanie`.
        - atrybut `oprocentowanie` jest przekazywany przez użytkownika podczas tworzenia obiektu tej klasy
        - `oprocentowanie` jest liczbą zmiennoprzecinkową wyrażającą oprocentowanie w skali roku (np. 1.5)
    - posiada jedną dodatkową metodę: `dolicz_odsetki`
        - metoda przyjmuje jeden argument `dni`
        - metoda oblicza oprocentowanie i dodaje je do salda
        - w zadaniu zakładamy, że rok zawsze ma 365 dni
        - oprocentowanie zaokrąglane jest do dwóch miejsc po przecinku
        - metoda wypisuje komunikat zgodny z tym, w przykładzie.


### Rozszerzenie:
Wypłacanie pieniędzy w koncie oszczędnościowym zwykle jest dodatkowo płatne. Zmodyfikuj klasę `KontoOszczednosciowe` tak, aby pierwsza wypłata była bezpłatna, a każda kolejna kosztowała 5PLN.