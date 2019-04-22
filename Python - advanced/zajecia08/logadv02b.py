import logging

formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(message)s')
formatter2 = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')

# logowanie do pliku
logger = logging.getLogger('uniwersalny_logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('z_file_handlera2b.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Uwaga, ustawiam poziom handlera, a nie loggera

logger.addHandler(file_handler)

scr_handler = logging.StreamHandler()
scr_handler.setFormatter(formatter2)
scr_handler.setLevel(logging.WARNING)

logger.addHandler(scr_handler)

logger.debug('informacja debugowa')
logger.info('informacja')
logger.warning('ostrzeżenie')
logger.error('błąd!')
logger.critical('JEST ŹLE!!!')
