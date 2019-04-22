import logging
import time

format = '%(asctime)s, %(levelname)s, %(message)s'

datefmt = '%d-%m-%Y %H:%M:%S'
# więcej tu: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

logging.basicConfig(level=logging.DEBUG, format=format, datefmt=datefmt)

logging.info('Treść informacji')
time.sleep(1)
logging.info('Treść informacji')
time.sleep(1)
logging.info('Treść informacji')
