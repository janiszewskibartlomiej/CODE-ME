# Zadanie 03:
Napisz skrypt, który wygeneruje losowe, ośmioznakowe hasło.

- Wiedząc, że w module `string` są stałe, które przechowują ciągi znaków, zaimportuj z tego modułu jeden z takich ciągów (może być to ten z samymi małymi literami).
- Zaimportuj z modułu `random` funkcję, która wybierze losowo element z listy.
- Wybierz kolejno osiem losowych znaków i sklej z nich hasło, a następnie wypisz je na ekranie.

Pamiętaj, że mając listę liter, możesz je skleić w jednego stringa używając metody `join()`. Przykładowo: `''.join(lista_znakow)`

## Rozszerzenie a:
Rozszerz zbiór znaków, z których można losować znaki do hasła o cyfry.

## Rozszerzenie b:
Zamknij kod generujący w funkcję `generuj_haslo`, która będzie przyjmować jeden argument: ilość znaków w generowanym haśle. Ten argument domyślnie ma być ustawiony na 8.
- Funkcja nie ma wypisywać hasła na ekran ale zwracać je.
- Wygeneruj hasło składające się z 10 znaków, zapisz wynik wywołanej funkcji do zmiennej i wypisz go na ekranie.

## Rozszerzenie c:
Dodaj do funkcji `generuj_haslo` opcjonalny parametr `trudnosc`, domyślnie ustawiony na `0`.
- Wartość `0` będzie losować hasło z małych liter, wartość `1` oznacza losowanie z małych i wielkich, `2`: małe, wielkie i cyfry, itd.
