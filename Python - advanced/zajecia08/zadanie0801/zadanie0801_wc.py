from zadanie08_funkcje import policz_linie, policz_wyrazy, policz_bajty
import log, time, datetime

start = datetime.datetime.now()

format = '%(asctime)s, %(levelname)s, %(message)s'

datefmt = '%d-%m-%Y %H:%M:%S'


log.basicConfig(level=log.DEBUG, format=format, datefmt=datefmt)
nazwa_pliku = 'zen.txt'

try:
    with open(nazwa_pliku) as f:
        zawartosc = f.read()

except FileNotFoundError:
    exit()

szablony = {'pelny': '{linie} {wyrazy} {bajty} {nazwa_pliku}',
            'linie': '{linie} {nazwa_pliku}'}

szablon = szablony['pelny']

wynik_pelny = szablon.format(linie=policz_linie(zawartosc),
                             wyrazy=policz_wyrazy(zawartosc),
                             bajty=policz_bajty(zawartosc),
                             nazwa_pliku=nazwa_pliku)

print(wynik_pelny)
