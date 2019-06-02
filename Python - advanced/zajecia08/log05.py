import log

format = '%(asctime)s, %(levelname)s, %(message)s'
# więcej: https://docs.python.org/3/library/logging.html#logrecord-attributes

log.basicConfig(level=log.DEBUG, format=format)

log.info('Treść informacji')

log.debug('Druga informacja')
