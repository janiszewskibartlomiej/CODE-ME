import log

logger = log.getLogger('moj_logger')

handler = log.StreamHandler()
formatter = log.Formatter('%(asctime)s, %(levelname)s, %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(log.INFO)

logger.info('informacja')
logger.warning('ostrzeżenie')
logger.critical('JEST ŹLE')

logger.setLevel(log.ERROR)

input('Wciśnij enter...')  # Uwaga, komunikat może pojawić się w dziwnych miejscach

logger.info('informacja')
logger.warning('ostrzeżenie')
logger.critical('JEST ŹLE')
