# Bartłomiej Janiszewski
from wc_funkcje import ustaw_logger, wc
import logging
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()

    nazwa_pliku = 'zen.txt'
    wybrany_szablon = 'pelny'
    poziom_logowania = logging.DEBUG

    ustaw_logger(poziom_logowania)
    wynik = wc(nazwa_pliku, wybrany_szablon)

    print(wynik)

    czas_wykonania = datetime.datetime.now() - start
    logging.debug(f'czas wykonywania programu: {czas_wykonania}')
