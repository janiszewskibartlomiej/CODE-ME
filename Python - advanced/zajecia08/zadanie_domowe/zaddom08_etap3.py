# Bartłomiej Janiszewski
from wc_funkcje import ustaw_logger, wc, policz_wyrazy
import logging
import datetime
import argparse

if __name__ == '__main__':
    start = datetime.datetime.now()
    nazwa_pliku = 'zen.txt'

    parser = argparse.ArgumentParser(description='Prosty program do logów.')
    parser.add_argument('-l', '--loglevel', choices=logging._nameToLevel, default='WARNING',
                        help='Uruchomienia programu w trybie logging LEVEL')
    parser.add_argument('-ln', '--lenline', choices=['pelny', 'linie'], default='linie',
                        help='Uruchomienia programu w celu obliczenia liczby linii')
    parser.add_argument('-w', '--words', nargs='?', action=policz_wyrazy(nazwa_pliku), help='Uruchomienia programu w celu obliczenia liczby wyrazów')

    args = parser.parse_args()
    print(args)
    x = args.loglevel
    print(x)
    poziom_logowania = x

    # tutaj należy napisać kod odpowiedzialny za wczytanie argumentów

    ln = args.lenline
    wybrany_szablon = ln
    print(wybrany_szablon)

    ustaw_logger(poziom_logowania)
    wynik = wc(nazwa_pliku, wybrany_szablon)

    print(wynik)

    czas_wykonania = datetime.datetime.now() - start
    logging.debug(f'czas wykonywania programu: {czas_wykonania}')
