import logging

formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(message)s')

# logowanie do pliku
logger_plik = logging.getLogger('log_do_pliku')

file_handler = logging.FileHandler('z_file_handlera2.log')
file_handler.setFormatter(formatter)

logger_plik.addHandler(file_handler)
logger_plik.setLevel(logging.INFO)

# logowanie na ekran
logger_ekran = logging.getLogger('log_na_ekran')

scr_handler = logging.StreamHandler()
scr_handler.setFormatter(formatter)

logger_ekran.addHandler(scr_handler)
# nie ustawiam poziomu, aby był domyślny


logger_plik.info('informacja do pliku')
logger_plik.warning('ostrzeżenie do pliku')
logger_plik.critical('JEST ŹLE (do pliku)')

logger_ekran.info('informacja na ekran')
logger_ekran.warning('ostrzeżenie na ekran')
logger_ekran.critical('JEST ŹLE (na ekran)')
