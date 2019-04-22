# Bartłomiej Janiszewski
from wc_funkcje import ustaw_logger, wc
import logging
import datetime
import argparse

if __name__ == '__main__':
    start = datetime.datetime.now()

    parser = argparse.ArgumentParser(description='Prosty program do logów.')
    parser.add_argument('-l', '--loglevel', choices=logging._nameToLevel, default='WARNING', help='Uruchomienia programu w trybie logging LEVEL')

    args = parser.parse_args()
    print(args)
    x = args.loglevel
    print(x)
    poziom_logowania = x

    nazwa_pliku = 'zen.txt'
    wybrany_szablon = 'pelny'

    ustaw_logger(poziom_logowania)
    wynik = wc(nazwa_pliku, wybrany_szablon)

    print(wynik)

    czas_wykonania = datetime.datetime.now() - start
    logging.debug(f'czas wykonywania programu: {czas_wykonania}')
