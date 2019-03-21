# Zadanie - średniowieczna gra strategiczna

## Etap 2
Stwórz klasę `Lucznik` kopiując klasę `Rycerz` i wklejając ją poniżej. Następnie wprowadz w skopiowanej klasie następujące modyfikacje:
- Łucznik zaczyna z mniejszą ilością punktów życia: 40 zamiast 60.
- We wszystkich komunikatach zamiast 'Rycerz' wpisz 'Łucznik'.
- Metoda `atakuj` ma wypisywać komunikat 'Łucznik: Wypuściłem strzałę!' a wypuszczenie strzały ma dodawać Łucznikowi 0.4 punktu doświadczenia.

Przetestuj działanie tej klasy podobnie, jak to miało miejsce przy klasie `Rycerz`.

## Rozszerzenie (opcjonalne):
Łucznik ma ograniczoną ilość strzał w kołczanie. Dodaj do klasy odpowiedni atrybut a następnie zmodyfikuj funkcję `atakuj` tak, aby Łucznik z każdym strzałem tracił jedną strzałę. Gdy strzały się skończą, uniemożliw strzelanie i zmień komunikat.