with open('dane.txt', 'r') as plik:
    wszystkie_linie = plik.readlines()
    print(wszystkie_linie)
    print('zamknięty?', plik.closed)

print('zamknięty?', plik.closed)

plik.read()  # po zamknięciu pliku nie mamy już do niego dostępu
