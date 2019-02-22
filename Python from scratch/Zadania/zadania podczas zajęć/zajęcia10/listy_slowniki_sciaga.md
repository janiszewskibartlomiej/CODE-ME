# Podstawowe operacje na słowniku:

- Stworzenie słownika `sl`:

`sl = { 'kl1': 'wart1', 'kl2': 'wart2'}`

- Wyciągnięcie wartości pod kluczem `kl1` ze słownika `sl` i zapisanie jej do zmiennej `pobrana`:

`pobrana = sl['kl1']`

- Zapisanie nowego stringa `'wart3'` pod istniejącym kluczem `kl2` w słowniku `sl`:

`sl['kl2'] = 'wart3'`

- Stworzenie nowego klucza `kl3` w słowniku `sl` i zapisanie pod nim stringa `'wart4'`:

`sl['kl3'] = 'wart4'`

- Usunięcie klucza `kl1` ze słownika `sl` (automatycznie usunięta zostanie wartość):

`del sl['kl1']` lub `sl.pop('kl1')`

# Podstawowe operacje na liście:

- Stworzenie listy `lt`:

`lt = ['el1', 'el2', 'el3']`

- Wyciągnięcie wartości pod indeksem 0 z listy `lt` i zapisanie jej do zmiennej `pobrana`:

`pobrana = lt[0]`

- Dodanie nowego elementu, stringa `'el4'`, na koniec listy `lt`:

`lt.append('el4')`

- Zmiana elementu istniejącego pod indeksem 1 na element, string `'el5'`:

`lt[1] = 'el5'`

- Usunięcie elementu pod indeksem 2 z listy `lt`:

`del lt[2]` lub `lt.pop(2)`
