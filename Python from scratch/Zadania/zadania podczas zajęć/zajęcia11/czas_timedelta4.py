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

o_ile_szybciej = pierwsza_roznica - druga_roznica
if pierwsza_roznica < druga_roznica:
    print(f'Za pierwszym razem naciśnięto szybciej o {-o_ile_szybciej}!')
else:
    print(f'Za drugim razem naciśnięto szybciej o {o_ile_szybciej}!')