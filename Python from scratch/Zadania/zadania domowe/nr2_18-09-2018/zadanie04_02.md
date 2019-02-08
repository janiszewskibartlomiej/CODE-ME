# Zadanie 02:
Napisz program, który:

- Będzie miał zadeklarowany string (może być w potrójnych cudzysłowach) zawierający prawdziwy, długi tekst. Przykład: wierszyk dla dzieci, lub tekst krótkiego artykułu.

- Program wykona na tym tekscie kolejno, następujące operacje:
  1. Zamieni wszystkie znaki w tekście na małe litery.
  2. Stworzy z tak przygotowanego tekstu listę zawierającą występujące w tekście wyrazy, w kolejności pojawiania się.
  3. Wypisze ilość wyrazów w tekscie.
  4. Posortuje wyrazy alfabetycznie od najmniejszego do największego. (Uwaga! Jest metoda obiektu `list`, która to robi dokładnie to. Znajdziesz ją w dokumentacji.)
  5. Stworzy z listy posortowanych wyrazów jednego stringa, w którym wszystkie wyrazy są wypisane po kolei i oddzielone przecinkiem. Wypisze tego stringa na ekran.
  6. Mając listę posortowanych wyrazów, wypisze trzy pierwsze i trzy ostatnie.

## Rozszerzenie (trudniejsze):
W prawdziwych tekstach, oprócz liter, znajdziemy również kropki, przecinki i inne znaki, które utrudnią nam powyższą analizę wyrazów w tekście. Dopisz do programu kod, który usunie z tekstu występujące w nim znaki, które nie są tekstem.