import log
import time

format = '%(asctime)s, %(levelname)s, %(message)s'

datefmt = '%d-%m-%Y %H:%M:%S'
# więcej tu: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

log.basicConfig(level=log.DEBUG, format=format, datefmt=datefmt)

log.info('Treść informacji')
time.sleep(1)
log.info('Treść informacji')
time.sleep(1)
log.info('Treść informacji')
