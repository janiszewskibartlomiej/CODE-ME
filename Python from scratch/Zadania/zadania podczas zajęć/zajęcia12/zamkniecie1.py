import time

plik = open('dane.txt', 'r')

print('długie oblicznia...')
time.sleep(30)

print('zamykam plik!')
plik.close()
time.sleep(30)

print('koniec obliczeń!')
