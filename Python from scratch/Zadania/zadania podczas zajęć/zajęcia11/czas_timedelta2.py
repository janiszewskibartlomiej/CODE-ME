from datetime import datetime

poczatek = datetime.now()

input('Naciśnij ENTER')

pierwszy_stop = datetime.now()
pierwsza_roznica = pierwszy_stop - poczatek

print(f'Naciśnięto ENTER po {pierwsza_roznica} sekundach.')
