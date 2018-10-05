# Zadanie "Sklep" - etap 3:

W tym zadaniu nasz sklep zwiększa asortyment.

Do pliku `sklep.py` dodaj drugą listę:
```
warzywa_i_owoce = [
    {'nazwa': 'jabłko', 'cena': 2.49, 'czy_na_sztuki': False},
    {'nazwa': 'kiwi', 'cena': 23.90, 'czy_na_sztuki': False},
    {'nazwa': 'figa', 'cena': 3.49, 'czy_na_sztuki': True},
    {'nazwa': 'pomidor', 'cena': 7.49, 'czy_na_sztuki': False},
    {'nazwa': 'arbuz', 'cena': 3.99, 'czy_na_sztuki': False},
    {'nazwa': 'cytryna', 'cena': 6.99, 'czy_na_sztuki': False},
    {'nazwa': 'awokado', 'cena': 4.99, 'czy_na_sztuki': True}
]
```

Zauważ, że nasze funkcje skonstruowane są tak, że mają "na sztywno" wpisane korzystanie z listy `slodycze`. Aby móc skorzystać wedle uznania z jednej lub drugiej listy wprowadź następujące modyfikacje:

- W pliku `zadanie_sklep.py` zmodyfikuj wszystkie funkcje tak, aby otrzymywały jeszcze jeden dodatkowy argument `lista_artykulow`.
- Wewnątrz każdej z funkcji zmień wpisaną na sztywno listę `slodycze` na `lista_artykulow`.
- Zmodyfikuj wywołania tych funkcji tak, aby każda z nich była wywołana z nowym argumentem `slodycze`. W rezultacie, cały program powinien działać jak poprzednio.

Na końcu pliku `zadanie_sklep.py` wywołaj funkcję `wypisz_artykuły` i przekaż jej listę `warzywa_i_owoce`. Pamiętaj, żeby wcześniej zaimportować tę listę do pliku `zadanie_sklep.py`.