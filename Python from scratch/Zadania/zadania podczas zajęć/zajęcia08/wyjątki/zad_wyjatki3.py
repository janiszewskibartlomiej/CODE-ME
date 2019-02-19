print('Program oblicza wynik dzielienia liczby 5150 przez liczbę podaną przez użytkownika!')
z_klawiatury = input('Proszę wpisać dowolną liczbę: ')

try:
    liczba = float(z_klawiatury)
    wynik = 5150 / liczba
except ValueError:
    print('Wprowadzona wartość jest nieprawidłowa!')
except ZeroDivisionError:
    print('Próba dzielenia przez zero!')
else:  # Ten blok będzie wykonany, gdy żaden wyjątek się nie pojawi
    print(f'5150 / {liczba} = {wynik}')
finally:  # To zostanie wykonane ZAWSZE!
    print('Dziękuję za skorzystanie z programu :)')