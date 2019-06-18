# Zadanie 01
Popraw aplikację dodając poniższe usprawnienia:

- Gdy użytkownik wpisze błędne dane, zamiast wyświetlenia tekstu "błąd!" przekieruj użytkownika ponownie do formularza logowania (wyświetlenie informacji o błędzie będzie dodane później)
- Gdy użytkownik poda poprawną nazwę użytkownika i hasło, powinien zostać przekierowany na stronę główną: `/`.
- W tym momencie, niezależnie od tego czy użytkownik jest zalogowany, czy też nie, może on zobaczyć zawartość strony głównej. Zmodyfikuj ten endpoint tak, aby zalogowany użytkownik pozostał na tej stronie, a niezalogowany był przekierowywany na stronę logowania. Wykorzystaj do tego stan obiektu pod zmienną `session`.
