import time

with open('dane.txt', 'r') as plik:
    wszystkie_linie = plik.readlines()
    print(wszystkie_linie)

    print('zamknięty?', plik.closed)
    time.sleep(20)

print('zamknięty?', plik.closed)
time.sleep(20)
print('Skryp zakończył działanie')