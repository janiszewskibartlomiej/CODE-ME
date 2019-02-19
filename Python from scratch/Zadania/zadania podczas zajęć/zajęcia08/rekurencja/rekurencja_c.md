# Zadanie: "Drukowanie listy"

## Etap 4:
Aby zasugerować użytkownikowi, które z wypisanych elementów są zadnieżdżone (i jak głęboko).
- Jeśli wypisujemy elementy zagnieżdżonej listy, komunikaty powinny być lekko przesunięte w prawo (możesz użyć znaku specjalnego '\t').
- Aby uzyskać ten efekt, dodaj do funkcji argument domyślny: `poziom` ustawiony na 0. Argument ten będzie sterował tym, o ile "poziomów" bardziej będzie wcięty komunikat.

Dla przykładowej listy, program powinien wypisać:
```
element: 1
	element: 2
	element: 3
	element: 4
	element: 5
		element: 6
		element: 7
```

## Rozszerzenie:
- Elementy sąsiadujących list (np. `[2, 3]` oraz `[4, 5]`) w naszym programie wyglądają jakby były w jednej dużej liście (np. `[2, 3, 4, 5]`). Oddziel graficznie elementy tak, aby było wiadomo, że należą one do różnych list.