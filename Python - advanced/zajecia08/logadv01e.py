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
