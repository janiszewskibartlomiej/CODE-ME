# Bartłomiej Janiszewski
from wc_funkcje import ustaw_logger, wc, policz_wyrazy
import logging
import datetime
import argparse

if __name__ == '__main__':
    start = datetime.datetime.now()
    
    parser = argparse.ArgumentParser(prog='Program like WC in linux', description='Prosty program do logów.')
    parser.add_argument('filename', help='Nazwa pliku który zostanie użyty do analizy')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--loglevel', choices=logging._nameToLevel, default='WARNING',
                       help='Uruchomienia programu w trybie logging LEVEL')
    group.add_argument('-ln', '--line', action='store_const', const='linie',
                       help='Uruchomienie programu w trybie liczenia linii')
    group.add_argument('-w', '--words', action='store_const', const='words', help='Uruchomienie programu w trybie liczenia wyrazów')
    group.add_argument('-c','--bytes', action='store_const', const='bytes', help='Urochomienie programu w tybie liczenia bajtów')
    
    args = parser.parse_args()
    print(args)
    logl = args.loglevel
    #print(logl)
    poziom_logowania = logl

    nazwa_pliku = args.filename

    #druga wersja
    wybrany_szablon = args.line or args.words or args.bytes or 'pelny'

    #pierwsza wersja:
    # if args.line:
    #     wybrany_szablon = args.line
    # elif args.words:
    #     wybrany_szablon = args.words
    # elif args.bytes:
    #     wybrany_szablon = args.bytes
    # else:
    #     wybrany_szablon = 'pelny'

    print(f'Uruchomiono program w trybie: {wybrany_szablon}')

    ustaw_logger(poziom_logowania)
    wynik = wc(nazwa_pliku, wybrany_szablon)

    print(wynik)

    czas_wykonania = datetime.datetime.now() - start
    logging.debug(f'czas wykonywania programu: {czas_wykonania}')
