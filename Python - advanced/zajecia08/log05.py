import logging

format = '%(asctime)s, %(levelname)s, %(message)s'
# więcej: https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(level=logging.DEBUG, format=format)

logging.info('Treść informacji')

logging.debug('Druga informacja')
