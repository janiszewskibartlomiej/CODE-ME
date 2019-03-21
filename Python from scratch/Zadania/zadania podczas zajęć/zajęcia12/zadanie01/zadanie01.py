from datetime import datetime

plik = open('uruchomienia.log', 'r')

zawartosc = plik.read()

print('Uruchomienia do tej pory: ')
print(zawartosc)


plik = open('uruchomienia.log', 'a')

teraz = datetime.now()

uruchomienie = 'Skrypt został uruchomiony: {}\n'.format(teraz)
print(uruchomienie)

plik.write(uruchomienie)
