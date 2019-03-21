from datetime import datetime

poczatek = datetime.now()

input('Naciśnij ENTER')

pierwszy_stop = datetime.now()
pierwsza_roznica = pierwszy_stop - poczatek

print(f'Naciśnięto ENTER po {pierwsza_roznica} sekundach.')

input('Naciśnij ENTER')

drugi_stop = datetime.now()
druga_roznica = drugi_stop - pierwszy_stop

print(f'Naciśnięto ENTER po {druga_roznica} sekundach.')

if pierwsza_roznica < druga_roznica:
    print('Za pierwszym razem naciśnięto szybciej!')
else:
    print('Za drugim razem naciśnięto szybciej!')