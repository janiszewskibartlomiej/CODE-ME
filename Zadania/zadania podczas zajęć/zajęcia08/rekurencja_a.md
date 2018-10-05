# Zadanie: "Drukowanie listy"

## Etap 1:

Program będzie pracował na wielokrotnie zadnieżdżonej liście (lista list, które same mogą posiadać listy). Użyj listy poniżej.

```
przyklad = [1, [2, 3], [4, 5, [6, 7, 8], 9], 10, 11, [12], 13]
```

- Napisz funkcję `wypisz_elementy_listy`, która będzie przyjmowała jeden argument: listę, której elementy trzeba wypisać.
- Wywołaj funkcję `wypisz_elementy_listy` dla listy `przyklad`.
- Każdy element wypisywanej listy, ma być wypisany w oddzielnym wierszu: "element: (wartość)". Dla listy powyżej, program ma zwracać:

```
element: 1
element: [2, 3]
element: [4, 5, [6, 7, 8], 9]
...i tak dalej...
```

## Etap 2:
Zmodyfikuj program powyżej tak, aby, gdy elemenem wypisywanej listy jest inna lista funkcja pisała komunikat "lista: (wartość)", a w przeciwnym wypadku, tak jak poprzednio: "element: (wartość)".

```
element: 1
lista: [2, 3]
lista: [4, 5, [6, 7, 8], 9]
...i tak dalej...
```
- Aby sprawdzić, czy sprawdzany właśnie element `el` jest typu `list` użyj funkcji `isinstance(el, list)`.


### obsługa pustych list: pusta lista jest elementem który trzeba wypisać