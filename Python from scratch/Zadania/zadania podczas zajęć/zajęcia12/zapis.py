from datetime import datetime

plik = open('uruchomienia.log', 'a')

teraz = datetime.now()

uruchomienie = 'Skrypt został uruchomiany: {}\n'.format(teraz)
print(uruchomienie)

plik.write(uruchomienie)
