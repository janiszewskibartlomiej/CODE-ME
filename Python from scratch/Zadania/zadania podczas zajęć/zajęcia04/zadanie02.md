# Zadanie 02

Napisz program, który:
1. Będzie wczytywał z klawiatury wyraz lub tekst.
2. Będzie powtarzał wczytywanie, aż do momentu, w którym użytkownik nie poda pustego stringa.
3. Jeśli użytkownik podał pusty string, przerwij wczytywanie i zakończ program.
4. Jeśli użytkownik wpisał coś innego, niż pusty string, sprawdź, czy we wpisanym tekście pojawia się spacja. Jeśli spacja występuje, wyświetl napis:
> 'Znaleziono spację, wpisz wyraz ponownie.'
i ponownie wczytaj tekst (wróć do pkt 1.)
5. Jeśli użytkownik wpisał wyraz bez spacji, oblicz długość tego wyrazu i wyświetl komunikat:
> 'Wpisany wyraz ma długość (tutaj obliczona wartość) znaków.'
i ponownie wczytaj tekst (wróć do pkt 1.)

Podpowiedzi:
- Cały program powinien być umieszczony w jednej nieskończonej pętli `while True`
- Aby wyjść z pętli używamy `break`, aby zakończyć to powtórzenie używamy `continue`
- Aby wykryć pusty string można porównać go z '' lub użyć faktu, że pusty string ma wartość False.
- Aby sprawdzić, czy znak lub tekst jest częścią większego tekstu, można użyć operatora `in` np. `'s' in 'tekst'`

Rozszerzenie:
- Jeśli użytkownik wpisał spacje przed lub po wyrazie, zignoruj je. Jest specjalna metoda obiektu string, która to umożliwia. Znajdź ją w dokumentacji.