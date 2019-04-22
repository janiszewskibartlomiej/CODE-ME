import datetime

start = datetime.datetime.now()

import logging

logging.basicConfig(level=logging.DEBUG)

czas_od_startu = datetime.datetime.now() - start

# stary sposób formatowania komunikatu
logging.info('czas wykonania skryptu: %s ', czas_od_startu)

# można też bardziej współcześnie
logging.info(f'czas wykonania skryptu: {czas_od_startu}')
