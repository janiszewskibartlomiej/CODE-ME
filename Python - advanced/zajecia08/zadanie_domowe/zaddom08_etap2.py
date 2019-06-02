# Bartłomiej Janiszewski
from wc_funkcje import ustaw_logger, wc
import log
import datetime
import argparse

if __name__ == '__main__':
    start = datetime.datetime.now()

    parser = argparse.ArgumentParser(description='Prosty program do logów.')
    parser.add_argument('-l', '--loglevel', choices=log._nameToLevel, default='WARNING',
                        help='Uruchomienia programu w trybie logging LEVEL')
    parser.add_argument('filename', help='Nazwa pliku, który będzie sprawdzany.')

    args = parser.parse_args()
    print(args)
    x = args.loglevel
    print(x)
    poziom_logowania = x

    nazwa_pliku = args.filename
    print(nazwa_pliku)
    wybrany_szablon = 'pelny'

    ustaw_logger(poziom_logowania)
    wynik = wc(nazwa_pliku, wybrany_szablon)

    print(wynik)

    czas_wykonania = datetime.datetime.now() - start
    log.debug(f'czas wykonywania programu: {czas_wykonania}')
