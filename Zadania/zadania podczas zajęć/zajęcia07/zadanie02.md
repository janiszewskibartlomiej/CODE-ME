# Zadanie 02
Napisz program, który poprosi o wpisanie liczby całkowitej, a następnie wczyta dane z klawiatury. Tym razem chcemy się zabezpieczyć przed niepoprawnymi danymi.
- Jeśli uda się z wczytanych znaków utworzyć liczbę, należy ją zapisać do zmiennej a następnie wyświetlić komunikat:
> "Wpisana liczba to (liczba)"
- Jeśli użytkownik wpisał coś innego niż liczba całkowita, program ma wypisać komunikat:
> "(wpisany tekst) to nie jest liczba całkowita" i zakończyć pracę. (Można użyć funkcji `exit()`)

# Rozszerzenie (a):
- Zmodyfikuj program tak, aby pytał się o liczbę całkowitą tak długo, aż ją otrzyma, lub użytkownik nie przerwie działania programu z zewnątrz.

# Rozszerzenie (b):
- Stwórz funkcję `wczytaj_liczbe()`, która będzie zwracać wczytaną z klawiatury liczbę. Funkcja ma, tak jak rozszerzenie a, prosić o liczbę tak długo, aż ją otrzyma.
- Wykorzystaj tę funkcję do tego, by wczytać z klawiatury dwie liczby, zapisać je do dwóch zmiennych i wyświetlić na ekranie ich sumę.

# Rozszerzenie (c):
- Zmodyfikuj funkcję tak, aby można było przekazać jej opcjonalnie parametr `nr`, który zmieni zaptanie na:
> "Proszę podać liczbę całkowitą numer (nr)".
- Używając pętli `for` zmodyfikuj program tak, aby wczytał pięć liczb z klawiatury, obliczył ich sumę i wyświetlił ją na ekran.