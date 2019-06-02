import log

formatter = log.Formatter('%(asctime)s, %(levelname)s, %(message)s')
formatter2 = log.Formatter('[%(asctime)s][%(levelname)s] %(message)s')

# logowanie do pliku
logger = log.getLogger('uniwersalny_logger')
logger.setLevel(log.DEBUG)

file_handler = log.FileHandler('z_file_handlera2b.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(log.DEBUG)  # Uwaga, ustawiam poziom handlera, a nie loggera

logger.addHandler(file_handler)

scr_handler = log.StreamHandler()
scr_handler.setFormatter(formatter2)
scr_handler.setLevel(log.WARNING)

logger.addHandler(scr_handler)

logger.debug('informacja debugowa')
logger.info('informacja')
logger.warning('ostrzeżenie')
logger.error('błąd!')
logger.critical('JEST ŹLE!!!')
