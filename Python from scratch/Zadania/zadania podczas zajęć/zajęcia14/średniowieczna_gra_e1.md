# Zadanie - średniowieczna gra strategiczna

## Etap 1
Stwórz klasę `Rycerz` o następujących charakterystykach:
- Klasa posiada dwa atrybuty:
    - `zycie` ustawione przy inicjalizacji na 60
    - `doswiadczenie` ustawione przy inicjalizacji na 0
- Klasa posiada zaimplementowaną metodę `__repr__`, która zwróci tekst: 'Rycerz: hp=(zycie), exp=(doswiadczenie)'
- Klasa posiada metodę `maszeruj`, która:
    - przyjmuje jeden argument: `dystans` (dystans w metrach, który przebył Rycerz)
    - wypisze na ekran komunikat 'Rycerz: Przeszedłem (ilość)m'
    - Rycerz za każdy metr, który przeszedł, dostaje 0.2 punkta doświadczenia. Metoda ma dodać do doświadczenia rycerza odpowiednią ilość punktów.
- Klasa posiada metodę `atakuj`, która:
    - wypisze na ekran komunikat: 'Rycerz: Machnąłem mieczem!'
    - doda Rycerzowi 0.3 punktu doświadczenia za jego ruch

Przetestuj napisany kod:
- Napisz blok `if __name__ == '__main__':` i kolejne wyrażenia pisz w jego wnętrzu
- Stwórz obiekt klasy Rycerz i wydrukuj do na ekran
- Wydaj rozkaz maszerowania a następnie ataku
- Ponownie wydrukuj Rycerza na ekran

