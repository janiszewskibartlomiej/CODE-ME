import logging

logger = logging.getLogger('moj_logger')

handler = logging.StreamHandler()
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.INFO)

logger.info('informacja')
logger.warning('ostrzeżenie')
logger.critical('JEST ŹLE')
