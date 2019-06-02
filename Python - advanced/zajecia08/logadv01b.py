import log

logger = log.getLogger('moj_logger')

handler = log.StreamHandler()
logger.addHandler(handler)

logger.setLevel(log.INFO)

logger.info('informacja')
logger.warning('ostrzeżenie')
logger.critical('JEST ŹLE')
