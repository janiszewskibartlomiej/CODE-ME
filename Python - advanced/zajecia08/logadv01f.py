import logging

logger = logging.getLogger('moj_logger')

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.INFO)

logger.info('informacja')
logger.warning('ostrzeżenie')
logger.critical('JEST ŹLE')

logger.setLevel(logging.ERROR)

input('Wciśnij enter...')  # Uwaga, komunikat może pojawić się w dziwnych miejscach

logger.info('informacja')
logger.warning('ostrzeżenie')
logger.critical('JEST ŹLE')
