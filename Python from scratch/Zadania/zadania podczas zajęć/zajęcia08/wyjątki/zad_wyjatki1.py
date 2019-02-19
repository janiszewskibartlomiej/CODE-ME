print('Program oblicza wynik dzielienia liczby 5150 przez liczbę podaną przez użytkownika!')
z_klawiatury = input('Proszę wpisać dowolną liczbę: ')

try:
    liczba = float(z_klawiatury)
    wynik = 5150 / liczba
    print(f'5150 / {liczba} = {wynik}')
except ValueError:
    print('Wprowadzona wartość jest nieprawidłowa!')
except ZeroDivisionError:
    print('Próba dzielenia przez zero!')

print('Dziękuję za skorzystanie z programu :)')