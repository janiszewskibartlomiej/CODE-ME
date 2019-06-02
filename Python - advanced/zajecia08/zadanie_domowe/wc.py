# Bartłomiej Janiszewski
from wc_funkcje import ustaw_logger, wc
import log
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()

    nazwa_pliku = 'zen.txt'
    wybrany_szablon = 'pelny'
    poziom_logowania = log.DEBUG

    ustaw_logger(poziom_logowania)
    wynik = wc(nazwa_pliku, wybrany_szablon)

    print(wynik)

    czas_wykonania = datetime.datetime.now() - start
    log.debug(f'czas wykonywania programu: {czas_wykonania}')
