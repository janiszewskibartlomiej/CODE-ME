# Zadanie 01:
Napisz program, który będzie wczytywał wyrazy z klawiatury.
Po wczytaniu wyrazu, program wypisze na ekran komunikat (dla wpisanego wyrazu 'Fender'):

> Wyraz "Fender" ma 6 znaków.
> Wyraz ten zaczyna się na literę "F".

- Skonstruuj komunikat przed wypisaniem go na ekran używając metody `.format()` i zapisz go do zmiennej.
- Zwróć uwagę na to, że komunikat mieści się w dwóch liniach. Aby uzyskać nową linię, użyj znaku specjalnego `\n`.
- Wypisz gotowy komunikat na ekran.
- Program ma skończyć pracę gdy użytkownik przerwie go z zewnątrz (ctrl+c w konsoli) lub "stop" w PyCharmie.

# Rozszerzenie:
- Gdy powyższy program będzie już poprawnie działał, dopisz kod sprawdzający, czy we wprowadzonym wyrazie pojawiła się spacja. Jeśli tak, zignoruj wpisany wyraz i ponownie poproś o wpisanie nowego.

# Rozszerzenie (dla chętnych):
- Dopuść wpisanie wielu wyrazów za jednym razem, np. "Fender Gibson Ibanez". Wyrazy muszą być oddzielone spacją, więc usuń poprzednie rozszerzenie.
- Program ma nadal działać gdy użytkownik wprowadzi jeden wyraz