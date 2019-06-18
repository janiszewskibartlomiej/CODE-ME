# Zadanie 01

Zmodyfikuj aplikację tak aby:

### Modyfikacja 1
Gdy nie jest podana waga przedmiotu, w tabelce była wartość '-' (myślnik), zamiast 'Nonekg'
- Powyższe zmiany należy wprowadzić w szablonie. 

### Modyfikacja 2
Pod tabelką umieść informację o sumarycznej wadze wszystkich przedmiotów w plecaku. Weź pod uwagę nie tylko wagę przedmiotu, ale też ich ilość w plecaku :)
- nie wykonuj dodatkowego zapytania do bazy.
- oblicznie sumy wykonaj po stronie kodu pythonowego (nie w szablonie)
- mając jeden rekord ('przedmiot'), możesz się dostać do jego pól jak do wartości w słowniku: `przedmiot['nazwa_pola']`
- podczas sumowania zignoruj przedmioty, które nie mają ustawionej wagi
