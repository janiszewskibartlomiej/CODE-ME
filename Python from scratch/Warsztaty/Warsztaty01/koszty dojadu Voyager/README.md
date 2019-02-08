I. Program do obliczania **kosztów przejazdów** samochodem Chrysler Town & Country 4.0L 2008-2010 z instalacją LPG na podstawie wprowadzonej liczby przejechanych klilometrów
(wymagania: Python 3.7)

II. Uruchomienie za pomocą pliku: koszt_dojazdu._cena_z_klawiatury_Wer2.py

III. Opis szczegółowy programu:
* Program zakłada nastepujące wartości spalania (podane przez użytkownika):
    * Spalanie na trasie: 17l/100km
    * Spalanie w mieście: 20l/100km
    * Spalanie średnie jest wyliczane na podstawie parametrów a) oraz b)
 
* Po uruchomieniu program prosi o wprowadzenie liczby całkowitej przejechanych klimotrów, w celu określenia kosztu przejazdu
* Następnie program prosi o wprowadzenie aktualnej ceny LPG jako wartość dziesiętną
* W przypadku wprowadzenia nie prawidłowych danych (np. tekst, inne znaki) program poinformuje użytkownika że wprowadził nie poprawne dane, a następnie program ponownie poprosi o wprowadzenie poprawnej wartości [aż do skutku].
* Program zwraca wyliczenie kosztów przejazdu w oparciu o spalanie w mieście, na trasie oraz uśrednione.